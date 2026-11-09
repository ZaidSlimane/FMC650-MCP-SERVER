# FMC650 Reverse-Engineered Schema & Compiler Artifacts (`re/`)

This directory contains the **machine-readable parameter schemas**, **vendor-compiled Configurator XML**, and **coverage/gap verification JSONs** for the Teltonika FMC650 (`Ver.03.01.01.Rev.15`, `ConfigurationVersion 4.43.1.0`, `HwVersion FMC650_1`, `FmType FMC650`, `SpecId 1`).

**Attribution Status: 100.0% (`11,688 / 11,688` IDs)** of the reference hardware `.cfg` export ([`../cfgs/device_export_original.cfg`](../cfgs/device_export_original.cfg)) are attributed with full provenance and regenerable byte-identically via the tools in [`../tools/`](../tools/README.md).

---

## Artifact Catalog

### 1. Merged Parameter Schema & Coverage Reports

| File | Description | Key Metrics |
| :--- | :--- | :--- |
| **[`fmx65_03.01.01.Rev.15_schema.json`](fmx65_03.01.01.Rev.15_schema.json)** | **Master JSON Parameter Schema.** Maps `id` → `{label, type, default, min, max, units, collection, validate, max_length, increment, source, branch, in_cfg, cfg_value}`. *Note: Contains `13,966` total IDs across FMX6 sibling branches; `11,688` have `in_cfg: true` for FMC650 SpecId 1.* | `13,966` total records · `11,688` in-cfg (`generator:FMC650:1`: `1,149` · `xml:ParameterId`: `126` · `xml:ListConfiguration`: `1,281` · `xml:Geozones`: `1,100` · `generator:IOItem`: `6,451` · `xml:Polygon`: `1,581`) |
| **[`fmx65_03.01.01.Rev.15_parameters.csv`](fmx65_03.01.01.Rev.15_parameters.csv)** | **Flat CSV Parameter Table.** UTF-8-BOM (`utf-8-sig`), CRLF, 20 columns (`id`, `in_cfg`, `cfg_value`, `source`, `element`, `type`, `label`, `default`, `min`, `max`, `units`, `collection`, `validate`, `max_length`, `increment`, `path`, `origin`, `branch`, `ambiguous`, `static_source`). | `13,966` rows + header (`2.01 MB`) |
| **[`fmx65_03.01.01.Rev.15_report.json`](fmx65_03.01.01.Rev.15_report.json)** | **Coverage Summary JSON.** Quantitative breakdown of `cfg_params`, `schema_ids`, `cfg_covered`, `cfg_unknown`, `schema_only`, and `by_source` counts. | `coverage_pct: 100.0`, `cfg_unknown: 0`, `schema_only: 2278` |
| **[`fmx65_03.01.01.Rev.15_gaps.json`](fmx65_03.01.01.Rev.15_gaps.json)** | **Unattributed Contiguous ID Ranges.** Lists any `.cfg` parameter IDs missing from the merged schema. | `[]` (0 gaps — 100% attributed) |

---

### 2. Authoritative Vendor-Compiled Configurator XML

| File | Description | Provenance & Metrics |
| :--- | :--- | :--- |
| **[`generated_FMC650_spec1_cfg4.43.1.0.xml`](generated_FMC650_spec1_cfg4.43.1.0.xml)** | **Compiled FMC650 Configurator XML (`4.43.1.0`).** Emitted directly by Teltonika's `Configuration.Generator.dll` via [`../tools/ximgen/`](../tools/ximgen) for `HardwareVersion("FMC650:1")`, `Version(4,43,1,0)`, `SpecId 1`. Defines all **81 `<CollectionConfiguration>` enum tables**, explicit `ParameterId` controls, and `<IOItem>` child offset rules. | `18,139` XML elements · `1,150` explicit `ParameterId`s · `81` `<CollectionConfiguration>` tables · `1,442,736` bytes (SHA-256 `d8137ae7…`) |
| **[`generated_FMC650_spec1_cfg4.43.1.0_ids.txt`](generated_FMC650_spec1_cfg4.43.1.0_ids.txt)** | **Explicit Parameter ID List.** Sorted list of the `1,150` explicit `ParameterId` integers present in `generated_FMC650_spec1_cfg4.43.1.0.xml`, one per line. | `1,150` lines (`6,643` bytes, SHA-256 `1b65d72a…`) |

---

## End-to-End Reproduction Chain

```bash
T=tools
R=re
C=cfgs
B=/path/to/brand_xml   # 150 vendor Brand.dll XML files

# 1. Decrypt firmware (.xim -> fw_image.bin):
python $T/xim_decrypt.py FMX65.Ver.03.01.01.Rev.15_ID1.e.xim fw_image.bin

# 2. Parse the reference .cfg export:
python $T/cfg_tool.py read $C/device_export_original.cfg cfg_parsed.json

# 3. Extract static schema from vendor XMLs (44.81% coverage alone):
python $T/build_schema.py $B cfg_parsed.json $R/fmx65_03.01.01.Rev.15

# 4. Merge compiled vendor XML + IOItem expansion -> 100.0% coverage:
python $T/merge_generator.py $R/generated_FMC650_spec1_cfg4.43.1.0.xml \
       cfg_parsed.json $R/fmx65_03.01.01.Rev.15_schema.json \
       $R/fmx65_03.01.01.Rev.15 $B
```

---

## Related Directories

- **Tools (`cfg_tool.py`, `make_cfg.py`, `build_schema.py`, `merge_generator.py`):** [`../tools/README.md`](../tools/README.md)
- **Reference & Production `.cfg` Files:** [`../cfgs/README.md`](../cfgs/README.md)
- **Engineering & Debugging Reports:** [`../mds/README.md`](../mds/README.md)
