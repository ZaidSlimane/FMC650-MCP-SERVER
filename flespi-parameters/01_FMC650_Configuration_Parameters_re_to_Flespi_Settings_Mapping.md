---
title: "FMC650 Configuration Parameters (re/) to Official Flespi Settings & Commands Mapping"
device: "FMC650"
firmware: "03.01.01.Rev.15 (ConfigurationVersion 4.43.1.0, SpecId 1)"
official_flespi_source: "https://flespi.com/devices/teltonika-fmc650"
re_schema_source: "fmc650-reverse-engineered/re/fmx65_03.01.01.Rev.15_schema.json"
captured: "2026-11-05"
---

# FMC650 Configuration Parameters (`re/`) to Official Flespi Device Settings & Commands Mapping

This document maps the **Teltonika FMC650 Configuration Parameters** extracted in [`fmc650-reverse-engineered/re/fmx65_03.01.01.Rev.15_schema.json`](./re/fmx65_03.01.01.Rev.15_schema.json) (`11,688` in-cfg `ParameterId`s across `13,966` total schema IDs) to the **Official Flespi Device Settings (`69` settings) and Commands (`10` commands)** documented at [`https://flespi.com/devices/teltonika-fmc650`](https://flespi.com/devices/teltonika-fmc650).

> [!CAUTION]
> **Two Non-Negotiable Architectural Rules**:
> 1. **Never confuse Telemetry Parameters with Configuration Parameters**:
>    - **Configuration Parameters (`ParameterId` / `PID` and `IoId` in `re/`)** exist in `.cfg` files (`C:\@cfg\settings.set`) and `setparam`/`getparam`/`setio` commands. They configure how the tracker behaves.
>    - **Telemetry Parameters (`AVL ID` in `Data_Sending_Parameters_ID/`)** are the runtime sensor/bus values transmitted inside Codec 8 / Codec 8 Extended packets and decoded by Flespi into **Flespi Message Parameters**.
>    - **82 identical integer IDs exist in both spaces with completely unrelated meanings** (see Section 1.1 below). For example, `100` in `.cfg` (`PID 100`) is `Movement Source`, whereas `100` in a telemetry packet (`AVL ID 100`) is `Axle weight 12` (`can.axle.weight.12`).
> 2. **Never assume a manufacturer Configuration Parameter maps directly to a Flespi Setting**:
>    - Out of **11,688 in-cfg `ParameterId`s** in `re/fmx65_03.01.01.Rev.15_schema.json`, Flespi's 69 Device Settings only cover **~240 in-cfg `ParameterId`s** (plus 16 camera settings from sibling hardware branches where `in_cfg: false`, and 14 action/status pseudo-settings that do not map to any `.cfg` `ParameterId` at all!).
>    - The remaining **>11,400 in-cfg `ParameterId`s** have **no dedicated Flespi setting** and must be read/written via Flespi's official `getparam`, `setparam`, or `setio` commands.

---

## 1. Architectural Guardrails & Proof of Non-Equivalence

### 1.1 Documented Table of 82 Exact Integer Collisions (`re/` Configuration `ParameterId` vs Telemetry `AVL ID`)

The table below lists 82 integer IDs documented as simultaneously appearing as an `in_cfg: true` **Configuration `ParameterId`** in the [FMC650 Rev. 15 schema](../fmc650-reverse-engineered/re/fmx65_03.01.01.Rev.15_schema.json) and as a **Telemetry `AVL ID`** in the [Teltonika Data Sending Parameter catalog](../teltonika-docs/Data_Sending_Parameters_ID/README.md). Confusing these two namespaces corrupts device configuration or misinterprets telemetry.

> **Graph audit update (2026-11-09):** Comparing the checked-in graph's `ConfigParameter.raw_schema.in_cfg=true` nodes with its manufacturer-sourced `AvlTelemetryElement` nodes yields **125** exact integer overlaps. The table below documents 82 of them; the following 43 additional IDs are present in those source records but are not yet individually described in this hand-maintained table: `1002`, `10150`, `106`, `105`, `107`, `115`, `117`, `118`, `120`, `121`, `134`, `140`, `230`, `270`, `801`, `900`, `902`, `903`, `1006`, `1113`, `1200`, `1201`, `10053`, `10054`, `10055`, `10151`, `10152`, `10153`, `10154`, `10155`, `11700`, `11701`, `11702`, `11703`, `11704`, `11705`, `11706`, `11713`, `12000`, `12001`, `12002`, `14200`, `14210`. The graph records these as numeric namespace collisions only; they do not imply that the configuration and telemetry values have the same meaning. Their graph provenance points to the configuration schema and telemetry source document, with no line number claimed where none is available.

| Integer ID | As FMC650 Configuration `ParameterId` (`re/` `.cfg` / `setparam`) | Config Type / Provenance | As FMC650 Telemetry `AVL ID` (Codec 8/8E Packet) | Telemetry Group | Official Flespi Telemetry Parameter(s) |
|---:|---|---|---|---|---|
| **`100`** | **Movement Source** | `Byte` (`generator:FMC650:1`) | **Axle weight 12** | FMS elements | `can.axle.weight`, `can.program.id` |
| **`101`** | **Ignition Source** | `Byte` (`generator:FMC650:1`) | **Axle weight 13** | FMS elements | `can.axle.weight`, `can.module.id` |
| **`102`** | **Sleep Settings** | `Byte` (`generator:FMC650:1`) | **Axle weight 14** | FMS elements | `can.axle.weight`, `can.engine.motorhours` |
| **`103`** | **Timeout** | `Int32` (`generator:FMC650:1`) | **Axle weight 15** | FMS elements | `can.axle.weight`, `can.counted.engine.motorhours`, `can.engine.motorhours` |
| **`104`** | **High Voltage** | `Int32` (`generator:FMC650:1`) | **Engine Total Hours Of Operation** | FMS elements | `ble.sensor.humidity`, `ble.sensor.humidity.error.code`, `engine.motorhours` |
| **`109`** | **GNSS Source** | `Byte` (`generator:FMC650:1`) | **Software Version Supported** | FMS elements | `fms.software.version` |
| **`110`** | **Battery Charge Mode** | `Byte` (`generator:FMC650:1`) | **Diagnostics Supported** | FMS elements | `can.engine.fuel.rate`, `fms.diagnostics.supported`, `segment.can.fuel.consumed` |
| **`111`** | **Analog Input Value Range** | `Byte` (`generator:FMC650:1`) | **Requests Supported** | FMS elements | `can.adblue.level`, `fms.requests.supported` |
| **`113`** | **Protocol Settings** | `Byte` (`generator:FMC650:1`) | **Service Distance** | FMS elements | `battery.level`, `can.service.mileage` |
| **`122`** | **Analog Input Value Range 3-4** | `Byte` (`generator:FMC650:1`) | **Direction Indication** | FMS elements | `can.axle.weight`, `fms.movement.direction` |
| **`123`** | **Static Navigation Deactivation Source** | `Byte` (`generator:FMC650:1`) | **Tachograph Performance** | FMS elements | `can.abs.failure.indicator.status`, `can.airbag.indicator.status`, `can.air.condition.status`, `can.automatic.retarder.status`, `can.battery.indicator.status`, `can.check.engine.indicator.status`, `can.coolant.level.low.indicator.status`, `can.cruise.status`, `can.driver.seatbelt.indicator.status`, `can.electronic.power.control.status`, `can.eps.indicator.status`, `can.esp.indicator.status`, `can.esp.status`, `can.front.fog.lights.status`, `can.fuel.level.low.indicator.status`, `can.glow.plug.indicator.status`, `can.handbrake.indicator.status`, `can.high.beam.status`, `can.lights.failure.indicator.status`, `can.low.beam.status`, `can.maintenance.required.status`, `can.manual.retarder.status`, `can.oil.pressure.indicator.status`, `can.parking.lights.status`, `can.passenger.seatbelt.indicator.status`, `can.ready.to.drive.indicator.status`, `can.rear.fog.lights.status`, `can.soot.filter.indicator.status`, `can.stop.indicator.status`, `can.tire.pressure.low.status`, `can.warning.indicator.status`, `can.wear.brake.pads.indicator.status`, `fms.tacho.performance` |
| **`136`** | **Beacon record** | `Byte` (`xml:ParameterId`) | **Instantaneous Fuel Economy** | FMS elements | `can.fuel.economy`, `tacho.driver.card.status` |
| **`137`** | **Record period on move** | `Int32` (`xml:ParameterId`) | **PTO Drive Engagement** | FMS elements | `pto.drive.engagement.enum`, `tacho.driver.activity.state`, `tacho.driver.activity.state.enum`, `tacho.driver.work.state.enum` |
| **`139`** | **Record period on stop** | `Int32` (`xml:ParameterId`) | **Gross Combination Vehicle Weight** | FMS elements | `tacho.driver.continuous_driving.duration`, `total.vehicle.weight` |
| **`141`** | **Beacon mode** | `Byte` (`xml:ParameterId`) | **Battery Temperature** | CAN adapters elements | `battery.temperature`, `tacho.driver.cumulative_break.duration` |
| **`144`** | **Beacon clear timeout** | `Int32` (`xml:ParameterId`) | **SD Status** | Permanent I/O elements | `sd.status`, `tacho.driver.activity.duration`, `tacho.driver.current.activity.duration` |
| **`146`** | **IO check on startup** | `Byte` (`generator:FMC650:1`) | **Manual CAN 01** | Manual CAN elements | `manual.can`, `manual.can.hex`, `tacho.driver.cumulative_driving.duration` |
| **`147`** | **CNG Consumption multiplier** | `Double` (`generator:FMC650:1`) | **Manual CAN 02** | Manual CAN elements | `manual.can`, `manual.can.hex`, `tacho.driver.card.code` |
| **`151`** | **Mode** | `Byte` (`generator:FMC650:1`) | **Manual CAN 06** | Manual CAN elements | `battery.temperature`, `manual.can`, `manual.can.hex` |
| **`152`** | **Baudrate** | `Byte` (`generator:FMC650:1`) | **Manual CAN 07** | Manual CAN elements | `battery.level`, `can.vehicle.battery.level`, `manual.can`, `manual.can.hex` |
| **`157`** | **Garmin Features** | `Byte` (`generator:FMC650:1`) | **Geofence zone 03** | Eventual I/O elements | `geofence.overspeeding.status`, `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` |
| **`158`** | **Message Timestamp** | `Byte` (`generator:FMC650:1`) | **Geofence zone 04** | Eventual I/O elements | `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` |
| **`160`** | **Mode** | `Byte` (`generator:FMC650:1`) | **Geofence zone 06** | Eventual I/O elements | `can.dtc.number`, `geofence.status`, `overspeeding.status` |
| **`161`** | **Baudrate** | `Byte` (`generator:FMC650:1`) | **Geofence zone 07** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`162`** | **LLS 1 Address** | `LLS` (`generator:FMC650:1`) | **Geofence zone 08** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`163`** | **LLS 2 Address** | `LLS` (`generator:FMC650:1`) | **Geofence zone 09** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`164`** | **LLS 3 Address** | `LLS` (`generator:FMC650:1`) | **Geofence zone 10** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`165`** | **LLS 4 Address** | `LLS` (`generator:FMC650:1`) | **Geofence zone 11** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`166`** | **LLS 5 Address** | `LLS` (`generator:FMC650:1`) | **Geofence zone 12** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`169`** | **Accelerometer Auto Calibration** | `Byte` (`generator:FMC650:1`) | **Geofence zone 15** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`170`** | **CMD ID** | `Byte` (`generator:FMC650:1`) | **Geofence zone 16** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`171`** | **Start byte** | `Int32` (`generator:FMC650:1`) | **Geofence zone 17** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`172`** | **Stop byte (delimiter)** | `Int32` (`generator:FMC650:1`) | **Geofence zone 18** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`173`** | **Mode** | `Byte` (`generator:FMC650:1`) | **Geofence zone 19** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`174`** | **Baudrate** | `Byte` (`generator:FMC650:1`) | **Geofence zone 20** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`175`** | **Message timestamp** | `Byte` (`generator:FMC650:1`) | **Auto Geofence** | Eventual I/O elements | `geofence.status` |
| **`176`** | **CMD ID** | `Byte` (`generator:FMC650:1`) | **DTC Errors** | CAN adapters elements | `can.dtc.number` |
| **`177`** | **Start byte** | `Int32` (`generator:FMC650:1`) | **Event Reserved01** | Eventual I/O elements | `idle.status` |
| **`178`** | **Stop byte (delimiter)** | `Int32` (`generator:FMC650:1`) | **Network Type** | Permanent I/O elements | `gsm.network.type` |
| **`180`** | **Start ID** | `Int32` (`generator:FMC650:1`) | **Digital Output 2** | Permanent I/O elements | `dout` |
| **`181`** | **Stop ID** | `Int32` (`generator:FMC650:1`) | **GNSS PDOP** | Permanent I/O elements | `position.pdop` |
| **`182`** | **Message Timestamp** | `Byte` (`generator:FMC650:1`) | **GNSS HDOP** | Permanent I/O elements | `position.hdop` |
| **`183`** | **CMD ID** | `Byte` (`generator:FMC650:1`) | **Drive Recognize** | Tachograph data elements | `tacho.drive.recognize.status` |
| **`186`** | **Device IMEI** | `Byte` (`generator:FMC650:1`) | **Tachograph Over Speed** | Tachograph data elements | `tacho.overspeeding.status` |
| **`187`** | **Device IMEI** | `Byte` (`generator:FMC650:1`) | **Driver 1 Card Presence** | Tachograph data elements | `tacho.driver.card.presence`, `tacho.driver.card.status` |
| **`188`** | **NMEA filter** | `Byte` (`generator:FMC650:1`) | **Driver 2 Card Presence** | Tachograph data elements | `can.retarder.torque.load`, `tacho.driver.card.presence`, `tacho.driver.card.status` |
| **`189`** | **Data reading period** | `Int32` (`xml:ParameterId`) | **Driver 1 Time Related States** | Tachograph data elements | `can.total.cruise.control.time`, `tacho.driver.time.state`, `tacho.driver.time.state.enum` |
| **`190`** | **Battery Fast CuttOff** | `Byte` (`generator:FMC650:1`) | **Driver 2 Time Related States** | Tachograph data elements | `geofence.status`, `overspeeding.status`, `tacho.driver.time.state`, `tacho.driver.time.state.enum` |
| **`200`** | **Status** | `Byte` (`generator:FMC650:1`) | **Sleep Mode** | Permanent I/O elements | `sleep.mode.enum` |
| **`201`** | **Domain** | `String` (`generator:FMC650:1`) | **LLS 1 Fuel Level** | Permanent I/O elements | `lls.value` |
| **`202`** | **Port** | `Int32` (`generator:FMC650:1`) | **LLS 1 Temperature** | Permanent I/O elements | `lls.temperature` |
| **`203`** | **Start delay** | `Int32` (`generator:FMC650:1`) | **LLS 2 Fuel Level** | Permanent I/O elements | `lls.value` |
| **`204`** | **Tachograph ignition source** | `Byte` (`generator:FMC650:1`) | **LLS 2 Temperature** | Permanent I/O elements | `lls.temperature` |
| **`205`** | **CAN1 bus speed** | `Byte` (`generator:FMC650:1`) | **GSM Cell ID** | Permanent I/O elements | `gsm.cellid` |
| **`206`** | **CAN1 bus mode** | `Byte` (`generator:FMC650:1`) | **GSM Area Code** | Permanent I/O elements | `gsm.lac` |
| **`207`** | **CAN2 bus speed** | `Byte` (`generator:FMC650:1`) | **RFID** | Permanent I/O elements | `rfid.code` |
| **`208`** | **CAN2 bus mode** | `Byte` (`generator:FMC650:1`) | **Ultrasonic Software Status 1** | Permanent I/O elements | `geofence.status`, `overspeeding.status`, `ultrasonic.software.state.enum` |
| **`209`** | **DDD download source** | `Byte` (`generator:FMC650:1`) | **Ultrasonic Software Status 2** | Permanent I/O elements | `geofence.status`, `overspeeding.status`, `ultrasonic.software.state.enum` |
| **`210`** | **FMS data source** | `Byte` (`generator:FMC650:1`) | **LLS 3 Fuel Level** | Permanent I/O elements | `lls.value` |
| **`211`** | **K-Line Voltage Control** | `Byte` (`generator:FMC650:1`) | **LLS 3 Temperature** | Permanent I/O elements | `lls.temperature` |
| **`215`** | **Download with alternative tacho settings** | `Byte` (`generator:FMC650:1`) | **LLS 5 Temperature** | Permanent I/O elements | `lls.temperature` |
| **`216`** | **CAN1 termination resistance** | `Byte` (`generator:FMC650:1`) | **Total Odometer** | Permanent I/O elements | `geofence.status`, `overspeeding.status`, `vehicle.mileage` |
| **`217`** | **CAN2 termination resistance** | `Byte` (`generator:FMC650:1`) | **RFID COM2** | Permanent I/O elements | `geofence.status`, `overspeeding.status`, `rfid.code` |
| **`221`** | **IO Send Mode** | `Byte` (`generator:FMC650:1`) | **CCID Part3** | Permanent I/O elements | `geofence.status`, `gsm.sim.iccid`, `overspeeding.status` |
| **`232`** | **Include Tachograph data into regular record** | `Byte` (`generator:FMC650:1`) | **Vehicle Registration Number Part2** | Tachograph data elements | `can.cng.status`, `gsm.sim.status`, `vehicle.registration.number` |
| **`252`** | **OneMinuteRule** | `Int32` (`generator:FMC650:1`) | **Authorized Driving** | Eventual I/O elements | `external.powersource.status`, `ibutton.authorized.state.enum`, `ibutton.authorized.status` |
| **`253`** | **N/A driver state** | `Int32` (`generator:FMC650:1`) | **Green Driving Type** | Eventual I/O elements | `harsh.acceleration.event`, `harsh.braking.event`, `harsh.cornering.event` |
| **`254`** | **Deny driver work state when ignition off** | `Int32` (`generator:FMC650:1`) | **Green Driving Value** | Eventual I/O elements | `absolute.acceleration`, `harsh.cornering.angle` |
| **`255`** | **TachoCAN Filter** | `Byte` (`generator:FMC650:1`) | **Over Speeding** | Eventual I/O elements | `overspeeding.speed`, `overspeeding.status` |
| **`330`** | **TrailerCAN Data Source** | `Byte` (`xml:ParameterId`) | **Geofence zone 24** | Eventual I/O elements | `geofence.status`, `overspeeding.status` |
| **`10050`** | **Min Period Home** | `Int32` (`generator:FMC650:1`) | **Zone 1 Evaporator temperature** | Reefer IO | `freezer.zone1.evaporator.coil.temperature` |
| **`10051`** | **Min Distance Home** | `Int32` (`generator:FMC650:1`) | **Zone 1 Return Air Sensor 2** | Reefer IO | `freezer.zone1.return.air.temperature` |
| **`10052`** | **Min Angle Home** | `Int32` (`generator:FMC650:1`) | **Zone 1 Supply Air Sensor 2** | Reefer IO | `freezer.zone1.supply.air.temperature` |
| **`10200`** | **Min Period Unknown** | `Int32` (`generator:FMC650:1`) | **Tire 9 pressure** | TPMS | *(Unmapped in Flespi)* |
| **`10204`** | **Min Saved Records Unknown** | `Int32` (`generator:FMC650:1`) | **Tire 13 pressure** | TPMS | *(Unmapped in Flespi)* |
| **`10205`** | **Send Period Unknown** | `Int32` (`generator:FMC650:1`) | **Tire 14 pressure** | TPMS | *(Unmapped in Flespi)* |
| **`12450`** | **Temperature sensor 1** | `LLS` (`xml:ParameterId`) | **Auxil ext valve number 8** | ISOBUS | *(Unmapped in Flespi)* |
| **`12452`** | **Temperature sensor 3** | `LLS` (`xml:ParameterId`) | **Auxil ext valve number 10** | ISOBUS | *(Unmapped in Flespi)* |
| **`12453`** | **Temperature sensor 4** | `LLS` (`xml:ParameterId`) | **Auxil ext valve number 11** | ISOBUS | *(Unmapped in Flespi)* |
| **`12454`** | **1-wire mode** | `Byte` (`xml:ParameterId`) | **Auxil ext valve number 12** | ISOBUS | *(Unmapped in Flespi)* |
| **`12455`** | **list entry 6 (candidates: DallasSensorIdList)** | `String` (`xml:ListConfiguration`) | **Auxil ext valve number 13** | ISOBUS | *(Unmapped in Flespi)* |
| **`12457`** | **1-Wire Mode** | `Byte` (`generator:FMC650:1`) | **Auxil ext valve number 15** | ISOBUS | *(Unmapped in Flespi)* |

### 1.2 Why Manufacturer Configuration Parameters Never Map 1:1 by Assumption to Flespi Settings

| Mapping Archetype | Count of Flespi Settings | Explanation & Examples |
|---|---:|---|
| **1. Scalar `1:1` Configuration Mapping** | `11` | A single Flespi setting with one property maps to a single `.cfg` `ParameterId` (e.g., `accelerometer_calibration` -> `PID 169`, `sleep_mode` -> `PID 102`, `static_filter` -> `PID 106`, `tls` -> `PID 2020`). |
| **2. Bitmask `1:N` Decomposition** | `1` | `ignition_detection` splits a single bitmask `.cfg` parameter (`PID 101` `Ignition Source`) into 6 boolean properties (`din1`, `din2`, `din3`, `din4`, `ign_mov`, `ign_volt`). |
| **3. Composite `N:1` Bundling** | `14` | A single Flespi setting bundles 3 to 10 distinct `.cfg` `ParameterId`s into one JSON object (e.g., `gprs` bundles `PID 2000..2003`; `home_network` bundles `PID 10000..10055`; `green_driving` bundles `PID 11000..11019`). |
| **4. 6-Field `IOItem` Block Bundling (`IoId + 0..5`)** | `13` | Each Flespi `*_io` setting bundles 5 or 6 consecutive `IOItem` configuration `ParameterId`s (`Priority`, `Operand`, `High`, `Low`, `Event Only`, `Average`). Note that `battery_level_io` is inherited from FMB trackers and is **`in_cfg: false`** on `FMC650:1`! |
| **5. Sibling-Branch Camera Settings (`in_cfg: false`)** | `16` | `camera_features_*`, `camera_image_*`, `camera_scenario_mode_*`, `camera_video_*` map to `PID 1001000..1012045` (`xml:ParameterId`), which are **`in_cfg: false`** in the standard `FMC650:1 SpecId 1` `.cfg` export! |
| **6. Action / Read-Only Command Pseudo-Settings (No `.cfg` PID)** | `14` | `cpureset`, `deleterecords`, `getgps`, `getimeiccid`, `getrecord`, `getver`, `mcan_cmd`, `mcan_stop`, `odoset`, `outputs`, `sdformat`, `setdigout_4`, `tachocheck`, `web_connect` execute runtime commands and **do not correspond to any `.cfg` `ParameterId`**. |
| **7. Unmapped `.cfg` Parameters (`>97%` of `re/` Schema)** | `0` dedicated settings | Over **11,400 `in_cfg` `ParameterId`s** in `re/fmx65_03.01.01.Rev.15_schema.json` have **no Flespi setting** and must be accessed via Flespi's `setparam`, `getparam`, or `setio` commands. |

---

## 2. Complete Mapping: All 69 Official Flespi Device Settings -> FMC650 `re/` Configuration Parameters

| # | Official Flespi Setting (`key`) | Official Flespi Title | Official Flespi Properties | Mapping Archetype | Exact FMC650 Configuration `ParameterId` / `IoId` in `re/fmx65_03.01.01.Rev.15_schema.json` |
|---:|---|---|---|---|---|
| 1 | `accelerometer_calibration` | **Accelerometer auto calibration** | **enable**: Enable | 1:1 Scalar (`in_cfg: true`) | PID `169` (`Accelerometer Auto Calibration`, Byte, `0=Disable, 1=Enable`) -> Flespi `enable` |
| 2 | `analog_input1_io` | **Analog Input 1 I/O** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50180..50185` (`Analog Input 1`): `50180`->`prio`, `50181`->`operand`, `50182`->`high`, `50183`->`low`, `50184`->`event`, `50185`->`avg` *(Configures Telemetry `AVL ID 9` -> `ain.1`)* |
| 3 | `axis_x` | **Axis X** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50220..50225` (`Axis X`): `50220`->`prio`, `50221`->`operand`, `50222`->`high`, `50223`->`low`, `50224`->`event`, `50225`->`avg` *(Configures Telemetry `AVL ID 17` -> `position.PitchAngle` / X-axis)* |
| 4 | `axis_y` | **Axis Y** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50230..50235` (`Axis Y`): `50230`->`prio`, `50231`->`operand`, `50232`->`high`, `50233`->`low`, `50234`->`event`, `50235`->`avg` *(Configures Telemetry `AVL ID 18` -> `position.RollAngle` / Y-axis)* |
| 5 | `axis_z` | **Axis Z** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50240..50245` (`Axis Z`): `50240`->`prio`, `50241`->`operand`, `50242`->`high`, `50243`->`low`, `50244`->`event`, `50245`->`avg` *(Configures Telemetry `AVL ID 19` -> Z-axis)* |
| 6 | `backup_server_fmb640` | **Secondary GPRS Server Setup** | **host**: Host, **mode**: Secondary GPRS server mode, **port**: Port, **protocol**: Secondary GPRS server protocol | N:1 Composite Bundle (`in_cfg: true`) | PID `2007` (`Backup Server Mode` -> `mode`), PID `2008` (`Backup Server Domain` -> `host`), PID `2009` (`Backup Server Port` -> `port`), PID `2010` (`Backup Server Protocol` -> `protocol`) |
| 7 | `battery_charge_mode` | **Battery charge mode** | **mode**: Mode | 1:1 Scalar (`in_cfg: true`) | PID `110` (`Battery Charge Mode`, Byte, `0=On need, 1=After ignition ON, 2=Always`) -> Flespi `mode` |
| 8 | `battery_level_io` | **Battery level** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: false` in FMC650:1) | Not in FMC650:1 `.cfg` (FMB family Battery Level `IoId`; FMC650 uses `50120` Battery Voltage & `50130` Battery Current). *Never assume this setting applies to FMC650:1.* |
| 9 | `battery_voltage_io` | **Battery voltage** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50120..50125` (`Battery Voltage`): `50120`->`prio`, `50121`->`operand`, `50122`->`high`, `50123`->`low`, `50124`->`event`, `50125`->`avg` *(Configures Telemetry `AVL ID 67` -> `battery.voltage`)* |
| 10 | `camera_features_dashcam_com1` | **COM1 - Camera features** | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1011000` (`resolution`), `1011001` (`compression`), `1011002` (`osd`), `1011003` (`frame_rate`), `1011024` (`timezone`), `1011025` (`transfer_priority`) |
| 11 | `camera_features_dashcam_com2` | **COM2 - Camera features** | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1012000` (`resolution`), `1012001` (`compression`), `1012002` (`osd`), `1012003` (`frame_rate`), `1012024` (`timezone`), `1012025` (`transfer_priority`) |
| 12 | `camera_features_dualcam_com1` | **COM1 - Camera features** | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1001000` (`resolution`), `1001001` (`compression`), `1001002` (`osd`), `1001003` (`frame_rate`), `1001024` (`timezone`), `1001025` (`transfer_priority`) |
| 13 | `camera_features_dualcam_com2` | **COM2 - Camera features** | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1002000` (`resolution`), `1002001` (`compression`), `1002002` (`osd`), `1002003` (`frame_rate`), `1002024` (`timezone`), `1002025` (`transfer_priority`) |
| 14 | `camera_image_dashcam_com1` | **COM1 - Image settings** | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1011006` / `1011007` (`periodic`), PID `1011022` (`triggers`) |
| 15 | `camera_image_dashcam_com2` | **COM2 - Image settings** | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1012006` / `1012007` (`periodic`), PID `1012022` (`triggers`) |
| 16 | `camera_image_dualcam_com1` | **COM1 - Image settings** | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1001006` / `1001007` (`periodic`), PID `1001022` (`triggers`) |
| 17 | `camera_image_dualcam_com2` | **COM2 - Image settings** | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1002006` / `1002007` (`periodic`), PID `1002022` (`triggers`) |
| 18 | `camera_scenario_mode_dashcam_com1` | **COM1 - Scenario mode** | **mode**: Mode | 1:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1011020` (`icam_loc_zmid_scenario` -> `mode`) |
| 19 | `camera_scenario_mode_dashcam_com2` | **COM2 - Scenario mode** | **mode**: Mode | 1:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1012020` (`icam_loc_zmid_scenario` -> `mode`) |
| 20 | `camera_scenario_mode_dualcam_com1` | **COM1 - Scenario mode** | **mode**: Mode | 1:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1001020` (`icam_loc_zmid_scenario` -> `mode`) |
| 21 | `camera_scenario_mode_dualcam_com2` | **COM2 - Scenario mode** | **mode**: Mode | 1:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1002020` (`icam_loc_zmid_scenario` -> `mode`) |
| 22 | `camera_video_dashcam_com1` | **COM1 - Video settings** | **sources**: Video Sources, **duration**: Video Duration | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1011009..1011010` (`duration` before/after), PID `1011023` & `1011040..1011045` (`sources`/triggers) |
| 23 | `camera_video_dashcam_com2` | **COM2 - Video settings** | **sources**: Video Sources, **duration**: Video Duration | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1012009..1012010` (`duration` before/after), PID `1012023` & `1012040..1012045` (`sources`/triggers) |
| 24 | `camera_video_dualcam_com1` | **COM1 - Video settings** | **sources**: Video Sources, **duration**: Video Duration | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1001009..1001010` (`duration` before/after), PID `1001023` & `1001040..1001045` (`sources`/triggers) |
| 25 | `camera_video_dualcam_com2` | **COM2 - Video settings** | **sources**: Video Sources, **duration**: Video Duration | N:1 Sibling Branch (`in_cfg: false` in SpecId 1) | PID `1002009..1002010` (`duration` before/after), PID `1002023` & `1002040..1002045` (`sources`/triggers) |
| 26 | `cpureset` | **Restart (reboot) the device** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends SMS/Codec 12 `cpureset` command to reboot the MCU. Does **not** map to any `.cfg` `ParameterId`. |
| 27 | `data_codec` | **Data codec to use for data transmission** | **codec**: Data codec | 1:1 Scalar (`in_cfg: true`) | PID `113` (`Protocol Settings`, Byte, `0=Codec 8, 1=Codec 8 Extended`) -> Flespi `codec` |
| 28 | `deleterecords` | **Delete all stored records** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends SMS/Codec 12 `deleterecords` command to wipe `recdb/0` and `sd:recdb/1`. Does **not** map to any `.cfg` `ParameterId`. |
| 29 | `external_voltage_io` | **External voltage** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50080..50085` (`External Voltage`): `50080`->`prio`, `50081`->`operand`, `50082`->`high`, `50083`->`low`, `50084`->`event`, `50085`->`avg` *(Configures Telemetry `AVL ID 66` -> `external.powersource.voltage`)* |
| 30 | `getgps` | **Request current GPS data, date and time.** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends `getgps` command; response is parsed as telemetry. No `.cfg` `ParameterId`. |
| 31 | `getimeiccid` | **Send getimeiccid command** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends `getimeiccid` command. No `.cfg` `ParameterId`. |
| 32 | `getrecord` | **Force device to generate a report** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends `getrecord` command to trigger an immediate high-priority AVL packet. No `.cfg` `ParameterId`. |
| 33 | `getver` | **getver command response** | **id**: Device configuration ID, **imei**: IMEI, **modem**: Modem version, **hardware_model**: Hardware model, **firmware_version**: Firmware version, **bootloader_version**: Bootloader version | Read-Only Status Pseudo-Setting (No `.cfg` PID) | Sends `getver` command and populates `firmware_version`, `hardware_model`, `imei`, `modem`, `bootloader_version`, `id`. No `.cfg` `ParameterId`. |
| 34 | `gnss_source` | **GNSS Source** | **mode**: Mode | 1:1 Scalar (`in_cfg: true`) | PID `109` (`GNSS Source`, Byte bitmask, default `15` = GPS+GLONASS+Galileo+BeiDou) -> Flespi `mode` |
| 35 | `gprs` | **GPRS Setup** | **apn**: APN Name, **enabled**: GPRS Enabled, **password**: APN Password, **username**: APN Username | N:1 Composite Bundle (`in_cfg: true`) | PID `2000` (`GPRS Context` -> `enabled`), PID `2001` (`APN` -> `apn`), PID `2002` (`APN Username` -> `username`), PID `2003` (`APN Password` -> `password`) *(Note: SIM 2 PIDs `2011..2014` are NOT mapped here; use `setparam`)* |
| 36 | `gprs_server` | **GPRS Server Setup** | **host**: Host, **port**: Port, **protocol**: Server protocol | N:1 Composite Bundle (`in_cfg: true`) | PID `2004` (`Domain` -> `host`), PID `2005` (`Port` -> `port`), PID `2006` (`Protocol` -> `protocol`, `0=TCP, 1=UDP`) |
| 37 | `green_driving` | **Green Driving** | **prio**: Priority, **output**: Output Control, **source**: Source, **duration**: Duration, **max_accel**: Max Acceleration, **max_angle**: Max Angle, **max_brake**: Max Braking, **eco_maximum**: Eco Driving Maximum, **advanced_eco**: Advanced Eco Driving, **cornering_duration**: Cornering Active Output Duration | N:1 Composite Bundle (`in_cfg: true`) | PID `11000` (`prio`), PID `11003` (`output`), PID `11004` (`max_accel`), PID `11005` (`max_brake`), PID `11006` (`max_angle`), PID `11007` (`source`), PID `11008` (`duration`), PID `11011` (`cornering_duration`), PID `11015` (`eco_maximum`), PID `11019` (`advanced_eco`) |
| 38 | `home_network` | **Home GSM Network Settings** | **on_move**: Vehicle Moving, **on_stop**: Vehicle On Stop | N:1 Composite Bundle (`in_cfg: true`) | **On Stop (`on_stop`)**: PID `10000` (`Min Period`), `10004` (`Min Saved Records`), `10005` (`Send Period`). **On Move (`on_move`)**: PID `10050` (`Min Period`), `10051` (`Min Distance`), `10052` (`Min Angle`), `10053` (`Min Speed Delta`), `10054` (`Min Saved Records`), `10055` (`Send Period`) |
| 39 | `idling_dout3` | **Excessive Idling Detection** | **prio**: Priority, **output**: Output Control, **record**: Eventual Records, **move_time**: Move Timeout, **stop_time**: Stop Timeout | N:1 Composite Bundle (`in_cfg: true`) | PID `11200` (`prio`), PID `11203` (`record`), PID `11204` (`output`), PID `11205` (`stop_time`), PID `11206` (`move_time`) |
| 40 | `ignition_detection` | **Ignition Detection Source** | **din1**: DIN1, **din2**: DIN2, **din3**: DIN3, **din4**: DIN4, **ign_mov**: Movement, **ign_volt**: Power Voltage | 1:N Bitmask Decomposition (`in_cfg: true`) | Decomposes **PID `101` (`Ignition Source`)** bitmask into booleans: `din1` (bit 1 = `2`), `din2` (bit 2 = `4`), `din3` (bit 3 = `8`), `din4` (bit 4 = `16`), `ign_volt` (bit 7 = `128`, thresholds in PID `104` High / `105` Low), `ign_mov` (bit 5 = `32`) |
| 41 | `inputs1_io` | **Digital Input 1 I/O** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50170..50175` (`Digital Input 1`): `50170`->`prio`, `50171`->`operand`, `50172`->`high`, `50173`->`low`, `50174`->`event`, `50175`->`avg` *(Configures Telemetry `AVL ID 1` -> `din.1`)* |
| 42 | `inputs2_io` | **Digital Input 2** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50270..50275` (`Digital Input 2`): `50270`->`prio`, `50271`->`operand`, `50272`->`high`, `50273`->`low`, `50274`->`event`, `50275`->`avg` *(Configures Telemetry `AVL ID 2` -> `din.2`)* |
| 43 | `inputs3_io` | **Digital Input 3** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50280..50285` (`Digital Input 3`): `50280`->`prio`, `50281`->`operand`, `50282`->`high`, `50283`->`low`, `50284`->`event`, `50285`->`avg` *(Configures Telemetry `AVL ID 3` -> `din.3`)* |
| 44 | `inputs4_io` | **Digital Input 4** | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 6-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50660..50665` (`Digital Input 4`): `50660`->`prio`, `50661`->`operand`, `50662`->`high`, `50663`->`low`, `50664`->`event`, `50665`->`avg` *(Configures Telemetry `AVL ID 4` -> `din.4`)* |
| 45 | `io_global_send_mode` | **IO Global Send Mode** | **mode**: Mode | 1:1 Scalar (`in_cfg: true`) | PID `221` (`IO Send Mode`, Byte, `0=Don't Send, 1=Send Zero, 2=Send Last Known, 3=Send 0xFF`) -> Flespi `mode` |
| 46 | `manual_can` | **Experimental. Manual CAN parameters setup.** | **config**: Command mode, **can_number**: CAN number | N:1 Indexed Block (`in_cfg: true`) | Manual CAN configuration blocks (`PID 70000..70699`, 70 slots × 10 parameters: CAN Type, Frame Type, CAN Source, Mask, CAN ID, + `IoId` blocks `90000..90695`) |
| 47 | `manual_can_command` | **Experimental. Manual CAN command parameters setup.** | **config**: Command mode, **command_number**: Command number | N:1 Indexed Block (`in_cfg: true`) | Manual CAN Command blocks (`PID 71000..71099`, 10 command slots) |
| 48 | `manual_can_request` | **Manual CAN Request parameters setup.** | **config**: Command mode, **can_number**: CAN number | N:1 Indexed Block (`in_cfg: true`) | Manual CAN Request blocks (`PID 72000..72699`, 70 request slots) |
| 49 | `mcan_cmd` | **Trigger Manual CAN Command** | **data**: Data override, **can_id**: CAN ID override, **slot_id**: Slot ID | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `mcan_cmd` command to trigger a Manual CAN Command slot (`slot_id`, `can_id`, `data`). No `.cfg` `ParameterId`. |
| 50 | `mcan_stop` | **Stop periodic Manual CAN Command** | **slot_id**: Slot ID | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `mcan_stop` command to stop a periodic Manual CAN Command slot (`slot_id`). No `.cfg` `ParameterId`. |
| 51 | `network_ping_640` | **Network Ping** | **timeout**: Timeout | 1:1 Scalar (`in_cfg: true`) | PID `1003` (`Network Ping Timeout`, Int32, `0..3000 s`, paired with PID `1007` `Ping mode`) -> Flespi `timeout` |
| 52 | `odometer_io` | **Odometer** | **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 5-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50160..50164` (`Total Odometer`): `50160`->`prio`, `50161`->`operand`, `50162`->`high`, `50163`->`low`, `50164`->`event` *(Configures Telemetry `AVL ID 16` -> `vehicle.mileage`)* |
| 53 | `odoset` | **Set total odometer value** | **value**: Odometer value | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `odoset:<value>` / `odoget` command to set/read total odometer. No `.cfg` `ParameterId`. |
| 54 | `outputs` | **Digital Outputs** | **out1**: Output 1, **out2**: Output 2, **out3**: Output 3, **out4**: Output 4 | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `setdigout` command to toggle Digital Outputs 1–4 (`out1..out4`). No `.cfg` `ParameterId`. |
| 55 | `overspeeding_dout4` | **Overspeeding** | **prio**: Priority, **output**: Output Control, **max_speed**: Max Speed | N:1 Composite Bundle (`in_cfg: true`) | PID `11100` (`prio`), PID `11103` (`output`), PID `11104` (`max_speed`) |
| 56 | `records_params` | **Records Parameters** | **order**: Records Sorting Order, **online**: Open Link Timeout, **response**: Server Response Timeout | N:1 Composite Bundle (`in_cfg: true`) | PID `1000` (`Open Link Timeout` -> `online`), PID `1001` (`Response Timeout` -> `response`), PID `1002` (`Sort By` -> `order`, `0=Newest, 1=Oldest`) |
| 57 | `roaming_network` | **Roaming GSM Network Settings** | **on_move**: Vehicle Moving, **on_stop**: Vehicle On Stop | N:1 Composite Bundle (`in_cfg: true`) | **On Stop (`on_stop`)**: PID `10100` (`Min Period`), `10104` (`Min Saved Records`), `10105` (`Send Period`). **On Move (`on_move`)**: PID `10150` (`Min Period`), `10151` (`Min Distance`), `10152` (`Min Angle`), `10153` (`Min Speed Delta`), `10154` (`Min Saved Records`), `10155` (`Send Period`) |
| 58 | `sdformat` | **Format SD card** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `sdformat` command to format the MicroSD card. No `.cfg` `ParameterId`. |
| 59 | `setdigout_4` | **Action command setdigout** | **out1**: State of digital output 1, **out2**: State of digital output 2, **out3**: State of digital output 3, **out4**: State of digital output 4 | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `setdigout` command with timeout and speed limit parameters for DOUT 1–4. No `.cfg` `ParameterId`. |
| 60 | `sleep_mode` | **Sleep Mode** | **mode**: Sleep Mode | 1:1 Scalar (`in_cfg: true`) | PID `102` (`Sleep Settings`, Byte, `0=Disable, 1=Gps Sleep, 2=Deep Sleep, 3=Online Deep Sleep`) -> Flespi `mode` *(Note: Sleep Timeout `PID 103` requires `setparam`)* |
| 61 | `static_filter` | **Static Navigation** | **stat_nav**: Static Navigation | 1:1 Scalar (`in_cfg: true`) | PID `106` (`Static Navigation`, Byte, `0=Disabled, 1=Enabled`) -> Flespi `stat_nav` |
| 62 | `tachocheck` | **Checking the tachograph configuration** | **addr**: Addr, **baud**: Baud, **ignition**: Ignition, **fms_on_bus**: [ABCD] FMS data presence on the bus, **tacho_on_bus**: [T] Tachograph presence on the bus, **k_line_on_bus**: [K] K-Line data presence on the bus, **close_last_auth**: [C] Response to close last authentication session validity check, **remote_session_validity**: [R] Response to open remote session validity check | Read-Only Status Pseudo-Setting (No `.cfg` PID) | Sends runtime `tachocheck` diagnostic command and parses CAN/K-Line/FMS/Tacho bus status. No `.cfg` `ParameterId`. |
| 63 | `tacho_download_source` | **Tachograph DDD download source** | **value**: Value | 1:1 Scalar (`in_cfg: true`) | PID `209` (`DDD download source`, Byte) -> Flespi `value` |
| 64 | `tacho_ignition_source` | **Tachograph ignition source** | **value**: Value | 1:1 Scalar (`in_cfg: true`) | PID `204` (`Tachograph ignition source`, Byte) -> Flespi `value` |
| 65 | `tacho_web` | **Tacho WEB settings** | **config**: Command mode | N:1 Composite Bundle (`in_cfg: true`) | PID `200` (`Status`), PID `201` (`Domain`), PID `202` (`Port`), PID `203` (`Start delay`) |
| 66 | `tls` | **Enable connection over TLS** | **enable**: TLS enable | 1:1 Scalar (`in_cfg: true`) | PID `2020` (`TLS Encryption`, Byte, `0=None, 1=TLS/DTLS`) -> Flespi `enable` |
| 67 | `trip_odometer_io` | **Trip Odometer** | **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand | 5-Field `IOItem` Block (`in_cfg: true`) | IoId Base `50150..50154` (`Trip Odometer`): `50150`->`prio`, `50151`->`operand`, `50152`->`high`, `50153`->`low`, `50154`->`event` *(Configures Telemetry `AVL ID 199` -> `trip.mileage`)* |
| 68 | `unknown_network` | **Unknown GSM Network Settings** | **on_move**: Vehicle Moving, **on_stop**: Vehicle On Stop | N:1 Composite Bundle (`in_cfg: true`) | **On Stop (`on_stop`)**: PID `10200` (`Min Period`), `10204` (`Min Saved Records`), `10205` (`Send Period`). **On Move (`on_move`)**: PID `10250` (`Min Period`), `10251` (`Min Distance`), `10252` (`Min Angle`), `10253` (`Min Speed Delta`), `10254` (`Min Saved Records`), `10255` (`Send Period`) |
| 69 | `web_connect` | **Connect to Fota WEB immediately.** | — | Action Command Pseudo-Setting (No `.cfg` PID) | Sends runtime `web_connect` command to initiate an immediate FOTA WEB session. No `.cfg` `ParameterId`. |

---

## 3. Reverse Mapping: All 11,688 `in_cfg` Configuration Parameters in `re/` -> Official Flespi Mechanism

### 3.1 Coverage by `re/fmx65_03.01.01.Rev.15_schema.json` Provenance Category

| `re/` Provenance (`source`) | `in_cfg` IDs | Total Schema IDs | ID Ranges | Dedicated Flespi Setting Coverage | Official Flespi Command Fallback |
|---|---:|---:|---|---|---|
| `generator:FMC650:1` | `1,149` | `1,150` | `10..181334` | **~75 IDs** covered across 28 composite/scalar Flespi settings (`sleep_mode`, `ignition_detection`, `gprs`, `gprs_server`, `backup_server_fmb640`, `home_network`, `roaming_network`, `unknown_network`, `green_driving`, `overspeeding_dout4`, `idling_dout3`, `tacho_web`, etc.) | `setparam` / `getparam` (`{"param": <PID>, "value": "..."}`) |
| `xml:ParameterId` | `126` | `2,293` | `108..2000394` | **16 Camera settings** map to `PID 1001000..1012045` (`in_cfg: false`); remaining `126` `in_cfg` IDs (Beacon, RS232, LLS, etc.) have **0** dedicated Flespi settings | `setparam` / `getparam` |
| `xml:ListConfiguration` | `1,281` | `1,392` | `1600..30500`, `70000..72699` | Only `manual_can`, `manual_can_command`, and `manual_can_request` (`70000..72699`) have experimental Flespi settings; Authorized Numbers (`4000..4199`), Predefined Numbers (`7000..7009`), Operator Lists (`5000..5549`, `9500..9549`), and iButton Lists (`30000..30500`) have **0** dedicated Flespi settings | `setparam` / `getparam` |
| `xml:Geozones` | `1,100` | `1,100` | `20100..22099` (100 zones × 11 fields) | **0** dedicated Flespi settings | `setparam` / `getparam` |
| `xml:Polygon` | `1,581` | `1,581` | `60310..62309` (100 polygons) | **0** dedicated Flespi settings | `setparam` / `getparam` |
| `generator:IOItem` | `6,451` | `6,451` | `45100..181334` (1,357 `IoId` bases × up to 6 fields) | **12 `IoId` bases (`70` IDs)** covered by Flespi `*_io` settings (`50080`, `50120`, `50150`, `50160`, `50170`, `50180`, `50220`, `50230`, `50240`, `50270`, `50280`, `50660`). The remaining **1,345 `IoId` bases (`6,381` IDs)** have **0** dedicated Flespi settings | `setio` (`{"id": <IoId_Base>, "priority": ..., "operand": ..., "high": ..., "low": ..., "event": ..., "average": ...}`) or `setparam` |

### 3.2 Detailed Mapping of Core Base Configuration Parameters (`PID 100` – `PID 12099` in `re/`)

| FMC650 Config `ParameterId` (`re/`) | `in_cfg` | `re/` Label | Type | Default | Ref `.cfg` Value | Official Flespi Setting (`key.property`) | Official Flespi Command Method |
|---:|---|---|---|---|---|---|---|
| `100` | `true` | **Movement Source** | `Byte` | `0` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=100`) |
| `101` | `true` | **Ignition Source** | `Byte` | `32` | `1` | `ignition_detection` (`din1..din4, ign_mov, ign_volt`) | `setparam` / `getparam` (`param=101`) |
| `102` | `true` | **Sleep Settings** | `Byte` | `2` | `0` | `sleep_mode.mode` | `setparam` / `getparam` (`param=102`) |
| `103` | `true` | **Timeout** | `Int32` | `10` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=103`) |
| `104` | `true` | **High Voltage** | `Int32` | `30000` | `30000` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=104`) |
| `105` | `true` | **Low Voltage** | `Int32` | `13200` | `23500` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=105`) |
| `106` | `true` | **Static Navigation** | `Byte` | `1` | `1` | `static_filter.stat_nav` | `setparam` / `getparam` (`param=106`) |
| `107` | `true` | **Records Saving/Sending Without TS** | `Byte` | `0` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=107`) |
| `109` | `true` | **GNSS Source** | `Byte` | `15` | `15` | `gnss_source.mode` | `setparam` / `getparam` (`param=109`) |
| `110` | `true` | **Battery Charge Mode** | `Byte` | `0` | `0` | `battery_charge_mode.mode` | `setparam` / `getparam` (`param=110`) |
| `111` | `true` | **Analog Input Value Range** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=111`) |
| `113` | `true` | **Protocol Settings** | `Byte` | `0` | `1` | `data_codec.codec` | `setparam` / `getparam` (`param=113`) |
| `115` | `true` | **AIN4/DOUT4 Mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=115`) |
| `117` | `true` | **Odometer source settings** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=117`) |
| `118` | `true` | **Speed source settings** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=118`) |
| `119` | `true` | **Fuel level source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=119`) |
| `120` | `true` | **Fuel consumption source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=120`) |
| `121` | `true` | **High resolution engine total fuel used** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=121`) |
| `122` | `true` | **Analog Input Value Range 3-4** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=122`) |
| `123` | `true` | **Static Navigation Deactivation Source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=123`) |
| `134` | `true` | **Beacon detection** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=134`) |
| `136` | `true` | **Beacon record** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=136`) |
| `137` | `true` | **Record period on move** | `Int32` | `60` | `60` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=137`) |
| `139` | `true` | **Record period on stop** | `Int32` | `60` | `60` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=139`) |
| `140` | `true` | **Gravity Filter** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=140`) |
| `141` | `true` | **Beacon mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=141`) |
| `144` | `true` | **Beacon clear timeout** | `Int32` | `10` | `10` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=144`) |
| `146` | `true` | **IO check on startup** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=146`) |
| `147` | `true` | **CNG Consumption multiplier** | `Double` | `0.5` | `0.5` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=147`) |
| `151` | `true` | **Mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=151`) |
| `152` | `true` | **Baudrate** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=152`) |
| `157` | `true` | **Garmin Features** | `Byte` | `3` | `3` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=157`) |
| `158` | `true` | **Message Timestamp** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=158`) |
| `160` | `true` | **Mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=160`) |
| `161` | `true` | **Baudrate** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=161`) |
| `162` | `true` | **LLS 1 Address** | `LLS` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=162`) |
| `163` | `true` | **LLS 2 Address** | `LLS` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=163`) |
| `164` | `true` | **LLS 3 Address** | `LLS` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=164`) |
| `165` | `true` | **LLS 4 Address** | `LLS` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=165`) |
| `166` | `true` | **LLS 5 Address** | `LLS` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=166`) |
| `169` | `true` | **Accelerometer Auto Calibration** | `Byte` | `1` | `1` | `accelerometer_calibration.enable` | `setparam` / `getparam` (`param=169`) |
| `170` | `true` | **CMD ID** | `Byte` | `6` | `6` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=170`) |
| `171` | `true` | **Start byte** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=171`) |
| `172` | `true` | **Stop byte (delimiter)** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=172`) |
| `173` | `true` | **Mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=173`) |
| `174` | `true` | **Baudrate** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=174`) |
| `175` | `true` | **Message timestamp** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=175`) |
| `176` | `true` | **CMD ID** | `Byte` | `6` | `6` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=176`) |
| `177` | `true` | **Start byte** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=177`) |
| `178` | `true` | **Stop byte (delimiter)** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=178`) |
| `180` | `true` | **Start ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=180`) |
| `181` | `true` | **Stop ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=181`) |
| `182` | `true` | **Message Timestamp** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=182`) |
| `183` | `true` | **CMD ID** | `Byte` | `6` | `6` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=183`) |
| `186` | `true` | **Device IMEI** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=186`) |
| `187` | `true` | **Device IMEI** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=187`) |
| `188` | `true` | **NMEA filter** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=188`) |
| `189` | `true` | **Data reading period** | `Int32` | `5` | `5` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=189`) |
| `190` | `true` | **Battery Fast CuttOff** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=190`) |
| `200` | `true` | **Status** | `Byte` | `0` | `1` | `tacho_web` (`Status`) | `setparam` / `getparam` (`param=200`) |
| `201` | `true` | **Domain** | `String` | `—` | `ddd.teltonika.lt` | `tacho_web` (`Domain`) | `setparam` / `getparam` (`param=201`) |
| `202` | `true` | **Port** | `Int32` | `—` | `29000` | `tacho_web` (`Port`) | `setparam` / `getparam` (`param=202`) |
| `203` | `true` | **Start delay** | `Int32` | `5` | `5` | `tacho_web` (`Start delay`) | `setparam` / `getparam` (`param=203`) |
| `204` | `true` | **Tachograph ignition source** | `Byte` | `0` | `1` | `tacho_ignition_source.value` | `setparam` / `getparam` (`param=204`) |
| `205` | `true` | **CAN1 bus speed** | `Byte` | `0` | `500` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=205`) |
| `206` | `true` | **CAN1 bus mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=206`) |
| `207` | `true` | **CAN2 bus speed** | `Byte` | `0` | `500` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=207`) |
| `208` | `true` | **CAN2 bus mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=208`) |
| `209` | `true` | **DDD download source** | `Byte` | `1` | `0` | `tacho_download_source.value` | `setparam` / `getparam` (`param=209`) |
| `210` | `true` | **FMS data source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=210`) |
| `211` | `true` | **K-Line Voltage Control** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=211`) |
| `215` | `true` | **Download with alternative tacho settings** | `Byte` | `0` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=215`) |
| `216` | `true` | **CAN1 termination resistance** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=216`) |
| `217` | `true` | **CAN2 termination resistance** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=217`) |
| `221` | `true` | **IO Send Mode** | `Byte` | `0` | `0` | `io_global_send_mode.mode` | `setparam` / `getparam` (`param=221`) |
| `230` | `true` | **Tachograph periodic record timeout** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=230`) |
| `232` | `true` | **Include Tachograph data into regular record** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=232`) |
| `252` | `true` | **OneMinuteRule** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=252`) |
| `253` | `true` | **N/A driver state** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=253`) |
| `254` | `true` | **Deny driver work state when ignition off** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=254`) |
| `255` | `true` | **TachoCAN Filter** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=255`) |
| `270` | `true` | **Beacon record priority** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=270`) |
| `330` | `true` | **TrailerCAN Data Source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=330`) |
| `700` | `true` | **Eco Score Allowed Events** | `Int32` | `10` | `10` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=700`) |
| `801` | `true` | **Local Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=801`) |
| `900` | `true` | **Synchronization Settings** | `Byte` | `2` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=900`) |
| `902` | `true` | **NTP Server 1** | `String` | `avl1.teltonika.lt` | `avl1.teltonika.lt` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=902`) |
| `903` | `true` | **NTP Server 2** | `String` | `pool.ntp.org` | `pool.ntp.org` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=903`) |
| `910` | `true` | **NTP sync. timeout** | `Int32` | `60` | `300` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=910`) |
| `1000` | `true` | **Open Link Timeout** | `Int32` | `30` | `600` | `records_params.online` | `setparam` / `getparam` (`param=1000`) |
| `1001` | `true` | **Response Timeout** | `Int32` | `30` | `30` | `records_params.response` | `setparam` / `getparam` (`param=1001`) |
| `1002` | `true` | **Sort By** | `Byte` | `0` | `0` | `records_params.order` | `setparam` / `getparam` (`param=1002`) |
| `1003` | `true` | **Network Ping Timeout** | `Int32` | `60` | `1` | `network_ping_640.timeout` | `setparam` / `getparam` (`param=1003`) |
| `1006` | `true` | **Save records to** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1006`) |
| `1007` | `true` | **Ping mode** | `Byte` | `0` | `2` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1007`) |
| `1100` | `true` | **Update frequency** | `Int32` | `30` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1100`) |
| `1111` | `true` | **BLE broadcasting service ID** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1111`) |
| `1113` | `true` | **BLE Scan duration** | `Int32` | `30` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1113`) |
| `1114` | `true` | **Scan retries until error** | `Int32` | `30` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1114`) |
| `1115` | `true` | **Non Stop Scan** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1115`) |
| `1116` | `true` | **Broadcasting control** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1116`) |
| `1200` | `true` | **Working mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1200`) |
| `1201` | `true` | **ID** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1201`) |
| `1202` | `true` | **MAC** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1202`) |
| `1250` | `true` | **Working mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1250`) |
| `1251` | `true` | **ID** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1251`) |
| `1252` | `true` | **MAC** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1252`) |
| `1300` | `true` | **Working mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1300`) |
| `1301` | `true` | **ID** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1301`) |
| `1302` | `true` | **MAC** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1302`) |
| `1350` | `true` | **Working mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1350`) |
| `1351` | `true` | **ID** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1351`) |
| `1352` | `true` | **MAC** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1352`) |
| `1700` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1700`) |
| `1701` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1701`) |
| `1702` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1702`) |
| `1703` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1703`) |
| `1704` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1704`) |
| `1705` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1705`) |
| `1706` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1706`) |
| `1707` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1707`) |
| `1708` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1708`) |
| `1710` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1710`) |
| `1711` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1711`) |
| `1712` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1712`) |
| `1713` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1713`) |
| `1714` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1714`) |
| `1715` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1715`) |
| `1716` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1716`) |
| `1717` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1717`) |
| `1718` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1718`) |
| `1720` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1720`) |
| `1721` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1721`) |
| `1722` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1722`) |
| `1723` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1723`) |
| `1724` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1724`) |
| `1725` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1725`) |
| `1726` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1726`) |
| `1727` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1727`) |
| `1728` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1728`) |
| `1730` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1730`) |
| `1731` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1731`) |
| `1732` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1732`) |
| `1733` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1733`) |
| `1734` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1734`) |
| `1735` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1735`) |
| `1736` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1736`) |
| `1737` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1737`) |
| `1738` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1738`) |
| `1740` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1740`) |
| `1741` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1741`) |
| `1742` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1742`) |
| `1743` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1743`) |
| `1744` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1744`) |
| `1745` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1745`) |
| `1746` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1746`) |
| `1747` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1747`) |
| `1748` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1748`) |
| `1750` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1750`) |
| `1751` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1751`) |
| `1752` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1752`) |
| `1753` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1753`) |
| `1754` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1754`) |
| `1755` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1755`) |
| `1756` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1756`) |
| `1757` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1757`) |
| `1758` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1758`) |
| `1760` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1760`) |
| `1761` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1761`) |
| `1762` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1762`) |
| `1763` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1763`) |
| `1764` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1764`) |
| `1765` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1765`) |
| `1766` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1766`) |
| `1767` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1767`) |
| `1768` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1768`) |
| `1770` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1770`) |
| `1771` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1771`) |
| `1772` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1772`) |
| `1773` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1773`) |
| `1774` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1774`) |
| `1775` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1775`) |
| `1776` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1776`) |
| `1777` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1777`) |
| `1778` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1778`) |
| `1780` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1780`) |
| `1781` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1781`) |
| `1782` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1782`) |
| `1783` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1783`) |
| `1784` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1784`) |
| `1785` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1785`) |
| `1786` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1786`) |
| `1787` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1787`) |
| `1788` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1788`) |
| `1790` | `true` | **Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1790`) |
| `1791` | `true` | **Manufacturer id** | `String` | `00000000` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1791`) |
| `1792` | `true` | **Manufacturer id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1792`) |
| `1793` | `true` | **Manufacturer id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1793`) |
| `1794` | `true` | **Beacon id offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1794`) |
| `1795` | `true` | **Beacon id size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1795`) |
| `1796` | `true` | **Aditional data offset** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1796`) |
| `1797` | `true` | **Aditional data size** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1797`) |
| `1798` | `true` | **Beacon id source** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=1798`) |
| `2000` | `true` | **GPRS Context** | `Byte` | `1` | `1` | `gprs.enabled` | `setparam` / `getparam` (`param=2000`) |
| `2001` | `true` | **APN** | `String` | `internet` | `m2m.sim1` | `gprs.apn` | `setparam` / `getparam` (`param=2001`) |
| `2002` | `true` | **APN Username** | `String` | `—` | `internet` | `gprs.username` | `setparam` / `getparam` (`param=2002`) |
| `2003` | `true` | **APN Password** | `String` | `—` | `internet` | `gprs.password` | `setparam` / `getparam` (`param=2003`) |
| `2004` | `true` | **Domain** | `String` | `—` | `203.0.113.10` | `gprs_server.host` | `setparam` / `getparam` (`param=2004`) |
| `2005` | `true` | **Port** | `Int32` | `—` | `20332` | `gprs_server.port` | `setparam` / `getparam` (`param=2005`) |
| `2006` | `true` | **Protocol** | `Byte` | `0` | `0` | `gprs_server.protocol` | `setparam` / `getparam` (`param=2006`) |
| `2007` | `true` | **Backup Server Domain** | `String` | `—` | `ch0000000.flespi.gw` | `backup_server_fmb640.mode` | `setparam` / `getparam` (`param=2007`) |
| `2008` | `true` | **Backup Server Port** | `Int32` | `—` | `20001` | `backup_server_fmb640.host` | `setparam` / `getparam` (`param=2008`) |
| `2009` | `true` | **Backup server protocol** | `Byte` | `0` | `0` | `backup_server_fmb640.port` | `setparam` / `getparam` (`param=2009`) |
| `2010` | `true` | **Backup server mode** | `Byte` | `2` | `2` | `backup_server_fmb640.protocol` | `setparam` / `getparam` (`param=2010`) |
| `2011` | `true` | **GPRS Context** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2011`) |
| `2012` | `true` | **APN** | `String` | `—` | `m2m.sim2` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2012`) |
| `2013` | `true` | **APN Username** | `String` | `—` | `internet` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2013`) |
| `2014` | `true` | **APN Password** | `String` | `—` | `internet` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2014`) |
| `2015` | `true` | **Device Id** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2015`) |
| `2016` | `true` | **GPRS authentication** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2016`) |
| `2017` | `true` | **GPRS authentication** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2017`) |
| `2020` | `true` | **TLS Encryption** | `Byte` | `0` | `0` | `tls.enable` | `setparam` / `getparam` (`param=2020`) |
| `2022` | `true` | **GPRS Limits** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2022`) |
| `2023` | `true` | **Home Limit** | `Int32` | `100` | `50` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2023`) |
| `2024` | `true` | **Roaming Limit** | `Int32` | `10` | `25` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2024`) |
| `2027` | `true` | **Primary SAS key** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2027`) |
| `2028` | `true` | **Secondary SAS key** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2028`) |
| `2029` | `true` | **SAS Policy Name** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2029`) |
| `2035` | `true` | **MQTT Client mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=2035`) |
| `3003` | `true` | **Login** | `String` | `—` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3003`) |
| `3004` | `true` | **Password** | `String` | `—` | `DEMO1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3004`) |
| `3005` | `true` | **Incoming Call Action** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3005`) |
| `3006` | `true` | **SMS Event Time Zone** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3006`) |
| `3009` | `true` | **Din 1 Call Trigger** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3009`) |
| `3010` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3010`) |
| `3011` | `true` | **Din 2 Call Trigger** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3011`) |
| `3012` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3012`) |
| `3013` | `true` | **Din 3 Call Trigger** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3013`) |
| `3014` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3014`) |
| `3015` | `true` | **Din 4 Call Trigger** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3015`) |
| `3016` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=3016`) |
| `7000` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7000`) |
| `7001` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7001`) |
| `7002` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7002`) |
| `7003` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7003`) |
| `7004` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7004`) |
| `7005` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7005`) |
| `7006` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7006`) |
| `7007` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7007`) |
| `7008` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7008`) |
| `7009` | `true` | **GSM Number** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7009`) |
| `7500` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7500`) |
| `7501` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7501`) |
| `7502` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7502`) |
| `7503` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7503`) |
| `7504` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7504`) |
| `7505` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7505`) |
| `7506` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7506`) |
| `7507` | `true` | **Send SMS To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=7507`) |
| `8500` | `true` | **SMS Text** | `String` | `Green Driving` | `Green Driving` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8500`) |
| `8501` | `true` | **SMS Text** | `String` | `Overspeeding` | `Overspeeding` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8501`) |
| `8502` | `true` | **SMS Text** | `String` | `Immobilizer` | `Immobilizer` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8502`) |
| `8503` | `true` | **SMS Text** | `String` | `Idling Event` | `Idling Event` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8503`) |
| `8504` | `true` | **SMS Text** | `String` | `Towing` | `Towing` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8504`) |
| `8505` | `true` | **SMS Text** | `String` | `Crash` | `Crash` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8505`) |
| `8506` | `true` | **SMS Text** | `String` | `AutoGeofence` | `AutoGeofence` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8506`) |
| `8507` | `true` | **SMS Text** | `String` | `Trip` | `Trip` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=8507`) |
| `9000` | `true` | **SMS Event 1 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9000`) |
| `9001` | `true` | **SMS Event 2 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9001`) |
| `9002` | `true` | **SMS Event 3 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9002`) |
| `9003` | `true` | **SMS Event 4 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9003`) |
| `9004` | `true` | **SMS Event 5 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9004`) |
| `9005` | `true` | **SMS Event 6 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9005`) |
| `9006` | `true` | **SMS Event 7 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9006`) |
| `9007` | `true` | **SMS Event 8 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9007`) |
| `9008` | `true` | **SMS Event 9 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9008`) |
| `9009` | `true` | **SMS Event 10 AVL ID** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=9009`) |
| `10000` | `true` | **Min Period Home** | `Int32` | `3600` | `60` | `home_network.on_stop` (`min_period`) | `setparam` / `getparam` (`param=10000`) |
| `10004` | `true` | **Min Saved Records Home** | `Int32` | `1` | `1` | `home_network.on_stop` (`min_saved_records`) | `setparam` / `getparam` (`param=10004`) |
| `10005` | `true` | **Send Period Home** | `Int32` | `120` | `60` | `home_network.on_stop` (`send_period`) | `setparam` / `getparam` (`param=10005`) |
| `10050` | `true` | **Min Period Home** | `Int32` | `300` | `30` | `home_network.on_move` (`min_period`) | `setparam` / `getparam` (`param=10050`) |
| `10051` | `true` | **Min Distance Home** | `Int32` | `100` | `100` | `home_network.on_move` (`min_distance`) | `setparam` / `getparam` (`param=10051`) |
| `10052` | `true` | **Min Angle Home** | `Int32` | `10` | `10` | `home_network.on_move` (`min_angle`) | `setparam` / `getparam` (`param=10052`) |
| `10053` | `true` | **Min Speed Delta Home** | `Int32` | `10` | `10` | `home_network.on_move` (`min_speed_delta`) | `setparam` / `getparam` (`param=10053`) |
| `10054` | `true` | **Min Saved Records Home** | `Int32` | `1` | `1` | `home_network.on_move` (`min_saved_records`) | `setparam` / `getparam` (`param=10054`) |
| `10055` | `true` | **Send Period Home** | `Int32` | `120` | `30` | `home_network.on_move` (`send_period`) | `setparam` / `getparam` (`param=10055`) |
| `10100` | `true` | **Min Period Roaming** | `Int32` | `3600` | `60` | `roaming_network.on_stop` (`min_period`) | `setparam` / `getparam` (`param=10100`) |
| `10104` | `true` | **Min Saved Records Roaming** | `Int32` | `1` | `1` | `roaming_network.on_stop` (`min_saved_records`) | `setparam` / `getparam` (`param=10104`) |
| `10105` | `true` | **Send Period Roaming** | `Int32` | `120` | `60` | `roaming_network.on_stop` (`send_period`) | `setparam` / `getparam` (`param=10105`) |
| `10150` | `true` | **Min Period Roaming** | `Int32` | `300` | `30` | `roaming_network.on_move` (`min_period`) | `setparam` / `getparam` (`param=10150`) |
| `10151` | `true` | **Min Distance Roaming** | `Int32` | `100` | `100` | `roaming_network.on_move` (`min_distance`) | `setparam` / `getparam` (`param=10151`) |
| `10152` | `true` | **Min Angle Roaming** | `Int32` | `10` | `10` | `roaming_network.on_move` (`min_angle`) | `setparam` / `getparam` (`param=10152`) |
| `10153` | `true` | **Min Speed Delta Roaming** | `Int32` | `10` | `10` | `roaming_network.on_move` (`min_speed_delta`) | `setparam` / `getparam` (`param=10153`) |
| `10154` | `true` | **Min Saved Records Roaming** | `Int32` | `1` | `1` | `roaming_network.on_move` (`min_saved_records`) | `setparam` / `getparam` (`param=10154`) |
| `10155` | `true` | **Send Period Roaming** | `Int32` | `120` | `30` | `roaming_network.on_move` (`send_period`) | `setparam` / `getparam` (`param=10155`) |
| `10200` | `true` | **Min Period Unknown** | `Int32` | `3600` | `60` | `unknown_network.on_stop` (`min_period`) | `setparam` / `getparam` (`param=10200`) |
| `10204` | `true` | **Min Saved Records Unknown** | `Int32` | `1` | `1` | `unknown_network.on_stop` (`min_saved_records`) | `setparam` / `getparam` (`param=10204`) |
| `10205` | `true` | **Send Period Unknown** | `Int32` | `120` | `60` | `unknown_network.on_stop` (`send_period`) | `setparam` / `getparam` (`param=10205`) |
| `10250` | `true` | **Min Period Unknown** | `Int32` | `300` | `30` | `unknown_network.on_move` (`min_period`) | `setparam` / `getparam` (`param=10250`) |
| `10251` | `true` | **Min Distance Unknown** | `Int32` | `100` | `100` | `unknown_network.on_move` (`min_distance`) | `setparam` / `getparam` (`param=10251`) |
| `10252` | `true` | **Min Angle Unknown** | `Int32` | `10` | `10` | `unknown_network.on_move` (`min_angle`) | `setparam` / `getparam` (`param=10252`) |
| `10253` | `true` | **Min Speed Delta Unknown** | `Int32` | `10` | `10` | `unknown_network.on_move` (`min_speed_delta`) | `setparam` / `getparam` (`param=10253`) |
| `10254` | `true` | **Min Saved Records Unknown** | `Int32` | `1` | `1` | `unknown_network.on_move` (`min_saved_records`) | `setparam` / `getparam` (`param=10254`) |
| `10255` | `true` | **Send Period Unknown** | `Int32` | `120` | `30` | `unknown_network.on_move` (`send_period`) | `setparam` / `getparam` (`param=10255`) |
| `10990` | `true` | **Period** | `Int32` | `10` | `10` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=10990`) |
| `10991` | `true` | **Duration** | `Int32` | `600` | `600` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=10991`) |
| `10992` | `true` | **Activation by:** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=10992`) |
| `10993` | `true` | **Activation by:** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=10993`) |
| `11000` | `true` | **Scenario Settings** | `Byte` | `0` | `2` | `green_driving.prio` | `setparam` / `getparam` (`param=11000`) |
| `11001` | `true` | **DOUT ON Duration** | `Int32` | `200` | `3000` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11001`) |
| `11002` | `true` | **DOUT OFF Duration** | `Int32` | `200` | `3000` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11002`) |
| `11003` | `true` | **Output Control** | `Byte` | `1` | `3` | `green_driving.output` | `setparam` / `getparam` (`param=11003`) |
| `11004` | `true` | **Max Acceleration** | `Double` | `2.2` | `3.3` | `green_driving.max_accel` | `setparam` / `getparam` (`param=11004`) |
| `11005` | `true` | **Max Braking** | `Double` | `2.5` | `3.5` | `green_driving.max_brake` | `setparam` / `getparam` (`param=11005`) |
| `11006` | `true` | **Max Cornering** | `Double` | `2.1` | `2.9` | `green_driving.max_angle` | `setparam` / `getparam` (`param=11006`) |
| `11007` | `true` | **Source** | `Byte` | `1` | `1` | `green_driving.source` | `setparam` / `getparam` (`param=11007`) |
| `11008` | `true` | **Eco/Green driving duration** | `Byte` | `0` | `1` | `green_driving.duration` | `setparam` / `getparam` (`param=11008`) |
| `11011` | `true` | **Eco driving average** | `Byte` | `0` | `0` | `green_driving.cornering_duration` | `setparam` / `getparam` (`param=11011`) |
| `11015` | `true` | **Eco driving maximum** | `Byte` | `0` | `0` | `green_driving.eco_maximum` | `setparam` / `getparam` (`param=11015`) |
| `11019` | `true` | **Advanced Eco Driving** | `Byte` | `0` | `0` | `green_driving.advanced_eco` | `setparam` / `getparam` (`param=11019`) |
| `11100` | `true` | **Scenario Settings** | `Byte` | `0` | `1` | `overspeeding_dout4.prio` | `setparam` / `getparam` (`param=11100`) |
| `11101` | `true` | **DOUT ON Duration** | `Int32` | `200` | `200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11101`) |
| `11102` | `true` | **DOUT OFF Duration** | `Int32` | `200` | `200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11102`) |
| `11103` | `true` | **Output Control** | `Byte` | `1` | `3` | `overspeeding_dout4.output` | `setparam` / `getparam` (`param=11103`) |
| `11104` | `true` | **Max Speed** | `Int32` | `90` | `90` | `overspeeding_dout4.max_speed` | `setparam` / `getparam` (`param=11104`) |
| `11200` | `true` | **Scenario settings** | `Byte` | `0` | `1` | `idling_dout3.prio` | `setparam` / `getparam` (`param=11200`) |
| `11201` | `true` | **DOUT ON Duration** | `Int32` | `200` | `200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11201`) |
| `11202` | `true` | **DOUT OFF Duration** | `Int32` | `200` | `200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11202`) |
| `11203` | `true` | **Eventual Records** | `Byte` | `1` | `1` | `idling_dout3.record` | `setparam` / `getparam` (`param=11203`) |
| `11204` | `true` | **Output Control** | `Byte` | `1` | `1` | `idling_dout3.output` | `setparam` / `getparam` (`param=11204`) |
| `11205` | `true` | **Time To Stoped** | `Int32` | `300` | `300` | `idling_dout3.stop_time` | `setparam` / `getparam` (`param=11205`) |
| `11206` | `true` | **Time To Moving** | `Int32` | `5` | `5` | `idling_dout3.move_time` | `setparam` / `getparam` (`param=11206`) |
| `11207` | `true` | **Start speed threshold** | `Int32` | `16` | `16` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11207`) |
| `11208` | `true` | **Stop speed threshold** | `Int32` | `20` | `20` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11208`) |
| `11300` | `true` | **Scenario Settings** | `Byte` | `0` | `2` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11300`) |
| `11301` | `true` | **DOUT ON Duration** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11301`) |
| `11302` | `true` | **DOUT OFF Duration** | `Int32` | `200` | `200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11302`) |
| `11303` | `true` | **Eventual Records** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11303`) |
| `11304` | `true` | **Output Control** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11304`) |
| `11305` | `true` | **Time until jamming event detection** | `Int32` | `60` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11305`) |
| `11306` | `true` | **Sensitivity** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11306`) |
| `11309` | `true` | **DOUT Hold Delay Duration** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11309`) |
| `11400` | `true` | **Scenario Settings** | `Byte` | `0` | `2` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11400`) |
| `11401` | `true` | **Duration** | `Int32` | `5` | `50` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11401`) |
| `11402` | `true` | **Threshold** | `Int32` | `1500` | `2200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11402`) |
| `11406` | `true` | **Crash Trace** | `Int32` | `0` | `2` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11406`) |
| `11410` | `true` | **Make Call To** | `Byte` | `100` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11410`) |
| `11412` | `true` | **Trace Filter** | `Byte` | `0` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11412`) |
| `11600` | `true` | **Scenario Settings** | `Byte` | `0` | `2` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11600`) |
| `11601` | `true` | **Eventual Records** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11601`) |
| `11602` | `true` | **Activate Timeout** | `Int32` | `5` | `3` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11602`) |
| `11603` | `true` | **Event Timeout** | `Int32` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11603`) |
| `11604` | `true` | **Make Call To** | `Byte` | `—` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11604`) |
| `11605` | `true` | **Threshold** | `Double` | `0.22` | `0.28` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11605`) |
| `11606` | `true` | **Angle** | `Double` | `1.5` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11606`) |
| `11607` | `true` | **Duration** | `Int32` | `2000` | `1000` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11607`) |
| `11700` | `true` | **Scenario Settings** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11700`) |
| `11701` | `true` | **Eventual Records** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11701`) |
| `11702` | `true` | **Output Control** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11702`) |
| `11703` | `true` | **iButton List Check** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11703`) |
| `11704` | `true` | **Output Control** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11704`) |
| `11705` | `true` | **DOUT ON Duration** | `Int32` | `200` | `200` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11705`) |
| `11706` | `true` | **List Checking for Authorization** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11706`) |
| `11707` | `true` | **Ignition TMO** | `Int32` | `30` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11707`) |
| `11708` | `true` | **Depend On Ignition** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11708`) |
| `11713` | `true` | **Authorization TMO** | `Int32` | `30` | `30` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11713`) |
| `11717` | `true` | **DOUT Pre-Activation** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11717`) |
| `11800` | `true` | **Scenario settings** | `Byte` | `0` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11800`) |
| `11801` | `true` | **Eventual records** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11801`) |
| `11802` | `true` | **Mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11802`) |
| `11803` | `true` | **Start Speed** | `Int32` | `5` | `5` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11803`) |
| `11804` | `true` | **Ignition OFF Timeout** | `Int32` | `60` | `60` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11804`) |
| `11805` | `true` | **Remember iButton/RFID** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=11805`) |
| `12000` | `true` | **Digital Output Control** | `Byte` | `1` | `1` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12000`) |
| `12001` | `true` | **DOUT Deactivation Settings** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12001`) |
| `12002` | `true` | **Duration Timeout** | `Int32` | `5` | `5` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12002`) |
| `12450` | `true` | **Temperature sensor 1** | `LLS` | `0` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12450`) |
| `12451` | `true` | **Temperature sensor 2** | `LLS` | `0` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12451`) |
| `12452` | `true` | **Temperature sensor 3** | `LLS` | `0` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12452`) |
| `12453` | `true` | **Temperature sensor 4** | `LLS` | `0` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12453`) |
| `12454` | `true` | **1-wire mode** | `Byte` | `0` | `—` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12454`) |
| `12457` | `true` | **1-Wire Mode** | `Byte` | `0` | `0` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=12457`) |
| `13000` | `true` | **Main Server Domain** | `String` | `fm.teltonika.lt` | `fm.teltonika.lt` | — *(No dedicated Flespi setting)* | `setparam` / `getparam` (`param=13000`) |

---

## 4. Dual-Domain Bridge: Permanent & Eventual `IOItem` Configuration Blocks (`50000`–`50890`) vs Telemetry `AVL ID`s

In [`re/fmx65_03.01.01.Rev.15_schema.json`](./re/fmx65_03.01.01.Rev.15_schema.json), each telemetry I/O element has a **6-parameter Configuration Block (`IoId + 0..5`)** (`Priority`, `Operand`, `High`, `Low`, `Event Only`, `Average`). Only **12** of these `IoId` bases have a dedicated Flespi `*_io` setting; all others are configured via Flespi's `setio` command (`{"id": <IoId_Base>, ...}`). Meanwhile, when the FMC650 transmits the measured value in a telemetry packet, it uses the **Telemetry `AVL ID`**, which Flespi parses into a **Flespi Telemetry Message Parameter**.

| Config `IoId` Base (`re/`) | Config Parameter Block (`Priority..Average`) | Element Name in `re/` | Official Flespi Config Setting | Official Flespi Config Command | Corresponding Telemetry `AVL ID` | Official Flespi Telemetry Parameter |
|---:|---|---|---|---|---:|---|
| **`50000`** | `50000..50005` (6 fields) | **Ignition** | — *(None)* | `setio` (`id=50000`) | `239` | `engine.ignition.status` |
| **`50010`** | `50010..50015` (6 fields) | **Movement** | — *(None)* | `setio` (`id=50010`) | `240` | `movement.status` |
| **`50020`** | `50020..50024` (5 fields) | **Data Mode** | — *(None)* | `setio` (`id=50020`) | `80` | `data.mode.enum` |
| **`50030`** | `50030..50035` (6 fields) | **GSM Signal** | — *(None)* | `setio` (`id=50030`) | `21` | `gsm.signal.level` |
| **`50040`** | `50040..50044` (5 fields) | **Sleep Mode** | — *(None)* | `setio` (`id=50040`) | `200` | `sleep.mode.enum` |
| **`50050`** | `50050..50054` (5 fields) | **GNSS Status** | — *(None)* | `setio` (`id=50050`) | `69` | `gnss.state.enum` / `gnss.status` |
| **`50060`** | `50060..50065` (6 fields) | **GNSS PDOP** | — *(None)* | `setio` (`id=50060`) | `181` | `position.pdop` |
| **`50070`** | `50070..50075` (6 fields) | **GNSS HDOP** | — *(None)* | `setio` (`id=50070`) | `182` | `position.hdop` |
| **`50080`** | `50080..50085` (6 fields) | **External Voltage** | `external_voltage_io` | `setio` (`id=50080`) | `66` | `external.powersource.voltage` |
| **`50090`** | `50090..50095` (6 fields) | **Speed** | — *(None)* | `setio` (`id=50090`) | `24` | `position.speed` / `can.vehicle.speed` |
| **`50100`** | `50100..50104` (5 fields) | **GSM Cell ID** | — *(None)* | `setio` (`id=50100`) | `205` | `gsm.cellid` |
| **`50110`** | `50110..50114` (5 fields) | **GSM Area Code** | — *(None)* | `setio` (`id=50110`) | `206` | `gsm.lac` |
| **`50120`** | `50120..50125` (6 fields) | **Battery Voltage** | `battery_voltage_io` | `setio` (`id=50120`) | `67` | `battery.voltage` |
| **`50130`** | `50130..50135` (6 fields) | **Battery Current** | — *(None)* | `setio` (`id=50130`) | `68` | `battery.current` |
| **`50140`** | `50140..50144` (5 fields) | **Active GSM Operator** | — *(None)* | `setio` (`id=50140`) | `241` | `gsm.operator.code` |
| **`50150`** | `50150..50154` (5 fields) | **Trip Odometer** | `trip_odometer_io` | `setio` (`id=50150`) | `199` | `trip.mileage` |
| **`50160`** | `50160..50164` (5 fields) | **Total Odometer** | `odometer_io` | `setio` (`id=50160`) | `16` | `vehicle.mileage` |
| **`50170`** | `50170..50175` (6 fields) | **Digital Input 1** | `inputs1_io` | `setio` (`id=50170`) | `1` | `din.1` |
| **`50180`** | `50180..50185` (6 fields) | **Analog Input 1** | `analog_input1_io` | `setio` (`id=50180`) | `9` | `ain.1` |
| **`50190`** | `50190..50195` (6 fields) | **Digital Output 1** | — *(None)* | `setio` (`id=50190`) | `179` | `dout.1` |
| **`50220`** | `50220..50225` (6 fields) | **Axis X** | `axis_x` | `setio` (`id=50220`) | `17` | `axis.x` |
| **`50230`** | `50230..50235` (6 fields) | **Axis Y** | `axis_y` | `setio` (`id=50230`) | `18` | `axis.y` |
| **`50240`** | `50240..50245` (6 fields) | **Axis Z** | `axis_z` | `setio` (`id=50240`) | `19` | `axis.z` |
| **`50250`** | `50250..50254` (3 fields) | **ICCID** | — *(None)* | `setio` (`id=50250`) | `11` | `gsm.sim.iccid` |
| **`50260`** | `50260..50264` (5 fields) | **SD Status** | — *(None)* | `setio` (`id=50260`) | `144` | `sd.status` |
| **`50270`** | `50270..50275` (6 fields) | **Digital Input 2** | `inputs2_io` | `setio` (`id=50270`) | `2` | `din.2` |
| **`50280`** | `50280..50285` (6 fields) | **Digital Input 3** | `inputs3_io` | `setio` (`id=50280`) | `3` | `din.3` |
| **`50290`** | `50290..50295` (6 fields) | **Analog Input 2** | — *(None)* | `setio` (`id=50290`) | `10` | `ain.2` |
| **`50300`** | `50300..50305` (6 fields) | **Digital Output 2** | — *(None)* | `setio` (`id=50300`) | `180` | `dout.2` |
| **`50310`** | `50310..50315` (6 fields) | **Dallas Temperature 1** | — *(None)* | `setio` (`id=50310`) | `72` | `sensor.temperature.1` |
| **`50320`** | `50320..50325` (6 fields) | **Dallas Temperature 2** | — *(None)* | `setio` (`id=50320`) | `73` | `sensor.temperature.2` |
| **`50330`** | `50330..50335` (6 fields) | **Dallas Temperature 3** | — *(None)* | `setio` (`id=50330`) | `74` | `sensor.temperature.3` |
| **`50340`** | `50340..50345` (6 fields) | **Dallas Temperature 4** | — *(None)* | `setio` (`id=50340`) | `75` | `sensor.temperature.4` |
| **`50350`** | `50350..50354` (5 fields) | **Dallas Temperature ID 1** | — *(None)* | `setio` (`id=50350`) | `76` | `onewire.sensor.serial.1` |
| **`50360`** | `50360..50364` (5 fields) | **Dallas Temperature ID 2** | — *(None)* | `setio` (`id=50360`) | `77` | `onewire.sensor.serial.2` |
| **`50370`** | `50370..50374` (5 fields) | **Dallas Temperature ID 3** | — *(None)* | `setio` (`id=50370`) | `79` | `onewire.sensor.serial.3` |
| **`50380`** | `50380..50384` (5 fields) | **Dallas Temperature ID 4** | — *(None)* | `setio` (`id=50380`) | `71` | `onewire.sensor.serial.4` |
| **`50390`** | `50390..50395` (6 fields) | **iButton** | — *(None)* | `setio` (`id=50390`) | `78` | `ibutton.code` |
| **`50400`** | `50400..50405` (6 fields) | **RFID** | — *(None)* | `setio` (`id=50400`) | `207` | `rfid.code` |
| **`50410`** | `50410..50415` (6 fields) | **LLS 1 Fuel Level** | — *(None)* | `setio` (`id=50410`) | `201` | `lls.value.1` |
| **`50420`** | `50420..50425` (6 fields) | **LLS 2 Fuel Level** | — *(None)* | `setio` (`id=50420`) | `203` | `lls.value.2` |
| **`50430`** | `50430..50435` (6 fields) | **LLS 3 Fuel Level** | — *(None)* | `setio` (`id=50430`) | `210` | `lls.value.3` |
| **`50440`** | `50440..50445` (6 fields) | **LLS 4 Fuel Level** | — *(None)* | `setio` (`id=50440`) | `212` | `lls.value.4` |
| **`50450`** | `50450..50455` (6 fields) | **LLS 5 Fuel Level** | — *(None)* | `setio` (`id=50450`) | `214` | `lls.value.5` |
| **`50460`** | `50460..50465` (6 fields) | **LLS 1 Temperature** | — *(None)* | `setio` (`id=50460`) | `202` | `lls.temperature.1` |
| **`50470`** | `50470..50475` (6 fields) | **LLS 2 Temperature** | — *(None)* | `setio` (`id=50470`) | `204` | `lls.temperature.2` |
| **`50480`** | `50480..50485` (6 fields) | **LLS 3 Temperature** | — *(None)* | `setio` (`id=50480`) | `211` | `lls.temperature.3` |
| **`50490`** | `50490..50495` (6 fields) | **LLS 4 Temperature** | — *(None)* | `setio` (`id=50490`) | `213` | `lls.temperature.4` |
| **`50500`** | `50500..50505` (6 fields) | **LLS 5 Temperature** | — *(None)* | `setio` (`id=50500`) | `215` | `lls.temperature.5` |
| **`50530`** | `50530..50534` (5 fields) | **BLE Temp #1** | — *(None)* | `setio` (`id=50530`) | `—` | — |
| **`50540`** | `50540..50544` (5 fields) | **BLE Temp #2** | — *(None)* | `setio` (`id=50540`) | `—` | — |
| **`50550`** | `50550..50554` (5 fields) | **BLE Temp #3** | — *(None)* | `setio` (`id=50550`) | `—` | — |
| **`50560`** | `50560..50564` (5 fields) | **BLE Temp #4** | — *(None)* | `setio` (`id=50560`) | `—` | — |
| **`50570`** | `50570..50574` (5 fields) | **BLE Battery #1** | — *(None)* | `setio` (`id=50570`) | `—` | — |
| **`50580`** | `50580..50584` (5 fields) | **BLE Battery #2** | — *(None)* | `setio` (`id=50580`) | `—` | — |
| **`50590`** | `50590..50594` (5 fields) | **BLE Battery #3** | — *(None)* | `setio` (`id=50590`) | `—` | — |
| **`50600`** | `50600..50604` (5 fields) | **BLE Battery #4** | — *(None)* | `setio` (`id=50600`) | `—` | — |
| **`50610`** | `50610..50614` (5 fields) | **BLE Humidity #1** | — *(None)* | `setio` (`id=50610`) | `—` | — |
| **`50620`** | `50620..50624` (5 fields) | **BLE Humidity #2** | — *(None)* | `setio` (`id=50620`) | `—` | — |
| **`50630`** | `50630..50634` (5 fields) | **BLE Humidity #3** | — *(None)* | `setio` (`id=50630`) | `—` | — |
| **`50640`** | `50640..50644` (5 fields) | **BLE Humidity #4** | — *(None)* | `setio` (`id=50640`) | `—` | — |
| **`50650`** | `50650..50654` (5 fields) | **Network Type** | — *(None)* | `setio` (`id=50650`) | `263` | `gsm.network.type.enum` / `bt.status.enum` |
| **`50660`** | `50660..50665` (6 fields) | **Authorized iButton** | `inputs4_io` | `setio` (`id=50660`) | `4` | `din.4` |
| **`50670`** | `50670..50675` (6 fields) | **Pulse Counter DIN1** | — *(None)* | `setio` (`id=50670`) | `11` | `ain.3` |
| **`50680`** | `50680..50685` (6 fields) | **Pulse Counter DIN2** | — *(None)* | `setio` (`id=50680`) | `245` | `ain.4` |
| **`50690`** | `50690..50695` (6 fields) | **Battery Level** | — *(None)* | `setio` (`id=50690`) | `50` | `dout.3` |
| **`50700`** | `50700..50705` (6 fields) | **Digital Output 4** | — *(None)* | `setio` (`id=50700`) | `51` | `dout.4` |
| **`50710`** | `50710..50715` (6 fields) | **Digital Input 4** | — *(None)* | `setio` (`id=50710`) | `—` | — |
| **`50720`** | `50720..50725` (6 fields) | **BT Status** | — *(None)* | `setio` (`id=50720`) | `6` | `sensor.temperature.5` |
| **`50730`** | `50730..50735` (6 fields) | **1Wire Sensor Temperature 6** | — *(None)* | `setio` (`id=50730`) | `8` | `sensor.temperature.6` |
| **`50740`** | `50740..50744` (5 fields) | **1Wire Sensor Temperature ID 5** | — *(None)* | `setio` (`id=50740`) | `5` | `onewire.sensor.serial.5` |
| **`50750`** | `50750..50754` (5 fields) | **BLE LLS #1** | — *(None)* | `setio` (`id=50750`) | `7` | `onewire.sensor.serial.6` |
| **`50760`** | `50760..50764` (5 fields) | **PCB Temperature** | — *(None)* | `setio` (`id=50760`) | `—` | — |
| **`50770`** | `50770..50774` (5 fields) | **Fuel Counter** | — *(None)* | `setio` (`id=50770`) | `—` | — |
| **`50780`** | `50780..50785` (6 fields) | **BLE LLS #2** | — *(None)* | `setio` (`id=50780`) | `224` | `ultrasonic.fuel.level.1` |
| **`50790`** | `50790..50795` (6 fields) | **Ultrasonic UL202 Fuel Level 2** | — *(None)* | `setio` (`id=50790`) | `225` | `ultrasonic.fuel.level.2` |
| **`50800`** | `50800..50804` (5 fields) | **Ultrasonic UL202 Status 1** | — *(None)* | `setio` (`id=50800`) | `208` | `ultrasonic.software.state.enum.1` |
| **`50810`** | `50810..50814` (5 fields) | **BLE LLS #3** | — *(None)* | `setio` (`id=50810`) | `209` | `ultrasonic.software.state.enum.2` |
| **`50820`** | `50820..50824` (3 fields) | **IMSI** | — *(None)* | `setio` (`id=50820`) | `218` | `gsm.sim.imsi` |
