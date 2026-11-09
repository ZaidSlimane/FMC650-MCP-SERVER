# Comprehensive FMC650 MCP Server (`fmc650-comprehensive-mcp` alfa-0.1)

A self-contained, portable **Model Context Protocol (MCP) & Web Diagnostic Server** unifying **100% of the Teltonika FMC650 firmware schema, `.cfg` compiler toolchain, Knowledge Graphs, Flespi & Wialon Parameter mappings, Subject-Indexed Diagnostic Playbooks (`diagnostic/`), some modem, GNSS and CPU Field Debugging Logs, and Official Teltonika Documentation**.

---

## 1. Quick Start & Server Deployment

### Clone & Install Dependencies
```bash
git clone https://github.com/ZaidSlimane/FMC650-MCP-SERVER.git
cd FMC650-MCP-SERVER
pip install -r requirements.txt
```

### Mode A: Run as MCP Server (Stdio Transport — Local IDE / Agent Clients)
```bash
python mcp_server.py
# or:
python -m fmc650_mcp_server.server
```

### Mode B: Run as Remote MCP Server (SSE or Streamable-HTTP Transport)
```bash
# Server-Sent Events (SSE) transport on 0.0.0.0:8065
python mcp_server.py --transport sse --host 0.0.0.0 --port 8065

# Streamable-HTTP transport on 0.0.0.0:8065
python mcp_server.py --transport streamable-http --host 0.0.0.0 --port 8065
```

### Mode C: Run Browser Explorer, React Workbench & REST API Server
```bash
python mcp_server.py --web --host 0.0.0.0 --port 8065
# or directly via Uvicorn:
python -m uvicorn fmc650_mcp_server.api:app --host 0.0.0.0 --port 8065
```
Once running, open:
- `/` or `/explorer` — Interactive Browser Explorer & Diagnostic Playground
- `/docs` — Swagger UI (interactive OpenAPI documentation)
- `/redoc` — ReDoc API documentation
- `/workbench` — React Configuration & Knowledge Graph Workbench
- `/health` — Server & Knowledge Graph health status

### Mode D: Deploy Anywhere with Docker
```bash
docker build -t fmc650-mcp-server .
docker run -d -p 8065:8065 --name fmc650-mcp fmc650-mcp-server
```
Environment variables supported on any host or cloud platform:
- `MCP_TRANSPORT` — `stdio` (default CLI), `web` (default in `Dockerfile`), `sse`, or `streamable-http`
- `HOST` — Bind address (default: `0.0.0.0`)
- `PORT` — Bind port (default: `8065`)
- `FMC650_SERVER_ROOT` — Optional override for the repository root path

### `.mcp.json` Client Registration
Configured in [`.mcp.json`](./.mcp.json):
```json
{
  "mcpServers": {
    "fmc650-comprehensive-mcp": {
      "command": "python",
      "args": ["-m", "fmc650_mcp_server.server"],
      "cwd": ".",
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

---

## 2. Exposed MCP Tools (17 Tools)

| # | Tool Name | Purpose & Capabilities |
| :-: | :--- | :--- |
| **1** | `mcp_resolve_identifiers` | Resolve configuration PIDs, IO block IDs, telemetry AVL IDs, Flespi keys, Wialon keys, or sensor IDs (e.g., `100`, `139`, `trailer.axle.load.sum`, `sensor:71`) and flag integer ID collisions across namespaces. |
| **2** | `mcp_search_all_knowledge` | Bilingual (EN/FR) keyword and synonym search across all FMC650 manuals, parameter catalogs, and engineering guides (e.g., `"axle weight"`, `"ignition threshold"`). |
| **3** | `mcp_query_diagnostic_playbooks` | Retrieve step-by-step troubleshooting guides for CAN1/J1939, TrailerCAN, axle load sensors, and incline calibration issues. |
| **4** | `mcp_investigate_device_behavior` | Analyze a field symptom end-to-end by combining troubleshooting playbooks, historical session evidence, and related parameter definitions. |
| **5** | `mcp_search_debugging_sessions` | Search real-world device debug logs and crash analyses (e.g., watchdog resets, ignition flapping, flash backlog drain, TLS timeouts). |
| **6** | `mcp_diagnose_weight_and_trailer_setup` | Diagnose truck FMS (`CAN1`) and trailer EBS (`CAN2`) weight telemetry issues (e.g., why gross combination weight `AVL 139` arrives without per-axle weights, Silent vs. Normal bus mode, or slope effects). |
| **7** | `mcp_lookup_telematics_mapping` | Map any parameter end-to-end across Teltonika `.cfg` ID $\leftrightarrow$ Codec 8E `AVL ID` $\leftrightarrow$ Flespi parameter $\leftrightarrow$ Wialon key $\leftrightarrow$ Wialon sensor. |
| **8** | `mcp_inspect_wialon_profile` | Search and filter configured Wialon unit sensors by ID, name, formula, or category (e.g., `weight`, `trailer`, `fuel`, `engine`, `tachograph`). |
| **9** | `mcp_generate_flespi_and_sms_commands` | Generate validated Teltonika SMS, GPRS Codec 12, and Flespi commands (e.g., `setparam`, `getparam`, `scanfms`, and CAN bus mode switching). |
| **10** | `mcp_inspect_cfg_profile` | Inspect `.cfg` configuration parameters with automatic credential masking, enum decoding, and comparison against factory defaults. |
| **11** | `mcp_diff_cfg_profiles` | Compare two `.cfg` profiles side-by-side and list all modified parameter values and decoded options. |
| **12** | `mcp_validate_and_compile_cfg` | Validate proposed `PID=Value` changes against hardware schema rules and compile a ready-to-upload `.cfg` archive. |
| **13** | `mcp_list_io_block_siblings` | List all sibling settings of an I/O block (`Priority`, `Operand`, `High/Low Level`, `Event Only`, `Averaging`) with allowed ranges. |
| **14** | `mcp_query_knowledge_graph` | Traverse multi-hop relationships between parameters, CAN PGNs, telemetry IDs, and hardware features with full provenance. |
| **15** | `mcp_get_full_document_section` | Read specific sections, headings, or line ranges of any indexed reference document with pagination. |
| **16** | `mcp_search_firmware_and_pcn_history` | Search firmware changelogs and Product Change Notifications (PCNs) for version-specific fixes and hardware revisions (e.g., `03.01.01`). |
| **17** | `mcp_verify_mermaid_diagram` | Validate and automatically repair Mermaid architecture and workflow diagrams. |

---

## 3. Exposed MCP Resources (6 Resources) & Prompts (4 Prompts)

### Resources
* `fmc650://schema/summary` — High-level counts of parameters, collections, telemetry IDs, sensors, graph nodes, and indexed documents.
* `fmc650://profiles/list` — Catalog of available `.cfg` profiles with SHA-256 checksums and parameter counts.
* `fmc650://corpus/manifest` — Complete index of available documentation categories and reference files.
* `fmc650://diagnostic/index` — Master index of CAN1, TrailerCAN, and axle weight troubleshooting playbooks.
* `fmc650://telematics/weight-and-trailer-catalog` — Reference catalog of truck (`CAN1`), trailer (`CAN2`), and computed weight telemetry parameters.
* `fmc650://telematics/mappings` — Unified cross-reference index linking configuration IDs, AVL IDs, Flespi parameters, and Wialon sensors.

### Prompts
* `prompt_diagnose_fms_or_trailer_weight`
* `prompt_audit_cfg_profile`
* `prompt_map_flespi_wialon_sensor`
* `prompt_explain_incline_and_calibration`

---

## 4. Directory Layout

Device configuration and schema utilities: [fmc650-reverse-engineered/tools/](./fmc650-reverse-engineered/tools/).

```text
FMC650-MCP-SERVER/
├── .mcp.json                             # Portable MCP Server registration config
├── Dockerfile                            # Container image for cloud / Linux server deployment
├── mcp_server.py                         # Root CLI entrypoint (stdio, sse, streamable-http, web)
├── pyproject.toml                        # Python package metadata
├── requirements.txt                      # Dependencies
├── README.md                             # Server documentation
├── fmc650_mcp_server/                    # Core MCP & FastAPI Server Python Package
│   ├── __init__.py
│   ├── api.py                            # FastAPI Browser Explorer, Swagger UI & REST Gateway
│   ├── schemas.py                        # Pydantic models
│   ├── mermaid_validator.py              # Mermaid validator & auto-repairer
│   ├── cfg_creator.py                    # .cfg inspection, diffing & compilation engine
│   ├── repository.py                     # 6-Tier unified indexer (auto-loads .json or .json.gz)
│   ├── session_store.py                  # SQLite session store
│   └── server.py                         # 17 MCP Tools, 6 Resources, 4 Prompts
├── diagnostic/                           # 7 Subject-Indexed Engineering & Diagnostic Playbooks
│   ├── 00_README_Diagnostic_Index.md
│   ├── 01_CAN1_FMS_J1939_LVCAN_EV_FMS_Architecture.md
│   ├── 02_Real_World_Weight_and_Trailer_IDs_Reference.md
│   ├── 03_SITRAK_C7H_3Axle_Models_and_Why_TrailerCAN_Is_Required.md
│   ├── 04_WABCO_TEBS_E_Bogie_Physics_and_Trailer_Parameters.md
│   ├── 05_Incline_Slope_Uneven_Load_and_WABCO_Calibration.md
│   └── 06_FMS_Axle_Weight_Troubleshooting_and_CAN_Bus_Modes.md
├── debugging-sessions/                   # 14 Field Traces & .cfg Save Failure Reports
├── flespi-parameters/                    # Flespi Settings, AVL IDs & 1,357 IOItem Catalog
├── wialon-parameters/                    # Wialon TR84 146-Sensor Profile & 1,161 Unified Params
├── fmc650-reverse-engineered/            # Compiler XML, Schema JSON, .cfg Profiles & Tools
├── teltonika-docs/                       # 10 Official Teltonika Documentation Categories
├── graph-db/                             # Versioned knowledge graph exports: graph-v1/ and graph-v3/
└── tests/                                # Automated Verification Test Suite
    └── test_mcp_server.py
```
