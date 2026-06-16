"""
Algebraic Encoder.

Converts a ConceptProfile into three representations:
  1. CASL S-expression
  2. MeTTa atoms (Hyperon / OpenCog compatible)
  3. JSON structured dict

No AI calls — pure deterministic serialisation.
"""

from __future__ import annotations
from models.schemas import ConceptProfile, ExtractedProperty


# ══════════════════════════════════════════════════════════════════════════════
# 1. CASL S-expression
# ══════════════════════════════════════════════════════════════════════════════

def _casl_world_spec_set(world_specs: list[str]) -> str:
    """
    (WorldSpecSet
      (WorldSpec-A
       WorldSpec-B
       WorldSpec-C))

    or, if empty:

    (WorldSpecSet ())
    """
    if not world_specs:
        return "(WorldSpecSet ())"

    if len(world_specs) == 1:
        return f"(WorldSpecSet\n          ({world_specs[0]}))"

    inner = f"({world_specs[0]}\n"
    for ws in world_specs[1:]:
        inner += f"           {ws}\n"
    inner = inner.rstrip("\n") + ")"
    return f"(WorldSpecSet\n          {inner})"


def _casl_property(prop: ExtractedProperty) -> str:
    """
      (property-name
        (WorldSpecSet ...)
        degree-n)
    """
    ws_block = _casl_world_spec_set(prop.world_specs)
    # indent WorldSpecSet block by 8 spaces
    ws_indented = "\n".join("        " + line for line in ws_block.splitlines())
    return (
        f"      ({prop.name}\n"
        f"{ws_indented}\n"
        f"        {prop.degree_label})"
    )


def encode_casl(profile: ConceptProfile) -> str:
    """
    Full CASL S-expression for a concept:

    (Concept ConceptName
      (V-predicate
        (Property

          (property-name
            (WorldSpecSet (...))
            degree-n)

          ...)))
    """
    concept_name = profile.name.replace(" ", "")
    lines = [
        f"(Concept {concept_name}",
        "  (V-predicate",
        "    (Property",
        "",
    ]
    for prop in profile.properties:
        lines.append(_casl_property(prop))
        lines.append("")
    lines.append("    )))")
    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# 2. MeTTa atoms
# ══════════════════════════════════════════════════════════════════════════════

def encode_metta(profile: ConceptProfile) -> str:
    """
    MeTTa atoms for Hyperon / OpenCog Hyperon.

    (Concept ConceptName)
    (Domain ConceptName "...")
    (: property-name (Property ConceptName))
    (WorldSpecSet property-name (WorldSpec-X WorldSpec-Y))
    (Degree property-name degree-n)
    (CentralityValue property-name 0.92)
    (Description property-name "...")
    """
    cname = profile.name.replace(" ", "")
    lines = [
        f"; ── Concept: {profile.name} ─────────────────────────────────────────",
        f"(Concept {cname})",
        f'(Domain {cname} "{profile.domain}")',
        f'(Description {cname} "{profile.raw_description}")',
        "",
    ]

    for pred in profile.core_predicates:
        lines.append(f'(CorePredicate {cname} "{pred}")')
    lines.append("")

    ws_str = " ".join(profile.world_specs) if profile.world_specs else ""
    lines.append(f"(ConceptWorldSpecs {cname} ({ws_str}))")
    lines.append("")

    for prop in profile.properties:
        pname = prop.name
        ws_atom = "(" + " ".join(prop.world_specs) + ")" if prop.world_specs else "()"
        lines += [
            f"(: {pname} (Property {cname}))",
            f"(WorldSpecSet {pname} {ws_atom})",
            f"(Degree {pname} {prop.degree_label})",
            f"(CentralityValue {pname} {prop.centrality:.4f})",
            f'(Description {pname} "{prop.description}")',
            "",
        ]

    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# 3. JSON
# ══════════════════════════════════════════════════════════════════════════════

def encode_json(profile: ConceptProfile) -> dict:
    """
    Structured JSON — mirrors the CASL structure exactly.
    """
    return {
        "Concept": profile.name,
        "domain": profile.domain,
        "description": profile.raw_description,
        "core_predicates": profile.core_predicates,
        "concept_world_specs": profile.world_specs,
        "relations": profile.relations,
        "V_predicate": {
            "Property": [
                {
                    "id": p.property_id,
                    "name": p.name,
                    "WorldSpecSet": p.world_specs,
                    "degree": p.degree_label,
                    "centrality": p.centrality,
                    "description": p.description,
                }
                for p in profile.properties
            ]
        },
    }


# ─── Smoke test ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from models.schemas import ConceptProfile, ExtractedProperty

    dummy = ConceptProfile(
        name="Solar Energy",
        domain="Physics / Renewable Energy",
        raw_description="Radiant energy from the Sun harnessed for electricity and heat.",
        core_predicates=["emits-radiation", "drives-photovoltaic-conversion"],
        world_specs=["WorldSpec-Physics", "WorldSpec-Energy", "WorldSpec-Ecology"],
        relations={"involves": ["photons", "panels"], "produces": ["electricity"]},
        properties=[
            ExtractedProperty(property_id="property-1", name="electromagnetic-radiation-emission",
                world_specs=["WorldSpec-Physics","WorldSpec-Energy","WorldSpec-Thermodynamics"],
                centrality=0.95, degree_label="degree-1",
                description="Emission of electromagnetic radiation from the Sun."),
            ExtractedProperty(property_id="property-2", name="photovoltaic-conversion",
                world_specs=["WorldSpec-Physics","WorldSpec-Engineering","WorldSpec-Energy"],
                centrality=0.91, degree_label="degree-1",
                description="Conversion of photons into electrical current via semiconductors."),
            ExtractedProperty(property_id="property-3", name="thermal-energy-generation",
                world_specs=["WorldSpec-Thermodynamics","WorldSpec-Engineering","WorldSpec-Ecology"],
                centrality=0.87, degree_label="degree-1",
                description="Generation of thermal energy through solar irradiance absorption."),
            ExtractedProperty(property_id="property-4", name="spectral-irradiance-variation",
                world_specs=["WorldSpec-Physics","WorldSpec-Ecology"],
                centrality=0.68, degree_label="degree-2",
                description="Variation in solar irradiance across UV, visible, and IR spectrum."),
            ExtractedProperty(property_id="property-5", name="photosynthesis-enablement",
                world_specs=["WorldSpec-Biology","WorldSpec-Ecology"],
                centrality=0.62, degree_label="degree-2",
                description="Enabling of photosynthesis in plants via solar radiation."),
            ExtractedProperty(property_id="property-6", name="grid-integration",
                world_specs=["WorldSpec-Engineering"],
                centrality=0.44, degree_label="degree-3",
                description="Integration of solar-generated power into electrical grids."),
            ExtractedProperty(property_id="property-7", name="seasonal-output-variability",
                world_specs=["WorldSpec-Ecology"],
                centrality=0.38, degree_label="degree-4",
                description="Variability of solar output with seasons and geographic location."),
            ExtractedProperty(property_id="property-8", name="abstract-energy-potentiality",
                world_specs=[],
                centrality=0.12, degree_label="degree-5",
                description="Abstract potential of solar energy as an unbounded resource."),
        ],
    )

    print("═" * 60)
    print("CASL OUTPUT")
    print("═" * 60)
    print(encode_casl(dummy))
    print("\n" + "═" * 60)
    print("METTA OUTPUT")
    print("═" * 60)
    print(encode_metta(dummy))
