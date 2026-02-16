"""High-level pipeline for generating READMEs from Python scripts."""

from __future__ import annotations

import os
from typing import Any, Dict, Tuple

from .analysis import analyze_script
from .llm import call_llm, choose_provider
from .prompt import build_messages


def _render_markdown(
    facts: Dict[str, Any], provider: str | None, model: str | None, *, api_keys: Dict[str, str] | None
) -> Tuple[str, str]:
    """Render README markdown using the configured LLM provider.

    Returns (markdown, mode) where mode is always "ai". Any LLM availability or
    runtime errors propagate to the caller so we never silently fall back to a
    static template.
    """

    provider_to_use = choose_provider(provider, api_keys=api_keys)
    messages, model_hint = build_messages(facts)
    content = call_llm(provider_to_use, model or model_hint, messages, api_keys=api_keys)
    if not content.endswith("\n"):
        content += "\n"
    return content, "ai"


def generate_readme_for_file(
    path: str,
    *,
    out_path: str | None = None,
    provider: str | None = None,
    model: str | None = None,
    api_keys: Dict[str, str] | None = None,
    probe_help: bool = False,
) -> Tuple[str, str, Dict[str, Any]]:
    """Generate a README for a single Python script.

    Returns (output_path, mode, facts).
    """

    facts = analyze_script(path, probe_help=probe_help)
    markdown, mode = _render_markdown(facts, provider, model, api_keys=api_keys)

    output_path = out_path or os.path.join(os.path.dirname(path) or ".", "README.generated.md")
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(markdown)

    return output_path, mode, facts


def generate_readmes_in_folder(
    source_folder: str,
    *,
    output_folder: str,
    provider: str | None = None,
    model: str | None = None,
    api_keys: Dict[str, str] | None = None,
    probe_help: bool = False,
) -> Dict[str, str]:
    """Generate READMEs for every .py file in a folder.

    Returns mapping of filename -> output path.
    """

    os.makedirs(output_folder, exist_ok=True)
    outputs: Dict[str, str] = {}
    for filename in sorted(os.listdir(source_folder)):
        if not filename.endswith(".py"):
            continue
        script_path = os.path.join(source_folder, filename)
        output_name = f"{os.path.splitext(filename)[0]}_AI_README.md"
        out_path = os.path.join(output_folder, output_name)
        out_path, _, _ = generate_readme_for_file(
            script_path,
            out_path=out_path,
            provider=provider,
            model=model,
            api_keys=api_keys,
            probe_help=probe_help,
        )
        outputs[filename] = out_path
    return outputs
