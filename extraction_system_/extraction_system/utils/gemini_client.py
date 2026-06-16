"""
Gemini API client — using the new google-genai SDK (google-genai>=2.0).

  from google import genai

Cleaner than the legacy google-generativeai package:
- Single client instance instead of module-level configure()
- generate_content() lives on client.models
- JSON mime type enforced natively via response_mime_type
"""

from __future__ import annotations
import json
import re
import time
from google import genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_TEMPERATURE, GEMINI_MAX_TOKENS


_CLIENT: genai.Client | None = None


def get_client() -> genai.Client:
    global _CLIENT
    if _CLIENT is None:
        _CLIENT = genai.Client(api_key=GEMINI_API_KEY)
    return _CLIENT


def _strip_fences(text: str) -> str:
    """Remove ```json ... ``` fences if the model added them anyway."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def _check_truncated(response) -> bool:
    """Return True if Gemini stopped due to token limit (MAX_TOKENS finish reason)."""
    try:
        reason = response.candidates[0].finish_reason
        # finish_reason 2 = MAX_TOKENS in the new SDK
        return str(reason) in ("FinishReason.MAX_TOKENS", "MAX_TOKENS", "2")
    except Exception:
        return False


def call_gemini(prompt: str, expect_json: bool = False, retries: int = 3):
    """
    Send a prompt to Gemini and return the response.

    If expect_json=True, asks the model to return application/json
    via response_mime_type (new SDK native feature) and parses the result.
    Falls back to fence-stripping if the model ignores the mime type.
    """
    client = get_client()

    config = types.GenerateContentConfig(
        temperature=GEMINI_TEMPERATURE,
        max_output_tokens=GEMINI_MAX_TOKENS,
        response_mime_type="application/json" if expect_json else "text/plain",
    )

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=config,
            )

            if _check_truncated(response):
                raise ValueError(
                    f"Response was truncated (MAX_TOKENS hit). "
                    f"Current limit: {GEMINI_MAX_TOKENS}. "
                    f"Increase GEMINI_MAX_TOKENS in config.py."
                )

            text = response.text

            if expect_json:
                return json.loads(_strip_fences(text))
            return text

        except json.JSONDecodeError as e:
            if attempt == retries - 1:
                raise ValueError(
                    f"Gemini returned non-JSON after {retries} attempts.\n"
                    f"Likely cause: response was cut off mid-JSON.\n"
                    f"Fix: increase GEMINI_MAX_TOKENS in config.py (currently {GEMINI_MAX_TOKENS}).\n"
                    f"Parse error: {e}\nRaw tail: ...{text[-200:]}"
                ) from e
            time.sleep(1.5)

        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2.0)

    return {}