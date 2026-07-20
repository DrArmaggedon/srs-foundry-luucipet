> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

CAT: **COMP** | Maps to: PRD §13.1, §13.3, §13.4, §13.7, §12.6, §9.5
*(Drafter-authored; §17 v1 — 24 blocks, SRS-COMP-0005–0028. COMP-0001–0004 previously consumed in §2.)*

## 17.0 Scope Note

This section binds the product design to the named technical standards whose test methods, clauses, or provisions underlie requirements already issued in §§5–16. §17 (COMP) answers "what standards does this design conform to"; §18 (REG) answers "what market certifications/approvals are needed."

## 17.1 Ingress Protection

**SRS-COMP-0005** | IEC 60529 Ingress Protection Standard Conformance | The collar device, in its standalone (CCF-unmated) configuration, shall conform to the IEC 60529 IPX7 test methodology as the verification basis for the IP67 ingress-protection rating required by SRS-HW-0003. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.4], [STD: RM-0028] | VM: Inspection | XR: SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007

## 17.2 Battery & Electrical Safety

**SRS-COMP-0006** | IEC 62133-2 Battery Cell Safety Standard Conformance | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). | Priority: CRITICAL | Stability: LIKELY-CHANGE | Source: [PRD §13.3], [STD: RM-0011] | VM: Inspection | XR: —

**SRS-COMP-0007** | UN 38.3 Battery Transport Safety Standard Conformance | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.4], [PRD §13.3], [STD: RM-0010] | VM: Inspection | XR: SRS-COMP-0006

**SRS-COMP-0008** | UL 1642/UL 2054 US Cell Safety Standard Conformance | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable to cell construction, for placement on the US market. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.3], [STD: RM-0012] | VM: Inspection | XR: SRS-COMP-0006

**SRS-COMP-0009** | EN 62368-1/UL 62368-1 Base Station Electrical Safety Standard Conformance | The Base Station, in both Charging and Relay tiers, shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.3], [STD: RM-0013] | VM: Inspection | XR: —

## 17.3 IoT Cybersecurity Baseline

**SRS-COMP-0010** | ETSI EN 303 645 Consumer IoT Security Baseline Conformance | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. | Priority: CRITICAL | Stability: LIKELY-CHANGE | Source: [PRD §12.3], [PRD §13.5], [STD: RM-0019] | VM: Inspection | XR: SRS-SEC-0001 through SRS-SEC-0006

## 17.4 Environmental Test-Method Series (IEC 60068-2)

**SRS-COMP-0011** | IEC 60068-2-14 Thermal-Cycling Test Standard Conformance | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.5], [STD: RM-0028], [ASSUMPTION: A-0003] | VM: Inspection | XR: SRS-ENV-0003

**SRS-COMP-0012** | IEC 60068-2-78 Damp-Heat Test Standard Conformance | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §13.4], [STD: RM-0028] | VM: Inspection | XR: SRS-ENV-0004

**SRS-COMP-0013** | IEC 60068-2-27 Mechanical Shock Test Standard Conformance | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §13.4], [STD: RM-0028] | VM: Inspection | XR: SRS-ENV-0010

**SRS-COMP-0014** | IEC 60068-2-64 Vibration Test Standard Conformance | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §13.4], [STD: RM-0028] | VM: Inspection | XR: SRS-ENV-0011

**SRS-COMP-0015** | IEC 60068-2-5 UV-Aging Test Standard Conformance | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.5], [STD: RM-0028] | VM: Inspection | XR: SRS-ENV-0013

## 17.5 Radio / EMC

**SRS-COMP-0016** | ETSI EN 300 328 2.4 GHz Radio Standard Conformance | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.1], [STD: RM-0004] | VM: Inspection | XR: SRS-CONN-0001, SRS-CONN-0002, SRS-CONN-0007

**SRS-COMP-0017** | Bluetooth SIG Qualification Conformance | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.1], [STD: RM-0008] | VM: Inspection | XR: SRS-COMP-0016

**SRS-COMP-0018** | FCC Part 15 Subpart C Intentional Radiator Standard Conformance | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.1], [STD: RM-0001] | VM: Inspection | XR: SRS-COMP-0016

**SRS-COMP-0019** | FCC Part 15 Subpart B Unintentional Radiator Standard Conformance | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.1], [STD: RM-0002] | VM: Inspection | XR: SRS-COMP-0018

**SRS-COMP-0020** | RED 2014/53/EU Essential Requirements Conformance | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.1], [STD: RM-0003] | VM: Inspection | XR: SRS-COMP-0016, SRS-COMP-0010

**SRS-COMP-0021** | RF Human-Exposure Standard Conformance (Contingent) | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applicable. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [PRD §13.1], [STD: RM-0029] | VM: Analysis | XR: —

## 17.6 Materials Compliance

**SRS-COMP-0022** | REACH Regulation Conformance | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.2], [PRD §13.2], [PRD §13.7], [STD: RM-0026] | VM: Inspection | XR: SRS-SAFE-0021

**SRS-COMP-0023** | RoHS Directive Conformance | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.7], [STD: RM-0026] | VM: Inspection | XR: SRS-COMP-0022

**SRS-COMP-0024** | California Proposition 65 Conformance | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.7], [STD: RM-0026] | VM: Inspection | XR: SRS-COMP-0022, SRS-COMP-0023

**SRS-COMP-0025** | EU Battery Regulation Material and Labelling Conformance | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.7], [STD: RM-0014] | VM: Inspection | XR: —

**SRS-COMP-0026** | WEEE Directive Conformance | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.7], [STD: RM-0027] | VM: Inspection | XR: —

**SRS-COMP-0027** | EU PPWR / UK Producer Responsibility Packaging Conformance | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [PRD §13.7], [STD: RM-0027] | VM: Inspection | XR: SRS-COMP-0026

## 17.7 Software & Quality Management

**SRS-COMP-0028** | SBOM Machine-Readable Format Conformance | The SBOM produced at each OTA release (SRS-FUNC-0061) and maintained across the supported service lifetime (SRS-MAINT-0002) shall be issued in a machine-readable format conforming to SPDX 2.3 or CycloneDX. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [PRD §9.5], [PRD §12.7], [PRD — ABSENT: sbom_format_standard] | VM: Inspection | XR: SRS-FUNC-0061, SRS-MAINT-0002

## 17.8 Out-of-Scope Standards (Explicit Attribution)

- **IEC 62304** — OUT OF SCOPE. Product is general-wellness for animals, not a medical device. Responsible: Regulatory Affairs / Product Management.
- **ISO 14971** — OUT OF SCOPE. Same NOT-a-medical-device basis. General safety governed by EU GPSR 2023/988.
- **ISO 13485 / ISO 9001** — OUT OF SCOPE. No PRD or Regulatory Map mandate; QMS is an organizational attribute. Responsible: Operations / Manufacturing team.
- **IPC PCB Design Standards** — OUT OF SCOPE. No PRD source; PCB implementation is a design-choice in Altium Designer 24.
- **RTOS-Specific Software Standard** — OUT OF SCOPE. No PRD source; RTOS selection (Zephyr-preferred) is a firmware-team implementation choice.
- **EU Battery Regulation Art 11 (Removability)** — CONTINGENT. Potential conflict with non-swappable design; [ASSUMPTION: A-0013] tracks INDICATIVE exemption. Responsible: Regulatory Affairs, via EU counsel.
- **GNSS Intentional-Radiator Exemption** — CONTINGENT. RM-0009 UNCERTAIN, escalated to user.
- **ASTM F2727** — EXCLUDED AS MISCITATION. Corrected to ASTM F2056 per RM-0030.
