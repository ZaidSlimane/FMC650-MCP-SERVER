---
title: How to install FMC650 to MB Actros
device: FMC650
source: https://wiki.teltonika-gps.com/view/How_to_install_FMC650_to_MB_Actros
archived-snapshot: https://web.archive.org/web/20260610003543/https://wiki.teltonika-gps.com/view/How_to_install_FMC650_to_MB_Actros
captured: 2026-11-04
---

# How to install FMC650 to MB Actros

![1_FMX640_and_MB_actros](assets/1_FMX640_and_MB_actros.png)

# Installation proccess

- Below is shown main installation location:

![Installation location](assets/2_cable_location.png)Installation location- Main cables, which should be used – twisted pair of violet and white-brown for FMS/CAN and Tachograph connection. The same line is used to read FMS data and to download Tachograph files. Additionally, K-line wire for live vehicle data from the tachograph is located in the same place violet – white wire:

![Locating FMS and K-Line wires](assets/3_wires.png)Locating FMS and K-Line wires- Below shown the connection of CAN1 pair from FMB6 device to FMS/TACHO line on vehicle and K-line connection to FMB6:

![3 FMS and K-Line connection to FMB6](assets/4_wire_meanings.png)3 FMS and K-Line connection to FMB6- To get proper resistance on the CAN circuit, needed to disconnect the resistance connector which is near the tachograph:

![Resistence connector location](assets/5_tacho_resistor_location.png)Resistence connector location![Resistence connector with attachment](assets/6_resistor_connector.png)Resistence connector with attachment![Resistence connector](assets/7_connector_removed.png)Resistence connector- Recommended power source and ignition connection wires:

![Power source and ignition wires](assets/8power_source_and_ignition_wires.png)Power source and ignition wiresMore detailed view of Ignition connection:

![Ignition detection wire](assets/9_ignition_detection_wires.png)Ignition detection wire- Recommended place for GNSS antenna:

![antenna prefered installation location](assets/10_gnss_antena_location.png)antenna prefered installation location![Installed GNSS antenna](assets/11_installed_gnss_antena.png)Installed GNSS antennaAfter installation and device configuration of FMC6 (CAN1 should be selected – FMS/TACHO), you can check if the installation is properly made. Turn on the ignition of the vehicle and send SMS command: “tachocheck”. If the response shows: “Can1:111,F2EF”, 111 -means tachograph properly connected, F2EF - or any other value which is not equal to 0000, means FMS data received also.
