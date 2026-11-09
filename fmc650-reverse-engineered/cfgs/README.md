# FMC650 Configuration Profiles & Reference Anchors (`cfgs/`)

This directory holds all **reference anchor `.cfg` exports**, **raw text payload captures**, and **validated production `.cfg` profiles** for the Teltonika FMC650.

Every `.cfg` binary file in this folder is a single-member GZip stream (`mtime=0`) wrapping a UTF-8 parameter stream of the form:
```text
ConfigurationVersion:<v>;HwVersion:FMC650_1;Title:<title>;FmType:FMC650;SpecId:1;<id>:<value>;...
```
All files are verified by [`../tools/cfg_tool.py`](../tools/cfg_tool.py) and [`../tools/make_cfg.py`](../tools/make_cfg.py) with **zero XML, hexadecimal, or `<CollectionConfiguration>` errors**.

---

## 1. Reference Anchor & Format Verification Files

| File | Config Version | Target Firmware | Param Count | Size (Bytes) | Purpose |
| :--- | :---: | :---: | :---: | :---: | :--- |
| [`device_export_original.cfg`](device_export_original.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `27,370` | **Primary hardware export anchor.** Ground-truth ID set (`100..181334`, including continuation `181334:0;10:FMC650DEMO`) and factory restore baseline. |
| [`device_export_original_text_payload.cfg`](device_export_original_text_payload.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `99,176` | Decompressed UTF-8 text payload of `device_export_original.cfg` (SHA-256 `a1c8c712…`). |
| [`my_solid_upload_test.cfg`](my_solid_upload_test.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `27,544` | Proof-of-concept `.cfg` built without Configurator (3 APN edits: `2001`, `2002`, `2003`), accepted by Teltonika Configurator on load. |
| [`my_solid_upload_test_text_payload.cfg`](my_solid_upload_test_text_payload.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `99,181` | Decompressed UTF-8 text payload of `my_solid_upload_test.cfg` (SHA-256 `126ef6ac…`). |

---

## 2. Fleet Telematics v1.2 Fleet Production Profiles

All five fleet profiles are deterministically compiled by `python ../tools/make_cfg.py --preset all` and validated against [`../re/generated_FMC650_spec1_cfg4.43.1.0.xml`](../re/generated_FMC650_spec1_cfg4.43.1.0.xml) and [`../re/fmx65_03.01.01.Rev.15_schema.json`](../re/fmx65_03.01.01.Rev.15_schema.json):

| Profile File | Config Version | Target Firmware | Param Count | Modified from Base | Operational Role |
| :--- | :---: | :---: | :---: | :---: | :--- |
| [`FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg`](FMC650_FLEET_P2_PRODUCTION_v1.2_rev15.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `73` | **Primary Fleet Production Profile (Rev.15).** Enables network/FIFO optimizations (`1000=120`, `1001=5`, `1002=1`), 40 Weight/WABCO TEBS-E TrailerCAN (`330=2`, `103000..104590`), FMS Axle 1–4 weights (`46100..46130`), FMS temperatures (`46790..46900`), DOUT2 safety (`11003=1`, `11103=1`), and P2 acquisition (`60s` moving / `300s` stationary). |
| [`FMC650_FLEET_P2_SURGICAL_rev15.cfg`](FMC650_FLEET_P2_SURGICAL_rev15.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `37` | **Surgical Weight + Queue Patch (Rev.15).** Modifies *only* the network/FIFO parameters (`1000..1006`) and the 40 Weight/TrailerCAN parameters (`330`, `45290..45330`, `46530`, `103000..104590`), leaving all other acquisition/FMS parameters identical to the truck's base config. |
| [`FMC650_FLEET_P1_PILOTE_HR_v1.2_rev15.cfg`](FMC650_FLEET_P1_PILOTE_HR_v1.2_rev15.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `76` | **High-Resolution Pilot Profile (Rev.15).** Same telemetry & safety set as `P2_PRODUCTION`, but with high-resolution P1 acquisition (`15s` min period, `30s` send period, `50m` distance, `5°` angle) for calibration and field testing. |
| [`FMC650_FLEET_P0_DECOUVERTE_v1.2_rev15.cfg`](FMC650_FLEET_P0_DECOUVERTE_v1.2_rev15.cfg) | `4.43.1.0` | `03.01.01.Rev.15` | `11,688` | `45` | **Tractor-Only Discovery Profile (Rev.15).** Same as `P2_PRODUCTION`, but with native TrailerCAN disabled (`330=0` and `103000..104590` Priority=`0`) for tractors operating without an ISO 11992-2 EBS trailer. |
| [`FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg`](FMC650_FLEET_P2_PRODUCTION_v1.2_fw010210.cfg) | `4.41.0.0` | `01.02.10` | `7,963` | `41` | **Legacy Firmware Compatible Production Profile (`01.02.10`).** Anchored on the `7,963`-parameter `4.41.0.0` ID set for units not yet upgraded to `03.01.01.Rev.15` (applies all network, LVCAN/FMS weight, safety, and P2 acquisition rules supported by `4.41.0.0`). |

---

## 3. Critical `.cfg` Integrity Rules Enforced

See [`../mds/FMC650_CFG_Save_Failure_Debugging_Report.md`](../mds/FMC650_CFG_Save_Failure_Debugging_Report.md) for the full root-cause investigation:
1. **Never alter the parameter ID set** of the reference `.cfg` (`11,688` IDs for `4.43.1.0`; `7,963` IDs for `4.41.0.0`).
2. **Manual CAN Requests (`17000..17699`)** keep their valid hex defaults (`+0 Req ID = '00000000'` 8 hex chars; `+2 Payload = '0000000000000000'` 16 hex chars).
3. **Tachograph Timestamp Priority (`PID 47500`)** uses `TimestampCollection` (`1=Low, 2=High, 3=Panic`) and is never set to `'0'`.
4. **Passive J1939 Manual CAN slots `CAN0..CAN23` (`47000..47090`, `47200..47290`, `90000..90030`)** and **Dual-Server Wialon (`2004..2006`) + Flespi (`2007..2010`)** are preserved untouched.
