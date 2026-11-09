---
title: FMC650 TrailerCAN
device: FMC650
source: https://wiki.teltonika-gps.com/view/FMC650_TrailerCAN
archived-snapshot: https://web.archive.org/web/20260415130152/https://wiki.teltonika-gps.com/view/FMC650_TrailerCAN
captured: 2026-11-04
---

# FMC650 TrailerCAN

This pages describes the TrailerCAN feature and gives related information.

# Introduction

The **Electronic Braking System (EBS) modulator** is a key component in a trailer’s braking system. It not only controls braking performance but also ensures seamless communication with the connected truck. The global EBS modulator market is dominated by WABCO, Knorr-Bremse, and Haldex, each integrated into a wide variety of trailer types, including curtain siders, reefers, and flatbeds for numerous trailer manufacturers.

Because trucks, trailers, and EBS modulators are manufactured by different companies, ECE Regulation No. 13 and ISO 11992 global standards were introduced to ensure full compatibility. This standard is regularly updated and allows for smooth coupling between any truck and trailer, regardless of brand. It also standardizes data exchange and communication, making mixed-fleet integration much easier worldwide.

FMC650, with its **TrailerCAN feature**, reads trailer data via CAN bus based on standardized regulations and provides it through **I/O elements**, enabling seamless integration with any fleet management platform.
FMC650 is a powerful and versatile device that can gather trailer CAN data from multiple sources:

- Directly from the truck
- Straight from the EBS modulator
- Via the trailer socket

# Truck and Trailer Coupling

Coupling of the towing truck and towed trailer is done according to ECE Regulation No. 13 and ISO 11992 standard.

CAN data between towing and towed vehicles is exchanged via the ISO 7638 7-pin socket.

- [](https://wiki.teltonika-gps.com/index.php?title=File:TrailerCAN_coupling_example.png)
 Coupling example (© Erich Jaeger)
- [](https://wiki.teltonika-gps.com/index.php?title=File:TrailerCAN_socket_example.png)
 Socket example (© Erich Jaeger)

| # | Function | Color |
| --- | --- | --- |
| 1 | Plus electrovalve | Red |
| 2 | Plus electronics | Black |
| 3 | Minus electronics | Yellow |
| 4 | Minus electrovalve | Brown |
| 5 | Warning device control (normally open) | White |
| 6 | CAN_H | White/green |
| 7 | CAN_L | White/brown |

# Physical Connection Options

**1. FMC650 reading trailer data via the truck:**

FMC650 is designed to read a coupled trailer‘s data from the truck itself. A connection can be made using the Teltonika ECAN02 adapter to avoid damaging wires or voiding the warranty. Connection schemes for different manufacturers, generations, and truck model years are in progress. You can contact our support team to get the guidelines for your specific truck.

Example:

- [](https://wiki.teltonika-gps.com/view/File:TrailerCAN_physical_truck1.png)
 TrailerCAN connection to truck
- [](https://wiki.teltonika-gps.com/index.php?title=File:TrailerCAN_physical_truck2.png)
 TrailerCAN connection to truck - Configurator

**2. Direct connection to the EBS modulator:**

FMC650 can be connected directly to the EBS modulator’s diagnostic line or another CAN line using a specific OEM cable from the manufacturer. Connection instructions and part numbers for OEM cables are being developed.

Example:

- [](https://wiki.teltonika-gps.com/index.php?title=File:TrailerCAN_physical_ebs1.png)
 TrailerCAN connection to EBS (1)
- [](https://wiki.teltonika-gps.com/view/File:TrailerCAN_physical_ebs2.png)
 TrailerCAN connection to EBS (2)
- [](https://wiki.teltonika-gps.com/view/File:TrailerCAN_physical_ebs3.png)

**3. Connection via the ISO 7638 7-pin socket:**

The ISO 7638 7-pin socket can be used as a data source. Pins 6 and 7 are used for CAN data exchange between the truck and trailer, to which FMC650 CAN lines can be connected. Power supply can be taken from Pins 2 and 3.

# Device Configuration

Currently, firmware version 03.01.01.Rev.03 can be used for trailer data reading, with the B.FMX6_R.167 configurator version to set up the device. Different truck manufacturers have different connection locations—baud rates may vary depending on the vehicle model.

- [](https://wiki.teltonika-gps.com/index.php?title=File:TrailerCAN_config1.png)
 Configurator: CAN \ Tachograph settings
- [](https://wiki.teltonika-gps.com/view/File:TrailerCAN_config2.png)
 Configurator: TrailerCAN settings

# AVL ID List

| AVL ID | Property Name | AVL ID | Property Name |
| --- | --- | --- | --- |
| 13651 | Detected towed vehicle | 13677 | Braking via electric control line support |
| 13652 | Trailer wheel based speed | 13678 | ROP system status |
| 13653 | ABS status | 13679 | YC system status |
| 13654 | Retarder control status | 13680 | Traction help status |
| 13655 | Red warning signal request | 13681 | Lift axle 1 position status |
| 13656 | Amber warning signal request | 13682 | Lift axle 2 position status |
| 13657 | Axle load sum | 13683 | Steering axle locking status |
| 13658 | Retarder wheel torque reference | 13684 - 13698 | Each wheel tire pressure status* |
| 13659 | Service brake status | 13699 - 13713 | Each wheel tire pressure* |
| 13660 | Electrical supply status | 13714 - 13728 | Each wheel brake lining status* |
| 13661 | Vehicle type | 13729 - 13743 | Each wheel brake lining* |
| 13662 | Axle load measured by towed vehicle | 13744 - 13758 | Each wheel brake temperature status* |
| 13663 | Axle load measured by external scale | 13759 - 13773 | Each wheel brake temperature |
| 13664 | Calibration data load level | 13774 | Vehicle pneumatic supply status |
| 13665 - 13670 | Brake cylinder pressure of each wheel | 13775 - 13789 | Each wheel air leakage detection* |
| 13671 | Trailer VIN** | 13790 - 13804 | Each tire temperature* |
| 13672 | VDC active | 13805 | Automatic towed vehicle braking status |
| 13673 | Lateral acceleration | 13806 | Electrical supply of non-braking system status |
| 13674 | Loading ramp approach assistance status | 13807 | Spring brake installation status |
| 13675 | Supply line braking | 13808 | Electrical load proportional function installation status |
| 13676 | Stop lamps request | 13809 | Spring brake status |
| 13810 | Pneumatic supply pressure | — | — |

## 2nd trailer CAN AVL ID

| AVL ID | Property Name | AVL ID | Property Name |
| --- | --- | --- | --- |
| 13814 | ABS status 2nd trailer | 13839 | ROP system status 2nd trailer |
| 13815 | Retarder control status 2nd trailer | 13840 | YC system status 2nd trailer |
| 13816 | Red warning signal request 2nd trailer | 13841 | Traction help status 2nd trailer |
| 13817 | Amber warning signal request 2nd trailer | 13842 | Lift axle 1 position status 2nd trailer |
| 13818 | Axle load sum 2nd trailer | 13843 | Lift axle 2 position status 2nd trailer |
| 13819 | Retarder wheel torque reference 2nd trailer | 13844 | Steering axle locking status 2nd trailer |
| 13820 | Service brake status 2nd trailer | 13845-13859 | Each wheel tire pressure status* 2nd trailer |
| 13821 | Electrical supply status 2nd trailer | 13860-13874 | Each wheel tire pressure* 2nd trailer |
| 13822 | Vehicle type 2nd trailer | 13875-13889 | Each wheel brake lining status* 2nd trailer |
| 13823 | Axle load measured by towed vehicle 2nd trailer | 13890-13904 | Each wheel brake lining* 2nd trailer |
| 13824 | Axle load measured by external scale 2nd trailer | 13905-13919 | Each wheel brake temperature status* 2nd trailer |
| 13825 | Calibration data load level 2nd trailer | 13920-13934 | Each wheel brake temperature 2nd trailer |
| 13826-13831 | Brake cylinder pressure of each wheel 2nd trailer | 13935 | Vehicle pneumatic supply status 2nd trailer |
| 13832 | Trailer VIN** 2nd trailer | 13936-13950 | Each wheel air leakage detection* 2nd trailer |
| 13833 | VDC active 2nd trailer | 13951-13965 | Each tire temperature* 2nd trailer |
| 13834 | Lateral acceleration 2nd trailer | 13966 | Automatic towed vehicle braking status 2nd trailer |
| 13835 | Loading ramp approach assistance status 2nd trailer | 13967 | Electrical supply of non-braking system status 2nd trailer |
| 13836 | Supply line braking 2nd trailer | 13968 | Spring brake installation status 2nd trailer |
| 13837 | Stop lamps request 2nd trailer | 13969 | Electrical load proportional function installation status 2nd trailer |
| 13838 | Braking via electric control line support 2nd trailer | 13970 | Spring brake status 2nd trailer |
| — | — | 13971 | Pneumatic supply pressure 2nd  trailer |

## 3rd trailer CAN AVL ID

| AVL ID | Property Name | AVL ID | Property Name |
| --- | --- | --- | --- |
| 13975 | ABS status 3rd trailer | 14000 | ROP system status 3rd trailer |
| 13976 | Retarder control status 3rd trailer | 14001 | YC system status 3rd trailer |
| 13977 | Red warning signal request 3rd trailer | 14002 | Traction help status 3rd trailer |
| 13978 | Amber warning signal request 3rd trailer | 14003 | Lift axle 1 position status 3rd trailer |
| — | — | — | — |
| 13979 | Axle load sum 3rd trailer | 14004 | Lift axle 2 position status 3rd trailer |
| 13980 | Retarder wheel torque reference 3rd trailer | 14005 | Steering axle locking status 3rd trailer |
| — | — | — | — |
| 13981 | Service brake status 3rd trailer | 14006 - 14020 | Each wheel tire pressure status* 3rd trailer |
| — | — | — | — |
| 13982 | Electrical supply status 3rd trailer | 14021 - 14035 | Each wheel tire pressure* 3rd trailer |
| 13983 | Vehicle type 3rd trailer | 14036 - 14050 | Each wheel brake lining status* 3rd trailer |
| 13984 | Axle load measured by towed vehicle 3rd trailer | 14051 - 14065 | Each wheel brake lining* 3rd trailer |
| 13985 | Axle load measured by external scale 3rd trailer | 14066 - 14080 | Each wheel brake temperature status* 3rd trailer |
| 13986 | Calibration data load level 3rd trailer | 14081 - 14095 | Each wheel brake temperature 3rd trailer |
| 13987 - 13992 | Brake cylinder pressure of each wheel 3rd trailer | 14096 | Vehicle pneumatic supply status 3rd trailer |
| 13993 | Trailer VIN** 3rd trailer | 14097 - 14111 | Each wheel air leakage detection* 3rd trailer |
| 13994 | VDC active 3rd trailer | 14112 - 14126 | Each tire temperature* 3rd trailer |
| 13995 | Lateral acceleration 3rd trailer | 14127 | Automatic towed vehicle braking status 3rd trailer |
| 13996 | Loading ramp approach assistance status 3rd trailer | 14128 | Electrical supply of non-braking system status 3rd trailer |
| 13997 | Supply line braking 3rd trailer | 14129 | Spring brake installation status 3rd trailer |
| 13998 | Stop lamps request 3rd trailer | 14130 | Electrical load proportional function installation status 3rd trailer |
| 13999 | Braking via electric control line support 3rd trailer | 14131 | Spring brake status 3rd trailer |
| — | — | 14132 | Pneumatic supply pressure 3rd trailer |

(*) Some parameters might not be available if the trailer is not fitted with a TPMS system or the required sensors.

(**) The trailer can provide the full VIN number, or only a partial one (equipment number/chassis number/serial number).

VIN example 1VIN example 2

> **Note:** this page embeds screenshots/images served by the archived snapshot from never-captured paths (`web.archive.org/images/...`); the Wayback Machine has no capture of these files, so they could not be preserved. The textual content above is complete.
