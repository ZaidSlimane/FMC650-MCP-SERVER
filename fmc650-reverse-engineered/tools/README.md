# FMC650 Reverse-Engineering & `.cfg` Tools (`tools/`)

Single-responsibility command-line and library tools (strictly **one tool per function, zero code duplication**) for decrypting `.xim` firmware, parsing/writing `.cfg` containers, extracting the 100% parameter schema, and compiling validated `.cfg` profiles.

- **Dependencies**: Python ≥ 3.10 (standard library only, except `xim_decrypt.py` requires `cryptography`) and .NET SDK 8 only when rebuilding `ximgen/`.

```text
FMX65.Ver.03.01.01.Rev.15_ID1.e.xim ──xim_decrypt.py────▶ fw_image.bin (+ sha256)
cfgs/device_export_original.cfg     ──cfg_tool.py read──▶ cfg_parsed.json (header + 11,688 params)
brand_xml/*.xml                     ──build_schema.py───▶ static *_schema.json (44.81% coverage)
bundle + brand                      ──ximgen (.NET 8)───▶ re/generated_FMC650_spec1_cfg4.43.1.0.xml
static schema + generated XML       ──merge_generator.py▶ 100% re/fmx65_03.01.01.Rev.15_*
cfgs/device_export_original.cfg     ──make_cfg.py───────▶ validated .cfg (custom edits or --preset all)
```

---

## Tool Catalog (1 Tool Per Function)

| Tool | Single Responsibility | Inputs → Outputs |
| :--- | :--- | :--- |
| **[`cfg_tool.py`](cfg_tool.py)** | **Binary & Text `.cfg` Codec** (`read`, `write`, `verify`, `parse_text`, `build_text`) | `.cfg` (GZip `mtime=0` or UTF-8) ↔ `(header, params)` JSON/dict with round-trip & key-set invariance checks |
| **[`make_cfg.py`](make_cfg.py)** | **Authoritative `.cfg` Validator, Preset Builder & Compiler** | Reference `.cfg` + (`PID=value` edits or `--preset all`) → Validated `.cfg` checked against `re/generated_FMC650_spec1_cfg4.43.1.0.xml` and `re/fmx65_03.01.01.Rev.15_schema.json` |
| **[`build_schema.py`](build_schema.py)** | **Static XML Schema Extractor (Stage 1)** | `Brand.dll` XML folder + `cfg_parsed.json` → Static `*_schema.json`, `*_report.json`, `*_gaps.json` (`44.81%` coverage) |
| **[`merge_generator.py`](merge_generator.py)** | **Compiler XML & `IOItem` Schema Merger (Stage 2)** | `generated_FMC650_spec1_cfg4.43.1.0.xml` + static schema + `Brand.dll` XMLs → `100%` `re/fmx65_03.01.01.Rev.15_{schema.json,parameters.csv,report.json,gaps.json}` |
| **[`xim_decrypt.py`](xim_decrypt.py)** | **`.xim` Firmware Container Decryptor** | `FMX65.Ver.*.e.xim` (`TLTF` + PBKDF2-HMAC-SHA1 + AES-256-CBC + GZip) → raw `fw_image.bin` |
| **[`ximgen/`](ximgen/Program.cs)** | **Vendor `Configuration.Generator` .NET 8 Harness** | Unpacked Configurator DLLs + `FMB640` brand XMLs → `re/generated_FMC650_spec1_cfg4.43.1.0.xml` + `_ids.txt` |

---

## 1. `cfg_tool.py` — `.cfg` Container & Grammar Codec

- **Container**: Single GZip member (`mtime=0`); payload is the UTF-8 parameter stream.
- **Grammar**: `ConfigurationVersion:<v>;HwVersion:<hw>;Title:<t>;FmType:<fm>;SpecId:<n>;` followed by ascending `id:value;` pairs.
- **Continuation Rule**: A new parameter starts only at `^\d+:` with an integer ID strictly greater than the previous ID. Any embedded `;` without a strictly increasing numeric prefix stays attached to the previous value (preserving `PID 181334` = `0;10:FMC650DEMO`).

```bash
python tools/cfg_tool.py read   cfgs/device_export_original.cfg cfg.json
python tools/cfg_tool.py write  cfg.json out.cfg
python tools/cfg_tool.py verify cfgs/device_export_original.cfg
```

---

## 2. `make_cfg.py` — Validator, Preset Generator & `.cfg` Compiler

Enforces every rule documented in [`../mds/FMC650_CFG_Save_Failure_Debugging_Report.md`](../mds/FMC650_CFG_Save_Failure_Debugging_Report.md) so neither a human nor an AI agent can generate a `.cfg` that fails Teltonika Configurator's `"Save to device"` check:

1. **Anchor-Set Invariance**: Copies the exact parameter ID set from the reference `.cfg` (`11,688` IDs on `4.43.1.0` or `7,963` IDs on `4.41.0.0`) and refuses any out-of-anchor ID.
2. **Manual CAN Requests (`17000..17699`) Hex & Offset Guard**:
   - `17000, 17010, …, 17690` (`Req ID`, `+0`): Must be an **exact 8-character hex string** (default `'00000000'`, never `'0'` or `''`; `+1` is `RTR`).
   - `17002, 17012, …, 17692` (`Payload`, `+2`): Must be an **exact 16-character hex string** (default `'0000000000000000'`, never `'0'` or 8-char `'00000000'`).
3. **Manual CAN I/O Reception `CanId` (`47002..47292`, `90002..90492`, `+2`) Decimal Guard**:
   - Stored in `.cfg` as a **decimal `UInt32`** (`0..4294967295`, e.g. `'419360512'` for `0x18FEEF00`). If a hex string is passed, validation rejects it and outputs the exact decimal conversion.
4. **Strict `<CollectionConfiguration>` Enum Membership (81 XML Tables)**:
   - Rejects `PID 47500 = '0'` (`Tachograph Data -> Timestamp -> Priority` uses `TimestampCollection = {'1': 'Low', '2': 'High', '3': 'Panic'}`).
   - Enforces all 5 `<Operand>` collections (`OperandCollection`, `OperandCollectionKLN`, `OperandCollectionKLNTimestamp`, `OperandCollectionLimited`, `OperandCollection_ainps`).

```bash
# Custom PID=value compilation:
python tools/make_cfg.py cfgs/device_export_original.cfg cfgs/custom.cfg 1000=120 1001=5 47500=1

# Regenerate all 5 Fleet Telematics v1.2 profiles into cfgs/:
python tools/make_cfg.py --preset all
```

---

## 3. `build_schema.py` & `merge_generator.py` — Schema Pipeline

- **`build_schema.py`**: Extracts static `ParameterId` attributes, `ListConfiguration` ranges, `Geozones`, and `Polygon` arithmetic from `Brand.dll` XMLs (`44.81%` coverage alone).
- **`merge_generator.py`**: Merges `re/generated_FMC650_spec1_cfg4.43.1.0.xml` and expands `IOItem` blocks (`IoId + 0..5`) to reach **100.0% (`11,688 / 11,688`) coverage**.

---

## 4. `xim_decrypt.py` & `ximgen/` — Firmware & Compiler Extraction

- **`xim_decrypt.py`**: Decrypts `FMX65.Ver.*.e.xim` using the deobfuscated vendor constant (`b[i] ^= (i & 0xFF) ^ 0xAA`), PBKDF2-HMAC-SHA1 (`1000` iterations), AES-256-CBC, and single-member GZip decompression.
- **`ximgen/`**: .NET 8 C# driver that loads `Configuration.Generator.dll` and `FMB.Core.dll` with offline license stubs (`StubKey`, `StubExt`) and invokes `GenerateConfiguration(new HardwareVersion("FMC650:1"), "FMC650", new Version(4,43,1,0), ...)`.
