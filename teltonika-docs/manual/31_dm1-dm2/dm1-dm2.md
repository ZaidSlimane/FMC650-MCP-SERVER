---
title: FMC650 DM1 and DM2
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_DM1_and_DM2
archived-snapshot: https://web.archive.org/web/20260512123233/https://wiki.teltonika-gps.com/view/FMC650_DM1_and_DM2
captured: 2026-11-04
---

# FMC650 DM1 and DM2

# Introduction

With a professional device lineup, telltale information (dashboard indicators) from heavy-duty vehicles can be read remotely to identify a variety of issues. New feature of Diagnostic Trouble Code (DTC) reading will help to narrow down the specific faults happening in vehicles.

With FMC650 you can read 2 types of DTC messages based on J1939 protocol:

- DM1 – Communicates currently present faults
- DM2 – Reports stored faults

FMC650 is able to read DM codes and pass them to the server in IO element. When active DM1 messages are present on the CAN line, they are broadcast frequently. The FMC650 device stores these codes in its internal memory and transmits only newly detected DTC codes.

DM2 messages are not streamed, but instead, they must be requested.

# Functionality Description

This functionality is available from Firmware version **03.01.02.rev.06** or higher.

For proper functionality, the device requires ignition to be active. Source of ignition and voltage level can be selected from **System** tab.

Ignition has to be active for at least 14 sec to start generating the DTC list. If ignition is turned off, the device will clean all DM1 and DM2 codes and functionality will not be working.

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Ignition.png)

After the device is connected to the Configurator, there will be **DM1 / DM2** tab made available. There is a configurable DM1 / DM2 Data source parameter. This parameter selects the CAN source based on which device will parse DM data from. Based on selected data source, device will also call a request for DTCs.

**Note:** The functionality is completely separated from the FMS source.

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Data_source_selection.png)

- NONE – Device will not use any CAN as data source
- CAN1 – Device will use CAN1 as data source
- CAN2 – Device will use CAN2 as data source
- BOTH – Device will use CAN1 and CAN2 as data source

Bellow **Data source** parameters there is a list of configurable IOs

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Configurable_IOs.png)

„DTC DM1“ and “DTC DM2“ shows the last DTC that has been detected. „Active DM1 List“ and „Active DM2 List“ provides a list of all active DTCs for a given source.

Example of generating DM1 / DM2 list: To register DM1 code, it is required to send a command using (pgn 0xFEFA). Device will first check if such DTC code exist in the system (MCUID and CAN Source has to be unique for each DTC). Otherwise, DTC will be rejected.

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Configurator_outputs.png)

9D000301:01:01

- 9D000301 – DTC in hexadecimal format
- 01 – MCU source that reported the DTC
- 01 – Device CAN source used (00 - CAN1, 01 - CAN2)

9D000302:02:01

- 9D000302 – DTC in hexadecimal format
- 02 – MCU source that reported the DTC
- 01 – Device CAN source used (00 - CAN1, 01 - CAN2)

Based on configured „Priority“, „Event Only“ and „Operand“ device will add this parameter to record.

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Terminal_logs.png)

To remove one of the DTC from DM1 list, DM2 code (pgn 0xFEFB) is required. Device will check if the sent DTC code exists in the system (MCUID and CAN Source has to be unique for each DTC). If sent DTC does not exist in the system, it will be rejected.

Based on previous example, sending DTC 9D000301 with MCUID 01 on CAN2, device remove this DTC from the system, as the result, this DTC is removed from „Active DM1 List“ and added to the „Active DM2 List“.

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Configurator_outputs_2.png)

Log example:

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Terminal_logs_2.png)

That DTCs will be added to record and would be accessible on server. Data on server need to be converted from HEX to ASCII.

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Outputs_from_server.png)

**39443030303330323A30323A30313B** -> (after conversion from hex to ANSCII) **9D000302:02:01**;

**39443030303330313A30313A30313B** -> (after conversion from hex to ANSCII) **9D000301:01:01**;

# DM1/DM2 Message Structure

**DM1** is a J1939 diagnostic message used to broadcast active faults and warning lamp status. Its structure is split into a header (lamp status) followed by one or more diagnostic trouble codes. Unlike most J1939 messages, DM1 has a variable length: if there are 0–1 active DTCs, it fits in a single CAN frame, while 2 or more DTCs require a multi-frame message with additional DTC entries added.

[](https://wiki.teltonika-gps.com/index.php?title=File:DM1_and_DM2_Message_Structure.png)

The first 2 bytes form the lamp status header, which is shared across all DTCs. Each lamp uses 2-bit values to indicate status (off/on), along with flash signals defining how the lamp blinks (slow or fast). These signals are interpreted collectively across ECUs, with a central controller typically deciding the final lamp behavior based on the most severe reported condition.

Each DTC contains four key components:

- **SPN(*Suspect Parameter Number)*** - Identifies the faulty subsystem.
- **FMI(*Failure Mode Identifier)*** - Describes the type of failure.
- **CM(*SPN Conversion Method)*** - Indicates the encoding method.
- **OC(*Occurrence Count)*** - Counts how often the fault has occurred.

These elements provide detailed, structured information about vehicle faults while supporting both standardized and proprietary diagnostics.

# DM1 Lamp Status and Flash Signals

The **DM1 (Diagnostic Message 1)** in the **J1939** protocol reports active **Diagnostic Trouble Codes (DTCs)** and controls vehicle warning indicators. It defines the behavior of the **Malfunction Indicator Lamp (MIL)** and other warning lamps, which can be off, on solid, or flashing, depending on the severity and priority of detected faults. Flashing typically signals a more urgent or severe condition, while a solid light indicates an active but less critical issue.

The first byte represents the status of four indicator lamps:

- **PL (Protect Lamp)** - DTC's indicate non-electronic subsystem issue.
- **AWL(Amber Warning Light)** - DTC's indicate a non-critical issue that does not warrant stopping the vehicle.

- **RSL(Red Stop Lamp)** - DTC's indicate a critical issue that warrants stopping the vehicle immediately.

- **MIL(Malfunction Indicator Lamp)** - At least one DTC indicates emissions related issue.

Each lamp is encoded using 2 bits, allowing four possible states: **off, on, slow flash, and fast flash**. This compact encoding means all lamp states are conveyed within a single byte, with each pair of bits mapped to a specific lamp in a fixed order. These lamp states directly inform the operator about the severity and urgency of active faults.

DM1 encodes warning lamp information in its first 2 bytes, combining both lamp status and flash behavior. Each lamp is represented by two 2-bit fields—one in byte 1 (status) and one in byte 2 (flash).

To decode, split each byte into 2-bit segments and map each pair to its corresponding lamp. The final behavior is determined by combining status and flash (e.g., ON + fast flash = rapidly blinking warning).

# Global and Manufacturer SPN Codes

## Global-Level SPN codes

Standard codes are defined by the SAE J1939 standards and are recognized across all compliant vehicles and equipment. The SPNs for these codes fall within the range of **1 to 24,324** representing widely used parameters such as engine speed, coolant temperature, or oil pressure. FMI values are standardized, describing specific failure patterns such as high voltage, circuit open, or out-of-range conditions.

Because they are standardized, these codes are universally interpretable by any compliant diagnostic tool without requiring manufacturer-specific references.

## Manufacturer-Level SPN codes

Manufacturer-level or proprietary codes are reserved for OEM-specific faults that are not defined in the J1939 standard. These allow manufacturers to monitor unique components, systems, or operational conditions that are specific to their equipment.

The SPNs for proprietary codes typically occupy the high end of the 19-bit field, ranging from **516,096 to 524,287**. FMI values may be standard or custom, but the meaning of the SPN is defined by the manufacturer. Accurate interpretation requires access to OEM documentation, as these codes are not universally defined or interpretable.

# Functionality Block Diagram

Graphic representation of **DM1** and **DM2** functionality:

[](https://wiki.teltonika-gps.com/index.php?title=File:DTC_Functionality_blok_diagram.png)

> **Note:** this page embeds screenshots/images served by the archived snapshot from never-captured paths (`web.archive.org/images/...`); the Wayback Machine has no capture of these files, so they could not be preserved. The textual content above is complete.
