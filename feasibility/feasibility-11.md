> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# [S-luucipet] Feasibility §11-v1 — Hardware / Physical & Mechanical Requirements

**Scope:** SRS-HW-0001 – SRS-HW-0028 (28 requirements, §11 v1)
**Dimensions scored (D1–D5, PASS/MARGINAL/FAIL):** D1 Technical Feasibility · D2 Regulatory Feasibility · D3 Testability (coarse screen only) · D4 Completeness/Consistency (intra-section) · D5 Design-Free
**Mandatory-field checks (D6–D7, POPULATED/MISSING):** D6 Priority · D7 Stability
**Note on D5 in this section:** §11 is a hardware/physical/mechanical requirements section per the approved ToC. Specifying component identity (accelerometer type, GNSS receiver, BLE radio, CCF polymer, pogo-pin arrangement) is the correct abstraction level for a hardware-CI section and is not treated as a "design" violation, provided the PRD itself specifies that same component/material as its normative requirement (verified per-item against inputs/prd.md and inputs/pcp.md below). D5 would FAIL only if the Drafter had invented an implementation approach not present in the PRD to satisfy a higher-level behavioral requirement from another section.

| SRS-HW-ID | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Overall | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SRS-HW-0001 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Mini ≤10 g verbatim from PCP §2/PRD §10.1.1. Outcome-level mass bound, no implementation. |
| SRS-HW-0002 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Max ≤22 g verbatim from PCP §2/PRD §10.1.1. Consistent with HW-0001 peer. |
| SRS-HW-0003 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | IP67/IEC 60529 cites RM-0028 (CONFIRMED, clause-INDICATIVE) correctly. Scope note reasonably distinguishes "device-standalone" governing claim from charging-interface-specific case (HW-0004). |
| SRS-HW-0004 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Advisory (non-blocking): statement content substantially overlaps SRS-INT-0035 (§10, same IP67-undocked-pogo-pin claim, one hardware-framed one behavior-framed). No intra-section contradiction — D4 scope is peers within §11, which is clean. Flagging for Conflict Resolver's future §11-vs-§10 cross-section pass, not a §11 defect. |
| SRS-HW-0005 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | LED indicator sourced verbatim from PRD §10.1.2. Simple presence requirement, Inspection-checkable. |
| SRS-HW-0006 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | ≥1.5 mm wall at lug base — verbatim numeric bound from PRD §10.1.2. |
| SRS-HW-0007 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | "Shall not penetrate wall/seal path" — verbatim negative constraint from PRD §10.1.2, consistent with HW-0003/HW-0006. |
| SRS-HW-0008 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Advisory (non-blocking): near-duplicate of SRS-INT-0036 (§10, "Charging Socket Self-Drainage"). Same pattern as HW-0004 — hardware-geometry framing vs interface-behavior framing. No intra-section conflict; flag for cross-section pass. |
| SRS-HW-0009 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | PA66-GF30 is the PRD's own normative material spec (§10.1.2/§6.2), not a Drafter-invented implementation choice — correct abstraction for a material-composition requirement in a hardware section. Stability=LIKELY-CHANGE is a reasonable call (materials are more prone to substitution during DVT than geometric/electrical bounds). |
| SRS-HW-0010 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | UV 0.3–0.5% + hydrolysis stabiliser verbatim from PRD §10.1.2. |
| SRS-HW-0011 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | No-metal-in-breakaway-zone verbatim from PRD §10.1.2/§10.1.3.2b. Consistent with SAFE-0006/0007 (fracture/fragment behavior) — correct hardware/safety split. |
| SRS-HW-0012 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | No chrome/nickel — correctly cites RM-0026 (CONFIRMED). Consistent with SAFE-0021 (non-toxicity behavior) — correct split between material composition (here) and safety outcome (§7). |
| SRS-HW-0013 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | 3-axis MEMS accelerometer presence, verbatim PRD §10.2.1. Component-identity requirement, correct for hardware section. |
| SRS-HW-0014 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | ODR ≥50 Hz — hardware capability floor backing SRS-FUNC-0014's behavioral sampling-rate requirement; correct capability/behavior split, consistent (not contradictory). |
| SRS-HW-0015 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Wake-on-motion + FIFO ≥512 B + DMA verbatim PRD §10.2.1. |
| SRS-HW-0016 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | GNSS absence on Mini — negative constraint, Inspection-checkable, consistent with HW-0001 (≤10 g budget rationale) and SRS-INT-0022. |
| SRS-HW-0017 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | GNSS presence on Max, consistent with HW-0002 and SRS-INT-0021. |
| SRS-HW-0018 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | BLE 5.x radio presence — component-identity requirement, correct for hardware section. |
| SRS-HW-0019 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Advisory (non-blocking): TX ≥+8 dBm capability overlaps SRS-CONN-0007/SRS-INT-0008 (behavioral operating-power reqs, §4/§10). Same hardware-capability-vs-operating-behavior split pattern as HW-0004/HW-0008 — not a defect, flag for cross-section awareness. Also advisory: RM-0029 (RF human-exposure, INDICATIVE) instructs "annotate derived reqs [INDICATIVE]" for TX-power-relevant requirements; recommend Regulatory/Conflict Resolver confirm whether this hardware-capability requirement also warrants that annotation, in addition to its behavioral counterparts. Not a contradiction — D2 remains PASS. |
| SRS-HW-0020 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Mini ≥120 mAh — correctly anchored to A-0006/CR-0002 (§10.4 governs over illustrative §15.3 figures). Explicit assumption dependency documented. |
| SRS-HW-0021 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Max ≥400 mAh — same A-0006/CR-0002 anchor, consistent with HW-0020. |
| SRS-HW-0022 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Battery protection functions — correctly cites RM-0011 with the version-corrected citation (IEC 62133-2:2017+AMD1:2021), matching the Regulatory Map's correction of the PRD's stale bare-:2017 citation. Good D2 compliance. |
| SRS-HW-0023 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | UN 38.3 before pilot — RM-0010 CONFIRMED, correctly cited. |
| SRS-HW-0024 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Low-battery alert ≤20% SoC — consistent with SRS-FUNC-0051's ≥10% SoC OTA reserve (20% alert precedes the 10% reserve floor chronologically; no contradiction). |
| SRS-HW-0025 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Advisory (non-blocking): pogo-pin+magnet hardware overlaps SRS-INT-0031/0032 (§10 behavioral charging-interface reqs). Same capability/behavior split pattern; not a defect, flag for cross-section awareness. |
| SRS-HW-0026 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | ≥30-day NV storage capacity — correct hardware-capacity backing for SRS-DATA-0005/0006's behavioral retention requirements. |
| SRS-HW-0027 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | On-device inference compute capability, consistent with SRS-FUNC-0031/SRS-DATA-0013 (no-cloud-round-trip behavior). |
| SRS-HW-0028 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | DMA + HW root of trust — correct physical-anchor framing for SRS-SEC-0005's secure-boot behavioral requirement. No conflict with RM-0019 (ETSI EN 303 645). |

## Summary

**28/28 requirements: PASS on all D1–D5, POPULATED on D6–D7. No FAILs, no MARGINALs.**

### Non-blocking advisories (informational only — do not block §11 approval)
Four hardware-capability requirements substantially overlap behavioral requirements already issued in other approved sections (same underlying physical constraint, expressed once as a hardware-component capability and once as an operating/interface behavior). This is an intentional and defensible pattern for a hardware-CI section, but is flagged here for the Conflict & Consistency Resolver's discretion on a future §11-vs-§10/§4 cross-section pass:

| §11 req | Overlaps with | Pattern |
|---|---|---|
| SRS-HW-0004 | SRS-INT-0035 (§10) | IP67 at charging interface, undocked |
| SRS-HW-0008 | SRS-INT-0036 (§10) | Charging socket self-drainage |
| SRS-HW-0019 | SRS-CONN-0007 / SRS-INT-0008 (§4/§10) | BLE TX ≥+8 dBm |
| SRS-HW-0025 | SRS-INT-0031 / SRS-INT-0032 (§10) | Pogo-pin + magnetic alignment |

None of these constitute a D4 FAIL under this review's scope (D4 is evaluated against intra-section peers only, per the Feasibility Checker's authority boundary) — §11 is internally self-consistent. Cross-section duplication/overlap adjudication belongs to the Conflict & Consistency Resolver.

### D5 methodology note
This section's component/material-identity requirements (accelerometer type, GNSS receiver, BLE radio, PA66-GF30, pogo-pin arrangement, DMA/root-of-trust) were checked against the PRD to confirm each is the PRD's own normative specification, not a Drafter-introduced implementation choice. All 28 passed this check.

### D3 note
Coarse screen only, per Feasibility Checker authority boundary — every requirement carries a measurable/inspectable criterion (mass in g, IP rating, N·m/N, mAh, Hz, bytes, %, presence/absence). Declared-method appropriateness (Test/Inspection typing) is reserved for the Verification-Method Validator's sequential pass, not re-litigated here.

**Verdict: PASS — §11 clears Feasibility Checker review. Ready for Verification-Method Validator.**

---

## FEASIBILITY_POST — SRS-HW-0008 (post-XSC-0008 VM change, CR-0017)

**Trigger:** CR-0017 (resolving cross-section finding XSC-0008) changed SRS-HW-0008's Verification Method field from **Inspection → Test**, to align with SRS-INT-0036 (§10), whose VM was independently corrected for the same reason (self-drainage is a functional/dynamic claim, not a static geometric feature). Requirement text, Rationale, Source, Priority (MEDIUM), Stability (STABLE), and XR are all unchanged. This re-opened §11 approval; re-scoring is scoped to SRS-HW-0008 only, all 7 dimensions.

| SRS-HW-ID | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Overall | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SRS-HW-0008 | PASS | PASS | PASS | PASS | PASS | POPULATED | POPULATED | PASS | Re-check after VM Inspection→Test (CR-0017/XSC-0008). D1 unaffected — functional testing of drainage (pour water / immersion-and-drain timing) is within stated technology bounds per PCP; no new technical burden beyond what IP67 test rigs (already implied by HW-0003/HW-0004) provide. D2 unaffected — no Regulatory Map entry (RM-0028 IP67/IEC 60529, CONFIRMED) constrains *which* verification method is used to demonstrate the self-draining outcome; RM-0028 is satisfied either way. D3 **strengthened, not weakened**: "self-draining" is a dynamic/functional claim (water must actually clear the socket) rather than a static geometric feature, so a Test-based criterion (e.g., pour a defined volume, measure residual/drain time against a threshold) is a *more* directly verifiable path than visual/dimensional Inspection of a drain channel — the coarse D3 screen (does *some* plausible verification path exist?) passes comfortably; per the authority boundary, the specific appropriateness of Test-vs-Inspection typing is the Verification-Method Validator's call, not re-litigated here, but nothing about the new VM raises an unverifiability concern. D4 unaffected — no contradiction introduced with intra-section peers (HW-0003/HW-0004/HW-0006/HW-0007 IP67/ingress family); XR to SRS-INT-0036 remains consistent, and this VM edit is exactly the kind of intentional alignment the original review's non-blocking advisory (HW-0008 ~ SRS-INT-0036 overlap) anticipated. D5 unaffected — requirement text still states outcome ("geometrically self-draining"), not implementation; VM field change carries no design content. D6/D7 unaffected — Priority MEDIUM and Stability STABLE both still populated and unchanged. |

**Verdict for SRS-HW-0008: PASS on all D1–D7.** No FAIL, no MARGINAL. The VM edit is a net-positive testability alignment; nothing in this change regresses any of the 5 scored dimensions or either mandatory-field check.

**Section impact:** This is a single-requirement re-check per Conductor scope. Combined with the original §11-v1 review (28/28 PASS), §11 remains PASS overall pending the Verification-Method Validator's re-verification of SRS-HW-0008's new Test method (sequential next step) before §11 can be re-APPROVED.
