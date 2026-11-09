---
title: FMC650 TCA
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_TCA
archived-snapshot: https://web.archive.org/web/20260416084528/https://wiki.teltonika-gps.com/view/FMC650_TCA
captured: 2026-11-04
---

# FMC650 TCA

## Introduction

The document explains how providers can integrate Teltonika’s TCA approved devices with their platform. Device data sending protocol is still the same with some slight changes made to comply with TMA Level 2 requirements. The purpose of this document is to provide TCA and ASPs the necessary guidance on how to implement the TCA compliant solution with FMC650.

**Device**: FMC650
**Firmware**: 03.00.16.Rev.304_1059
**Protocol**: Teltonika [Codec8 Extended](https://wiki.teltonika-gps.com/view/Codec)

**Firmware changelog**

**Previous firmware**: 03.00.16.Rev.303_1059
**New firmware**: 03.00.16.Rev.304_1059
**Changelog**:

- Added fixes where device was sending records every second once the ignition has

been turned off.

- Added fixes where device was generating data at 28th second instead of the

configured 30th (Min Period).

- Added fixes to eliminate record sending delay after vehicles enters or exits the

tunnel.

Identification of lost GPS FixThe base protocol remains the same as of Teltonika’s proprietary [**CODEC 8 EXTENDED**](https://wiki.teltonika-gps.com/view/Codec). Changes specific to TCA in SPEC ID 1059 are described below.

**Via longitude & Latitude values**
After the device’s GNSS Fix is lost, the device sends the following values as latitude and longitude instead of the last known locat on or 0/0.

**Latitude**: 0xFFFFFFFF
**Longitude**: 0xFFFFFFFF

The values are not plottable on the map and integrators can identify and discard these values.

**Via GNSS Status Flag (AVL ID 71)**
GNSS Status Flag (AVL ID 71) can be used to identify a lost GNSS Fix. Refer to the table below for more details:

| GNSS Status (71) | Value | Status |
| --- | --- | --- |
| GNSS Status (71) | 0 | GNSS OFF |
| GNSS Status (71) | 1 | GNSS ON, no GPS |
| GNSS Status (71) | 2 | GNSS ON, without fix |
| GNSS Status (71) | 3 | GNSS ON, with fix |
| GNSS Status (71) | 4 | GNSS SLEEP |
| GNSS Status (71) | 5 | GNSS Overcurrent/protect state |

As mentioned in the table above, GNSS Fix is only valid when the value for AVL ID 71 is “3”. If the GNSS status value (71) not 3, value of longitude and longitude can be discarded

Device configuration guideDevice configuration can be changed according to the described guidelines. Note that any changes should comply with the TCA guidelines.

**Key**:

● locked parameters / not available to be changed
●Can be changed but change should comply with TCA guidelines or as instructed.
● Can be changed.
● Any other changes to the config that are not covered below should be consulted with Teltonika & TCA.

**Note**: Any changes made to the config must not impact the data acquisition settingsand settings related to base parameters (time (data sending time), longitude, latitude & speed).

# Config sections that can be reconfigured as needed by the ASPs

[](https://wiki.teltonika-gps.com/index.php?title=File:2025-02-28_1.png)

# Security configuration

[](https://wiki.teltonika-gps.com/index.php?title=File:2025-02-28_2.png)

# GPRS configuration

[](https://wiki.teltonika-gps.com/index.php?title=File:2025-02-28_3.png)

# Data Acquisition configuration

[](https://wiki.teltonika-gps.com/index.php?title=File:2025-02-28_4.png)

# Features & Accelerometers Features configuration

Scenarios can be activated but **must** be set to low priority only. Any eventual data should be disabled.
By default, all the scenarios are disabled.

# IO configuration

[](https://wiki.teltonika-gps.com/index.php?title=File:2025-02-28_5.png)

# Configuration File

Base configuration file that has been approved by TCA can be provided by Teltonika via Helpdesk.

## Additional salient guidelines to maintain compliance

1. The following 3 parameters should be discarded by ASP from data received from device or should only be used for internal purposes. TCA’s solution should not have the visibility for it.
 1. Number of satellites
 2. HDOP
 3. PDOP
2. All peripherals (RS232/RS485, Video Solutions, Digital I/O, FMS, MobilEye, Tacho, Bluetooth etc.) are disabled* by default. To use any peripherals (including any that are not listed otherwise), approval from TCA and Teltonika is needed. *The only peripheral enabled by default is USB. The interface can be used to load the initial configurations, e.g., APN, server domain & port etc., as per the instructions provided in [Device configuration guide](https://wiki.teltonika-gps.com/index.php?title=Device_configuration_guide).
3. External power voltage and Ignition Status is sent with the AVL data and is contained in each packet.
4. SD card slot has not been used since internal memory is enough to hold records for up to 6 hours. In case external SD card is needed, approval is required from TCA and Teltonika.
5. Device is not password protected by default and can be accessed through USB. ASPs should add keyword protection for serial interface over USB. Refer to [Security Configuration](https://wiki.teltonika-gps.com/index.php?title=Security_Configuration) guide.

## Declarations

1. The date and time data collected by the telematics device is within:
 1. 1 second from UTC when using GNSS signals &
 2. 10 seconds from UTC when not using GNSS signals for 24 hours.

## FAQs

**Q:** How the Real-Time Clock (RTC) operates and is affected by the internal battery?

**A:** If external power is gone device works from battery without any issues in same manner as with external power supply.

**Q:** Clarification on how the internal battery affects timestamp generation and record creation when the device is powered off for several days?

**A:** Internal battery did not affect anything regarding record creation or timestamp. This only depends how log battery will maintain power for device.

**Q:** Understanding of how long the device can generate records once the external power source is disconnected and the internal battery is depleted just an estimate will be enough?

**A:** The amount of time the device will work from internal battery depends on the battery health, how often the device saves/sends information to the server, external peripherals connected to the device and the results may also differ depending on firmware used.

For general comparison purpose, and to see what results can be achieved, you can refer to the following internal test results in different modes and sending frequencies:

| Mode: | Min Period (data saving frequency) | Send Period (data sending frequency) | Starting Voltage | Cut off Voltage | Time achieved |
| --- | --- | --- | --- | --- | --- |
| Operating | 10 seconds | 60 seconds | 10.1V | 7.0V | 452 min (7 hours 32 minutes) |
| Operating | 60 seconds | 60 seconds | 10.1V | 7.0V | 507 min (8 hours 27 minutes) |
| Deep Sleep | 12 hours | 12 hours | 10.2V | 8.2V | 5040 min (84 hours 0 minutes) |
| Online Deep Sleep | 12 hours | 12 hours | 10.2V | 8.6V | 1440 min (24 hours 0 minutes) |

**Q:** What happens when the device is turned back on and how it recovers its clock and data saving capabilities?

**A:** When device is turned on after long time it try to sync RTC time with configured source, record generation capabilities depend on configuration.

**Intellectual property rights**
The Customer acknowledges that UAB TELTONIKA TELEMATICS shall be the exclusive owner of all intellectual property rights used in connection with the products and/or Services the Customer purchases.

AtachmentsYou can download this informatin about FMC650 TCA in a document, by clicking [here](https://web.archive.org/images/1/1b/TELTONIKA_FMCT650_TCA_GUIDELINES_2v4.pdf).

> **Note:** this page embeds screenshots/images served by the archived snapshot from never-captured paths (`web.archive.org/images/...`); the Wayback Machine has no capture of these files, so they could not be preserved. The textual content above is complete.
