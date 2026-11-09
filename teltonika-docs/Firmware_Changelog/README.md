---
title: FMC650 Firmware Changelog
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Firmware_Changelog
archived-snapshot: https://web.archive.org/web/20260416084726/https://wiki.teltonika-gps.com/view/FMC650_Firmware_Changelog
captured: 2026-11-04
---

# FMC650 Firmware Changelog

Two related wiki pages document the FMC650 firmware history:

```
01_firmware-changelog/   FMC650_Firmware_Changelog — current release notes, 8 releases
02_firmware-errata/      FMC650_firmware_errata     — older/partial copy of the same list, 7 releases
```

## Items

| # | Folder | Page | Releases | Bullets | Snapshot | Chars |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | [`01_firmware-changelog/`](01_firmware-changelog/firmware-changelog.md) | [FMC650_Firmware_Changelog](https://wiki.teltonika-gps.com/view/FMC650_Firmware_Changelog) | 8 (newest **03.01.01.rev.15**, 2026.03.26) | 175 | 2026-04-16 | 16,044 |
| 02 | [`02_firmware-errata/`](02_firmware-errata/firmware-errata.md) | [FMC650_firmware_errata](https://wiki.teltonika-gps.com/view/FMC650_firmware_errata) | 7 (newest **03.01.00.Rev.14**, 2025.05.27) | 110 | 2026-01-18 | 7,652 |

Both pages open with the same *Introduction* and *Firmware versioning* sections.

## Firmware versioning

```
FMX[##].VER.[XX].[YY].[ZZ].Rev.[##] _[ID###]
```

- `FMX[##]` — device model the firmware is compatible with.
- `XX` — major FW version.
- `YY` — branch number, shows major changes (new module support, new major feature).
- `ZZ` — major changes such as bigger fixes, improvements and new features.
- `##` — minor changes such as small fixes and improvements.
- `ID[###]` — Spec ID KEY, used for specific-client firmware changes.

## Format

The source renders releases as a 3-column table (`FIRMWARE VERSION | RELEASE DATE | CHANGES`). Each *CHANGES* cell contains bold group labels plus bullet lists, some nested three levels deep (e.g. `New Features → IO elements → individual IO names`). A Markdown table cell cannot hold that structure, so each release is rendered here as its own `###` section — every word, order and link is unchanged. The conversion restored **175** bullets in the changelog and **110** in the errata, including nesting.

## Notes

- **01 vs 02:** the errata page is a stale subset — it carries the same wording for releases up to `03.01.00.Rev.14` and stops there, while the changelog also lists `03.01.01.rev.15` (2026.03.26). The errata snapshot (2026-01-18) predates the changelog snapshot (2026-04-16).
- **Links preserved:** the changelog's release notes link to `RAM memory`, `one minute rule`, `Apache Thermograph`, `Trailer CAN`, `scanevfms`, `can_info` and `tachocheck` wiki pages; these are kept as absolute wiki URLs.
- **Source quirks kept verbatim:** literal `*` footnote markers before `NEW!` / `Initial release` (escaped as `\*` so they render literally), inconsistent version casing (`rev.15` vs `Rev.14`), and typos such as *vehciles*, *Tall Tale 4*.
- Both pages are linked from the firmware-update PCNs under [`../Product_Change_Notifications/`](../Product_Change_Notifications/README.md).
- Snapshots are the latest captures at extraction time (CDX-verified).
