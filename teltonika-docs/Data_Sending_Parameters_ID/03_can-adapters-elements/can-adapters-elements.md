---
title: "FMC650 Data Sending Parameters ID — CAN adapters elements"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "CAN adapters elements"
---

# CAN adapters elements

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 12 | Program Number | 2 | Unsigned | 0 | 999 | - | - | Value: Min – 0, Max – 999 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 13 | Module ID | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Module ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 14 | Engine Worktime | 4 | Unsigned | 0 | 16777215 | - | min | Engine work time in minutes | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 15 | Engine Worktime (Counted) | 4 | Unsigned | 0 | 16777215 | - | min | Total Engine work time in minutes | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 16 | Total Mileage (Counted) | 4 | Unsigned | 0 | 4294967295 | - | m | Total Vehicle Mileage, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 17 | Fuel Consumed (counted) | 4 | Unsigned | 0 | 2147483647 | 0,1 | l | Total Fuel Consumed, l | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 18 | Fuel Rate | 2 | Unsigned | 0 | 32768 | 0,1 | l/h | Fuel Rate l/h | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 19 | AdBlue Level Percent | 1 | Unsigned | 0 | 255 | - | % | AdBlue, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 20 | AdBlue Level Liters | 2 | Unsigned | 0 | 65535 | 0,1 | l | AdBlue level, L | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 23 | Engine Load | 1 | Unsigned | 0 | 130 | - | % | Engine load, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 25 | Engine Temperature | 2 | Signed | -600 | 1270 | 0,1 | °C | Engine Temperature, °C | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 26 | Axle 1 Load | 2 | Unsigned | 0 | 32768 | - | kg | Axle 1 load, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 27 | Axle 2 Load | 2 | Unsigned | 0 | 32768 | - | kg | Axle 2 load, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 28 | Axle 3 Load | 2 | Unsigned | 0 | 32768 | - | kg | Axle 3 load, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 29 | Axle 4 Load | 2 | Unsigned | 0 | 32768 | - | kg | Axle 4 load, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 30 | Vehicle Speed | 1 | Unsigned | 0 | 255 | - | km/h | Value in km/h | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 31 | Accelerator Pedal Position | 1 | Unsigned | 0 | 255 | - | % | Value in persentages, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 32 | Axle 5 Load | 2 | Unsigned | 0 | 32768 | - | kg | Axle 5 load, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 33 | Fuel Consumed | 4 | Unsigned | 0 | 2147483647 | 0,1 | l | Value in liters, L | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 34 | Fuel Level Liters | 2 | Unsigned | 0 | 65535 | 0,1 | l | Value in liters, L | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 35 | Engine RPM | 2 | Unsigned | 0 | 16384 | - | rpm | Value in rounds per minute, rpm | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 36 | Total Mileage | 4 | Unsigned | 0 | 4294967295 | - | m | Value in meters, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 37 | Fuel Level Percent | 1 | Unsigned | 0 | 255 | - | % | Value in percentages, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 38 | Control State Flags | 4 | Unsigned | 0 | 4294967295 | - | - | Control State Flags | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 39 | Agricultural Machinery Flags | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Agricultural machinery flags | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 40 | Harvesting Time | 4 | Unsigned | 0 | 16777215 | - | min | Harvesting time, minutes | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 41 | Area of Harvest | 4 | Unsigned | 0 | 4294967295 | - | m2 | Area of Harvest, m2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 42 | Mowing Efficiency | 4 | Unsigned | 0 | 4294967295 | - | m2/h | Mowing efficiency, (m^2)/h | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 43 | Grain Mown Volume | 4 | Unsigned | 0 | 4294967295 | - | kg | Mown Volume, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 44 | Grain Moisture | 2 | Unsigned | 0 | 65535 | 0,1 | % | Grain Moisture in proc, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 45 | Harvesting Drum RPM | 2 | Unsigned | 0 | 65535 | - | rpm | Harvesting Drum RPM, RPM | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 46 | Gap Under Harvesting Drum | 1 | Unsigned | 0 | 255 | - | mm | Gap Under Harvesting Drum, mm | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 47 | Security State Flags | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Security State Flag | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 141 | Battery Temperature | 2 | Unsigned | -600 | 1270 | 0,1 | °C | Degrees, °C | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 142 | Battery Level Percent | 1 | Unsigned | 0 | 255 | - | % | Value in percentages, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 143 | Door Status | 2 | Unsigned | 0 | 16128 | - | - | Min – 0, Max – 16128 / Door status is represented as bitmask converted to decimal value. / Possible values: / 0 – all doors closed, / 0x100 (256) – front left door is opened, / 0x200 (512) – front right door is opened, / 0x400 (1024) – rear left door is opened, / 0x800 (2048) – rear right door is opened, / 0x1000 (4096) – hood is opened, / 0x2000 (8192) – trunk is opened, / 0x3F00 (16128) – all doors are opened, or combinations of values | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 176 | DTC Errors | 1 | Unsigned | 0 | 255 | - | - | DTC Errors | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 226 | CNG Status | 1 | Unsigned | 0 | 1 | - | - | 0 - Engine not on CNG; / 1 - Engine on CNG. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 227 | CNG Used | 4 | Unsigned | 0 | 4294967295 | - | kg | CNG Used | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 228 | CNG Level | 2 | Unsigned | 0 | 65535 | - | % | CNG Level | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 500 | Slope Of Arm | 2 | Signed | -3276 | 3276 | - | ° | Slope Of Arm, degrees ° | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 501 | Rotation Of Arm | 2 | Signed | -180 | 180 | - | ° | Rotation Of Arm, degrees ° | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 502 | Eject Of Arm | 2 | Unsigned | 0 | 6553 | - | m | Eject Of Arm, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 503 | Horizontal Distance Arm | 2 | Unsigned | 0 | 6553 | - | m | Horizontal Distance Arm Vehicle, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 504 | Height Arm Above Ground | 2 | Unsigned | 0 | 6553 | - | m | Height Arm Above ground, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 505 | Drill RPM | 2 | Unsigned | 0 | 65535 | - | rpm | Drill RPM, RPM | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 506 | Spread Salt | 2 | Unsigned | 0 | 655 | - | g/m2 | Amount Of Spread Salt Square Meter, g/m2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 507 | Battery Voltage | 2 | Unsigned | 0 | 6553 | - | V | Battery Voltage, V | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 508 | Spread Fine Grained Salt | 4 | Unsigned | 0 | 1677722 | - | T | Amount Of Spread Fine Grained Salt, T | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 509 | Coarse Grained Salt | 4 | Unsigned | 0 | 1677722 | - | T | Amount Of Coarsed Grained Salt, T | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 510 | Spread DiMix | 4 | Unsigned | 0 | 1677722 | - | T | Amount Of Spread DiMix, T | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 511 | Spread Coarse Grained Calcium | 4 | Unsigned | 0 | 1677722 | - | m2 | Amount Of Spread Coarse Grained Calcium, m2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 512 | Spread Calcium Chloride | 4 | Unsigned | 0 | 1677722 | - | m2 | Amount Of Spread Calcium Chloride, m2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 513 | Spread Sodium Chloride | 4 | Unsigned | 0 | 1677722 | - | m2 | Amount Of Spread Sodium Chloride, m2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 514 | Spread Magnesium Chloride, m2 | 4 | Unsigned | 0 | 1677722 | - | m2 | Amount Of Spread Magnesium Chloride, m2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 515 | Amount Of Spread Gravel | 4 | Unsigned | 0 | 1677722 | - | T | Amount Of Spread Gravel, T | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 516 | Amount Of Spread Sand | 4 | Unsigned | 0 | 1677722 | - | T | Amount Of Spread Sand, T | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 517 | Width Pouring Left | 2 | Unsigned | 0 | 655 | - | m | Width pouring left, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 518 | Width Pouring Right | 2 | Unsigned | 0 | 655 | - | m | Width pouring right, m | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 519 | Salt Spreader Working Hours | 4 | Unsigned | 0 | 1677722 | - | h | Salt Spreader Working Hours, h | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 520 | Distance During Salting | 4 | Unsigned | 0 | 1677722 | - | km | Distance During salting, km | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 521 | Load Weight | 4 | Unsigned | 0 | 16777215 | - | kg | Load Weight, kg | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 522 | Retarder Load | 1 | Unsigned | 0 | 130 | - | % | Retarder Load, % | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 523 | Cruise Time | 4 | Unsigned | 0 | 16777215 | - | min | Cruise time, minutes | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 524 | Engine Oil Level | 1 | Unsigned | 0 | 255 | - | - | Oil level | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 525 | Fault Codes | 128 | ASCII | 0 | 128 | - | - | Fault Codes (values seperated via ".") | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 526 | Vehicles Range On Battery | 4 | Unsigned | 0 | 16777215 | - | m | Vehicles Range On Battery | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 527 | Vehicles Range On Additional Fuel | 4 | Unsigned | 0 | 2147483647 | - | m | Vehicles Range On Additional Fuel | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 528 | VIN | 17 | ASCII | 0 | 0xFF | - | - | VIN number | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 529 | Module ID 17B | 17 | HEX | 0 | 0x7fffffffffffffff | - | - | Module ID 17 bytes | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 10631 | LVCAN Driver Seatbelt | 1 | Unsigned | 0 | 1 | - | - | Driver Seatbelt | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
| 10632 | LVCAN Front Passenger Seatbelt | 1 | Unsigned | 0 | 1 | - | - | Front Passenger Seatbelt | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | CAN adapters elements |
