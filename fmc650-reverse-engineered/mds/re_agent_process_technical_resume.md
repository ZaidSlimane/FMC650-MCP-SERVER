---
title: FMC650 / FMX65 reverse engineering — corrected technical resume
supersedes: the earlier architecture narrative (cipher, cfg encoding, and generator-pipeline ordering in it were fabricated or inverted)
validated: 2026-11-05 (every number below re-measured against the artifacts)
---

# Corrected Technical Write-Up

## Phase 1: `.xim` Decryption

The cipher is **AES-256-CBC**, not a keystream XOR:

```
password = base64decode("hX9Xe0ttKg0SOCPRbAjdAcPy6VD96NRYo9GQ00MrEfU=")  # vendor constant
           # recovered from obfuscated string blob: b[i] ^= (i & 0xFF) ^ 0xAA over 0x56E bytes
key      = PBKDF2-HMAC-SHA1(password, salt_from_header, 1000, dkLen=32)
plain    = AES-256-CBC-decrypt(key, IV_from_header, payload)
image    = inflate(plain)
```

Container layout: `TLTF|ver|reserved|saltLen@16|salt@20|ivLen@52|IV@56|payloadLen@72|payload@76|sigLen|RSA sig`. Exact size: 76 + 1,037,776 + 4 + 128 = **1,037,984 bytes**. Output matches SHA256 `e20fafd9…39195`.

Independent re-run (`tools/xim_decrypt.py`): same sha256; **both other `.xim` files decrypt with the same constant** (Rev.28_ID1 → 1,042,616 B `e4e44f7d…`, Rev.34_ID1666 → 944,696 B `c1250b7f…`, both gzip-plaintext).

## Phase 2: `.cfg` Format

The `.cfg` is **one gzip member wrapping plain text**. Not binary, not LEB128, no header:

```
ConfigurationVersion:4.43.1.0;HwVersion:FMC650_1;Title:03.01.01+ (Automatic source);FmType:FMC650;SpecId:1;
100:1;101:1;102:0;…;181334:0;10:FMC650DEMO;
```

The only parsing trap: a new parameter starts only when `^(\d+):` **and** the id exceeds the previous id. In `181334:0;10:FMC650DEMO`, the `10` is not a parameter — it is part of the value because `10 < 181334`. A naive `split(';')` invents parameter `10`.

Container bytes are not reproducible: vendor `os` byte is `0x0A`; closest reproduction is SharpZipLib level 5 at 27,423 B vs 27,370 B. Only the text payload is byte-exact (`sha256 a1c8c712…4c315d`).

Independent re-run (`tools/cfg_tool.py verify` + a from-scratch JSON→text→gzip round trip): text identical, header reproduced, `181334` continuation preserved, all 11,688 params reparsed equal.

## Phase 3: Generator Pipeline

The blocker was `SpecFactory.BuildSpecs` — 266 `<Spec Id="1001" PatchNo="1"/>` references in `BaseExtension` caused `InvalidConfigurationException: Unable to find spec id(1001) configuration file`. The fix was **removing those patch refs** and **dropping the `BuildSpecs` call entirely** — the opposite of the earlier diagram.

Actual driver construction (`tools/ximgen/`):

```csharp
var familySettings = new FamilySettings(dirPath, specFilePaths, expFilePaths, loadedFromAssembly);
var stubExt = new StubExt { CanUse = true };  // ExtensionsService.RefreshKeys() NREs offline
var provider = ConfigurationProviderFactory.Create(familySettings, stubExt, specFiles);
var result = provider.GenerateConfiguration(HardwareId.FMC650, "FMC650", version, specId);
```

`FamilySettings` needs **absolute paths** whose basenames match the vendor resource names. Result: `generated_FMC650_spec1_cfg4.43.1.0.xml`, 1,150 distinct ids, 18,139 elements.

## Phase 4: Numbers (measured)

| Claim | Corrected value |
|---|---|
| "2,445 bases × 6 = 6,452" | 2,445 × 6 = **14,670** (the full universe). **6,451** are the base ids *present in the cfg* and not claimed by a stronger mechanism (after the attribution fix below). |
| "35 polygons × 8 × 6 = 1,680" | **100 blocks × 16 ids present in the cfg.** By source: 96 fully-Polygon blocks = 96·16; the 4 tail blocks' remaining ids are literal `ParameterId`s → Polygon covers 96·16 + 14 + 13 + 10 + 8 = **1,581**. |
| "100 geozones × 20 × 6 = 1,100" | 100 blocks × **11** ids = 1,100. Stride is 20; offset **3 is systematically absent** (measured orders 0,1,2,4…11 — each exactly 100×). |
| "All 4,157 residuals have `mod10 == 5`" | Two stages: width-5 over the full base set gave 4,157 unknown; the 109 at `base+5` appeared at the next stage (11,579 → 11,688). Measured: exactly **109** ids sit at base+5 (order-5 histogram). |
| `verify()` tautology | Removed with the fabricated narrative; `tools/cfg_tool.py verify` checks the real property (text round-trip identity). |

## Phase 5: Record Schema

Real field names from `fmx65_03.01.01.Rev.15_parameters.csv`:

```
element, label, default, collection, source, origin, branch, static_source,
id, in_cfg, cfg_value, ambiguous
```

Not: `ioitem_base`, `field_index`, `source: "xml:Generator"`.

## Attribution fix applied during validation

Re-running the tool chain reproduced the checked-in report exactly — **with one correction**: `merge_generator.py`'s IOItem pass overwrote id **48100**, which the vendor XML defines as `<NumberInput ParameterId="48100" Label="Default data request period" Min="0" Max="300" Units="s">` (also emitted by the compiled generator document). The pass now skips ids that a literal/generator definition already claims; only coincidental block matches are affected.

Corrected source breakdown (sums to 11,688):

| source | cfg ids |
| --- | --- |
| `generator:FMC650:1` | 1,149 |
| `xml:ParameterId` | 126 |
| `xml:ListConfiguration` | 1,281 |
| `xml:Geozones` | 1,100 |
| `xml:Polygon` | 1,581 |
| `generator:IOItem` | 6,451 |

**What holds:** coverage progression (44.81% → 64.43% → 100%), width-6 rule `id = IoId + order`, geozone/polygon stride, `PropertyVault` dead-end, `PropertyIdCalulator` vendor misspelling, the `dnfile` `ParamList` quirk, and every "not solved" row. `analysis_report.md`, `cfg_format.md`, and `xim_decryption.md` are consistent with the artifacts.

## Independent end-to-end re-validation (this session)

1. `cfg_tool.py verify` on the original download: `text_identical: True`, sha256 pair matches.
2. JSON → text → gzip → parse round trip: identical; 11,688 params; continuation preserved.
3. `xim_decrypt.py` on all three `.xim` files: gzip-plaintext images, sha256 of target matches the archived `fw_image.bin`.
4. `build_schema.py` re-run reproduces 5,237 / 44.81% exactly; generator merge reaches **11,688 / 11,688 (100.0%)**; report JSON is byte-equal (canonical) to the checked-in one.
5. No IOItem-attributed id has more than one competing base; the single static-demotion case (48100) is fixed in the tool and reflected in the re-exported schema/CSV/report.

Operational note: `merge_generator.py` takes **five** arguments — the brand-XML directory is the fifth and is required for the 6,451 IOItem attributions; omitting it silently yields only the 2,379 generator-document IOItems (65.16%).
