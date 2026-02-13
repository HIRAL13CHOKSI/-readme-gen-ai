"""Unified README generation pipeline (v2).

This package combines static analysis of Python scripts with LLM-powered
drafting to produce polished README files. See __main__.py for CLI
entrypoints.
"""

from .pipeline import generate_readme_for_file, generate_readmes_in_folder

__all__ = ["generate_readme_for_file", "generate_readmes_in_folder"]
