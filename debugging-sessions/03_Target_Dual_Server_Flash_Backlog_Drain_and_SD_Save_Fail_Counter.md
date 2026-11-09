---
title: "Target 03 — High-Throughput Dual-Server Flash Backlog Drain & SD Save Failure Counter (arg=53)"
device: "FMC650"
firmware: "03.01.01.Rev.15"
captured: "2026-10-28 12:24:24 to 12:25:51"
log_file: "03_2026-10-28_1224_dual_server_flash_backlog_drain_arg53.txt"
---

# Target 03 — High-Throughput Dual-Server Flash Backlog Drain & SD Save Failure Counter (`arg=53`)

- **Log File**: [03_2026-10-28_1224_dual_server_flash_backlog_drain_arg53.txt](./03_2026-10-28_1224_dual_server_flash_backlog_drain_arg53.txt) (renamed from `log3.txt`, 1,654 lines, 170,549 bytes)

---

## 1. Debugging Target & Session Context

Captured on **2026-10-28 (`12:24:24` – `12:25:51`, 87 seconds)** at `Device Uptime: 0:4:39` (`Startup Time: 2026/10/28 12:19:45`), this session provides a clean reference trace of **continuous dual-server backlog draining from internal NOR flash (`recdb/0`)** while also revealing two diagnostic markers in `[BATRAM.INFO]`:
1. **First Appearance of Non-Zero `SD Save Fail Cnt: 190`**: Between `09:21` and `12:24` on Oct 28, the MicroSD card was removed or became inaccessible while SD logging was still expected, causing **190 record writes to fail on SD and fall back to internal NOR flash (`db:0`)**.
2. **Prior Watchdog Reset Signature `Arg:53`**: `[Per.T]-> Periodic info: Up:0h :93 Arg:53 U:5` (`Reset Cause: SoftReset`, `Software: 6`) shows that the reboot at `12:19:45` was triggered by `m2m_task_watchdog.c:93` with `Arg:53` from Task `5` (`[WDG]`).

---

## 2. Telemetry & Storage State Snapshot (`12:24:24` – `12:24:31`, Lines 1–133)

| Metric / Subsystem | Value in `03_2026-10-28_1224_...txt` | Technical Interpretation |
|---|---|---|
| **Startup Time / Uptime** | `2026/10/28 12:19:45` / `0:4:39` | Booted 4 min 39 s before log capture started. |
| **Reset Counters (`[BATRAM.INFO]`)** | `PowerOn: 1, Software: 6, SD Save Fail Cnt: 190` | 190 SD write failures recorded in battery-backed RAM. |
| **Previous Crash Marker** | `Up:0h :93 Arg:53 U:5` | `m2m_task_watchdog.c:93` (`arg=53`, user task ID `5 [WDG]`). |
| **Power & Ignition** | `State:1 [FastCharge] Ext:14949(13200,30000) UBat:8425(8400)` | Stable `14.95 V` external supply; zero ignition flapping. |
| **CPU Load (`[Load.T]`)** | `5s:35% 15s:40% 30s:38% 1m:39% 5m:36%` | Moderate, healthy load during continuous dual-socket TCP draining. |
| **Mutex & Task Watchdogs** | All 17 mutexes `F:Y`; all 33 tasks `tmo:0/180` | Zero contention (`REC.WRT` `Tcnt:528 Rcnt:528 F:Y`). |

---

## 3. Mechanics of Dual-Server Interleaved Backlog Draining (`recdb/0`)

Throughout the 87-second capture, the FMC650 drains records stored in internal NOR flash (`db:0`, `File: 8`, `RecInFile: 256`, `Read Offset: 30720` moving backwards in **Newest-First `Order:2`**) simultaneously to **two independent servers**:
- **Server 1 (Primary — `SOC0`)**: `203.0.113.10:20332` (`Filter:1`, `Mark:1`)
- **Server 2 (Backup/Duplicate — `SOC5`)**: `198.51.100.130:20001` (`Filter:2`, `Mark:2`)

### Step-by-Step Cycle of a Dual-Server Batch Drain (Every ~3 Seconds)

1. **Batch Load for Server 2 (`Filter:2`, `Order:2`)**:
   ```text
   [2026.10.28 12:24:25]-[T.RECMNG]-> LoadRec db:0 Order:2 Count:7 Filter:2 FirstF:5 LastF:9 R_Off:30720 W_Off:27600
   [2026.10.28 12:24:25]-[T.RECMNG]-> Loaded 7 records from file 8 (db:0).
   ```
   - Packs **7 records × 120 bytes = 840 bytes** of payload into an **855-byte Codec 8E TCP packet** (`00000000 0000034F 8E 07 ... 07 <CRC16>`).
   - Transmits on `SOC5.TX` (`[DATA]-> Data Packet Send SUCCESS!`, `198.51.100.130:20001`).
2. **Batch Load for Server 1 (`Filter:1`, `Order:2`)**:
   ```text
   [2026.10.28 12:24:26]-[T.RECMNG]-> LoadRec db:0 Order:2 Count:7 Filter:1 FirstF:5 LastF:9 R_Off:30720 W_Off:27600
   [2026.10.28 12:24:26]-[T.RECMNG]-> Loaded 7 records from file 8 (db:0).
   ```
   - Transmits the corresponding 855-byte packet on `SOC0.TX` (`203.0.113.10:20332`).
3. **TCP-Layer (`AT+CIPACK`) & Application-Layer (`00000007`) Verification**:
   - Polls `AT+CIPACK=5` and `AT+CIPACK=0` to verify all 855 bytes were ACKed by the remote TCP stacks.
   - Reads the 4-byte Codec 8E response (`SOC5.RX:[00000007]`, `SOC0.RX:[00000007]`).
4. **Independent Bitmask Deletion (`Mark:2` and `Mark:1`)**:
   ```text
   [2026.10.28 12:24:27]-[T.RECMNG]-> Deleted 7 Records Mark:2
   [2026.10.28 12:24:27]-[T.RECMNG]-> [recdb/0] Status:0, First File:5, Last File:9, Write Offset:27600, Read Offset:30720, TotalRecCnt:537
   ...
   [2026.10.28 12:24:29]-[T.RECMNG]-> Deleted 7 Records Mark:1
   [2026.10.28 12:24:29]-[T.RECMNG]-> [recdb/0] Status:0, First File:5, Last File:9, Write Offset:27600, Read Offset:30720, TotalRecCnt:530
   ```
   - Notice that `TotalRecCnt` only decrements (`537 -> 530`) when **the second server (`Mark:1`)** also acknowledges the 7-record batch, proving that physical record reclamation in `recdb/0` waits until **both** servers have confirmed delivery.

### Throughput Summary Across the 87-Second Window
- **Total 7-Record Batches Sent & ACKed**: **58 batches** (29 on `SOC0` + 29 on `SOC5` = **406 record deliveries**).
- **Net Backlog Reduction**: `TotalRecCnt` drops from **`543`** (at `12:24:24`) to **`343`** (at `12:25:50`) — a net drain rate of **200 dual-acknowledged records (~2.3 records/sec per server)** while simultaneously recording and appending new live records every 30 seconds (`Write Offset: 27600 -> 27960`).
- **Packet Error Rate**: **0%** (zero timeouts, zero retransmissions).
