"""CLI entrypoint for the unified README generator."""

from __future__ import annotations

import argparse
import json
import os
from typing import Any, Dict

from .pipeline import generate_readme_for_file, generate_readmes_in_folder
from .llm import LLMUnavailable


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate README.md files from Python scripts.")
    parser.add_argument("path", help="Path to a .py file or a folder containing .py files")
    parser.add_argument("--out", help="Output README path (files) or folder (batch mode)")
    parser.add_argument("--provider", default="auto", help="LLM provider: auto|openai|groq")
    parser.add_argument("--model", help="Model name (provider-specific)")
    parser.add_argument(
        "--api-key",
        action="append",
        default=[],
        help="Override API key(s) in the form provider=KEY; can be passed multiple times to benchmark providers.",
    )
    parser.add_argument("--probe-help", action="store_true", help="Probe `python script.py --help` for richer metadata")
    parser.add_argument("--print-facts", action="store_true", help="Print collected facts for debugging")
    return parser.parse_args()


def _print_summary(path: str, mode: str, output_path: str, facts: Dict[str, Any]):
    print(f"README written to {output_path} [mode: {mode}]")
    print(f"Input: {path}")
    print(f"CLI flags detected: {len(facts.get('cli', {}).get('arguments', []))}")
    if facts.get("env_vars"):
        print(f"Environment variables: {', '.join(env['name'] for env in facts['env_vars'])}")


def main():
    args = _parse_args()

    provider = args.provider

    api_keys = {}
    for entry in args.api_key:
        if "=" not in entry:
            raise SystemExit("--api-key entries must look like provider=KEY")
        prov, key = entry.split("=", 1)
        api_keys[prov.strip().lower()] = key.strip()

    if os.path.isdir(args.path):
        output_folder = args.out or os.path.join(args.path, "ai_generated_readmes")
        try:
            outputs = generate_readmes_in_folder(
                args.path,
                output_folder=output_folder,
                provider=provider,
                model=args.model,
                api_keys=api_keys or None,
                probe_help=args.probe_help,
            )
            print(f"Generated {len(outputs)} README files into {output_folder}")
        except LLMUnavailable as exc:
            raise SystemExit(f"LLM unavailable: {exc}") from exc
        return

    try:
        output_path, mode, facts = generate_readme_for_file(
            args.path,
            out_path=args.out,
            provider=provider,
            model=args.model,
            api_keys=api_keys or None,
            probe_help=args.probe_help,
        )
    except LLMUnavailable as exc:
        raise SystemExit(f"LLM unavailable: {exc}") from exc

    if args.print_facts:
        print(json.dumps(facts, indent=2))
    _print_summary(args.path, mode, output_path, facts)


if __name__ == "__main__":
    main()
