# 06 — Troubleshooting Missing FMS Axle Weights, "Gross Sum Only", & `CAN1 Bus Mode` (`Silent` vs `Normal`)

This guide explains:
1. The **7 root causes** why an FMC650 fails to receive FMS Axle Weights (`AVL ID 89–103`).
2. Why an FMC650 receives **ONLY the Gross Sum (`AVL ID 139` on FMS or `AVL ID 13657` on TrailerCAN)** even though `Axle 1..4` (`AVL ID 89–92`) have their priority set to **`Low (1)`**.
3. What **`CAN1 Bus Mode` (`PID 206`: `0 = Silent` vs `1 = Normal`)** does and why 95% of CAN parameters arrive normally in `Silent` mode.

---

## Part 1: Why Does the FMC650 Receive ONLY the Gross Sum (`AVL ID 139`) Even When `Axle 1..4` Are Set to `Low`?

In [`FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md`](../fmc650-reverse-engineered/mds/FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md), both `Combined vehicle weight` (`AVL ID 139`, Priority `High = 2`) and `Axle 1..4 load` (`AVL ID 89–92`, Priority `Low = 1`) are enabled.

Yet on the truck, **only `AVL ID 139` (`Combined vehicle weight` / `total.vehicle.weight`) arrives**, while `AVL ID 89–92` stay empty.

### The Exact Reason: They Come from Two Different J1939 PGNs & Two Different ECUs!

| FMC650 Parameter | Wire `AVL ID` (`.cfg` `IoId`) | J1939 PGN & SPN | Which ECU Broadcasts It on Sitrak C7H? | Broadcast Rule in J1939 Standard |
| :--- | :--- | :--- | :--- | :--- |
| **`Combined vehicle weight`** (`total.vehicle.weight`) | **`AVL ID 139`** (`IoId 46530` = `High`) | **`PGN 65134` (`0x00FE6E`)**<br>*Combination Vehicle Weight (`SPN 1760`)* | **ZF TraXon 12TX Gearbox (`TCU`) / Bosch Engine ECU (`EMS`) / EBS** | **Automatic Cyclic Broadcast every `1,000 ms`** (Works in `Silent` mode!) |
| **`Axle 1..4 load`** (`can.axle.weight.1..4`) | **`AVL ID 89–92`** (`IoId 45290..45320` / `46100..46130` = `Low`) | **`PGN 65258` (`0x00FEEA`)**<br>*Vehicle Weight (`SPN 928` Axle Location + `SPN 582` Axle Weight)* | **ECAS Air Suspension ECU ONLY** | **On-Request (`PGN 59904`)** + Requires physical sensors on each axle! |

Because they are two completely different messages, **two mechanisms cause `AVL ID 139` to arrive without `AVL ID 89–92`**:

#### 1. The ZF TraXon Gearbox Calculates `AVL ID 139` Even on Steel-Spring Trucks!
* Your SINOTRUK SITRAK C7H uses a **ZF TraXon 12TX automated manual gearbox (`TCU`)** and **Bosch EDC17 Engine ECU**.
* Even if the Sitrak tractor has **steel leaf springs (zero physical weight sensors on Axles 1, 2, or 3)**, the **ZF TraXon gearbox** continuously calculates **`PGN 65134` (`Combined vehicle weight` $\rightarrow$ `AVL ID 139`)** using **Engine Torque + Wheel Acceleration + Road Grade ($m = F / a$)** (or sums it with the trailer EBS over ISO 11992) so the gearbox knows whether to start in **1st gear** (when loaded at `44,000 kg`) or **4th gear** (when empty at `15,500 kg`)!
* However, because the tractor has no physical pressure sensors on Axle 1, Axle 2, or Axle 3, **`PGN 65258` (`Axle 1..4 load`, `AVL ID 89–92`) is `0xFFFF` (*"Not Available"*)**, so the FMC650 omits `AVL ID 89–92` and sends **only `AVL ID 139`**.

#### 2. `CAN1 Bus Mode` Is Set to `Silent` (`PID 206 = 0`), Blocking the Request for `PGN 65258`!
* Even if a truck *does* have ECAS air suspension on its tractor axles:
  * **`PGN 65134` (`AVL ID 139` — Combined Vehicle Weight)** is broadcast **automatically every 1 second** by the truck.
  * **`PGN 65258` (`AVL ID 89–92` — Individual Axle Weights)** is an **On-Request message** (`PGN 59904` / `0xEA00`).
* In `P2_PRODUCTION_v1.2`, **`CAN1 Bus Mode` (`PID 206`) is set to `0` (`Silent`)**. In `Silent` mode, the FMC650 hears the automatic `PGN 65134` broadcast (`AVL ID 139`), **but cannot transmit the `PGN 59904` request needed to wake up `PGN 65258` (`AVL ID 89–92`)**!

*(Note: Similarly, on **`CAN2` TrailerCAN**, WABCO TEBS E only sends **`AVL ID 13657` (`Axle Load Sum`)** from `EBS22` `PGN 65218` because all 6 trailer airbags share a single pressure sensor on Port `42`, so individual trailer axle fields are `0xFFFF` Not Available.)*

---

## Part 2: What Does `CAN1 Bus Mode` (`PID 206`) Do, and Why Do We Receive 95% of CAN Data Normally in `Silent` Mode?

**`CAN1 Bus Mode` (`PID 206`)** controls whether the FMC650's CAN transceiver acts as a **One-Way Radio Receiver (`Silent`)** or a **Two-Way Walkie-Talkie (`Normal`)** ([`can-tachograph.md`](../teltonika-docs/Configuration/24_can-tachograph/configurator/can-tachograph.md)):

| `PID 206` Value | Mode Name | Hardware Behavior |
| :---: | :--- | :--- |
| **`0`** *(Default in `P2_v1.2`)* | **`Silent` (Passive Listening)** | **Receiver ON, Transmitter OFF.**<br>The FMC650 only *listens* to frames already flowing on the truck's wires. Its "microphone" is muted—it never sends a single bit or ACK onto the truck's CAN bus. |
| **`1`** | **`Normal` (Active Two-Way)** | **Receiver ON, Transmitter ON.**<br>The FMC650 both *listens* to the bus **and** can *transmit* J1939 Request frames (`PGN 59904`), Manual CAN Requests, or Tachograph `.DDD` download commands onto the truck's CAN bus. |

### Why 95% of CAN Data Arrives Normally in `Silent` Mode (`PID 206 = 0`)
On a heavy truck's J1939 network, there are **two types of messages**:

1. **Type A — Automatic "Cyclic Broadcast" Messages (95% of all data):**
   The truck's Engine (`MC13`), Gearbox (`ZF TraXon`), Brakes (`EBS`), and Dashboard constantly broadcast these messages automatically without anyone asking:
   * **Engine RPM (`AVL ID 88`, `PGN 61444`):** Broadcast every **`20 ms`**
   * **Wheel Speed (`AVL ID 80`, `PGN 65265`):** Broadcast every **`100 ms`**
   * **Accelerator / Brake Pedal (`AVL ID 84 / 357`):** Broadcast every **`50–100 ms`**
   * **Fuel Level (`AVL ID 87`) & Coolant Temp (`AVL ID 127`):** Broadcast every **`1,000 ms`**
   * **Combined Vehicle Weight (`AVL ID 139`, `PGN 65134`):** Broadcast every **`1,000 ms`**
   * **Result:** Because the truck shouts these onto the wire every second, the FMC650 hears all of them in **`Silent` mode (`PID 206 = 0`)**!

2. **Type B — "On-Request" Messages (The Remaining 5% of J1939 Data):**
   To avoid bus congestion, SAE J1939 defines certain messages as **"On-Request Only"** (*sur demande uniquement*):
   * **`PGN 65258` (`0x00FEEA`) — Individual Axle Weights (`AVL ID 89–103`)**
   * **`PGN 65253` (`0x00FEE5`) — Total Engine Hours (`AVL ID 104`)** *(on some gateways)*
   * **`PGN 65260` (`0x00FEEC`) — Vehicle VIN (`AVL ID 233–235`)**
   * **Tachograph `.DDD` Legal File Downloads**
   * **Result:** On Locked FMS gateways, the ECU will **not** transmit `PGN 65258` unless the FMC650 is in **`Normal` mode (`PID 206 = 1`)** and sends a J1939 Request (`PGN 59904`).

---

## Part 3: Complete Checklist of the 7 Reasons FMC650 Does Not Receive FMS Axle Weights (`AVL ID 89–103`)

| # | Root Cause | Symptom | Fix / Action |
| :-: | :--- | :--- | :--- |
| **1** | **Tractor Has Steel Leaf Springs (No Physical Axle Sensors)** | RPM, Fuel, Speed, and `AVL ID 139` (`GCVW`) arrive on `CAN1`, but `AVL ID 89–92` are missing. | **100% normal** for steel-spring Sitrak tractors. Use `AVL ID 139` (`CAN1` GCVW) + `AVL ID 13657` (`CAN2` Trailer Bogie Sum). |
| **2** | **Locked FMS Gateway + `CAN1` in `Silent` Mode (`PID 206 = 0`)** | Tractor has ECAS airbags, RPM/Fuel arrive, but `AVL ID 89–92` never arrive. | Switch `CAN1 Bus Mode` to **`Normal`** (`setparam 206:1`) and enable **Locked FMS Request** (requires direct wire connection, not contactless alligator clips). |
| **3** | **Connected to Filtered OBD Port Instead of FMS / Chassis CAN** | Even in `Normal` mode, suspension PGNs are blocked by the Central Gateway. | Connect `CAN1H` (Pin `12`) and `CAN1L` (Pin `2`) to the **12-pin FMS Gateway connector** or internal **Chassis/ECAS CAN bus**. |
| **4** | **Wrong CAN1 Baudrate (`250` vs `500 kbps`) or Wrong Source (`PID 210`)** | **Zero** FMS parameters arrive (`AVL ID 80, 87, 88, 139` all missing). | Check `PID 205` (`250` vs `500 kbps`) and `PID 210` (`0 = CAN1`). |
| **5** | **Proprietary Chinese ECAS PGN on SINOTRUK** | Cab screen shows axle loads, but standard FMS `PGN 65258` is not used. | Capture a 30s CAN log (`.can_dbg:1` + `.can_dbg_filter:1`) and map the custom 29-bit CAN ID in **`Manual CAN` (`AVL ID 145–214`)**. |
| **6** | **Configurator Priority Disabled (`IoId + 0 = 0`) or `IO Send Mode` (`PID 221 = 0`)** | Specific axles (e.g., `Axle 6..15`, `IoId 46150..46240`) are `Disabled` (`0`), or `0xFFFF` values are suppressed because `PID 221 = 0` (`Don't Send`). | Enable `IoId` Priority (`1 = Low`) or temporarily test with `setparam 221:1` (`Send Zero`) to see if `0` / `65535` arrives. |
| **7** | **Truck Ignition Is OFF (`AVL ID 239 = 0`)** | Tracker sends GPS packets while parked, but CAN values do not update. | Turn Ignition **ON** (`DIN1 = 1`); truck ECUs sleep when the key is OFF. |

---

## Part 4: Quick Field Diagnostic Commands (SMS / GPRS / Flespi)

1. **Scan Which FMS Elements Are Live on `CAN1` (With Engine Running):**
   ```text
   scanfms
   ```
   *Returns a comma-separated list of `0`s and `1`s showing every FMS parameter currently detected on `CAN1` ([`locked-fms-feature.md`](../teltonika-docs/manual/27_locked-fms-feature/locked-fms-feature.md)).*
2. **Switch `CAN1` to `Normal` Mode (`PID 206 = 1`) to Allow J1939 Requests:**
   ```text
   setparam 206:1
   ```
3. **Temporarily Force FMC650 to Send Zero / N/A CAN Values (`PID 221 = 1`) for Debugging:**
   ```text
   setparam 221:1
   ```
   *(Remember to restore `setparam 221:0` after testing so `0xFFFF` values don't pollute Wialon sensors.)*
