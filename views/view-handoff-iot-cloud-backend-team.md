> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:38:48Z
> **Audience:** External Handoff: IoT Cloud backend team
> ⚠️ For full context, always refer to the Master SRS.

---

### Contract Boundary: IoT Cloud backend team

**What IoT Cloud backend team Owns (External):**
The following requirements are tagged `[EXTERNAL: IoT Cloud backend team]` — they are the responsibility of the IoT Cloud backend team and are NOT delivered by the LUUCIPet collar/base-station system.

**What the LUUCIPet System Owns (In-Scope):**
The interface obligations below are delivered by the LUUCIPet system. The IoT Cloud backend team must design its side to consume these interfaces as specified.

### External-Party Owned Blocks (5 blocks)

#### From: 2.1 Product Functions

- **In scope (our build):**  on-device behavioral classification; collar↔base BLE sync and base↔cloud relay (device-management-layer interface); charging (Base Station + Portable Travel Charging Cradle); CCF breakaway/separation detection and event transport (SRS-FUNC-0001, SRS-FUNC-0002); device-side species-profile persistence (SRS-OPER-0003); device-local home/away determination that gates GNSS power behavior, relying solely on the device-local state machine ([ASSUMPTION: A-0016]).
- **External-party (documented, attributed):**  owner-facing Mobile App alerts/onboarding/CCF guidance/dashboards — **[EXTERNAL: Mobile App team]** (SRS-OPER-0008, SRS-OPER-0009, SRS-OPER-0010); IoT Cloud storage/analytics backend and the cloud-side home/away state machine for owner geofence alerting — **[EXTERNAL: IoT Cloud backend team]** (SRS-OPER-0011). Data transport to the cloud is our in-scope hand-off; cloud storage/analytics and app display are external ([ASSUMPTION: A-0015]).
- **Future-phase (deferred, Phase 2):**  GPS-M variant + cellular positioning — not addressed by any requirement in this SRS.

#### From: 15.1 Base Station Continuous Operation

| **SRS-OPER-0017** | **Device-Local Home/Away State Machine** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) readings from paired base stations in range, without reliance on any cloud-side determination. |
| **Rationale**    | PRD §6.4 states dual home/away state machines exist (device-local and cloud-side), and [ASSUMPTION: A-0016] confirms the device-local state machine is the sole in-scope authority for power gating — notably the Max GNSS smart power gate (SRS-INT-0027, SRS-OPER-0004) — with the cloud-side state machine external ([EXTERNAL: IoT Cloud backend team], SRS-OPER-0011). This requirement establishes the existence and RSSI basis of the device-local mechanism that SRS-INT-0027, SRS-OPER-0004, and SRS-PERF-0007 all depend on but which was not yet issued as its own requirement in any approved section. \| Verification Method: Demonstration \| Cross-References: SRS-INT-0027, SRS-OPER-0004, SRS-PERF-0007, SRS-OPER-0011 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

#### From: 15.1 Base Station Continuous Operation

| **SRS-OPER-0022** | **Device-Local Fallback Authority on Extended Cloud Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the base station has not had successful cloud contact for more than 24 hours, without requiring any additional fallback logic beyond the state machine's ordinary operation. |
| **Rationale**    | PRD §6.4 frames the device-local state machine's role as a ">24 h cloud loss" fallback governing the Max GNSS gate, implying the cloud-side state machine (external, [EXTERNAL: IoT Cloud backend team]) would otherwise have some role during shorter cloud outages. Per [ASSUMPTION: A-0016], however, the device-local state machine is the SOLE in-scope authority for power gating at all times, not only after 24 hours; this requirement makes explicit that no additional in-scope fallback mechanism activates at the 24-hour mark — the device-local state machine's continuous, unconditional operation (SRS-OPER-0017) already satisfies the PRD's fallback framing without requiring separate logic. \| Verification Method: Analysis \| Cross-References: SRS-OPER-0017, SRS-OPER-0011<br><br>## 15.7 Product Service Lifetime Reference |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

#### From: 16.0 Scope Note

- **OTA mechanics** owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004)
- **SBOM per-release production** owned by §5 (SRS-FUNC-0061)
- **Pre-launch vuln-disclosure gate** owned by §8 (SRS-SEC-0006)
- **Tier-2 via OTA no HW mod** owned by §3 (SRS-FUNC-0034, SRS-FUNC-0035)
- **2-year lifetime floor** owned by §15 (SRS-OPER-0023)
- **Cloud-side maintenance** is [EXTERNAL: IoT Cloud backend team]; in-scope interface obligation remains SRS-DATA-0024 (§9)

#### From: Appendix A. Requirements Traceability Matrix (RTM)

| Req-ID | Title | Source Tags | Section | Status | Verification Method |
|---|---|---|---|---|---|
| SRS-REG-0001 | Prohibit medical-classification claims | [PRD §13.6] | §1 | APPROVED | Inspection |
| SRS-REG-0002 | Require regulatory classification review | [PRD §13.6] | §1 | APPROVED | Analysis |
| SRS-OPER-0001 | Require ≥1 Charging-tier base station | [PRD §4.2],[PRD §4.5] | §2 | APPROVED | Inspection |
| SRS-OPER-0002 | Limit base stations to ≤8 | [PRD §4.2],[PRD §4.5] | §2 | APPROVED | Test |
| SRS-OPER-0003 | Persist species assignment across resets | [PRD §4.5],[PRD §7.2] | §2 | APPROVED | Test |
| SRS-OPER-0004 | Prohibit owner config of GNSS power gate | [PRD §4.5] | §2 | APPROVED | Inspection |
| SRS-OPER-0005 | Bound in-box CCF fitment (≥80%) | [PRD §14.2] | §2 | APPROVED | Analysis |
| SRS-OPER-0006 | Default to Standard CCF in-box | [PRD §4.1],[PRD §14.2] | §2 | APPROVED | Inspection |
| SRS-OPER-0007 | Degraded-mode below Wi-Fi bound | [ASSUMPTION: A-0009] | §2 | APPROVED | Test |
| SRS-OPER-0008 | Mobile App post-breakaway alert | [EXTERNAL: Mobile App team] | §2 | APPROVED | Analysis-ext |
| SRS-OPER-0009 | Mobile App species re-onboarding | [EXTERNAL: Mobile App team] | §2 | APPROVED | Analysis-ext |
| SRS-OPER-0010 | Mobile App CCF fitment guidance | [EXTERNAL: Mobile App team] | §2 | APPROVED | Analysis-ext |
| SRS-OPER-0011 | Cloud-side home/away state machine | [EXTERNAL: IoT Cloud backend team] | §2 | APPROVED | Analysis-ext |
| SRS-COMP-0001 | Collar-agnostic base station FW | [PRD §4.3],[PRD §4.5] | §2 | APPROVED | Test |
| SRS-COMP-0002 | Universal CCF-to-device compatibility | [PRD §4.1],[PRD §4.3] | §2 | APPROVED | Test |
| SRS-COMP-0003 | Equivalent classification outputs across variants | [PRD §4.3] | §2 | APPROVED | Analysis |
| SRS-COMP-0004 | Interoperable BLE protocol across variants | [PRD §4.3] | §2 | APPROVED | Test |
| SRS-FUNC-0001 | Detect + persist breakaway ≤5 s | [PRD §10.1.3.6],[A-0015],[A-0018] | §2 | APPROVED | Test |
| SRS-FUNC-0002 | Transport breakaway event to cloud | [PRD §10.1.3.6],[PRD §8.5],[A-0015],[A-0018] | §2 | APPROVED | Test |
| SRS-FUNC-0003 | Preserve + forward breakaway event | [PRD §8.4],[PRD §10.1.3.6],[A-0018] | §2 | APPROVED | Test |
| SRS-FUNC-0004 | Breakaway FP ≤0.1%/wear-day | [ASSUMPTION: A-0018] | §2 | APPROVED | Test |
| SRS-FUNC-0005 | Breakaway detection ≥99% | [ASSUMPTION: A-0018],[PRD §10.1.3.7] | §2 | APPROVED | Test |
| SRS-FUNC-0006 | Wellness Mode as default | [PRD §7.1] | §3 | APPROVED | Demonstration |
| SRS-FUNC-0007 | Insight Mode on demand | [PRD §7.1] | §3 | APPROVED | Demonstration |
| SRS-FUNC-0008 | Insight Mode 50 Hz continuous | [PRD §7.1] | §3 | APPROVED | Test |
| SRS-FUNC-0009 | Insight Mode auto-revert | [PRD §7.3] | §3 | APPROVED | Test |
| SRS-FUNC-0010 | Wellness 15-min confirmation burst | [PRD §7.3] | §3 | APPROVED | Test |
| SRS-FUNC-0011 | Wellness idle ≤4 µA | [PRD §7.3] | §3 | APPROVED | Test |
| SRS-FUNC-0012 | Longevity no samplerate reduction | [PRD §7.10] | §3 | APPROVED | Test |
| SRS-FUNC-0013 | Longevity no accuracy reduction | [PRD §7.10] | §3 | APPROVED | Test |
| SRS-FUNC-0014 | Accel ODR ≥50 Hz | [PRD §7.2] | §3 | APPROVED | Test |
| SRS-FUNC-0015 | No aux sensors Tier-1 | [PRD §7.2] | §3 | APPROVED | Inspection |
| SRS-FUNC-0016 | Unified pipeline across tiers | [PRD §7.2] | §3 | APPROVED | Inspection |
| SRS-FUNC-0017 | Species thresholds at onboarding | [PRD §7.2] | §3 | APPROVED | Test |
| SRS-FUNC-0018 | Tier-1 accuracy ≥85% | [PRD §7.4] | §3 | APPROVED | Test |
| SRS-FUNC-0019 | Tier-1 FP ≤5% | [PRD §7.4] | §3 | APPROVED | Test |
| SRS-FUNC-0020 | Tier-2 accuracy ≥80% | [PRD §7.4] | §3 | APPROVED | Test |
| SRS-FUNC-0021 | Tier-2 FP ≤10% | [PRD §7.4] | §3 | APPROVED | Test |
| SRS-FUNC-0
```

---

### View Coverage
External-party blocks tagged [EXTERNAL: IoT Cloud backend team] plus in-scope interface obligations from LUUCIPet system toward IoT Cloud backend team.
