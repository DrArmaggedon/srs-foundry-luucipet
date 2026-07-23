> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-23T01:00:00Z
⚠️ For full context, always refer to the Master SRS.

---


## 1. Introduction (Wellness-Not-Medical Boundary)


## 1.1 Purpose (Wellness-Not-Medical Boundary)


## 1.2 Scope (Wellness-Not-Medical Boundary)


## 1.3 Product Perspective (Wellness-Not-Medical Boundary)


## 1.4 Wellness-Not-Medical Boundary (Wellness-Not-Medical Boundary)

<a id="srs-reg-0001"></a>

| **SRS-REG-0001** | **Prohibit medical-classification claims in labeling and marketing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. |
| **Rationale**    | Derived from PRD §13.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.6 · SRS-REG-0002 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **Require regulatory classification review before releasing diagnostic-adjacent features** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. |
| **Rationale**    | Derived from PRD §13.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §13.6 · SRS-REG-0001


## 1.5 Definitions and References (Wellness-Not-Medical Boundary)


## 17. Standards Conformance



## 17.0 Scope Note

This section binds the product design to the named technical standards whose test methods, clauses, or provisions underlie requirements already issued in §§5–16. §17 (COMP) answers "what standards does this design conform to"; §18 (REG) answers "what market certifications/approvals are needed."

## 17.1 Ingress Protection

<a id="srs-comp-0005"></a>

| **SRS-COMP-0005** | **IEC 60529 Ingress Protection Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, in its standalone (CCF-unmated) configuration, shall conform to the IEC 60529 IPX7 test methodology as the verification basis for the IP67 ingress-protection rating required by SRS-HW-0003. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007

## 17.2 Battery & Electrical Safety |

<a id="srs-comp-0006"></a>

| **SRS-COMP-0006** | **IEC 62133-2 Battery Cell Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). |
| **Rationale**    | Derived from PRD §13.3. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 |

<a id="srs-comp-0007"></a>

| **SRS-COMP-0007** | **UN 38.3 Battery Transport Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. |
| **Rationale**    | Derived from PRD §10.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-COMP-0006 |

<a id="srs-comp-0008"></a>

| **SRS-COMP-0008** | **UL 1642/UL 2054 US Cell Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable to cell construction, for placement on the US market. |
| **Rationale**    | Derived from PRD §13.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 · SRS-COMP-0006 |

<a id="srs-comp-0009"></a>

| **SRS-COMP-0009** | **EN 62368-1/UL 62368-1 Base Station Electrical Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station, in both Charging and Relay tiers, shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. |
| **Rationale**    | Derived from PRD §13.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 · —

## 17.3 IoT Cybersecurity Baseline |

<a id="srs-comp-0010"></a>

| **SRS-COMP-0010** | **ETSI EN 303 645 Consumer IoT Security Baseline Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. |
| **Rationale**    | Derived from PRD §12.3. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 · SRS-SEC-0001 through SRS-SEC-0006

## 17.4 Environmental Test-Method Series (IEC 60068-2) |

<a id="srs-comp-0011"></a>

| **SRS-COMP-0011** | **IEC 60068-2-14 Thermal-Cycling Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. |
| **Rationale**    | Derived from PRD §12.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.5 · SRS-ENV-0003 |

<a id="srs-comp-0012"></a>

| **SRS-COMP-0012** | **IEC 60068-2-78 Damp-Heat Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0004 |

<a id="srs-comp-0013"></a>

| **SRS-COMP-0013** | **IEC 60068-2-27 Mechanical Shock Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0010 |

<a id="srs-comp-0014"></a>

| **SRS-COMP-0014** | **IEC 60068-2-64 Vibration Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0011 |

<a id="srs-comp-0015"></a>

| **SRS-COMP-0015** | **IEC 60068-2-5 UV-Aging Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. |
| **Rationale**    | Derived from PRD §12.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.5 · SRS-ENV-0013

## 17.5 Radio / EMC |

<a id="srs-comp-0016"></a>

| **SRS-COMP-0016** | **ETSI EN 300 328 2.4 GHz Radio Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-CONN-0001, SRS-CONN-0002, SRS-CONN-0007 |

<a id="srs-comp-0017"></a>

| **SRS-COMP-0017** | **Bluetooth SIG Qualification Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0016 |

<a id="srs-comp-0018"></a>

| **SRS-COMP-0018** | **FCC Part 15 Subpart C Intentional Radiator Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0016 |

<a id="srs-comp-0019"></a>

| **SRS-COMP-0019** | **FCC Part 15 Subpart B Unintentional Radiator Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0018 |

<a id="srs-comp-0020"></a>

| **SRS-COMP-0020** | **RED 2014/53/EU Essential Requirements Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0016, SRS-COMP-0010 |

<a id="srs-comp-0021"></a>

| **SRS-COMP-0021** | **RF Human-Exposure Standard Conformance (Contingent)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applicable. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 · —

## 17.6 Materials Compliance |

<a id="srs-comp-0022"></a>

| **SRS-COMP-0022** | **REACH Regulation Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. |
| **Rationale**    | Derived from PRD §10.1.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0021 |

<a id="srs-comp-0023"></a>

| **SRS-COMP-0023** | **RoHS Directive Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0022 |

<a id="srs-comp-0024"></a>

| **SRS-COMP-0024** | **California Proposition 65 Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0022, SRS-COMP-0023 |

<a id="srs-comp-0025"></a>

| **SRS-COMP-0025** | **EU Battery Regulation Material and Labelling Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 |

<a id="srs-comp-0026"></a>

| **SRS-COMP-0026** | **WEEE Directive Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 |

<a id="srs-comp-0027"></a>

| **SRS-COMP-0027** | **EU PPWR / UK Producer Responsibility Packaging Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0026

## 17.7 Software & Quality Management |

<a id="srs-comp-0028"></a>

| **SRS-COMP-0028** | **SBOM Machine-Readable Format Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The SBOM produced at each OTA release (SRS-FUNC-0061) and maintained across the supported service lifetime (SRS-MAINT-0002) shall be issued in a machine-readable format conforming to SPDX 2.3 or CycloneDX. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0061, SRS-MAINT-0002

## 17.8 Out-of-Scope Standards (Explicit Attribution)

- **IEC 62304** — OUT OF SCOPE. Product is general-wellness for animals, not a medical device. Responsible: Regulatory Affairs / Product Management.
- **ISO 14971** — OUT OF SCOPE. Same NOT-a-medical-device basis. General safety governed by EU GPSR 2023/988.
- **ISO 13485 / ISO 9001** — OUT OF SCOPE. No PRD or Regulatory Map mandate; QMS is an organizational attribute. Responsible: Operations / Manufacturing team.
- **IPC PCB Design Standards** — OUT OF SCOPE. No PRD source; PCB implementation is a design-choice in Altium Designer 24.
- **RTOS-Specific Software Standard** — OUT OF SCOPE. No PRD source; RTOS selection (Zephyr-preferred) is a firmware-team implementation choice.
- **EU Battery Regulation Art 11 (Removability)** — CONTINGENT. Potential conflict with non-swappable design; [ASSUMPTION: A-0013] tracks INDICATIVE exemption. Responsible: Regulatory Affairs, via EU counsel.
- **GNSS Intentional-Radiator Exemption** — CONTINGENT. RM-0009 UNCERTAIN, escalated to user.
- **ASTM F2727** — EXCLUDED AS MISCITATION. Corrected to ASTM F2056 per RM-0030. |

## 18. Regulatory

# §18 — Regulatory Certification & Market Pathways

****Pipeline:** Feasibility PASS (46/46) · V-Method PASS (46/46) · Intra-Conflict COMPLETE (/0029) · RTM ADD-ROW COMPLETE (323→369)

§18 (REG) answers "what certifications/approvals are needed to place the product on each market" — distinct from §17 (COMP), which binds the design to the underlying technical standards.

## Requirement Summary

| Part | Markets | Reqs | ID Range |
| :--- | :------ | :--- | :------- |
| A | US + Canada | 13 | REG-0001–0013 |
| B | EU/EEA + UK | 22 | REG-0014–0035 |
| B (Addendum) | EU+UK GNSS | 2 | REG-0045–0046 |
| C | AU/NZ + Global | 9 | REG-0036–0044 |
| **Total** | **5+ markets** | **46** | **REG-0001–0046** |

---

## Part A — US + Canada (REG-0001–0013)

### 18.A.1 United States Market

<a id="srs-reg-0001"></a>

| **SRS-REG-0001** | **FCC Part 15 Subpart C Certification Hold (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Body (TCB) prior to commercial distribution in the US market. \| |
| **Rationale**    | FCC 47 CFR Part 15 Subpart C §15.247 mandates third-party TCB certification (not self-declaration) for intentional radiators in the 2.4 GHz band; this is the market-access instrument corresponding to the technical conformance already required by SRS-COMP-0018. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0018 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0001 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **FCC Part 15 Subpart B Supplier's Declaration of Conformity (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions prior to commercial distribution. \| |
| **Rationale**    | FCC 47 CFR Part 15 Subpart B §15.107/§15.109 permits self-declaration rather than TCB certification for unintentional-emitter compliance. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0019 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0002 |

<a id="srs-reg-0003"></a>

| **SRS-REG-0003** | **FCC Identifier Marking (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the US market. \| |
| **Rationale**    | FCC ID marking is a mandatory labeling condition attached to the Part 15 Subpart C certification. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0001 |

<a id="srs-reg-0004"></a>

| **SRS-REG-0004** | **NRTL Listing Hold for Base Station Electrical Safety (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. \| |
| **Rationale**    | US retail market access for mains-powered electronic equipment requires NRTL listing. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0009 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0013 |

<a id="srs-reg-0005"></a>

| **SRS-REG-0005** | **California Proposition 65 Conditional Warning Labeling (US-CA)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is present above the applicable safe-harbor threshold, prior to commercial distribution in the US-CA market. \| |
| **Rationale**    | Proposition 65 imposes a conditional warning-labeling obligation that is procedurally distinct from the underlying materials-conformance requirement. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0024 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0026 |

<a id="srs-reg-0006"></a>

| **SRS-REG-0006** | **Certification Documentation Package Availability (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support FCC TCB certification (SRS-REG-0001) and NRTL listing (SRS-REG-0004) prior to submission for either certification. \| |
| **Rationale**    | Captures the delivering engineering team's own in-scope interface obligation toward the externally-executed certification processes, ensuring external TCB/NRTL bodies are not blocked by missing inputs. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001, SRS-REG-0004 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: us_certification_documentation_owner |

<a id="srs-reg-0007"></a>

| **SRS-REG-0007** | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to commercial distribution in the US market. \| |
| **Rationale**    | RM-0009 is UNCERTAIN; this block requires only that the determination be made and documented, rather than asserting a specific exemption outcome. \| Verification Method: Analysis \| Cross-References: SRS-REG-0001 | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0009 |

<a id="srs-reg-0008"></a>

| **SRS-REG-0008** | **ISED Certification Hold (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen prior to commercial distribution in the Canada market. \| |
| **Rationale**    | ISED RSS-247 governs 2.4 GHz license-exempt radio equipment and RSS-Gen sets general certification procedure. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0018, SRS-COMP-0016 | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0009"></a>

| **SRS-REG-0009** | **ISED ICES-003 Compliance (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to commercial distribution. \| |
| **Rationale**    | ICES-003 is Canada's counterpart to the US FCC Part 15 Subpart B self-declaration regime. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0019, SRS-REG-0002 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0010"></a>

| **SRS-REG-0010** | **Innovation Canada Identifier Marking (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the Canada market. \| |
| **Rationale**    | IC ID marking is a mandatory labeling condition attached to the ISED certification. \| Verification Method: Inspection \| Cross-References: SRS-REG-0008 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0011"></a>

| **SRS-REG-0011** | **Certification Documentation Package Availability (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support ISED certification (SRS-REG-0008) prior to submission. \| |
| **Rationale**    | Mirrors SRS-REG-0006 for the Canada market. \| Verification Method: Inspection \| Cross-References: SRS-REG-0008 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: canada_certification_documentation_owner |

<a id="srs-reg-0012"></a>

| **SRS-REG-0012** | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to commercial distribution in the Canada market. \| |
| **Rationale**    | Mirrors SRS-REG-0007; RM-0009's UNCERTAIN status is per-market and applies independently to Canada. \| Verification Method: Analysis \| Cross-References: SRS-REG-0008, SRS-REG-0007 | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0009 |

<a id="srs-reg-0013"></a>

| **SRS-REG-0013** | **Pre-Launch Certification-Status Gate (US + Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identified in SRS-REG-0001 through SRS-REG-0012 applicable to that market are complete and on file. \| |
| **Rationale**    | Umbrella gate preventing partial or premature market release. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001–0012 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 |

<a id="srs-reg-0014"></a>

| **SRS-REG-0014** | **RED 2014/53/EU Declaration of Conformity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | CE marking prerequisite for radio equipment. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0020, SRS-COMP-0016 |

<a id="srs-reg-0015"></a>

| **SRS-REG-0015** | **EU Notified Body Engagement Applicability Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Conditional on harmonised standard OJ listing. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0014 |

<a id="srs-reg-0016"></a>

| **SRS-REG-0016** | **CE Marking Physical Application** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On device or packaging. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0014, SRS-REG-0017 |

<a id="srs-reg-0017"></a>

| **SRS-REG-0017** | **EU GPSR General Product Safety Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | GPSR 2023/988 Art 5/6. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · §7 SAFE blocks |

<a id="srs-reg-0018"></a>

| **SRS-REG-0018** | **EU Authorized Representative Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | GPSR Art 4 / RED Art 11. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 |

<a id="srs-reg-0019"></a>

| **SRS-REG-0019** | **EU Technical Documentation File Availability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-scope interface obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0014, SRS-REG-0017 |

<a id="srs-reg-0020"></a>

| **SRS-REG-0020** | **RoHS Self-Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | 2011/65/EU + 2015/863. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0023 |

<a id="srs-reg-0021"></a>

| **SRS-REG-0021** | **WEEE Producer Registration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Per-member-state. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0026 |

<a id="srs-reg-0022"></a>

| **SRS-REG-0022** | **REACH SVHC Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Annex XVII. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0022 |

<a id="srs-reg-0023"></a>

| **SRS-REG-0023** | **EU Battery Regulation Labelling and CE Marking** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2023/1542 Art 6. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0025 |

<a id="srs-reg-0024"></a>

| **SRS-REG-0024** | **EU Battery Regulation Article 11 Removability Exemption Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Deadline 18 Feb 2027. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-COMP-0025, A-0013 |

<a id="srs-reg-0025"></a>

| **SRS-REG-0025** | **EU Cyber Resilience Act Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2024/2847 Annex I + Art 13–14. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0010, SRS-SEC-0006, SRS-MAINT-0003 |

<a id="srs-reg-0026"></a>

| **SRS-REG-0026** | **GDPR Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2016/679 + Art 30. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · §9 DATA blocks |

<a id="srs-reg-0027"></a>

| **SRS-REG-0027** | **EU Packaging and Packaging Waste Regulation Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | PPWR. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0027 |

<a id="srs-reg-0028"></a>

| **SRS-REG-0028** | **UKCA Marking Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK SI 2017/1206. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0020 |

<a id="srs-reg-0029"></a>

| **SRS-REG-0029** | **UK Approved Body Engagement Applicability Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Conditional. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0028, SRS-REG-0015 |

<a id="srs-reg-0030"></a>

| **SRS-REG-0030** | **UK Responsible Person Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK establishment requirement. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0028, SRS-REG-0018 |

<a id="srs-reg-0031"></a>

| **SRS-REG-0031** | **UK PSTI Act 2022 Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0010, SRS-REG-0025 |

<a id="srs-reg-0032"></a>

| **SRS-REG-0032** | **UK GDPR Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK GDPR + DPA 2018. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0026 |

<a id="srs-reg-0033"></a>

| **SRS-REG-0033** | **UK Materials and Environmental Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK REACH, UK RoHS, UK WEEE. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0022/0023/0026 |

<a id="srs-reg-0034"></a>

| **SRS-REG-0034** | **UK Producer Responsibility Packaging Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0027, SRS-REG-0027 |

<a id="srs-reg-0035"></a>

| **SRS-REG-0035** | **Pre-Launch Certification-Status Gate (EU + UK)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · REG-0013, REG-0014–0034, REG-0045, REG-0046 |

<a id="srs-reg-0045"></a>

| **SRS-REG-0045** | **GNSS Exemption Determination (EU)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0009 · SRS-REG-0014, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="srs-reg-0046"></a>

| **SRS-REG-0046** | **GNSS Exemption Determination (UK)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0009 · SRS-REG-0028, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="srs-reg-0036"></a>

| **SRS-REG-0036** | **RCM Marking Declaration (AU/NZ)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | AS/NZS 4268:2017. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0016 |

<a id="srs-reg-0037"></a>

| **SRS-REG-0037** | **ACMA Supplier Code Registration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Precondition to RCM. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0036 |

<a id="srs-reg-0038"></a>

| **SRS-REG-0038** | **AU/NZ Responsible Supplier Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-market required. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0018, SRS-REG-0030 |

<a id="srs-reg-0039"></a>

| **SRS-REG-0039** | **AU/NZ Certification Documentation Package** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-scope interface obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0036/0037 |

<a id="srs-reg-0040"></a>

| **SRS-REG-0040** | **GNSS Exemption Determination (AU/NZ)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | RM-0009 UNCERTAIN. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0007/0012 |

<a id="srs-reg-0041"></a>

| **SRS-REG-0041** | **CCPA/CPRA Contingent Market-Access Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Threshold-contingent. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-DATA-0022 |

<a id="srs-reg-0042"></a>

| **SRS-REG-0042** | **Post-Certification Regulatory-Change Monitoring** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Lifetime obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-MAINT-0002/0003 |

<a id="srs-reg-0043"></a>

| **SRS-REG-0043** | **Certification and DoC Archival Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Per-market minimum. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · A-0025 |

<a id="srs-reg-0044"></a>

| **SRS-REG-0044** | **Pre-Launch Certification-Status Gate (All Markets)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Consolidating gate. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · REG-0013, REG-0035, REG-0036–0043, REG-0045, REG-0046 |


---


---


---


## 2.4 General Constraints — Cross-Variant Standards Requirements

<a id="srs-comp-0001"></a>

| **SRS-COMP-0001** | **Require collar-agnostic base station firmware** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Base Station firmware **shall** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. |
| **Rationale**    | Derived from PRD §4.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.3 · SRS-COMP-0002 |

<a id="srs-comp-0002"></a>

| **SRS-COMP-0002** | **Require universal CCF-to-device mechanical compatibility** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **shall** be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. |
| **Rationale**    | Derived from PRD §4.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 · SRS-COMP-0001 |

<a id="srs-comp-0003"></a>

| **SRS-COMP-0003** | **Require equivalent behavioral-classification outputs across collar variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini and Max collar variants **shall** exhibit equivalent behavioral-classification outputs. |
| **Rationale**    | Derived from PRD §4.3 — ensures classification consistency regardless of variant. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0001 |

<a id="srs-comp-0031"></a>

| **SRS-COMP-0031** | **Require interoperable common BLE communication protocol across variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini and Max collar variants **shall** use an interoperable common BLE communication protocol. |
| **Rationale**    | Derived from PRD §4.3 — ensures cross-variant protocol compatibility. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0003 |<a id="srs-func-0001"></a>

| **SRS-FUNC-0001** | **Detect CCF breakaway/separation signature** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event record to non-volatile storage within 5 s of the separation event, with a false-positive rate not exceeding 0.1% per device-wear-day and a true-event detection rate of at least 99% under DVT drop/tension conditions. |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · SRS-FUNC-0002, SRS-FUNC-0003, SRS-OPER-0008 |

---


## Appendix B. Regulatory Map

The Regulatory Map enumerates 31 regulatory instruments (RM-0001–RM-0031) across five target markets. The full map is maintained in the project repository.

```
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
| RM-0005 | UK Radio Equipment Regs 2017 (SI 2017/1206)                                               | —                     | UK                      | Mini/Max/Base | CONFIRMED  | UKCA.                                                                                                                                                                                               
```

---

