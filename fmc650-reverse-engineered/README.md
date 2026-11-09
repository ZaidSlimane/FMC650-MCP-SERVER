# FMC650 Reverse-Engineering & Configuration Suite (`fmc650-reverse-engineered/`)

Authoritative reverse-engineering workspace for the **Teltonika FMC650 / FMX65** (FMX6 family LTE/GNSS/BLE/CAN/Tachograph terminal), covering:
1. **Firmware Container Decryption (`.xim`)** — PBKDF2-HMAC-SHA1 + AES-256-CBC + single-member GZip extraction (`03.01.01.Rev.15`, `Rev.28`, `Rev.34`).
2. **100% Parameter Schema & Compiler XML (`11,688 / 11,688` IDs)** — Static `Brand.dll` XML extraction merged with Teltonika's own `Configuration.Generator` (`4.43.1.0`, `SpecId 1`) and `IOItem` block expansion.
3. **Deterministic `.cfg` Codec & Validator** — Single-responsibility tools for reading, validating, and compiling device-grade `.cfg` files without Teltonika Configurator.
4. **Fleet Telematics v1.2 Production Profiles** — Validated `.cfg` profiles for SITRAK C7H / WABCO TEBS-E trailers (`4.43.1.0` and `4.41.0.0`).

---

## Clean 4-Folder Hierarchy

Every artifact in this module is strictly separated by function into four sibling directories, each with its own comprehensive `README.md`:

```text
fmc650-reverse-engineered/
├── README.md          ← Master index & architecture overview (this file)
├── tools/             ← Single-responsibility executable tools (1 tool per function)
│   ├── README.md      ← Tool reference, CLI usage, and reproduction pipeline
│   ├── cfg_tool.py    ← .cfg binary/text codec (read / write / verify)
│   ├── make_cfg.py    ← Authoritative XML/Schema validator & .cfg compiler (+ --preset all)
│   ├── build_schema.py← Static vendor XML schema extractor (Stage 1)
│   ├── merge_generator.py ← Compiler XML + IOItem 100% schema merger (Stage 2)
│   ├── xim_decrypt.py ← .xim firmware container decryptor (TLTF / AES-256-CBC)
│   └── ximgen/        ← .NET 8 harness driving Teltonika Configuration.Generator.dll
├── cfgs/              ← All reference anchors, test payloads & production .cfg profiles
│   ├── README.md      ← Complete catalog of all 9 .cfg files, headers, & SHA-256s
│   ├── device_export_original.cfg
│   ├── device_export_original_text_payload.cfg
│   ├── my_solid_upload_test.cfg
│   ├── my_solid_upload_test_text_payload.cfg
│   ├── FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg
│   ├── FMC650_FLEET_P2_SURGICAL_rev15.cfg
│   ├── FMC650_FLEET_P1_PILOTE_HR_v1.2_rev15.cfg
│   ├── FMC650_FLEET_P0_DECOUVERTE_v1.2_rev15.cfg
│   └── FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg
├── mds/               ← Technical analysis, debugging, simulation & mapping reports
│   ├── README.md      ← Executive synthesis & index of all 8 engineering reports
│   ├── analysis_report.md
│   ├── cfg_format.md
│   ├── xim_decryption.md
│   ├── re_agent_process.md
│   ├── re_agent_process_technical_resume.md
│   ├── FMC650_CFG_Save_Failure_Debugging_Report.md
│   ├── FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md
│   └── FMC650_FLEET_P2_PRODUCTION_v1.2_SITRAK_Simulation_Report.md
└── re/                ← Machine-readable schemas, compiled XML & coverage artifacts
    ├── README.md      ← Schema data dictionary, provenance breakdown & coverage metrics
    ├── fmx65_03.01.01.Rev.15_schema.json
    ├── fmx65_03.01.01.Rev.15_parameters.csv
    ├── fmx65_03.01.01.Rev.15_report.json
    ├── fmx65_03.01.01.Rev.15_gaps.json
    ├── generated_FMC650_spec1_cfg4.43.1.0.xml
    └── generated_FMC650_spec1_cfg4.43.1.0_ids.txt
```

---

## Directory Guide

| Directory | Contents | Documentation |
| :--- | :--- | :--- |
| **[`tools/`](tools/README.md)** | `cfg_tool.py`, `make_cfg.py`, `build_schema.py`, `merge_generator.py`, `xim_decrypt.py`, `ximgen/` | [`tools/README.md`](tools/README.md) |
| **[`cfgs/`](cfgs/README.md)** | 9 `.cfg` artifacts: factory reference export (`11,688` IDs), upload test, and 5 Fleet Telematics v1.2 profiles | [`cfgs/README.md`](cfgs/README.md) |
| **[`mds/`](mds/README.md)** | 8 technical reports: RE analysis, `.cfg` grammar, `.xim` decryption, save-failure debugging, SITRAK simulation & Flespi/Wialon mapping | [`mds/README.md`](mds/README.md) |
| **[`re/`](re/README.md)** | 6 data artifacts: `13,966`-row parameter schema (JSON/CSV), `1,442 KB` compiled Configurator XML (`81` collections), coverage & gap JSONs | [`re/README.md`](re/README.md) |

---

## Quick Start Commands

```bash
# 1. Verify a .cfg file's round-trip grammar & SHA-256:
python tools/cfg_tool.py verify cfgs/device_export_original.cfg

# 2. Compile a custom .cfg with strict XML + Schema + Hex validation:
python tools/make_cfg.py cfgs/device_export_original.cfg cfgs/custom.cfg 1000=120 1001=5 47500=1

# 3. Regenerate all 5 Fleet Telematics v1.2 fleet profiles:
python tools/make_cfg.py --preset all
```
