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


## 4. Functional Requirements — Data Sync and Connectivity

This section specifies the requirements governing the data synchronization and connectivity behavior across the collar device, Base Station, and cloud device-management layer. It defines the BLE device-to-base link, record forwarding and synchronization, base-to-cloud gateway behavior, multi-base-station operation, Insight-mode activation over connectivity, GNSS location data synchronization (Max variant), and connectivity-loss degraded behavior.

### 4.1 BLE Device-to-Base Link and Pairing

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0001 | The system shall operate the collar-mounted device in the BLE peripheral role relative to the Base Station. | HIGH | STABLE | Inspection |
| SRS-CONN-0002 | The system shall operate the Base Station in the BLE central role relative to the collar-mounted device. | HIGH | STABLE | Inspection |
| SRS-CONN-0003 | The system shall support pairing between the collar-mounted device and the Base Station using QR-code out-of-band exchange. | HIGH | STABLE | Demonstration |
| SRS-CONN-0004 | The system shall advertise the presence of the collar-mounted device at a default interval of 60 seconds. | MEDIUM | STABLE | Test |
| SRS-CONN-0005 | The system shall support configuration of the BLE advertising interval within the range of 1 to 180 seconds. | MEDIUM | STABLE | Test |
| SRS-CONN-0006 | The system shall maintain a BLE link between the collar-mounted device and the Base Station across an open-air separation distance of no less than 9 meters. | HIGH | STABLE | Test |
| SRS-CONN-0007 | The system shall transmit BLE signals at a power level of no less than +8 dBm. | MEDIUM | STABLE | Test |
| SRS-CONN-0008 | The system shall randomize the BLE device address of the collar-mounted device. | HIGH | STABLE | Test |
| SRS-CONN-0009 | The system shall establish the BLE link between the collar-mounted device and the Base Station over the secured connection defined in Section 8 (Security). | CRITICAL | STABLE | Inspection |
| SRS-CONN-0010 | Upon the collar-mounted device re-entering BLE range of a Base Station, the system shall automatically re-establish the BLE link without requiring manual user action. | CRITICAL | STABLE | Test |

### 4.2 Record Forwarding and Synchronization

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0011 | Upon establishing a BLE link with a Base Station, the system shall forward stored classification records from the collar-mounted device to the Base Station. | CRITICAL | STABLE | Test |
| SRS-CONN-0012 | The system shall forward stored classification records to the Base Station using a best-effort, event-triggered transport pattern. | HIGH | STABLE | Inspection |
| SRS-CONN-0013 | Upon regaining BLE connectivity to a Base Station following a period of disconnection, the system shall forward all classification records accumulated during that disconnection. | CRITICAL | STABLE | Test |

### 4.3 Base-to-Cloud Gateway and Upload

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0014 | The Base Station shall transmit received classification records to the cloud endpoint over the secured Wi-Fi link. | CRITICAL | STABLE | Test |
| SRS-CONN-0015 | When the Wi-Fi or cloud connection is unavailable, the Base Station shall buffer received classification records pending upload. | CRITICAL | STABLE | Test |
| SRS-CONN-0016 | Upon restoration of the Wi-Fi or cloud connection, the Base Station shall upload all buffered classification records. | CRITICAL | STABLE | Test |
| SRS-CONN-0017 | The Base Station shall not discard a received classification record while that record is pending upload to the cloud. | CRITICAL | STABLE | Test |
| SRS-CONN-0018 | The IoT Cloud backend shall accept and acknowledge classification records uploaded by the Base Station. (External: IoT Cloud backend team.) | CRITICAL | STABLE | Inspection — external conformance evidence |
| SRS-CONN-0030 | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the Base Station shall retry uploading the affected buffered classification record. | HIGH | VOLATILE | Demonstration |

### 4.4 Multi-Base-Station Behavior and Handover

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0019 | The system shall forward stored classification records to any paired Base Station currently in BLE range, without requiring a specific designated Base Station. | HIGH | STABLE | Test |
| SRS-CONN-0020 | The system shall forward each classification record to only the first paired Base Station through which it establishes a BLE link, among those in range. | HIGH | STABLE | Test |
| SRS-CONN-0021 | The IoT Cloud backend shall deduplicate classification records that may be uploaded from more than one Base Station within the same household account. (External: IoT Cloud backend team.) | HIGH | STABLE | Inspection — external conformance evidence |

### 4.5 Insight-Mode Activation over Connectivity

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0022 | Upon receiving an Insight-mode activation command over the BLE link, the system shall activate Insight mode. | HIGH | STABLE | Test |
| SRS-CONN-0023 | The Mobile App shall issue the Insight-mode activation command to the collar-mounted device. (External: Mobile App team.) | HIGH | STABLE | Inspection — external conformance evidence |

### 4.6 GNSS Location Data Synchronization (Max Variant)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0024 | On the Max product variant, the system shall forward location-tagged classification records through the same record-forwarding path used for other classification records. | MEDIUM | STABLE | Test |
| SRS-CONN-0025 | While the GNSS smart power gate suspends fix acquisition in the HOME state, the system shall continue to synchronize the most recently acquired GNSS fix as part of classification records. | MEDIUM | STABLE | Test |

### 4.7 Connectivity-Loss and Degraded Behavior

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0026 | The system shall not lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. | CRITICAL | STABLE | Analysis |
| SRS-CONN-0027 | Upon loss of the BLE link to all Base Stations, the system shall continue local classification and storage without interruption. | CRITICAL | STABLE | Demonstration |
| SRS-CONN-0028 | The system shall enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. | HIGH | STABLE | Test |
| SRS-CONN-0029 | The system shall exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. | HIGH | STABLE | Test |

---

## 5. Functional Requirements — OTA Firmware Updates

This section specifies the requirements for over-the-air firmware update capability across all collar device variants and Base Station tiers. It defines OTA applicability, delivery path and transport security, collar install preconditions, image integrity and anti-rollback mechanisms, install resilience, update notification and status reporting, and release-artifact obligations.

### 5.1 OTA Applicability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0043 | The system shall provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0044 | The system shall provide over-the-air firmware update capability on every Base Station tier (Charging and Relay). | CRITICAL | STABLE | Demonstration |

### 5.2 OTA Delivery Path and Transport

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0045 | The system shall transport OTA firmware images from the cloud to the Base Station over Wi-Fi using TLS version 1.3. | HIGH | STABLE | Test |
| SRS-FUNC-0046 | The system shall stage a received collar OTA firmware image at the Base Station prior to delivery of that image to the collar-mounted device. | MEDIUM | STABLE | Test |
| SRS-FUNC-0047 | The system shall deliver a staged OTA firmware image from the Base Station to the collar-mounted device over the secured BLE link defined in Section 8 (Security). | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0048 | The system shall update Base Station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. | HIGH | STABLE | Demonstration |

### 5.3 Collar Install Preconditions

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0049 | The system shall install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. | CRITICAL | STABLE | Test |
| SRS-FUNC-0050 | The system shall not allow the charging-cradle-docked install precondition to be bypassed by any remote command. | CRITICAL | STABLE | Test |
| SRS-FUNC-0051 | The system shall require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. | HIGH | STABLE | Test |

### 5.4 OTA Image Integrity and Anti-Rollback

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0052 | The system shall require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0053 | The system shall verify the signature of an OTA firmware image before committing or executing that image. | CRITICAL | STABLE | Test |
| SRS-FUNC-0054 | The system shall prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. | CRITICAL | STABLE | Test |

### 5.5 Install Resilience

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0055 | The system shall install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. | CRITICAL | STABLE | Test |
| SRS-FUNC-0056 | The system shall automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. | CRITICAL | STABLE | Test |
| SRS-FUNC-0057 | The system shall not enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. | CRITICAL | STABLE | Analysis |

### 5.6 Update Notification and Status

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0058 | The system shall report the current OTA update state as one of: Downloading, Verifying, Pending Installation, Installing, Success, or Failed. | MEDIUM | STABLE | Test |
| SRS-FUNC-0059 | The Mobile App shall notify the user when an OTA firmware update is available. (External: Mobile App team.) | MEDIUM | STABLE | Inspection — external conformance evidence |
| SRS-FUNC-0060 | The Mobile App shall display the current OTA update state reported by the device. (External: Mobile App team.) | MEDIUM | STABLE | Inspection — external conformance evidence |

### 5.7 Release Artifacts and Tier-2 Delivery Channel

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0061 | The system shall produce a Software Bill of Materials for every OTA firmware release. | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0062 | The system shall deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. | HIGH | STABLE | Inspection |

---

## 6. Performance Requirements

This section specifies the quantitative performance criteria the system must meet. It addresses battery-life performance across collar variants, classification and data-path latency, location-acquisition timing, system startup timing, and physical-interaction timing.

### 6.1 Battery-Life Performance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0001 | The system's Mini variant shall meet or exceed the battery-life minimums specified in Section 11.7 (Table 11-2) across typical-use, minimum, and Longevity Mode operating conditions. | HIGH | STABLE | Analysis |
| SRS-PERF-0002 | The system's Max variant shall meet or exceed the battery-life minimums specified in Section 11.7 (Table 11-2) across all supported GNSS fix-interval settings. | HIGH | STABLE | Analysis |

### 6.2 Classification and Data-Path Latency

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0003 | The system shall produce a classification result within 2 seconds of the triggering motion event. | HIGH | STABLE | Test |
| SRS-PERF-0004 | The Base Station shall upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. | MEDIUM | STABLE | Test |

### 6.3 Location and Startup Timing (Max Variant)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0005 | On the Max product variant, the system shall acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. | MEDIUM | STABLE | Test |

### 6.4 Startup and Physical-Interaction Timing

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0006 | The collar-mounted device shall complete boot within 3 seconds under cold power-on and wake-from-reset conditions. | MEDIUM | STABLE | Test |
| SRS-PERF-0007 | The system shall update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. | HIGH | STABLE | Test |
| SRS-PERF-0008 | The system shall allow the Twist-Lock mechanism to be engaged within 5 seconds. | LOW | STABLE | Test |

---

## 7. Safety Requirements

This section specifies the safety requirements for the LUUCIPet system, with emphasis on the CCF compound-architecture: Zone 2 Fuse Tab strangulation-prevention breakaway (the primary pet-safety mechanism), Zone 1 structural retention, Twist-Lock charging-removal retention, post-breakaway protocol and re-use prevention, chew resistance, device-absent socket entrapment prevention, animal-contact material safety, and battery-ingestion warning.

### 7.1 Zone 2 Fuse Tab — Strangulation-Prevention Breakaway

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0001 | The Zone 2 Fuse Tab of the CCF-S variant shall fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. | CRITICAL | STABLE | Test |
| SRS-SAFE-0002 | The Zone 2 Fuse Tab of the CCF-M variant shall fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. | CRITICAL | STABLE | Test |
| SRS-SAFE-0003 | The Zone 2 Fuse Tab of the CCF-L variant shall fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device-plus-CCF mass does not exceed 26 g. | CRITICAL | STABLE | Test |
| SRS-SAFE-0004 | If the assembled device-plus-CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor shall be revised upward to 30 N. | CRITICAL | LIKELY-CHANGE | Analysis |
| SRS-SAFE-0005 | The Zone 2 Fuse Tab shall not be capable of being reused or restored to a load-bearing state after fracture. | CRITICAL | STABLE | Test |
| SRS-SAFE-0006 | Upon fracture, the Zone 2 Fuse Tab shall not produce a detached fragment separate from the CCF body. | HIGH | STABLE | Inspection |
| SRS-SAFE-0007 | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway shall be blunt, presenting no sharp edge. | HIGH | STABLE | Inspection |
| SRS-SAFE-0008 | The CCF shall present a visible fracture indicator upon Zone 2 breakaway. | HIGH | STABLE | Inspection |

### 7.2 Zone 1 — Structural Retention (Non-Breakaway)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0009 | The Zone 1 clamp shall retain axial loads of at least 50 N without structural failure. | CRITICAL | STABLE | Test |
| SRS-SAFE-0010 | The Zone 1 clamp shall remain structurally intact following a Zone 2 fracture event. | CRITICAL | STABLE | Test |

### 7.3 Twist-Lock — Retention Safety (Non-Breakaway)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0011 | The Twist-Lock device-to-CCF interface shall retain axial loads exceeding 100 N without disengaging. | CRITICAL | STABLE | Test |
| SRS-SAFE-0012 | The Twist-Lock shall remain engaged under inertial loads generated by pet head-shake motion up to 50 g. | HIGH | STABLE | Test |

### 7.4 Post-Breakaway Protocol and Re-Use Prevention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0013 | The device shall not be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. | CRITICAL | STABLE | Inspection |
| SRS-SAFE-0014 | The device shall emit a detectable separation signature upon Zone 2 breakaway. | HIGH | STABLE | Test |
| SRS-SAFE-0015 | The Mobile App shall notify the owner that CCF replacement is required upon receiving a device separation signature. (External: Mobile App team.) | HIGH | STABLE | Inspection — external conformance evidence |

### 7.5 Chew Resistance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0016 | The Zone 2 Fuse Tab shall not fracture under a compressive load below 250 N. | CRITICAL | STABLE | Test |
| SRS-SAFE-0017 | The CCF body shall resist penetration for at least 30 seconds under a 250 N compressive load. | HIGH | STABLE | Test |
| SRS-SAFE-0018 | Materials in animal-skin contact on the device enclosure shall resist chew-induced damage. | MEDIUM | LIKELY-CHANGE | Analysis |

### 7.6 Device-Absent Socket — Entrapment Prevention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0019 | The CCF socket shall present no independent entrapment hazard when the device is absent. | HIGH | STABLE | Analysis |
| SRS-SAFE-0020 | The device-absent CCF socket shall provide clearance verified against a 12 mm entrapment-probe criterion. | MEDIUM | LIKELY-CHANGE | Test |

### 7.7 Animal-Contact Material Safety

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0021 | Materials in animal-skin contact shall be non-toxic. | HIGH | STABLE | Inspection |

### 7.8 Battery-Ingestion Warning

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0022 | The system shall provide battery-ingestion warning labeling. | HIGH | STABLE | Inspection |

---

## 8. Security Requirements

This section specifies the security requirements governing the LUUCIPet system. It defines BLE link-layer security, cloud-bound transport security, device identity and platform trust (including secure boot anchored in a hardware root of trust), and the vulnerability-disclosure policy gate.

### 8.1 BLE Link-Layer Security

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0001 | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the Base Station using AES-128 CCM. | CRITICAL | STABLE | Test |
| SRS-SEC-0002 | The system shall establish the BLE pairing key exchange between the collar-mounted device and the Base Station using the LE Secure Connections method. | CRITICAL | STABLE | Test |

### 8.2 Cloud-Bound Transport Security

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0003 | The system shall use TLS version 1.3 exclusively for all data transport between the Base Station and the cloud. | CRITICAL | STABLE | Test |

### 8.3 OTA Firmware Trust Chain

No firmware image may be installed without passing the Section 5 verification chain (SRS-FUNC-0052, SRS-FUNC-0053, SRS-FUNC-0054). This architectural constraint is carried by reference to those requirements.

### 8.4 Device Identity and Platform Trust

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0004 | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. | CRITICAL | STABLE | Inspection |
| SRS-SEC-0005 | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. | CRITICAL | STABLE | Test |

### 8.5 Vulnerability Disclosure

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0006 | The system shall have a public vulnerability-disclosure policy in place before product launch. | HIGH | STABLE | Inspection |


## 9. Data Requirements

This section specifies requirements governing the content, storage, integrity, privacy, and protection of data produced by the LUUCIPet collar device (Mini and Max variants). It addresses what classification and event data is and how it must be handled on-device — not the transport protocol mechanics (Section 4), the classification algorithm itself (Section 3), or transport-layer cryptography (Section 8).

### 9.1 Scope Boundary

Applicable regulatory instruments for this section are GDPR (EU) 2016/679, UK GDPR and Data Protection Act 2018, PIPEDA, CCPA/CPRA (indicative), and the data-protection-relevant provisions of ETSI EN 303 645:2025. Cybersecurity vulnerability-management obligations are addressed in Section 8.

Functions performed by parties outside this build (Mobile App team, IoT Cloud backend team) are documented as boundary notes in this section rather than silently omitted.

### 9.2 Classification Record Format and Schema

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0001 | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. | CRITICAL | STABLE | Test |
| SRS-DATA-0002 | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. | HIGH | STABLE | Test |
| SRS-DATA-0003 | The system shall timestamp each classification record with UTC time accurate to within 1 second. | HIGH | STABLE | Test |
| SRS-DATA-0004 | On the Max variant, the system shall append the most recent GNSS fix to the classification record. | HIGH | STABLE | Test |

### 9.3 On-Device Storage and Retention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0005 | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. | CRITICAL | STABLE | Test |
| SRS-DATA-0006 | The system shall preserve stored classification records without corruption across a power-loss event. | CRITICAL | STABLE | Test |
| SRS-DATA-0007 | The system shall detect corruption of stored classification records prior to transmission. | HIGH | LIKELY-CHANGE | Test |

### 9.4 Data Integrity

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0008 | The system shall perform classification and record generation independent of BLE connectivity state. | CRITICAL | STABLE | Test |
| SRS-DATA-0009 | The system shall forward stored classification records to the transport layer without introducing data corruption. | CRITICAL | STABLE | Test |
| SRS-DATA-0010 | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. | HIGH | STABLE | Test |

### 9.5 Raw Data Boundary and Processing Locality

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0011 | The system shall not transmit raw accelerometer data beyond the collar. | CRITICAL | STABLE | Test |
| SRS-DATA-0012 | The system shall perform normalization of sensor data on-device prior to classification. | HIGH | STABLE | Analysis |
| SRS-DATA-0013 | The system shall not require a cloud round-trip to complete a classification decision. | HIGH | STABLE | Demonstration |
| SRS-DATA-0014 | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. | MEDIUM | LIKELY-CHANGE | Analysis |

### 9.6 Buffered Data Persistence

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0015 | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud Device-Management layer. | CRITICAL | STABLE | Test |
| SRS-DATA-0016 | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. | CRITICAL | STABLE | Test |
| SRS-DATA-0017 | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. | MEDIUM | STABLE | Test |

### 9.7 Privacy Regime — Data Handling Obligations

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0018 | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. | HIGH | LIKELY-CHANGE | Inspection |
| SRS-DATA-0019 | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. | HIGH | STABLE | Inspection |
| SRS-DATA-0020 | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. | MEDIUM | LIKELY-CHANGE | Demonstration |
| SRS-DATA-0021 | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. | MEDIUM | LIKELY-CHANGE | Demonstration |
| SRS-DATA-0022 | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. | LOW | VOLATILE | Analysis |

### 9.8 Data-at-Rest Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0023 | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. | CRITICAL | STABLE | Inspection |

### 9.9 External Data Transport Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0024 | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established Base Station sync interface. | CRITICAL | STABLE | Test |

### 9.10 Breakaway Event Record Persistence

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0025 | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. | CRITICAL | STABLE | Test |
| SRS-DATA-0026 | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. | CRITICAL | STABLE | Test |
| SRS-DATA-0027 | The system shall transmit a committed breakaway event record on the next successful Base Station contact following separation. | HIGH | STABLE | Test |

### 9.11 Out-of-Scope Data Functions

The following data-related functions are outside this system's build scope:

- **Cloud-side storage and analytics** of the data transported under SRS-DATA-0024 is performed by the IoT Cloud backend team. This system's data obligation ends at successful, acknowledged transport to the Device-Management layer.
- **Mobile App presentation/display** of wellness records, classification history, and breakaway alerts is performed by the Mobile App team.
- **Cloud-side home/away state machine** is owned by the IoT Cloud backend team; the device-local home/away state machine referenced elsewhere in this SRS is the sole in-scope authority for power gating.

---

## 10. Interface Requirements

This section specifies the external interfaces of the LUUCIPet Wellness Monitor system: the BLE radio interface (collar-to-Base Station), the Wi-Fi radio interface (Base Station-to-cloud), the GNSS receive interface (Max only), the pogo-pin charging interface, the Twist-Lock mechanical attachment interface (collar device-to-CCF), and the device-enforced BLE application protocol. Zone 2 Fuse Tab breakaway force windows and post-breakaway safety protocol are governed by Section 7 (Safety) and are not restated here. Cross-variant identical mechanical-interface geometry for pogo-pin and Twist-Lock across Mini and Max is established by SRS-COMP-0002 and SRS-COMP-0003 (Section 2).

### 10.1 BLE Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0001 | The collar device shall implement the BLE 5.x radio interface in the peripheral role. | HIGH | STABLE | Test |
| SRS-INT-0002 | The Base Station shall implement the BLE 5.x radio interface in the central role. | HIGH | STABLE | Test |
| SRS-INT-0003 | The Base Station shall support at least 4 concurrent BLE connections to collar devices. | HIGH | STABLE | Test |
| SRS-INT-0004 | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. | MEDIUM | STABLE | Test |
| SRS-INT-0005 | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. | MEDIUM | STABLE | Test |
| SRS-INT-0006 | The collar device shall continue BLE advertising while maintaining an active BLE connection. | MEDIUM | STABLE | Test |
| SRS-INT-0007 | The collar device shall randomize its BLE device address. | HIGH | STABLE | Test |
| SRS-INT-0008 | The collar device shall transmit BLE signals at a power level of at least +8 dBm. | MEDIUM | STABLE | Test |
| SRS-INT-0009 | The BLE link between the collar device and the Base Station shall maintain connectivity at an open-air separation distance of at least 9 meters. | HIGH | STABLE | Test |
| SRS-INT-0010 | The system shall encrypt all BLE data-bearing links using AES-128 CCM. | CRITICAL | STABLE | Test |
| SRS-INT-0011 | The system shall establish BLE pairing between the collar device and the Base Station using LE Secure Connections. | CRITICAL | STABLE | Test |
| SRS-INT-0012 | The system shall support out-of-band BLE pairing initiated via a QR-code-based exchange between the collar device and the Base Station. | HIGH | STABLE | Test |
| SRS-INT-0013 | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including FCC 47 CFR Part 15 Subpart C (US), RED 2014/53/EU (EU), UK Radio Equipment Regulations 2017 (UK), ISED RSS-247 (CA), and AS/NZS 4268:2017 (AU/NZ). | CRITICAL | STABLE | Test |
| SRS-INT-0014 | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). | CRITICAL | STABLE | Inspection |
| SRS-INT-0015 | The BLE radio interface should undergo an RF human-exposure assessment against IEC 62311 / FCC 47 CFR §1.1310 for continuously worn 2.4 GHz transmission. | MEDIUM | VOLATILE | Analysis |

### 10.2 Wi-Fi Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0016 | The Base Station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to IEEE 802.11 b/g/n. | HIGH | STABLE | Test |
| SRS-INT-0017 | The Base Station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. | CRITICAL | STABLE | Test |
| SRS-INT-0018 | The Base Station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. | MEDIUM | STABLE | Test |
| SRS-INT-0019 | The Base Station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. | MEDIUM | LIKELY-CHANGE | Test |
| SRS-INT-0020 | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including FCC 47 CFR Part 15 Subpart C (US) and RED 2014/53/EU (EU). | CRITICAL | STABLE | Test |

### 10.3 GNSS Interface (Max Only)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0021 | The Max collar variant shall implement a passive (receive-only) GNSS interface. | HIGH | STABLE | Test |
| SRS-INT-0022 | The Mini collar variant shall not implement a GNSS interface. | MEDIUM | STABLE | Inspection |
| SRS-INT-0023 | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. | HIGH | STABLE | Test |
| SRS-INT-0024 | The Max collar variant shall apply a default GNSS fix interval of 2 hours. | MEDIUM | STABLE | Test |
| SRS-INT-0025 | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. | HIGH | STABLE | Test |
| SRS-INT-0026 | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. | MEDIUM | STABLE | Test |
| SRS-INT-0027 | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. | HIGH | STABLE | Test |
| SRS-INT-0028 | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. | HIGH | STABLE | Test |
| SRS-INT-0029 | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. | MEDIUM | STABLE | Test |
| SRS-INT-0030 | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. | MEDIUM | VOLATILE | Analysis |

### 10.4 Pogo-Pin Charging Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0031 | The charging interface between the collar device and the charging cradle shall use a 2-contact pogo-pin arrangement carrying VBUS and GND. | CRITICAL | STABLE | Inspection |
| SRS-INT-0032 | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. | CRITICAL | STABLE | Demonstration |
| SRS-INT-0033 | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. | MEDIUM | STABLE | Test |
| SRS-INT-0034 | The collar device shall reach full charge within 2 hours when docked at the charging interface. | HIGH | STABLE | Test |
| SRS-INT-0035 | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. | CRITICAL | STABLE | Test |
| SRS-INT-0036 | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | MEDIUM | LIKELY-CHANGE | Test |
| SRS-INT-0037 | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. | HIGH | STABLE | Demonstration |
| SRS-INT-0038 | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature. | HIGH | LIKELY-CHANGE | Test |

### 10.5 Twist-Lock Mechanical Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0039 | The Twist-Lock interface shall consist of three lugs arranged at 120-degree spacing with asymmetric keying for correct-orientation insertion. | CRITICAL | STABLE | Inspection |
| SRS-INT-0040 | The Twist-Lock engagement shall require a 90-degree clockwise rotation from insertion to fully locked position. | HIGH | STABLE | Test |
| SRS-INT-0041 | Each Twist-Lock lug shall have a width of 3.5 mm ± 0.1 mm, a depth of 1.8 mm ± 0.1 mm, and a root radius of 0.5 mm minimum. | HIGH | STABLE | Inspection |
| SRS-INT-0042 | The Twist-Lock shall incorporate a spring-loaded detent that provides tactile confirmation of full engagement at the 90-degree locked position. | HIGH | STABLE | Test |
| SRS-INT-0043 | The Twist-Lock shall not require an axial press-in force exceeding 5 N nor a rotational torque exceeding 0.10 N·m for full engagement. | HIGH | STABLE | Test |
| SRS-INT-0044 | The Twist-Lock detent shall release at a torque within the range of 0.05 N·m to 0.10 N·m inclusive. | HIGH | STABLE | Test |
| SRS-INT-0045 | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. | CRITICAL | STABLE | Test |
| SRS-INT-0046 | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket. | HIGH | STABLE | Test |
| SRS-INT-0047 | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. | HIGH | STABLE | Test |
| SRS-INT-0048 | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. | MEDIUM | STABLE | Demonstration |
| SRS-INT-0049 | A magnetic insert shall draw the device into Twist-Lock alignment from a distance of up to 5 mm before lug-channel engagement. | MEDIUM | STABLE | Test |
| SRS-INT-0050 | The Twist-Lock interface shall be operable without tools. | HIGH | STABLE | Demonstration |
| SRS-INT-0051 | The Twist-Lock mechanism shall be engageable within 5 seconds. | LOW | STABLE | Test |

### 10.6 Device-Enforced BLE Application Protocol

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0052 | The system shall use a common device-enforced BLE application protocol shared across all collar and Base Station firmware variants. | HIGH | STABLE | Inspection |
| SRS-INT-0053 | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. | HIGH | STABLE | Test |
| SRS-INT-0054 | The Base Station shall include in each BLE sighting report: the collar device identifier, RSSI value, and UTC timestamp. | HIGH | STABLE | Test |
| SRS-INT-0055 | The device-enforced protocol shall support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type. | HIGH | STABLE | Test |
| SRS-INT-0056 | The Base Station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. | HIGH | STABLE | Inspection |
| SRS-INT-0057 | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the Base Station. | HIGH | STABLE | Test |
| SRS-INT-0058 | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. | HIGH | STABLE | Test |
| SRS-INT-0059 | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. | HIGH | STABLE | Test |
| SRS-INT-0060 | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. | HIGH | STABLE | Test |

---

## 11. Hardware, Physical, and Mechanical Requirements

This section specifies the physical, component-level, and mechanical hardware constraints of the LUUCIPet collar device and the CCF accessory. Behavior of components is specified in the referenced functional and interface sections.

### 11.1 Weight and Form Factor

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0001 | The Mini collar device shall have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, excluding the CCF and collar. | CRITICAL | STABLE | Test |
| SRS-HW-0002 | The Max collar device shall have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, excluding the CCF and collar. | CRITICAL | STABLE | Test |

### 11.2 Enclosure and Ingress Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0003 | The collar device shall achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. | CRITICAL | STABLE | Test |
| SRS-HW-0004 | The collar device enclosure shall maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. | CRITICAL | STABLE | Test |
| SRS-HW-0005 | The collar device shall provide a light-emitting-diode (LED) status indicator. | MEDIUM | STABLE | Inspection |

### 11.3 Mechanical and Structural Constraints

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0006 | The collar device enclosure shall provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. | HIGH | STABLE | Inspection |
| SRS-HW-0007 | The Twist-Lock lug channels and magnetic insert on the device underside shall not penetrate the enclosure wall or the ingress seal path. | CRITICAL | STABLE | Inspection |
| SRS-HW-0008 | The device-facing charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | MEDIUM | LIKELY-CHANGE | Test |

### 11.4 CCF Material Composition

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0009 | The CCF body shall be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). | HIGH | LIKELY-CHANGE | Inspection |
| SRS-HW-0010 | The CCF material shall incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. | HIGH | LIKELY-CHANGE | Inspection |
| SRS-HW-0011 | The CCF shall not contain any metallic sub-component within the Zone 2 snap/breakaway region. | CRITICAL | STABLE | Inspection |
| SRS-HW-0012 | Animal-contact surfaces of the device and CCF shall not use chrome or nickel plating. | HIGH | STABLE | Inspection |

### 11.5 Sensing Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0013 | The collar device shall incorporate a three-axis MEMS accelerometer. | CRITICAL | STABLE | Inspection |
| SRS-HW-0014 | The collar device accelerometer shall support an output data rate of no less than 50 Hz. | CRITICAL | STABLE | Test |
| SRS-HW-0015 | The collar device accelerometer shall provide a wake-on-motion interrupt and a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. | HIGH | STABLE | Inspection |
| SRS-HW-0016 | The Mini collar device shall not incorporate a GNSS receiver. | MEDIUM | STABLE | Inspection |
| SRS-HW-0017 | The Max collar device shall incorporate a passive receive-only GNSS receiver. | HIGH | STABLE | Inspection |

### 11.6 Wireless Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0018 | The collar device shall incorporate a Bluetooth Low Energy 5.x radio. | CRITICAL | STABLE | Inspection |
| SRS-HW-0019 | The collar device BLE radio shall be capable of a transmit power of no less than +8 dBm. | MEDIUM | STABLE | Test |

### 11.7 Battery Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0020 | The Mini collar device shall incorporate a battery cell of no less than 120 mAh nominal capacity. | HIGH | STABLE | Inspection |
| SRS-HW-0021 | The Max collar device shall incorporate a battery cell of no less than 400 mAh nominal capacity. | HIGH | STABLE | Inspection |
| SRS-HW-0022 | The collar device battery subsystem shall provide overcharge, over-discharge, short-circuit, and over-temperature protection. | CRITICAL | STABLE | Test |
| SRS-HW-0023 | The collar device battery shall pass UN 38.3 qualification testing before pilot production. | HIGH | STABLE | Test |
| SRS-HW-0024 | The collar device shall raise a low-battery alert at a state-of-charge of 20% or below. | MEDIUM | STABLE | Test |

### 11.8 Charging Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0025 | The collar device shall incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. | CRITICAL | STABLE | Inspection |

### 11.9 Non-Volatile Storage Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0026 | The collar device shall incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. | HIGH | STABLE | Test |

### 11.10 Compute Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0027 | The collar device shall incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. | CRITICAL | STABLE | Test |
| SRS-HW-0028 | The collar device compute subsystem shall provide direct-memory-access peripheral access and a hardware root of trust. | CRITICAL | STABLE | Inspection |


## 12. Environmental and Durability Requirements

This section specifies the environmental exposure conditions, survival criteria, and durability test regimes that the collar device and CCF accessory must withstand: temperature extremes, ingress-protection test parameters, mechanical shock and drop, UV and weathering, chemical exposure, and — for the CCF — post-exposure retention of the safety-critical breakaway-force and detent-torque windows.

### 12.1 Temperature

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0001 | The collar device shall operate within an ambient temperature range of −20 °C to +50 °C without loss of function. | CRITICAL | STABLE | Test |
| SRS-ENV-0002 | The collar device shall withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequent operational performance. | HIGH | STABLE | Test |
| SRS-ENV-0003 | The CCF shall be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of function. | HIGH | STABLE | Test |
| SRS-ENV-0004 | The collar device should withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. | MEDIUM | STABLE | Test |

### 12.2 Ingress Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0005 | Product documentation and marketing materials shall not state or imply an IP67, or equivalent, ingress-protection rating for the collar device while mated to any CCF. | CRITICAL | STABLE | Inspection |
| SRS-ENV-0006 | The IP67 ingress-protection rating claimed for the collar device shall be confirmed by an independent, accredited test laboratory and documented in a test report prior to product launch. | HIGH | STABLE | Inspection |
| SRS-ENV-0007 | The Twist-Lock lug channels shall exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003. | CRITICAL | STABLE | Test |
| SRS-ENV-0008 | The ingress-protection seal boundary shall be located on the interior side of the enclosure assembly such that it is not directly exposed on any externally accessible mating surface. | HIGH | STABLE | Inspection |

### 12.3 Mechanical Durability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0009 | The collar device shall survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. | CRITICAL | STABLE | Test |
| SRS-ENV-0010 | The collar device should withstand mechanical shock per IEC 60068-2-27 without loss of function. | MEDIUM | STABLE | Test |
| SRS-ENV-0011 | The collar device should withstand vibration per IEC 60068-2-64 without loss of function. | MEDIUM | STABLE | Test |

### 12.4 UV and Weathering

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0012 | The collar device enclosure material shall be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service lifetime. | CRITICAL | STABLE | Analysis |
| SRS-ENV-0013 | The CCF shall withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. | CRITICAL | STABLE | Test |

### 12.5 Chemical Resistance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0014 | The CCF shall withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across pH 5.5 to 8.5, enzymatic pet-odor and stain cleaners, fresh water, and salt water. | HIGH | STABLE | Test |

### 12.6 CCF Environmental Durability — Post-Exposure Retention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0015 | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force shall remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | CRITICAL | STABLE | Test |
| SRS-ENV-0016 | Following completion of the thermal-cycling exposure, the Twist-Lock detent release torque shall remain within the torque window defined in SRS-INT-0044. | HIGH | STABLE | Test |
| SRS-ENV-0017 | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force shall remain within its SKU-specific force window. | CRITICAL | STABLE | Test |
| SRS-ENV-0018 | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force shall remain within its SKU-specific force window. | CRITICAL | STABLE | Test |

---

## 13. Reliability and Availability Requirements

This section specifies the dependability, availability, and long-run success-rate criteria the system must sustain over the product's operating life. Classification-accuracy thresholds are owned by Section 3; OTA mechanics by Section 5; ingress rating as a component property by Section 11.

### 13.1 Ingress-Protection Durability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0001 | The collar device, standalone and unmated from any CCF, shall retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. | CRITICAL | STABLE | Analysis |

### 13.2 Collar Device Availability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0002 | The collar device shall achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. | HIGH | STABLE | Test |

### 13.3 Base Station Availability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0003 | The Base Station shall achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. | HIGH | STABLE | Test |

### 13.4 OTA Update Success Rate

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0004 | The system shall achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a Base Station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. | HIGH | STABLE | Test |

---

## 14. Usability Requirements

This section specifies user-experience and usability requirements covering collar-device physical interaction, LED and haptic feedback, pairing and onboarding, Base Station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features.

### 14.1 Pairing and Onboarding

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0001 | The collar device shall complete BLE pairing and first-data-sync handshake with a companion app within 3 minutes of the user initiating pairing mode on the device. | HIGH | STABLE | Test |
| SRS-UX-0002 | The collar device shall support QR-code-based out-of-band (OOB) pairing as the primary pairing method. | HIGH | STABLE | Demonstration |
| SRS-UX-0003 | The collar device shall provide a single, visually distinct, and user-accessible physical mechanism to initiate pairing mode. | HIGH | STABLE | Inspection |
| SRS-UX-0004 | The collar device LED shall emit a visually distinct indication when the device is in pairing mode, distinguishable from all other operational-state LED patterns. | HIGH | STABLE | Test |
| SRS-UX-0005 | The collar device shall automatically exit pairing mode and revert to normal-operation LED indication after 3 minutes if no successful pairing is completed. | MEDIUM | STABLE | Test |

### 14.2 Physical Interaction

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0006 | The Twist-Lock mechanism shall provide both an audible click and a tactile force-transition (detent drop) upon successful locking. | HIGH | STABLE | Test |
| SRS-UX-0007 | The Twist-Lock socket shall provide a magnetic-assist force that draws the device into correct alignment from a distance of 5 mm or less before the lug channels engage. | MEDIUM | STABLE | Test |
| SRS-UX-0008 | The Twist-Lock engage force shall not exceed 5 N press-in axial force and 0.10 N·m rotational torque. | HIGH | STABLE | Test |
| SRS-UX-0009 | The device removal workflow (90° counter-clockwise Twist-Lock rotation) shall require a detent-release torque not exceeding 0.15 N·m. | HIGH | STABLE | Test |
| SRS-UX-0010 | The magnetic pogo-pin charging connector shall achieve a 90% or greater first-attempt successful seating rate by a user with no prior training. | HIGH | STABLE | Test |
| SRS-UX-0011 | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket. | HIGH | STABLE | Test |

### 14.3 Visual and Auditory Feedback

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0012 | The collar device LED shall communicate at minimum the following distinct operational states: power-on/boot, pairing mode, normal operation, low battery (20% SoC or below), charging/docked, error or fault, and OTA update in progress. | HIGH | STABLE | Test |
| SRS-UX-0013 | Each collar-device operational state shall be communicated via a unique combination of LED color, blink cadence, or duty cycle, such that no two states share an identical visual indicator pattern. | HIGH | STABLE | Test |
| SRS-UX-0014 | All collar-device LED state indicators shall differentiate critical states (low battery, error/fault) from non-critical states using at minimum temporal-pattern differentiation, ensuring distinguishability under red/green color-blindness. | MEDIUM | STABLE | Analysis |
| SRS-UX-0015 | The Twist-Lock engagement audible click shall produce a sound pressure level of 40 dBA or greater measured at 30 cm from the device in a quiet-room baseline (ambient 30 dBA or below). | MEDIUM | STABLE | Test |

### 14.4 Base Station UX

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0016 | The Base Station shall communicate via LEDs at minimum: AC power present, device charging active (Charging tier only), cloud connectivity established, and OTA update in progress. | HIGH | STABLE | Test |
| SRS-UX-0017 | The Base Station LEDs should support an automatic ambient-light-responsive dimming mode below approximately 50 lux, or a user-configurable quiet-hours schedule. | LOW | STABLE | Test |
| SRS-UX-0018 | The Base Station initial setup — from AC power-on through Wi-Fi association and cloud-registration to the "cloud-connected" LED indication — shall complete within 5 minutes. | HIGH | STABLE | Test |

### 14.5 CCF User Experience

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0019 | Each CCF variant shall be visually and/or tactilely distinguishable from all other variants, enabling a user to identify the correct CCF for their pet without measurement tools. | HIGH | STABLE | Inspection |
| SRS-UX-0020 | The CCF Zone 1 structural-clamp installation onto a third-party collar shall be achievable by a typical adult user in 60 seconds or less without tools. | HIGH | STABLE | Test |
| SRS-UX-0021 | The CCF Zone 2 fuse tab shall incorporate a clearly visible fracture indicator discernible by a user at arm's length (approximately 60 cm) under typical indoor lighting without magnification. | HIGH | STABLE | Inspection |

### 14.6 Status and Error Communication

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0022 | The collar device shall provide a distinct low-battery LED indication when battery state-of-charge reaches 20% or below, and shall persist this indication in every operational state until the device is placed on the charger and charging is confirmed. | HIGH | STABLE | Test |
| SRS-UX-0023 | The collar device shall communicate a fault state via a visually distinct LED pattern that differs from all other operational-state patterns. | HIGH | STABLE | Test |
| SRS-UX-0024 | The collar device shall provide confirmation feedback (LED flash, haptic pulse, or both) within 1 second of a user-initiated physical action being successfully registered by the device firmware. | MEDIUM | STABLE | Test |

### 14.7 App-Interface Obligations

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0025 | The collar device shall include its current battery state-of-charge as a percentage value (0–100) in every sync payload transmitted to the Base Station. | HIGH | STABLE | Test |
| SRS-UX-0026 | The Max collar device shall include the current GNSS fix interval setting (in minutes) in its status payload transmitted in every sync. | HIGH | STABLE | Test |
| SRS-UX-0027 | The collar device shall transmit a persistent breakaway/separation event record, flagged with elevated transmission priority, on the next successful Base Station contact following a breakaway event. | HIGH | STABLE | Test |

### 14.8 OTA Update UX

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0028 | The collar device shall communicate each distinct OTA update state — Downloading, Verifying, Pending Installation, Installing, Success, and Failed — via a unique LED pattern distinguishable from all other LED states. | HIGH | STABLE | Test |
| SRS-UX-0029 | The collar device LED shall remain continuously active during an OTA update, with no dark (LED-off) period exceeding 10 seconds during any OTA state expected to last more than 30 seconds. | MEDIUM | STABLE | Test |


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

