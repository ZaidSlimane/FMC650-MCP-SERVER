---
title: FMC650 and Tachograph Solution
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_and_Tachograph_Solution
archived-snapshot: https://web.archive.org/web/20260423034059/https://wiki.teltonika-gps.com/view/FMC650_and_Tachograph_Solution
captured: 2026-11-04
---

# FMC650 and Tachograph Solution

Single content page describing how to connect the FMC650 to a tachograph and download DDD files through Teltonika **WEB Tacho**. Referenced twice from [`../Configuration/24_can-tachograph/`](../Configuration/24_can-tachograph/can-tachograph.md) (CAN2 wiring and installation instructions).

```
tachograph-solution.md   full page, 11 headings, 11 figures
assets/                  11 preserved images
```

## Contents

| Section | Figures | Covers |
| --- | --- | --- |
| Introduction | — | WEB Tacho service, hourly DDD download cycle, EU Smart Tachograph v2 deadlines |
| Supported tachographs and formats | 5 | Siemens VDO DTCO 1381, Stoneridge SE5000, Intellic EFAS 4 — how to read the version/part number |
| Remote Data Download (RDD) via FMS | 2 | Vehicles whose FMS carries the RDD signal; FMS connector pinout |
| Connecting to tachograph | 3 | CAN line resistance measurement, wire routing, wiring diagram |
| Checking connection (tachocheck SMS) | — | Verifying that data is present on the connected lines |
| Configuring device | 1 | CAN/Tachograph and WEB Tacho settings in the configurator |
| Internal links | — | Product and wiki links |

## Notes

- All **11** figures are archived and preserved (`VDO_Tachograph_1/2`, `STONERIDGE_1.3`, `INTELLIC_1/2`, `FMS_connector`, `FMS_connector1`, `Tacho_connection`, `Wires`, `Wiring_diagram`, `Configuration_tacho1111`).
- **Source quirk:** the introduction names the **FMM650** ("FMM650 device has a possibility to connect to Web Tacho…") on a page titled *FMC650 and Tachograph Solution*; the compatibility list also names FMB/FMC/FMM640 and FMB641. Kept verbatim — it reads as copied boilerplate from the FMM650 page.
- Two images of the same FMS connector (`FMS_connector.png`, `FMS_connector1.png`) appear in the source and are both kept.
- Snapshot `2026-04-23` — latest capture at extraction time (CDX-verified).
