---
title: "Alphabetical dictionary FMC650 – FMS – CAN/J1939 – Wialon – Camera — Configurator notes (EN)"
source: "PDF export of the Alphabetical dictionary tab FMC650 – FMS – CAN/J1939 – Wialon – Camera (Teltonika Configurator)"
source-file: "dictionnaire-alphabetique-fmc650-fms-canj1939-wialon-camera.pdf"
source-pages: 50
source-generated: "2026-11-05T08:37:58Z"
language: en
companion-to: "../glossary.md"
---

# Alphabetical dictionary FMC650 – FMS – CAN/J1939 – Wialon – Camera — Configurator notes (EN)

> **Note:** Supplementary notes extracted from the French PDF of the Configurator tab
> `dictionnaire-alphabetique-fmc650-fms-canj1939-wialon-camera.pdf`, generated on
> **2026-11-05T08:37:58Z** — more recent than the wiki snapshot kept in
> this folder. The content was translated into English; it complements the reference
> page [`glossary.md`](../glossary.md).
> PDF extraction specifics: section headings sometimes appear
> after the text they introduce, figures reuse file
> names from page 1, and some wide tables are rendered
> row by row because the PDF text layer does not always preserve
> columns. Unarchived `docs.tinolyx.com` image links have been
> removed; unique figures are grouped under `## Figures` at the end of the file.
> This file contains no images.

<!-- PDF p. 1 -->

.cfg
Meaning: Configuration file saved from the Configurator.
Location / note: E.g. config_test26.cfg .
Original category: Validation and diagnostic terms.

**0x2D50 → 50 2D**

Meaning: Reordering of bytes in little-endian.
Location / note: CAN payload of the example.
Original category: J1939 encoding and decoding example.

**1-Wire**

Meaning: Simple bus used by the FMC650 for iButton/RFID and compatible
temperature probes.
Location / note: 1-Wire / Authorization ID List.
Original category: FMC650 peripheral interfaces.

**11600 → 0x2D50**

Meaning: Conversion of the raw decimal value into hexadecimal.
Location / note: Intermediate encoding step.
Original category: J1939 encoding and decoding example.

## 0–9 / symbols

<!-- PDF p. 2 -->

**1450 rpm → RAW 11600**

Meaning: Conversion example: with a factor of 0.125 rpm/bit and offset 0, 1450 / 0.125
= 11600.
Location / note: Educational example used in the conversation.
Original category: J1939 encoding and decoding example.

**29-bit / Extended CAN ID**

Meaning: Extended CAN identifier format used by J1939.
Location / note: Manual CAN can be configured as Extended 29-bit.
Original category: CAN, SAE J1939 and FMS.

**2G / GSM / GPRS**

Meaning: Older cellular technologies used for voice/SMS or GPRS data
and as a fallback when available.
Location / note: GPRS is also the name of the Configurator network tab.
Original category: Mobile network, SIM and servers.

**30 s before + 30 s after**

Meaning: Chosen video policy: keep a 60-second clip around the accident
rather than sending 24 h of video to the server.
Location / note: Setting to be made mainly in the DVR, not in the
FMC650.
Original category: Camera, DVR and 30 s before / 30 s after backup.

**4-direction / 360°**

Meaning: System using several cameras to cover several sides of the vehicle and
provide an extended view.
Location / note: SINOTRUK system photographed.
Original category: Camera, DVR and 30 s before / 30 s after backup.

**60301**

Meaning: Example MCC/MNC code discussed: 603 = the region, 01 = corresponding
operator. It is used to identify/classify a mobile network.
Location / note: GSM Operators → Home/Roaming lists.
Original category: Mobile network, SIM and servers.

## A

<!-- PDF p. 3 -->

**Accelerator Pedal Position**

Meaning: Accelerator pedal position as a percentage.
Location / note: FMS IO → Low + Monitoring.
Category: FMS IO – truck data.

**Accelerometer**

Meaning: Internal sensor measuring acceleration on three axes. It can be used for
Movement, Towing, Crash and other scenarios.
Location / note: FMC650 hardware.
Category: Safety, accelerometer and driving.

**Accelerometer (Movement Source)**

Meaning: Uses the internal accelerometer to detect movement. Choice retained for the
project so as not to depend solely on GPS or CAN.
Location / note: System → Movement Source = Accelerometer.
Category: System Settings and GNSS.

**Accept only DDD messages**

Meaning: Filter allowing only DDD messages to be accepted in the relevant logic.
Location / note: CAN/Tachograph → Tachograph Settings.
Category: Tachograph and DDD.

**Accumulator**

Meaning: Counter accumulated locally: distance, fuel, coasting, braking, cruise, retarder,
etc.
Location / note: FMSED.
Category: FMSED / FMS Eco Driving.

**ACK**

Meaning: Acknowledgement. Acknowledgment sent by the server to confirm
how many records have been accepted.
Location / note: Allows retransmission if necessary.
Category: AVL, Codec and server transmission.

**Activation Timeout**

Meaning: Waiting time before towing monitoring becomes active.
Location / note: Towing Detection.
Category: Safety, accelerometer and driving.

**AdBlue Level**

<!-- PDF p. 4 -->

Meaning: AdBlue level as a percentage.
Location / note: FMS IO → Low + Monitoring if available.
Category: FMS IO – truck data.

**AdBlue Status**

Meaning: Status of the AdBlue/DEF system.
Location / note: FMS IO → On Change if actual value.
Category: FMS IO – truck data.

**Source Address**

Meaning: Part of the J1939 identifier indicating the ECU that emits the message.
Location / note: Allows the network nodes to be distinguished.
Category: CAN, SAE J1939 and FMS.

**AIN**

Meaning: Analog Input. Analog input measuring a voltage from a compatible
sensor.
Location / note: 4 AIN on FMC650.
Category: I/O, priority and operands.

**AIN4/DOUT4 Mode**

Meaning: The shared channel can operate as an AIN4 analog input or a DOUT4 digital
output.
Location / note: System → AIN4/DOUT4 Mode.
Category: System Settings and GNSS.

**Alarm IN**

Meaning: DVR alarm input that can potentially trigger/protect an
event recording.
Location / note: To be identified in the DVR pinout.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Alarm OUT**

Meaning: DVR alarm output that can potentially inform the FMC650 of a
state/alarm.
Location / note: To be identified in the DVR pinout.
Category: Camera, DVR and 30 s before / 30 s after backup.

**ALL-CAN300**

Meaning: Teltonika CAN reading adapter with broader coverage for supported vehicles.

<!-- PDF p. 5 -->

Location / note: Optional device, not necessary if direct FMS is sufficient.
Category: CAN, SAE J1939 and FMS.

**ALM**

Meaning: DVR alarm indicator. It indicates that the DVR has event/alarm
logic, without by itself revealing the pinout.
Location / note: DVR front panel.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Ambient Air Temperature**

Meaning: Ambient air temperature provided by the vehicle.
Location / note: FMS IO → Low + Monitoring or None if not needed.
Category: FMS IO – truck data.

**Analog Input Value Range**

Meaning: Electrical range of an analog input, for example 10 V or 30 V. It must
match the sensor/wiring.
Location / note: System.
Category: System Settings and GNSS.

**Analog LLS**

Meaning: Fuel level probe providing an analog signal.
Location / note: FMC650 AIN with calibration.
Category: FMS Fuel Settings and fuel.

**Angle**

Meaning: Heading change threshold used in certain Towing settings.
Location / note: Towing Detection.
Category: Safety, accelerometer and driving.

**APN**

Meaning: Access Point Name. Operator parameter necessary to establish the mobile
data connection.
Location / note: GPRS → APN.
Category: Mobile network, SIM and servers.

**APN Username / Password**

Meaning: APN credentials if required by the operator.
Location / note: GPRS.
Category: Mobile network, SIM and servers.

<!-- PDF p. 6 -->

**Authorization ID List**

Meaning: List of authorized or registered iButton/sensor identifiers.
Location / note: Configurator → Authorization ID List.
Category: FMC650 peripheral interfaces.

**Auto DDD Address Selection**

Meaning: Automatic selection of the tachograph DDD communication address.
Location / note: CAN/Tachograph → Enable when used.
Category: Tachograph and DDD.

**Auto Geofence**

Meaning: Geofence created/managed automatically by the terminal according to the configured logic.
Location / note: Auto Geofence.
Category: Geofences, trip and odometer.

**AVIN-AVOUT**

Meaning: Audio-video inputs/outputs of the DVR for cameras and display.
Location / note: Marking visible on your DVR.
Category: Camera, DVR and 30 s before / 30 s after backup.

**AVL**

Meaning: Automatic Vehicle Location. In the Teltonika ecosystem, an AVL record groups
the timestamp, priority, GNSS position and I/O elements.
Location / note: Created by the FMC650 before transmission.
Category: AVL, Codec and server transmission.

**AVL ID**

Meaning: Teltonika identifier associated with a parameter transmitted in the I/O element of an
AVL record.
Location / note: E.g. FMS parameters, axes, ignition, etc.
Category: AVL, Codec and server transmission.

**AVL Record**

Meaning: Individual record containing timestamp, priority, GPS Element and I/O
Element.
Location / note: One or more records can be grouped in a
packet.
Category: AVL, Codec and server transmission.

**Axis X / Axis Y / Axis Z**

<!-- PDF p. 7 -->

Meaning: Raw values of the three axes of the internal accelerometer. They can be
disabled in the regular stream without disabling Crash, Towing or Movement.
Location / note: I/O → Axis X/Y/Z.
Category: I/O, priority and operands.

**Axle Weight 1..15**

Meaning: Estimated weight/load per axle when the truck exposes this data.
Location / note: FMS IO → None until validation with a weighbridge.
Category: FMS IO – truck data.

**Battery Charge Mode / On Need**

Meaning: Internal battery charging strategy. On Need means charge when
necessary.
Location / note: System.
Category: System Settings and GNSS.

**Battery Current**

Meaning: Current related to the internal battery according to available measurement.
Location / note: I/O.
Category: I/O, priority and operands.

**Battery Voltage**

Meaning: Voltage of the FMC650 internal battery.
Location / note: I/O / Maintenance.
Category: I/O, priority and operands.

**Beacon**

Meaning: BLE beacon used for proximity/asset or zone identification.
Location / note: Beacon List.
Category: FMC650 peripheral interfaces.

**BEIDOU**

Meaning: Chinese satellite navigation constellation.
Location / note: GNSS Source.
Category: System Settings and GNSS.

## B

<!-- PDF p. 8 -->

**Bit**

Meaning: Binary unit 0 or 1. CAN signals can start at a specific bit and have
a defined length.
Location / note: Used in masks and decoding.
Category: CAN, SAE J1939 and FMS.

**Blacklist**

Meaning: List of networks not to be used. An overly restrictive configuration can prevent
registration.
Location / note: GSM Operators.
Category: Mobile network, SIM and servers.

**Bluetooth / BLE**

Meaning: Bluetooth Low Energy for compatible beacons and sensors.
Location / note: Bluetooth 4.0 / Beacon List.
Category: FMC650 peripheral interfaces.

**Brake Pedal Position**

Meaning: Position/intensity of the brake control as a percentage.
Location / note: FMS IO → Low + Monitoring.
Category: FMS IO – truck data.

**Brake Switch**

Meaning: Brake state: applied or not. This is a binary state.
Location / note: FMS IO → Low + On Change recommended.
Category: FMS IO – truck data.

**Braking Count/Time**

Meaning: Number and duration of braking phases according to FMS data.
Location / note: FMSED.
Category: FMSED / FMS Eco Driving.

**Buffer**

Meaning: Memory/circular segment allowing images already recorded
before the event to be available.
Location / note: Necessary for 30 s pre-event.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Bus speed / CAN bit rate**

<!-- PDF p. 9 -->

Meaning: CAN bus speed in kbit/s. It must match the vehicle network
exactly.
Location / note: CAN/Tachograph → CAN1/CAN2 bus speed. 250 or 500
kbit/s are common depending on the vehicle.
Category: CAN, SAE J1939 and FMS.

**Buzzer**

Meaning: Audible warning device that can be controlled by a DOUT to warn the
driver.
Location / note: Must be physically identified before use.
Category: Safety, accelerometer and driving.

**Byte / octet**

Meaning: Group of 8 bits. J1939 values are stored in one or more bytes of the
CAN payload.
Location / note: E.g. two bytes for Engine Speed.
Category: CAN, SAE J1939 and FMS.

**Cab Interior Temperature**

Meaning: Cab interior temperature.
Location / note: FMS IO → often None for flatbed transport if not useful.
Category: FMS IO – truck data.

**Tracking rate**

Meaning: Overall frequency resulting from Min Period, distance, angle, speed and events.
There is no single fixed interval if several conditions are active.
Location / note: Data Acquisition.
Category: Data Acquisition and send logic.

**Calibration Table**

Meaning: Correspondence table between raw value and actual value, for example voltage
→ liters.
Location / note: Sensor settings.
Category: Wialon Local – processing, sensors and reports.

**Camera / camera**

## C

<!-- PDF p. 10 -->

Meaning: Optical sensor that produces the video stream. In your installation, several
cameras are connected to the DVR.
Location / note: Truck video system.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Camera I/O**

Meaning: Family of camera status parameters available for compatible Teltonika
integrations.
Location / note: Do not assume that it applies to the SINOTRUK DVR.
Category: Camera, DVR and 30 s before / 30 s after backup.

**CAN**

Meaning: Controller Area Network. Communication bus allowing ECUs to exchange
short digital messages over two differential wires.
Location / note: Vehicle bus. The FMC650 has two CAN J1939
interfaces.
Category: CAN, SAE J1939 and FMS.

**CAN ID**

Meaning: CAN frame identifier. In J1939, the 29-bit extended identifier contains
in particular the priority, information allowing the PGN to be determined and the source address.
Location / note: Used in Manual CAN.
Category: CAN, SAE J1939 and FMS.

**CAN speed (Movement Source)**

Meaning: Would use the vehicle speed read on CAN. To be used only after validation
of the CAN/FMS data.
Location / note: System option.
Category: System Settings and GNSS.

**CAN-CONTROL**

Meaning: Teltonika CAN solution intended for certain readings/commands on compatible
vehicles.
Location / note: Optional device.
Category: CAN, SAE J1939 and FMS.

**CAN-H**

Meaning: High line of the differential CAN bus.
Location / note: Always used with CAN-L.
Category: CAN, SAE J1939 and FMS.

<!-- PDF p. 11 -->

**CAN-L**

Meaning: Low line of the differential CAN bus.
Location / note: Always used with CAN-H.
Category: CAN, SAE J1939 and FMS.

**Payload weight**

Meaning: Mass of goods transported by the vehicle.
Location / note: Business KPI; may require vehicle/mission weight.
Category: Maintenance, weight, tires and fleet management.

**Protected clip / Locked Event File**

Meaning: Video file marked so that it is not overwritten by the normal loop, according to
the DVR function.
Location / note: To be configured in the DVR if supported.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Clutch Switch**

Meaning: Clutch state.
Location / note: FMS IO → Low + On Change.
Category: FMS IO – truck data.

**CMS**

Meaning: Content/Camera Management System depending on the manufacturer: platform for managing
DVRs, live streams and archives.
Location / note: Can act as an intermediary to Wialon if compatible.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Coasting**

Meaning: Driving phase with low or zero drive demand according to vehicle logic.
Location / note: FMSED / Eco Driving.
Category: Maintenance, weight, tires and fleet management.

**Codec 16**

Meaning: Another Teltonika AVL format mentioned in the protocol documentation.
Location / note: Use according to server compatibility.
Category: AVL, Codec and server transmission.

**Codec 8**

Meaning: Teltonika format for encoding AVL records.

<!-- PDF p. 12 -->

Location / note: Teltonika protocol option.
Category: AVL, Codec and server transmission.

**Codec 8 Extended / Codec 8E**

Meaning: Extended version allowing in particular larger I/O identifiers, suited
to the many advanced parameters of the FMC650.
Location / note: System → Data Protocol.
Category: AVL, Codec and server transmission.

**Combined Vehicle Weight**

Meaning: Combined vehicle/combination weight when the data is available.
Location / note: FMS IO → None until validation.
Category: FMS IO – truck data.

**Configurator**

Meaning: Teltonika software used to read, modify and save the FMC650
configuration.
Location / note: PC tool.
Category: Validation and diagnostic terms.

**Crash Detection**

Meaning: Function using the accelerometer to detect an impact consistent with an
accident according to threshold and duration.
Location / note: Accelerometer Features → Crash Detection.
Category: Safety, accelerometer and driving.

**Crash Trace**

Meaning: Acceleration trace kept around the Crash event.
Location / note: Crash Detection.
Category: Safety, accelerometer and driving.

**CRC-16**

Meaning: Packet integrity check. The server can reject a corrupted packet.
Location / note: Server-side validation step.
Category: AVL, Codec and server transmission.

**Cruise Control Active**

Meaning: Cruise control state.
Location / note: FMS IO → Low + On Change.
Category: FMS IO – truck data.

<!-- PDF p. 13 -->

**Cruise Control Distance/Time**

Meaning: Distance/time traveled with cruise control active.
Location / note: FMSED.
Category: FMSED / FMS Eco Driving.

**Current Value**

Meaning: Value currently received/measured in the Configurator. A hyphen "-" means
that no value is currently available in this screen.
Location / note: FMS IO / Status depending on display.
Category: I/O, priority and operands.

**Current Value = "-"**

Meaning: No value is currently displayed/received for this parameter. A Wialon sensor must
not be built on it before validation.
Location / note: FMS IO / Status.
Category: Validation and diagnostic terms.

**Custom Sensor / custom sensor**

Meaning: Sensor created from a parameter or a custom formula.
Location / note: Wialon.
Category: Wialon Local – processing, sensors and reports.

**Dallas Temperature Sensor**

Meaning: Compatible 1-Wire temperature probe.
Location / note: Authorization ID List / 1-Wire.
Category: FMC650 peripheral interfaces.

**Dashboard**

Meaning: Synthetic interface displaying certain current values of the unit. A value
displayed on the dashboard is not automatically the same source as a report's.
Location / note: Wialon UI.
Category: Wialon Local – processing, sensors and reports.

**Dashboard Mileage / dashboard mileage**

## D

<!-- PDF p. 14 -->

Meaning: Distance value displayed by the vehicle or in the Wialon interface depending on the
sensor/mapping. It must not be confused with the calculated GPS mileage.
Location / note: Wialon + FMS source to be validated.
Category: Geofences, trip and odometer.

**Data Acquisition**

Meaning: FMC650 collection engine. It decides when to create records based on
movement, time, distance, angle and speed variation, with
Home/Roaming/Unknown profiles.
Location / note: Configurator → Data Acquisition.
Category: Data Acquisition and send logic.

**Data Mask**

Meaning: Mask defining which bits/bytes of a Manual CAN frame are used to
extract a value.
Location / note: Manual CAN.
Category: Manual CAN, Requests and Commands.

**DDD**

Meaning: File format for downloading tachograph/driver card data used in the
tachograph ecosystem.
Location / note: Tachograph Settings / TachoSync.
Category: Tachograph and DDD.

**DDD Download Source**

Meaning: Choice of interface used to retrieve DDD data: CAN1, CAN2, Front
Panel or OFF depending on installation.
Location / note: CAN/Tachograph → Tachograph Settings.
Category: Tachograph and DDD.

**DEBUG**

Meaning: Manufacturer service/diagnostic port.
Location / note: Do not use as a normal interface without
documentation.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Decoding**

Meaning: Reverse operation: identification of the message, extraction of bits/bytes,
endianness, factor and offset to reconstruct the physical value.
Location / note: Performed by the FMC650 or a compatible decoder.
Category: J1939 encoding and decoding example.

<!-- PDF p. 15 -->

**Deep Sleep**

Meaning: Deeper sleep mode further reducing terminal activity.
Location / note: System → Sleep Mode.
Category: System Settings and GNSS.

**Device Type**

Meaning: Type of equipment chosen in Wialon to select the appropriate decoding
protocol.
Location / note: Unit Properties → General.
Category: Wialon Local – processing, sensors and reports.

**Diagnostics Supported**

Meaning: Indicates the diagnostic capabilities exposed by the FMS interface.
Location / note: FMS IO → diagnostic, often None in production.
Category: FMS IO – truck data.

**Digital LLS**

Meaning: Digital probe often communicating via RS232/RS485.
Location / note: RS232/RS485.
Category: FMS Fuel Settings and fuel.

**DIN**

Meaning: Digital Input. Digital 0/1 input for ignition, door, SOS button or another
contact.
Location / note: 4 DIN on FMC650.
Category: I/O, priority and operands.

**DIN1**

Meaning: Digital input 1. Often used for the contact/ignition when the wiring
is correct.
Location / note: System + I/O.
Category: System Settings and GNSS.

**Direction Indicator**

Meaning: State of the turn signals/direction indicators according to available data.
Location / note: FMS IO → On Change or None if not used.
Category: FMS IO – truck data.

**DLC**

<!-- PDF p. 16 -->

Meaning: Data Length Code. Size of the data field of the classic CAN frame,
often 8 bytes in classic J1939.
Location / note: CAN structure term.
Category: CAN, SAE J1939 and FMS.

**DM1**

Meaning: J1939 diagnostic message for active faults.
Location / note: Proactive maintenance; High + On Change if supported.
Category: FMS IO – truck data.

**DM2**

Meaning: J1939 diagnostic message for previously active/historical faults.
Location / note: Maintenance; Low + On Change if supported.
Category: FMS IO – truck data.

**DOUT**

Meaning: Digital Output. Digital output allowing a buzzer, relay, LED or
another compatible device to be controlled.
Location / note: 4 DOUT on FMC650.
Category: I/O, priority and operands.

**DOUT → DVR Alarm IN**

Meaning: Proposed architecture: an FMC650 DOUT, via relay/optocoupler if necessary,
can signal a crash to the DVR to protect the clip, only after validation of the
electrical pinout.
Location / note: Future integration.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Driver Card**

Meaning: Driver tachograph card and associated identification information.
Location / note: Tachograph Data.
Category: Tachograph and DDD.

**Driver Change trigger**

Meaning: Trigger on a driver change.
Location / note: FMSED.
Category: FMSED / FMS Eco Driving.

**Driver Score / driver score**

<!-- PDF p. 17 -->

Meaning: Index combining several driving events and measurements. It must be
normalized by distance/time for a fair comparison.
Location / note: Wialon / analytics.
Category: Maintenance, weight, tires and fleet management.

**Driver State**

Meaning: Driver state from the tachograph: driving, rest, work, availability
depending on protocol/source.
Location / note: Tachograph Data.
Category: Tachograph and DDD.

**DTC**

Meaning: Diagnostic Trouble Code, electronic fault code.
Location / note: FMS/diagnostic depending on support.
Category: FMS IO – truck data.

**DualCam / DashCam**

Meaning: Teltonika cameras with a specific documented integration with the
FMC650. Your SINOTRUK DVR must not be configured as DualCam/DashCam without
proof of compatibility.
Location / note: RS232/RS485 → Camera Interface only for
compatible hardware.
Category: Camera, DVR and 30 s before / 30 s after backup.

**Duplicate data mode**

Meaning: Mode in which records can be sent to two configured servers. To be used
only if the architecture provides for it.
Location / note: Relevant if Server #1 and Server #2 are both
active.
Category: Mobile network, SIM and servers.

**Duration**

Meaning: Duration during which a condition must be present or duration of an impact according to
the scenario.
Location / note: Towing/Crash.
Category: Safety, accelerometer and driving.

**DVR**

Meaning: Digital Video Recorder. Recording unit that receives the camera streams,
compresses them, stores them and manages playback and events.

<!-- PDF p. 18 -->

Location / note: Your SINOTRUK unit with AVIN-AVOUT, RS232, I/O, SD,
ALM.
Category: General architecture of the truck and telematics.

**ECM / Engine ECU**

Meaning: Engine control unit. It processes in particular engine speed, load, fuel,
temperatures and certain diagnostics.
Location / note: Frequent source of engine FMS data.

**Eco Driving**

Meaning: Wialon module for evaluating driving using acceleration, braking, cornering,
idling and speed according to configuration.
Location / note: Unit Properties → Eco Driving.

**ECU**

Meaning: Electronic Control Unit, electronic control unit of the vehicle. An ECU receives
sensor signals, calculates physical values and exchanges messages with the
other control units.
Location / note: E.g. engine ECU, ABS/EBS, transmission, suspension.

**EEC1**

Meaning: Electronic Engine Controller 1, engine parameter group used in
the J1939 example.
Location / note: PGN 61444 in the example.

**Encoding**

Meaning: Transformation of a physical value into a raw/bytes representation compliant with
the protocol.
Location / note: Performed by the ECU according to the signal rules.

**End of Day trigger**

Meaning: Trigger at the end of the day to send a summary.
Location / note: FMSED.

**Engine Coolant Temperature**

Meaning: Engine coolant temperature.

## E

<!-- PDF p. 19 -->

Location / note: FMS IO → Low + Monitoring.

**Engine Hours Sensor**

Meaning: Wialon sensor for engine hours depending on parameter/ignition/source.
Location / note: Unit Properties → Sensors.

**Engine MIL Indicator**

Meaning: Malfunction Indicator Lamp, engine fault indicator state.
Location / note: FMS IO → High + On Change recommended if reliable.

**Engine Oil Pressure**

Meaning: Engine oil pressure in kPa.
Location / note: FMS IO → Low + Monitoring; Wialon alert on manufacturer
threshold.

**Engine Oil Temperature**

Meaning: Engine oil temperature.
Location / note: FMS IO → Low + Monitoring.

**Engine Percent Load**

Meaning: Engine load expressed as a percentage.
Location / note: FMS IO → Low + Monitoring.

**Engine Speed / RPM**

Meaning 1 – J1939: Engine speed expressed in revolutions per minute. In J1939, it can be
represented by SPN 190.
Location / note 1: FMS IO → Engine speed.
Meaning 2 – FMS IO: Engine speed in revolutions/minute.
Location / note 2: FMS IO → Low + Monitoring.

**Engine Total Fuel Used**

Meaning: Cumulative counter of fuel consumed.
Location / note: FMS IO → Low + Monitoring.

**Engine Total Hours of Operation**

Meaning: Cumulative engine hours counter.
Location / note: FMS IO → Low + Monitoring.
eSIM

<!-- PDF p. 20 -->

Meaning: Electronically integrated SIM, supported by certain FMC650 variants/configurations.
Location / note: Alternative to physical SIM cards.

**ETA**

Meaning: Estimated Time of Arrival, estimated arrival time.
Location / note: Logistics KPI calculated from tracking and the trip.

**Event Only**

Meaning: Indicates whether the value should mainly be present in the event context rather
than in all regular records, according to the parameter logic.
Location / note: FMS IO/I/O.

**Event Record / Eventual Record**

Meaning: Record created or marked following a condition/event rather than only
by the normal rate.
Location / note: I/O, Features, Accelerometer Features.

**Excessive Idling**

Meaning: Detection of an active engine/ignition while the vehicle remains stopped beyond a
delay.
Location / note: Accelerometer Features / Features depending on firmware.

**External Voltage**

Meaning: External vehicle supply voltage measured by the terminal.
Location / note: I/O / Status.

**Firmware**

Meaning: Internal FMC650 software. Certain functions depend on the installed version.
Location / note: Maintenance / Configurator.
flespi.gw
Meaning: Domain name seen in a configuration file. The suffix indicates a
gateway-type endpoint, but its actual business role in your installation must not
be assumed without confirmation.

## F

<!-- PDF p. 21 -->

Location / note: Secondary server observed in config_test26.cfg .

**FMC650**

Meaning: Professional Teltonika telematics terminal for heavy trucks. It collects GNSS,
I/O, CAN/FMS, tachograph and device data and then creates AVL
records transmitted to the server.
Location / note: Unit installed in the truck.

**FMI**

Meaning: Failure Mode Identifier. Part of the J1939 diagnostic describing the type of failure
of an SPN.
Location / note: Used in the interpretation of J1939 DTCs.

**FMS**

Meaning: Fleet Management System Interface / FMS Standard. Standardized interface that
exposes certain truck data from J1939 to telematics. It does not represent
all the vehicle's internal data.
Location / note: Configurator → CAN/Tachograph → FMS data source, then
FMS IO.

**FMS Fuel Settings**

Meaning: Configuration block that selects the source of the fuel level and
consumption.
Location / note: FMS IO / FMS Fuel Settings.

**FMS Gateway**

Meaning: Vehicle gateway that exposes a standardized subset of fleet management
data from the truck's internal network.
Location / note: Between internal CAN/J1939 and FMC650.

**FMS I/O (Status)**

Meaning: Screen allowing you to see whether actual FMS values are arriving from the truck.
Location / note: Validation before enabling FMS IO.

**FMSED**

Meaning: FMS Eco Driving. FMC650 function that aggregates FMS driving statistics
locally before transmission.
Location / note: Configurator → FMSED / FMS Eco Driving.

**Formula**

<!-- PDF p. 22 -->

Meaning: Mathematical expression applied to a parameter to produce a sensor
value.
Location / note: Sensor settings.

**FOTA / FOTA Web**

Meaning: Remote firmware/terminal update/configuration mechanisms.
Location / note: Teltonika maintenance functions.

**Front Panel**

Meaning: Option in which DDD downloading is associated with the tachograph front
interface/panel according to supported configuration.
Location / note: DDD download source.

**FTP**

Meaning: File Transfer Protocol. Possible method of uploading files if the DVR supports it.
Location / note: Potential DVR function, not confirmed on your
model.

**Fuel Consumption Source = CAN**

Meaning: Total consumption comes from CAN/FMS.
Location / note: Recommended if reliable.

**Fuel Counter**

Meaning: Fuel function/counter managed by the terminal according to source/configuration.
Location / note: Features/I/O depending on firmware.

**Fuel Level / Fuel Level 1**

Meaning: Main tank level as a percentage or value defined by the
standard/source.
Location / note: FMS IO → Low + Monitoring.

**Fuel Level 2**

Meaning: Level of a second tank if the vehicle actually provides it.
Location / note: FMS IO → Low + Monitoring if real, otherwise None.

**Fuel Level Source = CAN**

Meaning: Fuel level is read from the CAN/FMS bus.
Location / note: To be kept if the CAN data is real and validated.

<!-- PDF p. 23 -->

**Fuel Level Source = J1708**

Meaning: Fuel level would be taken from J1708 on a compatible vehicle.
Location / note: Use only if actually wired/supported.

**Fuel Rate**

Meaning: Instantaneous fuel flow, generally in liters/hour.
Location / note: FMS IO → Low + Monitoring.

**Fuel Supply Estimated Remaining Distance**

Meaning: Estimate of the remaining range with the available fuel.
Location / note: FMS IO → Low + Monitoring if reliable.

**Fuel Type**

Meaning: Fuel type. Rather static information than recurring telemetry.
Location / note: FMS IO → generally None.

**Fuel While Idling**

Meaning: Fuel consumed while idling.
Location / note: FMSED / KPI.

**GALILEO**

Meaning: European satellite navigation constellation.
Location / note: GNSS Source.

**Gateway / gateway**

Meaning: Equipment or function that connects two networks or two protocols and can
filter/standardize data.
Location / note: E.g. manufacturer's FMS gateway.

**Geofence / geofence**

Meaning: Virtual geographic zone used to detect entry, exit or presence of the
vehicle.
Location / note: FMC650 Geofence or Wialon.

**Geofence Wialon**

## G

<!-- PDF p. 24 -->

Meaning: Geofence centralized in Wialon, often preferable for the business sites of a
fleet.
Location / note: Wialon → Geofences.

**GLONASS**

Meaning: Russian satellite navigation constellation.
Location / note: GNSS Source.

**GNSS (Movement Source)**

Meaning: Would use movement determined by GNSS.
Location / note: System option.

**GNSS Algorithm A1**

Meaning: GNSS algorithm proposed as a Green Driving source when one does not want
to use a classic accelerometer calibration.
Location / note: Features → Green Driving → Source.

**GNSS HDOP / PDOP**

Meaning: GNSS geometry/quality indicators. Lower is generally better.
Location / note: Status/I/O.

**GNSS Info**

Meaning: GNSS diagnostic screen: position, satellites and reception quality.
Location / note: Status.

**GNSS Source**

Meaning: Selection of the constellations used by the GNSS receiver.
Location / note: System → GNSS Source.

**GPS**

Meaning: American satellite navigation constellation.
Location / note: GNSS Source.

**GPS Element**

Meaning: Part of the AVL record containing position and GNSS information: latitude, longitude,
altitude, angle, satellites, speed.
Location / note: Created by the FMC650.

**GPS Sleep**

<!-- PDF p. 25 -->

Meaning: Sleep mode in which the GNSS part is saved according to conditions.
Location / note: System → Sleep Mode.

**Green Driving**

Meaning: Eco-driving scenario detecting behaviors such as harsh acceleration,
braking and cornering.
Location / note: Features → Green Driving.

**GSM Info**

Meaning: Mobile network diagnostic screen.
Location / note: Status.

**GSM Operators**

Meaning: Tab for managing allowed/roaming/blacklist operator lists according to
firmware.
Location / note: Configurator → GSM Operators.

**Handling Information**

Meaning: Operational information field whose usefulness depends on the vehicle/standard. Do
not enable it without understanding its value.
Location / note: FMS IO → None initially.

**Handshake**

Meaning: Initial connection exchange in which the terminal identifies itself and the server accepts or
rejects the IMEI.
Location / note: Before normal sending of AVL packets.

**Harsh Acceleration**

Meaning: Acceleration that is too sudden according to the configured threshold.
Location / note: Green Driving / Eco Driving.

**Harsh Braking**

Meaning: Deceleration/braking that is too sudden according to the configured threshold.
Location / note: Green Driving / Eco Driving.

**Harsh Cornering**

## H

<!-- PDF p. 26 -->

Meaning: Corner taken with lateral acceleration above the configured threshold.
Location / note: Green Driving / Eco Driving.

**Hexadecimal / HEX**

Meaning: Base 16 notation used to represent CAN identifiers and bytes easily.
Location / note: E.g. 0x2D50 .

**High**

Meaning: High priority for important events requiring fast transmission.
Location / note: I/O/FMS IO/Features.

**High Level**

Meaning: High threshold used when the operand depends on a range/condition.
Location / note: I/O/FMS IO.

**High Resolution Engine Total Fuel Used**

Meaning: Cumulative fuel counter with finer resolution.
Location / note: FMS IO → Low + Monitoring; source/units in FMS Fuel
Settings.

**High Resolution Fuel Used = Liters**

Meaning: Unit used for the high-resolution fuel counter.
Location / note: FMS Fuel Settings.

**History**

Meaning: Database of messages already received and stored per unit.
Location / note: Wialon Local → messages / reports / tracks.

**History / message storage**

Meaning: Decoded messages kept per unit and used for tracks, sensors, reports
and events.
Location / note: Wialon Local.

**Home**

Meaning: State in which the SIM is attached to its home network. The Data
Acquisition settings in the Home column apply.
Location / note: Data Acquisition → Home.
<!-- PDF p. 27 -->

**I/O**

Meaning: Input/Output. Set of inputs, outputs and parameters monitored/transmitted by
the FMC650.
Location / note: Configurator → I/O.

**I/O (DVR)**

Meaning: DVR input/output connector. It can contain Alarm IN/OUT and other
signals, but the exact pinout must be obtained before wiring.
Location / note: DVR unit.

**I/O Check on Startup**

Meaning: I/O check option at startup depending on firmware.
Location / note: System.

**I/O Element**

Meaning: Part of the AVL record containing the telematics parameters: ignition, FMS,
voltages, events, etc.
Location / note: Built according to the I/O/FMS IO configuration.

**I/O Info**

Meaning: Diagnostic screen for the FMC650 inputs/outputs and states.
Location / note: Status.

**I/O Send Mode**

Meaning: Determines how to handle unavailable I/Os. Don't Send avoids sending an
artificial/old value when the data is not valid.
Location / note: System.
iButton
Meaning: 1-Wire electronic identifier used to identify/authorize a driver.
Location / note: Authorization ID List / 1-Wire.

**Idling / idle**

Meaning: Engine/ignition active while the vehicle is not moving.
Location / note: Excessive Idling + Wialon reports.

## I

<!-- PDF p. 28 -->

**Ignition (Movement Source)**

Meaning: Would use the ignition state as an indication of movement, which can
confuse engine ON with the vehicle actually moving.
Location / note: System option.

**Ignition (Tachograph Source)**

Meaning: Option that reuses the ignition source defined in System.
Location / note: Preferable if System → Ignition Source is validated.

**Ignition OFF Timeout**

Meaning: Delay after ignition off before considering the trip finished.
Location / note: Trip/Odometer.

**Ignition Source**

Meaning: Source used to determine the vehicle ignition state.
Location / note: System → Ignition Source. DIN1 recommended if actually
wired.

**IMEI**

Meaning: International Mobile Equipment Identity. Unique identifier of the modem/terminal
used to identify the FMC650 to the server.
Location / note: Wialon → Unit Unique ID.

**Immobilizer**

Meaning: Function/scenario that can control an output for immobilization according to a
secure logic. Do not use without a safety study and validated wiring.
Location / note: Features.

**Instantaneous Fuel Economy**

Meaning: Instantaneous fuel efficiency indicator. May be redundant with Fuel Rate
+ speed.
Location / note: FMS IO → optional.

**Instrument Cluster / dashboard**

Meaning: Vehicle control unit and display. It displays speed, RPM, fuel, warning lights and
other information received from the ECUs. The FMC650 generally does not read the screen itself.
Location / note: The dashboard and the FMC650 can receive the
same CAN data.

<!-- PDF p. 29 -->

**Internal Memory**

Meaning: Internal flash memory used for configuration and temporary storage of
records.
Location / note: FMC650.

**IR**

Meaning: Infrared receiver, often intended for a remote control/service.
Location / note: DVR front panel.

**J1708**

Meaning: Older heavy truck communication standard that can provide in particular
fuel data on certain vehicles.
Location / note: FMS Fuel Settings can offer CAN or J1708.

**Jamming Detection**

Meaning: Detection of radio jamming/interference according to the FMC650 algorithm.
Location / note: Features → Network Jamming.

**K-Line**

Meaning: Automotive serial link used in particular for certain tachograph/diagnostic
communications.
Location / note: FMC650 hardware interface.

**KPI**

Meaning: Key Performance Indicator, key performance indicator.
Location / note: E.g. L/100 km, idling/100 km, events/100 km.

## J

## K

## L

<!-- PDF p. 30 -->

**L/100 km**

Meaning: Consumption indicator: liters consumed per 100 km.
Location / note: Wialon/report calculation from fuel and distance.

**Listener**

Meaning: Server process that listens on a port for a given terminal type/protocol.
Location / note: Wialon Local side.

**Little-endian**

Meaning: Byte order in which the least significant byte is placed first.
Location / note: In the RPM example, 0x2D50 is transmitted as 50 2D .

**LLS**

Meaning: Liquid Level Sensor. External fuel level probe, analog or
digital.
Location / note: Alternative/complement to FMS.

**Load from device**

Meaning: Reads the current FMC650 configuration in the Configurator.
Location / note: Backup procedure.

**Loop Recording**

Meaning: Loop recording: when storage is full or the retention duration is
reached, old normal videos are overwritten.
Location / note: DVR; in your case approximately 24 h.

**Low**

Meaning: Normal priority for telemetry and non-critical events.
Location / note: I/O/FMS IO.

**Low Level**

Meaning: Low threshold used when the operand depends on a range/condition.
Location / note: I/O/FMS IO.

**LTE Cat 1**

Meaning: 4G technology used by the FMC650 for data transmission, with 2G fallback
depending on model/network.
Location / note: Terminal cellular interface.

<!-- PDF p. 31 -->

**LVCAN / LV-CAN200**

Meaning: Teltonika CAN reading adapter for certain vehicles. It decodes vehicle
data according to program/configuration.
Location / note: LVCAN tab when the adapter is actually installed.

**Predictive maintenance**

Meaning: Use of trends and signals (DTC, temperatures, pressures, load, history) to anticipate a failure.
Location / note: Advanced project objective.

**Preventive maintenance**

Meaning: Maintenance planned before failure according to distance, engine hours or schedule.
Location / note: Wialon/ERP/workshop.

**Manage Video**

Meaning: Wialon right allowing the video functions to be managed.
Location / note: Access rights.

**Manual CAN**

Meaning: Function allowing manual decoding of CAN frames known by their
ID and structure.
Location / note: Configurator → Manual CAN.

**Manual CAN Command**

Meaning: Active command injected on the CAN. It can influence the vehicle and must remain
disabled without documentation and tests.
Location / note: Manual CAN Commands.

**Manual CAN Request**

Meaning: Active request sent on the CAN to request data from an ECU when
the protocol is known.
Location / note: Manual CAN Requests; leave disabled without manufacturer
specification.

**Manual Geofence**

## M

<!-- PDF p. 32 -->

Meaning: Zone defined manually in the FMC650.
Location / note: Manual Geofence Settings / Zones.

**Mapping**

Meaning: Association between a received AVL ID/parameter and a Wialon sensor/use.
Location / note: Essential step for mileage, fuel, engine hours, etc.

**Mapping validation**

Meaning: Verification that the correct AVL parameter is linked to the correct Wialon sensor with the
correct unit/formula.
Location / note: Wialon.

**Max Speed**

Meaning: Speed threshold of the Over Speeding scenario. It must comply with company
policy and applicable legal limits.
Location / note: Features → Over Speeding.

**MCC/MNC**

Meaning: Numeric codes identifying the country and the mobile operator.
Location / note: Used in GSM Operators.

**MDVR**

Meaning: Mobile Digital Video Recorder. DVR designed for vehicles, generally with
automotive power supply, camera inputs and alarm/network functions.
Location / note: Generic term for embedded video recorders.
mG
Meaning: Milli-g, unit used to express small accelerations relative to gravity.
Location / note: Accelerometer axes.

**MicroSD**

Meaning: External memory card supported by the FMC650 for certain storage uses
; not to be confused with the SD card of the video DVR.
Location / note: FMC650 hardware / DVR depending on context.

**Mileage Sensor**

Meaning: Wialon mileage sensor used to calculate/display a distance according to a
defined source.
Location / note: Unit Properties → Sensors / mileage settings.

<!-- PDF p. 33 -->

**Min Angle**

Meaning: Minimum heading change that can trigger a record.
Location / note: Data Acquisition → Moving.

**Min Distance**

Meaning: Minimum distance traveled that can trigger a new record.
Location / note: Data Acquisition → Moving.

**Min Period**

Meaning: Minimum time interval used to trigger the creation of a new record
according to the profile.
Location / note: Data Acquisition.

**Min Saved Records**

Meaning: Minimum number of records accumulated before certain send attempts/conditions.
Location / note: Data Acquisition.

**Min Speed Delta**

Meaning: Minimum speed variation that can trigger a record.
Location / note: Data Acquisition → Moving.

**Mission**

Meaning: Operational transport cycle from departure to arrival, used to calculate distance,
fuel, time and incidents.
Location / note: Wialon/ERP.

**Monitoring**

Meaning: Mode suited to continuous quantities: speed, RPM, temperature, pressure,
fuel level.
Location / note: Operand.

**Movement Source**

Meaning: Source used by the FMC650 to decide whether the vehicle is moving.
Location / note: System → Movement Source.

**Movement Start Delay**

Meaning: Delay before confirming the transition to the moving state.

<!-- PDF p. 34 -->

Location / note: System.

**Movement Stop Delay**

Meaning: Delay before confirming the stop. Avoids repeated toggling in traffic jams
or very short stops.
Location / note: System.

**Moving**

Meaning: Profile applied when the terminal considers the vehicle to be moving.
Location / note: Data Acquisition → Moving.

**NITZ**

Meaning: Network Identity and Time Zone, time provided by the mobile network.
Location / note: Time Synchronization.

**No DOUT Control**

Meaning: The scenario is detected and can be sent to Wialon, but no electrical
output is controlled.
Location / note: Output Control.

**Non Stop Scan**

Meaning: Permanent BLE scan. To be disabled when not necessary in order to avoid
unnecessary activity.
Location / note: Bluetooth 4.0.

**None**

Meaning: Parameter disabled for transmission/event in this context.
Location / note: Priority = None.

**Notification**

Meaning: Rule that triggers an action/alert when a condition is true.
Location / note: Wialon → Notifications.

**NTP**

## N

<!-- PDF p. 35 -->

Meaning: Network Time Protocol, time synchronization via network server.
Location / note: Time Synchronization.

**Odometer**

Meaning: Distance counter. Its source can be GPS or vehicle depending on configuration.
Location / note: System + Trip/Odometer.

**Odometer Source**

Meaning: Source used for mileage: GPS, FMS, LVCAN or K-Line depending on the options.
Location / note: System → Odometer Source settings.

**OEM**

Meaning: Original Equipment Manufacturer. Refers to equipment supplied/integrated by the
manufacturer or for the manufacturer's system.
Location / note: E.g. SINOTRUK/CNHTC OEM DVR.

**Offset**

Meaning: Value added after applying the factor to obtain the physical value.
Location / note: Depends on the SPN or on the proprietary decoding.

**On Change**

Meaning: Mode suited to states that change: brake ON/OFF, cruise control, clutch, PTO,
ignition.
Location / note: Operand.

**On Stop**

Meaning: Profile applied when the vehicle is stopped.
Location / note: Data Acquisition → On Stop.

**Online Deep Sleep**

Meaning: Sleep mode that saves energy while keeping more network availability
than Deep Sleep.
Location / note: System → Sleep Mode.

**Open Link Timeout**

## O

<!-- PDF p. 36 -->

Meaning: Time during which the terminal can keep the server link open/inactive
according to its logic.
Location / note: System.

**Operand**

Meaning: Data processing mode: continuous monitoring, state change or
comparison with thresholds depending on firmware.
Location / note: I/O and FMS IO.

**Output Control**

Meaning: Choice of a DOUT output to activate when a scenario is triggered.
Location / note: Features → Green Driving / Over Speeding / Jamming depending on
the function.

**Over Speeding**

Meaning: Scenario detecting a speed above the configured threshold.
Location / note: Features → Over Speeding.

**Panic**

Meaning: Maximum priority, to be reserved for genuinely critical events and defined
procedures.
Location / note: I/O/Features depending on option.

**Parameter / parameter**

Meaning: Name of the raw data received in a Wialon message.
Location / note: Messages / Sensors.

**Parsing**

Meaning: Structured decoding/reading of a received message in order to extract its fields and
parameters.
Location / note: Wialon server side.

**Payload**

Meaning: Data bytes transported in a CAN request/command.
Location / note: Manual CAN Requests/Commands.

## P

<!-- PDF p. 37 -->

**PGN**

Meaning: Parameter Group Number. Number identifying a group of J1939 parameters
transported together in a message.
Location / note: E.g. PGN 61444 for EEC1 in the RPM example.

**Ping Mode**

Meaning: Keep-alive/ping mechanism. Can be disabled if not necessary.
Location / note: System.

**Axle weight**

Meaning: Load applied to an axle, potentially estimated by suspension/EBS and
exposed via FMS.
Location / note: FMS IO → Axle Weight.

**Weighbridge**

Meaning: Reference scale for weighing the truck and validating the Axle
Weight/Combined Vehicle Weight data.
Location / note: Field validation.

**Port**

Meaning: Logical number of the network service that listens for FMC650 connections.
Location / note: Must match the Wialon listener or another service.

**Port 29000**

Meaning: Port used in the observed TachoSync configuration.
Location / note: TachoSync Settings.

**Post-event / Post-record**

Meaning: Video kept after the trigger.
Location / note: Objective: 30 s after accident.

**POWER**

Meaning: DVR power connector.
Location / note: DVR unit.

**Pre-event / Pre-record**

Meaning: Video kept before an event is triggered thanks to the
buffer/continuous recording.

<!-- PDF p. 38 -->

Location / note: Project objective: 30 s before accident.

**Priority**

Meaning: Priority level associated with the parameter/event.
Location / note: I/O and FMS IO.

**PTO Drive Engagement**

Meaning: Power take-off engagement information.
Location / note: FMS IO → On Change if useful.

**PTO State**

Meaning: Power take-off state.
Location / note: FMS IO → On Change if PTO is actually used, otherwise None.

**PWR**

Meaning: DVR power indicator light.
Location / note: DVR front panel.

**Record**

Meaning: Telematics record created by the FMC650 at a given time.
Location / note: Becomes an AVL Record.

**Relay / relay**

Meaning: Component allowing a load to be isolated or switched from a control
output.
Location / note: Can be used between DOUT and buzzer/DVR Alarm IN depending on
wiring.

**Report / report**

Meaning: Historical processing generating tables, statistics and events over a
period.
Location / note: Wialon → Reports.

**Req ID**

Meaning: CAN identifier of the request.

## R

<!-- PDF p. 39 -->

Location / note: Manual CAN Requests.

**Request Period**

Meaning: Period between automatic CAN requests.
Location / note: Manual CAN Requests.

**Requested Data Length**

Meaning: Expected length of the response data.
Location / note: Manual CAN Requests.

**Requests Supported**

Meaning: Indicates whether requests are supported by the interface.
Location / note: FMS IO → diagnostic.

**Resolution / factor**

Meaning: Coefficient allowing a raw value to be converted into a physical unit.
Location / note: General form: physical value = RAW × factor +
offset.

**Response Timeout**

Meaning: Waiting time for a server response before timeout/retry behavior.
Location / note: System.

**Retarder**

Meaning: Heavy truck auxiliary brake allowing the vehicle to slow down without using only the
service brakes.
Location / note: FMS IO / FMSED if available.

**Retarder Time**

Meaning: Retarder usage time.
Location / note: FMSED.

**Roaming**

Meaning: State in which the SIM uses a network classified as roaming according to the
operator lists/configuration.
Location / note: Data Acquisition → Roaming.

**RS232**

<!-- PDF p. 40 -->

Meaning: Point-to-point serial interface for external devices. The FMC650 has
two.
Location / note: RS232/RS485.

**RS485**

Meaning: Differential serial interface suited to certain probes and devices. The
FMC650 has one.
Location / note: RS232/RS485.

**RTR**

Meaning: Remote Transmission Request, CAN mechanism associated with certain requests. Do
not enable without knowing what the ECU expects.
Location / note: Manual CAN Requests.

**RUN**

Meaning: Indicator light showing DVR operation.
Location / note: DVR front panel.

**Run On Startup**

Meaning: Option that would launch a command at startup. It must remain disabled unless
the procedure is fully validated.
Location / note: Manual CAN Commands.

**S1 – FMC650 Datasheet**

Meaning: Hardware specifications: interfaces, CAN J1939, J1708, K-Line, I/O, BLE, memory,
GNSS, Crash/Towing/Green Driving functions, fuel and peripherals.
Location / note: Internal project reference.

**S2 – FMC650 Quick Manual / guide manual**

Meaning: Wiring, power supply, connection to the Configurator and commissioning.
Location / note: Internal project reference.

**S3 – Teltonika_FMC650 – AVL Protocols**

Meaning: Chain GNSS/CAN → value → AVL ID → Codec → TCP/UDP → server; IMEI, ACK,
CRC, Wialon reception and processing.

## S

<!-- PDF p. 41 -->

Location / note: Internal project reference.

**S4 – Project FMC650 configuration reports**

Meaning: Observed values, tab roles, FMS IO, Manual CAN, Tachograph,
RS232/RS485, validation recommendations.
Location / note: Internal project reference.

**S5 – Flatbed truck sensor report**

Meaning: Selection of parameters useful for goods transport, field validation
and Wialon mappings.
Location / note: Internal project reference.

**S6 – Project conversation**

Meaning: Terms, configuration choices, camera/DVR explanations, FMS, J1939, Data
Acquisition and Wialon requested and clarified with the user.
Location / note: Internal project reference.

**SAE J1939**

Meaning: Family of SAE standards used mainly on heavy vehicles. It organizes
CAN communications: 29-bit identifier, parameter groups, variables, units,
factors, diagnostics and transport rules.
Location / note: Standard language of heavy trucks above CAN.

**Save Records To**

Meaning: Destination for temporary storage of records not yet sent.
Location / note: System → Internal Memory or available media.

**Save to device**

Meaning: Writes the modified configuration into the FMC650.
Location / note: After validation.

**Save to file**

Meaning: Saves the configuration to a local file before modification.
Location / note: Safety procedure.
scanfms
Meaning: Diagnostic command mentioned for checking/scanning for the presence of
FMS data according to configuration.
Location / note: Diagnostic tool.

<!-- PDF p. 42 -->

**SD**

Meaning: Memory card used by the DVR to record videos locally in a
loop.
Location / note: SD indicator visible on the DVR.

**Send Period**

Meaning: Period for attempting to send records to the server. To be distinguished from Min
Period, which concerns the creation of records.
Location / note: Data Acquisition.

**Send Type**

Meaning: Command send mode, for example once only.
Location / note: Manual CAN Commands.

**Sensor / Wialon sensor**

Meaning: Software object transforming a received parameter into a business value with optional
unit, formula and calibration.
Location / note: Unit Properties → Sensors.

**Server #1 / Server #2**

Meaning: Two configurable destinations on certain FMC650 profiles. Their actual role depends
on the installation.
Location / note: GPRS → Server settings.

**Server Domain / IP**

Meaning: DNS or IP address of the destination server.
Location / note: GPRS → Server settings.

**Telematics server**

Meaning: Server that listens for tracker connections, verifies the unit identifier,
decodes messages and stores the history.
Location / note: In the project: Wialon Local.

**Service Distance**

Meaning: Remaining distance/counter linked to the next service when provided.
Location / note: FMS IO → Low + Monitoring.

**Silent (RS232/RS485)**

<!-- PDF p. 43 -->

Meaning: Mode in which the port remains without a specific active business protocol.
Location / note: Recommended when nothing is connected.

**Silent mode**

Meaning: Passive CAN listening mode: the terminal listens to the bus without behaving
as an active command ECU.
Location / note: CAN2 Bus Mode, and recommended use for reading.

**SIM1 / SIM2**

Meaning: SIM cards that the FMC650 can use depending on the Dual-SIM/eSIM configuration.
Location / note: Security/GPRS/GSM Operators depending on version.

**SINOTRUK / CNHTC**

Meaning: Manufacturer of the truck and of the video system visible in the photos of the
conversation.
Location / note: Truck and camera/DVR system of the project.

**Sleep**

Meaning: Profile applied in certain sleep states.
Location / note: Data Acquisition depending on firmware.

**Sleep Timeout**

Meaning: Delay before entering sleep when the conditions are met.
Location / note: System.

**Sort By Newest**

Meaning: During a recovery after network loss, prioritizes recent records according to
the configured logic.
Location / note: System → Sort By.

**SOS**

Meaning: Emergency button/input that can be connected to a DIN and generate an alert.
Location / note: I/O / Custom Scenarios.

**Speed Source**

Meaning: Source used as reference speed: GPS, FMS, LVCAN or K-Line.
Location / note: System → Speed Source settings.

**SPN**

<!-- PDF p. 44 -->

Meaning: Suspect Parameter Number. Identifier of a specific variable within a PGN.
Location / note: E.g. SPN 190 = Engine Speed.

**Start Delay**

Meaning: Delay after ignition before the start of the TachoSync procedure according to
configuration.
Location / note: TachoSync Settings.

**Start Speed**

Meaning: Minimum speed used to start a trip according to configuration.
Location / note: Trip/Odometer.

**Static Navigation**

Meaning: Filters small GNSS movements when the vehicle is actually stationary
in order to reduce GPS drift.
Location / note: System.

**Static Navigation Deactivation Source**

Meaning: Condition allowing the static navigation mode to be exited, for example
Movement OR Ignition.
Location / note: System.

**Status**

Meaning: Section of the Configurator displaying live information from the terminal.
Location / note: Status → GNSS Info, GSM Info, I/O Info, FMS I/O,
Tachograph, Maintenance.

**SW-Version Supported**

Meaning: Information on the supported FMS version/capability.
Location / note: FMS IO → useful mainly for diagnostics, often None in
production.

**System Event**

Meaning: Generic FMS system event. Its concrete meaning must be identified
before use.
Location / note: FMS IO → None initially.

<!-- PDF p. 45 -->

tachocheck
Meaning: Teltonika diagnostic command used to check tachograph communication
and certain parameters such as the bit rate.
Location / note: Diagnostic tool, not a business parameter.

**Tachograph / tachograph**

Meaning: Regulatory equipment recording in particular speed, distance and driver
activities according to the vehicle/regulation.
Location / note: CAN/Tachograph, Tachograph Data, Status → Tachograph.

**Tachograph Ignition Source**

Meaning: Ignition source used by the tachograph logic.
Location / note: CAN/Tachograph.

**Tachograph Performance**

Meaning: Status/performance associated with the tachograph according to the FMS parameter.
Location / note: FMS IO → Low + On Change if used.

**TachoSync**

Meaning: Tachograph synchronization and remote download service/function.
Location / note: CAN/Tachograph → TachoSync Settings.

**TachoSync Domain**

Meaning: Domain name of the service configured for TachoSync.
Location / note: E.g. domain displayed in the project configuration.

**TachoSync Status**

Meaning: Enables/disables the use of the TachoSync service.
Location / note: TachoSync Settings.

**Target CAN**

Meaning: CAN1 or CAN2 interface on which a command/request would be sent.
Location / note: Manual CAN Commands.

**TCP**

## T

<!-- PDF p. 46 -->

Meaning: Connection-oriented transport protocol with acknowledgments at the transport level.
Location / note: GPRS → Server Protocol if the listener is TCP.

**TCP ASCII/Binary**

Meaning: Modes that can transport serial data to a server according to the supported
functions.
Location / note: RS232/RS485, not equivalent to a universal video
protocol.

**Tell Tale ID0..ID4**

Meaning: Groups of dashboard states/warning lights. Their decoding must be known before
using them.
Location / note: FMS IO → None initially; On Change after validation.

**Telematics terminal / tracker**

Meaning: Embedded equipment that collects, time-stamps, filters, temporarily stores and
transmits vehicle data to a remote platform.
Location / note: The FMC650 is the terminal used in the project.

**Termination / 120-ohm resistor**

Meaning: Termination resistor at the ends of a CAN bus. A network that is already
correctly terminated must not receive a third unnecessary termination.
Location / note: CAN/Tachograph → Termination Resistance.

**Threshold**

Meaning: Acceleration/impact threshold used by an algorithm such as Towing or Crash.
Location / note: Accelerometer Features.

**Time Synchronization**

Meaning: Methods allowing the terminal to maintain a correct time.
Location / note: System.

**Tire Location**

Meaning: Identifies the wheel/tire to which a TPMS data item relates.
Location / note: FMS IO → diagnostic/configuration.

**Tire Pressure**

Meaning: Tire pressure in kPa when the TPMS/FMS system provides it.

<!-- PDF p. 47 -->

Location / note: FMS IO → Low + Monitoring; Wialon alert according to
tire specification.

**Total Vehicle Distance**

Meaning: Cumulative distance provided by the vehicle/FMS when it exists.
Location / note: FMS IO / Wialon reports.

**Towing Detection**

Meaning: Detection of abnormal movement when the vehicle is parked/ignition OFF
after an activation delay.
Location / note: Accelerometer Features → Towing Detection.

**TPMS**

Meaning: Tire Pressure Monitoring System. Tire pressure monitoring system.
Location / note: FMS or compatible external device.

**Trace Changes**

Meaning: Crash Trace mode that mainly keeps significant changes rather than
all samples.
Location / note: Crash Trace.

**Trace Full**

Meaning: Crash Trace mode recording a more complete and therefore larger
trace.
Location / note: Crash Trace.

**Tracking**

Meaning: Tracking of the vehicle's position and movement over time.
Location / note: Monitoring / tracks.

**Transmission Oil Temperature**

Meaning: Gearbox/transmission oil temperature.
Location / note: FMS IO → Low + Monitoring.

**Trip**

Meaning: Logical trip between a start and an end determined by
ignition/movement/speed according to configuration.
Location / note: Trip / Odometer.

<!-- PDF p. 48 -->

**Trip End trigger**

Meaning: Trigger of an aggregated report/record at the end of the trip.
Location / note: FMSED.

**Trip Mode Continuous**

Meaning: Mode in which distance/activity is tracked continuously during the trip.
Location / note: Trip Settings.

**UDP**

Meaning: Transport protocol without a persistent connection, lighter but with different
reliability characteristics.
Location / note: Server option if the listener supports it.

**Unique ID**

Meaning: Terminal identifier used to associate messages with the unit, generally
the FMC650 IMEI.
Location / note: Unit Properties → General.

**Unit / unit**

Meaning: Wialon object representing a vehicle/tracker.
Location / note: Wialon Local → Units.

**Units**

Meaning: Physical unit associated with the parameter: km/h, %, liters, RPM, kg, °C, kPa, etc.
Location / note: FMS IO.

**Unknown**

Meaning: State in which the network used is classified neither as Home nor as known
Roaming.
Location / note: Data Acquisition → Unknown.

**USB Mini-USB**

Meaning: FMC650 port used in particular for local power supply/configuration.
Location / note: FMC650 hardware.

## U

<!-- PDF p. 49 -->

**Raw value / RAW**

Meaning: Numeric value as encoded in the bytes before application of the
factor and offset.
Location / note: The FMC650 then decodes the physical value.

**Field validation**

Meaning: Real-world test allowing the telematics data to be compared with a reference:
dashboard, pressure gauge, weighbridge, full tank, etc.
Location / note: Before production.

**Video Server**

Meaning: Server intended to receive, process and store video files.
Location / note: Separate from the AVL server if the architecture requires it.

**Video Server URL**

Meaning: Address of the video service configured in Wialon Local when a compatible video
integration is used.
Location / note: Administration System → System → Settings.

**View Video**

Meaning: Wialon right allowing videos to be viewed/downloaded when a compatible
integration exists.
Location / note: Access rights.

**VIN**

Meaning: Vehicle Identification Number, vehicle identification number.
Location / note: FMS IO / Tachograph depending on source.

**VRN**

Meaning: Vehicle Registration Number, vehicle registration number.
Location / note: Tachograph Data depending on availability.

## V

## W

<!-- PDF p. 50 -->

**Water In Fuel**

Meaning: Indication of the presence of water in the fuel when available.
Location / note: FMS IO → High + On Change if reliable.

**Wheel Based Speed**

Meaning: Vehicle speed calculated from the wheels/EBS.
Location / note: FMS IO → Low + Monitoring.

**Wialon Local**

Meaning: Fleet management platform installed on a local server. It receives the FMC650
packets, decodes them, stores them and uses them in maps, sensors, alerts and
reports.
Location / note: Target server / platform of the project.
Revision #1
Created 2026-09-02 07:58:04 UTC by Guellaz hadil
Updated 2026-09-02 09:49:21 UTC by Guellaz hadil
