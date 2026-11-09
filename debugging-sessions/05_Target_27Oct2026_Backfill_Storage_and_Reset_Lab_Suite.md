---
title: "Target 05 — 27 Oct 2026 Lab Diagnostic Suite: Ignition Tuning, Network Outage Backfill, Dual-DB Drain & Brownout Crash"
device: "FMC650"
firmware: "03.01.01.Rev.15"
captured: "2026-10-27 12:06:23 to 19:20:40"
log_files:
  - "05_2026-10-27_1206_post_softreset_boot_and_ignition_flapping_com.txt"
  - "06_2026-10-27_1256_ignition_flapping_and_job_queue_overflow.txt"
  - "07_2026-10-27_1356_ignition_source_din1_vs_power_voltage_test.txt"
  - "08_2026-10-27_1404_ignition_threshold_20v_max_stabilization.txt"
  - "09_2026-10-27_1449_stable_dual_server_baseline_flash_only.txt"
  - "10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt"
  - "11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt"
  - "12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt"
  - "13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt"
---

# Target 05 — 27 Oct 2026 Lab Diagnostic Suite: Ignition Tuning, Network Outage Backfill, Dual-DB Drain & Brownout Crash

This document consolidates the 9 chronological laboratory sessions captured on **2026-10-27** (`12:06:23` to `19:20:40`) from `FULL_FMC650_DIAGNOSTIC.zip` and `FMC650 backfill and reset analysis — lab logs 27 Oct 2026.md`, mapping each renamed `.txt` log file to its specific debugging target and quantitative metrics.

---

## 1. Overview of the 9 Renamed Session Logs (27 Oct 2026)

| Session # | Renamed `.txt` File | Original Filename | Time Window (UTC+1) | Size / Lines | Specific Debugging Target & Outcome |
|---:|---|---|---|---:|---|
| **05** | [05_2026-10-27_1206_post_softreset_boot_and_ignition_flapping_com.txt](./05_2026-10-27_1206_post_softreset_boot_and_ignition_flapping_com.txt) | `FMC650_COM.log` | `12:06:23` – `12:10:53` | `158,922 B` (`4,708` lines) | Post-SoftReset (`Software: 11`) boot inspection, `m2m_recmng_internal_api.c:1012` unclosed file recovery, and initial ignition-flapping reproduction (`1` `[F.D.T.F]` overflow). |
| **06** | [06_2026-10-27_1256_ignition_flapping_and_job_queue_overflow.txt](./06_2026-10-27_1256_ignition_flapping_and_job_queue_overflow.txt) | `IGNITION_WATCH.log` | `12:56:24` – `13:01:31` | `38,679 B` (`955` lines) | Focused observation of ignition oscillation (`src:2` vs `src:128`) generating **23 `[F.D.T.F]-> Full can't process 16 job` drops** and `attr:7006` write saturation. |
| **07** | [07_2026-10-27_1356_ignition_source_din1_vs_power_voltage_test.txt](./07_2026-10-27_1356_ignition_source_din1_vs_power_voltage_test.txt) | `ignition din1 or pv.log` | `13:56:02` – `13:58:50` | `36,650 B` (`971` lines) | Live comparison of Ignition Source settings (`DIN1` `src:2` vs `Power Voltage` `src:128`); eliminates `[F.D.T.F]` queue overflow (`0` drops). |
| **08** | [08_2026-10-27_1404_ignition_threshold_20v_max_stabilization.txt](./08_2026-10-27_1404_ignition_threshold_20v_max_stabilization.txt) | `LAB IGNITION 20V MAX .log` | `14:04:14` – `14:06:33` | `83,401 B` (`1,904` lines) | Raising Power Voltage Ignition upper ceiling to `20,000 mV` (`12000,20000`) with bench supply at `15.1 V`; confirms stable ignition state (`0` drops). |
| **09** | [09_2026-10-27_1449_stable_dual_server_baseline_flash_only.txt](./09_2026-10-27_1449_stable_dual_server_baseline_flash_only.txt) | `putty 2.log` | `14:49:58` – `14:51:45` | `73,287 B` (`1,658` lines) | Clean baseline before outage simulation: SD removed (`FATRES: 3`), `recdb/0` (Flash) active, live records sent to `SOC0` (`203.0.113.10:20332`) and `SOC5` (`198.51.100.30:20001`). |
| **10** | [10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt](./10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt) | `DATA LOSS SIMULATION .log` | `14:51:47` – `16:01:42` | `765,172 B` (`29,307` lines) | **70-Minute Network Outage Simulation (SIM Removed)**: Proves continuous flash buffering in `recdb/0` across file rollover (`File 2 -> File 3` at `30,720 B` / 256 records) up to `TotalRecCnt: 379` with zero resets. |
| **11** | [11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt](./11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt) | `DLS2.log` | `16:28:11` – `16:38:40` *(boots at `2022.01.01`)* | `325,776 B` (`7,652` lines) | **Cold PowerOn Recovery (`PowerOn: 1`, `Software: 0`)**: Boots with uninitialized RTC (`2022.01.01 00:00:00`), syncs time to `2026.10.27 16:28:11` via GNSS/NITZ, recovers **382 flash records**, and drains them in 7–8 record batches to both servers down to `TotalRecCnt: 0` at `16:35:05`. |
| **12** | [12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt](./12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt) | `SD CARD TEST.txt` | `19:12:43` – `19:14:16` | `144,932 B` (`1,762` lines) | **Simultaneous SD (`db:1`) & Flash (`db:0`) Interleaved Drain**: With SD card inserted (`FATRES: 0`), drains 149 SD records (`File 11`, `sd:recdb/1`) and 13 Flash records (`File 5`, `recdb/0`) concurrently to both servers down to `0` backlog. |
| **13** | [13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt) | `SD CARD + SIM.txt` | `19:16:49` – `19:20:40` | `113,324 B` (`2,056` lines) | **External Voltage Sag (`8.6 V`) -> Ignition Flapping -> `AppSave` Watchdog Crash (`arg=46`)**: External power drops to `8,632 mV`, triggering `eSD_JobRemoveBattery` (`Busy`), 34 `[F.D.T.F]` drops, `AVLBUF` lock (`153/1800 F:N`), and `m2m_task_watchdog.c:93` (`arg=46`) at `19:20:39`. |

---

## 2. Deep-Dive Highlights from the 27 Oct 2026 Suite

### 2.1 Proof of Zero-Loss Offline Buffering & 256-Record File Rollover (Sessions 10 & 11)
- In [10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt](./10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt):
  - At `14:52:47`, the SIM card is removed (`+CPIN: NO SIM`), causing sockets `SOC0` and `SOC5` to close (`Error [4] M:modem_status.c L:68`, `Error [4] M:modem_init.c L:328`).
  - Even while the modem repeats its 15-second SIM detection / `Switch SIM -> 1` cycle (`[WD.FUNC]-> counter:0, State:1 Val:66..606 Limit:900`), the acquisition engine builds a 120-byte record every 20 seconds and writes it to `recdb/0`.
  - At `15:20:09`, `File 2` reaches its exact capacity of **256 records (`30,720 bytes`)**:
    ```text
    [2026.10.27 15:20:09]-[T.RECMNG]-> [recdb/0] Status:0, First File:2, Last File:2, Write Offset:30600, Read Offset:16680, TotalRecCnt:117
    [2026.10.27 15:20:09]-[T.RECMNG]-> Closed file handle: 0
    [2026.10.27 15:20:29]-[T.RECMNG]-> [recdb/0] Status:0, First File:2, Last File:3, Write Offset:0, Read Offset:16680, TotalRecCnt:118
    ```
  - By `16:01:28`, `TotalRecCnt` reaches **379 records** across `File 2` and `File 3` with CPU load at a calm `31%`.
- In [11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt](./11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt):
  - After full power removal, the unit cold-boots at default RTC `2022.01.01 00:00:00`, preserves the unclosed `File 4` via `m2m_recmng_internal_api.c:rec_file_read:1012` (`File not finished don't erase`), synchronizes the clock to `2026.10.27 16:28:11`, connects to both servers at `16:28:39`, and drains all **382 buffered records** down to `TotalRecCnt: 0` at `16:35:05`.

### 2.2 Dual-Database (`sd:recdb/1` + `recdb/0`) Concurrent Drain (Session 12)
- In [12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt](./12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt):
  - Both storage backends hold unacknowledged records simultaneously (`sd:recdb/1` has 149 records in `File 11`; `recdb/0` has 13 records in `File 5`).
  - The firmware drains `db:1` (SD) in 7-record (`855 B`) and 8-record (`975 B`) Codec 8E packets down to `TotalRecCnt: 0` at `19:13:26`, then seamlessly drains the remaining 13 records from `db:0` (Flash) down to `TotalRecCnt: 0` at `19:13:34`.

### 2.3 First Reproduction of the `arg=46` Watchdog Crash & Handoff to Target 01 (Session 13)
- In [13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt):
  - At `19:17:17`, external supply drops (`Ext:8632 mV`), triggering `[BAT.PWR.M]-> Busy, can't execute:eSD_JobRemoveBattery job` and rapid ignition flapping (`src:128` vs `src:2`).
  - At `19:20:39`, Task 0 (`[AppSave]`) hits `tmo:180/180` while `AVLBUF` is held (`153/1800 F:N`), triggering `[CPU RESET]->CPU reset has been initiated: 46, m2m_task_watchdog.c:93`.
  - The unit reboots at **`2026.10.27 19:20:40`** (line 2056) — which is the exact `Startup Time: 2026/10/27 19:20:40` observed 13 hours and 16 minutes later at the beginning of [Target 01 (`01_2026-10-28_0833_...txt`)](./01_Target_Ignition_Flapping_and_AppSave_Watchdog_Crash_Arg46.md).
