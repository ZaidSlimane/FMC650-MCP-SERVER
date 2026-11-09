---
title: How to Install FMC650 on DAF XF
device: FMC650
source: https://wiki.teltonika-gps.com/view/How_to_Install_FMC650_on_DAF_XF
archived-snapshot: https://web.archive.org/web/20260215075051/https://wiki.teltonika-gps.com/view/How_to_Install_FMC650_on_DAF_XF
captured: 2026-11-04
---

# How to Install FMC650 on DAF XF

![1_FMB___DAF](assets/1_FMB___DAF.png)

# Installation proccess

- Below is shown main installation location:

![Fuse panel cover](assets/2_Fuse_panel_cover.png)Fuse panel cover- Carefully unscrew the fuse panel screws and fold the panel down.

![Fuse panel and screws location](assets/3_Fuse_panel_and_screws_location.png)Fuse panel and screws location- Where to find main connector?

![Main FMS connector location](assets/4_Main_FMS_connector_location.png)Main FMS connector location- Connect the wires accordingly. It is recommended to use DIN 1 instead of DIN 3 for ignition detection.

![FMB640 and DAF XF connection](assets/5_FMB640_and_DAF_XF_connection_wires.png)FMB640 and DAF XF connection- After installation and device configuration of FMC650 (CAN1 should be selected – FMS/TACHO), you can check if installation is properly made. Turn on ignition of vehicle and send SMS command: “ tachocheck”. If response shows: “Can1:111,F2EF”, 111 -means tachograph properly connected, F2EF - or any other value which is not equal to 0000, means FMS data received also.
