---
title: FMC650 SMS/GPRS command list
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_SMS/GPRS_command_list
archived-snapshot: https://web.archive.org/web/20240715174822/https://wiki.teltonika-gps.com/view/FMC650_SMS/GPRS_command_list
captured: 2026-11-04
---

# FMC650 SMS/GPRS command list

All commands are case sensitive. When user tries to send SMS/GPRS message to FMC650 that operates in Deep Sleep mode, it cannot arrive to FMC650 device because the GSM/GPRS module is disabled most of the time. FMC650 will receive the SMS/GPRS message when it exits Deep Sleep mode.If FMC650 is in GPS Sleep or Online Deep Sleep mode, sent SMS/GPRS message will arrive to the device.

SMS command structure:

```
<SMS login><space><SMS password><space><command><space><value>
```

SMS command [getinfo](https://wiki.teltonika-gps.com/view/FMB_getinfo) example:

- If you have set SMS login and password: `login pass getinfo`
- If SMS login and password are not set leave two spaces before command: `getinfo`

# Common commands

| Command | Description | Response |
| --- | --- | --- |
| getstatus | Modem Status information | Yes |
| getrecord | SMS command initiates saving and sending of high priority record | No |
| getcfgtime | Date and Time of last successful configuration | Yes |
| getgps | Current GPS data and time | Yes |
| getnmeainfo | NMEA error debug SMS | Yes |
| cpureset | Reset CPU | No |
| defaultcfg | Reset configuration to default | Yes |
| getver | Device / Modem / Code version information | Yes |
| getinfo | Device runtime system information | Yes |
| tacho_connect | Connect to Web Tacho immediately | Yes |
| web_connect | Connect to Fota WEB immediately | Yes |
| deleterecords | Delete all records saved on FLASH | Yes |
| getio | Readout digital inputs and outputs, analog inputs | Yes |
| banlist | Banlist information | Yes |
| crashlog | Crash log information | Yes |
| delete_all_sms | Delete all read SMS | Yes |
| braminfo | BatRam info | Yes |
| getgnss | Current GNSS information | Yes |
| resetlimits | Resets data counters | Yes |
| getlimits | Gets home/roaming uploaded data information | Yes |
| scanfms | Shows FMS elements that can be read from vehicle | Yes |
| readio # | Returns IO status, # AVL ID | Yes |
| setdigout XXXX Y1 Y2 Y3 Y4 | Set digital output / 1. # – 0; 1 or ? (0 - OFF, 1 – ON or ? – Ignore) for DOUT1 / 2. # – 0; 1 or ? (0 - OFF, 1 – ON or ? – Ignore) for DOUT2 / 3. # – 0; 1 or ? (0 - OFF, 1 – ON or ? – Ignore) for DOUT3 / 4. # – 0; 1 or ? (0 - OFF, 1 – ON or ? – Ignore) for DOUT4 / Y1 – timeout value for DOUT1 if needed (in seconds) / Y2 – timeout value for DOUT2 if needed (in seconds) / Y3 – timeout value for DOUT3 if needed (in seconds) / Y4 – timeout value for DOUT4 if needed (in seconds) | Yes |
| getparam # | Readout parameter value according entered ID. / # - ID value | Yes |
| setparam #:# | Sets selected parameter value / 1.# - first ID value / 2.# - New first Parameter Value / 3.# - second ID value / 4.# - New second Parameter Value / 5.# - third ID value / 6.# - New third Parameter Value / SMS command is limited to 160 characters | Yes |
| setparam #:#;#:#;… | Sets selected parameter value / 1.# - first ID value / 2.# - New first Parameter Value / 3.# - second ID value / 4.# - New second Parameter Value / 5.# - third ID value / 6.# - New third Parameter Value / SMS command is limited to 160 characters | Yes |
| flush #,#,#,#,#,#,# | Redirects device to other server / 1.# - IMEI / 2.# - APN / 3.# - LOGIN / 4.# - PASS / 5.# - IP / 6.# - PORT / 7.# - MODE (0-TCP/1-UDP) | Yes |

# Commands related to features

| Command | Description | Response |
| --- | --- | --- |
| odoset:# | Set total odometer value / # - new odometer value in m | Yes |
| odoget | Display current odometer value | Yes |
| odinfo | Odometer Debug info | Yes |
| on_demand_trackingX | X=0 – Stops Tracking on Demand functionality. / X=1 – Starts Tracking on Demand functionality. / X=2 – Generates one high priority record and inititates data sending to server. / | Yes |

# Commands related to LV-CAN200/ALL-CAN300

| Command | Description | Response |
| --- | --- | --- |
| lvcansetprog # | Set program number to LV-CAN200/ ALL-CAN300 that is connected to FMx640. / # - three digit number that identity vehicle | Yes |
| lvcansimpletacho # | Add or remove simpletacho start byte. / # - 0 or 1 (0 – don’t add start byte, 1 – add start byte) | No |
| lvcangetprog | Get program number from LV-CAN200/ ALL-CAN300 that is connected to FMx640 | Yes |
| lvcangetinfo | Get information about connected LV-CAN200/ALL-CAN300 | Yes |
| lvcanclear # | Clear Total Mileage (counted), Engine Work Time (counted), Fuel Consumed (counted) parameters values. / # - parameter (0 – Engine work time (counted), 1 – Fuel Consumed (counted), 2 – Vehicle Mileage (counted)) | Yes |
