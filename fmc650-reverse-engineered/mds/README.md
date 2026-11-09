# FMC650 Reverse-Engineering & Telematics Reports (`mds/`)

This directory consolidates all **technical analysis documents**, **reverse-engineering process logs**, **save-failure debugging reports**, **vehicle simulation audits**, and **Flespi/Wialon telematics mapping specifications**.

---

## Report Catalog

| Document | Scope & Key Findings |
| :--- | :--- |
| **[`analysis_report.md`](analysis_report.md)** | **Master Reverse-Engineering Report.** Documents the `.xim` firmware decryption, `.cfg` format analysis, `Brand.dll` static XML extraction (`44.81%`), `Configuration.Generator.dll` (`ximgen`) invocation, `PropertyIdCalulator` formula (`id = startId + offsetMultiplier * blockIndex + orderId`), and `IOItem` block expansion achieving **100% (`11,688 / 11,688`) parameter attribution**. |
| **[`cfg_format.md`](cfg_format.md)** | **`.cfg` Container & Text Grammar Specification.** Details the single-member GZip container, fixed 5-key header (`ConfigurationVersion`, `HwVersion`, `Title`, `FmType`, `SpecId`), ascending numeric `id:value;` stream, and the `PID 181334` semicolon continuation rule (`0;10:FMC650DEMO`). |
| **[`xim_decryption.md`](xim_decryption.md)** | **`.xim` Firmware Encryption Specification.** Documents the `TLTF` binary header layout, obfuscated vendor password recovery (`b[i] ^= (i & 0xFF) ^ 0xAA`), `PBKDF2-HMAC-SHA1` (`1000` iterations, 32-byte AES-256 key), `AES-256-CBC` decryption, single-member GZip decompression, and 128-byte RSA-2048 signature tail. |
| **[`FMC650_CFG_Save_Failure_Debugging_Report.md`](FMC650_CFG_Save_Failure_Debugging_Report.md)** | **Root-Cause Debugging Report (`"Failed to be saved on device"`).** Identifies and resolves the exact failure modes when saving generated `.cfg` files to physical FMC650 units: (1) `17000..17690` (`Req ID` requires 8 hex chars `'00000000'`) & `17002..17692` (`Payload` requires 16 hex chars `'0000000000000000'`), (2) `PID 47500` (`TimestampCollection` only allows `'1'`, `'2'`, `'3'`, never `'0'`), (3) preservation of passive J1939 `CAN0..CAN23` (`47000..90030`) and Dual-Server Wialon + Flespi (`2004..2010`), and (4) `4.43.1.0` vs `4.41.0.0` firmware compatibility. |
| **[`FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md`](FMC650_FLEET_P2_PRODUCTION_v1.2_Flespi_Wialon_Mapping.md)** | **End-to-End PID → Codec 8E AVL ID → Flespi → Wialon Mapping.** Maps all active parameters in `P2_PRODUCTION_v1.2` across Configuration PIDs, Teltonika Codec 8 Extended AVL IDs, Flespi telemetry keys, and Wialon `TR84_Flespi_Test.wlp` sensor definitions (`146` sensors: `88` hardware + `58` `fleet_*` weight plugin). |
| **[`FMC650_FLEET_P2_PRODUCTION_v1.2_SITRAK_Simulation_Report.md`](FMC650_FLEET_P2_PRODUCTION_v1.2_SITRAK_Simulation_Report.md)** | **SITRAK C7H + WABCO TEBS-E Operational Simulation Report.** Simulates packet generation, dual-server queue behavior (`1000=120s`, `1001=5s`, `1002=1` FIFO), J1939 FMS/Manual CAN reception, and TrailerCAN weight telemetry under regional highway/cellular conditions. |
| **[`re_agent_process_technical_resume.md`](re_agent_process_technical_resume.md)** | **Technical Resume of the RE Pipeline.** Condensed engineering reference of the verification chain, byte-exact reproduction steps, and C# decompilation findings. |
| **[`re_agent_process.md`](re_agent_process.md)** | **Reverse-Engineering Audit Trail.** Chronological log of the investigation steps, hypotheses tested, and verification checkpoints. |

---

## Cross-References

- **Executable Tools:** [`../tools/README.md`](../tools/README.md)
- **Compiled `.cfg` Profiles:** [`../cfgs/README.md`](../cfgs/README.md)
- **Extracted Schemas & Compiler XML:** [`../re/README.md`](../re/README.md)
