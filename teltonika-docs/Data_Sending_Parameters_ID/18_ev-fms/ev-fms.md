---
title: "FMC650 Data Sending Parameters ID — EV FMS"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "EV FMS"
---

# EV FMS

| Property ID in AVL packet | Property Name | Bytes | Type | Min | Max | Multiplier | Units | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10879 | High voltage battery voltage | 4 | Unsigned | 0 | 4294967295 | 50 | mV | High voltage battery voltage |
| 10880 | High voltage battery current | 4 | Signed | -1600000 | 1612750 | 50 | mA | High voltage battery current |
| 10881 | Internal Charger Status | 1 | Unsigned | - | - | - | - | Internal Charger Status |
| 10882 | Generic state of charge | 1 | Unsigned | - | - | - | - | Generic state of charge |
| 10883 | Ignition | 1 | Unsigned | - | - | - | - | Ignition |
| 10884 | External Energy Source Connection Status | 1 | Unsigned | - | - | - | - | External Energy Source Connection Status |
| 10885 | Seatbelt switch | 1 | Unsigned | - | - | - | - | Seatbelt switch |
| 10886 | EVSE1 AC RMS Current | 4 | Signed | -1600000 | 1612750 | 50 | mA | EVSE1 AC RMS Current |
| 10887 | EVSE1 AC RMS Voltage | 4 | Unsigned | 0 | 4294967295 | 50 | mV | EVSE1 AC RMS Voltage |
| 10888 | DC Charging State | 1 | Unsigned | - | - | - | - | DC Charging State |
| 10889 | High Voltage Battery Highest Cell Temperature | 2 | Signed | -273 | 1735 | 0,03125 | °C | High Voltage Battery Highest Cell Temperature |
| 10890 | High Voltage Battery Lowest Cell Temperature | 2 | Signed | -273 | 1735 | 0,03125 | °C | High Voltage Battery Lowest Cell Temperature |
| 10891 | Propulsion Motor Coolant Fan 1 Control Temperature | 2 | Signed | -273 | 1735 | 0,03125 | °C | Propulsion Motor Coolant Fan 1 Control Temperature |
| 10892 | Air Conditioner Compressor Status | 1 | Unsigned | - | - | - | - | Air Conditioner Compressor Status |
| 10893 | High Voltage Battery Temperature | 1 | Signed | -40 | 210 | - | °C | High Voltage Battery Temperature |
| 10894 | HVESS Thermal Management System Heater Status | 1 | Unsigned | - | - | - | - | HVESS Thermal Management System Heater Status |
| 10895 | Fuel Supply Estimated Remaining Distance | 2 | Unsigned | 0 | 64255 | - | km | Fuel Supply Estimated Remaining Distance |
| 10896 | Trailer Weight | 2 | Unsigned | 0 | 128510 | 2 | kg | Trailer Weight |
| 10897 | Cargo Weight | 2 | Unsigned | 0 | 128510 | 2 | kg | Cargo Weight |
| 10898 | Powered Vehicle Weight | 2 | Unsigned | 0 | 642550 | 10 | kg | Powered Vehicle Weight |
| 10899 | Gross Combination Vehicle Weight | 2 | Unsigned | 0 | 642550 | 10 | kg | Gross Combination Vehicle Weight |
| 10901 | Highest cell voltage | 2 | Unsigned | 0 | 64255 | 1 | mV | Highest cell voltage |
| 10902 | Lowest cell voltage | 2 | Unsigned | 0 | 64255 | 1 | mV | Lowest cell voltage |
| 10903 | HVESS Nominal Rated Capacity | 4 | Unsigned | 0 | 100 | - | % | HVESS Nominal Rated Capacity |
| 10904 | HVESS State of Health | 1 | Unsigned | 0 | 100 | 0,4 | % | HVESS State of Health |
