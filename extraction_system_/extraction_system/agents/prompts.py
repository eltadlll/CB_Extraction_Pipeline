"""
Extraction agent prompt template.
"""

from config import WORLDSPEC_VOCAB

_WS_LIST = "\n".join(f"  - {ws}" for ws in WORLDSPEC_VOCAB)

EXTRACTION_PROMPT = """You are a property extraction agent for a Conceptual Blending system.

Your task: extract exactly 8 properties from the concept "{concept}".

Background knowledge:
{kb_context}

Rules for the 8 properties:
- Properties 1–3: HIGH centrality (0.85–1.00), FULL WorldSpecSet (3–5 WorldSpecs). These are the most defining, core properties of the concept.
- Properties 4–5: MEDIUM-HIGH centrality (0.55–0.75), PARTIAL WorldSpecSet (2–3 WorldSpecs).
- Properties 6–7: MEDIUM-LOW centrality (0.30–0.55), PARTIAL WorldSpecSet (1–2 WorldSpecs).
- Property 8:     LOW centrality (0.05–0.25), EMPTY WorldSpecSet (). This is a peripheral or abstract property.

Each property name must be a symbolic hyphenated identifier (e.g. "energy-transformation", "thermal-absorption").

Return ONLY valid JSON (no markdown, no extra text):
{{
  "name": "{concept}",
  "domain": "<primary domain>",
  "raw_description": "<one paragraph>",
  "core_predicates": ["<predicate>", "<predicate>", "<predicate>"],
  "world_specs": ["<concept-level WorldSpecs, 3-5>"],
  "relations": {{
    "involves":   ["<entity>"],
    "produces":   ["<entity>"],
    "requires":   ["<entity>"],
    "transforms": ["<input> → <output>"]
  }},
  "properties": [
    {{
      "property_id": "property-1",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X", "WorldSpec-Y", "WorldSpec-Z"],
      "centrality": <float 0.85–1.00>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-2",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X", "WorldSpec-Y", "WorldSpec-Z"],
      "centrality": <float 0.85–1.00>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-3",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X", "WorldSpec-Y", "WorldSpec-Z"],
      "centrality": <float 0.85–1.00>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-4",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X", "WorldSpec-Y"],
      "centrality": <float 0.55–0.75>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-5",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X", "WorldSpec-Y"],
      "centrality": <float 0.55–0.75>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-6",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X"],
      "centrality": <float 0.30–0.55>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-7",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": ["WorldSpec-X"],
      "centrality": <float 0.30–0.55>,
      "description": "<one sentence>"
    }},
    {{
      "property_id": "property-8",
      "name": "<symbolic-hyphenated-name>",
      "world_specs": [],
      "centrality": <float 0.05–0.25>,
      "description": "<one sentence>"
    }}
  ]
}}

Allowed WorldSpec values (use ONLY these):
{ws_list}
""".replace("{ws_list}", _WS_LIST)
