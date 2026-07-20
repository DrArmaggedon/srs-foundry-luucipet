> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# §13 — Reliability & Availability Requirements

CAT: **RELI** | Maps to: PRD §12.2 (Reliability) | Cross-refs: PRD §10.1.2/§13.4 (IP67), PRD §7.4 (classification accuracy), PRD §9 (OTA), PRD §11.7 (base station continuous operation)
*(Drafter-authored; §13 v2 — 4 blocks, SRS-RELI-0001–0004. v2: VM corrections per V-Method review — RELI-0002/0003/0004 Analysis→Test; RELI-0001 unchanged (Analysis, PASS).)*

## 13.0 Scope Note

This section specifies the dependability, availability, and long-run success-rate criteria the system must sustain over the product's operating life and over defined observation windows. It does **not** re-issue constraints already owned elsewhere:

- **Tier-1 (≥85% accuracy / ≤5% false-positive) and Tier-2 (≥80% accuracy / ≤10% false-positive) classification-accuracy thresholds** in PRD §12.2 restate the classification-accuracy floors already owned by §3 Behavioral Classification (SRS-FUNC-0018, SRS-FUNC-0019, SRS-FUNC-0020, SRS-FUNC-0021); §13 does not re-issue them. They are accuracy/performance criteria, not availability/dependability criteria, notwithstanding their placement under the PRD's "Reliability" heading.
- **The IP67 ingress-protection rating as a component property, the device-standalone qualification scope, and the ingress test-parameter/claim-boundary requirements** are owned by §11 Hardware (SRS-HW-0003) and §12 Environmental & Durability (SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007, SRS-ENV-0008); §13 owns only the additional temporal criterion that the rating must remain valid across the full expected service lifetime, not the rating itself.
- **OTA image integrity, atomicity, and dual-bank auto-revert mechanics** are owned by §5 OTA Firmware Updates (SRS-FUNC-0052–0057); §13 owns only the resulting aggregate success-rate criterion, not the underlying mechanism.

## 13.1 Ingress-Protection Durability

**SRS-RELI-0001** | IP67 Rating Retention Over Full Service Lifetime | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.2], [PRD — ABSENT: service_lifetime_duration_value] | Rationale: PRD §12.2 states the qualitative criterion "IP67 full lifetime (device standalone)" but does not itself state a numeric service-lifetime duration against which "full lifetime" can be tested. The Product Context Profile records a user-confirmed expected service lifetime of ~2–3 years, with a 2-year floor to be used wherever a single testable figure is required; that floor is applied here as the qualification duration. This requirement is the temporal-endurance complement to the device-standalone IP67 rating already established by SRS-HW-0003 and does not restate the rating itself. | Verification Method: Analysis | Cross-References: SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006

[GLOSS: service lifetime | the expected duration, from first use to end of intended service, over which a product must continue to meet its specified performance and safety criteria]

## 13.2 Collar Device Availability

**SRS-RELI-0002** | Collar Device Operational Availability | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.2], [PRD — ABSENT: collar_availability_measurement_window] | Rationale: PRD §12.2 states "collar operational ≥99% (excl. charging)" as a direct numeric floor, but — unlike the base station uptime criterion in the same clause, which specifies a 90-day measurement window — the PRD does not state the observation-window length over which collar availability is to be measured. Flagged per the numeric-vagueness gate rather than inventing a window; the 99% floor and the charging exclusion are PRD-stated and are issued as-is. Verification Method corrected from Analysis to Test per V-Method review: this is a directly observable field/DVT proportion metric (uptime vs. total non-charging elapsed time), matching the Test pattern this SRS already applies to equivalent rate/proportion criteria (SRS-FUNC-0018–0021, SRS-FUNC-0001); no MTBF-style modeling basis is stated that would justify Analysis. | Verification Method: Test | Cross-References: SRS-HW-0025, SRS-INT-0031, SRS-INT-0032

[GLOSS: operational availability | the proportion of time a system or device is capable of performing its specified function, expressed as a percentage of total elapsed time within a defined observation window]

## 13.3 Base Station Availability

**SRS-RELI-0003** | Base Station Uptime | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.2] | Rationale: PRD §12.2 states "base ≥99.5% uptime over 90-day window" as a direct, fully-bounded numeric criterion; the base station's continuous, mains-powered, no-sleep operating profile (PRD §11.7) makes a rolling-window uptime metric directly measurable in the field. Verification Method corrected from Analysis to Test per V-Method review: the criterion is fully bounded (explicit 90-day window) and directly observable via continuous-operation monitoring against the threshold — a practical DVT/pilot burn-in test, not a modeling exercise. | Verification Method: Test | Cross-References: —

[GLOSS: uptime | the proportion of a defined observation window during which a system remains powered, responsive, and capable of performing its specified function]

## 13.4 OTA Update Success Rate

**SRS-RELI-0004** | OTA Update Success Rate | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a base station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.2] | Rationale: PRD §12.2 states "OTA success ≥99%" as a direct numeric floor on the aggregate reliability of the OTA mechanism already specified functionally in §5; "success" is defined operationally against the existing auto-revert criterion (SRS-FUNC-0056) rather than inventing a separate definition. Verification Method corrected from Analysis to Test per V-Method review: this is a repeated-trial pass/fail statistic (run N install attempts, including fault-injected trials per SRS-FUNC-0057, and compute the pass proportion against the 99% floor), matching the Test pattern this SRS already applies to equivalent proportion-based criteria (SRS-FUNC-0001, SRS-FUNC-0018–0021). | Verification Method: Test | Cross-References: SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0057

---

## Drafter Notes — Out-of-Scope Items, Flags & Deferrals (not silently dropped)

- **IoT Cloud Device-Management layer availability/uptime — OUT OF SCOPE, no numeric floor available.** PRD §12.2 (this section's sole PRD source) specifies reliability/availability floors only for the collar device, the base station, and the OTA mechanism — all within our build. It states no uptime, availability, or success-rate target for the IoT Cloud Device-Management layer, which per [ASSUMPTION: A-0015] is external (IoT Cloud backend team) beyond our in-scope transport hand-off (SRS-CONN-0014, SRS-CONN-0018). No cloud-side reliability requirement is issued here. Responsible party for defining any such SLA, should one be needed: **IoT Cloud backend team**, via a future PRD amendment or an inter-team SLA — this is an omission in the PRD source material, not a drafting choice. Our own in-scope interface obligation toward that team (transporting records reliably to the hand-off point) is already captured as in-scope requirements in §4 (SRS-CONN-0014–0017, SRS-CONN-0026).
- **Mobile App reliability/availability — OUT OF SCOPE, no PRD source.** PRD §12.2 states no reliability or availability criterion for the Mobile App, which is external (Mobile App team) per PRD §14.1. No Mobile App reliability requirement is issued here; responsible party for any such criterion is the **Mobile App team**, via their own requirements process.
- **Field failure rate, MTBF/MTTR, and warranty-return-rate criteria** are not stated anywhere in the PRD (§12.2 or elsewhere) and are not invented here per the numeric-vagueness gate; no UNRESOLVED-CONTEXT flag is raised for their absence because there is no PRD clause implying such a metric is expected at the SRS level.
- **New UNRESOLVED-CONTEXT flag raised by §13** (in addition to the 8 pre-existing open flags, unchanged by this section):
  1. Collar operational-availability measurement-window length is absent from PRD §12.2, unlike the base station's explicit 90-day window (SRS-RELI-0002).
- **Format-vocabulary note for Conductor:** this section uses the established repo convention already in force across §§3–12 — `Priority: CRITICAL | HIGH | MEDIUM | LOW`, `Stability: STABLE | LIKELY-CHANGE | VOLATILE`, `Verification Method:` / `Cross-References:` fields — consistent with the mandatory requirement-block format for this drafting pass.
- **Assumption/PCP dependency:** SRS-RELI-0001 relies on the Product Context Profile §8 user-confirmed expected-service-lifetime figure (~2–3 years, 2-year floor applied), which is recorded in the PCP rather than in the Assumption Register; no A-ID currently carries this figure. Flagged for the Conductor/PRD Processing Agent in case a formal A-ID should be issued to carry it going forward.

---

### SRS-ID Inventory (§13 v2 — COMPLETE)
- **4 blocks, SRS-RELI-0001 … SRS-RELI-0004.** All in-scope.
- Next free RELI ID = **SRS-RELI-0005**.

### V-Method Revision Log
- **v2 (this revision):** Verification-Method Validator flagged SRS-RELI-0002/0003/0004 as carrying an Analysis label inconsistent with their proportion/rate-based, directly-observable criteria and with this SRS's own established Test pattern for equivalent metrics (SRS-FUNC-0018–0021, SRS-FUNC-0001). All three corrected to Test. SRS-RELI-0001 reviewed and confirmed PASS as Analysis (multi-year real-time IP67-lifetime retention is impractical to literally test pre-launch; Analysis via existing §12 accelerated-exposure tests is the correct fit, consistent with SRS-PERF-0001/0002 precedent) — left unchanged.
