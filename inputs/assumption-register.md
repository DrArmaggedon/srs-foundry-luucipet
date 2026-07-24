# Assumption Register — LUUCIPet Wellness Monitor

**Session:** S-luucipet · A-0001…A-0025 consumed · Next free: **A-0026**


| **A-0001** | **Device-enforced BLE protocol/ICD frozen before verification. Referenced in SR...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Device-enforced BLE protocol/ICD frozen before verification. Referenced in SRS-INT-0052 (§10). |
| **Basis** | Engineered default — a single shared protocol avoids per-variant fragmentation. |
| **Risk** | LOW-MEDIUM |

| **A-0002** | **Zone-2 blunt-edge/sharp-edge test methodology under EU GPSR. Specific sharp-e...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Zone-2 blunt-edge/sharp-edge test methodology under EU GPSR. Specific sharp-edge geometry not mandated; methodology-based compliance sufficiency assumed. |
| **Basis** | GPSR Art 6 (RM-0024); toy-safety analog on animal product has no direct mandate. |
| **Risk** | MEDIUM |

| **A-0003** | **CCF thermal-cycling profile per IEC 60068-2-14 Test Na. Referenced in SRS-ENV...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | CCF thermal-cycling profile per IEC 60068-2-14 Test Na. Referenced in SRS-ENV-0003 (§12), SRS-COMP-0027 (§17). |
| **Basis** | RM-0028 confirms 60068-2-14 as appropriate basis. |
| **Risk** | LOW |

| **A-0004** | **"Full-quality GNSS" interpreted as acquisition-based (fix obtained within 90 ...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | "Full-quality GNSS" interpreted as acquisition-based (fix obtained within 90 s using A-GPS) with no PDOP or metres-level position-accuracy bound. Referenced in §10.3 flag. |
| **Basis** | Engineered default — prevents future numeric-accuracy requirement from being silently assumed. |
| **Risk** | LOW |

| **A-0005** | **Device-enclosure chew-resistance: 250 N compressive / ≥30 s penetration.** |
|------------|------------------------------------------------------------------------|
| **Statement** | Device-enclosure chew-resistance: 250 N compressive / ≥30 s penetration. |
| **Basis** | ⚠ SUPERSEDED by A-0007. Reconciliation report #4 recommends merge. Retained for audit. |
| **Risk** | — |

| **A-0006** | **Governing battery cell capacities are §10.4 minimums: Mini ≥120 mAh, Max ≥400...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Governing battery cell capacities are §10.4 minimums: Mini ≥120 mAh, Max ≥400 mAh. §15.3 figures illustrative only. |
| **Basis** | Resolved conflict I-1 (PRD §10.4 vs §15.3). Referenced in §2, §6 (PERF), §11 (HW). |
| **Risk** | LOW-MEDIUM |

| **A-0007** | **Device-enclosure chew-resistance: 250 N compressive force / ≥30 s penetration...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Device-enclosure chew-resistance: 250 N compressive force / ≥30 s penetration. Referenced in §7 (SAFE), §11 (HW), §12 (ENV). |
| **Basis** | User-approved standard default (quality gate — numeric-vagueness resolution #1). |
| **Risk** | MEDIUM |

| **A-0008** | **Base-station LED dimming/nighttime mode: auto-dim below ~50 lux ambient or du...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Base-station LED dimming/nighttime mode: auto-dim below ~50 lux ambient or during owner-set quiet-hours schedule. |
| **Basis** | User-approved (quality gate — numeric-vagueness resolution #2). `should` recommendation, not `shall`. |
| **Risk** | LOW |

| **A-0009** | **Home Wi-Fi reliability bound: ≥−70 dBm RSSI at 2.4 GHz / ≥256 kbps sustained ...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Home Wi-Fi reliability bound: ≥−70 dBm RSSI at 2.4 GHz / ≥256 kbps sustained uplink. Below threshold → Base Station enters ≥30-day offline-buffering degraded mode. Referenced in SRS-OPER-0007 (§2), §4 (CONN), §10 (INT). |
| **Basis** | Engineered numeric floor. |
| **Risk** | MEDIUM |

| **A-0010** | **CCF device-absent socket entrapment: 12 mm probe geometric check. Referenced ...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | CCF device-absent socket entrapment: 12 mm probe geometric check. Referenced in SRS-INT-0042 (§10), SRS-SAFE-0009 (§7). |
| **Basis** | **INDICATIVE.** GPSR foreseeable-hazard duty (RM-0024) supports geometric check; 12 mm probe is engineered default pending regulatory guidance. |
| **Risk** | MEDIUM |

| **A-0011** | **Battery-ingestion risk: Li-Po pouch cell (NOT coin/button cell).** |
|------------|----------------------------------------------------------------|
| **Statement** | Battery-ingestion risk: Li-Po pouch cell (NOT coin/button cell). |
| **Basis** | **CONFIRMED.** Reese's Law / 16 CFR 1263 / UL 4200A apply only to button/coin cells, not pouch/prismatic Li-Po. General ingestion/small-part warning under GPSR/CPSA is correct basis. Referenced in quality gate report #5. |
| **Risk** | LOW-MEDIUM |

| **A-0012** | **CCF assembled-mass constant = 26 g (capsule mass + CCF body mass combined). R...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | CCF assembled-mass constant = 26 g (capsule mass + CCF body mass combined). Referenced in §2.5, §7 (SAFE-0003 — drop-impact energy calculation). |
| **Basis** | Engineered constant derived from CAD mass roll-up. |
| **Risk** | LOW |

| **A-0013** | **EU Battery Regulation (EU) 2023/1542 Art. 11 removability exemption applies t...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | EU Battery Regulation (EU) 2023/1542 Art. 11 removability exemption applies to LUUCIPet collar devices (pouch cell ≠ "portable battery" per Art. 3(1) definition, or IP67 sealing constitutes "designed for use in wet conditions" exemption per Art. 11(3)). Deadline: 18 Feb 2027. Referenced in SRS-REG-0024 (§18). |
| **Basis** | **VOLATILE.** Regulatory interpretation pending formal review. Potential conflict with non-swappable IP67 design if exemption fails. |
| **Risk** | HIGH |

| **A-0014** | **CCF-S feline breakaway force window: 15–20 N. Anchored to ASTM F2056 collar-r...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | CCF-S feline breakaway force window: 15–20 N. Anchored to ASTM F2056 collar-removal test per RM-0030. Referenced in §2.5, §7 (SAFE-0002). |
| **Basis** | Standard-derived; feline-specific hazard profile. |
| **Risk** | MEDIUM |

| **A-0015** | **Cloud-transport (device → Base Station → Device-Management layer) is in-scope...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Cloud-transport (device → Base Station → Device-Management layer) is in-scope. Cloud-side storage, analytics, and application logic are [EXTERNAL: IoT Cloud backend team]. Referenced in §2, §4, §9, §10, §13. |
| **Basis** | Scope boundary per PRD §6.1, §14.1. |
| **Risk** | LOW |

| **A-0016** | **Device-local HOME/AWAY state machine is the sole in-scope authority for GNSS ...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Device-local HOME/AWAY state machine is the sole in-scope authority for GNSS power gating. Cloud-side home/away state machine (for owner geofence alerting) is [EXTERNAL: IoT Cloud backend team]. Referenced in §2, §10, §15. |
| **Basis** | Scope boundary; prevents silent state-machine conflict. |
| **Risk** | MEDIUM |

| **A-0017** | **EU GPSR (EU) 2023/988 design-level strangulation-mitigation framing: Zone-2 F...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | EU GPSR (EU) 2023/988 design-level strangulation-mitigation framing: Zone-2 Fuse Tab is an indicative, risk-reducing measure, not a regulated safety device. Per RM-0031. |
| **Basis** | **INDICATIVE-pending-DVT.** Efficacy for feline SKU not yet confirmed. Referenced in §2, §7. |
| **Risk** | HIGH |

| **A-0018** | **Breakaway detection: FP ≤0.1%/wear-day, true-event detection ≥99%, 5 s commit...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Breakaway detection: FP ≤0.1%/wear-day, true-event detection ≥99%, 5 s commit to NVS, survivability across power loss. Referenced in §2 (FUNC-0001/0002/0003), §7 (SAFE), §9 (DATA), §14 (UX). |
| **Basis** | Engineered numeric targets validated during DVT. |
| **Risk** | MEDIUM |

| **A-0019** | **Collar boot-time ceiling: 3 s (cold power-on / wake-from-reset to classificat...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Collar boot-time ceiling: 3 s (cold power-on / wake-from-reset to classification-ready). Referenced in SRS-PERF-0006 (§6). |
| **Basis** | Engineered default — consistent with comparable BLE sensor platforms. |
| **Risk** | LOW |

| **A-0020** | **CCF-M/L canine breakaway force windows: CCF-M = 20–28 N, CCF-L = 28–40 N. No ...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | CCF-M/L canine breakaway force windows: CCF-M = 20–28 N, CCF-L = 28–40 N. No identifiable ASTM/EN canine collar-release standard. Engineering-derived from mass/force scaling. Referenced in §7 (SAFE-0002/0003), RM-0030. |
| **Basis** | Engineering-derived; no direct standard mandate. |
| **Risk** | HIGH |

| **A-0021** | ***(Reserved — no current reference in migrated project files. Preserved in seq...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | *(Reserved — no current reference in migrated project files. Preserved in sequence for audit continuity.)* |
| **Basis** | — |
| **Risk** | — |

| **A-0022** | **RSSI HOME/AWAY thresholds: HOME→AWAY at −85 dBm (5 consecutive readings, debo...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | RSSI HOME/AWAY thresholds: HOME→AWAY at −85 dBm (5 consecutive readings, debounce 3 s), AWAY→HOME at −80 dBm (3 consecutive readings, debounce 1.5 s). Referenced in SRS-OPER-0018, SRS-OPER-0024 (§15). |
| **Basis** | Engineered by analogy to A-0009 with hysteresis margin. |
| **Risk** | LOW-MEDIUM |

| **A-0023** | **Charging socket self-drainage criteria: 5 mL fill / 15 s drain window / ≤0.2 ...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Charging socket self-drainage criteria: 5 mL fill / 15 s drain window / ≤0.2 mL residual after drain. Referenced in SRS-INT-0036 (§10), SRS-HW-0008 (§11). |
| **Basis** | Engineered by analogy to A-0007 chewing-abrasion precedent. |
| **Risk** | LOW-MEDIUM |

| **A-0024** | **SBOM machine-readable format = SPDX 2.3 or CycloneDX. Anchored in SRS-COMP-00...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | SBOM machine-readable format = SPDX 2.3 or CycloneDX. Anchored in SRS-COMP-0028 (§17). |
| **Basis** | Standard-derived default. EU CRA Annex I + US EO 14028. Tier-1 verified 2026-07. |
| **Risk** | LOW-MEDIUM |

| **A-0025** | **Certification/DoC archival retention = 10 years after last unit placed on mar...** |
|------------|--------------------------------------------------------------------------------|
| **Statement** | Certification/DoC archival retention = 10 years after last unit placed on market (longest-obligation-dominates across all 5 markets: US, EU/EEA, UK, CA, AU/NZ). Anchored in SRS-REG-0043 (§18); resolves D4 MARGINAL. |
| **Basis** | RED Art 10 (10yr), CRA Art 13/31 (10yr/support), FCC §2.938 (2yr), ISED RSS-Gen, ACMA/EESS (5yr). Tier-1 verified 2026-07. |
| **Risk** | LOW-MEDIUM |
