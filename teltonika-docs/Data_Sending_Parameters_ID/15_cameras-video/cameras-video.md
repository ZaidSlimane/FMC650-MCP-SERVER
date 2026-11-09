---
title: "FMC650 Data Sending Parameters ID — Cameras/Video"
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
archived-snapshot: https://web.archive.org/web/20260416140930/https://wiki.teltonika-gps.com/view/FMC650_Teltonika_Data_Sending_Parameters_ID
captured: 2026-11-04
section: "Cameras/Video"
---

# Cameras/Video

| Property ID in AVL packet | Property Name | Bytes | Type | Value range | | Multiplier | Units | Description | HW Support | Parameter Group |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Property ID in AVL packet** | **Property Name** | **Bytes** | **Type** | **Min** | **Max** | **Multiplier** | **Units** | **Description** | **HW Support** | **Parameter Group** |
| 12301 | iCam DualCam1 Front State | 1 | Unsigned | 0 | 4 | - | - | 0 – Camera not detected / 1 – No card / 2 – Card mount failed / 3 – Card mounted / 4 – Card faulty | FMC650, FMM650 | Cameras/Video |
| 12302 | iCam DualCam1 Rear State | 1 | Unsigned | 0 | 4 | - | - | 0 – Camera not detected / 1 – No card / 2 – Card mount failed / 3 – Card mounted / 4 – Card faulty | FMC650, FMM650 | Cameras/Video |
| 12303 | iCam DashCam1 State | 1 | Unsigned | 0 | 4 | - | - | 0 – Camera not detected / 1 – No card / 2 – Card mount failed / 3 – Card mounted / 4 – Card faulty | FMC650, FMM650 | Cameras/Video |
| 12304 | iCam DualCam2 Front State | 1 | Unsigned | 0 | 4 | - | - | 0 – Camera not detected / 1 – No card / 2 – Card mount failed / 3 – Card mounted / 4 – Card faulty | FMC650, FMM650 | Cameras/Video |
| 12305 | iCam DualCam2 Rear State | 1 | Unsigned | 0 | 4 | - | - | 0 – Camera not detected / 1 – No card / 2 – Card mount failed / 3 – Card mounted / 4 – Card faulty | FMC650, FMM650 | Cameras/Video |
| 12306 | iCam DashCam2 State | 1 | Unsigned | 0 | 4 | - | - | 0 – Camera not detected / 1 – No card / 2 – Card mount failed / 3 – Card mounted / 4 – Card faulty | FMC650, FMM650 | Cameras/Video / |
| COM1 - 11700 COM2 - 12923 | DSM drowsiness event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11701 COM2 - 12924 | DSM distraction event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11702 COM2 - 12925 | DSM yawning event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11703 COM2 - 12926 | DSM phone event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11704 COM2 - 12927 | DSM smoking event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11705 COM2 - 12928 | DSM driver absence event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11706 COM2 - 1292 | DSM mask event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11707 COM2 - 12930 | DSM G-sensor event | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11708 COM2 - 12931 | DSM active driver name | 10 | ASCII | 0 | 10 | - | - | Active driver name | FMC650, FMM650 | Cameras/Video |
| COM1 - 11709 COM2 - 12932 | DSM recording status | 1 | Unsigned | 0 | 2 | - | - | 0 - None / 1 - Recording (mic off) / 2 - Recording (mic on) | FMC650, FMM650 | Cameras/Video |
| COM1 - 11710 COM2 - 12933 | DSM GPS status | 1 | Unsigned | 0 | 2 | - | - | 0 - None / 1 - Connected (no data) / 2 - Connected (valid data) | FMC650, FMM650 | Cameras/Video |
| COM1 - 11711 COM2 - 12934 | DSM speed | 1 | Unsigned | 0 | 255 | - | km/h | Vehicle speed, km/h (or mi/h) | FMC650, FMM650 | Cameras/Video |
| COM1 - 11712 COM2 - 12935 | DSM error code | 1 | HEX | 0 | 0x17 | - | - | Sum of individual error values (0x00 - no error): / 0x01 - Camera fail / 0x02 - GPS fail / 0x04 - CAN fail / 0x10 - Camera blocked | FMC650, FMM650 | Cameras/Video |
| COM1 - 11713 COM2 - 12936 | DSM seatbelt detection | 1 | Unsigned | 0 | 1 | - | - | 0 - inactive, 1 - detected | FMC650, FMM650 | Cameras/Video |
| COM1 - 11714 COM2 - 12937 | DSM state | 1 | Unsigned | 0 | 8 | - | - | 0 - unknown / 1 - ready / 2 - no communication / 3 - updating firmware / 4 - downloading snapshot / 5 - uploading file to server / 6 - rebooting / 7 - remounting SD / 8 - waiting for app config | FMC650, FMM650 | Cameras/Video |
