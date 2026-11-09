# 02 — Complete Catalog of Truck, Trailer & Flespi `fleet_*` Weight IDs (With Real-World Examples)

This reference defines **every Truck (`CAN1`), Trailer (`CAN2` WABCO TEBS E), and Flespi Analytics Plugin (`fleet_*` / `vhc_*`) parameter** used in [`FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md`](../fmc650-reverse-engineered/mds/FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md) and [`02_TR84_Flespi_Test_WLP_Complete_147_Sensors_Mapping.md`](../wialon-parameters/02_TR84_Flespi_Test_WLP_Complete_147_Sensors_Mapping.md).

---

## Reference Vehicle Baseline for Real-World Examples

All examples below use the same real-world heavy-haul combination from [`FMC650_FLEET_P2_PRODUCTION_v1.2_SITRAK_Simulation_Report.md`](../fmc650-reverse-engineered/mds/FMC650_FLEET_P2_PRODUCTION_v1.2_SITRAK_Simulation_Report.md):
* **Tractor (`CAN1` at `500 kbps`):** SINOTRUK SITRAK C7H (`MC13` Engine + `ZF TraXon 12TX` Gearbox), unladen weight **`8,300 kg`**
* **Semi-Trailer (`CAN2` at `500 kbps` / `250 kbps`):** 3-Axle CIMC Semi-Trailer with **WABCO TEBS E**, unladen weight **`7,200 kg`**
* **Empty Tare Weight (Tractor + Trailer):** **`15,500 kg`** (`4,200 kg` on the 3 trailer axles when empty)
* **Payload Loaded at Cement Plant:** **`+28,500 kg`** of bagged cement
* **Full Loaded Gross Weight (`GCVW`):** **`44,000 kg`** (`19,100 kg` on Tractor Axles + **`24,900 kg`** on Trailer 3-Axle Bogie)
* **Partial Unload / Theft Event:** **`-4,150 kg`** removed from the rear trailer doors

---

## Part 1: Truck Weight IDs (`CAN1` — Sitrak J1939 FMS, EV-FMS & LVCAN)

| `.cfg` `IoId` | Wire `AVL ID` | Configurator Name | Flespi Parameter | Wialon Key (`Path A` / `Path B`) | Real-World Loaded Sitrak Example & Meaning |
| :---: | :---: | :--- | :--- | :--- | :--- |
| `45290` / `46100` | **`89`** | `Axle weight 1` (`Axle 1 load`) | `can.axle.weight.1` (`fms_axle_load_1`) | `can_axle_weight_1` / `io_89` | **`7,100 kg`** — Front steering axle weight under the Sitrak cab + MC13 engine. |
| `45300` / `46110` | **`90`** | `Axle weight 2` (`Axle 2 load`) | `can.axle.weight.2` (`fms_axle_load_2`) | `can_axle_weight_2` / `io_90` | **`6,000 kg`** — 1st rear drive axle weight (carrying half of the fifth-wheel kingpin load on a `6x4`). |
| `45310` / `46120` | **`91`** | `Axle weight 3` (`Axle 3 load`) | `can.axle.weight.3` (`fms_axle_load_3`) | `can_axle_weight_3` / `io_91` | **`6,000 kg`** — 2nd rear drive axle weight (`7,100 + 6,000 + 6,000 = 19,100 kg` on the tractor). |
| `45320` / `46130` | **`92`** | `Axle weight 4` (`Axle 4 load`) | `can.axle.weight.4` (`fms_axle_load_4`) | `can_axle_weight_4` / `io_92` | **`8,300 kg`** — 4th axle on an `8x4` rigid dump truck, or 1st bridged trailer axle. |
| `45330` / `46140..46240` | **`93–103`** | `Axle weight 5..15` | `can.axle.weight.5..15` | `can_axle_weight_5..15` / `io_93..103` | **`8,300 kg`** — Additional multi-axle trailer / lowbed / road-train axles (`Axle 5` through `Axle 15`). |
| **`46530`** | **`139`** | **`Combined vehicle weight`** (`GCVW`) | **`total.vehicle.weight`** (`fms_total_weight`) | **`total_vhc_weight`** / `io_139` (**Sensor `21`**) | **`44,000 kg`** (`15,500 kg` empty $\rightarrow$ `44,000 kg` full). Total gross weight of Tractor + Trailer + Cargo (`PGN 65134` / `SPN 1760`). |
| `45860` | **`118`** | `CAN Adapter Axle Weight 1` | `can.axle.weight` | `can_axle_weight` / `io_118` | **`3,500 kg`** — Used only with an external `LV-CAN200`/`ALL-CAN300` adapter on light commercial vans (Disabled in `P2_v1.2`). |
| `90750` | **`10896`** | `Trailer Weight` (`EV-FMS`) | `can.ev.trailer.weight` | `can_ev_trailer_weight` / `io_10896` | **`35,700 kg`** — Total weight of the towed trailer + its cargo (`7,200 kg` chassis + `28,500 kg` cement) from `PGN 65258` `SPN 583`. |
| `90760` | **`10897`** | `Cargo Weight` (`EV-FMS`) | `can.ev.cargo.weight` | `can_ev_cargo_weight` / `io_10897` | **`28,500 kg`** — Net payload weight (`Cargo Weight` = `44,000 kg` Gross $-$ `15,500 kg` Tare) from `PGN 65258` `SPN 584`. |
| `90770` | **`10898`** | `Powered Vehicle Weight` (`EV-FMS`) | `can.ev.powered.vehicle.weight` | `can_ev_powered_vhc_weight` / `io_10898` | **`19,100 kg`** — Total weight resting on the Sitrak tractor's own tires (`8,300 kg` tractor + `10,800 kg` kingpin pressure) from `PGN 65134` `SPN 1585`. |
| `90780` / `48940` | **`10899`** | `Gross Combination Vehicle Weight` (`EV-FMS`) | `can.gross.combination.vehicle.weight` | `can_gross_combination_vhc_weight` / `io_10899` | **`44,000 kg`** — EV-FMS mirror of `AVL ID 139` (`PGN 65134` `SPN 1760`). |

---

## Part 2: Hardware TrailerCAN Parameters (`CAN2` — WABCO TEBS E ISO 11992-2)

| `.cfg` `IoId` | Wire `AVL ID` *(Apache RS232)* | Configurator Name | Flespi Parameter | Wialon Key (`Path A`) & Sensor | Real-World WABCO TEBS E Trailer Example & Meaning |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **`103060`** | **`13657`** *(10510)* | **`Axle Load Sum`** | **`trailer.axle.load.sum`** | **`trailer_axle_load_sum`** (**Sensor `71`**) | **`24,900 kg`** (`24.90 t` in Wialon with `/1000` multiplier; **`4,200 kg`** empty). Combined weight resting on all 6 airbags of the 3-axle trailer bogie (`EBS22` `PGN 65218`). |
| **`103110`** | **`13662`** *(10521)* | `Axle Load Measured By Towed Vehicle` | `trailer.towing.vehicle.axle.load` | `trailer_towing_vhc_axle_load` (**Sensor `70`**) | **`24,900 kg`** (`24.90 t`). Internal WABCO EBS bogie load measurement (`RGE22`). |
| **`103120`** | **`13663`** *(10518)* | `Axle Load Measured By External Scale` | `trailer.scale.axle.load` | `trailer_scale_axle_load` (**Sensor `69`**) | **`24,850 kg`** (`24.85 t`). Certified ground weighbridge (*pont-bascule*) reference weight stored during WABCO calibration. |
| **`103130`** | **`13664`** *(10511)* | `Axle Load Calibration Data Load Level` | `trailer.calibration.load.level.state.enum` | `trailer_calibration_load_lvl_state_enum` (**Sensor `68`**) | **`2`** (`0` = Uncalibrated, `1` = Empty Tare calibrated, `2` = Full Laden calibrated, `14` = Error). |
| **`104570`** | **`13808`** | `Electrical Load Proportional Function Installation Status` | `trailer.electric.load.proportional.function.installation.state.enum` | `trailer_electric_load_proportional_function_installation_st_enum` | **`1`** (`Installed & Active` — confirms WABCO airbag pressure sensor is enabled for dynamic brake proportioning). |
| **`104590`** | **`13810`** *(10513)* | **`Pneumatic Supply Pressure`** | **`trailer.pneumatic.supply.pressure`** | **`trailer_pneumatic_supply_press`** (**Sensor `62`**) | **`820 kPa`** (**`8.20 bar`** in Wialon). Air reservoir pressure from the Sitrak compressor. Drops to `< 400 kPa` if parked overnight with engine OFF (making airbag weights invalid!). |
| **`104230`** | **`13774`** *(10514)* | `Vehicle Pneumatic Supply Status` | `trailer.pneumatic.supply.state.enum` | `trailer_pneumatic_supply_st_enum` (**Sensor `61`**) | **`1`** = Sufficient air (`> 6.5 bar`, weights valid); **`0`** = Insufficient air (airbags deflating, ignore weight drop!). |
| **`103000`** | **`13651`** *(10520)* | `Detected Towed Vehicle` | `trailer.towing.state.enum` | `trailer_towing_st_enum` (**Sensor `74`**) | **`1`** = Trailer coupled to Sitrak tractor; **`0`** = Trailer unhooked. |
| **`103200`** | **`13671`** | `VIN` (Trailer VIN) | `can.trailer.vin` | `can_trailer_vin` | **`"LJRC1338Xgt019284"`** — 17-character chassis VIN programmed inside the WABCO TEBS E ECU. |
| **`103300`** | **`13681`** | `Lift Axle 1 Position Status` | `trailer.lift.axle.1.position.state.enum` | `trailer_lift_axle_1_pos_st_enum` | **`0`** = Down on asphalt (when bogie load `> 12,000 kg`); **`1`** = Lifted in the air (when empty `< 8,000 kg` to save tires). |
| **`103310`** | **`13682`** | `Lift Axle 2 Position Status` | `trailer.lift.axle.2.position.state.enum` | `trailer_lift_axle_2_pos_st_enum` | **`0`** = Down; **`1`** = Lifted. |
| **`103080`** | **`13659`** *(10522)* | `Vehicle Service Brake Status` | `trailer.vehicle.service.brake.state.enum` | `trailer_vhc_service_brake_st_enum` (**Sensor `65`**) | **`1`** = Trailer service brakes actively squeezing drums/discs; **`0`** = Released. |
| **`104580`** | **`13809`** *(10519)* | `Spring Brake Status` | `trailer.spring.brake.state.enum` | `trailer_spring_brake_st_enum` (**Sensor `59`**) | **`1`** = Trailer parking brake (*frein de parc à ressort*) engaged; **`0`** = Released for driving. |
| **`103140–103190`** | **`13665–13670`** | `Brake Cylinder Pressure Axles 1..3 Left/Right` | `trailer.braking.cylinder.pressure.axle.1..3.left/right` | `trailer_braking_cylinder_press_axle_1..3_left/right` | **`0 kPa`** cruising $\rightarrow$ **`180 kPa`** (`1.8 bar`) normal braking $\rightarrow$ **`650 kPa`** (`6.5 bar`) emergency braking across all 6 wheels. |
| **`103220`** | **`13673`** | `Lateral Acceleration` | `trailer.lateral.acceleration` | `trailer_lateral_accel` | **`0.1 m/s²`** straight road $\rightarrow$ **`3.8 m/s²`** taking a sharp highway roundabout too fast with a high center of gravity. |
| **`103210`** | **`13672`** | `VDC Active` | `trailer.vdc.active.state.enum` | `trailer_vdc_active_st_enum` | **`1`** = WABCO RSS (Roll Stability Support) actively auto-braking outside trailer wheels to prevent a rollover! |
| **`103270`** | **`13678`** *(10517)* | `ROP System Status` | `trailer.rop.system.state.enum` | `trailer_rop_system_st_enum` (**Sensor `60`**) | **`1`** = Roll-Over Protection armed & active. |
| **`103280`** | **`13679`** | `YC System Status` | `trailer.yc.system.state.enum` | `trailer_yc_system_st_enum` | **`1`** = Yaw Control anti-jackknife system active. |
| **`103020`** | **`13653`** *(10508)* | `Vehicle ABS Status` | `trailer.abs.state.enum` | `trailer_abs_st_enum` (**Sensor `72`**) | **`1`** = Trailer ABS healthy; **`0`** = Fault. |
| **`103090`** | **`13660`** *(10515)* | `Vehicle Electrical Supply Status` | `trailer.power.state.enum` | `trailer_power_st_enum` (**Sensor `63`**) | **`1`** = ISO 7638 24V power normal; **`0`** = Low voltage / fault. |
| **`103040`** | **`13655`** *(10516)* | `Red Warning Signal Request` | `trailer.red.warning.request.state.enum` | `trailer_red_warning_req_st_enum` (**Sensor `67`**) | **`0`** = Normal; **`1`** = Critical WABCO EBS red stop fault! |
| **`103050`** | **`13656`** *(10509)* | `Amber Warning Signal Request` | `trailer.amber.warning.request.state.enum` | `trailer_amber_warning_req_st_enum` (**Sensor `66`**) | **`0`** = Normal; **`1`** = Minor WABCO EBS yellow sensor warning. |

---

## Part 3: Flespi `fleet_*` & `vhc_*` Weight & Anti-Theft Analytics Plugin Parameters

The Flespi `tidj` plugin ingests `AVL ID 139` (`total.vehicle.weight`) and `AVL ID 13657` (`trailer.axle.load.sum`) and computes stabilized weights, net cargo, trip baselines, and theft alarms for Wialon (`TR84_Flespi_Test.wlp`):

| Wialon Key (`Path A`) | Wialon Sensor ID | Real-World Loaded Sitrak + WABCO Example & Meaning |
| :--- | :---: | :--- |
| **`fleet_weight_raw`** | `128` | **`44,350 kg`** — Raw unsmoothed total weight bouncing between `43,200` and `45,100 kg` over highway potholes. |
| **`fleet_weight_stable`** | `129` | **`44,000 kg`** — Stabilized total vehicle weight locked after variance settles. |
| **`fleet_cargo_weight_net`** | `104` | **`28,500 kg`** — Net payload inside the trailer (`44,000 kg` Stable $-$ `15,500 kg` Empty Tare). |
| **`fleet_load_pct_of_max`** | `124` | **`101.8 %`** — Percentage of rated `28,000 kg` payload capacity (`28,500 / 28,000`). |
| **`fleet_weight_variance`** | `130` | **`12.4 kg²`** (Parked/Stable) vs **`4,850.0 kg²`** (Bouncing on rough road or climbing a grade). |
| **`fleet_weight_confidence`** | `131` | **`98 %`** (Flat ground, air pressure `> 8 bar`, low variance) vs **`35 %`** (Rough road / slope). |
| **`fleet_load_state`** | `125` | **`"LOADED"`** (`"EMPTY"`, `"LOADING"`, `"LOADED"`, `"UNLOADING"`, `"OVERLOAD"`). |
| **`fleet_trailer_axle_raw`** | `99` / `138` | **`24,950 kg`** — Live raw WABCO trailer bogie weight from `AVL ID 13657`. |
| **`fleet_trailer_axle_stable`** | `98` / `139` | **`24,900 kg`** — Stabilized WABCO trailer bogie weight. |
| **`fleet_trailer_cargo_est`** | `97` / `140` | **`28,500 kg`** — Total cargo estimated from the trailer bogie weight curve. |
| **`fleet_trailer_trip_baseline`** | `96` / `141` | **`24,900 kg`** — Trailer bogie weight locked at departure from the loading dock. |
| **`fleet_trailer_loss_delta`** | `93` / `142` | **`-2,700 kg`** — Sudden drop on the trailer bogie during a roadside stop (`24,900 kg` $\rightarrow$ `22,200 kg`). |
| **`fleet_trailer_loss_pct`** | `92` / `143` | **`10.8 %`** — Percentage of trailer bogie load lost mid-trip. |
| **`fleet_cargo_loss_kg`** | `102` | **`4,150 kg`** — Total estimated cargo removed mid-trip (`-2,700 kg` on bogie + `-1,450 kg` off kingpin). |
| **`fleet_fraud_alert`** | `110` | **`1`** (`0` = Normal, `1` = Unscheduled mid-trip weight loss detected outside authorized geofence!). |
| **`fleet_fraud_type`** | `113` | **`"UNSCHEDULED_PARTIAL_UNLOAD"`** |
| **`fleet_fraud_severity`** | `112` | **`"CRITICAL"`** |
| **`fleet_overload_flag`** / **`fleet_overload_kg`** | `126` / `127` | **`1`** / **`4,000 kg`** — Triggered when `fleet_weight_stable` (`44,000 kg`) exceeds legal `40,000 kg` limit. |
| **`vhc_gross_weight`** / **`vhc_cargo_weight`** | `146` / `145` | **`44,000 kg`** / **`28,500 kg`** — Top-level Wialon dashboard summary sensors. |
