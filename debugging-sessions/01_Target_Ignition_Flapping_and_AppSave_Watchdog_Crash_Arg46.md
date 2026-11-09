---
title: "Target 01 — Overnight Stability & Ignition-Flapping Induced AppSave Task Watchdog Crash (arg=46)"
device: "FMC650"
firmware: "03.01.01.Rev.15"
captured: "2026-10-28 08:33:23 to 08:37:27"
log_file: "01_2026-10-28_0833_ignition_flapping_appsave_watchdog_crash_arg46.txt"
related_log: "13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt"
---

# Target 01 — Overnight Stability & Ignition-Flapping Induced `AppSave` Task Watchdog Crash (`arg=46`)

- **Primary Log File**: [01_2026-10-28_0833_ignition_flapping_appsave_watchdog_crash_arg46.txt](./01_2026-10-28_0833_ignition_flapping_appsave_watchdog_crash_arg46.txt) (renamed from `putty (1).log`, 4,392 lines, 192,479 bytes)
- **Precursor Log File**: [13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt) (renamed from `SD CARD + SIM.txt`, 2,056 lines, 113,324 bytes)

---

## 1. Debugging Target & Session Context

This session captures two critical engineering milestones on the same FMC650 unit (`IMEI: 860000000000001`):
1. **Proof of 13.25-Hour Uninterrupted Overnight Stability**: Following the crash at the end of [13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt](./13_2026-10-27_1916_battery_brownout_ignition_flapping_appsave_watchdog_crash.txt) (`2026-10-27 19:20:40`), the device booted at `2026/10/27 19:20:40` and ran **continuously for 13 hours, 16 minutes, and 19 seconds** (`Device Uptime: 13:16:19`) with **zero resets** (`Software: 2` unchanged) and **zero SD card write errors** (`SD Save Fail Cnt: 0`).
2. **Exact Reproduction of the `AppSave` Task Watchdog Crash (`arg=46`)**: At `08:34:14`, external voltage drops from nominal `13.2 V+` down to `8,577 mV`, triggering a violent ignition-flapping storm (**950 ignition state changes in 191 seconds**) that saturates the `[F.D.T.F]` job queue (**255 queue-full drops**), locks the `AVLBUF` mutex, stalls Task 0 (`[AppSave]`) for 180 seconds, and forces a watchdog reset (`arg=46, m2m_task_watchdog.c:93`) at `08:37:25`.

---

## 2. Phase-by-Phase Chronological Breakdown

### Phase 1: Healthy Overnight Steady-State (`08:33:23` – `08:34:13`)
- **Live Dual-Server Transmission (`08:33:30` – `08:33:32`, lines 40–118)**:
  - A periodic 120-byte record is built (`[Rec.Build]-> Finish building record, record size: 120 bytes`).
  - Written straight to RAM for both servers (`[LIVE.REC]-> Rec to RAM Srv:0 OK`, `[LIVE.REC]-> Rec to RAM Srv:1 OK`) and persisted to the SD card (`[T.RECMNG]-> Save to db:1 rec size: 120`, file `12`, write offset `15840` -> `15960`, `TotalRecCnt:1`).
  - Sent immediately over **Socket 0** (`203.0.113.10:20332`) and **Socket 5** (`198.51.100.30:20001`), acknowledged with `00000001` on both sockets, and deleted from SD (`Deleted 1 Records Mark:1`, `Deleted 1 Records Mark:2`).
- **60-Second Health Telemetry (`08:33:58` – `08:34:05`, lines 239–366)**:
  - `Startup Time: 2026/10/27 19:20:40`, `Device Uptime: 13:16:19`.
  - `[BATRAM.INFO]`: `PowerOn: 1`, `Software: 2`, `SD Save Fail Cnt: 0`.
  - `[Load.T]`: CPU load `5s:29% 15s:29% 30s:29% 1m:29% 5m:31%` — completely healthy.
  - All 17 mutexes are free (`F:Y`), and all 33 RTOS tasks show `tmo:0/180`.
  - SD card health check (`[SD.API]-> Job Type:7`) verifies `db:sd:recdb`, `db:sd:com1db`, and `db:sd:odosd` in <1 second.

### Phase 2: External Voltage Sag & Ignition-Flapping Storm (`08:34:14` – `08:34:30`)
- At `08:34:14` (line 407), external supply voltage drops to **8.577 V**, while the Power Voltage ignition threshold is configured as `Low: 12000 mV, High: 20000 mV`:
  ```text
  [2026.10.28 08:34:14]-[BAT.POWER.MAN] State:3 [Discharging] Charge:0 [Allowed]Src:1 [CONNECTED]Ext:8577(12000,20000) UBat:8028(8400), Temp:280(-200,600)
  ```
- Because Ignition Source is set to `DIN1 | Power Voltage` (`src:130`), the firmware enters an immediate oscillation loop between `src:128` (Power Voltage comparator forcing ignition `0`) and `src:2` (DIN1 high forcing ignition `1`):
  ```text
  [2026.10.28 08:34:14]-[Ignition]-> New Igniton state: 0, src:128 [D:1 V:0 C:0 M:0 R:0]
  [2026.10.28 08:34:14]-[Odometer]-> FSM Reset
  [2026.10.28 08:34:14]-[Ignition]-> New Igniton state: 1, src:2 [D:1 V:0 C:0 M:0 R:0]
  [2026.10.28 08:34:14]-[Odometer]-> FSM Reset
  ```
- Each flip queues an attribute `7006` write (`[T.RECMNG]-> Start writing attribute 7006 of length 4`) and an eventual record build.
- Within **16 seconds** (`08:34:30`, line 728), the 16-slot asynchronous job queue overflows for the first time:
  ```text
  [2026.10.28 08:34:30]-[F.D.T.F]-> Full can't process 16 job
  ```

### Phase 3: Progressive Watchdog Starvation & Mutex Contention (`08:35:04` – `08:37:25`)

| Timestamp | `[Load.T]` CPU Load (`5s / 1m / 5m`) | `AVLBUF` Mutex State | Task 0 `[AppSave]` Watchdog | Other Stalled Tasks (`[WDG.TASK]`) | Cumulative `[F.D.T.F]` Drops |
|---|---|---|---|---|---:|
| `08:33:59` | `29% / 29% / 31%` | `0/1800 F:Y` | `tmo:0/180` | None (`all 0/180`) | `0` |
| `08:35:04` | `94% / 77% / 47%` | `1/1800 F:Y` | `tmo:45/180` | None | `52` |
| `08:36:25` | `80% / 84% / 78%` | `121/1800 W:0 T:985 R:1049 F:N` | `tmo:90/180` | Tasks `1, 2, 12, 18, 19` at `tmo:45/180` | `149` |
| `08:37:00` | *(Modem timeout)* | Held (`F:N`) | `tmo:135/180` | `[SOCKET]-> Modem not responding` -> `Send ERR: 1` | `204` |
| `08:37:25` | `78% / 83% / 87%` | `189/1800 W:0 T:985 R:1049 F:N` | **`tmo:180/180` (CRASH)** | Tasks `1, 2, 12, 18, 19` at `tmo:135/180`; `SDLog` `90/300` | `255` |

### Phase 4: Crash Dump & Reboot (`08:37:25` – `08:37:27`, lines 4324–4392)
```text
[2026.10.28 08:37:25]-[WDG.TASK]-> Task: 0, timeout: 180 s
[2026.10.28 08:37:25]-[BAT.RAM]-> [CRASH] Data saved: m2m_task_watchdog.c:93 arg=46 ttype=U tid=5, tname: WDG
[2026.10.28 08:37:25]-[CPU RESET]->CPU reset has been initiated: 46, m2m_task_watchdog.c:93
```
- The unit immediately reboots into Bootloader `65.10` / Firmware `03.01.01.Rev.15` at `08:37:26`, increments `[BATRAM.INFO]` `Software` reset counter from `2` to `3`, and recovers `sd:recdb/1` (`First File: 12, Last File: 12, TotalRecCnt: 4`).

---

## 3. Root Cause & Fix

- **Root Cause**: Conflicting ignition inputs (`DIN1 = 1` vs `Power Voltage = 0` at `8.57 V`) evaluated in a tight loop without hardware/software hysteresis between sources.
- **Fix**: Set Ignition Source strictly to `DIN1` (`src:2`) or supply stable `>13.5 V` external power when `Power Voltage` (`src:128`) is enabled.
