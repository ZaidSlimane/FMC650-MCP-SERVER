"""Comprehensive FMC650 MCP Server Package (`fmc650-comprehensive-mcp`).

Unifies:
- Tier 1: Teltonika Compiler XML (`generated_FMC650_spec1_cfg4.43.1.0.xml`) & Merged Schema (`fmx65_03.01.01.Rev.15_schema.json`)
- Tier 2: `.cfg` Profile Inspection, Diffing, Validation & Compilation (`cfg_tool.py`, `make_cfg.py`)
- Tier 3: Knowledge Graphs (`graph_v3.json`, `graph.json`)
- Tier 4: Flespi & Wialon `TR84` 146-Sensor / 1,161-Parameter Telematics Mappings (`flespi-parameters/`, `wialon-parameters/`)
- Tier 5: Diagnostic Playbooks (`diagnostic/`, `debugging-sessions/`) & Official Teltonika Documentation (`teltonika-docs/`)
"""
from __future__ import annotations

__version__ = "alfa-0.1"
