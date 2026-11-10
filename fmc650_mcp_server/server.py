"""Comprehensive FMC650 FastMCP Server (`fmc650-comprehensive-mcp`).

Exposes:
- 17 deterministic MCP Tools (covering Identifier Resolution, Bilingual Corpus Search,
  Diagnostic Playbooks, Combined Device Behavior Investigation, Debugging Session Evidence Search, Telematics Mapping, Wialon TR84 146-Sensor Profile Inspection,
  Interactive Weight/Trailer Setup Diagnostics, Flespi/SMS Command Generation,
  .cfg Inspection, .cfg Diffing, .cfg Validation & Compilation, IO Block Siblings,
  Knowledge Graph Traversal, Document Section Reading, Firmware/PCN History, and
  Mermaid Validation)
- 6 MCP Resources (`fmc650://schema/summary`, `fmc650://profiles/list`,
  `fmc650://corpus/manifest`, `fmc650://diagnostic/index`,
  `fmc650://telematics/weight-and-trailer-catalog`, `fmc650://telematics/mappings`)
- 4 MCP Prompts (`prompt_diagnose_fms_or_trailer_weight`, `prompt_audit_cfg_profile`,
  `prompt_map_flespi_wialon_sensor`, `prompt_explain_incline_and_calibration`)
"""
from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Optional

try:
    from fastmcp import FastMCP
except ImportError:
    try:
        from mcp.server.mcpserver import MCPServer as FastMCP  # type: ignore
    except ImportError:
        try:
            from mcp.server.fastmcp import FastMCP  # type: ignore
        except ImportError:  # pragma: no cover
            class FastMCP:  # type: ignore
                def __init__(self, name: str):
                    self.name = name

                def tool(self, *args, **kwargs):
                    def _dec(fn):
                        return fn
                    return _dec

                def resource(self, *args, **kwargs):
                    def _dec(fn):
                        return fn
                    return _dec

                def prompt(self, *args, **kwargs):
                    def _dec(fn):
                        return fn
                    return _dec

                def run(self, *args, **kwargs):
                    pass

from fmc650_mcp_server.mermaid_validator import validate_and_repair_mermaid
from fmc650_mcp_server.repository import ALL_KNOWLEDGE_DIRS, FMC650KnowledgeRepository

mcp = FastMCP("fmc650-comprehensive-mcp")


# ============================================================================
# 1. IDENTIFIER RESOLUTION & FULL-CORPUS SEARCH TOOLS
# ============================================================================

@mcp.tool()
def mcp_resolve_identifiers(identifiers: List[str]) -> Dict[str, Any]:
    """Resolve any mix of Configuration PIDs, IO Block IoIds, Wire AVL IDs, Flespi parameters, Wialon keys, or Wialon Sensor IDs."""
    repo = FMC650KnowledgeRepository.get_instance()
    resolved: Dict[str, Any] = {}

    for raw_id in identifiers:
        token = str(raw_id).strip()
        if not token:
            continue

        # Check Wialon Sensor ID syntax (e.g. "sensor:71" or "Sensor 71")
        m_sens = re.match(r"^sensor\s*[:=#]?\s*(\d{1,3})$", token, flags=re.IGNORECASE)
        if m_sens:
            sid = int(m_sens.group(1))
            if sid in repo.wialon_sensors_by_id:
                resolved[token] = {
                    "type": "WIALON_TR84_SENSOR",
                    "sensor": repo.wialon_sensors_by_id[sid],
                }
                continue

        # Direct numeric PID or range (e.g. "46100..46240")
        m_range = re.match(r"^(\d{2,6})\s*(?:\.\.|-)\s*(\d{2,6})$", token)
        if m_range:
            start_p, end_p = int(m_range.group(1)), int(m_range.group(2))
            pids = [p for p in range(start_p, min(end_p + 1, start_p + 25)) if p in repo.all_valid_pids]
            resolved[token] = [repo.reconcile_parameter(p) for p in pids]
            continue

        # Explicit avl_id:<N> or io_<N>
        m_avl = re.match(r"^(?:avl_id|avl|io)\s*[:=_#]?\s*(\d{1,5})$", token, flags=re.IGNORECASE)
        if m_avl:
            aid = int(m_avl.group(1))
            if aid in repo.flespi_wialon_by_avl:
                resolved[token] = {
                    "type": "AVL_ID",
                    "avl_id": aid,
                    "telematics_mapping": repo.flespi_wialon_by_avl[aid],
                }
                continue

        clean_num = re.sub(r"^(?:pid|cfg_pid|cfg_ioblock|param|ioid)\s*[:=#]?\s*", "", token, flags=re.IGNORECASE)
        if clean_num.isdigit():
            num_val = int(clean_num)
            both_views: Dict[str, Any] = {}
            if num_val in repo.all_valid_pids:
                both_views["as_configuration_pid"] = repo.reconcile_parameter(num_val)
            if num_val in repo.flespi_wialon_by_avl:
                both_views["as_telemetry_avl_id"] = repo.flespi_wialon_by_avl[num_val]
            if both_views:
                if (
                    "as_configuration_pid" in both_views
                    and "as_telemetry_avl_id" in both_views
                    and num_val in repo.cfg_pid_avl_collisions
                ):
                    both_views["collision_warning"] = (
                        f"Integer {num_val} exists as BOTH a .cfg Configuration PID AND a Codec 8E Telemetry AVL ID "
                        "with completely different meanings. Never confuse these two domains."
                    )
                resolved[token] = both_views
                continue

        # Check Flespi / Wialon key table
        if token.lower() in repo.flespi_wialon_by_key:
            resolved[token] = {
                "type": "TELEMATICS_KEY",
                "key": token,
                "mapping": repo.flespi_wialon_by_key[token.lower()],
            }
            continue

        # Fallback: search parameter names in XML, schema.json, and Wialon TR84 sensors
        matches = []
        t_low = token.lower()
        for pid in sorted(repo.all_valid_pids):
            xname = repo.xml_params.get(pid, {}).get("name", "")
            sname = repo.schema_params.get(str(pid), {}).get("name", "")
            if t_low in xname.lower() or t_low in sname.lower():
                matches.append(repo.reconcile_parameter(pid))
                if len(matches) >= 8:
                    break
        sensor_matches = [
            s for s in repo.wialon_tr84_sensors
            if t_low in (s.get("name") or "").lower() or t_low in (s.get("parameter_expression") or "").lower()
        ][:5]
        if matches or sensor_matches:
            resolved[token] = {
                "matching_configuration_pids": matches,
                "matching_wialon_sensors": sensor_matches,
            }
        else:
            resolved[token] = {"status": "NOT_FOUND_IN_SCHEMA", "identifier": token}

    return {"resolved_count": len(resolved), "results": resolved}


@mcp.tool()
def mcp_search_all_knowledge(
    query: str,
    domains: Optional[List[str]] = None,
    top_k: int = 12,
) -> Dict[str, Any]:
    """Search across all server knowledge directories (`diagnostic`, `debugging-sessions`, `flespi-parameters`, `wialon-parameters`, `fmc650-reverse-engineered`, `teltonika-docs`) with bilingual expansion."""
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.search_all_knowledge(query=query, domains=domains, top_k=top_k)


# ============================================================================
# 2. DIAGNOSTIC PLAYBOOKS & INTERACTIVE WEIGHT/TRAILER DIAGNOSTIC TOOLS
# ============================================================================

@mcp.tool()
def mcp_query_diagnostic_playbooks(
    symptom_or_topic: str,
    include_full_playbook: bool = False,
    content_offset: int = 0,
) -> Dict[str, Any]:
    """Search diagnostic playbooks and historical sessions; optionally return a paginated page of the top matching file."""
    repo = FMC650KnowledgeRepository.get_instance()
    hits = repo.search_all_knowledge(
        query=symptom_or_topic,
        domains=["diagnostic", "debugging-sessions"],
        top_k=6,
        require_body_match=True,
    )
    results = hits.get("results", [])
    content_page = None
    if include_full_playbook and results:
        top_path = results[0]["path"]
        content_page = repo.get_full_document_section(
            doc_path=top_path,
            offset=max(0, content_offset),
            max_chars=12000,
        )

    return {
        "symptom_or_topic": symptom_or_topic,
        "matched_playbooks": results,
        "top_playbook_content_page": content_page,
        "top_playbook_full_content": content_page,
        "content_page_note": "The content field is one page; use next_offset to retrieve later pages. Matching excerpts are included in matched_playbooks.",
        "reconciled_pids": hits.get("reconciled_query_pids", {}),
    }


@mcp.tool()
def mcp_search_debugging_sessions(query: str, top_k: int = 5) -> Dict[str, Any]:
    """Search historical FMC650 debug logs and analyses, returning matching line-numbered evidence."""
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.search_debugging_sessions(query=query, top_k=top_k)


@mcp.tool()
def mcp_investigate_device_behavior(
    symptom_or_topic: str,
    identifiers: Optional[List[str]] = None,
    top_k: int = 5,
) -> Dict[str, Any]:
    """Combine diagnostic guidance, historical session evidence, and identifier/mapping context for a device symptom."""
    repo = FMC650KnowledgeRepository.get_instance()
    limit = max(1, min(int(top_k), 10))
    topic = str(symptom_or_topic).strip()

    playbooks = repo.search_all_knowledge(
        query=topic,
        domains=["diagnostic"],
        top_k=limit,
        require_body_match=True,
    )
    sessions = repo.search_debugging_sessions(query=topic, top_k=limit)

    resolved_identifiers: List[str] = []
    for identifier in identifiers or []:
        token = str(identifier).strip()
        if token and token not in resolved_identifiers:
            resolved_identifiers.append(token)
    for match in re.finditer(
        r"\b(cfg_pid|cfg_ioblock|configuration\s+pid|pid|avl_id|avl(?:\s*id)?|ioid|io\s*id|io|sensor)\s*[:=#_]?\s*(\d{1,6})\b",
        topic,
        flags=re.IGNORECASE,
    ):
        token = f"sensor:{match.group(2)}" if match.group(1).lower() == "sensor" else match.group(2)
        if token not in resolved_identifiers:
            resolved_identifiers.append(token)

    identifier_context: Dict[str, Any] = {}
    for token in resolved_identifiers:
        context: Dict[str, Any] = {}
        sensor_match = re.match(r"^sensor\s*[:=#]?\s*(\d{1,3})$", token, flags=re.IGNORECASE)
        numeric_match = re.match(
            r"^(?:(?:pid|cfg_pid|cfg_ioblock|param|avl_id|avl|ioid|io)\s*[:=#_]?\s*)?(\d{1,6})$",
            token,
            flags=re.IGNORECASE,
        )
        if sensor_match:
            sensor_id = int(sensor_match.group(1))
            sensor = repo.wialon_sensors_by_id.get(sensor_id)
            if sensor:
                context["wialon_tr84_sensor"] = sensor
        elif numeric_match:
            number = int(numeric_match.group(1))
            if number in repo.all_valid_pids:
                context["as_configuration_pid"] = repo.reconcile_parameter(number)
            if number in repo.flespi_wialon_by_pid:
                context["configuration_telematics_mapping"] = repo.flespi_wialon_by_pid[number]
            if number in repo.flespi_wialon_by_avl:
                context["as_telemetry_avl_id"] = repo.flespi_wialon_by_avl[number]
            if number in repo.cfg_pid_avl_collisions:
                context["collision_warning"] = (
                    f"{number} is present as both an in-cfg configuration PID and a telemetry AVL ID; "
                    "the namespaces have different meanings."
                )
        else:
            mapping = repo.flespi_wialon_by_key.get(token.lower())
            if mapping:
                context["mapping_by_key"] = mapping
        identifier_context[token] = context or {"status": "NO_MATCHING_IDENTIFIER_OR_MAPPING"}

    return {
        "symptom_or_topic": topic,
        "components_used": [
            "diagnostic playbook search",
            "debugging session evidence search",
            "configuration/telemetry identifier and mapping lookup",
        ],
        "evidence_scope": "Historical logs describe recorded cases and may not generalize to every device or firmware.",
        "diagnostic_playbooks": playbooks.get("results", []),
        "debugging_sessions": sessions.get("results", []),
        "identifier_context": identifier_context,
        "reconciled_query_pids": playbooks.get("reconciled_query_pids", {}),
    }


@mcp.tool()
def mcp_diagnose_weight_and_trailer_setup(
    tractor_model: str = "SINOTRUK SITRAK C7H 6x4",
    tractor_suspension: str = "steel_springs",
    trailer_ebs: str = "WABCO TEBS E",
    observed_avl_ids: Optional[List[int]] = None,
    can1_bus_mode: int = 0,
    on_incline: bool = False,
) -> Dict[str, Any]:
    """Interactive engineering diagnostic tool for Truck (`CAN1` FMS) + Trailer (`CAN2` WABCO TEBS E) weight telemetry."""
    observed = set(observed_avl_ids or [139, 13657])
    susp_low = tractor_suspension.lower()
    is_steel = any(k in susp_low for k in ("steel", "leaf", "spring", "lame", "ressort"))

    diagnosis: List[str] = []
    recommended_commands: List[str] = []

    if 139 in observed and not ({89, 90, 91, 92} & observed):
        if is_steel:
            diagnosis.append(
                "NORMAL FOR STEEL-SPRING TRACTOR: You receive AVL ID 139 (`Combined vehicle weight` / `total.vehicle.weight` from PGN 65134) "
                "because the ZF TraXon 12TX gearbox / Bosch Engine ECU calculates total combination mass dynamically from torque & acceleration (or sums trailer EBS). "
                "Individual `Axle 1..4 load` (`AVL ID 89..92` from PGN 65258) are absent because steel leaf springs have no per-axle pressure transducers."
            )
        else:
            diagnosis.append(
                "ECAS AIR-SUSPENSION TRACTOR WITH LOCKED FMS / SILENT CAN1: `AVL ID 139` (`PGN 65134`) is a 1-second cyclic broadcast (received even when "
                f"`CAN1 Bus Mode PID 206 = {can1_bus_mode}`), whereas individual `Axle 1..4 load` (`AVL ID 89..92`, `PGN 65258`) is an ON-REQUEST message "
                "requiring the FMC650 to transmit J1939 Request `PGN 59904` (`0xEA00`)."
            )
            if can1_bus_mode == 0:
                recommended_commands.append("setparam 206:1  # Switch CAN1 Bus Mode from Silent (0) to Normal (1) so FMC650 can transmit PGN 59904 requests")
                recommended_commands.append("scanfms         # Scan active FMS elements on CAN1 with engine running")

    if 13657 in observed:
        diagnosis.append(
            "WABCO TEBS E BOGIE SUM ACTIVE ON CAN2 (`AVL ID 13657` / `trailer.axle.load.sum`): All 6 airbags of the 3-axle trailer bogie "
            "share a single pneumatic levelling circuit connected to Port 42 of the WABCO TEBS E modulator, broadcasting one combined bogie weight."
        )
    else:
        diagnosis.append(
            "MISSING WABCO TEBS E BOGIE WEIGHT (`AVL ID 13657`): Verify ISO 7638 7-pin cable connection to CAN2 (Pin 16 = CAN2H, Pin 6 = CAN2L), "
            "`PID 330 = 2` (TrailerCAN Source = CAN2), `PID 207 = 250` or `500` kbps, and `IoId 103060 = 1` (Axle Load Sum Priority = Low)."
        )
        recommended_commands.append("setparam 330:2;103060:1;103061:3")

    if on_incline:
        diagnosis.append(
            "INCLINE / SLOPE PROTECTION: WABCO TEBS E does not pitch-correct static weight; locking the spring parking brake (`AVL ID 13809 = 1`) on a slope "
            "causes trailing-arm brake-bind, making the mechanical height-levelling valve over-inflate or vent air (+/- 1,500 to 3,500 kg distortion). "
            "Rely on Flespi `fleet_weight_stable` (Sensor 129) and `fleet_trailer_axle_stable` (Sensor 98/139), check FMC650 3-axis accelerometer (`AVL ID 17, 18, 19`), "
            "and release brakes for 3 seconds on level ground before taking a static reading."
        )

    return {
        "tractor_model": tractor_model,
        "tractor_suspension": tractor_suspension,
        "trailer_ebs": trailer_ebs,
        "observed_avl_ids": sorted(observed),
        "can1_bus_mode": "Silent (0)" if can1_bus_mode == 0 else "Normal (1)",
        "engineering_diagnosis": diagnosis,
        "recommended_commands": recommended_commands,
        "key_parameters_reference": {
            "CAN1_Gross_Combination_Weight": {"io_id": 46530, "avl_id": 139, "flespi": "total.vehicle.weight", "wialon_sensor": 21},
            "CAN1_Axle_1_to_4_Weights": {"io_ids": [46100, 46110, 46120, 46130], "avl_ids": [89, 90, 91, 92], "flespi": "can.axle.weight.1..4"},
            "CAN2_Trailer_Axle_Load_Sum": {"io_id": 103060, "avl_id": 13657, "flespi": "trailer.axle.load.sum", "wialon_sensor": 71},
            "CAN2_Trailer_Pneumatic_Pressure": {"io_id": 104590, "avl_id": 13810, "flespi": "trailer.pneumatic.supply.pressure", "wialon_sensor": 62},
            "Flespi_Stabilized_Weights": ["fleet_weight_stable (Sensor 129)", "fleet_trailer_axle_stable (Sensor 98/139)", "fleet_cargo_weight_net (Sensor 104)"],
        },
        "reference_playbooks": [
            "diagnostic/03_SITRAK_C7H_3Axle_Models_and_Why_TrailerCAN_Is_Required.md",
            "diagnostic/04_WABCO_TEBS_E_Bogie_Physics_and_Trailer_Parameters.md",
            "diagnostic/05_Incline_Slope_Uneven_Load_and_WABCO_Calibration.md",
            "diagnostic/06_FMS_Axle_Weight_Troubleshooting_and_CAN_Bus_Modes.md",
        ],
    }


# ============================================================================
# 3. TELEMATICS MAPPING, WIALON TR84 SENSORS & COMMAND GENERATION TOOLS
# ============================================================================

@mcp.tool()
def mcp_lookup_telematics_mapping(pids_or_avl_ids: List[str]) -> Dict[str, Any]:
    """Lookup Flespi parameter keys, Wialon Path A (Stream) & Path B (Direct io_*) keys, and Wialon TR84 sensors for PIDs, AVL IDs, or key names."""
    repo = FMC650KnowledgeRepository.get_instance()
    mappings: Dict[str, Any] = {}

    for raw in pids_or_avl_ids:
        tok = str(raw).strip()
        if tok.isdigit():
            num = int(tok)
            entry: Dict[str, Any] = {}
            if num in repo.flespi_wialon_by_pid:
                entry["by_configuration_pid"] = repo.flespi_wialon_by_pid[num]
            if num in repo.flespi_wialon_by_avl:
                entry["by_telemetry_avl_id"] = repo.flespi_wialon_by_avl[num]
            if entry:
                mappings[tok] = entry
                continue
        if tok.lower() in repo.flespi_wialon_by_key:
            mappings[tok] = repo.flespi_wialon_by_key[tok.lower()]
            continue
        search_res = repo.search_all_knowledge(
            query=tok,
            domains=["diagnostic", "flespi-parameters", "wialon-parameters", "fmc650-reverse-engineered"],
            top_k=3,
        )
        mappings[tok] = search_res.get("results", [])

    return {"mappings": mappings}


@mcp.tool()
def mcp_inspect_wialon_profile(
    sensor_query_or_id: Optional[str] = None,
    category: Optional[str] = None,
) -> Dict[str, Any]:
    """Inspect the 146 Wialon Unit Sensors in `wialon-parameters/FMC650_TEST_TR84_UNIT_PROFILE.json` by ID, name, parameter key (`fleet_*`, `trailer_*`, `can_*`), or category."""
    repo = FMC650KnowledgeRepository.get_instance()
    sensors = repo.wialon_tr84_sensors

    if sensor_query_or_id:
        q = sensor_query_or_id.strip()
        if q.isdigit() and int(q) in repo.wialon_sensors_by_id:
            return {
                "total_profile_sensors": len(sensors),
                "matched_count": 1,
                "sensors": [repo.wialon_sensors_by_id[int(q)]],
            }
        q_low = q.lower()
        sensors = [
            s for s in sensors
            if q_low in str(s.get("name", "")).lower()
            or q_low in str(s.get("description", "")).lower()
            or q_low in str(s.get("parameter_expression", "")).lower()
        ]

    if category:
        cat_low = category.lower().strip()
        cat_keywords = {
            "weight": ["weight", "poids", "charge", "axle", "essieu", "fleet_", "vhc_"],
            "trailer": ["trailer", "remorque", "ebs", "rop", "pneumatic"],
            "fleet": ["fleet_", "vhc_"],
            "tidj": ["fleet_", "vhc_"],
            "fuel": ["fuel", "carburant", "adblue"],
            "engine": ["eng", "moteur", "rpm", "coolant", "oil"],
            "accelerometer": ["accel", "inclinaison", "pitch", "roll"],
            "tachograph": ["tco", "tacho", "driver", "conducteur"],
        }.get(cat_low, [cat_low])
        sensors = [
            s for s in sensors
            if any(
                kw in str(s.get("name", "")).lower()
                or kw in str(s.get("description", "")).lower()
                or kw in str(s.get("parameter_expression", "")).lower()
                for kw in cat_keywords
            )
        ]

    return {
        "profile_file": "wialon-parameters/FMC650_TEST_TR84_UNIT_PROFILE.json",
        "total_profile_sensors": len(repo.wialon_tr84_sensors),
        "matched_count": len(sensors),
        "sensors": sensors[:60],
    }


@mcp.tool()
def mcp_generate_flespi_and_sms_commands(
    action: str,
    custom_pids: Optional[Dict[int, str]] = None,
) -> Dict[str, Any]:
    """Generate validated Teltonika SMS / GPRS Codec 12 / Flespi `setparam`, `getparam`, `scanfms`, and CAN debug commands."""
    repo = FMC650KnowledgeRepository.get_instance()
    act_low = action.lower().strip()

    presets: Dict[str, Dict[str, Any]] = {
        "enable_normal_can1": {
            "description": "Switch CAN1 Bus Mode (PID 206) from Silent (0) to Normal (1) so FMC650 can send J1939 Request PGN 59904 for Locked FMS Axle Weights (PGN 65258).",
            "pids": {205: "500", 206: "1", 210: "0"},
            "extra_commands": ["scanfms"],
        },
        "enable_silent_can1": {
            "description": "Switch CAN1 Bus Mode (PID 206) to Silent (0) for passive, zero-disturbance listening.",
            "pids": {205: "500", 206: "0", 210: "0"},
            "extra_commands": [],
        },
        "debug_zero_can_values": {
            "description": "Temporarily enable IO Send Mode = Send Zero (PID 221 = 1) to verify whether the truck sends 0/65535 vs no PGN at all.",
            "pids": {221: "1"},
            "extra_commands": ["setparam 221:0  # Run after testing to restore Don't Send mode"],
        },
        "capture_can_log": {
            "description": "Enable CAN bus debug logging on FMC650 terminal or remote log2srv server.",
            "pids": {},
            "extra_commands": [
                ".can_dbg:1",
                ".can_dbg_filter:1",
                "# Wait 30 seconds with Engine ON, then disable:",
                ".can_dbg:0",
            ],
        },
        "configure_sitrak_wabco_p2": {
            "description": "Core CAN1 (Sitrak 500 kbps FMS) + CAN2 (WABCO TEBS E TrailerCAN) weight & pneumatic telemetry settings from P2_PRODUCTION_v1.2.",
            "pids": {
                205: "500",
                206: "0",
                207: "500",
                208: "0",
                210: "0",
                330: "2",
                46530: "2",
                46100: "1",
                46110: "1",
                46120: "1",
                46130: "1",
                103000: "1",
                103060: "1",
                103110: "1",
                103120: "1",
                103130: "1",
                103200: "1",
                104230: "1",
                104590: "1",
            },
            "extra_commands": [],
        },
    }

    selected = presets.get(act_low)
    edits: Dict[int, str] = {}
    if selected:
        edits.update({int(k): str(v) for k, v in selected["pids"].items()})
    if custom_pids:
        edits.update({int(k): str(v) for k, v in custom_pids.items()})

    validation = None
    setparam_cmd = None
    getparam_cmd = None
    if edits:
        validation = repo.cfg_engine.validate_edits(
            base_profile="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
            proposed_edits=edits,
        )
        pairs = ";".join(f"{k}:{v}" for k, v in edits.items())
        ids_only = ";".join(str(k) for k in edits.keys())
        setparam_cmd = f"setparam {pairs}"
        getparam_cmd = f"getparam {ids_only}"

    return {
        "action": action,
        "available_presets": list(presets.keys()),
        "description": selected["description"] if selected else "Custom PID command generation",
        "setparam_command": setparam_cmd,
        "getparam_command": getparam_cmd,
        "extra_commands": selected["extra_commands"] if selected else ["scanfms"],
        "xml_validation_report": validation,
    }


# ============================================================================
# 4. .CFG PROFILE INSPECTION, DIFFING, VALIDATION & COMPILATION TOOLS
# ============================================================================

@mcp.tool()
def mcp_inspect_cfg_profile(
    profile_name_or_path: str = "FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
    pids: Optional[List[int]] = None,
    filter_non_default: bool = False,
) -> Dict[str, Any]:
    """Inspect a .cfg profile using cfg_tool.py with secret blinding, XML enum decoding, and factory diffs."""
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.cfg_engine.inspect_profile(
        profile_name_or_path=profile_name_or_path,
        pids=pids,
        filter_non_default=filter_non_default,
    )


@mcp.tool()
def mcp_diff_cfg_profiles(
    profile_a: str = "device_export_original.cfg",
    profile_b: str = "FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
) -> Dict[str, Any]:
    """Compare any two .cfg profiles and return all modified parameters with decoded XML enums."""
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.cfg_engine.diff_profiles(profile_a=profile_a, profile_b=profile_b)


@mcp.tool()
def mcp_validate_and_compile_cfg(
    base_profile: str,
    proposed_edits: Dict[int, str],
    output_filename: Optional[str] = None,
) -> Dict[str, Any]:
    """Validate proposed PID=Value edits via make_cfg.py and optionally compile a gzipped .cfg file."""
    repo = FMC650KnowledgeRepository.get_instance()
    int_edits = {int(k): str(v) for k, v in proposed_edits.items()}
    val_report = repo.cfg_engine.validate_edits(base_profile=base_profile, proposed_edits=int_edits)
    artifact = repo.cfg_engine.create_cfg(
        base_profile=base_profile,
        proposed_edits=int_edits,
        output_filename=output_filename,
    )
    return {
        "validation_report": val_report,
        "compiled_artifact": artifact.model_dump(mode="json"),
    }


@mcp.tool()
def mcp_list_io_block_siblings(
    io_block_or_pid: int,
    profile_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Return all sibling parameters of an IO block (`+0 Priority`..`+5 Avg`) with XML constraints and current .cfg values."""
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.list_io_block_siblings(io_block_or_pid=io_block_or_pid, profile_name=profile_name)


# ============================================================================
# 5. KNOWLEDGE GRAPH, DOCUMENT READER, FIRMWARE HISTORY & MERMAID TOOLS
# ============================================================================

@mcp.tool()
def mcp_query_knowledge_graph(concepts: List[str], max_hops: int = 2) -> Dict[str, Any]:
    """Traverse graph neighborhoods and return edge provenance for every assertion."""
    repo = FMC650KnowledgeRepository.get_instance()
    matched_nodes: List[Dict[str, Any]] = []
    edges_out: List[Dict[str, Any]] = []
    hop_limit = max(1, min(int(max_hops), 5))
    max_matched_nodes = 35
    max_edges = 60

    lower_concepts = [c.lower().strip() for c in concepts if c.strip()]
    graphs = (("graph_v3", repo.graph_v3), ("graph_v1", repo.graph_v1))
    node_candidates = []
    total_matched_nodes = 0
    matched_nodes_by_graph = {label: 0 for label, _ in graphs}
    for G_label, G in graphs:
        for node_id, ndata in G.nodes(data=True):
            n_str = f"{node_id} {ndata.get('name', '')} {ndata.get('canonical_name', '')}".lower()
            if any(c in n_str for c in lower_concepts):
                total_matched_nodes += 1
                matched_nodes_by_graph[G_label] += 1
                if len(node_candidates) < max_matched_nodes:
                    node_candidates.append((G_label, G, node_id, ndata))

    edges_truncated = False
    seen_edges_by_graph = {label: set() for label, _ in graphs}
    for G_label, G, node_id, ndata in node_candidates:
        seen_edges = seen_edges_by_graph[G_label]
        matched_nodes.append({
            "graph": G_label,
            "node_id": str(node_id),
            "type": ndata.get("type") or ndata.get("node_type"),
            "name": ndata.get("canonical_name") or ndata.get("name") or str(node_id),
        })
        visited = {node_id}
        frontier = [(node_id, 0)]
        while frontier:
            current, depth = frontier.pop(0)
            if depth >= hop_limit:
                continue
            incident_edges = [
                (current, tgt, tgt, edata)
                for _, tgt, edata in G.out_edges(current, data=True)
            ] + [
                (src, current, src, edata)
                for src, _, edata in G.in_edges(current, data=True)
            ]
            for edge_src, edge_tgt, neighbor, edata in incident_edges:
                relation = str(edata.get("relation") or edata.get("label") or "CONNECTED_TO")
                edge_identity = (
                    edge_src, edge_tgt, relation,
                    edata.get("source_file"), edata.get("source_location"),
                    edata.get("rationale") or edata.get("notes"),
                    edata.get("conditions"), edata.get("confidence"),
                    edata.get("confidence_score"), edata.get("verification_status"),
                )
                if edge_identity in seen_edges:
                    continue
                if len(edges_out) >= max_edges:
                    edges_truncated = True
                    break
                seen_edges.add(edge_identity)
                edges_out.append({
                    "graph": G_label,
                    "source": str(edge_src),
                    "relation": relation,
                    "target": str(edge_tgt),
                    "hop": depth + 1,
                    "confidence": edata.get("confidence"),
                    "confidence_score": edata.get("confidence_score"),
                    "source_file": edata.get("source_file"),
                    "source_location": edata.get("source_location"),
                    "rationale": edata.get("rationale") or edata.get("notes"),
                    "conditions": edata.get("conditions"),
                    "verification_status": edata.get("verification_status"),
                    "also_seen": edata.get("also_seen", []),
                    "legacy_provenance": edata.get("legacy_provenance"),
                })
                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.append((neighbor, depth + 1))
            if edges_truncated:
                break
        if edges_truncated:
            break

    return {
        "concepts": concepts,
        "max_hops": hop_limit,
        "retired_assertions_excluded": {
            "graph_v3": len(repo.graph_v3.graph.get("retired_assertions", [])),
            "graph_v1": len(repo.graph_v1.graph.get("retired_assertions", [])),
        },
        "total_matched_nodes": total_matched_nodes,
        "matched_nodes_by_graph": matched_nodes_by_graph,
        "matched_nodes_truncated": total_matched_nodes > len(matched_nodes),
        "edge_neighborhoods_truncated": total_matched_nodes > len(node_candidates),
        "max_matched_nodes": max_matched_nodes,
        "max_edges": max_edges,
        "edges_truncated": edges_truncated,
        "matched_nodes": matched_nodes,
        "edges": edges_out,
    }


@mcp.tool()
def mcp_get_full_document_section(
    doc_path: str,
    heading_or_line_range: Optional[str] = None,
    offset: int = 0,
    max_chars: int = 12000,
) -> Dict[str, Any]:
    """Read sections and Markdown tables of any file in `FMC650 MCP Server/` with safe pagination (max_chars<=12000)."""
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.get_full_document_section(
        doc_path=doc_path,
        heading_or_line_range=heading_or_line_range,
        offset=offset,
        max_chars=max_chars,
    )


@mcp.tool()
def mcp_search_firmware_and_pcn_history(query: str) -> Dict[str, Any]:
    """Search `teltonika-docs/Firmware_Changelog`, `teltonika-docs/Product_Change_Notifications`, and `fmc650-reverse-engineered`."""
    repo = FMC650KnowledgeRepository.get_instance()
    doc_hits = repo.search_all_knowledge(
        query=query,
        domains=["Firmware_Changelog", "Product_Change_Notifications", "fmc650-reverse-engineered"],
        top_k=8,
    )
    return {
        "query": query,
        "documentation_hits": doc_hits.get("results", []),
    }


@mcp.tool()
def mcp_verify_mermaid_diagram(mermaid_code: str) -> Dict[str, Any]:
    """Validate and auto-repair a Mermaid diagram string."""
    is_valid, repaired, notes = validate_and_repair_mermaid(mermaid_code)
    return {
        "is_valid": is_valid,
        "repaired_code": repaired,
        "notes": notes,
    }


# ============================================================================
# 6. MCP RESOURCES (6 COMPREHENSIVE RESOURCES)
# ============================================================================

@mcp.resource("fmc650://schema/summary")
def resource_schema_summary() -> str:
    repo = FMC650KnowledgeRepository.get_instance()
    return json.dumps({
        "server": "fmc650-comprehensive-mcp",
        "version": "alfa-0.1",
        "xml_collections_count": len(repo.collections),
        "xml_params_count": len(repo.xml_params),
        "schema_json_params_count": len(repo.schema_params),
        "total_valid_pids": len(repo.all_valid_pids),
        "indexed_avl_ids_count": len(repo.flespi_wialon_by_avl),
        "indexed_telematics_keys_count": len(repo.flespi_wialon_by_key),
        "wialon_tr84_sensors_count": len(repo.wialon_tr84_sensors),
        "graph_v3_nodes": repo.graph_v3.number_of_nodes(),
        "graph_v1_nodes": repo.graph_v1.number_of_nodes(),
        "total_indexed_documents": len(repo.doc_files),
    }, indent=2)


@mcp.resource("fmc650://profiles/list")
def resource_profiles_list() -> str:
    repo = FMC650KnowledgeRepository.get_instance()
    return json.dumps(repo.cfg_engine.list_profiles(), indent=2)


@mcp.resource("fmc650://corpus/manifest")
def resource_corpus_manifest() -> str:
    repo = FMC650KnowledgeRepository.get_instance()
    return json.dumps({
        "directories": ALL_KNOWLEDGE_DIRS,
        "total_indexed_files": len(repo.doc_files),
        "diagnostic_files": [
            str(p.relative_to(repo.knowledge_root)).replace("\\", "/")
            for p in repo.doc_files
            if str(p.relative_to(repo.knowledge_root)).replace("\\", "/").startswith("diagnostic/")
        ],
        "sample_files": [str(p.relative_to(repo.knowledge_root)).replace("\\", "/") for p in repo.doc_files[:60]],
    }, indent=2)


@mcp.resource("fmc650://diagnostic/index")
def resource_diagnostic_index() -> str:
    repo = FMC650KnowledgeRepository.get_instance()
    sec = repo.get_full_document_section("diagnostic/00_README_Diagnostic_Index.md", max_chars=12000)
    return json.dumps(sec, indent=2)


@mcp.resource("fmc650://telematics/weight-and-trailer-catalog")
def resource_weight_and_trailer_catalog() -> str:
    repo = FMC650KnowledgeRepository.get_instance()
    sec = repo.get_full_document_section("diagnostic/02_Real_World_Weight_and_Trailer_IDs_Reference.md", max_chars=12000)
    return json.dumps(sec, indent=2)


@mcp.resource("fmc650://telematics/mappings")
def resource_telematics_mappings() -> str:
    """Return configuration, telemetry, Flespi, Wialon, and sensor mapping indexes."""
    repo = FMC650KnowledgeRepository.get_instance()
    return json.dumps({
        "scope": [
            "Configuration PIDs and IO blocks",
            "Telemetry AVL IDs",
            "Flespi parameters",
            "Wialon stream and direct IO keys",
            "Wialon TR84 unit sensors",
        ],
        "counts": {
            "configuration_pid_mappings": len(repo.flespi_wialon_by_pid),
            "telemetry_avl_mappings": len(repo.flespi_wialon_by_avl),
            "flespi_and_wialon_key_aliases": len(repo.flespi_wialon_by_key),
            "wialon_tr84_sensors": len(repo.wialon_tr84_sensors),
        },
        "by_configuration_pid": repo.flespi_wialon_by_pid,
        "by_telemetry_avl_id": repo.flespi_wialon_by_avl,
        "by_flespi_or_wialon_key": repo.flespi_wialon_by_key,
        "wialon_tr84_sensors": repo.wialon_tr84_sensors,
    }, indent=2, ensure_ascii=False)


# ============================================================================
# 7. MCP PROMPTS (4 GUIDED ENGINEERING WORKFLOW PROMPTS)
# ============================================================================

@mcp.prompt()
def prompt_diagnose_fms_or_trailer_weight(
    tractor_model: str = "SINOTRUK SITRAK C7H 6x4",
    symptom: str = "Receives Combined vehicle weight (AVL ID 139) only, Axle 1..4 (AVL ID 89..92) missing",
) -> str:
    """Guided engineering prompt to diagnose Truck FMS (`CAN1`) and WABCO TEBS E (`CAN2`) weight telemetry issues."""
    return (
        f"Diagnose the following Teltonika FMC650 weight telemetry symptom on `{tractor_model}`:\n"
        f"Symptom: {symptom}\n\n"
        "Steps to execute:\n"
        "1. Call `mcp_investigate_device_behavior` with the symptom and any known PIDs or AVL IDs to combine playbooks, historical log evidence, and mapping context.\n"
        "2. Call `mcp_diagnose_weight_and_trailer_setup` for the vehicle-specific FMS/TrailerCAN interpretation.\n"
        "3. Explain the difference between `PGN 65134` (`AVL ID 139`, cyclic broadcast from ZF TraXon / EBS) "
        "and `PGN 65258` (`AVL ID 89..103`, On-Request from ECAS air suspension).\n"
        "4. Check whether `CAN1 Bus Mode` (`PID 206`) is `Silent (0)` vs `Normal (1)` and whether the tractor has steel leaf springs or ECAS airbags.\n"
        "5. Provide the exact `setparam` / `scanfms` diagnostic commands using `mcp_generate_flespi_and_sms_commands`."
    )


@mcp.prompt()
def prompt_audit_cfg_profile(
    profile_name: str = "FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
) -> str:
    """Guided prompt to audit an FMC650 `.cfg` configuration profile against Fleet Telematics P2 production standards."""
    return (
        f"Audit the FMC650 configuration profile `{profile_name}`:\n"
        "1. Call `mcp_inspect_cfg_profile` and `mcp_diff_cfg_profiles` against `device_export_original.cfg`.\n"
        "2. Verify network/queue settings (`PID 1000=120`, `PID 1001=5`, `PID 1002=1`, `PID 1006=0`).\n"
        "3. Verify CAN1 (`PID 205, 206, 210`) and CAN2 TrailerCAN (`PID 207, 208, 330`) settings.\n"
        "4. Verify FMS Weight (`IoId 46530, 46100..46130`) and WABCO TEBS E (`IoId 103000..104590`) priorities."
    )


@mcp.prompt()
def prompt_map_flespi_wialon_sensor(identifier: str = "13657") -> str:
    """Guided prompt to trace any Teltonika `.cfg` IoId, Codec 8E AVL ID, Flespi parameter, or Wialon sensor end-to-end."""
    return (
        f"Trace identifier `{identifier}` end-to-end across all 4 telematics domains:\n"
        "1. Call `mcp_resolve_identifiers` and `mcp_lookup_telematics_mapping`.\n"
        "2. Call `mcp_inspect_wialon_profile` to retrieve matching Wialon `TR84` sensors and `fleet_*` plugin outputs.\n"
        "3. Present the `.cfg` `IoId` block, Codec 8E `AVL ID`, Flespi parameter name, Wialon Path A (`Flespi Stream`) key, "
        "Wialon Path B (`Direct io_*`) key, and Wialon Sensor number."
    )


@mcp.prompt()
def prompt_explain_incline_and_calibration() -> str:
    """Guided prompt explaining incline/slope weight behavior, brake-bind on levelling valves, uneven cargo loading, and WABCO calibration."""
    return (
        "Explain how WABCO TEBS E, the FMC650, and the Flespi `fleet_*` plugin handle incline/slope and uneven cargo loading:\n"
        "1. Call `mcp_query_diagnostic_playbooks` with `'incline slope calibration brake-bind'`.\n"
        "2. Explain center-of-gravity transfer (`Kingpin <-> Trailer Bogie`) and trailing-arm `Brake-Bind` on the mechanical height-levelling valve when `AVL ID 13809` (Spring Brake) is locked on a hill.\n"
        "3. Show how `AVL ID 17, 18, 19` (3-axis accelerometer), `AVL ID 139` (`CAN1 + CAN2` sum), and `fleet_weight_stable` / `fleet_trailer_axle_stable` prevent false alarms.\n"
        "4. Explain WABCO 2-point calibration and online external scale calibration (`AVL ID 13663` & `13664`)."
    )


def resource_wialon_tr84_sensors() -> str:
    """Return all 146 Wialon TR84 unit sensors as JSON."""
    repo = FMC650KnowledgeRepository.get_instance()
    return json.dumps({
        "unit_profile": "SINOTRUK_TR84 (wialon-parameters/FMC650_TEST_TR84_UNIT_PROFILE.json)",
        "total_sensors": len(repo.wialon_tr84_sensors),
        "sensors": repo.wialon_tr84_sensors,
    }, indent=2, ensure_ascii=False)


def main() -> None:
    import argparse
    import os
    import uvicorn

    parser = argparse.ArgumentParser(
        description="Comprehensive FMC650 MCP & Web Diagnostic Server (alfa-0.1)"
    )
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http", "web"],
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
        help="Transport mode: 'stdio' (default MCP), 'sse', 'streamable-http', or 'web' (FastAPI Explorer + REST API).",
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Shortcut for --transport web (starts the FastAPI Browser Explorer & REST Server).",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "0.0.0.0"),
        help="Bind host for HTTP/SSE/Web server (default: 0.0.0.0).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "8065")),
        help="Bind port for HTTP/SSE/Web server (default: 8065 or $PORT).",
    )
    args = parser.parse_args()

    mode = "web" if args.web else args.transport
    if mode == "web":
        uvicorn.run("fmc650_mcp_server.api:app", host=args.host, port=args.port)
    elif mode in ("sse", "streamable-http"):
        mcp.settings.host = args.host
        mcp.settings.port = args.port
        mcp.run(transport=mode)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
