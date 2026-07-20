
## 15. Operational Requirements

This section specifies operational behavior of the deployed system: Base Station continuous-operation posture and included power accessory, Base Station status-indicator inventory, the device-local home/away determination, collar duty-cycle and power-optimization policies, cloud-loss fallback governance, and the product service lifetime reference.

### 15.1 Base Station Continuous Operation

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0012 | The Base Station shall remain in a continuously powered, non-sleeping operational state for as long as AC power is supplied, maintaining active BLE scanning and Wi-Fi uplink capability at all times. | HIGH | STABLE | Demonstration |
| SRS-OPER-0013 | The Base Station shall be supplied with an AC-to-USB-C power adapter as an included accessory. | MEDIUM | STABLE | Inspection |

### 15.2 Base Station Status Indicators

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0014 | The Base Station (Charging) tier shall provide exactly 3 status LEDs, indicating at minimum: AC power presence, device-charging activity, and cloud-connectivity status. | HIGH | STABLE | Inspection |
| SRS-OPER-0015 | The Base Station (Relay) tier shall provide exactly 2 status LEDs, indicating at minimum: AC power presence and cloud-connectivity status. | HIGH | STABLE | Inspection |

### 15.3 Household Geo-Fence Mesh Participation

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0016 | Every Base Station in a household deployment shall participate in a shared geo-fence mesh by independently reporting BLE sighting reports for every collar device within its range. | HIGH | STABLE | Demonstration |

### 15.4 Device-Local Home/Away Determination

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0017 | The collar device shall determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) readings from paired Base Stations in range, without reliance on any cloud-side determination. | HIGH | STABLE | Demonstration |
| SRS-OPER-0018 | The collar device's device-local home/away state machine shall transition from HOME to AWAY only when no paired Base Station RSSI reading exceeds −85 dBm for 5 consecutive readings taken at 1-second intervals. | MEDIUM | LIKELY-CHANGE | Test |
| SRS-OPER-0024 | The collar device's device-local home/away state machine shall transition from AWAY to HOME only when at least one paired Base Station RSSI reading exceeds −80 dBm for 3 consecutive readings taken at 1-second intervals. | MEDIUM | LIKELY-CHANGE | Test |

### 15.5 Collar Duty-Cycle and Power-Optimization Policy

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0019 | The collar device, while in Wellness Mode and not actively processing a motion-triggered confirmation burst, shall remain in its deepest available low-power idle state. | HIGH | STABLE | Analysis |
| SRS-OPER-0020 | When the owner changes the Max collar variant's configured GNSS fix interval, the collar device shall apply the new interval no later than the start of the next scheduled fix-acquisition cycle. | MEDIUM | STABLE | Test |
| SRS-OPER-0021 | Battery-life validation testing shall be performed using cells that have completed no fewer than 50 charge/discharge cycles prior to the validation measurement. | MEDIUM | STABLE | Test |

### 15.6 Cloud-Loss Fallback Governance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0022 | The collar device shall rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the Base Station has not had successful cloud contact for more than 24 hours. | MEDIUM | STABLE | Analysis |

### 15.7 Product Service Lifetime Reference

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0023 | The system's operational and durability requirements that reference an expected service lifetime shall use 2 years as the minimum testable floor. | MEDIUM | STABLE | Inspection |

---

## 16. Maintainability Requirements

This section specifies the lifetime-maintenance obligations for the LUUCIPet system: OTA-update capability availability through the supported service lifetime, SBOM currency, and post-launch vulnerability-disclosure process continuity.

### 16.1 OTA-Update Capability Lifetime

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-MAINT-0001 | The system shall retain OTA update capability, for both collar variants and both Base Station tiers, for no less than 2 years from product launch. | HIGH | STABLE | Inspection |

### 16.2 SBOM Lifetime Currency

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-MAINT-0002 | The system's Software Bill of Materials shall be kept current for each in-support firmware version throughout the 2-year supported service lifetime. | MEDIUM | STABLE | Inspection |

### 16.3 Post-Launch Vulnerability-Disclosure Process Continuity

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-MAINT-0003 | The public vulnerability-disclosure policy required by SRS-SEC-0006 shall remain active and operational for no less than the 2-year supported service lifetime. | HIGH | STABLE | Inspection |

---

## 17. Standards Conformance

This section binds the product design to the named technical standards whose test methods, clauses, or provisions underlie requirements already issued in Sections 5 through 16. It answers "what standards does this design conform to" — distinct from Section 18, which answers "what market certifications/approvals are needed."

### 17.1 Ingress Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0005 | The collar device, in its standalone (CCF-unmated) configuration, shall conform to IEC 60529 IPX7 test methodology as the verification basis for the IP67 ingress-protection rating. | CRITICAL | STABLE | Inspection |

### 17.2 Battery and Electrical Safety

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0006 | The Li-Po battery cells shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). | CRITICAL | LIKELY-CHANGE | Inspection |
| SRS-COMP-0007 | The Li-Po battery cells shall conform to UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0008 | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable, for placement on the US market. | HIGH | STABLE | Inspection |
| SRS-COMP-0009 | The Base Station shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. | CRITICAL | STABLE | Inspection |

### 17.3 IoT Cybersecurity Baseline

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0010 | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard. | CRITICAL | LIKELY-CHANGE | Inspection |

### 17.4 Environmental Test-Method Series (IEC 60068-2)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0011 | The CCF thermal-cycling exposure qualification shall be conducted per IEC 60068-2-14 Test Na. | HIGH | STABLE | Inspection |
| SRS-COMP-0012 | The collar device damp-heat exposure qualification shall be conducted per IEC 60068-2-78. | MEDIUM | STABLE | Inspection |
| SRS-COMP-0013 | The collar device mechanical-shock exposure qualification shall be conducted per IEC 60068-2-27. | MEDIUM | STABLE | Inspection |
| SRS-COMP-0014 | The collar device vibration exposure qualification shall be conducted per IEC 60068-2-64. | MEDIUM | STABLE | Inspection |
| SRS-COMP-0015 | The CCF UV-aging exposure qualification shall be conducted per IEC 60068-2-5. | HIGH | STABLE | Inspection |

### 17.5 Radio and EMC

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0016 | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0017 | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0018 | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0019 | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. | HIGH | STABLE | Inspection |
| SRS-COMP-0020 | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0021 | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applicable. | HIGH | LIKELY-CHANGE | Analysis |

### 17.6 Materials Compliance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0022 | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0023 | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0024 | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. | HIGH | STABLE | Inspection |
| SRS-COMP-0025 | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. | CRITICAL | STABLE | Inspection |
| SRS-COMP-0026 | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. | HIGH | STABLE | Inspection |
| SRS-COMP-0027 | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. | MEDIUM | LIKELY-CHANGE | Inspection |

### 17.7 Software and Quality Management

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-COMP-0028 | The SBOM produced at each OTA release and maintained across the supported service lifetime shall be issued in a machine-readable format conforming to SPDX 2.3 or CycloneDX. | MEDIUM | LIKELY-CHANGE | Inspection |

### 17.8 Out-of-Scope Standards

The following standards are explicitly excluded from this specification:

- **IEC 62304** — Out of scope. Product is general-wellness for animals, not a medical device.
- **ISO 14971** — Out of scope. Same NOT-a-medical-device basis. General safety governed by EU GPSR 2023/988.
- **ISO 13485 / ISO 9001** — Out of scope. Quality management system standards are organizational attributes, not product requirements.
- **EU Battery Regulation Article 11 (Removability)** — Contingent. Potential conflict with non-swappable design; tracked in Assumption Register.
- **ASTM F2727** — Excluded as miscitation. Corrected to ASTM F2056 per verified regulatory analysis.

---

## 18. Regulatory Certification and Market Pathways

This section answers "what certifications/approvals are needed to place the product on each market" — distinct from Section 17, which binds the design to underlying technical standards. The product targets five primary markets: United States, Canada, European Union/EEA, United Kingdom, and Australia/New Zealand.

### 18.A United States Market

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0001 | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized TCB prior to commercial distribution in the US market. | HIGH | STABLE | Inspection |
| SRS-REG-0002 | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions. | HIGH | STABLE | Inspection |
| SRS-REG-0003 | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or in an accessible electronic display. | HIGH | STABLE | Inspection |
| SRS-REG-0004 | Each Base Station tier shall hold a valid NRTL listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. | HIGH | STABLE | Inspection |
| SRS-REG-0005 | The system shall bear a California Proposition 65 warning label if any listed substance is present above the applicable safe-harbor threshold. | HIGH | STABLE | Inspection |
| SRS-REG-0006 | The system shall be accompanied by a complete technical documentation package sufficient to support FCC TCB certification and NRTL listing. | HIGH | STABLE | Inspection |
| SRS-REG-0007 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption. | HIGH | VOLATILE | Analysis |

### 18.A.2 Canada Market

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0008 | The BLE and Wi-Fi radio modules shall hold a valid ISED certification under RSS-247 and RSS-Gen prior to commercial distribution in Canada. | HIGH | LIKELY-CHANGE | Inspection |
| SRS-REG-0009 | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions. | HIGH | STABLE | Inspection |
| SRS-REG-0010 | Each collar variant and Base Station tier shall bear a unique IC ID on the device enclosure or in an accessible electronic display. | HIGH | STABLE | Inspection |
| SRS-REG-0011 | The system shall be accompanied by a complete technical documentation package sufficient to support ISED certification. | HIGH | STABLE | Inspection |
| SRS-REG-0012 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption. | HIGH | VOLATILE | Analysis |

### 18.A.3 US and Canada Cross-Market Gate

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0013 | The system shall not be released for commercial distribution into the US or Canada market until all applicable certifications, declarations, and markings are complete and on file. | HIGH | STABLE | Inspection |

### 18.B European Union / EEA Market

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0014 | The system shall hold a valid RED 2014/53/EU Declaration of Conformity as the CE-marking prerequisite for radio equipment. | CRITICAL | STABLE | Inspection |
| SRS-REG-0015 | The system shall undergo an EU Notified Body engagement applicability determination, conditional on harmonised standard listing in the Official Journal. | HIGH | VOLATILE | Analysis |
| SRS-REG-0016 | The CE marking shall be physically applied to the device or its packaging. | HIGH | STABLE | Inspection |
| SRS-REG-0017 | The system shall conform to EU GPSR 2023/988 as the general product safety compliance basis. | CRITICAL | STABLE | Inspection |
| SRS-REG-0018 | An EU Authorized Representative shall be designated per GPSR Article 4 and RED Article 11. | HIGH | STABLE | Inspection |
| SRS-REG-0019 | A complete EU technical documentation file shall be available as the in-scope interface obligation toward certification processes. | HIGH | STABLE | Inspection |
| SRS-REG-0020 | The system shall be placed on the EU market under a RoHS self-declaration per 2011/65/EU and 2015/863. | HIGH | STABLE | Inspection |
| SRS-REG-0021 | WEEE producer registration shall be completed per member-state requirements. | HIGH | STABLE | Inspection |
| SRS-REG-0022 | A REACH SVHC declaration shall be issued per Annex XVII. | HIGH | STABLE | Inspection |
| SRS-REG-0023 | Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 labelling and CE marking provisions. | CRITICAL | STABLE | Inspection |
| SRS-REG-0024 | An EU Battery Regulation Article 11 removability exemption determination shall be completed before the 18 February 2027 deadline. | CRITICAL | VOLATILE | Analysis |
| SRS-REG-0025 | The system shall hold an EU Cyber Resilience Act (EU) 2024/2847 compliance declaration covering Annex I and Articles 13–14. | CRITICAL | LIKELY-CHANGE | Inspection |
| SRS-REG-0026 | The system shall comply with GDPR (EU) 2016/679 as the data-protection compliance basis. | CRITICAL | STABLE | Inspection |
| SRS-REG-0027 | An EU Packaging and Packaging Waste Regulation (PPWR) compliance declaration shall be issued. | MEDIUM | LIKELY-CHANGE | Inspection |

### 18.B.2 United Kingdom Market

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0028 | The system shall hold a UKCA marking declaration per UK SI 2017/1206. | CRITICAL | STABLE | Inspection |
| SRS-REG-0029 | The system shall undergo a UK Approved Body engagement applicability determination. | HIGH | VOLATILE | Analysis |
| SRS-REG-0030 | A UK Responsible Person shall be designated per UK establishment requirement. | HIGH | STABLE | Inspection |
| SRS-REG-0031 | The system shall hold a UK PSTI Act 2022 compliance declaration. | CRITICAL | STABLE | Inspection |
| SRS-REG-0032 | The system shall comply with UK GDPR and Data Protection Act 2018. | CRITICAL | STABLE | Inspection |
| SRS-REG-0033 | The system shall hold UK REACH, UK RoHS, and UK WEEE compliance declarations. | HIGH | STABLE | Inspection |
| SRS-REG-0034 | A UK Producer Responsibility packaging compliance declaration shall be issued. | MEDIUM | LIKELY-CHANGE | Inspection |

### 18.B.3 EU and UK Cross-Market Gate

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0035 | The system shall not be released for commercial distribution into the EU or UK market until all applicable certifications, declarations, and markings are complete and on file. | CRITICAL | STABLE | Inspection |

### 18.B Addendum — GNSS Exemption (EU and UK)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0045 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for RED intentional-radiator exemption prior to commercial distribution in the EU. | HIGH | VOLATILE | Analysis |
| SRS-REG-0046 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for UK radio-equipment intentional-radiator exemption prior to commercial distribution in the United Kingdom. | HIGH | VOLATILE | Analysis |

### 18.C Australia / New Zealand Market

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0036 | The system shall hold an RCM marking declaration per AS/NZS 4268:2017. | HIGH | LIKELY-CHANGE | Inspection |
| SRS-REG-0037 | An ACMA Supplier Code registration shall be obtained as precondition to RCM marking. | HIGH | STABLE | Inspection |
| SRS-REG-0038 | An AU/NZ Responsible Supplier shall be designated. | HIGH | STABLE | Inspection |
| SRS-REG-0039 | A complete AU/NZ certification documentation package shall be available. | HIGH | STABLE | Inspection |
| SRS-REG-0040 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for AU/NZ intentional-radiator exemption. | HIGH | VOLATILE | Analysis |

### 18.C.2 Global Cross-Cutting Obligations

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0041 | Where applicable CCPA/CPRA thresholds are met, a CCPA/CPRA contingent market-access declaration shall be issued. | MEDIUM | LIKELY-CHANGE | Analysis |
| SRS-REG-0042 | Post-certification regulatory-change monitoring shall be maintained as a lifetime obligation. | HIGH | STABLE | Inspection |
| SRS-REG-0043 | Certification and Declaration of Conformity documentation shall be archived per applicable market minimum retention periods. | HIGH | LIKELY-CHANGE | Inspection |

### 18.C.3 Global Cross-Market Gate

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0044 | The system shall not be released for commercial distribution into any target market until all certifications, declarations, and markings applicable to that market are complete and on file. | CRITICAL | STABLE | Inspection |

