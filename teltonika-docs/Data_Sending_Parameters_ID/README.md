---
title: FMC650 Teltonika Data Sending Parameters ID
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
---

# FMC650 Teltonika Data Sending Parameters ID

Reference page listing the **AVL data-sending parameter IDs** the FMC650 can report, grouped by source: permanent I/O, FMS, CAN adapters, LV-CAN, eventual I/O, manual CAN, tachograph, Mobileye, TPMS, reefer, TK scanners, EV FMS, cameras, ISOBUS, BLE and Apache thermograph.

The wiki page is **not a hub** — it is 19 sections, each holding one long parameter table. Those sections are split here into one folder each, in page order:

- `<NN>_<slug>/<slug>.md` — the section heading plus its full table, with YAML front matter recording the snapshot and the source section.
- No `assets/`: the page contains no images.

## Sections

| # | Folder | Section | Parameter rows | Property ID range | Chars |
| --- | --- | --- | --- | --- | --- |
| 01 | [`01_permanent-io-elements/`](01_permanent-io-elements/permanent-io-elements.md) | Permanent I/O elements | 93 | 1–13200 | 19336 |
| 02 | [`02_fms-elements/`](02_fms-elements/fms-elements.md) | FMS elements | 55 | 79–13259 | 10138 |
| 03 | [`03_can-adapters-elements/`](03_can-adapters-elements/can-adapters-elements.md) | CAN adapters elements | 72 | 12–10632 | 13736 |
| 04 | [`04_lv-can-elements/`](04_lv-can-elements/lv-can-elements.md) | LV-CAN elements | 213 | 12710–12922 | 21796 |
| 05 | [`05_eventual-io-elements/`](05_eventual-io-elements/eventual-io-elements.md) | Eventual I/O elements | 127 | 52–10612 | 25354 |
| 06 | [`06_manual-can-elements/`](06_manual-can-elements/manual-can-elements.md) | Manual CAN elements | 70 | 145–10347 | 11947 |
| 07 | [`07_tachograph-data-elements/`](07_tachograph-data-elements/tachograph-data-elements.md) | Tachograph data elements | 79 | 48–13263 | 22419 |
| 08 | [`08_mobileye-elements/`](08_mobileye-elements/mobileye-elements.md) | Mobileye elements | 39 | 288–326 | 8297 |
| 09 | [`09_contipressurecheck-tpms/`](09_contipressurecheck-tpms/contipressurecheck-tpms.md) | ContiPressureCheck TPMS | 75 | 10189–10407 | 10399 |
| 10 | [`10_reefer-io/`](10_reefer-io/reefer-io.md) | Reefer IO | 47 | 10045–10649 | 8646 |
| 11 | [`11_tk-transcan-io/`](11_tk-transcan-io/tk-transcan-io.md) | TK Transcan IO | 12 | 10683–10694 | 2488 |
| 12 | [`12_tk-euroscan-io/`](12_tk-euroscan-io/tk-euroscan-io.md) | TK Euroscan IO | 10 | 484–10467 | 2406 |
| 13 | [`13_tk-touchprint-io/`](13_tk-touchprint-io/tk-touchprint-io.md) | TK Touchprint IO | 9 | 10695–10703 | 2146 |
| 14 | [`14_ev-fms-elements/`](14_ev-fms-elements/ev-fms-elements.md) | EV FMS elements | 26 | 10456–10904 | 4427 |
| 15 | [`15_cameras-video/`](15_cameras-video/cameras-video.md) | Cameras/Video | 21 | 12301–12306 | 4458 |
| 16 | [`16_isobus/`](16_isobus/isobus.md) | ISOBUS | 298 | 12400–124451 | 61834 |
| 17 | [`17_ble/`](17_ble/ble.md) | BLE | 46 | 548–10500 | 7992 |
| 18 | [`18_ev-fms/`](18_ev-fms/ev-fms.md) | EV FMS | 24 | 10879–10904 | 3182 |
| 19 | [`19_apache-thermograph/`](19_apache-thermograph/apache-thermograph.md) | Apache Thermograph | 134 | 13362–13583 | 23806 |

**Totals:** 19 sections, 1450 parameter rows, 0 images.

## Table format

Each table has the same columns, with a two-row header in the source:

`Property ID in AVL packet | Property Name | Bytes | Type | Value range (Min / Max) | Multiplier | Units | Description | HW Support | Parameter Group`

The merged `Value range` header is kept as a cell followed by an empty cell so that `Min` and `Max` stay aligned with their data columns. Cell text is verbatim (including comma decimal separators such as `0,001` and source typos); only the table grid was rebuilt.

## Notes

- **Overlap:** several groups duplicate tables that also appear on the module pages — e.g. LVCAN/FMS/Tachograph in [`../Configuration/18_lvcan-fms-tachograph-data-elements/`](../Configuration/18_lvcan-fms-tachograph-data-elements/lvcan-fms-tachograph-data-elements.md), ISOBUS in [`../Configuration/19_isobus/`](../Configuration/19_isobus/isobus.md). This page is the consolidated cross-module ID list.
- **Duplicate headings:** sections 14 (*EV FMS elements*) and 18 (*EV FMS*) are separate tables in the source and are kept separate here (28 and 26 rows).
- **No images, no links** are present on the source page; content is tables only.
- Snapshot `2026-04-16` — the latest capture at extraction time.

<!-- configurator-companions -->

## Configurator notes (EN)

English notes translated from the Configurator tab PDFs, generated **2026-11-05**:

- [`configurator/avl-protocols.md`](configurator/avl-protocols.md) — Teltonika FMC650 AVL & data-collection protocols: codecs 8/8E/16, IMEI handshake, binary structure and Wialon pipeline.

