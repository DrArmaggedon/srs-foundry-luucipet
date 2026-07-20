> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# §18 — Regulatory Certification & Market Pathways

**CAT: REG** · **46 blocks (REG-0001–0046)** · **Status: APPROVED**
**Pipeline:** Feasibility PASS (46/46) · V-Method PASS (46/46) · Intra-Conflict COMPLETE (CR-0028/0029) · RTM ADD-ROW COMPLETE (323→369)

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

**SRS-REG-0001** | FCC Part 15 Subpart C Certification Hold (US) | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Body (TCB) prior to commercial distribution in the US market. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0001], [PRD §13.1] | Rationale: FCC 47 CFR Part 15 Subpart C §15.247 mandates third-party TCB certification (not self-declaration) for intentional radiators in the 2.4 GHz band; this is the market-access instrument corresponding to the technical conformance already required by SRS-COMP-0018. | Verification Method: Inspection | Cross-References: SRS-COMP-0018

**SRS-REG-0002** | FCC Part 15 Subpart B Supplier's Declaration of Conformity (US) | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions prior to commercial distribution. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0002], [PRD §13.1] | Rationale: FCC 47 CFR Part 15 Subpart B §15.107/§15.109 permits self-declaration rather than TCB certification for unintentional-emitter compliance. | Verification Method: Inspection | Cross-References: SRS-COMP-0019

**SRS-REG-0003** | FCC Identifier Marking (US) | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the US market. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0001], [PRD §13.1] | Rationale: FCC ID marking is a mandatory labeling condition attached to the Part 15 Subpart C certification. | Verification Method: Inspection | Cross-References: SRS-REG-0001

**SRS-REG-0004** | NRTL Listing Hold for Base Station Electrical Safety (US) | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0013], [PRD §13.3] | Rationale: US retail market access for mains-powered electronic equipment requires NRTL listing. | Verification Method: Inspection | Cross-References: SRS-COMP-0009

**SRS-REG-0005** | California Proposition 65 Conditional Warning Labeling (US-CA) | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is present above the applicable safe-harbor threshold, prior to commercial distribution in the US-CA market. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0026], [PRD §13.7] | Rationale: Proposition 65 imposes a conditional warning-labeling obligation that is procedurally distinct from the underlying materials-conformance requirement. | Verification Method: Inspection | Cross-References: SRS-COMP-0024

**SRS-REG-0006** | Certification Documentation Package Availability (US) | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support FCC TCB certification (SRS-REG-0001) and NRTL listing (SRS-REG-0004) prior to submission for either certification. | Priority: HIGH | Stability: STABLE | Source: [PRD — ABSENT: us_certification_documentation_owner], [STD: RM-0001], [STD: RM-0013] | Rationale: Captures the delivering engineering team's own in-scope interface obligation toward the externally-executed certification processes, ensuring external TCB/NRTL bodies are not blocked by missing inputs. | Verification Method: Inspection | Cross-References: SRS-REG-0001, SRS-REG-0004

**SRS-REG-0007** | GNSS Passive-Receiver Intentional-Radiator Exemption Determination (US) | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to commercial distribution in the US market. | Priority: HIGH | Stability: VOLATILE | Source: [STD: RM-0009], [PRD §13.1] | Rationale: RM-0009 is UNCERTAIN; this block requires only that the determination be made and documented, rather than asserting a specific exemption outcome. | Verification Method: Analysis | Cross-References: SRS-REG-0001

### 18.A.2 Canada Market

**SRS-REG-0008** | ISED Certification Hold (Canada) | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen prior to commercial distribution in the Canada market. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [STD: RM-0006], [PRD §13.1] | Rationale: ISED RSS-247 governs 2.4 GHz license-exempt radio equipment and RSS-Gen sets general certification procedure. | Verification Method: Inspection | Cross-References: SRS-COMP-0018, SRS-COMP-0016

**SRS-REG-0009** | ISED ICES-003 Compliance (Canada) | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to commercial distribution. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0006], [PRD §13.1] | Rationale: ICES-003 is Canada's counterpart to the US FCC Part 15 Subpart B self-declaration regime. | Verification Method: Inspection | Cross-References: SRS-COMP-0019, SRS-REG-0002

**SRS-REG-0010** | Innovation Canada Identifier Marking (Canada) | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the Canada market. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0006], [PRD §13.1] | Rationale: IC ID marking is a mandatory labeling condition attached to the ISED certification. | Verification Method: Inspection | Cross-References: SRS-REG-0008

**SRS-REG-0011** | Certification Documentation Package Availability (Canada) | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support ISED certification (SRS-REG-0008) prior to submission. | Priority: HIGH | Stability: STABLE | Source: [PRD — ABSENT: canada_certification_documentation_owner], [STD: RM-0006] | Rationale: Mirrors SRS-REG-0006 for the Canada market. | Verification Method: Inspection | Cross-References: SRS-REG-0008

**SRS-REG-0012** | GNSS Passive-Receiver Intentional-Radiator Exemption Determination (Canada) | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to commercial distribution in the Canada market. | Priority: HIGH | Stability: VOLATILE | Source: [STD: RM-0009], [PRD §13.1] | Rationale: Mirrors SRS-REG-0007; RM-0009's UNCERTAIN status is per-market and applies independently to Canada. | Verification Method: Analysis | Cross-References: SRS-REG-0008, SRS-REG-0007

### 18.A.3 Cross-Market Gate

**SRS-REG-0013** | Pre-Launch Certification-Status Gate (US + Canada) | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identified in SRS-REG-0001 through SRS-REG-0012 applicable to that market are complete and on file. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.1], [PRD §13.7] | Rationale: Umbrella gate preventing partial or premature market release. | Verification Method: Inspection | Cross-References: SRS-REG-0001–0012

### 18.A.4 Out-of-Scope Items (Explicit Attribution)

- **FCC TCB certification test execution — OUT OF SCOPE.** Performed by FCC-recognized TCB (external). Delivering team's interface obligation: SRS-REG-0006.
- **NRTL listing test execution — OUT OF SCOPE.** Performed by NRTL laboratory (external). Delivering team's interface obligation: SRS-REG-0006.
- **ISED certification test execution — OUT OF SCOPE.** Performed by ISED-recognized certification body (external). Delivering team's interface obligation: SRS-REG-0011.
- **US/Canada importer of record / responsible-party legal designation — OUT OF SCOPE.** Regulatory Affairs / Import-Compliance function. Delivering team's interface obligation: SRS-REG-0006/0011.
- **US/Canada customs import filing — OUT OF SCOPE.** Logistics / Customs-Broker function.

---

## Part B — EU/EEA + UK (REG-0014–0035)

### 18.B.1 European Union / EEA Market

**SRS-REG-0014** | RED 2014/53/EU Declaration of Conformity | CE marking prerequisite for radio equipment. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0020, SRS-COMP-0016

**SRS-REG-0015** | EU Notified Body Engagement Applicability Determination | Conditional on harmonised standard OJ listing. Priority: HIGH | Stability: VOLATILE | VM: Analysis | XR: SRS-REG-0014

**SRS-REG-0016** | CE Marking Physical Application | On device or packaging. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-REG-0014, SRS-REG-0017

**SRS-REG-0017** | EU GPSR General Product Safety Compliance Basis | GPSR 2023/988 Art 5/6. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: §7 SAFE blocks

**SRS-REG-0018** | EU Authorized Representative Designation | GPSR Art 4 / RED Art 11. Priority: HIGH | Stability: STABLE | VM: Inspection

**SRS-REG-0019** | EU Technical Documentation File Availability | In-scope interface obligation. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-REG-0014, SRS-REG-0017

**SRS-REG-0020** | RoHS Self-Declaration | 2011/65/EU + 2015/863. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0023

**SRS-REG-0021** | WEEE Producer Registration | Per-member-state. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0026

**SRS-REG-0022** | REACH SVHC Declaration | Annex XVII. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0022

**SRS-REG-0023** | EU Battery Regulation Labelling and CE Marking | (EU) 2023/1542 Art 6. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0025

**SRS-REG-0024** | EU Battery Regulation Article 11 Removability Exemption Determination | Deadline 18 Feb 2027. Priority: CRITICAL | Stability: VOLATILE | VM: Analysis | XR: SRS-COMP-0025, A-0013

**SRS-REG-0025** | EU Cyber Resilience Act Compliance Declaration | (EU) 2024/2847 Annex I + Art 13–14. Priority: CRITICAL | Stability: LIKELY-CHANGE | VM: Inspection | XR: SRS-COMP-0010, SRS-SEC-0006, SRS-MAINT-0003

**SRS-REG-0026** | GDPR Compliance Basis | (EU) 2016/679 + Art 30. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: §9 DATA blocks

**SRS-REG-0027** | EU Packaging and Packaging Waste Regulation Compliance Declaration | PPWR. Priority: MEDIUM | Stability: LIKELY-CHANGE | VM: Inspection | XR: SRS-COMP-0027

### 18.B.2 United Kingdom Market

**SRS-REG-0028** | UKCA Marking Declaration | UK SI 2017/1206. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0020

**SRS-REG-0029** | UK Approved Body Engagement Applicability Determination | Conditional. Priority: HIGH | Stability: VOLATILE | VM: Analysis | XR: SRS-REG-0028, SRS-REG-0015

**SRS-REG-0030** | UK Responsible Person Designation | UK establishment requirement. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-REG-0028, SRS-REG-0018

**SRS-REG-0031** | UK PSTI Act 2022 Compliance Declaration | Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0010, SRS-REG-0025

**SRS-REG-0032** | UK GDPR Compliance Basis | UK GDPR + DPA 2018. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: SRS-REG-0026

**SRS-REG-0033** | UK Materials and Environmental Compliance Declaration | UK REACH, UK RoHS, UK WEEE. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-COMP-0022/0023/0026

**SRS-REG-0034** | UK Producer Responsibility Packaging Compliance Declaration | Priority: MEDIUM | Stability: LIKELY-CHANGE | VM: Inspection | XR: SRS-COMP-0027, SRS-REG-0027

### 18.B.3 Cross-Market Gate

**SRS-REG-0035** | Pre-Launch Certification-Status Gate (EU + UK) | Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: REG-0013, REG-0014–0034, REG-0045, REG-0046

### 18.B.4 Out-of-Scope Items (8 items, explicitly attributed)

- EU Notified Body assessment → Notified Body (external)
- UK Approved Body assessment → Approved Body (external)
- EU Authorized Representative ongoing duties → Authorized Rep (external)
- UK Responsible Person ongoing duties → Responsible Person (external)
- Battery Reg Art 11 legal adjudication → Regulatory Affairs / EU counsel
- EU/UK customs import filing → Logistics / Customs-Broker
- GDPR DPO appointment/operation → Regulatory Affairs / Legal
- EU/UK materials lab testing → Testing lab (external)

---

## Part B Addendum — EU+UK GNSS Exemption (REG-0045–0046)

**SRS-REG-0045** | GNSS Exemption Determination (EU) | Priority: HIGH | Stability: VOLATILE | VM: Analysis | Source: [STD: RM-0009], [PRD §13.1] | XR: SRS-REG-0014, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040

**SRS-REG-0046** | GNSS Exemption Determination (UK) | Priority: HIGH | Stability: VOLATILE | VM: Analysis | Source: [STD: RM-0009], [PRD §13.1] | XR: SRS-REG-0028, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040

Closes RM-0009 5-market coverage gap (US/CA/AU-NZ/EU/UK).

---

## Part C — AU/NZ + Global (REG-0036–0044)

### 18.C.1 Australia / New Zealand Market

**SRS-REG-0036** | RCM Marking Declaration (AU/NZ) | AS/NZS 4268:2017. Priority: HIGH | Stability: LIKELY-CHANGE | VM: Inspection | XR: SRS-COMP-0016

**SRS-REG-0037** | ACMA Supplier Code Registration | Precondition to RCM. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-REG-0036

**SRS-REG-0038** | AU/NZ Responsible Supplier Designation | In-market required. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-REG-0018, SRS-REG-0030

**SRS-REG-0039** | AU/NZ Certification Documentation Package | In-scope interface obligation. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-REG-0036/0037

**SRS-REG-0040** | GNSS Exemption Determination (AU/NZ) | RM-0009 UNCERTAIN. Priority: HIGH | Stability: VOLATILE | VM: Analysis | XR: SRS-REG-0007/0012

### 18.C.2 Global Cross-Cutting Obligations

**SRS-REG-0041** | CCPA/CPRA Contingent Market-Access Declaration | Threshold-contingent. Priority: MEDIUM | Stability: LIKELY-CHANGE | VM: Analysis | XR: SRS-DATA-0022

**SRS-REG-0042** | Post-Certification Regulatory-Change Monitoring | Lifetime obligation. Priority: HIGH | Stability: STABLE | VM: Inspection | XR: SRS-MAINT-0002/0003

**SRS-REG-0043** | Certification and DoC Archival Retention | Per-market minimum. Priority: HIGH | Stability: LIKELY-CHANGE | VM: Inspection | XR: A-0025

### 18.C.3 Global Cross-Market Gate

**SRS-REG-0044** | Pre-Launch Certification-Status Gate (All Markets) | Consolidating gate. Priority: CRITICAL | Stability: STABLE | VM: Inspection | XR: REG-0013, REG-0035, REG-0036–0043, REG-0045, REG-0046

### 18.C.4 Out-of-Scope (6 items)

- AU/NZ EMC/electrical-safety mapping → Regulatory Agent (no RM-ID)
- RCM test execution → Accredited lab (external)
- AU/NZ Responsible Supplier duties → Supplier (external)
- Regulatory-change monitoring mechanism → Regulatory Affairs
- Per-market retention period research → Regulatory Affairs / counsel
- AU/NZ customs import filing → Logistics / Customs-Broker

---

## Pipeline Status

| Stage | Verdict | Details |
| :---- | :------ | :------ |
| Draft + Addendum | COMPLETE | 46 blocks (REG-0001–0046) across 4 parts |
| Feasibility | PASS | v1: 44 base. vPOST: 2 addendum. 46/46 PASS |
| V-Method | PASS | 46/46, 0 FAIL. Inspection (market-access artifacts) + Analysis (contingent determinations) |
| Intra-Conflict | COMPLETE | CR-0028 (REG-0035 XR gap), CR-0029 (REG-0044 XR gap) |
| Traceability | COMPLETE | UPDATE-ROW + ADD-ROW: 46 rows. RTM 323→369 |
