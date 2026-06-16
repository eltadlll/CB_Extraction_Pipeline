"""
Configuration — all tuneable parameters.
Uses gemini-1.5-flash (free tier).
"""

import os

# ─── Gemini ───────────────────────────────────────────────────────────────────
GEMINI_API_KEY: str  = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL: str    = "gemini-1.5-flash"
GEMINI_TEMPERATURE   = 0.2
GEMINI_MAX_TOKENS    = 8192

# ─── Degree scale ─────────────────────────────────────────────────────────────
# Each extracted property gets a symbolic degree label based on its
# semantic centrality score (0.0 → 1.0).
DEGREE_LABELS: dict = {
    (0.85, 1.01): "degree-1",   # core / definitional
    (0.65, 0.85): "degree-2",   # strong
    (0.45, 0.65): "degree-3",   # moderate
    (0.25, 0.45): "degree-4",   # weak
    (0.00, 0.25): "degree-5",   # peripheral / abstract
}

# ─── WorldSpec fixed vocabulary ───────────────────────────────────────────────
WORLDSPEC_VOCAB: list[str] = [
    "WorldSpec-Physics",
    "WorldSpec-Chemistry",
    "WorldSpec-Biology",
    "WorldSpec-Ecology",
    "WorldSpec-Thermodynamics",
    "WorldSpec-Engineering",
    "WorldSpec-Mathematics",
    "WorldSpec-ComputerScience",
    "WorldSpec-Economics",
    "WorldSpec-SocialScience",
    "WorldSpec-Philosophy",
    "WorldSpec-Medicine",
    "WorldSpec-Agriculture",
    "WorldSpec-Energy",
    "WorldSpec-Materials",
    "WorldSpec-Information",
    "WorldSpec-Cognition",
    "WorldSpec-Linguistics",
]

# ─── Paths ────────────────────────────────────────────────────────────────────
_ROOT    = os.path.dirname(__file__)
KB_DIR   = os.path.join(_ROOT, "knowledge_base", "concepts")
METTA_KB = os.path.join(_ROOT, "metta", "knowledge_base.metta")
OUT_DIR  = os.path.join(_ROOT, "outputs")