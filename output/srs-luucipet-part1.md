# System Requirements Specification

## LUUCIPet Wellness Monitor — Phase 1

---

### Document Control

| Field | Value |
| :---- | :---- |
| **Document ID** | SRS-LUUCIPET-PH1-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Proprietary — Internal |
| **Date** | 2026-07-20 |
| **Organization** | LUUCI Systems |
| **Standard** | IEEE 830 / ISO/IEC/IEEE 29148 |

---

#### Prepared By

| Role | Responsibility |
| :--- | :--- |
| Requirements Engineering Team | Requirements authoring (functional and non-functional sections) |
| Regulatory & Compliance Engineering | Standards mapping and compliance verification |
| Systems Analysis | Consistency, interface, and cross-section analysis |
| Verification & Validation Engineering | Verification method definition and feasibility assessment |
| Requirements Manager | Conflict resolution and baseline control |
| Configuration & Traceability Engineering | Requirements traceability management |

---

#### Reviewed & Approved By

| Role | Action | Date |
| :--- | :----- | :--- |
| Lead Systems Engineer | Technical review and integration approval | 2026-07-20 |
| Regulatory & Compliance Engineering | Regulatory and standards review | 2026-07-20 |
| Verification & Validation Engineering | Verification-method review | 2026-07-20 |
| Requirements Manager | Baseline approval | 2026-07-20 |

---

#### Revision History

| Version | Date | Author Role | Description |
| :------ | :--- | :---------- | :---------- |
| 1.0 | 2026-07-20 | Requirements Engineering Team | Initial approved baseline. All 18 sections approved; cross-section consistency confirmed with zero defects; traceability complete at 369 RTM rows covering 397 requirements. |

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [Functional Requirements — Behavioral Classification](#3-functional-requirements--behavioral-classification)
4. [Functional Requirements — Data Sync and Connectivity](#4-functional-requirements--data-sync-and-connectivity)
5. [Functional Requirements — OTA Firmware Updates](#5-functional-requirements--ota-firmware-updates)
6. [Performance Requirements](#6-performance-requirements)
7. [Safety Requirements](#7-safety-requirements)
8. [Security Requirements](#8-security-requirements)
9. [Data Requirements](#9-data-requirements)
10. [Interface Requirements](#10-interface-requirements)
11. [Hardware, Physical, and Mechanical Requirements](#11-hardware-physical-and-mechanical-requirements)
12. [Environmental and Durability Requirements](#12-environmental-and-durability-requirements)
13. [Reliability and Availability Requirements](#13-reliability-and-availability-requirements)
14. [Usability Requirements](#14-usability-requirements)
15. [Operational Requirements](#15-operational-requirements)
16. [Maintainability Requirements](#16-maintainability-requirements)
17. [Standards Conformance](#17-standards-conformance)
18. [Regulatory Certification and Market Pathways](#18-regulatory-certification-and-market-pathways)

**Appendices**

- Appendix A — Requirements Traceability Matrix
- Appendix B — Regulatory Compliance Map
- Appendix C — Assumption Register
- Appendix D — Glossary
- Appendix E — Requirements Summary and Statistics

---

## 1. Introduction

### 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — comprising the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor Product Requirements Document (PRD) v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 and ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

### 1.2 Scope

This section specifies the boundaries of the system addressed by this SRS.

**In Scope**

The following elements are within the scope of this specification:

- Mini and Max collar device hardware and firmware
- Base Station (Charging and Relay tiers) hardware and firmware
- The device-enforced BLE/base-to-cloud protocol (device-management layer interface)
- The CCF accessory family (widths S, M, L; collar-types -RC and -MG)
- The Portable Travel Charging Cradle
- The LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract

**Out of Scope**

The following elements are explicitly excluded from this specification:

- GPS-M variant and cellular connectivity (Phase 2, separate PRD)
- LUUCI Mobile App
- IoT Cloud data storage and analytics backend
- Cloud-side home/away state machine
- Device-app interface control document (ICD)

### 1.3 Product Perspective

The LUUCIPet Wellness Monitor is a collar-mounted behavioral wellness system. Each collar device communicates with household Base Stations over Bluetooth Low Energy (BLE); Base Stations relay behavioral data, geo-fencing sighting reports, and over-the-air (OTA) firmware images to and from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar device attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface used for charging removal.

### 1.4 Wellness-Not-Medical Boundary

This product is positioned as a general wellness device for animals. It does not perform, and is not intended to support, medical diagnosis.

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-REG-0001 | The system's labeling and marketing materials shall not include diagnostic, treatment, or disease-detection claims. | CRITICAL | STABLE | Inspection |
| SRS-REG-0002 | Any post-launch feature that could constitute a diagnostic claim shall undergo regulatory classification review before release. | CRITICAL | STABLE | Analysis |

### 1.5 Definitions and References

Full term definitions are maintained in the Glossary (Appendix D). Standards and regulatory instruments are enumerated in the Regulatory Compliance Map (Appendix B) and cited inline throughout this document. Requirements trace back to the PRD, named technical standards, and the Assumption Register (Appendix C).

---

## 2. Overall Description

This section provides the high-level product context: the functions the system performs, the product variants and configurations available at launch, the intended user population, the general constraints imposed on the system, and the assumptions and dependencies that underpin the requirements in subsequent sections.

### 2.1 Product Functions

The LUUCIPet Wellness Monitor is a collar-mounted behavioral wellness system for cats and dogs, comprising an ultra-light wearable device, a companion household Base Station, and a mechanical CCF accessory family. The system continuously classifies pet behavior on-device using an accelerometer-based classification engine, relays behavioral and location data to the LUUCI IoT Cloud Device-Management layer via the Base Station, and supports OTA firmware and classifier updates.

At launch (Phase 1), the device ships with two factory-loaded Tier-1 behavioral classifiers: Rest/Sleep and Active/Awake. A broader Tier-2 classifier set — Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting (dog only), and Head-Shaking — is deliverable post-launch exclusively via OTA.

**Scope-model note on functional responsibility.** Product functions are delivered across in-scope (our build) and named external parties:

- **In scope (our build):** on-device behavioral classification; collar-to-base BLE sync and base-to-cloud relay (device-management-layer interface); charging (Base Station and Portable Travel Charging Cradle); CCF breakaway/separation detection and event transport; device-side species-profile persistence; device-local home/away determination that gates GNSS power behavior, relying solely on the device-local state machine.
- **External-party (documented, attributed):** owner-facing Mobile App alerts, onboarding, CCF guidance, and dashboards — attributed to the Mobile App team; IoT Cloud storage/analytics backend and the cloud-side home/away state machine for owner geofence alerting — attributed to the IoT Cloud backend team. Data transport to the cloud is the in-scope hand-off; cloud storage/analytics and app display are external.
- **Future-phase (deferred, Phase 2):** GPS-M variant and cellular positioning — not addressed by any requirement in this SRS.

The CCF Zone 2 Fuse Tab breakaway is designed as a strangulation-prevention mitigation with reference to the EU General Product Safety Regulation (GPSR) 2023/988. Substantive safety requirements are specified in Section 7.

### 2.2 Product Variants and Configurations

#### 2.2.1 Collar Devices

Two collar variants share a common platform (classification engine, BLE protocol, OTA path, Twist-Lock geometry) but differ in weight class, sensing, and target population:

- **Mini** — maximum 10 g; BLE-only; targets all cats and dogs; typical battery life equal to or greater than 90 days (equal to or greater than 180 days in Longevity Mode).
- **Max** — maximum 22 g; BLE plus full-quality GNSS (receive-only); targets large dogs (greater than 20 kg) and service dogs; battery life equal to or greater than 45 days at a 2-hour GNSS fix interval, equal to or greater than 90 days at a 4-hour interval; GNSS is power-gated off while the device is in the HOME state.

#### 2.2.2 Base Station Family

Two Base Station tiers share a common BLE-relay and Wi-Fi-uplink platform:

- **Base Station (Charging)** — BLE relay, Wi-Fi uplink, single-device pogo-pin charging cradle, three status LEDs.
- **Base Station (Relay)** — identical to the Charging tier minus the charging cradle; two status LEDs.

Both tiers support multi-device BLE connections (Mini and Max concurrently), participate in the household geo-fence mesh, relay OTA payloads to collars, self-update over Wi-Fi, and buffer collar data for at least 30 days during connectivity loss.

#### 2.2.3 Collar Connection Fixture (CCF) Family

The CCF is a compound mechanical accessory that attaches the collar device to the pet's own (third-party-supplied) collar. It provides two functionally distinct zones: Zone 1 (structural retention, not a breakaway feature) and Zone 2 (the Fuse Tab — a single-use, species/size-appropriate strangulation-prevention breakaway). The device engages the CCF through a three-lug Twist-Lock bayonet interface used for charging removal.

The CCF is offered in width variants S, M, and L and collar-type variants -RC (round) and -MG (martingale), sold separately from the in-box default. A Standard CCF (flat-webbing) ships in every box, sized to the collar variant (CCF-S with Mini, CCF-L with Max).

#### 2.2.4 Classifier Tiers

- **Tier-1 (factory-loaded):** Rest/Sleep; Active/Awake.
- **Tier-2 (OTA-delivered, post-launch):** Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting (dog only), Head-Shaking.

### 2.3 User Characteristics

The system is designed around six user personas, described here as user context only. Owner-facing app features are delivered by the Mobile App team and are outside the scope of this SRS.

| Persona | Description |
| :------ | :---------- |
| P1 — Single-Pet Owner | Primary user of a single Mini-equipped pet. |
| P2 — Multi-Pet Household | Manages a mix of Mini and Max devices across multiple pets. |
| P3 — Allergy/Skin-Concern Owner | Relies on fine-grained scratch-behavior logging. |
| P4 — Active-Lifestyle Large-Dog Owner | Primary user of Max; values GNSS behavioral context. |
| P5 — Veterinary Professional | Uses exported behavioral summaries as a wellness-conversation support tool. |
| P6 — Service Dog Handler | Monitors welfare of a working service dog (Max). |

### 2.4 General Constraints

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-OPER-0001 | A household deployment shall include at least one Base Station of the Charging tier. | CRITICAL | STABLE | Inspection |
| SRS-OPER-0002 | A household deployment shall not exceed 8 Base Stations, in any combination of Charging and Relay tiers. | HIGH | STABLE | Test |
| SRS-OPER-0003 | The collar device shall retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. | HIGH | STABLE | Test |
| SRS-OPER-0004 | The Max variant's GNSS smart power gate shall not be configurable by the owner. | HIGH | STABLE | Inspection |
| SRS-OPER-0005 | The in-box Standard CCF shall be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. | MEDIUM | LIKELY-CHANGE | Analysis |
| SRS-OPER-0006 | The system shall ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. | HIGH | STABLE | Inspection |
| SRS-OPER-0007 | The Base Station shall enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. | HIGH | STABLE | Test |
| SRS-OPER-0008 | The Mobile App shall display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. (External: Mobile App team.) | HIGH | STABLE | Analysis — external conformance evidence |
| SRS-OPER-0009 | The Mobile App shall provide a species re-onboarding flow that re-assigns the device's species classifier profile. (External: Mobile App team.) | MEDIUM | STABLE | Analysis — external conformance evidence |
| SRS-OPER-0010 | The Mobile App shall provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. (External: Mobile App team.) | MEDIUM | LIKELY-CHANGE | Analysis — external conformance evidence |
| SRS-OPER-0011 | The IoT Cloud Device-Management layer shall maintain a cloud-side home/away state machine to support owner-facing geofence alerting. (External: IoT Cloud backend team.) | MEDIUM | LIKELY-CHANGE | Analysis — external conformance evidence |
| SRS-COMP-0001 | Base Station firmware shall, from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. | HIGH | STABLE | Test |
| SRS-COMP-0002 | All CCF accessory variants (widths S, M, L; collar-types -RC, -MG) shall be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. | CRITICAL | STABLE | Test |
| SRS-COMP-0003 | The Mini and Max collar variants shall exhibit equivalent behavioral-classification outputs and use an interoperable common BLE communication protocol across the Mini and Max variants. | HIGH | STABLE | Inspection |
| SRS-FUNC-0001 | The collar device shall detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event record to non-volatile storage within 5 seconds of the separation event, with a false-positive rate not exceeding 0.1% per device-wear-day and a true-event detection rate of at least 99% under DVT drop/tension conditions. | CRITICAL | STABLE | Test |
| SRS-FUNC-0002 | The Base Station shall transport a recorded breakaway/separation event to the IoT Cloud Device-Management layer on the next successful Base Station contact and cloud sync. | CRITICAL | STABLE | Test |
| SRS-FUNC-0003 | The persisted breakaway event record shall survive subsequent power loss, battery depletion, and reboot without corruption, and be transmitted to the Base Station on the next successful Base Station contact. | CRITICAL | STABLE | Test |

### 2.5 Assumptions and Dependencies

This section's constraints depend on assumptions documented in the Assumption Register (Appendix C). Key assumptions include: governing battery cell capacities are the Section 10.4 minimums; home Wi-Fi reliability bound of −70 dBm RSSI and 256 kbps; CCF assembled-mass constant of 26 g; EU Battery Regulation Article 11 removability exemption (indicative); CCF-S feline breakaway force basis; cloud-transport versus cloud-storage/app boundary; device-local versus cloud-side home/away state machine; and GPSR design-level strangulation-mitigation framing (pending DVT).

---

## 3. Functional Requirements — Behavioral Classification

This section specifies the functional requirements governing the behavioral classification subsystem of the LUUCIPet collar device. It establishes the operating modes, sensing and classification pipeline, accuracy and false-positive bounds, classification record format, data locality and on-device processing constraints, Tier-2 extensibility via OTA, and configurable alert thresholds.

### 3.1 Operating Modes

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0006 | The system shall operate in Wellness mode as its default power-optimized classification mode. | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0007 | The system shall provide an Insight mode that can be activated on demand as an alternative to Wellness mode. | HIGH | STABLE | Demonstration |
| SRS-FUNC-0008 | While in Insight mode, the system shall sample the accelerometer continuously at 50 Hz. | HIGH | STABLE | Test |
| SRS-FUNC-0009 | The system shall automatically revert from Insight mode to Wellness mode without requiring a manual user action. | HIGH | STABLE | Test |
| SRS-FUNC-0010 | Upon detecting motion, the system shall initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. | HIGH | STABLE | Test |
| SRS-FUNC-0011 | While in Wellness mode and outside a confirmation burst, the system shall not exceed an idle current draw of 4 µA. | CRITICAL | STABLE | Test |
| SRS-FUNC-0012 | When Longevity Mode is active, the system shall not reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. | CRITICAL | STABLE | Test |
| SRS-FUNC-0013 | When Longevity Mode is active, the system shall not reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. | CRITICAL | STABLE | Test |

### 3.2 Sensing and Classification Pipeline

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0014 | The system shall sample the accelerometer at a rate of no less than 50 Hz. | CRITICAL | STABLE | Test |
| SRS-FUNC-0015 | The system shall classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. | HIGH | STABLE | Inspection |
| SRS-FUNC-0016 | The system shall process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0017 | The system shall set species-specific classification thresholds during the onboarding process. | HIGH | STABLE | Test |

### 3.3 Classification Accuracy and False-Positive Bounds

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0018 | The system shall achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. | CRITICAL | LIKELY-CHANGE | Test |
| SRS-FUNC-0019 | The system shall not exceed a false-positive rate of 5% for each Tier-1 behavior class. | CRITICAL | LIKELY-CHANGE | Test |
| SRS-FUNC-0020 | The system shall achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. | HIGH | LIKELY-CHANGE | Test |
| SRS-FUNC-0021 | The system shall not exceed a false-positive rate of 10% for each Tier-2 behavior class. | HIGH | LIKELY-CHANGE | Test |

### 3.4 Classification Records and Local Storage

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0022 | The system shall include a behavior class label in every generated classification record. | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0023 | The system shall include a confidence score in the range 0.0 to 1.0 in every generated classification record. | HIGH | STABLE | Test |
| SRS-FUNC-0024 | The system shall timestamp every classification record in UTC with a resolution no coarser than 1 second. | HIGH | STABLE | Test |
| SRS-FUNC-0025 | On the Max product variant, the system shall include the most recent GNSS fix in every generated classification record. | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0026 | The system shall retain generated classification records locally for no less than 30 days without a cloud connection. | CRITICAL | STABLE | Test |
| SRS-FUNC-0027 | The system shall not discard stored classification records upon loss of connectivity. | CRITICAL | STABLE | Test |
| SRS-FUNC-0028 | The system shall generate and record classifications independently of the current BLE connectivity state. | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0029 | The system shall forward stored classification records without data corruption. | CRITICAL | STABLE | Test |
| SRS-FUNC-0030 | The system shall forward stored classification records without loss of their original sequence order. | HIGH | STABLE | Test |

### 3.5 Data Locality and On-Device Processing

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0031 | The system shall normalize raw accelerometer data on-device prior to classification. | HIGH | STABLE | Inspection |
| SRS-FUNC-0032 | The system shall not transmit raw accelerometer data off the collar. | CRITICAL | STABLE | Test |
| SRS-FUNC-0033 | The system shall produce classification decisions without requiring a round-trip to a cloud service. | CRITICAL | STABLE | Demonstration |

### 3.6 Tier-2 Extensibility via OTA

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0034 | The system shall receive new Tier-2 behavior classifiers via over-the-air update. | HIGH | STABLE | Demonstration |
| SRS-FUNC-0035 | The system shall not require hardware modification or a service event to deploy a new Tier-2 classifier. | HIGH | STABLE | Demonstration |

### 3.7 Configurable Alert Thresholds (Scratching and Shaking)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0036 | The system shall apply a Scratching alert threshold value received via the companion application. | HIGH | VOLATILE | Test |
| SRS-FUNC-0037 | The system shall apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. | MEDIUM | VOLATILE | Inspection |
| SRS-FUNC-0038 | The system shall apply a Shaking alert threshold value received via the companion application. | HIGH | VOLATILE | Test |
| SRS-FUNC-0039 | The system shall apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. | MEDIUM | VOLATILE | Inspection |
| SRS-FUNC-0040 | The system shall retain configured Scratching and Shaking alert threshold values across OTA firmware updates. | HIGH | STABLE | Test |
| SRS-FUNC-0041 | The Mobile App shall provide a user interface for configuring the Scratching alert threshold. (External: Mobile App team.) | HIGH | STABLE | Inspection — external conformance evidence |
| SRS-FUNC-0042 | The Mobile App shall provide a user interface for configuring the Shaking alert threshold. (External: Mobile App team.) | HIGH | STABLE | Inspection — external conformance evidence |

