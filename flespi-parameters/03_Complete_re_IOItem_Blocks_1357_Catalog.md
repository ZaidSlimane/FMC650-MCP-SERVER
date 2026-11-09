---
title: "Complete Catalog of All 1,357 FMC650 IOItem Configuration Blocks in re/ (6,451 IDs) & Flespi setio Mapping"
device: "FMC650"
re_schema_source: "fmc650-reverse-engineered/re/fmx65_03.01.01.Rev.15_schema.json"
official_flespi_source: "https://flespi.com/devices/teltonika-fmc650"
captured: "2026-11-05"
---

# Complete Catalog of All 1,357 `in_cfg` `IOItem` Configuration Blocks in `re/` (`6,451` IDs) & Flespi `setio` Mapping

In [`fmc650-reverse-engineered/re/fmx65_03.01.01.Rev.15_schema.json`](./re/fmx65_03.01.01.Rev.15_schema.json), **6,451 out of the 11,688 `in_cfg` parameters (`55.2%`)** belong to **1,357 `IOItem` configuration blocks** (`IoId + order`, where `order` in `0..5` represents `[Priority, Operand, High Level, Low Level, Event Only, Average]`).

> [!WARNING]
> - **These `IoId` numbers (`45100..181330`) are Configuration `ParameterId`s, NOT Telemetry `AVL ID`s!**
> - Out of these **1,357 `IOItem` blocks**, Flespi only exposes **12 dedicated `*_io` settings** (`50080`, `50120`, `50150`, `50160`, `50170`, `50180`, `50220`, `50230`, `50240`, `50270`, `50280`, `50660`).
> - The remaining **1,345 `IOItem` blocks (`6,381` Configuration `ParameterId`s)** have **no dedicated Flespi setting** and must be configured using Flespi's official **`setio` command** (`{"id": <IoId_Base>, "priority": ..., "operand": ..., "high": ..., "low": ..., "event": ..., "average": ...}`) or **`setparam`**.

| # | `re/` `IoId` Base (`Priority` PID) | `in_cfg` Field Range | `re/` Element Label | Units | Ref `.cfg` Priority (`cfg_value`) | Dedicated Flespi Setting (`-settings` tab) | Official Flespi Command (`-commands` tab) |
|---:|---:|---|---|---|---|---|---|
| 1 | **`45100`** | `45100..45105` (6) | **Vehicle speed** | `km/h` | `0` | — *(None)* | `setio` (`{"id": 45100, ...}`) |
| 2 | **`45110`** | `45110..45115` (6) | **Acceleration pedal position** | `%` | `0` | — *(None)* | `setio` (`{"id": 45110, ...}`) |
| 3 | **`45120`** | `45120..45124` (5) | **Fuel Consumed** | `ltr×10` | `0` | — *(None)* | `setio` (`{"id": 45120, ...}`) |
| 4 | **`45130`** | `45130..45135` (6) | **Fuel level** | `ltr×10` | `0` | — *(None)* | `setio` (`{"id": 45130, ...}`) |
| 5 | **`45140`** | `45140..45145` (6) | **Engine RPM** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 45140, ...}`) |
| 6 | **`45150`** | `45150..45154` (5) | **Total mileage** | `m` | `0` | — *(None)* | `setio` (`{"id": 45150, ...}`) |
| 7 | **`45160`** | `45160..45165` (6) | **Fuel level** | `%` | `0` | — *(None)* | `setio` (`{"id": 45160, ...}`) |
| 8 | **`45170`** | `45170..45174` (5) | **Door status** | `—` | `0` | — *(None)* | `setio` (`{"id": 45170, ...}`) |
| 9 | **`45180`** | `45180..45184` (5) | **Program number** | `—` | `0` | — *(None)* | `setio` (`{"id": 45180, ...}`) |
| 10 | **`45190`** | `45190..45194` (5) | **Module ID 8B** | `—` | `0` | — *(None)* | `setio` (`{"id": 45190, ...}`) |
| 11 | **`45200`** | `45200..45204` (5) | **Engine worktime** | `min` | `0` | — *(None)* | `setio` (`{"id": 45200, ...}`) |
| 12 | **`45210`** | `45210..45214` (5) | **Engine worktime (counted)** | `min` | `0` | — *(None)* | `setio` (`{"id": 45210, ...}`) |
| 13 | **`45220`** | `45220..45224` (5) | **Total mileage (counted)** | `m` | `0` | — *(None)* | `setio` (`{"id": 45220, ...}`) |
| 14 | **`45230`** | `45230..45234` (5) | **Fuel consumed (counted)** | `ltr×10` | `0` | — *(None)* | `setio` (`{"id": 45230, ...}`) |
| 15 | **`45240`** | `45240..45245` (6) | **Fuel rate** | `ltr/h` | `0` | — *(None)* | `setio` (`{"id": 45240, ...}`) |
| 16 | **`45250`** | `45250..45255` (6) | **AdBlue level** | `%` | `0` | — *(None)* | `setio` (`{"id": 45250, ...}`) |
| 17 | **`45260`** | `45260..45265` (6) | **AdBlue level** | `ltr×10` | `0` | — *(None)* | `setio` (`{"id": 45260, ...}`) |
| 18 | **`45270`** | `45270..45275` (6) | **Engine load** | `%` | `0` | — *(None)* | `setio` (`{"id": 45270, ...}`) |
| 19 | **`45280`** | `45280..45285` (6) | **Engine temperature** | `℃×10` | `0` | — *(None)* | `setio` (`{"id": 45280, ...}`) |
| 20 | **`45290`** | `45290..45295` (6) | **Axle 1 load** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45290, ...}`) |
| 21 | **`45300`** | `45300..45305` (6) | **Axle 2 load** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45300, ...}`) |
| 22 | **`45310`** | `45310..45315` (6) | **Axle 3 load** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45310, ...}`) |
| 23 | **`45320`** | `45320..45325` (6) | **Axle 4 load** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45320, ...}`) |
| 24 | **`45330`** | `45330..45335` (6) | **Axle 5 load** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45330, ...}`) |
| 25 | **`45340`** | `45340..45344` (5) | **Control state flags** | `—` | `0` | — *(None)* | `setio` (`{"id": 45340, ...}`) |
| 26 | **`45350`** | `45350..45354` (5) | **Agricultural machinery flags** | `—` | `0` | — *(None)* | `setio` (`{"id": 45350, ...}`) |
| 27 | **`45360`** | `45360..45364` (5) | **Harvesting time** | `min` | `0` | — *(None)* | `setio` (`{"id": 45360, ...}`) |
| 28 | **`45370`** | `45370..45374` (5) | **Area of harvest** | `m²` | `0` | — *(None)* | `setio` (`{"id": 45370, ...}`) |
| 29 | **`45380`** | `45380..45385` (6) | **Mowing efficiency** | `m²/h` | `0` | — *(None)* | `setio` (`{"id": 45380, ...}`) |
| 30 | **`45390`** | `45390..45394` (5) | **Grain mown volume** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45390, ...}`) |
| 31 | **`45400`** | `45400..45405` (6) | **Grain moisture** | `%` | `0` | — *(None)* | `setio` (`{"id": 45400, ...}`) |
| 32 | **`45410`** | `45410..45415` (6) | **Harvesting drum RPM** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 45410, ...}`) |
| 33 | **`45420`** | `45420..45425` (6) | **Gap under harvesting drum** | `mm` | `0` | — *(None)* | `setio` (`{"id": 45420, ...}`) |
| 34 | **`45430`** | `45430..45434` (5) | **Security state flags** | `—` | `0` | — *(None)* | `setio` (`{"id": 45430, ...}`) |
| 35 | **`45440`** | `45440..45444` (5) | **Tachograph total vehicle distance** | `m` | `0` | — *(None)* | `setio` (`{"id": 45440, ...}`) |
| 36 | **`45450`** | `45450..45454` (5) | **Trip distance** | `m` | `0` | — *(None)* | `setio` (`{"id": 45450, ...}`) |
| 37 | **`45460`** | `45460..45464` (5) | **Tachograph vehicle speed** | `km/h` | `0` | — *(None)* | `setio` (`{"id": 45460, ...}`) |
| 38 | **`45620`** | `45620..45625` (6) | **Battery temperature** | `℃` | `0` | — *(None)* | `setio` (`{"id": 45620, ...}`) |
| 39 | **`45630`** | `45630..45635` (6) | **Battery level** | `%` | `0` | — *(None)* | `setio` (`{"id": 45630, ...}`) |
| 40 | **`45640`** | `45640..45644` (5) | **DTC Faults** | `—` | `0` | — *(None)* | `setio` (`{"id": 45640, ...}`) |
| 41 | **`45650`** | `45650..45654` (5) | **Slope Of Arm** | `°` | `0` | — *(None)* | `setio` (`{"id": 45650, ...}`) |
| 42 | **`45660`** | `45660..45664` (5) | **Rotation Of Arm** | `°` | `0` | — *(None)* | `setio` (`{"id": 45660, ...}`) |
| 43 | **`45670`** | `45670..45674` (5) | **Eject Of Arm** | `m` | `0` | — *(None)* | `setio` (`{"id": 45670, ...}`) |
| 44 | **`45680`** | `45680..45684` (5) | **Horizontal Distance Arm Vehicle** | `m` | `0` | — *(None)* | `setio` (`{"id": 45680, ...}`) |
| 45 | **`45690`** | `45690..45694` (5) | **Height Arm Above Ground** | `m` | `0` | — *(None)* | `setio` (`{"id": 45690, ...}`) |
| 46 | **`45700`** | `45700..45704` (5) | **Drill RPM** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 45700, ...}`) |
| 47 | **`45710`** | `45710..45714` (5) | **Amount Of spread Salt Square Meter** | `g/m²` | `0` | — *(None)* | `setio` (`{"id": 45710, ...}`) |
| 48 | **`45720`** | `45720..45724` (5) | **Battery Voltage** | `V` | `0` | — *(None)* | `setio` (`{"id": 45720, ...}`) |
| 49 | **`45730`** | `45730..45734` (5) | **Amount Of Spread Fine Grained Salt** | `T` | `0` | — *(None)* | `setio` (`{"id": 45730, ...}`) |
| 50 | **`45740`** | `45740..45744` (5) | **Amount Of Spread Coarse Grained Salt** | `T` | `0` | — *(None)* | `setio` (`{"id": 45740, ...}`) |
| 51 | **`45750`** | `45750..45754` (5) | **Amount Of Spread DiMix** | `T` | `0` | — *(None)* | `setio` (`{"id": 45750, ...}`) |
| 52 | **`45760`** | `45760..45764` (5) | **Amount Of Spread Coarse Grained Calcium** | `m³` | `0` | — *(None)* | `setio` (`{"id": 45760, ...}`) |
| 53 | **`45770`** | `45770..45774` (5) | **Amount Of Spread Calcium Chloride** | `m³` | `0` | — *(None)* | `setio` (`{"id": 45770, ...}`) |
| 54 | **`45780`** | `45780..45784` (5) | **Amount Of Spread Sodium Chloride** | `m³` | `0` | — *(None)* | `setio` (`{"id": 45780, ...}`) |
| 55 | **`45790`** | `45790..45794` (5) | **Amount Of Spread Magnesium Chloride** | `m³` | `0` | — *(None)* | `setio` (`{"id": 45790, ...}`) |
| 56 | **`45800`** | `45800..45804` (5) | **Amount Of Spread Gravel** | `T` | `0` | — *(None)* | `setio` (`{"id": 45800, ...}`) |
| 57 | **`45810`** | `45810..45814` (5) | **Amount Of Spread Sand** | `T` | `0` | — *(None)* | `setio` (`{"id": 45810, ...}`) |
| 58 | **`45820`** | `45820..45824` (5) | **Width Pouring Left** | `m` | `0` | — *(None)* | `setio` (`{"id": 45820, ...}`) |
| 59 | **`45830`** | `45830..45834` (5) | **Width Pouring Right** | `m` | `0` | — *(None)* | `setio` (`{"id": 45830, ...}`) |
| 60 | **`45840`** | `45840..45844` (5) | **Salt Spreader Working Hours** | `h` | `0` | — *(None)* | `setio` (`{"id": 45840, ...}`) |
| 61 | **`45850`** | `45850..45854` (5) | **Distance During Salting** | `km` | `0` | — *(None)* | `setio` (`{"id": 45850, ...}`) |
| 62 | **`45860`** | `45860..45864` (5) | **Load Weight** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45860, ...}`) |
| 63 | **`45870`** | `45870..45874` (5) | **Retarder Load** | `%` | `0` | — *(None)* | `setio` (`{"id": 45870, ...}`) |
| 64 | **`45880`** | `45880..45884` (5) | **Cruise Time** | `min` | `0` | — *(None)* | `setio` (`{"id": 45880, ...}`) |
| 65 | **`45890`** | `45890..45894` (5) | **CNG Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 45890, ...}`) |
| 66 | **`45900`** | `45900..45904` (5) | **CNG Used** | `kg` | `0` | — *(None)* | `setio` (`{"id": 45900, ...}`) |
| 67 | **`45910`** | `45910..45914` (5) | **CNG Level** | `%` | `0` | — *(None)* | `setio` (`{"id": 45910, ...}`) |
| 68 | **`45920`** | `45920..45924` (5) | **Oil Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 45920, ...}`) |
| 69 | **`45930`** | `45930..45934` (3) | **Fault Codes** | `—` | `0` | — *(None)* | `setio` (`{"id": 45930, ...}`) |
| 70 | **`45940`** | `45940..45944` (5) | **Vehicles Range On Battery** | `m` | `0` | — *(None)* | `setio` (`{"id": 45940, ...}`) |
| 71 | **`45950`** | `45950..45954` (5) | **Vehicles Range On Additional Fuel** | `m` | `0` | — *(None)* | `setio` (`{"id": 45950, ...}`) |
| 72 | **`45960`** | `45960..45964` (3) | **VIN** | `—` | `0` | — *(None)* | `setio` (`{"id": 45960, ...}`) |
| 73 | **`45970`** | `45970..45974` (5) | **LVC CNG Level Kg** | `kg×10` | `0` | — *(None)* | `setio` (`{"id": 45970, ...}`) |
| 74 | **`46000`** | `46000..46004` (3) | **Brake switch** | `—` | `1` | — *(None)* | `setio` (`{"id": 46000, ...}`) |
| 75 | **`46010`** | `46010..46014` (5) | **Wheel based speed** | `km/h` | `1` | — *(None)* | `setio` (`{"id": 46010, ...}`) |
| 76 | **`46020`** | `46020..46024` (3) | **Distance to next service** | `km` | `1` | — *(None)* | `setio` (`{"id": 46020, ...}`) |
| 77 | **`46030`** | `46030..46034` (3) | **Security state flags P4** | `—` | `1` | — *(None)* | `setio` (`{"id": 46030, ...}`) |
| 78 | **`46040`** | `46040..46044` (3) | **Control state flags P4** | `—` | `1` | — *(None)* | `setio` (`{"id": 46040, ...}`) |
| 79 | **`46050`** | `46050..46054` (5) | **Indicators state flags P4** | `—` | `1` | — *(None)* | `setio` (`{"id": 46050, ...}`) |
| 80 | **`46060`** | `46060..46064` (5) | **Agricultural state flags P4** | `—` | `1` | — *(None)* | `setio` (`{"id": 46060, ...}`) |
| 81 | **`46070`** | `46070..46074` (5) | **Utility state flags P4** | `—` | `1` | — *(None)* | `setio` (`{"id": 46070, ...}`) |
| 82 | **`46080`** | `46080..46084` (5) | **Cistern state flags P4** | `—` | `1` | — *(None)* | `setio` (`{"id": 46080, ...}`) |
| 83 | **`46090`** | `46090..46094` (5) | **Total LNG Used** | `kg` | `1` | — *(None)* | `setio` (`{"id": 46090, ...}`) |
| 84 | **`46100`** | `46100..46104` (5) | **Total LNG Used (counted)** | `kg` | `0` | — *(None)* | `setio` (`{"id": 46100, ...}`) |
| 85 | **`46110`** | `46110..46114` (5) | **Total LNG Level** | `%` | `0` | — *(None)* | `setio` (`{"id": 46110, ...}`) |
| 86 | **`46120`** | `46120..46124` (5) | **Total LNG Level** | `kg` | `0` | — *(None)* | `setio` (`{"id": 46120, ...}`) |
| 87 | **`46130`** | `46130..46134` (5) | **Distance from need of service** | `km` | `0` | — *(None)* | `setio` (`{"id": 46130, ...}`) |
| 88 | **`46140`** | `46140..46144` (5) | **Distance from last service** | `km` | `0` | — *(None)* | `setio` (`{"id": 46140, ...}`) |
| 89 | **`46150`** | `46150..46154` (5) | **Time to next service** | `days` | `0` | — *(None)* | `setio` (`{"id": 46150, ...}`) |
| 90 | **`46160`** | `46160..46164` (5) | **Time from need of service** | `days` | `0` | — *(None)* | `setio` (`{"id": 46160, ...}`) |
| 91 | **`46170`** | `46170..46174` (5) | **Time from last serivce** | `days` | `0` | — *(None)* | `setio` (`{"id": 46170, ...}`) |
| 92 | **`46180`** | `46180..46184` (5) | **Distance to next oil service** | `km` | `0` | — *(None)* | `setio` (`{"id": 46180, ...}`) |
| 93 | **`46190`** | `46190..46194` (5) | **Time to next oil service** | `days` | `0` | — *(None)* | `setio` (`{"id": 46190, ...}`) |
| 94 | **`46200`** | `46200..46204` (5) | **Vehicles Range** | `km` | `0` | — *(None)* | `setio` (`{"id": 46200, ...}`) |
| 95 | **`46210`** | `46210..46214` (5) | **SSF Key In Ignition Lock** | `—` | `0` | — *(None)* | `setio` (`{"id": 46210, ...}`) |
| 96 | **`46220`** | `46220..46224` (5) | **SSF Handbrake Is Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 46220, ...}`) |
| 97 | **`46230`** | `46230..46234` (5) | **SSF Front Left Door Opened** | `—` | `0` | — *(None)* | `setio` (`{"id": 46230, ...}`) |
| 98 | **`46240`** | `46240..46244` (5) | **SSF Front Right Door Opened** | `—` | `0` | — *(None)* | `setio` (`{"id": 46240, ...}`) |
| 99 | **`46250`** | `46250..46254` (5) | **SSF Rear Left Door Opened** | `—` | `1` | — *(None)* | `setio` (`{"id": 46250, ...}`) |
| 100 | **`46270`** | `46270..46274` (3) | **SSF Trunk Door Opened** | `—` | `0` | — *(None)* | `setio` (`{"id": 46270, ...}`) |
| 101 | **`46280`** | `46280..46284` (3) | **SSF Neutral Gear Is Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 46280, ...}`) |
| 102 | **`46290`** | `46290..46294` (3) | **SSF Parking Gear Is Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 46290, ...}`) |
| 103 | **`46310`** | `46310..46314` (5) | **SSF Car Is Closed** | `—` | `1` | — *(None)* | `setio` (`{"id": 46310, ...}`) |
| 104 | **`46400`** | `46400..46404` (3) | **Direction indicator** | `—` | `0` | — *(None)* | `setio` (`{"id": 46400, ...}`) |
| 105 | **`46410`** | `46410..46414` (3) | **Tachograph performance** | `—` | `0` | — *(None)* | `setio` (`{"id": 46410, ...}`) |
| 106 | **`46420`** | `46420..46424` (3) | **Handling information** | `—` | `0` | — *(None)* | `setio` (`{"id": 46420, ...}`) |
| 107 | **`46430`** | `46430..46434` (3) | **System event** | `—` | `0` | — *(None)* | `setio` (`{"id": 46430, ...}`) |
| 108 | **`46450`** | `46450..46454` (5) | **Engine coolant temperature** | `℃` | `1` | — *(None)* | `setio` (`{"id": 46450, ...}`) |
| 109 | **`46460`** | `46460..46464` (5) | **Ambient air temperature** | `℃` | `1` | — *(None)* | `setio` (`{"id": 46460, ...}`) |
| 110 | **`46490`** | `46490..46494` (5) | **Fuel rate** | `liters/h` | `1` | — *(None)* | `setio` (`{"id": 46490, ...}`) |
| 111 | **`46500`** | `46500..46504` (5) | **Instantaneous fuel economy** | `km/liter` | `1` | — *(None)* | `setio` (`{"id": 46500, ...}`) |
| 112 | **`46510`** | `46510..46514` (3) | **PTO Drive Engagement** | `—` | `1` | — *(None)* | `setio` (`{"id": 46510, ...}`) |
| 113 | **`46520`** | `46520..46524` (5) | **High resolution engine total fuel used** | `liter` | `1` | — *(None)* | `setio` (`{"id": 46520, ...}`) |
| 114 | **`46530`** | `46530..46534` (5) | **Combined vehicle weight** | `kg` | `1` | — *(None)* | `setio` (`{"id": 46530, ...}`) |
| 115 | **`46540`** | `46540..46544` (5) | **Brake pedal position** | `%` | `1` | — *(None)* | `setio` (`{"id": 46540, ...}`) |
| 116 | **`46550`** | `46550..46554` (3) | **AdBlue Status** | `—` | `1` | — *(None)* | `setio` (`{"id": 46550, ...}`) |
| 117 | **`46560`** | `46560..46564` (5) | **Fuel Level 2** | `%` | `1` | — *(None)* | `setio` (`{"id": 46560, ...}`) |
| 118 | **`46570`** | `46570..46574` (3) | **Engine MIL Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 46570, ...}`) |
| 119 | **`46580`** | `46580..46584` (3) | **Tell Tale ID0** | `—` | `1` | — *(None)* | `setio` (`{"id": 46580, ...}`) |
| 120 | **`46590`** | `46590..46594` (3) | **Tell Tale ID1** | `—` | `1` | — *(None)* | `setio` (`{"id": 46590, ...}`) |
| 121 | **`46600`** | `46600..46604` (3) | **Tell Tale ID2** | `—` | `1` | — *(None)* | `setio` (`{"id": 46600, ...}`) |
| 122 | **`46610`** | `46610..46614` (3) | **Tell Tale ID3** | `—` | `1` | — *(None)* | `setio` (`{"id": 46610, ...}`) |
| 123 | **`46790`** | `46790..46794` (5) | **SSF Battery Charging** | `—` | `0` | — *(None)* | `setio` (`{"id": 46790, ...}`) |
| 124 | **`46800`** | `46800..46804` (3) | **SSF Electric Engine State** | `—` | `0` | — *(None)* | `setio` (`{"id": 46800, ...}`) |
| 125 | **`46810`** | `46810..46814` (5) | **SSF Car Closed Factory Remote** | `—` | `1` | — *(None)* | `setio` (`{"id": 46810, ...}`) |
| 126 | **`46860`** | `46860..46864` (3) | **SSF Rearming Signal** | `—` | `0` | — *(None)* | `setio` (`{"id": 46860, ...}`) |
| 127 | **`46870`** | `46870..46874` (3) | **SSF Trunk Door Opened Factory Remote** | `—` | `0` | — *(None)* | `setio` (`{"id": 46870, ...}`) |
| 128 | **`46880`** | `46880..46884` (5) | **SSF CAN Module In Sleep** | `—` | `0` | — *(None)* | `setio` (`{"id": 46880, ...}`) |
| 129 | **`46890`** | `46890..46894` (5) | **SSF Factory Remote 3x** | `—` | `0` | — *(None)* | `setio` (`{"id": 46890, ...}`) |
| 130 | **`46900`** | `46900..46904` (5) | **SSF Factory Armed** | `—` | `0` | — *(None)* | `setio` (`{"id": 46900, ...}`) |
| 131 | **`46910`** | `46910..46914` (5) | **SSF Drive Is Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 46910, ...}`) |
| 132 | **`46920`** | `46920..46924` (3) | **CSF Parking Lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 46920, ...}`) |
| 133 | **`46930`** | `46930..46934` (3) | **CSF Dipped Headlights** | `—` | `0` | — *(None)* | `setio` (`{"id": 46930, ...}`) |
| 134 | **`46940`** | `46940..46944` (5) | **CSF Full Beam Headlights** | `—` | `0` | — *(None)* | `setio` (`{"id": 46940, ...}`) |
| 135 | **`46950`** | `46950..46954` (5) | **CSF Rear Fog Lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 46950, ...}`) |
| 136 | **`46960`** | `46960..46964` (5) | **CSF Front Fog Lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 46960, ...}`) |
| 137 | **`47000`** | `47000..47004` (5) | **CSF Air Conditioning** | `—` | `2` | — *(None)* | `setio` (`{"id": 47000, ...}`) |
| 138 | **`47010`** | `47010..47014` (5) | **CSF Cruise Control** | `—` | `2` | — *(None)* | `setio` (`{"id": 47010, ...}`) |
| 139 | **`47020`** | `47020..47024` (5) | **CSF Automatic Retarder** | `—` | `2` | — *(None)* | `setio` (`{"id": 47020, ...}`) |
| 140 | **`47030`** | `47030..47034` (5) | **CSF Manual Retarder** | `—` | `2` | — *(None)* | `setio` (`{"id": 47030, ...}`) |
| 141 | **`47040`** | `47040..47044` (5) | **CSF Drivers Seatbelt Fastened** | `—` | `2` | — *(None)* | `setio` (`{"id": 47040, ...}`) |
| 142 | **`47050`** | `47050..47054` (5) | **CSF Front Passengers Seatbelt Fastened** | `—` | `2` | — *(None)* | `setio` (`{"id": 47050, ...}`) |
| 143 | **`47060`** | `47060..47064` (5) | **CSF Rear Left Passengers Seatbelt Fastened** | `—` | `2` | — *(None)* | `setio` (`{"id": 47060, ...}`) |
| 144 | **`47070`** | `47070..47074` (5) | **CSF Rear Right Passengers Seatbelt Fastened** | `—` | `2` | — *(None)* | `setio` (`{"id": 47070, ...}`) |
| 145 | **`47080`** | `47080..47084` (5) | **CSF Rear Centre Passengers Seatbelt Fastened** | `—` | `2` | — *(None)* | `setio` (`{"id": 47080, ...}`) |
| 146 | **`47090`** | `47090..47094` (5) | **CSF Front Passenger Present** | `—` | `2` | — *(None)* | `setio` (`{"id": 47090, ...}`) |
| 147 | **`47200`** | `47200..47204` (5) | **ISF ESP Turned Off** | `—` | `2` | — *(None)* | `setio` (`{"id": 47200, ...}`) |
| 148 | **`47210`** | `47210..47214` (5) | **ISF STOP Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47210, ...}`) |
| 149 | **`47220`** | `47220..47224` (5) | **ISF Oil Level Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47220, ...}`) |
| 150 | **`47230`** | `47230..47234` (5) | **ISF Coolant Liquid Level** | `—` | `2` | — *(None)* | `setio` (`{"id": 47230, ...}`) |
| 151 | **`47240`** | `47240..47244` (5) | **ISF Battery Not Charging Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47240, ...}`) |
| 152 | **`47250`** | `47250..47254` (5) | **ISF Handbrake System Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47250, ...}`) |
| 153 | **`47260`** | `47260..47264` (5) | **ISF AIRBAG Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47260, ...}`) |
| 154 | **`47270`** | `47270..47274` (5) | **ISF EPS Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47270, ...}`) |
| 155 | **`47280`** | `47280..47284` (5) | **ISF Warning Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47280, ...}`) |
| 156 | **`47290`** | `47290..47294` (5) | **ISF Lights Failure Indicator** | `—` | `2` | — *(None)* | `setio` (`{"id": 47290, ...}`) |
| 157 | **`47500`** | `47500..47504` (3) | **ISF Low Washer Fluid Level Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47500, ...}`) |
| 158 | **`47510`** | `47510..47514` (3) | **ISF Low AdBlue Level Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47510, ...}`) |
| 159 | **`47520`** | `47520..47524` (3) | **ISF Low Trailer Tyre Pressure Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47520, ...}`) |
| 160 | **`47530`** | `47530..47534` (5) | **ISF Wear Of Trailer Brake Lining Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47530, ...}`) |
| 161 | **`47540`** | `47540..47544` (3) | **ISF High Trailer Brake Temperature Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47540, ...}`) |
| 162 | **`47550`** | `47550..47554` (3) | **ISF Incorrect Trailer Pneumatic Supply Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47550, ...}`) |
| 163 | **`47560`** | `47560..47564` (3) | **ISF Low CNG Level Indicator** | `—` | `1` | — *(None)* | `setio` (`{"id": 47560, ...}`) |
| 164 | **`47570`** | `47570..47574` (3) | **ASF Right Joystick Moved Right Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47570, ...}`) |
| 165 | **`47580`** | `47580..47584` (3) | **ASF Right Joystick Moved Left Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47580, ...}`) |
| 166 | **`47590`** | `47590..47594` (3) | **ASF Right Joystick Moved Forward Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47590, ...}`) |
| 167 | **`47600`** | `47600..47604` (3) | **ASF Right Joystick Moved Back Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47600, ...}`) |
| 168 | **`47610`** | `47610..47614` (3) | **ASF Left Joystick Moved Right Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 47610, ...}`) |
| 169 | **`47620`** | `47620..47624` (3) | **ASF Left Joystick Moved Left Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47620, ...}`) |
| 170 | **`47630`** | `47630..47634` (3) | **ASF Left Joystick Moved Forward Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47630, ...}`) |
| 171 | **`47640`** | `47640..47644` (3) | **ASF Left Joystick Moved Back Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47640, ...}`) |
| 172 | **`47650`** | `47650..47654` (3) | **ASF First Rear Hydraulic** | `—` | `0` | — *(None)* | `setio` (`{"id": 47650, ...}`) |
| 173 | **`47660`** | `47660..47664` (3) | **ASF Second Rear Hydraulic** | `—` | `0` | — *(None)* | `setio` (`{"id": 47660, ...}`) |
| 174 | **`47670`** | `47670..47674` (3) | **ASF Third Rear Hydraulic** | `—` | `0` | — *(None)* | `setio` (`{"id": 47670, ...}`) |
| 175 | **`47680`** | `47680..47684` (3) | **ASF Fourth Rear Hydraulic** | `—` | `1` | — *(None)* | `setio` (`{"id": 47680, ...}`) |
| 176 | **`47690`** | `47690..47694` (3) | **ASF First Front Hydraulic** | `—` | `0` | — *(None)* | `setio` (`{"id": 47690, ...}`) |
| 177 | **`47700`** | `47700..47704` (3) | **ASF Second Front Hydraulic** | `—` | `1` | — *(None)* | `setio` (`{"id": 47700, ...}`) |
| 178 | **`47710`** | `47710..47714` (3) | **ASF Third Front Hydraulic** | `—` | `0` | — *(None)* | `setio` (`{"id": 47710, ...}`) |
| 179 | **`47720`** | `47720..47724` (3) | **ASF Fourth Front Hydraulic** | `—` | `1` | — *(None)* | `setio` (`{"id": 47720, ...}`) |
| 180 | **`47730`** | `47730..47734` (3) | **ASF Front Three-point Hitch** | `—` | `0` | — *(None)* | `setio` (`{"id": 47730, ...}`) |
| 181 | **`47740`** | `47740..47744` (3) | **ASF Rear Three-point Hitch** | `—` | `1` | — *(None)* | `setio` (`{"id": 47740, ...}`) |
| 182 | **`47750`** | `47750..47754` (3) | **ASF Front Power Take-off** | `—` | `0` | — *(None)* | `setio` (`{"id": 47750, ...}`) |
| 183 | **`47770`** | `47770..47774` (3) | **ASF Mowing Active** | `—` | `1` | — *(None)* | `setio` (`{"id": 47770, ...}`) |
| 184 | **`47780`** | `47780..47784` (3) | **ASF Threshing Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 47780, ...}`) |
| 185 | **`47790`** | `47790..47794` (3) | **ASF Grain Release From Hopper** | `—` | `0` | — *(None)* | `setio` (`{"id": 47790, ...}`) |
| 186 | **`47800`** | `47800..47804` (3) | **ASF Grain Tank Is 100% Full** | `—` | `1` | — *(None)* | `setio` (`{"id": 47800, ...}`) |
| 187 | **`47810`** | `47810..47814` (3) | **ASF Grain Tank Is 70% Full** | `—` | `0` | — *(None)* | `setio` (`{"id": 47810, ...}`) |
| 188 | **`47820`** | `47820..47824` (3) | **ASF Grain Tank Is Opened** | `—` | `0` | — *(None)* | `setio` (`{"id": 47820, ...}`) |
| 189 | **`47830`** | `47830..47834` (3) | **ASF Unloader Drive** | `—` | `0` | — *(None)* | `setio` (`{"id": 47830, ...}`) |
| 190 | **`47840`** | `47840..47844` (3) | **ASF Cleaning Fan Control Turned Off** | `—` | `1` | — *(None)* | `setio` (`{"id": 47840, ...}`) |
| 191 | **`47850`** | `47850..47854` (3) | **ASF Threshing Drum Control Turned Off** | `—` | `1` | — *(None)* | `setio` (`{"id": 47850, ...}`) |
| 192 | **`47860`** | `47860..47864` (3) | **ASF Straw Walker Is Clogged** | `—` | `1` | — *(None)* | `setio` (`{"id": 47860, ...}`) |
| 193 | **`47870`** | `47870..47874` (3) | **ASF Excessive Clearance Under The Threshing Drum** | `—` | `0` | — *(None)* | `setio` (`{"id": 47870, ...}`) |
| 194 | **`47880`** | `47880..47884` (3) | **ASF Low Temperature Of Drive System Hydraulics Less Than 5 Grades** | `—` | `0` | — *(None)* | `setio` (`{"id": 47880, ...}`) |
| 195 | **`47890`** | `47890..47894` (3) | **ASF High Temperature Of Drive System Hydraulics Greater Than 86 Grades** | `—` | `0` | — *(None)* | `setio` (`{"id": 47890, ...}`) |
| 196 | **`47900`** | `47900..47904` (3) | **ASF Ear Auger Speed Below The Norm** | `—` | `0` | — *(None)* | `setio` (`{"id": 47900, ...}`) |
| 197 | **`47910`** | `47910..47914` (3) | **ASF Grain Auger Speed Below The Norm** | `—` | `1` | — *(None)* | `setio` (`{"id": 47910, ...}`) |
| 198 | **`47920`** | `47920..47924` (3) | **ASF Straw Chooper Speed Below The Norm** | `—` | `1` | — *(None)* | `setio` (`{"id": 47920, ...}`) |
| 199 | **`47930`** | `47930..47934` (3) | **ASF Straw Shaker Speed Below The Norm** | `—` | `0` | — *(None)* | `setio` (`{"id": 47930, ...}`) |
| 200 | **`47940`** | `47940..47944` (3) | **ASF Feeder Speed Below The Norm** | `—` | `0` | — *(None)* | `setio` (`{"id": 47940, ...}`) |
| 201 | **`47950`** | `47950..47954` (3) | **ASF Straw Chopper Switched On** | `—` | `1` | — *(None)* | `setio` (`{"id": 47950, ...}`) |
| 202 | **`47960`** | `47960..47964` (3) | **ASF Corn Header Connected** | `—` | `1` | — *(None)* | `setio` (`{"id": 47960, ...}`) |
| 203 | **`47970`** | `47970..47974` (3) | **ASF Grain Header Connected** | `—` | `1` | — *(None)* | `setio` (`{"id": 47970, ...}`) |
| 204 | **`47980`** | `47980..47984` (3) | **ASF Feeder Reverse Switched On** | `—` | `1` | — *(None)* | `setio` (`{"id": 47980, ...}`) |
| 205 | **`47990`** | `47990..47994` (3) | **ASF The Pressure Filter Of The Hydraulic Pump Is Clogged** | `—` | `0` | — *(None)* | `setio` (`{"id": 47990, ...}`) |
| 206 | **`48000`** | `48000..48004` (3) | **USF Spreading** | `—` | `0` | — *(None)* | `setio` (`{"id": 48000, ...}`) |
| 207 | **`48010`** | `48010..48014` (3) | **USF Pouring Chemicals** | `—` | `0` | — *(None)* | `setio` (`{"id": 48010, ...}`) |
| 208 | **`48020`** | `48020..48024` (3) | **USF Conveyor Belt** | `—` | `0` | — *(None)* | `setio` (`{"id": 48020, ...}`) |
| 209 | **`48030`** | `48030..48034` (3) | **USF Salt Spreaders Drive Wheel** | `—` | `0` | — *(None)* | `setio` (`{"id": 48030, ...}`) |
| 210 | **`48040`** | `48040..48044` (3) | **USF Brushes** | `—` | `0` | — *(None)* | `setio` (`{"id": 48040, ...}`) |
| 211 | **`48050`** | `48050..48054` (3) | **USF Vacuum Cleaner** | `—` | `0` | — *(None)* | `setio` (`{"id": 48050, ...}`) |
| 212 | **`48060`** | `48060..48064` (3) | **USF Water Supply** | `—` | `0` | — *(None)* | `setio` (`{"id": 48060, ...}`) |
| 213 | **`48070`** | `48070..48074` (3) | **USF High Pressure Washer** | `—` | `0` | — *(None)* | `setio` (`{"id": 48070, ...}`) |
| 214 | **`48080`** | `48080..48084` (3) | **USF Liquid Pump** | `—` | `0` | — *(None)* | `setio` (`{"id": 48080, ...}`) |
| 215 | **`48200`** | `48200..48204` (5) | **CiSF Section 2 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48200, ...}`) |
| 216 | **`48210`** | `48210..48214` (5) | **CiSF Section 2 Filled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48210, ...}`) |
| 217 | **`48220`** | `48220..48224` (5) | **CiSF Section 2 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48220, ...}`) |
| 218 | **`48230`** | `48230..48234` (5) | **CiSF Section 3 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48230, ...}`) |
| 219 | **`48240`** | `48240..48244` (5) | **CiSF Section 3 Filled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48240, ...}`) |
| 220 | **`48250`** | `48250..48254` (5) | **CiSF Section 3 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48250, ...}`) |
| 221 | **`48260`** | `48260..48264` (5) | **CiSF Section 4 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48260, ...}`) |
| 222 | **`48270`** | `48270..48274` (5) | **CiSF Section 4 Filled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48270, ...}`) |
| 223 | **`48280`** | `48280..48284` (5) | **CiSF Section 4 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48280, ...}`) |
| 224 | **`48290`** | `48290..48294` (5) | **CiSF Section 5 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48290, ...}`) |
| 225 | **`48300`** | `48300..48304` (5) | **CiSF Section 5 Filled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48300, ...}`) |
| 226 | **`48310`** | `48310..48314` (5) | **CiSF Section 5 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48310, ...}`) |
| 227 | **`48320`** | `48320..48324` (5) | **CiSF Section 6 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48320, ...}`) |
| 228 | **`48340`** | `48340..48344` (5) | **CiSF Section 6 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48340, ...}`) |
| 229 | **`48350`** | `48350..48354` (5) | **CiSF Section 7 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48350, ...}`) |
| 230 | **`48360`** | `48360..48364` (5) | **CiSF Section 7 Filled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48360, ...}`) |
| 231 | **`48370`** | `48370..48374` (5) | **CiSF Section 7 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48370, ...}`) |
| 232 | **`48380`** | `48380..48384` (5) | **CiSF Section 8 Presence Of Fluid In The Downpipe** | `—` | `0` | — *(None)* | `setio` (`{"id": 48380, ...}`) |
| 233 | **`48390`** | `48390..48394` (5) | **CiSF Section 8 Filled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48390, ...}`) |
| 234 | **`48400`** | `48400..48404` (5) | **CiSF Section 8 Overfilled** | `—` | `0` | — *(None)* | `setio` (`{"id": 48400, ...}`) |
| 235 | **`48410`** | `48410..48414` (5) | **Total Bale Count** | `—` | `0` | — *(None)* | `setio` (`{"id": 48410, ...}`) |
| 236 | **`48420`** | `48420..48424` (5) | **Bale Count** | `—` | `0` | — *(None)* | `setio` (`{"id": 48420, ...}`) |
| 237 | **`48430`** | `48430..48434` (5) | **Cut Bale Count** | `—` | `0` | — *(None)* | `setio` (`{"id": 48430, ...}`) |
| 238 | **`48440`** | `48440..48444` (5) | **Bale Slices** | `—` | `0` | — *(None)* | `setio` (`{"id": 48440, ...}`) |
| 239 | **`48450`** | `48450..48454` (5) | **SSF Engine Working On Dual Fuel** | `—` | `0` | — *(None)* | `setio` (`{"id": 48450, ...}`) |
| 240 | **`48460`** | `48460..48464` (5) | **SSF Engine Working On LPG** | `—` | `0` | — *(None)* | `setio` (`{"id": 48460, ...}`) |
| 241 | **`48470`** | `48470..48474` (5) | **CSF Trailer Connected** | `—` | `0` | — *(None)* | `setio` (`{"id": 48470, ...}`) |
| 242 | **`48480`** | `48480..48484` (5) | **CSF Start Stop System Inactive** | `—` | `0` | — *(None)* | `setio` (`{"id": 48480, ...}`) |
| 243 | **`48490`** | `48490..48494` (5) | **ASF Adapter Pressure Filter Sensor** | `—` | `0` | — *(None)* | `setio` (`{"id": 48490, ...}`) |
| 244 | **`48500`** | `48500..48504` (5) | **ASF Service 2 Required Indicator** | `—` | `0` | — *(None)* | `setio` (`{"id": 48500, ...}`) |
| 245 | **`48510`** | `48510..48514` (5) | **ASF Drain Filter Clogged Indicator** | `—` | `0` | — *(None)* | `setio` (`{"id": 48510, ...}`) |
| 246 | **`48520`** | `48520..48524` (5) | **ASF Section 1 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48520, ...}`) |
| 247 | **`48530`** | `48530..48534` (5) | **ASF Section 2 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48530, ...}`) |
| 248 | **`48540`** | `48540..48544` (5) | **ASF Section 3 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48540, ...}`) |
| 249 | **`48550`** | `48550..48554` (5) | **ASF Section 4 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48550, ...}`) |
| 250 | **`48570`** | `48570..48574` (5) | **ASF Section 6 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48570, ...}`) |
| 251 | **`48590`** | `48590..48594` (5) | **ASF Section 8 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48590, ...}`) |
| 252 | **`48600`** | `48600..48604` (5) | **ASF Section 9 Spraying** | `—` | `0` | — *(None)* | `setio` (`{"id": 48600, ...}`) |
| 253 | **`48610`** | `48610..48614` (5) | **USF Hydraulics Work Not Permitted** | `—` | `0` | — *(None)* | `setio` (`{"id": 48610, ...}`) |
| 254 | **`48620`** | `48620..48624` (5) | **Total LPG Used** | `ltr` | `0` | — *(None)* | `setio` (`{"id": 48620, ...}`) |
| 255 | **`48630`** | `48630..48634` (5) | **Total LPG Used (counted)** | `ltr` | `0` | — *(None)* | `setio` (`{"id": 48630, ...}`) |
| 256 | **`48640`** | `48640..48644` (5) | **Total LPG Level** | `%` | `0` | — *(None)* | `setio` (`{"id": 48640, ...}`) |
| 257 | **`48650`** | `48650..48654` (5) | **Total LPG Level** | `ltr` | `0` | — *(None)* | `setio` (`{"id": 48650, ...}`) |
| 258 | **`48660`** | `48660..48664` (5) | **Maintenance4 Hours** | `Hours` | `0` | — *(None)* | `setio` (`{"id": 48660, ...}`) |
| 259 | **`48670`** | `48670..48674` (5) | **Maintenance5 Hours** | `Hours` | `0` | — *(None)* | `setio` (`{"id": 48670, ...}`) |
| 260 | **`48680`** | `48680..48684` (5) | **Remaining work time on HV battery** | `min` | `0` | — *(None)* | `setio` (`{"id": 48680, ...}`) |
| 261 | **`48690`** | `48690..48694` (3) | **Error Codes** | `—` | `0` | — *(None)* | `setio` (`{"id": 48690, ...}`) |
| 262 | **`48700`** | `48700..48704` (5) | **Digital sensor 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 48700, ...}`) |
| 263 | **`48710`** | `48710..48714` (5) | **Digital sensor 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 48710, ...}`) |
| 264 | **`48720`** | `48720..48724` (5) | **Digital sensor 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 48720, ...}`) |
| 265 | **`48730`** | `48730..48734` (5) | **Max road speed** | `km/h` | `0` | — *(None)* | `setio` (`{"id": 48730, ...}`) |
| 266 | **`48740`** | `48740..48744` (5) | **Exceeded road speed** | `km/h` | `0` | — *(None)* | `setio` (`{"id": 48740, ...}`) |
| 267 | **`48750`** | `48750..48754` (5) | **Analog sensor 2** | `mV` | `0` | — *(None)* | `setio` (`{"id": 48750, ...}`) |
| 268 | **`48760`** | `48760..48764` (5) | **Analog sensor 3** | `mV` | `0` | — *(None)* | `setio` (`{"id": 48760, ...}`) |
| 269 | **`48770`** | `48770..48774` (5) | **Temperature Probe 1** | `*10 °C` | `0` | — *(None)* | `setio` (`{"id": 48770, ...}`) |
| 270 | **`48780`** | `48780..48784` (5) | **Engine oil pressure** | `bar×10` | `0` | — *(None)* | `setio` (`{"id": 48780, ...}`) |
| 271 | **`48790`** | `48790..48794` (5) | **Engine oil level** | `%` | `0` | — *(None)* | `setio` (`{"id": 48790, ...}`) |
| 272 | **`48800`** | `48800..48804` (5) | **RSF Speed Limit Sign** | `—` | `0` | — *(None)* | `setio` (`{"id": 48800, ...}`) |
| 273 | **`48810`** | `48810..48814` (5) | **RSF End Of Speed Limit Sign** | `—` | `0` | — *(None)* | `setio` (`{"id": 48810, ...}`) |
| 274 | **`48820`** | `48820..48824` (5) | **RSF Speed Exceeded** | `—` | `0` | — *(None)* | `setio` (`{"id": 48820, ...}`) |
| 275 | **`48830`** | `48830..48834` (5) | **RSF Time Speed Limit Sign** | `—` | `0` | — *(None)* | `setio` (`{"id": 48830, ...}`) |
| 276 | **`48840`** | `48840..48844` (5) | **RSF Weather Speed Limit Sign** | `—` | `0` | — *(None)* | `setio` (`{"id": 48840, ...}`) |
| 277 | **`48850`** | `48850..48854` (5) | **Temperature 3** | `*10 °C` | `0` | — *(None)* | `setio` (`{"id": 48850, ...}`) |
| 278 | **`48860`** | `48860..48864` (5) | **Temperature 4** | `*10 °C` | `0` | — *(None)* | `setio` (`{"id": 48860, ...}`) |
| 279 | **`48870`** | `48870..48874` (5) | **Status 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 48870, ...}`) |
| 280 | **`48880`** | `48880..48884` (5) | **Status 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 48880, ...}`) |
| 281 | **`48890`** | `48890..48894` (5) | **Water level for fire fighting** | `%×10` | `0` | — *(None)* | `setio` (`{"id": 48890, ...}`) |
| 282 | **`48900`** | `48900..48904` (5) | **Foam level for fire fighting** | `%×10` | `0` | — *(None)* | `setio` (`{"id": 48900, ...}`) |
| 283 | **`48910`** | `48910..48914` (5) | **Pump pressure for fire fighting** | `bar×10` | `0` | — *(None)* | `setio` (`{"id": 48910, ...}`) |
| 284 | **`48920`** | `48920..48924` (5) | **Wind speed** | `m/s` | `0` | — *(None)* | `setio` (`{"id": 48920, ...}`) |
| 285 | **`48930`** | `48930..48934` (5) | **Temperature outside** | `°C` | `0` | — *(None)* | `setio` (`{"id": 48930, ...}`) |
| 286 | **`48940`** | `48940..48944` (5) | **Gross vehicle combination weight** | `kg` | `0` | — *(None)* | `setio` (`{"id": 48940, ...}`) |
| 287 | **`48950`** | `48950..48954` (5) | **Drive system temperature** | `°C` | `0` | — *(None)* | `setio` (`{"id": 48950, ...}`) |
| 288 | **`48960`** | `48960..48964` (5) | **Rotation speed of auger conveyor** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 48960, ...}`) |
| 289 | **`48970`** | `48970..48974` (5) | **Rotation speed grain auger** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 48970, ...}`) |
| 290 | **`48980`** | `48980..48984` (5) | **Rotation speed of chopper** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 48980, ...}`) |
| 291 | **`48990`** | `48990..48994` (5) | **Rotation speed of straw shaker** | `rpm` | `0` | — *(None)* | `setio` (`{"id": 48990, ...}`) |
| 292 | **`49000`** | `49000..49004` (5) | **Input 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 49000, ...}`) |
| 293 | **`49010`** | `49010..49014` (5) | **Setpoint 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 49010, ...}`) |
| 294 | **`49020`** | `49020..49024` (5) | **Setpoint 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 49020, ...}`) |
| 295 | **`49030`** | `49030..49034` (5) | **Setpoint 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 49030, ...}`) |
| 296 | **`49040`** | `49040..49044` (5) | **Temperature 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 49040, ...}`) |
| 297 | **`49050`** | `49050..49054` (5) | **Temperature 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 49050, ...}`) |
| 298 | **`49060`** | `49060..49064` (5) | **Temperature 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 49060, ...}`) |
| 299 | **`49070`** | `49070..49074` (5) | **Temperature 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 49070, ...}`) |
| 300 | **`49080`** | `49080..49084` (5) | **Humidity** | `—` | `0` | — *(None)* | `setio` (`{"id": 49080, ...}`) |
| 301 | **`49090`** | `49090..49094` (5) | **Status 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 49090, ...}`) |
| 302 | **`49100`** | `49100..49104` (5) | **Status 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 49100, ...}`) |
| 303 | **`49110`** | `49110..49114` (5) | **Status 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 49110, ...}`) |
| 304 | **`49120`** | `49120..49124` (5) | **Status 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 49120, ...}`) |
| 305 | **`49130`** | `49130..49134` (5) | **Alarm 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 49130, ...}`) |
| 306 | **`49140`** | `49140..49144` (5) | **Alarm 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 49140, ...}`) |
| 307 | **`49150`** | `49150..49154` (5) | **Alarm 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 49150, ...}`) |
| 308 | **`49160`** | `49160..49164` (5) | **Alarm 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 49160, ...}`) |
| 309 | **`50000`** | `50000..50005` (6) | **Ignition** | `—` | `1` | — *(None)* | `setio` (`{"id": 50000, ...}`) |
| 310 | **`50010`** | `50010..50015` (6) | **Movement** | `—` | `1` | — *(None)* | `setio` (`{"id": 50010, ...}`) |
| 311 | **`50020`** | `50020..50024` (5) | **Data Mode** | `—` | `0` | — *(None)* | `setio` (`{"id": 50020, ...}`) |
| 312 | **`50030`** | `50030..50035` (6) | **GSM Signal** | `—` | `1` | — *(None)* | `setio` (`{"id": 50030, ...}`) |
| 313 | **`50040`** | `50040..50044` (5) | **Sleep Mode** | `—` | `0` | — *(None)* | `setio` (`{"id": 50040, ...}`) |
| 314 | **`50050`** | `50050..50054` (5) | **GNSS Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 50050, ...}`) |
| 315 | **`50060`** | `50060..50065` (6) | **GNSS PDOP** | `—` | `1` | — *(None)* | `setio` (`{"id": 50060, ...}`) |
| 316 | **`50070`** | `50070..50075` (6) | **GNSS HDOP** | `—` | `1` | — *(None)* | `setio` (`{"id": 50070, ...}`) |
| 317 | **`50080`** | `50080..50085` (6) | **External Voltage** | `mV` | `1` | `external_voltage_io` | `setio` (`{"id": 50080, ...}`) |
| 318 | **`50090`** | `50090..50095` (6) | **Speed** | `km/h` | `1` | — *(None)* | `setio` (`{"id": 50090, ...}`) |
| 319 | **`50100`** | `50100..50104` (5) | **GSM Cell ID** | `—` | `0` | — *(None)* | `setio` (`{"id": 50100, ...}`) |
| 320 | **`50110`** | `50110..50114` (5) | **GSM Area Code** | `—` | `0` | — *(None)* | `setio` (`{"id": 50110, ...}`) |
| 321 | **`50120`** | `50120..50125` (6) | **Battery Voltage** | `mV` | `1` | `battery_voltage_io` | `setio` (`{"id": 50120, ...}`) |
| 322 | **`50130`** | `50130..50135` (6) | **Battery Current** | `mA` | `1` | — *(None)* | `setio` (`{"id": 50130, ...}`) |
| 323 | **`50140`** | `50140..50144` (5) | **Active GSM Operator** | `—` | `0` | — *(None)* | `setio` (`{"id": 50140, ...}`) |
| 324 | **`50150`** | `50150..50154` (5) | **Trip Odometer** | `m` | `1` | `trip_odometer_io` | `setio` (`{"id": 50150, ...}`) |
| 325 | **`50160`** | `50160..50164` (5) | **Total Odometer** | `m` | `0` | `odometer_io` | `setio` (`{"id": 50160, ...}`) |
| 326 | **`50170`** | `50170..50175` (6) | **Digital Input 1** | `—` | `0` | `inputs1_io` | `setio` (`{"id": 50170, ...}`) |
| 327 | **`50180`** | `50180..50185` (6) | **Analog Input 1** | `mV` | `0` | `analog_input1_io` | `setio` (`{"id": 50180, ...}`) |
| 328 | **`50190`** | `50190..50195` (6) | **Digital Output 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50190, ...}`) |
| 329 | **`50220`** | `50220..50225` (6) | **Axis X** | `mG` | `1` | `axis_x` | `setio` (`{"id": 50220, ...}`) |
| 330 | **`50230`** | `50230..50235` (6) | **Axis Y** | `mG` | `1` | `axis_y` | `setio` (`{"id": 50230, ...}`) |
| 331 | **`50240`** | `50240..50245` (6) | **Axis Z** | `mG` | `1` | `axis_z` | `setio` (`{"id": 50240, ...}`) |
| 332 | **`50250`** | `50250..50254` (3) | **ICCID** | `—` | `0` | — *(None)* | `setio` (`{"id": 50250, ...}`) |
| 333 | **`50260`** | `50260..50264` (5) | **SD Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 50260, ...}`) |
| 334 | **`50270`** | `50270..50275` (6) | **Digital Input 2** | `—` | `0` | `inputs2_io` | `setio` (`{"id": 50270, ...}`) |
| 335 | **`50280`** | `50280..50285` (6) | **Digital Input 3** | `—` | `0` | `inputs3_io` | `setio` (`{"id": 50280, ...}`) |
| 336 | **`50290`** | `50290..50295` (6) | **Analog Input 2** | `mV` | `0` | — *(None)* | `setio` (`{"id": 50290, ...}`) |
| 337 | **`50300`** | `50300..50305` (6) | **Digital Output 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50300, ...}`) |
| 338 | **`50310`** | `50310..50315` (6) | **Dallas Temperature 1** | `℃` | `0` | — *(None)* | `setio` (`{"id": 50310, ...}`) |
| 339 | **`50320`** | `50320..50325` (6) | **Dallas Temperature 2** | `℃` | `0` | — *(None)* | `setio` (`{"id": 50320, ...}`) |
| 340 | **`50330`** | `50330..50335` (6) | **Dallas Temperature 3** | `℃` | `0` | — *(None)* | `setio` (`{"id": 50330, ...}`) |
| 341 | **`50340`** | `50340..50345` (6) | **Dallas Temperature 4** | `℃` | `0` | — *(None)* | `setio` (`{"id": 50340, ...}`) |
| 342 | **`50350`** | `50350..50354` (5) | **Dallas Temperature ID 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50350, ...}`) |
| 343 | **`50360`** | `50360..50364` (5) | **Dallas Temperature ID 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50360, ...}`) |
| 344 | **`50370`** | `50370..50374` (5) | **Dallas Temperature ID 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 50370, ...}`) |
| 345 | **`50380`** | `50380..50384` (5) | **Dallas Temperature ID 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 50380, ...}`) |
| 346 | **`50390`** | `50390..50395` (6) | **iButton** | `—` | `0` | — *(None)* | `setio` (`{"id": 50390, ...}`) |
| 347 | **`50400`** | `50400..50405` (6) | **RFID** | `—` | `0` | — *(None)* | `setio` (`{"id": 50400, ...}`) |
| 348 | **`50410`** | `50410..50415` (6) | **LLS 1 Fuel Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 50410, ...}`) |
| 349 | **`50420`** | `50420..50425` (6) | **LLS 2 Fuel Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 50420, ...}`) |
| 350 | **`50430`** | `50430..50435` (6) | **LLS 3 Fuel Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 50430, ...}`) |
| 351 | **`50440`** | `50440..50445` (6) | **LLS 4 Fuel Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 50440, ...}`) |
| 352 | **`50450`** | `50450..50455` (6) | **LLS 5 Fuel Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 50450, ...}`) |
| 353 | **`50460`** | `50460..50465` (6) | **LLS 1 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 50460, ...}`) |
| 354 | **`50470`** | `50470..50475` (6) | **LLS 2 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 50470, ...}`) |
| 355 | **`50480`** | `50480..50485` (6) | **LLS 3 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 50480, ...}`) |
| 356 | **`50490`** | `50490..50495` (6) | **LLS 4 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 50490, ...}`) |
| 357 | **`50500`** | `50500..50505` (6) | **LLS 5 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 50500, ...}`) |
| 358 | **`50530`** | `50530..50534` (5) | **BLE Temp #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50530, ...}`) |
| 359 | **`50540`** | `50540..50544` (5) | **BLE Temp #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50540, ...}`) |
| 360 | **`50550`** | `50550..50554` (5) | **BLE Temp #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 50550, ...}`) |
| 361 | **`50560`** | `50560..50564` (5) | **BLE Temp #4** | `—` | `0` | — *(None)* | `setio` (`{"id": 50560, ...}`) |
| 362 | **`50570`** | `50570..50574` (5) | **BLE Battery #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50570, ...}`) |
| 363 | **`50580`** | `50580..50584` (5) | **BLE Battery #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50580, ...}`) |
| 364 | **`50590`** | `50590..50594` (5) | **BLE Battery #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 50590, ...}`) |
| 365 | **`50600`** | `50600..50604` (5) | **BLE Battery #4** | `—` | `0` | — *(None)* | `setio` (`{"id": 50600, ...}`) |
| 366 | **`50610`** | `50610..50614` (5) | **BLE Humidity #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50610, ...}`) |
| 367 | **`50620`** | `50620..50624` (5) | **BLE Humidity #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50620, ...}`) |
| 368 | **`50630`** | `50630..50634` (5) | **BLE Humidity #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 50630, ...}`) |
| 369 | **`50640`** | `50640..50644` (5) | **BLE Humidity #4** | `—` | `0` | — *(None)* | `setio` (`{"id": 50640, ...}`) |
| 370 | **`50650`** | `50650..50654` (5) | **Network Type** | `—` | `0` | — *(None)* | `setio` (`{"id": 50650, ...}`) |
| 371 | **`50660`** | `50660..50665` (6) | **Authorized iButton** | `—` | `0` | `inputs4_io` | `setio` (`{"id": 50660, ...}`) |
| 372 | **`50670`** | `50670..50675` (6) | **Pulse Counter DIN1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50670, ...}`) |
| 373 | **`50680`** | `50680..50685` (6) | **Pulse Counter DIN2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50680, ...}`) |
| 374 | **`50690`** | `50690..50695` (6) | **Battery Level** | `%` | `0` | — *(None)* | `setio` (`{"id": 50690, ...}`) |
| 375 | **`50700`** | `50700..50705` (6) | **Digital Output 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 50700, ...}`) |
| 376 | **`50710`** | `50710..50715` (6) | **Digital Input 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 50710, ...}`) |
| 377 | **`50720`** | `50720..50725` (6) | **BT Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 50720, ...}`) |
| 378 | **`50730`** | `50730..50735` (6) | **1Wire Sensor Temperature 6** | `℃` | `0` | — *(None)* | `setio` (`{"id": 50730, ...}`) |
| 379 | **`50740`** | `50740..50744` (5) | **1Wire Sensor Temperature ID 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 50740, ...}`) |
| 380 | **`50750`** | `50750..50754` (5) | **BLE LLS #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50750, ...}`) |
| 381 | **`50760`** | `50760..50764` (5) | **PCB Temperature** | `℃` | `1` | — *(None)* | `setio` (`{"id": 50760, ...}`) |
| 382 | **`50770`** | `50770..50774` (5) | **Fuel Counter** | `—` | `1` | — *(None)* | `setio` (`{"id": 50770, ...}`) |
| 383 | **`50780`** | `50780..50785` (6) | **BLE LLS #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50780, ...}`) |
| 384 | **`50790`** | `50790..50795` (6) | **Ultrasonic UL202 Fuel Level 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 50790, ...}`) |
| 385 | **`50800`** | `50800..50804` (5) | **Ultrasonic UL202 Status 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 50800, ...}`) |
| 386 | **`50810`** | `50810..50814` (5) | **BLE LLS #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 50810, ...}`) |
| 387 | **`50820`** | `50820..50824` (3) | **IMSI** | `—` | `0` | — *(None)* | `setio` (`{"id": 50820, ...}`) |
| 388 | **`51000`** | `51000..51004` (5) | **Record Counter** | `—` | `0` | — *(None)* | `setio` (`{"id": 51000, ...}`) |
| 389 | **`51010`** | `51010..51014` (5) | **DIN2 Minutes** | `min` | `0` | — *(None)* | `setio` (`{"id": 51010, ...}`) |
| 390 | **`51020`** | `51020..51024` (5) | **DIN3 Minutes** | `min` | `0` | — *(None)* | `setio` (`{"id": 51020, ...}`) |
| 391 | **`51030`** | `51030..51034` (5) | **DIN4 Minutes** | `min` | `0` | — *(None)* | `setio` (`{"id": 51030, ...}`) |
| 392 | **`51040`** | `51040..51044` (5) | **Temperature Probe 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 51040, ...}`) |
| 393 | **`51050`** | `51050..51054` (5) | **Instant Movement** | `—` | `0` | — *(None)* | `setio` (`{"id": 51050, ...}`) |
| 394 | **`51060`** | `51060..51064` (5) | **BLE LLS Freq #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 51060, ...}`) |
| 395 | **`51070`** | `51070..51074` (5) | **BLE LLS Freq #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51070, ...}`) |
| 396 | **`51090`** | `51090..51094` (5) | **BLE LLS Freq #4** | `—` | `0` | — *(None)* | `setio` (`{"id": 51090, ...}`) |
| 397 | **`51100`** | `51100..51104` (5) | **BLE 2 Custom 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 51100, ...}`) |
| 398 | **`51110`** | `51110..51114` (5) | **BLE 3 Custom 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 51110, ...}`) |
| 399 | **`51120`** | `51120..51124` (5) | **BLE 4 Custom 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 51120, ...}`) |
| 400 | **`51130`** | `51130..51134` (5) | **BLE LLS Fuel #1** | `kvants` | `0` | — *(None)* | `setio` (`{"id": 51130, ...}`) |
| 401 | **`51140`** | `51140..51144` (5) | **BLE LLS Fuel #2** | `kvants` | `0` | — *(None)* | `setio` (`{"id": 51140, ...}`) |
| 402 | **`51150`** | `51150..51154` (5) | **UL202 Sensor Fuel level** | `—` | `0` | — *(None)* | `setio` (`{"id": 51150, ...}`) |
| 403 | **`51160`** | `51160..51164` (5) | **UL202 Sensor Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 51160, ...}`) |
| 404 | **`51170`** | `51170..51174` (5) | **BLE Luminosity #1** | `lx` | `0` | — *(None)* | `setio` (`{"id": 51170, ...}`) |
| 405 | **`51180`** | `51180..51184` (5) | **BLE Luminosity #2** | `lx` | `0` | — *(None)* | `setio` (`{"id": 51180, ...}`) |
| 406 | **`51190`** | `51190..51194` (5) | **BLE Custom sensor #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 51190, ...}`) |
| 407 | **`51200`** | `51200..51204` (5) | **BLE Custom sensor #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51200, ...}`) |
| 408 | **`51210`** | `51210..51214` (5) | **BLE Custom sensor #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 51210, ...}`) |
| 409 | **`51220`** | `51220..51224` (5) | **BLE Custom sensor #4** | `—` | `0` | — *(None)* | `setio` (`{"id": 51220, ...}`) |
| 410 | **`51230`** | `51230..51234` (5) | **BLE Illumination #1** | `—` | `0` | — *(None)* | `setio` (`{"id": 51230, ...}`) |
| 411 | **`51240`** | `51240..51244` (5) | **BLE Illumination #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51240, ...}`) |
| 412 | **`51860`** | `51860..51864` (5) | **BLE 1 Custom 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51860, ...}`) |
| 413 | **`51870`** | `51870..51874` (5) | **BLE 1 Custom 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 51870, ...}`) |
| 414 | **`51880`** | `51880..51884` (5) | **BLE 1 Custom 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 51880, ...}`) |
| 415 | **`51890`** | `51890..51894` (5) | **BLE 1 Custom 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 51890, ...}`) |
| 416 | **`51900`** | `51900..51904` (5) | **BLE 2 Custom 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51900, ...}`) |
| 417 | **`51910`** | `51910..51914` (5) | **BLE 2 Custom 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 51910, ...}`) |
| 418 | **`51920`** | `51920..51924` (5) | **BLE 2 Custom 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 51920, ...}`) |
| 419 | **`51930`** | `51930..51934` (5) | **BLE 2 Custom 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 51930, ...}`) |
| 420 | **`51940`** | `51940..51944` (5) | **BLE 3 Custom 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51940, ...}`) |
| 421 | **`51950`** | `51950..51954` (5) | **BLE 3 Custom 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 51950, ...}`) |
| 422 | **`51960`** | `51960..51964` (5) | **BLE 3 Custom 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 51960, ...}`) |
| 423 | **`51970`** | `51970..51974` (5) | **BLE 3 Custom 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 51970, ...}`) |
| 424 | **`51980`** | `51980..51984` (5) | **BLE 4 Custom 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 51980, ...}`) |
| 425 | **`51990`** | `51990..51994` (5) | **BLE 4 Custom 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 51990, ...}`) |
| 426 | **`52000`** | `52000..52004` (5) | **BLE 4 Custom 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 52000, ...}`) |
| 427 | **`52010`** | `52010..52014` (5) | **BLE 4 Custom 5** | `—` | `0` | — *(None)* | `setio` (`{"id": 52010, ...}`) |
| 428 | **`52020`** | `52020..52025` (6) | **1Wire Sensor Humidity 1** | `%RH` | `0` | — *(None)* | `setio` (`{"id": 52020, ...}`) |
| 429 | **`52030`** | `52030..52035` (6) | **UL202 Sensor Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 52030, ...}`) |
| 430 | **`52040`** | `52040..52045` (6) | **Driver Name** | `—` | `0` | — *(None)* | `setio` (`{"id": 52040, ...}`) |
| 431 | **`52050`** | `52050..52055` (6) | **Driver Card License Type** | `—` | `0` | — *(None)* | `setio` (`{"id": 52050, ...}`) |
| 432 | **`52060`** | `52060..52065` (6) | **Driver Gender** | `—` | `0` | — *(None)* | `setio` (`{"id": 52060, ...}`) |
| 433 | **`52070`** | `52070..52075` (6) | **Driver Card ID** | `—` | `0` | — *(None)* | `setio` (`{"id": 52070, ...}`) |
| 434 | **`52150`** | `52150..52155` (6) | **Impulse Frequency 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 52150, ...}`) |
| 435 | **`52160`** | `52160..52165` (6) | **Impulse RPM 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 52160, ...}`) |
| 436 | **`52170`** | `52170..52175` (6) | **Impulse Frequency 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 52170, ...}`) |
| 437 | **`52180`** | `52180..52185` (6) | **Impulse RPM 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 52180, ...}`) |
| 438 | **`52190`** | `52190..52194` (5) | **Eco Score** | `—` | `0` | — *(None)* | `setio` (`{"id": 52190, ...}`) |
| 439 | **`52250`** | `52250..52254` (5) | **No SIM Err Counter** | `—` | `0` | — *(None)* | `setio` (`{"id": 52250, ...}`) |
| 440 | **`52340`** | `52340..52344` (5) | **Ignition Work Time** | `s` | `1` | — *(None)* | `setio` (`{"id": 52340, ...}`) |
| 441 | **`52350`** | `52350..52354` (5) | **LTE Cell Id** | `—` | `0` | — *(None)* | `setio` (`{"id": 52350, ...}`) |
| 442 | **`52870`** | `52870..52874` (5) | **Impulse Counter 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 52870, ...}`) |
| 443 | **`52880`** | `52880..52884` (5) | **Impulse Counter 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 52880, ...}`) |
| 444 | **`52890`** | `52890..52895` (6) | **Impulse Frequency 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 52890, ...}`) |
| 445 | **`52900`** | `52900..52905` (6) | **Impulse RPM 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 52900, ...}`) |
| 446 | **`52910`** | `52910..52915` (6) | **Impulse Frequency 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 52910, ...}`) |
| 447 | **`52920`** | `52920..52925` (6) | **Impulse RPM 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 52920, ...}`) |
| 448 | **`52980`** | `52980..52985` (6) | **UL212 (P19) Fuel Volume 1** | `L/10` | `0` | — *(None)* | `setio` (`{"id": 52980, ...}`) |
| 449 | **`52990`** | `52990..52995` (6) | **UL212 (P19) Fuel Level 1** | `mm/10` | `0` | — *(None)* | `setio` (`{"id": 52990, ...}`) |
| 450 | **`53000`** | `53000..53005` (6) | **UL212 (P19) Fuel Volume 2** | `L/10` | `0` | — *(None)* | `setio` (`{"id": 53000, ...}`) |
| 451 | **`53010`** | `53010..53015` (6) | **UL212 (P19) Fuel Level 2** | `mm/10` | `0` | — *(None)* | `setio` (`{"id": 53010, ...}`) |
| 452 | **`53790`** | `53790..53795` (6) | **ConnectivityQuality** | `—` | `0` | — *(None)* | `setio` (`{"id": 53790, ...}`) |
| 453 | **`53920`** | `53920..53924` (3) | **IMEI IO** | `—` | `0` | — *(None)* | `setio` (`{"id": 53920, ...}`) |
| 454 | **`54220`** | `54220..54224` (5) | **Axl Calibration State** | `—` | `0` | — *(None)* | `setio` (`{"id": 54220, ...}`) |
| 455 | **`74000`** | `74000..74004` (3) | **Driver1 Remaining Current Driving Time** | `—` | `0` | — *(None)* | `setio` (`{"id": 74000, ...}`) |
| 456 | **`74010`** | `74010..74014` (3) | **Driver1 Remaining Driving Time On Current Shift** | `—` | `0` | — *(None)* | `setio` (`{"id": 74010, ...}`) |
| 457 | **`74020`** | `74020..74024` (3) | **Driver1 Remaining Driving Time Of Current Week** | `—` | `0` | — *(None)* | `setio` (`{"id": 74020, ...}`) |
| 458 | **`74030`** | `74030..74034` (3) | **Driver1 Open Compensation In The Last Week** | `—` | `0` | — *(None)* | `setio` (`{"id": 74030, ...}`) |
| 459 | **`74040`** | `74040..74044` (3) | **Driver1 Open Compensation In Week Before Last** | `—` | `0` | — *(None)* | `setio` (`{"id": 74040, ...}`) |
| 460 | **`74050`** | `74050..74054` (3) | **Driver1 Open Compensation In 2nd Week Before Last** | `—` | `0` | — *(None)* | `setio` (`{"id": 74050, ...}`) |
| 461 | **`74060`** | `74060..74064` (3) | **Driver1 Additional Information** | `—` | `0` | — *(None)* | `setio` (`{"id": 74060, ...}`) |
| 462 | **`74070`** | `74070..74074` (3) | **Driver1 Remaining Time Current Break Rest** | `—` | `0` | — *(None)* | `setio` (`{"id": 74070, ...}`) |
| 463 | **`74080`** | `74080..74084` (3) | **Driver1 Time Left Until Next Driving Period** | `—` | `0` | — *(None)* | `setio` (`{"id": 74080, ...}`) |
| 464 | **`74090`** | `74090..74094` (3) | **Driver1 Duration Of Next Driving Period** | `—` | `0` | — *(None)* | `setio` (`{"id": 74090, ...}`) |
| 465 | **`74100`** | `74100..74104` (3) | **Ferry/Train Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 74100, ...}`) |
| 466 | **`74110`** | `74110..74114` (3) | **Border Crossing Info** | `—` | `0` | — *(None)* | `setio` (`{"id": 74110, ...}`) |
| 467 | **`74120`** | `74120..74124` (3) | **K-Line Driver Privacy** | `—` | `0` | — *(None)* | `setio` (`{"id": 74120, ...}`) |
| 468 | **`74130`** | `74130..74134` (3) | **Vehicle Load Type** | `—` | `0` | — *(None)* | `setio` (`{"id": 74130, ...}`) |
| 469 | **`74140`** | `74140..74144` (3) | **Driver1 Last Load/Unload Operation Time** | `—` | `0` | — *(None)* | `setio` (`{"id": 74140, ...}`) |
| 470 | **`74150`** | `74150..74154` (3) | **Driver2 Last Load/Unload Operation Time** | `—` | `0` | — *(None)* | `setio` (`{"id": 74150, ...}`) |
| 471 | **`74160`** | `74160..74164` (3) | **Drivers Private Data Consent** | `—` | `0` | — *(None)* | `setio` (`{"id": 74160, ...}`) |
| 472 | **`74170`** | `74170..74174` (3) | **Driver1 Card Expiry Date** | `—` | `0` | — *(None)* | `setio` (`{"id": 74170, ...}`) |
| 473 | **`74180`** | `74180..74184` (3) | **Driver2 Card Expiry Date** | `—` | `0` | — *(None)* | `setio` (`{"id": 74180, ...}`) |
| 474 | **`90000`** | `90000..90004` (5) | **CAN20** | `—` | `2` | — *(None)* | `setio` (`{"id": 90000, ...}`) |
| 475 | **`90010`** | `90010..90014` (5) | **CAN21** | `—` | `2` | — *(None)* | `setio` (`{"id": 90010, ...}`) |
| 476 | **`90020`** | `90020..90024` (5) | **CAN22** | `—` | `2` | — *(None)* | `setio` (`{"id": 90020, ...}`) |
| 477 | **`90030`** | `90030..90034` (5) | **CAN23** | `—` | `2` | — *(None)* | `setio` (`{"id": 90030, ...}`) |
| 478 | **`90040`** | `90040..90044` (5) | **CAN24** | `—` | `0` | — *(None)* | `setio` (`{"id": 90040, ...}`) |
| 479 | **`90050`** | `90050..90054` (5) | **CAN25** | `—` | `0` | — *(None)* | `setio` (`{"id": 90050, ...}`) |
| 480 | **`90060`** | `90060..90064` (5) | **CAN26** | `—` | `0` | — *(None)* | `setio` (`{"id": 90060, ...}`) |
| 481 | **`90070`** | `90070..90074` (5) | **CAN27** | `—` | `0` | — *(None)* | `setio` (`{"id": 90070, ...}`) |
| 482 | **`90080`** | `90080..90084` (5) | **CAN28** | `—` | `0` | — *(None)* | `setio` (`{"id": 90080, ...}`) |
| 483 | **`90090`** | `90090..90094` (5) | **CAN29** | `—` | `0` | — *(None)* | `setio` (`{"id": 90090, ...}`) |
| 484 | **`90100`** | `90100..90104` (5) | **CAN30** | `—` | `0` | — *(None)* | `setio` (`{"id": 90100, ...}`) |
| 485 | **`90110`** | `90110..90114` (5) | **CAN31** | `—` | `0` | — *(None)* | `setio` (`{"id": 90110, ...}`) |
| 486 | **`90120`** | `90120..90124` (5) | **CAN32** | `—` | `0` | — *(None)* | `setio` (`{"id": 90120, ...}`) |
| 487 | **`90130`** | `90130..90134` (5) | **CAN33** | `—` | `0` | — *(None)* | `setio` (`{"id": 90130, ...}`) |
| 488 | **`90140`** | `90140..90144` (5) | **CAN34** | `—` | `0` | — *(None)* | `setio` (`{"id": 90140, ...}`) |
| 489 | **`90150`** | `90150..90154` (5) | **CAN35** | `—` | `0` | — *(None)* | `setio` (`{"id": 90150, ...}`) |
| 490 | **`90160`** | `90160..90164` (5) | **CAN36** | `—` | `0` | — *(None)* | `setio` (`{"id": 90160, ...}`) |
| 491 | **`90170`** | `90170..90174` (5) | **CAN37** | `—` | `0` | — *(None)* | `setio` (`{"id": 90170, ...}`) |
| 492 | **`90180`** | `90180..90184` (5) | **CAN38** | `—` | `0` | — *(None)* | `setio` (`{"id": 90180, ...}`) |
| 493 | **`90190`** | `90190..90194` (5) | **CAN39** | `—` | `0` | — *(None)* | `setio` (`{"id": 90190, ...}`) |
| 494 | **`90200`** | `90200..90204` (5) | **CAN40** | `—` | `0` | — *(None)* | `setio` (`{"id": 90200, ...}`) |
| 495 | **`90210`** | `90210..90214` (5) | **CAN41** | `—` | `0` | — *(None)* | `setio` (`{"id": 90210, ...}`) |
| 496 | **`90220`** | `90220..90224` (5) | **CAN42** | `—` | `0` | — *(None)* | `setio` (`{"id": 90220, ...}`) |
| 497 | **`90230`** | `90230..90234` (5) | **CAN43** | `—` | `0` | — *(None)* | `setio` (`{"id": 90230, ...}`) |
| 498 | **`90240`** | `90240..90244` (5) | **CAN44** | `—` | `0` | — *(None)* | `setio` (`{"id": 90240, ...}`) |
| 499 | **`90250`** | `90250..90254` (5) | **CAN45** | `—` | `0` | — *(None)* | `setio` (`{"id": 90250, ...}`) |
| 500 | **`90260`** | `90260..90264` (5) | **CAN46** | `—` | `0` | — *(None)* | `setio` (`{"id": 90260, ...}`) |
| 501 | **`90270`** | `90270..90274` (5) | **CAN47** | `—` | `0` | — *(None)* | `setio` (`{"id": 90270, ...}`) |
| 502 | **`90280`** | `90280..90284` (5) | **CAN48** | `—` | `0` | — *(None)* | `setio` (`{"id": 90280, ...}`) |
| 503 | **`90290`** | `90290..90294` (5) | **CAN49** | `—` | `0` | — *(None)* | `setio` (`{"id": 90290, ...}`) |
| 504 | **`90300`** | `90300..90304` (5) | **CAN50** | `—` | `0` | — *(None)* | `setio` (`{"id": 90300, ...}`) |
| 505 | **`90310`** | `90310..90314` (5) | **CAN51** | `—` | `0` | — *(None)* | `setio` (`{"id": 90310, ...}`) |
| 506 | **`90320`** | `90320..90324` (5) | **CAN52** | `—` | `0` | — *(None)* | `setio` (`{"id": 90320, ...}`) |
| 507 | **`90330`** | `90330..90334` (5) | **CAN53** | `—` | `0` | — *(None)* | `setio` (`{"id": 90330, ...}`) |
| 508 | **`90340`** | `90340..90344` (5) | **CAN54** | `—` | `0` | — *(None)* | `setio` (`{"id": 90340, ...}`) |
| 509 | **`90350`** | `90350..90354` (5) | **CAN55** | `—` | `0` | — *(None)* | `setio` (`{"id": 90350, ...}`) |
| 510 | **`90360`** | `90360..90364` (5) | **CAN56** | `—` | `0` | — *(None)* | `setio` (`{"id": 90360, ...}`) |
| 511 | **`90370`** | `90370..90374` (5) | **CAN57** | `—` | `0` | — *(None)* | `setio` (`{"id": 90370, ...}`) |
| 512 | **`90380`** | `90380..90384` (5) | **CAN58** | `—` | `0` | — *(None)* | `setio` (`{"id": 90380, ...}`) |
| 513 | **`90390`** | `90390..90394` (5) | **CAN59** | `—` | `0` | — *(None)* | `setio` (`{"id": 90390, ...}`) |
| 514 | **`90400`** | `90400..90404` (5) | **CAN60** | `—` | `0` | — *(None)* | `setio` (`{"id": 90400, ...}`) |
| 515 | **`90410`** | `90410..90414` (5) | **CAN61** | `—` | `0` | — *(None)* | `setio` (`{"id": 90410, ...}`) |
| 516 | **`90420`** | `90420..90424` (5) | **CAN62** | `—` | `0` | — *(None)* | `setio` (`{"id": 90420, ...}`) |
| 517 | **`90430`** | `90430..90434` (5) | **CAN63** | `—` | `0` | — *(None)* | `setio` (`{"id": 90430, ...}`) |
| 518 | **`90440`** | `90440..90444` (5) | **CAN64** | `—` | `0` | — *(None)* | `setio` (`{"id": 90440, ...}`) |
| 519 | **`90450`** | `90450..90454` (5) | **CAN65** | `—` | `0` | — *(None)* | `setio` (`{"id": 90450, ...}`) |
| 520 | **`90460`** | `90460..90464` (5) | **CAN66** | `—` | `0` | — *(None)* | `setio` (`{"id": 90460, ...}`) |
| 521 | **`90470`** | `90470..90474` (5) | **CAN67** | `—` | `0` | — *(None)* | `setio` (`{"id": 90470, ...}`) |
| 522 | **`90480`** | `90480..90484` (5) | **CAN68** | `—` | `0` | — *(None)* | `setio` (`{"id": 90480, ...}`) |
| 523 | **`90490`** | `90490..90494` (5) | **CAN69** | `—` | `0` | — *(None)* | `setio` (`{"id": 90490, ...}`) |
| 524 | **`90600`** | `90600..90604` (5) | **High voltage battery voltage** | `mV` | `0` | — *(None)* | `setio` (`{"id": 90600, ...}`) |
| 525 | **`90610`** | `90610..90614` (5) | **High voltage battery current** | `mA` | `0` | — *(None)* | `setio` (`{"id": 90610, ...}`) |
| 526 | **`90620`** | `90620..90624` (3) | **Internal Charger Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 90620, ...}`) |
| 527 | **`90630`** | `90630..90634` (3) | **Generic state of charge** | `—` | `0` | — *(None)* | `setio` (`{"id": 90630, ...}`) |
| 528 | **`90640`** | `90640..90644` (3) | **EV Ignition** | `—` | `0` | — *(None)* | `setio` (`{"id": 90640, ...}`) |
| 529 | **`90650`** | `90650..90654` (3) | **Seatbelt switch** | `—` | `0` | — *(None)* | `setio` (`{"id": 90650, ...}`) |
| 530 | **`90660`** | `90660..90664` (5) | **EVSE1 AC RMS Current** | `mA` | `0` | — *(None)* | `setio` (`{"id": 90660, ...}`) |
| 531 | **`90670`** | `90670..90674` (5) | **EVSE1 AC RMS Voltage** | `mV` | `0` | — *(None)* | `setio` (`{"id": 90670, ...}`) |
| 532 | **`90680`** | `90680..90684` (3) | **DC Charging State** | `—` | `0` | — *(None)* | `setio` (`{"id": 90680, ...}`) |
| 533 | **`90690`** | `90690..90694` (5) | **High Voltage Battery Highest Cell Temp** | `℃` | `0` | — *(None)* | `setio` (`{"id": 90690, ...}`) |
| 534 | **`90700`** | `90700..90704` (5) | **High Voltage Battery Lowest Cell Temp** | `℃` | `0` | — *(None)* | `setio` (`{"id": 90700, ...}`) |
| 535 | **`90710`** | `90710..90714` (5) | **Motor Coolant Fan1 Control Temp** | `℃` | `0` | — *(None)* | `setio` (`{"id": 90710, ...}`) |
| 536 | **`90720`** | `90720..90724` (3) | **Air Conditioner Compressor Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 90720, ...}`) |
| 537 | **`90730`** | `90730..90734` (5) | **High Voltage Battery Temp** | `℃` | `0` | — *(None)* | `setio` (`{"id": 90730, ...}`) |
| 538 | **`90740`** | `90740..90744` (3) | **HVESS Thermal Management System Heater Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 90740, ...}`) |
| 539 | **`90750`** | `90750..90754` (5) | **Trailer Weight** | `kg` | `0` | — *(None)* | `setio` (`{"id": 90750, ...}`) |
| 540 | **`90760`** | `90760..90764` (5) | **Cargo Weight** | `kg` | `0` | — *(None)* | `setio` (`{"id": 90760, ...}`) |
| 541 | **`90770`** | `90770..90774` (5) | **Powered Vehicle Weight** | `kg` | `0` | — *(None)* | `setio` (`{"id": 90770, ...}`) |
| 542 | **`90780`** | `90780..90784` (5) | **Gross Combination Vehicle Weight** | `kg` | `0` | — *(None)* | `setio` (`{"id": 90780, ...}`) |
| 543 | **`90790`** | `90790..90794` (5) | **Highest cell voltage** | `mV` | `0` | — *(None)* | `setio` (`{"id": 90790, ...}`) |
| 544 | **`90800`** | `90800..90804` (5) | **Lowest cell voltage** | `mV` | `0` | — *(None)* | `setio` (`{"id": 90800, ...}`) |
| 545 | **`90810`** | `90810..90814` (5) | **HVESS State of Health** | `%` | `0` | — *(None)* | `setio` (`{"id": 90810, ...}`) |
| 546 | **`90820`** | `90820..90824` (5) | **HVESS Total Energy Throughput** | `W` | `0` | — *(None)* | `setio` (`{"id": 90820, ...}`) |
| 547 | **`90830`** | `90830..90834` (5) | **HVESS Estimated Remaining Distance** | `km` | `0` | — *(None)* | `setio` (`{"id": 90830, ...}`) |
| 548 | **`90840`** | `90840..90844` (3) | **Propulsion System Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 90840, ...}`) |
| 549 | **`103000`** | `103000..103004` (5) | **Detected Towed Vehicle** | `—` | `0` | — *(None)* | `setio` (`{"id": 103000, ...}`) |
| 550 | **`103020`** | `103020..103024` (5) | **Vehicle ABS Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103020, ...}`) |
| 551 | **`103030`** | `103030..103034` (5) | **Vehicle Retarder Control Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103030, ...}`) |
| 552 | **`103040`** | `103040..103044` (5) | **Red Warning Signal Request** | `—` | `0` | — *(None)* | `setio` (`{"id": 103040, ...}`) |
| 553 | **`103050`** | `103050..103054` (5) | **Amber Warning Signal Request** | `—` | `0` | — *(None)* | `setio` (`{"id": 103050, ...}`) |
| 554 | **`103060`** | `103060..103064` (5) | **Axle Load Sum** | `kg` | `0` | — *(None)* | `setio` (`{"id": 103060, ...}`) |
| 555 | **`103070`** | `103070..103074` (5) | **Retarder Wheel Torque Reference** | `Nm` | `0` | — *(None)* | `setio` (`{"id": 103070, ...}`) |
| 556 | **`103080`** | `103080..103084` (5) | **Vehicle Service Brake Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103080, ...}`) |
| 557 | **`103090`** | `103090..103094` (5) | **Vehicle Electrical Supply Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103090, ...}`) |
| 558 | **`103100`** | `103100..103104` (5) | **Vehicle Type** | `—` | `0` | — *(None)* | `setio` (`{"id": 103100, ...}`) |
| 559 | **`103110`** | `103110..103114` (5) | **Axle Load Measured By Towed Vehicle** | `kg` | `0` | — *(None)* | `setio` (`{"id": 103110, ...}`) |
| 560 | **`103120`** | `103120..103124` (5) | **Axle Load Measured By External Scale** | `kg` | `0` | — *(None)* | `setio` (`{"id": 103120, ...}`) |
| 561 | **`103130`** | `103130..103134` (5) | **Axle Load Calibration Data Load Level** | `—` | `0` | — *(None)* | `setio` (`{"id": 103130, ...}`) |
| 562 | **`103140`** | `103140..103144` (5) | **Brake Cylinder Pressure First Axle Left Wheel** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103140, ...}`) |
| 563 | **`103150`** | `103150..103154` (5) | **Brake Cylinder Pressure First Axle Right Wheel** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103150, ...}`) |
| 564 | **`103160`** | `103160..103164` (5) | **Brake Cylinder Pressure Second Axle Left Wheel** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103160, ...}`) |
| 565 | **`103170`** | `103170..103174` (5) | **Brake Cylinder Pressure Second Axle Right Wheel** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103170, ...}`) |
| 566 | **`103180`** | `103180..103184` (5) | **Brake Cylinder Pressure Third Axle Left Wheel** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103180, ...}`) |
| 567 | **`103190`** | `103190..103194` (5) | **Brake Cylinder Pressure Third Axle Right Wheel** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103190, ...}`) |
| 568 | **`103200`** | `103200..103204` (5) | **VIN** | `—` | `0` | — *(None)* | `setio` (`{"id": 103200, ...}`) |
| 569 | **`103210`** | `103210..103214` (5) | **VDC Active** | `—` | `0` | — *(None)* | `setio` (`{"id": 103210, ...}`) |
| 570 | **`103220`** | `103220..103224` (5) | **Lateral Acceleration** | `m/s^2` | `0` | — *(None)* | `setio` (`{"id": 103220, ...}`) |
| 571 | **`103230`** | `103230..103234` (5) | **Loading Ramp Approach Assistance Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103230, ...}`) |
| 572 | **`103240`** | `103240..103244` (5) | **Supply Line Braking** | `—` | `0` | — *(None)* | `setio` (`{"id": 103240, ...}`) |
| 573 | **`103250`** | `103250..103254` (5) | **Stop Lamps Request** | `—` | `0` | — *(None)* | `setio` (`{"id": 103250, ...}`) |
| 574 | **`103260`** | `103260..103264` (5) | **Braking Via Electric Control Line Support** | `—` | `0` | — *(None)* | `setio` (`{"id": 103260, ...}`) |
| 575 | **`103270`** | `103270..103274` (5) | **ROP System Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103270, ...}`) |
| 576 | **`103280`** | `103280..103284` (5) | **YC System Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103280, ...}`) |
| 577 | **`103290`** | `103290..103294` (5) | **Traction Help Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103290, ...}`) |
| 578 | **`103300`** | `103300..103304` (5) | **Lift Axle 1 Position Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103300, ...}`) |
| 579 | **`103310`** | `103310..103314` (5) | **Lift Axle 2 Position Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103310, ...}`) |
| 580 | **`103320`** | `103320..103324` (5) | **Steering Axle Locking Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 103320, ...}`) |
| 581 | **`103330`** | `103330..103334` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103330, ...}`) |
| 582 | **`103340`** | `103340..103344` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103340, ...}`) |
| 583 | **`103350`** | `103350..103354` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103350, ...}`) |
| 584 | **`103360`** | `103360..103364` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103360, ...}`) |
| 585 | **`103370`** | `103370..103374` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103370, ...}`) |
| 586 | **`103380`** | `103380..103384` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103380, ...}`) |
| 587 | **`103390`** | `103390..103394` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103390, ...}`) |
| 588 | **`103400`** | `103400..103404` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103400, ...}`) |
| 589 | **`103410`** | `103410..103414` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103410, ...}`) |
| 590 | **`103420`** | `103420..103424` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103420, ...}`) |
| 591 | **`103430`** | `103430..103434` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103430, ...}`) |
| 592 | **`103440`** | `103440..103444` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103440, ...}`) |
| 593 | **`103450`** | `103450..103454` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103450, ...}`) |
| 594 | **`103460`** | `103460..103464` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103460, ...}`) |
| 595 | **`103470`** | `103470..103474` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103470, ...}`) |
| 596 | **`103480`** | `103480..103484` (5) | **Wheel Tire Pressure Axle 1 Wheel 6** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103480, ...}`) |
| 597 | **`103490`** | `103490..103494` (5) | **Wheel Tire Pressure Axle 1 Wheel 7** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103490, ...}`) |
| 598 | **`103500`** | `103500..103504` (5) | **Wheel Tire Pressure Axle 1 Wheel 8** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103500, ...}`) |
| 599 | **`103510`** | `103510..103514` (5) | **Wheel Tire Pressure Axle 1 Wheel 9** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103510, ...}`) |
| 600 | **`103520`** | `103520..103524` (5) | **Wheel Tire Pressure Axle 1 Wheel 10** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103520, ...}`) |
| 601 | **`103530`** | `103530..103534` (5) | **Wheel Tire Pressure Axle 2 Wheel 6** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103530, ...}`) |
| 602 | **`103540`** | `103540..103544` (5) | **Wheel Tire Pressure Axle 2 Wheel 7** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103540, ...}`) |
| 603 | **`103550`** | `103550..103554` (5) | **Wheel Tire Pressure Axle 2 Wheel 8** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103550, ...}`) |
| 604 | **`103560`** | `103560..103564` (5) | **Wheel Tire Pressure Axle 2 Wheel 9** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103560, ...}`) |
| 605 | **`103570`** | `103570..103574` (5) | **Wheel Tire Pressure Axle 2 Wheel 10** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103570, ...}`) |
| 606 | **`103580`** | `103580..103584` (5) | **Wheel Tire Pressure Axle 3 Wheel 6** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103580, ...}`) |
| 607 | **`103590`** | `103590..103594` (5) | **Wheel Tire Pressure Axle 3 Wheel 7** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103590, ...}`) |
| 608 | **`103600`** | `103600..103604` (5) | **Wheel Tire Pressure Axle 3 Wheel 8** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103600, ...}`) |
| 609 | **`103610`** | `103610..103614` (5) | **Wheel Tire Pressure Axle 3 Wheel 9** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103610, ...}`) |
| 610 | **`103620`** | `103620..103624` (5) | **Wheel Tire Pressure Axle 3 Wheel 10** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 103620, ...}`) |
| 611 | **`103630`** | `103630..103634` (5) | **Wheel Brake Lining Status Axle 1 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103630, ...}`) |
| 612 | **`103640`** | `103640..103644` (5) | **Wheel Brake Lining Status Axle 1 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103640, ...}`) |
| 613 | **`103650`** | `103650..103654` (5) | **Wheel Brake Lining Status Axle 1 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103650, ...}`) |
| 614 | **`103660`** | `103660..103664` (5) | **Wheel Brake Lining Status Axle 1 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103660, ...}`) |
| 615 | **`103670`** | `103670..103674` (5) | **Wheel Brake Lining Status Axle 1 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103670, ...}`) |
| 616 | **`103680`** | `103680..103684` (5) | **Wheel Brake Lining Status Axle 2 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103680, ...}`) |
| 617 | **`103690`** | `103690..103694` (5) | **Wheel Brake Lining Status Axle 2 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103690, ...}`) |
| 618 | **`103700`** | `103700..103704` (5) | **Wheel Brake Lining Status Axle 2 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103700, ...}`) |
| 619 | **`103710`** | `103710..103714` (5) | **Wheel Brake Lining Status Axle 2 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103710, ...}`) |
| 620 | **`103720`** | `103720..103724` (5) | **Wheel Brake Lining Status Axle 2 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103720, ...}`) |
| 621 | **`103730`** | `103730..103734` (5) | **Wheel Brake Lining Status Axle 3 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103730, ...}`) |
| 622 | **`103740`** | `103740..103744` (5) | **Wheel Brake Lining Status Axle 3 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103740, ...}`) |
| 623 | **`103750`** | `103750..103754` (5) | **Wheel Brake Lining Status Axle 3 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103750, ...}`) |
| 624 | **`103760`** | `103760..103764` (5) | **Wheel Brake Lining Status Axle 3 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103760, ...}`) |
| 625 | **`103770`** | `103770..103774` (5) | **Wheel Brake Lining Status Axle 3 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103770, ...}`) |
| 626 | **`103780`** | `103780..103784` (5) | **Wheel Brake Lining Axle 1 Wheel 6** | `%` | `0` | — *(None)* | `setio` (`{"id": 103780, ...}`) |
| 627 | **`103790`** | `103790..103794` (5) | **Wheel Brake Lining Axle 1 Wheel 7** | `%` | `0` | — *(None)* | `setio` (`{"id": 103790, ...}`) |
| 628 | **`103800`** | `103800..103804` (5) | **Wheel Brake Lining Axle 1 Wheel 8** | `%` | `0` | — *(None)* | `setio` (`{"id": 103800, ...}`) |
| 629 | **`103810`** | `103810..103814` (5) | **Wheel Brake Lining Axle 1 Wheel 9** | `%` | `0` | — *(None)* | `setio` (`{"id": 103810, ...}`) |
| 630 | **`103820`** | `103820..103824` (5) | **Wheel Brake Lining Axle 1 Wheel 10** | `%` | `0` | — *(None)* | `setio` (`{"id": 103820, ...}`) |
| 631 | **`103830`** | `103830..103834` (5) | **Wheel Brake Lining Axle 2 Wheel 6** | `%` | `0` | — *(None)* | `setio` (`{"id": 103830, ...}`) |
| 632 | **`103840`** | `103840..103844` (5) | **Wheel Brake Lining Axle 2 Wheel 7** | `%` | `0` | — *(None)* | `setio` (`{"id": 103840, ...}`) |
| 633 | **`103850`** | `103850..103854` (5) | **Wheel Brake Lining Axle 2 Wheel 8** | `%` | `0` | — *(None)* | `setio` (`{"id": 103850, ...}`) |
| 634 | **`103860`** | `103860..103864` (5) | **Wheel Brake Lining Axle 2 Wheel 9** | `%` | `0` | — *(None)* | `setio` (`{"id": 103860, ...}`) |
| 635 | **`103870`** | `103870..103874` (5) | **Wheel Brake Lining Axle 2 Wheel 10** | `%` | `0` | — *(None)* | `setio` (`{"id": 103870, ...}`) |
| 636 | **`103880`** | `103880..103884` (5) | **Wheel Brake Lining Axle 3 Wheel 6** | `%` | `0` | — *(None)* | `setio` (`{"id": 103880, ...}`) |
| 637 | **`103890`** | `103890..103894` (5) | **Wheel Brake Lining Axle 3 Wheel 7** | `%` | `0` | — *(None)* | `setio` (`{"id": 103890, ...}`) |
| 638 | **`103900`** | `103900..103904` (5) | **Wheel Brake Lining Axle 3 Wheel 8** | `%` | `0` | — *(None)* | `setio` (`{"id": 103900, ...}`) |
| 639 | **`103910`** | `103910..103914` (5) | **Wheel Brake Lining Axle 3 Wheel 9** | `%` | `0` | — *(None)* | `setio` (`{"id": 103910, ...}`) |
| 640 | **`103920`** | `103920..103924` (5) | **Wheel Brake Lining Axle 3 Wheel 10** | `%` | `0` | — *(None)* | `setio` (`{"id": 103920, ...}`) |
| 641 | **`103930`** | `103930..103934` (5) | **Wheel Brake Temp Status Axle 1 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103930, ...}`) |
| 642 | **`103940`** | `103940..103944` (5) | **Wheel Brake Temp Status Axle 1 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103940, ...}`) |
| 643 | **`103950`** | `103950..103954` (5) | **Wheel Brake Temp Status Axle 1 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 103950, ...}`) |
| 644 | **`103960`** | `103960..103964` (5) | **Wheel Brake Temp Status Axle 1 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 103960, ...}`) |
| 645 | **`103970`** | `103970..103974` (5) | **Wheel Brake Temp Status Axle 1 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 103970, ...}`) |
| 646 | **`103980`** | `103980..103984` (5) | **Wheel Brake Temp Status Axle 2 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 103980, ...}`) |
| 647 | **`103990`** | `103990..103994` (5) | **Wheel Brake Temp Status Axle 2 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 103990, ...}`) |
| 648 | **`104000`** | `104000..104004` (5) | **Wheel Brake Temp Status Axle 2 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 104000, ...}`) |
| 649 | **`104010`** | `104010..104014` (5) | **Wheel Brake Temp Status Axle 2 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 104010, ...}`) |
| 650 | **`104020`** | `104020..104024` (5) | **Wheel Brake Temp Status Axle 2 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 104020, ...}`) |
| 651 | **`104030`** | `104030..104034` (5) | **Wheel Brake Temp Status Axle 3 Wheel 6** | `—` | `0` | — *(None)* | `setio` (`{"id": 104030, ...}`) |
| 652 | **`104040`** | `104040..104044` (5) | **Wheel Brake Temp Status Axle 3 Wheel 7** | `—` | `0` | — *(None)* | `setio` (`{"id": 104040, ...}`) |
| 653 | **`104050`** | `104050..104054` (5) | **Wheel Brake Temp Status Axle 3 Wheel 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 104050, ...}`) |
| 654 | **`104060`** | `104060..104064` (5) | **Wheel Brake Temp Status Axle 3 Wheel 9** | `—` | `0` | — *(None)* | `setio` (`{"id": 104060, ...}`) |
| 655 | **`104070`** | `104070..104074` (5) | **Wheel Brake Temp Status Axle 3 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 104070, ...}`) |
| 656 | **`104080`** | `104080..104084` (5) | **Wheel Brake Temp Axle 1 Wheel 6** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104080, ...}`) |
| 657 | **`104090`** | `104090..104094` (5) | **Wheel Brake Temp Axle 1 Wheel 7** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104090, ...}`) |
| 658 | **`104100`** | `104100..104104` (5) | **Wheel Brake Temp Axle 1 Wheel 8** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104100, ...}`) |
| 659 | **`104110`** | `104110..104114` (5) | **Wheel Brake Temp Axle 1 Wheel 9** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104110, ...}`) |
| 660 | **`104120`** | `104120..104124` (5) | **Wheel Brake Temp Axle 1 Wheel 10** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104120, ...}`) |
| 661 | **`104130`** | `104130..104134` (5) | **Wheel Brake Temp Axle 2 Wheel 6** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104130, ...}`) |
| 662 | **`104140`** | `104140..104144` (5) | **Wheel Brake Temp Axle 2 Wheel 7** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104140, ...}`) |
| 663 | **`104150`** | `104150..104154` (5) | **Wheel Brake Temp Axle 2 Wheel 8** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104150, ...}`) |
| 664 | **`104160`** | `104160..104164` (5) | **Wheel Brake Temp Axle 2 Wheel 9** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104160, ...}`) |
| 665 | **`104170`** | `104170..104174` (5) | **Wheel Brake Temp Axle 2 Wheel 10** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104170, ...}`) |
| 666 | **`104180`** | `104180..104184` (5) | **Wheel Brake Temp Axle 3 Wheel 6** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104180, ...}`) |
| 667 | **`104190`** | `104190..104194` (5) | **Wheel Brake Temp Axle 3 Wheel 7** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104190, ...}`) |
| 668 | **`104200`** | `104200..104204` (5) | **Wheel Brake Temp Axle 3 Wheel 8** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104200, ...}`) |
| 669 | **`104210`** | `104210..104214` (5) | **Wheel Brake Temp Axle 3 Wheel 9** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104210, ...}`) |
| 670 | **`104220`** | `104220..104224` (5) | **Wheel Brake Temp Axle 3 Wheel 10** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104220, ...}`) |
| 671 | **`104230`** | `104230..104234` (5) | **Vehicle Pneumatic Supply Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 104230, ...}`) |
| 672 | **`104240`** | `104240..104244` (5) | **Air Leakage Detection Axle 1 Wheel 6** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104240, ...}`) |
| 673 | **`104250`** | `104250..104254` (5) | **Air Leakage Detection Axle 1 Wheel 7** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104250, ...}`) |
| 674 | **`104260`** | `104260..104264` (5) | **Air Leakage Detection Axle 1 Wheel 8** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104260, ...}`) |
| 675 | **`104270`** | `104270..104274` (5) | **Air Leakage Detection Axle 1 Wheel 9** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104270, ...}`) |
| 676 | **`104280`** | `104280..104284` (5) | **Air Leakage Detection Axle 1 Wheel 10** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104280, ...}`) |
| 677 | **`104290`** | `104290..104294` (5) | **Air Leakage Detection Axle 2 Wheel 6** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104290, ...}`) |
| 678 | **`104300`** | `104300..104304` (5) | **Air Leakage Detection Axle 2 Wheel 7** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104300, ...}`) |
| 679 | **`104310`** | `104310..104314` (5) | **Air Leakage Detection Axle 2 Wheel 8** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104310, ...}`) |
| 680 | **`104320`** | `104320..104324` (5) | **Air Leakage Detection Axle 2 Wheel 9** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104320, ...}`) |
| 681 | **`104330`** | `104330..104334` (5) | **Air Leakage Detection Axle 2 Wheel 10** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104330, ...}`) |
| 682 | **`104340`** | `104340..104344` (5) | **Air Leakage Detection Axle 3 Wheel 6** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104340, ...}`) |
| 683 | **`104350`** | `104350..104354` (5) | **Air Leakage Detection Axle 3 Wheel 7** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104350, ...}`) |
| 684 | **`104360`** | `104360..104364` (5) | **Air Leakage Detection Axle 3 Wheel 8** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104360, ...}`) |
| 685 | **`104370`** | `104370..104374` (5) | **Air Leakage Detection Axle 3 Wheel 9** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 104370, ...}`) |
| 686 | **`104380`** | `104380..104384` (5) | **Air Leakage Detection Axle 3 Wheel 10** | `—` | `0` | — *(None)* | `setio` (`{"id": 104380, ...}`) |
| 687 | **`104390`** | `104390..104394` (5) | **Tire Temperature Axle 1 Wheel 6** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104390, ...}`) |
| 688 | **`104400`** | `104400..104404` (5) | **Tire Temperature Axle 1 Wheel 7** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104400, ...}`) |
| 689 | **`104410`** | `104410..104414` (5) | **Tire Temperature Axle 1 Wheel 8** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104410, ...}`) |
| 690 | **`104420`** | `104420..104424` (5) | **Tire Temperature Axle 1 Wheel 9** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104420, ...}`) |
| 691 | **`104430`** | `104430..104434` (5) | **Tire Temperature Axle 1 Wheel 10** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104430, ...}`) |
| 692 | **`104440`** | `104440..104444` (5) | **Tire Temperature Axle 2 Wheel 6** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104440, ...}`) |
| 693 | **`104450`** | `104450..104454` (5) | **Tire Temperature Axle 2 Wheel 7** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104450, ...}`) |
| 694 | **`104460`** | `104460..104464` (5) | **Tire Temperature Axle 2 Wheel 8** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104460, ...}`) |
| 695 | **`104470`** | `104470..104474` (5) | **Tire Temperature Axle 2 Wheel 9** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104470, ...}`) |
| 696 | **`104480`** | `104480..104484` (5) | **Tire Temperature Axle 2 Wheel 10** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104480, ...}`) |
| 697 | **`104490`** | `104490..104494` (5) | **Tire Temperature Axle 3 Wheel 6** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104490, ...}`) |
| 698 | **`104500`** | `104500..104504` (5) | **Tire Temperature Axle 3 Wheel 7** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104500, ...}`) |
| 699 | **`104510`** | `104510..104514` (5) | **Tire Temperature Axle 3 Wheel 8** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104510, ...}`) |
| 700 | **`104520`** | `104520..104524` (5) | **Tire Temperature Axle 3 Wheel 9** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104520, ...}`) |
| 701 | **`104530`** | `104530..104534` (5) | **Tire Temperature Axle 3 Wheel 10** | `°C` | `0` | — *(None)* | `setio` (`{"id": 104530, ...}`) |
| 702 | **`104540`** | `104540..104544` (5) | **Automatic Towed Vehicle Braking Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 104540, ...}`) |
| 703 | **`104550`** | `104550..104554` (5) | **Electrical Supply of Non-Braking Systems Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 104550, ...}`) |
| 704 | **`104560`** | `104560..104564` (5) | **Spring Brake Installation Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 104560, ...}`) |
| 705 | **`104570`** | `104570..104574` (5) | **Electrical Load Proportional Function Installation Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 104570, ...}`) |
| 706 | **`104580`** | `104580..104584` (5) | **Spring Brake Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 104580, ...}`) |
| 707 | **`104590`** | `104590..104594` (5) | **Pneumatic Supply Pressure** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104590, ...}`) |
| 708 | **`104630`** | `104630..104634` (5) | **Vehicle ABS Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104630, ...}`) |
| 709 | **`104640`** | `104640..104644` (5) | **Vehicle Retarder Control Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104640, ...}`) |
| 710 | **`104650`** | `104650..104654` (5) | **Red Warning Signal Request #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104650, ...}`) |
| 711 | **`104660`** | `104660..104664` (5) | **Amber Warning Signal Request #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104660, ...}`) |
| 712 | **`104670`** | `104670..104674` (5) | **Axle Load Sum #2** | `kg` | `0` | — *(None)* | `setio` (`{"id": 104670, ...}`) |
| 713 | **`104680`** | `104680..104684` (5) | **Retarder Wheel Torque Reference #2** | `Nm` | `0` | — *(None)* | `setio` (`{"id": 104680, ...}`) |
| 714 | **`104690`** | `104690..104694` (5) | **Vehicle Service Brake Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104690, ...}`) |
| 715 | **`104700`** | `104700..104704` (5) | **Vehicle Electrical Supply Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104700, ...}`) |
| 716 | **`104710`** | `104710..104714` (5) | **Vehicle Type #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104710, ...}`) |
| 717 | **`104720`** | `104720..104724` (5) | **Axle Load Measured By Towed Vehicle #2** | `kg` | `0` | — *(None)* | `setio` (`{"id": 104720, ...}`) |
| 718 | **`104730`** | `104730..104734` (5) | **Axle Load Measured By External Scale #2** | `kg` | `0` | — *(None)* | `setio` (`{"id": 104730, ...}`) |
| 719 | **`104740`** | `104740..104744` (5) | **Axle Load Calibration Data Load Level #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104740, ...}`) |
| 720 | **`104750`** | `104750..104754` (5) | **Brake Cylinder Pressure First Axle Left Wheel #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104750, ...}`) |
| 721 | **`104760`** | `104760..104764` (5) | **Brake Cylinder Pressure First Axle Right Wheel #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104760, ...}`) |
| 722 | **`104770`** | `104770..104774` (5) | **Brake Cylinder Pressure Second Axle Left Wheel #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104770, ...}`) |
| 723 | **`104780`** | `104780..104784` (5) | **Brake Cylinder Pressure Second Axle Right Wheel #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104780, ...}`) |
| 724 | **`104790`** | `104790..104794` (5) | **Brake Cylinder Pressure Third Axle Left Wheel #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104790, ...}`) |
| 725 | **`104800`** | `104800..104804` (5) | **Brake Cylinder Pressure Third Axle Right Wheel #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 104800, ...}`) |
| 726 | **`104810`** | `104810..104814` (5) | **VIN #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104810, ...}`) |
| 727 | **`104820`** | `104820..104824` (5) | **VDC Active #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104820, ...}`) |
| 728 | **`104830`** | `104830..104834` (5) | **Lateral Acceleration #2** | `m/s^2` | `0` | — *(None)* | `setio` (`{"id": 104830, ...}`) |
| 729 | **`104840`** | `104840..104844` (5) | **Loading Ramp Approach Assistance Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104840, ...}`) |
| 730 | **`104850`** | `104850..104854` (5) | **Supply Line Braking #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104850, ...}`) |
| 731 | **`104860`** | `104860..104864` (5) | **Stop Lamps Request #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104860, ...}`) |
| 732 | **`104870`** | `104870..104874` (5) | **Braking Via Electric Control Line Support #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104870, ...}`) |
| 733 | **`104880`** | `104880..104884` (5) | **ROP System Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104880, ...}`) |
| 734 | **`104890`** | `104890..104894` (5) | **YC System Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104890, ...}`) |
| 735 | **`104900`** | `104900..104904` (5) | **Traction Help Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104900, ...}`) |
| 736 | **`104910`** | `104910..104914` (5) | **Lift Axle 1 Position Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104910, ...}`) |
| 737 | **`104920`** | `104920..104924` (5) | **Lift Axle 2 Position Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104920, ...}`) |
| 738 | **`104930`** | `104930..104934` (5) | **Steering Axle Locking Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104930, ...}`) |
| 739 | **`104940`** | `104940..104944` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104940, ...}`) |
| 740 | **`104950`** | `104950..104954` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104950, ...}`) |
| 741 | **`104960`** | `104960..104964` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104960, ...}`) |
| 742 | **`104970`** | `104970..104974` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104970, ...}`) |
| 743 | **`104980`** | `104980..104984` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104980, ...}`) |
| 744 | **`104990`** | `104990..104994` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 104990, ...}`) |
| 745 | **`105000`** | `105000..105004` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105000, ...}`) |
| 746 | **`105010`** | `105010..105014` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105010, ...}`) |
| 747 | **`105020`** | `105020..105024` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105020, ...}`) |
| 748 | **`105030`** | `105030..105034` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105030, ...}`) |
| 749 | **`105040`** | `105040..105044` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105040, ...}`) |
| 750 | **`105050`** | `105050..105054` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105050, ...}`) |
| 751 | **`105060`** | `105060..105064` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105060, ...}`) |
| 752 | **`105070`** | `105070..105074` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105070, ...}`) |
| 753 | **`105080`** | `105080..105084` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105080, ...}`) |
| 754 | **`105090`** | `105090..105094` (5) | **Wheel Tire Pressure Axle 1 Wheel 6 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105090, ...}`) |
| 755 | **`105100`** | `105100..105104` (5) | **Wheel Tire Pressure Axle 1 Wheel 7 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105100, ...}`) |
| 756 | **`105110`** | `105110..105114` (5) | **Wheel Tire Pressure Axle 1 Wheel 8 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105110, ...}`) |
| 757 | **`105120`** | `105120..105124` (5) | **Wheel Tire Pressure Axle 1 Wheel 9 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105120, ...}`) |
| 758 | **`105130`** | `105130..105134` (5) | **Wheel Tire Pressure Axle 1 Wheel 10 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105130, ...}`) |
| 759 | **`105140`** | `105140..105144` (5) | **Wheel Tire Pressure Axle 2 Wheel 6 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105140, ...}`) |
| 760 | **`105150`** | `105150..105154` (5) | **Wheel Tire Pressure Axle 2 Wheel 7 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105150, ...}`) |
| 761 | **`105160`** | `105160..105164` (5) | **Wheel Tire Pressure Axle 2 Wheel 8 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105160, ...}`) |
| 762 | **`105170`** | `105170..105174` (5) | **Wheel Tire Pressure Axle 2 Wheel 9 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105170, ...}`) |
| 763 | **`105180`** | `105180..105184` (5) | **Wheel Tire Pressure Axle 2 Wheel 10 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105180, ...}`) |
| 764 | **`105190`** | `105190..105194` (5) | **Wheel Tire Pressure Axle 3 Wheel 6 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105190, ...}`) |
| 765 | **`105200`** | `105200..105204` (5) | **Wheel Tire Pressure Axle 3 Wheel 7 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105200, ...}`) |
| 766 | **`105210`** | `105210..105214` (5) | **Wheel Tire Pressure Axle 3 Wheel 8 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105210, ...}`) |
| 767 | **`105220`** | `105220..105224` (5) | **Wheel Tire Pressure Axle 3 Wheel 9 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105220, ...}`) |
| 768 | **`105230`** | `105230..105234` (5) | **Wheel Tire Pressure Axle 3 Wheel 10 #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 105230, ...}`) |
| 769 | **`105240`** | `105240..105244` (5) | **Wheel Brake Lining Status Axle 1 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105240, ...}`) |
| 770 | **`105250`** | `105250..105254` (5) | **Wheel Brake Lining Status Axle 1 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105250, ...}`) |
| 771 | **`105260`** | `105260..105264` (5) | **Wheel Brake Lining Status Axle 1 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105260, ...}`) |
| 772 | **`105270`** | `105270..105274` (5) | **Wheel Brake Lining Status Axle 1 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105270, ...}`) |
| 773 | **`105280`** | `105280..105284` (5) | **Wheel Brake Lining Status Axle 1 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105280, ...}`) |
| 774 | **`105290`** | `105290..105294` (5) | **Wheel Brake Lining Status Axle 2 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105290, ...}`) |
| 775 | **`105300`** | `105300..105304` (5) | **Wheel Brake Lining Status Axle 2 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105300, ...}`) |
| 776 | **`105310`** | `105310..105314` (5) | **Wheel Brake Lining Status Axle 2 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105310, ...}`) |
| 777 | **`105320`** | `105320..105324` (5) | **Wheel Brake Lining Status Axle 2 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105320, ...}`) |
| 778 | **`105330`** | `105330..105334` (5) | **Wheel Brake Lining Status Axle 2 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105330, ...}`) |
| 779 | **`105340`** | `105340..105344` (5) | **Wheel Brake Lining Status Axle 3 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105340, ...}`) |
| 780 | **`105350`** | `105350..105354` (5) | **Wheel Brake Lining Status Axle 3 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105350, ...}`) |
| 781 | **`105360`** | `105360..105364` (5) | **Wheel Brake Lining Status Axle 3 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105360, ...}`) |
| 782 | **`105370`** | `105370..105374` (5) | **Wheel Brake Lining Status Axle 3 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105370, ...}`) |
| 783 | **`105380`** | `105380..105384` (5) | **Wheel Brake Lining Status Axle 3 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105380, ...}`) |
| 784 | **`105390`** | `105390..105394` (5) | **Wheel Brake Lining Axle 1 Wheel 6 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105390, ...}`) |
| 785 | **`105400`** | `105400..105404` (5) | **Wheel Brake Lining Axle 1 Wheel 7 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105400, ...}`) |
| 786 | **`105410`** | `105410..105414` (5) | **Wheel Brake Lining Axle 1 Wheel 8 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105410, ...}`) |
| 787 | **`105420`** | `105420..105424` (5) | **Wheel Brake Lining Axle 1 Wheel 9 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105420, ...}`) |
| 788 | **`105430`** | `105430..105434` (5) | **Wheel Brake Lining Axle 1 Wheel 10 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105430, ...}`) |
| 789 | **`105440`** | `105440..105444` (5) | **Wheel Brake Lining Axle 2 Wheel 6 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105440, ...}`) |
| 790 | **`105450`** | `105450..105454` (5) | **Wheel Brake Lining Axle 2 Wheel 7 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105450, ...}`) |
| 791 | **`105460`** | `105460..105464` (5) | **Wheel Brake Lining Axle 2 Wheel 8 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105460, ...}`) |
| 792 | **`105470`** | `105470..105474` (5) | **Wheel Brake Lining Axle 2 Wheel 9 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105470, ...}`) |
| 793 | **`105480`** | `105480..105484` (5) | **Wheel Brake Lining Axle 2 Wheel 10 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105480, ...}`) |
| 794 | **`105490`** | `105490..105494` (5) | **Wheel Brake Lining Axle 3 Wheel 6 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105490, ...}`) |
| 795 | **`105500`** | `105500..105504` (5) | **Wheel Brake Lining Axle 3 Wheel 7 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105500, ...}`) |
| 796 | **`105510`** | `105510..105514` (5) | **Wheel Brake Lining Axle 3 Wheel 8 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105510, ...}`) |
| 797 | **`105520`** | `105520..105524` (5) | **Wheel Brake Lining Axle 3 Wheel 9 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105520, ...}`) |
| 798 | **`105530`** | `105530..105534` (5) | **Wheel Brake Lining Axle 3 Wheel 10 #2** | `%` | `0` | — *(None)* | `setio` (`{"id": 105530, ...}`) |
| 799 | **`105540`** | `105540..105544` (5) | **Wheel Brake Temp Status Axle 1 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105540, ...}`) |
| 800 | **`105550`** | `105550..105554` (5) | **Wheel Brake Temp Status Axle 1 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105550, ...}`) |
| 801 | **`105560`** | `105560..105564` (5) | **Wheel Brake Temp Status Axle 1 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105560, ...}`) |
| 802 | **`105570`** | `105570..105574` (5) | **Wheel Brake Temp Status Axle 1 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105570, ...}`) |
| 803 | **`105580`** | `105580..105584` (5) | **Wheel Brake Temp Status Axle 1 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105580, ...}`) |
| 804 | **`105590`** | `105590..105594` (5) | **Wheel Brake Temp Status Axle 2 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105590, ...}`) |
| 805 | **`105600`** | `105600..105604` (5) | **Wheel Brake Temp Status Axle 2 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105600, ...}`) |
| 806 | **`105610`** | `105610..105614` (5) | **Wheel Brake Temp Status Axle 2 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105610, ...}`) |
| 807 | **`105620`** | `105620..105624` (5) | **Wheel Brake Temp Status Axle 2 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105620, ...}`) |
| 808 | **`105630`** | `105630..105634` (5) | **Wheel Brake Temp Status Axle 2 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105630, ...}`) |
| 809 | **`105640`** | `105640..105644` (5) | **Wheel Brake Temp Status Axle 3 Wheel 6 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105640, ...}`) |
| 810 | **`105650`** | `105650..105654` (5) | **Wheel Brake Temp Status Axle 3 Wheel 7 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105650, ...}`) |
| 811 | **`105660`** | `105660..105664` (5) | **Wheel Brake Temp Status Axle 3 Wheel 8 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105660, ...}`) |
| 812 | **`105670`** | `105670..105674` (5) | **Wheel Brake Temp Status Axle 3 Wheel 9 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105670, ...}`) |
| 813 | **`105680`** | `105680..105684` (5) | **Wheel Brake Temp Status Axle 3 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105680, ...}`) |
| 814 | **`105690`** | `105690..105694` (5) | **Wheel Brake Temp Axle 1 Wheel 6 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105690, ...}`) |
| 815 | **`105700`** | `105700..105704` (5) | **Wheel Brake Temp Axle 1 Wheel 7 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105700, ...}`) |
| 816 | **`105710`** | `105710..105714` (5) | **Wheel Brake Temp Axle 1 Wheel 8 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105710, ...}`) |
| 817 | **`105720`** | `105720..105724` (5) | **Wheel Brake Temp Axle 1 Wheel 9 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105720, ...}`) |
| 818 | **`105730`** | `105730..105734` (5) | **Wheel Brake Temp Axle 1 Wheel 10 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105730, ...}`) |
| 819 | **`105740`** | `105740..105744` (5) | **Wheel Brake Temp Axle 2 Wheel 6 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105740, ...}`) |
| 820 | **`105750`** | `105750..105754` (5) | **Wheel Brake Temp Axle 2 Wheel 7 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105750, ...}`) |
| 821 | **`105760`** | `105760..105764` (5) | **Wheel Brake Temp Axle 2 Wheel 8 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105760, ...}`) |
| 822 | **`105770`** | `105770..105774` (5) | **Wheel Brake Temp Axle 2 Wheel 9 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105770, ...}`) |
| 823 | **`105780`** | `105780..105784` (5) | **Wheel Brake Temp Axle 2 Wheel 10 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105780, ...}`) |
| 824 | **`105790`** | `105790..105794` (5) | **Wheel Brake Temp Axle 3 Wheel 6 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105790, ...}`) |
| 825 | **`105800`** | `105800..105804` (5) | **Wheel Brake Temp Axle 3 Wheel 7 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105800, ...}`) |
| 826 | **`105810`** | `105810..105814` (5) | **Wheel Brake Temp Axle 3 Wheel 8 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105810, ...}`) |
| 827 | **`105820`** | `105820..105824` (5) | **Wheel Brake Temp Axle 3 Wheel 9 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105820, ...}`) |
| 828 | **`105830`** | `105830..105834` (5) | **Wheel Brake Temp Axle 3 Wheel 10 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 105830, ...}`) |
| 829 | **`105840`** | `105840..105844` (5) | **Vehicle Pneumatic Supply Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105840, ...}`) |
| 830 | **`105850`** | `105850..105854` (5) | **Air Leakage Detection Axle 1 Wheel 6 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105850, ...}`) |
| 831 | **`105860`** | `105860..105864` (5) | **Air Leakage Detection Axle 1 Wheel 7 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105860, ...}`) |
| 832 | **`105870`** | `105870..105874` (5) | **Air Leakage Detection Axle 1 Wheel 8 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105870, ...}`) |
| 833 | **`105880`** | `105880..105884` (5) | **Air Leakage Detection Axle 1 Wheel 9 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105880, ...}`) |
| 834 | **`105890`** | `105890..105894` (5) | **Air Leakage Detection Axle 1 Wheel 10 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105890, ...}`) |
| 835 | **`105900`** | `105900..105904` (5) | **Air Leakage Detection Axle 2 Wheel 6 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105900, ...}`) |
| 836 | **`105910`** | `105910..105914` (5) | **Air Leakage Detection Axle 2 Wheel 7 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105910, ...}`) |
| 837 | **`105920`** | `105920..105924` (5) | **Air Leakage Detection Axle 2 Wheel 8 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105920, ...}`) |
| 838 | **`105930`** | `105930..105934` (5) | **Air Leakage Detection Axle 2 Wheel 9 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105930, ...}`) |
| 839 | **`105940`** | `105940..105944` (5) | **Air Leakage Detection Axle 2 Wheel 10 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105940, ...}`) |
| 840 | **`105950`** | `105950..105954` (5) | **Air Leakage Detection Axle 3 Wheel 6 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105950, ...}`) |
| 841 | **`105960`** | `105960..105964` (5) | **Air Leakage Detection Axle 3 Wheel 7 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105960, ...}`) |
| 842 | **`105970`** | `105970..105974` (5) | **Air Leakage Detection Axle 3 Wheel 8 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105970, ...}`) |
| 843 | **`105980`** | `105980..105984` (5) | **Air Leakage Detection Axle 3 Wheel 9 #2** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 105980, ...}`) |
| 844 | **`105990`** | `105990..105994` (5) | **Air Leakage Detection Axle 3 Wheel 10 #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 105990, ...}`) |
| 845 | **`106000`** | `106000..106004` (5) | **Tire Temperature Axle 1 Wheel 6 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106000, ...}`) |
| 846 | **`106010`** | `106010..106014` (5) | **Tire Temperature Axle 1 Wheel 7 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106010, ...}`) |
| 847 | **`106020`** | `106020..106024` (5) | **Tire Temperature Axle 1 Wheel 8 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106020, ...}`) |
| 848 | **`106030`** | `106030..106034` (5) | **Tire Temperature Axle 1 Wheel 9 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106030, ...}`) |
| 849 | **`106040`** | `106040..106044` (5) | **Tire Temperature Axle 1 Wheel 10 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106040, ...}`) |
| 850 | **`106050`** | `106050..106054` (5) | **Tire Temperature Axle 2 Wheel 6 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106050, ...}`) |
| 851 | **`106060`** | `106060..106064` (5) | **Tire Temperature Axle 2 Wheel 7 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106060, ...}`) |
| 852 | **`106070`** | `106070..106074` (5) | **Tire Temperature Axle 2 Wheel 8 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106070, ...}`) |
| 853 | **`106080`** | `106080..106084` (5) | **Tire Temperature Axle 2 Wheel 9 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106080, ...}`) |
| 854 | **`106090`** | `106090..106094` (5) | **Tire Temperature Axle 2 Wheel 10 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106090, ...}`) |
| 855 | **`106100`** | `106100..106104` (5) | **Tire Temperature Axle 3 Wheel 6 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106100, ...}`) |
| 856 | **`106110`** | `106110..106114` (5) | **Tire Temperature Axle 3 Wheel 7 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106110, ...}`) |
| 857 | **`106120`** | `106120..106124` (5) | **Tire Temperature Axle 3 Wheel 8 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106120, ...}`) |
| 858 | **`106130`** | `106130..106134` (5) | **Tire Temperature Axle 3 Wheel 9 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106130, ...}`) |
| 859 | **`106140`** | `106140..106144` (5) | **Tire Temperature Axle 3 Wheel 10 #2** | `°C` | `0` | — *(None)* | `setio` (`{"id": 106140, ...}`) |
| 860 | **`106150`** | `106150..106154` (5) | **Automatic Towed Vehicle Braking Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 106150, ...}`) |
| 861 | **`106160`** | `106160..106164` (5) | **Electrical Supply of Non N=2-Braking Systems Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 106160, ...}`) |
| 862 | **`106170`** | `106170..106174` (5) | **Spring Brake Installation Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 106170, ...}`) |
| 863 | **`106180`** | `106180..106184` (5) | **Electrical Load Proportional Function Installation Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 106180, ...}`) |
| 864 | **`106190`** | `106190..106194` (5) | **Spring Brake Status #2** | `—` | `0` | — *(None)* | `setio` (`{"id": 106190, ...}`) |
| 865 | **`106200`** | `106200..106204` (5) | **Pneumatic Supply Pressure #2** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106200, ...}`) |
| 866 | **`106240`** | `106240..106244` (5) | **Vehicle ABS Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106240, ...}`) |
| 867 | **`106250`** | `106250..106254` (5) | **Vehicle Retarder Control Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106250, ...}`) |
| 868 | **`106260`** | `106260..106264` (5) | **Red Warning Signal Request #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106260, ...}`) |
| 869 | **`106270`** | `106270..106274` (5) | **Amber Warning Signal Request #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106270, ...}`) |
| 870 | **`106280`** | `106280..106284` (5) | **Axle Load Sum #3** | `kg` | `0` | — *(None)* | `setio` (`{"id": 106280, ...}`) |
| 871 | **`106290`** | `106290..106294` (5) | **Retarder Wheel Torque Reference #3** | `Nm` | `0` | — *(None)* | `setio` (`{"id": 106290, ...}`) |
| 872 | **`106300`** | `106300..106304` (5) | **Vehicle Service Brake Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106300, ...}`) |
| 873 | **`106310`** | `106310..106314` (5) | **Vehicle Electrical Supply Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106310, ...}`) |
| 874 | **`106320`** | `106320..106324` (5) | **Vehicle Type #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106320, ...}`) |
| 875 | **`106330`** | `106330..106334` (5) | **Axle Load Measured By Towed Vehicle #3** | `kg` | `0` | — *(None)* | `setio` (`{"id": 106330, ...}`) |
| 876 | **`106340`** | `106340..106344` (5) | **Axle Load Measured By External Scale #3** | `kg` | `0` | — *(None)* | `setio` (`{"id": 106340, ...}`) |
| 877 | **`106350`** | `106350..106354` (5) | **Axle Load Calibration Data Load Level #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106350, ...}`) |
| 878 | **`106360`** | `106360..106364` (5) | **Brake Cylinder Pressure First Axle Left Wheel #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106360, ...}`) |
| 879 | **`106370`** | `106370..106374` (5) | **Brake Cylinder Pressure First Axle Right Wheel #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106370, ...}`) |
| 880 | **`106380`** | `106380..106384` (5) | **Brake Cylinder Pressure Second Axle Left Wheel #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106380, ...}`) |
| 881 | **`106390`** | `106390..106394` (5) | **Brake Cylinder Pressure Second Axle Right Wheel #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106390, ...}`) |
| 882 | **`106400`** | `106400..106404` (5) | **Brake Cylinder Pressure Third Axle Left Wheel #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106400, ...}`) |
| 883 | **`106410`** | `106410..106414` (5) | **Brake Cylinder Pressure Third Axle Right Wheel #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106410, ...}`) |
| 884 | **`106420`** | `106420..106424` (5) | **VIN #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106420, ...}`) |
| 885 | **`106430`** | `106430..106434` (5) | **VDC Active #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106430, ...}`) |
| 886 | **`106440`** | `106440..106444` (5) | **Lateral Acceleration #3** | `m/s^2` | `0` | — *(None)* | `setio` (`{"id": 106440, ...}`) |
| 887 | **`106450`** | `106450..106454` (5) | **Loading Ramp Approach Assistance Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106450, ...}`) |
| 888 | **`106460`** | `106460..106464` (5) | **Supply Line Braking #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106460, ...}`) |
| 889 | **`106470`** | `106470..106474` (5) | **Stop Lamps Request #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106470, ...}`) |
| 890 | **`106480`** | `106480..106484` (5) | **Braking Via Electric Control Line Support #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106480, ...}`) |
| 891 | **`106490`** | `106490..106494` (5) | **ROP System Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106490, ...}`) |
| 892 | **`106500`** | `106500..106504` (5) | **YC System Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106500, ...}`) |
| 893 | **`106510`** | `106510..106514` (5) | **Traction Help Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106510, ...}`) |
| 894 | **`106520`** | `106520..106524` (5) | **Lift Axle 1 Position Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106520, ...}`) |
| 895 | **`106530`** | `106530..106534` (5) | **Lift Axle 2 Position Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106530, ...}`) |
| 896 | **`106540`** | `106540..106544` (5) | **Steering Axle Locking Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106540, ...}`) |
| 897 | **`106550`** | `106550..106554` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106550, ...}`) |
| 898 | **`106560`** | `106560..106564` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106560, ...}`) |
| 899 | **`106570`** | `106570..106574` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106570, ...}`) |
| 900 | **`106580`** | `106580..106584` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106580, ...}`) |
| 901 | **`106590`** | `106590..106594` (5) | **Wheel Tire Pressure Status Axle 1 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106590, ...}`) |
| 902 | **`106600`** | `106600..106604` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106600, ...}`) |
| 903 | **`106610`** | `106610..106614` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106610, ...}`) |
| 904 | **`106620`** | `106620..106624` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106620, ...}`) |
| 905 | **`106630`** | `106630..106634` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106630, ...}`) |
| 906 | **`106640`** | `106640..106644` (5) | **Wheel Tire Pressure Status Axle 2 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106640, ...}`) |
| 907 | **`106650`** | `106650..106654` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106650, ...}`) |
| 908 | **`106660`** | `106660..106664` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106660, ...}`) |
| 909 | **`106670`** | `106670..106674` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106670, ...}`) |
| 910 | **`106680`** | `106680..106684` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106680, ...}`) |
| 911 | **`106690`** | `106690..106694` (5) | **Wheel Tire Pressure Status Axle 3 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106690, ...}`) |
| 912 | **`106700`** | `106700..106704` (5) | **Wheel Tire Pressure Axle 1 Wheel 6 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106700, ...}`) |
| 913 | **`106710`** | `106710..106714` (5) | **Wheel Tire Pressure Axle 1 Wheel 7 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106710, ...}`) |
| 914 | **`106720`** | `106720..106724` (5) | **Wheel Tire Pressure Axle 1 Wheel 8 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106720, ...}`) |
| 915 | **`106730`** | `106730..106734` (5) | **Wheel Tire Pressure Axle 1 Wheel 9 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106730, ...}`) |
| 916 | **`106740`** | `106740..106744` (5) | **Wheel Tire Pressure Axle 1 Wheel 10 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106740, ...}`) |
| 917 | **`106750`** | `106750..106754` (5) | **Wheel Tire Pressure Axle 2 Wheel 6 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106750, ...}`) |
| 918 | **`106760`** | `106760..106764` (5) | **Wheel Tire Pressure Axle 2 Wheel 7 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106760, ...}`) |
| 919 | **`106770`** | `106770..106774` (5) | **Wheel Tire Pressure Axle 2 Wheel 8 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106770, ...}`) |
| 920 | **`106780`** | `106780..106784` (5) | **Wheel Tire Pressure Axle 2 Wheel 9 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106780, ...}`) |
| 921 | **`106790`** | `106790..106794` (5) | **Wheel Tire Pressure Axle 2 Wheel 10 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106790, ...}`) |
| 922 | **`106800`** | `106800..106804` (5) | **Wheel Tire Pressure Axle 3 Wheel 6 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106800, ...}`) |
| 923 | **`106810`** | `106810..106814` (5) | **Wheel Tire Pressure Axle 3 Wheel 7 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106810, ...}`) |
| 924 | **`106820`** | `106820..106824` (5) | **Wheel Tire Pressure Axle 3 Wheel 8 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106820, ...}`) |
| 925 | **`106830`** | `106830..106834` (5) | **Wheel Tire Pressure Axle 3 Wheel 9 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106830, ...}`) |
| 926 | **`106840`** | `106840..106844` (5) | **Wheel Tire Pressure Axle 3 Wheel 10 #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 106840, ...}`) |
| 927 | **`106850`** | `106850..106854` (5) | **Wheel Brake Lining Status Axle 1 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106850, ...}`) |
| 928 | **`106860`** | `106860..106864` (5) | **Wheel Brake Lining Status Axle 1 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106860, ...}`) |
| 929 | **`106870`** | `106870..106874` (5) | **Wheel Brake Lining Status Axle 1 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106870, ...}`) |
| 930 | **`106880`** | `106880..106884` (5) | **Wheel Brake Lining Status Axle 1 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106880, ...}`) |
| 931 | **`106890`** | `106890..106894` (5) | **Wheel Brake Lining Status Axle 1 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106890, ...}`) |
| 932 | **`106900`** | `106900..106904` (5) | **Wheel Brake Lining Status Axle 2 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106900, ...}`) |
| 933 | **`106910`** | `106910..106914` (5) | **Wheel Brake Lining Status Axle 2 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106910, ...}`) |
| 934 | **`106920`** | `106920..106924` (5) | **Wheel Brake Lining Status Axle 2 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106920, ...}`) |
| 935 | **`106930`** | `106930..106934` (5) | **Wheel Brake Lining Status Axle 2 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106930, ...}`) |
| 936 | **`106940`** | `106940..106944` (5) | **Wheel Brake Lining Status Axle 2 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106940, ...}`) |
| 937 | **`106950`** | `106950..106954` (5) | **Wheel Brake Lining Status Axle 3 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106950, ...}`) |
| 938 | **`106960`** | `106960..106964` (5) | **Wheel Brake Lining Status Axle 3 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106960, ...}`) |
| 939 | **`106970`** | `106970..106974` (5) | **Wheel Brake Lining Status Axle 3 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106970, ...}`) |
| 940 | **`106980`** | `106980..106984` (5) | **Wheel Brake Lining Status Axle 3 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106980, ...}`) |
| 941 | **`106990`** | `106990..106994` (5) | **Wheel Brake Lining Status Axle 3 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 106990, ...}`) |
| 942 | **`107000`** | `107000..107004` (5) | **Wheel Brake Lining Axle 1 Wheel 6 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107000, ...}`) |
| 943 | **`107010`** | `107010..107014` (5) | **Wheel Brake Lining Axle 1 Wheel 7 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107010, ...}`) |
| 944 | **`107020`** | `107020..107024` (5) | **Wheel Brake Lining Axle 1 Wheel 8 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107020, ...}`) |
| 945 | **`107030`** | `107030..107034` (5) | **Wheel Brake Lining Axle 1 Wheel 9 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107030, ...}`) |
| 946 | **`107040`** | `107040..107044` (5) | **Wheel Brake Lining Axle 1 Wheel 10 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107040, ...}`) |
| 947 | **`107050`** | `107050..107054` (5) | **Wheel Brake Lining Axle 2 Wheel 6 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107050, ...}`) |
| 948 | **`107060`** | `107060..107064` (5) | **Wheel Brake Lining Axle 2 Wheel 7 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107060, ...}`) |
| 949 | **`107070`** | `107070..107074` (5) | **Wheel Brake Lining Axle 2 Wheel 8 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107070, ...}`) |
| 950 | **`107080`** | `107080..107084` (5) | **Wheel Brake Lining Axle 2 Wheel 9 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107080, ...}`) |
| 951 | **`107090`** | `107090..107094` (5) | **Wheel Brake Lining Axle 2 Wheel 10 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107090, ...}`) |
| 952 | **`107100`** | `107100..107104` (5) | **Wheel Brake Lining Axle 3 Wheel 6 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107100, ...}`) |
| 953 | **`107110`** | `107110..107114` (5) | **Wheel Brake Lining Axle 3 Wheel 7 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107110, ...}`) |
| 954 | **`107120`** | `107120..107124` (5) | **Wheel Brake Lining Axle 3 Wheel 8 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107120, ...}`) |
| 955 | **`107130`** | `107130..107134` (5) | **Wheel Brake Lining Axle 3 Wheel 9 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107130, ...}`) |
| 956 | **`107140`** | `107140..107144` (5) | **Wheel Brake Lining Axle 3 Wheel 10 #3** | `%` | `0` | — *(None)* | `setio` (`{"id": 107140, ...}`) |
| 957 | **`107150`** | `107150..107154` (5) | **Wheel Brake Temp Status Axle 1 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107150, ...}`) |
| 958 | **`107160`** | `107160..107164` (5) | **Wheel Brake Temp Status Axle 1 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107160, ...}`) |
| 959 | **`107170`** | `107170..107174` (5) | **Wheel Brake Temp Status Axle 1 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107170, ...}`) |
| 960 | **`107180`** | `107180..107184` (5) | **Wheel Brake Temp Status Axle 1 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107180, ...}`) |
| 961 | **`107190`** | `107190..107194` (5) | **Wheel Brake Temp Status Axle 1 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107190, ...}`) |
| 962 | **`107200`** | `107200..107204` (5) | **Wheel Brake Temp Status Axle 2 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107200, ...}`) |
| 963 | **`107210`** | `107210..107214` (5) | **Wheel Brake Temp Status Axle 2 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107210, ...}`) |
| 964 | **`107220`** | `107220..107224` (5) | **Wheel Brake Temp Status Axle 2 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107220, ...}`) |
| 965 | **`107230`** | `107230..107234` (5) | **Wheel Brake Temp Status Axle 2 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107230, ...}`) |
| 966 | **`107240`** | `107240..107244` (5) | **Wheel Brake Temp Status Axle 2 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107240, ...}`) |
| 967 | **`107250`** | `107250..107254` (5) | **Wheel Brake Temp Status Axle 3 Wheel 6 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107250, ...}`) |
| 968 | **`107260`** | `107260..107264` (5) | **Wheel Brake Temp Status Axle 3 Wheel 7 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107260, ...}`) |
| 969 | **`107270`** | `107270..107274` (5) | **Wheel Brake Temp Status Axle 3 Wheel 8 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107270, ...}`) |
| 970 | **`107280`** | `107280..107284` (5) | **Wheel Brake Temp Status Axle 3 Wheel 9 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107280, ...}`) |
| 971 | **`107290`** | `107290..107294` (5) | **Wheel Brake Temp Status Axle 3 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107290, ...}`) |
| 972 | **`107300`** | `107300..107304` (5) | **Wheel Brake Temp Axle 1 Wheel 6 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107300, ...}`) |
| 973 | **`107310`** | `107310..107314` (5) | **Wheel Brake Temp Axle 1 Wheel 7 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107310, ...}`) |
| 974 | **`107320`** | `107320..107324` (5) | **Wheel Brake Temp Axle 1 Wheel 8 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107320, ...}`) |
| 975 | **`107330`** | `107330..107334` (5) | **Wheel Brake Temp Axle 1 Wheel 9 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107330, ...}`) |
| 976 | **`107340`** | `107340..107344` (5) | **Wheel Brake Temp Axle 1 Wheel 10 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107340, ...}`) |
| 977 | **`107350`** | `107350..107354` (5) | **Wheel Brake Temp Axle 2 Wheel 6 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107350, ...}`) |
| 978 | **`107360`** | `107360..107364` (5) | **Wheel Brake Temp Axle 2 Wheel 7 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107360, ...}`) |
| 979 | **`107370`** | `107370..107374` (5) | **Wheel Brake Temp Axle 2 Wheel 8 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107370, ...}`) |
| 980 | **`107380`** | `107380..107384` (5) | **Wheel Brake Temp Axle 2 Wheel 9 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107380, ...}`) |
| 981 | **`107390`** | `107390..107394` (5) | **Wheel Brake Temp Axle 2 Wheel 10 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107390, ...}`) |
| 982 | **`107400`** | `107400..107404` (5) | **Wheel Brake Temp Axle 3 Wheel 6 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107400, ...}`) |
| 983 | **`107410`** | `107410..107414` (5) | **Wheel Brake Temp Axle 3 Wheel 7 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107410, ...}`) |
| 984 | **`107420`** | `107420..107424` (5) | **Wheel Brake Temp Axle 3 Wheel 8 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107420, ...}`) |
| 985 | **`107430`** | `107430..107434` (5) | **Wheel Brake Temp Axle 3 Wheel 9 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107430, ...}`) |
| 986 | **`107440`** | `107440..107444` (5) | **Wheel Brake Temp Axle 3 Wheel 10 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107440, ...}`) |
| 987 | **`107450`** | `107450..107454` (5) | **Vehicle Pneumatic Supply Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107450, ...}`) |
| 988 | **`107460`** | `107460..107464` (5) | **Air Leakage Detection Axle 1 Wheel 6 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107460, ...}`) |
| 989 | **`107470`** | `107470..107474` (5) | **Air Leakage Detection Axle 1 Wheel 7 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107470, ...}`) |
| 990 | **`107480`** | `107480..107484` (5) | **Air Leakage Detection Axle 1 Wheel 8 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107480, ...}`) |
| 991 | **`107490`** | `107490..107494` (5) | **Air Leakage Detection Axle 1 Wheel 9 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107490, ...}`) |
| 992 | **`107500`** | `107500..107504` (5) | **Air Leakage Detection Axle 1 Wheel 10 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107500, ...}`) |
| 993 | **`107510`** | `107510..107514` (5) | **Air Leakage Detection Axle 2 Wheel 6 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107510, ...}`) |
| 994 | **`107520`** | `107520..107524` (5) | **Air Leakage Detection Axle 2 Wheel 7 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107520, ...}`) |
| 995 | **`107530`** | `107530..107534` (5) | **Air Leakage Detection Axle 2 Wheel 8 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107530, ...}`) |
| 996 | **`107540`** | `107540..107544` (5) | **Air Leakage Detection Axle 2 Wheel 9 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107540, ...}`) |
| 997 | **`107550`** | `107550..107554` (5) | **Air Leakage Detection Axle 2 Wheel 10 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107550, ...}`) |
| 998 | **`107560`** | `107560..107564` (5) | **Air Leakage Detection Axle 3 Wheel 6 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107560, ...}`) |
| 999 | **`107570`** | `107570..107574` (5) | **Air Leakage Detection Axle 3 Wheel 7 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107570, ...}`) |
| 1000 | **`107580`** | `107580..107584` (5) | **Air Leakage Detection Axle 3 Wheel 8 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107580, ...}`) |
| 1001 | **`107590`** | `107590..107594` (5) | **Air Leakage Detection Axle 3 Wheel 9 #3** | `Pa/s` | `0` | — *(None)* | `setio` (`{"id": 107590, ...}`) |
| 1002 | **`107600`** | `107600..107604` (5) | **Air Leakage Detection Axle 3 Wheel 10 #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107600, ...}`) |
| 1003 | **`107610`** | `107610..107614` (5) | **Tire Temperature Axle 1 Wheel 6 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107610, ...}`) |
| 1004 | **`107620`** | `107620..107624` (5) | **Tire Temperature Axle 1 Wheel 7 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107620, ...}`) |
| 1005 | **`107630`** | `107630..107634` (5) | **Tire Temperature Axle 1 Wheel 8 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107630, ...}`) |
| 1006 | **`107640`** | `107640..107644` (5) | **Tire Temperature Axle 1 Wheel 9 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107640, ...}`) |
| 1007 | **`107650`** | `107650..107654` (5) | **Tire Temperature Axle 1 Wheel 10 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107650, ...}`) |
| 1008 | **`107660`** | `107660..107664` (5) | **Tire Temperature Axle 2 Wheel 6 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107660, ...}`) |
| 1009 | **`107670`** | `107670..107674` (5) | **Tire Temperature Axle 2 Wheel 7 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107670, ...}`) |
| 1010 | **`107680`** | `107680..107684` (5) | **Tire Temperature Axle 2 Wheel 8 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107680, ...}`) |
| 1011 | **`107690`** | `107690..107694` (5) | **Tire Temperature Axle 2 Wheel 9 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107690, ...}`) |
| 1012 | **`107700`** | `107700..107704` (5) | **Tire Temperature Axle 2 Wheel 10 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107700, ...}`) |
| 1013 | **`107710`** | `107710..107714` (5) | **Tire Temperature Axle 3 Wheel 6 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107710, ...}`) |
| 1014 | **`107720`** | `107720..107724` (5) | **Tire Temperature Axle 3 Wheel 7 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107720, ...}`) |
| 1015 | **`107730`** | `107730..107734` (5) | **Tire Temperature Axle 3 Wheel 8 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107730, ...}`) |
| 1016 | **`107740`** | `107740..107744` (5) | **Tire Temperature Axle 3 Wheel 9 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107740, ...}`) |
| 1017 | **`107750`** | `107750..107754` (5) | **Tire Temperature Axle 3 Wheel 10 #3** | `°C` | `0` | — *(None)* | `setio` (`{"id": 107750, ...}`) |
| 1018 | **`107760`** | `107760..107764` (5) | **Automatic Towed Vehicle Braking Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107760, ...}`) |
| 1019 | **`107770`** | `107770..107774` (5) | **Electrical Supply of Non N=3-Braking Systems Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 107770, ...}`) |
| 1020 | **`107780`** | `107780..107784` (5) | **Spring Brake Installation Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107780, ...}`) |
| 1021 | **`107790`** | `107790..107794` (5) | **Electrical Load Proportional Function Installation Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107790, ...}`) |
| 1022 | **`107800`** | `107800..107804` (5) | **Spring Brake Status #3** | `—` | `0` | — *(None)* | `setio` (`{"id": 107800, ...}`) |
| 1023 | **`107810`** | `107810..107814` (5) | **Pneumatic Supply Pressure #3** | `kPa` | `0` | — *(None)* | `setio` (`{"id": 107810, ...}`) |
| 1024 | **`107840`** | `107840..107844` (5) | **Braking System Wheel Based Vehicle Speed** | `km/h` | `0` | — *(None)* | `setio` (`{"id": 107840, ...}`) |
| 1025 | **`108000`** | `108000..108004` (5) | **Tire Pressures Combined Status, Axle 1 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108000, ...}`) |
| 1026 | **`108010`** | `108010..108014` (5) | **Brake Lining Combined Status, Axle 1 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108010, ...}`) |
| 1027 | **`108020`** | `108020..108024` (5) | **Brake Temperature Combined Status, Axle 1 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108020, ...}`) |
| 1028 | **`108030`** | `108030..108034` (5) | **Tire Pressures Combined Status, Axle 2 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108030, ...}`) |
| 1029 | **`108040`** | `108040..108044` (5) | **Brake Lining Combined Status, Axle 2 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108040, ...}`) |
| 1030 | **`108050`** | `108050..108054` (5) | **Brake Temperature Combined Status, Axle 2 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108050, ...}`) |
| 1031 | **`108060`** | `108060..108064` (5) | **Tire Pressures Combined Status, Axle 3 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108060, ...}`) |
| 1032 | **`108070`** | `108070..108074` (5) | **Brake Lining Combined Status, Axle 3 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108070, ...}`) |
| 1033 | **`108080`** | `108080..108084` (5) | **Brake Temperature Combined Status, Axle 3 Towed 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 108080, ...}`) |
| 1034 | **`108090`** | `108090..108094` (5) | **Tire Pressures Combined Status, Axle 1 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108090, ...}`) |
| 1035 | **`108100`** | `108100..108104` (5) | **Brake Lining Combined Status, Axle 1 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108100, ...}`) |
| 1036 | **`108110`** | `108110..108114` (5) | **Brake Temperature Combined Status, Axle 1 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108110, ...}`) |
| 1037 | **`108120`** | `108120..108124` (5) | **Tire Pressures Combined Status, Axle 2 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108120, ...}`) |
| 1038 | **`108130`** | `108130..108134` (5) | **Brake Lining Combined Status, Axle 2 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108130, ...}`) |
| 1039 | **`108140`** | `108140..108144` (5) | **Brake Temperature Combined Status, Axle 2 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108140, ...}`) |
| 1040 | **`108150`** | `108150..108154` (5) | **Tire Pressures Combined Status, Axle 3 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108150, ...}`) |
| 1041 | **`108160`** | `108160..108164` (5) | **Brake Lining Combined Status, Axle 3 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108160, ...}`) |
| 1042 | **`108170`** | `108170..108174` (5) | **Brake Temperature Combined Status, Axle 3 Towed 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 108170, ...}`) |
| 1043 | **`108180`** | `108180..108184` (5) | **Tire Pressures Combined Status, Axle 1 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108180, ...}`) |
| 1044 | **`108190`** | `108190..108194` (5) | **Brake Lining Combined Status, Axle 1 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108190, ...}`) |
| 1045 | **`108200`** | `108200..108204` (5) | **Brake Temperature Combined Status, Axle 1 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108200, ...}`) |
| 1046 | **`108210`** | `108210..108214` (5) | **Tire Pressures Combined Status, Axle 2 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108210, ...}`) |
| 1047 | **`108220`** | `108220..108224` (5) | **Brake Lining Combined Status, Axle 2 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108220, ...}`) |
| 1048 | **`108230`** | `108230..108234` (5) | **Brake Temperature Combined Status, Axle 2 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108230, ...}`) |
| 1049 | **`108240`** | `108240..108244` (5) | **Tire Pressures Combined Status, Axle 3 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108240, ...}`) |
| 1050 | **`108250`** | `108250..108254` (5) | **Brake Lining Combined Status, Axle 3 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108250, ...}`) |
| 1051 | **`108260`** | `108260..108264` (5) | **Brake Temperature Combined Status, Axle 3 Towed 3** | `—` | `0` | — *(None)* | `setio` (`{"id": 108260, ...}`) |
| 1052 | **`150010`** | `150010..150015` (6) | **Ground based speed** | `(m/s)/1000` | `0` | — *(None)* | `setio` (`{"id": 150010, ...}`) |
| 1053 | **`150020`** | `150020..150025` (6) | **Ground based distance** | `m/1000` | `0` | — *(None)* | `setio` (`{"id": 150020, ...}`) |
| 1054 | **`150030`** | `150030..150034` (5) | **Ground based direction** | `—` | `0` | — *(None)* | `setio` (`{"id": 150030, ...}`) |
| 1055 | **`150040`** | `150040..150045` (6) | **Wheel based speed** | `(m/s)/1000` | `0` | — *(None)* | `setio` (`{"id": 150040, ...}`) |
| 1056 | **`150050`** | `150050..150055` (6) | **Wheel based distance** | `m/1000` | `0` | — *(None)* | `setio` (`{"id": 150050, ...}`) |
| 1057 | **`150060`** | `150060..150065` (6) | **Maximum time of tractor power** | `min` | `0` | — *(None)* | `setio` (`{"id": 150060, ...}`) |
| 1058 | **`150070`** | `150070..150074` (5) | **Wheel based direction** | `—` | `0` | — *(None)* | `setio` (`{"id": 150070, ...}`) |
| 1059 | **`150080`** | `150080..150084` (5) | **Key switch state** | `—` | `0` | — *(None)* | `setio` (`{"id": 150080, ...}`) |
| 1060 | **`150090`** | `150090..150094` (5) | **Start/stop state** | `—` | `0` | — *(None)* | `setio` (`{"id": 150090, ...}`) |
| 1061 | **`150100`** | `150100..150104` (5) | **Maintain ECU power** | `—` | `0` | — *(None)* | `setio` (`{"id": 150100, ...}`) |
| 1062 | **`150110`** | `150110..150114` (5) | **Maintain actuator power** | `—` | `0` | — *(None)* | `setio` (`{"id": 150110, ...}`) |
| 1063 | **`150120`** | `150120..150124` (5) | **Implement transport state** | `—` | `0` | — *(None)* | `setio` (`{"id": 150120, ...}`) |
| 1064 | **`150130`** | `150130..150134` (5) | **Implement park state** | `—` | `0` | — *(None)* | `setio` (`{"id": 150130, ...}`) |
| 1065 | **`150140`** | `150140..150144` (5) | **Implement work state** | `—` | `0` | — *(None)* | `setio` (`{"id": 150140, ...}`) |
| 1066 | **`150150`** | `150150..150155` (6) | **Front hitch position** | `%` | `0` | — *(None)* | `setio` (`{"id": 150150, ...}`) |
| 1067 | **`150160`** | `150160..150164` (5) | **Front hitch in-work indication** | `—` | `0` | — *(None)* | `setio` (`{"id": 150160, ...}`) |
| 1068 | **`150170`** | `150170..150175` (6) | **Front nominal lower link force** | `%` | `0` | — *(None)* | `setio` (`{"id": 150170, ...}`) |
| 1069 | **`150180`** | `150180..150185` (6) | **Front draft** | `N` | `0` | — *(None)* | `setio` (`{"id": 150180, ...}`) |
| 1070 | **`150190`** | `150190..150195` (6) | **Rear hitch position** | `%` | `0` | — *(None)* | `setio` (`{"id": 150190, ...}`) |
| 1071 | **`150200`** | `150200..150204` (5) | **Rear hitch in-work indication** | `—` | `0` | — *(None)* | `setio` (`{"id": 150200, ...}`) |
| 1072 | **`150210`** | `150210..150215` (6) | **Rear nominal lower link force** | `%` | `0` | — *(None)* | `setio` (`{"id": 150210, ...}`) |
| 1073 | **`150220`** | `150220..150225` (6) | **Rear draft** | `N` | `0` | — *(None)* | `setio` (`{"id": 150220, ...}`) |
| 1074 | **`150230`** | `150230..150235` (6) | **Front PTO output shaft speed** | `(1/min)/1000` | `0` | — *(None)* | `setio` (`{"id": 150230, ...}`) |
| 1075 | **`150240`** | `150240..150245` (6) | **Front PTO shaft speed point** | `(1/min)/1000` | `0` | — *(None)* | `setio` (`{"id": 150240, ...}`) |
| 1076 | **`150250`** | `150250..150254` (5) | **Front PTO engagement** | `—` | `0` | — *(None)* | `setio` (`{"id": 150250, ...}`) |
| 1077 | **`150260`** | `150260..150264` (5) | **Front PTO mode** | `—` | `0` | — *(None)* | `setio` (`{"id": 150260, ...}`) |
| 1078 | **`150270`** | `150270..150274` (5) | **Front PTO economy mode** | `—` | `0` | — *(None)* | `setio` (`{"id": 150270, ...}`) |
| 1079 | **`150280`** | `150280..150285` (6) | **Rear PTO output shaft speed** | `(1/min)/1000` | `0` | — *(None)* | `setio` (`{"id": 150280, ...}`) |
| 1080 | **`150290`** | `150290..150295` (6) | **Rear PTO shaft speed point** | `(1/min)/1000` | `0` | — *(None)* | `setio` (`{"id": 150290, ...}`) |
| 1081 | **`150300`** | `150300..150304` (5) | **Rear PTO engagement** | `—` | `0` | — *(None)* | `setio` (`{"id": 150300, ...}`) |
| 1082 | **`150310`** | `150310..150314` (5) | **Rear PTO mode** | `—` | `0` | — *(None)* | `setio` (`{"id": 150310, ...}`) |
| 1083 | **`150320`** | `150320..150324` (5) | **Rear PTO economy mode** | `—` | `0` | — *(None)* | `setio` (`{"id": 150320, ...}`) |
| 1084 | **`150330`** | `150330..150335` (6) | **Front hitch position command** | `%` | `0` | — *(None)* | `setio` (`{"id": 150330, ...}`) |
| 1085 | **`150340`** | `150340..150345` (6) | **Rear hitch position command** | `%` | `0` | — *(None)* | `setio` (`{"id": 150340, ...}`) |
| 1086 | **`150350`** | `150350..150355` (6) | **Front PTO speed shaft point command** | `(1/min)/1000` | `0` | — *(None)* | `setio` (`{"id": 150350, ...}`) |
| 1087 | **`150360`** | `150360..150365` (6) | **Rear PTO speed shaft point command** | `(1/min)/1000` | `0` | — *(None)* | `setio` (`{"id": 150360, ...}`) |
| 1088 | **`150370`** | `150370..150374` (5) | **Front PTO engagement command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 150370, ...}`) |
| 1089 | **`150380`** | `150380..150384` (5) | **Rear PTO engagement command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 150380, ...}`) |
| 1090 | **`150390`** | `150390..150394` (5) | **Front PTO mode command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 150390, ...}`) |
| 1091 | **`150400`** | `150400..150404` (5) | **Rear PTO mode command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 150400, ...}`) |
| 1092 | **`150410`** | `150410..150414` (5) | **Front PTO economy mode command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 150410, ...}`) |
| 1093 | **`150420`** | `150420..150424` (5) | **Rear PTO economy mode command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 150420, ...}`) |
| 1094 | **`150430`** | `150430..150434` (3) | **Auxiliary valve 0 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150430, ...}`) |
| 1095 | **`150440`** | `150440..150444` (3) | **Auxiliary valve 1 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150440, ...}`) |
| 1096 | **`150450`** | `150450..150454` (3) | **Auxiliary valve 2 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150450, ...}`) |
| 1097 | **`150460`** | `150460..150464` (3) | **Auxiliary valve 3 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150460, ...}`) |
| 1098 | **`150470`** | `150470..150474` (3) | **Auxiliary valve 4 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150470, ...}`) |
| 1099 | **`150480`** | `150480..150484` (3) | **Auxiliary valve 5 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150480, ...}`) |
| 1100 | **`150490`** | `150490..150494` (3) | **Auxiliary valve 6 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150490, ...}`) |
| 1101 | **`150500`** | `150500..150504` (3) | **Auxiliary valve 7 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150500, ...}`) |
| 1102 | **`150510`** | `150510..150514` (3) | **Auxiliary valve 8 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150510, ...}`) |
| 1103 | **`150520`** | `150520..150524` (3) | **Auxiliary valve 9 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150520, ...}`) |
| 1104 | **`150530`** | `150530..150534` (3) | **Auxiliary valve 10 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150530, ...}`) |
| 1105 | **`150540`** | `150540..150544` (3) | **Auxiliary valve 11 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150540, ...}`) |
| 1106 | **`150550`** | `150550..150554` (3) | **Auxiliary valve 12 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150550, ...}`) |
| 1107 | **`150560`** | `150560..150564` (3) | **Auxiliary valve 13 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150560, ...}`) |
| 1108 | **`150570`** | `150570..150574` (3) | **Auxiliary valve 14 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150570, ...}`) |
| 1109 | **`150580`** | `150580..150584` (3) | **Auxiliary valve 15 estimated flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150580, ...}`) |
| 1110 | **`150590`** | `150590..150594` (3) | **Auxiliary valve 0 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150590, ...}`) |
| 1111 | **`150600`** | `150600..150604` (3) | **Auxiliary valve 1 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150600, ...}`) |
| 1112 | **`150610`** | `150610..150614` (3) | **Auxiliary valve 2 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150610, ...}`) |
| 1113 | **`150620`** | `150620..150624` (3) | **Auxiliary valve 3 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150620, ...}`) |
| 1114 | **`150630`** | `150630..150634` (3) | **Auxiliary valve 4 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150630, ...}`) |
| 1115 | **`150640`** | `150640..150644` (3) | **Auxiliary valve 5 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150640, ...}`) |
| 1116 | **`150650`** | `150650..150654` (3) | **Auxiliary valve 6 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150650, ...}`) |
| 1117 | **`150660`** | `150660..150664` (3) | **Auxiliary valve 7 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150660, ...}`) |
| 1118 | **`150670`** | `150670..150674` (3) | **Auxiliary valve 8 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150670, ...}`) |
| 1119 | **`150680`** | `150680..150684` (3) | **Auxiliary valve 9 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150680, ...}`) |
| 1120 | **`150690`** | `150690..150694` (3) | **Auxiliary valve 10 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150690, ...}`) |
| 1121 | **`150700`** | `150700..150704` (3) | **Auxiliary valve 11 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150700, ...}`) |
| 1122 | **`150710`** | `150710..150714` (3) | **Auxiliary valve 12 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150710, ...}`) |
| 1123 | **`150720`** | `150720..150724` (3) | **Auxiliary valve 13 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150720, ...}`) |
| 1124 | **`150730`** | `150730..150734` (3) | **Auxiliary valve 14 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150730, ...}`) |
| 1125 | **`150740`** | `150740..150744` (3) | **Auxiliary valve 15 measured flow** | `—` | `0` | — *(None)* | `setio` (`{"id": 150740, ...}`) |
| 1126 | **`150750`** | `150750..150754` (3) | **Auxiliary valve 0 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150750, ...}`) |
| 1127 | **`150760`** | `150760..150764` (3) | **Auxiliary valve 1 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150760, ...}`) |
| 1128 | **`150770`** | `150770..150774` (3) | **Auxiliary valve 2 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150770, ...}`) |
| 1129 | **`150780`** | `150780..150784` (3) | **Auxiliary valve 3 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150780, ...}`) |
| 1130 | **`150790`** | `150790..150794` (3) | **Auxiliary valve 4 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150790, ...}`) |
| 1131 | **`150800`** | `150800..150804` (3) | **Auxiliary valve 5 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150800, ...}`) |
| 1132 | **`150810`** | `150810..150814` (3) | **Auxiliary valve 6 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150810, ...}`) |
| 1133 | **`150820`** | `150820..150824` (3) | **Auxiliary valve 7 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150820, ...}`) |
| 1134 | **`150830`** | `150830..150834` (3) | **Auxiliary valve 8 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150830, ...}`) |
| 1135 | **`150840`** | `150840..150844` (3) | **Auxiliary valve 9 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150840, ...}`) |
| 1136 | **`150850`** | `150850..150854` (3) | **Auxiliary valve 10 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150850, ...}`) |
| 1137 | **`150860`** | `150860..150864` (3) | **Auxiliary valve 11 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150860, ...}`) |
| 1138 | **`150870`** | `150870..150874` (3) | **Auxiliary valve 12 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150870, ...}`) |
| 1139 | **`150880`** | `150880..150884` (3) | **Auxiliary valve 13 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150880, ...}`) |
| 1140 | **`150890`** | `150890..150894` (3) | **Auxiliary valve 14 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150890, ...}`) |
| 1141 | **`150900`** | `150900..150904` (3) | **Auxiliary valve 15 command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150900, ...}`) |
| 1142 | **`150910`** | `150910..150914` (5) | **Tractor high-beam head lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150910, ...}`) |
| 1143 | **`150920`** | `150920..150924` (5) | **Tractor low-beam head lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150920, ...}`) |
| 1144 | **`150930`** | `150930..150934` (5) | **Tractor alternate head lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150930, ...}`) |
| 1145 | **`150940`** | `150940..150944` (5) | **Daytime running lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150940, ...}`) |
| 1146 | **`150950`** | `150950..150954` (5) | **Left-turn signal lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150950, ...}`) |
| 1147 | **`150960`** | `150960..150964` (5) | **Right-turn signal lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150960, ...}`) |
| 1148 | **`150970`** | `150970..150974` (5) | **Beacon lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150970, ...}`) |
| 1149 | **`150980`** | `150980..150984` (5) | **Front fog lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150980, ...}`) |
| 1150 | **`150990`** | `150990..150994` (5) | **Left stop lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 150990, ...}`) |
| 1151 | **`151000`** | `151000..151004` (5) | **Right stop lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151000, ...}`) |
| 1152 | **`151010`** | `151010..151014` (5) | **Centre stop lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151010, ...}`) |
| 1153 | **`151020`** | `151020..151024` (5) | **Back up light and alarm horn command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151020, ...}`) |
| 1154 | **`151030`** | `151030..151034` (5) | **Tractor marker lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151030, ...}`) |
| 1155 | **`151040`** | `151040..151044` (5) | **Implement marker lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151040, ...}`) |
| 1156 | **`151050`** | `151050..151054` (5) | **Tractor clearance lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151050, ...}`) |
| 1157 | **`151060`** | `151060..151064` (5) | **Implement clearance lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151060, ...}`) |
| 1158 | **`151070`** | `151070..151074` (5) | **Rear high mounted work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151070, ...}`) |
| 1159 | **`151080`** | `151080..151084` (5) | **Rear low mounted work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151080, ...}`) |
| 1160 | **`151090`** | `151090..151094` (5) | **Underside work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151090, ...}`) |
| 1161 | **`151100`** | `151100..151104` (5) | **Rear fog lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151100, ...}`) |
| 1162 | **`151110`** | `151110..151114` (5) | **Front high-mounted work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151110, ...}`) |
| 1163 | **`151120`** | `151120..151124` (5) | **Front low-mounted work light command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151120, ...}`) |
| 1164 | **`151130`** | `151130..151134` (5) | **Side high-mounted work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151130, ...}`) |
| 1165 | **`151140`** | `151140..151144` (5) | **Side low mounted work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151140, ...}`) |
| 1166 | **`151150`** | `151150..151154` (5) | **Implement left forward work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151150, ...}`) |
| 1167 | **`151160`** | `151160..151164` (5) | **Implement right forward work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151160, ...}`) |
| 1168 | **`151170`** | `151170..151174` (5) | **Implement OEM option 1 light command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151170, ...}`) |
| 1169 | **`151180`** | `151180..151184` (5) | **Implement OEM option 2 light command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151180, ...}`) |
| 1170 | **`151190`** | `151190..151194` (5) | **Implement rear work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151190, ...}`) |
| 1171 | **`151200`** | `151200..151204` (5) | **Implement left work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151200, ...}`) |
| 1172 | **`151210`** | `151210..151214` (5) | **Implement right work lights command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151210, ...}`) |
| 1173 | **`151220`** | `151220..151224` (5) | **Lighting data message request** | `—` | `0` | — *(None)* | `setio` (`{"id": 151220, ...}`) |
| 1174 | **`151230`** | `151230..151234` (5) | **Tractor high-beam head lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151230, ...}`) |
| 1175 | **`151240`** | `151240..151244` (5) | **Tractor low-beam head lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151240, ...}`) |
| 1176 | **`151250`** | `151250..151254` (5) | **Tractor alternate head lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151250, ...}`) |
| 1177 | **`151260`** | `151260..151264` (5) | **Daytime running lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151260, ...}`) |
| 1178 | **`151270`** | `151270..151274` (5) | **Left-turn signal lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151270, ...}`) |
| 1179 | **`151280`** | `151280..151284` (5) | **Right-turn signal lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151280, ...}`) |
| 1180 | **`151290`** | `151290..151294` (5) | **Beacon lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151290, ...}`) |
| 1181 | **`151300`** | `151300..151304` (5) | **Front fog lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151300, ...}`) |
| 1182 | **`151310`** | `151310..151314` (5) | **Left stop lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151310, ...}`) |
| 1183 | **`151320`** | `151320..151324` (5) | **Right stop lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151320, ...}`) |
| 1184 | **`151330`** | `151330..151334` (5) | **Centre stop lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151330, ...}`) |
| 1185 | **`151340`** | `151340..151344` (5) | **Back up light and alarm horn** | `—` | `0` | — *(None)* | `setio` (`{"id": 151340, ...}`) |
| 1186 | **`151350`** | `151350..151354` (5) | **Tractor marker lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151350, ...}`) |
| 1187 | **`151360`** | `151360..151364` (5) | **Implement marker lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151360, ...}`) |
| 1188 | **`151370`** | `151370..151374` (5) | **Tractor clearance lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151370, ...}`) |
| 1189 | **`151380`** | `151380..151384` (5) | **Implement clearance lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151380, ...}`) |
| 1190 | **`151390`** | `151390..151394` (5) | **Rear high mounted work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151390, ...}`) |
| 1191 | **`151400`** | `151400..151404` (5) | **Rear low mounted work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151400, ...}`) |
| 1192 | **`151410`** | `151410..151414` (5) | **Underside work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151410, ...}`) |
| 1193 | **`151420`** | `151420..151424` (5) | **Rear fog lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151420, ...}`) |
| 1194 | **`151430`** | `151430..151434` (5) | **Front high-mounted work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151430, ...}`) |
| 1195 | **`151440`** | `151440..151444` (5) | **Front low-mounted work light** | `—` | `0` | — *(None)* | `setio` (`{"id": 151440, ...}`) |
| 1196 | **`151450`** | `151450..151454` (5) | **Side high-mounted work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151450, ...}`) |
| 1197 | **`151460`** | `151460..151464` (5) | **Side low mounted work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151460, ...}`) |
| 1198 | **`151470`** | `151470..151474` (5) | **Implement left forward work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151470, ...}`) |
| 1199 | **`151480`** | `151480..151484` (5) | **Implement right forward work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151480, ...}`) |
| 1200 | **`151490`** | `151490..151494` (5) | **Implement OEM option 1 light** | `—` | `0` | — *(None)* | `setio` (`{"id": 151490, ...}`) |
| 1201 | **`151500`** | `151500..151504` (5) | **Implement OEM option 2 light** | `—` | `0` | — *(None)* | `setio` (`{"id": 151500, ...}`) |
| 1202 | **`151510`** | `151510..151514` (5) | **Implement rear work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151510, ...}`) |
| 1203 | **`151520`** | `151520..151524` (5) | **Implement rear work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151520, ...}`) |
| 1204 | **`151530`** | `151530..151534` (5) | **Implement right work lights** | `—` | `0` | — *(None)* | `setio` (`{"id": 151530, ...}`) |
| 1205 | **`151540`** | `151540..151544` (5) | **Background illumination level** | `%` | `0` | — *(None)* | `setio` (`{"id": 151540, ...}`) |
| 1206 | **`151550`** | `151550..151554` (5) | **Control Command 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 151550, ...}`) |
| 1207 | **`151560`** | `151560..151564` (5) | **Command Action 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 151560, ...}`) |
| 1208 | **`151570`** | `151570..151574` (5) | **Control Command 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 151570, ...}`) |
| 1209 | **`151580`** | `151580..151584` (5) | **Command Action 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 151580, ...}`) |
| 1210 | **`151590`** | `151590..151595` (6) | **Control Value 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 151590, ...}`) |
| 1211 | **`151600`** | `151600..151604` (5) | **Control Limits 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 151600, ...}`) |
| 1212 | **`151610`** | `151610..151615` (6) | **Control Value 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 151610, ...}`) |
| 1213 | **`151620`** | `151620..151624` (5) | **Control Limits 2** | `—` | `0` | — *(None)* | `setio` (`{"id": 151620, ...}`) |
| 1214 | **`151630`** | `151630..151635` (6) | **Curvature Command** | `m-1` | `0` | — *(None)* | `setio` (`{"id": 151630, ...}`) |
| 1215 | **`151640`** | `151640..151644` (5) | **Curvature Command Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 151640, ...}`) |
| 1216 | **`151650`** | `151650..151655` (6) | **Machine selected speed set point command** | `(m/s)/1000` | `0` | — *(None)* | `setio` (`{"id": 151650, ...}`) |
| 1217 | **`151660`** | `151660..151665` (6) | **Machine selected speed setpoint limit** | `(m/s)/1000` | `0` | — *(None)* | `setio` (`{"id": 151660, ...}`) |
| 1218 | **`151670`** | `151670..151674` (5) | **Machine selected direction command** | `—` | `0` | — *(None)* | `setio` (`{"id": 151670, ...}`) |
| 1219 | **`151680`** | `151680..151684` (5) | **Drive strategy priority 1 request** | `—` | `0` | — *(None)* | `setio` (`{"id": 151680, ...}`) |
| 1220 | **`151690`** | `151690..151694` (5) | **Drive strategy priority 2 request** | `—` | `0` | — *(None)* | `setio` (`{"id": 151690, ...}`) |
| 1221 | **`151700`** | `151700..151704` (5) | **Drive strategy priority 3 request** | `—` | `0` | — *(None)* | `setio` (`{"id": 151700, ...}`) |
| 1222 | **`151710`** | `151710..151714` (5) | **Drive strategy priority 4 request** | `—` | `0` | — *(None)* | `setio` (`{"id": 151710, ...}`) |
| 1223 | **`151720`** | `151720..151724` (5) | **Restore operator drive strategy setting request** | `—` | `0` | — *(None)* | `setio` (`{"id": 151720, ...}`) |
| 1224 | **`180000`** | `180000..180004` (5) | **Device Serial Number** | `—` | `0` | — *(None)* | `setio` (`{"id": 180000, ...}`) |
| 1225 | **`180010`** | `180010..180014` (2) | **Device Version** | `—` | `0` | — *(None)* | `setio` (`{"id": 180010, ...}`) |
| 1226 | **`180020`** | `180020..180024` (2) | **Datetime** | `—` | `0` | — *(None)* | `setio` (`{"id": 180020, ...}`) |
| 1227 | **`180030`** | `180030..180034` (5) | **Sensor 1 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180030, ...}`) |
| 1228 | **`180040`** | `180040..180044` (2) | **Sensor 1 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180040, ...}`) |
| 1229 | **`180050`** | `180050..180054` (5) | **Sensor 2 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180050, ...}`) |
| 1230 | **`180060`** | `180060..180064` (2) | **Sensor 2 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180060, ...}`) |
| 1231 | **`180070`** | `180070..180074` (5) | **Sensor 3 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180070, ...}`) |
| 1232 | **`180080`** | `180080..180084` (2) | **Sensor 3 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180080, ...}`) |
| 1233 | **`180090`** | `180090..180094` (5) | **Sensor 4 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180090, ...}`) |
| 1234 | **`180100`** | `180100..180104` (2) | **Sensor 4 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180100, ...}`) |
| 1235 | **`180110`** | `180110..180114` (5) | **Sensor 5 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180110, ...}`) |
| 1236 | **`180120`** | `180120..180124` (2) | **Sensor 5 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180120, ...}`) |
| 1237 | **`180130`** | `180130..180134` (5) | **Sensor 6 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180130, ...}`) |
| 1238 | **`180140`** | `180140..180144` (2) | **Sensor 6 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180140, ...}`) |
| 1239 | **`180150`** | `180150..180154` (5) | **Sensor 7 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180150, ...}`) |
| 1240 | **`180160`** | `180160..180164` (2) | **Sensor 7 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180160, ...}`) |
| 1241 | **`180170`** | `180170..180174` (5) | **Sensor 8 Value** | `—` | `0` | — *(None)* | `setio` (`{"id": 180170, ...}`) |
| 1242 | **`180180`** | `180180..180184` (2) | **Sensor 8 Unit** | `—` | `0` | — *(None)* | `setio` (`{"id": 180180, ...}`) |
| 1243 | **`180190`** | `180190..180194` (5) | **Device Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180190, ...}`) |
| 1244 | **`180200`** | `180200..180204` (2) | **Vehicle Plate** | `—` | `0` | — *(None)* | `setio` (`{"id": 180200, ...}`) |
| 1245 | **`180210`** | `180210..180214` (5) | **Thermograph Battery Voltage** | `mV` | `0` | — *(None)* | `setio` (`{"id": 180210, ...}`) |
| 1246 | **`180220`** | `180220..180224` (2) | **Frigo Machine Type** | `—` | `0` | — *(None)* | `setio` (`{"id": 180220, ...}`) |
| 1247 | **`180230`** | `180230..180234` (5) | **Frigo Overall and Engine Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180230, ...}`) |
| 1248 | **`180240`** | `180240..180244` (3) | **Frigo Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180240, ...}`) |
| 1249 | **`180250`** | `180250..180254` (3) | **Frigo Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180250, ...}`) |
| 1250 | **`180260`** | `180260..180264` (5) | **Frigo Engine Hours** | `hours` | `0` | — *(None)* | `setio` (`{"id": 180260, ...}`) |
| 1251 | **`180270`** | `180270..180274` (5) | **Frigo Standby Hours** | `hours` | `0` | — *(None)* | `setio` (`{"id": 180270, ...}`) |
| 1252 | **`180280`** | `180280..180284` (5) | **Frigo Switch On Hours** | `hours` | `0` | — *(None)* | `setio` (`{"id": 180280, ...}`) |
| 1253 | **`180290`** | `180290..180294` (3) | **Frigo Active Alarms 1 to 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 180290, ...}`) |
| 1254 | **`180300`** | `180300..180304` (3) | **Frigo Active Alarms 5 to 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 180300, ...}`) |
| 1255 | **`180310`** | `180310..180314` (3) | **Frigo Active Alarms 9 to 12** | `—` | `0` | — *(None)* | `setio` (`{"id": 180310, ...}`) |
| 1256 | **`180320`** | `180320..180324` (3) | **Frigo Active Alarms 13 to 16** | `—` | `0` | — *(None)* | `setio` (`{"id": 180320, ...}`) |
| 1257 | **`180330`** | `180330..180334` (5) | **Frigo Comp. 1 Set Point** | `—` | `0` | — *(None)* | `setio` (`{"id": 180330, ...}`) |
| 1258 | **`180340`** | `180340..180344` (5) | **Frigo Comp. 1 Supply** | `—` | `0` | — *(None)* | `setio` (`{"id": 180340, ...}`) |
| 1259 | **`180350`** | `180350..180354` (5) | **Frigo Comp. 1 Return** | `—` | `0` | — *(None)* | `setio` (`{"id": 180350, ...}`) |
| 1260 | **`180360`** | `180360..180364` (5) | **Frigo Comp. 1 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180360, ...}`) |
| 1261 | **`180370`** | `180370..180374` (5) | **Frigo Comp. 2 Set Point** | `—` | `0` | — *(None)* | `setio` (`{"id": 180370, ...}`) |
| 1262 | **`180380`** | `180380..180384` (5) | **Frigo Comp. 2 Supply** | `—` | `0` | — *(None)* | `setio` (`{"id": 180380, ...}`) |
| 1263 | **`180390`** | `180390..180394` (5) | **Frigo Comp. 2 Return** | `—` | `0` | — *(None)* | `setio` (`{"id": 180390, ...}`) |
| 1264 | **`180400`** | `180400..180404` (5) | **Frigo Comp. 2 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180400, ...}`) |
| 1265 | **`180410`** | `180410..180414` (5) | **Frigo Comp. 3 Set Point** | `—` | `0` | — *(None)* | `setio` (`{"id": 180410, ...}`) |
| 1266 | **`180420`** | `180420..180424` (5) | **Frigo Comp. 3 Supply** | `—` | `0` | — *(None)* | `setio` (`{"id": 180420, ...}`) |
| 1267 | **`180430`** | `180430..180434` (5) | **Frigo Comp. 3 Return** | `—` | `0` | — *(None)* | `setio` (`{"id": 180430, ...}`) |
| 1268 | **`180440`** | `180440..180444` (5) | **Frigo Comp. 3 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180440, ...}`) |
| 1269 | **`180450`** | `180450..180454` (2) | **EBS Type** | `—` | `0` | — *(None)* | `setio` (`{"id": 180450, ...}`) |
| 1270 | **`180460`** | `180460..180464` (5) | **EBS Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180460, ...}`) |
| 1271 | **`180470`** | `180470..180474` (3) | **EBS Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180470, ...}`) |
| 1272 | **`180480`** | `180480..180484` (3) | **EBS Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180480, ...}`) |
| 1273 | **`180490`** | `180490..180494` (5) | **EBS Wheel Speed** | `km/h` | `0` | — *(None)* | `setio` (`{"id": 180490, ...}`) |
| 1274 | **`180500`** | `180500..180504` (5) | **EBS Odometer** | `km` | `0` | — *(None)* | `setio` (`{"id": 180500, ...}`) |
| 1275 | **`180510`** | `180510..180514` (5) | **EBS Weight Load** | `10*t` | `0` | — *(None)* | `setio` (`{"id": 180510, ...}`) |
| 1276 | **`180520`** | `180520..180524` (5) | **EBS Pneumatic Supply** | `10*Bar` | `0` | — *(None)* | `setio` (`{"id": 180520, ...}`) |
| 1277 | **`180530`** | `180530..180534` (3) | **EBS Truck VIN** | `—` | `0` | — *(None)* | `setio` (`{"id": 180530, ...}`) |
| 1278 | **`180540`** | `180540..180544` (3) | **EBS Active Alarms 1 to 4** | `—` | `0` | — *(None)* | `setio` (`{"id": 180540, ...}`) |
| 1279 | **`180550`** | `180550..180554` (3) | **EBS Active Alarms 5 to 8** | `—` | `0` | — *(None)* | `setio` (`{"id": 180550, ...}`) |
| 1280 | **`180560`** | `180560..180564` (3) | **EBS Active Alarms 9 to 12** | `—` | `0` | — *(None)* | `setio` (`{"id": 180560, ...}`) |
| 1281 | **`180570`** | `180570..180574` (3) | **EBS Active Alarms 13 to 16** | `—` | `0` | — *(None)* | `setio` (`{"id": 180570, ...}`) |
| 1282 | **`180580`** | `180580..180584` (3) | **EBS Security Status 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180580, ...}`) |
| 1283 | **`180590`** | `180590..180594` (3) | **EBS Security Status 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180590, ...}`) |
| 1284 | **`180600`** | `180600..180604` (3) | **EBS TPMS Status 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180600, ...}`) |
| 1285 | **`180610`** | `180610..180614` (3) | **EBS TPMS Status 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180610, ...}`) |
| 1286 | **`180620`** | `180620..180624` (5) | **EBS Tyre 1 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180620, ...}`) |
| 1287 | **`180630`** | `180630..180634` (5) | **EBS Tyre 1 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180630, ...}`) |
| 1288 | **`180640`** | `180640..180644` (5) | **EBS Tyre 1 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 180640, ...}`) |
| 1289 | **`180650`** | `180650..180654` (5) | **EBS Tyre 1 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180650, ...}`) |
| 1290 | **`180660`** | `180660..180664` (3) | **EBS Tyre 1 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180660, ...}`) |
| 1291 | **`180670`** | `180670..180674` (3) | **EBS Tyre 1 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180670, ...}`) |
| 1292 | **`180680`** | `180680..180684` (5) | **EBS Tyre 2 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180680, ...}`) |
| 1293 | **`180690`** | `180690..180694` (5) | **EBS Tyre 2 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180690, ...}`) |
| 1294 | **`180700`** | `180700..180704` (5) | **EBS Tyre 2 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 180700, ...}`) |
| 1295 | **`180710`** | `180710..180714` (5) | **EBS Tyre 2 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180710, ...}`) |
| 1296 | **`180720`** | `180720..180724` (3) | **EBS Tyre 2 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180720, ...}`) |
| 1297 | **`180730`** | `180730..180734` (3) | **EBS Tyre 2 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180730, ...}`) |
| 1298 | **`180740`** | `180740..180744` (5) | **EBS Tyre 3 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180740, ...}`) |
| 1299 | **`180750`** | `180750..180754` (5) | **EBS Tyre 3 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180750, ...}`) |
| 1300 | **`180760`** | `180760..180764` (5) | **EBS Tyre 3 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 180760, ...}`) |
| 1301 | **`180770`** | `180770..180774` (5) | **EBS Tyre 3 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180770, ...}`) |
| 1302 | **`180780`** | `180780..180784` (3) | **EBS Tyre 3 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180780, ...}`) |
| 1303 | **`180790`** | `180790..180794` (3) | **EBS Tyre 3 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180790, ...}`) |
| 1304 | **`180800`** | `180800..180804` (5) | **EBS Tyre 4 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180800, ...}`) |
| 1305 | **`180810`** | `180810..180814` (5) | **EBS Tyre 4 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180810, ...}`) |
| 1306 | **`180820`** | `180820..180824` (5) | **EBS Tyre 4 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 180820, ...}`) |
| 1307 | **`180830`** | `180830..180834` (5) | **EBS Tyre 4 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180830, ...}`) |
| 1308 | **`180840`** | `180840..180844` (3) | **EBS Tyre 4 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180840, ...}`) |
| 1309 | **`180850`** | `180850..180854` (3) | **EBS Tyre 4 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180850, ...}`) |
| 1310 | **`180860`** | `180860..180864` (5) | **EBS Tyre 5 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180860, ...}`) |
| 1311 | **`180870`** | `180870..180874` (5) | **EBS Tyre 5 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180870, ...}`) |
| 1312 | **`180880`** | `180880..180884` (5) | **EBS Tyre 5 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 180880, ...}`) |
| 1313 | **`180890`** | `180890..180894` (5) | **EBS Tyre 5 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180890, ...}`) |
| 1314 | **`180900`** | `180900..180904` (3) | **EBS Tyre 5 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180900, ...}`) |
| 1315 | **`180910`** | `180910..180914` (3) | **EBS Tyre 5 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180910, ...}`) |
| 1316 | **`180920`** | `180920..180924` (5) | **EBS Tyre 6 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180920, ...}`) |
| 1317 | **`180930`** | `180930..180934` (5) | **EBS Tyre 6 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180930, ...}`) |
| 1318 | **`180940`** | `180940..180944` (5) | **EBS Tyre 6 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 180940, ...}`) |
| 1319 | **`180950`** | `180950..180954` (5) | **EBS Tyre 6 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 180950, ...}`) |
| 1320 | **`180960`** | `180960..180964` (3) | **EBS Tyre 6 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 180960, ...}`) |
| 1321 | **`180970`** | `180970..180974` (3) | **EBS Tyre 6 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 180970, ...}`) |
| 1322 | **`180980`** | `180980..180984` (5) | **EBS Tyre 7 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 180980, ...}`) |
| 1323 | **`180990`** | `180990..180994` (5) | **EBS Tyre 7 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 180990, ...}`) |
| 1324 | **`181000`** | `181000..181004` (5) | **EBS Tyre 7 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 181000, ...}`) |
| 1325 | **`181010`** | `181010..181014` (5) | **EBS Tyre 7 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 181010, ...}`) |
| 1326 | **`181020`** | `181020..181024` (3) | **EBS Tyre 7 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 181020, ...}`) |
| 1327 | **`181030`** | `181030..181034` (3) | **EBS Tyre 7 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 181030, ...}`) |
| 1328 | **`181040`** | `181040..181044` (5) | **EBS Tyre 8 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 181040, ...}`) |
| 1329 | **`181050`** | `181050..181054` (5) | **EBS Tyre 8 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 181050, ...}`) |
| 1330 | **`181060`** | `181060..181064` (5) | **EBS Tyre 8 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 181060, ...}`) |
| 1331 | **`181070`** | `181070..181074` (5) | **EBS Tyre 8 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 181070, ...}`) |
| 1332 | **`181080`** | `181080..181084` (3) | **EBS Tyre 8 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 181080, ...}`) |
| 1333 | **`181090`** | `181090..181094` (3) | **EBS Tyre 8 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 181090, ...}`) |
| 1334 | **`181100`** | `181100..181104` (5) | **EBS Tyre 9 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 181100, ...}`) |
| 1335 | **`181110`** | `181110..181114` (5) | **EBS Tyre 9 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 181110, ...}`) |
| 1336 | **`181120`** | `181120..181124` (5) | **EBS Tyre 9 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 181120, ...}`) |
| 1337 | **`181130`** | `181130..181134` (5) | **EBS Tyre 9 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 181130, ...}`) |
| 1338 | **`181140`** | `181140..181144` (3) | **EBS Tyre 9 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 181140, ...}`) |
| 1339 | **`181150`** | `181150..181154` (3) | **EBS Tyre 9 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 181150, ...}`) |
| 1340 | **`181160`** | `181160..181164` (5) | **EBS Tyre 10 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 181160, ...}`) |
| 1341 | **`181170`** | `181170..181174` (5) | **EBS Tyre 10 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 181170, ...}`) |
| 1342 | **`181180`** | `181180..181184` (5) | **EBS Tyre 10 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 181180, ...}`) |
| 1343 | **`181190`** | `181190..181194` (5) | **EBS Tyre 10 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 181190, ...}`) |
| 1344 | **`181200`** | `181200..181204` (3) | **EBS Tyre 10 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 181200, ...}`) |
| 1345 | **`181210`** | `181210..181214` (3) | **EBS Tyre 10 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 181210, ...}`) |
| 1346 | **`181220`** | `181220..181224` (5) | **EBS Tyre 11 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 181220, ...}`) |
| 1347 | **`181230`** | `181230..181234` (5) | **EBS Tyre 11 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 181230, ...}`) |
| 1348 | **`181240`** | `181240..181244` (5) | **EBS Tyre 11 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 181240, ...}`) |
| 1349 | **`181250`** | `181250..181254` (5) | **EBS Tyre 11 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 181250, ...}`) |
| 1350 | **`181260`** | `181260..181264` (3) | **EBS Tyre 11 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 181260, ...}`) |
| 1351 | **`181270`** | `181270..181274` (3) | **EBS Tyre 11 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 181270, ...}`) |
| 1352 | **`181280`** | `181280..181284` (5) | **EBS Tyre 12 Position** | `—` | `0` | — *(None)* | `setio` (`{"id": 181280, ...}`) |
| 1353 | **`181290`** | `181290..181294` (5) | **EBS Tyre 12 Pressure** | `—` | `0` | — *(None)* | `setio` (`{"id": 181290, ...}`) |
| 1354 | **`181300`** | `181300..181304` (5) | **EBS Tyre 12 Temperature** | `—` | `0` | — *(None)* | `setio` (`{"id": 181300, ...}`) |
| 1355 | **`181310`** | `181310..181314` (5) | **EBS Tyre 12 Status** | `—` | `0` | — *(None)* | `setio` (`{"id": 181310, ...}`) |
| 1356 | **`181320`** | `181320..181324` (3) | **EBS Tyre 12 Additional Data 0** | `—` | `0` | — *(None)* | `setio` (`{"id": 181320, ...}`) |
| 1357 | **`181330`** | `181330..181334` (3) | **EBS Tyre 12 Additional Data 1** | `—` | `0` | — *(None)* | `setio` (`{"id": 181330, ...}`) |
