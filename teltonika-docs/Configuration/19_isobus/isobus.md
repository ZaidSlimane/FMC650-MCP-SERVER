---
title: FMC650 ISOBUS
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_ISOBUS
archived-snapshot: https://web.archive.org/web/20260518024724/https://wiki.teltonika-gps.com/view/FMC650_ISOBUS
captured: 2026-11-04
---

# FMC650 ISOBUS

# Description

ISOBUS (ISO 11783) is a standardized communication protocol used in agriculture to enable
seamless data exchange between tractors, implements, and other farm equipment from
different manufacturers. It simplifies the control and monitoring of equipment, allowing
operators to manage everything from a single control panel inside the tractors‘ cabin.
Essentially, ISOBUS ensures that all machines "speak the same language," reducing
compatibility issues and improving the efficiency of agricultural operations.

**NOTE:** ISOBUS data reading is available using the: **FMM650, FMC650** with the base firmware version of **03.01.XX**.

ISOBUS communication systems are used in:

• **Tractors and Combines**: Central systems where ISOBUS-compatible control terminals
are installed.

• **Implements**: Attachments like plows, seed drills, balers, sprayers, and more, which
exchange data with the tractor through the ISOBUS interface.

ISOBUS topology for FMx650 devicesIn agriculture, ISOBUS plays a role similar to **OBD-II** (On-Board Diagnostics) in cars and **FMS**
(Fleet Management Systems) in trucks. Just like OBD-II allows mechanics to access
standardised vehicle data to diagnose issues, and FMS allows accessing standardised data to
monitor and optimize truck operations, ISOBUS provides a standardized communication
platform for tractors and implements. It enables different machines, regardless of
manufacturer, to "speak the same language" and exchange vital operational data.

Our new hardware solution connects directly to the ISOBUS connector and reads CAN data
from the tractor and implement systems, helping farmers improve efficiency, monitor
equipment performance, and optimize their fieldwork

# ISOBUS connection

ISOBUS 9 pin connectionThe communication occurs via a Plug'n'Play cable which connects to the tractor's ISOBUS interface using a 9-pin adapter which looks like this:

This cable connects straight into the agricultural vehicle's interface, which has an in-built ISOBUS connector.

9 pin cable connection with the FMC650The connection from our device to the ISOBUS cable is visualized in this wiring diagram:

ISOBUS parameters travel via CAN lines, when connected to the 9 pin adapter.

**Note:** CAN1 and CAN2 can be connected to pins D and C interchangeably as the parameter is configurable.

# ISOBUS data

ISOBUS transfers essential **CAN data** between the tractor and the implement. Our hardware
solution is designed to capture key operational data through this connection. Below are the
types of data that can be gathered via ISOBUS:

**PTO (Power Take-Off) Data**:

***PTO Status***: Whether the PTO is engaged or disengaged.

***PTO Speed***: The rotational speed at which the PTO shaft is transferring power from the
tractor to the implement.

**Hitch Position Data**:

***Hitch Height***: The vertical position of the implement attached to the tractor’s hitch.

**Auxiliary Valve Data**:

***Hydraulic Flow and Pressure***: Information on the flow rate and pressure in auxiliary hydraulic circuits used to control attachments.

**FMS Data:**

Additionally, a few FMS parameters can be read using an ISOBUS connection. These include, but are not limited to:

• Fuel Rate

• Fuel Level

• Service Distance

• Engine Hours

A full list of FMS I/O IDs and their descriptions can be found **[here](https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID#FMS_elements)**.

# ISOBUS configuration

CAN \ Tachograph settingsAs shown in the connection diagram to the 9 pin Plug'n'Play, ISOBUS data is transferred via the CAN1 line, which is set as the source for FMS data in the default configuration in the **CAN \ Tachograph** tab:

If the user has selected CAN2 as the FMS source when using the 9 pin adapter, the aforementioned FMS data will **not** be received.

On Demand Tracking triggersISOBUS offers extra data acquisition triggers, which can be configured in the *"Data Acquisition"* tab in the Teltonika Configurator:

Like other On Demand Tracking triggers, the corresponding IO events must be configured to Low/High/Panic priorities. If IO operand is "Monitoring", On Demand Tracking will **NOT** be triggered.

**Multiple sources of On Demand Tracking can be selected**

**Valve Fail Safe Mode:** triggered, when the parameter reaches the configured value(-s).

**Valve State:** triggered, when the parameter reaches the configured state, indicating that an error has been detected or valve is currently extended/retracted.

**Valve Extend/Retract Port Measured Flow:** triggered, when the configured percentage of full possible flow is detected.

**Valve Extend/Retract Port Pressure:** triggered, when the configured pressure value (in kPa) is reached.

**Valve Return Port Pressure:** triggered, when the nominal pressure (in kPa) at the return port of the auxiliary valve is reached.

**Valve Port Flow:** this is a command, which is used to set the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. Triggered, when the configured percentage value is reached.

**Valve Fail Safe Mode Command:** triggered, when a command is sent to the device with the configured value describing the safe mode of the valve (0-3).

**Valve State Command:** triggered, when a valve state command with the configured value is reached.

**Hitch Status Commands:** triggered, when a configured Primary/Secondary or Front/Rear Hitch status is reached, for example, indicating that it is out-of-work or an error is detected.

**Front/Rear Hitch Position Command:** triggered, when a configured value (in %) is detected as the value of the Hitch Position command.

ISOBUS tab settings**ISOBUS periodic record timeout** - time in seconds, that it takes the device to generate a record, containing the values of selected ISOBUS parameters.

**Include ISOBUS data into regular record**:

***Disable*** - Disables the sending of ISOBUS parameters in regular data packets.

***Enable*** - Enables the sending of ISOBUS parameters in regular data packets.

# ISOBUS Data Parameter List

## ISOBUS

---

| Property ID in AVL packet | Property Name | Bytes | Type | **Value range** | Multiplier | Units | Description | HW Support | Parameter Group | — |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 12400 | Groundspeed of a machine | 2 | Unsigned | 0 | 64255 | 0.001 | m/s | Groundspeed of the machine | FMC650, FMM650 | ISOBUS |
| 12401 | Ground based distance | 4 | Unsigned | 0 | 4211081215 | 0.001 | m | Ground based distance | FMC650, FMM650 | ISOBUS |
| 12402 | Ground based direction | 1 | Unsigned | 0 | 3 | - | - | Wheel speed of the machine | FMC650, FMM650 | ISOBUS |
| 12403 | Wheel speed of a machine | 2 | Unsigned | 0 | 64255 | 0.001 | m/s | Wheel speed of the machine | FMC650, FMM650 | ISOBUS |
| 12404 | Wheel based distance | 4 | Unsigned | 0 | 4211081215 | 0.001 | m | Wheel based distance | FMC650, FMM650 | ISOBUS |
| 12405 | Maximum time of tractor power | 1 | Unsigned | 0 | 250 | - | min | Maximum time of tractor power | FMC650, FMM650 | ISOBUS |
| 12406 | Wheel based direction | 1 | Unsigned | 0 | 3 | - | - | Maximum time of tractor power | FMC650, FMM650 | ISOBUS |
| 12407 | Key switch state | 1 | Unsigned | 0 | 3 | - | - | 00 – Key switch Off / 01 – Key switch not Off / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12408 | Start/Stop state | 1 | Unsigned | 0 | 3 | - | - | 00 – Stop or disable implement work / 01 – Start or enable implement work / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12409 | Maintain ECU power | 1 | Unsigned | 0 | 3 | - | - | 00 – No further requirement for ECU_PW / 01 – Requirement for 2 s more of ECU_PWR / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12410 | Maintain actuator power | 1 | Unsigned | 0 | 3 | - | - | 00 – No further requirement for PWR / 01 – Requirement for 2 s more for PWR / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12411 | Implement transport state | 1 | Unsigned | 0 | 3 | - | - | 00 – Implement may not be transported / 01 – Implement may be transported / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12412 | Implement park state | 1 | Unsigned | 0 | 3 | - | - | 00 – Implement may not be disconnected / 01 – Implement may be disconnected / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12413 | Implement work state | 1 | Unsigned | 0 | 3 | - | - | 00 – Implement is not ready for field work / 01 – Implement is ready for field work / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12414 | Front hitch position | 1 | Unsigned | 0 | 100 | - | % | Front hitch position | FMC650, FMM650 | ISOBUS |
| 12415 | Front hitch in-work indication | 1 | Unsigned | 0 | 3 | - | - | 00 – Hitch position is out-of-work / 01 – Hitch position is in-work / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12416 | Front nominal lower link force | 1 | Signed | -100 | 100 | - | % | Front nominal lower link force | FMC650, FMM650 | ISOBUS |
| 12417 | Front draft | 4 | Signed | -320000 | 32250 | - | N | Apparent horizontal force applied to the front hitch by an implement | FMC650, FMM650 | ISOBUS |
| 12418 | Rear hitch position | 1 | Unsigned | 0 | 100 | - | % | Measured position of the rear three-point hitch | FMC650, FMM650 | ISOBUS |
| 12419 | Rear hitch in-work indication | 1 | Unsigned | 0 | 3 | - | - | 00 – Hitch position is out-of-work / 01 – Hitch position is in-work / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12420 | Rear nominal lower link force | 1 | Signed | -100 | 100 | - | % | Rear nominal lower link force | FMC650, FMM650 | ISOBUS |
| 12421 | Rear draft | 4 | Signed | -320000 | 322550 | - | N | Apparent horizontal force applied to the rear hitch by an implement | FMC650, FMM650 | ISOBUS |
| 12422 | Front PTO output shaft speed | 4 | Unsigned | 0 | 8031875 | 0.001 | 1/min | Measured rotational speed of the front power take-off (PTO) output shaft | FMC650, FMM650 | ISOBUS |
| 12423 | Front PTO shaft speed point | 4 | Unsigned | 0 | 8031875 | 0.001 | 1/min | Measured value of the set point of the rotational speed of the front power take-off (PTO) output shaft | FMC650, FMM650 | ISOBUS |
| 12424 | Front PTO engagement | 1 | Unsigned | 0 | 3 | - | - | 00 – PTO disengaged / 01 – PTO engaged / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12425 | Front PTO mode | 1 | Unsigned | 0 | 3 | - | - | 00 – PTO mode is 540 / 01 – PTO mode is 1 000 / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12426 | Front PTO economy mode | 1 | Unsigned | 0 | 3 | - | - | 00 – PTO economy mode is disengaged / 01 – PTO economy mode is engaged / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12427 | Rear PTO output shaft speed | 4 | Unsigned | 0 | 8031875 | 0.001 | 1/min | Measured rotational speed of the rear power take-off (PTO) output shaft | FMC650, FMM650 | ISOBUS |
| 12424 | Rear PTO shaft speed point | 4 | Unsigned | 0 | 8031875 | 0.001 | 1/min | Measured value of the set point of the rotational speed of the rear power take-off (PTO) output shaft | FMC650, FMM650 | ISOBUS |
| 12429 | Rear PTO engagement | 1 | Unsigned | 0 | 3 | - | - | "00 – PTO disengaged / 01 – PTO engaged / 10 – Error indication / 11 – Not available" | FMC650, FMM650 | ISOBUS |
| 12430 | Rear PTO mode | 1 | Unsigned | 0 | 3 | - | - | "00 – PTO mode is 540 / 01 – PTO mode is 1,000 / 10 – Error indication / 11 – Not available" | FMC650, FMM650 | ISOBUS |
| 12431 | Rear PTO economy mode | 1 | Unsigned | 0 | 3 | - | - | "00 – PTO economy mode is disengaged / 01 – PTO economy mode is engaged / 10 – Error indication / 11 – Not available" | FMC650, FMM650 | ISOBUS |
| 12432 | Front hitch position command | 1 | Unsigned | 0 | 100 | - | % | Command for allowing the position of the front three-point hitch to be set | FMC650, FMM650 | ISOBUS |
| 12433 | Rear hitch position command | 1 | Unsigned | 0 | 100 | - | % | Command for allowing the position of the rear three-point hitch to be set | FMC650, FMM650 | ISOBUS |
| 12434 | Front Shaft speed set point command | 4 | Unsigned | 0 | 8031875 | 0.001 | 1/min | Front PTO output shaft speed set point command | FMC650, FMM650 | ISOBUS |
| 12435 | Rear Shaft speed set point command | 4 | Unsigned | 0 | 8031875 | 0.001 | 1/min | Rear PTO output shaft speed set point command | FMC650, FMM650 | ISOBUS |
| 12436 | Front PTO engagement command | 1 | Unsigned | 0 | 3 | - | - | 00 – PTO disengaged / 01 – PTO engaged / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12437 | Rear PTO engagement command | 1 | Unsigned | 0 | 3 | - | - | "00 – PTO disengaged / 01 – PTO engaged / 10 – Reserved / 11 – Don’t care" | FMC650, FMM650 | ISOBUS |
| 12438 | Front PTO mode command | 1 | Unsigned | 0 | 3 | - | - | "00 – Select 540 r/min mode / 01 – Select 1,000 r/min mode / 10 – Reserved / 11 – Don’t care" | FMC650, FMM650 | ISOBUS |
| 12439 | Rear PTO mode command | 1 | Unsigned | 0 | 3 | - | - | "00 – Select 540 rpm mode / 01 – Select 1,000 rpm mode / 10 – Reserved / 11 – Don’t care" | FMC650, FMM650 | ISOBUS |
| 12440 | Front PTO economy mode command | 1 | Unsigned | 0 | 3 | - | - | "00 – Disengage PTO economy mode / 01 – Engage PTO economy mode / 10 – Reserved / 11 – Don’t care" | FMC650, FMM650 | ISOBUS |
| 12441 | Rear PTO economy mode command | 1 | Unsigned | 0 | 3 | - | - | "00 – Disengage PTO economy mode / 01 – Engage PTO economy mode / 10 – Reserved / 11 – Don’t care" | FMC650, FMM650 | ISOBUS |
| 12442 | Auxil ext valve number 0 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12443 | Auxil ext valve number 1 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12444 | Auxil ext valve number 2 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12445 | Auxil ext valve number 3 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12446 | Auxil ext valve number 4 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12447 | Auxil ext valve number 5 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12448 | Auxil ext valve number 6 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12449 | Auxil ext valve number 7 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12450 | Auxil ext valve number 8 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 124451 | Auxil ext valve number 9 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12452 | Auxil ext valve number 10 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12453 | Auxil ext valve number 11 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12454 | Auxil ext valve number 12 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12455 | Auxil ext valve number 13 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12456 | Auxil ext valve number 14 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12457 | Auxil ext valve number 15 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the extend port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12458 | Auxil ret valve number 0 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve. | FMC650, FMM650 | ISOBUS |
| 12459 | Auxil ret valve number 1 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12460 | Auxil ret valve number 2 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12461 | Auxil ret valve number 3 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12462 | Auxil ret valve number 4 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12463 | Auxil ret valve number 5 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12464 | Auxil ret valve number 6 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12465 | Auxil ret valve number 7 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12466 | Auxil ret valve number 8 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12467 | Auxil ret valve number 9 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12468 | Auxil ret valve number 10 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12469 | Auxil ret valve number 11 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12470 | Auxil ret valve number 12 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12471 | Auxil ret valve number 13 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 124672 | Auxil ret valve number 14 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12473 | Auxil ret valve number 15 | 1 | Signed | -125 | 125 | - | % | Value reported by the controller of flow through the retract port of auxiliary valve X of a tractor which could be based on the commanded position of the valve | FMC650, FMM650 | ISOBUS |
| 12474 | 0 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12475 | 1 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12476 | 2 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12477 | 3 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12478 | 4 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12479 | 5 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12480 | 6 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12481 | 7 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12482 | 8 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12483 | 9 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12484 | 10 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12485 | 11 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12486 | 12 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12487 | 13 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12488 | 14 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12489 | 15 valve fail safe state | 1 | Unsigned | 0 | 3 | - | - | 00 – Block / 01 – Float / 10 – Error indication / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12490 | 0 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12491 | 1 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12492 | 2 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12493 | 3 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12494 | 4 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12495 | 5 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12496 | 6 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12497 | 7 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12498 | 8 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12499 | 9 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12500 | 10 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12501 | 11 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12502 | 12 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12503 | 13 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12504 | 14 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12505 | 15 valve state | 1 | Unsigned | 0 | 15 | - | - | 0000 – Blocked / 0001 – Extend / 0010 – Retract / 0011 – Floating / 0100 to 1101 – Reserved / 1110 – Error indication / 1111 – Not available | FMC650, FMM650 | ISOBUS |
| 12506 | Extend Port Measured Flow 0 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12507 | Extend Port Measured Flow 1 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12508 | Extend Port Measured Flow 2 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12509 | Extend Port Measured Flow 3 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12510 | Extend Port Measured Flow 4 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12511 | Extend Port Measured Flow 5 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12512 | Extend Port Measured Flow 6 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12513 | Extend Port Measured Flow 7 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12514 | Extend Port Measured Flow 8 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12515 | Extend Port Measured Flow 9 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12516 | Extend Port Measured Flow 10 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12517 | Extend Port Measured Flow 11 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12518 | Extend Port Measured Flow 12 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12519 | Extend Port Measured Flow 13 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12520 | Extend Port Measured Flow 14 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12521 | Retract Port Measured Flow 15 | 1 | Signed | -125 | 125 | - | % | Measured flow through the extend port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12522 | Retract Port Measured Flow 0 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12523 | Retract Port Measured Flow 1 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12524 | Retract Port Measured Flow 2 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12525 | Retract Port Measured Flow 3 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12526 | Retract Port Measured Flow 4 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12527 | Retract Port Measured Flow 5 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12528 | Retract Port Measured Flow 6 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12529 | Retract Port Measured Flow 7 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12530 | Retract Port Measured Flow 8 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12531 | Retract Port Measured Flow 9 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12532 | Retract Port Measured Flow 10 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12533 | Retract Port Measured Flow 11 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12534 | Retract Port Measured Flow 12 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12535 | Retract Port Measured Flow 13 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12536 | Retract Port Measured Flow 14 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12537 | Retract Port Measured Flow 15 | 1 | Signed | -125 | 125 | - | % | Measured flow through the retract port of auxiliary valve number X of a tractor, expressed as a percentage of full possible flow | FMC650, FMM650 | ISOBUS |
| 12538 | Extend Port Pressure 0 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12539 | Extend Port Pressure 1 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12540 | Extend Port Pressure 2 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12541 | Extend Port Pressure 3 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12542 | Extend Port Pressure 4 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12543 | Extend Port Pressure 5 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12544 | Extend Port Pressure 6 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12545 | Extend Port Pressure 7 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12546 | Extend Port Pressure 8 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12547 | Extend Port Pressure 9 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12548 | Extend Port Pressure 10 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12549 | Extend Port Pressure 11 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12550 | Extend Port Pressure 12 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12551 | Extend Port Pressure 13 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12552 | Extend Port Pressure 14 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12553 | Extend Port Pressure 15 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the extend port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12554 | Retract Port Pressure 0 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12555 | Retract Port Pressure 1 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12556 | Retract Port Pressure 2 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12557 | Retract Port Pressure 3 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12558 | Retract Port Pressure 4 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12559 | Retract Port Pressure 5 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12560 | Retract Port Pressure 6 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12561 | Retract Port Pressure 7 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12562 | Retract Port Pressure 8 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12563 | Retract Port Pressure 9 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12564 | Retract Port Pressure 10 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12565 | Retract Port Pressure 11 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12566 | Retract Port Pressure 12 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12567 | Retract Port Pressure 13 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12568 | Retract Port Pressure 14 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12569 | Retract Port Pressure 15 | 4 | Unsigned | 0 | 321275 | - | kPa | Measured nominal pressure at the retract port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12570 | Return Port Pressure 0 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12571 | Return Port Pressure 1 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12572 | Return Port Pressure 2 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12573 | Return Port Pressure 3 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12574 | Return Port Pressure 4 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12575 | Return Port Pressure 5 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12576 | Return Port Pressure 6 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12577 | Return Port Pressure 7 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12578 | Return Port Pressure 8 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12579 | Return Port Pressure 9 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12580 | Return Port Pressure 10 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12581 | Return Port Pressure 11 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12582 | Return Port Pressure 12 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12583 | Return Port Pressure 13 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12584 | Return Port Pressure 14 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12585 | Return Port Pressure 15 | 2 | Unsigned | 0 | 4000 | - | kPa | Measured nominal pressure at the return port of auxiliary valve number X of a tractor, | FMC650, FMM650 | ISOBUS |
| 12586 | valve port flow 0 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12587 | valve port flow 1 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12588 | valve port flow 2 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12589 | valve port flow 3 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12590 | valve port flow 4 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12591 | valve port flow 5 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12592 | valve port flow 6 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12593 | valve port flow 7 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12594 | valve port flow 8 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12595 | valve port flow 9 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12596 | valve port flow 10 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12597 | valve port flow 11 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12598 | valve port flow 12 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12599 | valve port flow 13 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12600 | valve port flow 14 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12601 | valve port flow 15 | 1 | Unsigned | 0 | 100 | - | % | Command for setting the flow through the extend or retract port of auxiliary valve X of a tractor, expressed as a percentage of full possible flow. | FMC650, FMM650 | ISOBUS |
| 12602 | valve safe mode command 0 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12603 | valve safe mode command 1 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12604 | valve safe mode command 2 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12605 | valve safe mode command 3 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12606 | valve safe mode command 4 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12607 | valve safe mode command 5 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12608 | valve safe mode command 6 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12609 | valve safe mode command 7 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12610 | valve safe mode command 8 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12611 | valve safe mode command 9 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12612 | valve safe mode command 10 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12613 | valve safe mode command 11 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12614 | valve safe mode command 12 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12615 | valve safe mode command 13 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12616 | valve safe mode command 14 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12617 | valve safe mode command 15 | 1 | Unsigned | 0 | 3 | - | - | 00 — Block / 01 — Float / 10 — Reserved / 11 — Don't care | FMC650, FMM650 | ISOBUS |
| 12618 | valve state command 0 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12619 | valve state command 1 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12620 | valve state command 2 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12621 | valve state command 3 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12622 | valve state command 4 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12623 | valve state command 5 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12624 | valve state command 6 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12625 | valve state command 7 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12626 | valve state command 8 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12627 | valve state command 9 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12628 | valve state command 10 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12629 | valve state command 11 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12630 | valve state command 12 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12631 | valve state command 13 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12632 | valve state command 14 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12633 | valve state command 15 | 1 | Unsigned | 0 | 15 | - | - | 0000 — Block / 0001 — Extend / 0010 — Retract / 0011 — Float / 0100 to 1110 — Reserved / 1111 — Don't Care | FMC650, FMM650 | ISOBUS |
| 12634 | Tractor high-beam head lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12635 | Tractor low-beam head lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12636 | Tractor alternate head lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12637 | Daytime running lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12638 | Left-turn signal lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12639 | Right-turn signal lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12640 | Beacon lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12641 | Front fog lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12642 | Left stop lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12643 | Right stop lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12644 | Centre stop lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12645 | Back up light and alarm horn | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12646 | Tractor marker lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12647 | Implement marker lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12648 | Tractor clearance lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12649 | Implement clearance lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12650 | Rear high mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12651 | Rear low mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12652 | Underside work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12653 | Rear fog lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12654 | Front high-mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12655 | Front low-mounted work light | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12656 | Side high-mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12657 | Side low mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12658 | Implement left forward work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12659 | Implement right forward work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12660 | Implement OEM option 1 light | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12661 | Implement OEM option 2 light | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12662 | Implement rear work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12663 | Implement left work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12664 | Implement right work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12665 | Lighting data message request | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivate / 01 – Activate / 10 – Reserved / 11 – Don’t care | FMC650, FMM650 | ISOBUS |
| 12666 | Tractor high-beam head lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12667 | Tractor low-beam head lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12668 | Tractor alternate head lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12669 | Daytime running lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12670 | Left-turn signal lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12671 | Right-turn signal lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12672 | Beacon lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12673 | Front fog lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12674 | Left stop lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12675 | Right stop lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12676 | Centre stop lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12677 | Back up light and alarm horn | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12678 | Tractor marker lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12679 | Implement marker lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12680 | Tractor clearance lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12681 | Implement clearance lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12682 | Rear high mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12683 | Rear low mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12684 | Underside work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12685 | Rear fog lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12686 | Front high-mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12687 | Front low-mounted work light | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12688 | Side high-mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12689 | Side low mounted work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12690 | Implement left forward work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12691 | Implement right forward work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12692 | Implement OEM option 1 light | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12693 | Implement OEM option 2 light | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12694 | Implement rear work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12695 | Implement left work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12696 | Implement right work lights | 1 | Unsigned | 0 | 3 | - | - | 00 – Deactivated / 01 – Activated / 10 – Fault detected / 11 – Not available | FMC650, FMM650 | ISOBUS |
| 12697 | Background illumination level | 1 | Unsigned | 0 | 100 | - | % | Background illumination level - command | FMC650, FMM650 | ISOBUS |

> **Note:** all six figures on this page (ISOBUS topology, ISOBUS cable, pin wiring scheme, FMS data illustration, GIF, records screenshot) are served by the archived snapshot from unprefixed `web.archive.org/images/...` paths; the Wayback Machine has **no capture** of these files (CDX-verified), so they could not be preserved. The textual content above is complete.
