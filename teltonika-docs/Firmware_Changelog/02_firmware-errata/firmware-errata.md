---
title: FMC650 firmware errata
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_firmware_errata
archived-snapshot: https://web.archive.org/web/20260118041322/https://wiki.teltonika-gps.com/view/FMC650_firmware_errata
captured: 2026-11-04
---

# FMC650 firmware errata

## Introduction

We are always improving our devices performance, stability and reliability. That’s why Teltonika is one of the leading GNSS trackers manufacturers in the world.
This document describes **FMC650** devices firmware improvements, changes, new features implementations as well as current firmware release version.

## Firmware versioning

- Structure

```
FMX[##].VER.[XX].[YY].[ZZ].Rev.[##] _[ID###]
```

Syntax description

- `FMX[##]` – Specifies the device model compatible with the firmware version.
- `XX` – major FW version.
- `YY` – branch number, shows major changes in firmware, i.e. new module support added or new major feature added.
- `ZZ` – major changes like bigger fixes, improvements and new features addition.
- `##` – minor changes like small fixes and improvements.
- `ID[###]` – Spec ID KEY – Specific clients FW changes.

## Firmware versions

> **Note:** the source page presents firmware releases as a 3-column table (`FIRMWARE VERSION | RELEASE DATE | CHANGES`). Each *CHANGES* cell contains bold group labels plus bullet lists (some nested); flattening that into a table cell destroys the structure, so every release is rendered here as its own section. All wording, order and links are unchanged.

### 03.01.00.Rev.14 — 2025.05.27

**Features Improvement:**

- Enhanced MQTT functionality for reliable data transmission to AWS over RS232/RS485 TCP/UDP link modes.
- Improved MQTT command handling for sending and receiving GPRS commands via AWS servers
- Resolved issue with the tracker not sending beacon data to Azure IoT.
- Fixed an issue where the tracker failed to send beacon records exceeding 1024 bytes over UDP.
- Updated odometer logic for more accurate total distance tracking.

**CAN/Tachograph Improvements:**

- Stability improvements for handling CAN bus message overflow.
- Enhanced accuracy of FMS Eco-Driving metrics: total distance and fuel usage.
- Improved detection of driver state change events from the tachograph during sleep mode.
- Fixed issues where FMS and Manual CAN functions were not operating as intended.
- Corrected logic for Manual CAN command timing:
- Commands now respect the configured timeouts.
- Removed extra transmissions beyond the configured count.
- Ensured correct data transmission even with data masks < 8 bytes.

**General Improvements:**

- Fixed incorrect handling of spaces in APN usernames and passwords.
- Fixed an issue with FOTA Web configuration downloads being unsuccessful.
- Resolved issue where data link was closed after 30 seconds unexpectedly.

**New Implementation**

- Added new SMS/GPRS commands for accessing FMS Eco-Driving accumulator data.
- Introduced support for Codec 14 GPRS commands.

### 03.01.00.Rev.09 — 2025.03.15

**New Features:**

- Added FMS ECO Driving functionality
- Added DM1/DM2 reading functionality
- Added Manual CAN Requests functionality
- Added Manual CAN Commands functionality
- Added NMEA2000 functionality
- Added for electrical vehciles (EV) FMS parameters
- Added ISOBUS agricultural vehicle reading functionality
- Added MQTT support for IoT Azure and AWS
- Added TLS functionality

**General Improvements:**

- Stability improvements
- Connectivity improvements

### 03.00.17.Rev.06 — 2024.12.09

**New Features:**

- Introduced a new filter to accept only DDD messages.
- Added DOUT pre-activation for the Immobilizer feature.
- Implemented a tachograph auto baud rate detection feature.
- Reworked accelerometer calibration and recalibration algorithms.
- Added new IO Elements:
  - Tachograph IO element:
    - Border crossing info
    - Kline d8 privacy mode
    - Vehicle load type info
    - Driver1 last load unload operation time info
    - Driver2 last load unload operation time info
    - Driver private data consent
  - Tall Tale 4 IO element.
  - IMEI IO element.
  - No SIM counter IO element;
  - Detailed LTE signal IO element.
- Added a new SMS command "klinecheck"

**Connectivity Improvements:**

- Improved network connectivity algorithm.
- Improved SIM detection algorithm.
- Improved operator search algorithm.
- Resolved slow execution of GPRS/SMS commands.
- Added APN checks to identify IPv6 or IPv4.

**DDD Download Improvements:**

- Improved DDD files downloading from EFAS GEN2 tachographs.
- Improved tachograph message buffering for stable communication.
- Improved auto tachograph address selection algorithm.
- General improvements to DDD download stability.

**General Improvements:**

- Data Handling:
  - Improved DATA reading via J1708.
  - Improved CAN data reading stability.
  - Stability improvements for CAN adapter communication.
  - Improved tacho data reading from the K-line.
- Record Management:
  - The last known location when the GPS is lost will be saved, ensuring record continuity when configured to save after the position fix.
  - Improved record handling and transmission to duplicate servers.
  - Improved periodic record-sending logic.
- GNSS and Tracking:
  - Improved GNSS packet validation for better tracking quality.
  - Improved static navigation filter activation after restarts.

**Additional Improvements:**

- Updated fuel-level multiplier for CAN adapter.
- Improved manual geofence feature.
- Improved FMS data validation and auto baud rate detection algorithms.
- Improved BLE feature performance.
- Improved tachocheck response by including the following:
  - The tacho address, CAN speed, and ignition status are included in the tacho check response.
  - CAN_x:100 will be returned when incorrect tacho addresses are configured.
  - The device will respond to the tachocheck command during DDD download tasks.
- Stability improvements

### 03.00.15.rev.09 — 2023.12.14

- **NEW!** ALL-CAN300 support added via RS232
- Configuration saving to memory algorithms improvements
- Track (static navigation) stability improvements
- Home mode with Roaming/Global operator connection algorithm improvements
- GPRS activation status information improvements
- Data socket opening algorithms improvements
- Data sending improvements
- GPRS PAP/CHAP algorithms improvements
- Tachograph data source priority algorithms changes
- Tachograph data receiving/reading improvements
- DDD download stability improvements
- K-Line data receiving improvements
- CAN termination parameter configuration via SMS
- BLE records sending improvements
- Crash functionalities algorithms improvements
- WEB FOTA stability improvements
- Stability improvements

### 03.00.14.rev.11 — 2023.08.22

- **NEW!** Smart Tachograph Generation 2 Version 2 support added
- **CHANGED!** FM65 Record size increased to 1004B
- Live IO shown in configurator for Stoneridge tachograph
- Euroscan thermographs communication improvements
- Data socket opening improvements
- 1wire features stability improvements
- FMC650 PAP/CHAP GPRS authentication improvements
- J1708 functionality stability improvements
- Modem working stability improvements
- Communication with FOTA WEB improvements on device startup and receiving configuration

### 03.00.14.rev.01 — 2023.05.30

- FMC650 High frequency on DIN inputs improvements
- FMC650 record counting for getinfo SMS command
- GNSS dual band mode improvements
- RPM calibration on low frequencies improvements
- 1-Wire temperature stability improvements
- Configuration saving improvements

### 03.00.13.rev.05 — 2023.03.13

- Initial release
