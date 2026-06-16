"""
Extraction Agent.

For a single concept:
  1. Load or auto-generate its KB entry.
  2. Call Gemini with the extraction prompt to get 8 properties,
     each with WorldSpecs and a centrality score.
  3. Validate and return a ConceptProfile.
"""

from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from models.schemas import ConceptProfile, ExtractedProperty
from agents.prompts import EXTRACTION_PROMPT
from knowledge_base.kb import as_prompt_context
from utils.gemini_client import call_gemini
from config import WORLDSPEC_VOCAB, DEGREE_LABELS


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _degree_label(centrality: float) -> str:
    for (lo, hi), label in DEGREE_LABELS.items():
        if lo <= centrality < hi:
            return label
    return "degree-5"


def _clean_ws(ws_list: list) -> list[str]:
    return [w for w in ws_list if w in WORLDSPEC_VOCAB]


def _parse_properties(raw_props: list[dict]) -> list[ExtractedProperty]:
    props = []
    for i, p in enumerate(raw_props[:8]):
        centrality = float(p.get("centrality", 0.5))
        centrality = max(0.0, min(1.0, centrality))
        props.append(ExtractedProperty(
            property_id=f"property-{i + 1}",
            name=p.get("name", f"property-{i + 1}"),
            world_specs=_clean_ws(p.get("world_specs", [])),
            centrality=centrality,
            degree_label=_degree_label(centrality),
            description=p.get("description", ""),
        ))
    # Pad to 8 if Gemini returned fewer
    while len(props) < 8:
        i = len(props)
        props.append(ExtractedProperty(
            property_id=f"property-{i + 1}",
            name=f"abstract-property-{i + 1}",
            world_specs=[],
            centrality=0.1,
            degree_label="degree-5",
            description="Abstract peripheral property.",
        ))
    return props


# ─── Main ────────────────────────────────────────────────────────────────────

def extract(concept: str) -> ConceptProfile:
    """
    Extract 8 algebraic properties from a concept.
    Auto-generates KB entry if not already cached.
    """
    kb_context = as_prompt_context(concept)
    prompt = EXTRACTION_PROMPT.format(concept=concept, kb_context=kb_context)
    raw: dict = call_gemini(prompt, expect_json=True)

    properties = _parse_properties(raw.get("properties", []))

    profile = ConceptProfile(
        name=concept,
        domain=raw.get("domain", ""),
        raw_description=raw.get("raw_description", ""),
        core_predicates=raw.get("core_predicates", []),
        world_specs=_clean_ws(raw.get("world_specs", [])),
        relations=raw.get("relations", {}),
        properties=properties,
    )

    print(f"[ExtractionAgent] ✓ '{concept}' → {len(properties)} properties")
    for p in properties:
        ws = ", ".join(p.world_specs) if p.world_specs else "(empty)"
        print(f"   {p.property_id}: {p.name} | {ws} | {p.degree_label} ({p.centrality:.2f})")

    return profile
