"""FastAPI Browser & HTTP Server for the Comprehensive FMC650 MCP Server (`fmc650-comprehensive-mcp`).

Exposes:
- `/` and `/explorer` — Interactive Browser Dashboard & MCP Tool/Resource/Playbook Playground
- `/docs` — Interactive Swagger UI (Try-it-out for all 15 MCP Tools & REST endpoints)
- `/redoc` — ReDoc API Documentation
- `/workbench` — React Workbench UI
- `/health` — Server & Repository health summary
- `/mcp/tools` — Catalog of all 15 MCP Tools, 6 Resources, and 4 Prompts
- `/mcp/resources/*` — Direct browser GET endpoints for all 6 MCP Resources
- `/mcp/playbooks` & `/mcp/playbooks/{playbook_id}` — Direct browser viewers for the 7 Diagnostic Playbooks (`00`..`06`)
- `/mcp/resolve` — GET/POST Identifier Resolution (`PID`, `IoId`, `AVL ID`, Flespi key, Wialon key, Sensor ID)
- `/mcp/search` — GET/POST Full-corpus bilingual search
- `/mcp/diagnose-weight` — GET/POST Interactive Sitrak + WABCO TEBS E weight setup diagnostic engine
- `/mcp/telematics` — GET/POST Flespi & Wialon Path A/B mapping lookup
- `/mcp/wialon-sensors` — GET/POST Wialon TR84 146-Sensor explorer
- `/mcp/commands` — GET/POST XML-validated Flespi/SMS `setparam` & `scanfms` command generator
- `/cfg/profiles`, `/cfg/inspect`, `/cfg/diff`, `/cfg/validate`, `/cfg/create`, `/cfg/download/{filename}`
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from fmc650_mcp_server import server as mcp_srv, session_store
from fmc650_mcp_server.cfg_creator import GENERATED_CFGS_DIR
from fmc650_mcp_server.repository import ALL_KNOWLEDGE_DIRS, FMC650KnowledgeRepository

app = FastAPI(
    title="Comprehensive FMC650 MCP Server (Browser & API Explorer)",
    version="alfa-0.1",
    description=(
        "Interactive Browser Explorer & REST Gateway for `fmc650-comprehensive-mcp` — "
        "15 MCP Tools, 6 MCP Resources, 4 MCP Prompts, 7 Diagnostic Playbooks, "
        "11,688 Compiler XML/Schema Parameters, 146 Wialon TR84 Sensors, and .cfg Compiler."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# 1. HEALTH & MCP CATALOG ENDPOINTS
# ============================================================================

@app.get("/health", tags=["1. Health & Catalog"])
def health_check() -> Dict[str, Any]:
    """Return full live health & index statistics of the FMC650 MCP Server."""
    repo = FMC650KnowledgeRepository.get_instance()
    return {
        "status": "ok",
        "mcp_server": "fmc650-comprehensive-mcp",
        "version": "alfa-0.1",
        "knowledge_directories": ALL_KNOWLEDGE_DIRS,
        "indexed_doc_files": len(repo.doc_files),
        "diagnostic_playbooks_count": 7,
        "xml_collections_count": len(repo.collections),
        "xml_parameters_count": len(repo.xml_params),
        "schema_json_parameters_count": len(repo.schema_params),
        "total_valid_pids": len(repo.all_valid_pids),
        "indexed_avl_ids_count": len(repo.flespi_wialon_by_avl),
        "indexed_telematics_keys_count": len(repo.flespi_wialon_by_key),
        "wialon_tr84_sensors_count": len(repo.wialon_tr84_sensors),
        "graph_v3_nodes": repo.graph_v3.number_of_nodes(),
        "graph_v1_nodes": repo.graph_v1.number_of_nodes(),
        "available_cfg_profiles": len(repo.cfg_engine.list_profiles()),
    }


@app.get("/mcp/tools", tags=["1. Health & Catalog"])
def list_mcp_tools_resources_prompts() -> Dict[str, Any]:
    """List all 15 MCP Tools, 6 MCP Resources, and 4 MCP Prompts exposed by `fmc650-comprehensive-mcp`."""
    tool_names = [
        name for name in dir(mcp_srv)
        if name.startswith("mcp_") and callable(getattr(mcp_srv, name))
    ]
    prompt_names = [
        name for name in dir(mcp_srv)
        if name.startswith("prompt_") and callable(getattr(mcp_srv, name))
    ]
    return {
        "server": "fmc650-comprehensive-mcp",
        "version": "alfa-0.1",
        "tools_count": len(tool_names),
        "tools": [
            {
                "name": t,
                "description": (getattr(mcp_srv, t).__doc__ or "").strip(),
            }
            for t in tool_names
        ],
        "resources_count": 6,
        "resources": [
            {"uri": "fmc650://schema/summary", "http_url": "/mcp/resources/schema-summary"},
            {"uri": "fmc650://profiles/list", "http_url": "/mcp/resources/profiles-list"},
            {"uri": "fmc650://corpus/manifest", "http_url": "/mcp/resources/corpus-manifest"},
            {"uri": "fmc650://diagnostic/index", "http_url": "/mcp/resources/diagnostic-index"},
            {"uri": "fmc650://telematics/weight-and-trailer-catalog", "http_url": "/mcp/resources/weight-and-trailer-catalog"},
            {"uri": "fmc650://wialon/tr84-sensors", "http_url": "/mcp/resources/wialon-tr84-sensors"},
        ],
        "prompts_count": len(prompt_names),
        "prompts": [
            {
                "name": p,
                "description": (getattr(mcp_srv, p).__doc__ or "").strip(),
                "preview": getattr(mcp_srv, p)(),
            }
            for p in prompt_names
        ],
    }


# ============================================================================
# 2. MCP RESOURCES (DIRECT BROWSER GET ENDPOINTS)
# ============================================================================

@app.get("/mcp/resources/schema-summary", tags=["2. MCP Resources"])
def get_resource_schema_summary() -> Dict[str, Any]:
    return json.loads(mcp_srv.resource_schema_summary())


@app.get("/mcp/resources/profiles-list", tags=["2. MCP Resources"])
def get_resource_profiles_list() -> Any:
    return json.loads(mcp_srv.resource_profiles_list())


@app.get("/mcp/resources/corpus-manifest", tags=["2. MCP Resources"])
def get_resource_corpus_manifest() -> Dict[str, Any]:
    return json.loads(mcp_srv.resource_corpus_manifest())


@app.get("/mcp/resources/diagnostic-index", tags=["2. MCP Resources"])
def get_resource_diagnostic_index() -> Dict[str, Any]:
    return json.loads(mcp_srv.resource_diagnostic_index())


@app.get("/mcp/resources/weight-and-trailer-catalog", tags=["2. MCP Resources"])
def get_resource_weight_and_trailer_catalog() -> Dict[str, Any]:
    return json.loads(mcp_srv.resource_weight_and_trailer_catalog())


@app.get("/mcp/resources/wialon-tr84-sensors", tags=["2. MCP Resources"])
def get_resource_wialon_tr84_sensors() -> Dict[str, Any]:
    return json.loads(mcp_srv.resource_wialon_tr84_sensors())


@app.get("/mcp/resources/telematics-mappings", tags=["2. MCP Resources"])
def get_resource_telematics_mappings() -> Dict[str, Any]:
    return json.loads(mcp_srv.resource_telematics_mappings())


# ============================================================================
# 3. DIAGNOSTIC PLAYBOOKS (00..06) BROWSER VIEWERS
# ============================================================================

PLAYBOOK_FILES = {
    "00": "diagnostic/00_README_Diagnostic_Index.md",
    "01": "diagnostic/01_CAN1_FMS_J1939_LVCAN_EV_FMS_Architecture.md",
    "02": "diagnostic/02_Real_World_Weight_and_Trailer_IDs_Reference.md",
    "03": "diagnostic/03_SITRAK_C7H_3Axle_Models_and_Why_TrailerCAN_Is_Required.md",
    "04": "diagnostic/04_WABCO_TEBS_E_Bogie_Physics_and_Trailer_Parameters.md",
    "05": "diagnostic/05_Incline_Slope_Uneven_Load_and_WABCO_Calibration.md",
    "06": "diagnostic/06_FMS_Axle_Weight_Troubleshooting_and_CAN_Bus_Modes.md",
}


@app.get("/mcp/playbooks", tags=["3. Diagnostic Playbooks"])
def list_diagnostic_playbooks(q: Optional[str] = None) -> Dict[str, Any]:
    """List all 7 subject-indexed diagnostic playbooks in `diagnostic/` or search them by symptom `q`."""
    if q and q.strip():
        return mcp_srv.mcp_query_diagnostic_playbooks(symptom_or_topic=q.strip(), include_full_playbook=True)
    return {
        "count": len(PLAYBOOK_FILES),
        "playbooks": [
            {
                "id": k,
                "path": v,
                "url": f"/mcp/playbooks/{k}",
            }
            for k, v in PLAYBOOK_FILES.items()
        ],
    }


@app.get("/mcp/playbooks/{playbook_id}", tags=["3. Diagnostic Playbooks"])
def get_diagnostic_playbook_by_id(playbook_id: str) -> Dict[str, Any]:
    """Read any of the 7 diagnostic playbooks (`00` through `06`) in full."""
    key = playbook_id.strip().zfill(2) if playbook_id.strip().isdigit() else playbook_id.strip()
    doc_path = PLAYBOOK_FILES.get(key, f"diagnostic/{playbook_id}")
    return mcp_srv.mcp_get_full_document_section(doc_path=doc_path, max_chars=12000)


# ============================================================================
# 4. INTERACTIVE MCP TOOLS (BROWSER GET + REST POST)
# ============================================================================

@app.get("/mcp/resolve", tags=["4. Interactive MCP Tools"])
def resolve_identifiers_get(
    ids: str = Query(
        default="100,139,avl_id:13657,trailer.axle.load.sum,fleet_weight_stable,sensor:71",
        description="Comma-separated list of PIDs, IoIds, AVL IDs, Flespi keys, Wialon keys, or sensor:ID",
    ),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_resolve_identifiers`."""
    tokens = [t.strip() for t in ids.split(",") if t.strip()]
    return mcp_srv.mcp_resolve_identifiers(tokens)


@app.get("/mcp/search", tags=["4. Interactive MCP Tools"])
def search_knowledge_get(
    q: str = Query(default="Gross sum axle only 139 CAN1 Bus Mode Silent", description="Search query (EN/FR)"),
    domain: Optional[str] = Query(default=None, description="Optional domain filter e.g. diagnostic, Teltonica Docs, Wilaon_param"),
    top_k: int = Query(default=10),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_search_all_knowledge`."""
    domains = [domain] if domain else None
    return mcp_srv.mcp_search_all_knowledge(query=q, domains=domains, top_k=top_k)


@app.get("/mcp/diagnose-weight", tags=["4. Interactive MCP Tools"])
def diagnose_weight_setup_get(
    tractor_model: str = Query(default="SINOTRUK SITRAK C7H 6x4"),
    tractor_suspension: str = Query(default="steel_springs", description="steel_springs or ecas_air"),
    trailer_ebs: str = Query(default="WABCO TEBS E"),
    observed_avl_ids: str = Query(default="139,13657", description="Comma-separated AVL IDs observed"),
    can1_bus_mode: int = Query(default=0, description="0 = Silent, 1 = Normal"),
    on_incline: bool = Query(default=True, description="Include incline / slope brake-bind analysis"),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_diagnose_weight_and_trailer_setup`."""
    avl_list = [int(x.strip()) for x in observed_avl_ids.split(",") if x.strip().isdigit()]
    return mcp_srv.mcp_diagnose_weight_and_trailer_setup(
        tractor_model=tractor_model,
        tractor_suspension=tractor_suspension,
        trailer_ebs=trailer_ebs,
        observed_avl_ids=avl_list,
        can1_bus_mode=can1_bus_mode,
        on_incline=on_incline,
    )


@app.get("/mcp/telematics", tags=["4. Interactive MCP Tools"])
def lookup_telematics_get(
    keys: str = Query(
        default="46530,139,103060,13657,13810,fleet_weight_stable,fleet_fraud_alert",
        description="Comma-separated PIDs, AVL IDs, Flespi keys, or Wialon keys",
    ),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_lookup_telematics_mapping`."""
    tokens = [t.strip() for t in keys.split(",") if t.strip()]
    return mcp_srv.mcp_lookup_telematics_mapping(tokens)


@app.get("/mcp/wialon-sensors", tags=["4. Interactive MCP Tools"])
def inspect_wialon_sensors_get(
    q: Optional[str] = Query(default=None, description="Sensor ID (1..146), name, or parameter key"),
    category: Optional[str] = Query(default="weight", description="weight, trailer, tidj, fuel, engine, accelerometer, tachograph"),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_inspect_wialon_profile`."""
    return mcp_srv.mcp_inspect_wialon_profile(sensor_query_or_id=q, category=category)


@app.get("/mcp/commands", tags=["4. Interactive MCP Tools"])
def generate_commands_get(
    action: str = Query(
        default="enable_normal_can1",
        description="enable_normal_can1, enable_silent_can1, debug_zero_can_values, capture_can_log, or configure_sitrak_wabco_p2",
    ),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_generate_flespi_and_sms_commands`."""
    return mcp_srv.mcp_generate_flespi_and_sms_commands(action=action)


@app.get("/mcp/io-siblings/{io_block_or_pid}", tags=["4. Interactive MCP Tools"])
def list_io_siblings_get(
    io_block_or_pid: int,
    profile_name: str = Query(default="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg"),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_list_io_block_siblings`."""
    return mcp_srv.mcp_list_io_block_siblings(io_block_or_pid=io_block_or_pid, profile_name=profile_name)


@app.get("/mcp/graph", tags=["4. Interactive MCP Tools"])
def query_graph_get(
    concepts: str = Query(default="13657,46530,139", description="Comma-separated concepts or IDs"),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_query_knowledge_graph`."""
    tokens = [c.strip() for c in concepts.split(",") if c.strip()]
    return mcp_srv.mcp_query_knowledge_graph(concepts=tokens)


@app.get("/mcp/firmware-history", tags=["4. Interactive MCP Tools"])
def search_firmware_history_get(
    q: str = Query(default="03.01.01", description="Firmware version or PCN query"),
) -> Dict[str, Any]:
    """Browser GET endpoint for `mcp_search_firmware_and_pcn_history`."""
    return mcp_srv.mcp_search_firmware_and_pcn_history(query=q)


# ============================================================================
# 5. .CFG PROFILE ENDPOINTS & WORKBENCH COMPATIBILITY ENDPOINTS
# ============================================================================

class CfgInspectRequest(BaseModel):
    profile_name_or_path: str = Field(default="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg")
    pids: Optional[List[int]] = Field(default=None)
    filter_non_default: bool = Field(default=False)


class CfgValidateOrCreateRequest(BaseModel):
    base_profile: str = Field(default="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg")
    proposed_edits: Dict[int, str] = Field(description="Map of PID -> string value to validate/compile.")
    output_filename: Optional[str] = Field(default=None, description="Filename for generated .cfg in generated_cfgs/.")


@app.get("/cfg/profiles", tags=["5. .cfg Profile Engine"])
def list_cfg_profiles() -> Dict[str, Any]:
    repo = FMC650KnowledgeRepository.get_instance()
    profiles = repo.cfg_engine.list_profiles()
    return {"count": len(profiles), "profiles": profiles}


@app.get("/cfg/inspect", tags=["5. .cfg Profile Engine"])
def inspect_cfg_profile_get(
    profile: str = Query(default="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg"),
    pids: str = Query(default="205,206,207,208,210,330,1000,1001,1002,46100,46110,46120,46130,46530,103060,104590"),
) -> Dict[str, Any]:
    pid_list = [int(x.strip()) for x in pids.split(",") if x.strip().isdigit()] if pids else None
    return mcp_srv.mcp_inspect_cfg_profile(profile_name_or_path=profile, pids=pid_list)


@app.post("/cfg/inspect", tags=["5. .cfg Profile Engine"])
def inspect_cfg_profile_post(req: CfgInspectRequest) -> Dict[str, Any]:
    return mcp_srv.mcp_inspect_cfg_profile(
        profile_name_or_path=req.profile_name_or_path,
        pids=req.pids,
        filter_non_default=req.filter_non_default,
    )


@app.get("/cfg/diff", tags=["5. .cfg Profile Engine"])
def diff_cfg_profiles_get(
    profile_a: str = Query(default="device_export_original.cfg"),
    profile_b: str = Query(default="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg"),
) -> Dict[str, Any]:
    return mcp_srv.mcp_diff_cfg_profiles(profile_a=profile_a, profile_b=profile_b)


@app.post("/cfg/validate", tags=["5. .cfg Profile Engine"])
def validate_cfg_edits_post(req: CfgValidateOrCreateRequest) -> Dict[str, Any]:
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.cfg_engine.validate_edits(base_profile=req.base_profile, proposed_edits=req.proposed_edits)


@app.post("/cfg/create", tags=["5. .cfg Profile Engine"])
def create_cfg_file_post(req: CfgValidateOrCreateRequest) -> Dict[str, Any]:
    return mcp_srv.mcp_validate_and_compile_cfg(
        base_profile=req.base_profile,
        proposed_edits=req.proposed_edits,
        output_filename=req.output_filename or "custom_generated_fmc650.cfg",
    )


@app.get("/cfg/download/{filename}", tags=["5. .cfg Profile Engine"])
def download_cfg_file(filename: str):
    safe_name = os.path.basename(filename)
    repo = FMC650KnowledgeRepository.get_instance()
    try:
        path = repo.cfg_engine._resolve_profile_path(safe_name)
    except FileNotFoundError as exc:
        cand = GENERATED_CFGS_DIR / safe_name
        if cand.is_file():
            path = cand
        else:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
    return FileResponse(path=str(path), filename=path.name, media_type="application/octet-stream")


# Workbench compatibility routes
@app.get("/configurations", tags=["6. Workbench Compatibility"])
def list_ui_configurations() -> List[Dict[str, Any]]:
    repo = FMC650KnowledgeRepository.get_instance()
    ui_configs: List[Dict[str, Any]] = []
    for p in repo.cfg_engine.list_profiles():
        if "error" in p:
            continue
        hdr = p.get("header", {})
        ui_configs.append({
            "id": p["filename"],
            "filename": p["filename"],
            "device_family": hdr.get("FmType", "FMC650"),
            "spec_id": hdr.get("SpecId", "1"),
            "hw_version": hdr.get("HwVersion", "FMC650_1"),
            "schema_version": hdr.get("ConfigurationVersion", "4.43.1.0"),
            "parameter_count": p.get("parameter_count", 0),
            "is_quarantined": False,
            "source": "fmc650_mcp_server",
        })
    return ui_configs


@app.get("/parameters", tags=["6. Workbench Compatibility"])
def search_ui_parameters(q: str = "", limit: int = 50, offset: int = 0, io_block: Optional[int] = None) -> Dict[str, Any]:
    repo = FMC650KnowledgeRepository.get_instance()
    ql = q.strip().lower()
    matched: List[Dict[str, Any]] = []
    for pid in sorted(repo.all_valid_pids):
        if io_block is not None and (pid // 10) * 10 != io_block:
            continue
        xmeta = repo.xml_params.get(pid, {})
        srow = repo.schema_params.get(str(pid), {})
        name = xmeta.get("name") or srow.get("label") or srow.get("name") or f"Parameter {pid}"
        if ql and ql not in str(pid) and ql not in name.lower():
            continue
        matched.append({
            "parameter_id": pid,
            "name": name,
            "data_type": xmeta.get("attrib", {}).get("ParameterType") or srow.get("type") or "Unknown",
            "default_value": xmeta.get("attrib", {}).get("Default") or srow.get("default"),
            "min_value": xmeta.get("attrib", {}).get("Min") or srow.get("min"),
            "max_value": xmeta.get("attrib", {}).get("Max") or srow.get("max"),
            "ui_section": " > ".join(srow.get("section", [])) if srow.get("section") else "Teltonika Configurator",
        })
    return {"total": len(matched), "parameters": matched[offset: offset + limit]}


@app.get("/parameters/{pid}", tags=["6. Workbench Compatibility"])
def get_ui_parameter(pid: int) -> Dict[str, Any]:
    repo = FMC650KnowledgeRepository.get_instance()
    return repo.reconcile_parameter(pid)


@app.get("/graph/metadata", tags=["6. Workbench Compatibility"])
def get_ui_graph_metadata() -> Dict[str, Any]:
    repo = FMC650KnowledgeRepository.get_instance()
    return {
        "status": "loaded",
        "graph_v3_nodes": repo.graph_v3.number_of_nodes(),
        "graph_v3_edges": repo.graph_v3.number_of_edges(),
        "graph_v1_nodes": repo.graph_v1.number_of_nodes(),
        "graph_v1_edges": repo.graph_v1.number_of_edges(),
        "xml_collections": len(repo.collections),
        "total_valid_pids": len(repo.all_valid_pids),
    }


@app.get("/conversations", tags=["6. Workbench Compatibility"])
def list_conversations() -> List[Dict[str, Any]]:
    return session_store.list_conversations()


# ============================================================================
# 6. INTERACTIVE HTML BROWSER DASHBOARD (/ AND /explorer)
# ============================================================================

EXPLORER_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FMC650 Comprehensive MCP Server — Browser Explorer</title>
  <style>
    :root {
      --bg: #0b0f19;
      --card: #131b2e;
      --border: #23304d;
      --accent: #38bdf8;
      --accent2: #22c55e;
      --text: #e2e8f0;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }
    header {
      background: linear-gradient(90deg, #0f172a, #1e293b);
      border-bottom: 1px solid var(--border);
      padding: 20px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    header h1 { margin: 0; font-size: 1.35rem; color: #fff; }
    header p { margin: 4px 0 0; color: var(--muted); font-size: 0.9rem; }
    .badge-row { display: flex; gap: 10px; flex-wrap: wrap; }
    .badge {
      background: rgba(56, 189, 248, 0.14);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--accent);
      padding: 6px 12px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
    }
    .badge.green {
      background: rgba(34, 197, 94, 0.14);
      border-color: rgba(34, 197, 94, 0.4);
      color: var(--accent2);
    }
    main {
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 32px;
      display: grid;
      grid-template-columns: 440px 1fr;
      gap: 24px;
    }
    @media (max-width: 1024px) {
      main { grid-template-columns: 1fr; }
    }
    .panel {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px;
      margin-bottom: 18px;
    }
    .panel h2 {
      margin: 0 0 12px;
      font-size: 1rem;
      color: var(--accent);
      border-bottom: 1px solid var(--border);
      padding-bottom: 8px;
    }
    .link-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .btn-link {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1a243d;
      border: 1px solid var(--border);
      color: var(--text);
      padding: 9px 12px;
      border-radius: 8px;
      cursor: pointer;
      text-decoration: none;
      font-size: 0.85rem;
      transition: all 0.15s;
    }
    .btn-link:hover {
      border-color: var(--accent);
      background: #1e2d4d;
    }
    .btn-link code {
      color: var(--accent);
      font-size: 0.78rem;
    }
    .output-box {
      background: #070b14;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
      min-height: 680px;
      max-height: 82vh;
      overflow: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.83rem;
      white-space: pre-wrap;
      color: #cbd5e1;
    }
    .toolbar {
      display: flex;
      gap: 10px;
      margin-bottom: 12px;
      align-items: center;
      flex-wrap: wrap;
    }
    .toolbar input {
      flex: 1;
      background: #090d16;
      border: 1px solid var(--border);
      color: #fff;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 0.85rem;
    }
    .toolbar button {
      background: var(--accent);
      color: #090d16;
      border: none;
      padding: 9px 16px;
      border-radius: 8px;
      font-weight: 700;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Teltonika FMC650 Comprehensive MCP Server (alfa-0.1)</h1>
      <p>SINOTRUK SITRAK J1939 FMS (CAN1) + WABCO TEBS E TrailerCAN (CAN2) + Flespi Weight Analytics + Wialon TR84 (146 Sensors)</p>
    </div>
    <div class="badge-row">
      <a class="badge green" href="/docs" target="_blank">Swagger UI (/docs)</a>
      <a class="badge" href="/redoc" target="_blank">ReDoc (/redoc)</a>
      <a class="badge" href="/workbench" target="_blank">React Workbench (/workbench)</a>
      <a class="badge" href="/health" target="_blank">Health JSON (/health)</a>
    </div>
  </header>

  <main>
    <div>
      <div class="panel">
        <h2>1. Subject-Indexed Diagnostic Playbooks (diagnostic/)</h2>
        <div class="link-list">
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/00')"><span>00 — Master Diagnostic Index</span><code>GET /mcp/playbooks/00</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/01')"><span>01 — CAN1, J1939, FMS, EV-FMS & 15 Axles</span><code>GET /mcp/playbooks/01</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/02')"><span>02 — Real-World Truck & Trailer Weight IDs</span><code>GET /mcp/playbooks/02</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/03')"><span>03 — 3-Axle SITRAK C7H & Why TrailerCAN</span><code>GET /mcp/playbooks/03</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/04')"><span>04 — WABCO TEBS E Port 42 & 3-Axle Bogie</span><code>GET /mcp/playbooks/04</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/05')"><span>05 — Incline/Slope, Brake-Bind & Calibration</span><code>GET /mcp/playbooks/05</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/playbooks/06')"><span>06 — Missing FMS Axles, Gross Sum & CAN Mode</span><code>GET /mcp/playbooks/06</code></button>
        </div>
      </div>

      <div class="panel">
        <h2>2. Interactive MCP Tools (One-Click Live Test)</h2>
        <div class="link-list">
          <button class="btn-link" onclick="loadUrl('/mcp/diagnose-weight?tractor_model=SINOTRUK+SITRAK+C7H+6x4&tractor_suspension=steel_springs&observed_avl_ids=139,13657&can1_bus_mode=0&on_incline=true')">
            <span>Diagnose Steel-Spring Sitrak + WABCO + Incline</span><code>/mcp/diagnose-weight</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/diagnose-weight?tractor_model=SINOTRUK+SITRAK+C7H+6x4&tractor_suspension=ecas_air&observed_avl_ids=139,13657&can1_bus_mode=0&on_incline=false')">
            <span>Diagnose ECAS Sitrak (Silent Mode PID 206=0)</span><code>/mcp/diagnose-weight</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/resolve?ids=100,139,avl_id:13657,trailer.axle.load.sum,fleet_weight_stable,sensor:71')">
            <span>Resolve PIDs, AVL IDs, Flespi & Wialon Sensor 71</span><code>/mcp/resolve</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/telematics?keys=46530,139,103060,13657,13810,fleet_weight_stable,fleet_fraud_alert')">
            <span>Lookup Telematics Mappings (FMS + Trailer + Fleet)</span><code>/mcp/telematics</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/wialon-sensors?category=trailer')">
            <span>Inspect Wialon TR84 Trailer Sensors</span><code>/mcp/wialon-sensors</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/wialon-sensors?category=fleet')">
            <span>Inspect Wialon TR84 fleet_* Weight/Fraud Sensors</span><code>/mcp/wialon-sensors</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/commands?action=enable_normal_can1')">
            <span>Generate Commands: Switch CAN1 to Normal Mode</span><code>/mcp/commands</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/mcp/commands?action=configure_sitrak_wabco_p2')">
            <span>Generate Commands: Sitrak + WABCO P2 Setup</span><code>/mcp/commands</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/cfg/inspect')">
            <span>Inspect P2_PRODUCTION_v1.2 .cfg Profile</span><code>/cfg/inspect</code>
          </button>
          <button class="btn-link" onclick="loadUrl('/cfg/diff')">
            <span>Diff Factory .cfg vs P2_PRODUCTION_v1.2</span><code>/cfg/diff</code>
          </button>
        </div>
      </div>

      <div class="panel">
        <h2>3. MCP Resources (6 Resources & Tool Catalog)</h2>
        <div class="link-list">
          <button class="btn-link" onclick="loadUrl('/mcp/tools')"><span>All 15 Tools, 6 Resources & 4 Prompts</span><code>/mcp/tools</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/resources/schema-summary')"><span>Resource: Schema & Index Summary</span><code>fmc650://schema/summary</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/resources/profiles-list')"><span>Resource: .cfg Profiles Catalog</span><code>fmc650://profiles/list</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/resources/corpus-manifest')"><span>Resource: Corpus File Manifest</span><code>fmc650://corpus/manifest</code></button>
          <button class="btn-link" onclick="loadUrl('/mcp/resources/wialon-tr84-sensors')"><span>Resource: All 146 Wialon TR84 Sensors</span><code>fmc650://wialon/tr84-sensors</code></button>
        </div>
      </div>
    </div>

    <div>
      <div class="panel">
        <h2>Live MCP Response Viewer</h2>
        <div class="toolbar">
          <input id="searchInput" type="text" value="Gross sum axle only 139 CAN1 Bus Mode Silent Normal incline" placeholder="Search across all FMC650 knowledge & diagnostic playbooks..." />
          <button onclick="runSearch()">Search Corpus</button>
        </div>
        <div id="currentEndpoint" style="color: var(--accent2); font-size: 0.82rem; margin-bottom: 8px;">GET /mcp/tools</div>
        <div id="output" class="output-box">Loading...</div>
      </div>
    </div>
  </main>

  <script>
    async function loadUrl(url) {
      document.getElementById('currentEndpoint').textContent = 'GET ' + url;
      const out = document.getElementById('output');
      out.textContent = 'Fetching ' + url + ' ...';
      try {
        const res = await fetch(url);
        const data = await res.json();
        if (data && data.content && typeof data.content === 'string' && Object.keys(data).includes('returned_chars')) {
          out.textContent = '=== ' + data.path + ' (' + data.returned_chars + ' chars) ===\\n\\n' + data.content;
        } else {
          out.textContent = JSON.stringify(data, null, 2);
        }
      } catch (err) {
        out.textContent = 'Error: ' + err;
      }
    }
    function runSearch() {
      const q = encodeURIComponent(document.getElementById('searchInput').value);
      loadUrl('/mcp/search?q=' + q);
    }
    loadUrl('/mcp/tools');
  </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/explorer", response_class=HTMLResponse, include_in_schema=False)
def serve_browser_explorer() -> HTMLResponse:
    """Serve the interactive FMC650 MCP Browser Explorer & Diagnostic Playground."""
    return HTMLResponse(content=EXPLORER_HTML)


STATIC_DIR = Path(__file__).resolve().parent / "static"
if STATIC_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
    assets_dir = STATIC_DIR / "assets"
    if assets_dir.is_dir():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

    @app.get("/workbench", include_in_schema=False)
    def serve_workbench():
        return FileResponse(str(STATIC_DIR / "index.html"))
