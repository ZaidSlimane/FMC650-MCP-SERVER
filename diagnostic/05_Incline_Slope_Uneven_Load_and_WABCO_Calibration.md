# 05 — Incline / Slope Behavior, Uneven Cargo Distribution & WABCO Calibration

This document explains how **WABCO TEBS E**, the **FMC650**, and the **Flespi `fleet_*` Analytics Plugin** behave when:
1. The truck/trailer is parked or driving on an **incline / slope (*charge inclinée / en pente*)**.
2. Cargo is loaded **unevenly / inline (*déséquilibre longitudinal avant/arrière ou latéral gauche/droite*)** inside the trailer.
3. The WABCO TEBS E weight curve is **calibrated** (`AVL ID 13663` & `13664`).

---

## Case 1: The Truck/Trailer Is on an Incline / Slope (*Charge Inclinée / Véhicule en Pente*)

### 1. Does WABCO TEBS E Auto-Correct Static Weight for Road Slope?
* **No.** WABCO TEBS E only contains a *lateral* (left-to-right) accelerometer (`AVL ID 13673`) for anti-rollover braking. It does **not** have a pitch/slope sensor to correct airbag pressure when parked on a hill.
* Instead, slope compensation and filtering are handled by the **FMC650 + Flespi `fleet_*` Analytics Plugin**.

---

### 2. Why Raw Airbag Weight (`AVL ID 13657`) Changes on a Hill (Two Physical Effects)

When a loaded **44,000 kg** Sitrak + 3-axle trailer (`24,900 kg` on the trailer bogie on flat ground) stops or drives on a slope, two physical things happen:

#### Effect A: Center-of-Gravity Shift (Kingpin $\leftrightarrow$ Trailer Bogie)
* **Facing Uphill (e.g., $+6^\circ$ grade):** Gravity shifts the cargo's center of gravity backward. Weight transfers **off the tractor's fifth-wheel kingpin** and **onto the rear 3-axle trailer bogie**:
  * Tractor Drive Axles (`CAN1` `AVL ID 90 + 91`) drop by **$-1,100\text{ kg}$**.
  * Trailer Bogie (`CAN2` `AVL ID 13657`) rises by **$+1,100\text{ kg}$** (reading `26,000 kg` instead of `24,900 kg`).
* **Facing Downhill (e.g., $-6^\circ$ grade):** Gravity shifts weight forward onto the tractor kingpin:
  * Trailer Bogie (`AVL ID 13657`) drops by **$-1,100\text{ kg}$** (`23,800 kg`), while Tractor Drive Axles rise by **$+1,100\text{ kg}$**.

#### Effect B: "Brake-Bind" on the Mechanical Height-Levelling Valve (The Biggest Source of Slope Error!)
* Trailer axles are mounted on **trailing arms (*bras tirés*)** that pivot in an arc.
* When the driver stops on a hill and pulls the **Spring Parking Brake (`AVL ID 13809 = 1`)**, all 6 trailer wheels are locked against the asphalt.
* Gravity pulls the trailer chassis slightly downhill against the locked wheels, forcing the trailing-arm suspension to **bind/twist slightly upward or downward** by $1\text{–}2\text{ cm}$.
* The mechanical **height-levelling valve (*valve de nivellement*)** senses this $1.5\text{ cm}$ height change and tries to "correct" it:
  * If the suspension bound upward, the valve **dumps air (`exhaust`)** out of the airbags.
  * If the suspension bound downward, the valve **pumps extra air (`inflate`)** into the airbags trying to lift a locked chassis.
* **Result:** Raw `trailer.axle.load.sum` (`AVL ID 13657` / `fleet_trailer_axle_raw`) can be distorted by **$\pm 1,500\text{ kg to }\pm 3,500\text{ kg}$** while parked on a hill with locked brakes!

---

### 3. How the FMC650 + Flespi Architecture Solves Slope Errors

| Protection Layer | Parameters Used | How It Works |
| :--- | :--- | :--- |
| **1. Flespi Stabilization Lock (`fleet_*`)** | • `fleet_trailer_axle_raw` (Sensor `99`/`138`)<br>• **`fleet_trailer_axle_stable`** (Sensor `98`/`139`)<br>• `fleet_weight_raw` (Sensor `128`)<br>• **`fleet_weight_stable`** (Sensor `129`)<br>• `fleet_weight_variance` (Sensor `130`)<br>• `fleet_weight_confidence` (Sensor `131`) | During mountain climbs and steep descents ([Simulation Report Phases 3 & 4](../fmc650-reverse-engineered/mds/FMC650_FLEET_P2_PRODUCTION_v1.2_SITRAK_Simulation_Report.md)), raw axle loads fluctuate and `fleet_weight_variance` spikes (`fleet_weight_confidence` drops). The plugin **locks `fleet_weight_stable` at `44,000 kg` (`fleet_trailer_axle_stable` at `24,900 kg`)** and refuses to overwrite official weights until variance settles on flat ground. |
| **2. FMC650 3-Axis Tilt Sensor (`mG`)** | • **`AVL ID 17`** (`IoId 50220`): `x.acceleration` / `x_accel` (Sensor `87`, Pitch)<br>• **`AVL ID 18`** (`IoId 50230`): `y.acceleration` / `y_accel` (Sensor `88`, Roll)<br>• **`AVL ID 19`** (`IoId 50240`): `z.acceleration` / `z_accel` (Sensor `89`, Vertical $1\text{ G}$) | On flat ground, `x_accel ≈ 0 mG`, `y_accel ≈ 0 mG`, `z_accel ≈ 1000 mG`.<br>On a **$5^\circ$ slope**, `x_accel` reads **$\approx \pm 87\text{ mG}$** ($\sin 5^\circ \times 1000\text{ mG}$), allowing Flespi/Wialon to detect the hill and flag or compensate the reading. |
| **3. Combined Tractor + Trailer Sum (`CAN1 + CAN2`)** | • **`AVL ID 139`** (`total.vehicle.weight`)<br>• `AVL ID 89–91` + `AVL ID 13657` | On a gentle slope (with brakes released), the **$+1,100\text{ kg}$** shifted onto the rear trailer bogie (`CAN2`) equals the **$-1,100\text{ kg}$** removed from the front tractor axles (`CAN1`). Their sum stays constant: `24,900 + 1,100 + 19,100 - 1,100 = 44,000 kg`! |

> [!TIP]
> **Driver Best Practice for Accurate Static Weighing:**
> Stop on level ground, **release the foot/parking brake for 3 seconds** (so the trailer wheels roll $2\text{ cm}$ to release any suspension bind), and wait **10–15 seconds** for the WABCO levelling valve to settle.

---

## Case 2: Uneven Cargo Distribution Inside the Trailer (*Répartition de la Charge*)

What happens when the road is flat, but **10,000 kg of cargo** is loaded unevenly inside the 13.6-meter trailer?

### 1. Loaded More to the Left vs. Right (*Déséquilibre Latéral*)
* **Accuracy:** **100% accurate.**
* **Why:** All 6 airbags (Left and Right) share the same pneumatic circuit feeding Port `42` of the WABCO TEBS E modulator. The average air pressure across Left and Right airbags still equals the exact total vertical force on the bogie (`AVL ID 13657`).

### 2. Loaded All at the Front vs. All at the Back (*Déséquilibre Longitudinal : Avant vs Arrière*)
A 13.6m semi-trailer is a beam supported at two ends: the **Tractor Kingpin** at the front and the **3-Axle Bogie** at the back:

$$\text{Total Cargo Weight} = \Delta W_{\text{Kingpin (CAN1)}} + \Delta W_{\text{Trailer Bogie (CAN2)}}$$

| Cargo Position (`+10,000 kg` Payload) | Added to Tractor Axles (`CAN1` `AVL 90 + 91`) | Added to Trailer Bogie (`CAN2` `AVL 13657`) | Effect on Telemetry |
| :--- | :---: | :---: | :--- |
| **A. Evenly Distributed (Center of Trailer)** | **`+3,500 kg`** (35%) | **`+6,500 kg`** (65%) | Standard `35% / 65%` split; both `CAN2` cargo estimation (`fleet_trailer_cargo_est`) and `CAN1+CAN2` sum read **`+10,000 kg`**. |
| **B. All at the Rear Doors (Over 3-Axle Bogie)** | **`+500 kg`** (5%) | **`+9,500 kg`** (95%) | `AVL ID 13657` (`trailer.axle.load.sum`) accurately reads the **`+9,500 kg`** sitting on the rear bogie; `CAN1 + CAN2` reads **`+10,000 kg`**. |
| **C. All at the Front Bulkhead (Over Kingpin)** | **`+8,500 kg`** (85%) | **`+1,500 kg`** (15%) | Because 85% of the weight sits on the tractor's fifth wheel, the trailer's rear airbags only feel **`+1,500 kg`**. Combining **`CAN1` (`AVL 139` / `AVL 90+91`) + `CAN2` (`AVL 13657`)** captures all **`+10,000 kg`**. |

---

## Case 3: How WABCO TEBS E Calibrates Its Weight Curve (`AVL ID 13663` & `13664`)

1. **Standard 2-Point Workshop Calibration (Stored in WABCO TEBS E EEPROM):**
   * Using **WABCO TEBS E Diagnostic Software**, the technician enters two points from the trailer suspension plate:
     * **Point 1 (Unladen / Vide):** e.g., `0.8 bar` airbag pressure = **`4,200 kg`** bogie weight.
     * **Point 2 (Laden / Chargé):** e.g., `5.4 bar` airbag pressure = **`24,000 kg`** bogie weight (`8,000 kg × 3 axles`).
   * WABCO linearly interpolates every pressure reading into kilograms (`AVL ID 13657`).
2. **Online External Weighbridge Calibration Over CAN (`AVL ID 13663` & `13664`):**
   * When the trailer is weighed on a certified ground weighbridge (*pont-bascule*), the scale weight can be written over ISO 11992 (`PGN 65258`):
     * **`AVL ID 13663` (`trailer.scale.axle.load`, Sensor `69`):** External weighbridge reference weight in `kg`.
     * **`AVL ID 13664` (`trailer.calibration.load.level.state.enum`, Sensor `68`):** Calibration status (`0 = Uncalibrated`, `1 = Empty Level 1 Complete`, `2 = Full Level 2 Complete`, `14 = Calibration Error`).
