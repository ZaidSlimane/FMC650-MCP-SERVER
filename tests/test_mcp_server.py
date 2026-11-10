"""Automated Test Suite for the Comprehensive FMC650 MCP Server (`fmc650-comprehensive-mcp`)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

SERVER_ROOT = Path(__file__).resolve().parents[1]
if str(SERVER_ROOT) not in sys.path:
    sys.path.insert(0, str(SERVER_ROOT))

from fmc650_mcp_server.server import (
    mcp_diagnose_weight_and_trailer_setup,
    mcp_diff_cfg_profiles,
    mcp_generate_flespi_and_sms_commands,
    mcp_get_full_document_section,
    mcp_inspect_cfg_profile,
    mcp_inspect_wialon_profile,
    mcp_list_io_block_siblings,
    mcp_lookup_telematics_mapping,
    mcp_query_diagnostic_playbooks,
    mcp_query_knowledge_graph,
    mcp_resolve_identifiers,
    mcp_search_all_knowledge,
    mcp_search_firmware_and_pcn_history,
    mcp_validate_and_compile_cfg,
    mcp_verify_mermaid_diagram,
    prompt_audit_cfg_profile,
    prompt_diagnose_fms_or_trailer_weight,
    prompt_explain_incline_and_calibration,
    prompt_map_flespi_wialon_sensor,
    resource_corpus_manifest,
    resource_diagnostic_index,
    resource_profiles_list,
    resource_schema_summary,
    resource_weight_and_trailer_catalog,
    resource_wialon_tr84_sensors,
)


def test_schema_summary_and_resources():
    summary = json.loads(resource_schema_summary())
    assert summary["server"] == "fmc650-comprehensive-mcp"
    assert summary["total_valid_pids"] > 11000
    assert summary["wialon_tr84_sensors_count"] >= 140
    assert summary["total_indexed_documents"] >= 100

    manifest = json.loads(resource_corpus_manifest())
    assert len(manifest["diagnostic_files"]) == 7

    profiles = json.loads(resource_profiles_list())
    assert len(profiles) >= 4

    diag_idx = json.loads(resource_diagnostic_index())
    assert "01_CAN1_FMS_J1939_LVCAN_EV_FMS_Architecture.md" in diag_idx["content"]

    wt_cat = json.loads(resource_weight_and_trailer_catalog())
    assert "13657" in wt_cat["content"]

    tr84 = json.loads(resource_wialon_tr84_sensors())
    assert tr84["total_sensors"] >= 140


def test_resolve_identifiers_and_collision_detection():
    res = mcp_resolve_identifiers([
        "100",
        "139",
        "avl_id:13657",
        "trailer.axle.load.sum",
        "fleet_weight_stable",
        "sensor:71",
        "46100..46130",
    ])
    assert res["resolved_count"] == 7
    # PID 100 vs AVL ID 100 collision warning
    assert "collision_warning" in res["results"]["100"]
    # Sensor 71
    assert res["results"]["sensor:71"]["type"] == "WIALON_TR84_SENSOR"
    # AVL 13657
    assert res["results"]["avl_id:13657"]["avl_id"] == 13657


def test_diagnostic_playbooks_and_weight_setup():
    playbooks = mcp_query_diagnostic_playbooks(
        "Gross sum axle only 139 CAN1 Bus Mode Silent Normal incline brake-bind",
        include_full_playbook=True,
    )
    assert len(playbooks["matched_playbooks"]) >= 2
    assert playbooks["top_playbook_full_content"] is not None

    diag_steel = mcp_diagnose_weight_and_trailer_setup(
        tractor_model="SINOTRUK SITRAK C7H 6x4",
        tractor_suspension="steel_springs",
        trailer_ebs="WABCO TEBS E",
        observed_avl_ids=[139, 13657],
        can1_bus_mode=0,
        on_incline=True,
    )
    assert any("STEEL-SPRING" in d for d in diag_steel["engineering_diagnosis"])
    assert any("INCLINE" in d for d in diag_steel["engineering_diagnosis"])

    diag_ecas = mcp_diagnose_weight_and_trailer_setup(
        tractor_model="SINOTRUK SITRAK C7H 6x4",
        tractor_suspension="ecas_air",
        trailer_ebs="WABCO TEBS E",
        observed_avl_ids=[139, 13657],
        can1_bus_mode=0,
        on_incline=False,
    )
    assert any("setparam 206:1" in cmd for cmd in diag_ecas["recommended_commands"])


def test_telematics_wialon_and_commands():
    tmap = mcp_lookup_telematics_mapping(["46530", "13657", "trailer_axle_load_sum", "fleet_fraud_alert"])
    assert "46530" in tmap["mappings"]
    assert "13657" in tmap["mappings"]

    wprof = mcp_inspect_wialon_profile(category="trailer")
    assert wprof["matched_count"] >= 10

    cmds = mcp_generate_flespi_and_sms_commands("enable_normal_can1")
    assert cmds["setparam_command"] == "setparam 205:500;206:1;210:0"
    assert cmds["xml_validation_report"]["validation_passed"] is True


def test_cfg_tools_and_prompts():
    insp = mcp_inspect_cfg_profile(pids=[205, 206, 330, 46530, 103060])
    assert insp["returned_count"] == 5

    diff = mcp_diff_cfg_profiles(
        "device_export_original.cfg",
        "FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
    )
    assert diff["total_differences"] > 10

    sibs = mcp_list_io_block_siblings(103060, profile_name="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg")
    assert sibs["sibling_count"] >= 5

    comp = mcp_validate_and_compile_cfg(
        base_profile="FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg",
        proposed_edits={205: "500", 206: "1"},
        output_filename="test_normal_can1.cfg",
    )
    assert comp["compiled_artifact"]["validation_passed"] is True

    m_res = mcp_verify_mermaid_diagram("flowchart TB\n  A[CAN1 (Pins 12/2)] --> B[FMC650]")
    assert m_res["is_valid"] is True

    kg = mcp_query_knowledge_graph(["13657", "46530"])
    assert len(kg["matched_nodes"]) >= 1

    fw = mcp_search_firmware_and_pcn_history("03.01.01")
    assert "documentation_hits" in fw

    sec = mcp_get_full_document_section("diagnostic/06_FMS_Axle_Weight_Troubleshooting_and_CAN_Bus_Modes.md", max_chars=2000)
    assert "PGN 65134" in sec["content"]

    search_td = mcp_search_all_knowledge("Locked FMS scanfms", domains=["teltonika-docs"])
    assert search_td["total_matching_files"] >= 1

    assert "PGN 65134" in prompt_diagnose_fms_or_trailer_weight()
    assert "PID 1000" in prompt_audit_cfg_profile()
    assert "13657" in prompt_map_flespi_wialon_sensor()
    assert "Brake-Bind" in prompt_explain_incline_and_calibration()


def test_streamable_http_mcp_jsonrpc():
    from fastapi.testclient import TestClient
    from fmc650_mcp_server.api import app

    client = TestClient(app)

    # 1. initialize on /mcp
    init_res = client.post(
        "/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2025-03-26",
                "capabilities": {},
                "clientInfo": {"name": "claude-code", "version": "1.0.0"},
            },
        },
    )
    assert init_res.status_code == 200
    assert "mcp-session-id" in {k.lower() for k in init_res.headers.keys()}
    init_data = init_res.json()
    assert init_data["result"]["protocolVersion"] == "2025-03-26"
    assert init_data["result"]["serverInfo"]["name"] == "fmc650-comprehensive-mcp"

    # 2. notifications/initialized -> 202 Accepted
    notif_res = client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "method": "notifications/initialized"},
    )
    assert notif_res.status_code == 202

    # 3. tools/list
    tools_res = client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
    )
    assert tools_res.status_code == 200
    tools_list = tools_res.json()["result"]["tools"]
    assert len(tools_list) >= 15
    assert any(t["name"] == "mcp_resolve_identifiers" and "inputSchema" in t for t in tools_list)

    # 4. tools/call on both /mcp and /
    call_res = client.post(
        "/",
        json={
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "mcp_resolve_identifiers",
                "arguments": {"identifiers": ["100", "avl_id:13657"]},
            },
        },
    )
    assert call_res.status_code == 200
    call_body = call_res.json()["result"]
    assert call_body["isError"] is False
    assert "13657" in call_body["content"][0]["text"]

    # 5. resources/list & resources/read
    res_list = client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 4, "method": "resources/list", "params": {}},
    )
    assert res_list.status_code == 200
    assert len(res_list.json()["result"]["resources"]) >= 6

    res_read = client.post(
        "/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 5,
            "method": "resources/read",
            "params": {"uri": "fmc650://schema/summary"},
        },
    )
    assert res_read.status_code == 200
    assert res_read.json()["result"]["contents"][0]["uri"] == "fmc650://schema/summary"

    # 6. prompts/list & prompts/get
    pr_list = client.post(
        "/mcp",
        json={"jsonrpc": "2.0", "id": 6, "method": "prompts/list", "params": {}},
    )
    assert pr_list.status_code == 200
    assert len(pr_list.json()["result"]["prompts"]) == 4

    pr_get = client.post(
        "/mcp",
        json={
            "jsonrpc": "2.0",
            "id": 7,
            "method": "prompts/get",
            "params": {
                "name": "prompt_diagnose_fms_or_trailer_weight",
                "arguments": {"tractor_model": "SITRAK C7H"},
            },
        },
    )
    assert pr_get.status_code == 200
    assert "SITRAK C7H" in pr_get.json()["result"]["messages"][0]["content"]["text"]

    # 7. GET /mcp SSE probe returns 405 Method Not Allowed per MCP Streamable HTTP stateless spec
    sse_probe = client.get("/mcp", headers={"Accept": "text/event-stream"})
    assert sse_probe.status_code == 405

