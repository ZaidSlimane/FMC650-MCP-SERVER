# Wialon Parameter & Sensor Mapping (`wialon-parameters`) â€” Part 2: Flespi <-> Wialon (`FMC650_TEST_TR84_UNIT_PROFILE.wlp`)

This folder contains **Part 2** of the end-to-end telemetry & configuration mapping pipeline for the **Teltonika FMC650**:
- **Part 1 ([`../flespi-parameters/`](../flespi-parameters/README.md))**: Teltonika FMC650 (`re/` Configuration `PID`s & `Data_Sending_Parameters_ID/` Telemetry `AVL ID`s) <-> **Official Flespi Settings, Commands, and 1,161 Telemetry Parameters**.
- **Part 2 (`wialon-parameters/` â€” this directory)**: **Official Flespi Telemetry Parameters & Cloud Plugins <-> Wialon Message Parameters (`p`) & Unit Sensors (`FMC650_TEST_TR84_UNIT_PROFILE.wlp`)**.

---

## Core Architectural Principles Enforced

1. **Never confuse telemetry parameters with configuration parameters.**
   - **Configuration parameters (`Parameter ID` / `PID`)** configure the tracker's internal behavior in flash memory (`re/fmx65_03.01.01.Rev.15_schema.json`). They are **never** streamed to Wialon as sensor parameters.
   - **Telemetry parameters (`AVL ID` -> Flespi dotted parameter -> Wialon parameter `p`)** are live measurements carried inside Codec 8 / Codec 8E packets and evaluated by Wialon unit sensors.
2. **Never assume a manufacturer parameter maps directly to a Flespi setting or Wialon sensor.**
   - When streaming from Flespi to Wialon (**Path A**), Flespi transforms its dotted parameter names into abbreviated underscore keys (`can.engine.load.level` -> `can_eng_load_lvl`) and applies legacy Wialon Retranslator overrides (`tacho.vehicle.mileage` -> `tco_distance`, `can.fuel.level` -> `fuel_lvl`, `can.engine.motorhours` -> `eng_mth`).
   - When connecting an FMC650 directly to Wialon without Flespi (**Path B**), Wialon names parameters `io_<AVL_ID>` (`io_85`, `io_192`, `io_239`). Therefore, a `.wlp` sensor profile built for Flespi streaming (`FMC650_TEST_TR84_UNIT_PROFILE.wlp`) **will not work** on a direct Teltonika-to-Wialon connection without remapping the parameter keys and scaling constants.
   - Furthermore, **58 of the 147 sensors** in `FMC650_TEST_TR84_UNIT_PROFILE.wlp` (`fleet_*` and `vhc_*`) do **not** come from raw Teltonika `AVL ID`s at allâ€”they are synthesized in the Flespi cloud by the custom **`tidj` Weight & Cargo Fraud-Detection Plugin**!

---

## Deliverables in This Directory

| File | Description |
| :--- | :--- |
| **[`FMC650_00_UNIFIED_PARAMS.md`](./FMC650_00_UNIFIED_PARAMS.md)** | Unified FMC650 parameter inventory, independent of the TR84 test unit. |
| **[FMC650_01_TRANSLATION_ARCHITECTURE.md](./FMC650_01_TRANSLATION_ARCHITECTURE.md)** | Complete 3-stage pipeline architecture (`FMC650` -> `Flespi` -> `Wialon`), **Path A (Flespi Stream)** vs **Path B (Direct `io_<AVL_ID>`)** comparison, exact **Token Abbreviation Dictionary** & **Legacy `tco_*` Override Table**, J1939 SPN scaling formulas on `manual_can_N`, and **5 configuration bugs discovered in `FMC650_TEST_TR84_UNIT_PROFILE.wlp`**. |
| **[`FMC650_02_TR84_TEST_SENSOR_MAPPING.md`](./FMC650_02_TR84_TEST_SENSOR_MAPPING.md)** | Exhaustive sensor-by-sensor mapping for all **147 Wialon sensors** (`IDs 1..150`) in `FMC650_TEST_TR84_UNIT_PROFILE.wlp`:<br/>â€¢ **Part A (89 Hardware / FMS / Manual CAN / Tacho / Trailer EBS / GNSS Sensors)**: Maps `Wialon Sensor` -> `Wialon Formula (p)` -> `Official Flespi Parameter` -> `Teltonika Telemetry AVL ID` -> `Teltonika Configuration PID Block in re/`.<br/>â€¢ **Part B (58 Custom Flespi Plugin Weight Sensors `fleet_*` & `vhc_*`)**: Documents every derived weight, cargo status, phase, case code, and fraud/anomaly parameter alongside its state table (`ci`). |
| **[`FMC650_03_LEGACY_1161_PARAMETER_CATALOG.md`](./FMC650_03_LEGACY_1161_PARAMETER_CATALOG.md)** | Complete reference table mapping all **1,161 official Flespi `teltonika-fmc650` telemetry parameters** to both their **Flespi-Streamed Wialon Key (Path A)** and **Direct Wialon Key (`io_<AVL_ID>`, Path B)**, cross-referenced against `FMC650_TEST_TR84_UNIT_PROFILE.wlp`. |
| **[`FMC650_TEST_TR84_UNIT_PROFILE.wlp`](./FMC650_TEST_TR84_UNIT_PROFILE.wlp)** | Exact copy of the source Wialon unit template (`avl_unit`, version `b4`, 147 sensors). |
| **[`FMC650_TEST_TR84_UNIT_PROFILE.json`](./FMC650_TEST_TR84_UNIT_PROFILE.json)** | Pretty-printed, human-readable JSON version of `FMC650_TEST_TR84_UNIT_PROFILE.wlp` for easy inspection and diffing. |

---

## Key Statistics

- **Total Sensors in `FMC650_TEST_TR84_UNIT_PROFILE.wlp`**: **146 sensors** (Sensor IDs `1..150`; multiples of 32 â€” `32`, `64`, `96`, `128` â€” are skipped by Wialon's 32-bit sensor index allocator).
  - **Hardware / CAN / FMS / Tacho / Trailer EBS / GNSS Sensors**: **88 sensors** (`IDs 1..31`, `33..63`, `65..89` & `118`), driven by **64 unique Flespi hardware telemetry parameters**.
  - **Custom Flespi Cloud Plugin Weight Sensors (`fleet_*` & `vhc_*`)**: **58 sensors** (`IDs 90..95`, `97..117`, `119..127`, `129..150`), driven by **52 unique Flespi plugin parameters**.
- **Total Official Flespi `teltonika-fmc650` Telemetry Parameters Mapped to Wialon**: **1,161 parameters** (`1,734` expanded `AVL ID` mappings).



