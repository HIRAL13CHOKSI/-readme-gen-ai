"""Prompt builders for README generation."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Tuple


def build_messages(facts: Dict[str, Any]) -> Tuple[List[Dict[str, str]], str]:
    """Return (messages, model_hint) for chat completion providers.

    model_hint is a suggested default model name; providers are free to ignore it.
    """

    facts_json = json.dumps(facts, indent=2)
    system = (
        "You are a professional technical writer who produces production-quality README.md files "
        "for open-source Python projects. Use only the provided facts; never fabricate flags or dependencies. "
        "Prefer concise, actionable language, clean Markdown, and conventional section ordering. "
        "Ground every instruction (install, usage, flags, examples) in the provided facts or obvious project metadata."
    )
    user = f"""
Generate a README.md in the style of top open-source Python projects (Requests, Pandas, FastAPI).
Use polished Markdown with badges, tables, fenced code blocks, and a professional tone.

Required sections (in order):
1. Title + one-line tagline under the H1
2. Badges (insert placeholder badges if not provided)
3. Overview (what the tool does; mention external_tools if any; call out notable features implied by the code)
4. Requirements (Python version, OS)
5. Dependencies
   - List stdlib modules separately from true third-party packages (combine imports.third_party with project.requirement_packages and remove imports.local).
   - If external_tools exist, add an "External Tools" subsection listing them.
6. Installation
   - Prefer requirements_files or pyproject/setup.py when present.
   - Otherwise show pip install for third-party dependencies and include an editable install variant.
   - Mention concrete commands such as "pip install -r <file>" when requirement files exist.
7. Usage
   - Use the provided usage_examples verbatim when available.
   - If the script imports Streamlit (see usage_examples and imports), prefer a "streamlit run <file>" command instead of python.
   - If project.has_dockerfile is true, add a docker build/run snippet referencing the script filename.
8. Flags
   - If cli.arguments is non-empty, render a Markdown table: Flag | Alias | Type | Required | Default | Help (include every flag and alias from the facts, including choices when available).
   - If no CLI arguments are detected, state "None" succinctly instead of fabricating options.
9. cURL Options Passthrough (add this section ONLY if external_tools contains "curl")
10. Environment Variables (table with columns: Name | Default | Description; infer a short description from the surrounding context when possible; otherwise say "Controls runtime behavior")
11. Examples
   - Provide at least two realistic examples grounded in usage patterns, showing typical commands and any important flags.
12. Input/Output (small table)
13. Testing (only if project metadata indicates tests; recommend pytest as the default)
14. Troubleshooting (2+ likely issues)
15. Contributing (placeholder if no info)
16. License (placeholder if no info)

Rules:
- Never invent dependencies or flags not in the provided facts.
- Treat modules listed under imports.local as project code, not installable packages.
- If a section has no data, insert a brief placeholder (e.g., "None specified" or "Coming soon").
- Boolean flags (store_true/store_false) must NOT show a placeholder value.
- Always include at least one usage example and one example per major execution mode (CLI, Streamlit, Docker) when applicable.
- Format everything as clean, polished Markdown with consistent headings and concise prose.

Facts about this script:
```json
{facts_json}
```
"""

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    model_hint = "gpt-4o-mini"
    return messages, model_hint
