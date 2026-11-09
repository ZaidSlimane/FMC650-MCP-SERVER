---
title: "FMC650 Data Sending Parameters ID — BLE"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "BLE"
---

# BLE

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 701 | BLE Temperature 1 | 2 | Signed | -400 | 1250 | 0.1 | °C | Degrees ( °C ), -40 - +125; Error codes: / 4000 - abnormal sensor state / 3000 - sensor not found / 2000 - failed sensor data parsing | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 702 | BLE Temperature 2 | 2 | Signed | -400 | 1250 | 0.1 | °C | Degrees ( °C ), -40 - +125; Error codes: / 4000 - abnormal sensor state / 3000 - sensor not found / 2000 - failed sensor data parsing | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 703 | BLE Temperature 3 | 2 | Signed | -400 | 1250 | 0.1 | °C | Degrees ( °C ), -40 - +125; Error codes: / 4000 - abnormal sensor state / 3000 - sensor not found / 2000 - failed sensor data parsing | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 704 | BLE Temperature 4 | 2 | Signed | -400 | 1250 | 0.1 | °C | Degrees ( °C ), -40 - +125; Error codes: / 4000 - abnormal sensor state / 3000 - sensor not found / 2000 - failed sensor data parsing | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 705 | BLE Battery 1 | 1 | Unsigned | 0 | 100 | - | % | Battery level of sensor 1 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 706 | BLE Battery 2 | 1 | Unsigned | 0 | 100 | - | % | Battery level of sensor 2 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 707 | BLE Battery 3 | 1 | Unsigned | 0 | 100 | - | % | Battery level of sensor 3 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 708 | BLE Battery 4 | 1 | Unsigned | 0 | 100 | - | % | Battery level of sensor 4 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 709 | BLE Humidity 1 | 2 | Unsigned | 0 | 1000 | 0.1* | %RH | Humidity as measured by sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 710 | BLE Humidity 2 | 2 | Unsigned | 0 | 1000 | 0.1* | %RH | Humidity as measured by sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 711 | BLE Humidity 3 | 2 | Unsigned | 0 | 1000 | 0.1* | %RH | Humidity as measured by sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 712 | BLE Humidity 4 | 2 | Unsigned | 0 | 1000 | 0.1* | %RH | Humidity as measured by sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 713 | BLE Sensor Custom 1 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Raw data of 1st BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 714 | BLE Sensor Custom 2 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Raw data of 2nd BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 715 | BLE Sensor Custom 3 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Raw data of 3rd BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 716 | BLE Sensor Custom 4 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Raw data of 4th BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 717 | BLE Illum1 | 2 | Unsigned | 0 | 0xFFFF | - | - | Luminosity value of a BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 718 | BLE Illum2 | 2 | Unsigned | 0 | 0xFFFF | - | - | Luminosity value of a BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 719 | BLE Illum3 | 2 | Unsigned | 0 | 0xFFFF | - | - | Luminosity value of a BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 720 | BLE Illum4 | 2 | Unsigned | 0 | 0xFFFF | - | - | Luminosity value of a BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 721 | BLE LLS Fuel 1 | 2 | Unsigned | 0 | 0xFFFF | - | - | Fuel Level | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 722 | BLE LLS Fuel 2 | 2 | Unsigned | 0 | 0xFFFF | - | - | Fuel Level | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 723 | BLE LLS Fuel 3 | 2 | Unsigned | 0 | 0xFFFF | - | - | Fuel Level | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 724 | BLE LLS Fuel 4 | 2 | Unsigned | 0 | 0xFFFF | - | - | Fuel Level | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 725 | BLE Freq 1 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Frequency value of BLE fuel sensor #1 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 726 | BLE Freq 2 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Frequency value of BLE fuel sensor #2 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 727 | BLE Freq 3 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Frequency value of BLE fuel sensor #3 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 728 | BLE Freq 4 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Frequency value of BLE fuel sensor #4 | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 729 | BLE Sensor Custom 12 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 730 | BLE Sensor Custom 13 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 731 | BLE Sensor Custom 14 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 732 | BLE Sensor Custom 15 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 733 | BLE Sensor Custom 22 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 734 | BLE Sensor Custom 23 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 735 | BLE Sensor Custom 24 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 736 | BLE Sensor Custom 25 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 737 | BLE Sensor Custom 32 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 738 | BLE Sensor Custom 33 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 739 | BLE Sensor Custom 34 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 740 | BLE Sensor Custom 35 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 741 | BLE Sensor Custom 42 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 742 | BLE Sensor Custom 43 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 743 | BLE Sensor Custom 44 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 744 | BLE Sensor Custom 45 | 4 | Unsigned | 0 | 0xFFFFFFFF | - | - | Raw data of BLE sensor | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 10500 | BLE Advertisement data | Variable | HEX | 0 | 1024 | - | - | List of parsed advertising data of BLE beacons (Eddystone and iBeacon) found by BLE scanning | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
| 548 | Advanced BLE Advertisement data | Variable | HEX | 0 | 1024 | - | - | List of parsed advertising data of BLE beacons](Eddystone and iBeacon) found by BLE scanning | FMC650 / FMM650 / FMC640 / FMM640 | BLE elements |
