---
title: "FMC650 Telemetry Parameters (AVL ID) to Official Flespi Message Parameters Mapping"
device: "FMC650"
official_flespi_sources:
  - "https://flespi.com/devices/teltonika-fmc650"
  - "https://flespi.com/protocols/teltonika"
teltonika_avl_source: "Data_Sending_Parameters_ID"
captured: "2026-11-05"
---

# FMC650 Telemetry Parameters (`AVL ID`) to Official Flespi Message Parameters Mapping

This document maps **Teltonika FMC650 Telemetry Parameters (`Property ID in AVL packet` = `AVL ID`)** to their **Official Flespi Telemetry Message Parameters** as documented at [`https://flespi.com/devices/teltonika-fmc650`](https://flespi.com/devices/teltonika-fmc650) and [`https://flespi.com/protocols/teltonika`](https://flespi.com/protocols/teltonika).

> [!IMPORTANT]
> **Telemetry (`AVL ID`) vs Configuration (`ParameterId` / `IoId`)**:
> - Every ID in this document is a **Telemetry `AVL ID`** transmitted inside Codec 8 / Codec 8 Extended data packets.
> - **Never confuse an `AVL ID` with a `.cfg` Configuration `ParameterId` or `IoId` in `re/`!** For configuration parameter mappings, see [`01_FMC650_Configuration_Parameters_re_to_Flespi_Settings_Mapping.md`](./01_FMC650_Configuration_Parameters_re_to_Flespi_Settings_Mapping.md).

## 1. Summary of Official Flespi Coverage Across the 19 FMC650 Telemetry Sections

| Section # | FMC650 Telemetry Section | Total FMC650 `AVL ID` Rows | Mapped in Official Flespi Doc | Unmapped in Official Flespi Doc | Notes |
|---:|---|---:|---:|---:|---|
| `01` | `01_permanent-io-elements` | `93` | **`92`** | `1` | Partial official Flespi coverage |
| `02` | `02_fms-elements` | `55` | **`55`** | `0` | 100% official Flespi coverage |
| `03` | `03_can-adapters-elements` | `72` | **`53`** | `19` | Partial official Flespi coverage |
| `04` | `04_lv-can-elements` | `213` | **`0`** | `213` | LV-CAN 2-byte extended IDs (`12710..12922`); Flespi maps classic 1-byte CAN Adapter IDs (`81..152`) |
| `05` | `05_eventual-io-elements` | `127` | **`126`** | `1` | Partial official Flespi coverage |
| `06` | `06_manual-can-elements` | `70` | **`70`** | `0` | 100% official Flespi coverage |
| `07` | `07_tachograph-data-elements` | `79` | **`79`** | `0` | 100% official Flespi coverage |
| `08` | `08_mobileye-elements` | `39` | **`32`** | `7` | Partial official Flespi coverage |
| `09` | `09_contipressurecheck-tpms` | `75` | **`0`** | `75` | Partial official Flespi coverage |
| `10` | `10_reefer-io` | `47` | **`47`** | `0` | 100% official Flespi coverage |
| `11` | `11_tk-transcan-io` | `12` | **`12`** | `0` | 100% official Flespi coverage |
| `12` | `12_tk-euroscan-io` | `10` | **`4`** | `6` | Partial official Flespi coverage |
| `13` | `13_tk-touchprint-io` | `9` | **`0`** | `9` | Partial official Flespi coverage |
| `14` | `14_ev-fms-elements` | `26` | **`26`** | `0` | 100% official Flespi coverage |
| `15` | `15_cameras-video` | `6` | **`6`** | `0` | 100% official Flespi coverage |
| `16` | `16_isobus` | `298` | **`11`** | `287` | Partial official Flespi coverage |
| `17` | `17_ble` | `46` | **`46`** | `0` | 100% official Flespi coverage |
| `18` | `18_ev-fms` | `25` | **`25`** | `0` | 100% official Flespi coverage |
| `19` | `19_apache-thermograph` | `134` | **`20`** | `114` | Partial official Flespi coverage |

---

## 2. Complete Section-by-Section Mapping: FMC650 `AVL ID` -> Official Flespi Telemetry Parameter(s)

### Section `01_permanent-io-elements` (93 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`239`** | Ignition | `1 B` (`Unsigned`) | `-` (`×-`) | `engine.ignition.status` | `boolean` | Engine ignition or ACC status |
| **`240`** | Movement | `1 B` (`Unsigned`) | `-` (`×-`) | `movement.status` | `boolean` | Current movement state |
| **`22`** | Data Mode | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.battery.level`, `ble.sensor.battery.voltage`, `device.configuration.id`, `gsm.network.mode.enum`, `gsm.network.roaming.status` | `number` (`percentage`), `number` (`volts`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`21`** | GSM Signal | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `gsm.signal.level`, `overspeeding.status` | `boolean`, `number` (`percentage`) | Geofence entered status |
| **`200`** | Sleep Mode | `1 B` (`Unsigned`) | `-` (`×-`) | `sleep.mode.enum` | `number` | Protocol-specific value indicating device sleep mode state |
| **`71`** | GNSS Status | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance`, `gnss.antenna.short.circuit.status`, `gnss.antenna.status`, `gnss.sleep.mode.status`, `gnss.state.enum`, `gnss.status`, `onewire.sensor.serial`, `position.valid` | `number` (`lux`), `boolean` | BLE (Bluetooth Low Energy) sensor illuminance |
| **`181`** | GNSS PDOP | `2 B` (`Unsigned`) | `-` (`×0.1`) | `position.pdop` | `number` | Position dilution of precision |
| **`182`** | GNSS HDOP | `2 B` (`Unsigned`) | `-` (`×0.1`) | `position.hdop` | `number` | Horizontal dilution of precision |
| **`66`** | External Voltage | `2 B` (`Unsigned`) | `V` (`×0,001`) | `external.powersource.voltage` | `number` (`volts`) | External power voltage |
| **`24`** | Speed | `2 B` (`Unsigned`) | `km/h` (`×-`) | `position.speed` | `number` (`km/h`) | Instant speed at position detection moment |
| **`205`** | GSM Cell ID | `4 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`206`** | GSM Area Code | `2 B` (`Unsigned`) | `-` (`×-`) | `gsm.lac` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`67`** | Battery Voltage | `2 B` (`Unsigned`) | `V` (`×0,001`) | `battery.voltage` | `number` (`volts`) | Internal battery voltage |
| **`68`** | Battery Current | `2 B` (`Unsigned`) | `mA` (`×-`) | `battery.current` | `number` (`amperes`) | Battery current |
| **`241`** | Active GSM Operator | `4 B` (`Unsigned`) | `-` (`×-`) | `gsm.mcc`, `gsm.mnc`, `gsm.operator.code` | `number`, `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code |
| **`199`** | Trip Odometer | `4 B` (`Unsigned`) | `m` (`×-`) | `segment.vehicle.mileage` | `number` (`km`) | Segment mileage |
| **`216`** | Total Odometer | `4 B` (`Unsigned`) | `m` (`×-`) | `geofence.status`, `overspeeding.status`, `vehicle.mileage` | `boolean`, `boolean` | Geofence entered status |
| **`1`** | Digital Input 1 | `1 B` (`Unsigned`) | `-` (`×-`) | `din`, `din` | `number`, `number` | Digital inputs bitmask |
| **`9`** | Analog Input 1 | `2 B` (`Unsigned`) | `V` (`×0,001`) | `ain`, `geofence.status`, `overspeeding.status` | `number` (`volts`), `boolean` | Voltage on the analog input |
| **`179`** | Digital Output 1 | `1 B` (`Unsigned`) | `-` (`×-`) | `dout` | `number` | Digital outputs bitmask |
| **`236`** | Axis X | `2 B` (`Signed`) | `mG` (`×-`) | `alarm.event`, `x.acceleration` | `boolean`, `number` (`g`) | Alarm event triggered |
| **`237`** | Axis Y | `2 B` (`Signed`) | `mG` (`×-`) | `gsm.network.type`, `y.acceleration` | `string`, `number` (`g`) | The type of the Mobile network the device is currently registered to |
| **`238`** | Axis Z | `2 B` (`Signed`) | `mG` (`×-`) | `bluetooth.device.mac.address`, `z.acceleration` | `string`, `number` (`g`) | MAC address of bluetooth-connected peripheral device |
| **`219`** | CCID Part1 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`220`** | CCID Part2 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`221`** | CCID Part3 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `gsm.sim.iccid`, `overspeeding.status` | `boolean`, `string` | Geofence entered status |
| **`144`** | SD Status | `1 B` (`Unsigned`) | `-` (`×-`) | `sd.status`, `tacho.driver.activity.duration`, `tacho.driver.current.activity.duration` | `boolean`, `number` (`seconds`) | SD status presence |
| **`2`** | Digital Input 2 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.battery.level`, `ble.sensor.battery.voltage`, `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `can.axle.weight`, `din`, `din`, `din` | `number` (`percentage`), `number` (`volts`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`3`** | Digital Input 3 | `1 B` (`Unsigned`) | `-` (`×-`) | `din`, `din` | `number`, `number` | Digital inputs bitmask |
| **`10`** | Analog Input 2 | `2 B` (`Unsigned`) | `V` (`×0,001`) | `ain`, `sd.status` | `number` (`volts`), `boolean` | Voltage on the analog input |
| **`180`** | Digital Output 2 | `1 B` (`Unsigned`) | `-` (`×-`) | `dout` | `number` | Digital outputs bitmask |
| **`72`** | Dallas Temperature 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `ble.1.custom.payload.hex`, `ble.lls.fuel.level`, `ble.sensor.frequency`, `sensor.temperature`, `sensor.temperature`, `sensor.temperature.error.code` | `string`, `number` | Custom indexed element variable size payload for BLE sensor 1 |
| **`73`** | Dallas Temperature 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `ble.2.custom.payload.hex`, `ble.3.custom.payload.hex`, `sensor.temperature`, `sensor.temperature`, `sensor.temperature.error.code` | `string`, `string` | Custom indexed element variable size payload for BLE sensor 2 |
| **`74`** | Dallas Temperature 3 | `2 B` (`Signed`) | `°C` (`×0,1`) | `ble.4.custom.payload.hex`, `sensor.temperature`, `sensor.temperature`, `sensor.temperature.error.code` | `string`, `number` (`celsius`) | Custom indexed element variable size payload for BLE sensor 4 |
| **`75`** | Dallas Temperature 4 | `2 B` (`Signed`) | `°C` (`×0,1`) | `onewire.sensor.serial`, `sensor.temperature`, `sensor.temperature.error.code` | `string`, `number` (`celsius`) | External 1-Wire sensor serial number in HEX representation |
| **`62`** | Dallas Temperature ID 1 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `onewire.sensor.serial`, `overspeeding.status` | `boolean`, `string` | Geofence entered status |
| **`63`** | Dallas Temperature ID 2 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `onewire.sensor.serial`, `overspeeding.status` | `boolean`, `string` | Geofence entered status |
| **`64`** | Dallas Temperature ID 3 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `onewire.sensor.serial`, `overspeeding.status` | `boolean`, `string` | Geofence entered status |
| **`65`** | Dallas Temperature ID 4 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `onewire.sensor.serial`, `overspeeding.status` | `boolean`, `string` | Geofence entered status |
| **`78`** | iButton | `8 B` (`Unsigned`) | `-` (`×-`) | `ibutton.code` | `string` | Hexadecimal code of connected iButton |
| **`76`** | Fuel Counter | `4 B` (`Unsigned`) | `-` (`×-`) | `counter.impulses`, `onewire.sensor.serial` | `number`, `string` | Impulses counter |
| **`10640`** | Impulse counter frequency 1 | `4 B` (`Unsigned`) | `Hz` (`×-`) | `counter.impulses.frequency` | `number` (`hz`) | Impulses counter frequency |
| **`10641`** | Impulse counter RPM 1 | `4 B` (`Unsigned`) | `RPM` (`×-`) | `counter.impulses.rpm` | `number` (`rpm`) | Impulses counter RPM |
| **`483`** | Impulse Counter 2 | `4 B` (`Unsigned`) | `-` (`×-`) | `counter.impulses`, `ultrasonic.software.state`, `ultrasonic.software.state.enum` | `number`, `string` | Impulses counter |
| **`10642`** | Impulse counter frequency 2 | `4 B` (`Unsigned`) | `Hz` (`×-`) | `counter.impulses.frequency` | `number` (`hz`) | Impulses counter frequency |
| **`10643`** | Impulse counter RPM 2 | `4 B` (`Unsigned`) | `RPM` (`×-`) | `counter.impulses.rpm` | `number` (`rpm`) | Impulses counter RPM |
| **`10911`** | Impulse counter value 1 | `4 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10912`** | Impulse counter value 3 | `4 B` (`Unsigned`) | `-` (`×-`) | `counter.impulses` | `number` | Impulses counter |
| **`10913`** | Impulse counter frequency 3 | `4 B` (`Unsigned`) | `Hz` (`×-`) | `counter.impulses.frequency` | `number` (`hz`) | Impulses counter frequency |
| **`10914`** | Impulse counter RPM 3 | `4 B` (`Unsigned`) | `rpm` (`×-`) | `counter.impulses.rpm` | `number` (`rpm`) | Impulses counter RPM |
| **`10915`** | Impulse counter value 4 | `4 B` (`Unsigned`) | `-` (`×-`) | `counter.impulses` | `number` | Impulses counter |
| **`10916`** | Impulse counter frequency 4 | `4 B` (`Unsigned`) | `Hz` (`×-`) | `counter.impulses.frequency` | `number` (`hz`) | Impulses counter frequency |
| **`10917`** | Impulse counter RPM 4 | `4 B` (`Unsigned`) | `rpm` (`×-`) | `counter.impulses.rpm` | `number` (`rpm`) | Impulses counter RPM |
| **`207`** | RFID | `8 B` (`Unsigned`) | `-` (`×-`) | `rfid.code` | `string` | Hexadecimal code of connected RFID |
| **`201`** | LLS 1 Fuel Level | `2 B` (`Signed`) | `kvants or ltr` (`×-`) | `lls.value` | `number` | LLS (Liquid level sensor) fuel value |
| **`202`** | LLS 1 Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `lls.temperature` | `number` (`celsius`) | LLS (Liquid level sensor) fuel temperature |
| **`203`** | LLS 2 Fuel Level | `2 B` (`Signed`) | `kvants or ltr` (`×-`) | `lls.value` | `number` | LLS (Liquid level sensor) fuel value |
| **`204`** | LLS 2 Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `lls.temperature` | `number` (`celsius`) | LLS (Liquid level sensor) fuel temperature |
| **`210`** | LLS 3 Fuel Level | `2 B` (`Signed`) | `kvants or ltr` (`×-`) | `lls.value` | `number` | LLS (Liquid level sensor) fuel value |
| **`211`** | LLS 3 Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `lls.temperature` | `number` (`celsius`) | LLS (Liquid level sensor) fuel temperature |
| **`212`** | LLS 4 Fuel Level | `2 B` (`Signed`) | `kvants or ltr` (`×-`) | `lls.value` | `number` | LLS (Liquid level sensor) fuel value |
| **`213`** | LLS 4 Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `lls.temperature` | `number` (`celsius`) | LLS (Liquid level sensor) fuel temperature |
| **`214`** | LLS 5 Fuel Level | `2 B` (`Signed`) | `kvants or ltr` (`×-`) | `lls.value` | `number` | LLS (Liquid level sensor) fuel value |
| **`215`** | LLS 5 Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `lls.temperature` | `number` (`celsius`) | LLS (Liquid level sensor) fuel temperature |
| **`178`** | Network Type | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.network.type` | `string` | The type of the Mobile network the device is currently registered to |
| **`108`** | Number Of Records | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.humidity`, `ble.sensor.humidity.error.code`, `device.uptime.records.count` | `number` (`percentage`), `string` | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`4`** | Digital Input 4 | `1 B` (`Unsigned`) | `-` (`×-`) | `counter.impulses`, `din` | `number`, `number` | Impulses counter |
| **`50`** | Digital Output 3 | `1 B` (`Unsigned`) | `-` (`×-`) | `can.barometric.pressure`, `dout` | `number` (`kPa`), `number` | Absolute barometric pressure read from CAN |
| **`51`** | Digital Output 4 | `1 B` (`Unsigned`) | `-` (`×-`) | `can.control.module.voltage`, `dout` | `number` (`volts`), `number` | Control module voltage read from CAN |
| **`11`** | Analog Input 3 | `2 B` (`Unsigned`) | `V` (`×0,001`) | `ain`, `can.axle.weight`, `gsm.sim.iccid` | `number` (`volts`), `number` (`kg`) | Voltage on the analog input |
| **`245`** | Analog Input 4 | `2 B` (`Unsigned`) | `V` (`×0,001`) | `ain` | `number` (`volts`) | Voltage on the analog input |
| **`70`** | PCB Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `ble.sensor.battery.level`, `ble.sensor.humidity`, `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `geofence.status`, `overspeeding.status`, `pcb.temperature` | `number` (`percentage`), `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`5`** | Dallas Temperature ID 5 | `8 B` (`Unsigned`) | `-` (`×-`) | `counter.impulses`, `onewire.sensor.serial`, `tacho.driver.continuous_driving.duration`, `tacho.driver.cumulative_break.duration` | `number`, `string` | Impulses counter |
| **`6`** | Dallas Temperature 5 | `2 B` (`Signed`) | `°C` (`×0,1`) | `ain`, `geofence.status`, `onewire.sensor.serial`, `overspeeding.status`, `sensor.temperature`, `tacho.driver.activity.duration`, `tacho.driver.selected.activity.duration` | `number` (`volts`), `boolean` | Voltage on the analog input |
| **`7`** | Dallas Temperature ID 6 | `8 B` (`Unsigned`) | `-` (`×-`) | `onewire.sensor.serial`, `sensor.temperature`, `sensor.temperature.error.code` | `string`, `number` (`celsius`) | External 1-Wire sensor serial number in HEX representation |
| **`8`** | Dallas Temperature 6 | `2 B` (`Signed`) | `°C` (`×0,1`) | `can.axle.weight`, `sensor.temperature` | `number` (`kg`), `number` (`celsius`) | Weight on the axle read from CAN |
| **`217`** | RFID COM2 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `rfid.code` | `boolean`, `boolean` | Geofence entered status |
| **`218`** | IMSI | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `gsm.sim.imsi`, `overspeeding.status` | `boolean`, `string` | Geofence entered status |
| **`224`** | Ultrasonic Fuel Level 1 | `2 B` (`Signed`) | `mm` (`×0,1`) | `geofence.status`, `overspeeding.status`, `ultrasonic.fuel.level` | `boolean`, `boolean` | Geofence entered status |
| **`225`** | Ultrasonic Fuel Level 2 | `2 B` (`Signed`) | `mm` (`×0,1`) | `geofence.status`, `overspeeding.status`, `ultrasonic.fuel.level` | `boolean`, `boolean` | Geofence entered status |
| **`208`** | Ultrasonic Software Status 1 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `ultrasonic.software.state.enum` | `boolean`, `boolean` | Geofence entered status |
| **`209`** | Ultrasonic Software Status 2 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `ultrasonic.software.state.enum` | `boolean`, `boolean` | Geofence entered status |
| **`10009`** | Eco score | `2 B` (`Unsigned`) | `-` (`×0,01`) | `eco.driving.events.number` | `number` | Average amount of events on some distance |
| **`10487`** | 1Wire Humidity 1 | `1 B` (`Unsigned`) | `%` (`×-`) | `sensor.humidity` | `number` (`percentage`) | Humidity sensor value, i.e. relative air humidity level |
| **`10488`** | 1Wire Humidity 2 | `1 B` (`Unsigned`) | `%` (`×-`) | `sensor.humidity` | `number` (`percentage`) | Humidity sensor value, i.e. relative air humidity level |
| **`10489`** | 1Wire Humidity 3 | `1 B` (`Unsigned`) | `%` (`×-`) | `sensor.humidity` | `number` (`percentage`) | Humidity sensor value, i.e. relative air humidity level |
| **`10490`** | 1Wire Humidity 4 | `1 B` (`Unsigned`) | `%` (`×-`) | `sensor.humidity` | `number` (`percentage`) | Humidity sensor value, i.e. relative air humidity level |
| **`10491`** | 1Wire Humidity 5 | `1 B` (`Unsigned`) | `%` (`×-`) | `sensor.humidity` | `number` (`percentage`) | Humidity sensor value, i.e. relative air humidity level |
| **`10492`** | 1Wire Humidity 6 | `1 B` (`Unsigned`) | `%` (`×-`) | `sensor.humidity` | `number` (`percentage`) | Humidity sensor value, i.e. relative air humidity level |
| **`449`** | Ignition On Counter | `4 B` (`Unsigned`) | `s` (`×-`) | `engine.ignition.on.duration` | `number` (`seconds`) | Duration when engine is on |
| **`1161`** | IMEI | `8 B` (`HEX`) | `-` (`×-`) | `can.faulty.batteries`, `device.imei` | `number`, `string` | Faulty batteries from CAN bus |
| **`13200`** | No SIM Counter | `2 B` (`Unsigned`) | `-` (`×-`) | `sim.card.error.count` | `number` | Error counter for No Sim Card error |
| **`1148`** | Connectivity Quality | `4 B` (`Unsigned`) | `-` (`×-`) | `can.cluster.soc`, `gsm.signal.quality`, `network.signal.rsrp`, `network.signal.rssi`, `network.signal.sinr` | `number` (`percentage`), `number` | Cluster SoC from CAN bus |

### Section `02_fms-elements` (55 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`79`** | Brake Switch | `1 B` (`Unsigned`) | `-` (`×-`) | `can.pedal.brake.status`, `onewire.sensor.serial` | `boolean`, `string` | Footbrake pedal is depressed, read from CAN |
| **`80`** | Wheel Based Speed | `4 B` (`Unsigned`) | `km/h` (`×-`) | `can.wheel.speed`, `gsm.network.mode.enum`, `gsm.network.roaming.status` | `number` (`km/h`), `number` | Vehicle wheel based speed, read from CAN bus |
| **`81`** | Cruise Control Active | `1 B` (`Unsigned`) | `-` (`×-`) | `can.cruise.status`, `can.vehicle.speed` | `boolean`, `number` (`km/h`) | CAN cruise control is active |
| **`82`** | Clutch Switch | `1 B` (`Unsigned`) | `-` (`×-`) | `can.pedal.clutch.status`, `can.throttle.pedal.level` | `boolean`, `number` (`percentage`) | CAN clutch pedal pressed |
| **`83`** | PTO State | `1 B` (`Unsigned`) | `-` (`×-`) | `can.fuel.consumed`, `can.powersource.takeoff.enum` | `number` (`liters`), `number` | Fuel volume totally consumed by vehicle read from CAN |
| **`84`** | Acceleration Pedal Position | `4 B` (`Unsigned`) | `%` (`×-`) | `can.fuel.volume`, `can.throttle.pedal.level` | `number` (`liters`), `number` (`percentage`) | CAN fuel volume |
| **`85`** | Engine Current Load | `1 B` (`Unsigned`) | `%` (`×-`) | `can.engine.load.level`, `can.engine.rpm` | `number` (`percentage`), `number` (`rpm`) | Calculated engine load level read from CAN |
| **`86`** | Engine Total Fuel Used | `4 B` (`Unsigned`) | `l` (`×-`) | `ble.sensor.humidity`, `ble.sensor.humidity.error.code`, `can.fuel.consumed` | `number` (`percentage`), `string` | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`87`** | Fuel Level | `4 B` (`Unsigned`) | `%` (`×-`) | `can.vehicle.mileage`, `fuel.level` | `number` (`km`), `number` (`percentage`) | Total vehicle mileage read from CAN |
| **`88`** | Engine Speed | `4 B` (`Unsigned`) | `rpm` (`×-`) | `can.engine.rpm`, `geofence.status`, `overspeeding.status` | `number` (`rpm`), `boolean` | Engine RPM read from CAN |
| **`89`** | Axle weight 1 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.fuel.level` | `number` (`kg`), `number` (`percentage`) | Weight on the axle read from CAN |
| **`90`** | Axle weight 2 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.data.frame`, `can.front.left.door.status`, `can.front.right.door.status`, `can.hood.status`, `can.rear.left.door.status`, `can.rear.right.door.status`, `can.trunk.status`, `door.open.status` | `number` (`kg`), `string` | Weight on the axle read from CAN |
| **`91`** | Axle weight 3 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`92`** | Axle weight 4 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`93`** | Axle weight 5 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`94`** | Axle weight 6 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`95`** | Axle weight 7 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`96`** | Axle weight 8 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`97`** | Axle weight 9 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`98`** | Axle weight 10 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`99`** | Axle weight 11 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Weight on the axle read from CAN |
| **`100`** | Axle weight 12 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.program.id` | `number` (`kg`), `number` | Weight on the axle read from CAN |
| **`101`** | Axle weight 13 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.module.id` | `number` (`kg`), `number` | Weight on the axle read from CAN |
| **`102`** | Axle weight 14 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.engine.motorhours` | `number` (`kg`), `number` (`hours`) | Weight on the axle read from CAN |
| **`103`** | Axle weight 15 | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.counted.engine.motorhours`, `can.engine.motorhours` | `number` (`kg`), `number` (`hours`) | Weight on the axle read from CAN |
| **`104`** | Engine Total Hours Of Operation | `4 B` (`Unsigned`) | `h` (`×-`) | `ble.sensor.humidity`, `ble.sensor.humidity.error.code`, `engine.motorhours` | `number` (`percentage`), `string` | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`109`** | Software Version Supported | `4 B` (`Unsigned`) | `-` (`×-`) | `fms.software.version` | `string` | Issue level of FMS-standard document the software included into FMS gateway supports |
| **`110`** | Diagnostics Supported | `1 B` (`Unsigned`) | `-` (`×-`) | `can.engine.fuel.rate`, `fms.diagnostics.supported`, `segment.can.fuel.consumed` | `number` (`liters/h`), `number` | Engine fuel rate read from CAN |
| **`111`** | Requests Supported | `1 B` (`Unsigned`) | `-` (`×-`) | `can.adblue.level`, `fms.requests.supported` | `number` (`percentage`), `number` | AdBlue (diesel exhaust fluid) level read from CAN |
| **`113`** | Service Distance | `4 B` (`Signed`) | `km` (`×-`) | `battery.level`, `can.service.mileage` | `number` (`percentage`), `number` (`km`) | Internal battery level |
| **`122`** | Direction Indication | `1 B` (`Unsigned`) | `-` (`×-`) | `can.axle.weight`, `fms.movement.direction` | `number` (`kg`), `number` | Weight on the axle read from CAN |
| **`123`** | Tachograph Performance | `1 B` (`Unsigned`) | `-` (`×-`) | `can.abs.failure.indicator.status`, `can.airbag.indicator.status`, `can.air.condition.status`, `can.automatic.retarder.status`, `can.battery.indicator.status`, `can.check.engine.indicator.status`, `can.coolant.level.low.indicator.status`, `can.cruise.status`, `can.driver.seatbelt.indicator.status`, `can.electronic.power.control.status`, `can.eps.indicator.status`, `can.esp.indicator.status`, `can.esp.status`, `can.front.fog.lights.status`, `can.fuel.level.low.indicator.status`, `can.glow.plug.indicator.status`, `can.handbrake.indicator.status`, `can.high.beam.status`, `can.lights.failure.indicator.status`, `can.low.beam.status`, `can.maintenance.required.status`, `can.manual.retarder.status`, `can.oil.pressure.indicator.status`, `can.parking.lights.status`, `can.passenger.seatbelt.indicator.status`, `can.ready.to.drive.indicator.status`, `can.rear.fog.lights.status`, `can.soot.filter.indicator.status`, `can.stop.indicator.status`, `can.tire.pressure.low.status`, `can.warning.indicator.status`, `can.wear.brake.pads.indicator.status`, `fms.tacho.performance` | `boolean`, `boolean` | ABS failure indicator status read from CAN |
| **`124`** | Handling Info | `1 B` (`Unsigned`) | `-` (`×-`) | `agro.vehicle.state.bitmask`, `fms.handling.info` | `number`, `number` | Agricultural machinery flags |
| **`125`** | System Event | `1 B` (`Unsigned`) | `-` (`×-`) | `fms.system.event`, `harvest.duration` | `number`, `number` (`seconds`) | FMS system event |
| **`127`** | Engine Coolant Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `can.engine.coolant.temperature`, `grain.mowing.efficiency.meters2_h` | `number` (`celsius`), `number` (`m^2/h`) | Engine coolant temperature read from CAN |
| **`128`** | Ambient Air Temperature | `2 B` (`Signed`) | `°C` (`×-`) | `can.ambient.air.temperature`, `grain.mowing.volume.kg` | `number` (`celsius`), `number` (`kg`) | CAN ambient air temperature |
| **`135`** | Fuel Rate | `4 B` (`Unsigned`) | `l/h` (`×-`) | `can.fuel.consumption`, `tacho.position.speed` | `number` (`liters/h`), `number` (`km/h`) | Engine fuel rate read from CAN |
| **`136`** | Instantaneous Fuel Economy | `4 B` (`Unsigned`) | `km/l` (`×-`) | `can.fuel.economy`, `tacho.driver.card.status` | `number` (`km/liters`), `boolean` | CAN instantaneous fuel economy |
| **`137`** | PTO Drive Engagement | `1 B` (`Unsigned`) | `-` (`×-`) | `pto.drive.engagement.enum`, `tacho.driver.activity.state`, `tacho.driver.activity.state.enum`, `tacho.driver.work.state.enum` | `number`, `string` | PTO drive engagement. 0 - No PTO drive is engaged. 1 - At least one PTO drive is engaged, 2 - Error, 3 - Not available |
| **`138`** | High Resolution Engine Total Fuel Used | `4 B` (`Unsigned`) | `l or ml` (`×-`) | `fuel.consumed`, `tacho.driver.activity.state`, `tacho.driver.activity.state.enum`, `tacho.driver.work.state.enum` | `number` (`liters`), `string` | Fuel volume totally consumed by vehicle |
| **`139`** | Gross Combination Vehicle Weight | `4 B` (`Unsigned`) | `kg` (`×-`) | `tacho.driver.continuous_driving.duration`, `total.vehicle.weight` | `number` (`seconds`), `number` (`kg`) | Driver continuous driving time |
| **`229`** | AdBlue status | `1 B` (`Unsigned`) | `-` (`×-`) | `fms.adblue.state.enum`, `geofence.status`, `overspeeding.status` | `number`, `boolean` | FMS AdBlue status: 0 - Off, 1 - Cond. Red, 2 - Cond. Yellow, 3 - Cond. info |
| **`357`** | Brake Pedal Position | `1 B` (`Unsigned`) | `%` (`×-`) | `can.brake.pedal.level`, `segment.vehicle.mileage` | `number` (`percentage`), `number` (`km`) | Brake pedal push level read from CAN |
| **`10348`** | Fuel level 2 | `1 B` (`Unsigned`) | `%` (`×-`) | `fuel.level` | `number` (`percentage`) | Fuel level percentage |
| **`10349`** | MIL indicator | `1 B` (`Unsigned`) | `-` (`×-`) | `can.mil.status` | `boolean` | Malfunction indicator lamp status read from CAN |
| **`10428`** | Tell Tale 0 | `8 B` (`HEX`) | `-` (`×-`) | `can.battery.charging.indicator.state`, `can.brake.failure.indicator.state`, `can.cooling.air.conditioning.indicator.state`, `can.disabled.persons.indicator.state`, `can.engine.coolant.temperature.indicator.state`, `can.engine.oil.indicator.state`, `can.front.fog.light.indicator.state`, `can.fuel.level.indicator.state`, `can.hatch.open.indicator.state`, `can.hazard.warning.indicator.state`, `can.high.beam.indicator.state`, `can.low.beam.indicator.state`, `can.parking.brake.indicator.state`, `can.position.lights.indicator.state`, `can.turn.signals.indicator.state`, `fms.tell.tale` | `string`, `string` | Vehicle parameter for battery charging condition indicator read from CAN |
| **`10429`** | Tell Tale 1 | `8 B` (`HEX`) | `-` (`×-`) | `can.abs.failure.indicator.state`, `can.engine.coolant.level.indicator.state`, `can.engine.mil.indicator.state`, `can.engine.oil.level.indicator.state`, `can.engine.oil.temperature.indicator.state`, `can.malfunction.general.failure.indicator.state`, `can.park.heating.indicator.state`, `can.rear.fog.light.indicator.state`, `can.service.maintenance.indicator.state`, `can.steering.fluid.level.indicator.state`, `can.tire.failure.indicator.state`, `can.transmission.failure.indicator.state`, `can.transmission.fluid.temperature.indicator.state`, `can.windscreen.washer.fluid.indicator.state`, `can.worn.brake.linings.indicator.state`, `fms.tell.tale` | `string`, `string` | Vehicle parameter for anti-lock brake system failure indicator read from CAN |
| **`10430`** | Tell Tale 2 | `8 B` (`HEX`) | `-` (`×-`) | `can.adblue.level.indicator.state`, `can.articulation.indicator.state`, `can.brake.lights.indicator.state`, `can.bus.stop.brake.indicator.state`, `can.engine.compartment.temperature.indicator.state`, `can.engine.emission.failure.indicator.state`, `can.esc.indicator.state`, `can.height.control.indicator.state`, `can.kneeling.indicator.state`, `can.lowering.indicator.state`, `can.pram.request.indicator.state`, `can.raising.indicator.state`, `can.retarder.indicator.state`, `can.steering.failure.indicator.state`, `can.stop.request.indicator.state`, `fms.tell.tale` | `string`, `string` | Vehicle parameter for AdBlue level indicator read from CAN |
| **`10431`** | Tell Tale 3 | `8 B` (`HEX`) | `-` (`×-`) | `can.abs.trailer.indicator.state`, `can.adaptive.cruise.control.indicator.state`, `can.airbag.indicator.state`, `can.air.filter.clogged.indicator.state`, `can.auxiliary.air.pressure.indicator.state`, `can.ebs.indicator.state`, `can.ebs.trailer.indicator.state`, `can.emergency.braking.system.indicator.state`, `can.esc.switched.off.indicator.state`, `can.fuel.filter.pressure.indicator.state`, `can.lane.departure.indication.indicator.state`, `can.lane.departure.warning.off.indicator.state`, `can.seat.belt.indicator.state`, `can.tachograph.indication.indicator.state`, `can.trailer.connected.indicator.state`, `fms.tell.tale` | `string`, `string` | Vehicle parameter for ABS trailer indicator read from CAN |
| **`13259`** | Tell Tale 4 | `8 B` (`HEX`) | `-` (`×-`) | `can.adblue.tempering.indicator.state`, `can.battery.pack.cooling.indicator.state`, `can.battery.pack.indicator.state`, `can.battery.pack.temperature.indicator.state`, `can.engine.emission.filter.indicator.state`, `can.high.voltage.system.caution.indicator.state`, `can.motor.failures.indicator.state`, `can.motor.limited.performance.indicator.state`, `can.multiplex.system.indicator.state`, `fms.tell.tale` | `string`, `string` | Vehicle parameter for AdBlue tempering indicator read from CAN |
| **`10455`** | AdBlue level | `1 B` (`Unsigned`) | `%` (`×-`) | `can.adblue.level` | `number` (`percentage`) | AdBlue (diesel exhaust fluid) level read from CAN |
| **`10493`** | DTC DM1 | `4 B` (`Unsigned`) | `-` (`×-`) | `can.dtc` | `array` | Diagnostic trouble code array read from CAN May content list of OBDII codes or list of objects with codes. Standard object parameter names used: *standard* - Protocol standard (J1939, J1708(J1587), OBDII) *mid* - Message Identifier (J1708) *sid* - Subsystem Identifier (J1708) *fmi* - Failure Mode Identifier (J1939, J1708) *spn* - Suspect Parameter Number (J1939) *sa* - Source Address (J1939, OBDII) *oc* - Occurrence Count (J1939) *cm* - Conversion Method (J1939) *status* - Status of error code (active, pending, historical, permanent) |
| **`10494`** | DTC DM1 List | `Var B` (`ASCII`) | `-` (`×-`) | `can.dtc` | `array` | Diagnostic trouble code array read from CAN May content list of OBDII codes or list of objects with codes. Standard object parameter names used: *standard* - Protocol standard (J1939, J1708(J1587), OBDII) *mid* - Message Identifier (J1708) *sid* - Subsystem Identifier (J1708) *fmi* - Failure Mode Identifier (J1939, J1708) *spn* - Suspect Parameter Number (J1939) *sa* - Source Address (J1939, OBDII) *oc* - Occurrence Count (J1939) *cm* - Conversion Method (J1939) *status* - Status of error code (active, pending, historical, permanent) |
| **`10495`** | DTC DM2 | `4 B` (`Unsigned`) | `-` (`×-`) | `can.dtc` | `array` | Diagnostic trouble code array read from CAN May content list of OBDII codes or list of objects with codes. Standard object parameter names used: *standard* - Protocol standard (J1939, J1708(J1587), OBDII) *mid* - Message Identifier (J1708) *sid* - Subsystem Identifier (J1708) *fmi* - Failure Mode Identifier (J1939, J1708) *spn* - Suspect Parameter Number (J1939) *sa* - Source Address (J1939, OBDII) *oc* - Occurrence Count (J1939) *cm* - Conversion Method (J1939) *status* - Status of error code (active, pending, historical, permanent) |
| **`10496`** | DTC DM2 List | `Var B` (`ASCII`) | `-` (`×-`) | `can.dtc` | `array` | Diagnostic trouble code array read from CAN May content list of OBDII codes or list of objects with codes. Standard object parameter names used: *standard* - Protocol standard (J1939, J1708(J1587), OBDII) *mid* - Message Identifier (J1708) *sid* - Subsystem Identifier (J1708) *fmi* - Failure Mode Identifier (J1939, J1708) *spn* - Suspect Parameter Number (J1939) *sa* - Source Address (J1939, OBDII) *oc* - Occurrence Count (J1939) *cm* - Conversion Method (J1939) *status* - Status of error code (active, pending, historical, permanent) |

### Section `03_can-adapters-elements` (72 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`12`** | Program Number | `2 B` (`Unsigned`) | `-` (`×-`) | `can.program.id`, `fuel.consumed`, `gps.fuel.used` | `number`, `number` (`liters`) | CAN program number |
| **`13`** | Module ID | `8 B` (`Unsigned`) | `-` (`×-`) | `can.module.id`, `gps.fuel.rate` | `number`, `number` (`liters/h`) | CAN module ID |
| **`14`** | Engine Worktime | `4 B` (`Unsigned`) | `min` (`×-`) | `can.engine.motorhours`, `gsm.sim.iccid`, `manual.can`, `manual.can.hex` | `number` (`hours`), `string` | Total engine motorhours (engine work time) read from CAN |
| **`15`** | Engine Worktime (Counted) | `4 B` (`Unsigned`) | `min` (`×-`) | `can.engine.motorhours`, `eco.driving.events.number`, `geofence.status`, `overspeeding.status` | `number` (`hours`), `number` | Total engine motorhours (engine work time) read from CAN |
| **`16`** | Total Mileage (Counted) | `4 B` (`Unsigned`) | `m` (`×-`) | `can.tracker.counted.mileage`, `vehicle.mileage` | `number` (`km`), `number` (`km`) | CAN-bus mileage counted by tracker after plug in |
| **`17`** | Fuel Consumed (counted) | `4 B` (`Unsigned`) | `l` (`×0,1`) | `can.tracker.counted.fuel.consumed`, `x.acceleration` | `number` (`liters`), `number` (`g`) | Vehicle counted fuel consumed based on CAN-bus data |
| **`18`** | Fuel Rate | `2 B` (`Unsigned`) | `l/h` (`×0,1`) | `can.engine.fuel.rate`, `tacho.driver.time.state`, `tacho.driver.time.state.enum`, `y.acceleration` | `number` (`liters/h`), `string` | Engine fuel rate read from CAN |
| **`19`** | AdBlue Level Percent | `1 B` (`Unsigned`) | `%` (`×-`) | `ain`, `can.adblue.level`, `geofence.status`, `overspeeding.status`, `z.acceleration` | `number` (`volts`), `number` (`percentage`) | Voltage on the analog input |
| **`20`** | AdBlue Level Liters | `2 B` (`Unsigned`) | `l` (`×0,1`) | `ble.sensor.battery.level`, `ble.sensor.battery.voltage`, `can.adblue.volume`, `geofence.status`, `overspeeding.status` | `number` (`percentage`), `number` (`volts`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`23`** | Engine Load | `1 B` (`Unsigned`) | `%` (`×-`) | `absolute.acceleration`, `ble.sensor.battery.level`, `ble.sensor.battery.voltage`, `can.engine.load.level` | `number` (`g`), `number` (`percentage`) | Module of accelerometer vector |
| **`25`** | Engine Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `can.engine.temperature` | `number` (`celsius`), `string` | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`26`** | Axle 1 Load | `2 B` (`Unsigned`) | `kg` (`×-`) | `ble.sensor.temperature`, `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `can.axle.weight` | `number` (`celsius`), `number` (`celsius`) | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`27`** | Axle 2 Load | `2 B` (`Unsigned`) | `kg` (`×-`) | `ble.sensor.temperature`, `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `can.axle.weight` | `number` (`celsius`), `number` (`celsius`) | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`28`** | Axle 3 Load | `2 B` (`Unsigned`) | `kg` (`×-`) | `ble.sensor.temperature`, `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `can.axle.weight` | `number` (`celsius`), `number` (`celsius`) | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`29`** | Axle 4 Load | `2 B` (`Unsigned`) | `kg` (`×-`) | `ble.sensor.battery.level`, `ble.sensor.battery.voltage`, `can.axle.weight` | `number` (`percentage`), `number` (`volts`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`30`** | Vehicle Speed | `1 B` (`Unsigned`) | `km/h` (`×-`) | `ble.sensor.frequency`, `can.dtc.number`, `can.vehicle.speed` | `number`, `number` | Indexed BLE frequency sensor value |
| **`31`** | Accelerator Pedal Position | `1 B` (`Unsigned`) | `%` (`×-`) | `can.engine.load.level`, `can.throttle.pedal.level` | `number` (`percentage`), `number` (`percentage`) | Calculated engine load level read from CAN |
| **`32`** | Axle 5 Load | `2 B` (`Unsigned`) | `kg` (`×-`) | `can.axle.weight`, `can.engine.coolant.temperature`, `can.engine.temperature`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `number` (`celsius`) | Weight on the axle read from CAN |
| **`33`** | Fuel Consumed | `4 B` (`Unsigned`) | `l` (`×0,1`) | `ble.sensor.illuminance`, `can.fuel.consumed`, `can.short.fuel.trim` | `number` (`lux`), `number` (`liters`) | BLE (Bluetooth Low Energy) sensor illuminance |
| **`34`** | Fuel Level Liters | `2 B` (`Unsigned`) | `l` (`×0,1`) | `can.fuel.pressure`, `can.fuel.volume` | `number` (`kPa`), `number` (`liters`) | Fuel pressure read from CAN |
| **`35`** | Engine RPM | `2 B` (`Unsigned`) | `rpm` (`×-`) | `can.engine.rpm`, `can.intake.map`, `scenario.status` | `number` (`rpm`), `number` (`kPa`) | Engine RPM read from CAN |
| **`36`** | Total Mileage | `4 B` (`Unsigned`) | `m` (`×-`) | `can.engine.rpm`, `can.vehicle.mileage` | `number` (`rpm`), `number` (`km`) | Engine RPM read from CAN |
| **`37`** | Fuel Level Percent | `1 B` (`Unsigned`) | `%` (`×-`) | `can.fuel.level`, `can.vehicle.speed` | `number` (`percentage`), `number` (`km/h`) | Fuel level in tank read from CAN |
| **`38`** | Control State Flags | `4 B` (`Unsigned`) | `-` (`×-`) | `can.abs.failure.indicator.status`, `can.airbag.indicator.status`, `can.air.condition.status`, `can.automatic.retarder.status`, `can.battery.indicator.status`, `can.check.engine.indicator.status`, `can.coolant.level.low.indicator.status`, `can.cruise.status`, `can.driver.seatbelt.indicator.status`, `can.electronic.power.control.status`, `can.eps.indicator.status`, `can.esp.indicator.status`, `can.esp.status`, `can.front.fog.lights.status`, `can.fuel.level.low.indicator.status`, `can.glow.plug.indicator.status`, `can.handbrake.indicator.status`, `can.high.beam.status`, `can.lights.failure.indicator.status`, `can.low.beam.status`, `can.maintenance.required.status`, `can.manual.retarder.status`, `can.oil.pressure.indicator.status`, `can.parking.lights.status`, `can.passenger.seatbelt.indicator.status`, `can.ready.to.drive.indicator.status`, `can.rear.fog.lights.status`, `can.soot.filter.indicator.status`, `can.stop.indicator.status`, `can.timing.advance`, `can.tire.pressure.low.status`, `can.warning.indicator.status`, `can.wear.brake.pads.indicator.status`, `manual.can`, `manual.can.hex` | `boolean`, `boolean` | ABS failure indicator status read from CAN |
| **`39`** | Agricultural Machinery Flags | `8 B` (`Unsigned`) | `-` (`×-`) | `agro.vehicle.state.bitmask`, `can.intake.air.temperature`, `external.sensor.temperature` | `number`, `number` (`celsius`) | Agricultural machinery flags |
| **`40`** | Harvesting Time | `4 B` (`Unsigned`) | `min` (`×-`) | `can.maf.air.flow.rate`, `harvest.duration` | `number` (`g/sec`), `number` (`seconds`) | MAF air flow rate read from CAN |
| **`41`** | Area of Harvest | `4 B` (`Unsigned`) | `m2` (`×-`) | `can.throttle.pedal.level`, `harvest.area` | `number` (`percentage`), `number` (`m^2`) | Throttle pedal push level read from CAN |
| **`42`** | Mowing Efficiency | `4 B` (`Unsigned`) | `m2/h` (`×-`) | `can.engine.run.time`, `grain.mowing.efficiency.meters2_h` | `number` (`seconds`), `number` (`m^2/h`) | Run time since engine start read from CAN |
| **`43`** | Grain Mown Volume | `4 B` (`Unsigned`) | `kg` (`×-`) | `can.mil.mileage`, `grain.mowing.volume.kg` | `number` (`km`), `number` (`kg`) | Distance traveled while malfunction indicator lamp is activated, read from CAN |
| **`44`** | Grain Moisture | `2 B` (`Unsigned`) | `%` (`×0,1`) | `can.relative.fuel.rail.pressure`, `grain.moisture.level` | `number` (`kPa`), `number` (`percentage`) | Fuel rail pressure relative to manifold vacuum |
| **`45`** | Harvesting Drum RPM | `2 B` (`Unsigned`) | `rpm` (`×-`) | `ble.nbl2.button.1.status`, `ble.nbl2.button.2.status`, `ble.nbl2.rfid`, `can.direct.fuel.rail.pressure`, `harvest.drum.rpm` | `boolean`, `boolean` | BLE RFID reader Netronix NBL-2 button 1 status (4 programmable button states) |
| **`46`** | Gap Under Harvesting Drum | `1 B` (`Unsigned`) | `mm` (`×-`) | `ble.1.custom`, `ble.1.custom.payload.hex`, `ble.2.custom`, `ble.2.custom.payload.hex`, `can.commanded.egr`, `harvest.drum.gap` | `number`, `string` | Custom indexed element for BLE sensor 1 |
| **`47`** | Security State Flags | `8 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom`, `ble.3.custom.payload.hex`, `ble.4.custom`, `ble.4.custom.payload.hex`, `button.pressed.status`, `cable.connected.status`, `can.car.closed.remote.status`, `can.car.closed.status`, `can.connection.state`, `can.dynamic.ignition.status`, `can.egr.error`, `can.engine.ignition.status`, `can.engine.working.status`, `can.factory.armed.status`, `can.front.left.door.status`, `can.front.right.door.status`, `can.handbrake.status`, `can.hood.status`, `can.ignition.key.status`, `can.lights.hazard.lights.status`, `can.module.sleep.mode`, `can.parking.status`, `can.pedal.brake.status`, `can.private.status`, `can.rear.left.door.status`, `can.rear.right.door.status`, `can.reverse.gear.status`, `can.trunk.status`, `can.vehicle.battery.charging.status`, `can.webasto.status`, `car.remote.control.state`, `factory.alarm.actuated.status`, `factory.alarm.emulated.status`, `immobilizer.keys.status`, `immobilizer.service.status` | `number`, `string` | Custom indexed element for BLE sensor 3 |
| **`141`** | Battery Temperature | `2 B` (`Unsigned`) | `°C` (`×0,1`) | `battery.temperature`, `tacho.driver.cumulative_break.duration` | `number` (`celsius`), `number` (`seconds`) | Battery temperature |
| **`142`** | Battery Level Percent | `1 B` (`Unsigned`) | `%` (`×-`) | `battery.level`, `tacho.driver.cumulative_break.duration` | `number` (`percentage`), `number` (`seconds`) | Internal battery level |
| **`143`** | Door Status | `2 B` (`Unsigned`) | `-` (`×-`) | `can.front.left.door.status`, `can.front.right.door.status`, `can.hood.status`, `can.rear.left.door.status`, `can.rear.right.door.status`, `can.trunk.status`, `door.open.status`, `tacho.driver.activity.duration`, `tacho.driver.current.activity.duration` | `boolean`, `boolean` | CAN front left door is opened |
| **`176`** | DTC Errors | `1 B` (`Unsigned`) | `-` (`×-`) | `can.dtc.number` | `number` | Number of diagnostic trouble codes |
| **`226`** | CNG Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.cng.status`, `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Compressed natural gas status read from CAN |
| **`227`** | CNG Used | `4 B` (`Unsigned`) | `kg` (`×-`) | `can.cng.consumed`, `geofence.status`, `overspeeding.status` | `number` (`kg`), `boolean` | Consumed of compressed natural gas read from CAN |
| **`228`** | CNG Level | `2 B` (`Unsigned`) | `%` (`×-`) | `can.cng.level`, `geofence.status`, `overspeeding.status` | `number` (`percentage`), `boolean` | Compressed natural gas level read from CAN |
| **`500`** | Slope Of Arm | `2 B` (`Signed`) | `°` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`501`** | Rotation Of Arm | `2 B` (`Signed`) | `°` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`502`** | Eject Of Arm | `2 B` (`Unsigned`) | `m` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`503`** | Horizontal Distance Arm | `2 B` (`Unsigned`) | `m` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`504`** | Height Arm Above Ground | `2 B` (`Unsigned`) | `m` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`505`** | Drill RPM | `2 B` (`Unsigned`) | `rpm` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`506`** | Spread Salt | `2 B` (`Unsigned`) | `g/m2` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`507`** | Battery Voltage | `2 B` (`Unsigned`) | `V` (`×-`) | `can.battery.voltage` | `number` (`volts`) | Battery voltage read from CAN |
| **`508`** | Spread Fine Grained Salt | `4 B` (`Unsigned`) | `T` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`509`** | Coarse Grained Salt | `4 B` (`Unsigned`) | `T` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`510`** | Spread DiMix | `4 B` (`Unsigned`) | `T` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`511`** | Spread Coarse Grained Calcium | `4 B` (`Unsigned`) | `m2` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`512`** | Spread Calcium Chloride | `4 B` (`Unsigned`) | `m2` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`513`** | Spread Sodium Chloride | `4 B` (`Unsigned`) | `m2` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`514`** | Spread Magnesium Chloride, m2 | `4 B` (`Unsigned`) | `m2` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`515`** | Amount Of Spread Gravel | `4 B` (`Unsigned`) | `T` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`516`** | Amount Of Spread Sand | `4 B` (`Unsigned`) | `T` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`517`** | Width Pouring Left | `2 B` (`Unsigned`) | `m` (`×-`) | `cable.connected.status`, `can.car.closed.remote.status`, `can.car.closed.status`, `can.car.closing.remote.event`, `can.car.opening.remote.event`, `can.car.triple.closing.remote.event`, `can.cng.status`, `can.connection.state`, `can.drive.gear.status`, `can.engine.ignition.status`, `can.engine.lock.status`, `can.engine.working.status`, `can.factory.armed.status`, `can.front.left.door.status`, `can.front.right.door.status`, `can.handbrake.status`, `can.hood.status`, `can.ignition.key.status`, `can.interlock.active`, `can.lights.hazard.lights.status`, `can.module.sleep.mode`, `can.motor.status`, `can.neutral.gear.status`, `can.operator.present.status`, `can.parking.status`, `can.pedal.brake.status`, `can.pedal.clutch.status`, `can.private.status`, `can.ready.to.drive.indicator.status`, `can.rear.left.door.status`, `can.rearm.signal.event`, `can.rear.right.door.status`, `can.request.engine.lock.event`, `can.reverse.gear.status`, `can.roof.opened.status`, `can.standalone.engine`, `can.trunk.opening.remote.event`, `can.trunk.status`, `can.vehicle.battery.charging.status`, `can.webasto.status`, `factory.alarm.actuated.status`, `factory.alarm.emulated.status` | `boolean`, `boolean` | Charging cable connected status |
| **`518`** | Width Pouring Right | `2 B` (`Unsigned`) | `m` (`×-`) | `can.additional.front.lights.status`, `can.additional.rear.lights.status`, `can.air.condition.status`, `can.automatic.retarder.status`, `can.central.differential.4hi.status`, `can.central.differential.4lo.status`, `can.cruise.status`, `can.driver.seatbelt.status`, `can.front.differential.status`, `can.front.fog.lights.status`, `can.front.passenger.seatbelt.status`, `can.front.passenger.status`, `can.high.beam.status`, `can.light.signal.status`, `can.low.beam.status`, `can.manual.retarder.status`, `can.parking.lights.status`, `can.pto.status`, `can.rear.central.seatbelt.status`, `can.rear.differential.status`, `can.rear.fog.lights.status`, `can.rear.left.seatbelt.status`, `can.rear.right.seatbelt.status`, `can.trailer.axle.lift.status` | `boolean`, `boolean` | Additional front lights turned on status, read from CAN |
| **`519`** | Salt Spreader Working Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `can.abs.failure.indicator.status`, `can.adblue.level.low.indicator.status`, `can.airbag.indicator.status`, `can.air.filter.plugged.indicator.status`, `can.battery.indicator.status`, `can.brake.system.filter.clogged.indicator.status`, `can.cng.level.low.indicator.status`, `can.coolant.level.low.indicator.status`, `can.coolant.liquid.indicator.status`, `can.engine.oil.filter.plugged.indicator.status`, `can.engine.oil.temperature.high.indicator.status`, `can.epc.indicator.status`, `can.eps.indicator.status`, `can.esp.indicator.status`, `can.esp.status`, `can.fap.indicator.status`, `can.fuel.filter.plugged.indicator.status`, `can.fuel.low.indicator.status`, `can.glow.plug.indicator.status`, `can.handbrake.indicator.status`, `can.hydraulics.chamber.oil.overflow.indicator.status`, `can.hydraulics.high.temperature.status`, `can.hydraulics.oil.filter.plugged.indicator.status`, `can.hydraulics.oil.level.low.indicator.status`, `can.hydraulics.pressure.low.status`, `can.lights.failure.indicator.status`, `can.maintenance.required.status`, `can.mil.status`, `can.oil.level.low.indicator.status`, `can.oil.pressure.indicator.status`, `can.spreader.working.hours`, `can.stop.indicator.status`, `can.tire.pressure.low.status`, `can.trailer.brake.high.temperature.indicator.status`, `can.trailer.pneumatic.supply.incorrect.indicator.status`, `can.trailer.tire.pressure.low.status`, `can.trailer.wear.brake.lining.indicator.status`, `can.warning.indicator.status`, `can.washer.fluid.level.low.indicator.status`, `can.water.in.fuel.indicator.status`, `can.wear.brake.pads.indicator.status` | `boolean`, `boolean` | ABS failure indicator status read from CAN |
| **`520`** | Distance During Salting | `4 B` (`Unsigned`) | `km` (`×-`) | `can.cleaning.fan.control.status`, `can.corn.header.connected.status`, `can.ear.auger.speed.status`, `can.feeder.reverse.status`, `can.feeder.speed.status`, `can.front.hydraulic.status`, `can.front.pto.status`, `can.front.three.point.hitch.status`, `can.grain.auger.speed.status`, `can.grain.header.connected.status`, `can.grain.release.status`, `can.grain.tank.70.percent.event`, `can.grain.tank.full.event`, `can.grain.tank.opened.status`, `can.hydraulics.high.temperature.status`, `can.hydraulics.low.temperature.status`, `can.left.joystick.back.event`, `can.left.joystick.forward.event`, `can.left.joystick.left.event`, `can.left.joystick.right.event`, `can.mowing.status`, `can.pressure.filter.cloged.status`, `can.rear.hydraulic.status`, `can.rear.pto.status`, `can.rear.three.point.hitch.status`, `can.right.joystick.back.event`, `can.right.joystick.forward.event`, `can.right.joystick.left.event`, `can.right.joystick.right.event`, `can.straw.chopper.speed.status`, `can.straw.chopper.status`, `can.straw.shaker.speed.status`, `can.straw.walker.clogged.status`, `can.threshing.drum.control.status`, `can.threshing.drum.excessive.clearance.status`, `can.threshing.status`, `can.unloader.drive.status`, `tamper.alarm` | `boolean`, `boolean` | Cleaning fan control status: true - on, false - off, read from CAN |
| **`521`** | Load Weight | `4 B` (`Unsigned`) | `kg` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`522`** | Retarder Load | `1 B` (`Unsigned`) | `%` (`×-`) | `can.retarder.torque.load` | `number` (`percentage`) | Retarder torque load percentage read from CAN |
| **`523`** | Cruise Time | `4 B` (`Unsigned`) | `min` (`×-`) | `ble.sensor.battery.voltage`, `can.total.cruise.control.time` | `number` (`volts`), `number` (`hours`) | BLE (Bluetooth Low Energy) sensor battery voltage |
| **`524`** | Engine Oil Level | `1 B` (`Unsigned`) | `-` (`×-`) | `can.engine.oil.level` | `number` (`percentage`) | Engine oil level read from CAN |
| **`525`** | Fault Codes | `128 B` (`ASCII`) | `-` (`×-`) | `ble.sensor.humidity`, `ble.sensor.humidity.error.code`, `can.dtc` | `number` (`percentage`), `string` | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`526`** | Vehicles Range On Battery | `4 B` (`Unsigned`) | `m` (`×-`) | `can.vehicle.battery.range` | `number` (`km`) | Vehicle Range on Battery, read from CAN |
| **`527`** | Vehicles Range On Additional Fuel | `4 B` (`Unsigned`) | `m` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`528`** | VIN | `17 B` (`ASCII`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`529`** | Module ID 17B | `17 B` (`HEX`) | `-` (`×-`) | `can.module.id.hex` | `string` | CAN module ID in HEX format |
| **`10631`** | LVCAN Driver Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | `can.driver.seatbelt.status` | `boolean` | Driver's seatbelt fastened status, read from CAN |
| **`10632`** | LVCAN Front Passenger Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | `can.front.passenger.seatbelt.status` | `boolean` | Fron passenger's seatbelt fastened status, read from CAN |

### Section `04_lv-can-elements` (213 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`12710`** | Security State Flags P4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12711`** | Control State Flags P4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12712`** | Indicator State Flags P4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12713`** | SSF Ignition On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12714`** | Drive Right KeyInIgnition Lock | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12715`** | SSF Webasto | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12716`** | SSF Engine Working | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12717`** | SSF Standalone Engine | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12718`** | SSF Ready To Drive | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12719`** | SSF Engine Working On CNG | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12720`** | SSF Work Mode | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12721`** | SSF Operator | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12722`** | SSF Interlock | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12723`** | SSF Engine Lock Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12724`** | SSF Request To Lock Engine | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12725`** | Drive Right Handbrake Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12726`** | SSF Footbrake Actuated | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12727`** | SSF Clutch Pushed | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12728`** | SSF Hazard Warning Lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12729`** | Drive R Front L Door Opened | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12730`** | Drive R Rear L Door Opened | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12731`** | Drive R Rear R Door Opened | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12732`** | Drive R Trunk Door Opened | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12733`** | SSF Engine Cover Open | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12734`** | SSF Roof Open | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12735`** | SSF Charging Wire Plugged | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12736`** | SSF Battery Charging | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12737`** | SSF Electric Engine State | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12738`** | SSF Car Closed Factory Remote | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12739`** | Drive Right Car Closed | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12740`** | SSF Factory Alarm Actuated | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12741`** | SSF Factory Alarm Emulated | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12742`** | SSF Signal Close Factory Rem | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12743`** | SSF Signal Open Factory Rem | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12744`** | SSF Rearming Signal | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12745`** | SSF CAN Module In Sleep | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12746`** | SSF Factory Remote 3x | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12747`** | SSF Factory Armed | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12748`** | SSF Drive Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12749`** | Drive R Parking Gear Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12750`** | Drive R Reverse Gear Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12751`** | Drive R Neutral Gear Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12752`** | SSF EngineWork On Dual Fuel | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12753`** | SSF Engine Work On LPG | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12754`** | CSF Parking Lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12755`** | CSF Dipped Head lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12756`** | CSF Full Beam Head lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12757`** | CSF Rear Fog Lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12758`** | CSF Front Fog Lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12759`** | CSF Additional Front Lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12760`** | CSF Additional Rear Lights On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12761`** | CSF Light Signal On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12762`** | CSF Trailer Connected | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12763`** | CSF Air Cond On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12764`** | CSF Cruise Control On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12765`** | CSF Automatic Retarded On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12766`** | CSF Manual Retarded On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12767`** | CSF Driver Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12768`** | CSF Front Pass Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12769`** | CSF Rear Left Pass Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12770`** | CSF Rear Right Pass Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12771`** | CSF Rear Centre Pass Seatbelt | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12772`** | CSF Front Pass Present | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12773`** | CSF Start Stop System Inactive | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12774`** | CSF PTO | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12775`** | CSF Front Differential Locked | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12776`** | CSF Rear Differential Locked | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12777`** | CSF Central Diff4HI Locked | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12778`** | CSF Central Diff4LO Locked | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12779`** | CSF Trailer Axle1 Lift Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12780`** | CSF Trailer Axle2 Lift Active | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12781`** | ISF Check Engine On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12782`** | ISF ABS | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12783`** | ISF ESP Indicator | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12784`** | ISF ESP | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12785`** | ISF STOP | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12786`** | ISF Oil Level Indicator On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12787`** | ISF Coolant Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12788`** | ISF Battery Charging Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12789`** | ISF Handbrake System Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12790`** | ISF AIRBAG Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12791`** | ISF EPS Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12792`** | ISF Warning Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12793`** | ISF Light Failure Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12794`** | ISF Low Tire Press Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12795`** | ISF Wear Of Brake Pads Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12796`** | ISF Low Fuel Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12797`** | ISF Maintenance Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12798`** | ISF Glow Plug Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12799`** | ISF FAP Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12800`** | ISF EPC Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12801`** | ISF Engine Oil Filt Plug Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12802`** | ISF Low Engine Oil Press Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12803`** | ISF High Engine OilTemp Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12804`** | ISF Low Coolant Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12805`** | Hydraulic Sys High Temp Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12806`** | ISF Oil Over In Hdr Chamb Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12807`** | ISF Air Filter Is Plugged Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12808`** | ISF Fuel Filter Is Plugged Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12809`** | ISF Water In Fuel Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12810`** | ISF Clog Brk Sys Filt Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12811`** | ISF Low Washer Fluid Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12812`** | ISF Low AdBlue Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12813`** | ISF LowTrailer Tyre Press Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12814`** | ISF Wear Trail Brk Lining Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12815`** | ISF High Trailer Bk Temp Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12816`** | ISF Inc Trail Pneum Supp Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12817`** | ISF Low CNG Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12818`** | ASF Right Joystick Moved Right | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12819`** | ASF Right Joystick Moved Left | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12820`** | ASF Right Joystick Moved Frwd | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12821`** | ASF Right Joystick Moved Back | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12822`** | ASF Left Joystick Moved Right | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12823`** | ASF Left Joystick Moved Left | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12824`** | ASF Left Joystick Moved Frwd | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12825`** | ASF Left Joystick Moved Back | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12826`** | ASF First Rear Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12827`** | ASF Second Rear Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12828`** | ASF Third Rear Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12829`** | ASF Fourth Rear Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12830`** | ASF First Front Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12831`** | ASF Second Front Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12832`** | ASF Third Front Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12833`** | ASF Fourth Front Hydraulic On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12834`** | ASF Front Three Point Hitch On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12835`** | ASF Rear Three Point Hitch On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12836`** | ASF Front Power Take OffOn | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12837`** | ASF Rear Power Take OffOn | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12838`** | ASF Mowing On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12839`** | ASF Threshing On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12840`** | ASF Grain Releas Hopper On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12841`** | ASF Grain Tank 100 Proc | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12842`** | ASF Grain Tank 70 Proc | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12843`** | ASF Grain Tank Open | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12844`** | ASF Unloader Drive On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12845`** | ASF Cleaning Fan Ctrl On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12846`** | ASF Thresh Drum Ctrl On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12847`** | ASF Straw Walker Is Clogged | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12848`** | ASF Excessive Clearance Normal | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12849`** | ASF Low Temp Drive Sys Hydr | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12850`** | ASF High Temp Drive Sys Hydr | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12851`** | ASF Ear Auger Speed Normal | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12852`** | ASF GrainAugerSpeedNormal | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12853`** | ASF Straw Chop Spd Below Norm | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12854`** | ASF Straw Shak Spd Below Norm | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12855`** | ASF Feeder Speed Below Norm | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12856`** | ASF Straw Chopp Switched On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12857`** | ASF Corn Header Connected | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12858`** | ASF Grain Header Connected | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12859`** | ASF Feeder Reverse On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12860`** | ASF Hydr Pump Prs Flt Clogged | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12861`** | ASF Adapter Press Filter Sens | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12862`** | ASF Service2 Required Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12863`** | ASF Drain Filter Clogged Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12864`** | ASF Section1 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12865`** | ASF Section2 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12866`** | ASF Section3 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12867`** | ASF Section4 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12868`** | ASF Section5 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12869`** | ASF Section6 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12870`** | ASF Section7 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12871`** | ASF Section8 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12872`** | ASF Section9 Spraying | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12873`** | USF Salt Disperser On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12874`** | USF Pouring Chemicals On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12875`** | USF Conveyor Belt On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12876`** | USF Salt Spreader Drv Wheel On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12877`** | USF Brushes On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12878`** | USF Vacuum Cleaner On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12879`** | USF Water Supply On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12880`** | USF Karcher On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12881`** | USF Liquid Pump On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12882`** | USF Unloading Hopper On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12883`** | USF Low Salt Lvl In Cont Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12884`** | USF Low Water Lvl In Cont Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12885`** | USF Chemicals On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12886`** | USF Compressor On | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12887`** | USF Water Valve Opened | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12888`** | USF Cabin Moved Up Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12889`** | USF Cabin Moved Down Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12890`** | USF Hydrcs Work Not Permitted | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12891`** | CiSF Section1 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12892`** | CiSF Section1 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12893`** | CiSF Section1 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12894`** | CiSF Section2 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12895`** | CiSF Section2 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12896`** | CiSF Section2 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12897`** | CiSF Section3 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12898`** | CiSF Section3 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12899`** | CiSF Section3 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12900`** | CiSF Section4 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12901`** | CiSF Section4 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12902`** | CiSF Section4 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12903`** | CiSF Section5 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12904`** | CiSF Section5 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12905`** | CiSF Section5 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12906`** | CiSF Section6 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12907`** | CiSF Section6 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12908`** | CiSF Section6 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12909`** | CiSF Section7 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12910`** | CiSF Section7 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12911`** | CiSF Section7 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12912`** | CiSF Section8 Presence | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12913`** | CiSF Section8 Filled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12914`** | CiSF Section8 Overfilled | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12915`** | Drive R Front R Door Opened | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12916`** | ISF Hyd Sys Oil Filt Plugg Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12917`** | ISF Hydr Sys Low Press Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12918`** | ISF Hydr Oil Low Level Ind | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12919`** | SSF Trunk Door Open Factr Rem | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12920`** | Agricultural State Flags P4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12921`** | Utility State Flags P4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12922`** | Cistern State Flags P4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |

### Section `05_eventual-io-elements` (127 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`52`** | Tacho drive no card | `1 B` (`Unsigned`) | `-` (`×-`) | `can.absolute.load` | `number` (`percentage`) | Absolute load value - the normalized value of air mass per intake stroke, read from CAN |
| **`70`** | PCB Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `ble.sensor.battery.level`, `ble.sensor.humidity`, `ble.sensor.temperature`, `ble.sensor.temperature.error.code`, `geofence.status`, `overspeeding.status`, `pcb.temperature` | `number` (`percentage`), `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`155`** | Geofence zone 01 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.id`, `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` | `number`, `boolean` | Geofence ID |
| **`156`** | Geofence zone 02 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.entered.event`, `geofence.left.event`, `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` | `boolean`, `boolean` | Device entered geofence event |
| **`157`** | Geofence zone 03 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.overspeeding.status`, `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence overspeeding status |
| **`158`** | Geofence zone 04 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`159`** | Geofence zone 05 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `geofence.status`, `overspeeding.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`160`** | Geofence zone 06 | `1 B` (`Unsigned`) | `-` (`×-`) | `can.dtc.number`, `geofence.status`, `overspeeding.status` | `number`, `boolean` | Number of diagnostic trouble codes |
| **`161`** | Geofence zone 07 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`162`** | Geofence zone 08 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`163`** | Geofence zone 09 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`164`** | Geofence zone 10 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`165`** | Geofence zone 11 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`166`** | Geofence zone 12 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`167`** | Geofence zone 13 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`168`** | Geofence zone 14 | `1 B` (`Unsigned`) | `-` (`×-`) | `can.battery.voltage`, `geofence.status`, `overspeeding.status` | `number` (`volts`), `boolean` | Battery voltage read from CAN |
| **`169`** | Geofence zone 15 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`170`** | Geofence zone 16 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`171`** | Geofence zone 17 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`172`** | Geofence zone 18 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`173`** | Geofence zone 19 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`174`** | Geofence zone 20 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`177`** | Event Reserved01 | `- B` (`-`) | `-` (`×-`) | `idle.status` | `boolean` | Vehicle is in idling state |
| **`327`** | Geofence zone 21 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `ultrasonic.fuel.level` | `boolean`, `boolean` | Geofence entered status |
| **`328`** | Geofence zone 22 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`329`** | Geofence zone 23 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`330`** | Geofence zone 24 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`331`** | Geofence zone 25 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.1.custom`, `ble.1.custom.payload.hex`, `geofence.status`, `overspeeding.status` | `number`, `string` | Custom indexed element for BLE sensor 1 |
| **`332`** | Geofence zone 26 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.2.custom`, `ble.2.custom.payload.hex`, `geofence.status`, `overspeeding.status` | `number`, `string` | Custom indexed element for BLE sensor 2 |
| **`333`** | Geofence zone 27 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom`, `ble.3.custom.payload.hex`, `geofence.status`, `overspeeding.status` | `number`, `string` | Custom indexed element for BLE sensor 3 |
| **`334`** | Geofence zone 28 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.4.custom`, `ble.4.custom.payload.hex`, `geofence.status`, `overspeeding.status` | `number`, `string` | Custom indexed element for BLE sensor 4 |
| **`335`** | Geofence zone 29 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance`, `geofence.status`, `overspeeding.status` | `number` (`lux`), `boolean` | BLE (Bluetooth Low Energy) sensor illuminance |
| **`336`** | Geofence zone 30 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance`, `geofence.status`, `overspeeding.status` | `number` (`lux`), `boolean` | BLE (Bluetooth Low Energy) sensor illuminance |
| **`337`** | Geofence zone 31 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance`, `geofence.status`, `overspeeding.status` | `number` (`lux`), `boolean` | BLE (Bluetooth Low Energy) sensor illuminance |
| **`338`** | Geofence zone 32 | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance`, `geofence.status`, `overspeeding.status` | `number` (`lux`), `boolean` | BLE (Bluetooth Low Energy) sensor illuminance |
| **`339`** | Geofence zone 33 | `1 B` (`Unsigned`) | `-` (`×-`) | `device.serial.number`, `geofence.status`, `overspeeding.status` | `string`, `boolean` | Device serial number |
| **`340`** | Geofence zone 34 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `pcb.firmware.enum`, `software.version` | `boolean`, `boolean` | Geofence entered status |
| **`341`** | Geofence zone 35 | `1 B` (`Unsigned`) | `-` (`×-`) | `error.type`, `geofence.status`, `overspeeding.status` | `number`, `boolean` | Protocol-specific error identification number |
| **`342`** | Geofence zone 36 | `1 B` (`Unsigned`) | `-` (`×-`) | `event.code`, `geofence.status`, `overspeeding.status` | `string`, `boolean` | Protocol-specific event code string |
| **`343`** | Geofence zone 37 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`344`** | Geofence zone 38 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `lock.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`345`** | Geofence zone 39 | `1 B` (`Unsigned`) | `-` (`×-`) | `buzzer.alarm.status`, `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Buzzer alarm status |
| **`346`** | Geofence zone 40 | `1 B` (`Unsigned`) | `-` (`×-`) | `external.battery.status`, `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | External battery status |
| **`347`** | Geofence zone 41 | `1 B` (`Unsigned`) | `-` (`×-`) | `battery.charging.status`, `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Battery charging status |
| **`348`** | Geofence zone 42 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`349`** | Geofence zone 43 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `operating.mode.enum`, `overspeeding.status` | `boolean`, `number` | Geofence entered status |
| **`350`** | Geofence zone 44 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `internal.battery.voltage`, `overspeeding.status` | `boolean`, `number` (`volts`) | Geofence entered status |
| **`351`** | Geofence zone 45 | `1 B` (`Unsigned`) | `-` (`×-`) | `external.battery.voltage`, `geofence.status`, `overspeeding.status` | `number` (`volts`), `boolean` | External battery voltage |
| **`352`** | Geofence zone 46 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `scooter.battery.level` | `boolean`, `boolean` | Geofence entered status |
| **`353`** | Geofence zone 47 | `1 B` (`Unsigned`) | `-` (`×-`) | `actual.remaining.mileage`, `geofence.status`, `overspeeding.status` | `number` (`km`), `boolean` | Actual remaining mileage |
| **`354`** | Geofence zone 48 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `predicted.remaining.mileage` | `boolean`, `boolean` | Geofence entered status |
| **`355`** | Geofence zone 49 | `1 B` (`Unsigned`) | `-` (`×-`) | `extnav.position.speed`, `geofence.status`, `overspeeding.status` | `number` (`km/h`), `boolean` | External receiver instant speed at position detection moment |
| **`356`** | Geofence zone 50 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `vehicle.mileage` | `boolean`, `boolean` | Geofence entered status |
| **`550`** | Geofence zone 51 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`551`** | Geofence zone 52 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`552`** | Geofence zone 53 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`553`** | Geofence zone 54 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`554`** | Geofence zone 55 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`555`** | Geofence zone 56 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`556`** | Geofence zone 57 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`557`** | Geofence zone 58 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`558`** | Geofence zone 59 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`559`** | Geofence zone 60 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`560`** | Geofence zone 61 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`561`** | Geofence zone 62 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`562`** | Geofence zone 63 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`563`** | Geofence zone 64 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`564`** | Geofence zone 65 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`565`** | Geofence zone 66 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`566`** | Geofence zone 67 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`567`** | Geofence zone 68 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`568`** | Geofence zone 69 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`569`** | Geofence zone 70 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`570`** | Geofence zone 71 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`571`** | Geofence zone 72 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`572`** | Geofence zone 73 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`573`** | Geofence zone 74 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`574`** | Geofence zone 75 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`575`** | Geofence zone 76 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`576`** | Geofence zone 77 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`577`** | Geofence zone 78 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`578`** | Geofence zone 79 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`579`** | Geofence zone 80 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`580`** | Geofence zone 81 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`581`** | Geofence zone 82 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`582`** | Geofence zone 83 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`583`** | Geofence zone 84 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`584`** | Geofence zone 85 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`585`** | Geofence zone 86 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`586`** | Geofence zone 87 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`587`** | Geofence zone 88 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`588`** | Geofence zone 89 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`589`** | Geofence zone 90 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`590`** | Geofence zone 91 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`591`** | Geofence zone 92 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`592`** | Geofence zone 93 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`593`** | Geofence zone 94 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`594`** | Geofence zone 95 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`595`** | Geofence zone 96 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`596`** | Geofence zone 97 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`597`** | Geofence zone 98 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`598`** | Geofence zone 99 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`599`** | Geofence zone 100 | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status` | `boolean`, `boolean` | Geofence entered status |
| **`175`** | Auto Geofence | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status` | `boolean` | Geofence entered status |
| **`250`** | Trip | `1 B` (`Unsigned`) | `-` (`×-`) | `private.status`, `trip.state.enum`, `trip.status` | `boolean`, `number` | Device is in private mode |
| **`255`** | Over Speeding | `1 B` (`Unsigned`) | `km/h` (`×-`) | `overspeeding.speed`, `overspeeding.status` | `number` (`km/h`), `boolean` | GNSS based speed when overspeeding event is triggered |
| **`257`** | Crash Trace Data | `466 B` (`HEX`) | `-` (`×-`) | `acceleration.array` | `array` (`g`) | Array of objects with acceleration data by x, y, and z axis |
| **`258`** | EcoMaximum | `8 B` (`Unsigned`) | `-` (`×-`) | `max.x.acceleration`, `max.y.acceleration`, `max.z.acceleration` | `number` (`g`), `number` (`g`) | Harsh acceleration event max accelerometer value on X-axis |
| **`259`** | EcoAverage | `8 B` (`Unsigned`) | `-` (`×-`) | `average.x.acceleration`, `average.y.acceleration`, `average.z.acceleration` | `number` (`g`), `number` (`g`) | Harsh acceleration event average accelerometer value on X-axis |
| **`260`** | EcoDuration | `2 B` (`Unsigned`) | `-` (`×-`) | `eco.driving.event.duration` | `number` (`seconds`) | Duration of event that did generate Green driving |
| **`243`** | Idling | `1 B` (`Unsigned`) | `-` (`×-`) | `eco.driving.event.duration`, `idle.status` | `number` (`seconds`), `boolean` | Duration of event that did generate Green driving |
| **`244`** | Camera Image Generated | `4 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`253`** | Green Driving Type | `1 B` (`Unsigned`) | `-` (`×-`) | `harsh.acceleration.event`, `harsh.braking.event`, `harsh.cornering.event` | `boolean`, `boolean` | Harsh acceleration detected |
| **`246`** | Towing | `1 B` (`Unsigned`) | `-` (`×-`) | `towing.alarm.status` | `boolean` | Towing alarm state |
| **`248`** | Geofence Zone Over Speeding | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.overspeeding.status`, `ibutton.authorized.status`, `ibutton.connected.status`, `immobilizer.state.enum` | `boolean`, `boolean` | Geofence overspeeding status |
| **`247`** | Crash Detection | `1 B` (`Unsigned`) | `-` (`×-`) | `crash.event`, `crash.event.enum` | `boolean`, `number` | Crash event detected |
| **`251`** | Immobilizer | `1 B` (`Unsigned`) | `-` (`×-`) | `ibutton.authorized.status`, `ibutton.connected.status`, `idle.status`, `immobilizer.state`, `immobilizer.state.enum` | `boolean`, `boolean` | iButton authorized status |
| **`254`** | Green Driving Value | `1 B` (`Unsigned`) | `G or rad` (`×acc and braking: 0.01`) | `absolute.acceleration`, `harsh.cornering.angle` | `number` (`g`), `number` (`degrees`) | Module of accelerometer vector |
| **`249`** | Jamming | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.jamming.alarm.status` | `boolean` | Alarm status for the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) jamming |
| **`252`** | Authorized Driving | `1 B` (`Unsigned`) | `-` (`×-`) | `external.powersource.status`, `ibutton.authorized.state.enum`, `ibutton.authorized.status` | `boolean`, `number` | External power source connection status |
| **`242`** | Data Limit Hit | `1 B` (`Unsigned`) | `-` (`×-`) | `fall.status`, `mandown.alarm.status` | `boolean`, `boolean` | Device fall status true - device is falling, false - falling stopped |
| **`358`** | Custom Scenario 1 | `1 B` (`Unsigned`) | `-` (`×-`) | `scenario.status`, `total.operate.time` | `boolean`, `number` (`seconds`) | Custom scenario status |
| **`359`** | Custom Scenario 2 | `1 B` (`Unsigned`) | `-` (`×-`) | `scenario.status`, `total.driving.time` | `boolean`, `number` (`seconds`) | Custom scenario status |
| **`360`** | Custom Scenario 3 | `1 B` (`Unsigned`) | `-` (`×-`) | `scenario.status`, `trip.operate.time` | `boolean`, `number` (`seconds`) | Custom scenario status |
| **`361`** | Custom Scenario 4 | `1 B` (`Unsigned`) | `-` (`×-`) | `scenario.status`, `trip.driving.time` | `boolean`, `number` (`seconds`) | Custom scenario status |
| **`10611`** | RS232_COM1Data | `200 B` (`HEX`) | `-` (`×-`) | `payload.hex` | `string` | HEX Payload received from device |
| **`10612`** | RS232_COM2Data | `200 B` (`HEX`) | `-` (`×-`) | `payload.hex` | `string` | HEX Payload received from device |

### Section `06_manual-can-elements` (70 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`145`** | Manual CAN 00 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `tacho.driver.cumulative_driving.duration` | `number`, `string` | Indexed Manual CAN parameter value |
| **`146`** | Manual CAN 01 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `tacho.driver.cumulative_driving.duration` | `number`, `string` | Indexed Manual CAN parameter value |
| **`147`** | Manual CAN 02 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `tacho.driver.card.code` | `number`, `string` | Indexed Manual CAN parameter value |
| **`148`** | Manual CAN 03 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `tacho.driver.card.code` | `number`, `string` | Indexed Manual CAN parameter value |
| **`149`** | Manual CAN 04 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `tacho.driver.card.code` | `number`, `string` | Indexed Manual CAN parameter value |
| **`150`** | Manual CAN 05 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `tacho.driver.card.code` | `number`, `string` | Indexed Manual CAN parameter value |
| **`151`** | Manual CAN 06 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `battery.temperature`, `manual.can`, `manual.can.hex` | `number` (`celsius`), `number` | Battery temperature |
| **`152`** | Manual CAN 07 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `battery.level`, `can.vehicle.battery.level`, `manual.can`, `manual.can.hex` | `number` (`percentage`), `number` (`percentage`) | Internal battery level |
| **`153`** | Manual CAN 08 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `manual.can`, `manual.can.hex`, `overspeeding.status` | `boolean`, `number` | Geofence entered status |
| **`154`** | Manual CAN 09 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `manual.can`, `manual.can.hex`, `overspeeding.status` | `boolean`, `number` | Geofence entered status |
| **`380`** | Manual CAN 10 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `dout`, `manual.can`, `manual.can.hex` | `number`, `number` | Digital outputs bitmask |
| **`381`** | Manual CAN 11 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `negative.input.status` | `number`, `string` | Indexed Manual CAN parameter value |
| **`382`** | Manual CAN 12 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`383`** | Manual CAN 13 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `accelerometer.calibration.state`, `manual.can`, `manual.can.hex` | `number`, `number` | Accelerometer calibration state |
| **`384`** | Manual CAN 14 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`385`** | Manual CAN 15 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `ble.beacons`, `manual.can`, `manual.can.hex` | `array`, `number` | Standard parameter names used: *id* - beacon identification string. Usually it is beacon's UUID or MAC-address *local_name* - Beacons's Local Name *rssi* - BLE signal level. Units = dBm *battery.voltage* - Beacon's battery voltage. Units = volts *battery.level* - Beacon's battery level. Units = percentage *temperature* - Beacon's temperature. Units = celsius *humidity* - Beacon's humidity. Units = percentage |
| **`386`** | Manual CAN 16 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex`, `position.fix.age` | `number`, `string` | Indexed Manual CAN parameter value |
| **`387`** | Manual CAN 17 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `iso6709.coordinates`, `manual.can`, `manual.can.hex` | `string`, `number` | String with position in ISO 6709 format |
| **`388`** | Manual CAN 18 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `can.module.id.hex`, `manual.can`, `manual.can.hex` | `string`, `number` | CAN module ID in HEX format |
| **`389`** | Manual CAN 19 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `button.action.type`, `button.id`, `can.vehicle.mileage`, `manual.can`, `manual.can.hex` | `number`, `number` | Button Action type: 1 - 1 click 2 - 2 clicks 3 - long click |
| **`10298`** | Manual CAN 20 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10299`** | Manual CAN 21 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10300`** | Manual CAN 22 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10301`** | Manual CAN 23 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10302`** | Manual CAN 24 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10303`** | Manual CAN 25 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10304`** | Manual CAN 26 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10305`** | Manual CAN 27 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10306`** | Manual CAN 28 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10307`** | Manual CAN 29 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10308`** | Manual CAN 30 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10309`** | Manual CAN 31 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10310`** | Manual CAN 32 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10311`** | Manual CAN 33 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10312`** | Manual CAN 34 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10313`** | Manual CAN 35 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10314`** | Manual CAN 36 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10315`** | Manual CAN 37 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10316`** | Manual CAN 38 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10317`** | Manual CAN 39 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10318`** | Manual CAN 40 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10319`** | Manual CAN 41 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10320`** | Manual CAN 42 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10321`** | Manual CAN 43 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10322`** | Manual CAN 44 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10323`** | Manual CAN 45 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10324`** | Manual CAN 46 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10325`** | Manual CAN 47 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10326`** | Manual CAN 48 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10327`** | Manual CAN 49 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10328`** | Manual CAN 50 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10329`** | Manual CAN 51 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10330`** | Manual CAN 52 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10331`** | Manual CAN 53 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10332`** | Manual CAN 54 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10333`** | Manual CAN 55 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10334`** | Manual CAN 56 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10335`** | Manual CAN 57 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10336`** | Manual CAN 58 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10337`** | Manual CAN 59 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10338`** | Manual CAN 60 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10339`** | Manual CAN 61 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10340`** | Manual CAN 62 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10341`** | Manual CAN 63 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10342`** | Manual CAN 64 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10343`** | Manual CAN 65 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10344`** | Manual CAN 66 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10345`** | Manual CAN 67 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10346`** | Manual CAN 68 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |
| **`10347`** | Manual CAN 69 | `1-8 B` (`Unsigned`) | `-` (`×-`) | `manual.can`, `manual.can.hex` | `number`, `string` | Indexed Manual CAN parameter value |

### Section `07_tachograph-data-elements` (79 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`183`** | Drive Recognize | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.drive.recognize.status` | `boolean` | Tacho recognized vehicle drive |
| **`184`** | Driver 1 Working State | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.driver.activity.state`, `tacho.driver.activity.state.enum`, `tacho.driver.work.state`, `tacho.driver.work.state.enum` | `string`, `number` | Current driver activity reported by tacho, indexed by card slot, rest / work / drive / available / not available / error |
| **`185`** | Driver 2 Working State | `1 B` (`Unsigned`) | `-` (`×-`) | `can.spreader.working.hours`, `tacho.driver.activity.state`, `tacho.driver.activity.state.enum`, `tacho.driver.work.state`, `tacho.driver.work.state.enum` | `number` (`hours`), `string` | Salt spreader working hours read from CAN |
| **`186`** | Tachograph Over Speed | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.overspeeding.status` | `boolean` | Overspeeding status reported by tacho |
| **`187`** | Driver 1 Card Presence | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.driver.card.presence`, `tacho.driver.card.status` | `number`, `boolean` | Tacho driver card presence enum |
| **`188`** | Driver 2 Card Presence | `1 B` (`Unsigned`) | `-` (`×-`) | `can.retarder.torque.load`, `tacho.driver.card.presence`, `tacho.driver.card.status` | `number` (`percentage`), `number` | Retarder torque load percentage read from CAN |
| **`189`** | Driver 1 Time Related States | `1 B` (`Unsigned`) | `-` (`×-`) | `can.total.cruise.control.time`, `tacho.driver.time.state`, `tacho.driver.time.state.enum` | `number` (`hours`), `string` | Total driving time when cruise control is ON, read from CAN |
| **`190`** | Driver 2 Time Related States | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.driver.time.state`, `tacho.driver.time.state.enum` | `boolean`, `boolean` | Geofence entered status |
| **`191`** | Vehicle Speed | `2 B` (`Unsigned`) | `km/h` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.position.speed` | `boolean`, `boolean` | Geofence entered status |
| **`192`** | Odometer | `4 B` (`Unsigned`) | `m` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.vehicle.mileage` | `boolean`, `boolean` | Geofence entered status |
| **`193`** | Trip Distance | `4 B` (`Unsigned`) | `m` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.trip.mileage` | `boolean`, `boolean` | Geofence entered status |
| **`194`** | Timestamp | `4 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.timestamp` | `boolean`, `boolean` | Geofence entered status |
| **`231`** | Vehicle Registration Number Part1 | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `gsm.sim.imsi`, `overspeeding.status`, `vehicle.registration.number` | `boolean`, `string` | Geofence entered status |
| **`232`** | Vehicle Registration Number Part2 | `8 B` (`Unsigned`) | `-` (`×-`) | `can.cng.status`, `gsm.sim.status`, `vehicle.registration.number` | `boolean`, `boolean` | Compressed natural gas status read from CAN |
| **`233`** | Vehicle Identification Number Part1 | `8 B` (`Unsigned`) | `-` (`×-`) | `can.cng.consumed`, `vehicle.vin` | `number` (`kg`), `string` | Consumed of compressed natural gas read from CAN |
| **`234`** | Vehicle Identification Number Part2 | `8 B` (`Unsigned`) | `-` (`×-`) | `can.cng.level`, `vehicle.vin` | `number` (`percentage`), `string` | Compressed natural gas level read from CAN |
| **`235`** | Vehicle Identification Number Part3 | `1 B` (`Unsigned`) | `-` (`×-`) | `can.oil.level.low.indicator.status`, `vehicle.vin` | `boolean`, `string` | Oil level low indicator status read from CAN bus |
| **`222`** | Card 1 Issuing Member State | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `issuing.member.state.card`, `overspeeding.status` | `boolean`, `number` | Geofence entered status |
| **`223`** | Card 2 Issuing Member State | `1 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `issuing.member.state.card`, `overspeeding.status` | `boolean`, `number` | Geofence entered status |
| **`195`** | Driver 1 ID MSB | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.driver.card.code` | `boolean`, `boolean` | Geofence entered status |
| **`196`** | Driver 1 ID LSB | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.driver.card.code` | `boolean`, `boolean` | Geofence entered status |
| **`197`** | Driver 2 ID MSB | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.driver.card.code` | `boolean`, `boolean` | Geofence entered status |
| **`198`** | Driver 2 ID LSB | `8 B` (`Unsigned`) | `-` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.driver.card.code` | `boolean`, `boolean` | Geofence entered status |
| **`56`** | Driver 1 Continuous Driving Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `can.absolute.fuel.rail.pressure`, `tacho.driver.continuous_driving.duration` | `number` (`kPa`), `number` (`seconds`) | Absolute fuel rail pressure |
| **`57`** | Driver 2 Continuous Driving Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `can.hybrid.battery.pack.life`, `tacho.driver.continuous_driving.duration` | `number` (`percentage`), `number` (`seconds`) | Hybrid battery pack remaining life |
| **`58`** | Driver 1 Cumulative Break Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `can.engine.oil.temperature`, `tacho.driver.cumulative_break.duration` | `number` (`celsius`), `number` (`seconds`) | Engine oil temperature read from CAN |
| **`59`** | Driver 2 Cumulative Break Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `can.fuel.injection.timing`, `tacho.driver.cumulative_break.duration` | `number` (`degrees`), `number` (`seconds`) | Fuel injection timing read from CAN |
| **`60`** | Driver 1 Selected Activity Duration | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `can.fuel.consumption`, `tacho.driver.activity.duration`, `tacho.driver.selected.activity.duration` | `number` (`liters/h`), `number` (`seconds`) | Engine fuel rate read from CAN |
| **`61`** | Driver 2 Selected Activity Duration | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `geofence.status`, `overspeeding.status`, `tacho.driver.activity.duration`, `tacho.driver.selected.activity.duration` | `boolean`, `boolean` | Geofence entered status |
| **`69`** | Driver 1 Cumulative Driving Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `gnss.antenna.short.circuit.status`, `gnss.antenna.status`, `gnss.sleep.mode.status`, `gnss.state.enum`, `gnss.status`, `position.valid`, `tacho.driver.cumulative_driving.duration` | `boolean`, `boolean` | GNSS antenna short circuit status |
| **`77`** | Driver 2 Cumulative Driving Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `onewire.sensor.serial`, `tacho.driver.cumulative_driving.duration` | `string`, `number` (`seconds`) | External 1-Wire sensor serial number in HEX representation |
| **`48`** | Tacho Data Source | `1 B` (`Unsigned`) | `-` (`×-`) | `can.fuel.level`, `tacho.data.source` | `number` (`percentage`), `string` | Fuel level in tank read from CAN |
| **`10501`** | Drivers hours rules pre warning time delay | `1 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.time.before.warning` | `number` (`minutes`) | Tacho driver's hours rules pre warning time delay |
| **`10502`** | Out Of Scope Condition | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.out.of.scope.condition.status` | `boolean` | Tacho out of scope condition is met. Indicates whether the vehicle is currently operating under an exemption from tachograph regulations. |
| **`10503`** | Next Calibration Date | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.next.calibration.timestamp` | `number` | Tacho next calibration timestamp |
| **`10504`** | Driver 1 end of last daily rest report | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.driver.daily.rest.end.timestamp` | `number` | Tacho Driver end of last daily rest report timestamp |
| **`10505`** | Driver 1 end of last weekly rest period | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.driver.weekly.rest.end.timestamp` | `number` | Tacho Driver end of last weekly rest period timestamp |
| **`10506`** | Driver 1 end of second last weekly rest period | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.driver.weekly.second.rest.end.timestamp` | `number` | Tacho Driver end of second last weekly rest period timestamp |
| **`10507`** | Driver 1 current daily driving time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.daily.driving.duration` | `number` (`seconds`) | Current daily driving time read from Tacho, indexed for driver number |
| **`10508`** | Driver 1 current weekly driving time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.weekly.driving.duration` | `number` (`seconds`) | Current weekly driving time read from Tacho, indexed for driver number |
| **`10509`** | Driver 1 time left until new daily rest period | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.daily.before.rest.duration` | `number` (`seconds`) | Time left until new daily rest period read from Tacho, indexed for driver number |
| **`10510`** | Driver 1 number of times 9h daily driving time exceeds | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.driver.daily.limit.exceed.number` | `number` | Tacho Driver number of times 9h daily driving time exceeds |
| **`10511`** | Driver 2 end of last daily rest report | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.driver.daily.rest.end.timestamp` | `number` | Tacho Driver end of last daily rest report timestamp |
| **`10512`** | Driver 2 end of last weekly rest period | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.driver.weekly.rest.end.timestamp` | `number` | Tacho Driver end of last weekly rest period timestamp |
| **`10513`** | Driver 2 end of second last weekly rest period | `4 B` (`Unsigned`) | `Timestamp` (`×-`) | `tacho.driver.weekly.second.rest.end.timestamp` | `number` | Tacho Driver end of second last weekly rest period timestamp |
| **`10514`** | Driver 2 current daily driving time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.daily.driving.duration` | `number` (`seconds`) | Current daily driving time read from Tacho, indexed for driver number |
| **`10515`** | Driver 2 current weekly driving time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.weekly.driving.duration` | `number` (`seconds`) | Current weekly driving time read from Tacho, indexed for driver number |
| **`10516`** | Driver 2 time left until new daily rest period | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.daily.before.rest.duration` | `number` (`seconds`) | Time left until new daily rest period read from Tacho, indexed for driver number |
| **`10517`** | Driver 2 number of times 9h daily driving time exceeds | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.driver.daily.limit.exceed.number` | `number` | Tacho Driver number of times 9h daily driving time exceeds |
| **`10518`** | Driver 1 Name | `36 B` (`ASCII`) | `-` (`×-`) | `driver.first.name`, `driver.name` | `string`, `string` | Driver first name |
| **`10519`** | Driver 1 SurName | `36 B` (`ASCII`) | `-` (`×-`) | `driver.last.name`, `driver.name` | `string`, `string` | Drvier lsat name |
| **`10520`** | Driver 2 Name | `36 B` (`ASCII`) | `-` (`×-`) | `driver.first.name`, `driver.name` | `string`, `string` | Driver first name |
| **`10521`** | Driver 2 SurName | `36 B` (`ASCII`) | `-` (`×-`) | `driver.last.name`, `driver.name` | `string`, `string` | Drvier lsat name |
| **`10522`** | Driver 1 Time Left Until New Weekly Rest Period | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.weekly.before.rest.duration` | `number` (`seconds`) | Time left until new weekly rest period read from Tacho, indexed for driver number |
| **`10523`** | Driver 2 Time Left Until New Weekly Rest Period | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.weekly.before.rest.duration` | `number` (`seconds`) | Time left until new weekly rest period read from Tacho, indexed for driver number |
| **`10524`** | Driver 1 Minimum Daily Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.daily.minimum.rest.duration` | `number` (`seconds`) | Tacho Driver Minimum Daily Rest duration |
| **`10525`** | Driver 2 Minimum Daily Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.daily.minimum.rest.duration` | `number` (`seconds`) | Tacho Driver Minimum Daily Rest duration |
| **`10526`** | Driver 1 Minimum Weekly Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.weekly.minimum.rest.duration` | `number` (`seconds`) | Tacho Driver Minimum Weekly Rest duration |
| **`10527`** | Driver 2 Minimum Weekly Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.weekly.minimum.rest.duration` | `number` (`seconds`) | Tacho Driver Minimum Weekly Rest duration |
| **`10528`** | Driver 1 Duration Of Next Break Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.next.rest.duration` | `number` (`seconds`) | Duration of next rest period read from Tacho, indexed for driver number |
| **`10529`** | Driver 2 Duration Of Next Break Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.next.rest.duration` | `number` (`seconds`) | Duration of next rest period read from Tacho, indexed for driver number |
| **`10530`** | Driver 1 Remaining Time Until Next Break Or Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.remaining.before.rest.duration` | `number` (`seconds`) | Duration remaining before next rest period read from Tacho, indexed for driver number |
| **`10531`** | Driver 2 Remaining Time Until Next Break Or Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.remaining.before.rest.duration` | `number` (`seconds`) | Duration remaining before next rest period read from Tacho, indexed for driver number |
| **`10532`** | Driver 1 Remaining Current Driving Time | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.remaining.current.driving.duration` | `number` (`seconds`) | Tacho Driver remaining current driving time |
| **`10533`** | Driver 1 Remaining Driving Time On Current Shift | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.remaining.shift.driving.duration` | `number` (`seconds`) | Tacho Driver remaining driving time on current shift |
| **`10534`** | Driver 1 Remaining Driving Time Of Current Week | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.remaining.weekly.driving.duration` | `number` (`seconds`) | Tacho Driver remaining driving time of current week |
| **`10535`** | Driver 1 Open Compensation In The Last Week | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.compensation.last.week.duration` | `number` (`seconds`) | Tacho Driver open compensation in the last week |
| **`10536`** | Driver 1 Open Compensation In Week Before Last | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.compensation.before.last.week.duration` | `number` (`seconds`) | Tacho Driver open compensation in week before last |
| **`10537`** | Driver 1 Open Compensation In 2nd Week Before Last | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.compensation.second.before.last.week.duration` | `number` (`seconds`) | Tacho Driver open compensation in 2nd week before last |
| **`10538`** | Driver 1 Additional Information | `2 B` (`Unsigned`) | `Bit encoded` (`×-`) | `tacho.driver.card.data.available.status`, `tacho.driver.multi.manning.status`, `tacho.driver.remaining.reduced.daily.rest.periods`, `tacho.driver.remaining.ten.hour.driving.times`, `tacho.driver.time.overlap.status`, `tacho.driver.unknown.periods.present.status`, `tacho.driver.weekly.rest.calculation.status` | `boolean`, `boolean` | Tacho Driver card data availability |
| **`10539`** | Driver 1 Remaining Time Of Current Break Rest | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.remaining.current.rest.duration` | `number` (`seconds`) | Tacho Driver remaining time of current break/rest |
| **`10540`** | Driver 1 Time Left Until Next Driving Period | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.time.until.next.driving` | `number` (`seconds`) | Tacho Driver time left until next driving period |
| **`10541`** | Driver 1 Duration Of Next Driving Period | `2 B` (`Unsigned`) | `Minutes` (`×-`) | `tacho.driver.next.driving.duration` | `number` (`seconds`) | Tacho Driver duration of next driving period |
| **`10542`** | Border Crossing Info | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.border.crossing.info` | `number` | Tachograph border crossing info |
| **`10543`** | K-Line Privacy Mode | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.kline.privacy.mode.enum` | `string` | Tachograph K-Line privacy mode |
| **`13260`** | Vehicle load type info | `1 B` (`Unsigned`) | `-` (`×-`) | `tacho.vehicle.load.type` | `string` | Tachograph vehicle load type |
| **`13261`** | Driver1 load/unload time | `4 B` (`Unsigned`) | `s` (`×-`) | `tacho.driver.load.time` | `number` (`seconds`) | Driver loading/unloading time reported by tacho, indexed for driver number |
| **`13262`** | Driver2 load/unload time | `4 B` (`Unsigned`) | `s` (`×-`) | `tacho.driver.load.time` | `number` (`seconds`) | Driver loading/unloading time reported by tacho, indexed for driver number |
| **`13263`** | Drivers private data consent | `4 B` (`Unsigned`) | `-` (`×-`) | `tacho.driver.private.data.consent` | `number` | Drivers private data consent status reported by tacho |

### Section `08_mobileye-elements` (39 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`288`** | ME Sound Type | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid`, `mobileye.sound.type` | `number`, `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`289`** | ME Pedestrians in Danger Zone | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm`, `mobileye.pedestrian.danger.zone.status` | `number` (`dbm`), `boolean` | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`290`** | ME Pedestrians in Forward Collision Warning | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.lac`, `mobileye.pedestrian.collision.warning.status` | `number`, `boolean` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`291`** | ME Time Indicator | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid`, `mobileye.dusk.status`, `mobileye.night.status` | `number`, `boolean` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`292`** | ME Error Valid | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm`, `mobileye.error.valid.status` | `number` (`dbm`), `boolean` | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`293`** | ME Error Code | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.lac`, `mobileye.error.code` | `number`, `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`294`** | ME Zero Speed | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid`, `mobileye.movement.status` | `number`, `boolean` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`295`** | ME Headway Valid | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm`, `mobileye.headway.valid.status` | `number` (`dbm`), `boolean` | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`296`** | ME Headway Measurement | `1 B` (`Unsigned`) | `-` (`×0,1`) | `gsm.lac`, `mobileye.headway.measurement` | `number`, `number` (`seconds`) | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`297`** | ME LDW Off | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid`, `mobileye.lane.departure.warnings.status` | `number`, `boolean` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`298`** | ME Left LDW On | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm`, `mobileye.lane.departure.left.warning.status` | `number` (`dbm`), `boolean` | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`299`** | ME Right LDW On | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.lane.departure.right.warning.status` | `boolean` | Mobileye indicator of right lane departure warning event status |
| **`300`** | ME Maintenance | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.internal.error.status` | `boolean` | Mobileye indicator of internal error. See user manual for details |
| **`301`** | ME Fail Safe | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.failsafe.mode.status` | `boolean` | Mobileye indocator of failsafe mode activation |
| **`302`** | ME FCW On | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.forward.collision.warning.status` | `boolean` | Mobileye indicator of forward collision warning event status |
| **`303`** | ME TSR Enabled | `1 B` (`Unsigned`) | `-` (`×-`) | `instant.movement.status`, `mobileye.traffic.signs.recognition.status` | `boolean`, `boolean` | Instant movement status |
| **`304`** | ME Headway Warning Repeat Enabled | `1 B` (`Unsigned`) | `-` (`×-`) | `can.vehicle.battery.range`, `mobileye.headway.warning.repeat.enabled.status` | `number` (`km`), `boolean` | Vehicle Range on Battery, read from CAN |
| **`305`** | ME Headway Warning Level | `1 B` (`Unsigned`) | `-` (`×-`) | `can.vehicle.remaining.range`, `mobileye.headway.warning.level` | `number` (`km`), `number` | Vehicle Range read, from CAN |
| **`306`** | ME TSR Warning Level | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency`, `mobileye.traffic.signs.speed.warning.level` | `number`, `number` | Indexed BLE frequency sensor value |
| **`307`** | ME Tamper Alert | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency`, `mobileye.tamper.status` | `number`, `boolean` | Indexed BLE frequency sensor value |
| **`308`** | ME High Beam | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency`, `mobileye.high.beam.status` | `number`, `boolean` | Indexed BLE frequency sensor value |
| **`309`** | ME Low Beam | `1 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency`, `mobileye.low.beam.status` | `number`, `boolean` | Indexed BLE frequency sensor value |
| **`310`** | ME Wipers | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.wipers.status`, `movement.event` | `boolean`, `boolean` | Mobileye wipers status, true - wiper passes the windshield, false - wiper is static |
| **`311`** | ME Right Signal | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.right.blink.available.status` | `boolean` | Mobileye right blink available status, true - right blink available, false - right blink not available |
| **`312`** | ME Left Signal | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.left.blink.available.status` | `boolean` | Mobileye left blink available status, true - left blink available, false - left blink not available |
| **`313`** | ME Brake Signal | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.brake.signal.status` | `boolean` | Mobileye brake signal status, true - brake signal is on, false - brake signal is off |
| **`314`** | ME Wipers Available | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.wipers.available.status` | `boolean` | Mobileye wipers available status, true - wipers available, false - wipers not available |
| **`315`** | ME Low Beam Available | `1 B` (`Unsigned`) | `-` (`×-`) | `deadman.alarm.status`, `mobileye.low.beam.available.status` | `boolean`, `boolean` | Man down is active and no movement for configured timeout |
| **`316`** | ME High Beam Available | `1 B` (`Unsigned`) | `-` (`×-`) | `mobileye.high.beam.available.status` | `boolean` | Mobileye high beam available status, true - high beam available, false - high beam not available |
| **`317`** | ME Speed Available | `1 B` (`Unsigned`) | `-` (`×-`) | `crash.events.number`, `mobileye.speed.available.status` | `number`, `boolean` | Crash event counter |
| **`318`** | ME Speed | `1 B` (`Unsigned`) | `km/h` (`×-`) | `gnss.jamming.state`, `mobileye.speed` | `number`, `number` (`km/h`) | GNSS jamming state |
| **`319`** | ME TSR 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`320`** | ME TSR 2 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`321`** | ME TSR 3 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`322`** | ME TSR 4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`323`** | ME TSR 5 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`324`** | ME TSR 6 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`325`** | ME TSR 7 | `8 B` (`Unsigned`) | `-` (`×-`) | `vehicle.vin` | `string` | VIN of vehicle |
| **`326`** | ME TSR VO | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |

### Section `09_contipressurecheck-tpms` (75 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`10189`** | Total Tires | `1 B` (`Unsiged`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10190`** | Total Axles | `1 B` (`Unsiged`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10191`** | Graphical Position | `8 B` (`Unsiged`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10192`** | Tire 1 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10193`** | Tire 2 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10194`** | Tire 3 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10195`** | Tire 4 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10196`** | Tire 5 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10197`** | Tire 6 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10198`** | Tire 7 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10199`** | Tire 8 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10200`** | Tire 9 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10201`** | Tire 10 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10202`** | Tire 11 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10203`** | Tire 12 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10204`** | Tire 13 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10205`** | Tire 14 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10206`** | Tire 15 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10207`** | Tire 16 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10208`** | Tire 17 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10209`** | Tire 18 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10210`** | Tire 19 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10211`** | Tire 20 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10212`** | Tire 21 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10213`** | Tire 22 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10214`** | Tire 23 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10215`** | Tire 24 pressure | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10360`** | Tire 1 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10361`** | Tire 1 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10362`** | Tire 2 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10363`** | Tire 2 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10364`** | Tire 3 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10365`** | Tire 3 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10366`** | Tire 4 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10367`** | Tire 4 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10368`** | Tire 5 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10369`** | Tire 5 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10370`** | Tire 6 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10371`** | Tire 6 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10372`** | Tire 7 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10373`** | Tire 7 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10374`** | Tire 8 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10375`** | Tire 8 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10376`** | Tire 9 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10377`** | Tire 9 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10378`** | Tire 10 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10379`** | Tire 10 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10380`** | Tire 11 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10381`** | Tire 11 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10382`** | Tire 12 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10383`** | Tire 12 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10384`** | Tire 13 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10385`** | Tire 13 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10386`** | Tire 14 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10387`** | Tire 14 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10388`** | Tire 15 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10389`** | Tire 15 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10390`** | Tire 16 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10391`** | Tire 16 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10392`** | Tire 17 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10393`** | Tire 17 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10394`** | Tire 18 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10395`** | Tire 18 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10396`** | Tire 19 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10397`** | Tire 19 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10398`** | Tire 20 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10399`** | Tire 20 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10400`** | Tire 21 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10401`** | Tire 21 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10402`** | Tire 22 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10403`** | Tire 22 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10404`** | Tire 23 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10405`** | Tire 23 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10406`** | Tire 24 Temperature | `1 B` (`HEX`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10407`** | Tire 24 Warning | `1 B` (`HEX`) | `—` (`×-`) | — *(Not in official Flespi table)* | — | — |

### Section `10_reefer-io` (47 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`10045`** | Zone 1 Compartment state | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.zone1.alarm.type` | `number` | Freezer zone 1 alarm type |
| **`10046`** | Zone 1 Compartment mode | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.zone1.alarm.code` | `number` | Freezer zone 1 alarm code |
| **`10047`** | Zone 1 Return Air Sensor 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone1.return.air.temperature` | `number` | Freezer zone 1 return air temperature |
| **`10048`** | Zone 1 Supply Air Sensor 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone1.supply.air.temperature` | `number` | Freezer zone 1 supply air temperature |
| **`10049`** | Zone 1 Set Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone1.temperature.setpoint` | `number` | Freezer zone 1 temperature setpoint |
| **`10050`** | Zone 1 Evaporator temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone1.evaporator.coil.temperature` | `number` | Freezer zone 1 evaporator coil temperature |
| **`10051`** | Zone 1 Return Air Sensor 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone1.return.air.temperature` | `number` | Freezer zone 1 return air temperature |
| **`10052`** | Zone 1 Supply Air Sensor 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone1.supply.air.temperature` | `number` | Freezer zone 1 supply air temperature |
| **`10056`** | Zone 2 Return Air Sensor 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone2.return.air.temperature` | `number` | Freezer zone 2 return air temperature |
| **`10057`** | Zone 2 Supply Air Sensor 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone2.supply.air.temperature` | `number` | Freezer zone 2 supply air temperature |
| **`10058`** | Zone 2 Set Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone2.temperature.setpoint` | `number` | Freezer zone 2 temperature setpoint |
| **`10059`** | Zone 2 Evaporator temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone2.evaporator.coil.temperature` | `number` | Freezer zone 2 evaporator coil temperature |
| **`10060`** | Zone 2 Return Air sensor 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone2.return.air.temperature` | `number` | Freezer zone 2 return air temperature |
| **`10061`** | Zone 2 Supply Air sensor 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone2.supply.air.temperature` | `number` | Freezer zone 2 supply air temperature |
| **`10063`** | Zone 3 Compartment state | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.zone3.alarm.type` | `number` | Freezer zone 3 alarm type |
| **`10064`** | Zone 3 Compartment mode | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.zone3.alarm.code` | `number` | Freezer zone 3 alarm code |
| **`10065`** | Zone 3 Return Air sensor 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone3.return.air.temperature` | `number` | Freezer zone 3 return air temperature |
| **`10066`** | Zone 3 Supply Air sensor 1 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone3.supply.air.temperature` | `number` | Freezer zone 3 supply air temperature |
| **`10067`** | Zone 3 Set Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone3.temperature.setpoint` | `number` | Freezer zone 3 temperature setpoint |
| **`10068`** | Zone 3 Evaporator temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone3.evaporator.coil.temperature` | `number` | Freezer zone 3 evaporator coil temperature |
| **`10069`** | Zone 3 Return Air sensor 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone3.return.air.temperature` | `number` | Freezer zone 3 return air temperature |
| **`10070`** | Zone 3 Supply Air sensor 2 | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.zone3.supply.air.temperature` | `number` | Freezer zone 3 supply air temperature |
| **`10071`** | Zone 3 Operating Mode | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.zone3.operating.mode` | `number` | Freezer zone 3 operating mode |
| **`10350`** | Ambient Air Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.air.temperature` | `number` (`celsius`) | Freezer ambient air temperature |
| **`10351`** | Compressor Coolant Temperature | `2 B` (`Signed`) | `°C` (`×0,1`) | `freezer.coolant.temperature` | `number` (`celsius`) | Freezer coolant temperature |
| **`10353`** | Compressor RPM | `2 B` (`Unsigned`) | `—` (`×-`) | `freezer.compressor.rpm` | `number` (`rpm`) | Freezer compressor RPM |
| **`10354`** | Compressor Config | `1 B` (`Unsigned`) | `—` (`×-`) | `freezer.compressor.state` | `number` | Freezer compressor configuration state |
| **`10356`** | Installation Serial | `8 B` (`Unsigned`) | `String` (`×-`) | `freezer.installation.serial` | `string` | Freezer installation serial |
| **`10468`** | Analog Input 1 | `2 B` (`Unsigned`) | `V` (`×-`) | `freezer.datacold.ain` | `number` (`volts`) | Freezer datacold analog sensor |
| **`10469`** | Analog Input 2 | `2 B` (`Unsigned`) | `V` (`×-`) | `freezer.datacold.ain` | `number` (`volts`) | Freezer datacold analog sensor |
| **`10470`** | Analog Input 3 | `2 B` (`Unsigned`) | `V` (`×-`) | `freezer.datacold.ain` | `number` (`volts`) | Freezer datacold analog sensor |
| **`10472`** | Manufacturer ID | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.manufacturer.id` | `number` | Fridge Manufacturer ID |
| **`10473`** | Battery State Flags | `1 B` (`Unsigned`) | `enum (bit field)` (`×-`) | `freezer.battery.state` | `number` | Freezer battery state |
| **`10474`** | Fuel state flags | `1 B` (`Unsigned`) | `enum (bit field)` (`×-`) | `freezer.fuel.sensor.state` | `number` | Freezer fuel state flags |
| **`10475`** | Maintenance 1 Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `freezer.datacold.maintenance` | `number` (`hours`) | Freezer Maintanence |
| **`10476`** | Maintenance 2 Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `freezer.datacold.maintenance` | `number` (`hours`) | Freezer Maintanence |
| **`10477`** | Maintenance 3 Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `freezer.datacold.maintenance` | `number` (`hours`) | Freezer Maintanence |
| **`10478`** | Maintenance 4 Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `freezer.datacold.maintenance` | `number` (`hours`) | Freezer Maintanence |
| **`10479`** | Maintenance 5 Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `freezer.datacold.maintenance` | `number` (`hours`) | Freezer Maintanence |
| **`10480`** | Run Mode | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.run.mode` | `string` | Freezer run mode |
| **`10639`** | Error Codes | `16 B` (`HEX`) | `-` (`×-`) | `freezer.error.data` | `string` | Freezer error codes array hex string |
| **`10644`** | Temperature Probe 1 | `2 B` (`Signed`) | `-` (`×-`) | `freezer.datacold.sensor.temperature` | `number` (`celsius`) | Freezer datacold temperature sensor |
| **`10645`** | Temperature Probe 2 | `2 B` (`Signed`) | `-` (`×-`) | `freezer.datacold.sensor.temperature` | `number` (`celsius`) | Freezer datacold temperature sensor |
| **`10646`** | Temperature Probe 3 | `2 B` (`Signed`) | `-` (`×-`) | `freezer.datacold.sensor.temperature` | `number` (`celsius`) | Freezer datacold temperature sensor |
| **`10647`** | Temperature Probe 4 | `2 B` (`Signed`) | `-` (`×-`) | `freezer.datacold.sensor.temperature` | `number` (`celsius`) | Freezer datacold temperature sensor |
| **`10648`** | Temperature Probe 5 | `2 B` (`Signed`) | `-` (`×-`) | `freezer.datacold.sensor.temperature` | `number` (`celsius`) | Freezer datacold temperature sensor |
| **`10649`** | Temperature Probe 6 | `2 B` (`Signed`) | `-` (`×-`) | `freezer.datacold.sensor.temperature` | `number` (`celsius`) | Freezer datacold temperature sensor |

### Section `11_tk-transcan-io` (12 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`10683`** | Temperature 1 | `2 B` (`Signed`) | `°C` (`×0.1`) | `freezer.transcan.temperature` | `number` | Sensor temperature reported by TK Transcan |
| **`10684`** | Temperature 2 | `2 B` (`Signed`) | `°C` (`×0.1`) | `freezer.transcan.temperature` | `number` | Sensor temperature reported by TK Transcan |
| **`10685`** | Temperature 3 | `2 B` (`Signed`) | `°C` (`×0.1`) | `freezer.transcan.temperature` | `number` | Sensor temperature reported by TK Transcan |
| **`10686`** | Temperature 4 | `2 B` (`Signed`) | `°C` (`×0.1`) | `freezer.transcan.temperature` | `number` | Sensor temperature reported by TK Transcan |
| **`10687`** | Status 1 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.state.enum` | `number` | Status value as reported by TK Transcan |
| **`10688`** | Status 2 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.state.enum` | `number` | Status value as reported by TK Transcan |
| **`10689`** | Status 3 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.state.enum` | `number` | Status value as reported by TK Transcan |
| **`10690`** | Status 4 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.state.enum` | `number` | Status value as reported by TK Transcan |
| **`10691`** | Alarm 1 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.alarm.enum` | `number` | Alarm value as reported by TK Transcan |
| **`10692`** | Alarm 2 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.alarm.enum` | `number` | Alarm value as reported by TK Transcan |
| **`10693`** | Alarm 3 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.alarm.enum` | `number` | Alarm value as reported by TK Transcan |
| **`10694`** | Alarm 4 | `1 B` (`Unsigned`) | `—` (`×0`) | `freezer.transcan.alarm.enum` | `number` | Alarm value as reported by TK Transcan |

### Section `12_tk-euroscan-io` (10 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`484`** | External Sensor Temperature 1 | `2 B` (`Signed`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`485`** | External Sensor Temperature 2 | `2 B` (`Signed`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`486`** | External Sensor Temperature 3 | `2 B` (`Signed`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`487`** | External Sensor Temperature 4 | `2 B` (`Signed`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`488`** | External Sensor Temperature 5 | `2 B` (`Signed`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`489`** | External Sensor Temperature 6 | `2 B` (`Signed`) | `°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`10464`** | External Digital Sensor 1 | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.datacold.din` | `boolean` | Freezer datacold digital sensor |
| **`10465`** | External Digital Sensor 2 | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.datacold.din` | `boolean` | Freezer datacold digital sensor |
| **`10466`** | External Digital Sensor 3 | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.datacold.din` | `boolean` | Freezer datacold digital sensor |
| **`10467`** | External Digital Sensor 4 | `1 B` (`Unsigned`) | `-` (`×-`) | `freezer.datacold.din` | `boolean` | Freezer datacold digital sensor |

### Section `13_tk-touchprint-io` (9 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`10695`** | Input 1 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10696`** | Input 2 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10697`** | Input 3 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10698`** | Input 4 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10699`** | Input 5 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10700`** | Input 6 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10701`** | Setpoint 1 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10702`** | Setpoint 2 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |
| **`10703`** | Setpoint 3 | `2 B` (`Signed`) | `°C` (`×0.1`) | — *(Not in official Flespi table)* | — | — |

### Section `14_ev-fms-elements` (26 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`10456`** | FerryTrainStatus | `1 B` (`Unsigned`) | `-` (`×-`) | `fms.ferry.train.enum` | `number` | FMS ferry/train status |
| **`10879`** | High voltage battery voltage | `4 B` (`Unsigned`) | `mV` (`×50`) | `can.ev.battery.voltage` | `number` (`volts`) | High voltage battery voltage read from CAN, EV FMS |
| **`10880`** | High voltage battery current | `4 B` (`Signed`) | `mA` (`×50`) | `can.ev.battery.current` | `number` (`amperes`) | High voltage battery current read from CAN, EV FMS |
| **`10881`** | Internal Charger Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.internal.charger.state.enum` | `number` | Internal charger state read from CAN, EV FMS |
| **`10882`** | Generic state of charge | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.battery.level` | `number` (`percentage`) | High voltage battery state of charge read from CAN, EV FMS |
| **`10883`** | Ignition | `1 B` (`Unsigned`) | `-` (`×-`) | `can.engine.ignition.status` | `boolean` | CAN engine ignition status |
| **`10884`** | External Energy Source Connection Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.external.powersource.state.enum` | `number` | External energy source connection state read from CAN, EV FMS |
| **`10885`** | Seatbelt switch | `1 B` (`Unsigned`) | `-` (`×-`) | `can.seatbelt.status` | `boolean` | Seatbelt status read from CAN, false - the belt is not buckled, true - the belt is buckled |
| **`10886`** | EVSE1 AC RMS Current | `4 B` (`Signed`) | `mA` (`×50`) | `can.ev.evse1.ac.current` | `number` (`amperes`) | EVSE1 AC RMS current read from CAN, EV FMS |
| **`10887`** | EVSE1 AC RMS Voltage | `4 B` (`Unsigned`) | `mV` (`×50`) | `can.ev.evse1.ac.voltage` | `number` (`volts`) | EVSE1 AC RMS voltage read from CAN, EV FMS |
| **`10888`** | DC Charging State | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.dc.charging.state.enum` | `number` | DC charging state read from CAN, EV FMS |
| **`10889`** | High Voltage Battery Highest Cell Temperature | `2 B` (`Signed`) | `°C` (`×0.03125`) | `can.ev.battery.max.temperature` | `number` (`celsius`) | High voltage battery highest cell temperature read from CAN, EV FMS |
| **`10890`** | High Voltage Battery Lowest Cell Temperature | `2 B` (`Signed`) | `°C` (`×0.03125`) | `can.ev.battery.min.temperature` | `number` (`celsius`) | High voltage battery lowest cell temperature read from CAN, EV FMS |
| **`10891`** | Propulsion Motor Coolant Fan 1 Control Temperature | `2 B` (`Signed`) | `°C` (`×0.03125`) | `can.ev.propulsion.motor.coolant.fan.temperature` | `number` (`celsius`) | Propulsion motor coolant fan 1 control temperature read from CAN, EV FMS |
| **`10892`** | Air Conditioner Compressor Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.air.conditioner.compressor.state.enum` | `number` | Air conditioner compressor state read from CAN, EV FMS |
| **`10893`** | High Voltage Battery Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `can.ev.battery.temperature` | `number` (`celsius`) | High voltage battery temperature read from CAN, EV FMS |
| **`10894`** | HVESS Thermal Management System Heater Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.thermal.management.heater.state.enum` | `number` | High voltage energy storage system thermal management system heater state read from CAN, EV FMS |
| **`10895`** | Fuel Supply Estimated Remaining Distance | `2 B` (`Unsigned`) | `km` (`×-`) | `can.vehicle.battery.remaining.range` | `number` (`km`) | Vehicle battery remaining range, read from CAN |
| **`10896`** | Trailer Weight | `2 B` (`Unsigned`) | `kg` (`×2`) | `can.ev.trailer.weight` | `number` (`kg`) | Trailer weight read from CAN, EV FMS |
| **`10897`** | Cargo Weight | `2 B` (`Unsigned`) | `kg` (`×2`) | `can.ev.cargo.weight` | `number` (`kg`) | Cargo weight read from CAN, EV FMS |
| **`10898`** | Powered Vehicle Weight | `2 B` (`Unsigned`) | `kg` (`×10`) | `can.ev.powered.vehicle.weight` | `number` (`kg`) | Powered vehicle weight read from CAN, EV FMS |
| **`10899`** | Gross Combination Vehicle Weight | `2 B` (`Unsigned`) | `kg` (`×10`) | `can.gross.combination.vehicle.weight` | `number` (`kg`) | Gross combination vehicle weight read from CAN |
| **`10901`** | Highest cell voltage | `2 B` (`Unsigned`) | `mV` (`×1`) | `can.ev.battery.max.cell.voltage` | `number` (`volts`) | High voltage battery highest cell voltage read from CAN, EV FMS |
| **`10902`** | Lowest cell voltage | `2 B` (`Unsigned`) | `mV` (`×1`) | `can.ev.battery.min.cell.voltage` | `number` (`volts`) | High voltage battery lowest cell voltage read from CAN, EV FMS |
| **`10903`** | HVESS Nominal Rated Capacity | `4 B` (`Unsigned`) | `%` (`×-`) | `can.ev.battery.rated.capacity` | `number` (`percentage`) | High voltage energy storage system nominal rated capacity read from CAN, EV FMS |
| **`10904`** | HVESS State of Health | `1 B` (`Unsigned`) | `%` (`×0.4`) | `can.vehicle.battery.health` | `number` (`percentage`) | Battery State of Health |

### Section `15_cameras-video` (6 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`12301`** | iCam DualCam1 Front State | `1 B` (`Unsigned`) | `-` (`×-`) | `camera.front.state`, `camera.front.state.enum`, `camera.type` | `string`, `number` | Front camera ping transmission and TF status. Indexed by camera COM port. |
| **`12302`** | iCam DualCam1 Rear State | `1 B` (`Unsigned`) | `-` (`×-`) | `camera.rear.state`, `camera.rear.state.enum`, `camera.type` | `string`, `number` | Rear camera ping transmission and TF status. Indexed by camera COM port. |
| **`12303`** | iCam DashCam1 State | `1 B` (`Unsigned`) | `-` (`×-`) | `camera.front.state`, `camera.front.state.enum`, `camera.type` | `string`, `number` | Front camera ping transmission and TF status. Indexed by camera COM port. |
| **`12304`** | iCam DualCam2 Front State | `1 B` (`Unsigned`) | `-` (`×-`) | `camera.front.state`, `camera.front.state.enum`, `camera.type` | `string`, `number` | Front camera ping transmission and TF status. Indexed by camera COM port. |
| **`12305`** | iCam DualCam2 Rear State | `1 B` (`Unsigned`) | `-` (`×-`) | `camera.rear.state`, `camera.rear.state.enum`, `camera.type` | `string`, `number` | Rear camera ping transmission and TF status. Indexed by camera COM port. |
| **`12306`** | iCam DashCam2 State | `1 B` (`Unsigned`) | `-` (`×-`) | `camera.front.state`, `camera.front.state.enum`, `camera.type` | `string`, `number` | Front camera ping transmission and TF status. Indexed by camera COM port. |

### Section `16_isobus` (298 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`12400`** | Groundspeed of a machine | `2 B` (`Unsigned`) | `m/s` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12401`** | Ground based distance | `4 B` (`Unsigned`) | `m` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12402`** | Ground based direction | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12403`** | Wheel speed of a machine | `2 B` (`Unsigned`) | `m/s` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12404`** | Wheel based distance | `4 B` (`Unsigned`) | `m` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12405`** | Maximum time of tractor power | `1 B` (`Unsigned`) | `min` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12406`** | Wheel based direction | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12407`** | Key switch state | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.key.switch.status` | `boolean` | ISOBUS key switch status |
| **`12408`** | Start/Stop state | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.start.stop.status` | `boolean` | ISOBUS start/stop status |
| **`12409`** | Maintain ECU power | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.maintain.ecu.power.status` | `boolean` | ISOBUS maintain ECU power status |
| **`12410`** | Maintain actuator power | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.maintain.actuator.power.status` | `boolean` | ISOBUS maintain actuator power status |
| **`12411`** | Implement transport state | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.implement.transport.status` | `boolean` | ISOBUS implement transport status |
| **`12412`** | Implement park state | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.implement.park.status` | `boolean` | ISOBUS implement park status |
| **`12413`** | Implement work state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12414`** | Front hitch position | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12415`** | Front hitch in-work indication | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12416`** | Front nominal lower link force | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12417`** | Front draft | `4 B` (`Signed`) | `N` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12418`** | Rear hitch position | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12419`** | Rear hitch in-work indication | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12420`** | Rear nominal lower link force | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12421`** | Rear draft | `4 B` (`Signed`) | `N` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12422`** | Front PTO output shaft speed | `4 B` (`Unsigned`) | `1/min` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12423`** | Front PTO shaft speed point | `4 B` (`Unsigned`) | `1/min` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12424`** | Front PTO engagement | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12425`** | Front PTO mode | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12426`** | Front PTO economy mode | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12427`** | Rear PTO output shaft speed | `4 B` (`Unsigned`) | `1/min` (`×0.001`) | `isobus.rear.pto.output.shaft.speed` | `number` (`rpm`) | ISOBUS rear PTO output shaft speed |
| **`12428`** | Rear PTO shaft speed point | `4 B` (`Unsigned`) | `1/min` (`×0.001`) | `isobus.rear.pto.shaft.speed.point` | `number` (`rpm`) | ISOBUS rear PTO shaft speed set point |
| **`12429`** | Rear PTO engagement | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.rear.pto.engagement.status` | `boolean` | ISOBUS rear PTO engagement status |
| **`12430`** | Rear PTO mode | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.rear.pto.mode.enum` | `string` | ISOBUS rear PTO mode |
| **`12431`** | Rear PTO economy mode | `1 B` (`Unsigned`) | `-` (`×-`) | `isobus.rear.pto.economy.mode.status` | `boolean` | ISOBUS rear PTO economy mode status |
| **`12432`** | Front hitch position command | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12433`** | Rear hitch position command | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12434`** | Front Shaft speed set point command | `4 B` (`Unsigned`) | `1/min` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12435`** | Rear Shaft speed set point command | `4 B` (`Unsigned`) | `1/min` (`×0.001`) | — *(Not in official Flespi table)* | — | — |
| **`12436`** | Front PTO engagement command | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12437`** | Rear PTO engagement command | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12438`** | Front PTO mode command | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12439`** | Rear PTO mode command | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12440`** | Front PTO economy mode command | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12441`** | Rear PTO economy mode command | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12442`** | Auxil ext valve number 0 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12443`** | Auxil ext valve number 1 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12444`** | Auxil ext valve number 2 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12445`** | Auxil ext valve number 3 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12446`** | Auxil ext valve number 4 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12447`** | Auxil ext valve number 5 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12448`** | Auxil ext valve number 6 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12449`** | Auxil ext valve number 7 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12450`** | Auxil ext valve number 8 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`124451`** | Auxil ext valve number 9 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12452`** | Auxil ext valve number 10 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12453`** | Auxil ext valve number 11 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12454`** | Auxil ext valve number 12 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12455`** | Auxil ext valve number 13 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12456`** | Auxil ext valve number 14 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12457`** | Auxil ext valve number 15 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12458`** | Auxil ret valve number 0 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12459`** | Auxil ret valve number 1 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12460`** | Auxil ret valve number 2 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12461`** | Auxil ret valve number 3 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12462`** | Auxil ret valve number 4 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12463`** | Auxil ret valve number 5 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12464`** | Auxil ret valve number 6 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12465`** | Auxil ret valve number 7 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12466`** | Auxil ret valve number 8 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12467`** | Auxil ret valve number 9 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12468`** | Auxil ret valve number 10 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12469`** | Auxil ret valve number 11 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12470`** | Auxil ret valve number 12 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12471`** | Auxil ret valve number 13 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12472`** | Auxil ret valve number 14 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12473`** | Auxil ret valve number 15 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12474`** | 0 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12475`** | 1 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12476`** | 2 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12477`** | 3 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12478`** | 4 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12479`** | 5 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12480`** | 6 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12481`** | 7 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12482`** | 8 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12483`** | 9 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12484`** | 10 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12485`** | 11 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12486`** | 12 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12487`** | 13 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12488`** | 14 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12489`** | 15 valve fail safe state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12490`** | 0 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12491`** | 1 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12492`** | 2 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12493`** | 3 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12494`** | 4 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12495`** | 5 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12496`** | 6 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12497`** | 7 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12498`** | 8 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12499`** | 9 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12500`** | 10 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12501`** | 11 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12502`** | 12 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12503`** | 13 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12504`** | 14 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12505`** | 15 valve state | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12506`** | Extend Port Measured Flow 0 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12507`** | Extend Port Measured Flow 1 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12508`** | Extend Port Measured Flow 2 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12509`** | Extend Port Measured Flow 3 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12510`** | Extend Port Measured Flow 4 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12511`** | Extend Port Measured Flow 5 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12512`** | Extend Port Measured Flow 6 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12513`** | Extend Port Measured Flow 7 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12514`** | Extend Port Measured Flow 8 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12515`** | Extend Port Measured Flow 9 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12516`** | Extend Port Measured Flow 10 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12517`** | Extend Port Measured Flow 11 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12518`** | Extend Port Measured Flow 12 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12519`** | Extend Port Measured Flow 13 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12520`** | Extend Port Measured Flow 14 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12521`** | Retract Port Measured Flow 15 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12522`** | Retract Port Measured Flow 0 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12523`** | Retract Port Measured Flow 1 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12524`** | Retract Port Measured Flow 2 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12525`** | Retract Port Measured Flow 3 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12526`** | Retract Port Measured Flow 4 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12527`** | Retract Port Measured Flow 5 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12528`** | Retract Port Measured Flow 6 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12529`** | Retract Port Measured Flow 7 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12530`** | Retract Port Measured Flow 8 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12531`** | Retract Port Measured Flow 9 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12532`** | Retract Port Measured Flow 10 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12533`** | Retract Port Measured Flow 11 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12534`** | Retract Port Measured Flow 12 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12535`** | Retract Port Measured Flow 13 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12536`** | Retract Port Measured Flow 14 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12537`** | Retract Port Measured Flow 15 | `1 B` (`Signed`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12538`** | Extend Port Pressure 0 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12539`** | Extend Port Pressure 1 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12540`** | Extend Port Pressure 2 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12541`** | Extend Port Pressure 3 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12542`** | Extend Port Pressure 4 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12543`** | Extend Port Pressure 5 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12544`** | Extend Port Pressure 6 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12545`** | Extend Port Pressure 7 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12546`** | Extend Port Pressure 8 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12547`** | Extend Port Pressure 9 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12548`** | Extend Port Pressure 10 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12549`** | Extend Port Pressure 11 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12550`** | Extend Port Pressure 12 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12551`** | Extend Port Pressure 13 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12552`** | Extend Port Pressure 14 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12553`** | Extend Port Pressure 15 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12554`** | Retract Port Pressure 0 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12555`** | Retract Port Pressure 1 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12556`** | Retract Port Pressure 2 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12557`** | Retract Port Pressure 3 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12558`** | Retract Port Pressure 4 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12559`** | Retract Port Pressure 5 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12560`** | Retract Port Pressure 6 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12561`** | Retract Port Pressure 7 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12562`** | Retract Port Pressure 8 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12563`** | Retract Port Pressure 9 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12564`** | Retract Port Pressure 10 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12565`** | Retract Port Pressure 11 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12566`** | Retract Port Pressure 12 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12567`** | Retract Port Pressure 13 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12568`** | Retract Port Pressure 14 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12569`** | Retract Port Pressure 15 | `4 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12570`** | Return Port Pressure 0 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12571`** | Return Port Pressure 1 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12572`** | Return Port Pressure 2 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12573`** | Return Port Pressure 3 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12574`** | Return Port Pressure 4 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12575`** | Return Port Pressure 5 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12576`** | Return Port Pressure 6 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12577`** | Return Port Pressure 7 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12578`** | Return Port Pressure 8 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12579`** | Return Port Pressure 9 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12580`** | Return Port Pressure 10 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12581`** | Return Port Pressure 11 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12582`** | Return Port Pressure 12 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12583`** | Return Port Pressure 13 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12584`** | Return Port Pressure 14 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12585`** | Return Port Pressure 15 | `2 B` (`Unsigned`) | `kPa` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12586`** | valve port flow 0 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12587`** | valve port flow 1 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12588`** | valve port flow 2 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12589`** | valve port flow 3 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12590`** | valve port flow 4 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12591`** | valve port flow 5 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12592`** | valve port flow 6 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12593`** | valve port flow 7 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12594`** | valve port flow 8 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12595`** | valve port flow 9 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12596`** | valve port flow 10 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12597`** | valve port flow 11 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12598`** | valve port flow 12 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12599`** | valve port flow 13 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12600`** | valve port flow 14 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12601`** | valve port flow 15 | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12602`** | valve safe mode command 0 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12603`** | valve safe mode command 1 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12604`** | valve safe mode command 2 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12605`** | valve safe mode command 3 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12606`** | valve safe mode command 4 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12607`** | valve safe mode command 5 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12608`** | valve safe mode command 6 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12609`** | valve safe mode command 7 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12610`** | valve safe mode command 8 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12611`** | valve safe mode command 9 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12612`** | valve safe mode command 10 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12613`** | valve safe mode command 11 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12614`** | valve safe mode command 12 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12615`** | valve safe mode command 13 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12616`** | valve safe mode command 14 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12617`** | valve safe mode command 15 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12618`** | valve state command 0 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12619`** | valve state command 1 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12620`** | valve state command 2 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12621`** | valve state command 3 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12622`** | valve state command 4 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12623`** | valve state command 5 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12624`** | valve state command 6 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12625`** | valve state command 7 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12626`** | valve state command 8 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12627`** | valve state command 9 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12628`** | valve state command 10 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12629`** | valve state command 11 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12630`** | valve state command 12 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12631`** | valve state command 13 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12632`** | valve state command 14 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12633`** | valve state command 15 | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12634`** | Tractor high-beam head lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12635`** | Tractor low-beam head lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12636`** | Tractor alternate head lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12637`** | Daytime running lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12638`** | Left-turn signal lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12639`** | Right-turn signal lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12640`** | Beacon lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12641`** | Front fog lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12642`** | Left stop lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12643`** | Right stop lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12644`** | Centre stop lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12645`** | Back up light and alarm horn | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12646`** | Tractor marker lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12647`** | Implement marker lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12648`** | Tractor clearance lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12649`** | Implement clearance lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12650`** | Rear high mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12651`** | Rear low mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12652`** | Underside work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12653`** | Rear fog lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12654`** | Front high-mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12655`** | Front low-mounted work light | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12656`** | Side high-mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12657`** | Side low mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12658`** | Implement left forward work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12659`** | Implement right forward work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12660`** | Implement OEM option 1 light | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12661`** | Implement OEM option 2 light | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12662`** | Implement rear work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12663`** | Implement left work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12664`** | Implement right work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12665`** | Lighting data message request | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12666`** | Tractor high-beam head lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12667`** | Tractor low-beam head lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12668`** | Tractor alternate head lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12669`** | Daytime running lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12670`** | Left-turn signal lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12671`** | Right-turn signal lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12672`** | Beacon lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12673`** | Front fog lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12674`** | Left stop lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12675`** | Right stop lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12676`** | Centre stop lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12677`** | Back up light and alarm horn | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12678`** | Tractor marker lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12679`** | Implement marker lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12680`** | Tractor clearance lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12681`** | Implement clearance lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12682`** | Rear high mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12683`** | Rear low mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12684`** | Underside work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12685`** | Rear fog lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12686`** | Front high-mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12687`** | Front low-mounted work light | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12688`** | Side high-mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12689`** | Side low mounted work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12690`** | Implement left forward work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12691`** | Implement right forward work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12692`** | Implement OEM option 1 light | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12693`** | Implement OEM option 2 light | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12694`** | Implement rear work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12695`** | Implement left work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12696`** | Implement right work lights | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`12697`** | Background illumination level | `1 B` (`Unsigned`) | `%` (`×-`) | — *(Not in official Flespi table)* | — | — |

### Section `17_ble` (46 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`701`** | BLE Temperature 1 | `2 B` (`Signed`) | `°C` (`×0.1`) | `ble.sensor.temperature`, `ble.sensor.temperature.error.code` | `number` (`celsius`), `string` | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`702`** | BLE Temperature 2 | `2 B` (`Signed`) | `°C` (`×0.1`) | `ble.sensor.temperature`, `ble.sensor.temperature.error.code` | `number` (`celsius`), `string` | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`703`** | BLE Temperature 3 | `2 B` (`Signed`) | `°C` (`×0.1`) | `ble.sensor.temperature`, `ble.sensor.temperature.error.code` | `number` (`celsius`), `string` | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`704`** | BLE Temperature 4 | `2 B` (`Signed`) | `°C` (`×0.1`) | `ble.sensor.temperature`, `ble.sensor.temperature.error.code` | `number` (`celsius`), `string` | BLE (Bluetooth Low Energy) sensor Temperature value |
| **`705`** | BLE Battery 1 | `1 B` (`Unsigned`) | `%` (`×-`) | `ble.sensor.battery.level` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`706`** | BLE Battery 2 | `1 B` (`Unsigned`) | `%` (`×-`) | `ble.sensor.battery.level` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`707`** | BLE Battery 3 | `1 B` (`Unsigned`) | `%` (`×-`) | `ble.sensor.battery.level` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`708`** | BLE Battery 4 | `1 B` (`Unsigned`) | `%` (`×-`) | `ble.sensor.battery.level` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor battery level |
| **`709`** | BLE Humidity 1 | `2 B` (`Unsigned`) | `%RH` (`×0.1*`) | `ble.sensor.humidity` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`710`** | BLE Humidity 2 | `2 B` (`Unsigned`) | `%RH` (`×0.1*`) | `ble.sensor.humidity` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`711`** | BLE Humidity 3 | `2 B` (`Unsigned`) | `%RH` (`×0.1*`) | `ble.sensor.humidity` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`712`** | BLE Humidity 4 | `2 B` (`Unsigned`) | `%RH` (`×0.1*`) | `ble.sensor.humidity` | `number` (`percentage`) | BLE (Bluetooth Low Energy) sensor Humidity value |
| **`713`** | BLE Sensor Custom 1 | `8 B` (`Unsigned`) | `-` (`×-`) | `ble.1.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 1 |
| **`714`** | BLE Sensor Custom 2 | `8 B` (`Unsigned`) | `-` (`×-`) | `ble.2.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 2 |
| **`715`** | BLE Sensor Custom 3 | `8 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 3 |
| **`716`** | BLE Sensor Custom 4 | `8 B` (`Unsigned`) | `-` (`×-`) | `ble.4.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 4 |
| **`717`** | BLE Illum1 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance` | `number` (`lux`) | BLE (Bluetooth Low Energy) sensor illuminance |
| **`718`** | BLE Illum2 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance` | `number` (`lux`) | BLE (Bluetooth Low Energy) sensor illuminance |
| **`719`** | BLE Illum3 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance` | `number` (`lux`) | BLE (Bluetooth Low Energy) sensor illuminance |
| **`720`** | BLE Illum4 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.illuminance` | `number` (`lux`) | BLE (Bluetooth Low Energy) sensor illuminance |
| **`721`** | BLE LLS Fuel 1 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.lls.fuel.level` | `number` | Indexed BLE LLS fuel sensor value |
| **`722`** | BLE LLS Fuel 2 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.lls.fuel.level` | `number` | Indexed BLE LLS fuel sensor value |
| **`723`** | BLE LLS Fuel 3 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.lls.fuel.level` | `number` | Indexed BLE LLS fuel sensor value |
| **`724`** | BLE LLS Fuel 4 | `2 B` (`Unsigned`) | `-` (`×-`) | `ble.lls.fuel.level` | `number` | Indexed BLE LLS fuel sensor value |
| **`725`** | BLE Freq 1 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency` | `number` | Indexed BLE frequency sensor value |
| **`726`** | BLE Freq 2 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency` | `number` | Indexed BLE frequency sensor value |
| **`727`** | BLE Freq 3 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency` | `number` | Indexed BLE frequency sensor value |
| **`728`** | BLE Freq 4 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.sensor.frequency` | `number` | Indexed BLE frequency sensor value |
| **`729`** | BLE Sensor Custom 12 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.1.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 1 |
| **`730`** | BLE Sensor Custom 13 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.1.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 1 |
| **`731`** | BLE Sensor Custom 14 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.1.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 1 |
| **`732`** | BLE Sensor Custom 15 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.1.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 1 |
| **`733`** | BLE Sensor Custom 22 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.2.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 2 |
| **`734`** | BLE Sensor Custom 23 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.2.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 2 |
| **`735`** | BLE Sensor Custom 24 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.2.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 2 |
| **`736`** | BLE Sensor Custom 25 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.2.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 2 |
| **`737`** | BLE Sensor Custom 32 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 3 |
| **`738`** | BLE Sensor Custom 33 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 3 |
| **`739`** | BLE Sensor Custom 34 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 3 |
| **`740`** | BLE Sensor Custom 35 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.3.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 3 |
| **`741`** | BLE Sensor Custom 42 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.4.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 4 |
| **`742`** | BLE Sensor Custom 43 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.4.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 4 |
| **`743`** | BLE Sensor Custom 44 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.4.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 4 |
| **`744`** | BLE Sensor Custom 45 | `4 B` (`Unsigned`) | `-` (`×-`) | `ble.4.custom.payload.hex` | `string` | Custom indexed element variable size payload for BLE sensor 4 |
| **`10500`** | BLE Advertisement data | `Variable B` (`HEX`) | `-` (`×-`) | `ble.beacons` | `array` | Standard parameter names used: *id* - beacon identification string. Usually it is beacon's UUID or MAC-address *local_name* - Beacons's Local Name *rssi* - BLE signal level. Units = dBm *battery.voltage* - Beacon's battery voltage. Units = volts *battery.level* - Beacon's battery level. Units = percentage *temperature* - Beacon's temperature. Units = celsius *humidity* - Beacon's humidity. Units = percentage |
| **`548`** | Advanced BLE Advertisement data | `Variable B` (`HEX`) | `-` (`×-`) | `ble.beacons` | `array` | Standard parameter names used: *id* - beacon identification string. Usually it is beacon's UUID or MAC-address *local_name* - Beacons's Local Name *rssi* - BLE signal level. Units = dBm *battery.voltage* - Beacon's battery voltage. Units = volts *battery.level* - Beacon's battery level. Units = percentage *temperature* - Beacon's temperature. Units = celsius *humidity* - Beacon's humidity. Units = percentage |

### Section `18_ev-fms` (25 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`10879`** | High voltage battery voltage | `4 B` (`Unsigned`) | `mV` (`×50`) | `can.ev.battery.voltage` | `number` (`volts`) | High voltage battery voltage read from CAN, EV FMS |
| **`10880`** | High voltage battery current | `4 B` (`Signed`) | `mA` (`×50`) | `can.ev.battery.current` | `number` (`amperes`) | High voltage battery current read from CAN, EV FMS |
| **`10881`** | Internal Charger Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.internal.charger.state.enum` | `number` | Internal charger state read from CAN, EV FMS |
| **`10882`** | Generic state of charge | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.battery.level` | `number` (`percentage`) | High voltage battery state of charge read from CAN, EV FMS |
| **`10883`** | Ignition | `1 B` (`Unsigned`) | `-` (`×-`) | `can.engine.ignition.status` | `boolean` | CAN engine ignition status |
| **`10884`** | External Energy Source Connection Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.external.powersource.state.enum` | `number` | External energy source connection state read from CAN, EV FMS |
| **`10885`** | Seatbelt switch | `1 B` (`Unsigned`) | `-` (`×-`) | `can.seatbelt.status` | `boolean` | Seatbelt status read from CAN, false - the belt is not buckled, true - the belt is buckled |
| **`10886`** | EVSE1 AC RMS Current | `4 B` (`Signed`) | `mA` (`×50`) | `can.ev.evse1.ac.current` | `number` (`amperes`) | EVSE1 AC RMS current read from CAN, EV FMS |
| **`10887`** | EVSE1 AC RMS Voltage | `4 B` (`Unsigned`) | `mV` (`×50`) | `can.ev.evse1.ac.voltage` | `number` (`volts`) | EVSE1 AC RMS voltage read from CAN, EV FMS |
| **`10888`** | DC Charging State | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.dc.charging.state.enum` | `number` | DC charging state read from CAN, EV FMS |
| **`10889`** | High Voltage Battery Highest Cell Temperature | `2 B` (`Signed`) | `°C` (`×0,03125`) | `can.ev.battery.max.temperature` | `number` (`celsius`) | High voltage battery highest cell temperature read from CAN, EV FMS |
| **`10890`** | High Voltage Battery Lowest Cell Temperature | `2 B` (`Signed`) | `°C` (`×0,03125`) | `can.ev.battery.min.temperature` | `number` (`celsius`) | High voltage battery lowest cell temperature read from CAN, EV FMS |
| **`10891`** | Propulsion Motor Coolant Fan 1 Control Temperature | `2 B` (`Signed`) | `°C` (`×0,03125`) | `can.ev.propulsion.motor.coolant.fan.temperature` | `number` (`celsius`) | Propulsion motor coolant fan 1 control temperature read from CAN, EV FMS |
| **`10892`** | Air Conditioner Compressor Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.air.conditioner.compressor.state.enum` | `number` | Air conditioner compressor state read from CAN, EV FMS |
| **`10893`** | High Voltage Battery Temperature | `1 B` (`Signed`) | `°C` (`×-`) | `can.ev.battery.temperature` | `number` (`celsius`) | High voltage battery temperature read from CAN, EV FMS |
| **`10894`** | HVESS Thermal Management System Heater Status | `1 B` (`Unsigned`) | `-` (`×-`) | `can.ev.thermal.management.heater.state.enum` | `number` | High voltage energy storage system thermal management system heater state read from CAN, EV FMS |
| **`10895`** | Fuel Supply Estimated Remaining Distance | `2 B` (`Unsigned`) | `km` (`×-`) | `can.vehicle.battery.remaining.range` | `number` (`km`) | Vehicle battery remaining range, read from CAN |
| **`10896`** | Trailer Weight | `2 B` (`Unsigned`) | `kg` (`×2`) | `can.ev.trailer.weight` | `number` (`kg`) | Trailer weight read from CAN, EV FMS |
| **`10897`** | Cargo Weight | `2 B` (`Unsigned`) | `kg` (`×2`) | `can.ev.cargo.weight` | `number` (`kg`) | Cargo weight read from CAN, EV FMS |
| **`10898`** | Powered Vehicle Weight | `2 B` (`Unsigned`) | `kg` (`×10`) | `can.ev.powered.vehicle.weight` | `number` (`kg`) | Powered vehicle weight read from CAN, EV FMS |
| **`10899`** | Gross Combination Vehicle Weight | `2 B` (`Unsigned`) | `kg` (`×10`) | `can.gross.combination.vehicle.weight` | `number` (`kg`) | Gross combination vehicle weight read from CAN |
| **`10901`** | Highest cell voltage | `2 B` (`Unsigned`) | `mV` (`×1`) | `can.ev.battery.max.cell.voltage` | `number` (`volts`) | High voltage battery highest cell voltage read from CAN, EV FMS |
| **`10902`** | Lowest cell voltage | `2 B` (`Unsigned`) | `mV` (`×1`) | `can.ev.battery.min.cell.voltage` | `number` (`volts`) | High voltage battery lowest cell voltage read from CAN, EV FMS |
| **`10903`** | HVESS Nominal Rated Capacity | `4 B` (`Unsigned`) | `%` (`×-`) | `can.ev.battery.rated.capacity` | `number` (`percentage`) | High voltage energy storage system nominal rated capacity read from CAN, EV FMS |
| **`10904`** | HVESS State of Health | `1 B` (`Unsigned`) | `%` (`×0,4`) | `can.vehicle.battery.health` | `number` (`percentage`) | Battery State of Health |

### Section `19_apache-thermograph` (134 Parameters)

| FMC650 `AVL ID` | Teltonika Property Name | Bytes / Type | Teltonika Units (Mult) | Official Flespi Parameter Name(s) | Flespi Type / Unit | Official Flespi Description |
|---:|---|---|---|---|---|---|
| **`13362`** | Device Serial Number | `4 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13363`** | Device Version | `17 B` (`Unisgned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13364`** | Datetime | `20 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13365`** | Sensor 1 Value | `2 B` (`Signed`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13366`** | Sensor 1 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13367`** | Sensor 2 Value | `2 B` (`Signed`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13368`** | Sensor 2 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13369`** | Senor 3 Value | `2 B` (`Signed`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13370`** | Sensor 3 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.lac` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`13371`** | Sensor 4 Value | `2 B` (`Signed`) | `-` (`×-`) | `gsm.cellid` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`13372`** | Sensor 4 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm` | `number` (`dbm`) | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`13373`** | Sensor 5 Value | `2 B` (`Signed`) | `-` (`×-`) | `gsm.mnc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) code |
| **`13374`** | Sensor 5 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.mcc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code |
| **`13375`** | Sensor 6 Value | `2 B` (`Signed`) | `-` (`×-`) | `gsm.lac` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`13376`** | Sensor 6 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`13377`** | Sensor 7 Value | `2 B` (`Signed`) | `-` (`×-`) | `gsm.signal.dbm` | `number` (`dbm`) | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`13378`** | Sensor 7 Unit | `1 B` (`Signed`) | `-` (`×-`) | `gsm.mnc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) code |
| **`13379`** | Sensor 8 Value | `2 B` (`Signed`) | `-` (`×-`) | `gsm.mcc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code |
| **`13380`** | Sensor 8 Unit | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.lac` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`13381`** | Device Status | `2 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`13382`** | Vehicle Plate | `16 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm` | `number` (`dbm`) | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`13383`** | Thermograph Battery Voltage | `2 B` (`Unsigned`) | `mV` (`×-`) | `gsm.mnc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) code |
| **`13384`** | Frigo Machine Type | `1 B` (`Unsigned`) | `-` (`×-`) | `gsm.mcc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code |
| **`13385`** | Frigo Overall and Engine Status | `2 B` (`Unsigned`) | `-` (`×-`) | `gsm.lac` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| **`13386`** | Frigo Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | `gsm.cellid` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| **`13387`** | Frigo Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | `gsm.signal.dbm` | `number` (`dbm`) | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| **`13388`** | Frigo Engine Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `gsm.mnc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) code |
| **`13389`** | Frigo Standby Hours | `4 B` (`Unsigned`) | `h` (`×-`) | `gsm.mcc` | `number` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code |
| **`13390`** | Frigo Switch on Hours | `4 B` (`Unsigned`) | `h` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13391`** | Frigo Active Alarms 1 to 4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13392`** | Frigo Active Alarms 5 to 8 | `0 B` (`0`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13393`** | Frigo Active Alarms 9 to 12 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13394`** | Frigo Active Alarms 13 to 16 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13395`** | Frigo Comp 1 Set Point | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13396`** | Frigo Comp 1 Supply | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13397`** | Frigo Comp 1 Return | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13398`** | Frigo Comp 1 Status | `2 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13399`** | Frigo Comp 2 Set Point | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13400`** | Frigo Comp 2 Supply | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13401`** | Frigo Comp 2 Return | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13402`** | Frigo Comp 2 Status | `2 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13403`** | Frigo Comp 3 Set Point | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13404`** | Frigo Comp 3 Supply | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13405`** | Frigo Comp 3 Return | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13406`** | Frigo Comp 3 Status | `2 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13407`** | EBS type | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13408`** | EBS Status | `2 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13409`** | EBS Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13410`** | EBS Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13411`** | EBS Wheel Speed | `1 B` (`Unsigned`) | `km/h` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13412`** | EBS Odometer | `4 B` (`Unsigned`) | `km/h` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13413`** | EBS Weight Load | `2 B` (`Unsigned`) | `10*t` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13414`** | EBS Pneumatic Supply | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13415`** | EBS Truck VIN | `18 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13416`** | EBS Active Alarms 1 to 4 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13417`** | EBS Active Alarms 5 to 8 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13418`** | EBS Active Alarms 9 to 12 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13419`** | EBS Active Alarms 13 to 16 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13420`** | EBS Security Status 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13421`** | EBS Security Status 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13422`** | EBS TPMS Status 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13423`** | EBS TPMS Status 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13424`** | EBS Tyre 1 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13425`** | EBS Tyre 1 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13426`** | EBS Tyre 1 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13427`** | EBS Tyre 1 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13428`** | EBS Tyre 1 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13429`** | EBS Tyre 1 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13430`** | EBS Tyre 2 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13431`** | EBS Tyre 2 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13432`** | EBS Tyre 2 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13433`** | EBS Tyre 2 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13434`** | EBS Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13435`** | EBS Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13436`** | EBS Tyre 3 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13437`** | EBS Tyre 3 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13438`** | EBS Tyre 3 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13439`** | EBS Tyre 3 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13440`** | EBS Tyre 3 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13441`** | EBS Tyre 3 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13442`** | EBS Tyre 4 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13443`** | EBS Tyre 4 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13444`** | EBS Tyre 4 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13445`** | EBS Tyre 4 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13446`** | EBS Tyre 4 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13447`** | EBS Tyre 4 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13448`** | EBS Tyre 5 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13449`** | EBS Tyre 5 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13450`** | EBS Tyre 5 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13451`** | EBS Tyre 5 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13452`** | EBS Tyre 5 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13453`** | EBS Tyre 5 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13454`** | EBS Tyre 6 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13455`** | EBS Tyre 6 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13456`** | EBS Tyre 6 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13457`** | EBS Tyre 6 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13458`** | EBS Tyre 6 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13459`** | EBS Tyre 6 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13548`** | EBS Tyre 7 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13549`** | EBS Tyre 7 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13550`** | EBS Tyre 7 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13551`** | EBS Tyre 7 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13552`** | EBS Tyre 7 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13553`** | EBS Tyre 7 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13554`** | EBS Tyre 8 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13555`** | EBS Tyre 8 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13556`** | EBS Tyre 8 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13557`** | EBS Tyre 8 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13558`** | EBS Tyre 8 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13559`** | EBS Tyre 8 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13560`** | EBS Tyre 9 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13561`** | EBS Tyre 9 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13562`** | EBS Tyre 9 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13563`** | EBS Tyre 9 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13564`** | EBS Tyre 9 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13565`** | EBS Tyre 9 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13566`** | EBS Tyre 10 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13567`** | EBS Tyre 10 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13568`** | EBS Tyre 10 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13569`** | EBS Tyre 10 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13570`** | EBS Tyre 10 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13571`** | EBS Tyre 10 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13572`** | EBS Tyre 11 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13573`** | EBS Tyre 11 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13574`** | EBS Tyre 11 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13575`** | EBS Tyre 11 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13576`** | EBS Tyre 11 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13577`** | EBS Tyre 11 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13578`** | EBS Tyre 12 Position | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13579`** | EBS Tyre 12 Pressure | `1 B` (`Unsigned`) | `10*Bar` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13580`** | EBS Tyre 12 Temperature | `2 B` (`Signed`) | `10*°C` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13581`** | EBS Tyre 12 Status | `1 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13582`** | EBS Tyre 12 Additional Data 0 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |
| **`13583`** | EBS Tyre 12 Additional Data 1 | `8 B` (`Unsigned`) | `-` (`×-`) | — *(Not in official Flespi table)* | — | — |

