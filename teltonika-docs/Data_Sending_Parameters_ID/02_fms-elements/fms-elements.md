---
title: "FMC650 Data Sending Parameters ID — FMS elements"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "FMS elements"
---

# FMS elements

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 79 | Brake Switch | 1 | Unsigned | 0 | 1 | - | - | 0 - Pedal released / 1 - Pedal pressed | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 80 | Wheel Based Speed | 4 | Unsigned | 0 | 65536 | - | km/h | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 81 | Cruise Control Active | 1 | Unsigned | 0 | 1 | - | - | 0 - Switched off / 1 - Switched on | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 82 | Clutch Switch | 1 | Unsigned | 0 | 1 | - | - | 0 - Pedal released / 1 - Pedal pressed | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 83 | PTO State | 1 | Unsigned | 0 | 1 | - | - | 0 - Off/disabled / 1 - Set / 2 - Not available | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 84 | Acceleration Pedal Position | 4 | Unsigned | 0 | 102 | - | % | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 85 | Engine Current Load | 1 | Unsigned | 0 | 125 | - | % | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 86 | Engine Total Fuel Used | 4 | Unsigned | 0 | 2105540607 | - | l | Value in liters, L | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 87 | Fuel Level | 4 | Unsigned | 0 | 102 | - | % | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 88 | Engine Speed | 4 | Unsigned | 0 | 8032 | - | rpm | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 89 | Axle weight 1 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 90 | Axle weight 2 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 91 | Axle weight 3 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 92 | Axle weight 4 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 93 | Axle weight 5 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 94 | Axle weight 6 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 95 | Axle weight 7 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 96 | Axle weight 8 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 97 | Axle weight 9 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 98 | Axle weight 10 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 99 | Axle weight 11 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 100 | Axle weight 12 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 101 | Axle weight 13 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 102 | Axle weight 14 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 103 | Axle weight 15 | 2 | Unsigned | 0 | 32766 | - | kg | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 104 | Engine Total Hours Of Operation | 4 | Unsigned | 0 | 214748364 | - | h | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 109 | Software Version Supported | 4 | Unsigned | 0 | 0xffffffff | - | - | Format: ab.cd / ab = byte1 byte2 / cd = byte3 byte4 / | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 110 | Diagnostics Supported | 1 | Unsigned | 0 | 3 | - | - | 0 - Diagnostics is not supported / 1 - Diagnostics is supported / 2 - Reserved / 3 - Do not care / | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 111 | Requests Supported | 1 | Unsigned | 0 | 3 | - | - | 0 - Request is not supported / 1 - Request is supported / 2 - Reserved / 3 - Do not care / | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 113 | Service Distance | 4 | Signed | -160635 | 167040 | - | km | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 122 | Direction Indication | 1 | Unsigned | 0 | 3 | - | - | 0 - Vehicle is moving Forward / 1 - Reverse / 2 - Error / 3 - Not available / | FMB640 / FMC640 / FMM640 | FMS elements |
| 123 | Tachograph Performance | 1 | Unsigned | 0 | 3 | - | - | 0 - Normal performance / 1 - Performance analysis / 2 - Error / 3 - Not available / | FMB640 / FMC640 / FMM640 | FMS elements |
| 124 | Handling Info | 1 | Unsigned | 0 | 3 | - | - | 0 - No handling information / 1 - Handling information / 2 - Error / 3 - Not available / | FMB640 / FMC640 / FMM640 | FMS elements |
| 125 | System Event | 1 | Unsigned | 0 | 3 | - | - | 0 - No tachograph event / 1 - Tachograph event / 2 - Error / 3 - Not available / | FMB640 / FMC640 / FMM640 | FMS elements |
| 127 | Engine Coolant Temperature | 1 | Signed | -40 | 210 | - | °C | Offset by -40 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 128 | Ambient Air Temperature | 2 | Signed | -273 | 1770 | - | °C | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 135 | Fuel Rate | 4 | Unsigned | 0 | 3212 | - | l/h | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 136 | Instantaneous Fuel Economy | 4 | Unsigned | 0 | 125 | - | km/l | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 137 | PTO Drive Engagement | 1 | Unsigned | 0 | 3 | - | - | 0 - No PTO drive is engaged / 1 - At least one PTO drive is engaged / 2 - Error / 3 - Not available / | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 138 | High Resolution Engine Total Fuel Used | 4 | Unsigned | 0 | 4211081.215 | - | l or ml | Resolution in l or ml depending on the FMS fuel settings (item id 121) | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 139 | Gross Combination Vehicle Weight | 4 | Unsigned | 0 | 642550 | - | kg | The total weight of the truck and all attached trailers. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 229 | AdBlue status | 1 | Unsigned | 0 | 3 | - | - | 0 - Off / 1 - Cond. Red / 2 - Cond. Yellow / 3 - Cond. info / | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 357 | Brake Pedal Position | 1 | Unsigned | 0 | 100 | - | % | The ratio of current brake pedal position to the maximum possible position | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10348 | Fuel level 2 | 1 | Unsigned | 0 | 100 | - | % | This parameter shows fuel level in secondary tank (if fuel type is different then currently used fuel) | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10349 | MIL indicator | 1 | Unsigned | 0 | 100 | - | - | 0 - OFF / 1 - Condition Red / 2 - Condition Yellow / 3 - Condition Info / 7 - Not Available / / There are three possible conditions stated: Red, Yellow, Info. The interpretation of the status is manufacturer dependant and might be different. For details please refer to the manufacturer’s document. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10428 | Tell Tale 0 | 8 | HEX | 0 | 0xffffffffffffffff | - | - | IO element describes Tell Tale Block ID message received from Block ID 0 in Hexadecimal format. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10429 | Tell Tale 1 | 8 | HEX | 0 | 0xffffffffffffffff | - | - | IO element describes Tell Tale Block ID message received from Block ID 1 in Hexadecimal format. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10430 | Tell Tale 2 | 8 | HEX | 0 | 0xffffffffffffffff | - | - | IO element describes Tell Tale Block ID message received from Block ID 2 in Hexadecimal format. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10431 | Tell Tale 3 | 8 | HEX | 0 | 0xffffffffffffffff | - | - | IO element describes Tell Tale Block ID message received from Block ID 3 in Hexadecimal format. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 13259 | Tell Tale 4 | 8 | HEX | 0 | 0xffffffffffffffff | - | - | IO element describes Tell Tale Block ID message received from Block ID 4 in Hexadecimal format. | FMC650 | FMS elements |
| 10455 | AdBlue level | 1 | Unsigned | 0 | 100 | - | % | AdBlue level | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | FMS elements |
| 10493 | DTC DM1 | 4 | Unsigned | 0 | 4294967295 | - | - | DTC DM1 | FMB640 | FMS elements |
| 10494 | DTC DM1 List | Var | ASCII | 0 | 1024 | - | - | DTC DM1 List | FMB640 | FMS elements |
| 10495 | DTC DM2 | 4 | Unsigned | 0 | 4294967295 | - | - | DTC DM2 | FMB640 | FMS elements |
| 10496 | DTC DM2 List | Var | ASCII | 0 | 1024 | - | - | DTC DM2 List | FMB640 | FMS elements |
