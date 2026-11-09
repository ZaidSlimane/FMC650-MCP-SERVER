---
title: FMC650 Firmware Changelog
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Firmware_Changelog
archived-snapshot: https://web.archive.org/web/20260416084726/https://wiki.teltonika-gps.com/view/FMC650_Firmware_Changelog
captured: 2026-11-04
---

# FMC650 Firmware Changelog

## Introduction

We are always improving our devices performance, stability and reliability. That’s why Teltonika is one of the leading GNSS trackers manufacturers in the world.
This document describes **FMC650** devices firmware improvements, changes, new features implementations as well as current firmware release version.
**Important:** Please visit [Product Maintenance Policy](https://wiki.teltonika-gps.com/view/Product_Maintenance_Policy) for detailed firmware update policy.

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

### 03.01.01.rev.15 — 2026.03.26

**General Stability / Functionality**

- Improved internal device watchdog mechanisms to ensure more stable long-term operation.
- Fixed inconsistent generation of periodic records so they are now created according to configuration.
- Fixed the record counter IO so that it increments correctly when new records are created and does not reset unexpectedly in specific configurations.
- Fixed unnecessary daily activation of a specific event IO. The IO now triggers only on real events instead of once per day.
- Improved GNSS calculation algorithms for more stable, precise and faster coordinate updates.
- Fixed issues where idling events were not recorded even when idling detection was configured.
- Improved movement detection algorithms for more precise event recording.
- Fixed duplicate or missing “Trip End” status records.
- Fixed DOUT1 behaviour in Geofence scenarios where a non-zero speed was required even when configuration did not require it.
- Fixed unnecessary immobilizer status change records.
- Fixed an issue where the immobilizer scenario could be bypassed under certain conditions and where immobilizer events were generated without values.
- Fixed incorrect behaviour where the immobilizer scenario was not enforced when no authorization list was configured.
- Improved logic for DOUT control in immobilizer scenarios so DOUT states are handled consistently, including across sleep/wake transitions.
- Fixed mismatches between the device-calculated odometer and tachograph odometer.
- Fixed issues where fuel data from certain liquid level sensors could be lost, causing incomplete fuel history.
- Improved total distance and trip distance counting for more accurate mileage tracking.
- Included multiple minor internal stability and bug-fix improvements that collectively improve overall system robustness, logging, and performance.
- Fixed an issue where the device did not enter Deep Sleep mode properly.

**Connectivity & Server Communication**

- Fixed an issue where the device did not establish a data connection if the APN field was left blank.
- Improved modem and network handling, including better operator selection and reconnection behaviour, reducing unexpected data link issues.
- Fixed behaviour where the device continuously contacted the NTP server when GNSS fix was unavailable.
- Fixed an issue where incorrect NTP responses could lead to timestamps being set in the future.
- Fixed a problem where the device could receive future timestamps when NITZ was used as the time synchronisation source.
- Fixed an issue where the device did not send records to the configured duplicate server correctly.
- Fixed failures to send records to the duplicate server in some TCP/UDP scenarios.
- Fixed an issue where records were bundled into a single packet rather than being sent individually as expected.
- Fixed delays in record transmission over UDP.
- Fixed issues where the device could disconnect from the server after executing certain GPRS or configuration commands.
- Fixed internal log download issues via over-the-air tools.
- Fixed a situation where over-the-air firmware update tasks could remain stuck in “Pending” or “Executing” state.
- Fixed occasional failures of firmware updates performed via the configuration tool, reducing the chance of interrupted or failed local updates.
- Fixed an issue where the device was not generating Iridium SBD records.
- Improved RS232 data sending to the Iridium module to ensure that SBD payloads are delivered reliably and without truncation.

**Bluetooth / BLE**

- Fixed cases where the device generated unnecessary beacon records in stop mode.
- Fixed issues where advanced beacon packet length information was not generated correctly in advanced beacon mode.
- Fixed incorrect reading of custom BLE parameter values when the data size was less than three bytes.

**MQTT**

- Fixed incorrect packing of MQTT packets containing multiple JSON objects when sending to cloud platforms.
- Fixed an issue where the device did not send data via MQTT to custom cloud endpoints in some configurations.
- Fixed behaviour where long RS232 messages were not sent correctly via MQTT, which could cause truncation or loss when transmitted as JSON.
- Improved long-term stability of MQTT JSON operation, increasing reliability for continuous cloud integrations and complex payloads.

**Tachograph, K-Line & Driver/Company Data**

- Implemented separate internal instance IDs for tachograph IO elements and DDD file downloading to avoid interference between live data and file download.
- Fixed a problem where tachograph auto address selection did not work correctly.
- Fixed an issue where the working tachograph address could change unexpectedly after firmware updates, causing DDD download failures.
- Fixed errors where remote tachograph file download sessions could be interrupted or not start at all in certain conditions.
- Fixed behaviour where the tachograph company card number continued to be reported even after the card was removed.
- Fixed an issue where the tachograph Driver Name field was missing or incomplete in driver information data.
- Improved character encoding for tachograph Driver Name, including extended and Nordic letters.
- Fixed an issue where no data was received over K-Line, preventing tachograph and diagnostic data reception.
- Improved K-Line detection and privacy mode handling, including explicit privacy status reporting where applicable.
- Enhanced tachograph-related logging and error handling to make diagnostics clearer.
- Fixed transmission of vehicle and driver identification values (such as VIN, VRN and driver identification) so that accurate identification data is always sent.

**FMS / Manual CAN / CAN / Eco Driving & Vehicle Data**

- Fixed missing or incorrect reading of specific FMS parameters, including version-specific parameter sets.
- Fixed fluctuating fuel levels when using FMS or CAN sources, improving fuel accuracy for both standard and EV FMS use cases.
- Fixed issues where FMS-based speed was not being used correctly as the selected speed source.
- Improved overall CAN stability so that tachograph CAN and FMS information is not lost due to CAN bus overflow.
- Fixed incomplete or malformed responses to commands that start or stop Manual CAN (MCAN) transmissions, ensuring clear responses and reliable remote control.
- Ensured that Manual CAN requests and commands are no longer executed when ignition is OFF.

**New Features**

- NEW! Added support for storing and sending records from [RAM memory](https://wiki.teltonika-gps.com/view/FMC650_System_settings#Records_Saving/Sending_Without_TS). recommended for rapid data sending i.e. data saving every second etc.
- NEW! Implemented a new feature called the “[one minute rule](https://wiki.teltonika-gps.com/view/FMC650_LVCAN_I/O,FMS_IO_and_Tachograph_data_elements#Driver_Working_State_Filters)” for tachograph driving state, reducing unnecessary state toggling and improving driving/rest detection accuracy.
- NEW! [Apache Thermograph](https://wiki.teltonika-gps.com/view/FMC650_Thermograph#Apache).
- NEW! [Trailer CAN](https://wiki.teltonika-gps.com/view/FMC650_TrailerCAN) functionality.
- NEW! Implemented [“scanevfms“](https://wiki.teltonika-gps.com/view/FMB_scanevfms) command for diagnosing electric trucks, providing targeted EV CAN diagnostics.
- NEW! Implemented “[can_info](https://wiki.teltonika-gps.com/view/FMB_can%EF%BC%BFinfo)“ command that returns details of the CAN bus (baud rates, modes and other key parameters), aiding diagnostics.
- NEW! Updated the “[tachocheck“](https://wiki.teltonika-gps.com/view/FMB_tachocheck) command to show more detailed information.

**Configuration, Parameters & Tools**

- Fixed an issue where a single setparam command could not change multiple parameters at once.
- Fixed behaviour where the odometer command always returned a GNSS-based odometer value regardless of the configured odometer source.
- Fixed cases where the device disconnected unnecessarily from the configurator.
- Fixed an issue where the SIM PIN was not remembered after soft or hard reset.

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
- Axle wheel dependency is improved and configurable via command.

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

\***NEW!** ALL-CAN300 support added via RS232

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

\***NEW!** Smart Tachograph Generation 2 Version 2 support added

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

\*FMC650 High frequency on DIN inputs improvements

- FMC650 record counting for getinfo SMS command
- GNSS dual band mode improvements
- RPM calibration on low frequencies improvements
- 1-Wire temperature stability improvements
- Configuration saving improvements

### 03.00.13.rev.05 — 2023.03.13

\*Initial release
