# FMC650 `.cfg` Debugging Report — Investigating & Resolving `"Failed to be saved on device"`

- **Date**: 2026-11-08
- **Target Device**: Teltonika FMC650 (`HwVersion: FMC650_1`, `FmType: FMC650`, `SpecId: 1`)
- **Target Firmware**: `03.01.01.Rev.15` (`ConfigurationVersion: 4.43.1.0`) & `01.02.10` (`ConfigurationVersion: 4.41.0.0`)
- **Anchor Configuration**: `fmc650-reverse-engineered/cfgs/sendperiod_overspeed_config_rev15.cfg` (`11,688` parameters)
- **Symptom**: Loading the first generated `FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg` in Teltonika Configurator succeeded, but clicking **"Save to device"** triggered **"Failed to be saved on device"**.

---

## 1. Problem Statement & Initial Hypotheses

When Teltonika Configurator opens a `.cfg` file, it decompresses the GZip stream, parses the header and `id:value;` pairs, and binds each parameter ID to its UI controls defined in the device's compiled XML configuration schema (`generated_FMC650_spec1_cfg4.43.1.0.xml`).

However, **loading a `.cfg` into the Configurator UI is much more permissive than saving it to a physical FMC650 device**:
- During **Load from file**, Configurator populates UI controls on a best-effort basis.
- During **Save to device**, Configurator and the FMC650 firmware enforce:
  1. **Strict XML Validation Rules** (`Validate="Length(a,b); Hex"`, `Regex(...)`, numeric `[Min, Max]` bounds, and `ParameterType` width).
  2. **Strict Enum / `<CollectionConfiguration>` Membership** (every dropdown / `Collection` parameter must contain a value present in its `<CollectionItem>` set; otherwise the UI control has `SelectedItem = null` and fails serialization/device flush).
  3. **Hardware / Firmware Version Compatibility** (`ConfigurationVersion` and parameter ID support on the connected physical device).
  4. **Device Keyword Matching** (`ParameterId="10"`, e.g. `10:FMC650DEMO`).

---

## 2. Step-by-Step Debugging Process

### Step 1: Container & Structural Verification (`investigate_cfg_save_fail.py`)

We first compared the binary GZip container and text structure of the failing `FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg` against all 7 real truck `.cfg` exports in `fmc650-reverse-engineered/cfgs/`:
- `sendperiod_overspeed_config_rev15.cfg` (`ConfigurationVersion: 4.43.1.0`, `11,688` params)
- `my_solid.cfg` (`ConfigurationVersion: 4.43.1.0`, `11,688` params)
- `F15_TR115.cfg` (`ConfigurationVersion: 4.41.0.0`, `7,963` params)
- `fmc650.cfg` (`ConfigurationVersion: 4.41.0.0`, `7,963` params)
- `FMC650_TRIAL_CONFIG.cfg` (`ConfigurationVersion: 4.41.0.0`, `7,963` params)
- `F32_TR106.cfg` (`ConfigurationVersion: 4.40.20.0`, `9,919` params)
- `OLD CONFIF_TR84_TRIAL.cfg` (`ConfigurationVersion: 4.40.20.0`, `9,919` params)

**Findings from Step 1**:
- The GZip container, UTF-8 CRLF line endings, header order, parameter count (`11,688`), parameter ID ordering, and the trailing continuation token (`181334:0;10:FMC650DEMO;`) were **100% identical** to `sendperiod_overspeed_config_rev15.cfg`.
- Therefore, the failure was **not** a GZip format or token-order issue — it had to be caused by one or more **invalid parameter values** among the **324 parameters** modified by `generate_fleet_cfgs.py`, or by a firmware mismatch on the target unit.

---

### Step 2: Deep Audit of All 324 Modified Parameters (`deep_audit_cfg.py`)

Next, we wrote `deep_audit_cfg.py` to diff every single modified parameter (`base != p2`) between `sendperiod_overspeed_config_rev15.cfg` and `FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg`, printing the schema metadata (`type`, `min`, `max`, `default`, `validate`, `collection`, `label`) for each of the 324 changes.

This immediately exposed **Root Cause #1** in the `17000..17699` range (`Manual CAN Requests`):

```text
PID 17000: base='00000000'         p2='0'         type=String def='00000000'         val='Length(0,8); Length(8,8); Hex' label=Req ID
PID 17001: base='0'                p2='0'         type=Byte   def='0'                val=None                            label=RTR
PID 17002: base='0000000000000000' p2='00000000'  type=String def='0000000000000000' val='Length(0,16); Length(8,16); Hex' label=Payload
PID 17003: base='0'                p2='0'         type=Int32  def='0'                val=None                            label=Request Period
PID 17004: base='0'                p2='0'         type=Int32  def='0'                val=None                            label=Requested data length
```

#### Why `make_cfg.py` Missed It
In `tools/make_cfg.py` (lines 46–52), string validation was implemented as:
```python
rx = schema_entry.get("validate") or ""
if rx.startswith("Regex"):
    ...
```
Because `PID 17000`'s validation rule is `"Length(0,8); Length(8,8); Hex"` (which does **not** start with `"Regex"`), `make_cfg.py` silently passed `'0'`!

#### What `generate_fleet_cfgs.py` Did Wrong on `17000..17699`
In the initial version of `generate_fleet_cfgs.py`, the loop disabling Manual CAN Requests assumed `+0` was `RTR` and `+2` was `Req ID`:
```python
# BUGGY CODE (Initial version):
for base in range(17000, 17700, 10):
    edits[str(base)] = "0"             # BUG: base+0 is Req ID (requires 8 hex chars '00000000'!), NOT RTR!
    edits[str(base + 1)] = "0"         # base+1 is RTR
    edits[str(base + 2)] = "00000000"  # BUG: base+2 is Payload (default 16 hex chars '0000000000000000'!)
```
This corrupted **70 `Req ID` parameters (`17000, 17010, ..., 17690`)** to `'0'` (length `1` instead of `8` hex characters) and truncated **70 `Payload` parameters (`17002..17692`)** from 16 hex characters to 8. Furthermore, in `sendperiod_overspeed_config_rev15.cfg`, all 70 Manual CAN Request slots were **already disabled** with their valid factory defaults (`+0='00000000'`, `+1='0'`, `+2='0000000000000000'`, `+3='0'`, `+4='0'`).

---

### Step 3: Discovering Schema Label Collision & Auditing Against the True Compiler XML (`audit_true_xml.py`)

While inspecting the remaining modified parameters in `deep_audit_cfg.py`, we noticed something strange in `fmx65_03.01.01.Rev.15_schema.json`:
- In `fmx65_03.01.01.Rev.15_schema.json`, `PID 46020` was labeled `Distance to next service`, `PID 47000` was labeled `CSF Air Conditioning`, and `PID 47500` was labeled `ISF Low Washer Fluid Level Indicator`.
- Why? Reviewing `re/analysis_report.md` (§8) revealed that when `merge_generator.py` scanned all 150 vendor XML files in `Brand.dll` (which include LV-CAN200 / ALL-CAN300 definitions for other device families), secondary XML files overwrote the `IOItem` labels for `46020..47990`.
- However, **`re/generated_FMC650_spec1_cfg4.43.1.0.xml`** is the exact XML emitted by Teltonika's own `ConfigurationProvider.GenerateConfiguration(FMC650:1, "FMC650", 4.43.1.0, specId 1)` compiler for the FMC650!

We wrote `audit_true_xml.py` to parse `generated_FMC650_spec1_cfg4.43.1.0.xml` directly, extracting:
1. All **81 `<CollectionConfiguration>` enum tables** (`PriorityCollection`, `TimestampCollection`, `OperandCollection`, `OperandCollectionKLN`, `OperandCollectionKLNTimestamp`, `CanTypeCollection`, `CanSrcCollection`, `SortBy`, etc.).
2. All **`<IOItem>` blocks and child offsets** (`Priority`, `Operand`, `HighLevel`, `LowLevel`, `EventOnly`, `AverageConstant`, and Manual CAN `CanType`, `DataMask`, `CanId`, `CanSrc`, `Operand`).
3. All **`Validate` and `Min`/`Max` attributes**.

Running `audit_true_xml.py` against the failing `.cfg` pinpointed **Root Cause #2**:

```text
[FAIL] PID 47500 (Timestamp -> Priority): base='1' -> p2='0' | INVALID COLLECTION VALUE '0' for TimestampCollection (allowed={'1': 'Low', '2': 'High', '3': 'Panic'})
```

#### Why `PID 47500 = '0'` Breaks Saving to Device
In `generated_FMC650_spec1_cfg4.43.1.0.xml` (lines 13704–13719), `IoId="47500"` is **`Tachograph Data -> Timestamp`**:
```xml
<IOItem IoId="47500" Name="Timestamp">
  <Priority Collection="TimestampCollection" Default="1">
    <CollectionConfiguration Name="TimestampCollection" CollectionType="Byte">
      <CollectionItem Text="Low" Value="1" />
      <CollectionItem Text="High" Value="2" />
      <CollectionItem Text="Panic" Value="3" />
    </CollectionConfiguration>
  </Priority>
  <EventOnly Collection="EventOnlyCollection" Default="0">...</EventOnly>
  <Operand Collection="OperandCollectionKLNTimestamp" ControlType="DropDownList" Default="3">
    <CollectionConfiguration Name="OperandCollectionKLNTimestamp" CollectionType="Byte" CollectionControlType="DropDownList">
      <CollectionItem Text="Monitoring" Value="3" />
    </CollectionConfiguration>
  </Operand>
</IOItem>
```
Unlike standard `IOItem`s whose `Priority` uses `PriorityCollection` (`0=None, 1=Low, 2=High, 3=Panic`), **`PID 47500` uses `TimestampCollection` which ONLY allows `'1'`, `'2'`, or `'3'` (`Low`, `High`, `Panic`) — `'0'` does NOT exist!**
- In `generate_fleet_cfgs.py`, the loop `for io_id in range(47500, 48000, 10): set_io_block(..., priority="0")` forced `PID 47500 = '0'`.
- Checking all 7 real truck `.cfg` exports (`check_mcan_across_cfgs.py`) confirmed that `PID 47500` is **never `'0'`** in any valid config (`'1'` in `sendperiod_overspeed_config_rev15.cfg`, `F15_TR115.cfg`, `fmc650.cfg`, `my_solid.cfg`; `'2'` in `F32_TR106.cfg` and `OLD CONFIF_TR84_TRIAL.cfg`).

---

### Step 4: Cross-Checking Against All 7 Real Fleet `.cfg` Exports (`compare_all_diffs_with_real_cfgs.py`)

We then cross-checked every remaining difference against all 7 real truck `.cfg` files from the FLEET fleet and found two important operational configurations in `sendperiod_overspeed_config_rev15.cfg` that should **not** be disabled:

1. **Fleet J1939 Passive Manual CAN Slots `CAN0..CAN23` (`47000..47090`, `47200..47290`, `90000..90030`)**:
   - In `generated_FMC650_spec1_cfg4.43.1.0.xml`, `IoId="47000..47090"` (`CAN0..CAN9`), `47200..47290` (`CAN10..CAN19`), and `90000..90030` (`CAN20..CAN23`) are **passive Manual CAN I/O reception slots** (AVL IDs `145..168`, `can_0..can_23`), **not** active CAN transmissions.
   - Across all 7 real truck `.cfg` files (`F15_TR115.cfg`, `F32_TR106.cfg`, `sendperiod_overspeed_config_rev15.cfg`, etc.), those 24 slots are pre-configured to passively read J1939 PGNs (`0x18FEEF00`, `0x18FEEE00`, `0x18F00400`, `0x18F00503` ZF TraXon gear, `0x18FEF803` transmission oil temp, `0x18FEAE21` pneumatic pressures, `0x18FECA00` DM1 faults, etc.) used by Wialon's existing sensors.
   - Disabling `47000..47090`, `47200..47290`, and `90000..90030` stripped those 24 passive J1939 channels.

2. **Dual-Server Wialon + Flespi Configuration (`PID 2004..2010`)**:
   - In `sendperiod_overspeed_config_rev15.cfg`, `Server #1` (`2004..2006`) is Wialon (`203.0.113.10:20332`) and `Server #2` (`2007..2010`) is Flespi (`ch0000000.flespi.gw:20001`, `Mode = 2`).
   - This is the exact dual-server setup for which `Response Timeout = 5 s` (`PID 1001 = 5`) was requested (so a lag on Wialon/m2m.sim2 never blocks Flespi for 30 seconds).

3. **Hardware Firmware Generation (`4.43.1.0` vs `4.41.0.0`)**:
   - Diffing `sendperiod_overspeed_config_rev15.cfg` (`4.43.1.0`, `11,688` params) against `F15_TR115.cfg` (`4.41.0.0`, `7,963` params) showed only 8 value differences across all `7,963` shared parameters, proving `sendperiod_overspeed_config_rev15.cfg` is the `03.01.01.Rev.15` upgrade of `F15_TR115.cfg`.
   - However, if a physical FMC650 connected via USB is still running firmware `01.02.10` (`4.41.0.0`), it will reject a `4.43.1.0` `.cfg` because firmware `01.02.10` lacks `PID 330` and the `103000..104590` TrailerCAN table.

---

## 3. Summary of Fixes Applied in `generate_fleet_cfgs.py`

| Issue Found | Broken Value in Earlier `.cfg` | Fixed Value in Final `.cfg` | Why It Failed Previously |
|---|---|---|---|
| **Manual CAN Request `Req ID`** (`17000, 17010, …, 17690`) | `'0'` (1 char) | `'00000000'` (8 hex chars, untouched from base) | Violated XML `Validate="Length(0,8); Length(8,8); Hex"` across all 70 slots |
| **Manual CAN Request `Payload`** (`17002, 17012, …, 17692`) | `'00000000'` (8 chars) | `'0000000000000000'` (16 hex chars, untouched from base) | Truncated factory default 8-byte hex payload |
| **Tachograph `Timestamp -> Priority`** (`PID 47500`) | `'0'` (`None`) | `'1'` (`Low`, untouched from base) | Violated XML `TimestampCollection` (`allowed = {'1', '2', '3'}`); `'0'` is not in enum |
| **`IOItem` Operands (`+1`)** (`46311, 46511, 46581..46611, 46801, 46891`) | Altered between `'3'` and `'5'` | Preserved base `.cfg` `<Operand>` values | Prevented `<Operand>` collection mismatches |
| **Passive J1939 `CAN0..CAN23`** (`47000..47090, 47200..47290, 90000..90030`) | `'0'` (`Disabled`) | `'2'` (`Extended 29-bit`, untouched from base) | Preserved existing Wialon `can_0..can_23` J1939 sensors |
| **Dual-Server Wialon + Flespi** (`2004..2010`) | Swapped & disabled `2010='0'` | Untouched (`Server 1 = Wialon`, `Server 2 = Flespi`, `2010='2'`) | Preserved active dual-server telemetry |

---

## 4. Verification & Final Deliverables

We embedded `load_true_xml_validator()` and `validate_against_true_xml()` directly inside `generate_fleet_cfgs.py` so that every generated `.cfg` file is automatically checked against **both** `generated_FMC650_spec1_cfg4.43.1.0.xml` (all 81 `<CollectionConfiguration>` enums, `Length(a,b); Hex` rules, and `[Min, Max]` ranges) and `fmx65_03.01.01.Rev.15_schema.json` before writing.

### Final Verification Output
```text
[OK] FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg: 73 params modified from base (0 XML/Hex/Collection errors), 11688 total IDs, ver=4.43.1.0, size=27616 B
[OK] FMC650_FLEET_P2_SURGICAL_rev15.cfg: 37 params modified from base (0 XML/Hex/Collection errors), 11688 total IDs, ver=4.43.1.0, size=27598 B
[OK] FMC650_FLEET_P1_PILOTE_HR_v1.2_rev15.cfg: 76 params modified from base (0 XML/Hex/Collection errors), 11688 total IDs, ver=4.43.1.0, size=27606 B
[OK] FMC650_FLEET_P0_DECOUVERTE_v1.2_rev15.cfg: 45 params modified from base (0 XML/Hex/Collection errors), 11688 total IDs, ver=4.43.1.0, size=27574 B
[OK] FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg: 41 params modified from base (0 XML/Hex/Collection errors), 7963 total IDs, ver=4.41.0.0, size=18941 B
```
