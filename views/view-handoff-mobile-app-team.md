> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:38:48Z
> **Audience:** External Handoff: Mobile App team
> ⚠️ For full context, always refer to the Master SRS.

---

### Contract Boundary: Mobile App team

**What Mobile App team Owns (External):**
The following requirements are tagged `[EXTERNAL: Mobile App team]` — they are the responsibility of the Mobile App team and are NOT delivered by the LUUCIPet collar/base-station system.

**What the LUUCIPet System Owns (In-Scope):**
The interface obligations below are delivered by the LUUCIPet system. The Mobile App team must design its side to consume these interfaces as specified.

### External-Party Owned Blocks (9 blocks)

#### From: 2.1 Product Functions

- **In scope (our build):**  on-device behavioral classification; collar↔base BLE sync and base↔cloud relay (device-management-layer interface); charging (Base Station + Portable Travel Charging Cradle); CCF breakaway/separation detection and event transport (SRS-FUNC-0001, SRS-FUNC-0002); device-side species-profile persistence (SRS-OPER-0003); device-local home/away determination that gates GNSS power behavior, relying solely on the device-local state machine ([ASSUMPTION: A-0016]).
- **External-party (documented, attributed):**  owner-facing Mobile App alerts/onboarding/CCF guidance/dashboards — **[EXTERNAL: Mobile App team]** (SRS-OPER-0008, SRS-OPER-0009, SRS-OPER-0010); IoT Cloud storage/analytics backend and the cloud-side home/away state machine for owner geofence alerting — **[EXTERNAL: IoT Cloud backend team]** (SRS-OPER-0011). Data transport to the cloud is our in-scope hand-off; cloud storage/analytics and app display are external ([ASSUMPTION: A-0015]).
- **Future-phase (deferred, Phase 2):**  GPS-M variant + cellular positioning — not addressed by any requirement in this SRS.

#### From: 2.3 User Characteristics / Personas

The system is designed around six user personas, described here as user context only; owner-facing app features are captured as attributed [EXTERNAL: Mobile App team] requirements (see §2.4), not derived directly from these personas. [PRD §3]

#### From: 3.7 Configurable Alert Thresholds (Scratching & Shaking) |

### SRS-ID inventory (§3 v1)
**In-scope (35):** SRS-FUNC-0006 … SRS-FUNC-0040.
**External (2):** SRS-FUNC-0041, SRS-FUNC-0042 ([EXTERNAL: Mobile App team]).
**Total: 37 blocks.** Next free FUNC ID = SRS-FUNC-0043. |

#### From: §14 Usability Requirements

> The companion app is delivered by the Mobile App team \[EXTERNAL: Mobile App team]. The requirements in this subsection specify the device-side and base-station-side interface obligations that enable the app's user-facing features. These are in-scope for our delivery.

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

#### From: Appendix A. Requirements Traceability Matrix (RTM)

| Req-ID | Title | Source Tags | Section | Status | Linked Standards | Conflict IDs | Feasibility Score (D1–D5) | Verification Method | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SRS-FUNC-0043 | OTA Capability Mandatory on All Collar Variants | [PRD §9.1] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref FUNC-0034 |
| SRS-FUNC-0044 | OTA Capability Mandatory on All Base Station Tiers | [PRD §9.1] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref FUNC-0043 |
| SRS-FUNC-0045 | Cloud-to-Base OTA Transport Protocol (TLS 1.3) | [PRD §9.2],[PRD §6.5],[PRD §11.2] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | CR-0005 | PASS/PASS/PASS/PASS/PASS | Test | in-scope; TLS 1.3 per CR-0005; xref CONN-0014 |
| SRS-FUNC-0046 | Base Station Staging of Collar OTA Images | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref FUNC-0047 |
| SRS-FUNC-0047 | Base-to-Collar OTA Image Delivery Over Secured BLE Link | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; xref CONN-0009, SEC-0001, SEC-0002 |
| SRS-FUNC-0048 | Base Station Self-OTA Without User Action | [PRD §11.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-FUNC-0049 | Collar OTA Install Restricted to Charging-Cradle-Docked State | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0050 | Docked-Install Gate Shall Not Be Remotely Bypassable | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0051 | Minimum Battery Reserve Before OTA Install (≥10% SoC) | [PRD §9.2],[PRD §10.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0052 | Minimum OTA Image Signature Strength (≥256-bit ECDSA/RSA-2048) | [PRD §9.3] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-FUNC-0053 | OTA Image Signature Verification Before Commit | [PRD §9.3] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0054 | Anti-Rollback via Monotonic Version Counter | [PRD §9.3] | §5 | APPROVED | EU CRA 2024/2847 (RM-0021) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0055 | Atomic OTA Installation | [PRD §9.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0056 | Dual-Bank Auto-Revert on Boot Failure | [PRD §9.4],[PRD §11.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0057 | No Unrecoverable State on Power/Connection Loss During Install | [PRD §9.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-FUNC-0058 | Device-Side OTA Update State Reporting | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0059 | App Notification of Available OTA Update | [PRD §9.5],[EXTERNAL: Mobile App team] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-FUNC-0060 | App Display of OTA Update State | [PRD §9.5],[EXTERNAL: Mobile App team] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-FUNC-0061 | SBOM Production Per OTA Release | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; lifetime SBOM → §16 |
| SRS-FUNC-0062 | Tier-2 Classifier Delivery Restricted to Embedded OTA Components | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-PERF-0001 | Mini Variant Battery-Life Conformance | [PRD §12.1],[PRD §10.4],[CR-0002],[PRD §15.6] | §6 | APPROVED | — | CR-0002 | PASS/PASS/PASS/PAS
```

#### From: Appendix A. Requirements Traceability Matrix (RTM)

| Req-ID | Title | Source Tags | Section | Status | Linked Standards | Conflict IDs | Feasibility Score (D1–D5) | Verification Method | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SRS-FUNC-0043 | OTA Capability Mandatory on All Collar Variants | [PRD §9.1] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref FUNC-0034 |
| SRS-FUNC-0044 | OTA Capability Mandatory on All Base Station Tiers | [PRD §9.1] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref FUNC-0043 |
| SRS-FUNC-0045 | Cloud-to-Base OTA Transport Protocol (TLS 1.3) | [PRD §9.2],[PRD §6.5],[PRD §11.2] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | CR-0005 | PASS/PASS/PASS/PASS/PASS | Test | in-scope; TLS 1.3 per CR-0005; xref CONN-0014 |
| SRS-FUNC-0046 | Base Station Staging of Collar OTA Images | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref FUNC-0047 |
| SRS-FUNC-0047 | Base-to-Collar OTA Image Delivery Over Secured BLE Link | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; xref CONN-0009, SEC-0001, SEC-0002 |
| SRS-FUNC-0048 | Base Station Self-OTA Without User Action | [PRD §11.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-FUNC-0049 | Collar OTA Install Restricted to Charging-Cradle-Docked State | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0050 | Docked-Install Gate Shall Not Be Remotely Bypassable | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0051 | Minimum Battery Reserve Before OTA Install (≥10% SoC) | [PRD §9.2],[PRD §10.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0052 | Minimum OTA Image Signature Strength (≥256-bit ECDSA/RSA-2048) | [PRD §9.3] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-FUNC-0053 | OTA Image Signature Verification Before Commit | [PRD §9.3] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0054 | Anti-Rollback via Monotonic Version Counter | [PRD §9.3] | §5 | APPROVED | EU CRA 2024/2847 (RM-0021) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0055 | Atomic OTA Installation | [PRD §9.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0056 | Dual-Bank Auto-Revert on Boot Failure | [PRD §9.4],[PRD §11.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0057 | No Unrecoverable State on Power/Connection Loss During Install | [PRD §9.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-FUNC-0058 | Device-Side OTA Update State Reporting | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0059 | App Notification of Available OTA Update | [PRD §9.5],[EXTERNAL: Mobile App team] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-FUNC-0060 | App Display of OTA Update State | [PRD §9.5],[EXTERNAL: Mobile App team] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-FUNC-0061 | SBOM Production Per OTA Release | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; lifetime SBOM → §16 |
| SRS-FUNC-0062 | Tier-2 Classifier Delivery Restricted to Embedded OTA Components | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-PERF-0001 | Mini Variant Battery-Life Conformance | [PRD §12.1],[PRD §10.4],[CR-0002],[PRD §15.6] | §6 | APPROVED | — | CR-0002 | PASS/PASS/PASS/PAS
```

### In-Scope Interface Obligations (1 blocks)

## 10. Interface Requirements

**Version:** v6
**Session:** S-luucipet
**Status:** APPROVED — v6: SRS-INT-0036 reissued with quantified drainage criterion (5 mL/15 s/≤0.2 mL) per [ASSUMPTION: A-0023]; v5: cross-conflict resolutions applied per Conflict & Consistency Resolver — / (INT-0035 back-XR +SRS-HW-0004, link-only), / (INT-0008 back-XR +SRS-HW-0019, link-only), / (INT-0032 Priority HIGH→CRITICAL, aligns with HW-0025 CRITICAL framing of the pogo-pin+magnet assembly; priority field only, no text change). All three §10-side only — no approval revocation. v4: cross-section resolutions applied per Conflict & Consistency Resolver — / (INT-0027 cross-ref SRS-OPER-0005→SRS-OPER-0004 + footer relied-upon list corrected), / (INT-0008 Priority HIGH→MEDIUM, aligns with §4 SRS-CONN-0007), / (INT-0029 Priority HIGH→MEDIUM, aligns with §6 SRS-PERF-0005), / (INT-0051 Priority MEDIUM→LOW, aligns with §6 SRS-PERF-0008).  (INT-0045 vs §7 SRS-SAFE-0011) resolved §7-side (SAFE-0011 HIGH→CRITICAL by Requirements Drafter); INT-0045 remains CRITICAL, unchanged here (). v3:  (§10.4 terminology standardization),  (INT-0033↔INT-0049 reciprocal cross-refs + clarifiers),  (INT-0047 Priority MEDIUM→HIGH) applied per Conflict & Consistency Resolver. v2: torque contradiction (INT-0044/0047) and verification-method fixes (INT-0036, INT-0056) applied per Feasibility Checker & Verification-Method Validator flags

---

---

### View Coverage
External-party blocks tagged [EXTERNAL: Mobile App team] plus in-scope interface obligations from LUUCIPet system toward Mobile App team.
