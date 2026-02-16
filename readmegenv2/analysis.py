"""Static analysis utilities for README generation (v2).

This module reuses the v1 heuristics with a cleaner API. It extracts
imports, argparse flags, environment variables, entrypoints, and other
useful hints for documentation.
"""

from __future__ import annotations

import ast
import importlib.util
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


def _is_stdlib(module: str) -> bool:
    """Best-effort stdlib detection (Python 3.10+ exposes stdlib_module_names)."""
    if not module:
        return False
    base = module.split(".")[0]
    if hasattr(sys, "stdlib_module_names"):
        return base in sys.stdlib_module_names  # type: ignore[attr-defined]
    spec = importlib.util.find_spec(base)
    if spec is None or spec.origin is None:
        return False
    origin = str(spec.origin).lower()
    return "python" in origin and "site-packages" not in origin


def _gather_imports(tree: ast.AST) -> Set[str]:
    """Return the set of all imported module bases found in the AST."""

    modules: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                if name.name:
                    modules.add(name.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module.split(".")[0])
    return modules


def _get_module_docstring(tree: ast.AST) -> Optional[str]:
    return ast.get_docstring(tree)


def _top_level_defs(tree: ast.AST):
    functions = []
    classes = []
    if isinstance(tree, ast.Module):
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                functions.append({"name": node.name, "doc": ast.get_docstring(node)})
            elif isinstance(node, ast.ClassDef):
                classes.append({"name": node.name, "doc": ast.get_docstring(node)})
    return functions, classes


def _find_dunder_main_call(tree: ast.AST) -> Dict[str, Any]:
    result = {"callable": None, "has_dunder_main": False}
    for node in tree.body if isinstance(tree, ast.Module) else []:
        if isinstance(node, ast.If):
            test = node.test

            def _is_dunder_main(c: ast.AST) -> bool:
                return isinstance(c, ast.Constant) and c.value == "__main__"

            def _is_dunder_name(n: ast.AST) -> bool:
                return isinstance(n, ast.Name) and n.id == "__name__"

            if isinstance(test, ast.Compare) and len(test.comparators) == 1:
                left, right = test.left, test.comparators[0]
                if (_is_dunder_name(left) and _is_dunder_main(right)) or (
                    _is_dunder_main(left) and _is_dunder_name(right)
                ):
                    result["has_dunder_main"] = True
                    for stmt in node.body:
                        call_name = None
                        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                            fn = stmt.value.func
                            if isinstance(fn, ast.Name):
                                call_name = fn.id
                            elif isinstance(fn, ast.Attribute):
                                call_name = fn.attr
                        if call_name:
                            result["callable"] = call_name
                            return result
    return result


def _lit_str(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _lit_bool(node: ast.AST) -> Optional[bool]:
    if isinstance(node, ast.Constant) and isinstance(node.value, bool):
        return node.value
    return None


def _lit_any(node: ast.AST):
    if isinstance(node, ast.Constant):
        return node.value
    return None


def _type_name(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _extract_argparse_args(tree: ast.AST) -> List[Dict[str, Any]]:
    args_info: List[Dict[str, Any]] = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "add_argument":
            continue

        flags: List[str] = []
        for arg in node.args:
            literal = _lit_str(arg)
            if literal:
                flags.append(literal)

        kw_map = {kw.arg: kw.value for kw in node.keywords if kw.arg}

        type_name = _type_name(kw_map.get("type")) if "type" in kw_map else None
        required = _lit_bool(kw_map.get("required")) if "required" in kw_map else None
        default = _lit_any(kw_map.get("default")) if "default" in kw_map else None
        help_txt = _lit_str(kw_map.get("help")) if "help" in kw_map else None
        action = _lit_str(kw_map.get("action")) if "action" in kw_map else None

        nargs = None
        if "nargs" in kw_map:
            value = kw_map["nargs"]
            if isinstance(value, ast.Constant):
                nargs = value.value

        choices = None
        if "choices" in kw_map:
            value = kw_map["choices"]
            if isinstance(value, (ast.List, ast.Tuple)):
                literal_choices = []
                for elt in value.elts:
                    literal = _lit_any(elt)
                    if literal is not None:
                        literal_choices.append(literal)
                choices = literal_choices or None

        flag = None
        alias = None
        aliases: List[str] = []
        name = _lit_str(kw_map.get("dest")) if "dest" in kw_map else None
        if flags:
            flags_sorted = sorted(flags, key=len, reverse=True)
            flag = flags_sorted[0]
            short = [f for f in flags if f.startswith("-") and not f.startswith("--")]
            alias = short[0] if short else None
            aliases = [item for item in flags if item != flag]
            # If no explicit dest is provided, derive longest flag.
            if not name and flag.startswith("-"):
                name = flag.lstrip("-").replace("-", "_")

        takes_value = True
        if action in {"store_true", "store_false"}:
            takes_value = False
        arg_type = type_name or ("bool" if not takes_value else "str")

        if flag:
            args_info.append(
                {
                    "flag": flag,
                    "name": name,
                    "flags": flags,
                    "alias": alias,
                    "aliases": aliases,
                    "type": arg_type,
                    "required": bool(required) if required is not None else False,
                    "default": default,
                    "help": help_txt or "",
                    "action": action,
                    "takes_value": takes_value,
                    "nargs": nargs,
                    "choices": choices,
                }
            )
    return args_info


def _extract_external_tools(tree: ast.AST) -> List[str]:
    tools = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in {"run", "Popen", "call", "check_call", "check_output"}:
                if node.args and isinstance(node.args[0], (ast.List, ast.Tuple)):
                    elements = node.args[0].elts
                    if elements and isinstance(elements[0], ast.Constant) and isinstance(
                        elements[0].value, str
                    ):
                        first = elements[0].value.strip().split()[0]
                        if first and "/" not in first and "\\" not in first:
                            tools.add(first)
                elif node.args and isinstance(node.args[0], ast.Constant) and isinstance(
                    node.args[0].value, str
                ):
                    first = node.args[0].value.strip().split()[0]
                    if first and "/" not in first and "\\" not in first:
                        tools.add(first)
    return sorted(tools)


_ENV_NAME_RE = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")


def _is_env_like(value: str) -> bool:
    return bool(_ENV_NAME_RE.match(value)) and "_" in value


def _lit_scalar_value(node: ast.AST):
    if isinstance(node, ast.Constant) and isinstance(node.value, (bool, int, float, str)):
        return node.value
    return None


def _extract_env_vars(tree: ast.AST) -> List[dict]:
    found: Dict[str, Any] = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            func = node.func
            if isinstance(func.value, ast.Name) and func.value.id == "os" and func.attr == "getenv":
                if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                    name = node.args[0].value
                    default = _lit_scalar_value(node.args[1]) if len(node.args) >= 2 else None
                    if _is_env_like(name):
                        found.setdefault(name, default)
            if (
                isinstance(func.value, ast.Attribute)
                and isinstance(func.value.value, ast.Name)
                and func.value.value.id == "os"
                and func.value.attr == "environ"
                and func.attr == "get"
            ):
                if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                    name = node.args[0].value
                    default = _lit_scalar_value(node.args[1]) if len(node.args) >= 2 else None
                    if _is_env_like(name):
                        found.setdefault(name, default)

    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Attribute):
            if (
                isinstance(node.value.value, ast.Name)
                and node.value.value.id == "os"
                and node.value.attr == "environ"
            ):
                key = node.slice
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    name = key.value
                    if _is_env_like(name):
                        found.setdefault(name, None)

    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for key, value in zip(node.keys, node.values):
                if isinstance(key, ast.Constant) and isinstance(key.value, str) and _is_env_like(key.value):
                    default = _lit_scalar_value(value)
                    if key.value not in found or found[key.value] is None:
                        found[key.value] = default

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            candidate = node.value
            if _is_env_like(candidate) and candidate not in found:
                found[candidate] = None

    return [{"name": name, "default": found[name]} for name in sorted(found)]


def _collect_local_modules(script_path: Path, imports: Set[str]) -> Set[str]:
    """Identify imports that refer to local modules in the repo.

    We scan the script directory, its parent, and the nearest git root to
    avoid misclassifying project modules (e.g., "app" or "src") as third-party
    dependencies. This keeps dependency precision high while improving recall
    for real external packages.
    """

    local: Set[str] = set()
    candidates = list({script_path.parent})

    for parent in script_path.parents:
        if (parent / ".git").exists():
            candidates.append(parent)
            break
    else:
        if script_path.parent.parent:
            candidates.append(script_path.parent.parent)

    for base in imports:
        for root in candidates:
            if (root / f"{base}.py").exists() or (root / base / "__init__.py").exists():
                local.add(base)
                break
    return local


def _detect_positional_usage(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id == "sys" and node.attr == "argv":
                return True
    return False


def _scan_literals(tree: ast.AST):
    has_url_hint = False
    mentions_curl = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            content = node.value.lower()
            if "http://" in content or "https://" in content:
                has_url_hint = True
            if "curl" in re.split(r"[^\w]+", content):
                mentions_curl = True
    return has_url_hint, mentions_curl


def _discover_project_metadata(path: Path) -> Dict[str, Any]:
    """Surface lightweight project metadata useful for install/run guidance."""

    search_roots = [path.parent]
    if path.parent.parent:
        search_roots.append(path.parent.parent)

    requirement_files: List[str] = []
    requirement_packages: Set[str] = set()
    has_setup = False
    has_pyproject = False
    tests_hint = False

    for root in search_roots:
        if not root.exists():
            continue
        if (root / "setup.py").exists():
            has_setup = True
        if (root / "pyproject.toml").exists():
            has_pyproject = True
        if (root / "tests").exists():
            tests_hint = True
        for req in root.glob("requirements*.txt"):
            rel = os.path.relpath(req, path.parent)
            requirement_files.append(rel)
            try:
                with open(req, "r", encoding="utf-8") as fh:
                    for line in fh:
                        stripped = line.strip()
                        if not stripped or stripped.startswith(("#", "-r")):
                            continue
                        # Capture package name before any version specifiers/extras.
                        pkg = re.split(r"[;=<>!\[ ]", stripped, maxsplit=1)[0]
                        if pkg:
                            requirement_packages.add(pkg)
            except OSError:
                continue

    requirement_files = sorted({item for item in requirement_files})
    return {
        "requirements_files": requirement_files,
        "requirement_packages": sorted(requirement_packages),
        "has_setup_py": has_setup,
        "has_pyproject": has_pyproject,
        "has_tests": tests_hint,
        "has_dockerfile": any((root / "Dockerfile").exists() for root in search_roots),
    }


def _probe_help(script_path: str, timeout_s: float = 2.0) -> Dict[str, Any]:
    import subprocess
    import tempfile

    try:
        with tempfile.TemporaryDirectory() as td:
            cmd = [sys.executable, script_path, "--help"]
            env = os.environ.copy()
            env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONWARNINGS": "ignore", "NO_COLOR": "1"})
            proc = subprocess.run(
                cmd,
                cwd=td,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=timeout_s,
            )
            out = proc.stdout or ""
    except Exception:
        return {"help_stdout": "", "flags": [], "usage_lines": [], "env_candidates": []}

    usage_lines = [ln for ln in out.splitlines() if ln.strip().lower().startswith(("usage:", "usage "))]
    flag_re = re.compile(r"(^|\s)(--[a-z0-9][a-z0-9-]*|-{1}[a-zA-Z])(?=\s|,|$)")
    env_re = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b")
    flags = sorted({match.group(2) for match in flag_re.finditer(out)})
    env_candidates = sorted({name for name in env_re.findall(out) if "_" in name})
    return {"help_stdout": out, "flags": flags, "usage_lines": usage_lines, "env_candidates": env_candidates}


def analyze_script(path: str, *, probe_help: bool = False) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    script_path = Path(path).resolve()

    all_imports = _gather_imports(tree)
    local_modules = _collect_local_modules(script_path, all_imports)
    stdlib = sorted([module for module in all_imports if _is_stdlib(module)])
    third_party = sorted([module for module in all_imports if module not in stdlib and module not in local_modules])

    cli_args = _extract_argparse_args(tree)
    entry = _find_dunder_main_call(tree)
    functions, classes = _top_level_defs(tree)

    external_tools = _extract_external_tools(tree)
    env_vars = _extract_env_vars(tree)
    has_positional = _detect_positional_usage(tree)

    has_url_hint, mentions_curl = _scan_literals(tree)
    env_defaults = {item.get("name"): item.get("default") for item in env_vars}
    if any(str(value).lower() == "curl" for value in env_defaults.values() if value is not None):
        if "curl" not in external_tools:
            external_tools.append("curl")
    if mentions_curl and "curl" not in external_tools:
        external_tools.append("curl")
    external_tools = sorted(set(external_tools))

    base_cmd = f"python {os.path.basename(path)}"
    # Prefer the Streamlit entrypoint when the library is imported to mirror real usage.
    if "streamlit" in third_party:
        base_cmd = f"streamlit run {os.path.basename(path)}"
    usage = [base_cmd]
    if cli_args:
        parts: List[str] = []
        for arg in cli_args:
            long = arg.get("flag") or ""
            short = arg.get("alias")
            flag_to_show = long if long.startswith("--") else (short or long)
            if not flag_to_show:
                continue
            if arg.get("takes_value", True):
                nargs = arg.get("nargs")
                if nargs in (None, 1):
                    placeholder = "<value>"
                elif nargs in ("*", "+"):
                    placeholder = "<value1> <value2> ..."
                elif isinstance(nargs, int) and nargs > 1:
                    placeholder = " ".join(f"<v{i+1}>" for i in range(nargs))
                else:
                    placeholder = "<value>"
                parts.append(f"{flag_to_show} {placeholder}")
            else:
                parts.append(flag_to_show)
        if parts:
            usage = [base_cmd + " " + " ".join(parts)]
    elif has_positional:
        usage = [base_cmd + " " + ("<url>" if has_url_hint else "<arg>")]

    probe_info: Dict[str, Any] = {}
    if probe_help:
        probe_info = _probe_help(path)
        if not cli_args and probe_info.get("flags"):
            cli_args = [
                {
                    "flag": flag,
                    "flags": [flag],
                    "alias": None,
                    "aliases": [],
                    "type": "str",
                    "required": False,
                    "default": None,
                    "help": "",
                    "action": None,
                    "takes_value": True,
                    "nargs": None,
                    "choices": None,
                }
                for flag in probe_info["flags"]
            ]
        if probe_info.get("usage_lines"):
            usage = ["\n".join(probe_info["usage_lines"])]
        existing_env = {item["name"] for item in env_vars}
        for name in probe_info.get("env_candidates", []):
            if name not in existing_env and "_" in name:
                env_vars.append({"name": name, "default": None})

    project_meta = _discover_project_metadata(script_path)
    dependency_candidates = sorted(set(third_party) | set(project_meta.get("requirement_packages", [])))

    facts = {
        "filename": os.path.basename(path),
        "module_docstring": _get_module_docstring(tree),
        "imports": {"stdlib": stdlib, "third_party": third_party, "local": sorted(local_modules)},
        "cli": {"framework": "argparse" if cli_args else "none", "arguments": cli_args},
        "entrypoint": entry,
        "functions": functions,
        "classes": classes,
        "external_tools": external_tools,
        "env_vars": env_vars,
        "has_positional_args": has_positional,
        "usage_examples": usage,
        "project": project_meta,
        "dependency_candidates": dependency_candidates,
    }

    return facts
