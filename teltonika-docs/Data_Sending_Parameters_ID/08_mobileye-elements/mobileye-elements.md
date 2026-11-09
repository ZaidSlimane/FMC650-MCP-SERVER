---
title: "FMC650 Data Sending Parameters ID — Mobileye elements"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "Mobileye elements"
---

# Mobileye elements

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 288 | ME Sound Type | 1 | Unsigned | 0 | 7 | - | - | 0 - Silent; / 1 - LWD Left; / 2 - LWD Right; / 3 - HW 1; / 4 - TSR; / 5 - UFCW; / 6 - FCW + PCW; / 7 - Peds in danger zone (if enabled). | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 289 | ME Pedestrians in Danger Zone | 1 | Unsigned | 0 | 1 | - | - | 0 - Pedestrian not in danger zone; / 1 - Pedestrian in danger zone. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 290 | ME Pedestrians in Forward Collision Warning | 1 | Unsigned | 0 | 1 | - | - | 0 - No forward collision warning; / 1 - Forward collision warning. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 291 | ME Time Indicator | 1 | Unsigned | 0 | 2 | - | - | 0 - Day is indicated; / 1 - Dusk is indicated; / 2 - Night is indicated. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 292 | ME Error Valid | 1 | Unsigned | 0 | 1 | - | - | 0 - Error; / 1 - No error. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 293 | ME Error Code | 1 | Unsigned | 0 | 127 | - | - | Error code | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 294 | ME Zero Speed | 1 | Unsigned | 0 | 1 | - | - | 0 - Host vehicle is moving; / 1 - Host vehicle is stopped. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 295 | ME Headway Valid | 1 | Unsigned | 0 | 1 | - | - | 0 - Headway Valid is off; / 1 - Headway Valid is on (when CIPV is detected). | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 296 | ME Headway Measurement | 1 | Unsigned | 0 | 9,9 | 0,1 | - | Seconds | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 297 | ME LDW Off | 1 | Unsigned | 0 | 1 | - | - | 0 - LDW are enabled; / 1 - LDW are disabled. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 298 | ME Left LDW On | 1 | Unsigned | 0 | 1 | - | - | 0 - Left LDW are enabled; / 1 - Left LDW are disabled. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 299 | ME Right LDW On | 1 | Unsigned | 0 | 1 | - | - | 0 - Right LDW are enabled; / 1 - Right LDW are disabled. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 300 | ME Maintenance | 1 | Unsigned | 0 | 1 | - | - | 0 - Internal error is not detected; / 1 - Internal error is detected. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 301 | ME Fail Safe | 1 | Unsigned | 0 | 1 | - | - | 0 - Fail Safe indicator is off; / 1 - Fail Safe indicator (modes) is on (blur image, saturated image, low sun, partial blockage, partial transparent). | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 302 | ME FCW On | 1 | Unsigned | 0 | 1 | - | - | 0 - FCW are disabled; / 1 - FCW are enabled; | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 303 | ME TSR Enabled | 1 | Unsigned | 0 | 1 | - | - | 0 - TSR feature is disabled; 1 - TSR feature is enabled. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 304 | ME Headway Warning Repeat Enabled | 1 | Unsigned | 0 | 1 | - | - | 0 - Headway Warning Repeat is disabled; / 1 - Headway Warning Repeat is enabled. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 305 | ME Headway Warning Level | 1 | Unsigned | 0 | 2 | - | - | 0 - No CIPV is present; / 1 - A CIPV is present with HW > HW Config; / 2 - A CIPV is present with HW <= HW Config or HW < 0,6. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 306 | ME TSR Warning Level | 1 | Unsigned | 0 | 7 | - | - | 0 - Speed <= Road Speed; 1 - Speed > Road Speed + [0-5 km/h]; / 2 - Speed > Road Speed + [5-10 km/h]; / 3 - Speed > Road Speed + [10-15 km/h]; / 4 - Speed > Road Speed + [15-20 km/h]; / 5 - Speed > Road Speed + [20-25 km/h]; / 6 - Speed > Road Speed + [25-30 km/h]; / 7 - Speed > Road Speed + [30-35 km/h] and + 35 km/h; | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 307 | ME Tamper Alert | 1 | Unsigned | 0 | 1 | - | - | 0 - No tamper alert; / 1 - Tamper alert. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 308 | ME High Beam | 1 | Unsigned | 0 | 1 | - | - | 0 - Off; / 1 - On. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 309 | ME Low Beam | 1 | Unsigned | 0 | 1 | - | - | 0 - Off; / 1 - On. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 310 | ME Wipers | 1 | Unsigned | 0 | 1 | - | - | 0 - Off; / 1 - On. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 311 | ME Right Signal | 1 | Unsigned | 0 | 1 | - | - | 0 - Off; / 1 - On. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 312 | ME Left Signal | 1 | Unsigned | 0 | 1 | - | - | 0 - Off; / 1 - On. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 313 | ME Brake Signal | 1 | Unsigned | 0 | 1 | - | - | 0 - Off; / 1 - On. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 314 | ME Wipers Available | 1 | Unsigned | 0 | 1 | - | - | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 315 | ME Low Beam Available | 1 | Unsigned | 0 | 1 | - | - | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 316 | ME High Beam Available | 1 | Unsigned | 0 | 1 | - | - | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 317 | ME Speed Available | 1 | Unsigned | 0 | 1 | - | - | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 318 | ME Speed | 1 | Unsigned | 0 | 255 | - | km/h | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 319 | ME TSR 1 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 320 | ME TSR 2 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 321 | ME TSR 3 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 322 | ME TSR 4 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 323 | ME TSR 5 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 324 | ME TSR 6 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 325 | ME TSR 7 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye sign recognition data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
| 326 | ME TSR VO | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Mobileye vision only sign type data | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Mobileye elements |
