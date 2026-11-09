---
title: "Target 06 — FMC650 GPS, Data Acquisition & Network Configuration Parameter Map Linked to Debug Telemetry"
device: "FMC650"
firmware: "03.01.01.Rev.15"
captured: "2026-10-27 to 2026-10-31"
log_file: "14_fmc650_gps_and_network_parameter_map.txt"
---

# Target 06 — FMC650 GPS, Data Acquisition & Network Configuration Parameter Map Linked to Debug Telemetry

- **Parameter Map Text File**: [14_fmc650_gps_and_network_parameter_map.txt](./14_fmc650_gps_and_network_parameter_map.txt) (renamed from `fmc650_mapped.txt`, 68 lines, 11,947 bytes)

---

## 1. Purpose of This Target

This target correlates the extracted Teltonika FMC650 Configurator Parameter IDs (`PID`) in [14_fmc650_gps_and_network_parameter_map.txt](./14_fmc650_gps_and_network_parameter_map.txt) directly with the runtime firmware behaviors, log tags, and failure signatures observed across Sessions `01` through `13`.

---

## 2. System, Ignition, Sleep & Record Ordering Parameters (`PID 100` – `PID 199`)

| Parameter ID | Configurator Label | Default / Range | Firmware Module & Log Signature | Impact in Debugging Sessions |
|---:|---|---|---|---|
| **PID 100** | Data Send Order (`Priority`) | `0` (`Oldest First`) / `1` (`Newest First`) | `[T.RECMNG]-> LoadRec db:0/1 Order:2 ...` | Set to **Newest First (`Order:2` internally)** across all sessions (`01`–`13`), causing `[T.RECMNG]` to drain from `Write Offset` backwards so the server receives the freshest telemetry first after an outage. |
| **PID 101** | Ignition Source | `1` (`Power Voltage`) / `2` (`DIN1`) / `130` (`DIN1 \| Power Voltage`) | `[Ignition]-> New Igniton state: X, src:Y` | **Root cause of `arg=46` & `arg=21` crashes** when `src:128` (`Power Voltage`) and `src:2` (`DIN1`) conflict around `8.5 V – 12.0 V`. Setting to `DIN1` (`2`) only prevents voltage-sag flapping. |
| **PID 102** | Sleep Mode | `0` (`Disable`), `1` (`Gps Sleep`), `2` (`Deep Sleep`), `3` (`Online Deep Sleep`) | `[Dsleep]` (Task 3), `[GPS.INIT] Warning check failed -> GNSS stays on` | Controls when `[GPS.T]` powers down `AG3335M` (`$PAIR003`) and when `[MODEM]` detaches during ignition OFF. |
| **PID 103** | Sleep Timeout | `1..3000 min` | `[Dsleep]` delay timer after `Ignition: 0` & `Movement: 0` | Delay before entering the sleep mode configured in `PID 102`. |
| **PID 104 / 105** | Low / High Voltage for Power Voltage Ignition | `13200 mV` / `30000 mV` (tested with `12000,20000`) | `[BAT.POWER.MAN] ... Ext:8577(12000,20000)` | Directly printed inside the parentheses after `Ext:<mV>(<Low>,<High>)` on every `[BAT.POWER.MAN]` line! |
| **PID 106 / 112** | Static Navigation | `1` (`Enabled`) | `[GPS.T]` static navigation filter | Freezes GNSS coordinates when `Movement: 0` (`[Movement]-> Current movement state: 0`) or Ignition is OFF to eliminate stationary GPS drift. |
| **PID 108 / 109** | LED Indication | `1` (`Enabled`) | `[HBeat]` (Task 11) | Controls status LEDs on the FMC650 enclosure. |
| **PID 113** | GNSS Source Constellation | `3` (`GPS + GLONASS + Galileo`) | `[GPS.INIT]` `$PAIR` constellation setup | Configures Airoha `AG3335M` multi-constellation tracking (`Satellites: 11–14` in outdoor/assisted tests). |

---

## 3. GPRS, Primary Server & Backup Server Parameters (`PID 2000` – `PID 2104`)

| Parameter ID | Configurator Label | Values Observed in Logs | Firmware Module & Log Signature | Impact in Debugging Sessions |
|---:|---|---|---|---|
| **PID 2000 / 2001** | GPRS Context (SIM 1) | `1` (`Enabled`) | `[MODEM]`, `AT+CGACT=1,1` | Enables packet data context on SIM 1. |
| **PID 2002 / 2013** | APN (SIM 1 / SIM 2) | `djezzy.internet` / `internet.m2m.sim2.dz` | `[M.INIT]` APN configuration | SIM 1 used Djezzy (`IMSI: 60302...`) in Sessions `01–03`, `05–13` and m2m.sim2 (`IMSI: 60301...`) in Session `04`. |
| **PID 2004 / 2005** | Primary Server Domain / IP | `203.0.113.10` (Oct 27–28)<br/>`203.0.113.20` (Oct 31) | `[SOCKET]` **Handle `0` (`SOC0`)**, `Filter:1`, `Mark:1`, `WD.FUNC counter:2` | **Critical**: Monitored by `WD.FUNC counter:2` (`Limit:930 s`). In [Session 04](./04_Target_Primary_Server_TCP_TLS_Timeout_and_Full_Modem_Reset.md), unreachable `203.0.113.20` caused `counter:2` (`2443/930`) to trigger a Full Modem Reset (`app_data_sending.c:2304`). |
| **PID 2006** | Primary Server Port | `20332` (Oct 27–28)<br/>`5027` (Oct 31) | `AT+CIPSTART=0,"TCP","<host>",<port>` | Port for Primary Server (`SOC0`). |
| **PID 2007 / 2010** | Backup Server Mode | `0` (`Disable`), `1` (`Backup`), `2` (`Duplicate`) | `[LIVE.REC]-> Rec to RAM Srv:0 OK` & `Srv:1 OK` | Configured to **Duplicate Mode (`2`)** in all sessions: every record is marked with both `Filter:1` (`SOC0`) and `Filter:2` (`SOC5`) and must be ACKed by both servers before deletion. |
| **PID 2008** | Backup Server Domain / IP | `ch0000000.flespi.gw` (`198.51.100.30` / `198.51.100.130`) | `[SOCKET]` **Handle `5` (`SOC5`)**, `Filter:2`, `Mark:2`, `WD.FUNC counter:3` | Resolved via DNS to `198.51.100.30` or `198.51.100.130`. Maintained 100% availability whenever the modem was up. |
| **PID 2009** | Backup Server Port | `20001` | `AT+CIPSTART=5,"TCP","198.51.100.130",20001` | Port for Backup Server (`SOC5`). |

---

## 4. Data Acquisition & Send Period Matrix (`PID 10000` – `PID 10258`)

The FMC650 maintains 6 acquisition profiles (Home vs Roaming × On Stop vs Moving, across vehicle modes) with identical structure:

| Parameter Offset | Parameter Role | Default / Range | Observed in Lab Sessions | Firmware Log Signature |
|---|---|---|---|---|
| **PID 10000 / 10050 / 10100 / 10150 / 10200 / 10250** | **Min Period** (Record Acquisition Interval) | `Default: 3600 s` (`0..2592000 s`) | Set to **`20 s` or `30 s`** in lab profiles | `[Rec.Build]-> Start building record by event 0` (periodic acquisition timer). |
| **PID 10001 / 10051 / 10101 / 10151 / 10201 / 10251** | **Min Saved Records** per Packet | `Default: 1` (`1..255`) | **`1` record** on live link (`[LIVE.REC]`); **`7–8` records** during backlog drain (`LoadRec ... Count:7`) | Controls whether `[APP.SND.D]` transmits immediately on every record (`1`) or batches records. |
| **PID 10002 / 10052 / 10102 / 10152 / 10202 / 10252** | **Send Period** | `Default: 120 s` (`0..2592000 s`) | **`20 s` / `30 s`** on live link; **`720 s`** retry backoff on failed link | Printed every second in `[APP.SND.D]-> 0/1 Time until data sending <sec>`. |
| **PID 10005 / 10055 / 10105 / 10155 / 10205 / 10255** | **Min Distance** | `Default: 1000 m` | Triggered only when GNSS speed > 0 | Distance-based record acquisition trigger. |
| **PID 10006 / 10056 / 10106 / 10156 / 10206 / 10256** | **Min Angle** | `Default: 10 deg` | Course-change trigger | Heading-delta record acquisition trigger. |
| **PID 10007 / 10057 / 10107 / 10157 / 10207 / 10257** | **Min Speed Delta** | `Default: 10 km/h` | Speed-change trigger | Radial speed delta acquisition trigger. |
| **PID 10008 / 10058 / 10108 / 10158 / 10208 / 10258** | **GPRS Week Time / Timezone Sync** | Bitmask | NITZ / GNSS time sync | Used during cold boot in [Session 11](./11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt) to jump RTC from `2022.01.01` to `2026.10.27`. |
