"""
Data schemas for the extraction pipeline.
Only what is needed: ConceptProfile and ExtractedProperty.
"""

from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field


class ExtractedProperty(BaseModel):
    """
    One property extracted from a concept.
    Carries everything needed for CASL + MeTTa encoding.
    """
    property_id: str                          # "property-1" … "property-8"
    name: str                                 # symbolic hyphenated name
    world_specs: List[str] = Field(default_factory=list)
    centrality: float = Field(ge=0.0, le=1.0) # how core this property is (0–1)
    degree_label: str = ""                    # "degree-1" … "degree-5"
    description: str = ""                     # one-sentence human-readable gloss


class ConceptProfile(BaseModel):
    """Full semantic profile of one concept, including its 8 extracted properties."""
    name: str
    domain: str = ""
    raw_description: str = ""
    core_predicates: List[str] = Field(default_factory=list)
    world_specs: List[str] = Field(default_factory=list)   # concept-level WorldSpecs
    relations: dict = Field(default_factory=dict)
    properties: List[ExtractedProperty] = Field(default_factory=list)  # exactly 8


class ExtractionResult(BaseModel):
    """Top-level container returned by the pipeline for two concepts."""
    concept_a: ConceptProfile
    concept_b: ConceptProfile
