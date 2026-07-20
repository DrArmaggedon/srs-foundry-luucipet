> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

CAT: **PERF** | Maps to: PRD §12.1, supporting §10.4, §15.6
*(Drafter-authored; §6 v3 — 8 blocks, SRS-PERF-0001–0008.)*

## 6.1 Battery-Life Performance

**SRS-PERF-0001** | Mini Variant Battery-Life Conformance | The system's Mini variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.1], [PRD §10.4], [CR-0002], [PRD §15.6] | VM: Analysis | XR: SRS-FUNC-0012, SRS-FUNC-0013

**SRS-PERF-0002** | Max Variant Battery-Life Conformance | The system's Max variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval settings. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.1], [PRD §10.4], [CR-0002], [PRD §15.6] | VM: Analysis | XR: SRS-FUNC-0012, SRS-FUNC-0013

## 6.2 Classification & Data-Path Latency

**SRS-PERF-0003** | Classification Latency Ceiling | The system **shall** produce a classification result within 2 seconds of the triggering motion event. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.1] | VM: Test | XR: SRS-FUNC-0016

**SRS-PERF-0004** | Base Station Cloud-Upload Latency Ceiling | The base station **shall** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §12.1] | VM: Test | XR: SRS-CONN-0014, SRS-CONN-0015

## 6.3 Location & Startup Timing (Max Variant / System)

**SRS-PERF-0005** | GNSS Time-to-First-Fix Ceiling (Warm, A-GPS) | On the Max product variant, the system **shall** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §12.1] | VM: Test

## 6.4 Startup & Physical-Interaction Timing

**SRS-PERF-0006** | Collar Boot-Time Ceiling | The collar-mounted device **shall** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §12.1], [ASSUMPTION: A-0019] | VM: Test | XR: SRS-FUNC-0056

**SRS-PERF-0007** | Home/Away Status Update Latency Ceiling | The system **shall** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.1] | VM: Test | XR: SRS-CONN-0004, SRS-CONN-0005

**SRS-PERF-0008** | CCF Twist-Lock Engagement Time Ceiling | The system **shall** allow the Twist-Lock mechanism to be engaged within 5 seconds. | Priority: LOW | Stability: STABLE | Source: [PRD §12.1] | VM: Test

---

### SRS-ID Inventory (§6 v1 — COMPLETE)
- **8 blocks, SRS-PERF-0001 … SRS-PERF-0008.** All in-scope.
- Next free PERF ID = **SRS-PERF-0009**.
