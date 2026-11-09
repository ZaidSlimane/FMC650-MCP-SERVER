---
title: "FMC650 Data Sending Parameters ID — Permanent I/O elements"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "Permanent I/O elements"
---

# Permanent I/O elements

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 239 | Ignition | 1 | Unsigned | 0 | 1 | - | - | 0 – Ignition Off / 1 – Ignition On | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 240 | Movement | 1 | Unsigned | 0 | 1 | - | - | 0 – Movement Off / 1 – Movement On | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 22 | Data Mode | 1 | Unsigned | 0 | 5 | - | - | 0 – Home On Stop / 1 – Home On Moving / 2 – Roaming On Stop / 3 – Roaming On Moving / 4 – Unknown On Stop / 5 – Unknown On Moving | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 21 | GSM Signal | 1 | Unsigned | 0 | 5 | - | - | Value in range 1-5 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 200 | Sleep Mode | 1 | Unsigned | 0 | 3 | - | - | 0 - No Sleep / 1 - Deep Sleep / 2 - GPS Sleep / 3 - Online Deep Sleep | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 71 | GNSS Status | 1 | Unsigned | 0 | 5 | - | - | 0 - GNSS OFF / 1 - GNSS ON, no GPS antena / 2 - GNSS ON, without fix / 3 - GNSS ON, with fix / 4 - GNSS SLEEP / 5 - GNSS Overcurrent/protect state | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 181 | GNSS PDOP | 2 | Unsigned | 0 | 500 | 0.1 | - | Probability | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 182 | GNSS HDOP | 2 | Unsigned | 0 | 500 | 0.1 | - | Probability | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 66 | External Voltage | 2 | Unsigned | 0 | 30000 | 0,001 | V | Voltage | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 24 | Speed | 2 | Unsigned | 0 | 350 | - | km/h | Value, km/h | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 205 | GSM Cell ID | 4 | Unsigned | 0 | 4294967295 | - | - | GSM base station ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 206 | GSM Area Code | 2 | Unsigned | 0 | 65535 | - | - | Location Area code (LAC), it depends on GSM operator. It provides unique number which assigned to a set of base GSM stations. | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 67 | Battery Voltage | 2 | Unsigned | 0 | 30000 | 0,001 | V | Voltage, V | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 68 | Battery Current | 2 | Unsigned | 0 | 2400 | - | mA | Current, mA | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 241 | Active GSM Operator | 4 | Unsigned | 0 | 4294967295 | - | - | Currently used GSM Operator code | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 199 | Trip Odometer | 4 | Unsigned | 0 | 4294967295 | - | m | Trip Odometer value in meters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 216 | Total Odometer | 4 | Unsigned | 0 | 4294967295 | - | m | Total Odometer value in meters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 1 | Digital Input 1 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 9 | Analog Input 1 | 2 | Unsigned | 0 | 30000 | 0,001 | V | Voltage, V | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 179 | Digital Output 1 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 236 | Axis X | 2 | Signed | -8000 | 8000 | - | mG | X axis value, mG | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 237 | Axis Y | 2 | Signed | -8000 | 8000 | - | mG | Y axis value, mG | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 238 | Axis Z | 2 | Signed | -8000 | 8000 | - | mG | Z axis value, mG | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 219 | CCID Part1 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Value of SIM ICCID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 220 | CCID Part2 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Value of SIM ICCID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 221 | CCID Part3 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Value of SIM ICCID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 144 | SD Status | 1 | Unsigned | 0 | 1 | - | - | Logic: 0 – not present, 1 – present | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 2 | Digital Input 2 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 3 | Digital Input 3 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10 | Analog Input 2 | 2 | Unsigned | 0 | 30000 | 0,001 | V | Voltage, V | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 180 | Digital Output 2 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 72 | Dallas Temperature 1 | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ), -55 - +115, if 850 – Sensor not ready / if 2000 – Value read error / if 3000 – Not connected / if 4000 – ID failed / if 5000 – same as 850 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 73 | Dallas Temperature 2 | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ), -55 - +115, if 850 – Sensor not ready / if 2000 – Value read error / if 3000 – Not connected / if 4000 – ID failed / if 5000 – same as 850 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 74 | Dallas Temperature 3 | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ), -55 - +115, if 850 – Sensor not ready / if 2000 – Value read error / if 3000 – Not connected / if 4000 – ID failed / if 5000 – same as 850 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 75 | Dallas Temperature 4 | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ), -55 - +115, if 850 – Sensor not ready / if 2000 – Value read error / if 3000 – Not connected / if 4000 – ID failed / if 5000 – same as 850 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 62 | Dallas Temperature ID 1 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Dallas sensor ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 63 | Dallas Temperature ID 2 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Dallas sensor ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 64 | Dallas Temperature ID 3 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Dallas sensor ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 65 | Dallas Temperature ID 4 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Dallas sensor ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 78 | iButton | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | iButton ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 76 | Fuel Counter | 4 | Unsigned | 0 | 4294967295 | - | - | Number of impulses on selected input or difference between impulses on 2 lines Read more about impulse counters here | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10640 | Impulse counter frequency 1 | 4 | Unsigned | 0 | 4294967295 | - | Hz | Impulse frequency of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10641 | Impulse counter RPM 1 | 4 | Unsigned | 0 | 4294967295 | - | RPM | Impulse RPM of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 483 | Impulse Counter 2 | 4 | Unsigned | 0 | 4294967295 | - | - | Number of impulses on selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10642 | Impulse counter frequency 2 | 4 | Unsigned | 0 | 4294967295 | - | Hz | Impulse frequency of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10643 | Impulse counter RPM 2 | 4 | Unsigned | 0 | 4294967295 | - | RPM | Impulse RPM of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10911 | Impulse counter value 1 | 4 | Unsigned | 0 | 4294967295 | - | - | Impulse count of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10912 | Impulse counter value 3 | 4 | Unsigned | 0 | 4294967295 | - | - | Impulse count of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10913 | Impulse counter frequency 3 | 4 | Unsigned | 0 | 4294967295 | - | Hz | Impulse frequency of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10914 | Impulse counter RPM 3 | 4 | Unsigned | 0 | 4294967295 | - | rpm | Impulse RPM of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10915 | Impulse counter value 4 | 4 | Unsigned | 0 | 4294967295 | - | - | Impulse count of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10916 | Impulse counter frequency 4 | 4 | Unsigned | 0 | 4294967295 | - | Hz | Impulse frequency of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10917 | Impulse counter RPM 4 | 4 | Unsigned | 0 | 4294967295 | - | rpm | Impulse RPM of the selected input | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 207 | RFID | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | RFID ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 201 | LLS 1 Fuel Level | 2 | Signed | -4 | 32767 | - | kvants or ltr | Fuel level measured by LLS sensor via RS232 in kvants or liters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 202 | LLS 1 Temperature | 1 | Signed | -128 | 127 | - | °C | Fuel temperature measured by LLS via RS232 in degrees Celsius | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 203 | LLS 2 Fuel Level | 2 | Signed | -4 | 32767 | - | kvants or ltr | Fuel level measured by LLS sensor via RS232 in kvants or liters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 204 | LLS 2 Temperature | 1 | Signed | -128 | 127 | - | °C | Fuel temperature measured by LLS via RS232 in degrees Celsius | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 210 | LLS 3 Fuel Level | 2 | Signed | -4 | 32767 | - | kvants or ltr | Fuel level measured by LLS sensor via RS232 in kvants or liters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 211 | LLS 3 Temperature | 1 | Signed | -128 | 127 | - | °C | Fuel temperature measured by LLS via RS232 in degrees Celsius | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 212 | LLS 4 Fuel Level | 2 | Signed | -4 | 32767 | - | kvants or ltr | Fuel level measured by LLS sensor via RS232 in kvants or liters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 213 | LLS 4 Temperature | 1 | Signed | -128 | 127 | - | °C | Fuel temperature measured by LLS via RS232 in degrees Celsius | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 214 | LLS 5 Fuel Level | 2 | Signed | -4 | 32767 | - | kvants or ltr | Fuel level measured by LLS sensor via RS232 in kvants or liters | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 215 | LLS 5 Temperature | 1 | Signed | -128 | 127 | - | °C | Fuel temperature measured by LLS via RS232 in degrees Celsius | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 178 | Network Type | 1 | Unsigned | 0 | 255 | - | - | 0 - 3G / 1 - 2G / 2 - 4G / 3 - CAT M1 / 4 - CAT NB1 / 255 - Not Available (when in Deep Sleep mode) | FMC640 / FMM640 | Permanent I/O elements |
| 108 | Number Of Records | 2 | Unsigned | 0 | 65535 | - | - | Record counter, counts records saved since startup. | FMC640 / FMM640 | Permanent I/O elements |
| 4 | Digital Input 4 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 50 | Digital Output 3 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 51 | Digital Output 4 | 1 | Unsigned | 0 | 1 | - | - | Logic: 0/1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 11 | Analog Input 3 | 2 | Unsigned | 0 | 30000 | 0,001 | V | Voltage, V | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 245 | Analog Input 4 | 2 | Unsigned | 0 | 30000 | 0,001 | V | Voltage, V | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 70 | PCB Temperature | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ) | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 5 | Dallas Temperature ID 5 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Dallas sensor ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 6 | Dallas Temperature 5 | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ), -55 - +115, / if 850 – Sensor not ready / if 2000 – Value read error / if 3000 – Not connected / if 4000 – ID failed / if 5000 – same as 850 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 7 | Dallas Temperature ID 6 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | Dallas sensor ID | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 8 | Dallas Temperature 6 | 2 | Signed | -550 | 1150 | 0,1 | °C | Degrees ( °C ), -55 - +115, / if 850 – Sensor not ready / if 2000 – Value read error / if 3000 – Not connected / if 4000 – ID failed / if 5000 – same as 850 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 217 | RFID COM2 | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | RFID ID on COM2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 218 | IMSI | 8 | Unsigned | 0 | 0xffffffffffffffff | - | - | International mobile subscriber identity | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 224 | Ultrasonic Fuel Level 1 | 2 | Signed | -15 | 32767 | 0,1 | mm | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 225 | Ultrasonic Fuel Level 2 | 2 | Signed | -15 | 32767 | 0,1 | mm | | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 208 | Ultrasonic Software Status 1 | 1 | Unsigned | 0 | 255 | - | - | 0 – Software – Normal / 1 – Software – The system has just started, output measurement value / 2 – Software – Gas delay count / 3 – Software – The measured value is invalid / 4 – Software – The stationary state / 5 – No data received for 50-60 seconds / 9 – Software – a sudden drop / 10 – Software – a sudden rise / 11 – Software – delay time of the sudden drop / 12 – Software – delay time of the sudden rise / 13 – Software – The stationary state, maintain the liquid level height value outputu changed / 15 – Software – A sudden drop/rise on an tilt / | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 209 | Ultrasonic Software Status 2 | 1 | Unsigned | 0 | 255 | - | - | Values are identical to Ultrasonic Software Status 1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10009 | Eco score | 2 | Unsigned | 0 | 65535 | 0,01 | - | Average amount of events on some distance | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10487 | 1Wire Humidity 1 | 1 | Unsigned | 0 | 0xFF | - | % | 1Wire Humidity 1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10488 | 1Wire Humidity 2 | 1 | Unsigned | 0 | 0xFF | - | % | 1Wire Humidity 2 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10489 | 1Wire Humidity 3 | 1 | Unsigned | 0 | 0xFF | - | % | 1Wire Humidity 3 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10490 | 1Wire Humidity 4 | 1 | Unsigned | 0 | 0xFF | - | % | 1Wire Humidity 4 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10491 | 1Wire Humidity 5 | 1 | Unsigned | 0 | 0xFF | - | % | 1Wire Humidity 5 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 10492 | 1Wire Humidity 6 | 1 | Unsigned | 0 | 0xFF | - | % | 1Wire Humidity 1 | FMX6XX ExpandFMB640 / FMC640 / FMM640 / FMC650 / FMM650 / | Permanent I/O elements |
| 449 | Ignition On Counter | 4 | Unsigned | 0 | 2147483647 | - | s | Duration in seconds which is counted while Ignition state is On / | FMB641 / FMC650 / FMM650 | Permanent I/O elements |
| 1161 | IMEI | 8 | HEX | 0 | 0xffffffffffffffff | - | - | Device's IMEI | FMC650 | Permanent I/O elements |
| 13200 | No SIM Counter | 2 | Unsigned | 2 | 0xffffffff | - | - | No SIM Error Counter | FMC650 | Permanent I/O elements |
| 1148 | Connectivity Quality | 4 | Unsigned | 0 | 2147483647 | - | - | LTE (RSSI only), eMTC (CAT-Mx), and NBIoT Detailed signal strength: / byte 0 - RSSI: 0 - 255 in dBm (negative values) / byte 1 - RSRP: 0 - 255 in dBm (negative values) / byte 2 - SINR: 0 - 250 which translates to -20dB to +30dB (1/5th of dB) / byte 3 - RSRQ: 0 - 255 in dB (negative values) | FMC650 | Permanent I/O elements |
