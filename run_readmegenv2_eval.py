"""Evaluate readmegenv2 against bundled sample scripts.

The script runs the LLM-only pipeline on the sample scripts and compares the
outputs against the human-written READMEs. The ground-truth READMEs are read
**only after** generation for scoring purposes; they are never fed back into
the model.

A summary JSON and Markdown report are written under
`artifacts/readmegenv2_eval/` so new runs are easy to diff.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import statistics
from pathlib import Path
from typing import Dict, List

import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from readmegenv2.analysis import analyze_script
from readmegenv2.llm import call_llm, choose_judge_provider, choose_provider, load_api_keys
from readmegenv2.pipeline import generate_readme_for_file

DATASET = ROOT / "Sample_scripts"
EVAL_ROOT = ROOT / "artifacts" / "readmegenv2_eval"
DEFAULT_JUDGE_MODEL = "gpt-4o-mini"


def _run_paths(run_label: str) -> tuple[Path, Path]:
    report_dir = EVAL_ROOT / run_label
    generated_dir = report_dir / "generated"
    return report_dir, generated_dir


def _score_snapshot(item: Dict) -> Dict[str, float]:
    description = item.get("description", {})
    cli = item.get("cli", {})
    return {
        "clarity": float(description.get("clarity", 0)),
        "completeness": float(description.get("completeness", 0)),
        "helpfulness": float(description.get("helpfulness", 0)),
        "cli_completeness": float(cli.get("completeness", 0)),
    }


def _aggregate_signal_insights(results: List[Dict]) -> Dict[str, Dict[str, float | int]]:
    buckets: Dict[str, List[Dict[str, float]]] = {
        "docstrings_present": [],
        "structured_cli": [],
        "sys_argv_only": [],
        "requirements_detected": [],
    }

    for item in results:
        if "error" in item:
            continue
        profile = item.get("signal_profile", {})
        scores = _score_snapshot(item)

        doc_info = profile.get("docstrings", {})
        if doc_info.get("module_docstring") or doc_info.get("function_docstrings"):
            buckets["docstrings_present"].append(scores)

        cli_info = profile.get("cli", {})
        if cli_info.get("arguments"):
            buckets["structured_cli"].append(scores)
        elif cli_info.get("uses_sys_argv"):
            buckets["sys_argv_only"].append(scores)

        requirements = profile.get("requirements", {})
        if requirements.get("files") or requirements.get("packages"):
            buckets["requirements_detected"].append(scores)

    def _avg(values: List[Dict[str, float]], field: str) -> float:
        return round(sum(v[field] for v in values) / len(values), 3) if values else 0.0

    aggregates: Dict[str, Dict[str, float]] = {}
    for name, values in buckets.items():
        aggregates[name] = {
            "clarity": _avg(values, "clarity"),
            "completeness": _avg(values, "completeness"),
            "helpfulness": _avg(values, "helpfulness"),
            "cli_completeness": _avg(values, "cli_completeness"),
            "sample_size": len(values),
        }
    return aggregates


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _lower_name(value: str) -> str:
    return re.sub(r'["`~\']', "", value.strip()).lower()


def _extract_candidate_sections(text: str, keywords: List[str]) -> List[List[str]]:
    """Return lists of lines under headings matching any keyword."""
    sections: List[List[str]] = []
    current: List[str] | None = None
    for line in text.splitlines():
        heading = re.match(r"^#+\s*(.+)$", line)
        if heading:
            title = _lower_name(heading.group(1))
            if any(key in title for key in keywords):
                current = []
                sections.append(current)
            else:
                current = None
            continue
        if current is not None:
            current.append(line)
    return sections


def _extract_dependencies_from_readme(text: str) -> List[str]:
    """Heuristically collect dependency names from the ground-truth README."""

    keywords = ["requirement", "dependency", "install", "installation", "prerequisite"]
    sections = _extract_candidate_sections(text, keywords)

    allowed_pattern = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
    stopwords = {
        "note",
        "for",
        "if",
        "extra",
        "compatible",
        "operating",
        "system",
        "version",
        "windows",
        "linux",
        "macos",
        "anaconda",
        "conda",
        "miniconda",
        "python",
        "pip",
        "pip3",
        "pipx",
        "step",
        "download",
        "install",
        "clone",
        "repository",
        "git",
        "zip",
        "you",
        "any",
        "and",
        "or",
        "the",
        "requirements.txt",
        "readme",
    }

    packages: set[str] = set()

    def _clean_token(token: str) -> str | None:
        token = token.strip().strip("`",).strip().strip(",.;:()[]{}")
        token = re.sub(r"^[-]{1,2}[A-Za-z0-9_.-]*=", "", token)
        token = re.split(r"[<>=!~]", token, maxsplit=1)[0]
        token = token.strip()
        lowered = token.lower()

        if not token or lowered in stopwords:
            return None
        if lowered.replace(".", "").isdigit():
            return None
        if "/" in token or token.endswith(('.txt', '.md')):
            return None
        if not allowed_pattern.match(token):
            return None
        return token

    def _maybe_add(token: str) -> None:
        cleaned = _clean_token(token)
        if cleaned:
            packages.add(cleaned)

    for block in sections:
        for line in block:
            pip_match = re.search(r"pip(?:3|x)?\s+install\s+(.+)", line, re.IGNORECASE)
            if pip_match:
                for raw in re.split(r"\s+", pip_match.group(1)):
                    if raw.startswith("-"):
                        continue
                    _maybe_add(raw)
                continue

            inline_code = re.findall(r"`([^`]+)`", line)
            for snippet in inline_code:
                for token in re.split(r"[\s,]+", snippet):
                    _maybe_add(token)

            if re.match(r"^\s*[-*]", line):
                for token in re.findall(r"\b([A-Za-z0-9_.-]+)\b", line):
                    _maybe_add(token)
            elif re.match(r"^\s*\d+\.\s", line):
                for token in re.findall(r"`([^`]+)`", line):
                    _maybe_add(token)
    return sorted(packages)


def _dependency_metrics(predicted: Dict[str, List[str]], actual: List[str]):
    predicted_third = set(predicted.get("third_party", []))
    actual_third = set(actual)

    true_positive = len(predicted_third & actual_third)
    precision = true_positive / len(predicted_third) if predicted_third else 1.0
    recall = true_positive / len(actual_third) if actual_third else 1.0
    return precision, recall


def _extract_cli_flags(text: str) -> List[str]:
    """Extract CLI-like flags (e.g., --foo, -f) from relevant README sections."""
    keywords = ["usage", "argument", "option", "flag", "cli", "command"]
    sections = _extract_candidate_sections(text, keywords)
    flags: set[str] = set()

    pattern = re.compile(r"(?<![A-Za-z0-9/:])(--[A-Za-z][A-Za-z0-9_-]*|-{1}[A-Za-z][A-Za-z0-9_-]*)")

    for block in sections:
        for line in block:
            for match in pattern.findall(line):
                flags.add(match)
    return sorted(flags)


def _cli_completeness(predicted: Dict[str, List[dict]], actual_flags: List[str]):
    """Compute CLI completeness, counting aliases as well as primary flags."""
    predicted_items = predicted.get("arguments", []) if isinstance(predicted, dict) else []
    predicted_set: set[str] = set()

    for item in predicted_items:
        if not isinstance(item, dict):
            continue

        flag = item.get("flag") or item.get("name")
        alias = item.get("alias")
        aliases = item.get("aliases") if isinstance(item.get("aliases"), list) else []

        expanded: List[str] = []
        if flag:
            expanded.append(flag)
        if alias:
            expanded.append(alias)
        expanded.extend(aliases)

        for candidate in expanded:
            if candidate:
                predicted_set.add(candidate)

    actual_set = set(actual_flags)
    found = len(predicted_set & actual_set)
    predicted_count = len(predicted_set)
    actual_count = len(actual_set)
    completeness = found / actual_count if actual_count else 1.0
    return predicted_count, actual_count, completeness, found


def _build_signal_profile(
    actual_facts: Dict,
    predicted_cli: Dict,
    *,
    generation_provider: str | None,
    generation_model: str | None,
):
    module_docstring = bool(actual_facts.get("module_docstring"))
    function_docstrings = [f for f in actual_facts.get("functions", []) if f.get("doc")]
    class_docstrings = [c for c in actual_facts.get("classes", []) if c.get("doc")]

    cli_args = predicted_cli.get("arguments", []) if isinstance(predicted_cli, dict) else []
    uses_sys_argv = bool(actual_facts.get("has_positional_args"))
    requirements_meta = actual_facts.get("project", {})

    strengths = []
    risks = []

    if module_docstring or function_docstrings or class_docstrings:
        strengths.append("Docstrings supply narrative context for the LLM.")
    else:
        risks.append("No docstrings detected; the model must infer behavior from code structure.")

    if cli_args:
        strengths.append("Argparse metadata provides structured flag semantics.")
    elif uses_sys_argv:
        risks.append(
            "CLI handling relies on sys.argv without argparse, so flags may be under-documented (e.g., Local File Organizer)."
        )

    if requirements_meta.get("requirements_files"):
        strengths.append("Requirements files can be surfaced directly in installation guidance.")

    if actual_facts.get("external_tools"):
        strengths.append("External tool usage is explicitly detected for README mentions.")

    env_vars = actual_facts.get("env_vars", [])
    if not env_vars:
        risks.append("No environment variables detected; skip the section to avoid hallucination.")

    return {
        "docstrings": {
            "module_docstring": module_docstring,
            "function_docstrings": len(function_docstrings),
            "class_docstrings": len(class_docstrings),
        },
        "cli": {
            "framework": predicted_cli.get("framework") if isinstance(predicted_cli, dict) else "",
            "arguments": len(cli_args),
            "uses_sys_argv": uses_sys_argv,
        },
        "requirements": {
            "files": requirements_meta.get("requirements_files", []),
            "packages": requirements_meta.get("requirement_packages", []),
        },
        "external_tools": actual_facts.get("external_tools", []),
        "env_var_count": len(env_vars),
        "generation": {"provider": generation_provider, "model": generation_model},
        "notes": {"strengths": strengths, "risks": risks},
    }


def _similarity_score(text_a: str, text_b: str) -> float:
    return difflib.SequenceMatcher(None, text_a, text_b).ratio()


def _clarity_score(text: str) -> int:
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    if not sentences:
        return 3
    words_per_sentence = [len(s.split()) for s in sentences]
    avg = statistics.mean(words_per_sentence)
    if avg <= 18:
        return 5
    if avg <= 25:
        return 4
    if avg <= 35:
        return 3
    if avg <= 45:
        return 2
    return 1


def _helpfulness_score(text: str) -> int:
    lowered = text.lower()
    keywords = ["usage", "example", "install", "require", "argument", "option"]
    hits = sum(1 for kw in keywords if kw in lowered)
    return max(1, min(5, round((hits / len(keywords)) * 5)))


def _heuristic_description_scores(generated: str, ground_truth: str):
    """Defined for potential future experiments; not used in the main eval path."""
    similarity = _similarity_score(generated, ground_truth)
    clarity = _clarity_score(generated)
    completeness = max(1, min(5, round(similarity * 4 + 1)))
    helpfulness = _helpfulness_score(generated)
    return {
        "clarity": clarity,
        "completeness": completeness,
        "helpfulness": helpfulness,
        "similarity": similarity,
        "judge": "heuristic",
    }


def _llm_description_scores(
    generated: str,
    ground_truth: str,
    *,
    provider: str | None,
    model: str | None,
    api_keys: Dict[str, str] | None,
):
    """Ask an LLM to grade the generated README against the reference.

    This expects the LLM to return a JSON object, but is robust to
    code fences and short textual prefixes/suffixes by extracting the
    first JSON object found in the response. If we still cannot parse
    a JSON object, we raise an error and the script is marked as an
    evaluation error (no heuristic fallback).
    """

    provider_to_use = choose_judge_provider(provider, api_keys=api_keys)
    messages = [
        {
            "role": "system",
            "content": (
                "You are a meticulous README evaluator. Compare the candidate README against the reference README and "
                "respond with a single JSON object ONLY, with integer scores 1-5 for clarity, completeness, and "
                "helpfulness, plus a one-sentence rationale. Do not include any explanation, commentary, or markdown "
                "outside the JSON object."
            ),
        },
        {
            "role": "user",
            "content": (
                "Reference README:\n\n"
                + ground_truth
                + "\n\n"
                + "Candidate README:\n\n"
                + generated
                + "\n\n"
                + 'Respond with JSON like {"clarity":5,"completeness":4,"helpfulness":4,"rationale":"..."} and nothing else.'
            ),
        },
    ]

    content = call_llm(provider_to_use, model or DEFAULT_JUDGE_MODEL, messages, api_keys=api_keys)
    raw = content.strip()

    # If the model wrapped the JSON in markdown fences, strip them loosely.
    if raw.startswith("```"):
        # Common patterns: ```json\n{...}\n``` or ```\n{...}\n```
        # Remove leading/trailing fences and let JSON-extraction logic handle the rest.
        # This is intentionally simple: we mainly want to get to the { ... }.
        parts = raw.split("```")
        # e.g., ['', 'json\n{...}\n', '']
        raw = "".join(p for p in parts if "{" in p or "}" in p).strip()

    # Try direct parse first.
    try:
        parsed = json.loads(raw)
    except Exception:
        # Try to extract the first plausible JSON object between { and }.
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1 and end > start:
            candidate = raw[start : end + 1]
            try:
                parsed = json.loads(candidate)
            except Exception as exc:
                raise ValueError(
                    f"LLM judge failed to parse response: {exc}; raw={raw[:200]!r}"
                ) from exc
        else:
            raise ValueError(f"LLM judge returned no JSON object; raw={raw[:200]!r}")

    return {
        "clarity": int(parsed.get("clarity", 0)),
        "completeness": int(parsed.get("completeness", 0)),
        "helpfulness": int(parsed.get("helpfulness", 0)),
        "similarity": _similarity_score(generated, ground_truth),
        "rationale": parsed.get("rationale", ""),
        "judge": provider_to_use,
    }


def evaluate_script(
    script_path: Path,
    gt_readme: Path,
    *,
    provider: str | None,
    generation_model: str | None,
    judge_provider: str | None,
    judge_model: str | None,
    api_keys: Dict[str, str] | None,
    generated_dir: Path,
):
    generated_dir.mkdir(parents=True, exist_ok=True)
    output_name = f"{script_path.stem}_AI_README.md"
    output_path = generated_dir / output_name
    try:
        out_path, mode, predicted_facts = generate_readme_for_file(
            str(script_path),
            out_path=str(output_path),
            provider=provider,
            model=generation_model,
            api_keys=api_keys,
            probe_help=False,
        )

        gt_text = _read_text(gt_readme)
        readme_dependencies = _extract_dependencies_from_readme(gt_text)
        actual_facts = analyze_script(str(script_path), probe_help=True)
        combined_deps = sorted(
            {
                *readme_dependencies,
                *actual_facts.get("imports", {}).get("third_party", []),
            }
        )
        precision, recall = _dependency_metrics(predicted_facts.get("imports", {}), combined_deps)

        predicted_cli = predicted_facts.get("cli", {})
        actual_cli_flags = _extract_cli_flags(gt_text)
        predicted_flags, actual_flags, completeness, hits = _cli_completeness(
            predicted_cli, actual_cli_flags
        )

        generated_text = _read_text(Path(out_path))
        try:
            description_scores = _llm_description_scores(
                generated_text,
                gt_text,
                provider=judge_provider,
                model=judge_model,
                api_keys=api_keys,
            )
        except Exception as exc:
            # Enforce LLM-only scoring: if judge fails, this script is an error.
            raise RuntimeError(f"Description scoring failed: {exc}") from exc

        signal_profile = _build_signal_profile(
            actual_facts,
            predicted_cli,
            generation_provider=provider,
            generation_model=generation_model,
        )

        return {
            "script": script_path.name,
            "mode": mode,
            "readme_path": os.path.relpath(out_path, ROOT),
            "ground_truth": os.path.relpath(gt_readme, ROOT),
            "dependencies": {"precision": precision, "recall": recall, "actual": combined_deps},
            "cli": {
                "detected": predicted_flags,
                "actual": actual_flags,
                "hits": hits,
                "completeness": completeness,
            },
            "description": description_scores,
            "generation": {"provider": provider, "model": generation_model},
            "judge": {"provider": judge_provider, "model": judge_model},
            "signal_profile": signal_profile,
        }
    except Exception as exc:  # pragma: no cover - defensive for heterogeneous samples
        return {
            "script": script_path.name,
            "ground_truth": os.path.relpath(gt_readme, ROOT),
            "error": str(exc),
            "mode": "error",
            "generation": {"provider": provider, "model": generation_model},
            "judge": {"provider": judge_provider, "model": judge_model},
        }


def _summarize(results: List[Dict]):
    valid = [item for item in results if "error" not in item]

    deps_precision = [item["dependencies"]["precision"] for item in valid]
    deps_recall = [item["dependencies"]["recall"] for item in valid]
    cli_completeness = [item["cli"]["completeness"] for item in valid]
    clarity = [item["description"]["clarity"] for item in valid]
    completeness_scores = [item["description"]["completeness"] for item in valid]
    helpfulness = [item["description"]["helpfulness"] for item in valid]

    def avg(values: List[float]):
        return round(sum(values) / len(values), 3) if values else 0.0

    return {
        "dependencies": {"precision": avg(deps_precision), "recall": avg(deps_recall)},
        "cli": {"completeness": avg(cli_completeness)},
        "description": {
            "clarity": avg(clarity),
            "completeness": avg(completeness_scores),
            "helpfulness": avg(helpfulness),
        },
        "sample_size": len(valid),
        "skipped": len(results) - len(valid),
    }


def _write_reports(results: List[Dict], run_label: str, *, report_dir: Path, run_config: Dict[str, str]):
    report_dir.mkdir(parents=True, exist_ok=True)

    summary = _summarize(results)
    signal_insights = _aggregate_signal_insights(results)
    payload = {"summary": summary, "signal_insights": signal_insights, "run_config": run_config, "results": results}
    metrics_path = report_dir / f"metrics_{run_label}.json"
    metrics_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = [
        "# readmegenv2 evaluation",
        "",
        f"Samples evaluated: {summary['sample_size']}",
        f"Skipped due to errors: {summary['skipped']}",
        "",
    ]
    lines.append("## Aggregate metrics")
    lines.append(
        f"- Dependencies precision: {summary['dependencies']['precision']:.3f}\n"
        f"- Dependencies recall: {summary['dependencies']['recall']:.3f}\n"
        f"- CLI completeness: {summary['cli']['completeness']:.3f}\n"
        f"- Description clarity: {summary['description']['clarity']:.3f}\n"
        f"- Description completeness: {summary['description']['completeness']:.3f}\n"
        f"- Description helpfulness: {summary['description']['helpfulness']:.3f}\n"
    )

    lines.append("## Run configuration")
    lines.append(
        f"- Generation: {run_config.get('generation_provider', 'auto')} ({run_config.get('generation_model', 'default')})\n"
        f"- Judge: {run_config.get('judge_provider', 'openai')} ({run_config.get('judge_model', DEFAULT_JUDGE_MODEL)})\n"
        f"- Run label: {run_label}\n"
    )

    lines.append("## Signal insights")
    if any(v.get("sample_size", 0) for v in signal_insights.values()):
        for name, values in signal_insights.items():
            lines.append(
                f"- {name.replace('_', ' ').title()}: clarity={values['clarity']:.3f}, completeness={values['completeness']:.3f}, "
                f"helpfulness={values['helpfulness']:.3f}, cli={values['cli_completeness']:.3f} (n={values['sample_size']})"
            )
    else:
        lines.append("- No successful samples to analyze.")

    lines.append("\n## Per-file metrics")
    lines.append(
        "| Script | Dep. P | Dep. R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Judge | Notes |"
    )
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for item in results:
        if "error" in item:
            lines.append(
                f"| {item['script']} | — | — | — | — | — | — | error | — | {item['error']} |"
            )
            continue
        dep_p = item["dependencies"]["precision"]
        dep_r = item["dependencies"]["recall"]
        cli_c = item["cli"]["completeness"]
        desc = item["description"]
        judge = desc.get("judge", "")
        rationale = desc.get("rationale", "")
        cli_note = f"flags: {item['cli']['hits']}/{item['cli']['actual']}" if item["cli"]["actual"] else ""
        notes = ", ".join(filter(None, [cli_note, rationale]))
        lines.append(
            "| {script} | {dep_p:.2f} | {dep_r:.2f} | {cli_c:.2f} | {clarity} | {complete} | {helpful} | {mode} | {judge} | {notes} |".format(
                script=item["script"],
                dep_p=dep_p,
                dep_r=dep_r,
                cli_c=cli_c,
                clarity=desc["clarity"],
                complete=desc["completeness"],
                helpful=desc["helpfulness"],
                mode=item["mode"],
                judge=judge,
                notes=notes,
            )
        )

    summary_path = report_dir / f"summary_{run_label}.md"
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _parse_args():
    parser = argparse.ArgumentParser(description="Evaluate readmegenv2 against bundled samples.")
    parser.add_argument(
        "--gen-provider",
        default=None,
        help="Provider used for README generation (e.g., openai, google, groq).",
    )
    parser.add_argument(
        "--gen-model",
        default=None,
        help="Model name used for README generation (provider-specific).",
    )
    parser.add_argument(
        "--provider",
        default=None,
        help="Deprecated alias for --gen-provider.",
    )
    parser.add_argument(
        "--judge-provider",
        default=None,
        help="Provider used for judging (openai, google, groq).",
    )
    parser.add_argument(
        "--judge-model",
        default=None,
        help="Override model for the LLM judge (default gpt-4o-mini).",
    )
    parser.add_argument(
        "--run-label",
        default=None,
        help="Optional label for this run; used in the metrics/summary filenames.",
    )
    parser.add_argument(
        "--api-key",
        action="append",
        help="Provider-scoped API key in the form provider:key (can be passed multiple times).",
    )
    return parser.parse_args()


def _collect_api_keys(values: List[str] | None) -> Dict[str, str]:
    keys: Dict[str, str] = dict(load_api_keys(os.environ))
    for raw in values or []:
        if ":" not in raw:
            continue
        provider, key = raw.split(":", 1)
        provider = provider.strip().lower()
        key = key.strip()
        if provider and key:
            keys[provider] = key
    return keys


def main():
    args = _parse_args()
    if args.gen_provider is None and args.provider:
        args.gen_provider = args.provider

    api_keys = _collect_api_keys(args.api_key)
    gen_provider = choose_provider(args.gen_provider, api_keys=api_keys)
    judge_provider = choose_judge_provider(args.judge_provider, api_keys=api_keys)
    judge_model = args.judge_model or DEFAULT_JUDGE_MODEL

    pairs: List[tuple[Path, Path]] = []
    for path in sorted(DATASET.glob("*.py")):
        md_path = path.with_suffix(".md")
        if md_path.exists():
            pairs.append((path, md_path))
    if not pairs:
        raise SystemExit("No sample script/README pairs found")

    run_label = args.run_label
    if not run_label:
        gen_base = gen_provider or "openai"
        gen_model_part = args.gen_model or "default"
        judge_base = judge_provider or "openai"
        judge_model_part = judge_model or DEFAULT_JUDGE_MODEL
        run_label = f"{gen_base}-{gen_model_part}__judge-{judge_base}-{judge_model_part}"
        if sys.stdin.isatty():
            user_label = input(f"Run label for this evaluation (default {run_label}): ").strip()
            if user_label:
                run_label = user_label
    safe_label = re.sub(r"[^A-Za-z0-9_.-]+", "_", run_label)
    report_dir, generated_dir = _run_paths(safe_label)

    run_config = {
        "generation_provider": gen_provider,
        "generation_model": args.gen_model or "default",
        "judge_provider": judge_provider,
        "judge_model": judge_model,
        "label": safe_label,
    }

    results = [
        evaluate_script(
            script,
            md,
            provider=gen_provider,
            generation_model=args.gen_model,
            judge_provider=judge_provider,
            judge_model=judge_model,
            api_keys=api_keys,
            generated_dir=generated_dir,
        )
        for script, md in pairs
    ]

    if results and all("error" in r for r in results):
        errors = {r.get("error", "") for r in results}
        if len(errors) == 1:
            only_error = errors.pop()
            print(
                f"All {len(results)} evaluations failed with the same LLM error:\n"
                f"  {only_error}\n"
                "This usually means the generation model name is invalid or unsupported for your key.\n"
                "Try listing available models for your provider and rerun with --gen-model <valid-name>."
            )

    _write_reports(results, safe_label, report_dir=report_dir, run_config=run_config)
    print(
        f"Evaluated {len(results)} scripts with provider={gen_provider or 'auto'} "
        f"and run_label={safe_label}. Reports saved to {report_dir} "
        f"as metrics_{safe_label}.json and summary_{safe_label}.md."
    )


if __name__ == "__main__":
    main()
