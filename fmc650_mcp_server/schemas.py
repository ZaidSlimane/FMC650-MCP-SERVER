"""Structured Pydantic Output Schemas & Models for the Comprehensive FMC650 MCP Server."""
from __future__ import annotations

from enum import Enum
from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class ProvenanceTier(str, Enum):
    XML_COMPILER_SCHEMA = "TIER_1_XML_COMPILER_SCHEMA"
    VERIFIED_CFG_EXPORT = "TIER_2_VERIFIED_CFG_EXPORT"
    GRAPH_V3_ONTOLOGY = "TIER_3_GRAPH_V3_ONTOLOGY"
    TELEMATICS_MAPPING = "TIER_4_FLESPI_WIALON_MAPPING"
    DIAGNOSTIC_PLAYBOOK = "TIER_5_DIAGNOSTIC_PLAYBOOK"
    CLEANED_DOC_CORPUS = "TIER_6_CLEANED_DOCUMENTATION"


class CompiledCfgArtifact(BaseModel):
    base_profile: str
    output_path: Optional[str] = None
    sha256: Optional[str] = None
    total_parameters: int
    modified_count: int
    validation_passed: bool
    validation_errors: List[str] = Field(default_factory=list)
    applied_edits: Dict[str, str] = Field(default_factory=dict)


class TechnicalDefinitionItem(BaseModel):
    term_or_name: str = Field(description="Canonical name of the parameter, IO element, protocol, or hardware signal.")
    pid: Optional[str] = Field(default=None, description="Config Parameter ID(s), e.g. '46530' or '103060..103064', or 'N/A'.")
    avl_id: Optional[str] = Field(default=None, description="Teltonika Codec 8/8E AVL ID, e.g. '139' or '13657', or 'N/A'.")
    data_type_and_bounds: str = Field(description="Exact binary type, Min..Max range, Validate regex/hex rule, or Enum values.")
    default_value: Optional[str] = Field(default=None, description="Factory default value in 4.43.1.0 XML/schema.")
    flespi_wialon_mapping: Optional[str] = Field(default=None, description="Flespi parameter key and Wialon Path A/B key / sensor.")
    definition: str = Field(description="Clear, complete engineering definition with zero ambiguity.")
    provenance: ProvenanceTier = Field(default=ProvenanceTier.XML_COMPILER_SCHEMA)


class SituationDiagram(BaseModel):
    title: str = Field(description="Title of the diagram explaining the situation.")
    diagram_type: Literal["flowchart", "sequenceDiagram", "stateDiagram-v2"] = Field(
        default="flowchart",
        description="Mermaid diagram type: 'flowchart', 'sequenceDiagram', or 'stateDiagram-v2'.",
    )
    mermaid_code: str = Field(description="Syntax-validated Mermaid code modeling the exact situation.")
    caption: str = Field(description="Walkthrough of the nodes, transitions, or signals shown in the diagram.")
