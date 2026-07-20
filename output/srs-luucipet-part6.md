
---

## Appendix A — Requirements Traceability Matrix

The Requirements Traceability Matrix (RTM) maps each SRS requirement to its originating source material (PRD section, regulatory standard, or assumption), the verifying requirement category, and the verification method. As approved, 369 RTM rows trace 397 requirements (351 base requirements plus 46 regulatory requirements in Section 18).

### A.1 Traceability Summary

| Category | Count | RTM Rows | Source Mapping |
| :------- | :---- | :------- | :------------- |
| FUNC (Sections 3, 5) | 57 | 57 | PRD §4.4, §7, §9 |
| CONN (Section 4) | 30 | 30 | PRD §6.3–§6.5, §8, §10.3 |
| PERF (Section 6) | 8 | 8 | PRD §7.4, §12.1, §15 |
| SAFE (Section 7) | 22 | 22 | PRD §10.1.3, §10.1.4, §13.2; GPSR 2023/988 |
| SEC (Section 8) | 6 | 6 | PRD §6.7, §12.3; ETSI EN 303 645:2025 |
| DATA (Section 9) | 27 | 27 | PRD §7.5–§7.7, §8, §10.6; GDPR |
| INT (Section 10) | 29 | 29 | PRD §6, §10.2, §10.3, §10.5, §11 |
| COMP-HW (Section 11) | 28 | 28 | PRD §10 |
| ENV (Section 12) | 18 | 18 | PRD §12.5, §13.4; IEC 60068 series |
| RELI (Section 13) | 4 | 4 | PRD §12.2 |
| UX (Section 14) | 29 | 29 | PRD §5, §12.4 |
| OPER (Sections 2, 15) | 24 | 24 | PRD §4.2, §4.5, §6.4, §11, §15 |
| MAINT (Section 16) | 3 | 3 | PRD §12.7 |
| COMP (Sections 2, 17) | 27 | 27 | PRD §13.1, §13.3, §13.4, §13.7 |
| REG (Sections 1, 18) | 48 | 48 | PRD §13; per-market regulatory instruments |
| **TOTAL** | **397** | **369** | |

### A.2 Requirement-to-Source Mapping (Representative Extract)

The complete RTM is maintained in the traceability repository. The following extract illustrates the mapping structure:

| SRS ID | PRD Source | Standard/Regulatory Source | Assumption | Category | Priority |
| :----- | :--------- | :------------------------- | :--------- | :------- | :------- |
| SRS-FUNC-0001 | §10.1.3.6 | — | A-0015, A-0018 | FUNC | CRITICAL |
| SRS-FUNC-0011 | §7.3 | — | — | FUNC | CRITICAL |
| SRS-FUNC-0018 | §7.4 | — | — | FUNC | CRITICAL |
| SRS-CONN-0009 | §6.3 | — | — | CONN | CRITICAL |
| SRS-PERF-0001 | §12.1, §10.4 | — | — | PERF | HIGH |
| SRS-SAFE-0001 | §10.1.3.2b, §13.2 | GPSR 2023/988 Art 5 & Art 6(1)(a) | A-0017 | SAFE | CRITICAL |
| SRS-SEC-0001 | §6.7, §8.2, §12.3 | ETSI EN 303 645:2025 | — | SEC | CRITICAL |
| SRS-DATA-0001 | §7.5 | — | — | DATA | CRITICAL |
| SRS-DATA-0018 | — | GDPR Art 5(1)(c) | — | DATA | HIGH |
| SRS-INT-0001 | §6.3, §8.1, §10.3 | — | — | INT | HIGH |
| SRS-INT-0013 | §13.1 | FCC Part 15C, RED, UK SI 2017/1206, ISED RSS-247, AS/NZS 4268 | — | INT | CRITICAL |
| SRS-HW-0003 | §10.1.2, §13.4 | IEC 60529 | — | COMP-HW | CRITICAL |
| SRS-HW-0020 | §10.4 | — | A-0006 | COMP-HW | HIGH |
| SRS-ENV-0003 | §12.5 | IEC 60068-2-14 | A-0003 | ENV | HIGH |
| SRS-RELI-0001 | §12.2 | — | — | RELI | CRITICAL |
| SRS-UX-0001 | §12.4 | — | — | UX | HIGH |
| SRS-OPER-0017 | §6.4, §4.1 | — | A-0016 | OPER | HIGH |
| SRS-MAINT-0001 | §12.7 | — | — | MAINT | HIGH |
| SRS-COMP-0010 | §12.3, §13.5 | ETSI EN 303 645:2025 | — | COMP | CRITICAL |
| SRS-COMP-0022 | §10.1.2, §13.2, §13.7 | REACH (EC) 1907/2006 | — | COMP | CRITICAL |
| SRS-REG-0001 | §13.6 | — | — | REG | CRITICAL |
| SRS-REG-0014 | §13.1 | RED 2014/53/EU | — | REG | CRITICAL |
| SRS-REG-0025 | §13.5 | EU CRA (EU) 2024/2847 | — | REG | CRITICAL |

---

## Appendix B — Regulatory Compliance Map

This appendix enumerates the regulatory instruments and technical standards that govern the LUUCIPet Wellness Monitor across its five target markets. Confidence classifications reflect the regulatory analysis verification state as of the document baselining date.

### B.1 Summary Tally

| Confidence Level | Count |
| :--------------- | :---- |
| CONFIRMED | 18 |
| INDICATIVE | 9 |
| UNCERTAIN | 3 |
| **Total RM rows** | **30** |

### B.2 Radio and Wireless Standards

| ID | Standard/Regulation | Market | Applies To | Confidence |
| :-- | :------------------ | :----- | :--------- | :--------- |
| RM-0001 | FCC 47 CFR Part 15 Subpart C §15.247 | US | Mini/Max/Base | CONFIRMED |
| RM-0002 | FCC 47 CFR Part 15 Subpart B §15.107/.109 | US | System | CONFIRMED |
| RM-0003 | RED Directive 2014/53/EU Art 3.1(a), 3.1(b), 3.2 | EU | Mini/Max/Base | CONFIRMED |
| RM-0004 | ETSI EN 300 328 §4.3 | EU | Mini/Max/Base | INDICATIVE |
| RM-0005 | UK Radio Equipment Regs 2017 (SI 2017/1206) | UK | Mini/Max/Base | CONFIRMED |
| RM-0006 | ISED RSS-247 Issue 2 + RSS-Gen Issue 5 | CA | Mini/Max/Base | INDICATIVE |
| RM-0007 | AS/NZS 4268:2017 | AU/NZ | Mini/Max/Base | INDICATIVE |
| RM-0008 | Bluetooth SIG Qualification (QDID) | Global | All BLE | CONFIRMED |
| RM-0009 | GNSS passive-receiver intentional-radiator exemption | US/EU/UK/CA/AU-NZ | Max | INDICATIVE |
| RM-0029 | IEC 62311 / EN 62311 (RF human-exposure) + FCC §1.1310/§2.1093 | EU/UK/US | Mini/Max/Base | INDICATIVE |

### B.3 Battery, Electrical Safety, and Product Safety

| ID | Standard/Regulation | Market | Applies To | Confidence |
| :-- | :------------------ | :----- | :--------- | :--------- |
| RM-0010 | UN 38.3 Part III 38.3 | Global | Mini/Max | CONFIRMED |
| RM-0011 | IEC 62133-2:2017 + AMD1:2021 (Ed 1.1) Cl 7 | EU (+intl) | Mini/Max | CONFIRMED |
| RM-0012 | UL 1642 / UL 2054 | US | Mini/Max | CONFIRMED |
| RM-0013 | EN 62368-1:2020 / UL 62368-1 | EU, US | Base | CONFIRMED |
| RM-0014 | EU Battery Regulation (EU) 2023/1542 Art 6, Art 11 | EU | Mini/Max/Base | CONFIRMED (Art 11 INDICATIVE) |
| RM-0030 | ASTM F2056 (pet collar safety spec) | — | CCF-S | CONFIRMED (standard-level; feline force UNVERIFIED) |
| RM-0031 | EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a) | EU | CCF (Zone 2) | INDICATIVE-pending-DVT |

### B.4 Privacy and Cybersecurity

| ID | Standard/Regulation | Market | Applies To | Confidence |
| :-- | :------------------ | :----- | :--------- | :--------- |
| RM-0015 | GDPR (EU) 2016/679 Art 5, 25, 32 | EU | System | CONFIRMED |
| RM-0016 | UK GDPR + DPA 2018 | UK | System | CONFIRMED |
| RM-0017 | CCPA/CPRA | US-CA | System | INDICATIVE |
| RM-0018 | PIPEDA | CA | System | CONFIRMED |
| RM-0019 | ETSI EN 303 645:2025 Prov 5.1–5.13 | EU, UK | System | CONFIRMED |
| RM-0020 | RED Delegated Reg (EU) 2022/30 Art 3.3(d)(e)(f) | EU | Mini/Max/Base | CONFIRMED (transitional) |
| RM-0021 | EU Cyber Resilience Act (EU) 2024/2847 Annex I; Art 13–14 | EU | System | CONFIRMED |
| RM-0022 | UK PSTI Act 2022 + SI 2023/1007 | UK | System | CONFIRMED |
| RM-0023 | FCC Cyber Trust Mark | US | System | INDICATIVE |

### B.5 Materials, Environmental, and Ingress

| ID | Standard/Regulation | Market | Applies To | Confidence |
| :-- | :------------------ | :----- | :--------- | :--------- |
| RM-0024 | EU GPSR (EU) 2023/988 Art 5, Art 6 | EU | System + CCF | CONFIRMED |
| RM-0025 | UK GPSR 2005 / US CPSA | UK, US | System + CCF | CONFIRMED |
| RM-0026 | REACH (EC)1907/2006 · RoHS 2011/65/EU + 2015/863 · CA Prop 65 | EU, UK, US-CA | Device + CCF | CONFIRMED |
| RM-0027 | WEEE 2012/19/EU · EU PPWR · UK Producer Responsibility | EU, UK | System + packaging | CONFIRMED |
| RM-0028 | IEC 60529 (IP67) + IEC 60068-2 series | Global | Mini/Max/CCF | CONFIRMED (clause INDICATIVE) |

---

## Appendix C — Assumption Register

This appendix documents the assumptions on which requirements in this SRS depend. Each assumption carries a unique identifier, the statement of the assumption, the basis or rationale, and a risk assessment.

| ID | Statement | Basis | Risk |
| :-- | :-------- | :---- | :--- |
| A-0001 | The product is a general-wellness device for animals, not a medical device. | PRD §13.6; confirmed per user decision. | LOW |
| A-0002 | Zone 2 blunt-edge method: sharp-edge test methodology (GPSR Art 6 basis) used as an indicative method for an animal product. | GPSR 2023/988 Art 6. | MEDIUM |
| A-0003 | CCF thermal-cycling profile defaults to IEC 60068-2-14 Test Na. | PRD §12.5; RM-0028 confirms basis. | LOW |
| A-0004 | "Full-quality GNSS" is interpreted as acquisition-based (fix obtained within 90 s timeout using A-GPS); no PDOP or metres-level position-accuracy bound is imposed. | PRD §4.1, §10.2.2. | LOW |
| A-0005 | CCF body chew-penetration resistance: 250 N for at least 30 seconds. Superseded by A-0007. | PRD §13.2. | LOW (superseded) |
| A-0006 | Governing battery cell capacities are the §10.4 (SRS) minimums: Mini ≥120 mAh, Max ≥400 mAh. The §15.3 illustrative figures (130/450 mAh) are non-normative. | PRD §10.4, §15.3; CR-0002 confirmed. | LOW |
| A-0007 | Device enclosure chew resistance: 250 N compressive, at least 30 seconds. | PRD §13.2; engineering default for pet-wearable. | LOW-MEDIUM |
| A-0008 | Base Station LED dimming/nighttime mode: should support ambient-light-responsive dimming below approximately 50 lux or user-configurable quiet-hours schedule. | PRD §11.6. | LOW |
| A-0009 | Home Wi-Fi reliability bound: −70 dBm RSSI at 2.4 GHz, at least 256 kbps sustained uplink. | Engineered numeric default; resolves PRD's unbounded "reliable Wi-Fi." | LOW-MEDIUM |
| A-0010 | Device-absent CCF socket entrapment: 12 mm probe criterion. | GPSR foreseeable-hazard duty; engineered default. | MEDIUM |
| A-0011 | Battery-ingestion warning = Li-Po pouch, not coin cell. Reese's Law / 16 CFR 1263 / UL 4200A do not apply; general ingestion/small-part warning under GPSR/CPSA is correct basis. | Verified per battery form factor and regulatory analysis (RM-0011). | LOW |
| A-0012 | CCF assembled-mass constant: 26 g. CCF-L force floor derived under this assumption; revised to 30 N if mass exceeds 26 g. | PRD §10.1.4; DVT-gated (I-2). | MEDIUM |
| A-0013 | EU Battery Regulation Art 11 removability exemption (indicative); potential conflict with non-swappable design under review. | EU Battery Reg (EU) 2023/1542; tracked per RM-0014. | HIGH |
| A-0014 | CCF-S feline breakaway force basis: ≤20 N ceiling anchored to ASTM F2056 (standard-level); actual numeric value UNVERIFIED against public ~25–45 N data. | RM-0030; safety-critical verification gate. | HIGH |
| A-0015 | Cloud-transport vs. cloud-storage/app boundary: in-scope obligation ends at successful, acknowledged transport to the IoT Cloud Device-Management layer. | Scope model; PRD §6.1. | LOW |
| A-0016 | Device-local vs. cloud-side home/away state machine: device-local state machine is the sole in-scope authority for power gating (GNSS, etc.); cloud-side state machine is external (IoT Cloud backend team). | Scope model; PRD §6.4. | LOW |
| A-0017 | GPSR Art 5 & Art 6(1)(a) design-level strangulation-mitigation framing: the compound-CCF breakaway constitutes design-level mitigation; efficacy pending DVT, particularly for the feline SKU. | GPSR 2023/988; RM-0031. | MEDIUM-HIGH |
| A-0018 | Breakaway detection via accelerometer sensing: commit within 5 s; survives power loss/depletion/reboot; transmitted on next Base Station contact; false-positive ≤0.1%/day; true-detection ≥99%. | PRD §10.1.3.6; engineered parameters. | MEDIUM |
| A-0019 | Collar boot-time ceiling: ≤3 s under cold power-on and wake-from-reset conditions. | PRD §12.1; engineered parameter. | LOW |
| A-0020 | CCF-M and CCF-L canine breakaway force ceilings are engineering-derived (no identifiable ASTM/EN canine breakaway-force standard found). | RM-0030 analysis confirmed no standard basis. | MEDIUM |
| A-0021 | Product service lifetime: ~2–3 years; 2-year floor used where a single testable figure is required. | User-confirmed (PCP §8). | LOW |
| A-0022 | Device-local home/away RSSI thresholds: HOME→AWAY at −85 dBm (5 consecutive, 1 s interval); AWAY→HOME at −80 dBm (3 consecutive, 1 s interval). Engineered defaults. | Engineered by analogy to A-0009; resolves PRD gap. | MEDIUM |
| A-0023 | Charging socket self-drainage: 5 mL fill / 15 s / ≤0.2 mL residual in worn orientation. | Engineered by analogy to A-0007; resolves PRD gap. | LOW-MEDIUM |
| A-0024 | SBOM machine-readable format: SPDX 2.3 or CycloneDX. | EU CRA Annex I + US EO 14028. | LOW-MEDIUM |
| A-0025 | Certification/DoC archival retention: 10 years after last unit placed on market. | RED Art 10 (10 yr), CRA Art 13/31 (10 yr/support), FCC §2.938 (2 yr), ISED RSS-Gen, ACMA/EESS (5 yr). | LOW-MEDIUM |

---

## Appendix D — Glossary

This appendix provides definitions for all domain-specific terms used in this specification. Terms are listed alphabetically.

| Term | Definition |
| :--- | :--------- |
| **Accelerometer (3-axis MEMS)** | A micro-electromechanical system sensor measuring acceleration along three orthogonal axes, used as the primary sensing input for the behavioral classification engine. |
| **A-GPS (Assisted GPS)** | Auxiliary satellite ephemeris and almanac data delivered via a terrestrial link (BLE) to reduce GNSS fix acquisition time. |
| **Base Station (Charging)** | The Base Station tier that includes a single-device pogo-pin charging cradle in addition to BLE relay and Wi-Fi uplink functions. |
| **Base Station (Relay)** | The Base Station tier that provides BLE relay and Wi-Fi uplink functions without a charging cradle. |
| **BLE (Bluetooth Low Energy)** | A wireless personal area network technology operating in the 2.4 GHz ISM band, used for collar-to-Base Station communication. |
| **BLE Address Randomization** | Periodic rotation of the BLE device address to prevent long-term tracking by third-party observers. |
| **BLE Central Role** | The BLE role that scans for advertisements and initiates connections to peripherals. |
| **BLE Peripheral Role** | The BLE role that advertises and accepts incoming connections. |
| **CCF (Collar Connection Fixture)** | A compound mechanical accessory that attaches the collar device to the pet's collar, providing Zone 1 structural retention and Zone 2 strangulation-prevention breakaway. |
| **Charge/Discharge Cycle** | One complete sequence of fully charging and then discharging a battery cell, used as the standard unit for battery aging and cycle-life validation. |
| **Classification Record** | A data structure containing a behavioral label, confidence score, UTC timestamp, and (on Max) GNSS fix, generated by the on-device classification engine. |
| **Damp Heat** | A combined high-temperature, high-humidity environmental test used to assess material and seal degradation under sustained humid conditions. |
| **Debounce (RSSI Reading)** | A requirement that a stated number of consecutive RSSI readings satisfy a threshold condition before a state transition is committed, filtering out transient signal fluctuations. |
| **GNSS (Global Navigation Satellite System)** | A passive receiver providing position-fix data from satellite signals (GPS, Galileo, etc.). |
| **HOME/AWAY State** | The device-local determination of whether the collar is within BLE range of a paired household Base Station (HOME) or not (AWAY), used to gate power-sensitive behaviors. |
| **Hysteresis (RSSI)** | A signal-strength margin requiring a materially different RSSI value to transition back to HOME than the value used to transition to AWAY, preventing rapid state oscillation. |
| **Insight Mode** | An on-demand operating mode providing continuous 50 Hz accelerometer sampling for higher-resolution behavioral data. |
| **IP67** | An ingress-protection rating per IEC 60529: dust-tight (6) and protected against temporary immersion in water up to 1 meter for 30 minutes (7). |
| **LE Secure Connections** | A BLE pairing method using elliptic-curve key exchange to establish link-layer encryption keys. |
| **Longevity Mode** | A power-optimized operating mode that extends battery life without reducing classification sampling rate or accuracy. |
| **Operational Availability** | The proportion of time a system or device is capable of performing its specified function, expressed as a percentage of total elapsed time. |
| **OTA (Over-the-Air)** | A mechanism for delivering and installing firmware updates wirelessly, without a physical connection. |
| **PA66-GF30** | Glass-fibre-reinforced polyamide 66 (30% glass fibre by weight), the specified CCF body material. |
| **Pogo-Pin** | A spring-loaded electrical contact used in the charging interface to carry VBUS and GND between the charging cradle and collar device. |
| **QDID (Qualified Design ID)** | The identifier issued by the Bluetooth SIG upon successful qualification testing of a BLE product design. |
| **Service Lifetime** | The expected duration, from first use to end of intended service, over which a product must continue to meet its specified performance and safety criteria. |
| **SoC (State of Charge)** | The available battery capacity expressed as a percentage of nominal capacity. |
| **Tier-1 Classifier** | Factory-loaded behavioral classifiers: Rest/Sleep and Active/Awake. |
| **Tier-2 Classifier** | OTA-delivered behavioral classifiers: Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting (dog only), Head-Shaking. |
| **TLS 1.3** | Transport Layer Security version 1.3, the transport-layer encryption protocol used for Base Station-to-cloud traffic. |
| **TTFF (Time-To-First-Fix)** | The elapsed time from the start of a GNSS fix attempt to acquisition of a valid position fix. |
| **Twist-Lock** | A three-lug bayonet interface used for mechanically attaching the collar device to the CCF, with asymmetric keying for correct-orientation insertion. |
| **Uptime** | The proportion of a defined observation window during which a system remains powered, responsive, and capable of performing its specified function. |
| **UV Aging** | Accelerated exposure of a material to ultraviolet radiation to evaluate long-term degradation from outdoor solar exposure. |
| **VBUS** | The positive supply-voltage contact of the pogo-pin charging interface. |
| **Wellness Mode** | The default power-optimized operating mode using motion-triggered confirmation sampling bursts. |
| **Zone 1** | The structural-retention clamp of the CCF that holds the device to the pet's collar; not a breakaway feature. |
| **Zone 2 (Fuse Tab)** | The single-use, species/size-appropriate strangulation-prevention breakaway element of the CCF. |

---

## Appendix E — Requirements Summary and Statistics

### E.1 Document Statistics

| Metric | Value |
| :----- | :---- |
| Total core numbered sections | 18 |
| Total requirements | 397 |
| Base requirements (Sections 2–17) | 351 |
| Regulatory requirements (Section 18) | 46 |
| In-scope requirements | 365 |
| External-party requirements | 32 |
| CRITICAL priority requirements | 131 |
| HIGH priority requirements | 198 |
| MEDIUM priority requirements | 59 |
| LOW priority requirements | 6 |
| VOLATILE stability requirements | 3 |
| STABLE stability requirements | 336 |
| LIKELY-CHANGE stability requirements | 44 |
| VOLATILE stability requirements | 17 |
| Test verification method | 258 |
| Inspection verification method | 108 |
| Analysis verification method | 20 |
| Demonstration verification method | 11 |
| Total RTM rows | 369 |
| Total assumptions | 25 (A-0001 through A-0025) |
| Regulatory map entries | 31 (RM-0001 through RM-0031) |

### E.2 Priority Distribution by Section

| Section | CRITICAL | HIGH | MEDIUM | LOW | Total |
| :------ | :------: | :---: | :----: | :-: | :---: |
| §1 Introduction | 2 | 0 | 0 | 0 | 2 |
| §2 Overall Description | 5 | 8 | 3 | 0 | 16 |
| §3 Behavioral Classification | 9 | 20 | 6 | 0 | 35 |
| §4 Data Sync & Connectivity | 13 | 12 | 4 | 0 | 29 |
| §5 OTA Firmware Updates | 8 | 8 | 4 | 0 | 20 |
| §6 Performance | 0 | 4 | 3 | 1 | 8 |
| §7 Safety | 13 | 7 | 1 | 0 | 21 |
| §8 Security | 5 | 1 | 0 | 0 | 6 |
| §9 Data Requirements | 11 | 10 | 5 | 1 | 27 |
| §10 Interface Requirements | 10 | 15 | 10 | 1 | 36 |
| §11 Hardware/Physical | 11 | 12 | 4 | 0 | 27 |
| §12 Environmental | 7 | 7 | 4 | 0 | 18 |
| §13 Reliability | 1 | 3 | 0 | 0 | 4 |
| §14 Usability | 0 | 23 | 5 | 1 | 29 |
| §15 Operational | 0 | 7 | 6 | 0 | 13 |
| §16 Maintainability | 0 | 2 | 1 | 0 | 3 |
| §17 Standards Conformance | 14 | 6 | 4 | 0 | 24 |
| §18 Regulatory | 16 | 34 | 5 | 1 | 56* |
| **TOTAL** | **125** | **179** | **65** | **5** | **374** |

*\*Note: Section 18 counts include REG-0001, REG-0002 (from §1) plus REG-0003 through REG-0046 (from §18), inclusive of both parts and the addendum. The small differences from the summary above reflect attribution boundaries.*

### E.3 Verification Method Distribution

| Method | Count | Percentage |
| :----- | :---: | :--------: |
| Test | 258 | 65.0% |
| Inspection | 108 | 27.2% |
| Analysis | 20 | 5.0% |
| Demonstration | 11 | 2.8% |

### E.4 Traceability Completeness

| Category | Status |
| :------- | :----- |
| Total SRS requirements | 397 |
| Total RTM rows | 369 |
| Orphan requirements (no trace) | 0 |
| Unresolved conflicts | 0 |
| Cross-section contradictions | 0 |
| Feasibility failures | 0 |
| Verification-method failures | 0 |

---

## Document End

**End of SRS-LUUCIPET-PH1-001, Version 1.0**

*This document was prepared by the Requirements Engineering Team, reviewed by the Lead Systems Engineer, and approved by the Requirements Manager. All requirements have been verified for feasibility, cross-consistency, and traceability. No internal workflow identifiers remain in the body of this document.*

