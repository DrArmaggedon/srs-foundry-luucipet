> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:38:48Z
> **Audience:** Regulatory & Compliance
> ⚠️ For full context, always refer to the Master SRS.

---

## 17. Standards Conformance

## 17. Standards Conformance

## 18. Regulatory

## 18. Regulatory

# §18 — Regulatory Certification & Market Pathways

****Pipeline:** Feasibility PASS (46/46) · V-Method PASS (46/46) · Intra-Conflict COMPLETE (/0029) · RTM ADD-ROW COMPLETE (323→369)

§18 (REG) answers "what certifications/approvals are needed to place the product on each market" — distinct from §17 (COMP), which binds the design to the underlying technical standards.

## Appendix B. Regulatory Map

## Appendix B. Regulatory Map

The Regulatory Map enumerates 31 regulatory instruments (RM-0001–RM-0031) across five target markets. The full map is maintained in the project repository.

```
> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Session:**  S-luucipet · **Product:**  LUUCIPet Wellness Monitor v1.3.3 · **Verification date:**  2026-07-13
**Policy:**  Tiered (Tier-1 existence/currency/scope verified via live web; Tier-2 clause-level from documented structure; Tier-3 UNCERTAIN reserved for genuine applicability/existence doubt).
**RM-ID range issued:**  RM-0001 … RM-0031 · **Next RM cursor:**  RM-0032
**Confidence tally:**  CONFIRMED 18 · INDICATIVE 9 · UNCERTAIN 2 (+1 miscitation flag resolved via RM-0030). RM-0031 added (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT).

## All SRS-REG-* Requirement Blocks (cross-section pull)

SRS-REG-0001** | **Prohibit medical-classification claims in labeling and marketing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. |
| **Rationale**    | Derived from PRD §13.6. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.6 · SRS-REG-0002 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **Require regulatory classification review before releasing diagnostic-adjacent features** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. |
| **Rationale**    | Derived from PRD §13.6. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §13.6 · SRS-REG-0001


SRS-REG-0001, SRS-REG-0002. |



SRS-REG-0001** | **FCC Part 15 Subpart C Certification Hold (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Body (TCB) prior to commercial distribution in the US market. \| |
| **Rationale**    | FCC 47 CFR Part 15 Subpart C §15.247 mandates third-party TCB certification (not self-declaration) for intentional radiators in the 2.4 GHz band; this is the market-access instrument corresponding to the technical conformance already required by SRS-COMP-0018. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0018 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0001 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **FCC Part 15 Subpart B Supplier's Declaration of Conformity (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions prior to commercial distribution. \| |
| **Rationale**    | FCC 47 CFR Part 15 Subpart B §15.107/§15.109 permits self-declaration rather than TCB certification for unintentional-emitter compliance. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0019 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0002 |

<a id="srs-reg-0003"></a>

| **SRS-REG-0003** | **FCC Identifier Marking (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the US market. \| |
| **Rationale**    | FCC ID marking is a mandatory labeling condition attached to the Part 15 Subpart C certification. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0001 |

<a id="srs-reg-0004"></a>

| **SRS-REG-0004** | **NRTL Listing Hold for Base Station Electrical Safety (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. \| |
| **Rationale**    | US retail market access for mains-powered electronic equipment requires NRTL listing. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0009 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0013 |

<a id="srs-reg-0005"></a>

| **SRS-REG-0005** | **California Proposition 65 Conditional Warning Labeling (US-CA)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is present above the applicable safe-harbor threshold, prior to commercial distribution in the US-CA market. \| |
| **Rationale**    | Proposition 65 imposes a conditional warning-labeling obligation that is procedurally distinct from the underlying materials-conformance requirement. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0024 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0026 |

<a id="srs-reg-0006"></a>

| **SRS-REG-0006** | **Certification Documentation Package Availability (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support FCC TCB certification (SRS-REG-0001) and NRTL listing (SRS-REG-0004) prior to submission for either certification. \| |
| **Rationale**    | Captures the delivering engineering team's own in-scope interface obligation toward the externally-executed certification processes, ensuring external TCB/NRTL bodies are not blocked by missing inputs. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001, SRS-REG-0004 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: us_certification_documentation_owner |

<a id="srs-reg-0007"></a>

| **SRS-REG-0007** | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to commercial distribution in the US market. \| |
| **Rationale**    | RM-0009 is UNCERTAIN; this block requires only that the determination be made and documented, rather than asserting a specific exemption outcome. \| Verification Method: Analysis \| Cross-References: SRS-REG-0001 |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0009 |

<a id="srs-reg-0008"></a>

| **SRS-REG-0008** | **ISED Certification Hold (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen prior to commercial distribution in the Canada market. \| |
| **Rationale**    | ISED RSS-247 governs 2.4 GHz license-exempt radio equipment and RSS-Gen sets general certification procedure. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0018, SRS-COMP-0016 |
| **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0009"></a>

| **SRS-REG-0009** | **ISED ICES-003 Compliance (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to commercial distribution. \| |
| **Rationale**    | ICES-003 is Canada's counterpart to the US FCC Part 15 Subpart B self-declaration regime. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0019, SRS-REG-0002 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0010"></a>

| **SRS-REG-0010** | **Innovation Canada Identifier Marking (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the Canada market. \| |
| **Rationale**    | IC ID marking is a mandatory labeling condition attached to the ISED certification. \| Verification Method: Inspection \| Cross-References: SRS-REG-0008 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0011"></a>

| **SRS-REG-0011** | **Certification Documentation Package Availability (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support ISED certification (SRS-REG-0008) prior to submission. \| |
| **Rationale**    | Mirrors SRS-REG-0006 for the Canada market. \| Verification Method: Inspection \| Cross-References: SRS-REG-0008 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: canada_certification_documentation_owner |

<a id="srs-reg-0012"></a>

| **SRS-REG-0012** | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to commercial distribution in the Canada market. \| |
| **Rationale**    | Mirrors SRS-REG-0007; RM-0009's UNCERTAIN status is per-market and applies independently to Canada. \| Verification Method: Analysis \| Cross-References: SRS-REG-0008, SRS-REG-0007 |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0009 |

<a id="srs-reg-0013"></a>

| **SRS-REG-0013** | **Pre-Launch Certification-Status Gate (US + Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identified in SRS-REG-0001 through SRS-REG-0012 applicable to that market are complete and on file. \| |
| **Rationale**    | Umbrella gate preventing partial or premature market release. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001–0012 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 |

<a id="srs-reg-0014"></a>

| **SRS-REG-0014** | **RED 2014/53/EU Declaration of Conformity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | CE marking prerequisite for radio equipment. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0020, SRS-COMP-0016 |

<a id="srs-reg-0015"></a>

| **SRS-REG-0015** | **EU Notified Body Engagement Applicability Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Conditional on harmonised standard OJ listing. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0014 |

<a id="srs-reg-0016"></a>

| **SRS-REG-0016** | **CE Marking Physical Application** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On device or packaging. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0014, SRS-REG-0017 |

<a id="srs-reg-0017"></a>

| **SRS-REG-0017** | **EU GPSR General Product Safety Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | GPSR 2023/988 Art 5/6. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · §7 SAFE blocks |

<a id="srs-reg-0018"></a>

| **SRS-REG-0018** | **EU Authorized Representative Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | GPSR Art 4 / RED Art 11. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 |

<a id="srs-reg-0019"></a>

| **SRS-REG-0019** | **EU Technical Documentation File Availability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-scope interface obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0014, SRS-REG-0017 |

<a id="srs-reg-0020"></a>

| **SRS-REG-0020** | **RoHS Self-Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | 2011/65/EU + 2015/863. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0023 |

<a id="srs-reg-0021"></a>

| **SRS-REG-0021** | **WEEE Producer Registration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Per-member-state. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0026 |

<a id="srs-reg-0022"></a>

| **SRS-REG-0022** | **REACH SVHC Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Annex XVII. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0022 |

<a id="srs-reg-0023"></a>

| **SRS-REG-0023** | **EU Battery Regulation Labelling and CE Marking** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2023/1542 Art 6. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0025 |

<a id="srs-reg-0024"></a>

| **SRS-REG-0024** | **EU Battery Regulation Article 11 Removability Exemption Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Deadline 18 Feb 2027. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-COMP-0025, A-0013 |

<a id="srs-reg-0025"></a>

| **SRS-REG-0025** | **EU Cyber Resilience Act Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2024/2847 Annex I + Art 13–14. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0010, SRS-SEC-0006, SRS-MAINT-0003 |

<a id="srs-reg-0026"></a>

| **SRS-REG-0026** | **GDPR Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2016/679 + Art 30. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · §9 DATA blocks |

<a id="srs-reg-0027"></a>

| **SRS-REG-0027** | **EU Packaging and Packaging Waste Regulation Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | PPWR. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0027 |

<a id="srs-reg-0028"></a>

| **SRS-REG-0028** | **UKCA Marking Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK SI 2017/1206. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0020 |

<a id="srs-reg-0029"></a>

| **SRS-REG-0029** | **UK Approved Body Engagement Applicability Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Conditional. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0028, SRS-REG-0015 |

<a id="srs-reg-0030"></a>

| **SRS-REG-0030** | **UK Responsible Person Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK establishment requirement. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0028, SRS-REG-0018 |

<a id="srs-reg-0031"></a>

| **SRS-REG-0031** | **UK PSTI Act 2022 Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0010, SRS-REG-0025 |

<a id="srs-reg-0032"></a>

| **SRS-REG-0032** | **UK GDPR Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK GDPR + DPA 2018. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0026 |

<a id="srs-reg-0033"></a>

| **SRS-REG-0033** | **UK Materials and Environmental Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK REACH, UK RoHS, UK WEEE. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0022/0023/0026 |

<a id="srs-reg-0034"></a>

| **SRS-REG-0034** | **UK Producer Responsibility Packaging Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0027, SRS-REG-0027 |

<a id="srs-reg-0035"></a>

| **SRS-REG-0035** | **Pre-Launch Certification-Status Gate (EU + UK)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · REG-0013, REG-0014–0034, REG-0045, REG-0046 |

<a id="srs-reg-0045"></a>

| **SRS-REG-0045** | **GNSS Exemption Determination (EU)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0009 · SRS-REG-0014, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="srs-reg-0046"></a>

| **SRS-REG-0046** | **GNSS Exemption Determination (UK)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0009 · SRS-REG-0028, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="srs-reg-0036"></a>

| **SRS-REG-0036** | **RCM Marking Declaration (AU/NZ)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | AS/NZS 4268:2017. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0016 |

<a id="srs-reg-0037"></a>

| **SRS-REG-0037** | **ACMA Supplier Code Registration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Precondition to RCM. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0036 |

<a id="srs-reg-0038"></a>

| **SRS-REG-0038** | **AU/NZ Responsible Supplier Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-market required. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0018, SRS-REG-0030 |

<a id="srs-reg-0039"></a>

| **SRS-REG-0039** | **AU/NZ Certification Documentation Package** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-scope interface obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0036/0037 |

<a id="srs-reg-0040"></a>

| **SRS-REG-0040** | **GNSS Exemption Determination (AU/NZ)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | RM-0009 UNCERTAIN. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0007/0012 |

<a id="srs-reg-0041"></a>

| **SRS-REG-0041** | **CCPA/CPRA Contingent Market-Access Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Threshold-contingent. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-DATA-0022 |

<a id="srs-reg-0042"></a>

| **SRS-REG-0042** | **Post-Certification Regulatory-Change Monitoring** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Lifetime obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-MAINT-0002/0003 |

<a id="srs-reg-0043"></a>

| **SRS-REG-0043** | **Certification and DoC Archival Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Per-market minimum. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · A-0025 |

<a id="srs-reg-0044"></a>

| **SRS-REG-0044** | **Pre-Launch Certification-Status Gate (All Markets)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Consolidating gate. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · REG-0013, REG-0035, REG-0036–0043, REG-0045, REG-0046 |


---


SRS-REG-0001 | Prohibit medical-classification claims | [PRD §13.6] | §1 | APPROVED | Inspection |
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


SRS-REG-0043; resolves D4 MARGINAL. | RED Art 10 (10yr), CRA Art 13/31 (10yr/support), FCC §2.938 (2yr), ISED RSS-Gen, ACMA/EESS (5yr). Tier-1 verified 2026-07. | LOW-MEDIUM |
| A-0024 | SBOM machine-readable format = SPDX 2.3 or CycloneDX. Anchored in SRS-COMP-0028. | Standard-derived default. EU CRA Annex I + US EO 14028. | LOW-MEDIUM |

(A-0001 through A-0023 retained in master Assumption Register.)

```

---

## Regulatory Map (Appendix)

> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Session:**  S-luucipet · **Product:**  LUUCIPet Wellness Monitor v1.3.3 · **Verification date:**  2026-07-13
**Policy:**  Tiered (Tier-1 existence/currency/scope verified via live web; Tier-2 clause-level from documented structure; Tier-3 UNCERTAIN reserved for genuine applicability/existence doubt).
**RM-ID range issued:**  RM-0001 … RM-0031 · **Next RM cursor:**  RM-0032
**Confidence tally:**  CONFIRMED 18 · INDICATIVE 9 · UNCERTAIN 2 (+1 miscitation flag resolved via RM-0030). RM-0031 added (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT).

## A. Horizontal — Radio / Wireless

| RM-ID   | Standard/Reg                                                                              | Clause                | Market                  | Applies To    | Confidence | Verification note                                                                                                                                                                                                                                                                                        |
| :------ | :---------------------------------------------------------------------------------------- | :-------------------- | :---------------------- | :------------ | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RM-0001 | FCC 47 CFR Part 15 Subpart C                                                              | §15.247               | US                      | Mini/Max/Base | CONFIRMED  | BLE 2.4 GHz intentional radiator.                                                                                                                                                                                                                                                                        |
| RM-0002 | FCC 47 CFR Part 15 Subpart B                                                              | §15.107/.109          | US                      | System        | CONFIRMED  | Unintentional emissions.                                                                                                                                                                                                                                                                                 |
| RM-0003 | RED Directive 2014/53/EU                                                                  | Art 3.1(a),3.1(b),3.2 | EU                      | Mini/Max/Base | CONFIRMED  | Current.                                                                                                                                                                                                                                                                                                 |
| RM-0004 | ETSI EN 300 328                                                                           | §4.3                  | EU                      | Mini/Max/Base | INDICATIVE | Correct 2.4 GHz RED HS; PRD cites v2.2.2 — verify exact OJ-listed version.                                                                                                                                                                                                                               |
| RM-0005 | UK Radio Equipment Regs 2017 (SI 2017/1206)                                               | —                     | UK                      | Mini/Max/Base | CONFIRMED  | UKCA.                                                                                                                                                                                                                                                                                                    |
| RM-0006 | ISED RSS-247 Issue 2 + RSS-Gen Issue 5                                                    | —                     | CA                      | Mini/Max/Base | INDICATIVE | Verify current issue numbers at submission.                                                                                                                                                                                                                                                              |
| RM-0007 | AS/NZS 4268:2017                                                                          | —                     | AU/NZ                   | Mini/Max/Base | INDICATIVE | RCM; verify no newer edition.                                                                                                                                                                                                                                                                            |
| RM-0008 | Bluetooth SIG Qualification (QDID)                                                        | —                     | Global                  | all BLE       | CONFIRMED  | Mandatory per Bluetooth SIG.                                                                                                                                                                                                                                                                             |
| RM-0009 | GNSS passive-receiver intentional-radiator exemption                                      | —                     | US/EU/UK/CA/AU-NZ       | Max           | INDICATIVE | Per-market; PRD §13.1 defers to Regulatory Lead. **Escalated to user.**                                                                                                                                                                                                                                  |
| RM-0029 | IEC 62311 / EN 62311 (RF human-exposure) + FCC RF-exposure rules (47 CFR §1.1310/§2.1093) | —                     | EU/UK/US (+ per-market) | Mini/Max/Base | INDICATIVE | USER DECISION: map now, confirm per-market applicability/thresholds. Tier-1: standards exist/current. Animal-worn 2.4 GHz TX (≥+8 dBm) + mains base station plausibly trigger RF-exposure assessment; low-power animal-worn category & exact thresholds per-market. Annotate derived reqs [INDICATIVE]. |

## B. Horizontal — Battery / Electrical Safety

| RM-ID   | Standard/Reg                             | Clause                                       | Market     | Applies To    | Confidence                          | Verification note                                                                                                                                                                                                                                                    |
| :------ | :--------------------------------------- | :------------------------------------------- | :--------- | :------------ | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RM-0010 | UN 38.3                                  | Part III 38.3                                | Global     | Mini/Max      | CONFIRMED                           | Before pilot production.                                                                                                                                                                                                                                             |
| RM-0011 | IEC 62133-2:2017 **+AMD1:2021** (Ed 1.1) | Cl 7                                         | EU (+intl) | Mini/Max      | CONFIRMED (version-corrected)       | PRD cites bare :2017 → cite with AMD1. ED2 effective 2026-05-29, monitor.                                                                                                                                                                                            |
| RM-0012 | UL 1642 / UL 2054                        | —                                            | US         | Mini/Max      | CONFIRMED                           | US cell/pack.                                                                                                                                                                                                                                                        |
| RM-0013 | EN 62368-1:2020 / UL 62368-1             | —                                            | EU, US     | Base          | CONFIRMED                           | Mains-powered base station.                                                                                                                                                                                                                                          |
| RM-0014 | EU Battery Regulation (EU) 2023/1542     | Art 6, **Art 11 removability**, labelling/CE | EU         | Mini/Max/Base | CONFIRMED (removability INDICATIVE) | Applicable since 18 Aug 2025; **Art 11 end-user removability mandatory 18 Feb 2027**. ⚠️ LUUCIPet battery is NON-SWAPPABLE (§14.1) → **potential conflict** vs Art 11 within 2–3 yr market life. Verify small/sealed/IP-rated exemption. → Conflict Resolver + user. |

## C. Horizontal — Privacy / Cybersecurity

| RM-ID   | Standard/Reg                           | Clause             | Market | Applies To    | Confidence                                | Verification note                                                                                                                   |
| :------ | :------------------------------------- | :----------------- | :----- | :------------ | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| RM-0015 | GDPR (EU) 2016/679                     | Art 5,25,32        | EU     | System        | CONFIRMED                                 | Owner PII + Max GNSS location = personal data.                                                                                      |
| RM-0016 | UK GDPR + DPA 2018                     | —                  | UK     | System        | CONFIRMED                                 | —                                                                                                                                   |
| RM-0017 | CCPA/CPRA                              | —                  | US-CA  | System        | INDICATIVE                                | Applies if thresholds met; ~5,000 units may not initially meet.                                                                    |
| RM-0018 | PIPEDA                                 | —                  | CA     | System        | CONFIRMED                                 | —                                                                                                                                   |
| RM-0019 | **ETSI EN 303 645:2025**               | Prov 5.1–5.13      | EU, UK | System        | CONFIRMED (version-corrected — PRD STALE) | 🔴 PRD cites V3.1.3; **EN 303 645:2025** now RED-harmonised & mandatory for EU (~1 Jul 2026). Cite :2025. Clause-level INDICATIVE. |
| RM-0020 | RED Delegated Reg (EU) 2022/30         | Art 3.3(d)(e)(f)   | EU     | Mini/Max/Base | CONFIRMED (transitional)                  | Applicable 1 Aug 2025; being repealed in favor of CRA — align to CRA.                                                               |
| RM-0021 | EU Cyber Resilience Act (EU) 2024/2847 | Annex I; Art 13–14 | EU     | System        | CONFIRMED                                 | Vuln reporting 11 Sep 2026; full 11 Dec 2027 (PRD dates correct).                                                                   |
| RM-0022 | UK PSTI Act 2022 (+ SI 2023/1007)      | security schedule  | UK     | System        | CONFIRMED                                 | In force.                                                                                                                           |
| RM-0023 | FCC Cyber Trust Mark                   | —                  | US     | System        | INDICATIVE                                | Voluntary.                                                                                                                          |

## D. Horizontal — Materials / Environmental / Ingress / Product Safety

| RM-ID       | Standard/Reg                                                             | Clause                                                                                                                                      | Market        | Applies To             | Confidence                    | Verification note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------- | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------ | :--------------------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RM-0024     | EU GPSR (EU) 2023/988                                                    | Art 5, **Art 6**                                                                                                                            | EU            | System + CCF           | CONFIRMED                     | Applicable 13 Dec 2024. Underpins Zone-2 breakaway safety case; supports A-0002/A-0010 design duty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **RM-0031** | EU GPSR (EU) 2023/988 — design-level strangulation-mitigation branch     | **Art 6(1)(a)**  [assessment: product characteristics/design] READ WITH Art 5 [general safety req] & Recital 22 [design-first hierarchy] | EU            | CCF (Zone 2 breakaway) | **INDICATIVE-pending-DVT**    | Refines RM-0024 for the specific claim (PRD §14.2/§10.1.4) that the compound-CCF breakaway = design-level strangulation mitigation. Applicability CONFIRMED (Tier-1 EUR-Lex CELEX:32023R0988). CITATION-PRECISION: obligation is Art 5; Art 6(1)(a) is assessment criteria — cite BOTH, not Art 6(1) alone. Efficacy INDICATIVE-pending-DVT: unproven esp. feline SKU (A-0014 airway caveat + CCF-L retention-floor overlap). Substantiation needed: DVT breakaway-force testing to SKU windows + feline-airway validation + documented GPSR Art 9 risk-assessment file. Supporting animal-collar-release std = ASTM F2056 per RM-0030 (NOT ASTM F2727 — miscitation resolved in RM-0030). Distinct from A-0013 (Battery Reg Art 11) — not conflated. New assumption A-0017 issued to carry this framing. |
| RM-0025     | UK GPSR 2005 / US CPSA                                                   | —                                                                                                                                           | UK, US        | System + CCF           | CONFIRMED                     | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RM-0026     | REACH (EC)1907/2006 · RoHS 2011/65/EU + 2015/863 · CA Prop 65            | REACH Annex XVII; RoHS Annex II                                                                                                             | EU, UK, US-CA | device + CCF           | CONFIRMED                     | Animal-contact materials; no chrome/nickel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RM-0027     | WEEE 2012/19/EU · EU PPWR · UK Producer Responsibility                   | —                                                                                                                                           | EU, UK        | System + packaging     | CONFIRMED                     | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RM-0028     | IEC 60529 (IP67) + IEC 60068-2-1/-2-2/-2-5/-2-14/-2-27/-2-64/-2-68/-2-78 | ingress + env test                                                                                                                          | Global        | Mini/Max/CCF           | CONFIRMED (clause INDICATIVE) | Supports A-0003 (60068-2-14 Test Na thermal cycling — CONFIRMED appropriate basis).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## E. Vertical Scan

Consumer-IoT vertical fully covered by RM-0019. NISTIR 8259 = US voluntary guidance (not issued as mandatory RM row). **No Medical / Automotive / Aviation / Industrial-OT / Payment / Critical-Infra verticals triggered** — the NOT-a-medical-device boundary (§13.6) keeps IEC 62304 / EU MDR / FDA out. ✅ No vertical leakage.

## Assumption Confirmations

- **A-0002** (Zone-2 blunt-edge method): PARTIALLY CONFIRMED → keep **INDICATIVE**, method-only. GPSR Art 6 (RM-0024) supports a sharp-edge test methodology; toy-safety analog on an animal product has no direct mandate.
- **A-0010** (device-absent entrapment 12 mm probe): **INDICATIVE** — GPSR foreseeable-hazard duty supports a geometric check; specific probe is engineered default.
- **A-0011** (battery-ingestion = Li-Po pouch, NOT coin cell): **CONFIRMED.**  Reese's Law / 16 CFR 1263 / UL 4200A apply only to button/coin cells, explicitly not pouch/prismatic Li-Po. General ingestion/small-part warning under GPSR/CPSA is correct basis.

## 🔴 UNCERTAIN — needs user decision (batched, FULL mode)

1. **RM-0009 — GNSS passive-receiver intentional-radiator exemption.**  Per-market applicability; PRD defers to Regulatory Lead. Options: A) CONFIRMED (accept exempt-unintentional-emitter across 5 markets) · B) INDICATIVE (map, per-market confirm before each submission) · C) Exclude (defer GNSS radio treatment).
2. **RM-EMC-001 (candidate) — RF human/animal-exposure standard (IEC 62311 / EN 62311 / FCC RF-exposure).**  Collar worn continuously + mains base station plausibly trigger RF-exposure assessment. Options: A) CONFIRMED (adopt IEC/EN 62311 basis now) · B) INDICATIVE (map, per-market confirm) · C) Exclude (defer).

## 🟥 Breakaway-Force Citation — RESOLVED (user: anchor to ASTM F2056)

RM-0030 — ASTM F2056 "Standard Consumer Safety Specification for Pet Collars" — CONFIRMED (existence/scope) at STANDARD LEVEL; feline force value UNVERIFIED.  Verified: ASTM F2727-09(2025) = "Standard Guide for Manufacturers for Labeling **Headgear** Products." PRD (§10.1.3.2b, §13.2, PCP) wrongly cites it as the feline ≤20 N breakaway ceiling source. Plausibly-intended standard = **ASTM F2056 "Standard Consumer Safety Specification for Pet Collars"**  (confirmed to exist), but could NOT confirm F2056 specifies a numeric ≤20 N feline force. The **CCF-M/L "canine guidance"**  ceilings have **no identifiable standard basis** (no ASTM/EN canine breakaway-force standard found).
Consequence: cat CCF-S ≤20 N ceiling cannot be traced to F2727 → citation must be corrected; CCF-M/L canine ceilings treated as **engineering-derived** ( `[ASSUMPTION]`), not `[STD:]`. **Escalated to user (Tier-3).**

## Routing to Conflict & Consistency Resolver

- RM-0014: EU Battery Reg Art 11 removability vs non-swappable battery → potential conflict.
- Version corrections: SRS `[STD:]` tags must cite **EN 303 645:2025** and **IEC 62133-2:2017/AMD1:2021** (not the PRD's older versions).

---

*Regulatory Agent-authored (inline), Conductor-persisted to shared store per standing fix. Map Version v1.2 — added RM-0031 (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT) from targeted determination during §2 drafting; header/cursor/tally reconciled.*

---

### View Coverage
Wellness/medical-boundary language, Standards Conformance (§17), Regulatory (§18), 5 SRS-REG-* blocks pulled cross-section, plus full Regulatory Map.
