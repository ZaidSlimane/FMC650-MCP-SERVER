---
title: "Target 02 — Settings Mutex Deadlock, Scheduler Watchdog Crash (arg=21), Brownout Hibernate & Missing root.pem"
device: "FMC650"
firmware: "03.01.01.Rev.15"
captured: "2026-10-28 08:43:17 to 09:21:14"
log_file: "02_2026-10-28_0843_settings_mutex_scheduler_watchdog_crash_arg21_and_recovery.txt"
---

# Target 02 — `Settings` Mutex Deadlock, `Scheduler` Watchdog Crash (`arg=21`), Brownout Hibernate & Missing `root.pem`

- **Log File**: [02_2026-10-28_0843_settings_mutex_scheduler_watchdog_crash_arg21_and_recovery.txt](./02_2026-10-28_0843_settings_mutex_scheduler_watchdog_crash_arg21_and_recovery.txt) (renamed from `putty2 (1).log`, 24,244 lines, 807,650 bytes)

---

## 1. Debugging Target & Session Context

This 38-minute trace (`08:43:17` to `09:21:14`) spans **three distinct boot lifecycles** (`Software` reset counter incrementing `4 -> 5 -> 6`) and reveals **four failure mechanisms not seen in earlier logs**:
1. **A New Task Watchdog Crash Signature (`arg=21`, Task 10 `[Scheduler]`)**: Caused by a 221-second deadlock on the `Settings` mutex (`Settings: 221/1800 W:571 T:527 R:571 Tcnt:37 Rcnt:36 F:N`) when live configuration updates (`C:\@cfg\settings.tmp` -> `settings.set`) collide with brownout/ignition-flapping I/O.
2. **Brownout Hibernate & SD Card Park Contention (`Ext:7669 mV` to `8476 mV`)**: Triggers `Error [2] M:pwr_manager_cng_states.c L:60`, `Go to Hibernate State 2`, `[INIT.M]-> Bad Power:5`, and `[BAT.PWR.M]-> Busy, can't execute:eSD_JobRemoveBattery job`.
3. **Missing TLS Root Certificate (`z:\cert\root.pem`)**: When opening Socket 0 (`203.0.113.10:20332`), mbedTLS logs `[MBED.PRNT] Trying to parse z:\cert\root.pem` -> `[MBED.PRNT] Get file size error`.
4. **Full Stabilization once External Supply is Restored to `15.1 V` (`09:14:59` – `09:21:14`)**: Demonstrates immediate recovery of both servers (`SOC0` and `SOC5`) and complete elimination of ignition flapping and watchdog stalls.

---

## 2. Three-Boot Lifecycle Analysis

### Boot Lifecycle 1 (`08:43:17` – `08:54:51`, Lines 1–7725) — `Settings` Mutex Deadlock & `arg=21` Crash
- **Startup State (`08:43:17`)**:
  - `Reset Cause: SoftReset`, `[BATRAM.INFO]` `PowerOn: 1, Software: 4, SD Save Fail Cnt: 0`.
  - Flash `recdb/0` holds 2 records (`File: 5`); SD `sd:recdb/1` holds 5 records (`File: 12`).
- **Brownout & Ignition Storm at Boot (`08:43:18` – `08:45:00`)**:
  - External supply sags to `8,476 mV` (`Ext:8476(12000,20000)`).
  - Power manager fires `[BAT.PWR.M]-> Busy, can't execute:eSD_JobRemoveBattery job` (line 206) and `Error [2] M:pwr_manager_cng_states.c L:60` -> `Go to Hibernate State 2` (lines 722–723).
  - `[F.D.T.F]-> Full can't process 16 job` fires **212 times** during this boot.
- **Repeated Live Configuration Saves (`08:46:40` & `08:50:19`)**:
  - The user applies configuration changes via Configurator while the unit is running:
    ```text
    [2026.10.28 08:46:40]-[LFS]-> M2M_FS_FileOpen:C:\@cfg\settings.tmp, flags:0x102
    [2026.10.28 08:46:41]-[CFG]-> settings backup success: 104a3c02
    ```
- **Missing `z:\cert\root.pem` on Socket 0 Open (`08:48:04`, lines 4954–4961)**:
  ```text
  [2026.10.28 08:48:04]-[SOCKET]-> Set Host Types: 0 <- 0 (IP)
  [2026.10.28 08:48:04]-[MODEM]-> Connecting to 203.0.113.10:20332 by 0 (T:0 S:0)...
  [2026.10.28 08:48:04]-[MBED.PRNT] Trying to parse z:\cert\root.pem
  [2026.10.28 08:48:04]-[MBED.PRNT] Get file size error
  ```
- **`Settings` Mutex Deadlock & Task 10 `[Scheduler]` Watchdog Crash (`08:51:10` – `08:54:51`, lines 6450–7725)**:
  - At `08:51:10`, another settings save is initiated (`settings.tmp` -> `settings.set`).
  - The `Settings` mutex is taken at line `T:527` (`Tcnt:37 Rcnt:36 F:N`) and never released.
  - Task 10 (`[Scheduler]`) blocks waiting for `Settings` at line `W:571`:
    - `08:52:52` (line 7049): `Settings: 96/1800 W:571 T:527 R:571 Tcnt:37 Rcnt:36 F:N` | `Task ID:10 [Scheduler] tmo:45/180`
    - `08:53:52` (line 7384): `Settings: 156/1800 W:571 T:527 R:571 Tcnt:37 Rcnt:36 F:N` | `Task ID:10 [Scheduler] tmo:135/180`
    - `08:54:51` (line 7691): `Settings: 221/1800 W:571 T:527 R:571 Tcnt:37 Rcnt:36 F:N` | `Task ID:10 [Scheduler] tmo:180/180`
  - At `08:54:51` (lines 7723–7725):
    ```text
    [2026.10.28 08:54:51]-[WDG.TASK]-> Task: 10, timeout: 180 s
    [2026.10.28 08:54:51]-[BAT.RAM]-> [CRASH] Data saved: m2m_task_watchdog.c:93 arg=21 ttype=U tid=5, tname: WDG
    [2026.10.28 08:54:51]-[CPU RESET]->CPU reset has been initiated: 21, m2m_task_watchdog.c:93
    ```

### Boot Lifecycle 2 (`08:54:51` – `09:14:59`, Lines 7726–20545) — Severe Brownout (`7.66 V`) & Unclean Reset
- Boots with `Software: 5` and `Periodic info: Up:0h :93 Arg:21 U:5`.
- Connects both `SOC0` (`203.0.113.10:20332`) and `SOC5` (`198.51.100.30:20001`), draining buffered SD (`db:1`) and Flash (`db:0`) records.
- Between `09:11:48` and `09:14:50`, external voltage drops to **7,669 mV** while internal battery is down to **7,132 mV** (`Ext:7669(12000,30000) UBat:7132(8400)`), forcing repeated transitions into `Hibernate State 2` (`Hibernate State Waiting for PowerGood`).
- At `09:13:51`, another configuration write occurs during brownout (`process: 168/1800 F:N`, `REC.WRT: 41/1800 F:N`), culminating in a soft reset at `09:14:59` (`Software: 6`).

### Boot Lifecycle 3 (`09:14:59` – `09:21:14`, Lines 20546–24244) — Clean Recovery at `15.1 V`
- On boot at `09:15:00`, `[T.RECMNG]` flags the unclosed flash record file from the interrupted Boot 2 write:
  ```text
  [2026.10.28 09:15:00]-[T.RECMNG]-> ERROR: m2m_recmng_internal_api.c:rec_file_read:1012
  [2026.10.28 09:15:00]-[T.RECMNG]-> File not finished don't erase
  ```
- At `09:15:22`, the first SIM check transiently returns `+CPIN: NO SIM` (`Error [4] M:modem_init.c L:328` -> `Switch SIM -> 1`), then recovers on the next modem init cycle (`IMSI: 603021090089897`, Djezzy).
- External supply is stabilized at **`15,114 mV` (15.1 V)** (`State:1 [FastCharge] Ext:15114(13200,30000)`).
- Both `SOC0` and `SOC5` open cleanly, drain all remaining flash and SD records, and run until the end of the capture (`09:21:14`) with **0 ignition flips, 0 queue overflows, and 0 mutex stalls**.
