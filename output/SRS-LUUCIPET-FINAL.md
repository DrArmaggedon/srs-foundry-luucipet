# Software Requirements Specification
## LUUCIPet Wellness Monitor — Phase 1

---

**Document Reference:** SRS-LUUCIPET-FINAL  
**Issue:** 1.0  
**Issue Date:** July 2026  
**Classification:** Confidential — For Authorized Recipients Only  

**Conforms to:** IEEE 830-1998 / ISO/IEC/IEEE 29148:2018

---

## Document Control

### Prepared By

| Role | Organisation | Date |
|:-----|:-------------|:-----|
| Systems Engineering | SRS Foundry — Requirements Engineering | July 2026 |

### Revision History

| Revision | Date | Description |
|:---------|:-----|:------------|
| 1.0 | July 2026 | Final assembled deliverable. 18 sections approved. 397 requirements. RTM at 369 rows. Zero unresolved conflicts. All upstream gates PASSED. |

### Approval

| Role | Date |
|:-----|:-----|
| Lead Systems Engineer | July 2026 |
| Regulatory Affairs | July 2026 |
| Quality Assurance | July 2026 |

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [Functional Requirements — Behavioral Classification](#3-functional-requirements--behavioral-classification)
4. [Functional Requirements — Data Sync & Connectivity](#4-functional-requirements--data-sync--connectivity)
5. [Functional Requirements — OTA Firmware Updates](#5-functional-requirements--ota-firmware-updates)
6. [Performance Requirements](#6-performance-requirements)
7. [Safety Requirements](#7-safety-requirements)
8. [Security Requirements](#8-security-requirements)
9. [Data Requirements](#9-data-requirements)
10. [Interface Requirements](#10-interface-requirements)
11. [Hardware / Physical & Mechanical Requirements](#11-hardware--physical--mechanical-requirements)
12. [Environmental & Durability Requirements](#12-environmental--durability-requirements)
13. [Reliability & Availability Requirements](#13-reliability--availability-requirements)
14. [Usability Requirements](#14-usability-requirements)
15. [Operational Requirements](#15-operational-requirements)
16. [Maintainability Requirements](#16-maintainability-requirements)
17. [Standards Conformance](#17-standards-conformance)
18. [Regulatory Certification & Market Pathways](#18-regulatory-certification--market-pathways)

**Appendices**

A. [Requirements Traceability Matrix](#appendix-a--requirements-traceability-matrix-summary)  
B. [Regulatory Map Summary](#appendix-b--regulatory-map-summary)  
C. [Assumption Register](#appendix-c--assumption-register)  
D. [Glossary](#appendix-d--glossary)  
E. [Conflict Log Summary](#appendix-e--conflict-log-summary)  

---

## 1. Introduction

### 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

### 1.2 Scope

**In scope:** Mini and Max collar hardware and firmware; Base Station (Charging and Relay tiers) hardware and firmware; the device-enforced BLE and base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S, M, L; collar-types -RC, -MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar and base-station-facing interface contract.

**Out of scope:** GPS-M variant and cellular connectivity (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage and analytics backend; cloud-side home/away state machine; device-app interface control document.

### 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to and from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

### 1.4 Wellness-Not-Medical Boundary

| ID | Title | Statement | Priority | Stability | Source | Rationale | Verification Method |
|:---|:------|:----------|:---------|:----------|:-------|:----------|:--------------------|
| SRS-REG-0001 | Prohibit Medical-Classification Claims | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. | CRITICAL | STABLE | [PRD §13.6] | LUUCIPet is positioned as a general wellness device for animals, not a veterinary medical device. | Inspection |
| SRS-REG-0002 | Regulatory Classification Review Before Diagnostic-Adjacent Features | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. | CRITICAL | STABLE | [PRD §13.6] | Prevents inadvertent post-launch scope creep into medical-device territory. | Analysis |

### 1.5 Definitions and References

Full term definitions are maintained in the Glossary (Appendix D, derived from PRD §14.4). Standards and regulatory instruments are enumerated in the Regulatory Map (Appendix B) and cited inline using the closed source-tag set: `[PRD §x.x]`, `[STD: ID §clause]`, `[ASSUMPTION: A-NNNN]`, `[CONFLICT-RES: CR-NNNN]`, `[PRD — ABSENT: field]`.

---

## 2. Overall Description

### 2.1 Product Functions

The LUUCIPet Wellness Monitor is a collar-mounted behavioral wellness system for cats and dogs, comprising an ultra-light wearable device, a companion household Base Station, and a mechanical Collar Connection Fixture (CCF) accessory family. The system continuously classifies pet behavior on-device (accelerometer-based classification engine), relays behavioral and location data to the LUUCI IoT Cloud Device-Management layer via the Base Station, and supports over-the-air (OTA) firmware and classifier updates. The product is positioned strictly as a general wellness device for animals. [PRD §1]

At launch (Phase 1), the device ships with two factory-loaded Tier-1 behavioral classifiers (Rest/Sleep, Active/Awake); a broader Tier-2 classifier set is deliverable post-launch exclusively via OTA. [PRD §1], [PRD §4.4]

Functional responsibility is divided across in-scope deliverables and named external parties:

- **In scope:** on-device behavioral classification; collar-to-base BLE sync and base-to-cloud relay; charging; CCF breakaway/separation detection and event transport; device-side species-profile persistence; device-local home/away determination.
- **External-party:** owner-facing Mobile App alerts, onboarding, CCF guidance, and dashboards; IoT Cloud storage/analytics backend and cloud-side home/away state machine.
- **Future-phase (Phase 2):** GPS-M variant and cellular positioning.

### 2.2 Product Variants and Configurations

**Collar Devices:** Two variants sharing a common platform:
- **Mini** — ≤10 g; BLE-only; targets all cats and dogs; battery life ≥90 days (≥180 days Longevity Mode). [PRD §1], [PRD §4.1]
- **Max** — ≤22 g; BLE plus GNSS (receive-only); targets large dogs (>20 kg) and service dogs; battery life ≥45 days at 2-hour GNSS interval, ≥90 days at 4-hour interval. [PRD §1], [PRD §4.1]

**Base Station Family:** Two tiers sharing a common BLE-relay and Wi-Fi-uplink platform:
- **Charging** — BLE relay, Wi-Fi uplink, single-device pogo-pin charging cradle, 3 status LEDs.
- **Relay** — identical to Charging tier minus the charging cradle; 2 status LEDs.

**CCF Family:** Compound mechanical accessory with Zone 1 (structural retention) and Zone 2 (Fuse Tab — single-use breakaway). Width variants S/M/L; collar-type variants -RC (round) and -MG (martingale).

**Classifier Tiers:**
- Tier-1 (factory-loaded): Rest/Sleep; Active/Awake.
- Tier-2 (OTA-delivered, post-launch): Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting (dog only), Head-Shaking.

### 2.3 General Constraints

| ID | Title | Statement | Priority | Stability | Source | Rationale | VM |
|:---|:------|:----------|:---------|:----------|:-------|:----------|:---|
| SRS-OPER-0001 | At Least One Charging-Tier Base Station Per Household | A household deployment **shall** include at least one Base Station of the Charging tier. | CRITICAL | STABLE | [PRD §4.2], [PRD §4.5] | Without a Charging-tier station, no collar can be recharged. | Inspection |
| SRS-OPER-0002 | Maximum 8 Base Stations Per Household | A household deployment **shall not** exceed 8 Base Stations. | HIGH | STABLE | [PRD §4.2], [PRD §4.5] | Bounds BLE mesh and multi-device session load. | Test |
| SRS-OPER-0003 | Persist Species Assignment Across Resets | The collar device **shall** retain the species flag across firmware updates, power cycles, and factory resets. | HIGH | STABLE | [PRD §4.5], [PRD §7.2] | Species thresholds must remain stable. | Test |
| SRS-OPER-0004 | GNSS Smart Power Gate Not Owner-Configurable | The Max variant's GNSS smart power gate **shall not** be configurable by the owner. | HIGH | STABLE | [PRD §4.5] | Factory-controlled battery-life safeguard. | Inspection |
| SRS-OPER-0005 | In-Box CCF Fitment ≥80% Coverage | The in-box Standard CCF **shall** be appropriate for ≥80% of the launch population. | MEDIUM | LIKELY-CHANGE | [PRD §14.2] | Measurable coverage target for default accessory. | Analysis |
| SRS-OPER-0006 | Standard CCF as In-Box Default | The system **shall** ship a Standard CCF, sized to the paired collar variant, as the in-box default. | HIGH | STABLE | [PRD §4.1], [PRD §14.2] | Baseline accessory configuration. | Inspection |
| SRS-OPER-0007 | Degraded Mode Below Wi-Fi Reliability Bound | The Base Station **shall** enter offline-buffering mode (≥30 days retention) when Wi-Fi falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. | HIGH | STABLE | [ASSUMPTION: A-0009] | Operationalizes degraded-mode fallback. | Test |
| SRS-COMP-0001 | Collar-Agnostic Base Station Firmware | Base Station firmware **shall**, from a single common image, exhibit identical pairing/relay behavior for Mini and Max variants. | HIGH | STABLE | [PRD §4.3], [PRD §4.5] | Reduces field-support and OTA-fleet complexity. | Test |
| SRS-COMP-0002 | Universal CCF-to-Device Mechanical Compatibility | All CCF variants **shall** be mechanically compatible with both Mini and Max devices via the common Twist-Lock interface. | CRITICAL | STABLE | [PRD §4.1], [PRD §4.3] | Precondition for independent CCF SKU offering. | Test |
| SRS-COMP-0003 | Shared Classification Engine and Protocol | Mini and Max **shall** exhibit equivalent behavioral-classification outputs and use an interoperable common BLE protocol. | HIGH | STABLE | [PRD §4.3] | Ensures uniform Tier-2 OTA delivery and base-station compatibility. | Inspection |
| SRS-FUNC-0001 | Detect CCF Breakaway/Separation Signature | The device **shall** detect the CCF breakaway via accelerometer sensing and commit a persistent event record to NV storage within 5 s, with false-positive ≤0.1%/device-wear-day and detection ≥99% under DVT conditions. | CRITICAL | STABLE | [PRD §10.1.3.6], [ASSUMPTION: A-0015], [ASSUMPTION: A-0018] | Deterministic, always-powered portion of breakaway flow. | Test |
| SRS-FUNC-0003 | Preserve and Forward Breakaway Event | The persisted breakaway event **shall** survive power loss, battery depletion, and reboot, and be transmitted on next successful Base Station contact. | CRITICAL | STABLE | [PRD §8.4], [PRD §10.1.3.6], [ASSUMPTION: A-0018] | Released device may be lost/depleted before re-contact. | Test |
| SRS-FUNC-0002 | Transport Breakaway Event to Cloud | The Base Station **shall** transport a recorded breakaway event to the IoT Cloud Device-Management layer on next successful contact and cloud sync (event-triggered; no delivery-time guarantee). | CRITICAL | STABLE | [PRD §10.1.3.6], [PRD §8.5], [ASSUMPTION: A-0015], [ASSUMPTION: A-0018] | Best-effort in-scope hand-off enabling owner alert. | Test |

### 2.4 External-Party Requirements

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-OPER-0008 | Mobile App Post-Breakaway Owner Alert | The Mobile App **shall** display a "CCF Replacement Required" notification upon receiving a breakaway event from the device via the cloud. | HIGH | STABLE | [PRD §10.1.3.6], [EXTERNAL: Mobile App team] | Analysis — external evidence |
| SRS-OPER-0009 | Mobile App Species Re-Onboarding Flow | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's classifier profile. | MEDIUM | STABLE | [PRD §4.5], [EXTERNAL: Mobile App team] | Analysis — external evidence |
| SRS-OPER-0010 | Mobile App CCF Fitment/Sizing Guidance | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance. | MEDIUM | LIKELY-CHANGE | [PRD §14.2], [EXTERNAL: Mobile App team] | Analysis — external evidence |
| SRS-OPER-0011 | Cloud-Side Home/Away State Machine | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine for owner-facing geofence alerting. | MEDIUM | LIKELY-CHANGE | [ASSUMPTION: A-0016], [EXTERNAL: IoT Cloud backend team] | Analysis — external evidence |

### 2.5 Assumptions and Dependencies

Key assumptions underpinning this section (full register at Appendix C):

- [ASSUMPTION: A-0006] — Battery cell capacities: Mini ≥120 mAh, Max ≥400 mAh.
- [ASSUMPTION: A-0009] — Home Wi-Fi reliability bound: ≥−70 dBm RSSI at 2.4 GHz and ≥256 kbps sustained uplink.
- [ASSUMPTION: A-0012] — CCF assembled-mass constant (26 g, device+CCF-L) for Zone-2 force-window derivation.
- [ASSUMPTION: A-0013] — EU Battery Regulation Art. 11 removability exemption assumed for sealed IP67 battery.
- [ASSUMPTION: A-0014] — CCF-S feline breakaway force basis (~25–45 N per ASTM F2056); DVT re-validation gate.
- [ASSUMPTION: A-0015] — Device/base transport of telemetry/safety events to cloud is in-scope; cloud storage/analytics and app display are external.
- [ASSUMPTION: A-0016] — In-scope GNSS power gating relies solely on device-local home/away state machine.
- [ASSUMPTION: A-0017] — CCF Zone 2 breakaway is a design-level, INDICATIVE strangulation-prevention mitigation; DVT-pending.
- [ASSUMPTION: A-0018] — Breakaway detection bounds: ≤5 s detect+commit, false-positive ≤0.1%/day, detection ≥99%.

---

## 3. Functional Requirements — Behavioral Classification

**CAT: FUNC** | Maps to: PRD §7, §4.4

### 3.1 Classification Engine

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-FUNC-0004 | On-Device Behavioral Classification | The collar device **shall** classify pet behavior on-device using an accelerometer-based classification engine without requiring cloud connectivity. | CRITICAL | STABLE | [PRD §7.1] | Test |
| SRS-FUNC-0005 | Tier-1 Classifier — Rest/Sleep | The system **shall** classify Rest/Sleep behavior with accuracy ≥85% and false-positive rate ≤5%. | CRITICAL | STABLE | [PRD §7.4], [PRD §12.2] | Test |
| SRS-FUNC-0006 | Tier-1 Classifier — Active/Awake | The system **shall** classify Active/Awake behavior with accuracy ≥85% and false-positive rate ≤5%. | CRITICAL | STABLE | [PRD §7.4], [PRD §12.2] | Test |
| SRS-FUNC-0007 | Tier-2 Classifier OTA-Only Delivery | Tier-2 classifiers **shall** be delivered to the collar device exclusively via OTA firmware update. | CRITICAL | STABLE | [PRD §4.4], [PRD §7.3] | Inspection |
| SRS-FUNC-0008 | Tier-2 — Walking | The system **shall** classify Walking with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4], [PRD §12.2] | Test |
| SRS-FUNC-0009 | Tier-2 — Running | The system **shall** classify Running with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4], [PRD §12.2] | Test |
| SRS-FUNC-0010 | Tier-2 — Shaking | The system **shall** classify Shaking with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0011 | Tier-2 — Scratching | The system **shall** classify Scratching with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0012 | Tier-2 — Licking/Grooming | The system **shall** classify Licking/Grooming with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0013 | Tier-2 — Eating/Drinking | The system **shall** classify Eating/Drinking with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0014 | Tier-2 — Jumping | The system **shall** classify Jumping with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0015 | Tier-2 — Panting (Dog Only) | The Max variant **shall** classify Panting with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0016 | Tier-2 — Head-Shaking | The system **shall** classify Head-Shaking with accuracy ≥80% and false-positive ≤10%. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-FUNC-0017 | Species-Specific Classification Thresholds | The classification engine **shall** apply species-specific thresholds (cat vs. dog) as assigned during onboarding. | CRITICAL | STABLE | [PRD §7.2] | Test |

### 3.2 Classification Modes

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-FUNC-0018 | Wellness Mode Default Operation | The system **shall** operate in Wellness Mode as the default, continuously classifying all loaded Tier-1 and Tier-2 classifiers at the nominal sampling rate. | CRITICAL | STABLE | [PRD §7.3] | Test |
| SRS-FUNC-0019 | Insight Mode Owner-Activated | The system **shall** support Insight Mode, activated by the owner via the Mobile App, increasing classification sampling rate for a user-defined duration. | MEDIUM | STABLE | [PRD §7.3] | Test |

### 3.3 Baseline Calibration

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-FUNC-0020 | 72-Hour Baseline Calibration Period | The system **shall** complete an initial baseline calibration period of 72 hours after first activation before reporting normalized behavioral metrics. | HIGH | STABLE | [PRD §7.2] | Test |
| SRS-FUNC-0021 | On-Device Personalization | The system **shall** adapt classification thresholds to the individual pet over time using on-device learning without requiring cloud processing. | MEDIUM | LIKELY-CHANGE | [PRD §7.2] | Analysis |

---

## 4. Functional Requirements — Data Sync & Connectivity

**CAT: CONN** | Maps to: PRD §8, §6.3–§6.5, §10.3

### 4.1 BLE Connectivity

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-CONN-0001 | BLE 5.x Peripheral Role | The collar device **shall** operate as a BLE 5.x peripheral. | CRITICAL | STABLE | [PRD §8.2] | Test |
| SRS-CONN-0002 | BLE 5.x Central Role (Base Station) | The Base Station **shall** operate as a BLE 5.x central, supporting concurrent connections to both Mini and Max collar devices. | CRITICAL | STABLE | [PRD §8.2], [PRD §11.2] | Test |
| SRS-CONN-0003 | BLE Advertisement Configurability | The collar device **shall** support configurable BLE advertisement interval in the range 100 ms to 2000 ms. | HIGH | STABLE | [PRD §8.2] | Test |
| SRS-CONN-0004 | BLE Range ≥10 m | The collar-to-base BLE link **shall** maintain reliable data transfer at a range of at least 10 meters in free space. | HIGH | STABLE | [PRD §8.2] | Test |
| SRS-CONN-0005 | BLE Connection Recovery | The collar device **shall** automatically re-establish the BLE connection to any available in-range Base Station within 30 s of entering range after a disconnection. | HIGH | STABLE | [PRD §8.2] | Test |

### 4.2 Wi-Fi Uplink (Base Station)

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-CONN-0006 | Wi-Fi 802.11 b/g/n (2.4 GHz) | The Base Station **shall** support Wi-Fi 802.11 b/g/n in the 2.4 GHz band for cloud uplink. | CRITICAL | STABLE | [PRD §11.3] | Test |
| SRS-CONN-0007 | Wi-Fi WPA2/WPA3 Support | The Base Station **shall** support WPA2-Personal and WPA3-Personal Wi-Fi security protocols. | CRITICAL | STABLE | [PRD §11.3] | Test |

### 4.3 GNSS (Max Only)

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-CONN-0008 | GNSS Receive-Only Module (Max) | The Max variant **shall** include a GNSS receive-only module supporting GPS and GLONASS constellations. | HIGH | STABLE | [PRD §6.6] | Test |
| SRS-CONN-0009 | GNSS Power-Gated Off in HOME State | The Max variant's GNSS module **shall** be power-gated off when the device-local home/away state machine indicates the HOME state. | CRITICAL | STABLE | [PRD §6.4], [ASSUMPTION: A-0016] | Test |

### 4.4 Offline Operation

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-CONN-0010 | Connectivity-Independent Classification | The collar device **shall** continue behavioral classification and on-device data storage during periods with no BLE connectivity to any Base Station. | CRITICAL | STABLE | [PRD §8.1] | Test |
| SRS-CONN-0011 | On-Device Storage ≥30 Days | The collar device **shall** store at least 30 days of behavioral classification records locally when disconnected from all Base Stations. | CRITICAL | STABLE | [PRD §8.3] | Test |

---

## 5. Functional Requirements — OTA Firmware Updates

**CAT: FUNC (OTA)** | Maps to: PRD §9

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-FUNC-0043 | OTA Update Capability — Collar | The collar device **shall** support firmware updates delivered over-the-air via the Base Station BLE relay. | CRITICAL | STABLE | [PRD §9.1] | Test |
| SRS-FUNC-0044 | OTA Update Capability — Base Station | The Base Station **shall** support self-update of its own firmware over Wi-Fi from the LUUCI IoT Cloud Device-Management layer. | CRITICAL | STABLE | [PRD §9.1] | Test |
| SRS-FUNC-0045 | TLS 1.3 for OTA Transport | All OTA firmware image transfers between the cloud and Base Station **shall** use TLS version 1.3 exclusively. | CRITICAL | STABLE | [PRD §9.3], [STD: ETSI EN 303 645:2025] | Test |
| SRS-FUNC-0052 | Dual-Bank Partitioning | The collar device **shall** implement dual-bank firmware partitioning to support atomic firmware installation. | CRITICAL | STABLE | [PRD §9.2] | Inspection |
| SRS-FUNC-0053 | OTA Image Cryptographic Signature Verification | The device **shall** verify the cryptographic signature of each OTA firmware image before installation. | CRITICAL | STABLE | [PRD §9.3] | Test |
| SRS-FUNC-0054 | Anti-Rollback Protection | The device **shall** reject OTA firmware images whose version number is lower than the currently installed version. | CRITICAL | STABLE | [PRD §9.3] | Test |
| SRS-FUNC-0055 | Automatic Rollback on Boot Failure | The device **shall** automatically revert to the previous firmware bank if the new firmware fails to boot successfully within 3 attempts. | CRITICAL | STABLE | [PRD §9.4] | Test |
| SRS-FUNC-0056 | OTA Progress Reporting | The Base Station **shall** report OTA update progress (downloading, verifying, installing, success/failure) to the cloud. | HIGH | STABLE | [PRD §9.5] | Test |
| SRS-FUNC-0061 | SBOM Generation Per OTA Release | The system **shall** generate a Software Bill of Materials (SBOM) at each OTA firmware release. | MEDIUM | STABLE | [PRD §9.5] | Inspection |

---

## 6. Performance Requirements

**CAT: PERF** | Maps to: PRD §7.4, §12.1, §15

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-PERF-0001 | Mini Battery Life — Wellness Mode | The Mini collar device **shall** achieve battery life of at least 90 days in Wellness Mode at the nominal sampling rate. | CRITICAL | STABLE | [PRD §15.1] | Test |
| SRS-PERF-0002 | Mini Battery Life — Longevity Mode | The Mini collar device **shall** achieve battery life of at least 180 days in Longevity Mode. | HIGH | STABLE | [PRD §15.1] | Test |
| SRS-PERF-0003 | Max Battery Life — 2-Hour GNSS Fix Interval | The Max collar device **shall** achieve battery life of at least 45 days at a 2-hour GNSS fix interval. | CRITICAL | STABLE | [PRD §15.2] | Test |
| SRS-PERF-0004 | Max Battery Life — 4-Hour GNSS Fix Interval | The Max collar device **shall** achieve battery life of at least 90 days at a 4-hour GNSS fix interval. | HIGH | STABLE | [PRD §15.2] | Test |
| SRS-PERF-0005 | Classification Output Latency | The collar device **shall** produce a behavioral classification output within 2 seconds of detecting a behavioral state transition. | HIGH | STABLE | [PRD §7.4] | Test |
| SRS-PERF-0006 | Boot Time ≤3 s | The collar device **shall** complete boot and begin behavioral classification within 3 seconds of power-on. | HIGH | STABLE | [PRD §12.1] | Test |
| SRS-PERF-0007 | GNSS TTFF ≤60 s (Cold Start) | The Max variant's GNSS module **shall** achieve a cold-start Time to First Fix (TTFF) of no more than 60 seconds under open-sky conditions. | HIGH | STABLE | [PRD §6.6] | Test |
| SRS-PERF-0008 | Twist-Lock Engagement Time ≤2 s | The Twist-Lock engagement operation **shall** require no more than 2 seconds of owner manipulation for secure seating. | MEDIUM | STABLE | [PRD §10.5] | Test |

---

## 7. Safety Requirements

**CAT: SAFE** | Maps to: PRD §10.1.3, §10.1.4, §13.2

### 7.1 Zone 2 Fuse Tab — Breakaway (Strangulation Prevention)

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0001 | CCF-S Zone 2 Breakaway Force Window (Feline) | The Zone 2 Fuse Tab of the CCF-S variant **shall** fracture at axial load 15 N to 20 N. | CRITICAL | STABLE | [PRD §10.1.3.2b], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)], [ASSUMPTION: A-0017] | Test |
| SRS-SAFE-0002 | CCF-M Zone 2 Breakaway Force Window (Canine, Medium) | The Zone 2 Fuse Tab of the CCF-M variant **shall** fracture at axial load 20 N to 28 N. | CRITICAL | STABLE | [PRD §10.1.3.2b], [PRD §13.2], [ASSUMPTION: A-0017], [ASSUMPTION: A-0020] | Test |
| SRS-SAFE-0003 | CCF-L Zone 2 Breakaway Force Window (Canine, Large) | The Zone 2 Fuse Tab of the CCF-L variant **shall** fracture at axial load 28 N to 40 N, under design-basis assembled mass ≤26 g. | CRITICAL | STABLE | [PRD §10.1.3.2b], [PRD §10.1.4], [PRD §13.2], [ASSUMPTION: A-0017], [ASSUMPTION: A-0020] | Test |
| SRS-SAFE-0004 | CCF-L Force-Window Contingency for Mass >26 g | If assembled device+CCF-L mass exceeds 26 g, the CCF-L breakaway force floor **shall** be revised upward to 30 N. | CRITICAL | LIKELY-CHANGE | [PRD §10.1.4] | Analysis |
| SRS-SAFE-0005 | Zone 2 Single-Use Restriction | The Zone 2 Fuse Tab **shall not** be capable of reuse after fracture. | CRITICAL | STABLE | [PRD §10.1.3.2b], [PRD §13.2] | Test |
| SRS-SAFE-0006 | Zone 2 No-Detached-Fragment on Fracture | Upon fracture, the Zone 2 Fuse Tab **shall** not produce a detached fragment separate from the CCF body. | HIGH | STABLE | [PRD §10.1.3.2b] | Inspection |
| SRS-SAFE-0007 | Zone 2 Post-Fracture Surface Bluntness | Fracture surfaces of the Zone 2 Fuse Tab **shall** be blunt, presenting no sharp edge. | HIGH | STABLE | [PRD §10.1.3.2b] | Inspection |
| SRS-SAFE-0008 | Zone 2 Visible Fracture Indicator | The CCF **shall** present a visible fracture indicator upon Zone 2 breakaway. | HIGH | STABLE | [PRD §10.1.3.2b], [PRD §13.2] | Inspection |

### 7.2 Zone 1 — Structural Retention

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0009 | Zone 1 Structural Retention Force ≥50 N | The Zone 1 clamp **shall** retain axial loads of at least 50 N without structural failure. | CRITICAL | STABLE | [PRD §10.1.3.1], [PRD §10.1.3.4], [PRD §13.2] | Test |
| SRS-SAFE-0010 | Zone 1 Survival Through Zone 2 Fracture | The Zone 1 clamp **shall** remain structurally intact following a Zone 2 fracture event. | CRITICAL | STABLE | [PRD §10.1.3.1] | Test |

### 7.3 Twist-Lock Retention Safety

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0011 | Twist-Lock Axial Retention >100 N | The Twist-Lock device-to-CCF interface **shall** retain axial loads exceeding 100 N without disengaging. | HIGH | STABLE | [PRD §10.1.3.1] | Test |
| SRS-SAFE-0012 | Twist-Lock Retention Under Pet-Motion Inertial Loading | The Twist-Lock **shall** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. | HIGH | STABLE | [PRD §10.1.3.2a] | Test |

### 7.4 Post-Breakaway Protocol

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0013 | No-Wear-Without-Intact-Zone-2 | The device **shall** not be worn on an animal without a CCF that has an intact Zone 2 Fuse Tab. | CRITICAL | STABLE | [PRD §10.1.3.6] | Inspection |
| SRS-SAFE-0014 | Device Separation-Signature Emission | The device **shall** emit a detectable separation signature upon Zone 2 breakaway. | HIGH | STABLE | [PRD §10.1.3.6] | Test |
| SRS-SAFE-0015 | Mobile App CCF-Replacement-Required Notification | The Mobile App **shall** notify the owner that CCF replacement is required upon receiving a device separation signature. | HIGH | STABLE | [PRD §10.1.3.6], [EXTERNAL: Mobile App team] | Inspection (external evidence) |

### 7.5 Chew Resistance

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0016 | Zone 2 Non-Fracture Under Chew Load <250 N | The Zone 2 Fuse Tab **shall** not fracture under a compressive load below 250 N. | CRITICAL | STABLE | [PRD §13.2] | Test |
| SRS-SAFE-0017 | CCF Body Chew-Penetration Resistance | The CCF body **shall** resist penetration for at least 30 seconds under a 250 N compressive load. | HIGH | STABLE | [PRD §13.2] | Test |
| SRS-SAFE-0018 | Device Enclosure Chew Resistance | Materials in animal-skin contact on the device enclosure **shall** resist chew-induced damage. | MEDIUM | LIKELY-CHANGE | [PRD §10.1.2], [PRD — ABSENT: enclosure chew-resistance numeric bound] | Analysis |

### 7.6 Entrapment Prevention

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0019 | Device-Absent Socket Entrapment-Hazard Avoidance | The CCF socket **shall** present no independent entrapment hazard when the device is absent. | HIGH | STABLE | [PRD §10.1.3.5], [PRD §13.2] | Analysis |
| SRS-SAFE-0020 | Device-Absent Socket 12 mm Probe Clearance | The device-absent CCF socket **shall** provide clearance verified against a 12 mm entrapment-probe criterion. | MEDIUM | LIKELY-CHANGE | [PRD §10.1.3.5], [ASSUMPTION: A-0010] | Test |

### 7.7 Material Safety and Battery Warning

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SAFE-0021 | Animal-Contact Material Non-Toxicity | Materials in animal-skin contact **shall** be non-toxic. | HIGH | STABLE | [PRD §10.1.2], [PRD §13.2] | Inspection |
| SRS-SAFE-0022 | Battery-Ingestion Warning Labeling | The system **shall** provide battery-ingestion warning labeling. | HIGH | STABLE | [PRD §13.2], [ASSUMPTION: A-0011] | Inspection |

---

## 8. Security Requirements

**CAT: SEC** | Maps to: PRD §6.7, §12.3

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-SEC-0001 | BLE Link-Layer AES-128 CCM Encryption | The system **shall** encrypt every data-bearing BLE link between collar and base station using AES-128 CCM. | CRITICAL | STABLE | [PRD §6.7], [PRD §8.2], [PRD §12.3], [STD: ETSI EN 303 645:2025] | Test |
| SRS-SEC-0002 | BLE LE Secure Connections Pairing | The system **shall** establish BLE pairing key exchange using the LE Secure Connections method. | CRITICAL | STABLE | [PRD §6.3], [PRD §8.2], [STD: ETSI EN 303 645:2025] | Test |
| SRS-SEC-0003 | TLS 1.3 for Base-to-Cloud Transport | The system **shall** use TLS version 1.3 exclusively for all data transport between the base station and the cloud. | CRITICAL | STABLE | [PRD §6.5], [PRD §12.3], [STD: ETSI EN 303 645:2025] | Test |
| SRS-SEC-0004 | Unique Cryptographic Identity at Manufacturing | The system **shall** provision each manufactured device with a unique cryptographic identity at the time of manufacturing. | CRITICAL | STABLE | [PRD §12.3] | Inspection |
| SRS-SEC-0005 | Secure Boot Anchored in Hardware Root of Trust | The device **shall** verify its own firmware integrity at boot using a hardware root of trust before executing application code. | CRITICAL | STABLE | [PRD §10.7] | Test |
| SRS-SEC-0006 | Public Vulnerability-Disclosure Policy Before Launch | The system **shall** have a public vulnerability-disclosure policy in place before product launch. | HIGH | STABLE | [PRD §12.3], [PRD §13.5], [STD: ETSI EN 303 645:2025], [STD: EU CRA (EU) 2024/2847 Art 13-14] | Inspection |

---

## 9. Data Requirements

**CAT: DATA** | Maps to: PRD §7.5–§7.7, §8, §10.6, §13.5

### 9.1 Classification Record Format

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-DATA-0001 | Classification Record Content | The system **shall** generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. | CRITICAL | STABLE | [PRD §7.5] | Test |
| SRS-DATA-0002 | Confidence Score Bound 0.0–1.0 | The system **shall** express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. | HIGH | STABLE | [PRD §7.5] | Test |
| SRS-DATA-0003 | Record Timestamp Accuracy | The system **shall** timestamp each classification record with UTC time accurate to within ±5 seconds. | HIGH | STABLE | [PRD §7.5] | Test |

### 9.2 Storage and Retention

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-DATA-0004 | On-Device Non-Volatile Storage | Classification records **shall** be stored in non-volatile memory and survive power loss without data corruption. | CRITICAL | STABLE | [PRD §8.3] | Test |
| SRS-DATA-0005 | Device Data Retention ≥30 Days | The collar device **shall** retain at least 30 days of classification records in on-device storage. | CRITICAL | STABLE | [PRD §8.3] | Test |
| SRS-DATA-0006 | Base Station Buffer Retention ≥30 Days | The Base Station **shall** retain buffered collar data for at least 30 days during cloud connectivity loss. | HIGH | STABLE | [PRD §11.7] | Test |
| SRS-DATA-0007 | FIFO Eviction on Storage Full | When on-device storage reaches capacity, the system **shall** evict the oldest records first (FIFO). | HIGH | STABLE | [PRD §8.3] | Test |

### 9.3 Sync and Integrity

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-DATA-0008 | Delta-Transfer Sync Behavior | The system **shall** transfer only new or changed records (delta sync) since the last confirmed cloud acknowledgment. | HIGH | STABLE | [PRD §8.4] | Test |
| SRS-DATA-0009 | Acknowledged-Record Clearance | Records **shall** be eligible for clearance from on-device storage only after the device receives cloud acknowledgment of receipt. | HIGH | STABLE | [PRD §8.4] | Test |
| SRS-DATA-0010 | Stale-Data Flagging on Reconnection | Records older than 30 days at the time of successful sync **shall** be flagged as stale in the transmitted payload. | MEDIUM | STABLE | [PRD §8.5] | Test |

### 9.4 Data Privacy

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-DATA-0011 | GDPR Data Minimization Principle | The system **shall** collect and transmit only the minimum personal data necessary for its stated wellness-monitoring function. | CRITICAL | STABLE | [PRD §13.5], [STD: GDPR (EU) 2016/679 Art 5] | Analysis |
| SRS-DATA-0012 | Data Sensitivity Classification | All pet behavioral and location data **shall** be classified and handled as personal data under the applicable privacy framework(s). | CRITICAL | STABLE | [PRD §13.5], [ASSUMPTION: A-0005] | Inspection |

---

## 10. Interface Requirements

**CAT: INT** | Maps to: PRD §6, §10.2, §10.3, §10.5, §11

### 10.1 Collar-to-Base Station BLE Interface

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-INT-0001 | BLE GATT Service for Behavioral Data | The collar device **shall** expose a dedicated BLE GATT service for behavioral classification data transfer to the Base Station. | CRITICAL | STABLE | [PRD §8.2] | Test |
| SRS-INT-0002 | BLE GATT Service for Device Status | The collar device **shall** expose a BLE GATT service for device status (battery level, firmware version, operational mode) to the Base Station. | HIGH | STABLE | [PRD §8.2] | Test |

### 10.2 Base-Station-to-Cloud Interface

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-INT-0003 | MQTT or HTTPS Cloud Transport Protocol | The Base Station **shall** communicate with the LUUCI IoT Cloud Device-Management layer using MQTT or HTTPS as the application-layer transport protocol. | CRITICAL | STABLE | [PRD §11.3] | Test |
| SRS-INT-0004 | JSON Payload Format | All data payloads between Base Station and cloud **shall** be formatted as JSON. | HIGH | STABLE | [PRD §11.4] | Inspection |

### 10.3 Charging Interface

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-INT-0005 | Pogo-Pin Magnetic Charging Interface | The collar device **shall** use a magnetic pogo-pin interface for charging, with contact count sufficient for power and ground. | CRITICAL | STABLE | [PRD §10.5] | Test |
| SRS-INT-0036 | Charging Socket Self-Drainage | The charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the device held in its normal worn orientation (0–45° from vertical). | MEDIUM | LIKELY-CHANGE | [PRD §10.5], [PRD §10.1.3.5], [ASSUMPTION: A-0023] | Test |

### 10.4 CCF Twist-Lock Mechanical Interface

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-INT-0006 | Twist-Lock 3-Lug Bayonet Geometry | The device-to-CCF interface **shall** employ a 3-lug bayonet Twist-Lock geometry. | CRITICAL | STABLE | [PRD §10.5] | Inspection |
| SRS-INT-0007 | Twist-Lock Detent Torque Window | The Twist-Lock detent release torque **shall** fall within the calibrated torque window established during DVT. | HIGH | STABLE | [PRD §10.5] | Test |

---

## 11. Hardware / Physical & Mechanical Requirements

**CAT: COMP-HW** | Maps to: PRD §10

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-HW-0001 | Mini Device Mass ≤10 g | The Mini collar device **shall** have a mass not exceeding 10 grams (excluding CCF). | CRITICAL | STABLE | [PRD §10.1] | Test |
| SRS-HW-0002 | Max Device Mass ≤22 g | The Max collar device **shall** have a mass not exceeding 22 grams (excluding CCF). | CRITICAL | STABLE | [PRD §10.1] | Test |
| SRS-HW-0003 | Device-Standalone IP67 Rating | The collar device, standalone and unmated from any CCF, **shall** achieve an IP67 ingress-protection rating per IEC 60529. | CRITICAL | STABLE | [PRD §10.1.1], [STD: IEC 60529] | Test |
| SRS-HW-0004 | Exposed Pogo-Pin Contact Ingress Integrity | The pogo-pin charging contacts **shall** maintain ingress protection consistent with the device's IP67 rating. | HIGH | STABLE | [PRD §10.5] | Test |
| SRS-HW-0005 | CCF Base Polymer — PA66-GF30 | The CCF body **shall** be manufactured from PA66-GF30 (glass-fiber-reinforced polyamide 66). | HIGH | STABLE | [PRD §10.2] | Inspection |
| SRS-HW-0006 | No Metallic Subcomponents in Breakaway Zone | The Zone 2 Fuse Tab region of the CCF **shall** contain no metallic subcomponents. | CRITICAL | STABLE | [PRD §10.1.3.2b] | Inspection |
| SRS-HW-0007 | No Chrome/Nickel Plating on Animal-Contact Surfaces | Animal-contact surfaces on the device enclosure and CCF **shall not** use chrome or nickel plating. | HIGH | STABLE | [PRD §10.1.2] | Inspection |
| SRS-HW-0008 | Charging Socket Self-Drainage Criterion | The device-facing charging socket **shall** drain per the acceptance criterion in SRS-INT-0036. | MEDIUM | LIKELY-CHANGE | [PRD §10.5], [ASSUMPTION: A-0023] | Test |

---

## 12. Environmental & Durability Requirements

**CAT: ENV** | Maps to: PRD §12.5, §13.4

### 12.1 Temperature

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-ENV-0001 | Device Operating Temperature −20 °C to +50 °C | The collar device **shall** operate within −20 °C to +50 °C without loss of function. | CRITICAL | STABLE | [PRD §12.5] | Test |
| SRS-ENV-0002 | Device Storage Temperature −30 °C to +60 °C | The collar device **shall** withstand non-operating storage at −30 °C to +60 °C without degradation. | HIGH | STABLE | [PRD §12.5] | Test |
| SRS-ENV-0003 | CCF Thermal-Cycling Exposure per IEC 60068-2-14 Test Na | The CCF **shall** be subjected to thermal cycling −20 °C to +50 °C per IEC 60068-2-14 Test Na without loss of function. | HIGH | STABLE | [PRD §12.5], [ASSUMPTION: A-0003] | Test |

### 12.2 Ingress Protection

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-ENV-0005 | Prohibit IP67 Claims for CCF-Mated Configuration | Product documentation **shall not** state or imply an IP67 rating for the device while mated to any CCF. | CRITICAL | STABLE | [PRD §4.1], [PRD §13.4] | Inspection |
| SRS-ENV-0006 | Independent Lab Confirmation of IP67 | The IP67 rating **shall** be confirmed by an independent, accredited test laboratory prior to product launch. | HIGH | STABLE | [PRD §13.4] | Inspection |
| SRS-ENV-0007 | Twist-Lock Channel Water-Ingress Exclusion | The Twist-Lock lug channels **shall** exclude water ingress when subjected to the IP67 immersion test. | CRITICAL | STABLE | [PRD §13.4] | Test |

### 12.3 Mechanical Durability

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-ENV-0009 | 1.5 m Drop Survival | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. | CRITICAL | STABLE | [PRD §12.5] | Test |
| SRS-ENV-0010 | IEC 60068-2-27 Mechanical Shock Resistance (Recommended) | The collar device **should** withstand mechanical shock per IEC 60068-2-27. | MEDIUM | STABLE | [PRD §13.4] | Test |
| SRS-ENV-0011 | IEC 60068-2-64 Vibration Resistance (Recommended) | The collar device **should** withstand vibration per IEC 60068-2-64. | MEDIUM | STABLE | [PRD §13.4] | Test |

### 12.4 UV and Chemical Resistance

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-ENV-0012 | Enclosure UV Stabilization | The collar device enclosure material **shall** be UV-stabilized to resist degradation over the product's service lifetime. | CRITICAL | STABLE | [PRD §12.5] | Analysis |
| SRS-ENV-0013 | CCF UV Aging 2,000 Hours per IEC 60068-2-5 | The CCF **shall** withstand 2,000 hours of UV exposure per IEC 60068-2-5 without loss of function. | CRITICAL | STABLE | [PRD §12.5] | Test |
| SRS-ENV-0014 | CCF Chemical-Fluid Exposure 24 Hours | The CCF **shall** withstand 24 hours of continuous exposure to pet shampoo (pH 5.5–8.5), enzymatic cleaners, fresh water, and salt water without loss of function. | HIGH | STABLE | [PRD §12.5] | Test |

### 12.5 Post-Exposure Retention

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-ENV-0015 | Post-Thermal-Cycling Zone 2 Force-Window Retention | After thermal cycling (SRS-ENV-0003), the Zone 2 breakaway force **shall** remain within its SKU-specific force window. | CRITICAL | STABLE | [PRD §12.5] | Test |
| SRS-ENV-0017 | Post-UV-Aging Zone 2 Force-Window Retention | After UV aging (SRS-ENV-0013), the Zone 2 breakaway force **shall** remain within its SKU-specific force window. | CRITICAL | STABLE | [PRD §12.5] | Test |
| SRS-ENV-0018 | Post-Chemical-Exposure Zone 2 Force-Window Retention | After chemical exposure (SRS-ENV-0014), the Zone 2 breakaway force **shall** remain within its SKU-specific force window. | CRITICAL | STABLE | [PRD §12.5] | Test |

---

## 13. Reliability & Availability Requirements

**CAT: RELI** | Maps to: PRD §12.2

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-RELI-0001 | IP67 Rating Retention Over 2-Year Service Lifetime | The collar device, standalone and unmated, **shall** retain its IP67 rating (SRS-HW-0003) for no less than 2 years of expected service life. | CRITICAL | STABLE | [PRD §12.2], [PRD — ABSENT: service_lifetime_duration_value] | Analysis |
| SRS-RELI-0002 | Collar Device Operational Availability ≥99% | The collar device **shall** achieve operational availability of no less than 99%, excluding time docked and charging. | HIGH | STABLE | [PRD §12.2] | Analysis |
| SRS-RELI-0003 | Base Station Uptime ≥99.5% Over 90-Day Rolling Window | The base station **shall** achieve uptime of no less than 99.5%, measured over any rolling 90-day window. | HIGH | STABLE | [PRD §12.2] | Analysis |
| SRS-RELI-0004 | OTA Delivery Success Rate ≥99% | The OTA firmware update delivery success rate **shall** be no less than 99% across the deployed fleet. | HIGH | STABLE | [PRD §9.5] | Analysis |

---

## 14. Usability Requirements

**CAT: UX** | Maps to: PRD §12.4, §5

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-UX-0001 | First-Time Pairing Setup ≤3 Minutes | A first-time user **shall** be able to complete initial collar-to-base-station pairing and the companion setup workflow within 3 minutes. | HIGH | STABLE | [PRD §12.4] | Test |
| SRS-UX-0002 | CCF Twist-Lock Tool-Free Installation | The CCF Twist-Lock installation and removal **shall** be performed without tools. | CRITICAL | STABLE | [PRD §10.5] | Test |
| SRS-UX-0003 | Charging Docking Confirmation Feedback | The Base Station **shall** provide a visual confirmation within 2 seconds of successful collar docking on the charging cradle. | HIGH | STABLE | [PRD §10.5] | Test |
| SRS-UX-0004 | CCF Visual SKU Distinguishability | CCF variants (S/M/L, -RC/-MG) **shall** be visually distinguishable by the owner without measurement tools. | MEDIUM | STABLE | [PRD §4.5] | Inspection |

---

## 15. Operational Requirements

**CAT: OPER** | Maps to: PRD §6.4, §11.7, §15.5

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-OPER-0012 | Wellness Mode — Continuous Classification | The collar device **shall** perform continuous behavioral classification when in Wellness Mode. | CRITICAL | STABLE | [PRD §7.3] | Test |
| SRS-OPER-0013 | Longevity Mode — Reduced Sampling | The collar device **shall** reduce classification sampling rate in Longevity Mode to extend battery life to the defined targets. | HIGH | STABLE | [PRD §7.3] | Test |
| SRS-OPER-0014 | GNSS Smart Power Gate — Non-Configurable | The Max variant's GNSS module **shall** be power-gated off when the device-local state machine determines the HOME state, and this behavior **shall not** be owner-configurable. | CRITICAL | STABLE | [PRD §6.4], [ASSUMPTION: A-0016] | Test |
| SRS-OPER-0015 | GNSS Fix Interval Configurable 2-Hour or 4-Hour | The Max variant **shall** support GNSS fix intervals of 2 hours and 4 hours, selectable via the Mobile App. | HIGH | STABLE | [PRD §6.6] | Test |
| SRS-OPER-0016 | Device-Local Home/Away Fallback After >24 h Cloud Loss | The device **shall** revert to a device-local home/away determination if cloud connectivity is lost for more than 24 hours. | HIGH | STABLE | [PRD §6.4], [ASSUMPTION: A-0016] | Test |
| SRS-OPER-0023 | Expected Service Lifetime 2–3 Years (2-Year Testable Floor) | The product **shall** meet all specified performance and safety criteria for a minimum of 2 years under normal use conditions. | HIGH | STABLE | [PCP §8] | Analysis |

---

## 16. Maintainability Requirements

**CAT: MAINT** | Maps to: PRD §12.7

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-MAINT-0001 | OTA-Update Capability Through Supported Service Lifetime | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. | HIGH | STABLE | [PRD §12.7] | Inspection |
| SRS-MAINT-0002 | SBOM Currency Across Supported Service Lifetime | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetime. | MEDIUM | STABLE | [PRD §12.7], [PRD §9.5] | Inspection |
| SRS-MAINT-0003 | Post-Launch Vulnerability-Disclosure Process Continuity | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported service lifetime. | HIGH | STABLE | [PRD §12.7], [STD: EU CRA (EU) 2024/2847 Art 13-14] | Inspection |

---

## 17. Standards Conformance

**CAT: COMP** | Maps to: PRD §13.1, §13.3, §13.4, §13.7, §12.6

### 17.1 Ingress Protection

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-COMP-0005 | IEC 60529 IPX7 Conformance | The collar device, standalone (CCF-unmated), **shall** conform to IEC 60529 IPX7 test methodology as the verification basis for IP67. | CRITICAL | STABLE | [PRD §13.4], [STD: IEC 60529] | Inspection |

### 17.2 Battery and Electrical Safety

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-COMP-0006 | IEC 62133-2 Battery Cell Safety | Li-Po battery cells **shall** conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). | CRITICAL | LIKELY-CHANGE | [PRD §13.3] | Inspection |
| SRS-COMP-0007 | UN 38.3 Battery Transport Safety | Li-Po battery cells **shall** conform to UN Manual of Tests and Criteria, Part III, Section 38.3 prior to pilot production. | CRITICAL | STABLE | [PRD §10.4], [PRD §13.3] | Inspection |
| SRS-COMP-0008 | UL 1642/UL 2054 US Cell Safety | Li-Po cells **shall** conform to UL 1642 or UL 2054 for the US market. | HIGH | STABLE | [PRD §13.3] | Inspection |
| SRS-COMP-0009 | EN 62368-1/UL 62368-1 Base Station Electrical Safety | The Base Station, both tiers, **shall** conform to EN 62368-1:2020 or UL 62368-1. | CRITICAL | STABLE | [PRD §13.3] | Inspection |

### 17.3 IoT Cybersecurity

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-COMP-0010 | ETSI EN 303 645:2025 Consumer IoT Security Baseline | The system **shall** conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline. | CRITICAL | LIKELY-CHANGE | [PRD §12.3], [PRD §13.5] | Inspection |

### 17.4 Environmental Test Methods

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-COMP-0011 | IEC 60068-2-14 Thermal Cycling | CCF thermal-cycling qualification (SRS-ENV-0003) **shall** be conducted per IEC 60068-2-14 Test Na. | HIGH | STABLE | [PRD §12.5], [ASSUMPTION: A-0003] | Inspection |
| SRS-COMP-0015 | IEC 60068-2-5 UV Aging | CCF UV-aging qualification (SRS-ENV-0013) **shall** be conducted per IEC 60068-2-5. | CRITICAL | STABLE | [PRD §12.5] | Inspection |

### 17.5 Radio and EMC

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-COMP-0016 | ETSI EN 300 328 2.4 GHz Radio | The BLE 5.x radio interface **shall** conform to ETSI EN 300 328 for the EU market. | CRITICAL | STABLE | [PRD §13.1] | Inspection |
| SRS-COMP-0017 | Bluetooth SIG Qualification (QDID) | Each collar variant and Base Station tier **shall** hold a valid Bluetooth SIG Qualified Design ID prior to product launch. | CRITICAL | STABLE | [PRD §13.1] | Inspection |
| SRS-COMP-0018 | FCC Part 15 Subpart C (Intentional Radiator) | The BLE radio interface **shall** conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. | CRITICAL | STABLE | [PRD §13.1] | Inspection |
| SRS-COMP-0020 | RED 2014/53/EU Essential Requirements | The collar devices and Base Station **shall** conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. | CRITICAL | STABLE | [PRD §13.1] | Inspection |

### 17.6 Materials and Environmental Compliance

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-COMP-0022 | REACH Regulation Conformance | Device and CCF materials **shall** conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. | CRITICAL | STABLE | [PRD §10.1.2], [PRD §13.2], [PRD §13.7] | Inspection |
| SRS-COMP-0023 | RoHS Directive Conformance | Electronic components and materials **shall** conform to RoHS 2011/65/EU as amended by 2015/863. | CRITICAL | STABLE | [PRD §13.7] | Inspection |
| SRS-COMP-0024 | California Proposition 65 Conformance | The system **shall** conform to California Proposition 65 warning and substance-disclosure requirements. | HIGH | STABLE | [PRD §13.7] | Inspection |
| SRS-COMP-0025 | EU Battery Regulation Material and Labelling | Li-Po cells **shall** conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. | CRITICAL | STABLE | [PRD §13.7] | Inspection |
| SRS-COMP-0026 | WEEE Directive Conformance | The system and packaging **shall** conform to WEEE 2012/19/EU. | HIGH | STABLE | [PRD §13.7] | Inspection |

---

## 18. Regulatory Certification & Market Pathways

**CAT: REG** | Maps to: PRD §13.1, §13.2, §13.5, §13.6, §13.7

### 18.1 United States Market

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-REG-0003 | FCC Identifier Marking | Each collar variant and Base Station tier **shall** bear a unique FCC Identifier (FCC ID) prior to commercial distribution in the US. | HIGH | STABLE | [PRD §13.1] | Inspection |
| SRS-REG-0004 | NRTL Listing for Base Station Electrical Safety | Each Base Station tier **shall** hold a valid NRTL listing evidencing UL 62368-1 conformance prior to US commercial distribution. | HIGH | STABLE | [PRD §13.3] | Inspection |
| SRS-REG-0005 | California Proposition 65 Conditional Warning Labeling | The system **shall** bear a Proposition 65 warning label if any listed substance is present above the applicable safe-harbor threshold. | HIGH | STABLE | [PRD §13.7] | Inspection |
| SRS-REG-0007 | GNSS Passive-Receiver Intentional-Radiator Exemption Determination | The Max variant's GNSS receive-only module **shall** undergo a documented applicability determination for FCC intentional-radiator exemption prior to US commercial distribution. | HIGH | VOLATILE | [PRD §13.1] | Analysis |

### 18.2 European Union / EEA Market

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-REG-0008 | CE Marking — RED Directive | The collar devices and Base Station **shall** bear CE marking under RED 2014/53/EU prior to placing on the EU/EEA market. | CRITICAL | STABLE | [PRD §13.1] | Inspection |
| SRS-REG-0009 | EU GPSR Compliance File | The system **shall** be accompanied by a technical documentation file demonstrating conformity with EU GPSR (EU) 2023/988 prior to placing on the EU market. | CRITICAL | STABLE | [PRD §13.2] | Inspection |
| SRS-REG-0010 | EU Declaration of Conformity | The system **shall** be accompanied by an EU Declaration of Conformity covering RED, RoHS, and GPSR prior to placing on the EU market. | CRITICAL | STABLE | [PRD §13.1], [PRD §13.7] | Inspection |

### 18.3 United Kingdom Market

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-REG-0011 | UKCA Marking | The system **shall** bear UKCA marking under UK Radio Equipment Regulations 2017 prior to placing on the GB market. | CRITICAL | STABLE | [PRD §13.1] | Inspection |

### 18.4 Canada Market

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-REG-0012 | ISED Certification | The system **shall** hold valid ISED certification under RSS-247 prior to commercial distribution in Canada. | CRITICAL | STABLE | [PRD §13.1] | Inspection |

### 18.5 Australia / New Zealand Market

| ID | Title | Statement | Priority | Stability | Source | VM |
|:---|:------|:----------|:---------|:----------|:-------|:---|
| SRS-REG-0013 | RCM Marking | The system **shall** bear RCM marking under AS/NZS 4268:2017 prior to placing on the AU/NZ market. | HIGH | STABLE | [PRD §13.1] | Inspection |

---

## Appendix A — Requirements Traceability Matrix Summary

The full Requirements Traceability Matrix comprises **369 rows** across 18 sections, maintained in CSV format. The traceability structure maps each requirement ID to its source(s), priority, verification method, and cross-references.

### RTM Section Summary

| Section | CAT | Requirement Count | ID Range |
|:--------|:----|:-----------------|:---------|
| §1 Introduction | — | 2 | SRS-REG-0001–0002 |
| §2 Overall Description | — | 15 | SRS-OPER-0001–0011, SRS-COMP-0001–0003, SRS-FUNC-0001–0003 |
| §3 Behavioral Classification | FUNC | 18 | SRS-FUNC-0004–0021 |
| §4 Data Sync & Connectivity | CONN | 11 | SRS-CONN-0001–0011 |
| §5 OTA Firmware Updates | FUNC (OTA) | 19 | SRS-FUNC-0043–0061 |
| §6 Performance | PERF | 8 | SRS-PERF-0001–0008 |
| §7 Safety | SAFE | 22 | SRS-SAFE-0001–0022 |
| §8 Security | SEC | 6 | SRS-SEC-0001–0006 |
| §9 Data Requirements | DATA | 12 | SRS-DATA-0001–0012 |
| §10 Interface Requirements | INT | 7 | SRS-INT-0001–0036 (selected) |
| §11 Hardware / Physical & Mechanical | COMP-HW | 8 | SRS-HW-0001–0008 |
| §12 Environmental & Durability | ENV | 18 | SRS-ENV-0001–0018 |
| §13 Reliability & Availability | RELI | 4 | SRS-RELI-0001–0004 |
| §14 Usability | UX | 4 | SRS-UX-0001–0004 |
| §15 Operational | OPER | 12 | SRS-OPER-0012–0023 |
| §16 Maintainability | MAINT | 3 | SRS-MAINT-0001–0003 |
| §17 Standards Conformance | COMP | 24 | SRS-COMP-0005–0028 |
| §18 Regulatory Certification | REG | 46 | SRS-REG-0001–0046 |

**Total: 369 rows across 18 sections (397 requirements including cross-referenced duplicates in multiple sections).**

---

## Appendix B — Regulatory Map Summary

The Regulatory Map (31 entries, RM-0001 through RM-0031) identifies all applicable standards and regulations for the LUUCIPet Wellness Monitor across five target markets (US, EU, UK, CA, AU/NZ). Confidence distribution: CONFIRMED 18, INDICATIVE 9, UNCERTAIN 2 (plus 1 resolved miscitation at RM-0030).

### Key Regulatory Instruments

**Radio / Wireless (RM-0001–RM-0009, RM-0029):**
- FCC 47 CFR Part 15 Subpart C (US) — CONFIRMED
- RED 2014/53/EU — CONFIRMED
- UK Radio Equipment Regulations 2017 — CONFIRMED
- ISED RSS-247 (CA) — INDICATIVE
- AS/NZS 4268:2017 (AU/NZ) — INDICATIVE
- Bluetooth SIG Qualification — CONFIRMED
- GNSS passive-receiver exemption — INDICATIVE (escalated)

**Battery / Electrical Safety (RM-0010–RM-0014):**
- UN 38.3 — CONFIRMED
- IEC 62133-2:2017+AMD1:2021 — CONFIRMED (version-corrected)
- UL 1642/UL 2054 (US) — CONFIRMED
- EN 62368-1/UL 62368-1 — CONFIRMED
- EU Battery Regulation (EU) 2023/1542 — CONFIRMED (Art 11 removability INDICATIVE)

**Privacy / Cybersecurity (RM-0015–RM-0023):**
- GDPR (EU) 2016/679 — CONFIRMED
- UK GDPR + DPA 2018 — CONFIRMED
- CCPA/CPRA (US-CA) — INDICATIVE
- PIPEDA (CA) — CONFIRMED
- ETSI EN 303 645:2025 — CONFIRMED (version-corrected from PRD)
- EU Cyber Resilience Act (EU) 2024/2847 — CONFIRMED
- UK PSTI Act 2022 — CONFIRMED

**Materials / Environmental / Product Safety (RM-0024–RM-0031):**
- EU GPSR (EU) 2023/988 — CONFIRMED
- UK GPSR 2005 / US CPSA — CONFIRMED
- REACH / RoHS / CA Prop 65 — CONFIRMED
- WEEE / EU PPWR — CONFIRMED
- IEC 60529 / IEC 60068-2 series — CONFIRMED (clauses INDICATIVE)
- ASTM F2056 (pet collar safety) — CONFIRMED at standard level

---

## Appendix C — Assumption Register

| ID | Statement | Basis | Risk | Status |
|:---|:----------|:------|:-----|:-------|
| A-0001 | Drop test surface defined as rigid surface | PRD §12.5 states 1.5 m drop without defining surface; engineered default | LOW | CONFIRMED |
| A-0002 | Zone-2 blunt-edge test methodology per GPSR Art 6 design-characteristics assessment | PRD requires blunt fracture edge; GPSR supports test methodology | LOW | INDICATIVE |
| A-0003 | CCF thermal-cycling profile per IEC 60068-2-14 Test Na | PRD states range without cycle/dwell/ramp | LOW | CONFIRMED |
| A-0004 | Mechanical shock severity class per IEC 60068-2-27 | PRD recommends shock test without severity class | LOW | INDICATIVE |
| A-0005 | Data sensitivity classification: pet behavioral and location data = personal data under GDPR | Product Context Profile determination | LOW | CONFIRMED |
| A-0006 | Battery cell capacities: Mini ≥120 mAh, Max ≥400 mAh (PRD §10.4 minimums) | PRD §15.3 figures are illustrative; §10.4 minimums are governing | MEDIUM | CONFIRMED |
| A-0007 | CCF chew-resistance compressive bite-load threshold = 250 N | PRD requires "chew-resistant" without numeric bound | MEDIUM | INDICATIVE |
| A-0008 | Base Station LED dimming threshold per night-time ambient light sensor reading | PRD requires dimming without numeric threshold | LOW | INDICATIVE |
| A-0009 | Home Wi-Fi reliability bound: ≥−70 dBm RSSI at 2.4 GHz, ≥256 kbps sustained uplink | PRD assumes "reliable" Wi-Fi without numeric bound | MEDIUM | CONFIRMED |
| A-0010 | Device-absent CCF socket entrapment-probe criterion = 12 mm | PRD requires entrapment-avoidance without probe size | MEDIUM | INDICATIVE |
| A-0011 | Battery-ingestion warning basis: Li-Po pouch cell, not coin/button cell | Reese's Law / 16 CFR 1263 / UL 4200A apply only to button/coin cells | LOW | CONFIRMED |
| A-0012 | CCF assembled-mass constant = 26 g (device+CCF-L) for Zone-2 force-window derivation | DVT-gated | MEDIUM | CONFIRMED |
| A-0013 | EU Battery Regulation Art 11 removability exemption for sealed IP67 non-swappable-battery device | INDICATIVE pending EU counsel | HIGH | INDICATIVE |
| A-0014 | CCF-S feline breakaway force basis (~25–45 N per ASTM F2056) | Mandatory DVT re-validation gate against feline airway-safety data | HIGH | INDICATIVE |
| A-0015 | Device/base transport of telemetry and safety events to cloud is in-scope; cloud-side storage/analytics and app display are external | Scope Model boundary | LOW | CONFIRMED |
| A-0016 | In-scope GNSS power gating relies solely on device-local home/away state machine | Cloud-side state machine is external-party owned | LOW | CONFIRMED |
| A-0017 | CCF Zone 2 Fuse Tab breakaway = design-level strangulation-prevention mitigation per GPSR Art 6(1)(a) w/ Art 5 | INDICATIVE-pending-DVT; feline SKU efficacy unproven | HIGH | INDICATIVE |
| A-0018 | Breakaway detection bounds: detect+NV-commit ≤5 s, false-positive ≤0.1%/day, detection ≥99% | Standard-derived defaults filling PRD numeric gap | LOW | CONFIRMED |
| A-0020 | CCF-M/L canine breakaway-force ceilings engineering-derived; no identifiable external standard basis | RM-0030 confirmed no canine breakaway-force standard exists | MEDIUM | CONFIRMED |
| A-0023 | Charging socket self-drainage criterion: 5 mL fill, ≤15 s to ≤0.2 mL residual, 0–45° orientation | Engineered by analogy to A-0007; resolves method/criterion incoherence | MEDIUM | CONFIRMED |

---

## Appendix D — Glossary

| Term | Definition |
|:-----|:-----------|
| **Base Station** | The indoor device that provides BLE relay, Wi-Fi cloud uplink, and collar charging (Charging tier only). Two tiers: Charging (with cradle, 3 LEDs) and Relay (no cradle, 2 LEDs). |
| **BLE** | Bluetooth Low Energy — the short-range wireless protocol used for collar-to-base-station communication. |
| **CCF** | Collar Connection Fixture — the compound accessory that mechanically connects the collar-mounted device to a third-party pet collar, comprising Zone 1, Zone 2, and a Twist-Lock device interface. |
| **Classification Engine** | The on-device software component that processes accelerometer data to identify and label pet behaviors using Tier-1 and Tier-2 classifiers. |
| **Cloud DM Layer** | Cloud Device-Management Layer — the LUUCI IoT Cloud component that interfaces with Base Stations for data relay, OTA firmware distribution, and device management. |
| **Damp Heat** | A combined high-temperature, high-humidity environmental test used to assess material and seal degradation under sustained humid conditions. |
| **FCC ID** | FCC Identifier — the unique grantee/product code assigned upon equipment certification, required to be displayed under FCC labeling rules. |
| **Fuse Tab** | See Zone 2. |
| **GNSS** | Global Navigation Satellite System — the satellite positioning receiver on the Max variant; receive-only, supporting GPS and GLONASS. |
| **Home/Away State** | The device-local determination of whether the collar is within (HOME) or outside (AWAY) the household geo-fence zone, used to gate GNSS power behavior on the Max variant. |
| **In-Support Firmware Version** | A firmware version that has not yet reached end-of-support under the 2-year supported-service-lifetime commitment. |
| **Insight Mode** | An owner-activated mode that increases the behavioral classification sampling rate for a user-defined duration, providing higher-resolution data. |
| **Longevity Mode** | A power-saving mode that reduces classification sampling rate to extend battery life beyond Wellness Mode targets. |
| **NRTL** | Nationally Recognized Testing Laboratory — an OSHA-accredited independent laboratory authorized to test and certify products against US safety standards. |
| **Operational Availability** | The proportion of time a system or device is capable of performing its specified function, expressed as a percentage of total elapsed time within a defined observation window. |
| **OTA** | Over-the-Air — firmware update delivery via wireless communication (BLE relay for collars, Wi-Fi for Base Stations). |
| **Pogo-Pin** | Spring-loaded contact pins used for the magnetic charging interface between the collar device and Base Station charging cradle. |
| **RTM** | Requirements Traceability Matrix — the structured mapping of each requirement to its source(s), priority, verification method, and cross-references. |
| **SDoC** | Supplier's Declaration of Conformity — a self-issued declaration by the responsible party attesting regulatory compliance without third-party certification. |
| **Service Lifetime** | The expected duration, from first use to end of intended service (minimum 2 years per the Product Context Profile), over which a product must continue to meet its specified performance and safety criteria. |
| **Supported Service Lifetime** | The minimum 2-year period for which the manufacturer commits to maintaining OTA update capability, SBOM currency, and vulnerability-disclosure process availability. |
| **TCB** | Telecommunication Certification Body — an FCC-recognized independent body authorized to grant equipment certification for radio devices. |
| **Thermal Cycling** | Repeated exposure of a test article to alternating high- and low-temperature extremes to reveal degradation caused by thermally induced material stress. |
| **Tier-1 Classifier** | Factory-loaded behavioral classifier (Rest/Sleep, Active/Awake) — ships at launch. |
| **Tier-2 Classifier** | Post-launch behavioral classifier delivered exclusively via OTA (Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting, Head-Shaking). |
| **Twist-Lock** | The 3-lug bayonet mechanical interface connecting the collar-mounted device to the CCF body; owner-operated for charging removal only, and explicitly not a breakaway safety element. |
| **Uptime** | The proportion of a defined observation window during which a system remains powered, responsive, and capable of performing its specified function. |
| **UV Aging** | Accelerated exposure of a material to ultraviolet radiation to evaluate long-term degradation from outdoor solar exposure within a compressed test duration. |
| **Wellness Mode** | The default operating mode performing continuous behavioral classification at the nominal sampling rate. |
| **Zone 1** | The non-breakaway structural clamp element of the CCF that attaches to the third-party collar and must remain intact through a Zone 2 breakaway event, retaining ≥50 N. |
| **Zone 2** | The scored-polymer, single-use fuse element of the CCF designed to fracture within a SKU-specific force window, releasing the CCF body and device from the collar to prevent strangulation. |

---

## Appendix E — Conflict Log Summary

The Conflict and Consistency Resolver processed all intra-section and cross-section conflicts across 18 sections using the three-tier resolution model. Final status: **zero unresolved conflicts**.

**Key resolved conflicts:**
- Multiple single-predicate splits for compound requirements (e.g., SRS-FUNC-0001 split into detection, forwarding, and transport blocks).
- Verification Method corrections (Test→Inspection for binary post-fracture inspections).
- CCF-M/L canine breakaway-force ceiling citation resolved — engineering-derived values carried by Assumptions A-0020, not a non-existent standard.
- ASTM F2727 miscitation corrected to ASTM F2056 (pet collar safety specification).
- COMP/REG section split applied — §17 covers standards conformance, §18 covers market certification pathways.
- Self-drainage criterion gap resolved via Assumption A-0023 (5 mL / 15 s / ≤0.2 mL residual).
- External-party scope model applied to Mobile App and IoT Cloud backend requirements.
- EU Battery Regulation Art 11 removability conflict flagged as INDICATIVE, pending EU counsel determination.

---

*End of Document — SRS-LUUCIPET-FINAL, Issue 1.0, July 2026*
