---
title: FMC650 2×10 socket pinout — plain algorithm
schema-image: ../assets/first-start/Fmc_650_2x10_pinout.png
source-table: https://wiki.teltonika-gps.com/view/FMC650_First_Start#2x10_socket_pinout
captured: 2026-11-04
---

# FMC650 2×10 socket — plain algorithm

Derived from the color-coded connector diagram ([image](../assets/first-start/Fmc_650_2x10_pinout.png)) and the official pinout table on the wiki.

## What the connector is

- One physical plug: **2 columns × 10 rows = 20 pins**.
- Odd pins **1–9 (and 10)** on the **left** column, even pins **11–20** on the **right** column of the diagram.

## Algorithm: map a required function to a pin

For each function the installer needs, pick pins from the list below exactly:

| # | Function | Pins | Rule |
| --- | --- | --- | --- |
| 1 | Connect power supply | **11** = `VCC (+)`, **1** = `GND (−)` | +8…32 V DC; connect GND/POWER directly to battery terminals or low-impedance point (see mounting notes); external fuse **3 A, 125 V** |
| 2 | Detect ignition | **15** = `DIN 1` | Dedicated to ignition input. Verify real ignition wire (power must not disappear when engine runs) — do not confuse with ACC |
| 3 | E earth/ground of peripherals | **1** | Same GND returns |
| 4 | CAN bus 1 (SAE J1939) | **12** = `CAN1H`, **2** = `CAN1L` | High/Low pair — keep twisted |
| 5 | CAN bus 2 (SAE J1939) | **16** = `CAN2H`, **6** = `CAN2L` | High/Low pair — keep twisted |
| 6 | Dallas 1-Wire® devices (e.g. iButton, temperature sensor) | **3** = `1 WIRE POWER`, **13** = `1 WIRE DATA` | Power + data; device ground shares pin 1 |
| 7 | Digital inputs | **5** = `DIN 2`, **14** = `DIN 3`, **4** = `DIN 4` | Channel 1 (ignition) is reserved on pin 15 |
| 8 | Analog inputs | **17** = `AIN 1`, **7** = `AIN 2`, **10** = `AIN 3` | Range **0–30 V / 0–10 V DC** (configurable) |
| 9 | Digital outputs (open collector) | **19** = `DOUT 1`, **9** = `DOUT 2`, **8** = `DOUT 3`, **18** = `DOUT 4` | Open collector — needs external pull-up to switched supply |
| 10 | Pin 18 as analog instead of digital | **18** = `DOUT4/AIN 4` | Shared pin: digital output **or** analog input, range 0–30 V / 0–10 V DC |
| 11 | Tachograph data (K-Line) | **20** = `K-LINE` | K-LINE interface for online tachograph vehicle data transfer |

## Algorithm: safe wiring procedure (derived constraints)

1. `WHILE` device is connected to power or internal battery is connected:
   `DO NOT modify 2×10 wiring` (per safety info: disconnect 2×10 before unmounting; disconnect vehicle power supply jumpers before connecting cables).
2. Insert SIM cards and connect battery only while the case is open and powered off (First Start steps 1–6).
3. Connect wires with the module **not plugged in**; fasten wires to non-moving parts; no exposed wires.
4. After wiring the power source: measure voltage again — car computer sleep mode may remove power 5–30 min after ignition off.
5. For ground wire: attach to vehicle frame or fixed metal part; if bolted, crimp the ring loop; scrub paint for better contact.
6. `AFTER` wiring: connect 8–32 V DC power, observe **FMC650 LED status** (see [FMC650 LED status page](https://wiki.teltonika-gps.com/view/FMC650_LED_status)).

## Cross-check (diagram ⇄ table)

The diagram colors in the image are a legend for wire colors in Teltonika's cable harnesses; the pin numbers and names above are verified against the wiki table text (`PIN NUMBER / PIN NAME / DESCRIPTION` = 20 rows) — no mismatch found on 2026-11-04 capture.

## Related

- [FMC650 First Start](../first-start.md) — step 1 of the knowledge project
- Source page: [FMC650_First_Start § 2x10 socket pinout](https://wiki.teltonika-gps.com/view/FMC650_First_Start#2x10_socket_pinout)
