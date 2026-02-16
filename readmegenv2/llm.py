"""LLM client abstraction with provider overrides.

The module supports multiple providers
"""

from __future__ import annotations

import os
from typing import Dict, List, Mapping, Optional


def load_api_keys(env: Mapping[str, str] | None = None) -> Dict[str, str]:
    """Load available API keys from environment variables.
    """

    env = env or os.environ
    keys: Dict[str, str] = {}

    openai_key = env.get("OPENAI_API_KEY") or env.get("READMEGENV2_OPENAI_API_KEY")
    if openai_key:
        keys["openai"] = openai_key

    groq_key = env.get("GROQ_API_KEY") or env.get("READMEGENV2_GROQ_API_KEY")
    if groq_key:
        keys["groq"] = groq_key

    google_key = env.get("GEMINI_API_KEY") or env.get("GOOGLE_API_KEY")
    if google_key:
        keys["google"] = google_key

    extras = env.get("READMEGENV2_EXTRA_API_KEYS", "")
    for raw in extras.split(","):
        if not raw.strip():
            continue
        if ":" not in raw:
            continue
        provider, key = raw.split(":", 1)
        provider = provider.strip().lower()
        key = key.strip()
        if provider and key:
            keys[provider] = key

    return keys


class LLMUnavailable(RuntimeError):
    """Raised when no provider is available."""


def _openai_client(api_key: Optional[str] = None):
    api_key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("READMEGENV2_OPENAI_API_KEY")
    if not api_key:
        raise LLMUnavailable("OPENAI_API_KEY not set")
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise LLMUnavailable(f"openai package not installed: {exc}") from exc
    return OpenAI(api_key=api_key)


def _groq_client(api_key: Optional[str] = None):
    api_key = api_key or os.getenv("GROQ_API_KEY") or os.getenv("READMEGENV2_GROQ_API_KEY")
    if not api_key:
        raise LLMUnavailable("GROQ_API_KEY not set")
    try:
        from groq import Groq
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise LLMUnavailable(f"groq package not installed: {exc}") from exc
    return Groq(api_key=api_key)


def _google_client(api_key: Optional[str] = None):
    """
    Return a configured google.generativeai client.
    Looks up key from:
      - explicit api_key argument, or
      - load_api_keys()["google"], or
      - GEMINI_API_KEY / GOOGLE_API_KEY
    """

    api_key = (
        api_key
        or load_api_keys().get("google")
        or os.getenv("GEMINI_API_KEY")
        or os.getenv("GOOGLE_API_KEY")
    )
    if not api_key:
        raise LLMUnavailable("Google Gemini API key not set")
    try:
        import google.generativeai as genai
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise LLMUnavailable(f"google-generativeai package not installed: {exc}") from exc

    genai.configure(api_key=api_key)
    return genai


def call_llm(
    provider: str, model: str, messages: List[Dict[str, str]], *, api_keys: Dict[str, str] | None = None
) -> str:
    """Call a chat-completions style API and return text content.

    Provider can be "openai", "google", or "groq". Raises LLMUnavailable if the
    provider cannot be used.
    """

    provider = provider.lower()
    keys = api_keys or load_api_keys()
    key = keys.get(provider)
    if provider == "openai":
        client = _openai_client(key)
        response = client.chat.completions.create(model=model, messages=messages, temperature=0.25)
        return response.choices[0].message.content or ""
    if provider == "groq":
        client = _groq_client(key)
        response = client.chat.completions.create(model=model, messages=messages, temperature=0.25)
        return response.choices[0].message.content or ""
    if provider == "google":
        genai = _google_client(key)
        prompt = "\n\n".join(
            f"{m.get('role', 'user').upper()}: {m.get('content', '')}"
            for m in messages
        )
        try:
            model_obj = genai.GenerativeModel(model)
            result = model_obj.generate_content(prompt)
        except Exception as exc:  # pragma: no cover - passthrough errors
            raise LLMUnavailable(f"Gemini generate_content failed: {exc}") from exc

        text = getattr(result, "text", None)
        if not text:
            candidates = getattr(result, "candidates", []) or []
            if candidates:
                content = getattr(candidates[0], "content", None)
                parts = getattr(content, "parts", None) if content is not None else None
                if isinstance(parts, list) and parts:
                    text = getattr(parts[0], "text", None)
        if not text:
            raise LLMUnavailable("Gemini returned no text content")
        return text

    raise LLMUnavailable(f"Unknown provider: {provider}")


def choose_provider(preferred: str | None = None, *, api_keys: Dict[str, str] | None = None) -> str:
    """Return provider string based on preference and available API keys.

    Priority:
      1. explicit provider argument (if not "auto")
      2. presence of keys: openai -> google -> groq
      3. raise LLMUnavailable with a clear message
    """

    if preferred and preferred != "auto":
        return preferred.lower()

    keys = {**load_api_keys(), **(api_keys or {})}

    if "openai" in keys:
        return "openai"
    if "google" in keys:
        return "google"
    if "groq" in keys:
        return "groq"

    raise LLMUnavailable(
        "No provider specified and no usable API key found; "
        "set OPENAI_API_KEY, GEMINI_API_KEY, or READMEGENV2_EXTRA_API_KEYS, "
        "or pass --gen-provider explicitly."
    )


def choose_judge_provider(preferred: str | None = None, *, api_keys: Dict[str, str] | None = None) -> str:
    """Return provider used as the evaluation judge.

    Preference order mirrors generation selection while defaulting to OpenAI
    when available so existing behavior is preserved. Any provider with a valid
    API key (openai, google, groq, or entries from READMEGENV2_EXTRA_API_KEYS)
    can serve as the judge, enabling judge-bias experiments.
    """

    if preferred and preferred != "auto":
        return preferred.lower()

    keys = {**load_api_keys(), **(api_keys or {})}
    for candidate in ("openai", "google", "groq"):
        if candidate in keys:
            return candidate

    raise RuntimeError(
        "No judge provider available; set OPENAI_API_KEY, GEMINI_API_KEY/GOOGLE_API_KEY, "
        "GROQ_API_KEY, or pass provider-scoped keys via --api-key provider:key."
    )
