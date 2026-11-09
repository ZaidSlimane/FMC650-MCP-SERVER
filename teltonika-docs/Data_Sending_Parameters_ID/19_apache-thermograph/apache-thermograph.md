---
title: "FMC650 Data Sending Parameters ID — Apache Thermograph"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "Apache Thermograph"
---

# Apache Thermograph

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 13362 | Device Serial Number | 4 | Unsigned | 0 | 2147483647 | - | - | Apache thermograph serial number | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13363 | Device Version | 17 | Unisgned | 0 | 0 | - | - | Apache thermograph software version | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13364 | Datetime | 20 | Unsigned | 0 | 0 | - | - | Apache thermograph current time | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13365 | Sensor 1 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 1 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13366 | Sensor 1 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 1 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13367 | Sensor 2 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 2 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13368 | Sensor 2 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 2 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13369 | Senor 3 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 3 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13370 | Sensor 3 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 3 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13371 | Sensor 4 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 4 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13372 | Sensor 4 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 4 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13373 | Sensor 5 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 5 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13374 | Sensor 5 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 5 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13375 | Sensor 6 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 6 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13376 | Sensor 6 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 6 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13377 | Sensor 7 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 7 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13378 | Sensor 7 Unit | 1 | Signed | 0 | 255 | - | - | Apache thermograph Sensor 7 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13379 | Sensor 8 Value | 2 | Signed | -32768 | 32768 | - | - | Apache thermograph Sensor 8 value | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13380 | Sensor 8 Unit | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Sensor 8 unit | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13381 | Device Status | 2 | Unsigned | 0 | 0xFFFF | - | - | Apache thermograph status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13382 | Vehicle Plate | 16 | Unsigned | 0 | 0 | - | - | Apache thermograph vehicle plate | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13383 | Thermograph Battery Voltage | 2 | Unsigned | 0 | 65535 | - | mV | Apache thermograph battery voltage | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13384 | Frigo Machine Type | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph Frigo machine type | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13385 | Frigo Overall and Engine Status | 2 | Unsigned | 0 | 0xFFFF | - | - | Apache thermograph Frigo engine status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13386 | Frigo Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph Frigo additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13387 | Frigo Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph Frigo additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13388 | Frigo Engine Hours | 4 | Unsigned | 0 | 2147483647 | - | h | Apache thermograph Frigo engine hours | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13389 | Frigo Standby Hours | 4 | Unsigned | 0 | 2147483647 | - | h | Apache thermograph Frigo standby hours | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13390 | Frigo Switch on Hours | 4 | Unsigned | 0 | 2147483647 | - | h | Apache thermograph Frigo switch on hours | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13391 | Frigo Active Alarms 1 to 4 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph Frigo active alarm codes 1 to 4 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13392 | Frigo Active Alarms 5 to 8 | 0 | 0 | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph Frigo active alarm codes 5 to 8 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13393 | Frigo Active Alarms 9 to 12 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph Frigo active alarm codes 9 to 12 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13394 | Frigo Active Alarms 13 to 16 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph Frigo active alarm codes 13 to 16 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13395 | Frigo Comp 1 Set Point | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 1 set point temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13396 | Frigo Comp 1 Supply | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 1 supply temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13397 | Frigo Comp 1 Return | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 1 set point temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13398 | Frigo Comp 1 Status | 2 | Unsigned | 0 | 0xFFFF | - | - | Apache thermograph Frigo Comp. 1 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13399 | Frigo Comp 2 Set Point | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 2 set point temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13400 | Frigo Comp 2 Supply | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 2 supply temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13401 | Frigo Comp 2 Return | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 2 return temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13402 | Frigo Comp 2 Status | 2 | Unsigned | 0 | 0xFFFF | - | - | Apache thermograph Frigo Comp. 2 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13403 | Frigo Comp 3 Set Point | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 3 set point temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13404 | Frigo Comp 3 Supply | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 3 supply temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13405 | Frigo Comp 3 Return | 2 | Signed | -32768 | 32768 | - | 10*°C | Apache thermograph Frigo Comp. 3 return temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13406 | Frigo Comp 3 Status | 2 | Unsigned | 0 | 0xFFFF | - | - | Apache thermograph Frigo Comp. 3 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13407 | EBS type | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS type | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13408 | EBS Status | 2 | Unsigned | 0 | 0xFFFF | - | - | Apache thermograph EBS status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13409 | EBS Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13410 | EBS Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13411 | EBS Wheel Speed | 1 | Unsigned | 0 | 255 | - | km/h | Apache thermograph EBS wheel speed | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13412 | EBS Odometer | 4 | Unsigned | 0 | 2147483647 | - | km/h | Apache thermograph EBS odometer | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13413 | EBS Weight Load | 2 | Unsigned | 0 | 65535 | - | 10*t | Apache thermograph EBS weight load | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13414 | EBS Pneumatic Supply | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS pneumatic supply | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13415 | EBS Truck VIN | 18 | Unsigned | 0 | 0 | - | - | Apache thermograph EBS truck VIN | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13416 | EBS Active Alarms 1 to 4 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS active alarm codes 1 to 4 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13417 | EBS Active Alarms 5 to 8 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS active alarm codes 5 to 8 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13418 | EBS Active Alarms 9 to 12 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS active alarm codes 9 to 12 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13419 | EBS Active Alarms 13 to 16 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS active alarm codes 13 to 16 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13420 | EBS Security Status 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS security status 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13421 | EBS Security Status 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS security status 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13422 | EBS TPMS Status 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS TPMS status 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13423 | EBS TPMS Status 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS TPMS status 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13424 | EBS Tyre 1 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 1 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13425 | EBS Tyre 1 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 1 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13426 | EBS Tyre 1 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 1 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13427 | EBS Tyre 1 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 1 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13428 | EBS Tyre 1 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 1 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13429 | EBS Tyre 1 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 1 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13430 | EBS Tyre 2 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 2 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13431 | EBS Tyre 2 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 2 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13432 | EBS Tyre 2 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 2 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13433 | EBS Tyre 2 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 2 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13434 | EBS Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 2 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13435 | EBS Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 2 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13436 | EBS Tyre 3 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 3 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13437 | EBS Tyre 3 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 3 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13438 | EBS Tyre 3 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 3 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13439 | EBS Tyre 3 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 3 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13440 | EBS Tyre 3 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 3 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13441 | EBS Tyre 3 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 3 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13442 | EBS Tyre 4 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 4 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13443 | EBS Tyre 4 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 4 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13444 | EBS Tyre 4 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 4 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13445 | EBS Tyre 4 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 4 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13446 | EBS Tyre 4 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 4 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13447 | EBS Tyre 4 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 4 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13448 | EBS Tyre 5 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 5 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13449 | EBS Tyre 5 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 5 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13450 | EBS Tyre 5 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 5 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13451 | EBS Tyre 5 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 5 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13452 | EBS Tyre 5 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 5 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13453 | EBS Tyre 5 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 5 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13454 | EBS Tyre 6 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 6 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13455 | EBS Tyre 6 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 6 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13456 | EBS Tyre 6 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 6 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13457 | EBS Tyre 6 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 6 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13458 | EBS Tyre 6 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 6 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13459 | EBS Tyre 6 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 6 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13548 | EBS Tyre 7 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 7 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13549 | EBS Tyre 7 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 7 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13550 | EBS Tyre 7 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 7 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13551 | EBS Tyre 7 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 7 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13552 | EBS Tyre 7 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 7 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13553 | EBS Tyre 7 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 7 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13554 | EBS Tyre 8 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 8 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13555 | EBS Tyre 8 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 8 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13556 | EBS Tyre 8 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 8 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13557 | EBS Tyre 8 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 8 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13558 | EBS Tyre 8 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 8 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13559 | EBS Tyre 8 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 8 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13560 | EBS Tyre 9 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 9 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13561 | EBS Tyre 9 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 9 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13562 | EBS Tyre 9 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 9 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13563 | EBS Tyre 9 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 9 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13564 | EBS Tyre 9 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 9 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13565 | EBS Tyre 9 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 9 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13566 | EBS Tyre 10 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 10 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13567 | EBS Tyre 10 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 10 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13568 | EBS Tyre 10 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 10 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13569 | EBS Tyre 10 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 10 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13570 | EBS Tyre 10 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 10 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13571 | EBS Tyre 10 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 10 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13572 | EBS Tyre 11 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 11 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13573 | EBS Tyre 11 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 11 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13574 | EBS Tyre 11 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 11 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13575 | EBS Tyre 11 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 11 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13576 | EBS Tyre 11 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 11 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13577 | EBS Tyre 11 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 11 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13578 | EBS Tyre 12 Position | 1 | Unsigned | 0 | 255 | - | - | Apache thermograph EBS Tyre 12 position | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13579 | EBS Tyre 12 Pressure | 1 | Unsigned | 0 | 255 | - | 10*Bar | Apache thermograph EBS Tyre 12 pressure | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13580 | EBS Tyre 12 Temperature | 2 | Signed | -32768 | 32767 | - | 10*°C | Apache thermograph EBS Tyre 12 temperature | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13581 | EBS Tyre 12 Status | 1 | Unsigned | 0 | 0xFF | - | - | Apache thermograph EBS Tyre 12 status | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13582 | EBS Tyre 12 Additional Data 0 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 12 additional data 0 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
| 13583 | EBS Tyre 12 Additional Data 1 | 8 | Unsigned | 0 | 0xFFFFFFFFFFFFFFFF | - | - | Apache thermograph EBS Tyre 12 additional data 1 | FMX650 ExpandFMC650 / FMM650 | Apache Thermograph IO |
