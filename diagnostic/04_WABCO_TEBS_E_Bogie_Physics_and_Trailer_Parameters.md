# 04 — 3-Axle Trailer Bogie Physics, WABCO TEBS E Roles & Complete Trailer Parameter List

This document explains what a **3-Axle Trailer Bogie (*Tridem*)** is, why all 6 airbags share a single pressure sensor on **Port `42` of the WABCO TEBS E modulator** to broadcast one combined `Axle Load Sum` (`AVL ID 13657`), and details the **6 physical jobs of WABCO TEBS E**.

---

## 1. What Is a "3-Axle Bogie" (*Tridem*) and Why Does It Broadcast One Combined Number (`AVL ID 13657`)?

### A. What is a "Bogie"?
In heavy-truck engineering, a **bogie** (called a **tridem** when it has 3 axles, or **tandem** when it has 2 axles) is the **cluster of 3 closely-spaced axles mounted together under the rear of a semi-trailer**:
* **3 Axles × 2 Sides (Left & Right) = 6 Rubber Airbags (*6 coussins d'air / soufflets pneumatiques*)**.

### B. Why All 6 Airbags Share a Single Pneumatic Pipe & Sensor (Pascal's Law)
On a standard 3-axle semi-trailer (CIMC, Schmitz, Krone, Lecitrailer), the manufacturer does **not** install 6 separate electronic pressure sensors (one on each airbag). Instead, all 6 airbags are connected together by **shared plastic air pipes (`Ø 8–10 mm`)** into a **single pneumatic loop** fed by one mechanical **Height-Levelling Valve (*Valve de nivellement*)**:

```
   [ TRAILER AIR TANK (8.2 bar) ] ──► [ Height-Levelling Valve ]
                                                 │
             ┌───────────────────────────────────┼───────────────────────────────────┐
             ▼                                   ▼                                   ▼
   [ Trailer Axle 1 ]                  [ Trailer Axle 2 ]                  [ Trailer Axle 3 ]
  (Left Bag + Right Bag)              (Left Bag + Right Bag)              (Left Bag + Right Bag)
             │                                   │                                   │
             └───────────────────────────────────┼───────────────────────────────────┘
                                                 │ (Single Shared Air Pressure: e.g. 5.4 bar)
                                                 ▼
                                  [ Port 42 on WABCO TEBS E ECU ]
                                  (1 Internal Pressure Sensor)
                                                 │
                                                 ▼
                         Broadcasts 1 Combined Number on CAN2 (ISO 11992-2):
                         AVL ID 13657 (trailer.axle.load.sum) = 24,900 kg!
```

* **Why trailers are built this way:**
  1. **Equalizing Load Over Bumps (Pascal's Law):** Because all 6 airbags are connected by the same air tube, when the 1st trailer axle hits a bump or pothole, air flows instantly into the 2nd and 3rd axles' airbags so all 3 axles always share the load equally (`1/3 + 1/3 + 1/3`) instead of breaking one axle!
  2. **Single Pressure Sensor at Port `42`:** A single T-fitting runs from that shared airbag pipe into **Port `42`** of the **WABCO TEBS E modulator**.
  3. **One Combined Number (`AVL ID 13657`):** Because the WABCO TEBS E only sees that **one shared air pressure** (e.g., `5.4 bar`), it multiplies the pressure by the total area of all 6 airbags and outputs **one combined weight for the entire 3-axle bogie**:
     * **`AVL ID 13657` (`trailer.axle.load.sum`) = `24,900 kg`** (which equals **`8,300 kg × 3 axles`**).

---

## 2. What Does the WABCO TEBS E Modulator Do? (Its 6 Physical Jobs)

The **WABCO TEBS E** (*Trailer Electronic Braking System — Generation E*) is a heavy aluminum computer-and-valve block bolted underneath the middle of the semi-trailer between the 3 axles. It connects to the Sitrak tractor through the **7-pin ISO 7638 cable (`CAN2` ISO 11992-2)** and performs **6 physical jobs**:

### Job 1: High-Speed Electronic Braking & ABS (`AVL ID 13653, 13659, 13665–13670`)
* On old pneumatic trailers, air took `0.5 seconds` to travel 13 meters down a rubber hose when the driver stepped on the brake—causing the trailer to push the tractor.
* With **WABCO TEBS E**, the brake command travels at the speed of light over the **ISO 11992-2 CAN2 wire**, and WABCO instantly opens its local air valves into all 6 brake cylinders (`AVL ID 13665–13670`), while monitoring wheel speed sensors (`ABS` `AVL ID 13653`) so no trailer wheel locks up.

### Job 2: Automatic Load-Sensing Brake Proportioning (`ALB` / `EBD` — `AVL ID 13808`)
* **This is the main reason WABCO has a weight sensor inside it!**
  * If an **empty trailer (`4,200 kg`)** braked with **`6.5 bar`** of air pressure, all 6 tires would skid violently and the trailer would jackknife (*mise en portefeuille*).
  * If a **fully loaded trailer (`24,900 kg`)** braked with only **`1.5 bar`**, the truck wouldn't stop!
* WABCO TEBS E reads the airbag pressure on **Port `42`** every millisecond and automatically scales the brake cylinder pressure (`AVL ID 13665–13670`) to match the exact cargo weight!

### Job 3: Broadcasting Trailer Bogie Weight Over CAN2 (`AVL ID 13657, 13662, 13663, 13664`)
* Using its internal 2-point calibration curve (Empty `bar` $\rightarrow$ `kg`, Full `bar` $\rightarrow$ `kg`), WABCO converts the airbag pressure into kilograms and broadcasts **`AVL ID 13657` (`trailer.axle.load.sum`)** every `100–200 ms` on `CAN2`.

### Job 4: Anti-Rollover Active Intervention (`RSS` / `ROP` / `VDC` — `AVL ID 13672, 13673, 13678`)
* Built inside the WABCO TEBS E aluminum housing is a precision **Lateral Accelerometer (`AVL ID 13673` `trailer.lateral.acceleration` in `m/s²`)**.
* If the driver enters a curve or highway exit ramp too fast with a heavy load, `AVL ID 13673` exceeds the rollover threshold (e.g., `> 3.2 m/s²`), and WABCO **automatically applies the trailer brakes by itself (`AVL ID 13672` `VDC Active = 1`)**—even if the driver's foot is still on the accelerator—saving the truck from tipping over!

### Job 5: Automatic Lift-Axle Control (`AVL ID 13681 & 13682`)
* When the trailer is empty (`AVL ID 13657 < 8,000 kg`), WABCO TEBS E automatically vents the 1st trailer axle's suspension bags and inflates the lift-bag (`AVL ID 13681 = 1`), lifting the 1st trailer axle off the road to save tire wear and fuel.
* As soon as a forklift loads cargo past `12,000 kg`, WABCO automatically lowers the lift axle back onto the asphalt (`AVL ID 13681 = 0`).

### Job 6: Pneumatic Supply Guard & Digital Chassis Identity (`AVL ID 13810, 13774, 13671`)
* Continuously measures the trailer air reservoir pressure (`AVL ID 13810` in `kPa`), spring parking brake state (`AVL ID 13809`), and broadcasts the trailer's permanent **17-character VIN (`AVL ID 13671`)** so the FMC650 always knows which trailer is coupled.

---

## 3. Quick Summary of All 27 Hardware + 13 Flespi Trailer Parameters

| Category | Hardware `AVL ID`s (`CAN2`) | Flespi `fleet_trailer_*` Plugin Keys |
| :--- | :--- | :--- |
| **Weight & Calibration (5)** | `13657` (`Axle Load Sum`), `13662` (`Towed Vehicle Load`), `13663` (`External Scale Load`), `13664` (`Calibration Level`), `13808` (`Load Proportional Status`) | `fleet_trailer_axle_raw`, `fleet_trailer_axle_stable`, `fleet_trailer_cargo_est`, `fleet_trailer_trip_baseline`, `fleet_trailer_loss_delta`, `fleet_trailer_loss_pct` |
| **Pneumatic & Air Supply (2)** | `13810` (`Pneumatic Supply Pressure kPa`), `13774` (`Pneumatic Supply Status`) | `fleet_trailer_pneumatic_kpa`, `fleet_trailer_pneumatic_ok` |
| **Identity, Coupling & Lift Axles (4)** | `13651` (`Detected Towed Vehicle`), `13671` (`Trailer VIN`), `13681` (`Lift Axle 1`), `13682` (`Lift Axle 2`) | `fleet_trailer_coupled` |
| **Brakes & 6 Wheel Cylinders (8)** | `13659` (`Service Brake`), `13809` (`Spring Parking Brake`), `13665–13670` (`Axle 1..3 Left/Right Cylinder Pressures kPa`) | — |
| **Roll-Over & Stability (4)** | `13673` (`Lateral Acceleration m/s²`), `13672` (`VDC Active`), `13678` (`ROP Status`), `13679` (`YC Status`) | `fleet_trailer_rop_ok` |
| **ABS, Power & Fault Lamps (4)** | `13653` (`ABS Status`), `13660` (`Electrical Power Status`), `13655` (`Red Warning`), `13656` (`Amber Warning`) | `fleet_trailer_abs_ok`, `fleet_trailer_ebs_powered`, `fleet_trailer_warning_amber`, `fleet_trailer_warning_red` |
