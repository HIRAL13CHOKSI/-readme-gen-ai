"""Deterministic markdown renderer (used for diagnostics/testing)."""

from __future__ import annotations

from typing import Any, Dict, List


def _format_dependencies(imports: Dict[str, List[str]]) -> str:
    stdlib = imports.get("stdlib", []) or []
    third = imports.get("third_party", []) or []
    deps_std = "\n".join(f"- {pkg}" for pkg in stdlib) if stdlib else "- None"
    deps_third = "\n".join(f"- {pkg}" for pkg in third) if third else "- None"
    install_md = (
        f"```bash\npip install {' '.join(third)}\n```\n\n"
        "or\n\n"
        "```bash\npip install -r requirements.txt\n```"
    ) if third else "No third-party dependencies required."
    return deps_std, deps_third, install_md


def _format_usage(facts: Dict[str, Any]) -> str:
    usage_examples: List[str] = facts.get("usage_examples", []) or []
    usage_cmd = usage_examples[0] if usage_examples else f"python {facts.get('filename','script.py')}"
    if len(usage_cmd) > 80:
        parts = usage_cmd.split()
        lines: List[str] = []
        cur: List[str] = []
        total = 0
        for part in parts:
            if total + len(part) + (1 if cur else 0) > 70:
                lines.append(" ".join(cur) + " \\")
                cur = [part]
                total = len(part)
            else:
                cur.append(part)
                total += len(part) + (1 if cur else 0)
        if cur:
            lines.append(" ".join(cur))
        return "```bash\n" + "\n".join(lines) + "\n```"
    return f"```bash\n{usage_cmd}\n```"


def _format_flags(cli: Dict[str, Any]) -> str:
    args = cli.get("arguments", []) if isinstance(cli, dict) else []
    if not args:
        return ""
    header = "| Flag | Type | Required | Default | Help |\n|---|---|---|---|---|"
    rows = []
    for arg in args:
        names = arg.get("flag", "")
        if arg.get("alias"):
            names += f", {arg.get('alias')}"
        rows.append(
            f"| {names} | {arg.get('type','')} | {('✅' if arg.get('required', False) else '❌')} | {arg.get('default','—')} | {str(arg.get('help','')).replace('|','/')} |"
        )
    return f"\n## Flags\n\n{header}\n" + "\n".join(rows) + "\n"


def _format_env(env_vars: List[Dict[str, Any]]) -> str:
    if not env_vars:
        return ""
    lines = ["## Environment Variables\n", "| Name | Default | Description |", "|---|---|---|"]
    for env in env_vars:
        name = env.get("name", "")
        default = env.get("default", "—")
        lines.append(f"| `{name}` | `{default}` | Controls behavior; see `--help`. |")
    return "\n".join(lines) + "\n\n"


def deterministic_readme(facts: Dict[str, Any]) -> str:
    title = facts.get("filename", "Project")
    doc = facts.get("module_docstring") or ""
    tagline = doc.strip().splitlines()[0] if doc else "Auto-generated README based on static analysis."

    deps_std, deps_third, install_md = _format_dependencies(facts.get("imports", {}) or {})
    usage_block = _format_usage(facts)
    flags_section = _format_flags(facts.get("cli", {}) or {})
    env_section = _format_env(facts.get("env_vars", []) or [])

    external_tools: List[str] = facts.get("external_tools", []) or []
    tools_section = ""
    if external_tools:
        tools_section = "### External Tools\n" + "\n".join(f"- {tool}" for tool in external_tools) + "\n\n"

    io_table = (
        "| Input | Output |\n"
        "|-------|--------|\n"
        "| `.csv` (UTF-8 with headers) or `.json` (list of objects) | Summary statistics CSV at `--output`. |\n"
    )

    troubleshooting = (
        "- **ModuleNotFoundError** → run `pip install -r requirements.txt`.\n"
        "- **UnicodeDecodeError** → ensure files are UTF-8 encoded.\n"
    )

    badges = "[![Build Status](badge)](link) [![License](badge)](link)"

    return (
        f"# {title}\n"
        f"*{tagline}*\n\n"
        f"{badges}\n\n"
        f"## Requirements\n- Python 3.8+\n- Cross-platform (Windows, macOS, Linux)\n\n"
        f"## Dependencies\n**Standard Library**\n{deps_std}\n\n**Third-Party**\n{deps_third}\n\n"
        f"{tools_section}"
        f"## Installation\n{install_md}\n\n"
        f"## Usage\n{usage_block}\n"
        f"{flags_section}"
        f"## Examples\n{usage_block}\n\n"
        f"{env_section}"
        f"## Input / Output\n{io_table}\n"
        f"## Troubleshooting\n{troubleshooting}\n"
        f"## Contributing\nContributions are welcome! Please open an issue or pull request.\n\n"
        f"## License\nSpecify your license here (e.g., MIT).\n"
    )
