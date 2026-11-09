# Complete 1,161 Official Flespi Parameters to Wialon Mapping Reference (`Teltonika FMC650`)

This reference maps all **1,161 official Flespi telemetry parameters** registered for the **`teltonika-fmc650`** device type (`https://flespi.com/devices/teltonika-fmc650` & `https://flespi.com/protocols/teltonika`) to:
1. **Official Flespi Telemetry Parameter Name** (dotted notation).
2. **Flespi Data Type & Physical Unit**.
3. **Teltonika Telemetry `AVL ID`(s)** (extracted from Flespi's official `AVL_ID:` parameter descriptions).
4. **Wialon Parameter Key via Flespi Stream (`Path A`)** â€” the exact parameter name received by Wialon when streamed from Flespi (`wialon` / `wialon_retranslator` stream).
5. **Wialon Parameter Key via Direct Teltonika Connection (`Path B`)** â€” the `io_<AVL_ID>` key received by Wialon when the FMC650 connects directly to Wialon without Flespi.
6. **Usage in `FMC650_TEST_TR84_UNIT_PROFILE.wlp`** â€” links directly to the sensor ID(s) in `FMC650_TEST_TR84_UNIT_PROFILE.wlp` where configured.

---

| # | Official Flespi Parameter | Type | Unit | Teltonika Telemetry `AVL ID`(s) | Wialon Key via Flespi Stream (Path A) | Wialon Key Direct (Path B) | Used in `FMC650_TEST_TR84_UNIT_PROFILE.wlp` | Official Description |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `absolute.acceleration` | `number` | `â€”` | `23`, `254` | `absolute_accel` | `io_23`, `io_254` | Sensor `51` (VALEUR DE GREEN DRIVING) | Module of accelerometer vector |
| 2 | `acceleration.array` | `array` | `â€”` | `257` | `accel_array` | `io_257` | â€” | Array of objects with acceleration data by x, y, and z axis |
| 3 | `accelerometer.calibration.quality.level` | `number` | `â€”` | `1440` | `accelerometer_calibration_quality_lvl` | `io_1440` | â€” | Accelerometer calibration quality |
| 4 | `accelerometer.calibration.side.vector.delta` | `number` | `â€”` | `1437` | `accelerometer_calibration_side_vector_delta` | `io_1437` | â€” | Angle between the calculated accelerometer calibration and the actual device mounting position |
| 5 | `accelerometer.calibration.state` | `number` | `â€”` | `383` | `accelerometer_calibration_st` | `io_383` | â€” | Accelerometer calibration state |
| 6 | `activity.state` | `number` | `â€”` | `395` | `activity_st` | `io_395` | â€” | Device activity state |
| 7 | `actual.remaining.mileage` | `number` | `â€”` | `353` | `actual_remaining_mileage` | `io_353` | â€” | Actual remaining mileage |
| 8 | `adas.ahead.object.distance` | `number` | `â€”` | `12961`, `617` | `adas_ahead_object_dist` | `io_12961`, `io_617` | â€” | Distance to the object ahead reported by ADAS. Indexed by camera COM port. |
| 9 | `adas.ahead.object.speed` | `number` | `â€”` | `12962`, `618` | `adas_ahead_object_speed` | `io_12962`, `io_618` | â€” | Speed of the object ahead reported by ADAS. Indexed by camera COM port. |
| 10 | `adas.brake.signal.status` | `boolean` | `â€”` | `12947`, `603` | `adas_brake_signal_stat` | `io_12947`, `io_603` | â€” | Brake signal status reported by ADAS. Indexed by camera COM port. |
| 11 | `adas.camera.state` | `string` | `â€”` | `12967`, `666` | `adas_camera_st` | `io_12967`, `io_666` | â€” | ADAS camera operating state. Indexed by camera COM port. |
| 12 | `adas.camera.state.enum` | `number` | `â€”` | `12967`, `666` | `adas_camera_st_enum` | `io_12967`, `io_666` | â€” | ADAS camera operating state. Numeric representation. Indexed by camera COM port. |
| 13 | `adas.collision.warning.state` | `string` | `â€”` | `12957`, `613` | `adas_collision_warning_st` | `io_12957`, `io_613` | â€” | ADAS front collision warning state. Indexed by camera COM port. |
| 14 | `adas.collision.warning.state.enum` | `number` | `â€”` | `12957`, `613` | `adas_collision_warning_st_enum` | `io_12957`, `io_613` | â€” | ADAS front collision warning state. Numeric representation. Indexed by camera COM port. |
| 15 | `adas.distance.state` | `string` | `â€”` | `12954`, `610` | `adas_dist_st` | `io_12954`, `io_610` | â€” | ADAS safety distance alert state. Indexed by camera COM port. |
| 16 | `adas.distance.state.enum` | `number` | `â€”` | `12954`, `610` | `adas_dist_st_enum` | `io_12954`, `io_610` | â€” | ADAS safety distance alert state. Numeric representation. Indexed by camera COM port. |
| 17 | `adas.engine.rpm` | `number` | `â€”` | `12948`, `604` | `adas_eng_rpm` | `io_12948`, `io_604` | â€” | Engine speed reported by ADAS. Indexed by camera COM port. |
| 18 | `adas.error.state` | `string` | `â€”` | `12960`, `616` | `adas_error_st` | `io_12960`, `io_616` | â€” | ADAS camera error state. Indexed by camera COM port. |
| 19 | `adas.error.state.enum` | `number` | `â€”` | `12960`, `616` | `adas_error_st_enum` | `io_12960`, `io_616` | â€” | ADAS camera error state. Numeric representation. Indexed by camera COM port. |
| 20 | `adas.front.vehicle.start.state` | `string` | `â€”` | `12955`, `611` | `adas_front_vhc_start_st` | `io_12955`, `io_611` | â€” | ADAS front vehicle start alarm state. Indexed by camera COM port. |
| 21 | `adas.front.vehicle.start.state.enum` | `number` | `â€”` | `12955`, `611` | `adas_front_vhc_start_st_enum` | `io_12955`, `io_611` | â€” | ADAS front vehicle start alarm state. Numeric representation. Indexed by camera COM port. |
| 22 | `adas.lane.departure.left.state` | `string` | `â€”` | `12949`, `605` | `adas_lane_departure_left_st` | `io_12949`, `io_605` | â€” | ADAS left lane departure warning state. Indexed by camera COM port. |
| 23 | `adas.lane.departure.left.state.enum` | `number` | `â€”` | `12949`, `605` | `adas_lane_departure_left_st_enum` | `io_12949`, `io_605` | â€” | ADAS left lane departure warning state. Numeric representation. Indexed by camera COM port. |
| 24 | `adas.lane.departure.right.state` | `string` | `â€”` | `12950`, `606` | `adas_lane_departure_right_st` | `io_12950`, `io_606` | â€” | ADAS right lane departure warning state. Indexed by camera COM port. |
| 25 | `adas.lane.departure.right.state.enum` | `number` | `â€”` | `12950`, `606` | `adas_lane_departure_right_st_enum` | `io_12950`, `io_606` | â€” | ADAS right lane departure warning state. Numeric representation. Indexed by camera COM port. |
| 26 | `adas.lane.left.distance` | `number` | `â€”` | `12951`, `607` | `adas_lane_left_dist` | `io_12951`, `io_607` | â€” | Distance to the left lane line reported by ADAS. Indexed by camera COM port. |
| 27 | `adas.lane.right.distance` | `number` | `â€”` | `12952`, `608` | `adas_lane_right_dist` | `io_12952`, `io_608` | â€” | Distance to the right lane line reported by ADAS. Indexed by camera COM port. |
| 28 | `adas.left.turn.signal.status` | `boolean` | `â€”` | `12945`, `601` | `adas_left_turn_signal_stat` | `io_12945`, `io_601` | â€” | Left turn signal status reported by ADAS. Indexed by camera COM port. |
| 29 | `adas.pedestrian.state` | `string` | `â€”` | `12958`, `614` | `adas_pedestrian_st` | `io_12958`, `io_614` | â€” | ADAS pedestrian collision warning state. Indexed by camera COM port. |
| 30 | `adas.pedestrian.state.enum` | `number` | `â€”` | `12958`, `614` | `adas_pedestrian_st_enum` | `io_12958`, `io_614` | â€” | ADAS pedestrian collision warning state. Numeric representation. Indexed by camera COM port. |
| 31 | `adas.proximity.state` | `string` | `â€”` | `12956`, `612` | `adas_proximity_st` | `io_12956`, `io_612` | â€” | ADAS front proximity warning state. Indexed by camera COM port. |
| 32 | `adas.proximity.state.enum` | `number` | `â€”` | `12956`, `612` | `adas_proximity_st_enum` | `io_12956`, `io_612` | â€” | ADAS front proximity warning state. Numeric representation. Indexed by camera COM port. |
| 33 | `adas.recording.state` | `string` | `â€”` | `12959`, `615` | `adas_recording_st` | `io_12959`, `io_615` | â€” | ADAS recording and microphone state. Indexed by camera COM port. |
| 34 | `adas.recording.state.enum` | `number` | `â€”` | `12959`, `615` | `adas_recording_st_enum` | `io_12959`, `io_615` | â€” | ADAS recording and microphone state. Numeric representation. Indexed by camera COM port. |
| 35 | `adas.right.turn.signal.status` | `boolean` | `â€”` | `12946`, `602` | `adas_right_turn_signal_stat` | `io_12946`, `io_602` | â€” | Right turn signal status reported by ADAS. Indexed by camera COM port. |
| 36 | `adas.sdcard.state` | `string` | `â€”` | `12966`, `665` | `adas_sdcard_st` | `io_12966`, `io_665` | â€” | ADAS camera SD card state. Indexed by camera COM port. |
| 37 | `adas.sdcard.state.enum` | `number` | `â€”` | `12966`, `665` | `adas_sdcard_st_enum` | `io_12966`, `io_665` | â€” | ADAS camera SD card state. Numeric representation. Indexed by camera COM port. |
| 38 | `adas.speed` | `number` | `â€”` | `12944`, `600` | `adas_speed` | `io_12944`, `io_600` | â€” | Vehicle speed reported by ADAS. Indexed by camera COM port. |
| 39 | `adas.speed.limit` | `number` | `â€”` | `12964`, `620` | `adas_speed_limit` | `io_12964`, `io_620` | â€” | Speed limit recognized by ADAS. Indexed by camera COM port. |
| 40 | `adas.speed.limit.recognition.state` | `string` | `â€”` | `12963`, `619` | `adas_speed_limit_recognition_st` | `io_12963`, `io_619` | â€” | ADAS speed limit recognition state. Indexed by camera COM port. |
| 41 | `adas.speed.limit.recognition.state.enum` | `number` | `â€”` | `12963`, `619` | `adas_speed_limit_recognition_st_enum` | `io_12963`, `io_619` | â€” | ADAS speed limit recognition state. Numeric representation. Indexed by camera COM port. |
| 42 | `adas.speed.limit.sensitivity` | `number` | `â€”` | `12965`, `621` | `adas_speed_limit_sensitivity` | `io_12965`, `io_621` | â€” | ADAS speed limit recognition sensitivity. Indexed by camera COM port. |
| 43 | `adas.time.to.collision` | `number` | `â€”` | `12953`, `609` | `adas_time_to_collision` | `io_12953`, `io_609` | â€” | Time to collision reported by ADAS. Indexed by camera COM port. |
| 44 | `agro.vehicle.state.bitmask` | `number` | `â€”` | `124`, `39` | `agro_vhc_st_bitmask` | `io_124`, `io_39` | â€” | Agricultural machinery flags |
| 45 | `ain` | `number` | `â€”` | `10`, `11`, `14210`, `19`, `245`, `6`, `839`, `840`, `9`, `9` | `ain` | `io_10`, `io_11`, `io_14210`, `io_19` (+6) | â€” | Voltage on the analog input |
| 46 | `alarm.event` | `boolean` | `â€”` | `236`, `846` | `alarm_event` | `io_236`, `io_846` | â€” | Alarm event triggered |
| 47 | `amber.alert.state` | `number` | `â€”` | `400` | `amber_alert_st` | `io_400` | â€” | Amber Alert state. 0 - Turned Off. 1 - Turned On, count down timer started. 2 - Amber Alert On button pressed to restard active timer. 3 - Alarm. 4 - Amber Alert turned On when timer is set to 0 seconds |
| 48 | `amber.alert.timeout` | `number` | `â€”` | `401` | `amber_alert_timeout` | `io_401` | â€” | Amber Alert time-out configured value |
| 49 | `available.status` | `boolean` | `â€”` | `825` | `available_stat` | `io_825` | â€” | Vehicle available status: true - available, false - not available |
| 50 | `average.x.acceleration` | `number` | `â€”` | `1429`, `259` | `average_x_accel` | `io_1429`, `io_259` | â€” | Harsh acceleration event average accelerometer value on X-axis |
| 51 | `average.y.acceleration` | `number` | `â€”` | `1429`, `259` | `average_y_accel` | `io_1429`, `io_259` | â€” | Harsh acceleration event average accelerometer value on Y-axis |
| 52 | `average.z.acceleration` | `number` | `â€”` | `1429`, `259` | `average_z_accel` | `io_1429`, `io_259` | â€” | Harsh acceleration event average accelerometer value on Z-axis |
| 53 | `barcode.id` | `string` | `â€”` | `264` | `barcode_id` | `io_264` | â€” | Barcode ID |
| 54 | `battery.capacity.full` | `number` | `â€”` | `829` | `bat_capacity_full` | `io_829` | â€” | Full battery capacity |
| 55 | `battery.capacity.remaining` | `number` | `â€”` | `828` | `bat_capacity_remaining` | `io_828` | â€” | Remaining battery capacity |
| 56 | `battery.charging.status` | `boolean` | `â€”` | `347`, `826` | `bat_charging_stat` | `io_347`, `io_826` | â€” | Battery charging status |
| 57 | `battery.current` | `number` | `â€”` | `68` | `battery_current` | `io_68` | Sensor `20` (AmpÃ©rage Batterie) | Battery current |
| 58 | `battery.health` | `number` | `â€”` | `823` | `bat_health` | `io_823` | â€” | Battery health level (SoH) |
| 59 | `battery.level` | `number` | `â€”` | `113`, `142`, `152`, `824` | `bat_lvl` | `io_113`, `io_142`, `io_152`, `io_824` | â€” | Internal battery level |
| 60 | `battery.overvoltage.status` | `boolean` | `â€”` | `851` | `bat_overvoltage_stat` | `io_851` | â€” | Battery overvoltage status (true - battery overvoltage, false - no battery overvoltage) |
| 61 | `battery.regeneration.status` | `boolean` | `â€”` | `848` | `bat_regeneration_stat` | `io_848` | â€” | Battery regeneration status: true - disabled, false - enabled |
| 62 | `battery.short.circuit` | `boolean` | `â€”` | `852` | `bat_short_circuit` | `io_852` | â€” | Battery short circuit (overcurrent) warning status: true - battery short circuit, false - no battery short circuit |
| 63 | `battery.status` | `boolean` | `â€”` | `849` | `bat_stat` | `io_849` | â€” | Battery on/off status: true - battery is on, false - battery is off |
| 64 | `battery.temperature` | `number` | `â€”` | `141`, `151`, `363`, `364` | `bat_temp` | `io_141`, `io_151`, `io_363`, `io_364` | â€” | Battery temperature |
| 65 | `battery.temperature.status` | `boolean` | `â€”` | `847` | `bat_temp_stat` | `io_847` | â€” | Battery temperature status: true - temperature is over or under the normal, false - temperature is normal |
| 66 | `battery.undervoltage.status` | `boolean` | `â€”` | `850` | `bat_undervoltage_stat` | `io_850` | â€” | Battery undervoltage status: true - battery undervoltage, false - no battery undervoltage |
| 67 | `battery.voltage` | `number` | `â€”` | `67` | `bat_vlt` | `io_67` | â€” | Internal battery voltage |
| 68 | `ble.1.custom` | `number` | `â€”` | `331`, `463` | `ble_1_custom` | `io_331`, `io_463` | â€” | Custom indexed element for BLE sensor 1 |
| 69 | `ble.1.custom.payload.hex` | `string` | `â€”` | `331`, `463`, `713`, `729` | `ble_1_custom_payload_hex` | `io_331`, `io_463`, `io_713`, `io_729` | â€” | Custom indexed element variable size payload for BLE sensor 1 |
| 70 | `ble.2.custom` | `number` | `â€”` | `332`, `467` | `ble_2_custom` | `io_332`, `io_467` | â€” | Custom indexed element for BLE sensor 2 |
| 71 | `ble.2.custom.payload.hex` | `string` | `â€”` | `332`, `467`, `714`, `733` | `ble_2_custom_payload_hex` | `io_332`, `io_467`, `io_714`, `io_733` | â€” | Custom indexed element variable size payload for BLE sensor 2 |
| 72 | `ble.3.custom` | `number` | `â€”` | `333`, `471` | `ble_3_custom` | `io_333`, `io_471` | â€” | Custom indexed element for BLE sensor 3 |
| 73 | `ble.3.custom.payload.hex` | `string` | `â€”` | `333`, `471`, `715`, `737` | `ble_3_custom_payload_hex` | `io_333`, `io_471`, `io_715`, `io_737` | â€” | Custom indexed element variable size payload for BLE sensor 3 |
| 74 | `ble.4.custom` | `number` | `â€”` | `334`, `475` | `ble_4_custom` | `io_334`, `io_475` | â€” | Custom indexed element for BLE sensor 4 |
| 75 | `ble.4.custom.payload.hex` | `string` | `â€”` | `334`, `475`, `716`, `741` | `ble_4_custom_payload_hex` | `io_334`, `io_475`, `io_716`, `io_741` | â€” | Custom indexed element variable size payload for BLE sensor 4 |
| 76 | `ble.beacon.present` | `boolean` | `â€”` | `1474` | `ble_beacon_present` | `io_1474` | â€” | BLE beacon presence indication |
| 77 | `ble.beacons` | `array` | `â€”` | `10500`, `10828`, `10829`, `10831`, `11317`, `385`, `548` | `ble_beacons` | `io_10500`, `io_10828`, `io_10829`, `io_10831` (+3) | â€” | Standard parameter names used: *id* - beacon identification string. Usually it is beacon's UUID or MAC-address *local_name* - Beacons's Local Name *rssi* - BLE signal level. Units = dBm *battery.voltage* - Beacon's battery voltage. Units = volts *battery.level* - Beacon's battery level. Units = percentage *temperature* - Beacon's temperature. Units = celsius *humidity* - Beacon's humidity. Units = percentage |
| 78 | `ble.lls.fuel.level` | `number` | `â€”` | `721` | `ble_lls_fuel_lvl` | `io_721` | â€” | Indexed BLE LLS fuel sensor value |
| 79 | `ble.lock.battery.level` | `number` | `â€”` | `872` | `ble_lock_bat_lvl` | `io_872` | â€” | BLE (Bluetooth Low Energy) Electronic Lock battery level |
| 80 | `ble.lock.status` | `boolean` | `â€”` | `871` | `ble_lock_stat` | `io_871` | â€” | BLE (Bluetooth Low Energy) Electronic lock is locked |
| 81 | `ble.mac.address` | `string` | `â€”` | `13243`, `891` | `ble_mac_address` | `io_13243`, `io_891` | â€” | BLE (Bluetooth Low Energy) MAC address |
| 82 | `ble.nbl2.button.1.status` | `boolean` | `â€”` | `455` | `ble_nbl2_button_1_stat` | `io_455` | â€” | BLE RFID reader Netronix NBL-2 button 1 status (4 programmable button states) |
| 83 | `ble.nbl2.button.2.status` | `boolean` | `â€”` | `459` | `ble_nbl2_button_2_stat` | `io_459` | â€” | BLE RFID reader Netronix NBL-2 button 2 status (4 programmable button states) |
| 84 | `ble.nbl2.rfid` | `string` | `â€”` | `451` | `ble_nbl2_rfid` | `io_451` | â€” | BLE RFID reader Netronix NBL-2 indexed RFID code read |
| 85 | `ble.sensor.battery.level` | `number` | `â€”` | `20`, `22`, `29`, `705` | `ble_sensor_bat_lvl` | `io_20`, `io_22`, `io_29`, `io_705` | â€” | BLE (Bluetooth Low Energy) sensor battery level |
| 86 | `ble.sensor.battery.voltage` | `number` | `â€”` | `10824`, `13222`, `20`, `22`, `29`, `523` | `ble_sensor_bat_vlt` | `io_10824`, `io_13222`, `io_20`, `io_22` (+2) | â€” | BLE (Bluetooth Low Energy) sensor battery voltage |
| 87 | `ble.sensor.battery.voltage.error.code` | `string` | `â€”` | `10824` | `ble_sensor_bat_vlt_error_code` | `io_10824` | â€” | Indexed BLE battery voltage sensor error description |
| 88 | `ble.sensor.device.name` | `string` | `â€”` | `13325` | `ble_sensor_device_name` | `io_13325` | â€” | BLE (Bluetooth Low Energy) sensor device name |
| 89 | `ble.sensor.frequency` | `number` | `â€”` | `306`, `725` | `ble_sensor_frequency` | `io_306`, `io_725` | â€” | Indexed BLE frequency sensor value |
| 90 | `ble.sensor.humidity` | `number` | `â€”` | `104`, `106`, `108`, `10804`, `13335`, `525`, `709`, `86` | `ble_sensor_humidity` | `io_104`, `io_106`, `io_108`, `io_10804` (+4) | â€” | BLE (Bluetooth Low Energy) sensor Humidity value |
| 91 | `ble.sensor.humidity.error.code` | `string` | `â€”` | `104`, `106`, `108`, `10804`, `13335`, `525`, `86` | `ble_sensor_humidity_error_code` | `io_104`, `io_106`, `io_108`, `io_10804` (+3) | â€” | BLE humidity sensor error description |
| 92 | `ble.sensor.illuminance` | `number` | `â€”` | `335`, `717` | `ble_sensor_illuminance` | `io_335`, `io_717` | â€” | BLE (Bluetooth Low Energy) sensor illuminance |
| 93 | `ble.sensor.low.battery.error.code` | `string` | `â€”` | `10820`, `13253` | `ble_sensor_low_bat_error_code` | `io_10820`, `io_13253` | â€” | Indexed BLE low battery sensor error description |
| 94 | `ble.sensor.low.battery.status` | `boolean` | `â€”` | `10820`, `13253` | `ble_sensor_low_bat_stat` | `io_10820`, `io_13253` | â€” | Indexed low battery indication BLE sensor |
| 95 | `ble.sensor.magnet.count` | `number` | `â€”` | `10840` | `ble_sensor_magnet_count` | `io_10840` | â€” | Indexed magnet count value of BLE Sensor |
| 96 | `ble.sensor.magnet.count.error.code` | `string` | `â€”` | `10840` | `ble_sensor_magnet_count_error_code` | `io_10840` | â€” | Indexed BLE magnet count sensor error description |
| 97 | `ble.sensor.magnet.status` | `boolean` | `â€”` | `10808`, `13460` | `ble_sensor_magnet_stat` | `io_10808`, `io_13460` | â€” | Indexed magnet state measured by BLE sensor |
| 98 | `ble.sensor.magnet.status.error.code` | `string` | `â€”` | `10808`, `13460` | `ble_sensor_magnet_stat_error_code` | `io_10808`, `io_13460` | â€” | Indexed BLE magnet sensor error description |
| 99 | `ble.sensor.movement.count` | `number` | `â€”` | `10812`, `10836`, `13468` | `ble_sensor_mvm_count` | `io_10812`, `io_10836`, `io_13468` | â€” | Indexed movement count value of BLE Sensor |
| 100 | `ble.sensor.movement.count.error.code` | `string` | `â€”` | `10836` | `ble_sensor_mvm_count_error_code` | `io_10836` | â€” | Indexed BLE movement count sensor error description |
| 101 | `ble.sensor.movement.error.code` | `string` | `â€”` | `10812` | `ble_sensor_mvm_error_code` | `io_10812` | â€” | Indexed movement BLE sensor error code |
| 102 | `ble.sensor.movement.status` | `boolean` | `â€”` | `10812` | `ble_sensor_mvm_stat` | `io_10812` | â€” | Indexed movement state measured by BLE sensor |
| 103 | `ble.sensor.pitch.angle` | `number` | `â€”` | `10816`, `13474` | `ble_sensor_pitch_angle` | `io_10816`, `io_13474` | â€” | Indexed pitch angle measured by BLE sensor |
| 104 | `ble.sensor.pitch.angle.error.code` | `string` | `â€”` | `10816`, `13474` | `ble_sensor_pitch_angle_error_code` | `io_10816`, `io_13474` | â€” | Indexed BLE pitch angle sensor error description |
| 105 | `ble.sensor.roll.angle` | `number` | `â€”` | `10832`, `13480` | `ble_sensor_roll_angle` | `io_10832`, `io_13480` | â€” | Indexed roll angle measured by BLE sensor |
| 106 | `ble.sensor.roll.angle.error.code` | `string` | `â€”` | `10832`, `13480` | `ble_sensor_roll_angle_error_code` | `io_10832`, `io_13480` | â€” | Indexed BLE roll angle sensor error description |
| 107 | `ble.sensor.rssi` | `number` | `â€”` | `13233` | `ble_sensor_rssi` | `io_13233` | â€” | BLE (Bluetooth Low Energy) sensor RSSI signal strength |
| 108 | `ble.sensor.temperature` | `number` | `â€”` | `10800`, `13227`, `25`, `25`, `26`, `701` | `ble_sensor_temp` | `io_10800`, `io_13227`, `io_25`, `io_25` (+2) | â€” | BLE (Bluetooth Low Energy) sensor Temperature value |
| 109 | `ble.sensor.temperature.error.code` | `string` | `â€”` | `10800`, `13227`, `25`, `701` | `ble_sensor_temp_error_code` | `io_10800`, `io_13227`, `io_25`, `io_701` | â€” | BLE temperature sensor error description |
| 110 | `bluetooth.device.mac.address` | `string` | `â€”` | `238` | `bluetooth_device_mac_address` | `io_238` | â€” | MAC address of bluetooth-connected peripheral device |
| 111 | `bluetooth.state.enum` | `number` | `â€”` | `263` | `bluetooth_st_enum` | `io_263` | â€” | Bluetooth state: 0 - BT is disabled 1 - BT Enabled, not device connected 2 - Device connected, BTv3 Only 3 - Device connected, BLE only 4 - Device connected, BLE + BT |
| 112 | `button.action.type` | `number` | `â€”` | `389`, `392` | `button_action_type` | `io_389`, `io_392` | â€” | Button Action type: 1 - 1 click 2 - 2 clicks 3 - long click |
| 113 | `button.id` | `number` | `â€”` | `389`, `392` | `button_id` | `io_389`, `io_392` | â€” | The number of the button pressed |
| 114 | `button.pressed.status` | `boolean` | `â€”` | `132`, `47` | `button_pressed_stat` | `io_132`, `io_47` | â€” | Any operate button in the car was put |
| 115 | `buzzer.alarm.status` | `boolean` | `â€”` | `345` | `buzzer_alarm_stat` | `io_345` | â€” | Buzzer alarm status |
| 116 | `cable.connected.status` | `boolean` | `â€”` | `132`, `47`, `517`, `914` | `cable_connected_stat` | `io_132`, `io_47`, `io_517`, `io_914` | â€” | Charging cable connected status |
| 117 | `camera.front.operating.state` | `string` | `â€”` | `12969`, `12971`, `12972`, `12974` | `camera_front_operating_st` | `io_12969`, `io_12971`, `io_12972`, `io_12974` | â€” | Front camera running state. Indexed by camera COM port. |
| 118 | `camera.front.operating.state.enum` | `number` | `â€”` | `12969`, `12971`, `12972`, `12974` | `camera_front_operating_st_enum` | `io_12969`, `io_12971`, `io_12972`, `io_12974` | â€” | Front camera running state. Number representation. Indexed by camera COM port. |
| 119 | `camera.front.state` | `string` | `â€”` | `12301`, `12303`, `12304`, `12306` | `camera_front_st` | `io_12301`, `io_12303`, `io_12304`, `io_12306` | â€” | Front camera ping transmission and TF status. Indexed by camera COM port. |
| 120 | `camera.front.state.enum` | `number` | `â€”` | `12301`, `12303`, `12304`, `12306` | `camera_front_st_enum` | `io_12301`, `io_12303`, `io_12304`, `io_12306` | â€” | Front camera ping transmission and TF status. Number representation. Indexed by camera COM port. |
| 121 | `camera.rear.operating.state` | `string` | `â€”` | `12970`, `12973` | `camera_rear_operating_st` | `io_12970`, `io_12973` | â€” | Rear camera running state. Indexed by camera COM port. |
| 122 | `camera.rear.operating.state.enum` | `number` | `â€”` | `12970`, `12973` | `camera_rear_operating_st_enum` | `io_12970`, `io_12973` | â€” | Rear camera running state. Number representation. Indexed by camera COM port. |
| 123 | `camera.rear.state` | `string` | `â€”` | `12302`, `12305` | `camera_rear_st` | `io_12302`, `io_12305` | â€” | Rear camera ping transmission and TF status. Indexed by camera COM port. |
| 124 | `camera.rear.state.enum` | `number` | `â€”` | `12302`, `12305` | `camera_rear_st_enum` | `io_12302`, `io_12305` | â€” | Rear camera ping transmission and TF status. Number representation. Indexed by camera COM port. |
| 125 | `camera.report.reason` | `string` | `â€”` | `498` | `camera_report_reason` | `io_498` | â€” | Camera report reason |
| 126 | `camera.report.reason.enum` | `number` | `â€”` | `498` | `camera_report_reason_enum` | `io_498` | â€” | Camera report reason ID |
| 127 | `camera.state` | `string` | `â€”` | `499` | `camera_st` | `io_499` | â€” | Front camera ping transmission and TF status checking parameters ID |
| 128 | `camera.state.enum` | `number` | `â€”` | `499` | `camera_st_enum` | `io_499` | â€” | Front camera ping transmission and TF status checking parameters ID. Number representation. |
| 129 | `camera.status` | `boolean` | `â€”` | *(Protocol / Header)* | `camera_stat` | â€” | â€” | Camera connected status |
| 130 | `camera.type` | `string` | `â€”` | `12301`, `12302`, `12303`, `12304`, `12305`, `12306`, `12969`, `12970`, `12971`, `12972`, `12973`, `12974` | `camera_type` | `io_12301`, `io_12302`, `io_12303`, `io_12304` (+8) | â€” | Connected camera type |
| 131 | `can.abs.failure.indicator.state` | `string` | `â€”` | `10429` | `can_abs_failure_indicator_st` | `io_10429` | â€” | Vehicle parameter for anti-lock brake system failure indicator read from CAN |
| 132 | `can.abs.failure.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `954` | `can_abs_failure_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_954` | â€” | ABS failure indicator status read from CAN |
| 133 | `can.absolute.fuel.rail.pressure` | `number` | `â€”` | `56` | `can_absolute_fuel_rail_press` | `io_56` | â€” | Absolute fuel rail pressure |
| 134 | `can.absolute.load` | `number` | `â€”` | `52` | `can_absolute_load` | `io_52` | â€” | Absolute load value - the normalized value of air mass per intake stroke, read from CAN |
| 135 | `can.abs.trailer.indicator.state` | `string` | `â€”` | `10431` | `can_abs_trailer_indicator_st` | `io_10431` | â€” | Vehicle parameter for ABS trailer indicator read from CAN |
| 136 | `can.acceleration.rate.limit.state` | `number` | `â€”` | `939` | `can_accel_rate_limit_st` | `io_939` | â€” | Vehicle acceleration rate limit status |
| 137 | `can.accelerator.pedal.kickdown.switch.state` | `number` | `â€”` | `931` | `can_accelerator_pedal_kickdown_switch_st` | `io_931` | â€” | Accelerator pedal kickdown switch status |
| 138 | `can.accelerator.pedal.low.idle.switch.state` | `number` | `â€”` | `930`, `933` | `can_accelerator_pedal_low_idle_switch_st` | `io_930`, `io_933` | â€” | Accelerator pedal low idle switch status, indexed parameter |
| 139 | `can.accelerator.pedal.position` | `number` | `â€”` | `934`, `938` | `can_accelerator_pedal_pos` | `io_934`, `io_938` | â€” | Accelerator pedal position read from CAN |
| 140 | `can.activated.batteries` | `number` | `â€”` | `1160` | `can_activated_batteries` | `io_1160` | â€” | Activated batteries from CAN bus |
| 141 | `can.actual.engine.additional.torque` | `number` | `â€”` | `946` | `can_actual_eng_additional_torque` | `io_946` | â€” | Actual engine additional torque in percent of the reference engine torque (fractional) |
| 142 | `can.actual.engine.torque` | `number` | `â€”` | `948` | `can_actual_eng_torque` | `io_948` | â€” | Actual calculated output torque of the engine |
| 143 | `can.adaptive.cruise.control.indicator.state` | `string` | `â€”` | `10431` | `can_adaptive_cruise_control_indicator_st` | `io_10431` | â€” | Vehicle parameter for adaptive cruise control indicator read from CAN |
| 144 | `can.adblue.level` | `number` | `â€”` | `10455`, `111`, `19` | `can_adblue_lvl` | `io_10455`, `io_111`, `io_19` | Sensor `86` (Niveau AdBlue) | AdBlue (diesel exhaust fluid) level read from CAN |
| 145 | `can.adblue.level.indicator.state` | `string` | `â€”` | `10430` | `can_adblue_lvl_indicator_st` | `io_10430` | â€” | Vehicle parameter for AdBlue level indicator read from CAN |
| 146 | `can.adblue.level.low.indicator.status` | `boolean` | `â€”` | `519`, `987` | `can_adblue_lvl_low_indicator_stat` | `io_519`, `io_987` | â€” | Low AdBlue level indicator from CAN bus |
| 147 | `can.adblue.tempering.indicator.state` | `string` | `â€”` | `13259` | `can_adblue_tempering_indicator_st` | `io_13259` | â€” | Vehicle parameter for AdBlue tempering indicator read from CAN |
| 148 | `can.adblue.volume` | `number` | `â€”` | `112`, `20` | `can_adblue_volume` | `io_112`, `io_20` | â€” | AdBlue (diesel exhaust fluid) volume read from CAN |
| 149 | `can.additional.front.lights.status` | `boolean` | `â€”` | `518`, `933` | `can_additional_front_lights_stat` | `io_518`, `io_933` | â€” | Additional front lights turned on status, read from CAN |
| 150 | `can.additional.rear.lights.status` | `boolean` | `â€”` | `518`, `934` | `can_additional_rear_lights_stat` | `io_518`, `io_934` | â€” | Additional rear lights turned on status, read from CAN |
| 151 | `can.airbag.indicator.state` | `string` | `â€”` | `10431` | `can_airbag_indicator_st` | `io_10431` | â€” | Vehicle parameter for airbag indicator read from CAN |
| 152 | `can.airbag.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `962` | `can_airbag_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_962` | â€” | Airbag indicator status read from CAN |
| 153 | `can.air.condition.status` | `boolean` | `â€”` | `123`, `38`, `518`, `936` | `can_air_condition_stat` | `io_123`, `io_38`, `io_518`, `io_936` | â€” | CAN air conditioning is on |
| 154 | `can.air.filter.clogged.indicator.state` | `string` | `â€”` | `10431` | `can_air_filter_clogged_indicator_st` | `io_10431` | â€” | Vehicle parameter for air filter clogged indicator read from CAN |
| 155 | `can.air.filter.plugged.indicator.status` | `boolean` | `â€”` | `519`, `982` | `can_air_filter_plugged_indicator_stat` | `io_519`, `io_982` | â€” | Air filter is plugged indicator from CAN bus |
| 156 | `can.alternator.current` | `number` | `â€”` | `1053` | `can_alternator_current` | `io_1053` | â€” | Measure of electrical current flow from the alternator |
| 157 | `can.ambient.air.temperature` | `number` | `â€”` | `1188`, `128`, `1396`, `53` | `can_ambient_air_temp` | `io_1188`, `io_128`, `io_1396`, `io_53` | Sensor `25` (TempÃ©rature ambiante) | CAN ambient air temperature |
| 158 | `can.articulation.indicator.state` | `string` | `â€”` | `10430` | `can_articulation_indicator_st` | `io_10430` | â€” | Vehicle parameter for articulation indicator read from CAN |
| 159 | `can.automatic.retarder.status` | `boolean` | `â€”` | `123`, `38`, `518`, `938` | `can_automatic_retarder_stat` | `io_123`, `io_38`, `io_518`, `io_938` | â€” | Automatic retarder status, read from CAN |
| 160 | `can.auxiliary.air.pressure.indicator.state` | `string` | `â€”` | `10431` | `can_auxiliary_air_press_indicator_st` | `io_10431` | â€” | Vehicle parameter for auxiliary air pressure indicator read from CAN |
| 161 | `can.available.engine.torque` | `number` | `â€”` | `943` | `can_available_eng_torque` | `io_943` | â€” | Actual maximum available engine - percent torque |
| 162 | `can.average.fuel.economy` | `number` | `â€”` | `1037` | `can_average_fuel_eco` | `io_1037` | â€” | CAN average fuel economy |
| 163 | `can.axle.weight` | `number` | `â€”` | `118`, `26`, `32`, `89` | `can_axle_weight` | `io_118`, `io_26`, `io_32`, `io_89` | â€” | Weight on the axle read from CAN |
| 164 | `can.barometric.pressure` | `number` | `â€”` | `50` | `can_barometric_press` | `io_50` | â€” | Absolute barometric pressure read from CAN |
| 165 | `can.battery1.current` | `number` | `â€”` | `1163` | `can_battery1_current` | `io_1163` | â€” | Battery 1 current from CAN bus |
| 166 | `can.battery1.power.stage.temperature` | `number` | `â€”` | `1168` | `can_battery1_power_stage_temp` | `io_1168` | â€” | Battery 1 power stage temp from CAN bus |
| 167 | `can.battery1.remaining.capacity` | `number` | `â€”` | `1169` | `can_battery1_remaining_capacity` | `io_1169` | â€” | Battery 1 remaining capacity from CAN bus |
| 168 | `can.battery1.soc` | `number` | `â€”` | `1165` | `can_battery1_soc` | `io_1165` | â€” | Battery 1 SoC from CAN bus |
| 169 | `can.battery1.state.enum` | `number` | `â€”` | `1164` | `can_battery1_st_enum` | `io_1164` | â€” | Battery 1 state from CAN bus |
| 170 | `can.battery1.temperature` | `number` | `â€”` | `1166`, `1167` | `can_battery1_temp` | `io_1166`, `io_1167` | â€” | Indexed battery 1 temperature from CAN bus |
| 171 | `can.battery1.voltage` | `number` | `â€”` | `1162` | `can_battery1_vlt` | `io_1162` | â€” | Battery 1 voltage from CAN bus |
| 172 | `can.battery2.current` | `number` | `â€”` | `1171` | `can_battery2_current` | `io_1171` | â€” | Battery 2 current from CAN bus |
| 173 | `can.battery2.power.stage.temperature` | `number` | `â€”` | `1176` | `can_battery2_power_stage_temp` | `io_1176` | â€” | Battery 2 power stage temp from CAN bus |
| 174 | `can.battery2.remaining.capacity` | `number` | `â€”` | `1177` | `can_battery2_remaining_capacity` | `io_1177` | â€” | Battery 2 remaining capacity from CAN bus |
| 175 | `can.battery2.soc` | `number` | `â€”` | `1173` | `can_battery2_soc` | `io_1173` | â€” | Battery 2 SoC from CAN bus |
| 176 | `can.battery2.state.enum` | `number` | `â€”` | `1172` | `can_battery2_st_enum` | `io_1172` | â€” | Battery 2 state from CAN bus |
| 177 | `can.battery2.temperature` | `number` | `â€”` | `1174`, `1175` | `can_battery2_temp` | `io_1174`, `io_1175` | â€” | Indexed battery 2 temperature from CAN bus |
| 178 | `can.battery2.voltage` | `number` | `â€”` | `1170` | `can_battery2_vlt` | `io_1170` | â€” | Battery 2 voltage from CAN bus |
| 179 | `can.battery.charging.indicator.state` | `string` | `â€”` | `10428` | `can_bat_charging_indicator_st` | `io_10428` | â€” | Vehicle parameter for battery charging condition indicator read from CAN |
| 180 | `can.battery.error.code` | `string` | `â€”` | `1178`, `1179` | `can_bat_error_code` | `io_1178`, `io_1179` | â€” | Battery error code read from CAN |
| 181 | `can.battery.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `960` | `can_bat_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_960` | â€” | Battery indicator status read from CAN |
| 182 | `can.battery.pack.cooling.indicator.state` | `string` | `â€”` | `13259` | `can_bat_pack_cooling_indicator_st` | `io_13259` | â€” | Vehicle parameter for battery pack cooling indicator read from CAN |
| 183 | `can.battery.pack.indicator.state` | `string` | `â€”` | `13259` | `can_bat_pack_indicator_st` | `io_13259` | â€” | Vehicle parameter for battery pack indicator read from CAN |
| 184 | `can.battery.pack.temperature.indicator.state` | `string` | `â€”` | `13259` | `can_bat_pack_temp_indicator_st` | `io_13259` | â€” | Vehicle parameter for battery pack temperature indicator read from CAN |
| 185 | `can.battery.voltage` | `number` | `â€”` | `1184`, `168`, `507` | `can_bat_vlt` | `io_1184`, `io_168`, `io_507` | â€” | Battery voltage read from CAN |
| 186 | `can.brake.failure.indicator.state` | `string` | `â€”` | `10428` | `can_brake_failure_indicator_st` | `io_10428` | â€” | Vehicle parameter for brake failure/brake system malfunction indicator read from CAN |
| 187 | `can.brake.lights.indicator.state` | `string` | `â€”` | `10430` | `can_brake_lights_indicator_st` | `io_10430` | â€” | Vehicle parameter for brake lights indicator read from CAN |
| 188 | `can.brake.pedal.level` | `number` | `â€”` | `1201`, `357` | `can_brake_pedal_lvl` | `io_1201`, `io_357` | Sensor `8` (Position de la pÃ©dale de frein) | Brake pedal push level read from CAN |
| 189 | `can.brake.pressure` | `number` | `â€”` | `1120` | `can_brake_press` | `io_1120` | â€” | Brake application pressure from CAN bus |
| 190 | `can.brake.system.filter.clogged.indicator.status` | `boolean` | `â€”` | `519`, `985` | `can_brake_system_filter_clogged_indicator_stat` | `io_519`, `io_985` | â€” | Clogged brake system filter indicator from CAN bus |
| 191 | `can.bus.stop.brake.indicator.state` | `string` | `â€”` | `10430` | `can_bus_stop_brake_indicator_st` | `io_10430` | â€” | Vehicle parameter for bus stop brake indicator read from CAN |
| 192 | `can.car.closed.remote.status` | `boolean` | `â€”` | `132`, `47`, `517`, `917` | `can_car_closed_remote_stat` | `io_132`, `io_47`, `io_517`, `io_917` | â€” | Car closed by factory's remote control, read from CAN |
| 193 | `can.car.closed.status` | `boolean` | `â€”` | `132`, `47`, `517`, `662` | `can_car_closed_stat` | `io_132`, `io_47`, `io_517`, `io_662` | â€” | Car closed status, read from CAN |
| 194 | `can.car.closing.remote.event` | `boolean` | `â€”` | `517`, `920` | `can_car_closing_remote_event` | `io_517`, `io_920` | â€” | Signal of closing with factory remote control was sent, read from CAN |
| 195 | `can.car.opening.remote.event` | `boolean` | `â€”` | `517`, `921` | `can_car_opening_remote_event` | `io_517`, `io_921` | â€” | Signal of opening with factory remote control was sent, read from CAN |
| 196 | `can.car.triple.closing.remote.event` | `boolean` | `â€”` | `517`, `925` | `can_car_triple_closing_remote_event` | `io_517`, `io_925` | â€” | Signal of closing with factory remote control was sent 3 times, read from CAN |
| 197 | `can.catalyst.differential.pressure` | `number` | `â€”` | `955` | `can_catalyst_differential_press` | `io_955` | â€” | Exhaust differential pressure measured between the intake and exhaust of a diesel oxidation catalyst in exhaust bank parameter is indexed by bank number |
| 198 | `can.catalyst.intake.temperature` | `number` | `â€”` | `953` | `can_catalyst_intake_temp` | `io_953` | â€” | Temperature of engine combustion byproducts entering the diesel oxidation catalyst in exhaust bank parameter is indexed by bank number |
| 199 | `can.catalyst.outlet.temperature` | `number` | `â€”` | `954` | `can_catalyst_outlet_temp` | `io_954` | â€” | Temperature of engine combustion byproducts leaving the diesel oxidation catalyst exhaust in exhaust bank parameter is indexed by bank number |
| 200 | `can.central.differential.4hi.status` | `boolean` | `â€”` | `518`, `949` | `can_central_differential_4hi_stat` | `io_518`, `io_949` | â€” | Central differential 4HI locked status, read from CAN |
| 201 | `can.central.differential.4lo.status` | `boolean` | `â€”` | `518`, `950` | `can_central_differential_4lo_stat` | `io_518`, `io_950` | â€” | Central differential with reductor 4LO locked status, read from CAN |
| 202 | `can.check.engine.indicator.status` | `boolean` | `â€”` | `123`, `38` | `can_check_eng_indicator_stat` | `io_123`, `io_38` | â€” | Check engine indicator status read from CAN |
| 203 | `can.cleaning.fan.control.status` | `boolean` | `â€”` | `520` | `can_cleaning_fan_control_stat` | `io_520` | â€” | Cleaning fan control status: true - on, false - off, read from CAN |
| 204 | `can.cluster.current` | `number` | `â€”` | `1155` | `can_cluster_current` | `io_1155` | â€” | Cluster current from CAN bus |
| 205 | `can.cluster.error.code` | `string` | `â€”` | `1180` | `can_cluster_error_code` | `io_1180` | â€” | Cluster error code from CAN bus in hex form |
| 206 | `can.cluster.soc` | `number` | `â€”` | `1148` | `can_cluster_soc` | `io_1148` | â€” | Cluster SoC from CAN bus |
| 207 | `can.cluster.state.enum` | `number` | `â€”` | `1147` | `can_cluster_st_enum` | `io_1147` | â€” | Cluster state from CAN bus |
| 208 | `can.cluster.voltage` | `number` | `â€”` | `1154` | `can_cluster_vlt` | `io_1154` | â€” | Cluster voltage from CAN bus |
| 209 | `can.cng.consumed` | `number` | `â€”` | `227`, `233` | `can_cng_consumed` | `io_227`, `io_233` | â€” | Consumed of compressed natural gas read from CAN |
| 210 | `can.cng.level` | `number` | `â€”` | `228`, `234` | `can_cng_lvl` | `io_228`, `io_234` | â€” | Compressed natural gas level read from CAN |
| 211 | `can.cng.level.low.indicator.status` | `boolean` | `â€”` | `519`, `992` | `can_cng_lvl_low_indicator_stat` | `io_519`, `io_992` | â€” | Low CNG level indicator from CAN bus |
| 212 | `can.cng.status` | `boolean` | `â€”` | `226`, `232`, `517`, `903` | `can_cng_stat` | `io_226`, `io_232`, `io_517`, `io_903` | â€” | Compressed natural gas status read from CAN |
| 213 | `can.com.error.status` | `boolean` | `â€”` | `1129` | `can_com_error_stat` | `io_1129` | â€” | COM Error status from CAN bus |
| 214 | `can.commanded.egr` | `number` | `â€”` | `46` | `can_commanded_egr` | `io_46` | â€” | Commanded EGR value read from CAN |
| 215 | `can.connection.state` | `number` | `â€”` | `132`, `47`, `517` | `can_connection_st` | `io_132`, `io_47`, `io_517` | â€” | The car CAN bus synchronization state |
| 216 | `can.control.module.voltage` | `number` | `â€”` | `51` | `can_control_module_vlt` | `io_51` | â€” | Control module voltage read from CAN |
| 217 | `can.coolant.level.low.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `976` | `can_coolant_lvl_low_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_976` | â€” | Coolant level low indicator status read from CAN |
| 218 | `can.coolant.liquid.indicator.status` | `boolean` | `â€”` | `519`, `959` | `can_coolant_liquid_indicator_stat` | `io_519`, `io_959` | â€” | Coolant liquid temperature / level indicator from CAN bus |
| 219 | `can.cooling.air.conditioning.indicator.state` | `string` | `â€”` | `10428` | `can_cooling_air_conditioning_indicator_st` | `io_10428` | â€” | Vehicle parameter for cooling air conditioning indicator read from CAN |
| 220 | `can.corn.header.connected.status` | `boolean` | `â€”` | `520` | `can_corn_header_connected_stat` | `io_520` | â€” | Corn header connected status, read from CAN |
| 221 | `can.counted.engine.motorhours` | `number` | `â€”` | `103` | `can_counted_eng_motorhours` | `io_103` | â€” | Engine Worktime counted by the IoT device from 0 starting from the connection of the CAN adapter or CAN device |
| 222 | `can.cruise.control.state` | `number` | `â€”` | `1195` | `can_cruise_control_st` | `io_1195` | â€” | Cruise control state read from CAN |
| 223 | `can.cruise.status` | `boolean` | `â€”` | `123`, `38`, `518`, `81`, `937` | `can_cruise_stat` | `io_123`, `io_38`, `io_518`, `io_81` (+1) | Sensor `29` (RÃ©gulateur de vitesse) | CAN cruise control is active |
| 224 | `can.data.frame` | `string` | `â€”` | `900` | `can_data_frame` | `io_900` | â€” | CAN data frame value in HEX representation, indexed by CAN message ID or element identifier |
| 225 | `can.direct.fuel.rail.pressure` | `number` | `â€”` | `45` | `can_direct_fuel_rail_press` | `io_45` | â€” | Fuel rail gauge pressure for diesel or gasoline direct injection |
| 226 | `can.disabled.persons.indicator.state` | `string` | `â€”` | `10428` | `can_disabled_persons_indicator_st` | `io_10428` | â€” | Vehicle parameter for provision for disabled/handicapped persons indicator read from CAN |
| 227 | `can.discharge.time` | `number` | `â€”` | `1145` | `can_discharge_time` | `io_1145` | â€” | Time to empty from CAN bus |
| 228 | `can.distance.since.codes.cleared` | `number` | `â€”` | `49` | `can_dist_since_codes_cleared` | `io_49` | â€” | Distance traveled since codes cleared |
| 229 | `can.dpf.thermal.management.state` | `number` | `â€”` | `941` | `can_dpf_thermal_management_st` | `io_941` | â€” | DPF thermal management active |
| 230 | `can.drive.gear.status` | `boolean` | `â€”` | `517`, `927` | `can_drive_gear_stat` | `io_517`, `io_927` | â€” | CAN drive gear is on |
| 231 | `can.driver.demand.engine.torque` | `number` | `â€”` | `947` | `can_driver_demand_eng_torque` | `io_947` | â€” | Requested torque output of the engine by the driver |
| 232 | `can.driver.seatbelt.indicator.status` | `boolean` | `â€”` | `123`, `38` | `can_driver_seatbelt_indicator_stat` | `io_123`, `io_38` | â€” | Driver's seatbelt indicator status read from CAN |
| 233 | `can.driver.seatbelt.status` | `boolean` | `â€”` | `10631`, `1194`, `518`, `940` | `can_driver_seatbelt_stat` | `io_10631`, `io_1194`, `io_518`, `io_940` | â€” | Driver's seatbelt fastened status, read from CAN |
| 234 | `can.dtc` | `array` | `â€”` | `10493`, `10494`, `10495`, `10496`, `281`, `282`, `525` | `can_dtc` | `io_10493`, `io_10494`, `io_10495`, `io_10496` (+3) | â€” | Diagnostic trouble code array read from CAN May content list of OBDII codes or list of objects with codes. Standard object parameter names used: *standard* - Protocol standard (J1939, J1708(J1587), OBDII) *mid* - Message Identifier (J1708) *sid* - Subsystem Identifier (J1708) *fmi* - Failure Mode Identifier (J1939, J1708) *spn* - Suspect Parameter Number (J1939) *sa* - Source Address (J1939, OBDII) *oc* - Occurrence Count (J1939) *cm* - Conversion Method (J1939) *status* - Status of error code (active, pending, historical, permanent) |
| 235 | `can.dtc.number` | `number` | `â€”` | `1182`, `160`, `176`, `30` | `can_dtc_num` | `io_1182`, `io_160`, `io_176`, `io_30` | â€” | Number of diagnostic trouble codes |
| 236 | `can.dual.fuel.status` | `boolean` | `â€”` | `1083` | `can_dual_fuel_stat` | `io_1083` | â€” | Engine working on dual fuel status, read from CAN bus |
| 237 | `can.dynamic.ignition.status` | `boolean` | `â€”` | `132`, `47` | `can_dynamic_ignition_stat` | `io_132`, `io_47` | â€” | Dynamic ignition is ON, read from CAN |
| 238 | `can.ear.auger.speed.status` | `boolean` | `â€”` | `520` | `can_ear_auger_speed_stat` | `io_520` | â€” | Ear auger speed normal status, read from CAN: true - Ok, false - below normal |
| 239 | `can.ebs.indicator.state` | `string` | `â€”` | `10431` | `can_ebs_indicator_st` | `io_10431` | â€” | Vehicle parameter for EBS indicator read from CAN |
| 240 | `can.ebs.trailer.indicator.state` | `string` | `â€”` | `10431` | `can_ebs_trailer_indicator_st` | `io_10431` | â€” | Vehicle parameter for EBS trailer indicator read from CAN |
| 241 | `can.egr.error` | `number` | `â€”` | `47` | `can_egr_error` | `io_47` | â€” | EGR Error read from CAN |
| 242 | `can.electronic.power.control.status` | `boolean` | `â€”` | `123`, `38` | `can_electronic_power_control_stat` | `io_123`, `io_38` | â€” | Electronic power control status, read from CAN |
| 243 | `can.emergency.braking.system.indicator.state` | `string` | `â€”` | `10431` | `can_emergency_braking_system_indicator_st` | `io_10431` | â€” | Vehicle parameter for advanced emergency braking system indicator read from CAN |
| 244 | `can.engine.compartment.temperature.indicator.state` | `string` | `â€”` | `10430` | `can_eng_compartment_temp_indicator_st` | `io_10430` | â€” | Vehicle parameter for engine compartment temperature indicator read from CAN |
| 245 | `can.engine.coolant.level` | `number` | `â€”` | `1197` | `can_eng_coolant_lvl` | `io_1197` | â€” | Engine coolant level read from CAN |
| 246 | `can.engine.coolant.level.indicator.state` | `string` | `â€”` | `10429` | `can_eng_coolant_lvl_indicator_st` | `io_10429` | â€” | Vehicle parameter for engine coolant level indicator read from CAN |
| 247 | `can.engine.coolant.pressure` | `number` | `â€”` | `1198` | `can_eng_coolant_press` | `io_1198` | â€” | Engine coolant pressure |
| 248 | `can.engine.coolant.temperature` | `number` | `â€”` | `1002`, `127`, `32` | `can_eng_coolant_temp` | `io_1002`, `io_127`, `io_32` | Sensor `31` (TempÃ©rature du liquide de refroidissement du moteur) | Engine coolant temperature read from CAN |
| 249 | `can.engine.coolant.temperature.indicator.state` | `string` | `â€”` | `10428` | `can_eng_coolant_temp_indicator_st` | `io_10428` | â€” | Vehicle parameter for engine coolant temperature indicator read from CAN |
| 250 | `can.engine.emission.failure.indicator.state` | `string` | `â€”` | `10430` | `can_eng_emission_failure_indicator_st` | `io_10430` | â€” | Vehicle parameter for engine emission system failure (MIL) indicator read from CAN |
| 251 | `can.engine.emission.filter.indicator.state` | `string` | `â€”` | `13259` | `can_eng_emission_filter_indicator_st` | `io_13259` | â€” | Vehicle parameter for engine emission filter (soot filter) indicator read from CAN |
| 252 | `can.engine.fuel.rate` | `number` | `â€”` | `1035`, `110`, `18` | `can_eng_fuel_rate` | `io_1035`, `io_110`, `io_18` | â€” | Engine fuel rate read from CAN |
| 253 | `can.engine.ignition.status` | `boolean` | `â€”` | `10883`, `1178`, `132`, `47`, `517`, `898` | `can_eng_ignition_stat` | `io_10883`, `io_1178`, `io_132`, `io_47` (+2) | â€” | CAN engine ignition status |
| 254 | `can.engine.intercooler.temperature` | `number` | `â€”` | `1006` | `can_eng_intercooler_temp` | `io_1006` | â€” | Temperature of liquid found in the intercooler located after the turbocharger |
| 255 | `can.engine.load` | `number` | `â€”` | `1189`, `936` | `can_eng_load` | `io_1189`, `io_936` | â€” | Engine percent load at current speed |
| 256 | `can.engine.load.level` | `number` | `â€”` | `114`, `23`, `31`, `85` | `can_eng_load_lvl` | `io_114`, `io_23`, `io_31`, `io_85` | Sensor `2` (Charge actuelle du moteur), Sensor `44` (Puissance_output), Sensor `45` (Couple Moteur) | Calculated engine load level read from CAN |
| 257 | `can.engine.lock.status` | `boolean` | `â€”` | `517`, `907` | `can_eng_lock_stat` | `io_517`, `io_907` | â€” | Engine lock status read from CAN |
| 258 | `can.engine.maximum.power.support.state` | `number` | `â€”` | `940` | `can_eng_maximum_power_support_st` | `io_940` | â€” | Momentary engine maximum power enable feedback |
| 259 | `can.engine.mil.indicator.state` | `string` | `â€”` | `10429` | `can_eng_mil_indicator_st` | `io_10429` | â€” | Vehicle parameter for engine/MIL indicator read from CAN |
| 260 | `can.engine.motorhours` | `number` | `â€”` | `102`, `103`, `1177`, `14`, `15`, `991` | `eng_mth` | `io_102`, `io_103`, `io_1177`, `io_14` (+2) | Sensor `30` (Engine Hours), Sensor `58` (TOTAL HEUR MOTEUR) | Total engine motorhours (engine work time) read from CAN |
| 261 | `can.engine.oil.filter.plugged.indicator.status` | `boolean` | `â€”` | `519`, `973` | `can_eng_oil_filter_plugged_indicator_stat` | `io_519`, `io_973` | â€” | Engine oil filter plugged indicator from CAN bus |
| 262 | `can.engine.oil.indicator.state` | `string` | `â€”` | `10428` | `can_eng_oil_indicator_st` | `io_10428` | â€” | Vehicle parameter for engine oil indicator read from CAN |
| 263 | `can.engine.oil.level` | `number` | `â€”` | `1159`, `524` | `can_eng_oil_lvl` | `io_1159`, `io_524` | â€” | Engine oil level read from CAN |
| 264 | `can.engine.oil.level.indicator.state` | `string` | `â€”` | `10429` | `can_eng_oil_lvl_indicator_st` | `io_10429` | â€” | Vehicle parameter for engine oil level indicator read from CAN |
| 265 | `can.engine.oil.pressure` | `number` | `â€”` | `1158`, `1193` | `can_eng_oil_press` | `io_1158`, `io_1193` | â€” | CAN Engine oil pressure |
| 266 | `can.engine.oil.temperature` | `number` | `â€”` | `1191`, `1270`, `13154`, `58` | `can_eng_oil_temp` | `io_1191`, `io_1270`, `io_13154`, `io_58` | â€” | Engine oil temperature read from CAN |
| 267 | `can.engine.oil.temperature.high.indicator.status` | `boolean` | `â€”` | `519`, `975` | `can_eng_oil_temp_high_indicator_stat` | `io_519`, `io_975` | â€” | Too high engine oil temperature indicator from CAN bus |
| 268 | `can.engine.oil.temperature.indicator.state` | `string` | `â€”` | `10429` | `can_eng_oil_temp_indicator_st` | `io_10429` | â€” | Vehicle parameter for engine oil temperature indicator read from CAN |
| 269 | `can.engine.rpm` | `number` | `â€”` | `1130`, `35`, `36`, `85`, `88`, `949` | `can_eng_rpm` | `io_1130`, `io_35`, `io_36`, `io_85` (+2) | Sensor `34` (RPM La vitesse du moteur), Sensor `44` (Puissance_output) | Engine RPM read from CAN |
| 270 | `can.engine.run.time` | `number` | `â€”` | `42` | `can_eng_run_time` | `io_42` | â€” | Run time since engine start read from CAN |
| 271 | `can.engine.temperature` | `number` | `â€”` | `115`, `25`, `32` | `can_eng_temp` | `io_115`, `io_25`, `io_32` | â€” | Engine temperature read from CAN |
| 272 | `can.engine.torque.mode` | `number` | `â€”` | `945` | `can_eng_torque_mode` | `io_945` | â€” | Engine torque mode |
| 273 | `can.engine.turbocharger.oil.temperature` | `number` | `â€”` | `1005` | `can_eng_turbocharger_oil_temp` | `io_1005` | â€” | Temperature of the turbocharger lubricant |
| 274 | `can.engine.working.status` | `boolean` | `â€”` | `132`, `47`, `517`, `900` | `can_eng_working_stat` | `io_132`, `io_47`, `io_517`, `io_900` | â€” | Engine is working, read from CAN |
| 275 | `can.epc.indicator.status` | `boolean` | `â€”` | `519`, `972` | `can_epc_indicator_stat` | `io_519`, `io_972` | â€” | EPC (Electronic Power Control) indicator status from CAN bus |
| 276 | `can.eps.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `963` | `can_eps_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_963` | â€” | Electric power steering indicator status, reaf from CAN |
| 277 | `can.equivalence.ratio` | `number` | `â€”` | `541` | `can_equivalence_ratio` | `io_541` | â€” | Fuel-air commanded equivalence ratio read from CAN |
| 278 | `can.esc.indicator.state` | `string` | `â€”` | `10430` | `can_esc_indicator_st` | `io_10430` | â€” | Vehicle parameter for ESC indication read from CAN |
| 279 | `can.esc.switched.off.indicator.state` | `string` | `â€”` | `10431` | `can_esc_switched_off_indicator_st` | `io_10431` | â€” | Vehicle parameter for ESC switched off indicator read from CAN |
| 280 | `can.esp.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `955` | `can_esp_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_955` | â€” | Electronic stability program indicator status, read from CAN |
| 281 | `can.esp.status` | `boolean` | `â€”` | `123`, `38`, `519`, `956` | `can_esp_stat` | `io_123`, `io_38`, `io_519`, `io_956` | â€” | CAN ESP warning is on |
| 282 | `can.ev.air.conditioner.compressor.state.enum` | `number` | `â€”` | `10892` | `can_ev_air_conditioner_compressor_st_enum` | `io_10892` | â€” | Air conditioner compressor state read from CAN, EV FMS |
| 283 | `can.ev.battery.current` | `number` | `â€”` | `10880` | `can_ev_bat_current` | `io_10880` | â€” | High voltage battery current read from CAN, EV FMS |
| 284 | `can.ev.battery.level` | `number` | `â€”` | `10882` | `can_ev_bat_lvl` | `io_10882` | â€” | High voltage battery state of charge read from CAN, EV FMS |
| 285 | `can.ev.battery.max.cell.voltage` | `number` | `â€”` | `10901` | `can_ev_bat_max_cell_vlt` | `io_10901` | â€” | High voltage battery highest cell voltage read from CAN, EV FMS |
| 286 | `can.ev.battery.max.temperature` | `number` | `â€”` | `10889` | `can_ev_bat_max_temp` | `io_10889` | â€” | High voltage battery highest cell temperature read from CAN, EV FMS |
| 287 | `can.ev.battery.min.cell.voltage` | `number` | `â€”` | `10902` | `can_ev_bat_min_cell_vlt` | `io_10902` | â€” | High voltage battery lowest cell voltage read from CAN, EV FMS |
| 288 | `can.ev.battery.min.temperature` | `number` | `â€”` | `10890` | `can_ev_bat_min_temp` | `io_10890` | â€” | High voltage battery lowest cell temperature read from CAN, EV FMS |
| 289 | `can.ev.battery.rated.capacity` | `number` | `â€”` | `10903` | `can_ev_bat_rated_capacity` | `io_10903` | â€” | High voltage energy storage system nominal rated capacity read from CAN, EV FMS |
| 290 | `can.ev.battery.temperature` | `number` | `â€”` | `10893` | `can_ev_bat_temp` | `io_10893` | â€” | High voltage battery temperature read from CAN, EV FMS |
| 291 | `can.ev.battery.voltage` | `number` | `â€”` | `10879` | `can_ev_bat_vlt` | `io_10879` | â€” | High voltage battery voltage read from CAN, EV FMS |
| 292 | `can.ev.cargo.weight` | `number` | `â€”` | `10897` | `can_ev_cargo_weight` | `io_10897` | â€” | Cargo weight read from CAN, EV FMS |
| 293 | `can.ev.dc.charging.state.enum` | `number` | `â€”` | `10888` | `can_ev_dc_charging_st_enum` | `io_10888` | â€” | DC charging state read from CAN, EV FMS |
| 294 | `can.ev.evse1.ac.current` | `number` | `â€”` | `10886` | `can_ev_evse1_ac_current` | `io_10886` | â€” | EVSE1 AC RMS current read from CAN, EV FMS |
| 295 | `can.ev.evse1.ac.voltage` | `number` | `â€”` | `10887` | `can_ev_evse1_ac_vlt` | `io_10887` | â€” | EVSE1 AC RMS voltage read from CAN, EV FMS |
| 296 | `can.ev.external.powersource.state.enum` | `number` | `â€”` | `10884` | `can_ev_ext_pwrs_st_enum` | `io_10884` | â€” | External energy source connection state read from CAN, EV FMS |
| 297 | `can.ev.internal.charger.state.enum` | `number` | `â€”` | `10881` | `can_ev_int_charger_st_enum` | `io_10881` | â€” | Internal charger state read from CAN, EV FMS |
| 298 | `can.ev.powered.vehicle.weight` | `number` | `â€”` | `10898` | `can_ev_powered_vhc_weight` | `io_10898` | â€” | Powered vehicle weight read from CAN, EV FMS |
| 299 | `can.ev.propulsion.motor.coolant.fan.temperature` | `number` | `â€”` | `10891` | `can_ev_propulsion_motor_coolant_fan_temp` | `io_10891` | â€” | Propulsion motor coolant fan 1 control temperature read from CAN, EV FMS |
| 300 | `can.ev.thermal.management.heater.state.enum` | `number` | `â€”` | `10894` | `can_ev_thermal_management_heater_st_enum` | `io_10894` | â€” | High voltage energy storage system thermal management system heater state read from CAN, EV FMS |
| 301 | `can.ev.trailer.weight` | `number` | `â€”` | `10896` | `can_ev_trailer_weight` | `io_10896` | â€” | Trailer weight read from CAN, EV FMS |
| 302 | `can.factory.armed.status` | `boolean` | `â€”` | `132`, `47`, `517`, `926` | `can_factory_armed_stat` | `io_132`, `io_47`, `io_517`, `io_926` | â€” | Factory armed status, read from CAN |
| 303 | `can.fap.indicator.status` | `boolean` | `â€”` | `519`, `971` | `can_fap_indicator_stat` | `io_519`, `io_971` | â€” | FAP indicator status from CAN bus |
| 304 | `can.faulty.batteries` | `number` | `â€”` | `1161` | `can_faulty_batteries` | `io_1161` | â€” | Faulty batteries from CAN bus |
| 305 | `can.feeder.reverse.status` | `boolean` | `â€”` | `520` | `can_feeder_reverse_stat` | `io_520` | â€” | Feeder revers switched on status, read from CAN |
| 306 | `can.feeder.speed.status` | `boolean` | `â€”` | `520` | `can_feeder_speed_stat` | `io_520` | â€” | Feeder speed normal status, read from CAN: true - Ok, false - below normal |
| 307 | `can.front.differential.status` | `boolean` | `â€”` | `518`, `947` | `can_front_differential_stat` | `io_518`, `io_947` | â€” | Front differential locked status, read from CAN |
| 308 | `can.front.fog.light.indicator.state` | `string` | `â€”` | `10428` | `can_front_fog_light_indicator_st` | `io_10428` | â€” | Vehicle parameter for front fog light indicator read from CAN |
| 309 | `can.front.fog.lights.status` | `boolean` | `â€”` | `123`, `38`, `518`, `932` | `can_front_fog_lights_stat` | `io_123`, `io_38`, `io_518`, `io_932` | â€” | CAN front fog lights are on |
| 310 | `can.front.hydraulic.status` | `boolean` | `â€”` | `520` | `can_front_hydraulic_stat` | `io_520` | â€” | Front hydraulic turned on status. read from CAN |
| 311 | `can.front.left.door.status` | `boolean` | `â€”` | `132`, `143`, `47`, `517`, `654`, `90` | `can_front_left_door_stat` | `io_132`, `io_143`, `io_47`, `io_517` (+2) | â€” | CAN front left door is opened |
| 312 | `can.front.left.window.status` | `boolean` | `â€”` | `1211` | `can_front_left_window_stat` | `io_1211` | â€” | CAN front left window is opened |
| 313 | `can.front.passenger.seatbelt.status` | `boolean` | `â€”` | `10632`, `518`, `941` | `can_front_passenger_seatbelt_stat` | `io_10632`, `io_518`, `io_941` | â€” | Fron passenger's seatbelt fastened status, read from CAN |
| 314 | `can.front.passenger.status` | `boolean` | `â€”` | `518`, `945` | `can_front_passenger_stat` | `io_518`, `io_945` | â€” | Front pasenger is present status, read from CAN |
| 315 | `can.front.pto.status` | `boolean` | `â€”` | `520` | `can_front_pto_stat` | `io_520` | â€” | Front power take-off status turned on status, read from CAN |
| 316 | `can.front.right.door.status` | `boolean` | `â€”` | `132`, `143`, `47`, `517`, `655`, `90` | `can_front_right_door_stat` | `io_132`, `io_143`, `io_47`, `io_517` (+2) | â€” | CAN front right door is opened |
| 317 | `can.front.right.window.status` | `boolean` | `â€”` | `1212` | `can_front_right_window_stat` | `io_1212` | â€” | CAN front right window is opened |
| 318 | `can.front.three.point.hitch.status` | `boolean` | `â€”` | `520` | `can_front_three_point_hitch_stat` | `io_520` | â€” | Front three-point hitch turned on status, read from CAN |
| 319 | `can.fuel.consumed` | `number` | `â€”` | `1180`, `33`, `83`, `86`, `996` | `can_fuel_consumed` | `io_1180`, `io_33`, `io_83`, `io_86` (+1) | Sensor `27` (consommation carburant au 100), Sensor `35` (Moteur total carburant utilisÃ©) | Fuel volume totally consumed by vehicle read from CAN |
| 320 | `can.fuel.consumption` | `number` | `â€”` | `135`, `60` | `can_fuel_cons` | `io_135`, `io_60` | Sensor `5` (Tarif carburant) | Engine fuel rate read from CAN |
| 321 | `can.fuel.economy` | `number` | `â€”` | `1036`, `1187`, `1345`, `136` | `can_fuel_eco` | `io_1036`, `io_1187`, `io_1345`, `io_136` | Sensor `26` (Ã‰conomie de carburant instantanÃ©e) | CAN instantaneous fuel economy |
| 322 | `can.fuel.filter.plugged.indicator.status` | `boolean` | `â€”` | `519`, `983` | `can_fuel_filter_plugged_indicator_stat` | `io_519`, `io_983` | â€” | Fuel filter is plugged indicator from CAN bus |
| 323 | `can.fuel.filter.pressure.indicator.state` | `string` | `â€”` | `10431` | `can_fuel_filter_press_indicator_st` | `io_10431` | â€” | Vehicle parameter for fuel filter differential pressure indicator read from CAN |
| 324 | `can.fuel.idle.consumed` | `number` | `â€”` | `1185` | `can_fuel_idle_consumed` | `io_1185` | â€” | Fuel volume totally consumed during idling state of the vehicle read from CAN |
| 325 | `can.fuel.injection.timing` | `number` | `â€”` | `59` | `can_fuel_injection_timing` | `io_59` | â€” | Fuel injection timing read from CAN |
| 326 | `can.fuel.level` | `number` | `â€”` | `1066`, `1070`, `1183`, `37`, `48`, `89` | `fuel_lvl` | `io_1066`, `io_1070`, `io_1183`, `io_37` (+2) | Sensor `3` (Fuel level in litters), Sensor `4` (Niveau de carburant), Sensor `39` (Consomation carburant) | Fuel level in tank read from CAN |
| 327 | `can.fuel.level.indicator.state` | `string` | `â€”` | `10428` | `can_fuel_lvl_indicator_st` | `io_10428` | â€” | Vehicle parameter for fuel level indicator read from CAN |
| 328 | `can.fuel.level.low.indicator.status` | `boolean` | `â€”` | `123`, `38` | `can_fuel_lvl_low_indicator_stat` | `io_123`, `io_38` | â€” | Low fuel level indicator status, read from CAN |
| 329 | `can.fuel.low.indicator.status` | `boolean` | `â€”` | `519`, `968` | `can_fuel_low_indicator_stat` | `io_519`, `io_968` | â€” | CAN low fuel indicator is on |
| 330 | `can.fuel.pressure` | `number` | `â€”` | `34` | `can_fuel_press` | `io_34` | â€” | Fuel pressure read from CAN |
| 331 | `can.fuel.type.enum` | `number` | `â€”` | `759` | `can_fuel_type_enum` | `io_759` | â€” | Fuel type read from CAN |
| 332 | `can.fuel.volume` | `number` | `â€”` | `34`, `390`, `84` | `can_fuel_volume` | `io_34`, `io_390`, `io_84` | â€” | CAN fuel volume |
| 333 | `can.full.charge.time` | `number` | `â€”` | `1146` | `can_full_charge_time` | `io_1146` | â€” | Time to full charge from CAN bus |
| 334 | `can.gas.fuel.consumed` | `number` | `â€”` | `974` | `can_gas_fuel_consumed` | `io_974` | â€” | Natural gas fuel amount totally consumed by vehicle read from CAN |
| 335 | `can.gear.current` | `number` | `â€”` | `1332` | `can_gear_current` | `io_1332` | â€” | Current gear read from CAN (J1939 transmission actual gear) |
| 336 | `can.gear.selected` | `number` | `â€”` | `1331` | `can_gear_selected` | `io_1331` | â€” | Selected gear read from CAN (J1939 transmission requested gear) |
| 337 | `can.glow.plug.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `970` | `can_glow_plug_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_970` | â€” | Glow plug indicator status, read from CAN |
| 338 | `can.grain.auger.speed.status` | `boolean` | `â€”` | `520` | `can_grain_auger_speed_stat` | `io_520` | â€” | Grain auger speed normal status, read from CAN: true - Ok, false - below normal |
| 339 | `can.grain.header.connected.status` | `boolean` | `â€”` | `520` | `can_grain_header_connected_stat` | `io_520` | â€” | Grain header connected status, read from CAN |
| 340 | `can.grain.release.status` | `boolean` | `â€”` | `520` | `can_grain_release_stat` | `io_520` | â€” | Grain release from hopper is turned on status, read from CAN |
| 341 | `can.grain.tank.70.percent.event` | `boolean` | `â€”` | `520` | `can_grain_tank_70_percent_event` | `io_520` | â€” | Grain task is 70% full event, read from CAN |
| 342 | `can.grain.tank.full.event` | `boolean` | `â€”` | `520` | `can_grain_tank_full_event` | `io_520` | â€” | Grain tank is full event, read from CAN |
| 343 | `can.grain.tank.opened.status` | `boolean` | `â€”` | `520` | `can_grain_tank_opened_stat` | `io_520` | â€” | Grain task is opened status, read from CAN |
| 344 | `can.gross.combination.vehicle.weight` | `number` | `â€”` | `10899` | `can_gross_combination_vhc_weight` | `io_10899` | â€” | Gross combination vehicle weight read from CAN |
| 345 | `can.handbrake.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `961` | `can_handbrake_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_961` | â€” | Status of handbrake system indicator, read from CAN |
| 346 | `can.handbrake.status` | `boolean` | `â€”` | `132`, `47`, `517`, `653` | `can_handbrake_stat` | `io_132`, `io_47`, `io_517`, `io_653` | â€” | CAN handbrake is pulled up |
| 347 | `can.handlebar.lock.status` | `boolean` | `â€”` | `1127` | `can_handlebar_lock_stat` | `io_1127` | â€” | Handlebar lock status from CAN bus |
| 348 | `can.hatch.open.indicator.state` | `string` | `â€”` | `10428` | `can_hatch_open_indicator_st` | `io_10428` | â€” | Vehicle parameter for hatch open indicator read from CAN |
| 349 | `can.hazard.warning.indicator.state` | `string` | `â€”` | `10428` | `can_hazard_warning_indicator_st` | `io_10428` | â€” | Vehicle parameter for hazard warning indicator read from CAN |
| 350 | `can.height.control.indicator.state` | `string` | `â€”` | `10430` | `can_height_control_indicator_st` | `io_10430` | â€” | Vehicle parameter for height control (levelling) indicator read from CAN |
| 351 | `can.high.beam.indicator.state` | `string` | `â€”` | `10428` | `can_high_beam_indicator_st` | `io_10428` | â€” | Vehicle parameter for high beam/main beam indicator read from CAN |
| 352 | `can.high.beam.status` | `boolean` | `â€”` | `123`, `38`, `518`, `930` | `can_high_beam_stat` | `io_123`, `io_38`, `io_518`, `io_930` | â€” | CAN high beams are on |
| 353 | `can.highest.battery2.temperature` | `number` | `â€”` | `1183` | `can_highest_battery2_temp` | `io_1183` | â€” | Highest battery 2 temperature from CAN bus |
| 354 | `can.highest.battery2.voltage` | `number` | `â€”` | `1185` | `can_highest_battery2_vlt` | `io_1185` | â€” | Highest battery 2 voltage from CAN bus |
| 355 | `can.highest.battery.code` | `string` | `â€”` | `1137` | `can_highest_bat_code` | `io_1137` | â€” | Highest battery ID code from CAN bus |
| 356 | `can.highest.battery.temperature` | `number` | `â€”` | `1142` | `can_highest_bat_temp` | `io_1142` | â€” | Highest battery temperature from CAN bus |
| 357 | `can.highest.battery.temperature.code` | `string` | `â€”` | `1143` | `can_highest_bat_temp_code` | `io_1143` | â€” | Highest temperature battery ID code from CAN bus |
| 358 | `can.highest.battery.voltage` | `number` | `â€”` | `1136` | `can_highest_bat_vlt` | `io_1136` | â€” | Highest battery voltage from CAN bus |
| 359 | `can.highest.mismatch.code` | `string` | `â€”` | `1139` | `can_highest_mismatch_code` | `io_1139` | â€” | Highest mismatch ID code from CAN bus |
| 360 | `can.highest.mismatch.voltage` | `number` | `â€”` | `1138` | `can_highest_mismatch_vlt` | `io_1138` | â€” | Highest mismatch voltage from CAN bus |
| 361 | `can.high.voltage.system.caution.indicator.state` | `string` | `â€”` | `13259` | `can_high_vlt_system_caution_indicator_st` | `io_13259` | â€” | Vehicle parameter for high voltage system caution indicator read from CAN |
| 362 | `can.hood.status` | `boolean` | `â€”` | `132`, `143`, `47`, `517`, `90`, `913` | `can_hood_stat` | `io_132`, `io_143`, `io_47`, `io_517` (+2) | â€” | CAN hood is opened |
| 363 | `can.hybrid.battery.capacity` | `number` | `â€”` | `1382` | `can_hybrid_bat_capacity` | `io_1382` | â€” | OEM HV Battery Max Energy read from CAN |
| 364 | `can.hybrid.battery.current` | `number` | `â€”` | `1380` | `can_hybrid_bat_current` | `io_1380` | â€” | OEM HV Battery Current read from CAN |
| 365 | `can.hybrid.battery.max.cell.voltage` | `number` | `â€”` | `1379` | `can_hybrid_bat_max_cell_vlt` | `io_1379` | â€” | OEM HV Battery Max Cell Voltage read from CAN |
| 366 | `can.hybrid.battery.max.temperature` | `number` | `â€”` | `1387` | `can_hybrid_bat_max_temp` | `io_1387` | â€” | OEM HV Battery Max Cell Temperature read from CAN |
| 367 | `can.hybrid.battery.measured.capacity` | `number` | `â€”` | `1383` | `can_hybrid_bat_measured_capacity` | `io_1383` | â€” | OEM HV Battery Measured Energy read from CAN |
| 368 | `can.hybrid.battery.min.cell.voltage` | `number` | `â€”` | `1378` | `can_hybrid_bat_min_cell_vlt` | `io_1378` | â€” | OEM HV Battery Min Cell Voltage read from CAN |
| 369 | `can.hybrid.battery.min.temperature` | `number` | `â€”` | `1386` | `can_hybrid_bat_min_temp` | `io_1386` | â€” | OEM HV Battery Min Cell Temperature read from CAN |
| 370 | `can.hybrid.battery.pack.life` | `number` | `â€”` | `57` | `can_hybrid_bat_pack_life` | `io_57` | â€” | Hybrid battery pack remaining life |
| 371 | `can.hybrid.battery.voltage` | `number` | `â€”` | `1381` | `can_hybrid_bat_vlt` | `io_1381` | â€” | OEM HV Battery High Voltage read from CAN |
| 372 | `can.hybrid.onboard.current` | `number` | `â€”` | `544` | `can_hybrid_onboard_current` | `io_544` | â€” | Hybrid vehicle system current |
| 373 | `can.hybrid.onboard.power.voltage` | `number` | `â€”` | `543` | `can_hybrid_onboard_power_vlt` | `io_543` | â€” | Hybrid vehicle system voltage |
| 374 | `can.hydraulics.chamber.oil.overflow.indicator.status` | `boolean` | `â€”` | `519`, `981` | `can_hydraulics_chamber_oil_overflow_indicator_stat` | `io_519`, `io_981` | â€” | Oil overflow in hydraulic chamber indicator from CAN bus |
| 375 | `can.hydraulics.high.temperature.status` | `boolean` | `â€”` | `519`, `520`, `980` | `can_hydraulics_high_temp_stat` | `io_519`, `io_520`, `io_980` | â€” | High temperature of drive system hydraulics (>86 degrees), reaed from CAN |
| 376 | `can.hydraulics.low.temperature.status` | `boolean` | `â€”` | `520` | `can_hydraulics_low_temp_stat` | `io_520` | â€” | Low temperature of drive system hydraulics (<5 degrees), read from CAN |
| 377 | `can.hydraulics.oil.filter.plugged.indicator.status` | `boolean` | `â€”` | `519`, `977` | `can_hydraulics_oil_filter_plugged_indicator_stat` | `io_519`, `io_977` | â€” | Hydraulic system oil filter plugged indicator from CAN bus |
| 378 | `can.hydraulics.oil.level.low.indicator.status` | `boolean` | `â€”` | `519`, `979` | `can_hydraulics_oil_lvl_low_indicator_stat` | `io_519`, `io_979` | â€” | Hydraulic oil low level indicator from CAN bus |
| 379 | `can.hydraulics.pressure.low.status` | `boolean` | `â€”` | `519`, `978` | `can_hydraulics_press_low_stat` | `io_519`, `io_978` | â€” | Hydraulic system low pressure indicator from CAN bus |
| 380 | `can.ignition.key.status` | `boolean` | `â€”` | `132`, `47`, `517`, `652` | `can_ignition_key_stat` | `io_132`, `io_47`, `io_517`, `io_652` | â€” | The key is in ignition lock status, read from CAN |
| 381 | `can.intake.air.pressure` | `number` | `â€”` | `1048` | `can_intake_air_press` | `io_1048` | â€” | Absolute air pressure at input port to intake manifold or air box |
| 382 | `can.intake.air.temperature` | `number` | `â€”` | `39` | `can_intake_air_temp` | `io_39` | â€” | Intake air temperature |
| 383 | `can.intake.map` | `number` | `â€”` | `35`, `542` | `can_intake_map` | `io_35`, `io_542` | â€” | Intake manifold absolute pressure |
| 384 | `can.interlock.active` | `boolean` | `â€”` | `517`, `906` | `can_interlock_active` | `io_517`, `io_906` | â€” | Interlock active status, read from CAN |
| 385 | `can.kneeling.indicator.state` | `string` | `â€”` | `10430` | `can_kneeling_indicator_st` | `io_10430` | â€” | Vehicle parameter for kneeling indicator read from CAN |
| 386 | `can.lane.departure.indication.indicator.state` | `string` | `â€”` | `10431` | `can_lane_departure_indication_indicator_st` | `io_10431` | â€” | Vehicle parameter for lane departure indication read from CAN |
| 387 | `can.lane.departure.warning.off.indicator.state` | `string` | `â€”` | `10431` | `can_lane_departure_warning_off_indicator_st` | `io_10431` | â€” | Vehicle parameter for lane departure warning switched off indicator read from CAN |
| 388 | `can.left.joystick.back.event` | `boolean` | `â€”` | `520` | `can_left_joystick_back_event` | `io_520` | â€” | Left joystick moved back active, read from CAN |
| 389 | `can.left.joystick.forward.event` | `boolean` | `â€”` | `520` | `can_left_joystick_forward_event` | `io_520` | â€” | Left joystick moved forward active, read from CAN |
| 390 | `can.left.joystick.left.event` | `boolean` | `â€”` | `520` | `can_left_joystick_left_event` | `io_520` | â€” | Left joystick moved left active, read from CAN |
| 391 | `can.left.joystick.right.event` | `boolean` | `â€”` | `520` | `can_left_joystick_right_event` | `io_520` | â€” | Left joystick moved right active, read from CAN |
| 392 | `can.lights.failure.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `965` | `can_lights_failure_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_965` | â€” | Lights failure indicator status, read from CAN |
| 393 | `can.lights.hazard.lights.status` | `boolean` | `â€”` | `132`, `47`, `517`, `912` | `can_lights_hazard_lights_stat` | `io_132`, `io_47`, `io_517`, `io_912` | â€” | CAN lights info hazard lights status |
| 394 | `can.light.signal.status` | `boolean` | `â€”` | `518`, `935` | `can_light_signal_stat` | `io_518`, `io_935` | â€” | Light signal turned on status, read from CAN |
| 395 | `can.low.beam.indicator.state` | `string` | `â€”` | `10428` | `can_low_beam_indicator_st` | `io_10428` | â€” | Vehicle parameter for low beam/dipped beam indicator read from CAN |
| 396 | `can.low.beam.status` | `boolean` | `â€”` | `123`, `38`, `518`, `929` | `can_low_beam_stat` | `io_123`, `io_38`, `io_518`, `io_929` | â€” | CAN low beams are on |
| 397 | `can.lowering.indicator.state` | `string` | `â€”` | `10430` | `can_lowering_indicator_st` | `io_10430` | â€” | Vehicle parameter for lowering indicator read from CAN |
| 398 | `can.lowest.battery2.temperature` | `number` | `â€”` | `1182` | `can_lowest_battery2_temp` | `io_1182` | â€” | Lowest battery 2 voltage from CAN bus |
| 399 | `can.lowest.battery2.voltage` | `number` | `â€”` | `1184` | `can_lowest_battery2_vlt` | `io_1184` | â€” | Lowest battery 2 voltage from CAN bus |
| 400 | `can.lowest.battery.code` | `string` | `â€”` | `1135` | `can_lowest_bat_code` | `io_1135` | â€” | Lowest battery ID code from CAN bus |
| 401 | `can.lowest.battery.temperature` | `number` | `â€”` | `1140` | `can_lowest_bat_temp` | `io_1140` | â€” | Lowest battery temperature from CAN bus |
| 402 | `can.lowest.battery.temperature.code` | `string` | `â€”` | `1141` | `can_lowest_bat_temp_code` | `io_1141` | â€” | Lowest temperature battery ID code from CAN bus |
| 403 | `can.lowest.battery.voltage` | `number` | `â€”` | `1134` | `can_lowest_bat_vlt` | `io_1134` | â€” | Lowest Battery Voltage from CAN bus |
| 404 | `can.lpg.fuel.status` | `boolean` | `â€”` | `1084` | `can_lpg_fuel_stat` | `io_1084` | â€” | Engine working on LPG fuel status, read from CAN bus |
| 405 | `can.maf.air.flow.rate` | `number` | `â€”` | `40` | `can_maf_air_flow_rate` | `io_40` | â€” | MAF air flow rate read from CAN |
| 406 | `can.maintenance.required.status` | `boolean` | `â€”` | `123`, `38`, `519`, `969` | `can_maintenance_required_stat` | `io_123`, `io_38`, `io_519`, `io_969` | â€” | Maintenance required status, read from CAN |
| 407 | `can.major.version` | `string` | `â€”` | `1156` | `can_major_version` | `io_1156` | â€” | Major version from CAN bus in hex form |
| 408 | `can.malfunction.general.failure.indicator.state` | `string` | `â€”` | `10429` | `can_malfunction_general_failure_indicator_st` | `io_10429` | â€” | Vehicle parameter for malfunction/general failure indicator read from CAN |
| 409 | `can.manual.retarder.status` | `boolean` | `â€”` | `123`, `38`, `518`, `939` | `can_manual_retarder_stat` | `io_123`, `io_38`, `io_518`, `io_939` | â€” | Manual retarder status, read from CAN |
| 410 | `can.max.available.power` | `number` | `â€”` | `1126` | `can_max_available_power` | `io_1126` | â€” | Maximum available power from CAN bus |
| 411 | `can.max.charge.current` | `number` | `â€”` | `1181` | `can_max_charge_current` | `io_1181` | â€” | Max charge current from CAN bus |
| 412 | `can.max.discharge.current` | `number` | `â€”` | `1149` | `can_max_discharge_current` | `io_1149` | â€” | Max discharge current from CAN bus |
| 413 | `can.mil.mileage` | `number` | `â€”` | `43` | `can_mil_mileage` | `io_43` | â€” | Distance traveled while malfunction indicator lamp is activated, read from CAN |
| 414 | `can.mil.status` | `boolean` | `â€”` | `10349`, `519`, `953` | `can_mil_stat` | `io_10349`, `io_519`, `io_953` | Sensor `84` (Voyant dÃ©faut moteur MIL) | Malfunction indicator lamp status read from CAN |
| 415 | `can.mil.time` | `number` | `â€”` | `54` | `can_mil_time` | `io_54` | â€” | Time run with malfunction indicator lamp activated, read from CAN |
| 416 | `can.minor.version` | `string` | `â€”` | `1157` | `can_minor_version` | `io_1157` | â€” | Minor version from CAN bus in hex form |
| 417 | `can.module.id` | `number` | `â€”` | `101`, `13` | `can_module_id` | `io_101`, `io_13` | â€” | CAN module ID |
| 418 | `can.module.id.hex` | `string` | `â€”` | `388`, `529` | `can_module_id_hex` | `io_388`, `io_529` | â€” | CAN module ID in HEX format |
| 419 | `can.module.sleep.mode` | `boolean` | `â€”` | `132`, `47`, `517`, `924` | `can_module_sleep_mode` | `io_132`, `io_47`, `io_517`, `io_924` | â€” | CAN module goes to the sleep mode |
| 420 | `can.motor.failures.indicator.state` | `string` | `â€”` | `13259` | `can_motor_failures_indicator_st` | `io_13259` | â€” | Vehicle parameter for electric motor failures indicator read from CAN |
| 421 | `can.motor.limited.performance.indicator.state` | `string` | `â€”` | `13259` | `can_motor_limited_performance_indicator_st` | `io_13259` | â€” | Vehicle parameter for limited performance electric motor indicator read from CAN |
| 422 | `can.motor.status` | `boolean` | `â€”` | `517`, `916` | `can_motor_stat` | `io_517`, `io_916` | â€” | Electric motor status |
| 423 | `can.mowing.status` | `boolean` | `â€”` | `520` | `can_mowing_stat` | `io_520` | â€” | Mowing is active status, read from CAN bus |
| 424 | `can.multiplex.system.indicator.state` | `string` | `â€”` | `13259` | `can_multiplex_system_indicator_st` | `io_13259` | â€” | Vehicle parameter for multiplex system indicator read from CAN bus |
| 425 | `can.neutral.gear.status` | `boolean` | `â€”` | `517`, `659` | `can_neutral_gear_stat` | `io_517`, `io_659` | â€” | CAN neutral gear is on |
| 426 | `can.oil.level.low.indicator.status` | `boolean` | `â€”` | `235`, `519`, `958` | `can_oil_lvl_low_indicator_stat` | `io_235`, `io_519`, `io_958` | â€” | Oil level low indicator status read from CAN bus |
| 427 | `can.oil.pressure.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `974` | `can_oil_press_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_974` | â€” | Oil pressure indicator status read from CAN bus |
| 428 | `can.oil.service.mileage` | `number` | `â€”` | `864` | `can_oil_service_mileage` | `io_864` | â€” | Distance to next oil service |
| 429 | `can.oil.service.time` | `number` | `â€”` | `865` | `can_oil_service_time` | `io_865` | â€” | Time to next oil service |
| 430 | `can.operator.present.status` | `boolean` | `â€”` | `517`, `905` | `can_operator_present_stat` | `io_517`, `io_905` | â€” | Operator is present status, read from CAN bus |
| 431 | `can.park.heating.indicator.state` | `string` | `â€”` | `10429` | `can_park_heating_indicator_st` | `io_10429` | â€” | Vehicle parameter for park heating indicator read from CAN |
| 432 | `can.parking.brake.indicator.state` | `string` | `â€”` | `10428` | `can_parking_brake_indicator_st` | `io_10428` | â€” | Vehicle parameter for parking brake indicator read from CAN |
| 433 | `can.parking.brake.status` | `boolean` | `â€”` | `1179` | `can_parking_brake_stat` | `io_1179` | â€” | Parking break status from CAN |
| 434 | `can.parking.lights.status` | `boolean` | `â€”` | `123`, `38`, `518`, `928` | `can_parking_lights_stat` | `io_123`, `io_38`, `io_518`, `io_928` | â€” | Parking light status, read from CAN |
| 435 | `can.parking.status` | `boolean` | `â€”` | `132`, `47`, `517`, `660` | `can_parking_stat` | `io_132`, `io_47`, `io_517`, `io_660` | â€” | Parking is activated for automatic gearbox, read from CAN |
| 436 | `can.part.charge.capacity` | `number` | `â€”` | `1153` | `can_part_charge_capacity` | `io_1153` | â€” | Part charge capacity |
| 437 | `can.passenger.seatbelt.indicator.status` | `boolean` | `â€”` | `123`, `38` | `can_passenger_seatbelt_indicator_stat` | `io_123`, `io_38` | â€” | Passenger seatbelt indicator status read from CAN |
| 438 | `can.patch.version` | `string` | `â€”` | `1158` | `can_patch_version` | `io_1158` | â€” | Patch version from CAN bus in hex form |
| 439 | `can.pedal.brake.status` | `boolean` | `â€”` | `132`, `47`, `517`, `79`, `816`, `910` | `can_pedal_brake_stat` | `io_132`, `io_47`, `io_517`, `io_79` (+2) | Sensor `33` (Interrupteur de frien) | Footbrake pedal is depressed, read from CAN |
| 440 | `can.pedal.clutch.status` | `boolean` | `â€”` | `517`, `82`, `911` | `can_pedal_clutch_stat` | `io_517`, `io_82`, `io_911` | Sensor `10` (Interrupteur d'embrayage) | CAN clutch pedal pressed |
| 441 | `can.position.lights.indicator.state` | `string` | `â€”` | `10428` | `can_pos_lights_indicator_st` | `io_10428` | â€” | Vehicle parameter for position lights/side lights indicator read from CAN |
| 442 | `can.powersource.takeoff.enum` | `number` | `â€”` | `83` | `can_pwrs_takeoff_enum` | `io_83` | â€” | CAN power takeoff bitmask |
| 443 | `can.pram.request.indicator.state` | `string` | `â€”` | `10430` | `can_pram_req_indicator_st` | `io_10430` | â€” | Vehicle parameter for pram request indicator read from CAN |
| 444 | `can.pressure.filter.cloged.status` | `boolean` | `â€”` | `520` | `can_press_filter_cloged_stat` | `io_520` | â€” | Pressure filter of the hydraulic pump is clogged, read from CAN |
| 445 | `can.private.status` | `boolean` | `â€”` | `132`, `47`, `517`, `904` | `can_private_stat` | `io_132`, `io_47`, `io_517`, `io_904` | â€” | Vehicle works in private mode, read from CAN bus |
| 446 | `can.program.id` | `number` | `â€”` | `100`, `12` | `can_program_id` | `io_100`, `io_12` | â€” | CAN program number |
| 447 | `can.pto.status` | `boolean` | `â€”` | `518`, `946` | `can_pto_stat` | `io_518`, `io_946` | â€” | Power take-off status, read from CAN |
| 448 | `can.pumping.torque` | `number` | `â€”` | `944` | `can_pumping_torque` | `io_944` | â€” | Estimated pumping - percent torque |
| 449 | `can.raising.indicator.state` | `string` | `â€”` | `10430` | `can_raising_indicator_st` | `io_10430` | â€” | Vehicle parameter for raising indicator read from CAN |
| 450 | `can.ready.to.drive.indicator.status` | `boolean` | `â€”` | `123`, `38`, `517`, `902` | `can_ready_to_drive_indicator_stat` | `io_123`, `io_38`, `io_517`, `io_902` | â€” | Ready to drive indicator status, read from CAN |
| 451 | `can.rear.brake.status` | `boolean` | `â€”` | `1128` | `can_rear_brake_stat` | `io_1128` | â€” | Rear brake status from CAN bus |
| 452 | `can.rear.central.seatbelt.status` | `boolean` | `â€”` | `518`, `944` | `can_rear_central_seatbelt_stat` | `io_518`, `io_944` | â€” | Rear central seatbelt fastened status, read from CAN |
| 453 | `can.rear.differential.status` | `boolean` | `â€”` | `518`, `948` | `can_rear_differential_stat` | `io_518`, `io_948` | â€” | Rear differential locked status, read from CAN |
| 454 | `can.rear.fog.light.indicator.state` | `string` | `â€”` | `10429` | `can_rear_fog_light_indicator_st` | `io_10429` | â€” | Vehicle parameter for rear fog light indicator read from CAN |
| 455 | `can.rear.fog.lights.status` | `boolean` | `â€”` | `123`, `38`, `518`, `931` | `can_rear_fog_lights_stat` | `io_123`, `io_38`, `io_518`, `io_931` | â€” | CAN rear fog lights are on |
| 456 | `can.rear.hydraulic.status` | `boolean` | `â€”` | `520` | `can_rear_hydraulic_stat` | `io_520` | â€” | Read hydraulic turned on status, read from CAN |
| 457 | `can.rear.left.door.status` | `boolean` | `â€”` | `132`, `143`, `47`, `517`, `656`, `90` | `can_rear_left_door_stat` | `io_132`, `io_143`, `io_47`, `io_517` (+2) | â€” | CAN rear left door is opened |
| 458 | `can.rear.left.seatbelt.status` | `boolean` | `â€”` | `518`, `942` | `can_rear_left_seatbelt_stat` | `io_518`, `io_942` | â€” | Rear left seatbelt fastened status, read from CAN |
| 459 | `can.rear.left.window.status` | `boolean` | `â€”` | `1213` | `can_rear_left_window_stat` | `io_1213` | â€” | CAN rear left window is opened |
| 460 | `can.rearm.signal.event` | `boolean` | `â€”` | `517`, `922` | `can_rearm_signal_event` | `io_517`, `io_922` | â€” | Rearm signal was sent |
| 461 | `can.rear.pto.status` | `boolean` | `â€”` | `520` | `can_rear_pto_stat` | `io_520` | â€” | Rear power take-off status turned on status, read from CAN |
| 462 | `can.rear.right.door.status` | `boolean` | `â€”` | `132`, `143`, `47`, `517`, `657`, `90` | `can_rear_right_door_stat` | `io_132`, `io_143`, `io_47`, `io_517` (+2) | â€” | CAN rear right door is opened |
| 463 | `can.rear.right.seatbelt.status` | `boolean` | `â€”` | `518`, `943` | `can_rear_right_seatbelt_stat` | `io_518`, `io_943` | â€” | Rear right seatbelt fastened status, read from CAN |
| 464 | `can.rear.right.window.status` | `boolean` | `â€”` | `1214` | `can_rear_right_window_stat` | `io_1214` | â€” | CAN rear right window is opened |
| 465 | `can.rear.three.point.hitch.status` | `boolean` | `â€”` | `520` | `can_rear_three_point_hitch_stat` | `io_520` | â€” | Rear three-point hitch turned on status, read from CAN |
| 466 | `can.recognized.batteries` | `number` | `â€”` | `1159` | `can_recognized_batteries` | `io_1159` | â€” | Recognized batteries from CAN bus |
| 467 | `can.recuperation.status` | `boolean` | `â€”` | `1150` | `can_recuperation_stat` | `io_1150` | â€” | Recuperation status from CAN bus |
| 468 | `can.relative.fuel.rail.pressure` | `number` | `â€”` | `44` | `can_relative_fuel_rail_press` | `io_44` | â€” | Fuel rail pressure relative to manifold vacuum |
| 469 | `can.remote.accelerator.pedal.position` | `number` | `â€”` | `937` | `can_remote_accelerator_pedal_pos` | `io_937` | â€” | The ratio of actual position of the remote analog engine speed/torque request input device (such as an accelerator pedal or throttle lever) to the maximum position of the input device |
| 470 | `can.request.engine.lock.event` | `boolean` | `â€”` | `517`, `908` | `can_req_eng_lock_event` | `io_517`, `io_908` | â€” | Request to lock the engine (activation after attempt to restart the engine) event |
| 471 | `can.retarder.indicator.state` | `string` | `â€”` | `10430` | `can_retarder_indicator_st` | `io_10430` | â€” | Vehicle parameter for retarder indicator read from CAN |
| 472 | `can.retarder.torque.load` | `number` | `â€”` | `188`, `522` | `can_retarder_torque_load` | `io_188`, `io_522` | â€” | Retarder torque load percentage read from CAN |
| 473 | `can.reverse.gear.status` | `boolean` | `â€”` | `132`, `47`, `517`, `661` | `can_reverse_gear_stat` | `io_132`, `io_47`, `io_517`, `io_661` | â€” | CAN reverse gear is on |
| 474 | `can.right.joystick.back.event` | `boolean` | `â€”` | `520` | `can_right_joystick_back_event` | `io_520` | â€” | Right joystick moved back active, read from CAN |
| 475 | `can.right.joystick.forward.event` | `boolean` | `â€”` | `520` | `can_right_joystick_forward_event` | `io_520` | â€” | Right joystick moved forward active, read from CAN |
| 476 | `can.right.joystick.left.event` | `boolean` | `â€”` | `520` | `can_right_joystick_left_event` | `io_520` | â€” | Right joystick moved left active, read from CAN |
| 477 | `can.right.joystick.right.event` | `boolean` | `â€”` | `520` | `can_right_joystick_right_event` | `io_520` | â€” | Right joystick moved right active, read from CAN |
| 478 | `can.road.speed.limit.state` | `number` | `â€”` | `932` | `can_road_speed_limit_st` | `io_932` | â€” | Road speed limit status |
| 479 | `can.roof.opened.status` | `boolean` | `â€”` | `517`, `909` | `can_roof_opened_stat` | `io_517`, `io_909` | â€” | Roof is opened status, read from CAN |
| 480 | `can.scr.thermal.management.state` | `number` | `â€”` | `942` | `can_scr_thermal_management_st` | `io_942` | â€” | SCR thermal management active |
| 481 | `can.seat.belt.indicator.state` | `string` | `â€”` | `10431` | `can_seat_belt_indicator_st` | `io_10431` | â€” | Vehicle parameter for seat belt indicator read from CAN |
| 482 | `can.seatbelt.status` | `boolean` | `â€”` | `10885` | `can_seatbelt_stat` | `io_10885` | â€” | Seatbelt status read from CAN, false - the belt is not buckled, true - the belt is buckled |
| 483 | `can.service.last.mileage` | `number` | `â€”` | `860` | `can_service_last_mileage` | `io_860` | â€” | Distance from last service |
| 484 | `can.service.last.time` | `number` | `â€”` | `863` | `can_service_last_time` | `io_863` | â€” | Time from last serivce |
| 485 | `can.service.maintenance.indicator.state` | `string` | `â€”` | `10429` | `can_service_maintenance_indicator_st` | `io_10429` | â€” | Vehicle parameter for service/call for maintenance indicator read from CAN |
| 486 | `can.service.mileage` | `number` | `â€”` | `113`, `400`, `402` | `can_service_mileage` | `io_113`, `io_400`, `io_402` | Sensor `23` (Distance de service) | Service distance read from CAN |
| 487 | `can.service.required.mileage` | `number` | `â€”` | `859` | `can_service_required_mileage` | `io_859` | â€” | Distance from need of service |
| 488 | `can.service.required.time` | `number` | `â€”` | `862` | `can_service_required_time` | `io_862` | â€” | Time from need of service |
| 489 | `can.service.time` | `number` | `â€”` | `861` | `can_service_time` | `io_861` | â€” | Time to next service |
| 490 | `can.short.fuel.trim` | `number` | `â€”` | `33` | `can_short_fuel_trim` | `io_33` | â€” | Short term fuel trim read from CAN |
| 491 | `can.sn.high` | `string` | `â€”` | `1132` | `can_sn_high` | `io_1132` | â€” | SN High from CAN bus |
| 492 | `can.sn.low` | `string` | `â€”` | `1133` | `can_sn_low` | `io_1133` | â€” | SN Low from CAN bus |
| 493 | `can.soc.switch.level` | `number` | `â€”` | `1152` | `can_soc_switch_lvl` | `io_1152` | â€” | SoC switch level from CAN bus |
| 494 | `can.soot.filter.indicator.status` | `boolean` | `â€”` | `123`, `38` | `can_soot_filter_indicator_stat` | `io_123`, `io_38` | â€” | DPF/FAP soot filter indicator status, read from CAN |
| 495 | `can.spreader.working.hours` | `number` | `â€”` | `185`, `519` | `can_spreader_working_hours` | `io_185`, `io_519` | â€” | Salt spreader working hours read from CAN |
| 496 | `can.standalone.engine` | `boolean` | `â€”` | `517`, `901` | `can_standalone_eng` | `io_517`, `io_901` | â€” | Standalone engine status read from CAN |
| 497 | `can.start.stop.inactive.status` | `boolean` | `â€”` | `1086` | `can_start_stop_inactive_stat` | `io_1086` | â€” | Start-stop system inactive status read from CAN bus |
| 498 | `can.steering.failure.indicator.state` | `string` | `â€”` | `10430` | `can_steering_failure_indicator_st` | `io_10430` | â€” | Vehicle parameter for steering failure indicator read from CAN |
| 499 | `can.steering.fluid.level.indicator.state` | `string` | `â€”` | `10429` | `can_steering_fluid_lvl_indicator_st` | `io_10429` | â€” | Vehicle parameter for steering fluid level indicator read from CAN |
| 500 | `can.stop.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `957` | `can_stop_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_957` | â€” | STOP indicator status read from CAN |
| 501 | `can.stop.request.indicator.state` | `string` | `â€”` | `10430` | `can_stop_req_indicator_st` | `io_10430` | â€” | Vehicle parameter for stop request indicator read from CAN |
| 502 | `can.straw.chopper.speed.status` | `boolean` | `â€”` | `520` | `can_straw_chopper_speed_stat` | `io_520` | â€” | Straw chopper speed normal status, read from CAN: true - Ok, false - below normal |
| 503 | `can.straw.chopper.status` | `boolean` | `â€”` | `520` | `can_straw_chopper_stat` | `io_520` | â€” | Straw chopper switched on status, read from CAN |
| 504 | `can.straw.shaker.speed.status` | `boolean` | `â€”` | `520` | `can_straw_shaker_speed_stat` | `io_520` | â€” | Straw shaler speed normal status, read from CAN: true - Ok, false - below normal |
| 505 | `can.straw.walker.clogged.status` | `boolean` | `â€”` | `520` | `can_straw_walker_clogged_stat` | `io_520` | â€” | Straw walker is clogged status, read from CAN |
| 506 | `can.switch.process.status` | `boolean` | `â€”` | `1151` | `can_switch_process_stat` | `io_1151` | â€” | Switch process status from CAN bus |
| 507 | `can.tachograph.indication.indicator.state` | `string` | `â€”` | `10431` | `can_tachograph_indication_indicator_st` | `io_10431` | â€” | Vehicle parameter for tachograph indication read from CAN |
| 508 | `can.threshing.drum.control.status` | `boolean` | `â€”` | `520` | `can_threshing_drum_control_stat` | `io_520` | â€” | Threshing drum status: true - on, false - off, read from CAN |
| 509 | `can.threshing.drum.excessive.clearance.status` | `boolean` | `â€”` | `520` | `can_threshing_drum_excessive_clearance_stat` | `io_520` | â€” | Excessive clearance under the threshing drum, read from CAN |
| 510 | `can.threshing.status` | `boolean` | `â€”` | `520` | `can_threshing_stat` | `io_520` | â€” | Threshing is active status, read from CAN |
| 511 | `can.throttle.pedal.level` | `number` | `â€”` | `1196`, `31`, `41`, `540`, `815`, `82`, `84` | `can_thrt_pedal_lvl` | `io_1196`, `io_31`, `io_41`, `io_540` (+3) | Sensor `36` (Position de la PÃ©dale d'accÃ©lÃ©ration), Sensor `46` (Frein Moteur activÃ©) | Throttle pedal push level read from CAN |
| 512 | `can.time.since.codes.cleared` | `number` | `â€”` | `55` | `can_time_since_codes_cleared` | `io_55` | â€” | Time since trouble codes cleared |
| 513 | `can.timing.advance` | `number` | `â€”` | `38` | `can_timing_advance` | `io_38` | â€” | Ignition timing advance read from CAN |
| 514 | `can.tire.failure.indicator.state` | `string` | `â€”` | `10429` | `can_tire_failure_indicator_st` | `io_10429` | â€” | Vehicle parameter for tire failure/malfunction indicator read from CAN |
| 515 | `can.tire.pressure` | `number` | `â€”` | `13160` | `can_tire_press` | `io_13160` | â€” | Aggregate vehicle tire pressure, read from CAN |
| 516 | `can.tire.pressure.low.status` | `boolean` | `â€”` | `123`, `38`, `519`, `966` | `can_tire_press_low_stat` | `io_123`, `io_38`, `io_519`, `io_966` | â€” | Tire pressure low status, read from CAN |
| 517 | `can.torque.current` | `number` | `â€”` | `1131` | `can_torque_current` | `io_1131` | â€” | Torque current from CAN bus |
| 518 | `can.total.cruise.control.time` | `number` | `â€”` | `189`, `523` | `can_total_cruise_control_time` | `io_189`, `io_523` | â€” | Total driving time when cruise control is ON, read from CAN |
| 519 | `can.total.engine.idle.time` | `number` | `â€”` | `1181` | `can_total_eng_idle_time` | `io_1181` | â€” | Time of engine running in idling status (vehicle stopped) since vehicle manufacture, read from CAN |
| 520 | `can.tracker.counted.fuel.consumed` | `number` | `â€”` | `107`, `17` | `can_tracker_counted_fuel_consumed` | `io_107`, `io_17` | â€” | Vehicle counted fuel consumed based on CAN-bus data |
| 521 | `can.tracker.counted.mileage` | `number` | `â€”` | `105`, `16` | `can_tracker_counted_mileage` | `io_105`, `io_16` | â€” | CAN-bus mileage counted by tracker after plug in |
| 522 | `can.trailer.axle.lift.status` | `boolean` | `â€”` | `518`, `951`, `952` | `can_trailer_axle_lift_stat` | `io_518`, `io_951`, `io_952` | â€” | Trailer axle lift status, read from CAN |
| 523 | `can.trailer.brake.high.temperature.indicator.status` | `boolean` | `â€”` | `519`, `990` | `can_trailer_brake_high_temp_indicator_stat` | `io_519`, `io_990` | â€” | High trailer brake temperature indicator from CAN bus |
| 524 | `can.trailer.connected.indicator.state` | `string` | `â€”` | `10431` | `can_trailer_connected_indicator_st` | `io_10431` | â€” | Vehicle parameter for trailer connected indicator read from CAN |
| 525 | `can.trailer.connected.status` | `boolean` | `â€”` | `1085` | `can_trailer_connected_stat` | `io_1085` | â€” | Trailer connected status read from CAN bus |
| 526 | `can.trailer.pneumatic.supply.incorrect.indicator.status` | `boolean` | `â€”` | `519`, `991` | `can_trailer_pneumatic_supply_incorrect_indicator_stat` | `io_519`, `io_991` | â€” | Incorrect trailer pneumatic supply indicator from CAN bus |
| 527 | `can.trailer.tire.pressure.low.status` | `boolean` | `â€”` | `519`, `988` | `can_trailer_tire_press_low_stat` | `io_519`, `io_988` | â€” | Low trailer tire pressure indicator from CAN bus |
| 528 | `can.trailer.vin` | `string` | `â€”` | `13671` | `can_trailer_vin` | `io_13671` | â€” | Trailer VIN number, read from CAN |
| 529 | `can.trailer.wear.brake.lining.indicator.status` | `boolean` | `â€”` | `519`, `989` | `can_trailer_wear_brake_lining_indicator_stat` | `io_519`, `io_989` | â€” | Wear of trailer brake lining indicator from CAN bus |
| 530 | `can.transmission.failure.indicator.state` | `string` | `â€”` | `10429` | `can_transmission_failure_indicator_st` | `io_10429` | â€” | Vehicle parameter for transmission failure/malfunction indicator read from CAN |
| 531 | `can.transmission.fluid.temperature.indicator.state` | `string` | `â€”` | `10429` | `can_transmission_fluid_temp_indicator_st` | `io_10429` | â€” | Vehicle parameter for transmission fluid temperature indicator read from CAN |
| 532 | `can.transmission.oil.temperature` | `number` | `â€”` | `1199` | `can_transmission_oil_temp` | `io_1199` | â€” | Transmission oil temperature reaed from CAN |
| 533 | `can.trip.fuel.consumed` | `number` | `â€”` | `1192` | `can_trip_fuel_consumed` | `io_1192` | â€” | Volume of liquid fuel consumed during the trip, read from CAN |
| 534 | `can.trip.vehicle.mileage` | `number` | `â€”` | `1186`, `989` | `can_trip_vhc_mileage` | `io_1186`, `io_989` | â€” | Distance travelled during all or part of a journey |
| 535 | `can.trunk.opening.remote.event` | `boolean` | `â€”` | `517`, `923` | `can_trunk_opening_remote_event` | `io_517`, `io_923` | â€” | Trunk was opened with remote control event, read from CAN |
| 536 | `can.trunk.status` | `boolean` | `â€”` | `132`, `143`, `47`, `517`, `658`, `90` | `can_trunk_stat` | `io_132`, `io_143`, `io_47`, `io_517` (+2) | â€” | CAN trunk is opened |
| 537 | `can.turn.signals.indicator.state` | `string` | `â€”` | `10428` | `can_turn_signals_indicator_st` | `io_10428` | â€” | Vehicle parameter for turn signals indicator read from CAN |
| 538 | `can.unloader.drive.status` | `boolean` | `â€”` | `520` | `can_unloader_drive_stat` | `io_520` | â€” | Unloader drive is on unloading tube pivot is in idle position, read from CAN |
| 539 | `can.vehicle.battery.charging.status` | `boolean` | `â€”` | `132`, `410`, `47`, `517`, `915` | `can_vhc_bat_charging_stat` | `io_132`, `io_410`, `io_47`, `io_517` (+1) | â€” | Vehicle battery charging status get from CAN Bus |
| 540 | `can.vehicle.battery.current` | `number` | `â€”` | `1113` | `can_vhc_bat_current` | `io_1113` | â€” | Vehicle battery current, read from CAN |
| 541 | `can.vehicle.battery.energy.consumed` | `number` | `â€”` | `1155`, `1388` | `can_vhc_bat_energy_consumed` | `io_1155`, `io_1388` | â€” | Energy consumed from the vehicle battery read from CAN |
| 542 | `can.vehicle.battery.energy.recuperated` | `number` | `â€”` | `1156` | `can_vhc_bat_energy_recuperated` | `io_1156` | â€” | Recuperated energy into the vehicle battery read from CAN |
| 543 | `can.vehicle.battery.health` | `number` | `â€”` | `10904`, `1151` | `can_vhc_bat_health` | `io_10904`, `io_1151` | â€” | Battery State of Health |
| 544 | `can.vehicle.battery.level` | `number` | `â€”` | `152`, `411` | `can_vhc_bat_lvl` | `io_152`, `io_411` | â€” | CAN-bus reported vehicle battery level for EV or HEV |
| 545 | `can.vehicle.battery.power` | `number` | `â€”` | `1157` | `can_vhc_bat_power` | `io_1157` | â€” | Vehicle battery power read from CAN |
| 546 | `can.vehicle.battery.power.consumption` | `number` | `â€”` | `412` | `can_vhc_bat_power_cons` | `io_412` | â€” | Vehicle battery power consumption read from CAN |
| 547 | `can.vehicle.battery.range` | `number` | `â€”` | `304`, `526` | `can_vhc_bat_range` | `io_304`, `io_526` | â€” | Vehicle Range on Battery, read from CAN |
| 548 | `can.vehicle.battery.remaining.range` | `number` | `â€”` | `10895` | `can_vhc_bat_remaining_range` | `io_10895` | â€” | Vehicle battery remaining range, read from CAN |
| 549 | `can.vehicle.battery.temperature` | `number` | `â€”` | `1152` | `can_vhc_bat_temp` | `io_1152` | â€” | Battery pack temperature, read from CAN |
| 550 | `can.vehicle.battery.total.charge.energy` | `number` | `â€”` | `1389` | `can_vhc_bat_total_charge_energy` | `io_1389` | â€” | Vehicle battery charged total energy, read from CAN |
| 551 | `can.vehicle.battery.voltage` | `number` | `â€”` | `1112` | `can_vhc_bat_vlt` | `io_1112` | â€” | Vehicle battery voltage, read from CAN |
| 552 | `can.vehicle.mileage` | `number` | `â€”` | `105`, `1176`, `36`, `389`, `87`, `990` | `can_vhc_mileage` | `io_105`, `io_1176`, `io_36`, `io_389` (+2) | â€” | Total vehicle mileage read from CAN |
| 553 | `can.vehicle.motorhours` | `number` | `â€”` | `993` | `can_vhc_motorhours` | `io_993` | â€” | Accumulated time of operation of vehicle |
| 554 | `can.vehicle.remaining.range` | `number` | `â€”` | `305`, `755`, `866` | `can_vhc_remaining_range` | `io_305`, `io_755`, `io_866` | â€” | Vehicle Range read, from CAN |
| 555 | `can.vehicle.speed` | `number` | `â€”` | `30`, `37`, `81`, `835` | `can_vhc_speed` | `io_30`, `io_37`, `io_81`, `io_835` | â€” | Vehicle speed read from CAN |
| 556 | `can.warning.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `964` | `can_warning_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_964` | â€” | Warning indicator status, read from CAN bus |
| 557 | `can.washer.fluid.level.low.indicator.status` | `boolean` | `â€”` | `519`, `986` | `can_washer_fluid_lvl_low_indicator_stat` | `io_519`, `io_986` | â€” | Low washer fluid level indicator, read from CAN bus |
| 558 | `can.water.in.fuel.indicator.status` | `boolean` | `â€”` | `519`, `984` | `can_water_in_fuel_indicator_stat` | `io_519`, `io_984` | â€” | Water in fuel indicator from CAN bus |
| 559 | `can.wear.brake.pads.indicator.status` | `boolean` | `â€”` | `123`, `38`, `519`, `967` | `can_wear_brake_pads_indicator_stat` | `io_123`, `io_38`, `io_519`, `io_967` | â€” | Wear brake pads indicator status, read from CAN bus |
| 560 | `can.webasto.status` | `boolean` | `â€”` | `132`, `47`, `517`, `899` | `can_webasto_stat` | `io_132`, `io_47`, `io_517`, `io_899` | â€” | Webasto status read from CAN bus |
| 561 | `can.wheel.speed` | `number` | `â€”` | `1019`, `80` | `can_wheel_speed` | `io_1019`, `io_80` | Sensor `28` (Vitesse BasÃ©e sur les Roues) | Vehicle wheel based speed, read from CAN bus |
| 562 | `can.windscreen.washer.fluid.indicator.state` | `string` | `â€”` | `10429` | `can_windscreen_washer_fluid_indicator_st` | `io_10429` | â€” | Vehicle parameter for windscreen/windshield washer fluid indicator read from CAN bus |
| 563 | `can.worn.brake.linings.indicator.state` | `string` | `â€”` | `10429` | `can_worn_brake_linings_indicator_st` | `io_10429` | â€” | Vehicle parameter for worn brake linings indicator read from CAN bus |
| 564 | `car.remote.control.state` | `number` | `â€”` | `132`, `47` | `car_remote_control_st` | `io_132`, `io_47` | â€” | State of the vehicle's factory remote control action |
| 565 | `central.standup.status` | `boolean` | `â€”` | `845` | `central_standup_stat` | `io_845` | â€” | Central stuandup up status: true - up, false - down |
| 566 | `channel.id` | `number` | `â€”` | *(Protocol / Header)* | `channel_id` | â€” | â€” | ID of channel that received a message |
| 567 | `charger.bms.timeout.status` | `boolean` | `â€”` | `807` | `charger_bms_timeout_stat` | `io_807` | â€” | Charger BMS COM timeout: true - not expired, false - expired |
| 568 | `charger.control.mode` | `number` | `â€”` | `806` | `charger_control_mode` | `io_806` | â€” | Charger control mode currently in use |
| 569 | `charger.crc.violation.status` | `boolean` | `â€”` | `808` | `charger_crc_violation_stat` | `io_808` | â€” | Charger CRC violation: true - violation happened, false - no violation |
| 570 | `charger.current` | `number` | `â€”` | `814` | `charger_current` | `io_814` | â€” | Charger actual current |
| 571 | `charger.energy` | `number` | `â€”` | `813` | `charger_energy` | `io_813` | â€” | Charger actual energy |
| 572 | `charger.fault.status` | `boolean` | `â€”` | `812` | `charger_fault_stat` | `io_812` | â€” | Charger internal fault status: true - no internal fault happened, false - internal fault happened |
| 573 | `charger.mc.violation.status` | `boolean` | `â€”` | `809` | `charger_mc_violation_stat` | `io_809` | â€” | Charger MC violation: true - violation happened, false - no violation |
| 574 | `charger.mode` | `boolean` | `â€”` | `802` | `charger_mode` | `io_802` | â€” | Selected charge mode, read from CAN: 0 - default, 1 - fast |
| 575 | `charger.mode.state` | `number` | `â€”` | `803` | `charger_mode_st` | `io_803` | â€” | Charger mode state |
| 576 | `charger.plug.status` | `boolean` | `â€”` | `817` | `charger_plug_stat` | `io_817` | â€” | Charger plug status |
| 577 | `charger.setpoint.current` | `number` | `â€”` | `805` | `charger_setpoint_current` | `io_805` | â€” | Charger current setpoint |
| 578 | `charger.setpoint.voltage` | `number` | `â€”` | `804` | `charger_setpoint_vlt` | `io_804` | â€” | Charger svoltage setpoint |
| 579 | `charger.state` | `number` | `â€”` | `810` | `charger_st` | `io_810` | â€” | Charger state |
| 580 | `charger.voltage` | `number` | `â€”` | `811` | `charger_vlt` | `io_811` | â€” | Charger actual voltage |
| 581 | `charge.time.remining` | `number` | `â€”` | `827` | `charge_time_remining` | `io_827` | â€” | Remaining charge time |
| 582 | `codec.id` | `number` | `â€”` | *(Protocol / Header)* | `codec_id` | â€” | â€” | Decimal representation for Teltonika Codec ID 1-byte, 0x8E = 142 for Codec 8 Extended. |
| 583 | `command.type` | `number` | `â€”` | *(Protocol / Header)* | `command_type` | â€” | â€” | Command type |
| 584 | `control.module.voltage` | `number` | `â€”` | `366` | `control_module_vlt` | `io_366` | â€” | Supply voltage of the central control (system driving voltage) |
| 585 | `counter.impulses` | `number` | `â€”` | `10912`, `10915`, `4`, `4`, `483`, `5`, `76` | `counter_impulses` | `io_10912`, `io_10915`, `io_4`, `io_4` (+3) | â€” | Impulses counter |
| 586 | `counter.impulses.frequency` | `number` | `â€”` | `10640`, `10642`, `10913`, `10916`, `622`, `623` | `counter_impulses_frequency` | `io_10640`, `io_10642`, `io_10913`, `io_10916` (+2) | â€” | Impulses counter frequency |
| 587 | `counter.impulses.rpm` | `number` | `â€”` | `10641`, `10643`, `10914`, `10917` | `counter_impulses_rpm` | `io_10641`, `io_10643`, `io_10914`, `io_10917` | â€” | Impulses counter RPM |
| 588 | `crash.accelerometer.status` | `boolean` | `â€”` | `1430` | `crash_accelerometer_stat` | `io_1430` | â€” | Crash accelerometer is calibrated |
| 589 | `crash.direction.enum` | `number` | `â€”` | `1430` | `crash_dir_enum` | `io_1430` | â€” | Crash direction - front, rear, left, right etc. |
| 590 | `crash.duration` | `number` | `â€”` | `1431` | `crash_dur` | `io_1431` | â€” | Crash duration |
| 591 | `crash.event` | `boolean` | `â€”` | `247` | `crash_event` | `io_247` | â€” | Crash event detected |
| 592 | `crash.event.enum` | `number` | `â€”` | `247` | `crash_event_enum` | `io_247` | Sensor `17` (Detecteur d'accident) | Crash report reason code |
| 593 | `crash.events.number` | `number` | `â€”` | `317` | `crash_events_num` | `io_317` | â€” | Crash event counter |
| 594 | `crash.impact.acceleration` | `number` | `â€”` | `1429` | `crash_impact_accel` | `io_1429` | â€” | Crash impact acceleration |
| 595 | `crash.max.acceleration` | `number` | `â€”` | `1432` | `crash_max_accel` | `io_1432` | â€” | Maximum acceleration (x or y) during crash |
| 596 | `custom` | `any` | `â€”` | *(Protocol / Header)* | `custom` | â€” | â€” | Any custom parameter |
| 597 | `deadman.alarm.status` | `boolean` | `â€”` | `315` | `deadman_alarm_stat` | `io_315` | â€” | Man down is active and no movement for configured timeout |
| 598 | `dead.reckoning.calibration.state` | `string` | `â€”` | `1433` | `dead_reckoning_calibration_st` | `io_1433` | â€” | Dead Reckoning Calibration Status |
| 599 | `dead.reckoning.calibration.state.enum` | `number` | `â€”` | `1433` | `dead_reckoning_calibration_st_enum` | `io_1433` | â€” | Dead Reckoning Calibration Status value |
| 600 | `dead.reckoning.straight.alignment` | `number` | `â€”` | `1435` | `dead_reckoning_straight_alignment` | `io_1435` | â€” | Dead Reckoning straight alignment progress, percent |
| 601 | `dead.reckoning.turning.alignment` | `number` | `â€”` | `1434` | `dead_reckoning_turning_alignment` | `io_1434` | â€” | Dead Reckoning turning alignment progress, percent |
| 602 | `device.configuration.id` | `number` | `â€”` | `22` | `device_configuration_id` | `io_22` | â€” | Configuration profile index |
| 603 | `device.id` | `number` | `â€”` | *(Protocol / Header)* | `device_id` | â€” | â€” | ID of device that received a message |
| 604 | `device.imei` | `string` | `â€”` | `1161` | `device_imei` | `io_1161` | â€” | IMEI of the device |
| 605 | `device.mounting.state` | `string` | `â€”` | `1452` | `device_mounting_st` | `io_1452` | â€” | Device mounting state |
| 606 | `device.mounting.state.enum` | `number` | `â€”` | `1452` | `device_mounting_st_enum` | `io_1452` | â€” | Device mounting state numeric code |
| 607 | `device.name` | `string` | `â€”` | *(Protocol / Header)* | `device_name` | â€” | â€” | Name of device that received a message |
| 608 | `device.serial.number` | `string` | `â€”` | `339` | `device_serial_num` | `io_339` | â€” | Device serial number |
| 609 | `device.temperature` | `number` | `â€”` | `362` | `device_temp` | `io_362` | â€” | Temperature of device |
| 610 | `device.type.id` | `number` | `â€”` | *(Protocol / Header)* | `device_type_id` | â€” | â€” | ID of device type of device that received a message |
| 611 | `device.uptime.records.count` | `number` | `â€”` | `108` | `device_uptime_records_count` | `io_108` | â€” | Number of records saved by the device since last power on |
| 612 | `din` | `number` | `â€”` | `1`, `1`, `1`, `14200`, `2`, `2`, `262`, `3`, `4` | `din` | `io_1`, `io_1`, `io_1`, `io_14200` (+5) | â€” | Digital inputs bitmask |
| 613 | `distance.since.refuel` | `number` | `â€”` | `1443` | `dist_since_refuel` | `io_1443` | â€” | Calculated distance covered after the latest refueling |
| 614 | `door.open.status` | `boolean` | `â€”` | `143`, `90` | `door_open_stat` | `io_143`, `io_90` | â€” | Door open status |
| 615 | `dout` | `number` | `â€”` | `10001`, `179`, `180`, `380`, `50`, `51` | `dout` | `io_10001`, `io_179`, `io_180`, `io_380` (+2) | â€” | Digital outputs bitmask |
| 616 | `dout.overcurrent.status` | `boolean` | `â€”` | `841`, `842`, `843` | `dout_overcurrent_stat` | `io_841`, `io_842`, `io_843` | â€” | Overcurrent status for digital output |
| 617 | `driver.first.name` | `string` | `â€”` | `10518`, `10520` | `driver_first_name` | `io_10518`, `io_10520` | â€” | Driver first name |
| 618 | `driver.last.name` | `string` | `â€”` | `10519`, `10521` | `driver_last_name` | `io_10519`, `io_10521` | â€” | Drvier lsat name |
| 619 | `driver.name` | `string` | `â€”` | `10518`, `10519`, `10520`, `10521` | `driver_name` | `io_10518`, `io_10519`, `io_10520`, `io_10521` | â€” | Driver name |
| 620 | `driver.status.enum` | `number` | `â€”` | `409` | `driver_stat_enum` | `io_409` | â€” | Driver status |
| 621 | `driving.state` | `number` | `â€”` | `830` | `driving_st` | `io_830` | â€” | Vehicle current driving direction state |
| 622 | `dsm.distraction.event` | `boolean` | `â€”` | `11701` | `dsm_distraction_event` | `io_11701` | â€” | Driver distraction event generated by Driver status monitoring system (DSM) |
| 623 | `dsm.driver.mask.event` | `boolean` | `â€”` | `11706` | `dsm_driver_mask_event` | `io_11706` | â€” | Driver wearing mask event generated by Driver status monitoring system (DSM) |
| 624 | `dsm.driver.missing.event` | `boolean` | `â€”` | `11705` | `dsm_driver_missing_event` | `io_11705` | â€” | Driver missing event generated by Driver status monitoring system (DSM) |
| 625 | `dsm.driver.phone.event` | `boolean` | `â€”` | `11703` | `dsm_driver_phone_event` | `io_11703` | â€” | Driver using the phone event generated by Driver status monitoring system (DSM) |
| 626 | `dsm.fatigue.event` | `boolean` | `â€”` | `11700` | `dsm_fatigue_event` | `io_11700` | â€” | Driver fatigue event generated by Driver status monitoring system (DSM) |
| 627 | `dsm.seatbelt.event` | `boolean` | `â€”` | `11713` | `dsm_seatbelt_event` | `io_11713` | â€” | Driver seatbelt event generated by Driver status monitoring system (DSM) |
| 628 | `dsm.smoking.event` | `boolean` | `â€”` | `11704` | `dsm_smoking_event` | `io_11704` | â€” | Driver smoking event generated by Driver status monitoring system (DSM) |
| 629 | `dsm.yawning.event` | `boolean` | `â€”` | `11702` | `dsm_yawning_event` | `io_11702` | â€” | Driver yawning event generated by Driver status monitoring system (DSM) |
| 630 | `eco.driving.event.duration` | `number` | `â€”` | `243`, `260` | `eco_driving_event_dur` | `io_243`, `io_260` | â€” | Duration of event that did generate Green driving |
| 631 | `eco.driving.events.number` | `number` | `â€”` | `10009`, `15` | `eco_driving_events_num` | `io_10009`, `io_15` | â€” | Average amount of events on some distance |
| 632 | `engine.ignition.on.duration` | `number` | `â€”` | `449` | `eng_ignition_on_dur` | `io_449` | â€” | Duration when engine is on |
| 633 | `engine.ignition.status` | `boolean` | `â€”` | `239`, `837` | `eng_ignition_stat` | `io_239`, `io_837` | Sensor `13` (Capteur demmarage moteur), Sensor `57` (Engine ignition) | Engine ignition or ACC status |
| 634 | `engine.motorhours` | `number` | `â€”` | `104` | `eng_motorhours` | `io_104` | â€” | Total calculated engine motorhours |
| 635 | `error.type` | `number` | `â€”` | `341` | `error_type` | `io_341` | â€” | Protocol-specific error identification number |
| 636 | `escort.lls.battery.voltage` | `number` | `â€”` | `271`, `274`, `277`, `280` | `escort_lls_bat_vlt` | `io_271`, `io_274`, `io_277`, `io_280` | â€” | Escort LLS Temperature |
| 637 | `escort.lls.temperature` | `number` | `â€”` | `269`, `272`, `275`, `278` | `escort_lls_temp` | `io_269`, `io_272`, `io_275`, `io_278` | â€” | Escort LLS Temperature |
| 638 | `escort.lls.value` | `number` | `â€”` | `270`, `273`, `276`, `279` | `escort_lls_value` | `io_270`, `io_273`, `io_276`, `io_279` | â€” | Escort LLS fuel level |
| 639 | `event.code` | `string` | `â€”` | `342` | `event_code` | `io_342` | â€” | Protocol-specific event code string |
| 640 | `event.enum` | `number` | `â€”` | *(Protocol / Header)* | `event_enum` | â€” | â€” | Protocol-specific event code |
| 641 | `event.priority.enum` | `number` | `â€”` | *(Protocol / Header)* | `event_priority_enum` | â€” | â€” | Event priority enum |
| 642 | `external.battery.capacity` | `number` | `â€”` | `375` | `ext_bat_capacity` | `io_375` | â€” | Current residual capacity percentage of external battery |
| 643 | `external.battery.firmware.version` | `string` | `â€”` | `370` | `ext_bat_firmware_version` | `io_370` | â€” | Firmware version of teltonika external battery |
| 644 | `external.battery.level` | `number` | `â€”` | `375` | `ext_bat_lvl` | `io_375` | â€” | External battery level |
| 645 | `external.battery.status` | `boolean` | `â€”` | `346` | `ext_bat_stat` | `io_346` | â€” | External battery status |
| 646 | `external.battery.temperature` | `number` | `â€”` | `365`, `367` | `ext_bat_temp` | `io_365`, `io_367` | â€” | External battery temperature |
| 647 | `external.battery.voltage` | `number` | `â€”` | `351` | `ext_bat_vlt` | `io_351` | â€” | External battery voltage |
| 648 | `external.powersource.status` | `boolean` | `â€”` | `252` | `ext_pwrs_stat` | `io_252` | â€” | External power source connection status |
| 649 | `external.powersource.voltage` | `number` | `â€”` | `66`, `800` | `ext_pwrs_vlt` | `io_66`, `io_800` | Sensor `14` (Voltage batterie) | External power voltage |
| 650 | `external.sensor.temperature` | `number` | `â€”` | `390` | `ext_sensor_temp` | `io_390` | â€” | External sensor temperature |
| 651 | `extnav.position.speed` | `number` | `â€”` | `355` | `extnav_pos_speed` | `io_355` | â€” | External receiver instant speed at position detection moment |
| 652 | `factory.alarm.actuated.status` | `boolean` | `â€”` | `132`, `47`, `517`, `918` | `factory_alarm_actuated_stat` | `io_132`, `io_47`, `io_517`, `io_918` | â€” | Factory-installed alarm system is actuated (is in panic mode) status |
| 653 | `factory.alarm.emulated.status` | `boolean` | `â€”` | `132`, `47`, `517`, `919` | `factory_alarm_emulated_stat` | `io_132`, `io_47`, `io_517`, `io_919` | â€” | Factory-installed alarm system is emulated by module status |
| 654 | `fall.status` | `boolean` | `â€”` | `242` | `fall_stat` | `io_242` | â€” | Device fall status true - device is falling, false - falling stopped |
| 655 | `fms.active.driver.id` | `string` | `â€”` | `12001` | `fms_active_driver_id` | `io_12001` | â€” | FMS Eco driving active driver ID |
| 656 | `fms.adblue.state.enum` | `number` | `â€”` | `229` | `fms_adblue_state_enum` | `io_229` | Sensor `85` (Ã‰tat AdBlue) | FMS AdBlue status: 0 - Off, 1 - Cond. Red, 2 - Cond. Yellow, 3 - Cond. info |
| 657 | `fms.braking.fuel.used` | `number` | `â€”` | `12017` | `fms_braking_fuel_used` | `io_12017` | â€” | FMS Eco driving Braking fuel used |
| 658 | `fms.braking.mileage` | `number` | `â€”` | `12016` | `fms_braking_mileage` | `io_12016` | â€” | FMS Eco driving Braking distance |
| 659 | `fms.braking.number` | `number` | `â€”` | `12019` | `fms_braking_num` | `io_12019` | â€” | FMS Eco driving Braking count |
| 660 | `fms.braking.time` | `number` | `â€”` | `12018` | `fms_braking_time` | `io_12018` | â€” | FMS Eco driving Braking time |
| 661 | `fms.coasting.fuel.used` | `number` | `â€”` | `12011` | `fms_coasting_fuel_used` | `io_12011` | â€” | FMS Eco driving coasting fuel used |
| 662 | `fms.coasting.mileage` | `number` | `â€”` | `12010` | `fms_coasting_mileage` | `io_12010` | â€” | FMS Eco driving coasting distance |
| 663 | `fms.coasting.time` | `number` | `â€”` | `12012` | `fms_coasting_time` | `io_12012` | â€” | FMS Eco driving coasting time |
| 664 | `fms.cruise.fuel.used` | `number` | `â€”` | `12024` | `fms_cruise_fuel_used` | `io_12024` | â€” | FMS Eco driving Cruise fuel used |
| 665 | `fms.cruise.mileage` | `number` | `â€”` | `12023` | `fms_cruise_mileage` | `io_12023` | â€” | FMS Eco driving Cruise distance |
| 666 | `fms.cruise.time` | `number` | `â€”` | `12025` | `fms_cruise_time` | `io_12025` | â€” | FMS Eco driving Cruise time |
| 667 | `fms.diagnostics.supported` | `number` | `â€”` | `110` | `fms_diagnostics_supported` | `io_110` | â€” | Indicates if FMS Gateway supports diagnositcs messages to FMS network. 0 - Diagnostics is not supported, 1 - Diagnostics is supported, 2 - Reserved, 3 - Do not care |
| 668 | `fms.driving.fuel.used` | `number` | `â€”` | `12032` | `fms_driving_fuel_used` | `io_12032` | â€” | FMS Eco driving fuel used while driving |
| 669 | `fms.ecoroll.fuel.used` | `number` | `â€”` | `12014` | `fms_ecoroll_fuel_used` | `io_12014` | â€” | FMS Eco driving EcoRoll fuel used |
| 670 | `fms.ecoroll.mileage` | `number` | `â€”` | `12013` | `fms_ecoroll_mileage` | `io_12013` | â€” | FMS Eco driving EcoRoll distance |
| 671 | `fms.ecoroll.time` | `number` | `â€”` | `12015` | `fms_ecoroll_time` | `io_12015` | â€” | FMS Eco driving EcoRoll time |
| 672 | `fms.engine.load.fuel.used` | `number` | `â€”` | `12034` | `fms_eng_load_fuel_used` | `io_12034` | â€” | FMS Eco driving fuel used while engine load |
| 673 | `fms.event.enum` | `number` | `â€”` | `12000` | `fms_event_enum` | `io_12000` | â€” | FMS Eco driving event IO ID |
| 674 | `fms.event.number` | `number` | `â€”` | `12003` | `fms_event_num` | `io_12003` | â€” | FMS Eco driving event counter |
| 675 | `fms.ferry.train.enum` | `number` | `â€”` | `10456` | `fms_ferry_train_enum` | `io_10456` | â€” | FMS ferry/train status |
| 676 | `fms.fuel.used.braking.range` | `number` | `â€”` | `12200` | `fms_fuel_used_braking_range` | `io_12200` | â€” | FMS Eco driving fuel used indexed parameter for braking range 1 to 10 |
| 677 | `fms.fuel.used.rpm.range` | `number` | `â€”` | `12140` | `fms_fuel_used_rpm_range` | `io_12140` | â€” | FMS Eco driving fuel used indexed parameter for RPM range 1 to 10 |
| 678 | `fms.fuel.used.speed.range` | `number` | `â€”` | `12110` | `fms_fuel_used_speed_range` | `io_12110` | â€” | FMS Eco driving fuel used indexed parameter for speed range 1 to 10 |
| 679 | `fms.fuel.used.torque.range` | `number` | `â€”` | `12170` | `fms_fuel_used_torque_range` | `io_12170` | â€” | FMS Eco driving fuel used indexed parameter for torque range 1 to 10 |
| 680 | `fms.handling.info` | `number` | `â€”` | `124` | `fms_handling_info` | `io_124` | â€” | FMS handling info |
| 681 | `fms.harsh.acceleration.number` | `number` | `â€”` | `12053` | `fms_harsh_accel_num` | `io_12053` | â€” | FMS Eco driving harsh acceleration count |
| 682 | `fms.harsh.braking.number` | `number` | `â€”` | `12054` | `fms_harsh_braking_num` | `io_12054` | â€” | FMS Eco driving harsh braking count |
| 683 | `fms.harsh.cornering.number` | `number` | `â€”` | `12055` | `fms_harsh_cornering_num` | `io_12055` | â€” | FMS Eco driving harsh cornering count |
| 684 | `fms.idle.fuel.used` | `number` | `â€”` | `12033` | `fms_idle_fuel_used` | `io_12033` | â€” | FMS Eco driving fuel used while idling |
| 685 | `fms.long.stops.number` | `number` | `â€”` | `12051` | `fms_long_stops_num` | `io_12051` | â€” | FMS Eco driving long stops count |
| 686 | `fms.mileage.braking.range` | `number` | `â€”` | `12190` | `fms_mileage_braking_range` | `io_12190` | â€” | FMS Eco driving distance indexed parameter for braking range 1 to 10 |
| 687 | `fms.mileage.rpm.range` | `number` | `â€”` | `12130` | `fms_mileage_rpm_range` | `io_12130` | â€” | FMS Eco driving distance indexed parameter for RPM range 1 to 10 |
| 688 | `fms.mileage.speed.range` | `number` | `â€”` | `12100` | `fms_mileage_speed_range` | `io_12100` | â€” | FMS Eco driving distance indexed parameter for speed range 1 to 10 |
| 689 | `fms.mileage.torque.range` | `number` | `â€”` | `12160` | `fms_mileage_torque_range` | `io_12160` | â€” | FMS Eco driving distance indexed parameter for torque range 1 to 10 |
| 690 | `fms.movement.direction` | `number` | `â€”` | `122` | `fms_mvm_dir` | `io_122` | Sensor `24` (Indication de direction) | FMS element direction indicator: 0 - Vehicle is moving Forward, 1 - Reverse |
| 691 | `fms.parking.brake.number` | `number` | `â€”` | `12052` | `fms_parking_brake_num` | `io_12052` | â€” | FMS Eco driving parking brake count |
| 692 | `fms.pto.fuel.used` | `number` | `â€”` | `12030` | `fms_pto_fuel_used` | `io_12030` | â€” | FMS Eco driving PTO fuel used |
| 693 | `fms.pto.mileage` | `number` | `â€”` | `12029` | `fms_pto_mileage` | `io_12029` | â€” | FMS Eco driving PTO distance |
| 694 | `fms.pto.time` | `number` | `â€”` | `12031` | `fms_pto_time` | `io_12031` | â€” | FMS Eco driving PTO time |
| 695 | `fms.requests.supported` | `number` | `â€”` | `111` | `fms_requests_supported` | `io_111` | Sensor `47` (Demandes prises en charge) | Indicates if FMS Gateway will response to requests from FMS network. 0 - Requests are not supported, 1 - Requests are supported, 2 - Reserved, 3 - Do not care |
| 696 | `fms.retarder.fuel.used` | `number` | `â€”` | `12021` | `fms_retarder_fuel_used` | `io_12021` | â€” | FMS Eco driving Retarder fuel used |
| 697 | `fms.retarder.mileage` | `number` | `â€”` | `12020` | `fms_retarder_mileage` | `io_12020` | â€” | FMS Eco driving Retarder distance |
| 698 | `fms.retarder.time` | `number` | `â€”` | `12022` | `fms_retarder_time` | `io_12022` | â€” | FMS Eco driving Retarder time |
| 699 | `fms.short.stops.number` | `number` | `â€”` | `12050` | `fms_short_stops_num` | `io_12050` | â€” | FMS Eco driving short stops count |
| 700 | `fms.software.version` | `string` | `â€”` | `109` | `fms_software_version` | `io_109` | â€” | Issue level of FMS-standard document the software included into FMS gateway supports |
| 701 | `fms.system.event` | `number` | `â€”` | `125` | `fms_system_event` | `io_125` | â€” | FMS system event |
| 702 | `fms.tacho.performance` | `number` | `â€”` | `123` | `fms_tacho_performance` | `io_123` | â€” | FMS element Tachograph Performance |
| 703 | `fms.tell.tale` | `string` | `â€”` | `10428`, `10429`, `10430`, `10431`, `13259` | `fms_tell_tale` | `io_10428`, `io_10429`, `io_10430`, `io_10431` (+1) | â€” | FMS Tell Tale index parameter in HEX string view |
| 704 | `fms.time.braking.range` | `number` | `â€”` | `12210` | `fms_time_braking_range` | `io_12210` | â€” | FMS Eco driving time indexed parameter for braking range 1 to 10 |
| 705 | `fms.time.rpm.range` | `number` | `â€”` | `12150` | `fms_time_rpm_range` | `io_12150` | â€” | FMS Eco driving time indexed parameter for RPM range 1 to 10 |
| 706 | `fms.time.speed.range` | `number` | `â€”` | `12120` | `fms_time_speed_range` | `io_12120` | â€” | FMS Eco driving time indexed parameter for speed range 1 to 10 |
| 707 | `fms.time.torque.range` | `number` | `â€”` | `12180` | `fms_time_torque_range` | `io_12180` | â€” | FMS Eco driving time indexed parameter for torque range 1 to 10 |
| 708 | `fms.torque.fuel.used` | `number` | `â€”` | `12027` | `fms_torque_fuel_used` | `io_12027` | â€” | FMS Eco driving Torque fuel used |
| 709 | `fms.torque.mileage` | `number` | `â€”` | `12026` | `fms_torque_mileage` | `io_12026` | â€” | FMS Eco driving Torque distance |
| 710 | `fms.torque.time` | `number` | `â€”` | `12028` | `fms_torque_time` | `io_12028` | â€” | FMS Eco driving Torque time |
| 711 | `fms.total.fuel.used` | `number` | `â€”` | `12036` | `fms_total_fuel_used` | `io_12036` | â€” | FMS Eco driving total fuel used |
| 712 | `fms.total.mileage` | `number` | `â€”` | `12035` | `fms_total_mileage` | `io_12035` | â€” | FMS Eco driving total distance |
| 713 | `fms.total.time` | `number` | `â€”` | `12037` | `fms_total_time` | `io_12037` | â€” | FMS Eco driving total time |
| 714 | `fms.vehicle.vin` | `string` | `â€”` | `12002` | `fms_vhc_vin` | `io_12002` | â€” | FMS Eco driving VIN |
| 715 | `freezer.air.temperature` | `number` | `â€”` | `10350` | `freezer_air_temp` | `io_10350` | â€” | Freezer ambient air temperature |
| 716 | `freezer.battery.state` | `number` | `â€”` | `10473` | `freezer_bat_st` | `io_10473` | â€” | Freezer battery state |
| 717 | `freezer.battery.voltage` | `number` | `â€”` | `10041` | `freezer_bat_vlt` | `io_10041` | â€” | Freezer battery voltage |
| 718 | `freezer.compressor.rpm` | `number` | `â€”` | `10353` | `freezer_compressor_rpm` | `io_10353` | â€” | Freezer compressor RPM |
| 719 | `freezer.compressor.state` | `number` | `â€”` | `10354` | `freezer_compressor_st` | `io_10354` | â€” | Freezer compressor configuration state |
| 720 | `freezer.coolant.temperature` | `number` | `â€”` | `10351` | `freezer_coolant_temp` | `io_10351` | â€” | Freezer coolant temperature |
| 721 | `freezer.datacold.ain` | `number` | `â€”` | `10468` | `freezer_datacold_ain` | `io_10468` | â€” | Freezer datacold analog sensor |
| 722 | `freezer.datacold.din` | `boolean` | `â€”` | `10464` | `freezer_datacold_din` | `io_10464` | â€” | Freezer datacold digital sensor |
| 723 | `freezer.datacold.maintenance` | `number` | `â€”` | `10475` | `freezer_datacold_maintenance` | `io_10475` | â€” | Freezer Maintanence |
| 724 | `freezer.datacold.sensor.temperature` | `number` | `â€”` | `10644` | `freezer_datacold_sensor_temp` | `io_10644` | â€” | Freezer datacold temperature sensor |
| 725 | `freezer.door.status` | `number` | `â€”` | `10355` | `freezer_door_stat` | `io_10355` | â€” | Freezer door status bitmask |
| 726 | `freezer.electric.total` | `number` | `â€”` | `10042` | `freezer_electric_total` | `io_10042` | â€” | Freezer electric total |
| 727 | `freezer.engine.total` | `number` | `â€”` | `10044` | `freezer_eng_total` | `io_10044` | â€” | Freezer engine total |
| 728 | `freezer.error.count` | `number` | `â€”` | `10352` | `freezer_error_count` | `io_10352` | â€” | Freezer error count |
| 729 | `freezer.error.data` | `string` | `â€”` | `10639` | `freezer_error_data` | `io_10639` | â€” | Freezer error codes array hex string |
| 730 | `freezer.fuel.level` | `number` | `â€”` | `10040` | `freezer_fuel_lvl` | `io_10040` | â€” | Freezer fuel level |
| 731 | `freezer.fuel.sensor.state` | `number` | `â€”` | `10474` | `freezer_fuel_sensor_st` | `io_10474` | â€” | Freezer fuel state flags |
| 732 | `freezer.installation.serial` | `string` | `â€”` | `10356` | `freezer_installation_serial` | `io_10356` | â€” | Freezer installation serial |
| 733 | `freezer.manufacturer.id` | `number` | `â€”` | `10472` | `freezer_manufacturer_id` | `io_10472` | â€” | Fridge Manufacturer ID |
| 734 | `freezer.run.mode` | `string` | `â€”` | `10480` | `freezer_run_mode` | `io_10480` | â€” | Freezer run mode |
| 735 | `freezer.trailer.serial` | `string` | `â€”` | `10357` | `freezer_trailer_serial` | `io_10357` | â€” | Freezer trailer serial |
| 736 | `freezer.transcan.alarm.enum` | `number` | `â€”` | `10691` | `freezer_transcan_alarm_enum` | `io_10691` | â€” | Alarm value as reported by TK Transcan |
| 737 | `freezer.transcan.state.enum` | `number` | `â€”` | `10687` | `freezer_transcan_st_enum` | `io_10687` | â€” | Status value as reported by TK Transcan |
| 738 | `freezer.transcan.temperature` | `number` | `â€”` | `10683` | `freezer_transcan_temp` | `io_10683` | â€” | Sensor temperature reported by TK Transcan |
| 739 | `freezer.vehicle.total` | `number` | `â€”` | `10043` | `freezer_vhc_total` | `io_10043` | â€” | Freezer vehicle total |
| 740 | `freezer.zone1.alarm.code` | `number` | `â€”` | `10046` | `freezer_zone1_alarm_code` | `io_10046` | â€” | Freezer zone 1 alarm code |
| 741 | `freezer.zone1.alarm.type` | `number` | `â€”` | `10045` | `freezer_zone1_alarm_type` | `io_10045` | â€” | Freezer zone 1 alarm type |
| 742 | `freezer.zone1.evaporator.coil.temperature` | `number` | `â€”` | `10050` | `freezer_zone1_evaporator_coil_temp` | `io_10050` | â€” | Freezer zone 1 evaporator coil temperature |
| 743 | `freezer.zone1.operating.mode` | `number` | `â€”` | `10053` | `freezer_zone1_operating_mode` | `io_10053` | â€” | Freezer zone 1 operating mode |
| 744 | `freezer.zone1.return.air.temperature` | `number` | `â€”` | `10047`, `10051` | `freezer_zone1_return_air_temp` | `io_10047`, `io_10051` | â€” | Freezer zone 1 return air temperature |
| 745 | `freezer.zone1.supply.air.temperature` | `number` | `â€”` | `10048`, `10052` | `freezer_zone1_supply_air_temp` | `io_10048`, `io_10052` | â€” | Freezer zone 1 supply air temperature |
| 746 | `freezer.zone1.temperature.setpoint` | `number` | `â€”` | `10049` | `freezer_zone1_temp_setpoint` | `io_10049` | â€” | Freezer zone 1 temperature setpoint |
| 747 | `freezer.zone2.alarm.code` | `number` | `â€”` | `10055` | `freezer_zone2_alarm_code` | `io_10055` | â€” | Freezer zone 2 alarm code |
| 748 | `freezer.zone2.alarm.type` | `number` | `â€”` | `10054` | `freezer_zone2_alarm_type` | `io_10054` | â€” | Freezer zone 2 alarm type |
| 749 | `freezer.zone2.evaporator.coil.temperature` | `number` | `â€”` | `10059` | `freezer_zone2_evaporator_coil_temp` | `io_10059` | â€” | Freezer zone 2 evaporator coil temperature |
| 750 | `freezer.zone2.operating.mode` | `number` | `â€”` | `10062` | `freezer_zone2_operating_mode` | `io_10062` | â€” | Freezer zone 2 operating mode |
| 751 | `freezer.zone2.return.air.temperature` | `number` | `â€”` | `10056`, `10060` | `freezer_zone2_return_air_temp` | `io_10056`, `io_10060` | â€” | Freezer zone 2 return air temperature |
| 752 | `freezer.zone2.supply.air.temperature` | `number` | `â€”` | `10057`, `10061` | `freezer_zone2_supply_air_temp` | `io_10057`, `io_10061` | â€” | Freezer zone 2 supply air temperature |
| 753 | `freezer.zone2.temperature.setpoint` | `number` | `â€”` | `10058` | `freezer_zone2_temp_setpoint` | `io_10058` | â€” | Freezer zone 2 temperature setpoint |
| 754 | `freezer.zone3.alarm.code` | `number` | `â€”` | `10064` | `freezer_zone3_alarm_code` | `io_10064` | â€” | Freezer zone 3 alarm code |
| 755 | `freezer.zone3.alarm.type` | `number` | `â€”` | `10063` | `freezer_zone3_alarm_type` | `io_10063` | â€” | Freezer zone 3 alarm type |
| 756 | `freezer.zone3.evaporator.coil.temperature` | `number` | `â€”` | `10068` | `freezer_zone3_evaporator_coil_temp` | `io_10068` | â€” | Freezer zone 3 evaporator coil temperature |
| 757 | `freezer.zone3.operating.mode` | `number` | `â€”` | `10071` | `freezer_zone3_operating_mode` | `io_10071` | â€” | Freezer zone 3 operating mode |
| 758 | `freezer.zone3.return.air.temperature` | `number` | `â€”` | `10065`, `10069` | `freezer_zone3_return_air_temp` | `io_10065`, `io_10069` | â€” | Freezer zone 3 return air temperature |
| 759 | `freezer.zone3.supply.air.temperature` | `number` | `â€”` | `10066`, `10070` | `freezer_zone3_supply_air_temp` | `io_10066`, `io_10070` | â€” | Freezer zone 3 supply air temperature |
| 760 | `freezer.zone3.temperature.setpoint` | `number` | `â€”` | `10067` | `freezer_zone3_temp_setpoint` | `io_10067` | â€” | Freezer zone 3 temperature setpoint |
| 761 | `fuel.consumed` | `number` | `â€”` | `12`, `138` | `fuel_consumed` | `io_12`, `io_138` | â€” | Fuel volume totally consumed by vehicle |
| 762 | `fuel.level` | `number` | `â€”` | `10348`, `87` | `fuel_lvl` | `io_10348`, `io_87` | â€” | Fuel level percentage |
| 763 | `geofence.entered.event` | `boolean` | `â€”` | `156` | `geofence_entered_event` | `io_156` | â€” | Device entered geofence event |
| 764 | `geofence.id` | `number` | `â€”` | `155` | `geofence_id` | `io_155` | â€” | Geofence ID |
| 765 | `geofence.left.event` | `boolean` | `â€”` | `156` | `geofence_left_event` | `io_156` | â€” | Device left geofence event |
| 766 | `geofence.overspeeding.status` | `boolean` | `â€”` | `157`, `248` | `geofence_overspeeding_stat` | `io_157`, `io_248` | â€” | Geofence overspeeding status |
| 767 | `geofence.status` | `boolean` | `â€”` | `153`, `155`, `155`, `175`, `190`, `191`, `208`, `216`, `327`, `550`, `61`, `70`, `88`, `91` | `geofence_stat` | `io_153`, `io_155`, `io_155`, `io_175` (+10) | â€” | Geofence entered status |
| 768 | `gnss.antenna.short.circuit.status` | `boolean` | `â€”` | `69`, `71` | `gnss_antenna_short_circuit_stat` | `io_69`, `io_71` | â€” | GNSS antenna short circuit status |
| 769 | `gnss.antenna.status` | `boolean` | `â€”` | `69`, `71` | `gnss_antenna_stat` | `io_69`, `io_71` | â€” | GNSS receiver antenna status |
| 770 | `gnss.first.fix.duration` | `number` | `â€”` | `399` | `gnss_first_fix_dur` | `io_399` | â€” | Amount of time it took to get first GNSS fix |
| 771 | `gnss.jamming.state` | `number` | `â€”` | `318` | `gnss_jamming_st` | `io_318` | â€” | GNSS jamming state |
| 772 | `gnss.sleep.mode.status` | `boolean` | `â€”` | `69`, `71` | `gnss_sleep_mode_stat` | `io_69`, `io_71` | â€” | GNSS receiver is in sleep mode |
| 773 | `gnss.state.enum` | `number` | `â€”` | `69`, `71` | `gnss_st_enum` | `io_69`, `io_71` | â€” | Protocol-specific GNSS state code. May contain information about GNSS fix status, sleep status, ON/OFF, Overcurrent/protect state. |
| 774 | `gnss.status` | `boolean` | `â€”` | `69`, `71` | `gnss_stat` | `io_69`, `io_71` | â€” | GNSS receiver on/off status |
| 775 | `gps.fuel.rate` | `number` | `â€”` | `13` | `gps_fuel_rate` | `io_13` | â€” | GPS-based fuel rate |
| 776 | `gps.fuel.used` | `number` | `â€”` | `12` | `gps_fuel_used` | `io_12` | â€” | GPS-based fuel used |
| 777 | `grain.moisture.level` | `number` | `â€”` | `129`, `44` | `grain_moisture_lvl` | `io_129`, `io_44` | â€” | Grain moisture |
| 778 | `grain.mowing.efficiency.meters2_h` | `number` | `â€”` | `127`, `42` | `grain_mowing_efficiency_meters2_h` | `io_127`, `io_42` | â€” | Mowing efficiency |
| 779 | `grain.mowing.volume.kg` | `number` | `â€”` | `128`, `43` | `grain_mowing_volume_kg` | `io_128`, `io_43` | â€” | Mown volume |
| 780 | `gsm.cellid` | `number` | `â€”` | `13371`, `13376`, `13381`, `13386`, `205`, `25021`, `25024`, `25027`, `25030`, `288`, `291`, `294`, `297`, `636` | `gsm_cellid` | `io_13371`, `io_13376`, `io_13381`, `io_13386` (+10) | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) base station ID |
| 781 | `gsm.jamming.alarm.status` | `boolean` | `â€”` | `249` | `gsm_jamming_alarm_stat` | `io_249` | â€” | Alarm status for the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) jamming |
| 782 | `gsm.lac` | `number` | `â€”` | `13370`, `13375`, `13380`, `13385`, `206`, `25020`, `25023`, `25026`, `25029`, `287`, `290`, `293`, `296` | `gsm_lac` | `io_13370`, `io_13375`, `io_13380`, `io_13385` (+9) | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) location area code |
| 783 | `gsm.mcc` | `number` | `â€”` | `13374`, `13379`, `13384`, `13389`, `241` | `gsm_mcc` | `io_13374`, `io_13379`, `io_13384`, `io_13389` (+1) | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) country code |
| 784 | `gsm.mnc` | `number` | `â€”` | `1200`, `1201`, `13373`, `13378`, `13383`, `13388`, `241`, `25032`, `25033` | `gsm_mnc` | `io_1200`, `io_1201`, `io_13373`, `io_13378` (+5) | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) code |
| 785 | `gsm.network.mode.enum` | `number` | `â€”` | `22`, `80` | `gsm_network_mode_enum` | `io_22`, `io_80` | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) registration mode reported by the device, protocol-specific value set |
| 786 | `gsm.network.roaming.status` | `boolean` | `â€”` | `22`, `80` | `gsm_network_roaming_stat` | `io_22`, `io_80` | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) in roaming mode |
| 787 | `gsm.network.type` | `string` | `â€”` | `178`, `237` | `gsm_network_type` | `io_178`, `io_237` | â€” | The type of the Mobile network the device is currently registered to |
| 788 | `gsm.operator.code` | `string` | `â€”` | `241` | `gsm_operator_code` | `io_241` | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) operator code, which is MCC joined with MNC |
| 789 | `gsm.signal.dbm` | `number` | `â€”` | `13372`, `13377`, `13382`, `13387`, `25019`, `25022`, `25025`, `25028`, `25031`, `286`, `289`, `292`, `295`, `298` | `gsm_signal_dbm` | `io_13372`, `io_13377`, `io_13382`, `io_13387` (+10) | â€” | Strength of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| 790 | `gsm.signal.level` | `number` | `â€”` | `21` | `gsm_signal_lvl` | `io_21` | â€” | Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal strength level |
| 791 | `gsm.signal.quality` | `number` | `â€”` | `1148`, `20017`, `25017` | `gsm_signal_quality` | `io_1148`, `io_20017`, `io_25017` | â€” | The quality (bit error rate) of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) signal |
| 792 | `gsm.sim.iccid` | `string` | `â€”` | `11`, `14`, `221`, `641` | `gsm_sim_iccid` | `io_11`, `io_14`, `io_221`, `io_641` | â€” | Integrated Circuit Card Id of SIM card of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) |
| 793 | `gsm.sim.imsi` | `string` | `â€”` | `218`, `230`, `231` | `gsm_sim_imsi` | `io_218`, `io_230`, `io_231` | â€” | IMSI of SIM card of the Mobile network (GSM, 3G, 4G, LTE, 5G, ...) |
| 794 | `gsm.sim.status` | `boolean` | `â€”` | `232` | `gsm_sim_stat` | `io_232` | â€” | SIM card is active |
| 795 | `harsh.acceleration.event` | `boolean` | `â€”` | `253` | `harsh_accel_event` | `io_253` | Sensor `12` (GREEN DRIVING) | Harsh acceleration detected |
| 796 | `harsh.braking.event` | `boolean` | `â€”` | `253` | `harsh_braking_event` | `io_253` | Sensor `12` (GREEN DRIVING) | Harsh braking detected |
| 797 | `harsh.cornering.angle` | `number` | `â€”` | `254` | `harsh_cornering_angle` | `io_254` | â€” | Harsh cornering angle |
| 798 | `harsh.cornering.event` | `boolean` | `â€”` | `253` | `harsh_cornering_event` | `io_253` | Sensor `12` (GREEN DRIVING) | Harsh cornering detected |
| 799 | `harvest.area` | `number` | `â€”` | `126`, `41` | `harvest_area` | `io_126`, `io_41` | â€” | Area of harvest |
| 800 | `harvest.drum.gap` | `number` | `â€”` | `131`, `46` | `harvest_drum_gap` | `io_131`, `io_46` | â€” | Gap under harvesting drum |
| 801 | `harvest.drum.rpm` | `number` | `â€”` | `130`, `45` | `harvest_drum_rpm` | `io_130`, `io_45` | â€” | Harvesting drum RPM |
| 802 | `harvest.duration` | `number` | `â€”` | `125`, `40` | `harvest_dur` | `io_125`, `io_40` | â€” | Harvesting time |
| 803 | `helmet.status` | `boolean` | `â€”` | `843` | `helmet_stat` | `io_843` | â€” | Helmet status: true - helmet is in, false - helmet is not in |
| 804 | `ibutton.authorized.state.enum` | `number` | `â€”` | `252` | `ibutton_authorized_st_enum` | `io_252` | â€” | iButton authorization state code |
| 805 | `ibutton.authorized.status` | `boolean` | `â€”` | `248`, `251`, `252` | `ibutton_authorized_stat` | `io_248`, `io_251`, `io_252` | â€” | iButton authorized status |
| 806 | `ibutton.code` | `string` | `â€”` | `78` | `ibutton_code` | `io_78` | â€” | Hexadecimal code of connected iButton |
| 807 | `ibutton.connected.status` | `boolean` | `â€”` | `248`, `251` | `ibutton_connected_stat` | `io_248`, `io_251` | â€” | iButton connection status |
| 808 | `ident` | `string` | `â€”` | *(Protocol / Header)* | `ident` | â€” | â€” | Device unique identifier like serial number, IMEI, etc |
| 809 | `idle.status` | `boolean` | `â€”` | `177`, `243`, `251` | `idle_stat` | `io_177`, `io_243`, `io_251` | Sensor `18` (Moteur en ralenti) | Vehicle is in idling state |
| 810 | `ignition.state` | `number` | `â€”` | `836` | `ignition_st` | `io_836` | â€” | Ignition state according to device manual |
| 811 | `immobilizer.keys.status` | `boolean` | `â€”` | `132`, `47` | `immobilizer_keys_stat` | `io_132`, `io_47` | â€” | Programmed sequence of keys is introduced to the imm2m.sim2er in the car |
| 812 | `immobilizer.service.status` | `boolean` | `â€”` | `132`, `47` | `immobilizer_service_stat` | `io_132`, `io_47` | â€” | immobilizer is in the service mode status |
| 813 | `immobilizer.state` | `string` | `â€”` | `251` | `immobilizer_st` | `io_251` | â€” | Immobilizer state |
| 814 | `immobilizer.state.enum` | `number` | `â€”` | `248`, `251` | `immobilizer_st_enum` | `io_248`, `io_251` | â€” | Immobilizer state number |
| 815 | `instant.movement.status` | `boolean` | `â€”` | `303` | `instant_mvm_stat` | `io_303` | â€” | Instant movement status |
| 816 | `instrument.panel.firmware.version` | `string` | `â€”` | `372` | `instrument_panel_firmware_version` | `io_372` | â€” | Scooter's Instrument panel FW version |
| 817 | `internal.battery.capacity` | `number` | `â€”` | `374` | `int_bat_capacity` | `io_374` | â€” | Current residual capacity percentage of internal battery |
| 818 | `internal.battery.firmware.version` | `string` | `â€”` | `371` | `int_bat_firmware_version` | `io_371` | â€” | Firmware version of teltonika internal(IoT) battery |
| 819 | `internal.battery.voltage` | `number` | `â€”` | `350` | `int_bat_vlt` | `io_350` | â€” | Internal battery voltage |
| 820 | `iso6709.coordinates` | `string` | `â€”` | `387` | `iso6709_coordinates` | `io_387` | â€” | String with position in ISO 6709 format |
| 821 | `isobus.implement.park.status` | `boolean` | `â€”` | `12412` | `isobus_implement_park_stat` | `io_12412` | â€” | ISOBUS implement park status |
| 822 | `isobus.implement.transport.status` | `boolean` | `â€”` | `12411` | `isobus_implement_transport_stat` | `io_12411` | â€” | ISOBUS implement transport status |
| 823 | `isobus.key.switch.status` | `boolean` | `â€”` | `12407` | `isobus_key_switch_stat` | `io_12407` | â€” | ISOBUS key switch status |
| 824 | `isobus.maintain.actuator.power.status` | `boolean` | `â€”` | `12410` | `isobus_maintain_actuator_power_stat` | `io_12410` | â€” | ISOBUS maintain actuator power status |
| 825 | `isobus.maintain.ecu.power.status` | `boolean` | `â€”` | `12409` | `isobus_maintain_ecu_power_stat` | `io_12409` | â€” | ISOBUS maintain ECU power status |
| 826 | `isobus.rear.pto.economy.mode.status` | `boolean` | `â€”` | `12431` | `isobus_rear_pto_eco_mode_stat` | `io_12431` | â€” | ISOBUS rear PTO economy mode status |
| 827 | `isobus.rear.pto.engagement.status` | `boolean` | `â€”` | `12429` | `isobus_rear_pto_engagement_stat` | `io_12429` | â€” | ISOBUS rear PTO engagement status |
| 828 | `isobus.rear.pto.mode.enum` | `string` | `â€”` | `12430` | `isobus_rear_pto_mode_enum` | `io_12430` | â€” | ISOBUS rear PTO mode |
| 829 | `isobus.rear.pto.output.shaft.speed` | `number` | `â€”` | `12427` | `isobus_rear_pto_output_shaft_speed` | `io_12427` | â€” | ISOBUS rear PTO output shaft speed |
| 830 | `isobus.rear.pto.shaft.speed.point` | `number` | `â€”` | `12428` | `isobus_rear_pto_shaft_speed_point` | `io_12428` | â€” | ISOBUS rear PTO shaft speed set point |
| 831 | `isobus.start.stop.status` | `boolean` | `â€”` | `12408` | `isobus_start_stop_stat` | `io_12408` | â€” | ISOBUS start/stop status |
| 832 | `issuing.member.state.card` | `number` | `â€”` | `10167`, `10168`, `222`, `223` | `issuing_member_st_card` | `io_10167`, `io_10168`, `io_222`, `io_223` | â€” | Card Issuing Member State, NationNumeric as described in EEC 3821_85 |
| 833 | `kickstand.status` | `boolean` | `â€”` | `819` | `kickstand_stat` | `io_819` | â€” | Kickstand status true - not released, false - released |
| 834 | `kill.switch.status` | `boolean` | `â€”` | `818` | `kill_switch_stat` | `io_818` | â€” | Kill switch status: true - not active, false - active |
| 835 | `lls.temperature` | `number` | `â€”` | `202`, `204`, `211`, `213`, `215` | `lls_temp` | `io_202`, `io_204`, `io_211`, `io_213` (+1) | â€” | LLS (Liquid level sensor) fuel temperature |
| 836 | `lls.value` | `number` | `â€”` | `201`, `203`, `210`, `212`, `214` | `lls_value` | `io_201`, `io_203`, `io_210`, `io_212` (+1) | â€” | LLS (Liquid level sensor) fuel value |
| 837 | `lock.status` | `boolean` | `â€”` | `344` | `lock_stat` | `io_344` | â€” | Lock status |
| 838 | `log.file.current` | `number` | `â€”` | `13266` | `log_file_current` | `io_13266` | â€” | Current active log file |
| 839 | `log.file.max.count` | `number` | `â€”` | `13267` | `log_file_max_count` | `io_13267` | â€” | Max log file count |
| 840 | `malfunction.indicator.status` | `boolean` | `â€”` | `821` | `malfunction_indicator_stat` | `io_821` | â€” | Malfunction indicator status: true - active, false - not active |
| 841 | `mandown.alarm.status` | `boolean` | `â€”` | `242` | `mandown_alarm_stat` | `io_242` | â€” | Man down alarm activated |
| 842 | `manual.can` | `number` | `â€”` | `10216`, `10298`, `145`, `380` | `manual_can` | `io_10216`, `io_10298`, `io_145`, `io_380` | â€” | Indexed Manual CAN parameter value |
| 843 | `manual.can.extended` | `string` | `â€”` | `10358` | `manual_can_extended` | `io_10358` | â€” | HEX representation of Manual CAN Extended |
| 844 | `manual.can.hex` | `string` | `â€”` | `10216`, `10298`, `145`, `380` | `manual_can_hex` | `io_10216`, `io_10298`, `io_145`, `io_380` | â€” | Indexed manual CAN parameter value in HEX representation |
| 845 | `max.x.acceleration` | `number` | `â€”` | `1432`, `258` | `max_x_accel` | `io_1432`, `io_258` | â€” | Harsh acceleration event max accelerometer value on X-axis |
| 846 | `max.y.acceleration` | `number` | `â€”` | `1432`, `258` | `max_y_accel` | `io_1432`, `io_258` | â€” | Harsh acceleration event max accelerometer value on Y-axis |
| 847 | `max.z.acceleration` | `number` | `â€”` | `1432`, `258` | `max_z_accel` | `io_1432`, `io_258` | â€” | Harsh acceleration event max accelerometer value on Z-axis |
| 848 | `media` | `boolean` | `â€”` | *(Protocol / Header)* | `media` | â€” | â€” | Message contain media file |
| 849 | `media.image` | `object` | `â€”` | *(Protocol / Header)* | `media_image` | â€” | â€” | Image file in media storage |
| 850 | `media.type.enum` | `number` | `â€”` | *(Protocol / Header)* | `media_type_enum` | â€” | â€” | Media type enum |
| 851 | `media.type.enum.description` | `string` | `â€”` | *(Protocol / Header)* | `media_type_enum_description` | â€” | â€” | Media type enum description |
| 852 | `media.video` | `object` | `â€”` | *(Protocol / Header)* | `media_video` | â€” | â€” | Video file in media storage |
| 853 | `mobileye.brake.signal.status` | `boolean` | `â€”` | `313` | `mobileye_brake_signal_stat` | `io_313` | â€” | Mobileye brake signal status, true - brake signal is on, false - brake signal is off |
| 854 | `mobileye.dusk.status` | `boolean` | `â€”` | `291` | `mobileye_dusk_stat` | `io_291` | â€” | Mobileye dusk time indicator |
| 855 | `mobileye.error.code` | `number` | `â€”` | `293` | `mobileye_error_code` | `io_293` | â€” | Mobileye error code |
| 856 | `mobileye.error.valid.status` | `boolean` | `â€”` | `292` | `mobileye_error_valid_stat` | `io_292` | â€” | Mobileye error is valid status |
| 857 | `mobileye.failsafe.mode.status` | `boolean` | `â€”` | `301` | `mobileye_failsafe_mode_stat` | `io_301` | â€” | Mobileye indocator of failsafe mode activation |
| 858 | `mobileye.forward.collision.warning.status` | `boolean` | `â€”` | `302` | `mobileye_forward_collision_warning_stat` | `io_302` | â€” | Mobileye indicator of forward collision warning event status |
| 859 | `mobileye.headway.measurement` | `number` | `â€”` | `296` | `mobileye_headway_measurement` | `io_296` | â€” | Mobileye headway measurement, 0 means no closest in-path vehicle on the range |
| 860 | `mobileye.headway.valid.status` | `boolean` | `â€”` | `295` | `mobileye_headway_valid_stat` | `io_295` | â€” | Mobileye headway valid status |
| 861 | `mobileye.headway.warning.level` | `number` | `â€”` | `305` | `mobileye_headway_warning_lvl` | `io_305` | â€” | Mobileye headway warning level |
| 862 | `mobileye.headway.warning.repeat.enabled.status` | `boolean` | `â€”` | `304` | `mobileye_headway_warning_repeat_enabled_stat` | `io_304` | â€” | Mobileye headway warning repeat enabled status |
| 863 | `mobileye.high.beam.available.status` | `boolean` | `â€”` | `316` | `mobileye_high_beam_available_stat` | `io_316` | â€” | Mobileye high beam available status, true - high beam available, false - high beam not available |
| 864 | `mobileye.high.beam.status` | `boolean` | `â€”` | `308` | `mobileye_high_beam_stat` | `io_308` | â€” | Mobileye high beam status, true - high beam on, false - high beam off |
| 865 | `mobileye.internal.error.status` | `boolean` | `â€”` | `300` | `mobileye_int_error_stat` | `io_300` | â€” | Mobileye indicator of internal error. See user manual for details |
| 866 | `mobileye.lane.departure.left.warning.status` | `boolean` | `â€”` | `298` | `mobileye_lane_departure_left_warning_stat` | `io_298` | â€” | Mobileye indicator of left lane departure warning event status |
| 867 | `mobileye.lane.departure.right.warning.status` | `boolean` | `â€”` | `299` | `mobileye_lane_departure_right_warning_stat` | `io_299` | â€” | Mobileye indicator of right lane departure warning event status |
| 868 | `mobileye.lane.departure.warnings.status` | `boolean` | `â€”` | `297` | `mobileye_lane_departure_warnings_stat` | `io_297` | â€” | Mobileye lane departure warnings status, true - wanrings enabled, false - warnings disabled due to low speed or configuration |
| 869 | `mobileye.left.blink.available.status` | `boolean` | `â€”` | `312` | `mobileye_left_blink_available_stat` | `io_312` | â€” | Mobileye left blink available status, true - left blink available, false - left blink not available |
| 870 | `mobileye.low.beam.available.status` | `boolean` | `â€”` | `315` | `mobileye_low_beam_available_stat` | `io_315` | â€” | Mobileye low beam available status, true - low beam available, false - low beam not available |
| 871 | `mobileye.low.beam.status` | `boolean` | `â€”` | `309` | `mobileye_low_beam_stat` | `io_309` | â€” | Mobileye low beam status, true - low beam on, false - low beam off |
| 872 | `mobileye.movement.status` | `boolean` | `â€”` | `294` | `mobileye_mvm_stat` | `io_294` | â€” | Mobileye host vehicle is moving status |
| 873 | `mobileye.night.status` | `boolean` | `â€”` | `291` | `mobileye_night_stat` | `io_291` | â€” | Mobileye night time indicator |
| 874 | `mobileye.pedestrian.collision.warning.status` | `boolean` | `â€”` | `290` | `mobileye_pedestrian_collision_warning_stat` | `io_290` | â€” | Mobileye indicator of pedestrians collision warning |
| 875 | `mobileye.pedestrian.danger.zone.status` | `boolean` | `â€”` | `289` | `mobileye_pedestrian_danger_zone_stat` | `io_289` | â€” | Mobileye indicator of pedestrians in danger zone |
| 876 | `mobileye.right.blink.available.status` | `boolean` | `â€”` | `311` | `mobileye_right_blink_available_stat` | `io_311` | â€” | Mobileye right blink available status, true - right blink available, false - right blink not available |
| 877 | `mobileye.sound.type` | `number` | `â€”` | `288` | `mobileye_sound_type` | `io_288` | â€” | Mobileye sound type |
| 878 | `mobileye.speed` | `number` | `â€”` | `318` | `mobileye_speed` | `io_318` | â€” | Mobileye speed |
| 879 | `mobileye.speed.available.status` | `boolean` | `â€”` | `317` | `mobileye_speed_available_stat` | `io_317` | â€” | Mobileye speed available status, true - speed available, false - speed not available |
| 880 | `mobileye.tamper.status` | `boolean` | `â€”` | `307` | `mobileye_tamper_stat` | `io_307` | â€” | Mobileye indicator of tamper alert (tamper alert is activated if there is no vehicle or lane detection for duration of 10 minutes tamper alert is active above 15 km/h |
| 881 | `mobileye.traffic.signs.recognition.status` | `boolean` | `â€”` | `303` | `mobileye_traffic_signs_recognition_stat` | `io_303` | â€” | Mobileye traffic signs recognition enabled status |
| 882 | `mobileye.traffic.signs.speed.warning.level` | `number` | `â€”` | `306` | `mobileye_traffic_signs_speed_warning_lvl` | `io_306` | â€” | Mobileye traffic signs recongition system's warning level |
| 883 | `mobileye.wipers.available.status` | `boolean` | `â€”` | `314` | `mobileye_wipers_available_stat` | `io_314` | â€” | Mobileye wipers available status, true - wipers available, false - wipers not available |
| 884 | `mobileye.wipers.status` | `boolean` | `â€”` | `310` | `mobileye_wipers_stat` | `io_310` | â€” | Mobileye wipers status, true - wiper passes the windshield, false - wiper is static |
| 885 | `modem.uptime` | `number` | `â€”` | `20015`, `25015` | `modem_uptime` | `io_20015`, `io_25015` | â€” | The total time the modem has been powered on |
| 886 | `motorcycle.fall.event` | `boolean` | `â€”` | `1412` | `motorcycle_fall_event` | `io_1412` | â€” | Motorcycle fall event |
| 887 | `movement.event` | `boolean` | `â€”` | `310` | `mvm_event` | `io_310` | â€” | Movement detected |
| 888 | `movement.status` | `boolean` | `â€”` | `240` | `mvm_stat` | `io_240` | Sensor `19` (MOVEMENT) | Current movement state |
| 889 | `negative.input.status` | `boolean` | `â€”` | `381` | `negative_input_stat` | `io_381` | â€” | Negative input connection to ground status: true - connected, false - disconnected |
| 890 | `network.lte.band` | `number` | `â€”` | `1149` | `network_lte_band` | `io_1149` | â€” | LTE band |
| 891 | `network.signal.rsrp` | `number` | `â€”` | `1148`, `20016`, `25016` | `network_signal_rsrp` | `io_1148`, `io_20016`, `io_25016` | â€” | LTE reference signal received power (RSRP) |
| 892 | `network.signal.rssi` | `number` | `â€”` | `1148` | `network_signal_rssi` | `io_1148` | â€” | Network signal strength |
| 893 | `network.signal.sinr` | `number` | `â€”` | `1148` | `network_signal_sinr` | `io_1148` | â€” | Network Singal to Interference plus Noise ratio |
| 894 | `onewire.sensor.serial` | `string` | `â€”` | `5`, `62`, `7`, `71`, `75`, `76`, `77`, `79` | `onewire_sensor_serial` | `io_5`, `io_62`, `io_7`, `io_71` (+4) | â€” | External 1-Wire sensor serial number in HEX representation |
| 895 | `operating.mode.enum` | `number` | `â€”` | `349`, `831` | `operating_mode_enum` | `io_349`, `io_831` | â€” | Protocol-specific device operating mode |
| 896 | `overspeeding.speed` | `number` | `â€”` | `255` | `overspeeding_speed` | `io_255` | â€” | GNSS based speed when overspeeding event is triggered |
| 897 | `overspeeding.status` | `boolean` | `â€”` | `153`, `155`, `155`, `190`, `191`, `208`, `216`, `255`, `327`, `550`, `61`, `70`, `88`, `91` | `overspeeding_stat` | `io_153`, `io_155`, `io_155`, `io_190` (+10) | â€” | Overspeeding detected |
| 898 | `park.brake.status` | `boolean` | `â€”` | `801`, `832` | `park_brake_stat` | `io_801`, `io_832` | â€” | Park brake status: true - active, false - not active |
| 899 | `payload.hex` | `string` | `â€”` | `10611` | `payload_hex` | `io_10611` | â€” | HEX Payload received from device |
| 900 | `payload.text` | `string` | `â€”` | *(Protocol / Header)* | `payload_text` | â€” | â€” | Text Payload received from device |
| 901 | `pcb.firmware.enum` | `number` | `â€”` | `340` | `pcb_firmware_enum` | `io_340` | â€” | Firmware version of the teltonika PCB |
| 902 | `pcb.temperature` | `number` | `â€”` | `13201`, `70` | `pcb_temp` | `io_13201`, `io_70` | â€” | PCB temperature |
| 903 | `peer` | `string` | `â€”` | *(Protocol / Header)* | `peer` | â€” | â€” | IP:port from which device connecting to the channel |
| 904 | `phone.call.state.enum` | `number` | `â€”` | `13361` | `phone_call_st_enum` | `io_13361` | â€” | Phone call status |
| 905 | `position.altitude` | `number` | `â€”` | *(Protocol / Header)* | `pos_altitude` | `alt` | Sensor `118` (Altitude) | Altitude value for position |
| 906 | `position.direction` | `number` | `â€”` | *(Protocol / Header)* | `course` | â€” | â€” | Heading angle at position detection moment |
| 907 | `position.fix.age` | `number` | `â€”` | `386` | `pos_fix_age` | `io_386` | â€” | Time since the last position fix |
| 908 | `position.hdop` | `number` | `â€”` | `182` | `hdop` | `io_182` | â€” | Horizontal dilution of precision |
| 909 | `position.latitude` | `number` | `â€”` | *(Protocol / Header)* | `lat` | `lat` | Sensor `52` (lat) | Latitude coordinate value |
| 910 | `position.longitude` | `number` | `â€”` | *(Protocol / Header)* | `lon` | `lon` | Sensor `53` (long) | Longitude coordinate value |
| 911 | `position.media.latitude` | `number` | `â€”` | *(Protocol / Header)* | `pos_media_latitude` | â€” | â€” | Latitude recorded by a media device. For example, a camera |
| 912 | `position.media.longitude` | `number` | `â€”` | *(Protocol / Header)* | `pos_media_longitude` | â€” | â€” | Longitude recorded by a media device. For example, a camera |
| 913 | `position.pdop` | `number` | `â€”` | `181` | `pdop` | `io_181` | â€” | Position dilution of precision |
| 914 | `position.satellites` | `number` | `â€”` | *(Protocol / Header)* | `sats` | `sats` | â€” | Quantity of satellites used to calculate coordinates for given position information |
| 915 | `position.speed` | `number` | `â€”` | `24` | `speed` | `io_24` | â€” | Instant speed at position detection moment |
| 916 | `position.valid` | `boolean` | `â€”` | `69`, `71` | `pos_valid` | `io_69`, `io_71` | â€” | Is position information accurate and valid for given timestamp |
| 917 | `power.consumtion` | `number` | `â€”` | `838` | `power_consumtion` | `io_838` | â€” | Vehicle power consumtion |
| 918 | `power.on.status` | `boolean` | `â€”` | `390` | `power_on_stat` | `io_390` | â€” | Power-on device status |
| 919 | `powertrain.state` | `number` | `â€”` | `820` | `powertrain_st` | `io_820` | â€” | Powertrain state |
| 920 | `predicted.remaining.mileage` | `number` | `â€”` | `354` | `predicted_remaining_mileage` | `io_354` | â€” | Predicted remaining mileage |
| 921 | `private.status` | `boolean` | `â€”` | `250`, `391` | `private_stat` | `io_250`, `io_391` | â€” | Device is in private mode |
| 922 | `protocol.id` | `number` | `â€”` | *(Protocol / Header)* | `protocol_id` | â€” | â€” | ID of protocol |
| 923 | `proximity.duration` | `number` | `â€”` | `890` | `proximity_dur` | `io_890` | â€” | Proximity violation duration |
| 924 | `proximity.violation.ident` | `string` | `â€”` | `875` | `proximity_violation_ident` | `io_875` | â€” | IMEI of the device which violates personal space |
| 925 | `proximity.violation.mac.address` | `string` | `â€”` | `875` | `proximity_violation_mac_address` | `io_875` | â€” | MAC address which violates personal space |
| 926 | `proximity.violation.reason` | `number` | `â€”` | `889` | `proximity_violation_reason` | `io_889` | â€” | Cause of Proximity violation |
| 927 | `proximity.violation.state` | `number` | `â€”` | `874` | `proximity_violation_st` | `io_874` | â€” | Bitmask describing the causes of proximity violation |
| 928 | `pto.drive.engagement.enum` | `number` | `â€”` | `137` | `pto_drive_engagement_enum` | `io_137` | Sensor `15` (PTO Drive Engagement) | PTO drive engagement. 0 - No PTO drive is engaged. 1 - At least one PTO drive is engaged, 2 - Error, 3 - Not available |
| 929 | `recovery.alarm` | `boolean` | `â€”` | `20012` | `recovery_alarm` | `io_20012` | â€” | Recovery alarm |
| 930 | `remaining.range` | `number` | `â€”` | `822` | `remaining_range` | `io_822` | â€” | Current remaining range |
| 931 | `rfid.code` | `string` | `â€”` | `207`, `217` | `rfid_code` | `io_207`, `io_217` | â€” | Hexadecimal code of connected RFID |
| 932 | `scenario.status` | `boolean` | `â€”` | `358`, `358`, `359`, `360` | `scenario_stat` | `io_358`, `io_358`, `io_359`, `io_360` | â€” | Custom scenario status |
| 933 | `scooter.battery.level` | `number` | `â€”` | `352` | `scooter_bat_lvl` | `io_352` | â€” | Scooter battery level |
| 934 | `sd.status` | `boolean` | `â€”` | `10`, `144` | `sd_stat` | `io_10`, `io_144` | â€” | SD status presence |
| 935 | `seco.state` | `string` | `â€”` | `396` | `seco_st` | `io_396` | â€” | Secure engine cut-off (SECO) output state |
| 936 | `seco.state.enum` | `number` | `â€”` | `396` | `seco_st_enum` | `io_396` | â€” | Secure engine cut-off (SECO) output state: 0 - off, 1 - pulsing, 2 - on |
| 937 | `segment.can.fuel.consumed` | `number` | `â€”` | `110` | `segment_can_fuel_consumed` | `io_110` | â€” | Fuel volume consumed by vehicle on the last segment using CAN data |
| 938 | `segment.can.vehicle.mileage` | `number` | `â€”` | `134` | `segment_can_vhc_mileage` | `io_134` | â€” | Vehicle mileage on the last segment using CAN data |
| 939 | `segment.vehicle.mileage` | `number` | `â€”` | `199`, `357` | `segment_vhc_mileage` | `io_199`, `io_357` | â€” | Segment mileage |
| 940 | `sensor.humidity` | `number` | `â€”` | `10487` | `sensor_humidity` | `io_10487` | â€” | Humidity sensor value, i.e. relative air humidity level |
| 941 | `sensor.temperature` | `number` | `â€”` | `6`, `72`, `72`, `75`, `8` | `sensor_temp` | `io_6`, `io_72`, `io_72`, `io_75` (+1) | â€” | Temperature sensor value |
| 942 | `sensor.temperature.error.code` | `string` | `â€”` | `72` | `sensor_temp_error_code` | `io_72` | â€” | Temperature sensor error description |
| 943 | `server.timestamp` | `number` | `â€”` | *(Protocol / Header)* | `server_timestamp` | â€” | â€” | Timestamp when server received a message |
| 944 | `sim.card.error.count` | `number` | `â€”` | `13200` | `sim_card_error_count` | `io_13200` | â€” | Error counter for No Sim Card error |
| 945 | `sleep.mode.enum` | `number` | `â€”` | `200` | `sleep_mode_enum` | `io_200` | â€” | Protocol-specific value indicating device sleep mode state |
| 946 | `software.version` | `string` | `â€”` | `340` | `software_version` | `io_340` | â€” | Software version string |
| 947 | `supersoco.battery.capacity` | `number` | `â€”` | `858` | `supersoco_bat_capacity` | `io_858` | â€” | SuperSoco battery capacity left |
| 948 | `supersoco.battery.energy` | `number` | `â€”` | `867` | `supersoco_bat_energy` | `io_867` | â€” | SuperSoco battery energy |
| 949 | `supersoco.current.trip.range` | `number` | `â€”` | `856` | `supersoco_current_trip_range` | `io_856` | â€” | SuperSoco current trip range |
| 950 | `supersoco.fw.version` | `number` | `â€”` | `865` | `supersoco_fw_version` | `io_865` | â€” | SuperSoco vehicle firmware version |
| 951 | `supersoco.instrument.system.error` | `string` | `â€”` | `870` | `supersoco_instrument_system_error` | `io_870` | â€” | SuperSoco instrument system error |
| 952 | `supersoco.lock.status` | `boolean` | `â€”` | `864` | `supersoco_lock_stat` | `io_864` | â€” | SuperSoco lock status |
| 953 | `supersoco.moving.abnormal.status` | `boolean` | `â€”` | `862` | `supersoco_moving_abnormal_stat` | `io_862` | â€” | SuperSoco moving abnormal status |
| 954 | `supersoco.power.status` | `boolean` | `â€”` | `855` | `supersoco_power_stat` | `io_855` | â€” | SuperSoco power status: true - ON, false - OFF |
| 955 | `supersoco.power.system.error` | `string` | `â€”` | `868` | `supersoco_power_system_error` | `io_868` | â€” | SuperSoco power system error |
| 956 | `supersoco.powertrain.error` | `string` | `â€”` | `869` | `supersoco_powertrain_error` | `io_869` | â€” | SuperSoco power traing error |
| 957 | `supersoco.range` | `number` | `â€”` | `863` | `supersoco_range` | `io_863` | â€” | SuperSoco range |
| 958 | `supersoco.temperature.high.status` | `boolean` | `â€”` | `860` | `supersoco_temp_high_stat` | `io_860` | â€” | SuperSoco high temperature status |
| 959 | `supersoco.total.range` | `number` | `â€”` | `866` | `supersoco_total_range` | `io_866` | â€” | SuperSoco total range |
| 960 | `supersoco.total.trip.range` | `number` | `â€”` | `857` | `supersoco_total_trip_range` | `io_857` | â€” | SuperSoco total trip range |
| 961 | `supersoco.upload.time` | `number` | `â€”` | `861` | `supersoco_upload_time` | `io_861` | â€” | SuperSoco upload time |
| 962 | `supersoco.voltage.low.status` | `boolean` | `â€”` | `859` | `supersoco_vlt_low_stat` | `io_859` | â€” | SuperSoco low voltage status |
| 963 | `tacho.border.crossing.info` | `number` | `â€”` | `10542` | `tacho_border_crossing_info` | `io_10542` | â€” | Tachograph border crossing info |
| 964 | `tacho.data.source` | `string` | `â€”` | `48` | `tco_data_source` | `io_48` | Sensor `75` (Source des donnÃ©es tachygraphe) | Tacho data source |
| 965 | `tacho.driver.activity.duration` | `number` | `â€”` | `10173`, `10174`, `143`, `144`, `60` | `tacho_driver_activity_dur` | `io_10173`, `io_10174`, `io_143`, `io_144` (+1) | â€” | Duration of the current driver activity reported by tacho, indexed by card slot |
| 966 | `tacho.driver.activity.state` | `string` | `â€”` | `10159`, `10160`, `115`, `116`, `137`, `138`, `184`, `185` | `tacho_driver_activity_st` | `io_10159`, `io_10160`, `io_115`, `io_116` (+4) | â€” | Current driver activity reported by tacho, indexed by card slot, rest / work / drive / available / not available / error |
| 967 | `tacho.driver.activity.state.enum` | `number` | `â€”` | `10159`, `10160`, `115`, `116`, `137`, `138`, `184`, `185` | `tacho_driver_activity_st_enum` | `io_10159`, `io_10160`, `io_115`, `io_116` (+4) | â€” | Current driver activity reported by tacho, indexed by card slot, 0 - rest, 1 - work, 2 - drive, 3 - available, 4 - not available, 5 - error |
| 968 | `tacho.driver.card.code` | `string` | `â€”` | `10165`, `10166`, `147`, `148`, `149`, `150`, `195`, `196`, `197`, `198` | `tacho_driver_card_code` | `io_10165`, `io_10166`, `io_147`, `io_148` (+6) | â€” | Driver identification card id for tacho, indexed by card slot |
| 969 | `tacho.driver.card.data.available.status` | `boolean` | `â€”` | `10538` | `tacho_driver_card_data_available_stat` | `io_10538` | â€” | Tacho Driver card data availability |
| 970 | `tacho.driver.card.expiration` | `number` | `â€”` | `13466`, `13467` | `tacho_driver_card_expiration` | `io_13466`, `io_13467` | â€” | Driver card expiry date reported by tacho, indexed for driver number |
| 971 | `tacho.driver.card.presence` | `number` | `â€”` | `10161`, `10162`, `120`, `121`, `187`, `188` | `tacho_driver_card_presence` | `io_10161`, `io_10162`, `io_120`, `io_121` (+2) | â€” | Tacho driver card presence enum |
| 972 | `tacho.driver.card.status` | `boolean` | `â€”` | `10161`, `10162`, `120`, `121`, `136`, `187`, `188` | `tacho_driver_card_stat` | `io_10161`, `io_10162`, `io_120`, `io_121` (+3) | â€” | Tacho driver card status |
| 973 | `tacho.driver.compensation.before.last.week.duration` | `number` | `â€”` | `10536` | `tacho_driver_compensation_before_last_week_dur` | `io_10536` | â€” | Tacho Driver open compensation in week before last |
| 974 | `tacho.driver.compensation.last.week.duration` | `number` | `â€”` | `10535` | `tacho_driver_compensation_last_week_dur` | `io_10535` | â€” | Tacho Driver open compensation in the last week |
| 975 | `tacho.driver.compensation.second.before.last.week.duration` | `number` | `â€”` | `10537` | `tacho_driver_compensation_second_before_last_week_dur` | `io_10537` | â€” | Tacho Driver open compensation in 2nd week before last |
| 976 | `tacho.driver.continuous_driving.duration` | `number` | `â€”` | `10169`, `10170`, `139`, `140`, `56` | `tacho_driver_continuous_driving_dur` | `io_10169`, `io_10170`, `io_139`, `io_140` (+1) | â€” | Driver continuous driving time |
| 977 | `tacho.driver.cumulative_break.duration` | `number` | `â€”` | `10171`, `10172`, `141`, `142`, `58` | `tacho_driver_cumulative_break_dur` | `io_10171`, `io_10172`, `io_141`, `io_142` (+1) | â€” | Driver cumulative break time |
| 978 | `tacho.driver.cumulative_driving.duration` | `number` | `â€”` | `10175`, `10176`, `145`, `146`, `69`, `77` | `tacho_driver_cumulative_driving_dur` | `io_10175`, `io_10176`, `io_145`, `io_146` (+2) | â€” | Driver cumulative driving time |
| 979 | `tacho.driver.current.activity.duration` | `number` | `â€”` | `143`, `144` | `tacho_driver_current_activity_dur` | `io_143`, `io_144` | â€” | Current driver activity duration |
| 980 | `tacho.driver.daily.before.rest.duration` | `number` | `â€”` | `10509`, `10516` | `tacho_driver_daily_before_rest_dur` | `io_10509`, `io_10516` | â€” | Time left until new daily rest period read from Tacho, indexed for driver number |
| 981 | `tacho.driver.daily.driving.duration` | `number` | `â€”` | `10507`, `10514` | `tacho_driver_daily_driving_dur` | `io_10507`, `io_10514` | â€” | Current daily driving time read from Tacho, indexed for driver number |
| 982 | `tacho.driver.daily.limit.exceed.number` | `number` | `â€”` | `10510`, `10517` | `tacho_driver_daily_limit_exceed_num` | `io_10510`, `io_10517` | â€” | Tacho Driver number of times 9h daily driving time exceeds |
| 983 | `tacho.driver.daily.minimum.rest.duration` | `number` | `â€”` | `10524`, `10525` | `tacho_driver_daily_minimum_rest_dur` | `io_10524`, `io_10525` | â€” | Tacho Driver Minimum Daily Rest duration |
| 984 | `tacho.driver.daily.rest.end.timestamp` | `number` | `â€”` | `10504`, `10511` | `tacho_driver_daily_rest_end_timestamp` | `io_10504`, `io_10511` | â€” | Tacho Driver end of last daily rest report timestamp |
| 985 | `tacho.drive.recognize.status` | `boolean` | `â€”` | `10154`, `183` | `tco_drive_recognize_stat` | `io_10154`, `io_183` | Sensor `83` (Reconnaissance conduite tachygraphe) | Tacho recognized vehicle drive |
| 986 | `tacho.driver.load.time` | `number` | `â€”` | `13261`, `13262` | `tacho_driver_load_time` | `io_13261`, `io_13262` | â€” | Driver loading/unloading time reported by tacho, indexed for driver number |
| 987 | `tacho.driver.multi.manning.status` | `boolean` | `â€”` | `10538` | `tacho_driver_multi_manning_stat` | `io_10538` | â€” | Tacho Driver multi-manning detection status |
| 988 | `tacho.driver.next.driving.duration` | `number` | `â€”` | `10541` | `tacho_driver_next_driving_dur` | `io_10541` | â€” | Tacho Driver duration of next driving period |
| 989 | `tacho.driver.next.rest.duration` | `number` | `â€”` | `10528`, `10529` | `tacho_driver_next_rest_dur` | `io_10528`, `io_10529` | â€” | Duration of next rest period read from Tacho, indexed for driver number |
| 990 | `tacho.driver.private.data.consent` | `number` | `â€”` | `13263` | `tacho_driver_private_data_consent` | `io_13263` | â€” | Drivers private data consent status reported by tacho |
| 991 | `tacho.driver.remaining.before.rest.duration` | `number` | `â€”` | `10530`, `10531` | `tacho_driver_remaining_before_rest_dur` | `io_10530`, `io_10531` | â€” | Duration remaining before next rest period read from Tacho, indexed for driver number |
| 992 | `tacho.driver.remaining.current.driving.duration` | `number` | `â€”` | `10532` | `tacho_driver_remaining_current_driving_dur` | `io_10532` | â€” | Tacho Driver remaining current driving time |
| 993 | `tacho.driver.remaining.current.rest.duration` | `number` | `â€”` | `10539` | `tacho_driver_remaining_current_rest_dur` | `io_10539` | â€” | Tacho Driver remaining time of current break/rest |
| 994 | `tacho.driver.remaining.reduced.daily.rest.periods` | `number` | `â€”` | `10538` | `tacho_driver_remaining_reduced_daily_rest_periods` | `io_10538` | â€” | Tacho Driver remaining reduced daily rest periods. Range 0 to 3 |
| 995 | `tacho.driver.remaining.shift.driving.duration` | `number` | `â€”` | `10533` | `tacho_driver_remaining_shift_driving_dur` | `io_10533` | â€” | Tacho Driver remaining driving time on current shift |
| 996 | `tacho.driver.remaining.ten.hour.driving.times` | `number` | `â€”` | `10538` | `tacho_driver_remaining_ten_hour_driving_times` | `io_10538` | â€” | Tacho Driver remaining 10h driving times. Range 0 to 2 |
| 997 | `tacho.driver.remaining.weekly.driving.duration` | `number` | `â€”` | `10534` | `tacho_driver_remaining_weekly_driving_dur` | `io_10534` | â€” | Tacho Driver remaining driving time of current week |
| 998 | `tacho.driver.selected.activity.duration` | `number` | `â€”` | `10173`, `10174`, `60` | `tacho_driver_selected_activity_dur` | `io_10173`, `io_10174`, `io_60` | â€” | Indexed Tacho parameter indicating current duration of the selected activity, since selected and which may be the current driving period, availability period, rest period or work period |
| 999 | `tacho.driver.time.before.warning` | `number` | `â€”` | `10501` | `tacho_driver_time_before_warning` | `io_10501` | â€” | Tacho driver's hours rules pre warning time delay |
| 1000 | `tacho.driver.time.overlap.status` | `boolean` | `â€”` | `10538` | `tacho_driver_time_overlap_stat` | `io_10538` | â€” | Tacho Driver time overlap detection status |
| 1001 | `tacho.driver.time.state` | `string` | `â€”` | `10163`, `10164`, `189` | `tacho_driver_time_st` | `io_10163`, `io_10164`, `io_189` | â€” | Tacho driver time related states |
| 1002 | `tacho.driver.time.state.enum` | `number` | `â€”` | `10163`, `10164`, `189` | `tacho_driver_time_st_enum` | `io_10163`, `io_10164`, `io_189` | â€” | Tacho driver time related states |
| 1003 | `tacho.driver.time.until.next.driving` | `number` | `â€”` | `10540` | `tacho_driver_time_until_next_driving` | `io_10540` | â€” | Tacho Driver time left until next driving period |
| 1004 | `tacho.driver.unknown.periods.present.status` | `boolean` | `â€”` | `10538` | `tacho_driver_unknown_periods_present_stat` | `io_10538` | â€” | Tacho Driver unknown periods presence |
| 1005 | `tacho.driver.weekly.before.rest.duration` | `number` | `â€”` | `10522`, `10523` | `tacho_driver_weekly_before_rest_dur` | `io_10522`, `io_10523` | â€” | Time left until new weekly rest period read from Tacho, indexed for driver number |
| 1006 | `tacho.driver.weekly.driving.duration` | `number` | `â€”` | `10508`, `10515` | `tacho_driver_weekly_driving_dur` | `io_10508`, `io_10515` | â€” | Current weekly driving time read from Tacho, indexed for driver number |
| 1007 | `tacho.driver.weekly.minimum.rest.duration` | `number` | `â€”` | `10526`, `10527` | `tacho_driver_weekly_minimum_rest_dur` | `io_10526`, `io_10527` | â€” | Tacho Driver Minimum Weekly Rest duration |
| 1008 | `tacho.driver.weekly.rest.calculation.status` | `boolean` | `â€”` | `10538` | `tacho_driver_weekly_rest_calculation_stat` | `io_10538` | â€” | Tacho Driver weekly rest period calculation status |
| 1009 | `tacho.driver.weekly.rest.end.timestamp` | `number` | `â€”` | `10505`, `10512` | `tacho_driver_weekly_rest_end_timestamp` | `io_10505`, `io_10512` | â€” | Tacho Driver end of last weekly rest period timestamp |
| 1010 | `tacho.driver.weekly.second.rest.end.timestamp` | `number` | `â€”` | `10506`, `10513` | `tacho_driver_weekly_second_rest_end_timestamp` | `io_10506`, `io_10513` | â€” | Tacho Driver end of second last weekly rest period timestamp |
| 1011 | `tacho.driver.work.state` | `string` | `â€”` | `10159`, `10160`, `115`, `116`, `184`, `185` | `tacho_driver_work_st` | `io_10159`, `io_10160`, `io_115`, `io_116` (+2) | â€” | Protocol-specific driver work state name |
| 1012 | `tacho.driver.work.state.enum` | `number` | `â€”` | `10159`, `10160`, `115`, `116`, `137`, `138`, `184`, `185` | `tacho_driver_work_st_enum` | `io_10159`, `io_10160`, `io_115`, `io_116` (+4) | â€” | Protocol-specific driver work state value |
| 1013 | `tacho.kline.privacy.mode.enum` | `string` | `â€”` | `10543` | `tacho_kline_privacy_mode_enum` | `io_10543` | â€” | Tachograph K-Line privacy mode |
| 1014 | `tacho.movement.status` | `boolean` | `â€”` | `114` | `tacho_mvm_stat` | `io_114` | â€” | Movement status reported by tacho |
| 1015 | `tacho.next.calibration.timestamp` | `number` | `â€”` | `10503` | `tacho_next_calibration_timestamp` | `io_10503` | â€” | Tacho next calibration timestamp |
| 1016 | `tacho.out.of.scope.condition.status` | `boolean` | `â€”` | `10502` | `tacho_out_of_scope_condition_stat` | `io_10502` | â€” | Tacho out of scope condition is met. Indicates whether the vehicle is currently operating under an exemption from tachograph regulations. |
| 1017 | `tacho.overspeeding.status` | `boolean` | `â€”` | `10155`, `117`, `186` | `tco_overspeed_stat` | `io_10155`, `io_117`, `io_186` | Sensor `7` (Speed Above Threshold) | Overspeeding status reported by tacho |
| 1018 | `tacho.position.speed` | `number` | `â€”` | `10156`, `126`, `135`, `191` | `tco_pos_speed` | `io_10156`, `io_126`, `io_135`, `io_191` | Sensor `81` (Vitesse tachygraphe) | Instant speed reported by tacho |
| 1019 | `tacho.timestamp` | `number` | `â€”` | `10153`, `194` | `tacho_timestamp` | `io_10153`, `io_194` | â€” | Time reported by tacho |
| 1020 | `tacho.trip.mileage` | `number` | `â€”` | `10152`, `193` | `tco_trip_distance` | `io_10152`, `io_193` | Sensor `80` (Distance trajet tachygraphe) | Trip mileage reported by tacho |
| 1021 | `tacho.vehicle.load.type` | `string` | `â€”` | `13260` | `tacho_vhc_load_type` | `io_13260` | â€” | Tachograph vehicle load type |
| 1022 | `tacho.vehicle.mileage` | `number` | `â€”` | `10151`, `133`, `192` | `tco_distance` | `io_10151`, `io_133`, `io_192` | Sensor `1` (KilomÃ©trage Tableau de bord), Sensor `27` (consommation carburant au 100) | Total mileage calculated by tacho |
| 1023 | `tamper.alarm` | `boolean` | `â€”` | `520` | `tamper_alarm` | `io_520` | â€” | Tamper alarm event |
| 1024 | `tamper.alarm.state` | `string` | `â€”` | `20019` | `tamper_alarm_st` | `io_20019` | â€” | Tamper record event reason |
| 1025 | `tamper.alarm.state.enum` | `number` | `â€”` | `20019` | `tamper_alarm_st_enum` | `io_20019` | â€” | Tamper record event numeric reason |
| 1026 | `timestamp` | `number` | `â€”` | *(Protocol / Header)* | `timestamp` | â€” | â€” | Message timestamp |
| 1027 | `top.case.status` | `boolean` | `â€”` | `844` | `top_case_stat` | `io_844` | â€” | Top case opened status: true - opened, false - closed |
| 1028 | `total.driving.time` | `number` | `â€”` | `359` | `total_driving_time` | `io_359` | â€” | Total riding time |
| 1029 | `total.mileage` | `number` | `â€”` | `112` | `total_mileage` | `io_112` | â€” | Total mileage |
| 1030 | `total.operate.time` | `number` | `â€”` | `358` | `total_operate_time` | `io_358` | â€” | Total operation time |
| 1031 | `total.vehicle.weight` | `number` | `â€”` | `139` | `total_vhc_weight` | `io_139` | Sensor `21` (Poids brut combinÃ© du vÃ©hicule) | Total vehicle weight |
| 1032 | `towing.alarm.status` | `boolean` | `â€”` | `246` | `towing_alarm_stat` | `io_246` | Sensor `11` (Remorquage) | Towing alarm state |
| 1033 | `trailer.abs.state.enum` | `number` | `â€”` | `13653` | `trailer_abs_st_enum` | `io_13653` | Sensor `72` (Ã‰tat ABS remorque) | Trailer ABS Status |
| 1034 | `trailer.amber.warning.request.state.enum` | `number` | `â€”` | `13656` | `trailer_amber_warning_req_st_enum` | `io_13656` | Sensor `66` (Alerte jaune EBS) | Amber warning request status |
| 1035 | `trailer.automatic.towed.vehicle.braking.state.enum` | `number` | `â€”` | `13805` | `trailer_automatic_towed_vhc_braking_st_enum` | `io_13805` | â€” | Automatic towed vehicle braking status |
| 1036 | `trailer.axle.load.sum` | `number` | `â€”` | `13657` | `trailer_axle_load_sum` | `io_13657` | Sensor `71` (Charge totale essieux remorque) | Sum of all axle loads |
| 1037 | `trailer.brake.lining.axle.1.wheel.10.level` | `number` | `â€”` | `13733` | `trailer_brake_lining_axle_1_wheel_10_lvl` | `io_13733` | â€” | Brake lining level for axle 1 wheel 10 |
| 1038 | `trailer.brake.lining.axle.1.wheel.10.state.enum` | `number` | `â€”` | `13718` | `trailer_brake_lining_axle_1_wheel_10_st_enum` | `io_13718` | â€” | Brake lining status for axle 1 wheel 10 |
| 1039 | `trailer.brake.lining.axle.1.wheel.6.level` | `number` | `â€”` | `13729` | `trailer_brake_lining_axle_1_wheel_6_lvl` | `io_13729` | â€” | Brake lining level for axle 1 wheel 6 |
| 1040 | `trailer.brake.lining.axle.1.wheel.6.state.enum` | `number` | `â€”` | `13714` | `trailer_brake_lining_axle_1_wheel_6_st_enum` | `io_13714` | â€” | Brake lining status for axle 1 wheel 6 |
| 1041 | `trailer.brake.lining.axle.1.wheel.7.level` | `number` | `â€”` | `13730` | `trailer_brake_lining_axle_1_wheel_7_lvl` | `io_13730` | â€” | Brake lining level for axle 1 wheel 7 |
| 1042 | `trailer.brake.lining.axle.1.wheel.7.state.enum` | `number` | `â€”` | `13715` | `trailer_brake_lining_axle_1_wheel_7_st_enum` | `io_13715` | â€” | Brake lining status for axle 1 wheel 7 |
| 1043 | `trailer.brake.lining.axle.1.wheel.8.level` | `number` | `â€”` | `13731` | `trailer_brake_lining_axle_1_wheel_8_lvl` | `io_13731` | â€” | Brake lining level for axle 1 wheel 8 |
| 1044 | `trailer.brake.lining.axle.1.wheel.8.state.enum` | `number` | `â€”` | `13716` | `trailer_brake_lining_axle_1_wheel_8_st_enum` | `io_13716` | â€” | Brake lining status for axle 1 wheel 8 |
| 1045 | `trailer.brake.lining.axle.1.wheel.9.level` | `number` | `â€”` | `13732` | `trailer_brake_lining_axle_1_wheel_9_lvl` | `io_13732` | â€” | Brake lining level for axle 1 wheel 9 |
| 1046 | `trailer.brake.lining.axle.1.wheel.9.state.enum` | `number` | `â€”` | `13717` | `trailer_brake_lining_axle_1_wheel_9_st_enum` | `io_13717` | â€” | Brake lining status for axle 1 wheel 9 |
| 1047 | `trailer.brake.lining.axle.2.wheel.10.level` | `number` | `â€”` | `13738` | `trailer_brake_lining_axle_2_wheel_10_lvl` | `io_13738` | â€” | Brake lining level for axle 2 wheel 10 |
| 1048 | `trailer.brake.lining.axle.2.wheel.10.state.enum` | `number` | `â€”` | `13723` | `trailer_brake_lining_axle_2_wheel_10_st_enum` | `io_13723` | â€” | Brake lining status for axle 2 wheel 10 |
| 1049 | `trailer.brake.lining.axle.2.wheel.6.level` | `number` | `â€”` | `13734` | `trailer_brake_lining_axle_2_wheel_6_lvl` | `io_13734` | â€” | Brake lining level for axle 2 wheel 6 |
| 1050 | `trailer.brake.lining.axle.2.wheel.6.state.enum` | `number` | `â€”` | `13719` | `trailer_brake_lining_axle_2_wheel_6_st_enum` | `io_13719` | â€” | Brake lining status for axle 2 wheel 6 |
| 1051 | `trailer.brake.lining.axle.2.wheel.7.level` | `number` | `â€”` | `13735` | `trailer_brake_lining_axle_2_wheel_7_lvl` | `io_13735` | â€” | Brake lining level for axle 2 wheel 7 |
| 1052 | `trailer.brake.lining.axle.2.wheel.7.state.enum` | `number` | `â€”` | `13720` | `trailer_brake_lining_axle_2_wheel_7_st_enum` | `io_13720` | â€” | Brake lining status for axle 2 wheel 7 |
| 1053 | `trailer.brake.lining.axle.2.wheel.8.level` | `number` | `â€”` | `13736` | `trailer_brake_lining_axle_2_wheel_8_lvl` | `io_13736` | â€” | Brake lining level for axle 2 wheel 8 |
| 1054 | `trailer.brake.lining.axle.2.wheel.8.state.enum` | `number` | `â€”` | `13721` | `trailer_brake_lining_axle_2_wheel_8_st_enum` | `io_13721` | â€” | Brake lining status for axle 2 wheel 8 |
| 1055 | `trailer.brake.lining.axle.2.wheel.9.level` | `number` | `â€”` | `13737` | `trailer_brake_lining_axle_2_wheel_9_lvl` | `io_13737` | â€” | Brake lining level for axle 2 wheel 9 |
| 1056 | `trailer.brake.lining.axle.2.wheel.9.state.enum` | `number` | `â€”` | `13722` | `trailer_brake_lining_axle_2_wheel_9_st_enum` | `io_13722` | â€” | Brake lining status for axle 2 wheel 9 |
| 1057 | `trailer.brake.lining.axle.3.wheel.10.level` | `number` | `â€”` | `13743` | `trailer_brake_lining_axle_3_wheel_10_lvl` | `io_13743` | â€” | Brake lining level for axle 3 wheel 10 |
| 1058 | `trailer.brake.lining.axle.3.wheel.10.state.enum` | `number` | `â€”` | `13728` | `trailer_brake_lining_axle_3_wheel_10_st_enum` | `io_13728` | â€” | Brake lining status for axle 3 wheel 10 |
| 1059 | `trailer.brake.lining.axle.3.wheel.6.level` | `number` | `â€”` | `13739` | `trailer_brake_lining_axle_3_wheel_6_lvl` | `io_13739` | â€” | Brake lining level for axle 3 wheel 6 |
| 1060 | `trailer.brake.lining.axle.3.wheel.6.state.enum` | `number` | `â€”` | `13724` | `trailer_brake_lining_axle_3_wheel_6_st_enum` | `io_13724` | â€” | Brake lining status for axle 3 wheel 6 |
| 1061 | `trailer.brake.lining.axle.3.wheel.7.level` | `number` | `â€”` | `13740` | `trailer_brake_lining_axle_3_wheel_7_lvl` | `io_13740` | â€” | Brake lining level for axle 3 wheel 7 |
| 1062 | `trailer.brake.lining.axle.3.wheel.7.state.enum` | `number` | `â€”` | `13725` | `trailer_brake_lining_axle_3_wheel_7_st_enum` | `io_13725` | â€” | Brake lining status for axle 3 wheel 7 |
| 1063 | `trailer.brake.lining.axle.3.wheel.8.level` | `number` | `â€”` | `13741` | `trailer_brake_lining_axle_3_wheel_8_lvl` | `io_13741` | â€” | Brake lining level for axle 3 wheel 8 |
| 1064 | `trailer.brake.lining.axle.3.wheel.8.state.enum` | `number` | `â€”` | `13726` | `trailer_brake_lining_axle_3_wheel_8_st_enum` | `io_13726` | â€” | Brake lining status for axle 3 wheel 8 |
| 1065 | `trailer.brake.lining.axle.3.wheel.9.level` | `number` | `â€”` | `13742` | `trailer_brake_lining_axle_3_wheel_9_lvl` | `io_13742` | â€” | Brake lining level for axle 3 wheel 9 |
| 1066 | `trailer.brake.lining.axle.3.wheel.9.state.enum` | `number` | `â€”` | `13727` | `trailer_brake_lining_axle_3_wheel_9_st_enum` | `io_13727` | â€” | Brake lining status for axle 3 wheel 9 |
| 1067 | `trailer.brake.temperature.axle.1.wheel` | `number` | `â€”` | `13759` | `trailer_brake_temp_axle_1_wheel` | `io_13759` | â€” | Brake temperature for axle 1, indexed by wheel number |
| 1068 | `trailer.brake.temperature.axle.1.wheel.10.state.enum` | `number` | `â€”` | `13748` | `trailer_brake_temp_axle_1_wheel_10_st_enum` | `io_13748` | â€” | Brake temperature status for axle 1 wheel 10 |
| 1069 | `trailer.brake.temperature.axle.1.wheel.6.state.enum` | `number` | `â€”` | `13744` | `trailer_brake_temp_axle_1_wheel_6_st_enum` | `io_13744` | â€” | Brake temperature status for axle 1 wheel 6 |
| 1070 | `trailer.brake.temperature.axle.1.wheel.7.state.enum` | `number` | `â€”` | `13745` | `trailer_brake_temp_axle_1_wheel_7_st_enum` | `io_13745` | â€” | Brake temperature status for axle 1 wheel 7 |
| 1071 | `trailer.brake.temperature.axle.1.wheel.8.state.enum` | `number` | `â€”` | `13746` | `trailer_brake_temp_axle_1_wheel_8_st_enum` | `io_13746` | â€” | Brake temperature status for axle 1 wheel 8 |
| 1072 | `trailer.brake.temperature.axle.1.wheel.9.state.enum` | `number` | `â€”` | `13747` | `trailer_brake_temp_axle_1_wheel_9_st_enum` | `io_13747` | â€” | Brake temperature status for axle 1 wheel 9 |
| 1073 | `trailer.brake.temperature.axle.2.wheel` | `number` | `â€”` | `13764` | `trailer_brake_temp_axle_2_wheel` | `io_13764` | â€” | Brake temperature for axle 2, indexed by wheel number |
| 1074 | `trailer.brake.temperature.axle.2.wheel.10.state.enum` | `number` | `â€”` | `13753` | `trailer_brake_temp_axle_2_wheel_10_st_enum` | `io_13753` | â€” | Brake temperature status for axle 2 wheel 10 |
| 1075 | `trailer.brake.temperature.axle.2.wheel.6.state.enum` | `number` | `â€”` | `13749` | `trailer_brake_temp_axle_2_wheel_6_st_enum` | `io_13749` | â€” | Brake temperature status for axle 2 wheel 6 |
| 1076 | `trailer.brake.temperature.axle.2.wheel.7.state.enum` | `number` | `â€”` | `13750` | `trailer_brake_temp_axle_2_wheel_7_st_enum` | `io_13750` | â€” | Brake temperature status for axle 2 wheel 7 |
| 1077 | `trailer.brake.temperature.axle.2.wheel.8.state.enum` | `number` | `â€”` | `13751` | `trailer_brake_temp_axle_2_wheel_8_st_enum` | `io_13751` | â€” | Brake temperature status for axle 2 wheel 8 |
| 1078 | `trailer.brake.temperature.axle.2.wheel.9.state.enum` | `number` | `â€”` | `13752` | `trailer_brake_temp_axle_2_wheel_9_st_enum` | `io_13752` | â€” | Brake temperature status for axle 2 wheel 9 |
| 1079 | `trailer.brake.temperature.axle.3.wheel` | `number` | `â€”` | `13769` | `trailer_brake_temp_axle_3_wheel` | `io_13769` | â€” | Brake temperature for axle 3, indexed by wheel number |
| 1080 | `trailer.brake.temperature.axle.3.wheel.10.state.enum` | `number` | `â€”` | `13758` | `trailer_brake_temp_axle_3_wheel_10_st_enum` | `io_13758` | â€” | Brake temperature status for axle 3 wheel 10 |
| 1081 | `trailer.brake.temperature.axle.3.wheel.6.state.enum` | `number` | `â€”` | `13754` | `trailer_brake_temp_axle_3_wheel_6_st_enum` | `io_13754` | â€” | Brake temperature status for axle 3 wheel 6 |
| 1082 | `trailer.brake.temperature.axle.3.wheel.7.state.enum` | `number` | `â€”` | `13755` | `trailer_brake_temp_axle_3_wheel_7_st_enum` | `io_13755` | â€” | Brake temperature status for axle 3 wheel 7 |
| 1083 | `trailer.brake.temperature.axle.3.wheel.8.state.enum` | `number` | `â€”` | `13756` | `trailer_brake_temp_axle_3_wheel_8_st_enum` | `io_13756` | â€” | Brake temperature status for axle 3 wheel 8 |
| 1084 | `trailer.brake.temperature.axle.3.wheel.9.state.enum` | `number` | `â€”` | `13757` | `trailer_brake_temp_axle_3_wheel_9_st_enum` | `io_13757` | â€” | Brake temperature status for axle 3 wheel 9 |
| 1085 | `trailer.braking.cylinder.pressure.axle.1.left` | `number` | `â€”` | `13665` | `trailer_braking_cylinder_press_axle_1_left` | `io_13665` | â€” | Braking cylinder pressure for axle 1 left side |
| 1086 | `trailer.braking.cylinder.pressure.axle.1.right` | `number` | `â€”` | `13666` | `trailer_braking_cylinder_press_axle_1_right` | `io_13666` | â€” | Braking cylinder pressure for axle 1 right side |
| 1087 | `trailer.braking.cylinder.pressure.axle.2.left` | `number` | `â€”` | `13667` | `trailer_braking_cylinder_press_axle_2_left` | `io_13667` | â€” | Braking cylinder pressure for axle 2 left side |
| 1088 | `trailer.braking.cylinder.pressure.axle.2.right` | `number` | `â€”` | `13668` | `trailer_braking_cylinder_press_axle_2_right` | `io_13668` | â€” | Braking cylinder pressure for axle 2 right side |
| 1089 | `trailer.braking.cylinder.pressure.axle.3.left` | `number` | `â€”` | `13669` | `trailer_braking_cylinder_press_axle_3_left` | `io_13669` | â€” | Braking cylinder pressure for axle 3 left side |
| 1090 | `trailer.braking.cylinder.pressure.axle.3.right` | `number` | `â€”` | `13670` | `trailer_braking_cylinder_press_axle_3_right` | `io_13670` | â€” | Braking cylinder pressure for axle 3 right side |
| 1091 | `trailer.braking.electric.control.line.support.state.enum` | `number` | `â€”` | `13677` | `trailer_braking_electric_control_line_support_st_enum` | `io_13677` | â€” | Braking via electric control line support status |
| 1092 | `trailer.calibration.load.level.state.enum` | `number` | `â€”` | `13664` | `trailer_calibration_load_lvl_state_enum` | `io_13664` | Sensor `68` (Ã‰tat calibration charge) | Calibration load level status |
| 1093 | `trailer.ebs.vehicle.speed` | `number` | `â€”` | `13652` | `trailer_ebs_vhc_speed` | `io_13652` | Sensor `73` (Vitesse EBS remorque) | Vehicle speed from EBS (Electronic Braking System) |
| 1094 | `trailer.electric.load.proportional.function.installation.state.enum` | `number` | `â€”` | `13808` | `trailer_electric_load_proportional_function_installation_st_enum` | `io_13808` | â€” | Electrical load proportional function installation status |
| 1095 | `trailer.electric.supply.non.braking.systems.state.enum` | `number` | `â€”` | `13806` | `trailer_electric_supply_non_braking_systems_st_enum` | `io_13806` | â€” | Electrical supply of non-braking systems status |
| 1096 | `trailer.lateral.acceleration` | `number` | `â€”` | `13673` | `trailer_lateral_accel` | `io_13673` | â€” | Trailers Lateral acceleration |
| 1097 | `trailer.lift.axle.1.position.state.enum` | `number` | `â€”` | `13681` | `trailer_lift_axle_1_pos_st_enum` | `io_13681` | â€” | Lift axle 1 position status |
| 1098 | `trailer.lift.axle.2.position.state.enum` | `number` | `â€”` | `13682` | `trailer_lift_axle_2_pos_st_enum` | `io_13682` | â€” | Lift axle 2 position status |
| 1099 | `trailer.loading.ramp.approach.assistance.state.enum` | `number` | `â€”` | `13674` | `trailer_loading_ramp_approach_assistance_st_enum` | `io_13674` | â€” | Loading ramp approach assistance status |
| 1100 | `trailer.pneumatic.supply.pressure` | `number` | `â€”` | `13810` | `trailer_pneumatic_supply_press` | `io_13810` | Sensor `62` (Pression pneumatique remorque) | Trailer pneumatic supply pressure |
| 1101 | `trailer.pneumatic.supply.state.enum` | `number` | `â€”` | `13774` | `trailer_pneumatic_supply_st_enum` | `io_13774` | Sensor `61` (Ã‰tat alimentation pneumatique) | Vehicle pneumatic supply status |
| 1102 | `trailer.power.state.enum` | `number` | `â€”` | `13660` | `trailer_power_st_enum` | `io_13660` | Sensor `63` (Ã‰tat alimentation EBS) | Vehicle electrical supply status |
| 1103 | `trailer.red.warning.request.state.enum` | `number` | `â€”` | `13655` | `trailer_red_warning_req_st_enum` | `io_13655` | Sensor `67` (Alerte rouge EBS) | Red warning request status |
| 1104 | `trailer.retarder.control.state.enum` | `number` | `â€”` | `13654` | `trailer_retarder_control_st_enum` | `io_13654` | â€” | Retarder control status |
| 1105 | `trailer.retarder.wheel.torque.load` | `number` | `â€”` | `13658` | `trailer_retarder_wheel_torque_load` | `io_13658` | â€” | Retarder wheel torque |
| 1106 | `trailer.rop.system.state.enum` | `number` | `â€”` | `13678` | `trailer_rop_system_st_enum` | `io_13678` | Sensor `60` (ROP anti-retournement) | ROP (roll over protection) system status |
| 1107 | `trailer.scale.axle.load` | `number` | `â€”` | `13663` | `trailer_scale_axle_load` | `io_13663` | Sensor `69` (Charge balance externe) | Scale axle load measurement |
| 1108 | `trailer.spring.brake.installation.state.enum` | `number` | `â€”` | `13807` | `trailer_spring_brake_installation_st_enum` | `io_13807` | â€” | Spring brake installation status |
| 1109 | `trailer.spring.brake.state.enum` | `number` | `â€”` | `13809` | `trailer_spring_brake_st_enum` | `io_13809` | Sensor `59` (Ã‰tat frein Ã  ressort) | Spring brake status |
| 1110 | `trailer.steering.axle.locking.state.enum` | `number` | `â€”` | `13683` | `trailer_steering_axle_locking_st_enum` | `io_13683` | â€” | Steering axle locking status |
| 1111 | `trailer.stop.lamps.request.state.enum` | `number` | `â€”` | `13676` | `trailer_stop_lamps_req_st_enum` | `io_13676` | â€” | Stop lamps request status |
| 1112 | `trailer.supply.line.braking.state.enum` | `number` | `â€”` | `13675` | `trailer_supply_line_braking_st_enum` | `io_13675` | â€” | Supply line braking status |
| 1113 | `trailer.tire.air.leakage.rate.axle.1.wheel` | `number` | `â€”` | `13775` | `trailer_tire_air_leakage_rate_axle_1_wheel` | `io_13775` | â€” | Tire air leakage rate for axle 1, indexed by wheel number, Pa/sec |
| 1114 | `trailer.tire.air.leakage.rate.axle.2.wheel` | `number` | `â€”` | `13780` | `trailer_tire_air_leakage_rate_axle_2_wheel` | `io_13780` | â€” | Tire air leakage rate for axle 2, indexed by wheel number, Pa/sec |
| 1115 | `trailer.tire.air.leakage.rate.axle.3.wheel` | `number` | `â€”` | `13785` | `trailer_tire_air_leakage_rate_axle_3_wheel` | `io_13785` | â€” | Tire air leakage rate for axle 3, indexed by wheel number, Pa/sec |
| 1116 | `trailer.tire.pressure.axle.1.wheel` | `number` | `â€”` | `13699` | `trailer_tire_press_axle_1_wheel` | `io_13699` | â€” | Tire pressure for axle 1, indexed by wheel number |
| 1117 | `trailer.tire.pressure.axle.2.wheel` | `number` | `â€”` | `13704` | `trailer_tire_press_axle_2_wheel` | `io_13704` | â€” | Tire pressure for axle 2, indexed by wheel number |
| 1118 | `trailer.tire.pressure.axle.3.wheel` | `number` | `â€”` | `13709` | `trailer_tire_press_axle_3_wheel` | `io_13709` | â€” | Tire pressure for axle 3, indexed by wheel number |
| 1119 | `trailer.tire.pressure.state.axle.1.wheel.10.tire.enum` | `number` | `â€”` | `13688` | `trailer_tire_press_st_axle_1_wheel_10_tire_enum` | `io_13688` | â€” | Tire pressure status for axle 1 wheel 10 |
| 1120 | `trailer.tire.pressure.state.axle.1.wheel.6.tire.enum` | `number` | `â€”` | `13684` | `trailer_tire_press_st_axle_1_wheel_6_tire_enum` | `io_13684` | â€” | Tire pressure status for axle 1 wheel 6 |
| 1121 | `trailer.tire.pressure.state.axle.1.wheel.7.tire.enum` | `number` | `â€”` | `13685` | `trailer_tire_press_st_axle_1_wheel_7_tire_enum` | `io_13685` | â€” | Tire pressure status for axle 1 wheel 7 |
| 1122 | `trailer.tire.pressure.state.axle.1.wheel.8.tire.enum` | `number` | `â€”` | `13686` | `trailer_tire_press_st_axle_1_wheel_8_tire_enum` | `io_13686` | â€” | Tire pressure status for axle 1 wheel 8 |
| 1123 | `trailer.tire.pressure.state.axle.1.wheel.9.tire.enum` | `number` | `â€”` | `13687` | `trailer_tire_press_st_axle_1_wheel_9_tire_enum` | `io_13687` | â€” | Tire pressure status for axle 1 wheel 9 |
| 1124 | `trailer.tire.pressure.state.axle.2.wheel.10.tire.enum` | `number` | `â€”` | `13693` | `trailer_tire_press_st_axle_2_wheel_10_tire_enum` | `io_13693` | â€” | Tire pressure status for axle 2 wheel 10 |
| 1125 | `trailer.tire.pressure.state.axle.2.wheel.6.tire.enum` | `number` | `â€”` | `13689` | `trailer_tire_press_st_axle_2_wheel_6_tire_enum` | `io_13689` | â€” | Tire pressure status for axle 2 wheel 6 |
| 1126 | `trailer.tire.pressure.state.axle.2.wheel.7.tire.enum` | `number` | `â€”` | `13690` | `trailer_tire_press_st_axle_2_wheel_7_tire_enum` | `io_13690` | â€” | Tire pressure status for axle 2 wheel 7 |
| 1127 | `trailer.tire.pressure.state.axle.2.wheel.8.tire.enum` | `number` | `â€”` | `13691` | `trailer_tire_press_st_axle_2_wheel_8_tire_enum` | `io_13691` | â€” | Tire pressure status for axle 2 wheel 8 |
| 1128 | `trailer.tire.pressure.state.axle.2.wheel.9.tire.enum` | `number` | `â€”` | `13692` | `trailer_tire_press_st_axle_2_wheel_9_tire_enum` | `io_13692` | â€” | Tire pressure status for axle 2 wheel 9 |
| 1129 | `trailer.tire.pressure.state.axle.3.wheel.10.tire.enum` | `number` | `â€”` | `13698` | `trailer_tire_press_st_axle_3_wheel_10_tire_enum` | `io_13698` | â€” | Tire pressure status for axle 3 wheel 10 |
| 1130 | `trailer.tire.pressure.state.axle.3.wheel.6.tire.enum` | `number` | `â€”` | `13694` | `trailer_tire_press_st_axle_3_wheel_6_tire_enum` | `io_13694` | â€” | Tire pressure status for axle 3 wheel 6 |
| 1131 | `trailer.tire.pressure.state.axle.3.wheel.7.tire.enum` | `number` | `â€”` | `13695` | `trailer_tire_press_st_axle_3_wheel_7_tire_enum` | `io_13695` | â€” | Tire pressure status for axle 3 wheel 7 |
| 1132 | `trailer.tire.pressure.state.axle.3.wheel.8.tire.enum` | `number` | `â€”` | `13696` | `trailer_tire_press_st_axle_3_wheel_8_tire_enum` | `io_13696` | â€” | Tire pressure status for axle 3 wheel 8 |
| 1133 | `trailer.tire.pressure.state.axle.3.wheel.9.tire.enum` | `number` | `â€”` | `13697` | `trailer_tire_press_st_axle_3_wheel_9_tire_enum` | `io_13697` | â€” | Tire pressure status for axle 3 wheel 9 |
| 1134 | `trailer.tire.temperature.axle.1.wheel` | `number` | `â€”` | `13790` | `trailer_tire_temp_axle_1_wheel` | `io_13790` | â€” | Tire temperature for axle 1, indexed by wheel number |
| 1135 | `trailer.tire.temperature.axle.2.wheel` | `number` | `â€”` | `13795` | `trailer_tire_temp_axle_2_wheel` | `io_13795` | â€” | Tire temperature for axle 2, indexed by wheel number |
| 1136 | `trailer.tire.temperature.axle.3.wheel` | `number` | `â€”` | `13800` | `trailer_tire_temp_axle_3_wheel` | `io_13800` | â€” | Tire temperature for axle 3, indexed by wheel number |
| 1137 | `trailer.towing.state.enum` | `number` | `â€”` | `13651` | `trailer_towing_st_enum` | `io_13651` | Sensor `74` (Remorque dÃ©tectÃ©e) | Towed vehicle detection status |
| 1138 | `trailer.towing.vehicle.axle.load` | `number` | `â€”` | `13662` | `trailer_towing_vhc_axle_load` | `io_13662` | Sensor `70` (Charge EBS remorque) | Towed vehicle axle load |
| 1139 | `trailer.traction.help.state.enum` | `number` | `â€”` | `13680` | `trailer_traction_help_st_enum` | `io_13680` | â€” | Traction help system status |
| 1140 | `trailer.vdc.active.state.enum` | `number` | `â€”` | `13672` | `trailer_vdc_active_st_enum` | `io_13672` | â€” | VDC (vehicle dynamic control) active status |
| 1141 | `trailer.vehicle.service.brake.state.enum` | `number` | `â€”` | `13659` | `trailer_vhc_service_brake_st_enum` | `io_13659` | Sensor `65` (Ã‰tat frein de service remorque) | Vehicle service brake status |
| 1142 | `trailer.vehicle.type.enum` | `number` | `â€”` | `13661` | `trailer_vhc_type_enum` | `io_13661` | â€” | Vehicle type classification |
| 1143 | `trailer.yc.system.state.enum` | `number` | `â€”` | `13679` | `trailer_yc_system_st_enum` | `io_13679` | â€” | YC (Yaw Control) system status |
| 1144 | `trip.average.speed` | `number` | `â€”` | `369` | `trip_average_speed` | `io_369` | â€” | Average speed of the trip |
| 1145 | `trip.driving.time` | `number` | `â€”` | `361` | `trip_driving_time` | `io_361` | â€” | Single riding time |
| 1146 | `trip.mileage` | `number` | `â€”` | `834` | `trip_mileage` | `io_834` | â€” | Distance driven since engine start |
| 1147 | `trip.operate.time` | `number` | `â€”` | `360` | `trip_operate_time` | `io_360` | â€” | Single operation time |
| 1148 | `trip.state.enum` | `number` | `â€”` | `250` | `trip_st_enum` | `io_250` | â€” | Trip status |
| 1149 | `trip.status` | `boolean` | `â€”` | `250` | `trip_stat` | `io_250` | â€” | Trip status, true if trip started, false - if stopped |
| 1150 | `ultrasonic.fuel.level` | `number` | `â€”` | `224`, `225`, `327` | `ultrasonic_fuel_lvl` | `io_224`, `io_225`, `io_327` | â€” | Indexed parameter for ultrasonic fuel level |
| 1151 | `ultrasonic.software.state` | `string` | `â€”` | `483` | `ultrasonic_software_st` | `io_483` | â€” | The ultrasonic fuel sensor status as a 2-character code (Software code followed by Hardware code), each character '0' meaning Normal |
| 1152 | `ultrasonic.software.state.enum` | `number` | `â€”` | `208`, `209`, `483` | `ultrasonic_software_st_enum` | `io_208`, `io_209`, `io_483` | â€” | Indexed parameter showing Ultrasonic Fuel sensor software status. 0 - Normal, 1 - The system has just started, output measurement value, 2 - Gas delay count, 3 - The measured value is invalid, 4 - The stationary state, 5 - No data received for 50-60 seconds, 9 - sudden drop, 10 - sudden rise, 11 - delay time of the sudden drop, 12 - delay time of the sudden rise, 13 - The stationary state, maintain the liquid level height value outputu changed, 15 - sudden drop/rise on an tilt |
| 1153 | `user.id` | `string` | `â€”` | `854` | `user_id` | `io_854` | â€” | User ID |
| 1154 | `vehicle.mileage` | `number` | `â€”` | `16`, `216`, `356`, `833` | `vhc_mileage` | `io_16`, `io_216`, `io_356`, `io_833` | â€” | Total calculated mileage |
| 1155 | `vehicle.registration.number` | `string` | `â€”` | `10158`, `231`, `232` | `vhc_registration_num` | `io_10158`, `io_231`, `io_232` | â€” | Vehicle registration number |
| 1156 | `vehicle.vin` | `string` | `â€”` | `10157`, `233`, `234`, `235`, `256`, `325` | `vhc_vin` | `io_10157`, `io_233`, `io_234`, `io_235` (+2) | â€” | VIN of vehicle |
| 1157 | `wifi.mac.address` | `string` | `â€”` | `25036` | `wifi_mac_address` | `io_25036` | â€” | WiFi MAC address |
| 1158 | `wifi.signal.strength` | `number` | `â€”` | `25036` | `wifi_signal_strength` | `io_25036` | â€” | WiFi signal strength, RSSI |
| 1159 | `x.acceleration` | `number` | `â€”` | `17`, `236` | `x_accel` | `io_17`, `io_236` | Sensor `89` (AccÃ©lÃ©ration axe X) | Accelerometer value X |
| 1160 | `y.acceleration` | `number` | `â€”` | `18`, `237` | `y_accel` | `io_18`, `io_237` | Sensor `88` (AccÃ©lÃ©ration axe Y) | Accelerometer value Y |
| 1161 | `z.acceleration` | `number` | `â€”` | `19`, `238` | `z_accel` | `io_19`, `io_238` | Sensor `87` (AccÃ©lÃ©ration axe Z) | Accelerometer value Z |

