---
title: "Official Flespi Full Parameters, Settings & Commands Reference — Teltonika FMC650"
device: "FMC650"
official_sources:
  - "https://flespi.com/devices/teltonika-fmc650"
  - "https://flespi.com/protocols/teltonika"
captured: "2026-11-05"
---

# Official Flespi Full Parameters, Device Settings & Commands Reference (`teltonika-fmc650`)

This standalone document contains **100% of the official Flespi definitions** for the **Teltonika FMC650** fetched directly from the official Flespi documentation ([`https://flespi.com/devices/teltonika-fmc650`](https://flespi.com/devices/teltonika-fmc650) and [`https://flespi.com/protocols/teltonika`](https://flespi.com/protocols/teltonika)).

> [!IMPORTANT]
> **Strict Domain Separation (Official Flespi Architecture)**:
> 1. **Telemetry Message Parameters (Section 1 — 1,161 parameters)**: Output by the Flespi `teltonika` channel parser when decoding incoming Codec 8 / Codec 8 Extended / Codec 16 packets from the FMC650. These map to **Teltonika Telemetry `AVL ID`s** (or packet headers), **never** to `.cfg` Configuration `ParameterId`s.
> 2. **Device Configuration Settings (Section 2 — 69 settings)**: High-level device configuration tabs managed by Flespi's Device Management layer over SMS / Codec 12 GPRS (`setparam` / `getparam` / `setio`). Never assume a manufacturer `.cfg` `ParameterId` maps 1-to-1 to a Flespi setting.
> 3. **Device Commands (Section 3 — 10 commands)**: Low-level and action commands (`setparam`, `getparam`, `setio`, `custom`, `request_tachograph_file`, etc.) exposed on the Flespi device.

## Summary Statistics

| Official Flespi Category | Total Count | Breakdown |
|---|---:|---|
| **1. Telemetry Message Parameters** | **1161** | **1133** mapped from Teltonika `AVL ID`s + **28** protocol/header/channel parameters |
| **2. Device Configuration Settings** | **69** | **58** configuration settings (composite/scalar/IO) + **11** action/readonly pseudo-settings |
| **3. Device Commands** | **10** | Includes `setparam`, `getparam`, `setio`, `custom`, `bluetooth`, `serial_port`, `garmin`, `request_tachograph_file`, `request_video`, `take_photo` |

---

## 1. Official Flespi Telemetry Message Parameters (1,161 Total)

### 1.1 Protocol, Packet Header & GNSS Envelope Telemetry Parameters (28 Parameters)

These 28 Flespi message parameters are extracted from the Flespi channel envelope, Codec 8/8E/16 header, Codec 12/14 command frames, or the standard 15-byte Teltonika GPS element (Timestamp, Priority, Longitude, Latitude, Altitude, Angle, Satellites, Speed) rather than an indexed `AVL ID`.

| # | Flespi Telemetry Parameter Name | Type | Unit | Official Flespi Description |
|---:|---|---|---|---|
| 1 | `camera.status` | `boolean` | — | Camera connected status |
| 2 | `channel.id` | `number` | — | ID of channel that received a message |
| 3 | `codec.id` | `number` | — | Decimal representation for Teltonika Codec ID 1-byte, 0x8E = 142 for Codec 8 Extended. |
| 4 | `command.type` | `number` | — | Command type |
| 5 | `custom` | `any` | — | Any custom parameter |
| 6 | `device.id` | `number` | — | ID of device that received a message |
| 7 | `device.name` | `string` | — | Name of device that received a message |
| 8 | `device.type.id` | `number` | — | ID of device type of device that received a message |
| 9 | `event.enum` | `number` | — | Protocol-specific event code |
| 10 | `event.priority.enum` | `number` | — | Event priority enum |
| 11 | `ident` | `string` | — | Device unique identifier like serial number, IMEI, etc |
| 12 | `media` | `boolean` | — | Message contain media file |
| 13 | `media.image` | `object` | — | Image file in media storage |
| 14 | `media.type.enum` | `number` | — | Media type enum |
| 15 | `media.type.enum.description` | `string` | — | Media type enum description |
| 16 | `media.video` | `object` | — | Video file in media storage |
| 17 | `payload.text` | `string` | — | Text Payload received from device |
| 18 | `peer` | `string` | — | IP:port from which device connecting to the channel |
| 19 | `position.altitude` | `number` | `meters` | Altitude value for position |
| 20 | `position.direction` | `number` | `degrees` | Heading angle at position detection moment |
| 21 | `position.latitude` | `number` | `degrees` | Latitude coordinate value |
| 22 | `position.longitude` | `number` | `degrees` | Longitude coordinate value |
| 23 | `position.media.latitude` | `number` | — | Latitude recorded by a media device. For example, a camera |
| 24 | `position.media.longitude` | `number` | — | Longitude recorded by a media device. For example, a camera |
| 25 | `position.satellites` | `number` | — | Quantity of satellites used to calculate coordinates for given position information |
| 26 | `protocol.id` | `number` | — | ID of protocol |
| 27 | `server.timestamp` | `number` | `seconds` | Timestamp when server received a message |
| 28 | `timestamp` | `number` | `seconds` | Message timestamp |

### 1.2 AVL ID-Sourced Telemetry Message Parameters (1,133 Parameters)

These 1,133 Flespi message parameters are decoded by the Flespi `teltonika` protocol parser from specific Teltonika **Telemetry `AVL ID`s** inside Codec 8 / Codec 8 Extended payloads.

| # | Flespi Telemetry Parameter Name | Type | Unit | Official Flespi Description | Official Flespi Sources (`AVL ID`) |
|---:|---|---|---|---|---|
| 1 | `absolute.acceleration` | `number` | `g` | Module of accelerometer vector | `AVL ID 23, , AVL ID 254` |
| 2 | `acceleration.array` | `array` | `g` | Array of objects with acceleration data by x, y, and z axis | `AVL ID 257` |
| 3 | `accelerometer.calibration.quality.level` | `number` | `percentage` | Accelerometer calibration quality | `AVL ID 1440` |
| 4 | `accelerometer.calibration.side.vector.delta` | `number` | `degrees` | Angle between the calculated accelerometer calibration and the actual device mounting position | `AVL ID 1437` |
| 5 | `accelerometer.calibration.state` | `number` | — | Accelerometer calibration state | `AVL ID 383` |
| 6 | `activity.state` | `number` | — | Device activity state | `AVL ID 395` |
| 7 | `actual.remaining.mileage` | `number` | `km` | Actual remaining mileage | `AVL ID 353` |
| 8 | `adas.ahead.object.distance` | `number` | `meters` | Distance to the object ahead reported by ADAS. Indexed by camera COM port. | `AVL ID 12961, , AVL ID 617` |
| 9 | `adas.ahead.object.speed` | `number` | `km/h` | Speed of the object ahead reported by ADAS. Indexed by camera COM port. | `AVL ID 12962, , AVL ID 618` |
| 10 | `adas.brake.signal.status` | `boolean` | — | Brake signal status reported by ADAS. Indexed by camera COM port. | `AVL ID 12947, , AVL ID 603` |
| 11 | `adas.camera.state` | `string` | — | ADAS camera operating state. Indexed by camera COM port. | `AVL ID 12967, , AVL ID 666` |
| 12 | `adas.camera.state.enum` | `number` | — | ADAS camera operating state. Numeric representation. Indexed by camera COM port. | `AVL ID 12967, , AVL ID 666` |
| 13 | `adas.collision.warning.state` | `string` | — | ADAS front collision warning state. Indexed by camera COM port. | `AVL ID 12957, , AVL ID 613` |
| 14 | `adas.collision.warning.state.enum` | `number` | — | ADAS front collision warning state. Numeric representation. Indexed by camera COM port. | `AVL ID 12957, , AVL ID 613` |
| 15 | `adas.distance.state` | `string` | — | ADAS safety distance alert state. Indexed by camera COM port. | `AVL ID 12954, , AVL ID 610` |
| 16 | `adas.distance.state.enum` | `number` | — | ADAS safety distance alert state. Numeric representation. Indexed by camera COM port. | `AVL ID 12954, , AVL ID 610` |
| 17 | `adas.engine.rpm` | `number` | `rpm` | Engine speed reported by ADAS. Indexed by camera COM port. | `AVL ID 12948, , AVL ID 604` |
| 18 | `adas.error.state` | `string` | — | ADAS camera error state. Indexed by camera COM port. | `AVL ID 12960, , AVL ID 616` |
| 19 | `adas.error.state.enum` | `number` | — | ADAS camera error state. Numeric representation. Indexed by camera COM port. | `AVL ID 12960, , AVL ID 616` |
| 20 | `adas.front.vehicle.start.state` | `string` | — | ADAS front vehicle start alarm state. Indexed by camera COM port. | `AVL ID 12955, , AVL ID 611` |
| 21 | `adas.front.vehicle.start.state.enum` | `number` | — | ADAS front vehicle start alarm state. Numeric representation. Indexed by camera COM port. | `AVL ID 12955, , AVL ID 611` |
| 22 | `adas.lane.departure.left.state` | `string` | — | ADAS left lane departure warning state. Indexed by camera COM port. | `AVL ID 12949, , AVL ID 605` |
| 23 | `adas.lane.departure.left.state.enum` | `number` | — | ADAS left lane departure warning state. Numeric representation. Indexed by camera COM port. | `AVL ID 12949, , AVL ID 605` |
| 24 | `adas.lane.departure.right.state` | `string` | — | ADAS right lane departure warning state. Indexed by camera COM port. | `AVL ID 12950, , AVL ID 606` |
| 25 | `adas.lane.departure.right.state.enum` | `number` | — | ADAS right lane departure warning state. Numeric representation. Indexed by camera COM port. | `AVL ID 12950, , AVL ID 606` |
| 26 | `adas.lane.left.distance` | `number` | `meters` | Distance to the left lane line reported by ADAS. Indexed by camera COM port. | `AVL ID 12951, , AVL ID 607` |
| 27 | `adas.lane.right.distance` | `number` | `meters` | Distance to the right lane line reported by ADAS. Indexed by camera COM port. | `AVL ID 12952, , AVL ID 608` |
| 28 | `adas.left.turn.signal.status` | `boolean` | — | Left turn signal status reported by ADAS. Indexed by camera COM port. | `AVL ID 12945, , AVL ID 601` |
| 29 | `adas.pedestrian.state` | `string` | — | ADAS pedestrian collision warning state. Indexed by camera COM port. | `AVL ID 12958, , AVL ID 614` |
| 30 | `adas.pedestrian.state.enum` | `number` | — | ADAS pedestrian collision warning state. Numeric representation. Indexed by camera COM port. | `AVL ID 12958, , AVL ID 614` |
| 31 | `adas.proximity.state` | `string` | — | ADAS front proximity warning state. Indexed by camera COM port. | `AVL ID 12956, , AVL ID 612` |
| 32 | `adas.proximity.state.enum` | `number` | — | ADAS front proximity warning state. Numeric representation. Indexed by camera COM port. | `AVL ID 12956, , AVL ID 612` |
| 33 | `adas.recording.state` | `string` | — | ADAS recording and microphone state. Indexed by camera COM port. | `AVL ID 12959, , AVL ID 615` |
| 34 | `adas.recording.state.enum` | `number` | — | ADAS recording and microphone state. Numeric representation. Indexed by camera COM port. | `AVL ID 12959, , AVL ID 615` |
| 35 | `adas.right.turn.signal.status` | `boolean` | — | Right turn signal status reported by ADAS. Indexed by camera COM port. | `AVL ID 12946, , AVL ID 602` |
| 36 | `adas.sdcard.state` | `string` | — | ADAS camera SD card state. Indexed by camera COM port. | `AVL ID 12966, , AVL ID 665` |
| 37 | `adas.sdcard.state.enum` | `number` | — | ADAS camera SD card state. Numeric representation. Indexed by camera COM port. | `AVL ID 12966, , AVL ID 665` |
| 38 | `adas.speed` | `number` | `km/h` | Vehicle speed reported by ADAS. Indexed by camera COM port. | `AVL ID 12944, , AVL ID 600` |
| 39 | `adas.speed.limit` | `number` | `km/h` | Speed limit recognized by ADAS. Indexed by camera COM port. | `AVL ID 12964, , AVL ID 620` |
| 40 | `adas.speed.limit.recognition.state` | `string` | — | ADAS speed limit recognition state. Indexed by camera COM port. | `AVL ID 12963, , AVL ID 619` |
| 41 | `adas.speed.limit.recognition.state.enum` | `number` | — | ADAS speed limit recognition state. Numeric representation. Indexed by camera COM port. | `AVL ID 12963, , AVL ID 619` |
| 42 | `adas.speed.limit.sensitivity` | `number` | `percentage` | ADAS speed limit recognition sensitivity. Indexed by camera COM port. | `AVL ID 12965, , AVL ID 621` |
| 43 | `adas.time.to.collision` | `number` | `seconds` | Time to collision reported by ADAS. Indexed by camera COM port. | `AVL ID 12953, , AVL ID 609` |
| 44 | `agro.vehicle.state.bitmask` | `number` | — | Agricultural machinery flags | `AVL ID 124, , AVL ID 39` |
| 45 | `ain` | `number` | `volts` | Voltage on the analog input | `AVL ID 10, , AVL ID 11, , AVL ID 14210, , AVL ID 19, , AVL ID 245, , AVL ID 6, , AVL ID 839, , AVL ID 840, , AVL ID 9, , AVL ID 9...10, , Command type 0x06` |
| 46 | `alarm.event` | `boolean` | — | Alarm event triggered | `AVL ID 236, , AVL ID 846` |
| 47 | `amber.alert.state` | `number` | — | Amber Alert state. 0 - Turned Off. 1 - Turned On, count down timer started. 2 - Amber Alert On button pressed to restard active timer. 3 - Alarm. 4 - Amber Alert turned On when timer is set to 0 seconds | `AVL ID 400` |
| 48 | `amber.alert.timeout` | `number` | — | Amber Alert time-out configured value | `AVL ID 401` |
| 49 | `available.status` | `boolean` | — | Vehicle available status: true - available, false - not available | `AVL ID 825` |
| 50 | `average.x.acceleration` | `number` | `g` | Harsh acceleration event average accelerometer value on X-axis | `AVL ID 1429, , AVL ID 259` |
| 51 | `average.y.acceleration` | `number` | `g` | Harsh acceleration event average accelerometer value on Y-axis | `AVL ID 1429, , AVL ID 259` |
| 52 | `average.z.acceleration` | `number` | `g` | Harsh acceleration event average accelerometer value on Z-axis | `AVL ID 1429, , AVL ID 259` |
| 53 | `barcode.id` | `string` | — | Barcode ID | `AVL ID 264` |
| 54 | `battery.capacity.full` | `number` | `Ah` | Full battery capacity | `AVL ID 829` |
| 55 | `battery.capacity.remaining` | `number` | `Ah` | Remaining battery capacity | `AVL ID 828` |
| 56 | `battery.charging.status` | `boolean` | — | Battery charging status | `AVL ID 347, , AVL ID 826` |
| 57 | `battery.current` | `number` | `amperes` | Battery current | `AVL ID 68` |
| 58 | `battery.health` | `number` | `percentage` | Battery health level (SoH) | `AVL ID 823` |
| 59 | `battery.level` | `number` | `percentage` | Internal battery level | `AVL ID 113, , AVL ID 142, , AVL ID 152, , AVL ID 824` |
| 60 | `battery.overvoltage.status` | `boolean` | — | Battery overvoltage status (true - battery overvoltage, false - no battery overvoltage) | `AVL ID 851` |
| 61 | `battery.regeneration.status` | `boolean` | — | Battery regeneration status: true - disabled, false - enabled | `AVL ID 848` |
| 62 | `battery.short.circuit` | `boolean` | — | Battery short circuit (overcurrent) warning status: true - battery short circuit, false - no battery short circuit | `AVL ID 852` |
| 63 | `battery.status` | `boolean` | — | Battery on/off status: true - battery is on, false - battery is off | `AVL ID 849` |
| 64 | `battery.temperature` | `number` | `celsius` | Battery temperature | `AVL ID 141, , AVL ID 151, , AVL ID 363, , AVL ID 364` |
| 65 | `battery.temperature.status` | `boolean` | — | Battery temperature status: true - temperature is over or under the normal, false - temperature is normal | `AVL ID 847` |
| 66 | `battery.undervoltage.status` | `boolean` | — | Battery undervoltage status: true - battery undervoltage, false - no battery undervoltage | `AVL ID 850` |
| 67 | `battery.voltage` | `number` | `volts` | Internal battery voltage | `AVL ID 67` |
| 68 | `ble.1.custom` | `number` | — | Custom indexed element for BLE sensor 1 | `AVL ID 331, , AVL ID 463...466` |
| 69 | `ble.1.custom.payload.hex` | `string` | — | Custom indexed element variable size payload for BLE sensor 1 | `AVL ID 331, , AVL ID 463...466, , AVL ID 713, , AVL ID 729...732` |
| 70 | `ble.2.custom` | `number` | — | Custom indexed element for BLE sensor 2 | `AVL ID 332, , AVL ID 467...470` |
| 71 | `ble.2.custom.payload.hex` | `string` | — | Custom indexed element variable size payload for BLE sensor 2 | `AVL ID 332, , AVL ID 467...470, , AVL ID 714, , AVL ID 733...736` |
| 72 | `ble.3.custom` | `number` | — | Custom indexed element for BLE sensor 3 | `AVL ID 333, , AVL ID 471...474` |
| 73 | `ble.3.custom.payload.hex` | `string` | — | Custom indexed element variable size payload for BLE sensor 3 | `AVL ID 333, , AVL ID 471...474, , AVL ID 715, , AVL ID 737...740` |
| 74 | `ble.4.custom` | `number` | — | Custom indexed element for BLE sensor 4 | `AVL ID 334, , AVL ID 475...478` |
| 75 | `ble.4.custom.payload.hex` | `string` | — | Custom indexed element variable size payload for BLE sensor 4 | `AVL ID 334, , AVL ID 475...478, , AVL ID 716, , AVL ID 741...744` |
| 76 | `ble.beacon.present` | `boolean` | — | BLE beacon presence indication | `AVL ID 1474` |
| 77 | `ble.beacons` | `array` | — | Standard parameter names used: *id* - beacon identification string. Usually it is beacon's UUID or MAC-address *local_name* - Beacons's Local Name *rssi* - BLE signal level. Units = dBm *battery.voltage* - Beacon's battery voltage. Units = volts *battery.level* - Beacon's battery level. Units = percentage *temperature* - Beacon's temperature. Units = celsius *humidity* - Beacon's humidity. Units = percentage | `AVL ID 10500, , AVL ID 10828, , AVL ID 10829, , AVL ID 10831, , AVL ID 11317, , AVL ID 385, , AVL ID 548` |
| 78 | `ble.lls.fuel.level` | `number` | — | Indexed BLE LLS fuel sensor value | `AVL ID 721...724` |
| 79 | `ble.lock.battery.level` | `number` | `percentage` | BLE (Bluetooth Low Energy) Electronic Lock battery level | `AVL ID 872` |
| 80 | `ble.lock.status` | `boolean` | — | BLE (Bluetooth Low Energy) Electronic lock is locked | `AVL ID 871` |
| 81 | `ble.mac.address` | `string` | — | BLE (Bluetooth Low Energy) MAC address | `AVL ID 13243...13252, , AVL ID 891` |
| 82 | `ble.nbl2.button.1.status` | `boolean` | — | BLE RFID reader Netronix NBL-2 button 1 status (4 programmable button states) | `AVL ID 455...458` |
| 83 | `ble.nbl2.button.2.status` | `boolean` | — | BLE RFID reader Netronix NBL-2 button 2 status (4 programmable button states) | `AVL ID 459...462` |
| 84 | `ble.nbl2.rfid` | `string` | — | BLE RFID reader Netronix NBL-2 indexed RFID code read | `AVL ID 451...454` |
| 85 | `ble.sensor.battery.level` | `number` | `percentage` | BLE (Bluetooth Low Energy) sensor battery level | `AVL ID 20, , AVL ID 22...23, , AVL ID 29, , AVL ID 705...708` |
| 86 | `ble.sensor.battery.voltage` | `number` | `volts` | BLE (Bluetooth Low Energy) sensor battery voltage | `AVL ID 10824...10827, , AVL ID 13222...13226, , AVL ID 20, , AVL ID 22...23, , AVL ID 29, , AVL ID 523` |
| 87 | `ble.sensor.battery.voltage.error.code` | `string` | — | Indexed BLE battery voltage sensor error description | `AVL ID 10824...10827` |
| 88 | `ble.sensor.device.name` | `string` | — | BLE (Bluetooth Low Energy) sensor device name | `AVL ID 13325...13334` |
| 89 | `ble.sensor.frequency` | `number` | — | Indexed BLE frequency sensor value | `AVL ID 306...309, , AVL ID 725...728` |
| 90 | `ble.sensor.humidity` | `number` | `percentage` | BLE (Bluetooth Low Energy) sensor Humidity value | `AVL ID 104, , AVL ID 106, , AVL ID 108, , AVL ID 10804...10807, , AVL ID 13335...13339, , AVL ID 525, , AVL ID 709...712, , AVL ID 86` |
| 91 | `ble.sensor.humidity.error.code` | `string` | — | BLE humidity sensor error description | `AVL ID 104, , AVL ID 106, , AVL ID 108, , AVL ID 10804...10807, , AVL ID 13335...13339, , AVL ID 525, , AVL ID 86` |
| 92 | `ble.sensor.illuminance` | `number` | `lux` | BLE (Bluetooth Low Energy) sensor illuminance | `AVL ID 335...338, , AVL ID 717...720` |
| 93 | `ble.sensor.low.battery.error.code` | `string` | — | Indexed BLE low battery sensor error description | `AVL ID 10820...10823, , AVL ID 13253...13258` |
| 94 | `ble.sensor.low.battery.status` | `boolean` | — | Indexed low battery indication BLE sensor | `AVL ID 10820...10823, , AVL ID 13253...13258` |
| 95 | `ble.sensor.magnet.count` | `number` | — | Indexed magnet count value of BLE Sensor | `AVL ID 10840...10843` |
| 96 | `ble.sensor.magnet.count.error.code` | `string` | — | Indexed BLE magnet count sensor error description | `AVL ID 10840...10843` |
| 97 | `ble.sensor.magnet.status` | `boolean` | — | Indexed magnet state measured by BLE sensor | `AVL ID 10808...10811, , AVL ID 13460...13465` |
| 98 | `ble.sensor.magnet.status.error.code` | `string` | — | Indexed BLE magnet sensor error description | `AVL ID 10808...10811, , AVL ID 13460...13465` |
| 99 | `ble.sensor.movement.count` | `number` | — | Indexed movement count value of BLE Sensor | `AVL ID 10812...10815, , AVL ID 10836...10839, , AVL ID 13468...13473` |
| 100 | `ble.sensor.movement.count.error.code` | `string` | — | Indexed BLE movement count sensor error description | `AVL ID 10836...10839` |
| 101 | `ble.sensor.movement.error.code` | `string` | — | Indexed movement BLE sensor error code | `AVL ID 10812...10815` |
| 102 | `ble.sensor.movement.status` | `boolean` | — | Indexed movement state measured by BLE sensor | `AVL ID 10812...10815` |
| 103 | `ble.sensor.pitch.angle` | `number` | `degrees` | Indexed pitch angle measured by BLE sensor | `AVL ID 10816...10819, , AVL ID 13474...13479` |
| 104 | `ble.sensor.pitch.angle.error.code` | `string` | — | Indexed BLE pitch angle sensor error description | `AVL ID 10816...10819, , AVL ID 13474...13479` |
| 105 | `ble.sensor.roll.angle` | `number` | `degrees` | Indexed roll angle measured by BLE sensor | `AVL ID 10832...10835, , AVL ID 13480...13485` |
| 106 | `ble.sensor.roll.angle.error.code` | `string` | — | Indexed BLE roll angle sensor error description | `AVL ID 10832...10835, , AVL ID 13480...13485` |
| 107 | `ble.sensor.rssi` | `number` | `dbm` | BLE (Bluetooth Low Energy) sensor RSSI signal strength | `AVL ID 13233...13242` |
| 108 | `ble.sensor.temperature` | `number` | `celsius` | BLE (Bluetooth Low Energy) sensor Temperature value | `AVL ID 10800...10803, , AVL ID 13227...13232, , AVL ID 25, , AVL ID 25...28, , AVL ID 26...28, , AVL ID 701...704` |
| 109 | `ble.sensor.temperature.error.code` | `string` | — | BLE temperature sensor error description | `AVL ID 10800...10803, , AVL ID 13227...13232, , AVL ID 25...28, , AVL ID 701...704` |
| 110 | `bluetooth.device.mac.address` | `string` | — | MAC address of bluetooth-connected peripheral device | `AVL ID 238` |
| 111 | `bluetooth.state.enum` | `number` | — | Bluetooth state: 0 - BT is disabled 1 - BT Enabled, not device connected 2 - Device connected, BTv3 Only 3 - Device connected, BLE only 4 - Device connected, BLE + BT | `AVL ID 263` |
| 112 | `button.action.type` | `number` | — | Button Action type: 1 - 1 click 2 - 2 clicks 3 - long click | `AVL ID 389, , AVL ID 392` |
| 113 | `button.id` | `number` | — | The number of the button pressed | `AVL ID 389, , AVL ID 392` |
| 114 | `button.pressed.status` | `boolean` | — | Any operate button in the car was put | `AVL ID 132, , AVL ID 47` |
| 115 | `buzzer.alarm.status` | `boolean` | — | Buzzer alarm status | `AVL ID 345` |
| 116 | `cable.connected.status` | `boolean` | — | Charging cable connected status | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 914` |
| 117 | `camera.front.operating.state` | `string` | — | Front camera running state. Indexed by camera COM port. | `AVL ID 12969, , AVL ID 12971, , AVL ID 12972, , AVL ID 12974` |
| 118 | `camera.front.operating.state.enum` | `number` | — | Front camera running state. Number representation. Indexed by camera COM port. | `AVL ID 12969, , AVL ID 12971, , AVL ID 12972, , AVL ID 12974` |
| 119 | `camera.front.state` | `string` | — | Front camera ping transmission and TF status. Indexed by camera COM port. | `AVL ID 12301, , AVL ID 12303, , AVL ID 12304, , AVL ID 12306` |
| 120 | `camera.front.state.enum` | `number` | — | Front camera ping transmission and TF status. Number representation. Indexed by camera COM port. | `AVL ID 12301, , AVL ID 12303, , AVL ID 12304, , AVL ID 12306` |
| 121 | `camera.rear.operating.state` | `string` | — | Rear camera running state. Indexed by camera COM port. | `AVL ID 12970, , AVL ID 12973` |
| 122 | `camera.rear.operating.state.enum` | `number` | — | Rear camera running state. Number representation. Indexed by camera COM port. | `AVL ID 12970, , AVL ID 12973` |
| 123 | `camera.rear.state` | `string` | — | Rear camera ping transmission and TF status. Indexed by camera COM port. | `AVL ID 12302, , AVL ID 12305` |
| 124 | `camera.rear.state.enum` | `number` | — | Rear camera ping transmission and TF status. Number representation. Indexed by camera COM port. | `AVL ID 12302, , AVL ID 12305` |
| 125 | `camera.report.reason` | `string` | — | Camera report reason | `AVL ID 498` |
| 126 | `camera.report.reason.enum` | `number` | — | Camera report reason ID | `AVL ID 498` |
| 127 | `camera.state` | `string` | — | Front camera ping transmission and TF status checking parameters ID | `AVL ID 499` |
| 128 | `camera.state.enum` | `number` | — | Front camera ping transmission and TF status checking parameters ID. Number representation. | `AVL ID 499` |
| 129 | `camera.type` | `string` | — | Connected camera type | `AVL ID 12301, , AVL ID 12302, , AVL ID 12303, , AVL ID 12304, , AVL ID 12305, , AVL ID 12306, , AVL ID 12969, , AVL ID 12970, , AVL ID 12971, , AVL ID 12972, , AVL ID 12973, , AVL ID 12974` |
| 130 | `can.abs.failure.indicator.state` | `string` | — | Vehicle parameter for anti-lock brake system failure indicator read from CAN | `AVL ID 10429` |
| 131 | `can.abs.failure.indicator.status` | `boolean` | — | ABS failure indicator status read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 954` |
| 132 | `can.absolute.fuel.rail.pressure` | `number` | `kPa` | Absolute fuel rail pressure | `AVL ID 56` |
| 133 | `can.absolute.load` | `number` | `percentage` | Absolute load value - the normalized value of air mass per intake stroke, read from CAN | `AVL ID 52` |
| 134 | `can.abs.trailer.indicator.state` | `string` | — | Vehicle parameter for ABS trailer indicator read from CAN | `AVL ID 10431` |
| 135 | `can.acceleration.rate.limit.state` | `number` | — | Vehicle acceleration rate limit status | `AVL ID 939` |
| 136 | `can.accelerator.pedal.kickdown.switch.state` | `number` | — | Accelerator pedal kickdown switch status | `AVL ID 931` |
| 137 | `can.accelerator.pedal.low.idle.switch.state` | `number` | — | Accelerator pedal low idle switch status, indexed parameter | `AVL ID 930, , AVL ID 933` |
| 138 | `can.accelerator.pedal.position` | `number` | `percentage` | Accelerator pedal position read from CAN | `AVL ID 934, , AVL ID 938` |
| 139 | `can.activated.batteries` | `number` | — | Activated batteries from CAN bus | `AVL ID 1160` |
| 140 | `can.actual.engine.additional.torque` | `number` | — | Actual engine additional torque in percent of the reference engine torque (fractional) | `AVL ID 946` |
| 141 | `can.actual.engine.torque` | `number` | `percentage` | Actual calculated output torque of the engine | `AVL ID 948` |
| 142 | `can.adaptive.cruise.control.indicator.state` | `string` | — | Vehicle parameter for adaptive cruise control indicator read from CAN | `AVL ID 10431` |
| 143 | `can.adblue.level` | `number` | `percentage` | AdBlue (diesel exhaust fluid) level read from CAN | `AVL ID 10455, , AVL ID 111, , AVL ID 19` |
| 144 | `can.adblue.level.indicator.state` | `string` | — | Vehicle parameter for AdBlue level indicator read from CAN | `AVL ID 10430` |
| 145 | `can.adblue.level.low.indicator.status` | `boolean` | — | Low AdBlue level indicator from CAN bus | `AVL ID 519, , AVL ID 987` |
| 146 | `can.adblue.tempering.indicator.state` | `string` | — | Vehicle parameter for AdBlue tempering indicator read from CAN | `AVL ID 13259` |
| 147 | `can.adblue.volume` | `number` | `liters` | AdBlue (diesel exhaust fluid) volume read from CAN | `AVL ID 112, , AVL ID 20` |
| 148 | `can.additional.front.lights.status` | `boolean` | — | Additional front lights turned on status, read from CAN | `AVL ID 518, , AVL ID 933` |
| 149 | `can.additional.rear.lights.status` | `boolean` | — | Additional rear lights turned on status, read from CAN | `AVL ID 518, , AVL ID 934` |
| 150 | `can.airbag.indicator.state` | `string` | — | Vehicle parameter for airbag indicator read from CAN | `AVL ID 10431` |
| 151 | `can.airbag.indicator.status` | `boolean` | — | Airbag indicator status read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 962` |
| 152 | `can.air.condition.status` | `boolean` | — | CAN air conditioning is on | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 936` |
| 153 | `can.air.filter.clogged.indicator.state` | `string` | — | Vehicle parameter for air filter clogged indicator read from CAN | `AVL ID 10431` |
| 154 | `can.air.filter.plugged.indicator.status` | `boolean` | — | Air filter is plugged indicator from CAN bus | `AVL ID 519, , AVL ID 982` |
| 155 | `can.alternator.current` | `number` | `amperes` | Measure of electrical current flow from the alternator | `AVL ID 1053` |
| 156 | `can.ambient.air.temperature` | `number` | `celsius` | CAN ambient air temperature | `AVL ID 1188, , AVL ID 128, , AVL ID 1396, , AVL ID 53` |
| 157 | `can.articulation.indicator.state` | `string` | — | Vehicle parameter for articulation indicator read from CAN | `AVL ID 10430` |
| 158 | `can.automatic.retarder.status` | `boolean` | — | Automatic retarder status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 938` |
| 159 | `can.auxiliary.air.pressure.indicator.state` | `string` | — | Vehicle parameter for auxiliary air pressure indicator read from CAN | `AVL ID 10431` |
| 160 | `can.available.engine.torque` | `number` | `percentage` | Actual maximum available engine - percent torque | `AVL ID 943` |
| 161 | `can.average.fuel.economy` | `number` | `km/liters` | CAN average fuel economy | `AVL ID 1037` |
| 162 | `can.axle.weight` | `number` | `kg` | Weight on the axle read from CAN | `AVL ID 118...122, , AVL ID 26...29, , AVL ID 32, , AVL ID 89...103` |
| 163 | `can.barometric.pressure` | `number` | `kPa` | Absolute barometric pressure read from CAN | `AVL ID 50` |
| 164 | `can.battery1.current` | `number` | `amperes` | Battery 1 current from CAN bus | `AVL ID 1163` |
| 165 | `can.battery1.power.stage.temperature` | `number` | `celsius` | Battery 1 power stage temp from CAN bus | `AVL ID 1168` |
| 166 | `can.battery1.remaining.capacity` | `number` | `Ah` | Battery 1 remaining capacity from CAN bus | `AVL ID 1169` |
| 167 | `can.battery1.soc` | `number` | — | Battery 1 SoC from CAN bus | `AVL ID 1165` |
| 168 | `can.battery1.state.enum` | `number` | — | Battery 1 state from CAN bus | `AVL ID 1164` |
| 169 | `can.battery1.temperature` | `number` | `celsius` | Indexed battery 1 temperature from CAN bus | `AVL ID 1166, , AVL ID 1167` |
| 170 | `can.battery1.voltage` | `number` | `volts` | Battery 1 voltage from CAN bus | `AVL ID 1162` |
| 171 | `can.battery2.current` | `number` | `amperes` | Battery 2 current from CAN bus | `AVL ID 1171` |
| 172 | `can.battery2.power.stage.temperature` | `number` | `celsius` | Battery 2 power stage temp from CAN bus | `AVL ID 1176` |
| 173 | `can.battery2.remaining.capacity` | `number` | `Ah` | Battery 2 remaining capacity from CAN bus | `AVL ID 1177` |
| 174 | `can.battery2.soc` | `number` | — | Battery 2 SoC from CAN bus | `AVL ID 1173` |
| 175 | `can.battery2.state.enum` | `number` | — | Battery 2 state from CAN bus | `AVL ID 1172` |
| 176 | `can.battery2.temperature` | `number` | `celsius` | Indexed battery 2 temperature from CAN bus | `AVL ID 1174, , AVL ID 1175` |
| 177 | `can.battery2.voltage` | `number` | `volts` | Battery 2 voltage from CAN bus | `AVL ID 1170` |
| 178 | `can.battery.charging.indicator.state` | `string` | — | Vehicle parameter for battery charging condition indicator read from CAN | `AVL ID 10428` |
| 179 | `can.battery.error.code` | `string` | — | Battery error code read from CAN | `AVL ID 1178, , AVL ID 1179` |
| 180 | `can.battery.indicator.status` | `boolean` | — | Battery indicator status read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 960` |
| 181 | `can.battery.pack.cooling.indicator.state` | `string` | — | Vehicle parameter for battery pack cooling indicator read from CAN | `AVL ID 13259` |
| 182 | `can.battery.pack.indicator.state` | `string` | — | Vehicle parameter for battery pack indicator read from CAN | `AVL ID 13259` |
| 183 | `can.battery.pack.temperature.indicator.state` | `string` | — | Vehicle parameter for battery pack temperature indicator read from CAN | `AVL ID 13259` |
| 184 | `can.battery.voltage` | `number` | `volts` | Battery voltage read from CAN | `AVL ID 1184, , AVL ID 168, , AVL ID 507` |
| 185 | `can.brake.failure.indicator.state` | `string` | — | Vehicle parameter for brake failure/brake system malfunction indicator read from CAN | `AVL ID 10428` |
| 186 | `can.brake.lights.indicator.state` | `string` | — | Vehicle parameter for brake lights indicator read from CAN | `AVL ID 10430` |
| 187 | `can.brake.pedal.level` | `number` | `percentage` | Brake pedal push level read from CAN | `AVL ID 1201, , AVL ID 357` |
| 188 | `can.brake.pressure` | `number` | `kPa` | Brake application pressure from CAN bus | `AVL ID 1120` |
| 189 | `can.brake.system.filter.clogged.indicator.status` | `boolean` | — | Clogged brake system filter indicator from CAN bus | `AVL ID 519, , AVL ID 985` |
| 190 | `can.bus.stop.brake.indicator.state` | `string` | — | Vehicle parameter for bus stop brake indicator read from CAN | `AVL ID 10430` |
| 191 | `can.car.closed.remote.status` | `boolean` | — | Car closed by factory's remote control, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 917` |
| 192 | `can.car.closed.status` | `boolean` | — | Car closed status, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 662` |
| 193 | `can.car.closing.remote.event` | `boolean` | — | Signal of closing with factory remote control was sent, read from CAN | `AVL ID 517, , AVL ID 920` |
| 194 | `can.car.opening.remote.event` | `boolean` | — | Signal of opening with factory remote control was sent, read from CAN | `AVL ID 517, , AVL ID 921` |
| 195 | `can.car.triple.closing.remote.event` | `boolean` | — | Signal of closing with factory remote control was sent 3 times, read from CAN | `AVL ID 517, , AVL ID 925` |
| 196 | `can.catalyst.differential.pressure` | `number` | `kPa` | Exhaust differential pressure measured between the intake and exhaust of a diesel oxidation catalyst in exhaust bank parameter is indexed by bank number | `AVL ID 955` |
| 197 | `can.catalyst.intake.temperature` | `number` | `celsius` | Temperature of engine combustion byproducts entering the diesel oxidation catalyst in exhaust bank parameter is indexed by bank number | `AVL ID 953` |
| 198 | `can.catalyst.outlet.temperature` | `number` | `celsius` | Temperature of engine combustion byproducts leaving the diesel oxidation catalyst exhaust in exhaust bank parameter is indexed by bank number | `AVL ID 954` |
| 199 | `can.central.differential.4hi.status` | `boolean` | — | Central differential 4HI locked status, read from CAN | `AVL ID 518, , AVL ID 949` |
| 200 | `can.central.differential.4lo.status` | `boolean` | — | Central differential with reductor 4LO locked status, read from CAN | `AVL ID 518, , AVL ID 950` |
| 201 | `can.check.engine.indicator.status` | `boolean` | — | Check engine indicator status read from CAN | `AVL ID 123, , AVL ID 38` |
| 202 | `can.cleaning.fan.control.status` | `boolean` | — | Cleaning fan control status: true - on, false - off, read from CAN | `AVL ID 520` |
| 203 | `can.cluster.current` | `number` | `amperes` | Cluster current from CAN bus | `AVL ID 1155` |
| 204 | `can.cluster.error.code` | `string` | — | Cluster error code from CAN bus in hex form | `AVL ID 1180` |
| 205 | `can.cluster.soc` | `number` | `percentage` | Cluster SoC from CAN bus | `AVL ID 1148` |
| 206 | `can.cluster.state.enum` | `number` | — | Cluster state from CAN bus | `AVL ID 1147` |
| 207 | `can.cluster.voltage` | `number` | `volts` | Cluster voltage from CAN bus | `AVL ID 1154` |
| 208 | `can.cng.consumed` | `number` | `kg` | Consumed of compressed natural gas read from CAN | `AVL ID 227, , AVL ID 233` |
| 209 | `can.cng.level` | `number` | `percentage` | Compressed natural gas level read from CAN | `AVL ID 228, , AVL ID 234` |
| 210 | `can.cng.level.low.indicator.status` | `boolean` | — | Low CNG level indicator from CAN bus | `AVL ID 519, , AVL ID 992` |
| 211 | `can.cng.status` | `boolean` | — | Compressed natural gas status read from CAN | `AVL ID 226, , AVL ID 232, , AVL ID 517, , AVL ID 903` |
| 212 | `can.com.error.status` | `boolean` | — | COM Error status from CAN bus | `AVL ID 1129` |
| 213 | `can.commanded.egr` | `number` | `percentage` | Commanded EGR value read from CAN | `AVL ID 46` |
| 214 | `can.connection.state` | `number` | — | The car CAN bus synchronization state | `AVL ID 132, , AVL ID 47, , AVL ID 517` |
| 215 | `can.control.module.voltage` | `number` | `volts` | Control module voltage read from CAN | `AVL ID 51` |
| 216 | `can.coolant.level.low.indicator.status` | `boolean` | — | Coolant level low indicator status read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 976` |
| 217 | `can.coolant.liquid.indicator.status` | `boolean` | — | Coolant liquid temperature / level indicator from CAN bus | `AVL ID 519, , AVL ID 959` |
| 218 | `can.cooling.air.conditioning.indicator.state` | `string` | — | Vehicle parameter for cooling air conditioning indicator read from CAN | `AVL ID 10428` |
| 219 | `can.corn.header.connected.status` | `boolean` | — | Corn header connected status, read from CAN | `AVL ID 520` |
| 220 | `can.counted.engine.motorhours` | `number` | `hours` | Engine Worktime counted by the IoT device from 0 starting from the connection of the CAN adapter or CAN device | `AVL ID 103` |
| 221 | `can.cruise.control.state` | `number` | — | Cruise control state read from CAN | `AVL ID 1195` |
| 222 | `can.cruise.status` | `boolean` | — | CAN cruise control is active | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 81, , AVL ID 937` |
| 223 | `can.data.frame` | `string` | — | CAN data frame value in HEX representation, indexed by CAN message ID or element identifier | `AVL ID 900...929` |
| 224 | `can.direct.fuel.rail.pressure` | `number` | `kPa` | Fuel rail gauge pressure for diesel or gasoline direct injection | `AVL ID 45` |
| 225 | `can.disabled.persons.indicator.state` | `string` | — | Vehicle parameter for provision for disabled/handicapped persons indicator read from CAN | `AVL ID 10428` |
| 226 | `can.discharge.time` | `number` | `seconds` | Time to empty from CAN bus | `AVL ID 1145` |
| 227 | `can.distance.since.codes.cleared` | `number` | `km` | Distance traveled since codes cleared | `AVL ID 49` |
| 228 | `can.dpf.thermal.management.state` | `number` | — | DPF thermal management active | `AVL ID 941` |
| 229 | `can.drive.gear.status` | `boolean` | — | CAN drive gear is on | `AVL ID 517, , AVL ID 927` |
| 230 | `can.driver.demand.engine.torque` | `number` | `percentage` | Requested torque output of the engine by the driver | `AVL ID 947` |
| 231 | `can.driver.seatbelt.indicator.status` | `boolean` | — | Driver's seatbelt indicator status read from CAN | `AVL ID 123, , AVL ID 38` |
| 232 | `can.driver.seatbelt.status` | `boolean` | — | Driver's seatbelt fastened status, read from CAN | `AVL ID 10631, , AVL ID 1194, , AVL ID 518, , AVL ID 940` |
| 233 | `can.dtc` | `array` | — | Diagnostic trouble code array read from CAN May content list of OBDII codes or list of objects with codes. Standard object parameter names used: *standard* - Protocol standard (J1939, J1708(J1587), OBDII) *mid* - Message Identifier (J1708) *sid* - Subsystem Identifier (J1708) *fmi* - Failure Mode Identifier (J1939, J1708) *spn* - Suspect Parameter Number (J1939) *sa* - Source Address (J1939, OBDII) *oc* - Occurrence Count (J1939) *cm* - Conversion Method (J1939) *status* - Status of error code (active, pending, historical, permanent) | `AVL ID 10493, , AVL ID 10494, , AVL ID 10495, , AVL ID 10496, , AVL ID 281, , AVL ID 282, , AVL ID 525` |
| 234 | `can.dtc.number` | `number` | — | Number of diagnostic trouble codes | `AVL ID 1182, , AVL ID 160, , AVL ID 176, , AVL ID 30` |
| 235 | `can.dual.fuel.status` | `boolean` | — | Engine working on dual fuel status, read from CAN bus | `AVL ID 1083` |
| 236 | `can.dynamic.ignition.status` | `boolean` | — | Dynamic ignition is ON, read from CAN | `AVL ID 132, , AVL ID 47` |
| 237 | `can.ear.auger.speed.status` | `boolean` | — | Ear auger speed normal status, read from CAN: true - Ok, false - below normal | `AVL ID 520` |
| 238 | `can.ebs.indicator.state` | `string` | — | Vehicle parameter for EBS indicator read from CAN | `AVL ID 10431` |
| 239 | `can.ebs.trailer.indicator.state` | `string` | — | Vehicle parameter for EBS trailer indicator read from CAN | `AVL ID 10431` |
| 240 | `can.egr.error` | `number` | `percentage` | EGR Error read from CAN | `AVL ID 47` |
| 241 | `can.electronic.power.control.status` | `boolean` | — | Electronic power control status, read from CAN | `AVL ID 123, , AVL ID 38` |
| 242 | `can.emergency.braking.system.indicator.state` | `string` | — | Vehicle parameter for advanced emergency braking system indicator read from CAN | `AVL ID 10431` |
| 243 | `can.engine.compartment.temperature.indicator.state` | `string` | — | Vehicle parameter for engine compartment temperature indicator read from CAN | `AVL ID 10430` |
| 244 | `can.engine.coolant.level` | `number` | `percentage` | Engine coolant level read from CAN | `AVL ID 1197` |
| 245 | `can.engine.coolant.level.indicator.state` | `string` | — | Vehicle parameter for engine coolant level indicator read from CAN | `AVL ID 10429` |
| 246 | `can.engine.coolant.pressure` | `number` | `kPa` | Engine coolant pressure | `AVL ID 1198` |
| 247 | `can.engine.coolant.temperature` | `number` | `celsius` | Engine coolant temperature read from CAN | `AVL ID 1002, , AVL ID 127, , AVL ID 32` |
| 248 | `can.engine.coolant.temperature.indicator.state` | `string` | — | Vehicle parameter for engine coolant temperature indicator read from CAN | `AVL ID 10428` |
| 249 | `can.engine.emission.failure.indicator.state` | `string` | — | Vehicle parameter for engine emission system failure (MIL) indicator read from CAN | `AVL ID 10430` |
| 250 | `can.engine.emission.filter.indicator.state` | `string` | — | Vehicle parameter for engine emission filter (soot filter) indicator read from CAN | `AVL ID 13259` |
| 251 | `can.engine.fuel.rate` | `number` | `liters/h` | Engine fuel rate read from CAN | `AVL ID 1035, , AVL ID 110, , AVL ID 18` |
| 252 | `can.engine.ignition.status` | `boolean` | — | CAN engine ignition status | `AVL ID 10883, , AVL ID 1178, , AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 898` |
| 253 | `can.engine.intercooler.temperature` | `number` | `celsius` | Temperature of liquid found in the intercooler located after the turbocharger | `AVL ID 1006` |
| 254 | `can.engine.load` | `number` | `percentage` | Engine percent load at current speed | `AVL ID 1189, , AVL ID 936` |
| 255 | `can.engine.load.level` | `number` | `percentage` | Calculated engine load level read from CAN | `AVL ID 114, , AVL ID 23, , AVL ID 31, , AVL ID 85` |
| 256 | `can.engine.lock.status` | `boolean` | — | Engine lock status read from CAN | `AVL ID 517, , AVL ID 907` |
| 257 | `can.engine.maximum.power.support.state` | `number` | — | Momentary engine maximum power enable feedback | `AVL ID 940` |
| 258 | `can.engine.mil.indicator.state` | `string` | — | Vehicle parameter for engine/MIL indicator read from CAN | `AVL ID 10429` |
| 259 | `can.engine.motorhours` | `number` | `hours` | Total engine motorhours (engine work time) read from CAN | `AVL ID 102, , AVL ID 103, , AVL ID 1177, , AVL ID 14, , AVL ID 15, , AVL ID 991` |
| 260 | `can.engine.oil.filter.plugged.indicator.status` | `boolean` | — | Engine oil filter plugged indicator from CAN bus | `AVL ID 519, , AVL ID 973` |
| 261 | `can.engine.oil.indicator.state` | `string` | — | Vehicle parameter for engine oil indicator read from CAN | `AVL ID 10428` |
| 262 | `can.engine.oil.level` | `number` | `percentage` | Engine oil level read from CAN | `AVL ID 1159, , AVL ID 524` |
| 263 | `can.engine.oil.level.indicator.state` | `string` | — | Vehicle parameter for engine oil level indicator read from CAN | `AVL ID 10429` |
| 264 | `can.engine.oil.pressure` | `number` | `kPa` | CAN Engine oil pressure | `AVL ID 1158, , AVL ID 1193` |
| 265 | `can.engine.oil.temperature` | `number` | `celsius` | Engine oil temperature read from CAN | `AVL ID 1191, , AVL ID 1270, , AVL ID 13154, , AVL ID 58` |
| 266 | `can.engine.oil.temperature.high.indicator.status` | `boolean` | — | Too high engine oil temperature indicator from CAN bus | `AVL ID 519, , AVL ID 975` |
| 267 | `can.engine.oil.temperature.indicator.state` | `string` | — | Vehicle parameter for engine oil temperature indicator read from CAN | `AVL ID 10429` |
| 268 | `can.engine.rpm` | `number` | `rpm` | Engine RPM read from CAN | `AVL ID 1130, , AVL ID 35, , AVL ID 36, , AVL ID 85, , AVL ID 88, , AVL ID 949` |
| 269 | `can.engine.run.time` | `number` | `seconds` | Run time since engine start read from CAN | `AVL ID 42` |
| 270 | `can.engine.temperature` | `number` | `celsius` | Engine temperature read from CAN | `AVL ID 115, , AVL ID 25, , AVL ID 32` |
| 271 | `can.engine.torque.mode` | `number` | — | Engine torque mode | `AVL ID 945` |
| 272 | `can.engine.turbocharger.oil.temperature` | `number` | `celsius` | Temperature of the turbocharger lubricant | `AVL ID 1005` |
| 273 | `can.engine.working.status` | `boolean` | — | Engine is working, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 900` |
| 274 | `can.epc.indicator.status` | `boolean` | — | EPC (Electronic Power Control) indicator status from CAN bus | `AVL ID 519, , AVL ID 972` |
| 275 | `can.eps.indicator.status` | `boolean` | — | Electric power steering indicator status, reaf from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 963` |
| 276 | `can.equivalence.ratio` | `number` | — | Fuel-air commanded equivalence ratio read from CAN | `AVL ID 541` |
| 277 | `can.esc.indicator.state` | `string` | — | Vehicle parameter for ESC indication read from CAN | `AVL ID 10430` |
| 278 | `can.esc.switched.off.indicator.state` | `string` | — | Vehicle parameter for ESC switched off indicator read from CAN | `AVL ID 10431` |
| 279 | `can.esp.indicator.status` | `boolean` | — | Electronic stability program indicator status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 955` |
| 280 | `can.esp.status` | `boolean` | — | CAN ESP warning is on | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 956` |
| 281 | `can.ev.air.conditioner.compressor.state.enum` | `number` | — | Air conditioner compressor state read from CAN, EV FMS | `AVL ID 10892` |
| 282 | `can.ev.battery.current` | `number` | `amperes` | High voltage battery current read from CAN, EV FMS | `AVL ID 10880` |
| 283 | `can.ev.battery.level` | `number` | `percentage` | High voltage battery state of charge read from CAN, EV FMS | `AVL ID 10882` |
| 284 | `can.ev.battery.max.cell.voltage` | `number` | `volts` | High voltage battery highest cell voltage read from CAN, EV FMS | `AVL ID 10901` |
| 285 | `can.ev.battery.max.temperature` | `number` | `celsius` | High voltage battery highest cell temperature read from CAN, EV FMS | `AVL ID 10889` |
| 286 | `can.ev.battery.min.cell.voltage` | `number` | `volts` | High voltage battery lowest cell voltage read from CAN, EV FMS | `AVL ID 10902` |
| 287 | `can.ev.battery.min.temperature` | `number` | `celsius` | High voltage battery lowest cell temperature read from CAN, EV FMS | `AVL ID 10890` |
| 288 | `can.ev.battery.rated.capacity` | `number` | `percentage` | High voltage energy storage system nominal rated capacity read from CAN, EV FMS | `AVL ID 10903` |
| 289 | `can.ev.battery.temperature` | `number` | `celsius` | High voltage battery temperature read from CAN, EV FMS | `AVL ID 10893` |
| 290 | `can.ev.battery.voltage` | `number` | `volts` | High voltage battery voltage read from CAN, EV FMS | `AVL ID 10879` |
| 291 | `can.ev.cargo.weight` | `number` | `kg` | Cargo weight read from CAN, EV FMS | `AVL ID 10897` |
| 292 | `can.ev.dc.charging.state.enum` | `number` | — | DC charging state read from CAN, EV FMS | `AVL ID 10888` |
| 293 | `can.ev.evse1.ac.current` | `number` | `amperes` | EVSE1 AC RMS current read from CAN, EV FMS | `AVL ID 10886` |
| 294 | `can.ev.evse1.ac.voltage` | `number` | `volts` | EVSE1 AC RMS voltage read from CAN, EV FMS | `AVL ID 10887` |
| 295 | `can.ev.external.powersource.state.enum` | `number` | — | External energy source connection state read from CAN, EV FMS | `AVL ID 10884` |
| 296 | `can.ev.internal.charger.state.enum` | `number` | — | Internal charger state read from CAN, EV FMS | `AVL ID 10881` |
| 297 | `can.ev.powered.vehicle.weight` | `number` | `kg` | Powered vehicle weight read from CAN, EV FMS | `AVL ID 10898` |
| 298 | `can.ev.propulsion.motor.coolant.fan.temperature` | `number` | `celsius` | Propulsion motor coolant fan 1 control temperature read from CAN, EV FMS | `AVL ID 10891` |
| 299 | `can.ev.thermal.management.heater.state.enum` | `number` | — | High voltage energy storage system thermal management system heater state read from CAN, EV FMS | `AVL ID 10894` |
| 300 | `can.ev.trailer.weight` | `number` | `kg` | Trailer weight read from CAN, EV FMS | `AVL ID 10896` |
| 301 | `can.factory.armed.status` | `boolean` | — | Factory armed status, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 926` |
| 302 | `can.fap.indicator.status` | `boolean` | — | FAP indicator status from CAN bus | `AVL ID 519, , AVL ID 971` |
| 303 | `can.faulty.batteries` | `number` | — | Faulty batteries from CAN bus | `AVL ID 1161` |
| 304 | `can.feeder.reverse.status` | `boolean` | — | Feeder revers switched on status, read from CAN | `AVL ID 520` |
| 305 | `can.feeder.speed.status` | `boolean` | — | Feeder speed normal status, read from CAN: true - Ok, false - below normal | `AVL ID 520` |
| 306 | `can.front.differential.status` | `boolean` | — | Front differential locked status, read from CAN | `AVL ID 518, , AVL ID 947` |
| 307 | `can.front.fog.light.indicator.state` | `string` | — | Vehicle parameter for front fog light indicator read from CAN | `AVL ID 10428` |
| 308 | `can.front.fog.lights.status` | `boolean` | — | CAN front fog lights are on | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 932` |
| 309 | `can.front.hydraulic.status` | `boolean` | — | Front hydraulic turned on status. read from CAN | `AVL ID 520` |
| 310 | `can.front.left.door.status` | `boolean` | — | CAN front left door is opened | `AVL ID 132, , AVL ID 143, , AVL ID 47, , AVL ID 517, , AVL ID 654, , AVL ID 90` |
| 311 | `can.front.left.window.status` | `boolean` | — | CAN front left window is opened | `AVL ID 1211` |
| 312 | `can.front.passenger.seatbelt.status` | `boolean` | — | Fron passenger's seatbelt fastened status, read from CAN | `AVL ID 10632, , AVL ID 518, , AVL ID 941` |
| 313 | `can.front.passenger.status` | `boolean` | — | Front pasenger is present status, read from CAN | `AVL ID 518, , AVL ID 945` |
| 314 | `can.front.pto.status` | `boolean` | — | Front power take-off status turned on status, read from CAN | `AVL ID 520` |
| 315 | `can.front.right.door.status` | `boolean` | — | CAN front right door is opened | `AVL ID 132, , AVL ID 143, , AVL ID 47, , AVL ID 517, , AVL ID 655, , AVL ID 90` |
| 316 | `can.front.right.window.status` | `boolean` | — | CAN front right window is opened | `AVL ID 1212` |
| 317 | `can.front.three.point.hitch.status` | `boolean` | — | Front three-point hitch turned on status, read from CAN | `AVL ID 520` |
| 318 | `can.fuel.consumed` | `number` | `liters` | Fuel volume totally consumed by vehicle read from CAN | `AVL ID 1180, , AVL ID 33, , AVL ID 83, , AVL ID 86, , AVL ID 996` |
| 319 | `can.fuel.consumption` | `number` | `liters/h` | Engine fuel rate read from CAN | `AVL ID 135, , AVL ID 60` |
| 320 | `can.fuel.economy` | `number` | `km/liters` | CAN instantaneous fuel economy | `AVL ID 1036, , AVL ID 1187, , AVL ID 1345, , AVL ID 136` |
| 321 | `can.fuel.filter.plugged.indicator.status` | `boolean` | — | Fuel filter is plugged indicator from CAN bus | `AVL ID 519, , AVL ID 983` |
| 322 | `can.fuel.filter.pressure.indicator.state` | `string` | — | Vehicle parameter for fuel filter differential pressure indicator read from CAN | `AVL ID 10431` |
| 323 | `can.fuel.idle.consumed` | `number` | `liters` | Fuel volume totally consumed during idling state of the vehicle read from CAN | `AVL ID 1185` |
| 324 | `can.fuel.injection.timing` | `number` | `degrees` | Fuel injection timing read from CAN | `AVL ID 59` |
| 325 | `can.fuel.level` | `number` | `percentage` | Fuel level in tank read from CAN | `AVL ID 1066, , AVL ID 1070, , AVL ID 1183, , AVL ID 37, , AVL ID 48, , AVL ID 89` |
| 326 | `can.fuel.level.indicator.state` | `string` | — | Vehicle parameter for fuel level indicator read from CAN | `AVL ID 10428` |
| 327 | `can.fuel.level.low.indicator.status` | `boolean` | — | Low fuel level indicator status, read from CAN | `AVL ID 123, , AVL ID 38` |
| 328 | `can.fuel.low.indicator.status` | `boolean` | — | CAN low fuel indicator is on | `AVL ID 519, , AVL ID 968` |
| 329 | `can.fuel.pressure` | `number` | `kPa` | Fuel pressure read from CAN | `AVL ID 34` |
| 330 | `can.fuel.type.enum` | `number` | — | Fuel type read from CAN | `AVL ID 759` |
| 331 | `can.fuel.volume` | `number` | `liters` | CAN fuel volume | `AVL ID 34, , AVL ID 390, , AVL ID 84` |
| 332 | `can.full.charge.time` | `number` | `seconds` | Time to full charge from CAN bus | `AVL ID 1146` |
| 333 | `can.gas.fuel.consumed` | `number` | `kg` | Natural gas fuel amount totally consumed by vehicle read from CAN | `AVL ID 974` |
| 334 | `can.gear.current` | `number` | — | Current gear read from CAN (J1939 transmission actual gear) | `AVL ID 1332` |
| 335 | `can.gear.selected` | `number` | — | Selected gear read from CAN (J1939 transmission requested gear) | `AVL ID 1331` |
| 336 | `can.glow.plug.indicator.status` | `boolean` | — | Glow plug indicator status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 970` |
| 337 | `can.grain.auger.speed.status` | `boolean` | — | Grain auger speed normal status, read from CAN: true - Ok, false - below normal | `AVL ID 520` |
| 338 | `can.grain.header.connected.status` | `boolean` | — | Grain header connected status, read from CAN | `AVL ID 520` |
| 339 | `can.grain.release.status` | `boolean` | — | Grain release from hopper is turned on status, read from CAN | `AVL ID 520` |
| 340 | `can.grain.tank.70.percent.event` | `boolean` | — | Grain task is 70% full event, read from CAN | `AVL ID 520` |
| 341 | `can.grain.tank.full.event` | `boolean` | — | Grain tank is full event, read from CAN | `AVL ID 520` |
| 342 | `can.grain.tank.opened.status` | `boolean` | — | Grain task is opened status, read from CAN | `AVL ID 520` |
| 343 | `can.gross.combination.vehicle.weight` | `number` | `kg` | Gross combination vehicle weight read from CAN | `AVL ID 10899` |
| 344 | `can.handbrake.indicator.status` | `boolean` | — | Status of handbrake system indicator, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 961` |
| 345 | `can.handbrake.status` | `boolean` | — | CAN handbrake is pulled up | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 653` |
| 346 | `can.handlebar.lock.status` | `boolean` | — | Handlebar lock status from CAN bus | `AVL ID 1127` |
| 347 | `can.hatch.open.indicator.state` | `string` | — | Vehicle parameter for hatch open indicator read from CAN | `AVL ID 10428` |
| 348 | `can.hazard.warning.indicator.state` | `string` | — | Vehicle parameter for hazard warning indicator read from CAN | `AVL ID 10428` |
| 349 | `can.height.control.indicator.state` | `string` | — | Vehicle parameter for height control (levelling) indicator read from CAN | `AVL ID 10430` |
| 350 | `can.high.beam.indicator.state` | `string` | — | Vehicle parameter for high beam/main beam indicator read from CAN | `AVL ID 10428` |
| 351 | `can.high.beam.status` | `boolean` | — | CAN high beams are on | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 930` |
| 352 | `can.highest.battery2.temperature` | `number` | `celsius` | Highest battery 2 temperature from CAN bus | `AVL ID 1183` |
| 353 | `can.highest.battery2.voltage` | `number` | `volts` | Highest battery 2 voltage from CAN bus | `AVL ID 1185` |
| 354 | `can.highest.battery.code` | `string` | — | Highest battery ID code from CAN bus | `AVL ID 1137` |
| 355 | `can.highest.battery.temperature` | `number` | `celsius` | Highest battery temperature from CAN bus | `AVL ID 1142` |
| 356 | `can.highest.battery.temperature.code` | `string` | — | Highest temperature battery ID code from CAN bus | `AVL ID 1143` |
| 357 | `can.highest.battery.voltage` | `number` | `volts` | Highest battery voltage from CAN bus | `AVL ID 1136` |
| 358 | `can.highest.mismatch.code` | `string` | — | Highest mismatch ID code from CAN bus | `AVL ID 1139` |
| 359 | `can.highest.mismatch.voltage` | `number` | `volts` | Highest mismatch voltage from CAN bus | `AVL ID 1138` |
| 360 | `can.high.voltage.system.caution.indicator.state` | `string` | — | Vehicle parameter for high voltage system caution indicator read from CAN | `AVL ID 13259` |
| 361 | `can.hood.status` | `boolean` | — | CAN hood is opened | `AVL ID 132, , AVL ID 143, , AVL ID 47, , AVL ID 517, , AVL ID 90, , AVL ID 913` |
| 362 | `can.hybrid.battery.capacity` | `number` | `kWh` | OEM HV Battery Max Energy read from CAN | `AVL ID 1382` |
| 363 | `can.hybrid.battery.current` | `number` | `amperes` | OEM HV Battery Current read from CAN | `AVL ID 1380` |
| 364 | `can.hybrid.battery.max.cell.voltage` | `number` | `volts` | OEM HV Battery Max Cell Voltage read from CAN | `AVL ID 1379` |
| 365 | `can.hybrid.battery.max.temperature` | `number` | `celsius` | OEM HV Battery Max Cell Temperature read from CAN | `AVL ID 1387` |
| 366 | `can.hybrid.battery.measured.capacity` | `number` | `kWh` | OEM HV Battery Measured Energy read from CAN | `AVL ID 1383` |
| 367 | `can.hybrid.battery.min.cell.voltage` | `number` | `volts` | OEM HV Battery Min Cell Voltage read from CAN | `AVL ID 1378` |
| 368 | `can.hybrid.battery.min.temperature` | `number` | `celsius` | OEM HV Battery Min Cell Temperature read from CAN | `AVL ID 1386` |
| 369 | `can.hybrid.battery.pack.life` | `number` | `percentage` | Hybrid battery pack remaining life | `AVL ID 57` |
| 370 | `can.hybrid.battery.voltage` | `number` | `volts` | OEM HV Battery High Voltage read from CAN | `AVL ID 1381` |
| 371 | `can.hybrid.onboard.current` | `number` | `amperes` | Hybrid vehicle system current | `AVL ID 544` |
| 372 | `can.hybrid.onboard.power.voltage` | `number` | `volts` | Hybrid vehicle system voltage | `AVL ID 543` |
| 373 | `can.hydraulics.chamber.oil.overflow.indicator.status` | `boolean` | — | Oil overflow in hydraulic chamber indicator from CAN bus | `AVL ID 519, , AVL ID 981` |
| 374 | `can.hydraulics.high.temperature.status` | `boolean` | — | High temperature of drive system hydraulics (>86 degrees), reaed from CAN | `AVL ID 519, , AVL ID 520, , AVL ID 980` |
| 375 | `can.hydraulics.low.temperature.status` | `boolean` | — | Low temperature of drive system hydraulics (<5 degrees), read from CAN | `AVL ID 520` |
| 376 | `can.hydraulics.oil.filter.plugged.indicator.status` | `boolean` | — | Hydraulic system oil filter plugged indicator from CAN bus | `AVL ID 519, , AVL ID 977` |
| 377 | `can.hydraulics.oil.level.low.indicator.status` | `boolean` | — | Hydraulic oil low level indicator from CAN bus | `AVL ID 519, , AVL ID 979` |
| 378 | `can.hydraulics.pressure.low.status` | `boolean` | — | Hydraulic system low pressure indicator from CAN bus | `AVL ID 519, , AVL ID 978` |
| 379 | `can.ignition.key.status` | `boolean` | — | The key is in ignition lock status, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 652` |
| 380 | `can.intake.air.pressure` | `number` | `kPa` | Absolute air pressure at input port to intake manifold or air box | `AVL ID 1048` |
| 381 | `can.intake.air.temperature` | `number` | `celsius` | Intake air temperature | `AVL ID 39` |
| 382 | `can.intake.map` | `number` | `kPa` | Intake manifold absolute pressure | `AVL ID 35, , AVL ID 542` |
| 383 | `can.interlock.active` | `boolean` | — | Interlock active status, read from CAN | `AVL ID 517, , AVL ID 906` |
| 384 | `can.kneeling.indicator.state` | `string` | — | Vehicle parameter for kneeling indicator read from CAN | `AVL ID 10430` |
| 385 | `can.lane.departure.indication.indicator.state` | `string` | — | Vehicle parameter for lane departure indication read from CAN | `AVL ID 10431` |
| 386 | `can.lane.departure.warning.off.indicator.state` | `string` | — | Vehicle parameter for lane departure warning switched off indicator read from CAN | `AVL ID 10431` |
| 387 | `can.left.joystick.back.event` | `boolean` | — | Left joystick moved back active, read from CAN | `AVL ID 520` |
| 388 | `can.left.joystick.forward.event` | `boolean` | — | Left joystick moved forward active, read from CAN | `AVL ID 520` |
| 389 | `can.left.joystick.left.event` | `boolean` | — | Left joystick moved left active, read from CAN | `AVL ID 520` |
| 390 | `can.left.joystick.right.event` | `boolean` | — | Left joystick moved right active, read from CAN | `AVL ID 520` |
| 391 | `can.lights.failure.indicator.status` | `boolean` | — | Lights failure indicator status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 965` |
| 392 | `can.lights.hazard.lights.status` | `boolean` | — | CAN lights info hazard lights status | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 912` |
| 393 | `can.light.signal.status` | `boolean` | — | Light signal turned on status, read from CAN | `AVL ID 518, , AVL ID 935` |
| 394 | `can.low.beam.indicator.state` | `string` | — | Vehicle parameter for low beam/dipped beam indicator read from CAN | `AVL ID 10428` |
| 395 | `can.low.beam.status` | `boolean` | — | CAN low beams are on | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 929` |
| 396 | `can.lowering.indicator.state` | `string` | — | Vehicle parameter for lowering indicator read from CAN | `AVL ID 10430` |
| 397 | `can.lowest.battery2.temperature` | `number` | `celsius` | Lowest battery 2 voltage from CAN bus | `AVL ID 1182` |
| 398 | `can.lowest.battery2.voltage` | `number` | `volts` | Lowest battery 2 voltage from CAN bus | `AVL ID 1184` |
| 399 | `can.lowest.battery.code` | `string` | — | Lowest battery ID code from CAN bus | `AVL ID 1135` |
| 400 | `can.lowest.battery.temperature` | `number` | `celsius` | Lowest battery temperature from CAN bus | `AVL ID 1140` |
| 401 | `can.lowest.battery.temperature.code` | `string` | — | Lowest temperature battery ID code from CAN bus | `AVL ID 1141` |
| 402 | `can.lowest.battery.voltage` | `number` | `volts` | Lowest Battery Voltage from CAN bus | `AVL ID 1134` |
| 403 | `can.lpg.fuel.status` | `boolean` | — | Engine working on LPG fuel status, read from CAN bus | `AVL ID 1084` |
| 404 | `can.maf.air.flow.rate` | `number` | `g/sec` | MAF air flow rate read from CAN | `AVL ID 40` |
| 405 | `can.maintenance.required.status` | `boolean` | — | Maintenance required status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 969` |
| 406 | `can.major.version` | `string` | — | Major version from CAN bus in hex form | `AVL ID 1156` |
| 407 | `can.malfunction.general.failure.indicator.state` | `string` | — | Vehicle parameter for malfunction/general failure indicator read from CAN | `AVL ID 10429` |
| 408 | `can.manual.retarder.status` | `boolean` | — | Manual retarder status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 939` |
| 409 | `can.max.available.power` | `number` | `W` | Maximum available power from CAN bus | `AVL ID 1126` |
| 410 | `can.max.charge.current` | `number` | `amperes` | Max charge current from CAN bus | `AVL ID 1181` |
| 411 | `can.max.discharge.current` | `number` | `amperes` | Max discharge current from CAN bus | `AVL ID 1149` |
| 412 | `can.mil.mileage` | `number` | `km` | Distance traveled while malfunction indicator lamp is activated, read from CAN | `AVL ID 43` |
| 413 | `can.mil.status` | `boolean` | — | Malfunction indicator lamp status read from CAN | `AVL ID 10349, , AVL ID 519, , AVL ID 953` |
| 414 | `can.mil.time` | `number` | `hours` | Time run with malfunction indicator lamp activated, read from CAN | `AVL ID 54` |
| 415 | `can.minor.version` | `string` | — | Minor version from CAN bus in hex form | `AVL ID 1157` |
| 416 | `can.module.id` | `number` | — | CAN module ID | `AVL ID 101, , AVL ID 13` |
| 417 | `can.module.id.hex` | `string` | — | CAN module ID in HEX format | `AVL ID 388, , AVL ID 529` |
| 418 | `can.module.sleep.mode` | `boolean` | — | CAN module goes to the sleep mode | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 924` |
| 419 | `can.motor.failures.indicator.state` | `string` | — | Vehicle parameter for electric motor failures indicator read from CAN | `AVL ID 13259` |
| 420 | `can.motor.limited.performance.indicator.state` | `string` | — | Vehicle parameter for limited performance electric motor indicator read from CAN | `AVL ID 13259` |
| 421 | `can.motor.status` | `boolean` | — | Electric motor status | `AVL ID 517, , AVL ID 916` |
| 422 | `can.mowing.status` | `boolean` | — | Mowing is active status, read from CAN bus | `AVL ID 520` |
| 423 | `can.multiplex.system.indicator.state` | `string` | — | Vehicle parameter for multiplex system indicator read from CAN bus | `AVL ID 13259` |
| 424 | `can.neutral.gear.status` | `boolean` | — | CAN neutral gear is on | `AVL ID 517, , AVL ID 659` |
| 425 | `can.oil.level.low.indicator.status` | `boolean` | — | Oil level low indicator status read from CAN bus | `AVL ID 235, , AVL ID 519, , AVL ID 958` |
| 426 | `can.oil.pressure.indicator.status` | `boolean` | — | Oil pressure indicator status read from CAN bus | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 974` |
| 427 | `can.oil.service.mileage` | `number` | `km` | Distance to next oil service | `AVL ID 864` |
| 428 | `can.oil.service.time` | `number` | `days` | Time to next oil service | `AVL ID 865` |
| 429 | `can.operator.present.status` | `boolean` | — | Operator is present status, read from CAN bus | `AVL ID 517, , AVL ID 905` |
| 430 | `can.park.heating.indicator.state` | `string` | — | Vehicle parameter for park heating indicator read from CAN | `AVL ID 10429` |
| 431 | `can.parking.brake.indicator.state` | `string` | — | Vehicle parameter for parking brake indicator read from CAN | `AVL ID 10428` |
| 432 | `can.parking.brake.status` | `boolean` | — | Parking break status from CAN | `AVL ID 1179` |
| 433 | `can.parking.lights.status` | `boolean` | — | Parking light status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 928` |
| 434 | `can.parking.status` | `boolean` | — | Parking is activated for automatic gearbox, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 660` |
| 435 | `can.part.charge.capacity` | `number` | `Ah` | Part charge capacity | `AVL ID 1153` |
| 436 | `can.passenger.seatbelt.indicator.status` | `boolean` | — | Passenger seatbelt indicator status read from CAN | `AVL ID 123, , AVL ID 38` |
| 437 | `can.patch.version` | `string` | — | Patch version from CAN bus in hex form | `AVL ID 1158` |
| 438 | `can.pedal.brake.status` | `boolean` | — | Footbrake pedal is depressed, read from CAN | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 79, , AVL ID 816, , AVL ID 910` |
| 439 | `can.pedal.clutch.status` | `boolean` | — | CAN clutch pedal pressed | `AVL ID 517, , AVL ID 82, , AVL ID 911` |
| 440 | `can.position.lights.indicator.state` | `string` | — | Vehicle parameter for position lights/side lights indicator read from CAN | `AVL ID 10428` |
| 441 | `can.powersource.takeoff.enum` | `number` | — | CAN power takeoff bitmask | `AVL ID 83` |
| 442 | `can.pram.request.indicator.state` | `string` | — | Vehicle parameter for pram request indicator read from CAN | `AVL ID 10430` |
| 443 | `can.pressure.filter.cloged.status` | `boolean` | — | Pressure filter of the hydraulic pump is clogged, read from CAN | `AVL ID 520` |
| 444 | `can.private.status` | `boolean` | — | Vehicle works in private mode, read from CAN bus | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 904` |
| 445 | `can.program.id` | `number` | — | CAN program number | `AVL ID 100, , AVL ID 12` |
| 446 | `can.pto.status` | `boolean` | — | Power take-off status, read from CAN | `AVL ID 518, , AVL ID 946` |
| 447 | `can.pumping.torque` | `number` | `percentage` | Estimated pumping - percent torque | `AVL ID 944` |
| 448 | `can.raising.indicator.state` | `string` | — | Vehicle parameter for raising indicator read from CAN | `AVL ID 10430` |
| 449 | `can.ready.to.drive.indicator.status` | `boolean` | — | Ready to drive indicator status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 517, , AVL ID 902` |
| 450 | `can.rear.brake.status` | `boolean` | — | Rear brake status from CAN bus | `AVL ID 1128` |
| 451 | `can.rear.central.seatbelt.status` | `boolean` | — | Rear central seatbelt fastened status, read from CAN | `AVL ID 518, , AVL ID 944` |
| 452 | `can.rear.differential.status` | `boolean` | — | Rear differential locked status, read from CAN | `AVL ID 518, , AVL ID 948` |
| 453 | `can.rear.fog.light.indicator.state` | `string` | — | Vehicle parameter for rear fog light indicator read from CAN | `AVL ID 10429` |
| 454 | `can.rear.fog.lights.status` | `boolean` | — | CAN rear fog lights are on | `AVL ID 123, , AVL ID 38, , AVL ID 518, , AVL ID 931` |
| 455 | `can.rear.hydraulic.status` | `boolean` | — | Read hydraulic turned on status, read from CAN | `AVL ID 520` |
| 456 | `can.rear.left.door.status` | `boolean` | — | CAN rear left door is opened | `AVL ID 132, , AVL ID 143, , AVL ID 47, , AVL ID 517, , AVL ID 656, , AVL ID 90` |
| 457 | `can.rear.left.seatbelt.status` | `boolean` | — | Rear left seatbelt fastened status, read from CAN | `AVL ID 518, , AVL ID 942` |
| 458 | `can.rear.left.window.status` | `boolean` | — | CAN rear left window is opened | `AVL ID 1213` |
| 459 | `can.rearm.signal.event` | `boolean` | — | Rearm signal was sent | `AVL ID 517, , AVL ID 922` |
| 460 | `can.rear.pto.status` | `boolean` | — | Rear power take-off status turned on status, read from CAN | `AVL ID 520` |
| 461 | `can.rear.right.door.status` | `boolean` | — | CAN rear right door is opened | `AVL ID 132, , AVL ID 143, , AVL ID 47, , AVL ID 517, , AVL ID 657, , AVL ID 90` |
| 462 | `can.rear.right.seatbelt.status` | `boolean` | — | Rear right seatbelt fastened status, read from CAN | `AVL ID 518, , AVL ID 943` |
| 463 | `can.rear.right.window.status` | `boolean` | — | CAN rear right window is opened | `AVL ID 1214` |
| 464 | `can.rear.three.point.hitch.status` | `boolean` | — | Rear three-point hitch turned on status, read from CAN | `AVL ID 520` |
| 465 | `can.recognized.batteries` | `number` | — | Recognized batteries from CAN bus | `AVL ID 1159` |
| 466 | `can.recuperation.status` | `boolean` | — | Recuperation status from CAN bus | `AVL ID 1150` |
| 467 | `can.relative.fuel.rail.pressure` | `number` | `kPa` | Fuel rail pressure relative to manifold vacuum | `AVL ID 44` |
| 468 | `can.remote.accelerator.pedal.position` | `number` | `percentage` | The ratio of actual position of the remote analog engine speed/torque request input device (such as an accelerator pedal or throttle lever) to the maximum position of the input device | `AVL ID 937` |
| 469 | `can.request.engine.lock.event` | `boolean` | — | Request to lock the engine (activation after attempt to restart the engine) event | `AVL ID 517, , AVL ID 908` |
| 470 | `can.retarder.indicator.state` | `string` | — | Vehicle parameter for retarder indicator read from CAN | `AVL ID 10430` |
| 471 | `can.retarder.torque.load` | `number` | `percentage` | Retarder torque load percentage read from CAN | `AVL ID 188, , AVL ID 522` |
| 472 | `can.reverse.gear.status` | `boolean` | — | CAN reverse gear is on | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 661` |
| 473 | `can.right.joystick.back.event` | `boolean` | — | Right joystick moved back active, read from CAN | `AVL ID 520` |
| 474 | `can.right.joystick.forward.event` | `boolean` | — | Right joystick moved forward active, read from CAN | `AVL ID 520` |
| 475 | `can.right.joystick.left.event` | `boolean` | — | Right joystick moved left active, read from CAN | `AVL ID 520` |
| 476 | `can.right.joystick.right.event` | `boolean` | — | Right joystick moved right active, read from CAN | `AVL ID 520` |
| 477 | `can.road.speed.limit.state` | `number` | — | Road speed limit status | `AVL ID 932` |
| 478 | `can.roof.opened.status` | `boolean` | — | Roof is opened status, read from CAN | `AVL ID 517, , AVL ID 909` |
| 479 | `can.scr.thermal.management.state` | `number` | — | SCR thermal management active | `AVL ID 942` |
| 480 | `can.seat.belt.indicator.state` | `string` | — | Vehicle parameter for seat belt indicator read from CAN | `AVL ID 10431` |
| 481 | `can.seatbelt.status` | `boolean` | — | Seatbelt status read from CAN, false - the belt is not buckled, true - the belt is buckled | `AVL ID 10885` |
| 482 | `can.service.last.mileage` | `number` | `km` | Distance from last service | `AVL ID 860` |
| 483 | `can.service.last.time` | `number` | `days` | Time from last serivce | `AVL ID 863` |
| 484 | `can.service.maintenance.indicator.state` | `string` | — | Vehicle parameter for service/call for maintenance indicator read from CAN | `AVL ID 10429` |
| 485 | `can.service.mileage` | `number` | `km` | Service distance read from CAN | `AVL ID 113, , AVL ID 400, , AVL ID 402` |
| 486 | `can.service.required.mileage` | `number` | `km` | Distance from need of service | `AVL ID 859` |
| 487 | `can.service.required.time` | `number` | `days` | Time from need of service | `AVL ID 862` |
| 488 | `can.service.time` | `number` | `days` | Time to next service | `AVL ID 861` |
| 489 | `can.short.fuel.trim` | `number` | `percentage` | Short term fuel trim read from CAN | `AVL ID 33` |
| 490 | `can.sn.high` | `string` | — | SN High from CAN bus | `AVL ID 1132` |
| 491 | `can.sn.low` | `string` | — | SN Low from CAN bus | `AVL ID 1133` |
| 492 | `can.soc.switch.level` | `number` | `percentage` | SoC switch level from CAN bus | `AVL ID 1152` |
| 493 | `can.soot.filter.indicator.status` | `boolean` | — | DPF/FAP soot filter indicator status, read from CAN | `AVL ID 123, , AVL ID 38` |
| 494 | `can.spreader.working.hours` | `number` | `hours` | Salt spreader working hours read from CAN | `AVL ID 185, , AVL ID 519` |
| 495 | `can.standalone.engine` | `boolean` | — | Standalone engine status read from CAN | `AVL ID 517, , AVL ID 901` |
| 496 | `can.start.stop.inactive.status` | `boolean` | — | Start-stop system inactive status read from CAN bus | `AVL ID 1086` |
| 497 | `can.steering.failure.indicator.state` | `string` | — | Vehicle parameter for steering failure indicator read from CAN | `AVL ID 10430` |
| 498 | `can.steering.fluid.level.indicator.state` | `string` | — | Vehicle parameter for steering fluid level indicator read from CAN | `AVL ID 10429` |
| 499 | `can.stop.indicator.status` | `boolean` | — | STOP indicator status read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 957` |
| 500 | `can.stop.request.indicator.state` | `string` | — | Vehicle parameter for stop request indicator read from CAN | `AVL ID 10430` |
| 501 | `can.straw.chopper.speed.status` | `boolean` | — | Straw chopper speed normal status, read from CAN: true - Ok, false - below normal | `AVL ID 520` |
| 502 | `can.straw.chopper.status` | `boolean` | — | Straw chopper switched on status, read from CAN | `AVL ID 520` |
| 503 | `can.straw.shaker.speed.status` | `boolean` | — | Straw shaler speed normal status, read from CAN: true - Ok, false - below normal | `AVL ID 520` |
| 504 | `can.straw.walker.clogged.status` | `boolean` | — | Straw walker is clogged status, read from CAN | `AVL ID 520` |
| 505 | `can.switch.process.status` | `boolean` | — | Switch process status from CAN bus | `AVL ID 1151` |
| 506 | `can.tachograph.indication.indicator.state` | `string` | — | Vehicle parameter for tachograph indication read from CAN | `AVL ID 10431` |
| 507 | `can.threshing.drum.control.status` | `boolean` | — | Threshing drum status: true - on, false - off, read from CAN | `AVL ID 520` |
| 508 | `can.threshing.drum.excessive.clearance.status` | `boolean` | — | Excessive clearance under the threshing drum, read from CAN | `AVL ID 520` |
| 509 | `can.threshing.status` | `boolean` | — | Threshing is active status, read from CAN | `AVL ID 520` |
| 510 | `can.throttle.pedal.level` | `number` | `percentage` | Throttle pedal push level read from CAN | `AVL ID 1196, , AVL ID 31, , AVL ID 41, , AVL ID 540, , AVL ID 815, , AVL ID 82, , AVL ID 84` |
| 511 | `can.time.since.codes.cleared` | `number` | `minutes` | Time since trouble codes cleared | `AVL ID 55` |
| 512 | `can.timing.advance` | `number` | `degrees` | Ignition timing advance read from CAN | `AVL ID 38` |
| 513 | `can.tire.failure.indicator.state` | `string` | — | Vehicle parameter for tire failure/malfunction indicator read from CAN | `AVL ID 10429` |
| 514 | `can.tire.pressure` | `number` | `kPa` | Aggregate vehicle tire pressure, read from CAN | `AVL ID 13160` |
| 515 | `can.tire.pressure.low.status` | `boolean` | — | Tire pressure low status, read from CAN | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 966` |
| 516 | `can.torque.current` | `number` | `amperes` | Torque current from CAN bus | `AVL ID 1131` |
| 517 | `can.total.cruise.control.time` | `number` | `hours` | Total driving time when cruise control is ON, read from CAN | `AVL ID 189, , AVL ID 523` |
| 518 | `can.total.engine.idle.time` | `number` | `hours` | Time of engine running in idling status (vehicle stopped) since vehicle manufacture, read from CAN | `AVL ID 1181` |
| 519 | `can.tracker.counted.fuel.consumed` | `number` | `liters` | Vehicle counted fuel consumed based on CAN-bus data | `AVL ID 107, , AVL ID 17` |
| 520 | `can.tracker.counted.mileage` | `number` | `km` | CAN-bus mileage counted by tracker after plug in | `AVL ID 105, , AVL ID 16` |
| 521 | `can.trailer.axle.lift.status` | `boolean` | — | Trailer axle lift status, read from CAN | `AVL ID 518, , AVL ID 951, , AVL ID 952` |
| 522 | `can.trailer.brake.high.temperature.indicator.status` | `boolean` | — | High trailer brake temperature indicator from CAN bus | `AVL ID 519, , AVL ID 990` |
| 523 | `can.trailer.connected.indicator.state` | `string` | — | Vehicle parameter for trailer connected indicator read from CAN | `AVL ID 10431` |
| 524 | `can.trailer.connected.status` | `boolean` | — | Trailer connected status read from CAN bus | `AVL ID 1085` |
| 525 | `can.trailer.pneumatic.supply.incorrect.indicator.status` | `boolean` | — | Incorrect trailer pneumatic supply indicator from CAN bus | `AVL ID 519, , AVL ID 991` |
| 526 | `can.trailer.tire.pressure.low.status` | `boolean` | — | Low trailer tire pressure indicator from CAN bus | `AVL ID 519, , AVL ID 988` |
| 527 | `can.trailer.vin` | `string` | — | Trailer VIN number, read from CAN | `AVL ID 13671` |
| 528 | `can.trailer.wear.brake.lining.indicator.status` | `boolean` | — | Wear of trailer brake lining indicator from CAN bus | `AVL ID 519, , AVL ID 989` |
| 529 | `can.transmission.failure.indicator.state` | `string` | — | Vehicle parameter for transmission failure/malfunction indicator read from CAN | `AVL ID 10429` |
| 530 | `can.transmission.fluid.temperature.indicator.state` | `string` | — | Vehicle parameter for transmission fluid temperature indicator read from CAN | `AVL ID 10429` |
| 531 | `can.transmission.oil.temperature` | `number` | `celsius` | Transmission oil temperature reaed from CAN | `AVL ID 1199` |
| 532 | `can.trip.fuel.consumed` | `number` | `liters` | Volume of liquid fuel consumed during the trip, read from CAN | `AVL ID 1192` |
| 533 | `can.trip.vehicle.mileage` | `number` | `km` | Distance travelled during all or part of a journey | `AVL ID 1186, , AVL ID 989` |
| 534 | `can.trunk.opening.remote.event` | `boolean` | — | Trunk was opened with remote control event, read from CAN | `AVL ID 517, , AVL ID 923` |
| 535 | `can.trunk.status` | `boolean` | — | CAN trunk is opened | `AVL ID 132, , AVL ID 143, , AVL ID 47, , AVL ID 517, , AVL ID 658, , AVL ID 90` |
| 536 | `can.turn.signals.indicator.state` | `string` | — | Vehicle parameter for turn signals indicator read from CAN | `AVL ID 10428` |
| 537 | `can.unloader.drive.status` | `boolean` | — | Unloader drive is on unloading tube pivot is in idle position, read from CAN | `AVL ID 520` |
| 538 | `can.vehicle.battery.charging.status` | `boolean` | — | Vehicle battery charging status get from CAN Bus | `AVL ID 132, , AVL ID 410, , AVL ID 47, , AVL ID 517, , AVL ID 915` |
| 539 | `can.vehicle.battery.current` | `number` | `amperes` | Vehicle battery current, read from CAN | `AVL ID 1113` |
| 540 | `can.vehicle.battery.energy.consumed` | `number` | `kWh` | Energy consumed from the vehicle battery read from CAN | `AVL ID 1155, , AVL ID 1388` |
| 541 | `can.vehicle.battery.energy.recuperated` | `number` | `kWh` | Recuperated energy into the vehicle battery read from CAN | `AVL ID 1156` |
| 542 | `can.vehicle.battery.health` | `number` | `percentage` | Battery State of Health | `AVL ID 10904, , AVL ID 1151` |
| 543 | `can.vehicle.battery.level` | `number` | `percentage` | CAN-bus reported vehicle battery level for EV or HEV | `AVL ID 152, , AVL ID 411` |
| 544 | `can.vehicle.battery.power` | `number` | `kW` | Vehicle battery power read from CAN | `AVL ID 1157` |
| 545 | `can.vehicle.battery.power.consumption` | `number` | `kWh/100km` | Vehicle battery power consumption read from CAN | `AVL ID 412` |
| 546 | `can.vehicle.battery.range` | `number` | `km` | Vehicle Range on Battery, read from CAN | `AVL ID 304, , AVL ID 526` |
| 547 | `can.vehicle.battery.remaining.range` | `number` | `km` | Vehicle battery remaining range, read from CAN | `AVL ID 10895` |
| 548 | `can.vehicle.battery.temperature` | `number` | `celsius` | Battery pack temperature, read from CAN | `AVL ID 1152` |
| 549 | `can.vehicle.battery.total.charge.energy` | `number` | `kWh` | Vehicle battery charged total energy, read from CAN | `AVL ID 1389` |
| 550 | `can.vehicle.battery.voltage` | `number` | `volts` | Vehicle battery voltage, read from CAN | `AVL ID 1112` |
| 551 | `can.vehicle.mileage` | `number` | `km` | Total vehicle mileage read from CAN | `AVL ID 105, , AVL ID 1176, , AVL ID 36, , AVL ID 389, , AVL ID 87, , AVL ID 990` |
| 552 | `can.vehicle.motorhours` | `number` | `hours` | Accumulated time of operation of vehicle | `AVL ID 993` |
| 553 | `can.vehicle.remaining.range` | `number` | `km` | Vehicle Range read, from CAN | `AVL ID 305, , AVL ID 755, , AVL ID 866` |
| 554 | `can.vehicle.speed` | `number` | `km/h` | Vehicle speed read from CAN | `AVL ID 30, , AVL ID 37, , AVL ID 81, , AVL ID 835` |
| 555 | `can.warning.indicator.status` | `boolean` | — | Warning indicator status, read from CAN bus | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 964` |
| 556 | `can.washer.fluid.level.low.indicator.status` | `boolean` | — | Low washer fluid level indicator, read from CAN bus | `AVL ID 519, , AVL ID 986` |
| 557 | `can.water.in.fuel.indicator.status` | `boolean` | — | Water in fuel indicator from CAN bus | `AVL ID 519, , AVL ID 984` |
| 558 | `can.wear.brake.pads.indicator.status` | `boolean` | — | Wear brake pads indicator status, read from CAN bus | `AVL ID 123, , AVL ID 38, , AVL ID 519, , AVL ID 967` |
| 559 | `can.webasto.status` | `boolean` | — | Webasto status read from CAN bus | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 899` |
| 560 | `can.wheel.speed` | `number` | `km/h` | Vehicle wheel based speed, read from CAN bus | `AVL ID 1019, , AVL ID 80` |
| 561 | `can.windscreen.washer.fluid.indicator.state` | `string` | — | Vehicle parameter for windscreen/windshield washer fluid indicator read from CAN bus | `AVL ID 10429` |
| 562 | `can.worn.brake.linings.indicator.state` | `string` | — | Vehicle parameter for worn brake linings indicator read from CAN bus | `AVL ID 10429` |
| 563 | `car.remote.control.state` | `number` | — | State of the vehicle's factory remote control action | `AVL ID 132, , AVL ID 47` |
| 564 | `central.standup.status` | `boolean` | — | Central stuandup up status: true - up, false - down | `AVL ID 845` |
| 565 | `charger.bms.timeout.status` | `boolean` | — | Charger BMS COM timeout: true - not expired, false - expired | `AVL ID 807` |
| 566 | `charger.control.mode` | `number` | — | Charger control mode currently in use | `AVL ID 806` |
| 567 | `charger.crc.violation.status` | `boolean` | — | Charger CRC violation: true - violation happened, false - no violation | `AVL ID 808` |
| 568 | `charger.current` | `number` | `amperes` | Charger actual current | `AVL ID 814` |
| 569 | `charger.energy` | `number` | `Wh` | Charger actual energy | `AVL ID 813` |
| 570 | `charger.fault.status` | `boolean` | — | Charger internal fault status: true - no internal fault happened, false - internal fault happened | `AVL ID 812` |
| 571 | `charger.mc.violation.status` | `boolean` | — | Charger MC violation: true - violation happened, false - no violation | `AVL ID 809` |
| 572 | `charger.mode` | `boolean` | — | Selected charge mode, read from CAN: 0 - default, 1 - fast | `AVL ID 802` |
| 573 | `charger.mode.state` | `number` | — | Charger mode state | `AVL ID 803` |
| 574 | `charger.plug.status` | `boolean` | — | Charger plug status | `AVL ID 817` |
| 575 | `charger.setpoint.current` | `number` | `amperes` | Charger current setpoint | `AVL ID 805` |
| 576 | `charger.setpoint.voltage` | `number` | `volts` | Charger svoltage setpoint | `AVL ID 804` |
| 577 | `charger.state` | `number` | — | Charger state | `AVL ID 810` |
| 578 | `charger.voltage` | `number` | `volts` | Charger actual voltage | `AVL ID 811` |
| 579 | `charge.time.remining` | `number` | `minutes` | Remaining charge time | `AVL ID 827` |
| 580 | `control.module.voltage` | `number` | `volts` | Supply voltage of the central control (system driving voltage) | `AVL ID 366` |
| 581 | `counter.impulses` | `number` | — | Impulses counter | `AVL ID 10912, , AVL ID 10915, , AVL ID 4, , AVL ID 4...5, , AVL ID 483, , AVL ID 5, , AVL ID 76` |
| 582 | `counter.impulses.frequency` | `number` | `hz` | Impulses counter frequency | `AVL ID 10640, , AVL ID 10642, , AVL ID 10913, , AVL ID 10916, , AVL ID 622, , AVL ID 623` |
| 583 | `counter.impulses.rpm` | `number` | `rpm` | Impulses counter RPM | `AVL ID 10641, , AVL ID 10643, , AVL ID 10914, , AVL ID 10917` |
| 584 | `crash.accelerometer.status` | `boolean` | — | Crash accelerometer is calibrated | `AVL ID 1430` |
| 585 | `crash.direction.enum` | `number` | — | Crash direction - front, rear, left, right etc. | `AVL ID 1430` |
| 586 | `crash.duration` | `number` | `seconds` | Crash duration | `AVL ID 1431` |
| 587 | `crash.event` | `boolean` | — | Crash event detected | `AVL ID 247` |
| 588 | `crash.event.enum` | `number` | — | Crash report reason code | `AVL ID 247` |
| 589 | `crash.events.number` | `number` | — | Crash event counter | `AVL ID 317` |
| 590 | `crash.impact.acceleration` | `number` | `g` | Crash impact acceleration | `AVL ID 1429` |
| 591 | `crash.max.acceleration` | `number` | `g` | Maximum acceleration (x or y) during crash | `AVL ID 1432` |
| 592 | `deadman.alarm.status` | `boolean` | — | Man down is active and no movement for configured timeout | `AVL ID 315` |
| 593 | `dead.reckoning.calibration.state` | `string` | — | Dead Reckoning Calibration Status | `AVL ID 1433` |
| 594 | `dead.reckoning.calibration.state.enum` | `number` | — | Dead Reckoning Calibration Status value | `AVL ID 1433` |
| 595 | `dead.reckoning.straight.alignment` | `number` | — | Dead Reckoning straight alignment progress, percent | `AVL ID 1435` |
| 596 | `dead.reckoning.turning.alignment` | `number` | — | Dead Reckoning turning alignment progress, percent | `AVL ID 1434` |
| 597 | `device.configuration.id` | `number` | — | Configuration profile index | `AVL ID 22` |
| 598 | `device.imei` | `string` | — | IMEI of the device | `AVL ID 1161` |
| 599 | `device.mounting.state` | `string` | — | Device mounting state | `AVL ID 1452` |
| 600 | `device.mounting.state.enum` | `number` | — | Device mounting state numeric code | `AVL ID 1452` |
| 601 | `device.serial.number` | `string` | — | Device serial number | `AVL ID 339` |
| 602 | `device.temperature` | `number` | `celsius` | Temperature of device | `AVL ID 362` |
| 603 | `device.uptime.records.count` | `number` | — | Number of records saved by the device since last power on | `AVL ID 108` |
| 604 | `din` | `number` | — | Digital inputs bitmask | `AVL ID 1, , AVL ID 1...2, , AVL ID 1...4, , AVL ID 14200, , AVL ID 2, , AVL ID 2...3, , AVL ID 262, , AVL ID 3, , AVL ID 4, , Command type 0x06` |
| 605 | `distance.since.refuel` | `number` | `km` | Calculated distance covered after the latest refueling | `AVL ID 1443` |
| 606 | `door.open.status` | `boolean` | — | Door open status | `AVL ID 143, , AVL ID 90` |
| 607 | `dout` | `number` | — | Digital outputs bitmask | `AVL ID 10001, , AVL ID 179, , AVL ID 180, , AVL ID 380, , AVL ID 50, , AVL ID 51` |
| 608 | `dout.overcurrent.status` | `boolean` | — | Overcurrent status for digital output | `AVL ID 841, , AVL ID 842, , AVL ID 843` |
| 609 | `driver.first.name` | `string` | — | Driver first name | `AVL ID 10518, , AVL ID 10520` |
| 610 | `driver.last.name` | `string` | — | Drvier lsat name | `AVL ID 10519, , AVL ID 10521` |
| 611 | `driver.name` | `string` | — | Driver name | `AVL ID 10518, , AVL ID 10519, , AVL ID 10520, , AVL ID 10521` |
| 612 | `driver.status.enum` | `number` | — | Driver status | `AVL ID 409` |
| 613 | `driving.state` | `number` | — | Vehicle current driving direction state | `AVL ID 830` |
| 614 | `dsm.distraction.event` | `boolean` | — | Driver distraction event generated by Driver status monitoring system (DSM) | `AVL ID 11701` |
| 615 | `dsm.driver.mask.event` | `boolean` | — | Driver wearing mask event generated by Driver status monitoring system (DSM) | `AVL ID 11706` |
| 616 | `dsm.driver.missing.event` | `boolean` | — | Driver missing event generated by Driver status monitoring system (DSM) | `AVL ID 11705` |
| 617 | `dsm.driver.phone.event` | `boolean` | — | Driver using the phone event generated by Driver status monitoring system (DSM) | `AVL ID 11703` |
| 618 | `dsm.fatigue.event` | `boolean` | — | Driver fatigue event generated by Driver status monitoring system (DSM) | `AVL ID 11700` |
| 619 | `dsm.seatbelt.event` | `boolean` | — | Driver seatbelt event generated by Driver status monitoring system (DSM) | `AVL ID 11713` |
| 620 | `dsm.smoking.event` | `boolean` | — | Driver smoking event generated by Driver status monitoring system (DSM) | `AVL ID 11704` |
| 621 | `dsm.yawning.event` | `boolean` | — | Driver yawning event generated by Driver status monitoring system (DSM) | `AVL ID 11702` |
| 622 | `eco.driving.event.duration` | `number` | `seconds` | Duration of event that did generate Green driving | `AVL ID 243, , AVL ID 260` |
| 623 | `eco.driving.events.number` | `number` | — | Average amount of events on some distance | `AVL ID 10009, , AVL ID 15` |
| 624 | `engine.ignition.on.duration` | `number` | `seconds` | Duration when engine is on | `AVL ID 449` |
| 625 | `engine.ignition.status` | `boolean` | — | Engine ignition or ACC status | `AVL ID 239, , AVL ID 837` |
| 626 | `engine.motorhours` | `number` | `hours` | Total calculated engine motorhours | `AVL ID 104` |
| 627 | `error.type` | `number` | — | Protocol-specific error identification number | `AVL ID 341` |
| 628 | `escort.lls.battery.voltage` | `number` | `celsius` | Escort LLS Temperature | `AVL ID 271, , AVL ID 274, , AVL ID 277, , AVL ID 280` |
| 629 | `escort.lls.temperature` | `number` | `celsius` | Escort LLS Temperature | `AVL ID 269, , AVL ID 272, , AVL ID 275, , AVL ID 278` |
| 630 | `escort.lls.value` | `number` | — | Escort LLS fuel level | `AVL ID 270, , AVL ID 273, , AVL ID 276, , AVL ID 279` |
| 631 | `event.code` | `string` | — | Protocol-specific event code string | `AVL ID 342` |
| 632 | `external.battery.capacity` | `number` | `percentage` | Current residual capacity percentage of external battery | `AVL ID 375` |
| 633 | `external.battery.firmware.version` | `string` | — | Firmware version of teltonika external battery | `AVL ID 370` |
| 634 | `external.battery.level` | `number` | `percentage` | External battery level | `AVL ID 375` |
| 635 | `external.battery.status` | `boolean` | — | External battery status | `AVL ID 346` |
| 636 | `external.battery.temperature` | `number` | `celsius` | External battery temperature | `AVL ID 365, , AVL ID 367` |
| 637 | `external.battery.voltage` | `number` | `volts` | External battery voltage | `AVL ID 351` |
| 638 | `external.powersource.status` | `boolean` | — | External power source connection status | `AVL ID 252` |
| 639 | `external.powersource.voltage` | `number` | `volts` | External power voltage | `AVL ID 66, , AVL ID 800` |
| 640 | `external.sensor.temperature` | `number` | `degrees` | External sensor temperature | `AVL ID 390...395` |
| 641 | `extnav.position.speed` | `number` | `km/h` | External receiver instant speed at position detection moment | `AVL ID 355` |
| 642 | `factory.alarm.actuated.status` | `boolean` | — | Factory-installed alarm system is actuated (is in panic mode) status | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 918` |
| 643 | `factory.alarm.emulated.status` | `boolean` | — | Factory-installed alarm system is emulated by module status | `AVL ID 132, , AVL ID 47, , AVL ID 517, , AVL ID 919` |
| 644 | `fall.status` | `boolean` | — | Device fall status true - device is falling, false - falling stopped | `AVL ID 242` |
| 645 | `fms.active.driver.id` | `string` | — | FMS Eco driving active driver ID | `AVL ID 12001` |
| 646 | `fms.adblue.state.enum` | `number` | — | FMS AdBlue status: 0 - Off, 1 - Cond. Red, 2 - Cond. Yellow, 3 - Cond. info | `AVL ID 229` |
| 647 | `fms.braking.fuel.used` | `number` | `liters` | FMS Eco driving Braking fuel used | `AVL ID 12017` |
| 648 | `fms.braking.mileage` | `number` | `km` | FMS Eco driving Braking distance | `AVL ID 12016` |
| 649 | `fms.braking.number` | `number` | — | FMS Eco driving Braking count | `AVL ID 12019` |
| 650 | `fms.braking.time` | `number` | `seconds` | FMS Eco driving Braking time | `AVL ID 12018` |
| 651 | `fms.coasting.fuel.used` | `number` | `liters` | FMS Eco driving coasting fuel used | `AVL ID 12011` |
| 652 | `fms.coasting.mileage` | `number` | `km` | FMS Eco driving coasting distance | `AVL ID 12010` |
| 653 | `fms.coasting.time` | `number` | `seconds` | FMS Eco driving coasting time | `AVL ID 12012` |
| 654 | `fms.cruise.fuel.used` | `number` | `liters` | FMS Eco driving Cruise fuel used | `AVL ID 12024` |
| 655 | `fms.cruise.mileage` | `number` | `km` | FMS Eco driving Cruise distance | `AVL ID 12023` |
| 656 | `fms.cruise.time` | `number` | `seconds` | FMS Eco driving Cruise time | `AVL ID 12025` |
| 657 | `fms.diagnostics.supported` | `number` | — | Indicates if FMS Gateway supports diagnositcs messages to FMS network. 0 - Diagnostics is not supported, 1 - Diagnostics is supported, 2 - Reserved, 3 - Do not care | `AVL ID 110` |
| 658 | `fms.driving.fuel.used` | `number` | `liters` | FMS Eco driving fuel used while driving | `AVL ID 12032` |
| 659 | `fms.ecoroll.fuel.used` | `number` | `liters` | FMS Eco driving EcoRoll fuel used | `AVL ID 12014` |
| 660 | `fms.ecoroll.mileage` | `number` | `km` | FMS Eco driving EcoRoll distance | `AVL ID 12013` |
| 661 | `fms.ecoroll.time` | `number` | `seconds` | FMS Eco driving EcoRoll time | `AVL ID 12015` |
| 662 | `fms.engine.load.fuel.used` | `number` | `liters` | FMS Eco driving fuel used while engine load | `AVL ID 12034` |
| 663 | `fms.event.enum` | `number` | — | FMS Eco driving event IO ID | `AVL ID 12000` |
| 664 | `fms.event.number` | `number` | — | FMS Eco driving event counter | `AVL ID 12003` |
| 665 | `fms.ferry.train.enum` | `number` | — | FMS ferry/train status | `AVL ID 10456` |
| 666 | `fms.fuel.used.braking.range` | `number` | `liters` | FMS Eco driving fuel used indexed parameter for braking range 1 to 10 | `AVL ID 12200...12209` |
| 667 | `fms.fuel.used.rpm.range` | `number` | `liters` | FMS Eco driving fuel used indexed parameter for RPM range 1 to 10 | `AVL ID 12140...12149` |
| 668 | `fms.fuel.used.speed.range` | `number` | `liters` | FMS Eco driving fuel used indexed parameter for speed range 1 to 10 | `AVL ID 12110...12119` |
| 669 | `fms.fuel.used.torque.range` | `number` | `liters` | FMS Eco driving fuel used indexed parameter for torque range 1 to 10 | `AVL ID 12170...12179` |
| 670 | `fms.handling.info` | `number` | — | FMS handling info | `AVL ID 124` |
| 671 | `fms.harsh.acceleration.number` | `number` | — | FMS Eco driving harsh acceleration count | `AVL ID 12053` |
| 672 | `fms.harsh.braking.number` | `number` | — | FMS Eco driving harsh braking count | `AVL ID 12054` |
| 673 | `fms.harsh.cornering.number` | `number` | — | FMS Eco driving harsh cornering count | `AVL ID 12055` |
| 674 | `fms.idle.fuel.used` | `number` | `liters` | FMS Eco driving fuel used while idling | `AVL ID 12033` |
| 675 | `fms.long.stops.number` | `number` | — | FMS Eco driving long stops count | `AVL ID 12051` |
| 676 | `fms.mileage.braking.range` | `number` | `km` | FMS Eco driving distance indexed parameter for braking range 1 to 10 | `AVL ID 12190...12199` |
| 677 | `fms.mileage.rpm.range` | `number` | `km` | FMS Eco driving distance indexed parameter for RPM range 1 to 10 | `AVL ID 12130...12139` |
| 678 | `fms.mileage.speed.range` | `number` | `km` | FMS Eco driving distance indexed parameter for speed range 1 to 10 | `AVL ID 12100...12109` |
| 679 | `fms.mileage.torque.range` | `number` | `km` | FMS Eco driving distance indexed parameter for torque range 1 to 10 | `AVL ID 12160...12169` |
| 680 | `fms.movement.direction` | `number` | — | FMS element direction indicator: 0 - Vehicle is moving Forward, 1 - Reverse | `AVL ID 122` |
| 681 | `fms.parking.brake.number` | `number` | — | FMS Eco driving parking brake count | `AVL ID 12052` |
| 682 | `fms.pto.fuel.used` | `number` | `liters` | FMS Eco driving PTO fuel used | `AVL ID 12030` |
| 683 | `fms.pto.mileage` | `number` | `km` | FMS Eco driving PTO distance | `AVL ID 12029` |
| 684 | `fms.pto.time` | `number` | `seconds` | FMS Eco driving PTO time | `AVL ID 12031` |
| 685 | `fms.requests.supported` | `number` | — | Indicates if FMS Gateway will response to requests from FMS network. 0 - Requests are not supported, 1 - Requests are supported, 2 - Reserved, 3 - Do not care | `AVL ID 111` |
| 686 | `fms.retarder.fuel.used` | `number` | `liters` | FMS Eco driving Retarder fuel used | `AVL ID 12021` |
| 687 | `fms.retarder.mileage` | `number` | `km` | FMS Eco driving Retarder distance | `AVL ID 12020` |
| 688 | `fms.retarder.time` | `number` | `seconds` | FMS Eco driving Retarder time | `AVL ID 12022` |
| 689 | `fms.short.stops.number` | `number` | — | FMS Eco driving short stops count | `AVL ID 12050` |
| 690 | `fms.software.version` | `string` | — | Issue level of FMS-standard document the software included into FMS gateway supports | `AVL ID 109` |
| 691 | `fms.system.event` | `number` | — | FMS system event | `AVL ID 125` |
| 692 | `fms.tacho.performance` | `number` | — | FMS element Tachograph Performance | `AVL ID 123` |
| 693 | `fms.tell.tale` | `string` | — | FMS Tell Tale index parameter in HEX string view | `AVL ID 10428, , AVL ID 10429, , AVL ID 10430, , AVL ID 10431, , AVL ID 13259` |
| 694 | `fms.time.braking.range` | `number` | `seconds` | FMS Eco driving time indexed parameter for braking range 1 to 10 | `AVL ID 12210...12219` |
| 695 | `fms.time.rpm.range` | `number` | `seconds` | FMS Eco driving time indexed parameter for RPM range 1 to 10 | `AVL ID 12150...12159` |
| 696 | `fms.time.speed.range` | `number` | `seconds` | FMS Eco driving time indexed parameter for speed range 1 to 10 | `AVL ID 12120...12129` |
| 697 | `fms.time.torque.range` | `number` | `seconds` | FMS Eco driving time indexed parameter for torque range 1 to 10 | `AVL ID 12180...12189` |
| 698 | `fms.torque.fuel.used` | `number` | `liters` | FMS Eco driving Torque fuel used | `AVL ID 12027` |
| 699 | `fms.torque.mileage` | `number` | `km` | FMS Eco driving Torque distance | `AVL ID 12026` |
| 700 | `fms.torque.time` | `number` | `seconds` | FMS Eco driving Torque time | `AVL ID 12028` |
| 701 | `fms.total.fuel.used` | `number` | `liters` | FMS Eco driving total fuel used | `AVL ID 12036` |
| 702 | `fms.total.mileage` | `number` | `km` | FMS Eco driving total distance | `AVL ID 12035` |
| 703 | `fms.total.time` | `number` | `seconds` | FMS Eco driving total time | `AVL ID 12037` |
| 704 | `fms.vehicle.vin` | `string` | — | FMS Eco driving VIN | `AVL ID 12002` |
| 705 | `freezer.air.temperature` | `number` | `celsius` | Freezer ambient air temperature | `AVL ID 10350` |
| 706 | `freezer.battery.state` | `number` | — | Freezer battery state | `AVL ID 10473` |
| 707 | `freezer.battery.voltage` | `number` | `volts` | Freezer battery voltage | `AVL ID 10041` |
| 708 | `freezer.compressor.rpm` | `number` | `rpm` | Freezer compressor RPM | `AVL ID 10353` |
| 709 | `freezer.compressor.state` | `number` | — | Freezer compressor configuration state | `AVL ID 10354` |
| 710 | `freezer.coolant.temperature` | `number` | `celsius` | Freezer coolant temperature | `AVL ID 10351` |
| 711 | `freezer.datacold.ain` | `number` | `volts` | Freezer datacold analog sensor | `AVL ID 10468...10470` |
| 712 | `freezer.datacold.din` | `boolean` | — | Freezer datacold digital sensor | `AVL ID 10464...10467` |
| 713 | `freezer.datacold.maintenance` | `number` | `hours` | Freezer Maintanence | `AVL ID 10475...10479` |
| 714 | `freezer.datacold.sensor.temperature` | `number` | `celsius` | Freezer datacold temperature sensor | `AVL ID 10644...10649` |
| 715 | `freezer.door.status` | `number` | — | Freezer door status bitmask | `AVL ID 10355` |
| 716 | `freezer.electric.total` | `number` | `hours` | Freezer electric total | `AVL ID 10042` |
| 717 | `freezer.engine.total` | `number` | `hours` | Freezer engine total | `AVL ID 10044` |
| 718 | `freezer.error.count` | `number` | — | Freezer error count | `AVL ID 10352` |
| 719 | `freezer.error.data` | `string` | — | Freezer error codes array hex string | `AVL ID 10639` |
| 720 | `freezer.fuel.level` | `number` | `percentage` | Freezer fuel level | `AVL ID 10040` |
| 721 | `freezer.fuel.sensor.state` | `number` | — | Freezer fuel state flags | `AVL ID 10474` |
| 722 | `freezer.installation.serial` | `string` | — | Freezer installation serial | `AVL ID 10356` |
| 723 | `freezer.manufacturer.id` | `number` | — | Fridge Manufacturer ID | `AVL ID 10472` |
| 724 | `freezer.run.mode` | `string` | — | Freezer run mode | `AVL ID 10480` |
| 725 | `freezer.trailer.serial` | `string` | — | Freezer trailer serial | `AVL ID 10357` |
| 726 | `freezer.transcan.alarm.enum` | `number` | — | Alarm value as reported by TK Transcan | `AVL ID 10691...10694` |
| 727 | `freezer.transcan.state.enum` | `number` | — | Status value as reported by TK Transcan | `AVL ID 10687...10690` |
| 728 | `freezer.transcan.temperature` | `number` | — | Sensor temperature reported by TK Transcan | `AVL ID 10683...10686` |
| 729 | `freezer.vehicle.total` | `number` | `hours` | Freezer vehicle total | `AVL ID 10043` |
| 730 | `freezer.zone1.alarm.code` | `number` | — | Freezer zone 1 alarm code | `AVL ID 10046` |
| 731 | `freezer.zone1.alarm.type` | `number` | — | Freezer zone 1 alarm type | `AVL ID 10045` |
| 732 | `freezer.zone1.evaporator.coil.temperature` | `number` | — | Freezer zone 1 evaporator coil temperature | `AVL ID 10050` |
| 733 | `freezer.zone1.operating.mode` | `number` | — | Freezer zone 1 operating mode | `AVL ID 10053` |
| 734 | `freezer.zone1.return.air.temperature` | `number` | — | Freezer zone 1 return air temperature | `AVL ID 10047, , AVL ID 10051` |
| 735 | `freezer.zone1.supply.air.temperature` | `number` | — | Freezer zone 1 supply air temperature | `AVL ID 10048, , AVL ID 10052` |
| 736 | `freezer.zone1.temperature.setpoint` | `number` | — | Freezer zone 1 temperature setpoint | `AVL ID 10049` |
| 737 | `freezer.zone2.alarm.code` | `number` | — | Freezer zone 2 alarm code | `AVL ID 10055` |
| 738 | `freezer.zone2.alarm.type` | `number` | — | Freezer zone 2 alarm type | `AVL ID 10054` |
| 739 | `freezer.zone2.evaporator.coil.temperature` | `number` | — | Freezer zone 2 evaporator coil temperature | `AVL ID 10059` |
| 740 | `freezer.zone2.operating.mode` | `number` | — | Freezer zone 2 operating mode | `AVL ID 10062` |
| 741 | `freezer.zone2.return.air.temperature` | `number` | — | Freezer zone 2 return air temperature | `AVL ID 10056, , AVL ID 10060` |
| 742 | `freezer.zone2.supply.air.temperature` | `number` | — | Freezer zone 2 supply air temperature | `AVL ID 10057, , AVL ID 10061` |
| 743 | `freezer.zone2.temperature.setpoint` | `number` | — | Freezer zone 2 temperature setpoint | `AVL ID 10058` |
| 744 | `freezer.zone3.alarm.code` | `number` | — | Freezer zone 3 alarm code | `AVL ID 10064` |
| 745 | `freezer.zone3.alarm.type` | `number` | — | Freezer zone 3 alarm type | `AVL ID 10063` |
| 746 | `freezer.zone3.evaporator.coil.temperature` | `number` | — | Freezer zone 3 evaporator coil temperature | `AVL ID 10068` |
| 747 | `freezer.zone3.operating.mode` | `number` | — | Freezer zone 3 operating mode | `AVL ID 10071` |
| 748 | `freezer.zone3.return.air.temperature` | `number` | — | Freezer zone 3 return air temperature | `AVL ID 10065, , AVL ID 10069` |
| 749 | `freezer.zone3.supply.air.temperature` | `number` | — | Freezer zone 3 supply air temperature | `AVL ID 10066, , AVL ID 10070` |
| 750 | `freezer.zone3.temperature.setpoint` | `number` | — | Freezer zone 3 temperature setpoint | `AVL ID 10067` |
| 751 | `fuel.consumed` | `number` | `liters` | Fuel volume totally consumed by vehicle | `AVL ID 12, , AVL ID 138` |
| 752 | `fuel.level` | `number` | `percentage` | Fuel level percentage | `AVL ID 10348, , AVL ID 87` |
| 753 | `geofence.entered.event` | `boolean` | — | Device entered geofence event | `AVL ID 156` |
| 754 | `geofence.id` | `number` | — | Geofence ID | `AVL ID 155` |
| 755 | `geofence.left.event` | `boolean` | — | Device left geofence event | `AVL ID 156` |
| 756 | `geofence.overspeeding.status` | `boolean` | — | Geofence overspeeding status | `AVL ID 157, , AVL ID 248` |
| 757 | `geofence.status` | `boolean` | — | Geofence entered status | `AVL ID 153...154, , AVL ID 155...159, , AVL ID 155...174, , AVL ID 175, , AVL ID 190, , AVL ID 191...198, , AVL ID 208...209, , AVL ID 216...231, , AVL ID 327...356, , AVL ID 550...599, , AVL ID 61...65, , AVL ID 70, , AVL ID 88, , AVL ID 91...99` |
| 758 | `gnss.antenna.short.circuit.status` | `boolean` | — | GNSS antenna short circuit status | `AVL ID 69, , AVL ID 71` |
| 759 | `gnss.antenna.status` | `boolean` | — | GNSS receiver antenna status | `AVL ID 69, , AVL ID 71` |
| 760 | `gnss.first.fix.duration` | `number` | `seconds` | Amount of time it took to get first GNSS fix | `AVL ID 399` |
| 761 | `gnss.jamming.state` | `number` | — | GNSS jamming state | `AVL ID 318` |
| 762 | `gnss.sleep.mode.status` | `boolean` | — | GNSS receiver is in sleep mode | `AVL ID 69, , AVL ID 71` |
| 763 | `gnss.state.enum` | `number` | — | Protocol-specific GNSS state code. May contain information about GNSS fix status, sleep status, ON/OFF, Overcurrent/protect state. | `AVL ID 69, , AVL ID 71` |
| 764 | `gnss.status` | `boolean` | — | GNSS receiver on/off status | `AVL ID 69, , AVL ID 71` |
| 765 | `gps.fuel.rate` | `number` | `liters/h` | GPS-based fuel rate | `AVL ID 13` |
| 766 | `gps.fuel.used` | `number` | `liters` | GPS-based fuel used | `AVL ID 12` |
| 767 | `grain.moisture.level` | `number` | `percentage` | Grain moisture | `AVL ID 129, , AVL ID 44` |
| 768 | `grain.mowing.efficiency.meters2_h` | `number` | `m^2/h` | Mowing efficiency | `AVL ID 127, , AVL ID 42` |
| 769 | `grain.mowing.volume.kg` | `number` | `kg` | Mown volume | `AVL ID 128, , AVL ID 43` |
| 770 | `gsm.cellid` | `number` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID | `AVL ID 13371, , AVL ID 13376, , AVL ID 13381, , AVL ID 13386, , AVL ID 205, , AVL ID 25021, , AVL ID 25024, , AVL ID 25027, , AVL ID 25030, , AVL ID 288, , AVL ID 291, , AVL ID 294, , AVL ID 297, , AVL ID 636` |
| 771 | `gsm.jamming.alarm.status` | `boolean` | — | Alarm status for the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) jamming | `AVL ID 249` |
| 772 | `gsm.lac` | `number` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code | `AVL ID 13370, , AVL ID 13375, , AVL ID 13380, , AVL ID 13385, , AVL ID 206, , AVL ID 25020, , AVL ID 25023, , AVL ID 25026, , AVL ID 25029, , AVL ID 287, , AVL ID 290, , AVL ID 293, , AVL ID 296` |
| 773 | `gsm.mcc` | `number` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code | `AVL ID 13374, , AVL ID 13379, , AVL ID 13384, , AVL ID 13389, , AVL ID 241` |
| 774 | `gsm.mnc` | `number` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) code | `AVL ID 1200, , AVL ID 1201...1203, , AVL ID 13373, , AVL ID 13378, , AVL ID 13383, , AVL ID 13388, , AVL ID 241, , AVL ID 25032, , AVL ID 25033...25035` |
| 775 | `gsm.network.mode.enum` | `number` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) registration mode reported by the device, protocol-specific value set | `AVL ID 22, , AVL ID 80` |
| 776 | `gsm.network.roaming.status` | `boolean` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) in roaming mode | `AVL ID 22, , AVL ID 80` |
| 777 | `gsm.network.type` | `string` | — | The type of the Mobile network the device is currently registered to | `AVL ID 178, , AVL ID 237` |
| 778 | `gsm.operator.code` | `string` | — | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) operator code, which is MCC joined with MNC | `AVL ID 241` |
| 779 | `gsm.signal.dbm` | `number` | `dbm` | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal | `AVL ID 13372, , AVL ID 13377, , AVL ID 13382, , AVL ID 13387, , AVL ID 25019, , AVL ID 25022, , AVL ID 25025, , AVL ID 25028, , AVL ID 25031, , AVL ID 286, , AVL ID 289, , AVL ID 292, , AVL ID 295, , AVL ID 298` |
| 780 | `gsm.signal.level` | `number` | `percentage` | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal strength level | `AVL ID 21` |
| 781 | `gsm.signal.quality` | `number` | — | The quality (bit error rate) of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal | `AVL ID 1148, , AVL ID 20017, , AVL ID 25017` |
| 782 | `gsm.sim.iccid` | `string` | — | Integrated Circuit Card Id of SIM card of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) | `AVL ID 11, , AVL ID 14, , AVL ID 221, , AVL ID 641, , Command type 0x06` |
| 783 | `gsm.sim.imsi` | `string` | — | IMSI of SIM card of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) | `AVL ID 218, , AVL ID 230, , AVL ID 231` |
| 784 | `gsm.sim.status` | `boolean` | — | SIM card is active | `AVL ID 232` |
| 785 | `harsh.acceleration.event` | `boolean` | — | Harsh acceleration detected | `AVL ID 253` |
| 786 | `harsh.braking.event` | `boolean` | — | Harsh braking detected | `AVL ID 253` |
| 787 | `harsh.cornering.angle` | `number` | `degrees` | Harsh cornering angle | `AVL ID 254` |
| 788 | `harsh.cornering.event` | `boolean` | — | Harsh cornering detected | `AVL ID 253` |
| 789 | `harvest.area` | `number` | `m^2` | Area of harvest | `AVL ID 126, , AVL ID 41` |
| 790 | `harvest.drum.gap` | `number` | `mm` | Gap under harvesting drum | `AVL ID 131, , AVL ID 46` |
| 791 | `harvest.drum.rpm` | `number` | `rpm` | Harvesting drum RPM | `AVL ID 130, , AVL ID 45` |
| 792 | `harvest.duration` | `number` | `seconds` | Harvesting time | `AVL ID 125, , AVL ID 40` |
| 793 | `helmet.status` | `boolean` | — | Helmet status: true - helmet is in, false - helmet is not in | `AVL ID 843` |
| 794 | `ibutton.authorized.state.enum` | `number` | — | iButton authorization state code | `AVL ID 252` |
| 795 | `ibutton.authorized.status` | `boolean` | — | iButton authorized status | `AVL ID 248, , AVL ID 251, , AVL ID 252` |
| 796 | `ibutton.code` | `string` | — | Hexadecimal code of connected iButton | `AVL ID 78` |
| 797 | `ibutton.connected.status` | `boolean` | — | iButton connection status | `AVL ID 248, , AVL ID 251` |
| 798 | `idle.status` | `boolean` | — | Vehicle is in idling state | `AVL ID 177, , AVL ID 243, , AVL ID 251` |
| 799 | `ignition.state` | `number` | — | Ignition state according to device manual | `AVL ID 836` |
| 800 | `immobilizer.keys.status` | `boolean` | — | Programmed sequence of keys is introduced to the imm2m.sim2er in the car | `AVL ID 132, , AVL ID 47` |
| 801 | `immobilizer.service.status` | `boolean` | — | immobilizer is in the service mode status | `AVL ID 132, , AVL ID 47` |
| 802 | `immobilizer.state` | `string` | — | Immobilizer state | `AVL ID 251` |
| 803 | `immobilizer.state.enum` | `number` | — | Immobilizer state number | `AVL ID 248, , AVL ID 251` |
| 804 | `instant.movement.status` | `boolean` | — | Instant movement status | `AVL ID 303` |
| 805 | `instrument.panel.firmware.version` | `string` | — | Scooter's Instrument panel FW version | `AVL ID 372` |
| 806 | `internal.battery.capacity` | `number` | `percentage` | Current residual capacity percentage of internal battery | `AVL ID 374` |
| 807 | `internal.battery.firmware.version` | `string` | — | Firmware version of teltonika internal(IoT) battery | `AVL ID 371` |
| 808 | `internal.battery.voltage` | `number` | `volts` | Internal battery voltage | `AVL ID 350` |
| 809 | `iso6709.coordinates` | `string` | — | String with position in ISO 6709 format | `AVL ID 387` |
| 810 | `isobus.implement.park.status` | `boolean` | — | ISOBUS implement park status | `AVL ID 12412` |
| 811 | `isobus.implement.transport.status` | `boolean` | — | ISOBUS implement transport status | `AVL ID 12411` |
| 812 | `isobus.key.switch.status` | `boolean` | — | ISOBUS key switch status | `AVL ID 12407` |
| 813 | `isobus.maintain.actuator.power.status` | `boolean` | — | ISOBUS maintain actuator power status | `AVL ID 12410` |
| 814 | `isobus.maintain.ecu.power.status` | `boolean` | — | ISOBUS maintain ECU power status | `AVL ID 12409` |
| 815 | `isobus.rear.pto.economy.mode.status` | `boolean` | — | ISOBUS rear PTO economy mode status | `AVL ID 12431` |
| 816 | `isobus.rear.pto.engagement.status` | `boolean` | — | ISOBUS rear PTO engagement status | `AVL ID 12429` |
| 817 | `isobus.rear.pto.mode.enum` | `string` | — | ISOBUS rear PTO mode | `AVL ID 12430` |
| 818 | `isobus.rear.pto.output.shaft.speed` | `number` | `rpm` | ISOBUS rear PTO output shaft speed | `AVL ID 12427` |
| 819 | `isobus.rear.pto.shaft.speed.point` | `number` | `rpm` | ISOBUS rear PTO shaft speed set point | `AVL ID 12428` |
| 820 | `isobus.start.stop.status` | `boolean` | — | ISOBUS start/stop status | `AVL ID 12408` |
| 821 | `issuing.member.state.card` | `number` | — | Card Issuing Member State, NationNumeric as described in EEC 3821_85 | `AVL ID 10167, , AVL ID 10168, , AVL ID 222, , AVL ID 223` |
| 822 | `kickstand.status` | `boolean` | — | Kickstand status true - not released, false - released | `AVL ID 819` |
| 823 | `kill.switch.status` | `boolean` | — | Kill switch status: true - not active, false - active | `AVL ID 818` |
| 824 | `lls.temperature` | `number` | `celsius` | LLS (Liquid level sensor) fuel temperature | `AVL ID 202, , AVL ID 204, , AVL ID 211, , AVL ID 213, , AVL ID 215` |
| 825 | `lls.value` | `number` | — | LLS (Liquid level sensor) fuel value | `AVL ID 201, , AVL ID 203, , AVL ID 210, , AVL ID 212, , AVL ID 214` |
| 826 | `lock.status` | `boolean` | — | Lock status | `AVL ID 344` |
| 827 | `log.file.current` | `number` | — | Current active log file | `AVL ID 13266` |
| 828 | `log.file.max.count` | `number` | — | Max log file count | `AVL ID 13267` |
| 829 | `malfunction.indicator.status` | `boolean` | — | Malfunction indicator status: true - active, false - not active | `AVL ID 821` |
| 830 | `mandown.alarm.status` | `boolean` | — | Man down alarm activated | `AVL ID 242` |
| 831 | `manual.can` | `number` | — | Indexed Manual CAN parameter value | `AVL ID 10216...10235, , AVL ID 10298...10347, , AVL ID 145...154, , AVL ID 380...389` |
| 832 | `manual.can.extended` | `string` | — | HEX representation of Manual CAN Extended | `AVL ID 10358` |
| 833 | `manual.can.hex` | `string` | — | Indexed manual CAN parameter value in HEX representation | `AVL ID 10216...10235, , AVL ID 10298...10347, , AVL ID 145...154, , AVL ID 380...389` |
| 834 | `max.x.acceleration` | `number` | `g` | Harsh acceleration event max accelerometer value on X-axis | `AVL ID 1432, , AVL ID 258` |
| 835 | `max.y.acceleration` | `number` | `g` | Harsh acceleration event max accelerometer value on Y-axis | `AVL ID 1432, , AVL ID 258` |
| 836 | `max.z.acceleration` | `number` | `g` | Harsh acceleration event max accelerometer value on Z-axis | `AVL ID 1432, , AVL ID 258` |
| 837 | `mobileye.brake.signal.status` | `boolean` | — | Mobileye brake signal status, true - brake signal is on, false - brake signal is off | `AVL ID 313` |
| 838 | `mobileye.dusk.status` | `boolean` | — | Mobileye dusk time indicator | `AVL ID 291` |
| 839 | `mobileye.error.code` | `number` | — | Mobileye error code | `AVL ID 293` |
| 840 | `mobileye.error.valid.status` | `boolean` | — | Mobileye error is valid status | `AVL ID 292` |
| 841 | `mobileye.failsafe.mode.status` | `boolean` | — | Mobileye indocator of failsafe mode activation | `AVL ID 301` |
| 842 | `mobileye.forward.collision.warning.status` | `boolean` | — | Mobileye indicator of forward collision warning event status | `AVL ID 302` |
| 843 | `mobileye.headway.measurement` | `number` | `seconds` | Mobileye headway measurement, 0 means no closest in-path vehicle on the range | `AVL ID 296` |
| 844 | `mobileye.headway.valid.status` | `boolean` | — | Mobileye headway valid status | `AVL ID 295` |
| 845 | `mobileye.headway.warning.level` | `number` | — | Mobileye headway warning level | `AVL ID 305` |
| 846 | `mobileye.headway.warning.repeat.enabled.status` | `boolean` | — | Mobileye headway warning repeat enabled status | `AVL ID 304` |
| 847 | `mobileye.high.beam.available.status` | `boolean` | — | Mobileye high beam available status, true - high beam available, false - high beam not available | `AVL ID 316` |
| 848 | `mobileye.high.beam.status` | `boolean` | — | Mobileye high beam status, true - high beam on, false - high beam off | `AVL ID 308` |
| 849 | `mobileye.internal.error.status` | `boolean` | — | Mobileye indicator of internal error. See user manual for details | `AVL ID 300` |
| 850 | `mobileye.lane.departure.left.warning.status` | `boolean` | — | Mobileye indicator of left lane departure warning event status | `AVL ID 298` |
| 851 | `mobileye.lane.departure.right.warning.status` | `boolean` | — | Mobileye indicator of right lane departure warning event status | `AVL ID 299` |
| 852 | `mobileye.lane.departure.warnings.status` | `boolean` | — | Mobileye lane departure warnings status, true - wanrings enabled, false - warnings disabled due to low speed or configuration | `AVL ID 297` |
| 853 | `mobileye.left.blink.available.status` | `boolean` | — | Mobileye left blink available status, true - left blink available, false - left blink not available | `AVL ID 312` |
| 854 | `mobileye.low.beam.available.status` | `boolean` | — | Mobileye low beam available status, true - low beam available, false - low beam not available | `AVL ID 315` |
| 855 | `mobileye.low.beam.status` | `boolean` | — | Mobileye low beam status, true - low beam on, false - low beam off | `AVL ID 309` |
| 856 | `mobileye.movement.status` | `boolean` | — | Mobileye host vehicle is moving status | `AVL ID 294` |
| 857 | `mobileye.night.status` | `boolean` | — | Mobileye night time indicator | `AVL ID 291` |
| 858 | `mobileye.pedestrian.collision.warning.status` | `boolean` | — | Mobileye indicator of pedestrians collision warning | `AVL ID 290` |
| 859 | `mobileye.pedestrian.danger.zone.status` | `boolean` | — | Mobileye indicator of pedestrians in danger zone | `AVL ID 289` |
| 860 | `mobileye.right.blink.available.status` | `boolean` | — | Mobileye right blink available status, true - right blink available, false - right blink not available | `AVL ID 311` |
| 861 | `mobileye.sound.type` | `number` | — | Mobileye sound type | `AVL ID 288` |
| 862 | `mobileye.speed` | `number` | `km/h` | Mobileye speed | `AVL ID 318` |
| 863 | `mobileye.speed.available.status` | `boolean` | — | Mobileye speed available status, true - speed available, false - speed not available | `AVL ID 317` |
| 864 | `mobileye.tamper.status` | `boolean` | — | Mobileye indicator of tamper alert (tamper alert is activated if there is no vehicle or lane detection for duration of 10 minutes tamper alert is active above 15 km/h | `AVL ID 307` |
| 865 | `mobileye.traffic.signs.recognition.status` | `boolean` | — | Mobileye traffic signs recognition enabled status | `AVL ID 303` |
| 866 | `mobileye.traffic.signs.speed.warning.level` | `number` | — | Mobileye traffic signs recongition system's warning level | `AVL ID 306` |
| 867 | `mobileye.wipers.available.status` | `boolean` | — | Mobileye wipers available status, true - wipers available, false - wipers not available | `AVL ID 314` |
| 868 | `mobileye.wipers.status` | `boolean` | — | Mobileye wipers status, true - wiper passes the windshield, false - wiper is static | `AVL ID 310` |
| 869 | `modem.uptime` | `number` | `seconds` | The total time the modem has been powered on | `AVL ID 20015, , AVL ID 25015` |
| 870 | `motorcycle.fall.event` | `boolean` | — | Motorcycle fall event | `AVL ID 1412` |
| 871 | `movement.event` | `boolean` | — | Movement detected | `AVL ID 310` |
| 872 | `movement.status` | `boolean` | — | Current movement state | `AVL ID 240` |
| 873 | `negative.input.status` | `boolean` | — | Negative input connection to ground status: true - connected, false - disconnected | `AVL ID 381` |
| 874 | `network.lte.band` | `number` | — | LTE band | `AVL ID 1149` |
| 875 | `network.signal.rsrp` | `number` | `dbm` | LTE reference signal received power (RSRP) | `AVL ID 1148, , AVL ID 20016, , AVL ID 25016` |
| 876 | `network.signal.rssi` | `number` | `dbm` | Network signal strength | `AVL ID 1148` |
| 877 | `network.signal.sinr` | `number` | `dbm` | Network Singal to Interference plus Noise ratio | `AVL ID 1148` |
| 878 | `onewire.sensor.serial` | `string` | — | External 1-Wire sensor serial number in HEX representation | `AVL ID 5, , AVL ID 62...65, , AVL ID 7, , AVL ID 71, , AVL ID 75, , AVL ID 76, , AVL ID 77, , AVL ID 79` |
| 879 | `operating.mode.enum` | `number` | — | Protocol-specific device operating mode | `AVL ID 349, , AVL ID 831` |
| 880 | `overspeeding.speed` | `number` | `km/h` | GNSS based speed when overspeeding event is triggered | `AVL ID 255` |
| 881 | `overspeeding.status` | `boolean` | — | Overspeeding detected | `AVL ID 153...154, , AVL ID 155...159, , AVL ID 155...174, , AVL ID 190, , AVL ID 191...198, , AVL ID 208...209, , AVL ID 216...231, , AVL ID 255, , AVL ID 327...356, , AVL ID 550...599, , AVL ID 61...65, , AVL ID 70, , AVL ID 88, , AVL ID 91...99` |
| 882 | `park.brake.status` | `boolean` | — | Park brake status: true - active, false - not active | `AVL ID 801, , AVL ID 832` |
| 883 | `payload.hex` | `string` | — | HEX Payload received from device | `AVL ID 10611...10612, , Command type 0x06` |
| 884 | `pcb.firmware.enum` | `number` | — | Firmware version of the teltonika PCB | `AVL ID 340` |
| 885 | `pcb.temperature` | `number` | `celsius` | PCB temperature | `AVL ID 13201, , AVL ID 70` |
| 886 | `phone.call.state.enum` | `number` | — | Phone call status | `AVL ID 13361` |
| 887 | `position.fix.age` | `number` | `seconds` | Time since the last position fix | `AVL ID 386` |
| 888 | `position.hdop` | `number` | — | Horizontal dilution of precision | `AVL ID 182` |
| 889 | `position.pdop` | `number` | — | Position dilution of precision | `AVL ID 181` |
| 890 | `position.speed` | `number` | `km/h` | Instant speed at position detection moment | `AVL ID 24, , Command type 0x06` |
| 891 | `position.valid` | `boolean` | — | Is position information accurate and valid for given timestamp | `AVL ID 69, , AVL ID 71, , Command type 0x06` |
| 892 | `power.consumtion` | `number` | `Wh/km` | Vehicle power consumtion | `AVL ID 838` |
| 893 | `power.on.status` | `boolean` | — | Power-on device status | `AVL ID 390` |
| 894 | `powertrain.state` | `number` | — | Powertrain state | `AVL ID 820` |
| 895 | `predicted.remaining.mileage` | `number` | `km` | Predicted remaining mileage | `AVL ID 354` |
| 896 | `private.status` | `boolean` | — | Device is in private mode | `AVL ID 250, , AVL ID 391` |
| 897 | `proximity.duration` | `number` | `seconds` | Proximity violation duration | `AVL ID 890` |
| 898 | `proximity.violation.ident` | `string` | — | IMEI of the device which violates personal space | `AVL ID 875` |
| 899 | `proximity.violation.mac.address` | `string` | — | MAC address which violates personal space | `AVL ID 875` |
| 900 | `proximity.violation.reason` | `number` | — | Cause of Proximity violation | `AVL ID 889` |
| 901 | `proximity.violation.state` | `number` | — | Bitmask describing the causes of proximity violation | `AVL ID 874` |
| 902 | `pto.drive.engagement.enum` | `number` | — | PTO drive engagement. 0 - No PTO drive is engaged. 1 - At least one PTO drive is engaged, 2 - Error, 3 - Not available | `AVL ID 137` |
| 903 | `recovery.alarm` | `boolean` | — | Recovery alarm | `AVL ID 20012` |
| 904 | `remaining.range` | `number` | `km` | Current remaining range | `AVL ID 822` |
| 905 | `rfid.code` | `string` | — | Hexadecimal code of connected RFID | `AVL ID 207, , AVL ID 217` |
| 906 | `scenario.status` | `boolean` | — | Custom scenario status | `AVL ID 358, , AVL ID 358...361, , AVL ID 359, , AVL ID 360` |
| 907 | `scooter.battery.level` | `number` | `percentage` | Scooter battery level | `AVL ID 352` |
| 908 | `sd.status` | `boolean` | — | SD status presence | `AVL ID 10, , AVL ID 144` |
| 909 | `seco.state` | `string` | — | Secure engine cut-off (SECO) output state | `AVL ID 396` |
| 910 | `seco.state.enum` | `number` | — | Secure engine cut-off (SECO) output state: 0 - off, 1 - pulsing, 2 - on | `AVL ID 396` |
| 911 | `segment.can.fuel.consumed` | `number` | `liters` | Fuel volume consumed by vehicle on the last segment using CAN data | `AVL ID 110` |
| 912 | `segment.can.vehicle.mileage` | `number` | `km` | Vehicle mileage on the last segment using CAN data | `AVL ID 134` |
| 913 | `segment.vehicle.mileage` | `number` | `km` | Segment mileage | `AVL ID 199, , AVL ID 357` |
| 914 | `sensor.humidity` | `number` | `percentage` | Humidity sensor value, i.e. relative air humidity level | `AVL ID 10487...10492` |
| 915 | `sensor.temperature` | `number` | `celsius` | Temperature sensor value | `AVL ID 6, , AVL ID 72...74, , AVL ID 72...75, , AVL ID 75, , AVL ID 8` |
| 916 | `sensor.temperature.error.code` | `string` | — | Temperature sensor error description | `AVL ID 72...75` |
| 917 | `sim.card.error.count` | `number` | — | Error counter for No Sim Card error | `AVL ID 13200` |
| 918 | `sleep.mode.enum` | `number` | — | Protocol-specific value indicating device sleep mode state | `AVL ID 200` |
| 919 | `software.version` | `string` | — | Software version string | `AVL ID 340` |
| 920 | `supersoco.battery.capacity` | `number` | — | SuperSoco battery capacity left | `AVL ID 858` |
| 921 | `supersoco.battery.energy` | `number` | — | SuperSoco battery energy | `AVL ID 867` |
| 922 | `supersoco.current.trip.range` | `number` | — | SuperSoco current trip range | `AVL ID 856` |
| 923 | `supersoco.fw.version` | `number` | — | SuperSoco vehicle firmware version | `AVL ID 865` |
| 924 | `supersoco.instrument.system.error` | `string` | — | SuperSoco instrument system error | `AVL ID 870` |
| 925 | `supersoco.lock.status` | `boolean` | — | SuperSoco lock status | `AVL ID 864` |
| 926 | `supersoco.moving.abnormal.status` | `boolean` | — | SuperSoco moving abnormal status | `AVL ID 862` |
| 927 | `supersoco.power.status` | `boolean` | — | SuperSoco power status: true - ON, false - OFF | `AVL ID 855` |
| 928 | `supersoco.power.system.error` | `string` | — | SuperSoco power system error | `AVL ID 868` |
| 929 | `supersoco.powertrain.error` | `string` | — | SuperSoco power traing error | `AVL ID 869` |
| 930 | `supersoco.range` | `number` | — | SuperSoco range | `AVL ID 863` |
| 931 | `supersoco.temperature.high.status` | `boolean` | — | SuperSoco high temperature status | `AVL ID 860` |
| 932 | `supersoco.total.range` | `number` | — | SuperSoco total range | `AVL ID 866` |
| 933 | `supersoco.total.trip.range` | `number` | — | SuperSoco total trip range | `AVL ID 857` |
| 934 | `supersoco.upload.time` | `number` | — | SuperSoco upload time | `AVL ID 861` |
| 935 | `supersoco.voltage.low.status` | `boolean` | — | SuperSoco low voltage status | `AVL ID 859` |
| 936 | `tacho.border.crossing.info` | `number` | — | Tachograph border crossing info | `AVL ID 10542` |
| 937 | `tacho.data.source` | `string` | — | Tacho data source | `AVL ID 48` |
| 938 | `tacho.driver.activity.duration` | `number` | `seconds` | Duration of the current driver activity reported by tacho, indexed by card slot | `AVL ID 10173, , AVL ID 10174, , AVL ID 143, , AVL ID 144, , AVL ID 60...61` |
| 939 | `tacho.driver.activity.state` | `string` | — | Current driver activity reported by tacho, indexed by card slot, rest / work / drive / available / not available / error | `AVL ID 10159, , AVL ID 10160, , AVL ID 115, , AVL ID 116, , AVL ID 137, , AVL ID 138, , AVL ID 184, , AVL ID 185` |
| 940 | `tacho.driver.activity.state.enum` | `number` | — | Current driver activity reported by tacho, indexed by card slot, 0 - rest, 1 - work, 2 - drive, 3 - available, 4 - not available, 5 - error | `AVL ID 10159, , AVL ID 10160, , AVL ID 115, , AVL ID 116, , AVL ID 137, , AVL ID 138, , AVL ID 184, , AVL ID 185` |
| 941 | `tacho.driver.card.code` | `string` | — | Driver identification card id for tacho, indexed by card slot | `AVL ID 10165, , AVL ID 10166, , AVL ID 147, , AVL ID 148, , AVL ID 149, , AVL ID 150, , AVL ID 195, , AVL ID 196, , AVL ID 197, , AVL ID 198` |
| 942 | `tacho.driver.card.data.available.status` | `boolean` | — | Tacho Driver card data availability | `AVL ID 10538` |
| 943 | `tacho.driver.card.expiration` | `number` | `seconds` | Driver card expiry date reported by tacho, indexed for driver number | `AVL ID 13466, , AVL ID 13467` |
| 944 | `tacho.driver.card.presence` | `number` | — | Tacho driver card presence enum | `AVL ID 10161, , AVL ID 10162, , AVL ID 120, , AVL ID 121, , AVL ID 187, , AVL ID 188` |
| 945 | `tacho.driver.card.status` | `boolean` | — | Tacho driver card status | `AVL ID 10161, , AVL ID 10162, , AVL ID 120, , AVL ID 121, , AVL ID 136, , AVL ID 187, , AVL ID 188` |
| 946 | `tacho.driver.compensation.before.last.week.duration` | `number` | `seconds` | Tacho Driver open compensation in week before last | `AVL ID 10536` |
| 947 | `tacho.driver.compensation.last.week.duration` | `number` | `seconds` | Tacho Driver open compensation in the last week | `AVL ID 10535` |
| 948 | `tacho.driver.compensation.second.before.last.week.duration` | `number` | `seconds` | Tacho Driver open compensation in 2nd week before last | `AVL ID 10537` |
| 949 | `tacho.driver.continuous_driving.duration` | `number` | `seconds` | Driver continuous driving time | `AVL ID 10169, , AVL ID 10170, , AVL ID 139, , AVL ID 140, , AVL ID 56...57` |
| 950 | `tacho.driver.cumulative_break.duration` | `number` | `seconds` | Driver cumulative break time | `AVL ID 10171, , AVL ID 10172, , AVL ID 141, , AVL ID 142, , AVL ID 58...59` |
| 951 | `tacho.driver.cumulative_driving.duration` | `number` | `seconds` | Driver cumulative driving time | `AVL ID 10175, , AVL ID 10176, , AVL ID 145, , AVL ID 146, , AVL ID 69, , AVL ID 77` |
| 952 | `tacho.driver.current.activity.duration` | `number` | `seconds` | Current driver activity duration | `AVL ID 143, , AVL ID 144` |
| 953 | `tacho.driver.daily.before.rest.duration` | `number` | `seconds` | Time left until new daily rest period read from Tacho, indexed for driver number | `AVL ID 10509, , AVL ID 10516` |
| 954 | `tacho.driver.daily.driving.duration` | `number` | `seconds` | Current daily driving time read from Tacho, indexed for driver number | `AVL ID 10507, , AVL ID 10514` |
| 955 | `tacho.driver.daily.limit.exceed.number` | `number` | — | Tacho Driver number of times 9h daily driving time exceeds | `AVL ID 10510, , AVL ID 10517` |
| 956 | `tacho.driver.daily.minimum.rest.duration` | `number` | `seconds` | Tacho Driver Minimum Daily Rest duration | `AVL ID 10524, , AVL ID 10525` |
| 957 | `tacho.driver.daily.rest.end.timestamp` | `number` | — | Tacho Driver end of last daily rest report timestamp | `AVL ID 10504, , AVL ID 10511` |
| 958 | `tacho.drive.recognize.status` | `boolean` | — | Tacho recognized vehicle drive | `AVL ID 10154, , AVL ID 183` |
| 959 | `tacho.driver.load.time` | `number` | `seconds` | Driver loading/unloading time reported by tacho, indexed for driver number | `AVL ID 13261, , AVL ID 13262` |
| 960 | `tacho.driver.multi.manning.status` | `boolean` | — | Tacho Driver multi-manning detection status | `AVL ID 10538` |
| 961 | `tacho.driver.next.driving.duration` | `number` | `seconds` | Tacho Driver duration of next driving period | `AVL ID 10541` |
| 962 | `tacho.driver.next.rest.duration` | `number` | `seconds` | Duration of next rest period read from Tacho, indexed for driver number | `AVL ID 10528, , AVL ID 10529` |
| 963 | `tacho.driver.private.data.consent` | `number` | — | Drivers private data consent status reported by tacho | `AVL ID 13263` |
| 964 | `tacho.driver.remaining.before.rest.duration` | `number` | `seconds` | Duration remaining before next rest period read from Tacho, indexed for driver number | `AVL ID 10530, , AVL ID 10531` |
| 965 | `tacho.driver.remaining.current.driving.duration` | `number` | `seconds` | Tacho Driver remaining current driving time | `AVL ID 10532` |
| 966 | `tacho.driver.remaining.current.rest.duration` | `number` | `seconds` | Tacho Driver remaining time of current break/rest | `AVL ID 10539` |
| 967 | `tacho.driver.remaining.reduced.daily.rest.periods` | `number` | — | Tacho Driver remaining reduced daily rest periods. Range 0 to 3 | `AVL ID 10538` |
| 968 | `tacho.driver.remaining.shift.driving.duration` | `number` | `seconds` | Tacho Driver remaining driving time on current shift | `AVL ID 10533` |
| 969 | `tacho.driver.remaining.ten.hour.driving.times` | `number` | — | Tacho Driver remaining 10h driving times. Range 0 to 2 | `AVL ID 10538` |
| 970 | `tacho.driver.remaining.weekly.driving.duration` | `number` | `seconds` | Tacho Driver remaining driving time of current week | `AVL ID 10534` |
| 971 | `tacho.driver.selected.activity.duration` | `number` | `seconds` | Indexed Tacho parameter indicating current duration of the selected activity, since selected and which may be the current driving period, availability period, rest period or work period | `AVL ID 10173, , AVL ID 10174, , AVL ID 60...61` |
| 972 | `tacho.driver.time.before.warning` | `number` | `minutes` | Tacho driver's hours rules pre warning time delay | `AVL ID 10501` |
| 973 | `tacho.driver.time.overlap.status` | `boolean` | — | Tacho Driver time overlap detection status | `AVL ID 10538` |
| 974 | `tacho.driver.time.state` | `string` | — | Tacho driver time related states | `AVL ID 10163, , AVL ID 10164, , AVL ID 189...190` |
| 975 | `tacho.driver.time.state.enum` | `number` | — | Tacho driver time related states | `AVL ID 10163, , AVL ID 10164, , AVL ID 189...190` |
| 976 | `tacho.driver.time.until.next.driving` | `number` | `seconds` | Tacho Driver time left until next driving period | `AVL ID 10540` |
| 977 | `tacho.driver.unknown.periods.present.status` | `boolean` | — | Tacho Driver unknown periods presence | `AVL ID 10538` |
| 978 | `tacho.driver.weekly.before.rest.duration` | `number` | `seconds` | Time left until new weekly rest period read from Tacho, indexed for driver number | `AVL ID 10522, , AVL ID 10523` |
| 979 | `tacho.driver.weekly.driving.duration` | `number` | `seconds` | Current weekly driving time read from Tacho, indexed for driver number | `AVL ID 10508, , AVL ID 10515` |
| 980 | `tacho.driver.weekly.minimum.rest.duration` | `number` | `seconds` | Tacho Driver Minimum Weekly Rest duration | `AVL ID 10526, , AVL ID 10527` |
| 981 | `tacho.driver.weekly.rest.calculation.status` | `boolean` | — | Tacho Driver weekly rest period calculation status | `AVL ID 10538` |
| 982 | `tacho.driver.weekly.rest.end.timestamp` | `number` | — | Tacho Driver end of last weekly rest period timestamp | `AVL ID 10505, , AVL ID 10512` |
| 983 | `tacho.driver.weekly.second.rest.end.timestamp` | `number` | — | Tacho Driver end of second last weekly rest period timestamp | `AVL ID 10506, , AVL ID 10513` |
| 984 | `tacho.driver.work.state` | `string` | — | Protocol-specific driver work state name | `AVL ID 10159, , AVL ID 10160, , AVL ID 115, , AVL ID 116, , AVL ID 184, , AVL ID 185` |
| 985 | `tacho.driver.work.state.enum` | `number` | — | Protocol-specific driver work state value | `AVL ID 10159, , AVL ID 10160, , AVL ID 115, , AVL ID 116, , AVL ID 137, , AVL ID 138, , AVL ID 184, , AVL ID 185` |
| 986 | `tacho.kline.privacy.mode.enum` | `string` | — | Tachograph K-Line privacy mode | `AVL ID 10543` |
| 987 | `tacho.movement.status` | `boolean` | — | Movement status reported by tacho | `AVL ID 114` |
| 988 | `tacho.next.calibration.timestamp` | `number` | — | Tacho next calibration timestamp | `AVL ID 10503` |
| 989 | `tacho.out.of.scope.condition.status` | `boolean` | — | Tacho out of scope condition is met. Indicates whether the vehicle is currently operating under an exemption from tachograph regulations. | `AVL ID 10502` |
| 990 | `tacho.overspeeding.status` | `boolean` | — | Overspeeding status reported by tacho | `AVL ID 10155, , AVL ID 117, , AVL ID 186` |
| 991 | `tacho.position.speed` | `number` | `km/h` | Instant speed reported by tacho | `AVL ID 10156, , AVL ID 126, , AVL ID 135, , AVL ID 191` |
| 992 | `tacho.timestamp` | `number` | `seconds` | Time reported by tacho | `AVL ID 10153, , AVL ID 194` |
| 993 | `tacho.trip.mileage` | `number` | `km` | Trip mileage reported by tacho | `AVL ID 10152, , AVL ID 193` |
| 994 | `tacho.vehicle.load.type` | `string` | — | Tachograph vehicle load type | `AVL ID 13260` |
| 995 | `tacho.vehicle.mileage` | `number` | `km` | Total mileage calculated by tacho | `AVL ID 10151, , AVL ID 133, , AVL ID 192` |
| 996 | `tamper.alarm` | `boolean` | — | Tamper alarm event | `AVL ID 520` |
| 997 | `tamper.alarm.state` | `string` | — | Tamper record event reason | `AVL ID 20019` |
| 998 | `tamper.alarm.state.enum` | `number` | — | Tamper record event numeric reason | `AVL ID 20019` |
| 999 | `top.case.status` | `boolean` | — | Top case opened status: true - opened, false - closed | `AVL ID 844` |
| 1000 | `total.driving.time` | `number` | `seconds` | Total riding time | `AVL ID 359` |
| 1001 | `total.mileage` | `number` | `km` | Total mileage | `AVL ID 112` |
| 1002 | `total.operate.time` | `number` | `seconds` | Total operation time | `AVL ID 358` |
| 1003 | `total.vehicle.weight` | `number` | `kg` | Total vehicle weight | `AVL ID 139` |
| 1004 | `towing.alarm.status` | `boolean` | — | Towing alarm state | `AVL ID 246` |
| 1005 | `trailer.abs.state.enum` | `number` | — | Trailer ABS Status | `AVL ID 13653` |
| 1006 | `trailer.amber.warning.request.state.enum` | `number` | — | Amber warning request status | `AVL ID 13656` |
| 1007 | `trailer.automatic.towed.vehicle.braking.state.enum` | `number` | — | Automatic towed vehicle braking status | `AVL ID 13805` |
| 1008 | `trailer.axle.load.sum` | `number` | `kg` | Sum of all axle loads | `AVL ID 13657` |
| 1009 | `trailer.brake.lining.axle.1.wheel.10.level` | `number` | `percentage` | Brake lining level for axle 1 wheel 10 | `AVL ID 13733` |
| 1010 | `trailer.brake.lining.axle.1.wheel.10.state.enum` | `number` | — | Brake lining status for axle 1 wheel 10 | `AVL ID 13718` |
| 1011 | `trailer.brake.lining.axle.1.wheel.6.level` | `number` | `percentage` | Brake lining level for axle 1 wheel 6 | `AVL ID 13729` |
| 1012 | `trailer.brake.lining.axle.1.wheel.6.state.enum` | `number` | — | Brake lining status for axle 1 wheel 6 | `AVL ID 13714` |
| 1013 | `trailer.brake.lining.axle.1.wheel.7.level` | `number` | `percentage` | Brake lining level for axle 1 wheel 7 | `AVL ID 13730` |
| 1014 | `trailer.brake.lining.axle.1.wheel.7.state.enum` | `number` | — | Brake lining status for axle 1 wheel 7 | `AVL ID 13715` |
| 1015 | `trailer.brake.lining.axle.1.wheel.8.level` | `number` | `percentage` | Brake lining level for axle 1 wheel 8 | `AVL ID 13731` |
| 1016 | `trailer.brake.lining.axle.1.wheel.8.state.enum` | `number` | — | Brake lining status for axle 1 wheel 8 | `AVL ID 13716` |
| 1017 | `trailer.brake.lining.axle.1.wheel.9.level` | `number` | `percentage` | Brake lining level for axle 1 wheel 9 | `AVL ID 13732` |
| 1018 | `trailer.brake.lining.axle.1.wheel.9.state.enum` | `number` | — | Brake lining status for axle 1 wheel 9 | `AVL ID 13717` |
| 1019 | `trailer.brake.lining.axle.2.wheel.10.level` | `number` | `percentage` | Brake lining level for axle 2 wheel 10 | `AVL ID 13738` |
| 1020 | `trailer.brake.lining.axle.2.wheel.10.state.enum` | `number` | — | Brake lining status for axle 2 wheel 10 | `AVL ID 13723` |
| 1021 | `trailer.brake.lining.axle.2.wheel.6.level` | `number` | `percentage` | Brake lining level for axle 2 wheel 6 | `AVL ID 13734` |
| 1022 | `trailer.brake.lining.axle.2.wheel.6.state.enum` | `number` | — | Brake lining status for axle 2 wheel 6 | `AVL ID 13719` |
| 1023 | `trailer.brake.lining.axle.2.wheel.7.level` | `number` | `percentage` | Brake lining level for axle 2 wheel 7 | `AVL ID 13735` |
| 1024 | `trailer.brake.lining.axle.2.wheel.7.state.enum` | `number` | — | Brake lining status for axle 2 wheel 7 | `AVL ID 13720` |
| 1025 | `trailer.brake.lining.axle.2.wheel.8.level` | `number` | `percentage` | Brake lining level for axle 2 wheel 8 | `AVL ID 13736` |
| 1026 | `trailer.brake.lining.axle.2.wheel.8.state.enum` | `number` | — | Brake lining status for axle 2 wheel 8 | `AVL ID 13721` |
| 1027 | `trailer.brake.lining.axle.2.wheel.9.level` | `number` | `percentage` | Brake lining level for axle 2 wheel 9 | `AVL ID 13737` |
| 1028 | `trailer.brake.lining.axle.2.wheel.9.state.enum` | `number` | — | Brake lining status for axle 2 wheel 9 | `AVL ID 13722` |
| 1029 | `trailer.brake.lining.axle.3.wheel.10.level` | `number` | `percentage` | Brake lining level for axle 3 wheel 10 | `AVL ID 13743` |
| 1030 | `trailer.brake.lining.axle.3.wheel.10.state.enum` | `number` | — | Brake lining status for axle 3 wheel 10 | `AVL ID 13728` |
| 1031 | `trailer.brake.lining.axle.3.wheel.6.level` | `number` | `percentage` | Brake lining level for axle 3 wheel 6 | `AVL ID 13739` |
| 1032 | `trailer.brake.lining.axle.3.wheel.6.state.enum` | `number` | — | Brake lining status for axle 3 wheel 6 | `AVL ID 13724` |
| 1033 | `trailer.brake.lining.axle.3.wheel.7.level` | `number` | `percentage` | Brake lining level for axle 3 wheel 7 | `AVL ID 13740` |
| 1034 | `trailer.brake.lining.axle.3.wheel.7.state.enum` | `number` | — | Brake lining status for axle 3 wheel 7 | `AVL ID 13725` |
| 1035 | `trailer.brake.lining.axle.3.wheel.8.level` | `number` | `percentage` | Brake lining level for axle 3 wheel 8 | `AVL ID 13741` |
| 1036 | `trailer.brake.lining.axle.3.wheel.8.state.enum` | `number` | — | Brake lining status for axle 3 wheel 8 | `AVL ID 13726` |
| 1037 | `trailer.brake.lining.axle.3.wheel.9.level` | `number` | `percentage` | Brake lining level for axle 3 wheel 9 | `AVL ID 13742` |
| 1038 | `trailer.brake.lining.axle.3.wheel.9.state.enum` | `number` | — | Brake lining status for axle 3 wheel 9 | `AVL ID 13727` |
| 1039 | `trailer.brake.temperature.axle.1.wheel` | `number` | `celsius` | Brake temperature for axle 1, indexed by wheel number | `AVL ID 13759...13763` |
| 1040 | `trailer.brake.temperature.axle.1.wheel.10.state.enum` | `number` | — | Brake temperature status for axle 1 wheel 10 | `AVL ID 13748` |
| 1041 | `trailer.brake.temperature.axle.1.wheel.6.state.enum` | `number` | — | Brake temperature status for axle 1 wheel 6 | `AVL ID 13744` |
| 1042 | `trailer.brake.temperature.axle.1.wheel.7.state.enum` | `number` | — | Brake temperature status for axle 1 wheel 7 | `AVL ID 13745` |
| 1043 | `trailer.brake.temperature.axle.1.wheel.8.state.enum` | `number` | — | Brake temperature status for axle 1 wheel 8 | `AVL ID 13746` |
| 1044 | `trailer.brake.temperature.axle.1.wheel.9.state.enum` | `number` | — | Brake temperature status for axle 1 wheel 9 | `AVL ID 13747` |
| 1045 | `trailer.brake.temperature.axle.2.wheel` | `number` | `celsius` | Brake temperature for axle 2, indexed by wheel number | `AVL ID 13764...13768` |
| 1046 | `trailer.brake.temperature.axle.2.wheel.10.state.enum` | `number` | — | Brake temperature status for axle 2 wheel 10 | `AVL ID 13753` |
| 1047 | `trailer.brake.temperature.axle.2.wheel.6.state.enum` | `number` | — | Brake temperature status for axle 2 wheel 6 | `AVL ID 13749` |
| 1048 | `trailer.brake.temperature.axle.2.wheel.7.state.enum` | `number` | — | Brake temperature status for axle 2 wheel 7 | `AVL ID 13750` |
| 1049 | `trailer.brake.temperature.axle.2.wheel.8.state.enum` | `number` | — | Brake temperature status for axle 2 wheel 8 | `AVL ID 13751` |
| 1050 | `trailer.brake.temperature.axle.2.wheel.9.state.enum` | `number` | — | Brake temperature status for axle 2 wheel 9 | `AVL ID 13752` |
| 1051 | `trailer.brake.temperature.axle.3.wheel` | `number` | `celsius` | Brake temperature for axle 3, indexed by wheel number | `AVL ID 13769...13773` |
| 1052 | `trailer.brake.temperature.axle.3.wheel.10.state.enum` | `number` | — | Brake temperature status for axle 3 wheel 10 | `AVL ID 13758` |
| 1053 | `trailer.brake.temperature.axle.3.wheel.6.state.enum` | `number` | — | Brake temperature status for axle 3 wheel 6 | `AVL ID 13754` |
| 1054 | `trailer.brake.temperature.axle.3.wheel.7.state.enum` | `number` | — | Brake temperature status for axle 3 wheel 7 | `AVL ID 13755` |
| 1055 | `trailer.brake.temperature.axle.3.wheel.8.state.enum` | `number` | — | Brake temperature status for axle 3 wheel 8 | `AVL ID 13756` |
| 1056 | `trailer.brake.temperature.axle.3.wheel.9.state.enum` | `number` | — | Brake temperature status for axle 3 wheel 9 | `AVL ID 13757` |
| 1057 | `trailer.braking.cylinder.pressure.axle.1.left` | `number` | `kPa` | Braking cylinder pressure for axle 1 left side | `AVL ID 13665` |
| 1058 | `trailer.braking.cylinder.pressure.axle.1.right` | `number` | `kPa` | Braking cylinder pressure for axle 1 right side | `AVL ID 13666` |
| 1059 | `trailer.braking.cylinder.pressure.axle.2.left` | `number` | `kPa` | Braking cylinder pressure for axle 2 left side | `AVL ID 13667` |
| 1060 | `trailer.braking.cylinder.pressure.axle.2.right` | `number` | `kPa` | Braking cylinder pressure for axle 2 right side | `AVL ID 13668` |
| 1061 | `trailer.braking.cylinder.pressure.axle.3.left` | `number` | `kPa` | Braking cylinder pressure for axle 3 left side | `AVL ID 13669` |
| 1062 | `trailer.braking.cylinder.pressure.axle.3.right` | `number` | `kPa` | Braking cylinder pressure for axle 3 right side | `AVL ID 13670` |
| 1063 | `trailer.braking.electric.control.line.support.state.enum` | `number` | — | Braking via electric control line support status | `AVL ID 13677` |
| 1064 | `trailer.calibration.load.level.state.enum` | `number` | — | Calibration load level status | `AVL ID 13664` |
| 1065 | `trailer.ebs.vehicle.speed` | `number` | `km/h` | Vehicle speed from EBS (Electronic Braking System) | `AVL ID 13652` |
| 1066 | `trailer.electric.load.proportional.function.installation.state.enum` | `number` | — | Electrical load proportional function installation status | `AVL ID 13808` |
| 1067 | `trailer.electric.supply.non.braking.systems.state.enum` | `number` | — | Electrical supply of non-braking systems status | `AVL ID 13806` |
| 1068 | `trailer.lateral.acceleration` | `number` | `m/s^2` | Trailers Lateral acceleration | `AVL ID 13673` |
| 1069 | `trailer.lift.axle.1.position.state.enum` | `number` | — | Lift axle 1 position status | `AVL ID 13681` |
| 1070 | `trailer.lift.axle.2.position.state.enum` | `number` | — | Lift axle 2 position status | `AVL ID 13682` |
| 1071 | `trailer.loading.ramp.approach.assistance.state.enum` | `number` | — | Loading ramp approach assistance status | `AVL ID 13674` |
| 1072 | `trailer.pneumatic.supply.pressure` | `number` | `kPa` | Trailer pneumatic supply pressure | `AVL ID 13810` |
| 1073 | `trailer.pneumatic.supply.state.enum` | `number` | — | Vehicle pneumatic supply status | `AVL ID 13774` |
| 1074 | `trailer.power.state.enum` | `number` | — | Vehicle electrical supply status | `AVL ID 13660` |
| 1075 | `trailer.red.warning.request.state.enum` | `number` | — | Red warning request status | `AVL ID 13655` |
| 1076 | `trailer.retarder.control.state.enum` | `number` | — | Retarder control status | `AVL ID 13654` |
| 1077 | `trailer.retarder.wheel.torque.load` | `number` | `percentage` | Retarder wheel torque | `AVL ID 13658` |
| 1078 | `trailer.rop.system.state.enum` | `number` | — | ROP (roll over protection) system status | `AVL ID 13678` |
| 1079 | `trailer.scale.axle.load` | `number` | `kg` | Scale axle load measurement | `AVL ID 13663` |
| 1080 | `trailer.spring.brake.installation.state.enum` | `number` | — | Spring brake installation status | `AVL ID 13807` |
| 1081 | `trailer.spring.brake.state.enum` | `number` | — | Spring brake status | `AVL ID 13809` |
| 1082 | `trailer.steering.axle.locking.state.enum` | `number` | — | Steering axle locking status | `AVL ID 13683` |
| 1083 | `trailer.stop.lamps.request.state.enum` | `number` | — | Stop lamps request status | `AVL ID 13676` |
| 1084 | `trailer.supply.line.braking.state.enum` | `number` | — | Supply line braking status | `AVL ID 13675` |
| 1085 | `trailer.tire.air.leakage.rate.axle.1.wheel` | `number` | — | Tire air leakage rate for axle 1, indexed by wheel number, Pa/sec | `AVL ID 13775...13779` |
| 1086 | `trailer.tire.air.leakage.rate.axle.2.wheel` | `number` | — | Tire air leakage rate for axle 2, indexed by wheel number, Pa/sec | `AVL ID 13780...13784` |
| 1087 | `trailer.tire.air.leakage.rate.axle.3.wheel` | `number` | — | Tire air leakage rate for axle 3, indexed by wheel number, Pa/sec | `AVL ID 13785...13789` |
| 1088 | `trailer.tire.pressure.axle.1.wheel` | `number` | `kPa` | Tire pressure for axle 1, indexed by wheel number | `AVL ID 13699...13703` |
| 1089 | `trailer.tire.pressure.axle.2.wheel` | `number` | `kPa` | Tire pressure for axle 2, indexed by wheel number | `AVL ID 13704...13708` |
| 1090 | `trailer.tire.pressure.axle.3.wheel` | `number` | `kPa` | Tire pressure for axle 3, indexed by wheel number | `AVL ID 13709...13713` |
| 1091 | `trailer.tire.pressure.state.axle.1.wheel.10.tire.enum` | `number` | — | Tire pressure status for axle 1 wheel 10 | `AVL ID 13688` |
| 1092 | `trailer.tire.pressure.state.axle.1.wheel.6.tire.enum` | `number` | — | Tire pressure status for axle 1 wheel 6 | `AVL ID 13684` |
| 1093 | `trailer.tire.pressure.state.axle.1.wheel.7.tire.enum` | `number` | — | Tire pressure status for axle 1 wheel 7 | `AVL ID 13685` |
| 1094 | `trailer.tire.pressure.state.axle.1.wheel.8.tire.enum` | `number` | — | Tire pressure status for axle 1 wheel 8 | `AVL ID 13686` |
| 1095 | `trailer.tire.pressure.state.axle.1.wheel.9.tire.enum` | `number` | — | Tire pressure status for axle 1 wheel 9 | `AVL ID 13687` |
| 1096 | `trailer.tire.pressure.state.axle.2.wheel.10.tire.enum` | `number` | — | Tire pressure status for axle 2 wheel 10 | `AVL ID 13693` |
| 1097 | `trailer.tire.pressure.state.axle.2.wheel.6.tire.enum` | `number` | — | Tire pressure status for axle 2 wheel 6 | `AVL ID 13689` |
| 1098 | `trailer.tire.pressure.state.axle.2.wheel.7.tire.enum` | `number` | — | Tire pressure status for axle 2 wheel 7 | `AVL ID 13690` |
| 1099 | `trailer.tire.pressure.state.axle.2.wheel.8.tire.enum` | `number` | — | Tire pressure status for axle 2 wheel 8 | `AVL ID 13691` |
| 1100 | `trailer.tire.pressure.state.axle.2.wheel.9.tire.enum` | `number` | — | Tire pressure status for axle 2 wheel 9 | `AVL ID 13692` |
| 1101 | `trailer.tire.pressure.state.axle.3.wheel.10.tire.enum` | `number` | — | Tire pressure status for axle 3 wheel 10 | `AVL ID 13698` |
| 1102 | `trailer.tire.pressure.state.axle.3.wheel.6.tire.enum` | `number` | — | Tire pressure status for axle 3 wheel 6 | `AVL ID 13694` |
| 1103 | `trailer.tire.pressure.state.axle.3.wheel.7.tire.enum` | `number` | — | Tire pressure status for axle 3 wheel 7 | `AVL ID 13695` |
| 1104 | `trailer.tire.pressure.state.axle.3.wheel.8.tire.enum` | `number` | — | Tire pressure status for axle 3 wheel 8 | `AVL ID 13696` |
| 1105 | `trailer.tire.pressure.state.axle.3.wheel.9.tire.enum` | `number` | — | Tire pressure status for axle 3 wheel 9 | `AVL ID 13697` |
| 1106 | `trailer.tire.temperature.axle.1.wheel` | `number` | `celsius` | Tire temperature for axle 1, indexed by wheel number | `AVL ID 13790...13794` |
| 1107 | `trailer.tire.temperature.axle.2.wheel` | `number` | `celsius` | Tire temperature for axle 2, indexed by wheel number | `AVL ID 13795...13799` |
| 1108 | `trailer.tire.temperature.axle.3.wheel` | `number` | `celsius` | Tire temperature for axle 3, indexed by wheel number | `AVL ID 13800...13804` |
| 1109 | `trailer.towing.state.enum` | `number` | — | Towed vehicle detection status | `AVL ID 13651` |
| 1110 | `trailer.towing.vehicle.axle.load` | `number` | `kg` | Towed vehicle axle load | `AVL ID 13662` |
| 1111 | `trailer.traction.help.state.enum` | `number` | — | Traction help system status | `AVL ID 13680` |
| 1112 | `trailer.vdc.active.state.enum` | `number` | — | VDC (vehicle dynamic control) active status | `AVL ID 13672` |
| 1113 | `trailer.vehicle.service.brake.state.enum` | `number` | — | Vehicle service brake status | `AVL ID 13659` |
| 1114 | `trailer.vehicle.type.enum` | `number` | — | Vehicle type classification | `AVL ID 13661` |
| 1115 | `trailer.yc.system.state.enum` | `number` | — | YC (Yaw Control) system status | `AVL ID 13679` |
| 1116 | `trip.average.speed` | `number` | `km/h` | Average speed of the trip | `AVL ID 369` |
| 1117 | `trip.driving.time` | `number` | `seconds` | Single riding time | `AVL ID 361` |
| 1118 | `trip.mileage` | `number` | `km` | Distance driven since engine start | `AVL ID 834` |
| 1119 | `trip.operate.time` | `number` | `seconds` | Single operation time | `AVL ID 360` |
| 1120 | `trip.state.enum` | `number` | — | Trip status | `AVL ID 250` |
| 1121 | `trip.status` | `boolean` | — | Trip status, true if trip started, false - if stopped | `AVL ID 250` |
| 1122 | `ultrasonic.fuel.level` | `number` | `mm` | Indexed parameter for ultrasonic fuel level | `AVL ID 224, , AVL ID 225, , AVL ID 327` |
| 1123 | `ultrasonic.software.state` | `string` | — | The ultrasonic fuel sensor status as a 2-character code (Software code followed by Hardware code), each character '0' meaning Normal | `AVL ID 483` |
| 1124 | `ultrasonic.software.state.enum` | `number` | — | Indexed parameter showing Ultrasonic Fuel sensor software status. 0 - Normal, 1 - The system has just started, output measurement value, 2 - Gas delay count, 3 - The measured value is invalid, 4 - The stationary state, 5 - No data received for 50-60 seconds, 9 - sudden drop, 10 - sudden rise, 11 - delay time of the sudden drop, 12 - delay time of the sudden rise, 13 - The stationary state, maintain the liquid level height value outputu changed, 15 - sudden drop/rise on an tilt | `AVL ID 208, , AVL ID 209, , AVL ID 483` |
| 1125 | `user.id` | `string` | — | User ID | `AVL ID 854` |
| 1126 | `vehicle.mileage` | `number` | `km` | Total calculated mileage | `AVL ID 16, , AVL ID 216, , AVL ID 356, , AVL ID 833` |
| 1127 | `vehicle.registration.number` | `string` | — | Vehicle registration number | `AVL ID 10158, , AVL ID 231, , AVL ID 232` |
| 1128 | `vehicle.vin` | `string` | — | VIN of vehicle | `AVL ID 10157, , AVL ID 233, , AVL ID 234, , AVL ID 235, , AVL ID 256, , AVL ID 325` |
| 1129 | `wifi.mac.address` | `string` | — | WiFi MAC address | `AVL ID 25036...25041` |
| 1130 | `wifi.signal.strength` | `number` | — | WiFi signal strength, RSSI | `AVL ID 25036...25041` |
| 1131 | `x.acceleration` | `number` | `g` | Accelerometer value X | `AVL ID 17, , AVL ID 236` |
| 1132 | `y.acceleration` | `number` | `g` | Accelerometer value Y | `AVL ID 18, , AVL ID 237` |
| 1133 | `z.acceleration` | `number` | `g` | Accelerometer value Z | `AVL ID 19, , AVL ID 238` |

---

## 2. Official Flespi Device Configuration Settings for Teltonika FMC650 (69 Settings)

These 69 settings represent the complete set of official Flespi Device Settings defined under the **Settings** tab on [`https://flespi.com/devices/teltonika-fmc650`](https://flespi.com/devices/teltonika-fmc650). For their exact mapping to Teltonika `.cfg` Configuration `ParameterId`s in `re/fmx65_03.01.01.Rev.15_schema.json`, see [`FMC650_to_Flespi_Configuration_and_Telemetry_Mappings.md`](./FMC650_to_Flespi_Configuration_and_Telemetry_Mappings.md).

| # | Flespi Setting Name (`key`) | Official Flespi Title | Official Flespi Description | Official Flespi Sub-Properties (`key`: Label) |
|---:|---|---|---|---|
| 1 | `accelerometer_calibration` | **Accelerometer auto calibration** | — | **enable**: Enable |
| 2 | `analog_input1_io` | **Analog Input 1 I/O** | Analog input 1 I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 3 | `axis_x` | **Axis X** | Axis X parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 4 | `axis_y` | **Axis Y** | Axis Y parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 5 | `axis_z` | **Axis Z** | Axis Z parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 6 | `backup_server_fmb640` | **Secondary GPRS Server Setup** | — | **host**: Host, **mode**: Secondary GPRS server mode, **port**: Port, **protocol**: Secondary GPRS server protocol |
| 7 | `battery_charge_mode` | **Battery charge mode** | — | **mode**: Mode |
| 8 | `battery_level_io` | **Battery level** | Battery level I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 9 | `battery_voltage_io` | **Battery voltage** | Battery voltage I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 10 | `camera_features_dashcam_com1` | **COM1 - Camera features** | — | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority |
| 11 | `camera_features_dashcam_com2` | **COM2 - Camera features** | — | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority |
| 12 | `camera_features_dualcam_com1` | **COM1 - Camera features** | — | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority |
| 13 | `camera_features_dualcam_com2` | **COM2 - Camera features** | — | **osd**: OSD Display, **timezone**: Camera Time Zone, **frame_rate**: Video Frame Rate, **resolution**: Camera Picture Resolution, **compression**: Camera Picture Compression, **transfer_priority**: File Transfer Priority |
| 14 | `camera_image_dashcam_com1` | **COM1 - Image settings** | — | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger |
| 15 | `camera_image_dashcam_com2` | **COM2 - Image settings** | — | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger |
| 16 | `camera_image_dualcam_com1` | **COM1 - Image settings** | — | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger |
| 17 | `camera_image_dualcam_com2` | **COM2 - Image settings** | — | **periodic**: Periodic Image Sending, **triggers**: Image Sending Trigger |
| 18 | `camera_scenario_mode_dashcam_com1` | **COM1 - Scenario mode** | — | **mode**: Mode |
| 19 | `camera_scenario_mode_dashcam_com2` | **COM2 - Scenario mode** | — | **mode**: Mode |
| 20 | `camera_scenario_mode_dualcam_com1` | **COM1 - Scenario mode** | — | **mode**: Mode |
| 21 | `camera_scenario_mode_dualcam_com2` | **COM2 - Scenario mode** | — | **mode**: Mode |
| 22 | `camera_video_dashcam_com1` | **COM1 - Video settings** | — | **sources**: Video Sources, **duration**: Video Duration |
| 23 | `camera_video_dashcam_com2` | **COM2 - Video settings** | — | **sources**: Video Sources, **duration**: Video Duration |
| 24 | `camera_video_dualcam_com1` | **COM1 - Video settings** | — | **sources**: Video Sources, **duration**: Video Duration |
| 25 | `camera_video_dualcam_com2` | **COM2 - Video settings** | — | **sources**: Video Sources, **duration**: Video Duration |
| 26 | `cpureset` | **Restart (reboot) the device** | — | — |
| 27 | `data_codec` | **Data codec to use for data transmission** | — | **codec**: Data codec |
| 28 | `deleterecords` | **Delete all stored records** | Send deleterecords command to the device. It will erase all AVL records from internal FLASH memory | — |
| 29 | `external_voltage_io` | **External voltage** | External voltage I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 30 | `getgps` | **Request current GPS data, date and time.** | Send getgps command to the device. The response will be stored as telemetry message | — |
| 31 | `getimeiccid` | **Send getimeiccid command** | — | — |
| 32 | `getrecord` | **Force device to generate a report** | — | — |
| 33 | `getver` | **getver command response** | Readonly settings to check device firmware and hardware info | **id**: Device configuration ID, **imei**: IMEI, **modem**: Modem version, **hardware_model**: Hardware model, **firmware_version**: Firmware version, **bootloader_version**: Bootloader version |
| 34 | `gnss_source` | **GNSS Source** | — | **mode**: Mode |
| 35 | `gprs` | **GPRS Setup** | Setup sending data by GPRS link. Note: after changing this setting device will be disconnected from current server. | **apn**: APN Name, **enabled**: GPRS Enabled, **password**: APN Password, **username**: APN Username |
| 36 | `gprs_server` | **GPRS Server Setup** | Setup server to send data by GPRS link. Note: after changing this setting device will be disconnected from current server. | **host**: Host, **port**: Port, **protocol**: Server protocol |
| 37 | `green_driving` | **Green Driving** | Green driving scenario settings | **prio**: Priority, **output**: Output Control, **source**: Source, **duration**: Duration, **max_accel**: Max Acceleration, **max_angle**: Max Angle, **max_brake**: Max Braking, **eco_maximum**: Eco Driving Maximum, **advanced_eco**: Advanced Eco Driving, **cornering_duration**: Cornering Active Output Duration |
| 38 | `home_network` | **Home GSM Network Settings** | Data acquisition parameters for home GSM network. | **on_move**: Vehicle Moving, **on_stop**: Vehicle On Stop |
| 39 | `idling_dout3` | **Excessive Idling Detection** | Excessive idling detection scenario settings | **prio**: Priority, **output**: Output Control, **record**: Eventual Records, **move_time**: Move Timeout, **stop_time**: Stop Timeout |
| 40 | `ignition_detection` | **Ignition Detection Source** | Ignition source is configurable and used to determine vehicle ignition status. Ignition status is used in power management and the following functionalities: eco driving, excessive idling, fuel consumption, over speeding, towing and trip. If multiple sources are needed - enable desired combination of sources. | **din1**: DIN1, **din2**: DIN2, **din3**: DIN3, **din4**: DIN4, **ign_mov**: Movement, **ign_volt**: Power Voltage |
| 41 | `inputs1_io` | **Digital Input 1 I/O** | Digital input I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 42 | `inputs2_io` | **Digital Input 2** | Digital input I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 43 | `inputs3_io` | **Digital Input 3** | Digital input I/O parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 44 | `inputs4_io` | **Digital Input 4** | Digital input 4 parameters settings | **avg**: Average, **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 45 | `io_global_send_mode` | **IO Global Send Mode** | In IO Global settings a user can set IO value if I/O is not present for 30 seconds. Note: This setting only affects CAN/FMS IO IDs. | **mode**: Mode |
| 46 | `manual_can` | **Experimental. Manual CAN parameters setup.** | Experimental command to work with manual CAN parameters. 2 modes: request mode gets specified values from the device, current value mode allows to set up new values. | **config**: Command mode, **can_number**: CAN number |
| 47 | `manual_can_command` | **Experimental. Manual CAN command parameters setup.** | Experimental command to work with manual CAN command parameters. 2 modes: request mode gets specified values from the device, current value mode allows to set up new values. | **config**: Command mode, **command_number**: Command number |
| 48 | `manual_can_request` | **Manual CAN Request parameters setup.** | Manual CAN Request parameters setup. 2 modes: request mode gets specified values from the device, current value mode allows to set up new values. | **config**: Command mode, **can_number**: CAN number |
| 49 | `mcan_cmd` | **Trigger Manual CAN Command** | Trigger a configured Manual CAN Command slot. Optionally override CAN ID and data payload. | **data**: Data override, **can_id**: CAN ID override, **slot_id**: Slot ID |
| 50 | `mcan_stop` | **Stop periodic Manual CAN Command** | Stop a periodic Manual CAN Command slot. | **slot_id**: Slot ID |
| 51 | `network_ping_640` | **Network Ping** | Set up network ping with a certain timeout to prevent link close by the operator. | **timeout**: Timeout |
| 52 | `odometer_io` | **Odometer** | Enable odometer | **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 53 | `odoset` | **Set total odometer value** | Send odoset/odoget commands | **value**: Odometer value |
| 54 | `outputs` | **Digital Outputs** | Change state of digital outputs 1 - 4 | **out1**: Output 1, **out2**: Output 2, **out3**: Output 3, **out4**: Output 4 |
| 55 | `overspeeding_dout4` | **Overspeeding** | Overspeeding scenario settings | **prio**: Priority, **output**: Output Control, **max_speed**: Max Speed |
| 56 | `records_params` | **Records Parameters** | Records sending parameters setup. | **order**: Records Sorting Order, **online**: Open Link Timeout, **response**: Server Response Timeout |
| 57 | `roaming_network` | **Roaming GSM Network Settings** | Data acquisition parameters for roaming GSM network. | **on_move**: Vehicle Moving, **on_stop**: Vehicle On Stop |
| 58 | `sdformat` | **Format SD card** | Send sdformat command to the device. It will clear all undelivered telemetry reports | — |
| 59 | `setdigout_4` | **Action command setdigout** | Send setdigout command to control digital outputs 1 - 4 with timeout and speed limit options | **out1**: State of digital output 1, **out2**: State of digital output 2, **out3**: State of digital output 3, **out4**: State of digital output 4 |
| 60 | `sleep_mode` | **Sleep Mode** | Device power saving mode setup. In sleep mode module reduces level of power consumption by turning GPS module to sleep. In deep sleep mode module turns GPS module to sleep and device is deregistered from GSM network (device do not receive SMS in deep sleep). In Online Deep Sleep mode device works as in Deep Sleep mode, but without deregistering from GSM network. In Ultra Deep Sleep mode device turn off GPS and GSM modem and suspend functions for maximum battery saving | **mode**: Sleep Mode |
| 61 | `static_filter` | **Static Navigation** | Static Navigation Mode is a filter, which filters out track jumps when the object is not moving. | **stat_nav**: Static Navigation |
| 62 | `tachocheck` | **Checking the tachograph configuration** | Readonly settings to check the tachograph configuration | **addr**: Addr, **baud**: Baud, **ignition**: Ignition, **fms_on_bus**: [ABCD] FMS data presence on the bus, **tacho_on_bus**: [T] Tachograph presence on the bus, **k_line_on_bus**: [K] K-Line data presence on the bus, **close_last_auth**: [C] Response to close last authentication session validity check, **remote_session_validity**: [R] Response to open remote session validity check |
| 63 | `tacho_download_source` | **Tachograph DDD download source** | — | **value**: Value |
| 64 | `tacho_ignition_source` | **Tachograph ignition source** | — | **value**: Value |
| 65 | `tacho_web` | **Tacho WEB settings** | Remote server address for automatic connection according to specified parameters. | **config**: Command mode |
| 66 | `tls` | **Enable connection over TLS** | — | **enable**: TLS enable |
| 67 | `trip_odometer_io` | **Trip Odometer** | — | **low**: Low Level, **high**: High Level, **prio**: Priority, **event**: Event Only, **operand**: Operand |
| 68 | `unknown_network` | **Unknown GSM Network Settings** | Data acquisition parameters for unknown GSM network. | **on_move**: Vehicle Moving, **on_stop**: Vehicle On Stop |
| 69 | `web_connect` | **Connect to Fota WEB immediately.** | — | — |

---

## 3. Official Flespi Device Commands for Teltonika FMC650 (10 Commands)

These 10 commands represent the complete set of official Flespi Device Commands defined under the **Commands** tab on [`https://flespi.com/devices/teltonika-fmc650`](https://flespi.com/devices/teltonika-fmc650). In particular, `getparam`, `setparam`, and `setio` are the official Flespi mechanisms for reading and writing the >11,400 FMC650 Configuration `ParameterId`s in `re/fmx65_03.01.01.Rev.15_schema.json` that do not have a dedicated Flespi setting in Section 2.

| # | Flespi Command Name (`key`) | Official Flespi Title | Official Flespi Description | Official Flespi Properties | Official Examples |
|---:|---|---|---|---|---|
| 1 | `bluetooth` | **Forward packet to paired Bluetooth device** | Send custom command to forward packet to paired bluetooth device | — | Send custom bytes to paired Bluetooth device as codec 12 command `{"hex":"DEADBEEF"}` \| Send custom string to paired Bluetooth device as codec 12 command `{"text":"ASCII command to paired Bluetooth device"}` |
| 2 | `custom` | **Custom command** | Send custom command via connection or over SMS | — | Force device to generate a record and connect to server to deliver it `{"text":"getrecord"}` \| Send custom bytes to device as codec 12 command. May be used to communicate with external equipment connected over serial port `{"hex":"DEADBEEF"}` |
| 3 | `garmin` | **Forward packet meant for Garmin system** | Send custom command to forward packet to Garmin device | — | Send custom bytes to Garmin system as codec 12 command `{"hex":"DEADBEEF"}` \| Send custom string to Garmin system as codec 12 command `{"text":"ASCII command to Garmin"}` |
| 4 | `getparam` | **Get configuration param** | Get configuration parameter by its number | **param**: Param number | — |
| 5 | `request_tachograph_file` | **Request tachograph file** | Request tachograph file from tachograph | — | — |
| 6 | `request_video` | **Request video** | Request video file upload from device | **from**: Time from, **channel**: Camera channel, **duration**: Duration | — |
| 7 | `serial_port` | **Forward packet to external device via serial port** | Send custom command to forward packet to external device via uart using RS232/RS485 | — | Send custom bytes to device as codec 12 command. Used to communicate with external equipment connected over serial port `{"hex":"DEADBEEF"}` |
| 8 | `setio` | **Set IO param** | Set IO parameter by its priority id | **id**: Param ID of Priority, **low**: Low level, **high**: High level, **event**: Event Only, **average**: Average, **operand**: Operand, **priority**: Priority | Setup Speed input to generate an event when the speed exceeds a high level of 60km/h. The event should have panic priority and should only be added to eventual records. `{"id":50090,"low":0,"high":60,"event":1,"operand":0,"priority":3}` \| Setup Battery voltage input to generate an event when the voltage leaves the range from 2500mv to 3300mv. The event should have a low priority and should be added to every AVL record. `{"id":50120,"low":2500,"high":3300,"event":0,"operand":2,"priority":1}` |
| 9 | `setparam` | **Set configuration param** | Set configuration parameter by its number | **param**: Param number, **value**: Param value | — |
| 10 | `take_photo` | **Take a photo** | Take a photo | **channel**: Camera channel | — |
