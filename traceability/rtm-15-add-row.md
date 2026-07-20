> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# [S-luucipet] RTM §15 ADD-ROW Report

**Date:** 2026-07-18 | **Mode:** ADD-ROWS | **Section:** §15 Operational Requirements
**Source:** §15 Draft v3 (SRS-OPER-0012–0024, 13 blocks) | **Intra-Conflict:** CR-0025 CLEAN (no defect)

## New RTM Rows — §15

| RTM Row # | SRS ID | SRS Requirement Summary | PRD Source(s) | Parent Req(s) | Notes |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 284 | SRS-OPER-0012 | Base Station Continuous Operational Posture | [PRD §11.7] | SRS-RELI-0003 | in-scope; mains-powered always-on |
| 285 | SRS-OPER-0013 | AC Power Adapter Inclusion | [PRD §11.7] | — | in-scope; included accessory |
| 286 | SRS-OPER-0014 | Charging-Tier Base Station LED Inventory | [PRD §11.6], [PRD §4.2] | SRS-OPER-0015, SRS-UX-0016 | in-scope; 3-LED charging tier |
| 287 | SRS-OPER-0015 | Relay-Tier Base Station LED Inventory | [PRD §11.6], [PRD §4.2] | SRS-OPER-0014, SRS-UX-0016 | in-scope; 2-LED relay tier |
| 288 | SRS-OPER-0016 | Multi-Base Household Geo-Fence Mesh Participation | [PRD §4.2], [PRD §5.3] | SRS-INT-0054, SRS-CONN-0019 | in-scope; mesh sighting reports |
| 289 | SRS-OPER-0017 | Device-Local Home/Away State Machine | [PRD §6.4], [PRD §4.1], [A-0016] | SRS-INT-0027, SRS-OPER-0004, SRS-PERF-0007, SRS-OPER-0011 | in-scope; RSSI-based local authority |
| 290 | SRS-OPER-0018 | Device-Local Home-to-Away RSSI Transition Threshold | [PRD §6.4], [PRD §4.1], [A-0022] | SRS-OPER-0017, SRS-OPER-0024 | in-scope; −85 dBm / 5-reading debounce |
| 291 | SRS-OPER-0019 | Wellness-Mode Deep-Sleep Idle State | [PRD §15.2], [PRD §7.3] | SRS-FUNC-0011, SRS-FUNC-0010 | in-scope; deepest-sleep policy |
| 292 | SRS-OPER-0020 | GNSS Fix-Interval Change Application Timing | [PRD §15.5] | SRS-INT-0023, SRS-INT-0024 | in-scope; apply within next cycle |
| 293 | SRS-OPER-0021 | Battery Cell Cycle-Life Validation Basis | [PRD §15.6] | SRS-PERF-0001, SRS-PERF-0002 | in-scope; ≥50-cycle precondition, VM: Inspection |
| 294 | SRS-OPER-0022 | Device-Local Fallback Authority on Extended Cloud Loss | [PRD §6.4] | SRS-OPER-0017, SRS-OPER-0011 | in-scope; no extra fallback logic |
| 295 | SRS-OPER-0023 | Expected Product Service Lifetime Reference Figure | [PRD — ABSENT] | SRS-RELI-0001 | in-scope; 2-year floor reference |
| 296 | SRS-OPER-0024 | Device-Local Away-to-Home RSSI Hysteresis Threshold | [PRD §6.4], [PRD §4.1], [A-0022] | SRS-OPER-0017, SRS-OPER-0018 | in-scope; −80 dBm / 3-reading hysteresis |

## Row-Count Reconciliation

| Metric | Count |
| :-- | :-- |
| Starting total (before §15) | 283 |
| Part A (§§1–4) | 89 |
| Part B (§§5–14) | 194 |
| §15 new rows added | 13 |
| **Ending total** | **296** |

## Orphans / Unmapped

**None detected.** All 13 SRS-OPER requirements trace to at least one PRD paragraph or assumption.

## Cross-Section Candidates (deferred)
- C-§15-a: SRS-OPER-0018/0024 (RSSI thresholds) ↔ §10 SRS-INT-0027 / §2 SRS-OPER-0004
- C-§15-b: SRS-OPER-0019 (deep-sleep idle) ↔ §3 SRS-FUNC-0011 (≤4 µA)
- C-§15-c: SRS-OPER-0021 (≥50-cycle validation) ↔ §6 SRS-PERF-0001/0002
- C-§15-d: SRS-OPER-0023 (2-yr lifetime) ↔ §13 SRS-RELI-0001
