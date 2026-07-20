> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Session:**  S-luucipet · Standard basis: IEEE 830 / ISO/IEC/IEEE 29148 · **COMP and REG SPLIT into separate sections (user decision).**

## Front Matter

- Title, revision, approval, scope/purpose statement, definitions/acronyms reference.

## Core Numbered Sections

| §  | Section                                                                                                                                                                        | CAT            | Maps to PRD                       |
| :- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------- | :-------------------------------- |
| 1  | Introduction (purpose, scope, product perspective, wellness-not-medical boundary, references)                                                                                  | —              | §1, §2, §6.1, §13.6, §14.1        |
| 2  | Overall Description (product functions, variants Mini/Max + base tiers + CCF family, user personas, constraints, assumptions & dependencies)                                   | —              | §1, §3, §4, §14.2                 |
| 3  | Functional Requirements — Behavioral Classification                                                                                                                            | **FUNC**       | §7, §4.4                          |
| 4  | Functional Requirements — Data Sync & Connectivity                                                                                                                             | **CONN**       | §8, §6.3–§6.5, §10.3              |
| 5  | Functional Requirements — OTA Firmware Updates                                                                                                                                 | **FUNC** (OTA) | §9                                |
| 6  | Performance Requirements                                                                                                                                                       | **PERF**       | §7.4, §12.1, §15                  |
| 7  | Safety Requirements (Zone 2 breakaway, Zone 1 retention, Twist-Lock, chew, entrapment, battery-ingestion)                                                                      | **SAFE**       | §10.1.3, §10.1.4, §13.2           |
| 8  | Security Requirements                                                                                                                                                          | **SEC**        | §6.7, §9.3, §12.3                 |
| 9  | Data Requirements (records, storage, buffering, privacy)                                                                                                                       | **DATA**       | §7.5–§7.7, §8, §10.6, §13.5       |
| 10 | Interface Requirements (BLE, Wi-Fi, GNSS, pogo-pin, Twist-Lock mechanical, device-enforced protocol)                                                                           | **INT**        | §6, §10.2, §10.3, §10.5, §11      |
| 11 | Hardware / Physical & Mechanical Requirements (weight, enclosure, materials, CCF architecture, sensing, battery, charging, compute)                                            | **COMP-HW**    | §10                               |
| 12 | Environmental & Durability Requirements                                                                                                                                        | **ENV**        | §12.5, §13.4                      |
| 13 | Reliability & Availability Requirements                                                                                                                                        | **RELI**       | §12.2                             |
| 14 | Usability Requirements                                                                                                                                                         | **UX**         | §12.4, §5                         |
| 15 | Operational Requirements (base-station operation, power, geo-fencing, home/away, lifetime ~2–3 yr)                                                                            | **OPER**       | §6.4, §11.7, §15.5                |
| 16 | Maintainability Requirements (OTA lifetime, SBOM, vuln disclosure)                                                                                                             | **MAINT**      | §12.7                             |
| 17 | **Standards Conformance** (technical standards the product conforms to: IEC 60529, IEC 62133-2, ETSI EN 303 645, IEC 60068 series, UN 38.3, BLE/EN 300 328, etc.)              | **COMP**       | §13.1, §13.3, §13.4, §12.6        |
| 18 | **Regulatory Certification & Market Pathways** (per-market certification/marking: FCC, CE/RED, UKCA, ISED, RCM, GPSR, GDPR/privacy regime, CRA/PSTI, WEEE/RoHS/REACH, Prop 65) | **REG**        | §13.1, §13.2, §13.5, §13.6, §13.7 |

> **COMP/REG split (user decision):**  §17 COMP = *what technical standards the design conforms to*; §18 REG = *what certifications/approvals are needed to place the product on each market*. Kept distinct for this regulated multi-market product.

## Appendices

- **A. Requirements Traceability Matrix (RTM)**  — owned by Traceability Agent.
- **B. Regulatory Map** — owned by Regulatory Agent.
- **C. Assumption Register** — A-0001…A-0011 (+ future).
- **D. Conflict Log & Cross-Section Report** — owned by Conflict & Consistency Resolver.
- **E. Glossary** — from PRD §14.4 + SRS-added terms; owned by Document Assembler.

---

*Conductor-authored (shared-store visibility guarantee). Presented to user at TOC_REVIEW. 18 core sections + 5 appendices.*
