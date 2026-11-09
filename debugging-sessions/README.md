---
title: "Teltonika FMC650 — Laboratory Debugging Sessions, Renamed Logs & Target Analyses"
device: "FMC650"
firmware: "03.01.01.Rev.15"
hardware: "HW:17 (Bootloader 65.10)"
imei: "860000000000001"
captured: "2026-10-27 to 2026-10-31"
---

# Teltonika FMC650 — Debugging Sessions Knowledge Base

This directory contains the complete collection of **14 renamed diagnostic `.txt` logs and parameter maps** captured on a Teltonika FMC650 (`IMEI: 860000000000001`, FW `03.01.01.Rev.15`) between **27 Oct 2026 and 31 Oct 2026**, paired with **7 structured Markdown technical references and per-target debugging analyses**.

---

## 1. Master Architecture & Critical Errors Reference

- **[FMC650_Core_Functionalities_and_Critical_Errors.md](./FMC650_Core_Functionalities_and_Critical_Errors.md)**
  - **Part 1 — Core Functionalities**: Boot pipeline (`[HW.INIT]`, LittleFS 16 MB XTX NOR flash `0B4018`, FATFS MicroSD `SD:`), complete 33-slot RTOS Task table (`0:[AppSave]` through `31:[GPS.T]`), 17-mutex watchdog table (`[MTX.WDG]`), 3-tier watchdog architecture (`[WDG.TASK]`, `[MTX.WDG]`, `[WD.FUNC]`), dual-database (`recdb/0` + `sd:recdb/1`) & RAM fast-path (`[LIVE.REC]`) storage pipeline, dual-socket cellular transport (`SOC0` Primary vs `SOC5` Backup), and power/battery management (`[BAT.POWER.MAN]`).
  - **Part 2 — Critical Errors & Root Causes**: Complete catalog (`E1`–`E13`) of every crash (`m2m_task_watchdog.c:93` with `arg=46`, `arg=21`, `arg=53`; `flash_api.c:590` with `arg=27`), job queue saturation (`[F.D.T.F]-> Full can't process 16 job`), full modem reset (`app_data_sending.c:2304`), shared AT channel head-of-line blocking (`Server Response TMO` + `CODEC12 ERROR`), missing TLS root certificate (`z:\cert\root.pem`), and brownout hibernate contention (`pwr_manager_cng_states.c:60`).

---

## 2. Per-Target Markdown Analyses

| Target ID | Target Markdown Document | Primary Debugging Target Defined | Associated Renamed `.txt` Files |
|---|---|---|---|
| **Target 01** | [01_Target_Ignition_Flapping_and_AppSave_Watchdog_Crash_Arg46.md](./01_Target_Ignition_Flapping_and_AppSave_Watchdog_Crash_Arg46.md) | 13h 16m overnight stability verification followed by `8.57 V` voltage sag, 950 ignition flips, 255 `[F.D.T.F]` queue drops, `AVLBUF` mutex lock, and Task 0 (`[AppSave]`) watchdog crash (`arg=46`). | [01_2026-10-28_0833_...txt](./01_2026-10-28_0833_ignition_flapping_appsave_watchdog_crash_arg46.txt)<br/>[13_2026-10-27_1916_...txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt) |
| **Target 02** | [02_Target_Settings_Mutex_Deadlock_Scheduler_Watchdog_Crash_Arg21_and_Brownout.md](./02_Target_Settings_Mutex_Deadlock_Scheduler_Watchdog_Crash_Arg21_and_Brownout.md) | 3-boot stress trace: `Settings` mutex deadlock (`221/1800 F:N`), Task 10 (`[Scheduler]`) watchdog crash (`arg=21`), `7.66 V` brownout hibernate (`pwr_manager_cng_states.c:60`), missing `z:\cert\root.pem`, and full recovery at `15.1 V`. | [02_2026-10-28_0843_...txt](./02_2026-10-28_0843_settings_mutex_scheduler_watchdog_crash_arg21_and_recovery.txt) |
| **Target 03** | [03_Target_Dual_Server_Flash_Backlog_Drain_and_SD_Save_Fail_Counter.md](./03_Target_Dual_Server_Flash_Backlog_Drain_and_SD_Save_Fail_Counter.md) | High-throughput interleaved dual-server (`SOC0` + `SOC5`) flash backlog drain (`Order:2`, 7 recs/pkt, 406 deliveries in 87 s), prior `arg=53` reset marker, and `SD Save Fail Cnt: 190`. | [03_2026-10-28_1224_...txt](./03_2026-10-28_1224_dual_server_flash_backlog_drain_arg53.txt) |
| **Target 04** | [04_Target_Primary_Server_TCP_TLS_Timeout_and_Full_Modem_Reset.md](./04_Target_Primary_Server_TCP_TLS_Timeout_and_Full_Modem_Reset.md) | m2m.sim2 SIM test with unreachable Primary Server (`203.0.113.20:5027`), shared AT channel blocking dropping healthy Backup Server (`SOC5`), false `CODEC12 ERROR`, `WD.FUNC counter:2` (`2443/930`) escalation, Full Modem Reset (`app_data_sending.c:2304`), and `flash_api.c:590` (`arg=27`) marker. | [04_2026-10-31_1502_...txt](./04_2026-10-31_1502_primary_server_tcp_tls_timeout_and_full_modem_reset.txt) |
| **Target 05** | [05_Target_27Oct2026_Backfill_Storage_and_Reset_Lab_Suite.md](./05_Target_27Oct2026_Backfill_Storage_and_Reset_Lab_Suite.md) | Complete 9-session lab suite from 27 Oct 2026: ignition source tuning (`DIN1` vs `Power Voltage`), 70-min SIM-removed outage buffering (`379` recs across 256-rec file rollover), RTC `2022.01.01` cold-boot recovery, and simultaneous SD + Flash interleaved drain. | [05_2026-10-27_1206_...txt](./05_2026-10-27_1206_post_softreset_boot_and_ignition_flapping_com.txt) through [13_2026-10-27_1916_...txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt) |
| **Target 06** | [06_Target_GPS_and_Network_Configuration_Parameter_Map.md](./06_Target_GPS_and_Network_Configuration_Parameter_Map.md) | Complete mapping of FMC650 Configurator Parameter IDs (`PID 100..199`, `PID 2000..2104`, `PID 10000..10258`) to the exact firmware log tags and failure modes observed in Sessions `01`–`13`. | [14_fmc650_gps_and_network_parameter_map.txt](./14_fmc650_gps_and_network_parameter_map.txt) |

---

## 3. Inventory of Renamed `.txt` Log Files

| # | Renamed `.txt` Filename | Original Source Filename | Capture Timestamp (UTC+1) | Lines | Size |
|---:|---|---|---|---:|---:|
| `01` | [01_2026-10-28_0833_ignition_flapping_appsave_watchdog_crash_arg46.txt](./01_2026-10-28_0833_ignition_flapping_appsave_watchdog_crash_arg46.txt) | `putty (1).log` | `2026-10-28 08:33:23 – 08:37:27` | `4,392` | `192,479 B` |
| `02` | [02_2026-10-28_0843_settings_mutex_scheduler_watchdog_crash_arg21_and_recovery.txt](./02_2026-10-28_0843_settings_mutex_scheduler_watchdog_crash_arg21_and_recovery.txt) | `putty2 (1).log` | `2026-10-28 08:43:17 – 09:21:14` | `24,244` | `807,650 B` |
| `03` | [03_2026-10-28_1224_dual_server_flash_backlog_drain_arg53.txt](./03_2026-10-28_1224_dual_server_flash_backlog_drain_arg53.txt) | `log3.txt` | `2026-10-28 12:24:24 – 12:25:51` | `1,654` | `170,549 B` |
| `04` | [04_2026-10-31_1502_primary_server_tcp_tls_timeout_and_full_modem_reset.txt](./04_2026-10-31_1502_primary_server_tcp_tls_timeout_and_full_modem_reset.txt) | `TLS TEST (4).txt` | `2026-10-31 15:02:33 – 15:16:12` | `4,285` | `222,355 B` |
| `05` | [05_2026-10-27_1206_post_softreset_boot_and_ignition_flapping_com.txt](./05_2026-10-27_1206_post_softreset_boot_and_ignition_flapping_com.txt) | `FMC650_COM.log` | `2026-10-27 12:06:23 – 12:10:53` | `4,708` | `158,922 B` |
| `06` | [06_2026-10-27_1256_ignition_flapping_and_job_queue_overflow.txt](./06_2026-10-27_1256_ignition_flapping_and_job_queue_overflow.txt) | `IGNITION_WATCH.log` | `2026-10-27 12:56:24 – 13:01:31` | `955` | `38,679 B` |
| `07` | [07_2026-10-27_1356_ignition_source_din1_vs_power_voltage_test.txt](./07_2026-10-27_1356_ignition_source_din1_vs_power_voltage_test.txt) | `ignition din1 or pv.log` | `2026-10-27 13:56:02 – 13:58:50` | `971` | `36,650 B` |
| `08` | [08_2026-10-27_1404_ignition_threshold_20v_max_stabilization.txt](./08_2026-10-27_1404_ignition_threshold_20v_max_stabilization.txt) | `LAB IGNITION 20V MAX .log` | `2026-10-27 14:04:14 – 14:06:33` | `1,904` | `83,401 B` |
| `09` | [09_2026-10-27_1449_stable_dual_server_baseline_flash_only.txt](./09_2026-10-27_1449_stable_dual_server_baseline_flash_only.txt) | `putty 2.log` | `2026-10-27 14:49:58 – 14:51:45` | `1,658` | `73,287 B` |
| `10` | [10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt](./10_2026-10-27_1451_network_outage_sim_removal_flash_buffering.txt) | `DATA LOSS SIMULATION .log` | `2026-10-27 14:51:47 – 16:01:42` | `29,307` | `765,172 B` |
| `11` | [11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt](./11_2026-10-27_1628_power_loss_rtc_2022_recovery_and_flash_backlog_drain.txt) | `DLS2.log` | `2026-10-27 16:28:11 – 16:38:40` | `7,652` | `325,776 B` |
| `12` | [12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt](./12_2026-10-27_1912_dual_db_sd_and_flash_interleaved_drain.txt) | `SD CARD TEST.txt` | `2026-10-27 19:12:43 – 19:14:16` | `1,762` | `144,932 B` |
| `13` | [13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt) | `SD CARD + SIM.txt` | `2026-10-27 19:16:49 – 19:20:40` | `2,056` | `113,324 B` |
| `14` | [14_fmc650_gps_and_network_parameter_map.txt](./14_fmc650_gps_and_network_parameter_map.txt) | `fmc650_mapped.txt` | `N/A (Parameter Map)` | `68` | `11,947 B` |
