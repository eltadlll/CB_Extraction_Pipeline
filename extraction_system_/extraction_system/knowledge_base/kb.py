"""
Knowledge Base — auto-generates and caches concept entries.

First time a concept is seen → Gemini profiles it → saved as JSON.
Every time after → loaded from disk instantly, no API call.
"""

from __future__ import annotations
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from config import KB_DIR, WORLDSPEC_VOCAB

_WS_LIST = "\n".join(f"  - {ws}" for ws in WORLDSPEC_VOCAB)

# ─── Prompt ──────────────────────────────────────────────────────────────────

_KB_PROMPT = """You are a knowledge engineering agent.

Generate a structured knowledge base entry for the concept: "{concept}"

Return ONLY valid JSON (no markdown fences, no extra text):
{{
  "concept": "{concept}",
  "description": "<one clear paragraph>",
  "domain": "<primary domain, e.g. Physics / Engineering>",
  "key_processes": ["<process>", "<process>", "<process>", "<process>", "<process>"],
  "world_specs": ["<choose 3-5 from the allowed list below>"],
  "relations": {{
    "involves":   ["<entity>", "<entity>"],
    "produces":   ["<entity>", "<entity>"],
    "requires":   ["<entity>", "<entity>"],
    "transforms": ["<input> → <output>"]
  }}
}}

Allowed world_specs (use ONLY these exact strings):
{ws_list}
""".replace("{ws_list}", _WS_LIST)


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _safe(name: str) -> str:
    return name.lower().replace(" ", "_").replace("-", "_")


def _path(name: str) -> str:
    os.makedirs(KB_DIR, exist_ok=True)
    return os.path.join(KB_DIR, f"{_safe(name)}.json")


# ─── Public API ───────────────────────────────────────────────────────────────

def is_cached(concept: str) -> bool:
    return os.path.exists(_path(concept))


def load_or_generate(concept: str) -> dict:
    """
    Return the KB entry for a concept.
    Generates and caches it via Gemini if it doesn't exist yet.
    """
    p = _path(concept)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"[KB] '{concept}' loaded from cache.")
        return data

    # ── Not cached — generate ────────────────────────────────────────────────
    from utils.gemini_client import call_gemini
    print(f"[KB] '{concept}' not cached — generating via Gemini...")

    prompt = _KB_PROMPT.format(concept=concept)
    data: dict = call_gemini(prompt, expect_json=True)

    # Validate WorldSpecs
    data["world_specs"] = [w for w in data.get("world_specs", []) if w in WORLDSPEC_VOCAB]
    data["concept"] = concept

    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[KB] ✓ '{concept}' saved → {p}")
    return data


def as_prompt_context(concept: str) -> str:
    """Return the KB entry formatted for injection into an agent prompt."""
    data = load_or_generate(concept)
    lines = [f"Knowledge base entry for: {concept}"]
    for key, val in data.items():
        if isinstance(val, list):
            lines.append(f"  {key}: {', '.join(str(v) for v in val)}")
        elif isinstance(val, dict):
            for k2, v2 in val.items():
                lines.append(f"  {key}.{k2}: {v2}")
        else:
            lines.append(f"  {key}: {val}")
    return "\n".join(lines)


def list_cached() -> list[str]:
    if not os.path.exists(KB_DIR):
        return []
    return [
        f.replace(".json", "").replace("_", " ").title()
        for f in sorted(os.listdir(KB_DIR))
        if f.endswith(".json")
    ]


def delete(concept: str) -> bool:
    p = _path(concept)
    if os.path.exists(p):
        os.remove(p)
        print(f"[KB] Deleted '{concept}'")
        return True
    return False
