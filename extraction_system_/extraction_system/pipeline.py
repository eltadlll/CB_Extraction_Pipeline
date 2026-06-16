"""
Pipeline — Extraction + Algebraic Encoding.

Steps:
  1. Load or auto-generate KB entry for Concept A  (parallel with B)
  2. Load or auto-generate KB entry for Concept B
  3. Extract 8 algebraic properties for each concept via Gemini
  4. Encode each → CASL S-expression
  5. Encode each → MeTTa atoms
  6. Encode each → JSON
  7. Save all outputs
  8. Append MeTTa atoms to knowledge_base.metta
"""

from __future__ import annotations
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(__file__))

from config import GEMINI_API_KEY, OUT_DIR, METTA_KB
from agents.extractor import extract
from encoder.algebraic_encoder import encode_casl, encode_metta, encode_json
from models.schemas import ConceptProfile, ExtractionResult


# ─── Save helpers ─────────────────────────────────────────────────────────────

def _save(profile: ConceptProfile):
    os.makedirs(OUT_DIR, exist_ok=True)
    safe = profile.name.replace(" ", "_")

    casl_path  = os.path.join(OUT_DIR, f"{safe}.casl")
    metta_path = os.path.join(OUT_DIR, f"{safe}.metta")
    json_path  = os.path.join(OUT_DIR, f"{safe}.json")

    casl_str  = encode_casl(profile)
    metta_str = encode_metta(profile)
    json_data = encode_json(profile)

    with open(casl_path,  "w", encoding="utf-8") as f: f.write(casl_str)
    with open(metta_path, "w", encoding="utf-8") as f: f.write(metta_str)
    with open(json_path,  "w", encoding="utf-8") as f: json.dump(json_data, f, indent=2)

    # Append to shared MeTTa KB
    with open(METTA_KB, "a", encoding="utf-8") as f:
        f.write(f"\n; ── {profile.name} (auto-extracted) ──────────────────────────\n")
        f.write(metta_str)
        f.write("\n")

    print(f"[Pipeline] Saved: {safe}.casl | {safe}.metta | {safe}.json")
    return casl_str, metta_str, json_data


# ─── Main ─────────────────────────────────────────────────────────────────────

def run(concept_a: str, concept_b: str) -> dict:
    """
    Run the extraction pipeline for two concepts in parallel.

    Returns a dict with keys:
      concept_a, concept_b — each containing casl, metta, json, profile
    """
    if not GEMINI_API_KEY:
        raise EnvironmentError(
            "GEMINI_API_KEY not set.\n"
            "Get a free key: https://aistudio.google.com/app/apikey\n"
            "Then: export GEMINI_API_KEY='your_key'"
        )

    t0 = time.time()
    print("=" * 60)
    print(f" Extraction Pipeline")
    print(f" Concept A: {concept_a}")
    print(f" Concept B: {concept_b}")
    print("=" * 60)

    # ── Step 1–3: Parallel extraction ────────────────────────────────────────
    print("\n[Step 1] Extracting both concepts in parallel...")
    with ThreadPoolExecutor(max_workers=2) as ex:
        fut_a = ex.submit(extract, concept_a)
        fut_b = ex.submit(extract, concept_b)
        profile_a: ConceptProfile = fut_a.result()
        profile_b: ConceptProfile = fut_b.result()

    # ── Steps 4–8: Encode and save ───────────────────────────────────────────
    print("\n[Step 2] Encoding and saving outputs...")
    casl_a, metta_a, json_a = _save(profile_a)
    casl_b, metta_b, json_b = _save(profile_b)

    # ── Print CASL to terminal ────────────────────────────────────────────────
    print(f"\n{'─' * 60}")
    print(f"CASL — {concept_a}")
    print('─' * 60)
    print(casl_a)
    print(f"\n{'─' * 60}")
    print(f"CASL — {concept_b}")
    print('─' * 60)
    print(casl_b)

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f" ✓ Done in {elapsed:.1f}s — outputs in {OUT_DIR}/")
    print(f"{'=' * 60}")

    return {
        "concept_a": {"profile": profile_a, "casl": casl_a, "metta": metta_a, "json": json_a},
        "concept_b": {"profile": profile_b, "casl": casl_b, "metta": metta_b, "json": json_b},
    }


# ─── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extraction + Algebraic Encoding Pipeline")
    parser.add_argument("--concept-a", default="Solar Energy")
    parser.add_argument("--concept-b", default="Water Purification")
    args = parser.parse_args()
    run(args.concept_a, args.concept_b)
