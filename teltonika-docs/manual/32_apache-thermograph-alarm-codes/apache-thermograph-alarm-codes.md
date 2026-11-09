---
title: FMC650 Apache Thermograph Alarm Code Parsing
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Apache_Thermograph_Alarm_Code_Parsing
archived-snapshot: https://web.archive.org/web/20260410143817/https://wiki.teltonika-gps.com/view/FMC650_Apache_Thermograph_Alarm_Code_Parsing
captured: 2026-11-04
---

# FMC650 Apache Thermograph Alarm Code Parsing

# Introduction

AT+FRIGO and AT+EBS commands can send up to 16 Active Alarm codes each. To reduce IO count, 4 Active Alarms are being combined into single IO. Parsing examples of each Active Alarm IO can be seen below.

# Examples

**Note:** The following examples are examples and not actual alarm codes.

*Active Alarms 1 to 4 parsing example.*

| **Active Alarms 1 to 4 code: 0x1A5B6C9DF04568AA** | — |
| --- | --- |
| 0x68AA | Alarm 1 |
| 0xF045 | Alarm 2 |
| 0x6C9D | Alarm 3 |
| 0x1A5B | Alarm 4 |

*Active Alarms 5 to 8 parsing example.*

| **Active Alarms 5 to 8 code: 0x7F3A2D8CB91E47F2** | — |
| --- | --- |
| 0x47F2 | Alarm 5 |
| 0xB91E | Alarm 6 |
| 0x2D8C | Alarm 7 |
| 0x7F3A | Alarm 8 |

*Active Alarms 9 to 12 parsing example.*

| **Active Alarms 9 to 12 code: 0x4C98EB7A0531ACD7** | — |
| --- | --- |
| 0xACD7 | Alarm 9 |
| 0x0531 | Alarm 10 |
| 0xEB7A | Alarm 11 |
| 0x4C98 | Alarm 12 |

*Active Alarms 13 ot 16 parsing example.*

| **Active Alarms 13 to 16 code: 0x9AB24F6ED8375C14** | — |
| --- | --- |
| 0x5C14 | Alarm 13 |
| 0xD837 | Alarm 14 |
| 0x4F6E | Alarm 15 |
| 0x9AB2 | Alarm 16 |

# Error Codes

Upon trying to read information from thermograph for 3 consecutive times and failing to receive response, error values will be set to all IO’s. For integer type of IO’s error value will be maximum possible value for this specific IO. For string type of IO’s, None will be set.
