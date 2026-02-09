"""Evaluate the LLM-only readmegenv2_no_ast pipeline against bundled sample scripts."""

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

from readmegenv2.llm import call_llm, choose_judge_provider, choose_provider
from readmegenv2_no_ast.pipeline import generate_readme_for_file

DATASET = ROOT / "Sample_scripts"
EVAL_ROOT = ROOT / "artifacts" / "readmegenv2_eval_no_ast"
DEFAULT_JUDGE_MODEL = "gpt-4o-mini"


def _run_paths(run_label: str) -> tuple[Path, Path]:
    report_dir = EVAL_ROOT / run_label
    generated_dir = report_dir / "generated"
    return report_dir, generated_dir


def _score_snapshot(item: Dict) -> Dict[str, float]:
    description = item.get("description", {})
    cli = item.get("cli", {})
    deps = item.get("dependencies", {})
    return {
        "clarity": float(description.get("clarity", 0)),
        "completeness": float(description.get("completeness", 0)),
        "helpfulness": float(description.get("helpfulness", 0)),
        "cli_completeness": float(cli.get("completeness", 0)),
        "dep_precision": float(deps.get("precision", 0)),
        "dep_recall": float(deps.get("recall", 0)),
    }


def _avg(values: List[Dict[str, float]], field: str) -> float:
    return round(sum(v[field] for v in values) / len(values), 3) if values else 0.0


def _aggregate_signal_insights(results: List[Dict]) -> Dict[str, Dict[str, float | int]]:
    buckets: Dict[str, List[Dict[str, float]]] = {
        "has_cli_flags": [],
        "no_cli_flags": [],
        "has_imports": [],
        "no_imports": [],
        "no_ast": [],
    }

    for item in results:
        if "error" in item:
            continue
        profile = item.get("signal_profile", {})
        deps = item.get("dependencies", {})
        predicted_imports = deps.get("predicted", []) if isinstance(deps, dict) else []
        actual_imports = deps.get("actual", []) if isinstance(deps, dict) else []
        scores = _score_snapshot(item)

        cli_info = profile.get("cli", {})
        cli_args = cli_info.get("arguments") if isinstance(cli_info, dict) else 0
        if cli_args:
            buckets["has_cli_flags"].append(scores)
        else:
            buckets["no_cli_flags"].append(scores)

        has_imports = bool(predicted_imports or actual_imports)
        if has_imports:
            buckets["has_imports"].append(scores)
        else:
            buckets["no_imports"].append(scores)

        if profile.get("no_ast") is True:
            buckets["no_ast"].append(scores)

    aggregates: Dict[str, Dict[str, float | int]] = {}
    for name, values in buckets.items():
        aggregates[name] = {
            "clarity": _avg(values, "clarity"),
            "completeness": _avg(values, "completeness"),
            "helpfulness": _avg(values, "helpfulness"),
            "cli_completeness": _avg(values, "cli_completeness"),
            "dep_precision": _avg(values, "dep_precision"),
            "dep_recall": _avg(values, "dep_recall"),
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
                for token in pip_match.group(1).split():
                    _maybe_add(token)
                continue

            for token in re.split(r"\s+", line):
                _maybe_add(token)

    return sorted(packages)


def _extract_cli_flags(text: str) -> List[str]:
    keywords = ["usage", "argument", "option", "flag", "cli"]
    sections = _extract_candidate_sections(text, keywords)
    flags: set[str] = set()
    for block in sections:
        for line in block:
            for flag in re.findall(r"(--?[A-Za-z0-9][A-Za-z0-9_-]*)", line):
                flags.add(flag)
    return sorted(flags)


def _dependency_metrics(predicted_imports: Dict, ground_truth_packages: List[str]) -> tuple[float, float]:
    predicted = set(predicted_imports.get("third_party", [])) if isinstance(predicted_imports, dict) else set()
    actual = set(ground_truth_packages)
    if not predicted and not actual:
        return 1.0, 1.0
    true_positive = len(predicted & actual)
    precision = true_positive / len(predicted) if predicted else 0.0
    recall = true_positive / len(actual) if actual else 0.0
    return precision, recall


def _similarity_score(a: str, b: str) -> float:
    return round(difflib.SequenceMatcher(None, a, b).ratio(), 3)


def _llm_description_scores(
    generated: str,
    ground_truth: str,
    *,
    provider: str | None,
    model: str | None,
    api_keys: Dict[str, str] | None,
) -> Dict:
    provider_to_use = choose_judge_provider(provider, api_keys=api_keys)
    model_to_use = model or DEFAULT_JUDGE_MODEL

    prompt = """
You are judging the quality of a generated README against a human reference. Use the FULL 1–5
scale for clarity, completeness, and helpfulness.

5 = exceptional, professional-quality, essentially no important issues
4 = strong but with some minor or moderate issues
3 = average / acceptable, several issues or omissions
2 = weak, many issues or missing important content
1 = very poor or unusable

Compare the generated README to the reference: punish missing sections, missing dependencies, weak
usage docs, or unclear explanations.
Respond ONLY with JSON: {"clarity": int, "completeness": int, "helpfulness": int, "rationale": str}.
""".strip()

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Generated README:\n{generated}\n\nReference README:\n{ground_truth}"},
    ]

    raw = call_llm(provider_to_use, model_to_use, messages, api_keys=api_keys)
    try:
        parsed = json.loads(raw)
    except Exception:
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
        "clarity": max(1, min(5, int(parsed.get("clarity", 0)))),
        "completeness": max(1, min(5, int(parsed.get("completeness", 0)))),
        "helpfulness": max(1, min(5, int(parsed.get("helpfulness", 0)))),
        "similarity": _similarity_score(generated, ground_truth),
        "rationale": parsed.get("rationale", ""),
        "judge": provider_to_use,
    }


def _cli_completeness(predicted_cli: Dict, actual_flags: List[str]):
    predicted_set = set()
    if isinstance(predicted_cli, dict):
        for entry in predicted_cli.get("arguments", []):
            flag = entry.get("flag") if isinstance(entry, dict) else None
            alias = entry.get("alias") if isinstance(entry, dict) else None
            aliases = entry.get("aliases", []) if isinstance(entry, dict) else []
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
    predicted_cli: Dict,
    *,
    generation_provider: str | None,
    generation_model: str | None,
) -> Dict:
    cli_args = predicted_cli.get("arguments", []) if isinstance(predicted_cli, dict) else []

    strengths: List[str] = []
    risks: List[str] = [
        "No static analysis facts available; README is based solely on code text and LLM inference.",
    ]

    if cli_args:
        strengths.append("CLI flags inferred from runtime help output.")

    return {
        "docstrings": {
            "module_docstring": False,
            "function_docstrings": 0,
            "class_docstrings": 0,
        },
        "cli": {
            "framework": predicted_cli.get("framework") if isinstance(predicted_cli, dict) else "",
            "arguments": len(cli_args),
            "uses_sys_argv": False,
        },
        "requirements": {"files": [], "packages": []},
        "external_tools": [],
        "env_var_count": 0,
        "generation": {"provider": generation_provider, "model": generation_model},
        "notes": {"strengths": strengths, "risks": risks},
        "no_ast": True,
    }


def _summarize(results: List[Dict]):
    valid = [item for item in results if "error" not in item]

    deps_precision = [item["dependencies"]["precision"] for item in valid]
    deps_recall = [item["dependencies"]["recall"] for item in valid]
    cli_completeness = [item["cli"]["completeness"] for item in valid]
    desc_clarity = [item["description"]["clarity"] for item in valid]
    desc_completeness = [item["description"]["completeness"] for item in valid]
    desc_helpfulness = [item["description"]["helpfulness"] for item in valid]

    def _safe_stats(values: List[float]):
        if not values:
            return {"avg": 0.0, "min": 0.0, "max": 0.0, "median": 0.0}
        return {
            "avg": round(statistics.mean(values), 3),
            "min": round(min(values), 3),
            "max": round(max(values), 3),
            "median": round(statistics.median(values), 3),
        }

    deps_precision_stats = _safe_stats(deps_precision)
    deps_recall_stats = _safe_stats(deps_recall)
    cli_completeness_stats = _safe_stats(cli_completeness)
    desc_clarity_stats = _safe_stats(desc_clarity)
    desc_completeness_stats = _safe_stats(desc_completeness)
    desc_helpfulness_stats = _safe_stats(desc_helpfulness)

    return {
        "sample_size": len(valid),
        "dependencies_precision": deps_precision_stats,
        "dependencies_recall": deps_recall_stats,
        "cli_completeness": cli_completeness_stats,
        "description_clarity": desc_clarity_stats,
        "description_completeness": desc_completeness_stats,
        "description_helpfulness": desc_helpfulness_stats,
        # Legacy averages retained for compatibility
        "dependencies_precision_avg": deps_precision_stats.get("avg", 0.0),
        "dependencies_recall_avg": deps_recall_stats.get("avg", 0.0),
        "cli_completeness_avg": cli_completeness_stats.get("avg", 0.0),
        "description_clarity_avg": desc_clarity_stats.get("avg", 0.0),
        "description_completeness_avg": desc_completeness_stats.get("avg", 0.0),
        "description_helpfulness_avg": desc_helpfulness_stats.get("avg", 0.0),
    }


def _truncate(text: str, limit: int = 220) -> str:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return clean if len(clean) <= limit else f"{clean[: limit - 1]}…"


def _examples(results: List[Dict]) -> Dict[str, List[Dict[str, str | float]]]:
    valid = [item for item in results if "error" not in item]

    def _entry(item: Dict) -> Dict[str, str | float]:
        deps = item.get("dependencies", {})
        desc = item.get("description", {})
        return {
            "script": item.get("script", ""),
            "dep_precision": round(float(deps.get("precision", 0)), 3),
            "dep_recall": round(float(deps.get("recall", 0)), 3),
            "cli_completeness": round(float(item.get("cli", {}).get("completeness", 0)), 3),
            "clarity": round(float(desc.get("clarity", 0)), 3),
            "completeness": round(float(desc.get("completeness", 0)), 3),
            "helpfulness": round(float(desc.get("helpfulness", 0)), 3),
            "rationale": _truncate(str(desc.get("rationale", ""))),
        }

    top_helpfulness = sorted(
        valid, key=lambda x: x.get("description", {}).get("helpfulness", 0), reverse=True
    )[:3]
    bottom_deps = sorted(valid, key=lambda x: x.get("dependencies", {}).get("recall", 0))[:3]

    return {
        "top_helpfulness": [_entry(item) for item in top_helpfulness],
        "bottom_dependencies": [_entry(item) for item in bottom_deps],
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
            probe_help=True,
        )

        gt_text = _read_text(gt_readme)
        readme_dependencies = _extract_dependencies_from_readme(gt_text)
        precision, recall = _dependency_metrics(predicted_facts.get("imports", {}), readme_dependencies)

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
            raise RuntimeError(f"Description scoring failed: {exc}") from exc

        signal_profile = _build_signal_profile(
            predicted_cli,
            generation_provider=provider,
            generation_model=generation_model,
        )

        return {
            "script": script_path.name,
            "mode": mode,
            "readme_path": os.path.relpath(out_path, ROOT),
            "ground_truth": os.path.relpath(gt_readme, ROOT),
            "dependencies": {
                "precision": precision,
                "recall": recall,
                "actual": readme_dependencies,
                "predicted": predicted_facts.get("imports", {}).get("third_party", [])
                if isinstance(predicted_facts.get("imports", {}), dict)
                else [],
            },
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
    except Exception as exc:  # pragma: no cover
        return {
            "script": script_path.name,
            "ground_truth": os.path.relpath(gt_readme, ROOT),
            "error": str(exc),
            "mode": "error",
            "generation": {"provider": provider, "model": generation_model},
            "judge": {"provider": judge_provider, "model": judge_model},
        }


def _sanitize_label(value: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", value)
    return safe.strip("-") or "default"


def _ensure_run_label(args: argparse.Namespace) -> str:
    if args.run_label:
        return _sanitize_label(args.run_label)

    gen_base = args.gen_provider or args.provider or "openai"
    gen_model_part = args.gen_model or "auto"
    judge_base = args.judge_provider or gen_base
    judge_model_part = args.judge_model or DEFAULT_JUDGE_MODEL
    run_label = f"{gen_base}-{gen_model_part}__judge-{judge_base}-{judge_model_part}"
    return _sanitize_label(run_label)


def _key_findings(summary: Dict, results: List[Dict]) -> List[str]:
    if summary.get("sample_size", 0) == 0:
        if results:
            return [
                "- All samples failed to evaluate successfully; see the per-file table for error messages.",
            ]
        return ["- No samples were evaluated."]

    findings: List[str] = []

    dep_precision = summary.get("dependencies_precision", {}).get("avg", 0.0)
    dep_recall = summary.get("dependencies_recall", {}).get("avg", 0.0)
    if dep_precision < 0.1 and dep_recall < 0.1:
        findings.append(
            "- Dependency recovery is very poor (precision ~"
            f"{dep_precision:.3f}, recall ~{dep_recall:.3f}), indicating that the LLM-only "
            "pipeline struggles to infer real installation dependencies without AST/static analysis."
        )
    else:
        findings.append(
            "- Dependency recovery is mixed (precision ~"
            f"{dep_precision:.3f}, recall ~{dep_recall:.3f}) for the LLM-only pipeline."
        )

    clarity_stats = summary.get("description_clarity", {})
    completeness_stats = summary.get("description_completeness", {})
    helpfulness_stats = summary.get("description_helpfulness", {})
    tight_band = (
        (clarity_stats.get("max", 0) - clarity_stats.get("min", 0) < 1.0)
        and (completeness_stats.get("max", 0) - completeness_stats.get("min", 0) < 1.0)
        and (helpfulness_stats.get("max", 0) - helpfulness_stats.get("min", 0) < 1.0)
    )
    if tight_band:
        findings.append(
            "- Description scores are tightly clustered (clarity/completeness/helpfulness all in a "
            "narrow band), suggesting the judge is not strongly differentiating between stronger and "
            "weaker READMEs."
        )
    else:
        findings.append(
            "- Description scores show meaningful spread across scripts, indicating the judge is "
            "using the rating scale more discriminatively."
        )

    cli_avg = summary.get("cli_completeness", {}).get("avg", 0.0)
    findings.append(
        "- Average CLI flag coverage is ~"
        f"{cli_avg:.3f}; scripts with clear --help output do better, but some tools still miss flags "
        "mentioned in the reference README."
    )

    return findings


def _write_reports(run_label: str, results: List[Dict]):
    report_dir, _ = _run_paths(run_label)
    report_dir.mkdir(parents=True, exist_ok=True)

    report_path = report_dir / f"metrics_{run_label}.json"
    summary_path = report_dir / f"summary_{run_label}.md"

    summary = _summarize(results)
    signal_insights = _aggregate_signal_insights(results)
    example_sets = _examples(results)

    payload = {
        "run_label": run_label,
        "results": results,
        "summary": summary,
        "signal_insights": signal_insights,
        "examples": example_sets,
    }

    report_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    gen_info = next((item.get("generation", {}) for item in results if item.get("generation")), {})
    judge_info = next((item.get("judge", {}) for item in results if item.get("judge")), {})

    def _metric_row(label: str, data: Dict[str, float]) -> str:
        return (
            f"| {label} | {data.get('avg', 0):.3f} | {data.get('median', 0):.3f} | "
            f"{data.get('min', 0):.3f} | {data.get('max', 0):.3f} |"
        )

    def _signal_row(name: str, data: Dict[str, float | int]) -> str:
        return (
            f"| {name} | {data.get('sample_size', 0)} | {data.get('clarity', 0):.3f} | "
            f"{data.get('completeness', 0):.3f} | {data.get('helpfulness', 0):.3f} | "
            f"{data.get('cli_completeness', 0):.3f} | {data.get('dep_precision', 0):.3f} | "
            f"{data.get('dep_recall', 0):.3f} |"
        )

    lines = [f"# readmegenv2_no_ast evaluation: {run_label}", ""]
    lines.extend(
        [
            "## Run configuration",
            f"- Generation: {gen_info.get('provider', 'unknown')} / {gen_info.get('model', 'auto')}",
            f"- Judge: {judge_info.get('provider', 'unknown')} / {judge_info.get('model', DEFAULT_JUDGE_MODEL)}",
            f"- Sample size: {summary.get('sample_size', 0)}",
            "",
        ]
    )

    lines.append("## Aggregate metrics")
    lines.append("| metric | avg | median | min | max |")
    lines.append("| --- | --- | --- | --- | --- |")
    metric_map = {
        "Dependencies precision": summary.get("dependencies_precision", {}),
        "Dependencies recall": summary.get("dependencies_recall", {}),
        "CLI completeness": summary.get("cli_completeness", {}),
        "Description clarity": summary.get("description_clarity", {}),
        "Description completeness": summary.get("description_completeness", {}),
        "Description helpfulness": summary.get("description_helpfulness", {}),
    }
    for label, data in metric_map.items():
        lines.append(_metric_row(label, data))
    lines.append("")

    lines.append("## Key findings")
    for point in _key_findings(summary, results):
        lines.append(point)
    lines.append("")

    lines.append("## Signal insights")
    lines.append(
        "| bucket | sample size | clarity | completeness | helpfulness | CLI completeness | dep precision | dep recall |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for name, data in signal_insights.items():
        lines.append(_signal_row(name, data))
    lines.append("")

    if signal_insights.get("no_ast", {}).get("sample_size", 0) == summary.get("sample_size", 0):
        lines.append(
            "- All samples in this run are LLM-only (no AST facts), so the 'no_ast' bucket matches "
            "the global averages by design."
        )

    cli_gap = abs(
        signal_insights.get("has_cli_flags", {}).get("cli_completeness", 0.0)
        - signal_insights.get("no_cli_flags", {}).get("cli_completeness", 0.0)
    )
    if cli_gap >= 0.2:
        lines.append(
            "- Scripts where CLI flags were inferred from help output ('has_cli_flags') show notably "
            "higher CLI completeness than scripts without any inferred flags."
        )

    has_imports = signal_insights.get("has_imports", {})
    if (
        has_imports.get("dep_precision", 0.0) < 0.1
        and has_imports.get("dep_recall", 0.0) < 0.1
    ):
        lines.append(
            "- Even when imports are guessed from the source (has_imports), dependency precision/recall "
            "remain low, highlighting the limits of LLM-only analysis for installation guidance."
        )

    lines.append("")

    lines.append("## Example highlights")
    lines.append("### Top 3 scripts by description helpfulness")
    top_examples = example_sets.get("top_helpfulness", [])
    if top_examples:
        for ex in top_examples:
            lines.append(
                f"- **{ex['script']}** — strong README: dep P/R {ex['dep_precision']:.3f}/{ex['dep_recall']:.3f}, "
                f"CLI completeness {ex['cli_completeness']:.3f}, desc {ex['clarity']:.1f}/"
                f"{ex['completeness']:.1f}/{ex['helpfulness']:.1f}. "
                f"Rationale: {ex['rationale']}"
            )
    else:
        lines.append("- No successful runs to highlight.")

    lines.append("")
    lines.append("### Bottom 3 scripts by dependency recall")
    bottom_examples = example_sets.get("bottom_dependencies", [])
    if bottom_examples:
        for ex in bottom_examples:
            lines.append(
                f"- **{ex['script']}** — weak dependency coverage: dep P/R {ex['dep_precision']:.3f}/{ex['dep_recall']:.3f}, "
                f"CLI completeness {ex['cli_completeness']:.3f}, desc {ex['clarity']:.1f}/"
                f"{ex['completeness']:.1f}/{ex['helpfulness']:.1f}. "
                f"Rationale: {ex['rationale']}"
            )
    else:
        lines.append("- No dependency data available.")

    lines.append("")
    lines.append("## Per-file results")
    lines.append(
        "| Script | Dep P | Dep R | CLI completeness | Clarity | Completeness | Helpfulness | Mode | Error |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for item in results:
        if "error" in item:
            lines.append(
                f"| {item.get('script', '')} | — | — | — | — | — | — | {item.get('mode', 'error')} | "
                f"{str(item.get('error', '')).replace('|', '/')[:120]} |"
            )
            continue
        deps = item.get("dependencies", {})
        desc = item.get("description", {})
        cli = item.get("cli", {})
        lines.append(
            f"| {item.get('script', '')} | {deps.get('precision', 0):.3f} | {deps.get('recall', 0):.3f} | "
            f"{cli.get('completeness', 0):.3f} | {desc.get('clarity', 0):.3f} | {desc.get('completeness', 0):.3f} | "
            f"{desc.get('helpfulness', 0):.3f} | {item.get('mode', '')} | |"
        )

    summary_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {report_path} and {summary_path}")


def _parse_kv(text: str) -> tuple[str, str]:
    if ":" not in text:
        raise argparse.ArgumentTypeError("Expected provider:key")
    provider, key = text.split(":", 1)
    provider = provider.strip().lower()
    key = key.strip()
    if not provider or not key:
        raise argparse.ArgumentTypeError("Both provider and key must be non-empty")
    return provider, key


def main(argv: List[str] | None = None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gen-provider", "--provider", dest="gen_provider", default=None)
    parser.add_argument("--gen-model", dest="gen_model", default=None)
    parser.add_argument("--judge-provider", dest="judge_provider", default=None)
    parser.add_argument("--judge-model", dest="judge_model", default=None)
    parser.add_argument("--run-label", dest="run_label", default=None)
    parser.add_argument(
        "--api-key",
        dest="api_keys",
        action="append",
        default=None,
        type=_parse_kv,
        help="Optional provider-scoped API key overrides: provider:key",
    )

    args = parser.parse_args(argv)
    api_keys = dict(args.api_keys or [])

    gen_provider = choose_provider(args.gen_provider, api_keys=api_keys)
    judge_provider = choose_judge_provider(args.judge_provider, api_keys=api_keys)
    generation_model = args.gen_model
    judge_model = args.judge_model or DEFAULT_JUDGE_MODEL

    run_label = _ensure_run_label(args)
    report_dir, generated_dir = _run_paths(run_label)
    report_dir.mkdir(parents=True, exist_ok=True)
    generated_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for script_path in sorted(DATASET.glob("*.py")):
        gt_readme = script_path.with_suffix(".md")
        if not gt_readme.exists():
            print(f"Skipping {script_path.name}: missing ground-truth README")
            continue
        result = evaluate_script(
            script_path,
            gt_readme,
            provider=gen_provider,
            generation_model=generation_model,
            judge_provider=judge_provider,
            judge_model=judge_model,
            api_keys=api_keys,
            generated_dir=generated_dir,
        )
        results.append(result)

    _write_reports(run_label, results)


if __name__ == "__main__":  # pragma: no cover
    main()
