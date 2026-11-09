# 03 — 3-Axle SINOTRUK SITRAK C7H (`6x4` & `6x2`) Configurations & Why TrailerCAN (`CAN2`) Is Required

This document details how the **3-Axle SINOTRUK SITRAK C7H** models (`6x4` and `6x2`) map to FMC650 weight telemetry and explains the **6 physics and engineering reasons** why **`CAN2` TrailerCAN** is mandatory even when a truck already reports FMS axle weights on `CAN1`.

---

## Part 1: The 3 Configurations of 3-Axle SINOTRUK SITRAK C7H (`6x4` / `6x2`)

A **3-axle Sitrak C7H** has **1 Front Steer Axle (`Axle 1`)** + **2 Rear Tandem Axles (`Axle 2` & `Axle 3`)**:

```
       [ SITRAK C7H 3-AXLE TRACTOR (6x4) ]              [ 3-AXLE WABCO SEMI-TRAILER ]
        ┌──────────┐
        │  CAB     │       Fifth-Wheel Kingpin (35%)             65% of Cargo Load
        │  MC13    │               ▼                                    ▼
  ┌─────┴──────────┴───────────────────────────┐   ┌─────────────────────────────────────────┐
  │                 CHASSIS                    ├───┤            TRAILER BED                  │
  └─────── (O) ─────────────── (O) ─── (O) ────┘   └─────────────── (O) ─── (O) ─── (O) ─────┘
         Axle 1              Axle 2   Axle 3                      Trailer Bogie (3 Axles)
      (Front Steer)         (Rear Drive Tandem)                  (Shared Airbag Circuit)
      CAN1: AVL 89         CAN1: AVL 90 & AVL 91                     CAN2: AVL 13657
```

Depending on the suspension installed on the Sitrak C7H, it behaves in one of **3 ways**:

---

### Variant A: Sitrak C7H `6x4` Tractor with Steel Leaf Springs (*Ressorts à Lames*) + 3-Axle WABCO Trailer — *Most Common in the region*
* **Physical Suspension:**
  * **Tractor (`Axle 1, 2, 3`):** Parabolic / multi-leaf steel springs (9 or 12 leaves). **Zero air bags or load sensors on the tractor.**
  * **Trailer (`Axles 4, 5, 6`):** Air suspension (*coussins d'air*) controlled by **WABCO TEBS E**.
* **What `CAN1` (FMS) Outputs:**
  * `AVL ID 89, 90, 91` (`Axle 1..3 load`): **Empty / Not Sent** (because steel springs have no pressure transducers).
  * `AVL ID 139` (`Combined vehicle weight`): Sent by the **ZF TraXon 12TX gearbox** (estimated from engine torque/acceleration or bridged from trailer EBS).
* **What `CAN2` (TrailerCAN) Outputs:**
  * **`AVL ID 13657` (`trailer.axle.load.sum`):** Exact measured weight on the 3-axle trailer bogie (e.g., `4,200 kg` empty $\rightarrow$ `24,900 kg` loaded).
* **How Total Payload Is Calculated:**
  * Using **`CAN2` (`AVL ID 13657`)** + **`CAN1` (`AVL ID 139`)** inside the Flespi `tidj` plugin.

---

### Variant B: Sitrak C7H `6x4` / `6x2` Tractor with Rear ECAS Air Suspension (8 Airbags on Tractor) + 3-Axle WABCO Trailer
* **Physical Suspension:**
  * **Tractor `Axle 1` (Steer):** Steel springs (or air suspension on full-air spec).
  * **Tractor `Axle 2 & 3` (Rear Tandem):** **WABCO ECAS (Electronically Controlled Air Suspension)** with pressure sensors on the rear drive airbags (and liftable 3rd tag/pusher axle on `6x2` models).
  * **Trailer:** Air suspension with **WABCO TEBS E**.
* **Exact Weight Split Across `CAN1` and `CAN2` (44,000 kg Loaded Example):**

| Axle Group | FMC650 Bus & `AVL ID` | Empty (`15,500 kg`) | Loaded (`44,000 kg`) | Notes |
| :--- | :--- | :---: | :---: | :--- |
| **Tractor Axle 1 (Steer)** | `CAN1` — **`AVL ID 89`** | `5,100 kg` | **`7,100 kg`** | Front cab + engine weight |
| **Tractor Axle 2 (Drive 1)** | `CAN1` — **`AVL ID 90`** | `3,100 kg` | **`6,000 kg`** | Half of fifth-wheel kingpin load |
| **Tractor Axle 3 (Drive 2)** | `CAN1` — **`AVL ID 91`** | `3,100 kg` | **`6,000 kg`** | Half of fifth-wheel kingpin load |
| **Tractor Subtotal (`CAN1`)** | `AVL 89 + 90 + 91` *(or `AVL 10898`)* | **`11,300 kg`** | **`19,100 kg`** | **35% of cargo sits on the kingpin** |
| **Trailer 3-Axle Bogie (`CAN2`)** | `CAN2` — **`AVL ID 13657`** | **`4,200 kg`** | **`24,900 kg`** | **65% of cargo sits on trailer bogie** |
| **Total Combination (`GCVW`)** | `CAN1` — **`AVL ID 139`** | **`15,500 kg`** | **`44,000 kg`** | **`19,100 kg + 24,900 kg = 44,000 kg`** |

---

### Variant C: Sitrak C7H `6x4` Rigid Truck / Dump Tipper (*Camion Porteur / Benne 6x4 — Sans Remorque*)
* **Physical Setup:** The cargo box or dump body is bolted directly onto the Sitrak's 3-axle chassis (`Axle 1` Steer + `Axle 2 & 3` Rear Tandem). There is **no trailer** (`CAN2` is unused or used for Tachograph).
* **Weight Parameters Used:**
  * **100% of the cargo rests on the tractor's 3 axles (`CAN1`)**:
    * `AVL ID 89` (`Axle 1`): `7,500 kg`
    * `AVL ID 90` (`Axle 2`): `13,000 kg`
    * `AVL ID 91` (`Axle 3`): `13,000 kg`
    * `AVL ID 139` (`Combined vehicle weight`): **`33,500 kg`**

---

## Part 2: If We Have FMS Axle Weights (`CAN1`), Why Do We Still Need TrailerCAN (`CAN2`)?

Even if your Sitrak tractor has ECAS air suspension on `CAN1`, **relying on `CAN1` alone fails in 6 critical real-world scenarios**:

### 1. The 35% vs. 65% Semi-Trailer Physics Split
On an articulated tractor-trailer (`13.6 m` semi-trailer):
* Only **~30% to 35%** of the cargo weight presses down on the tractor's fifth-wheel kingpin (`CAN1` `AVL ID 90 + 91`).
* The remaining **~65% to 70%** of the cargo weight rests directly on the **trailer's rear 3-axle bogie (`CAN2` `AVL ID 13657`)**!

### 2. Rear-Door Cargo Theft Detection (`4×` Higher Sensitivity on `CAN2`)
Suppose thieves open the **rear doors of the trailer** at night and steal **`1,000 kg` (20 bags of cement)** from the back of the trailer:
* Because those pallets are sitting right on top of the rear trailer bogie (11 meters behind the kingpin):
  * **Tractor Axles (`CAN1` `AVL 90 + 91`)** barely change by **`-80 kg`** (invisible inside normal suspension friction!).
  * **Trailer Bogie (`CAN2` `AVL ID 13657`)** immediately drops by **`-920 kg`**!
* Without `CAN2` TrailerCAN, rear-door theft of `500–1,500 kg` is completely undetectable.

### 3. Most Export Sitrak Tractors Have Steel Leaf Springs on `CAN1`
As shown in Variant A above, most heavy-duty export SINOTRUK SITRAK `4x2` and `6x4` tractors have **steel leaf springs** with no axle load sensors on `CAN1`, whereas almost all modern semi-trailers (CIMC, Schmitz, Krone, Lecitrailer) have **WABCO TEBS E** with a built-in pressure transducer on `CAN2`.

### 4. Preventing False Overnight Theft Alarms (`AVL ID 13810` Pneumatic Supply Pressure)
* When a driver parks overnight with the **engine OFF**, the air compressor stops. Over 6–8 hours, air slowly bleeds out of the trailer's airbags (`AVL ID 13657` drops from `24,900 kg` down to `0 kg` as the chassis settles onto its rubber bump stops).
* If you only look at weight, your server will trigger a **false "24-Ton Cargo Theft Alarm" at 03:00 AM**!
* **TrailerCAN (`CAN2`)** provides **`AVL ID 13810` (`trailer.pneumatic.supply.pressure`, `kPa`)** and **`AVL ID 13774` (`trailer.pneumatic.supply.state.enum`)**.
* When `AVL ID 13810` drops below **`650 kPa` (`6.5 bar`)**, the Flespi `tidj` plugin knows the air tanks are empty and **locks the last valid weight (`fleet_trailer_axle_stable = 24,900 kg`)**, preventing any false alarm!

### 5. Automatic Trailer Identification (`AVL ID 13671` VIN) & Coupling (`AVL ID 13651`)
* Tractors swap trailers every day. Only `CAN2` TrailerCAN gives you:
  * **`AVL ID 13651` (`trailer.towing.state.enum`):** Instant hook/unhook detection (`1 = Coupled`, `0 = Uncoupled`).
  * **`AVL ID 13671` (`can.trailer.vin`):** The exact **17-character VIN** of whichever trailer is currently plugged into the Sitrak's 7-pin ISO 7638 socket!

### 6. WABCO Safety, Rollover Prevention & Brake Health (`AVL ID 13665–13679`)
* Only `CAN2` TrailerCAN reports:
  * **Individual Brake Cylinder Pressures (`AVL ID 13665–13670`)** on all 6 trailer wheels (detecting a seized or non-braking trailer wheel).
  * **Roll-Over Protection (`AVL ID 13678`)**, **VDC Active (`AVL ID 13672`)**, and **Lateral Acceleration (`AVL ID 13673`)** (detecting when a driver takes a curve too fast and WABCO auto-brakes the trailer to prevent a tip-over).
  * **Lift Axle Position (`AVL ID 13681 / 13682`)** (verifying that the driver isn't driving empty with the lift axle dragging on the asphalt).
