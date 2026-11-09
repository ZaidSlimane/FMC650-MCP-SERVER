---
title: "Target 04 — Primary Server TCP/TLS Timeout, Shared Modem Blocking, Function Watchdog Escalation & Full Modem Reset"
device: "FMC650"
firmware: "03.01.01.Rev.15"
captured: "2026-10-31 15:02:33 to 15:16:12"
log_file: "04_2026-10-31_1502_primary_server_tcp_tls_timeout_and_full_modem_reset.txt"
---

# Target 04 — Primary Server TCP/TLS Timeout, Shared Modem Blocking, Function Watchdog Escalation & Full Modem Reset (`app_data_sending.c:2304`)

- **Log File**: [04_2026-10-31_1502_primary_server_tcp_tls_timeout_and_full_modem_reset.txt](./04_2026-10-31_1502_primary_server_tcp_tls_timeout_and_full_modem_reset.txt) (renamed from `TLS TEST (4).txt`, 4,285 lines, 222,355 bytes)

---

## 1. Debugging Target & Session Context

Captured on **2026-10-31 (`15:02:33` – `15:16:12`, 13 minutes 39 seconds)**, this session tests a new network and server topology:
- **SIM / Operator Changed**: Switched from Djezzy (`60302`) to **m2m.sim2 the region (`IMSI: 603019072318087`, Operator `60301`, LTE Band 3, EARFCN `1680`)**.
- **Primary Server (`Server 1`, `SOC0`) Changed**: Configured to **`203.0.113.20:5027`** (unreachable / dropping TCP SYN packets from this APN).
- **Backup Server (`Server 2`, `SOC5`)**: Configured to Flespi **`198.51.100.130:20001`** (connected and actively acknowledging live packets every 30 seconds).
- **MicroSD Card Removed (`FATRES: 3`)**: All records are stored in internal NOR flash (`recdb/0`), while `SD Save Fail Cnt` climbs from **`1898`** to **`1963`**, and `[Per.T]` reveals that the last soft reset at `13:20:06` was caused by **`flash_api.c:590 Arg:27 U:18` (Task 18 `[FlashJob]`)**.

---

## 2. Key Diagnostic Findings in This Session

### Finding 1: Asymmetric Backlog (`Filter:1` vs `Filter:2`)
Because Server 2 (`SOC5`, `198.51.100.130:20001`) is online and receiving live 114-byte records via RAM (`[LIVE.REC]-> Rec to RAM Srv:1 OK`) while Server 1 (`SOC0`, `203.0.113.20:5027`) is offline on a 720-second retry backoff timer (`1 Time until data sending 714` down to `0`), the internal flash database `recdb/0` accumulates records **only for Server 1**:
```text
[2026.10.31 15:02:41]-[T.RECMNG]-> CheckRec Filter:1 Order:2 Count:148 db:0
[2026.10.31 15:02:41]-[T.RECMNG]-> CheckRec Filter:2 Order:2 Count:0 db:0
```
- By `15:14:39`, `Filter:1` has grown from **148 records** to **171 records** waiting for `203.0.113.20:5027`, while `Filter:2` remains at **0 records** (100% real-time delivery to Flespi).

### Finding 2: Climbing `SD Save Fail Cnt` (`1898 -> 1963`) & Prior `flash_api.c:590` Reset
Every 60 seconds, the periodic health dump reports:
```text
[2026.10.31 15:02:40]-[Per.T]-> Periodic info: Up:1h flash_api.c:590 Arg:27 U:18
[2026.10.31 15:02:40]-[BATRAM.INFO]-> ... Software: 5 ... SD Save Fail Cnt: 1898
[2026.10.31 15:02:47]-[SD.API]-> SD card mount not OK. FATRES: 3
```
- Every time `[T.RECMNG]-> Save to db:0 rec size: 114` executes (roughly every 30 seconds plus movement events), `SD Save Fail Cnt` increments by `3` (`1898 -> 1901 -> 1907 -> ... -> 1963`).
- Furthermore, `Up:1h flash_api.c:590 Arg:27 U:18` proves that continuous fallback writes to internal NOR flash (`recdb/0`) previously caused Task 18 (`[FlashJob]`) to trigger a software reset at `flash_api.c` line `590` (`Arg:27`).

### Finding 3: Function Watchdog `WD.FUNC counter:2` Exceeding its 930-Second Limit
While Server 1 waits on its 12-minute (`720 s`) reconnect timer, its Function Watchdog counter (`counter:2`, `Limit:930`) continues ticking upward every second without being reset:
- `15:02:40` (line 84): `[WD.FUNC]-> counter:2, State:1 Val:1643 Limit:930`
- `15:14:40` (line 3684): `[WD.FUNC]-> counter:2, State:1 Val:2363 Limit:930`
- `15:16:00` (line 4030): `[WD.FUNC]-> counter:2, State:1 Val:2443 Limit:930`
- Meanwhile, Server 2's Function Watchdog (`counter:3`, `Limit:930`) resets to `1..29` every 30 seconds each time Flespi acknowledges a packet.

### Finding 4: Shared Modem AT Channel Blocking Drops the Healthy Backup Socket (`SOC5`) & Triggers False `CODEC12 ERROR`
When Server 1's retry timer reaches `0` at `15:14:39` (line 3668), `TID_TCP_SEND_1` attempts to open Socket 0 to `203.0.113.20:5027`:

| Timestamp | Line | Event & Firmware Log Signature | Impact |
|---|---:|---|---|
| `15:14:39` | `3668` | `[APP.SND.D]-> Task Id:[0] Name:[TID_TCP_SEND_1] Start Reason:[Normal execution]` | Server 1 retry begins (`Filter:1 Count:171`). |
| `15:14:41` | `3787` | `[SOC5.TX]` sends 129-byte live packet (`1 rec`) to Flespi (`198.51.100.130:20001`). | `SOC5` starts its 30-second `Server Response TMO` timer. |
| `15:14:42` | `3805` | `AT+CIPSTART=0,"TCP","203.0.113.20",5027` issued on shared modem AT channel. | **Modem AT channel blocks for 36 seconds** waiting for TCP SYN-ACK from `203.0.113.20`. |
| `15:15:12` | `3874` | `[APP.SND.D]-> Server Response TMO` -> `[MODEM]-> Closing socket 5, caller: 2440` | Because `AT+CIPSTART=0` is blocking the modem, `SOC5` cannot read Flespi's ACK within 30 s and tears down the healthy backup link! |
| `15:15:18` | `3901` | Modem finally outputs `0,CONNECT FAIL` + queued `+CIPRXGET: 1,5` (`SOC5.RX:[00000001]`). | Late arrival of `00000001` during `SOC5` teardown is routed to `[D.P.TCP]`, logging: `[D.P.TCP]-> CODEC12 ERROR in state 0, ZEROES MISSING`. |
| `15:15:18` | `3914` | `[MODEM]-> DNS 203.0.113.20 Resolving failed` -> `Error [1] M:app_data_sending.c L:1275` | Note: Firmware logs `"DNS <host> Resolving failed"` on any `CONNECT FAIL`, even when `<host>` is a literal IPv4 address (`203.0.113.20`). |
| `15:15:20` | `3934` | 2nd retry: `AT+CIPSTART=0,"TCP","203.0.113.20",5027` -> fails at `15:15:58` (`0,CONNECT FAIL`). | Total link-open execution time exceeds 60 seconds. |
| `15:16:00` | `4009` | `[APP.SND.D]-> Link open executin over a minute - exit` -> `WRN: Data Link cannot be Established!` | Server 1 connection sequence aborts. |
| `15:16:10` | `4230` | `[APP.SND.D]-> Can't Establish communication with GPRS on - Full Modem reset` -> `Error [12] M:app_data_sending.c L:2304` | Because `WD.FUNC counter:2` (`2443`) > `Limit:930`, the firmware resets `counter:2` to `1`, detaches GPRS (`AT+CGACT=0`, `AT+CIPSHUT`), and powers down the entire modem (`AT+CFUN=0`, `MODEM OFF, caller 3536`). |

---

## 3. Root Cause & Remediation

1. **Unreachable Primary Server IP/Port (`203.0.113.20:5027`)**:
   - The TCP SYN packets to `203.0.113.20:5027` receive no response (firewall drop or unroutable destination from the m2m.sim2 network), causing two consecutive 36–38 s `AT+CIPSTART` timeouts.
2. **Collateral Damage to Backup Server (`SOC5`)**:
   - In the FMC650 firmware, `WD.FUNC counter:2` (Primary Server watchdog) triggers a **Full Modem Reset (`app_data_sending.c:2304`)** whenever Primary Server fails to connect after `930 s`, even if Backup Server (`SOC5`) is actively transferring data.
   - **Fix**: Never leave an unreachable IP/port configured as **Primary Server (Server 1)**. Always place the reachable production endpoint (e.g., Flespi `198.51.100.130:20001`) in **Primary Server (`PID 2004` / `PID 2006`)**, or ensure `203.0.113.20:5027` is open and reachable from the SIM's APN.
