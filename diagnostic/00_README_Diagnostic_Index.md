# FMC650 Weight & TrailerCAN Diagnostic Knowledge Base

- **Target Hardware**: Teltonika `FMC650` (Firmware `03.01.01.Rev.15`, `ConfigurationVersion 4.43.1.0`)
- **Target Fleet Combination**: **SINOTRUK SITRAK C7H** (`MC11/MC13` Engine + `ZF TraXon 12TX` Gearbox on `CAN1`) + **3-Axle Semi-Trailer** (**WABCO TEBS E** ISO 11992-2 on `CAN2`)
- **Telematics Pipeline**: `FMC650` (Codec 8 Extended) $\rightarrow$ **Flespi** (`teltonika-fmc650` + `tidj` Weight Analytics Plugin) $\rightarrow$ **Wialon Local** (`TR84_Flespi_Test.wlp`)

---

## Directory Index (By Subject)

| File | Subject Covered | Key Topics & Parameters |
| :--- | :--- | :--- |
| [**`01_CAN1_FMS_J1939_LVCAN_EV_FMS_Architecture.md`**](./01_CAN1_FMS_J1939_LVCAN_EV_FMS_Architecture.md) | **CAN1, SAE J1939, FMS, LVCAN & EV-FMS Architecture + The 15 FMS Axle Slots** | • Physical `CAN1` (Pins `12`/`2`) vs `CAN2` (Pins `16`/`6`)<br>• How `SAE J1939` (`PGN`s & `SPN`s) works<br>• Difference between `FMS`, `LVCAN` (`AVL 118`), `EV-FMS` (`AVL 10896–10899`), and `Manual CAN` (`AVL 145–214`)<br>• The 16 FMS Weight Parameters (`AVL ID 89–103` & `139`)<br>• Why J1939 has **15 Axle Weight slots** (`SPN 928` 4-bit index) |
| [**`02_Real_World_Weight_and_Trailer_IDs_Reference.md`**](./02_Real_World_Weight_and_Trailer_IDs_Reference.md) | **Complete Catalog of Truck, Trailer & Flespi `fleet_*` Weight IDs with Real Examples** | • Real-world loaded Sitrak (`44,000 kg`) + WABCO TEBS E (`24,900 kg`) examples for every parameter<br>• Exact `.cfg` `IoId`, Codec 8E `AVL ID`, Flespi parameter, Wialon Path A/B key, and Wialon Sensor ID<br>• All 58 Flespi `fleet_*` & `vhc_*` Weight & Anti-Theft Plugin parameters |
| [**`03_SITRAK_C7H_3Axle_Models_and_Why_TrailerCAN_Is_Required.md`**](./03_SITRAK_C7H_3Axle_Models_and_Why_TrailerCAN_Is_Required.md) | **3-Axle SITRAK C7H (`6x4`/`6x2`) Configurations & Why TrailerCAN Is Required** | • Variant A: Steel-Spring `6x4` Tractor + WABCO Trailer<br>• Variant B: ECAS Air-Suspension `6x4`/`6x2` Tractor + WABCO Trailer<br>• Variant C: `6x4` Rigid Tipper / Porteur<br>• The **6 Physics & Engineering Reasons** why `CAN2` TrailerCAN is mandatory even if `CAN1` has axle weights |
| [**`04_WABCO_TEBS_E_Bogie_Physics_and_Trailer_Parameters.md`**](./04_WABCO_TEBS_E_Bogie_Physics_and_Trailer_Parameters.md) | **3-Axle Trailer Bogie Physics, WABCO TEBS E Roles & Complete Trailer Parameter List** | • What a **3-Axle Bogie (*Tridem*)** is and why all 6 airbags share 1 pressure sensor on **Port `42`** (`AVL ID 13657`)<br>• The **6 Physical Jobs** of WABCO TEBS E (EBS braking, load proportioning, weight calculation, ROP anti-rollover, lift axle, pneumatic guard)<br>• Complete table of **27 Hardware TrailerCAN + 13 Flespi `fleet_trailer_*` parameters** |
| [**`05_Incline_Slope_Uneven_Load_and_WABCO_Calibration.md`**](./05_Incline_Slope_Uneven_Load_and_WABCO_Calibration.md) | **Incline / Slope Behavior, Uneven Cargo Distribution & WABCO Calibration** | • Why raw airbag weight (`AVL ID 13657`) drifts on a slope (CoG shift + **Brake-Bind** on the levelling valve)<br>• How FMC650 3-Axis Accelerometer (`AVL ID 17–19`), `CAN1+CAN2` sum (`AVL ID 139`), and Flespi Stabilization (`fleet_weight_stable`) solve slope errors<br>• Uneven cargo loading (Front bulkhead vs Rear doors vs Left/Right)<br>• WABCO 2-Point & Online Scale Calibration (`AVL ID 13663` & `13664`) |
| [**`06_FMS_Axle_Weight_Troubleshooting_and_CAN_Bus_Modes.md`**](./06_FMS_Axle_Weight_Troubleshooting_and_CAN_Bus_Modes.md) | **Troubleshooting Missing FMS Axle Weights, "Gross Sum Only", & `CAN1 Bus Mode` (`Silent` vs `Normal`)** | • The **7 Reasons** why FMC650 fails to receive FMS Axle Weights (`AVL ID 89–103`)<br>• Why FMC650 receives **ONLY `AVL ID 139` (`Combined vehicle weight`)** while `Axle 1..4` (`AVL ID 89–92`) stay empty (`PGN 65134` vs `PGN 65258`)<br>• What **`CAN1 Bus Mode` (`PID 206`: `Silent` vs `Normal`)** does and why 95% of CAN data works in `Silent` mode |

---

## Core Architectural Golden Rules

1. **Configuration Domain (`.cfg` `PID` / `IoId`) $\neq$ Telemetry Domain (`AVL ID`)**:
   - **Configuration IDs** (`PID 100..13002` and `IoId 45290..180540`) only exist inside `.cfg` files and `setparam`/`setio` commands.
   - **Telemetry `AVL ID`s** (`1..13810`) are the runtime values sent inside Codec 8 Extended TCP packets to Flespi and Wialon.
   - **82 identical numbers collide across both domains** (e.g., `PID 100` = `Movement Source`, whereas `AVL ID 100` = `Axle weight 12`).
2. **Correction of Common External AI / Wiki Hallucinations**:
   - External generic notes often claim `AVL ID 26, 27, 28, 29` are `can_axle_load1..4`. **On the FMC650 (`03.01.01.Rev.15`), that is false**: `AVL ID 26..28` are Analog/SOS/GSM parameters.
   - Real FMC650 FMS Axle Weights are **`AVL ID 89–103`** (`IoId 45290..45330` / `46100..46240`), Gross Combination Weight is **`AVL ID 139`** (`IoId 46530`), and WABCO Trailer Bogie Weight Sum is **`AVL ID 13657`** (`IoId 103060`).
