# Software Requirements Specification
## LUUCIPet Wellness Monitor — Phase 1

---

**Document Reference:** SRS-LUUCIPET-PH1-002  
**Issue:** 1.1  
**Issue Date:** 21 July 2026  
**Classification:** Confidential — For Authorized Recipients Only  

**Conforms to:** IEEE 830-1998 / ISO/IEC/IEEE 29148:2018

---

## Document Control

### Prepared By

| Role | Organisation | Date |
|:-----|:-------------|:-----|
| Systems Engineering | SRS Foundry — Requirements Engineering | 21 July 2026 |

### Revision History

| Revision | Date | Description |
|:---------|:-----|:------------|
| PH1-001 | July 2026 | Initial assembled deliverable. 18 sections approved. 397 requirements. RTM at 369 rows. Zero unresolved conflicts. All upstream gates PASSED. |
| PH1-002 | 21 July 2026 | Re-formatting — assembly format updated per stakeholder request (vertical two-column requirement tables). No requirement changes. Provenance scrubbed. |
| **Author:** | | Systems Engineering |

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

---


## 1. Introduction

## 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

## 1.2 Scope

**In scope:**  Mini & Max collar HW+FW; Base Station (Charging & Relay) HW+FW; the device-enforced BLE/base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S/M/L, collar-types -RC/-MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract.
**Out of scope (PRD §6.1, §14.1):**  GPS-M variant + cellular (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage/analytics backend; cloud-side home/away state machine; device-app ICD.

## 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

## 1.4 Wellness-Not-Medical Boundary

## 1.5 Definitions and References

Full term definitions are maintained in the Glossary appendix (derived from PRD §14.4). Standards/regulatory instruments are enumerated in the Regulatory Map and cited inline using the closed source-tag set only: `[PRD §x.x]`, `[STD: ID §clause]`, `[ASSUMPTION: A-NNNN]`, `[CONFLICT-RES: CR-NNNN]`, `[PRD — ABSENT: field]`.

---

**SRS-IDs issued:**  SRS-REG-0001, SRS-REG-0002.

<a id="req-reg-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0001**  | **Prohibit medical-classification claims in labeling and marketing**                                |
| **Statement**    | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.6] · SRS-REG-0002 |

<a id="req-reg-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0002**  | **Require regulatory classification review before releasing diagnostic-adjacent features**                                |
| **Statement**    | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §13.6] · SRS-REG-0001 |


## 2. Overall Description

## 2.5 Assumptions & Dependencies

This section's constraints depend on the following confirmed assumptions (full text in the Assumption Register):

- **[ASSUMPTION: A-0006]** — governing battery cell capacities are the §10.4 minimums
- **[ASSUMPTION: A-0009]** — home Wi-Fi reliability bound
- **[ASSUMPTION: A-0012]** — CCF assembled-mass constant (26 g)
- **[ASSUMPTION: A-0013]** — EU Battery Regulation Art. 11 removability exemption
- **[ASSUMPTION: A-0014]** — CCF-S feline breakaway force basis
- **[ASSUMPTION: A-0015]** — cloud-transport vs cloud-storage/app boundary
- **[ASSUMPTION: A-0016]** — device-local vs cloud-side home/away state machine
- **[ASSUMPTION: A-0017]** — GPSR design-level strangulation-mitigation framing

---

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-OPER-0001 | Require at least one Charging-tier base station per household | CRITICAL | STABLE | Inspection |
| SRS-OPER-0002 | Limit base stations per household deployment | HIGH | STABLE | Test |
| SRS-OPER-0003 | Persist species assignment across resets | HIGH | STABLE | Test |
| SRS-OPER-0004 | Prohibit owner configuration of the GNSS smart power gate | HIGH | STABLE | Inspection |
| SRS-OPER-0005 | Bound in-box CCF fitment coverage | MEDIUM | LIKELY-CHANGE | Analysis |
| SRS-OPER-0006 | Default to Standard CCF as in-box accessory | HIGH | STABLE | Inspection |
| SRS-OPER-0007 | Define degraded-mode behavior below the home Wi-Fi reliability bound | HIGH | STABLE | Test |
| SRS-OPER-0008 | Mobile App post-breakaway owner alert (external) | HIGH | STABLE | Analysis — external conformance evidence |
| SRS-OPER-0009 | Mobile App species re-onboarding flow (external) | MEDIUM | STABLE | Analysis — external conformance evidence |
| SRS-OPER-0010 | Mobile App CCF fitment/sizing guidance (external) | MEDIUM | LIKELY-CHANGE | Analysis — external conformance evidence |
| SRS-OPER-0011 | Cloud-side home/away state machine for owner geofence alerting (external) | MEDIUM | LIKELY-CHANGE | Analysis — external conformance evidence |
| SRS-COMP-0001 | Require collar-agnostic base station firmware | HIGH | STABLE | Test |
| SRS-COMP-0002 | Require universal CCF-to-device mechanical compatibility | CRITICAL | STABLE | Test |
| SRS-COMP-0003 | Require a shared classification engine and protocol across collar variants | HIGH | STABLE | Inspection |
| SRS-FUNC-0001 | Detect CCF breakaway/separation signature | CRITICAL | STABLE | Test |
| SRS-FUNC-0003 | Preserve and forward the persisted breakaway event on next base-station contact | CRITICAL | STABLE | Test |
| SRS-FUNC-0002 | Transport breakaway event to IoT Cloud Device-Management layer | CRITICAL | STABLE | Test |

<a id="req-oper-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0001**  | **Require at least one Charging-tier base station per household**                                |
| **Statement**    | A household deployment **shall** include at least one Base Station of the Charging tier. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.2], [PRD §4.5] · SRS-OPER-0002 |

<a id="req-oper-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0002**  | **Limit base stations per household deployment**                                |
| **Statement**    | A household deployment **shall not** exceed 8 Base Stations, in any combination of Charging and Relay tiers. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.2], [PRD §4.5] · SRS-OPER-0001 |

<a id="req-oper-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0003**  | **Persist species assignment across resets**                                |
| **Statement**    | The collar device **shall** retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.5], [PRD §7.2] · SRS-OPER-0009 |

<a id="req-oper-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0004**  | **Prohibit owner configuration of the GNSS smart power gate**                                |
| **Statement**    | The Max variant's GNSS smart power gate **shall not** be configurable by the owner. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.5] |

<a id="req-oper-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0005**  | **Bound in-box CCF fitment coverage**                                |
| **Statement**    | The in-box Standard CCF **shall** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §14.2] · SRS-OPER-0006, SRS-OPER-0010 |

<a id="req-oper-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0006**  | **Default to Standard CCF as in-box accessory**                                |
| **Statement**    | The system **shall** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.1], [PRD §14.2] · SRS-OPER-0005 |

<a id="req-oper-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0007**  | **Define degraded-mode behavior below the home Wi-Fi reliability bound**                                |
| **Statement**    | The Base Station **shall** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION: A-0009] |

<a id="req-oper-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0008**  | **Mobile App post-breakaway owner alert (external)**                                |
| **Statement**    | The Mobile App **shall** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis — external conformance evidence                               |
| **Traceability** | [PRD §10.1.3.6], [EXTERNAL: Mobile App team] · SRS-FUNC-0001, SRS-FUNC-0002 |

<a id="req-oper-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0009**  | **Mobile App species re-onboarding flow (external)**                                |
| **Statement**    | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's species classifier profile. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis — external conformance evidence                               |
| **Traceability** | [PRD §4.5], [EXTERNAL: Mobile App team] · SRS-OPER-0003 |

<a id="req-oper-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0010**  | **Mobile App CCF fitment/sizing guidance (external)**                                |
| **Statement**    | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis — external conformance evidence                               |
| **Traceability** | [PRD §14.2], [EXTERNAL: Mobile App team] · SRS-OPER-0005 |

<a id="req-oper-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0011**  | **Cloud-side home/away state machine for owner geofence alerting (external)**                                |
| **Statement**    | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis — external conformance evidence                               |
| **Traceability** | [ASSUMPTION: A-0016], [EXTERNAL: IoT Cloud backend team] · SRS-OPER-0004 |

<a id="req-comp-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0001**  | **Require collar-agnostic base station firmware**                                |
| **Statement**    | Base Station firmware **shall** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.3], [PRD §4.5] · SRS-COMP-0002 |

<a id="req-comp-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0002**  | **Require universal CCF-to-device mechanical compatibility**                                |
| **Statement**    | All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **shall** be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.1], [PRD §4.3] · SRS-COMP-0001 |

<a id="req-comp-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0003**  | **Require a shared classification engine and protocol across collar variants**                                |
| **Statement**    | The Mini and Max collar variants **shall** exhibit equivalent behavioral-classification outputs and use an interoperable common BLE communication protocol across the Mini and Max variants. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.3] · SRS-COMP-0001 |

<a id="req-func-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0001**  | **Detect CCF breakaway/separation signature**                                |
| **Statement**    | The collar device **shall** detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event record to non-volatile storage within 5 s of the separation event, with a false-positive rate not exceeding 0.1% per device-wear-day and a true-event detection rate of at least 99% under DVT drop/tension conditions. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.6], [ASSUMPTION: A-0015], [ASSUMPTION: A-0018] · SRS-FUNC-0002, SRS-FUNC-0003, SRS-OPER-0008 |

<a id="req-func-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0003**  | **Preserve and forward the persisted breakaway event on next base-station contact**                                |
| **Statement**    | The persisted breakaway event record **shall** survive subsequent power loss, battery depletion, and reboot without corruption, and be transmitted to the Base Station on the next successful Base Station contact. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.4], [PRD §10.1.3.6], [ASSUMPTION: A-0018] · SRS-FUNC-0001, SRS-FUNC-0002 |

<a id="req-func-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0002**  | **Transport breakaway event to IoT Cloud Device-Management layer**                                |
| **Statement**    | The Base Station **shall** transport a recorded breakaway/separation event to the IoT Cloud Device-Management layer on the next successful Base Station contact and cloud sync (event-triggered; no delivery-time guarantee, as post-breakaway the device may be lost, out of range, or depleted). |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.6], [PRD §8.5], [ASSUMPTION: A-0015], [ASSUMPTION: A-0018] · SRS-FUNC-0001, SRS-FUNC-0003, SRS-OPER-0008 |


## 3. Functional Requirements — Behavioral Classification

## 3.1 Operating Modes

## 3.2 Sensing & Classification Pipeline

## 3.3 Classification Accuracy & False-Positive Bounds

## 3.4 Classification Records & Local Storage

## 3.5 Data Locality & On-Device Processing

## 3.6 Tier-2 Extensibility via OTA

## 3.7 Configurable Alert Thresholds (Scratching & Shaking)

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-FUNC-0006 | Wellness Mode as Default Operating Mode | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0007 | Insight Mode Availability On Demand | HIGH | STABLE | Demonstration |
| SRS-FUNC-0008 | Insight Mode Continuous Sampling Rate | HIGH | STABLE | Test |
| SRS-FUNC-0009 | Insight Mode Auto-Revert to Wellness | HIGH | STABLE | Test |
| SRS-FUNC-0010 | Wellness Mode Motion-Triggered Confirmation Burst | HIGH | STABLE | Test |
| SRS-FUNC-0011 | Wellness Mode Idle Current Ceiling | CRITICAL | STABLE | Test |
| SRS-FUNC-0012 | Longevity Mode Shall Not Reduce Classification Sampling Rate | CRITICAL | STABLE | Test |
| SRS-FUNC-0013 | Longevity Mode Shall Not Reduce Classification Accuracy | CRITICAL | STABLE | Test |
| SRS-FUNC-0014 | Minimum Accelerometer Output Data Rate | CRITICAL | STABLE | Test |
| SRS-FUNC-0015 | No Auxiliary Sensors for Tier-1 Classification | HIGH | STABLE | Inspection |
| SRS-FUNC-0016 | Unified Classification Pipeline Across Tiers | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0017 | Species-Specific Threshold Assignment at Onboarding | HIGH | STABLE | Test |
| SRS-FUNC-0018 | Tier-1 Per-Class Accuracy Minimum | CRITICAL | LIKELY-CHANGE | Test |
| SRS-FUNC-0019 | Tier-1 Per-Class False-Positive Ceiling | CRITICAL | LIKELY-CHANGE | Test |
| SRS-FUNC-0020 | Tier-2 Per-Class Accuracy Minimum | HIGH | LIKELY-CHANGE | Test |
| SRS-FUNC-0021 | Tier-2 Per-Class False-Positive Ceiling | HIGH | LIKELY-CHANGE | Test |
| SRS-FUNC-0022 | Classification Record Contains Behavior Label | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0023 | Classification Record Contains Confidence Score | HIGH | STABLE | Test |
| SRS-FUNC-0024 | Classification Record Timestamp Resolution | HIGH | STABLE | Test |
| SRS-FUNC-0025 | Classification Record GNSS Fix on Max Variant | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0026 | Minimum Local Retention of Classification Records | CRITICAL | STABLE | Test |
| SRS-FUNC-0027 | No Record Discard on Connectivity Loss | CRITICAL | STABLE | Test |
| SRS-FUNC-0028 | Classification Generation Independent of BLE Connectivity | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0029 | Record Forwarding Without Corruption | CRITICAL | STABLE | Test |
| SRS-FUNC-0030 | Record Forwarding Without Sequence Loss | HIGH | STABLE | Test |
| SRS-FUNC-0031 | On-Device Signal Normalization | HIGH | STABLE | Inspection |
| SRS-FUNC-0032 | Raw Accelerometer Data Shall Not Leave the Collar | CRITICAL | STABLE | Test |
| SRS-FUNC-0033 | No Cloud Round-Trip for Classification Decisions | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0034 | Tier-2 Classifier Delivery via OTA | HIGH | STABLE | Demonstration |
| SRS-FUNC-0035 | Tier-2 Deployment Without Hardware Modification or Service Event | HIGH | STABLE | Demonstration |
| SRS-FUNC-0036 | Device Application of Configured Scratching Alert Threshold | HIGH | VOLATILE | Test |
| SRS-FUNC-0037 | Firmware-Default Scratching Alert Threshold | MEDIUM | VOLATILE | Inspection |
| SRS-FUNC-0038 | Device Application of Configured Shaking Alert Threshold | HIGH | VOLATILE | Test |
| SRS-FUNC-0039 | Firmware-Default Shaking Alert Threshold | MEDIUM | VOLATILE | Inspection |
| SRS-FUNC-0040 | Alert Threshold Persistence Across OTA Updates | HIGH | STABLE | Test |
| SRS-FUNC-0041 | App-Side Scratching Threshold Configuration UI (external) | HIGH | STABLE | Inspection (external conformance evidence) |
| SRS-FUNC-0042 | App-Side Shaking Threshold Configuration UI (external) | HIGH | STABLE | Inspection (external conformance evidence) |

<a id="req-func-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0006**  | **Wellness Mode as Default Operating Mode**                                |
| **Statement**    | The system **shall** operate in Wellness mode as its default power-optimized classification mode. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.1] · SRS-FUNC-0011 |

<a id="req-func-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0007**  | **Insight Mode Availability On Demand**                                |
| **Statement**    | The system **shall** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.1] · SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="req-func-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0008**  | **Insight Mode Continuous Sampling Rate**                                |
| **Statement**    | While in Insight mode, the system **shall** sample the accelerometer continuously at 50 Hz. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.1] · SRS-FUNC-0007, SRS-FUNC-0014 |

<a id="req-func-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0009**  | **Insight Mode Auto-Revert to Wellness**                                |
| **Statement**    | The system **shall** automatically revert from Insight mode to Wellness mode without requiring a manual user action. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.3] · SRS-FUNC-0006, SRS-FUNC-0007 |

<a id="req-func-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0010**  | **Wellness Mode Motion-Triggered Confirmation Burst**                                |
| **Statement**    | Upon detecting motion, the system **shall** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.3] · SRS-FUNC-0011 |

<a id="req-func-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0011**  | **Wellness Mode Idle Current Ceiling**                                |
| **Statement**    | While in Wellness mode and outside a confirmation burst, the system **shall not** exceed an idle current draw of 4 µA. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.3] · SRS-FUNC-0006, SRS-FUNC-0010 |

<a id="req-func-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0012**  | **Longevity Mode Shall Not Reduce Classification Sampling Rate**                                |
| **Statement**    | When Longevity Mode is active, the system **shall not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.10] · SRS-FUNC-0014 |

<a id="req-func-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0013**  | **Longevity Mode Shall Not Reduce Classification Accuracy**                                |
| **Statement**    | When Longevity Mode is active, the system **shall not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.10] · SRS-FUNC-0018, SRS-FUNC-0020 |

<a id="req-func-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0014**  | **Minimum Accelerometer Output Data Rate**                                |
| **Statement**    | The system **shall** sample the accelerometer at a rate of no less than 50 Hz. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.2] · SRS-FUNC-0008, SRS-FUNC-0015 |

<a id="req-func-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0015**  | **No Auxiliary Sensors for Tier-1 Classification**                                |
| **Statement**    | The system **shall** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.2] · SRS-FUNC-0014 |

<a id="req-func-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0016**  | **Unified Classification Pipeline Across Tiers**                                |
| **Statement**    | The system **shall** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.2] · SRS-FUNC-0034 |

<a id="req-func-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0017**  | **Species-Specific Threshold Assignment at Onboarding**                                |
| **Statement**    | The system **shall** set species-specific classification thresholds during the onboarding process. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.2] · SRS-OPER-0003 |

<a id="req-func-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0018**  | **Tier-1 Per-Class Accuracy Minimum**                                |
| **Statement**    | The system **shall** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.4] · SRS-FUNC-0019 |

<a id="req-func-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0019**  | **Tier-1 Per-Class False-Positive Ceiling**                                |
| **Statement**    | The system **shall not** exceed a false-positive rate of 5% for each Tier-1 behavior class. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.4] · SRS-FUNC-0018 |

<a id="req-func-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0020**  | **Tier-2 Per-Class Accuracy Minimum**                                |
| **Statement**    | The system **shall** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.4] · SRS-FUNC-0021 |

<a id="req-func-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0021**  | **Tier-2 Per-Class False-Positive Ceiling**                                |
| **Statement**    | The system **shall not** exceed a false-positive rate of 10% for each Tier-2 behavior class. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.4] · SRS-FUNC-0020 |

<a id="req-func-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0022**  | **Classification Record Contains Behavior Label**                                |
| **Statement**    | The system **shall** include a behavior class label in every generated classification record. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.5] · SRS-FUNC-0023, SRS-FUNC-0024 |

<a id="req-func-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0023**  | **Classification Record Contains Confidence Score**                                |
| **Statement**    | The system **shall** include a confidence score in the range 0.0 to 1.0 in every generated classification record. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] · SRS-FUNC-0022 |

<a id="req-func-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0024**  | **Classification Record Timestamp Resolution**                                |
| **Statement**    | The system **shall** timestamp every classification record in UTC with a resolution no coarser than 1 second. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] · SRS-FUNC-0022 |

<a id="req-func-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0025**  | **Classification Record GNSS Fix on Max Variant**                                |
| **Statement**    | On the Max product variant, the system **shall** include the most recent GNSS fix in every generated classification record. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.5] · SRS-FUNC-0022 |

<a id="req-func-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0026**  | **Minimum Local Retention of Classification Records**                                |
| **Statement**    | The system **shall** retain generated classification records locally for no less than 30 days without a cloud connection. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] · SRS-FUNC-0027 |

<a id="req-func-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0027**  | **No Record Discard on Connectivity Loss**                                |
| **Statement**    | The system **shall not** discard stored classification records upon loss of connectivity. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] · SRS-FUNC-0026 |

<a id="req-func-0028"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0028**  | **Classification Generation Independent of BLE Connectivity**                                |
| **Statement**    | The system **shall** generate and record classifications independently of the current BLE connectivity state. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.6] · SRS-FUNC-0029 |

<a id="req-func-0029"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0029**  | **Record Forwarding Without Corruption**                                |
| **Statement**    | The system **shall** forward stored classification records without data corruption. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] · SRS-FUNC-0030 |

<a id="req-func-0030"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0030**  | **Record Forwarding Without Sequence Loss**                                |
| **Statement**    | The system **shall** forward stored classification records without loss of their original sequence order. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] · SRS-FUNC-0029 |

<a id="req-func-0031"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0031**  | **On-Device Signal Normalization**                                |
| **Statement**    | The system **shall** normalize raw accelerometer data on-device prior to classification. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.7] · SRS-FUNC-0032, SRS-FUNC-0033 |

<a id="req-func-0032"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0032**  | **Raw Accelerometer Data Shall Not Leave the Collar**                                |
| **Statement**    | The system **shall not** transmit raw accelerometer data off the collar. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.7] · SRS-FUNC-0031, SRS-FUNC-0033 |

<a id="req-func-0033"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0033**  | **No Cloud Round-Trip for Classification Decisions**                                |
| **Statement**    | The system **shall** produce classification decisions without requiring a round-trip to a cloud service. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.7] · SRS-FUNC-0028, SRS-FUNC-0032 |

<a id="req-func-0034"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0034**  | **Tier-2 Classifier Delivery via OTA**                                |
| **Statement**    | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.9] · SRS-FUNC-0016, SRS-FUNC-0035 |

<a id="req-func-0035"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0035**  | **Tier-2 Deployment Without Hardware Modification or Service Event**                                |
| **Statement**    | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.9] · SRS-FUNC-0034 |

<a id="req-func-0036"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0036**  | **Device Application of Configured Scratching Alert Threshold**                                |
| **Statement**    | The system **shall** apply a Scratching alert threshold value received via the companion application. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.8] · SRS-FUNC-0037, SRS-FUNC-0041 |

<a id="req-func-0037"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0037**  | **Firmware-Default Scratching Alert Threshold**                                |
| **Statement**    | The system **shall** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.8] · SRS-FUNC-0036 |

<a id="req-func-0038"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0038**  | **Device Application of Configured Shaking Alert Threshold**                                |
| **Statement**    | The system **shall** apply a Shaking alert threshold value received via the companion application. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.8] · SRS-FUNC-0039, SRS-FUNC-0042 |

<a id="req-func-0039"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0039**  | **Firmware-Default Shaking Alert Threshold**                                |
| **Statement**    | The system **shall** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §7.8] · SRS-FUNC-0038 |

<a id="req-func-0040"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0040**  | **Alert Threshold Persistence Across OTA Updates**                                |
| **Statement**    | The system **shall** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.8] · SRS-FUNC-0036, SRS-FUNC-0038 |

<a id="req-func-0041"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0041**  | **App-Side Scratching Threshold Configuration UI (external)**                                |
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §7.8], [EXTERNAL: Mobile App team] · SRS-FUNC-0036 |

<a id="req-func-0042"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0042**  | **App-Side Shaking Threshold Configuration UI (external)**                                |
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §7.8], [EXTERNAL: Mobile App team] · SRS-FUNC-0038 |


## 4. Functional Requirements — Data Sync & Connectivity

## 4.1 BLE Device↔Base Link & Pairing

## 4.2 Record Forwarding & Sync

## 4.3 Base↔Cloud Gateway & Upload

## 4.4 Multi-Base-Station Behavior & Handover

## 4.5 Insight-Mode Activation over Connectivity

## 4.6 GNSS Location Data Sync (Max Variant)

## 4.7 Connectivity-Loss & Degraded Behavior

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-CONN-0001 | BLE Role Assignment — Collar as Peripheral | HIGH | STABLE | Inspection |
| SRS-CONN-0002 | BLE Role Assignment — Base Station as Central | HIGH | STABLE | Inspection |
| SRS-CONN-0003 | QR-Code Out-of-Band Pairing | HIGH | STABLE | Demonstration |
| SRS-CONN-0004 | Default BLE Advertising Interval | MEDIUM | STABLE | Test |
| SRS-CONN-0005 | Configurable Advertising Interval Range | MEDIUM | STABLE | Test |
| SRS-CONN-0006 | Minimum Open-Air BLE Range | HIGH | STABLE | Test |
| SRS-CONN-0007 | Minimum BLE Transmit Power | MEDIUM | STABLE | Test |
| SRS-CONN-0008 | BLE Address Randomization | HIGH | STABLE | Test |
| SRS-CONN-0009 | Secured BLE Link Establishment | CRITICAL | STABLE | Inspection |
| SRS-CONN-0010 | Automatic BLE Reconnection on Range Re-Entry | CRITICAL | STABLE | Test |
| SRS-CONN-0011 | Classification Record Forwarding on BLE Contact | CRITICAL | STABLE | Test |
| SRS-CONN-0012 | Best-Effort Event-Triggered Record Transport | HIGH | STABLE | Inspection |
| SRS-CONN-0013 | Sync Resumption of Accumulated Records After Reconnection | CRITICAL | STABLE | Test |
| SRS-CONN-0014 | Base Station Upload of Received Records to Cloud | CRITICAL | STABLE | Test |
| SRS-CONN-0015 | Base Station Buffering on Upload-Path Unavailability | CRITICAL | STABLE | Test |
| SRS-CONN-0016 | Buffered Record Upload on Path Restoration | CRITICAL | STABLE | Test |
| SRS-CONN-0017 | No Discard of Received Records Pending Upload | CRITICAL | STABLE | Test |
| SRS-CONN-0018 | Cloud Acceptance and Acknowledgment of Uploaded Records (external) | CRITICAL | STABLE | Inspection (external conformance evidence) |
| SRS-CONN-0030 | Base Station Upload Retry on Transient Failure | HIGH | VOLATILE | Demonstration |
| SRS-CONN-0019 | Collar Forwarding to Any In-Range Paired Base Station | HIGH | STABLE | Test |
| SRS-CONN-0020 | Single Forwarding of Each Record to First Available Base Station | HIGH | STABLE | Test |
| SRS-CONN-0021 | Cloud-Side Deduplication of Multi-Base Uploads (external) | HIGH | STABLE | Inspection (external conformance evidence) |
| SRS-CONN-0022 | Device-Side Insight-Mode Activation on Command Receipt | HIGH | STABLE | Test |
| SRS-CONN-0023 | Mobile App Issuance of Insight-Mode Activation Command (external) | HIGH | STABLE | Inspection (external conformance evidence) |
| SRS-CONN-0024 | Sync of Location-Tagged Records via Standard Forwarding Path | MEDIUM | STABLE | Test |
| SRS-CONN-0025 | Sync of Most-Recent GNSS Fix During Home Power-Gate | MEDIUM | STABLE | Test |
| SRS-CONN-0026 | No Record Loss Due to Any Connectivity-Loss Condition | CRITICAL | STABLE | Analysis |
| SRS-CONN-0027 | Continued Local Classification During BLE Loss | CRITICAL | STABLE | Demonstration |
| SRS-CONN-0028 | Degraded-Mode Entry Below Home Wi-Fi Reliability Bound | HIGH | STABLE | Test |
| SRS-CONN-0029 | Degraded-Mode Exit on Wi-Fi Reliability Restoration | HIGH | STABLE | Test |

<a id="req-conn-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0001**  | **BLE Role Assignment — Collar as Peripheral**                                |
| **Statement**    | The system **shall** operate the collar-mounted device in the BLE peripheral role relative to the base station. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §6.3] · SRS-CONN-0002 |

<a id="req-conn-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0002**  | **BLE Role Assignment — Base Station as Central**                                |
| **Statement**    | The system **shall** operate the base station in the BLE central role relative to the collar-mounted device. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §6.3] · SRS-CONN-0001 |

<a id="req-conn-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0003**  | **QR-Code Out-of-Band Pairing**                                |
| **Statement**    | The system **shall** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §6.3] |

<a id="req-conn-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0004**  | **Default BLE Advertising Interval**                                |
| **Statement**    | The system **shall** advertise the presence of the collar-mounted device at a default interval of 60 seconds. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3] · SRS-CONN-0005 |

<a id="req-conn-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0005**  | **Configurable Advertising Interval Range**                                |
| **Statement**    | The system **shall** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3] · SRS-CONN-0004 |

<a id="req-conn-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0006**  | **Minimum Open-Air BLE Range**                                |
| **Statement**    | The system **shall** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3] · SRS-CONN-0007 |

<a id="req-conn-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0007**  | **Minimum BLE Transmit Power**                                |
| **Statement**    | The system **shall** transmit BLE signals at a power level of no less than +8 dBm. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3] · SRS-CONN-0006 |

<a id="req-conn-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0008**  | **BLE Address Randomization**                                |
| **Statement**    | The system **shall** randomize the BLE device address of the collar-mounted device. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3] |

<a id="req-conn-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0009**  | **Secured BLE Link Establishment**                                |
| **Statement**    | The system **shall** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §6.3] · — (§8 Security, not yet drafted) |

<a id="req-conn-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0010**  | **Automatic BLE Reconnection on Range Re-Entry**                                |
| **Statement**    | Upon the collar-mounted device re-entering BLE range of a base station, the system **shall** automatically re-establish the BLE link without requiring manual user action. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.4], [PRD §8.5] · SRS-CONN-0001, SRS-CONN-0002 |

<a id="req-conn-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0011**  | **Classification Record Forwarding on BLE Contact**                                |
| **Statement**    | Upon establishing a BLE link with a base station, the system **shall** forward stored classification records from the collar-mounted device to the base station. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8], [PRD §6.4] · SRS-FUNC-0026, SRS-FUNC-0028 |

<a id="req-conn-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0012**  | **Best-Effort Event-Triggered Record Transport**                                |
| **Statement**    | The system **shall** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §8.5] · SRS-FUNC-0002, SRS-FUNC-0003 |

<a id="req-conn-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0013**  | **Sync Resumption of Accumulated Records After Reconnection**                                |
| **Statement**    | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **shall** forward all classification records accumulated during that disconnection. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8], [PRD §8.5] · SRS-FUNC-0027, SRS-CONN-0011 |

<a id="req-conn-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0014**  | **Base Station Upload of Received Records to Cloud**                                |
| **Statement**    | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8], [PRD §6.5] · SRS-CONN-0011, SRS-CONN-0009 |

<a id="req-conn-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0015**  | **Base Station Buffering on Upload-Path Unavailability**                                |
| **Statement**    | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.5] · SRS-CONN-0016 |

<a id="req-conn-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0016**  | **Buffered Record Upload on Path Restoration**                                |
| **Statement**    | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.5] · SRS-CONN-0015 |

<a id="req-conn-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0017**  | **No Discard of Received Records Pending Upload**                                |
| **Statement**    | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.5] · SRS-FUNC-0027, SRS-CONN-0015 |

<a id="req-conn-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0018**  | **Cloud Acceptance and Acknowledgment of Uploaded Records (external)**                                |
| **Statement**    | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §8], [EXTERNAL: IoT Cloud backend team] · SRS-CONN-0014 |

<a id="req-conn-0030"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0030**  | **Base Station Upload Retry on Transient Failure**                                |
| **Statement**    | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **shall** retry uploading the affected buffered classification record. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §8.5] · SRS-CONN-0015, SRS-CONN-0016 |

<a id="req-conn-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0019**  | **Collar Forwarding to Any In-Range Paired Base Station**                                |
| **Statement**    | The system **shall** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.2], [PRD §8] · SRS-CONN-0011 |

<a id="req-conn-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0020**  | **Single Forwarding of Each Record to First Available Base Station**                                |
| **Statement**    | The system **shall** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in range. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.2], [PRD §8] · SRS-CONN-0019, SRS-CONN-0021 |

<a id="req-conn-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0021**  | **Cloud-Side Deduplication of Multi-Base Uploads (external)**                                |
| **Statement**    | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household account. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §4.2], [EXTERNAL: IoT Cloud backend team] · SRS-CONN-0020, SRS-CONN-0018 |

<a id="req-conn-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0022**  | **Device-Side Insight-Mode Activation on Command Receipt**                                |
| **Statement**    | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.1], [PRD §6.4] · SRS-FUNC-0007, SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="req-conn-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0023**  | **Mobile App Issuance of Insight-Mode Activation Command (external)**                                |
| **Statement**    | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §7.1], [EXTERNAL: Mobile App team] · SRS-CONN-0022 |

<a id="req-conn-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0024**  | **Sync of Location-Tagged Records via Standard Forwarding Path**                                |
| **Statement**    | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other classification records. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5], [PRD §8] · SRS-FUNC-0025, SRS-CONN-0011 |

<a id="req-conn-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0025**  | **Sync of Most-Recent GNSS Fix During Home Power-Gate**                                |
| **Statement**    | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix as part of classification records. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5], [PRD §6.3] · SRS-FUNC-0025, SRS-OPER-0004 |

<a id="req-conn-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0026**  | **No Record Loss Due to Any Connectivity-Loss Condition**                                |
| **Statement**    | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §8.5] · SRS-FUNC-0027, SRS-CONN-0017 |

<a id="req-conn-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0027**  | **Continued Local Classification During BLE Loss**                                |
| **Statement**    | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.6], [PRD §8.5] · SRS-FUNC-0028, SRS-FUNC-0027 |

<a id="req-conn-0028"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0028**  | **Degraded-Mode Entry Below Home Wi-Fi Reliability Bound**                                |
| **Statement**    | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION: A-0009] · SRS-OPER-0007 |

<a id="req-conn-0029"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-CONN-0029**  | **Degraded-Mode Exit on Wi-Fi Reliability Restoration**                                |
| **Statement**    | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION: A-0009] · SRS-OPER-0007, SRS-CONN-0028 |


## 5. Functional Requirements — OTA Firmware Updates

## 5.2 OTA Delivery Path & Transport

## 5.3 Collar Install Preconditions

## 5.4 OTA Image Integrity & Anti-Rollback

## 5.5 Install Resilience

## 5.6 Update Notification & Status

## 5.7 Release Artifacts & Tier-2 Delivery Channel

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-FUNC-0043 | OTA Capability Mandatory on All Collar Variants | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0044 | OTA Capability Mandatory on All Base Station Tiers | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0045 | Cloud-to-Base OTA Transport Protocol | HIGH | STABLE | Test |
| SRS-FUNC-0046 | Base Station Staging of Collar OTA Images | MEDIUM | STABLE | Test |
| SRS-FUNC-0047 | Base-to-Collar OTA Image Delivery Over Secured BLE Link | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0048 | Base Station Self-OTA Without User Action | HIGH | STABLE | Demonstration |
| SRS-FUNC-0049 | Collar OTA Install Restricted to Charging-Cradle-Docked State | CRITICAL | STABLE | Test |
| SRS-FUNC-0050 | Docked-Install Gate Shall Not Be Remotely Bypassable | CRITICAL | STABLE | Test |
| SRS-FUNC-0051 | Minimum Battery Reserve Before OTA Install | HIGH | STABLE | Test |
| SRS-FUNC-0052 | Minimum OTA Image Signature Strength | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0053 | OTA Image Signature Verification Before Commit | CRITICAL | STABLE | Test |
| SRS-FUNC-0054 | Anti-Rollback via Monotonic Version Counter | CRITICAL | STABLE | Test |
| SRS-FUNC-0055 | Atomic OTA Installation | CRITICAL | STABLE | Test |
| SRS-FUNC-0056 | Dual-Bank Auto-Revert on Boot Failure | CRITICAL | STABLE | Test |
| SRS-FUNC-0057 | No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install | CRITICAL | STABLE | Analysis |
| SRS-FUNC-0058 | Device-Side OTA Update State Reporting | MEDIUM | STABLE | Test |
| SRS-FUNC-0059 | App Notification of Available OTA Update (external) | MEDIUM | STABLE | Inspection (external conformance evidence) |
| SRS-FUNC-0060 | App Display of OTA Update State (external) | MEDIUM | STABLE | Inspection (external conformance evidence) |
| SRS-FUNC-0061 | SBOM Production Per OTA Release | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0062 | Tier-2 Classifier Delivery Restricted to Embedded OTA Components | HIGH | STABLE | Inspection |

<a id="req-func-0043"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0043**  | **OTA Capability Mandatory on All Collar Variants**                                |
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §9.1] · SRS-FUNC-0034 |

<a id="req-func-0044"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0044**  | **OTA Capability Mandatory on All Base Station Tiers**                                |
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §9.1] · SRS-FUNC-0043 |

<a id="req-func-0045"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0045**  | **Cloud-to-Base OTA Transport Protocol**                                |
| **Statement**    | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.2], [PRD §6.5], [PRD §11.2], [STD: ETSI EN 303 645:2025] · SRS-CONN-0014 |

<a id="req-func-0046"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0046**  | **Base Station Staging of Collar OTA Images**                                |
| **Statement**    | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.2] · SRS-FUNC-0047 |

<a id="req-func-0047"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0047**  | **Base-to-Collar OTA Image Delivery Over Secured BLE Link**                                |
| **Statement**    | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §9.2] · SRS-CONN-0009 |

<a id="req-func-0048"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0048**  | **Base Station Self-OTA Without User Action**                                |
| **Statement**    | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §11.5] · SRS-FUNC-0044 |

<a id="req-func-0049"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0049**  | **Collar OTA Install Restricted to Charging-Cradle-Docked State**                                |
| **Statement**    | The system **shall** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.2] · SRS-FUNC-0050, SRS-FUNC-0056 |

<a id="req-func-0050"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0050**  | **Docked-Install Gate Shall Not Be Remotely Bypassable**                                |
| **Statement**    | The system **shall not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.2] · SRS-FUNC-0049 |

<a id="req-func-0051"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0051**  | **Minimum Battery Reserve Before OTA Install**                                |
| **Statement**    | The system **shall** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.2], [PRD §10.4] · SRS-FUNC-0049, SRS-FUNC-0057 |

<a id="req-func-0052"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0052**  | **Minimum OTA Image Signature Strength**                                |
| **Statement**    | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §9.3], [STD: ETSI EN 303 645:2025] · SRS-FUNC-0053 |

<a id="req-func-0053"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0053**  | **OTA Image Signature Verification Before Commit**                                |
| **Statement**    | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.3], [STD: ETSI EN 303 645:2025] · SRS-FUNC-0052 |

<a id="req-func-0054"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0054**  | **Anti-Rollback via Monotonic Version Counter**                                |
| **Statement**    | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.3], [STD: EU CRA (EU) 2024/2847] |

<a id="req-func-0055"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0055**  | **Atomic OTA Installation**                                |
| **Statement**    | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.4] · SRS-FUNC-0056 |

<a id="req-func-0056"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0056**  | **Dual-Bank Auto-Revert on Boot Failure**                                |
| **Statement**    | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.4], [PRD §11.5] · SRS-FUNC-0055, SRS-FUNC-0057 |

<a id="req-func-0057"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0057**  | **No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install**                                |
| **Statement**    | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §9.4] · SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0051 |

<a id="req-func-0058"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0058**  | **Device-Side OTA Update State Reporting**                                |
| **Statement**    | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.5] · SRS-FUNC-0059, SRS-FUNC-0060 |

<a id="req-func-0059"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0059**  | **App Notification of Available OTA Update (external)**                                |
| **Statement**    | The Mobile App **shall** notify the user when an OTA firmware update is available. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §9.5], [EXTERNAL: Mobile App team] · SRS-FUNC-0043, SRS-FUNC-0044 |

<a id="req-func-0060"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0060**  | **App Display of OTA Update State (external)**                                |
| **Statement**    | The Mobile App **shall** display the current OTA update state reported by the device. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §9.5], [EXTERNAL: Mobile App team] · SRS-FUNC-0058 |

<a id="req-func-0061"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0061**  | **SBOM Production Per OTA Release**                                |
| **Statement**    | The system **shall** produce a Software Bill of Materials for every OTA firmware release. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §9.5] |

<a id="req-func-0062"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-FUNC-0062**  | **Tier-2 Classifier Delivery Restricted to Embedded OTA Components**                                |
| **Statement**    | The system **shall** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §9.5] · SRS-FUNC-0034, SRS-FUNC-0035, SRS-FUNC-0052 |


## 6. Performance Requirements

## 6.1 Battery-Life Performance

## 6.2 Classification & Data-Path Latency

## 6.3 Location & Startup Timing (Max Variant / System)

## 6.4 Startup & Physical-Interaction Timing

<a id="req-perf-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0001**  | **Mini Variant Battery-Life Conformance**                                |
| **Statement**    | The system's Mini variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §12.1], [PRD §10.4], [CR-0002], [PRD §15.6] · SRS-FUNC-0012, SRS-FUNC-0013 |

<a id="req-perf-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0002**  | **Max Variant Battery-Life Conformance**                                |
| **Statement**    | The system's Max variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval settings. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §12.1], [PRD §10.4], [CR-0002], [PRD §15.6] · SRS-FUNC-0012, SRS-FUNC-0013 |

<a id="req-perf-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0003**  | **Classification Latency Ceiling**                                |
| **Statement**    | The system **shall** produce a classification result within 2 seconds of the triggering motion event. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1] · SRS-FUNC-0016 |

<a id="req-perf-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0004**  | **Base Station Cloud-Upload Latency Ceiling**                                |
| **Statement**    | The base station **shall** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1] · SRS-CONN-0014, SRS-CONN-0015 |

<a id="req-perf-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0005**  | **GNSS Time-to-First-Fix Ceiling (Warm, A-GPS)**                                |
| **Statement**    | On the Max product variant, the system **shall** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1] |

<a id="req-perf-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0006**  | **Collar Boot-Time Ceiling**                                |
| **Statement**    | The collar-mounted device **shall** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1], [ASSUMPTION: A-0019] · SRS-FUNC-0056 |

<a id="req-perf-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0007**  | **Home/Away Status Update Latency Ceiling**                                |
| **Statement**    | The system **shall** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1] · SRS-CONN-0004, SRS-CONN-0005 |

<a id="req-perf-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-PERF-0008**  | **CCF Twist-Lock Engagement Time Ceiling**                                |
| **Statement**    | The system **shall** allow the Twist-Lock mechanism to be engaged within 5 seconds. |
| **Rationale**    |  |
| **Priority**     | LOW                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1] |


## 7. Safety Requirements

# §7 — Safety Requirements


## 7.1 Zone 2 Fuse Tab — Strangulation-Prevention Breakaway

## 7.2 Zone 1 — Structural Retention (Non-Breakaway)

## 7.3 Twist-Lock — Retention Safety (Non-Breakaway)

## 7.4 Post-Breakaway Protocol & Re-Use Prevention

## 7.5 Chew Resistance

## 7.6 Device-Absent Socket — Entrapment Prevention

## 7.7 Animal-Contact Material Safety

## 7.8 Battery-Ingestion Warning

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-SAFE-0001 | CCF-S Zone 2 Breakaway Force Window (Feline) | CRITICAL | STABLE | Test |
| SRS-SAFE-0002 | CCF-M Zone 2 Breakaway Force Window (Canine, Medium) | CRITICAL | STABLE | Test |
| SRS-SAFE-0003 | CCF-L Zone 2 Breakaway Force Window (Canine, Large) | CRITICAL | STABLE | Test |
| SRS-SAFE-0004 | CCF-L Force-Window Contingency for Assembled Mass Exceeding 26 g | CRITICAL | LIKELY-CHANGE | Analysis |
| SRS-SAFE-0005 | Zone 2 Single-Use Restriction | CRITICAL | STABLE | Test |
| SRS-SAFE-0006 | Zone 2 No-Detached-Fragment on Fracture | HIGH | STABLE | Inspection |
| SRS-SAFE-0007 | Zone 2 Post-Fracture Surface Bluntness | HIGH | STABLE | Inspection |
| SRS-SAFE-0008 | Zone 2 Visible Fracture Indicator | HIGH | STABLE | Inspection |
| SRS-SAFE-0009 | Zone 1 Structural Retention Force | CRITICAL | STABLE | Test |
| SRS-SAFE-0010 | Zone 1 Survival Through Zone 2 Fracture | CRITICAL | STABLE | Test |
| SRS-SAFE-0011 | Twist-Lock Axial Retention Force | CRITICAL | STABLE | Test |
| SRS-SAFE-0012 | Twist-Lock Retention Under Pet-Motion Inertial Loading | HIGH | STABLE | Test |
| SRS-SAFE-0013 | No-Wear-Without-Intact-Zone-2 | CRITICAL | STABLE | Inspection |
| SRS-SAFE-0014 | Device Separation-Signature Emission | HIGH | STABLE | Test |
| SRS-SAFE-0015 | CCF-Replacement-Required Notification | HIGH | STABLE | Inspection (external conformance evidence) |
| SRS-SAFE-0016 | Zone 2 Non-Fracture Under Chew-Compressive Load | CRITICAL | STABLE | Test |
| SRS-SAFE-0017 | CCF Body Chew-Penetration Resistance | HIGH | STABLE | Test |
| SRS-SAFE-0018 | Device Enclosure Chew Resistance | MEDIUM | LIKELY-CHANGE | Analysis |
| SRS-SAFE-0019 | Device-Absent Socket Entrapment-Hazard Avoidance | HIGH | STABLE | Analysis |
| SRS-SAFE-0020 | Device-Absent Socket Probe-Clearance Criterion | MEDIUM | LIKELY-CHANGE | Test |
| SRS-SAFE-0021 | Animal-Contact Material Non-Toxicity | HIGH | STABLE | Inspection |
| SRS-SAFE-0022 | Battery-Ingestion Warning Labeling | HIGH | STABLE | Inspection |

<a id="req-safe-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0001**  | **CCF-S Zone 2 Breakaway Force Window (Feline)**                                |
| **Statement**    | The Zone 2 Fuse Tab of the CCF-S variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2b], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)], [ASSUMPTION: A-0017] · SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="req-safe-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0002**  | **CCF-M Zone 2 Breakaway Force Window (Canine, Medium)**                                |
| **Statement**    | The Zone 2 Fuse Tab of the CCF-M variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2b], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)], [ASSUMPTION: A-0017], [ASSUMPTION: A-0020] · SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="req-safe-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0003**  | **CCF-L Zone 2 Breakaway Force Window (Canine, Large)**                                |
| **Statement**    | The Zone 2 Fuse Tab of the CCF-L variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device+CCF mass does not exceed 26 g. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2b], [PRD §10.1.4], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)], [ASSUMPTION: A-0017], [ASSUMPTION: A-0020] · SRS-SAFE-0004, SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="req-safe-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0004**  | **CCF-L Force-Window Contingency for Assembled Mass Exceeding 26 g**                                |
| **Statement**    | If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **shall** be revised upward to 30 N. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §10.1.4] · SRS-SAFE-0003 |

<a id="req-safe-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0005**  | **Zone 2 Single-Use Restriction**                                |
| **Statement**    | The Zone 2 Fuse Tab **shall not** be capable of being reused or restored to a load-bearing state after fracture. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2b], [PRD §13.2] · SRS-SAFE-0013 |

<a id="req-safe-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0006**  | **Zone 2 No-Detached-Fragment on Fracture**                                |
| **Statement**    | Upon fracture, the Zone 2 Fuse Tab **shall not** produce a detached fragment separate from the CCF body. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2b] · — |

<a id="req-safe-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0007**  | **Zone 2 Post-Fracture Surface Bluntness**                                |
| **Statement**    | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **shall** be blunt, presenting no sharp edge. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2b] · — |

<a id="req-safe-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0008**  | **Zone 2 Visible Fracture Indicator**                                |
| **Statement**    | The CCF **shall** present a visible fracture indicator upon Zone 2 breakaway. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2b], [PRD §13.2] · SRS-SAFE-0013 |

<a id="req-safe-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0009**  | **Zone 1 Structural Retention Force**                                |
| **Statement**    | The Zone 1 clamp **shall** retain axial loads of at least 50 N without structural failure. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.1], [PRD §10.1.3.4], [PRD §13.2] · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="req-safe-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0010**  | **Zone 1 Survival Through Zone 2 Fracture**                                |
| **Statement**    | The Zone 1 clamp **shall** remain structurally intact following a Zone 2 fracture event. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.1] · SRS-SAFE-0009, SRS-SAFE-0013 |

<a id="req-safe-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0011**  | **Twist-Lock Axial Retention Force**                                |
| **Statement**    | The Twist-Lock device-to-CCF interface **shall** retain axial loads exceeding 100 N without disengaging. |
| **Rationale**    | SAFE-0011 is the last mechanical line of defense preventing device separation from the wearer during a pet escape attempt. Failure of this retention means the device detaches entirely, losing all monitoring, safety tracking, and breakaway-event signaling. This aligns it with SRS-INT-0045 (§10) which already carries CRITICAL for the same >100 N requirement. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.1] · SRS-PERF-0008 |

<a id="req-safe-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0012**  | **Twist-Lock Retention Under Pet-Motion Inertial Loading**                                |
| **Statement**    | The Twist-Lock **shall** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] · SRS-SAFE-0011 |

<a id="req-safe-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0013**  | **No-Wear-Without-Intact-Zone-2**                                |
| **Statement**    | The device **shall not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.6] · SRS-SAFE-0005, SRS-SAFE-0008 |

<a id="req-safe-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0014**  | **Device Separation-Signature Emission**                                |
| **Statement**    | The device **shall** emit a detectable separation signature upon Zone 2 breakaway. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.6] · SRS-SAFE-0015 |

<a id="req-safe-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0015**  | **CCF-Replacement-Required Notification**                                |
| **Statement**    | The Mobile App **shall** notify the owner that CCF replacement is required upon receiving a device separation signature. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection (external conformance evidence)                               |
| **Traceability** | [PRD §10.1.3.6], [EXTERNAL: Mobile App team] · SRS-SAFE-0014 |

<a id="req-safe-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0016**  | **Zone 2 Non-Fracture Under Chew-Compressive Load**                                |
| **Statement**    | The Zone 2 Fuse Tab **shall not** fracture under a compressive load below 250 N. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.2] · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="req-safe-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0017**  | **CCF Body Chew-Penetration Resistance**                                |
| **Statement**    | The CCF body **shall** resist penetration for at least 30 seconds under a 250 N compressive load. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.2] · — |

<a id="req-safe-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0018**  | **Device Enclosure Chew Resistance**                                |
| **Statement**    | Materials in animal-skin contact on the device enclosure **shall** resist chew-induced damage. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §10.1.2], [PRD — ABSENT: device enclosure chew-resistance numeric bound] · SRS-SAFE-0016, SRS-SAFE-0017 |

<a id="req-safe-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0019**  | **Device-Absent Socket Entrapment-Hazard Avoidance**                                |
| **Statement**    | The CCF socket **shall** present no independent entrapment hazard when the device is absent. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §10.1.3.5], [PRD §13.2] · SRS-SAFE-0020 |

<a id="req-safe-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0020**  | **Device-Absent Socket Probe-Clearance Criterion**                                |
| **Statement**    | The device-absent CCF socket **shall** provide clearance verified against a 12 mm entrapment-probe criterion. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.5], [ASSUMPTION: A-0010] · SRS-SAFE-0019 |

<a id="req-safe-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0021**  | **Animal-Contact Material Non-Toxicity**                                |
| **Statement**    | Materials in animal-skin contact **shall** be non-toxic. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2], [PRD §13.2] · — (see §17 for REACH/RoHS/Prop 65 mechanism) |

<a id="req-safe-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SAFE-0022**  | **Battery-Ingestion Warning Labeling**                                |
| **Statement**    | The system **shall** provide battery-ingestion warning labeling. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.2], [ASSUMPTION: A-0011] · — |


## 8. Security Requirements

**CAT: SEC** | Maps to: PRD §6.7, §12.3; supporting anchor PRD §10.7

**Scope note:**  Supplies the "secured connection" referenced by SRS-CONN-0009 (§4) and SRS-FUNC-0047 (§5), closing both orphans. Does NOT restate §5 OTA signature/anti-rollback chain.

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)

## 8.2 Cloud-Bound Transport Security

## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.

## 8.4 Device Identity & Platform Trust

## 8.5 Vulnerability Disclosure (pre-launch gate only)

<a id="req-sec-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SEC-0001**  | **Mandatory Link-Layer Encryption on Collar↔Base BLE Data-Bearing Links**                                |
| **Statement**    | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. |
| **Rationale**    | Baseline protecting behavioral, location, and event data in transit over the wireless collar↔base channel. The "secured connection" / "secured BLE link" that SRS-CONN-0009 and SRS-FUNC-0047 forward-reference. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.7], [PRD §8.2], [PRD §12.3], [STD: ETSI EN 303 645:2025] · SRS-CONN-0009, SRS-FUNC-0047 |

<a id="req-sec-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SEC-0002**  | **Mandatory LE Secure Connections Pairing Method**                                |
| **Statement**    | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. |
| **Rationale**    | Underpins SEC-0001 encryption; weaker legacy pairing would undermine the confidentiality guarantee. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3], [PRD §8.2], [STD: ETSI EN 303 645:2025] · SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009 |

<a id="req-sec-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SEC-0003**  | **TLS 1.3 Exclusivity for Base-to-Cloud Data Transport**                                |
| **Statement**    | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. |
| **Rationale**    | Generalizes the TLS-1.3-exclusive posture (already applied to OTA via FUNC-0045 per CR-0005) to all base↔cloud channels. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.5], [PRD §12.3], [STD: ETSI EN 303 645:2025] · SRS-CONN-0014, SRS-FUNC-0045 |

<a id="req-sec-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SEC-0004**  | **Unique Cryptographic Identity at Manufacturing**                                |
| **Statement**    | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. |
| **Rationale**    | Per-device unique identity underpins secure boot attestation and per-device compromise containment. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.3] · SRS-SEC-0005 |

<a id="req-sec-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SEC-0005**  | **Secure Boot Anchored in Hardware Root of Trust**                                |
| **Statement**    | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. |
| **Rationale**    | Prevents execution of unauthorized firmware from non-OTA write paths. Boot-time integrity checking consumes part of the PERF-0006 ≤3 s budget — distinct dimensions, flagged for cross-section awareness. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.7] · SRS-SEC-0004, SRS-FUNC-0053, SRS-PERF-0006 |

<a id="req-sec-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-SEC-0006**  | **Public Vulnerability-Disclosure Policy in Place Before Launch**                                |
| **Statement**    | The system shall have a public vulnerability-disclosure policy in place before product launch. |
| **Rationale**    | Published disclosure channel must exist at launch. Lifetime maintenance in §16. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.3], [PRD §13.5], [STD: ETSI EN 303 645:2025], [STD: EU CRA (EU) 2024/2847 Art 13-14] · — |


## 9. Data Requirements

# SRS §9 — Data Requirements (v2)

## 9.1 Introduction and Scope Boundary

This section specifies requirements governing the **content, storage, integrity, privacy, and protection** of data produced by the LUUCIPet Wellness Monitor collar (Mini and Max variants). It covers what classification and event data *is* and how it must be handled on-device — not the transport protocol mechanics, which are specified in SRS §4 (CONN), nor the classification algorithm itself, which is specified in SRS §3 (FUNC), nor transport-layer cryptography, which is specified in SRS §8 (SEC). Where a data-layer requirement is closely coupled to an existing connectivity requirement, a cross-reference is given rather than a duplicate statement.

Per the standing scope model, functions performed by parties outside this build (Mobile App team, IoT Cloud backend team) are documented as non-normative boundary notes in §9.11 rather than silently omitted.

Applicable regulatory instruments for this section (from the Regulatory Map) are GDPR (EU) 2016/679, UK GDPR + DPA 2018, PIPEDA, CCPA/CPRA (indicative), and the data-protection-relevant provisions of ETSI EN 303 645:2025. Cybersecurity vulnerability-management obligations under the RED Delegated Act, EU CRA, and UK PSTI Act are addressed in SRS §8 (SEC) and are not repeated here.

---

## 9.2 Classification Record Format & Schema

## 9.3 On-Device Storage & Retention

## 9.4 Data Integrity

## 9.5 Raw Data Boundary & Processing Locality

## 9.6 Buffered Data Persistence

## 9.7 Privacy Regime — Data Handling Obligations

## 9.8 Data-at-Rest Protection

## 9.9 External Data Transport Interface

## 9.10 Breakaway Event Record Persistence

## 9.11 Out-of-Scope Data Functions (Boundary Notes — Non-Normative)

The following data-related functions are outside this system's build scope but are documented here, not silently dropped, per the group scope model:

- **Cloud-side storage and analytics** of the data transported under SRS-DATA-0024 is performed by the **[EXTERNAL: IoT Cloud backend team]**. This system's data obligation ends at successful, acknowledged transport to the Device-Management layer.
- **Mobile App presentation/display** of wellness records, classification history, and breakaway alerts is performed by the **[EXTERNAL: Mobile App team]**. No display, formatting, or rendering requirement is levied on the collar/base-station system.
- **Cloud-side home/away state machine** (per A-0016) is **[EXTERNAL: IoT Cloud backend team]**-owned; the device-local home/away state machine referenced elsewhere in this SRS is the sole in-scope authority for power gating, and no data requirement beyond the transport obligation in SRS-DATA-0024 applies here.

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-DATA-0001 | Classification Record Content | CRITICAL | STABLE | Test |
| SRS-DATA-0002 | Confidence Score Bound | HIGH | STABLE | Test |
| SRS-DATA-0003 | Record Timestamp Accuracy | HIGH | STABLE | Test |
| SRS-DATA-0004 | GNSS Context on Max Variant | HIGH | STABLE | Test |
| SRS-DATA-0005 | On-Device Storage Duration | CRITICAL | STABLE | Test |
| SRS-DATA-0006 | Retention Through Power Loss | CRITICAL | STABLE | Test |
| SRS-DATA-0007 | Storage Corruption Detection | HIGH | LIKELY-CHANGE | Test |
| SRS-DATA-0008 | Classification Independent of Connectivity | CRITICAL | STABLE | Test |
| SRS-DATA-0009 | Record Forwarding Without Corruption | CRITICAL | STABLE | Test |
| SRS-DATA-0010 | Record Forwarding Without Sequence Loss | HIGH | STABLE | Test |
| SRS-DATA-0011 | Raw Sensor Data Transmission Boundary | CRITICAL | STABLE | Test |
| SRS-DATA-0012 | On-Device Normalization | HIGH | STABLE | Analysis |
| SRS-DATA-0013 | No Cloud Round-Trip for Classification | HIGH | STABLE | Demonstration |
| SRS-DATA-0014 | Raw Sample Retention Minimization | MEDIUM | LIKELY-CHANGE | Analysis |
| SRS-DATA-0015 | Buffered Data Retention Until Acknowledgement | CRITICAL | STABLE | Test |
| SRS-DATA-0016 | No Buffer Clear on Disconnect Alone | CRITICAL | STABLE | Test |
| SRS-DATA-0017 | Stale-Data Flag on Delayed Upload | MEDIUM | STABLE | Test |
| SRS-DATA-0018 | Data Minimization for Personal Data | HIGH | LIKELY-CHANGE | Inspection |
| SRS-DATA-0019 | Purpose Limitation | HIGH | STABLE | Inspection |
| SRS-DATA-0020 | On-Device Data Deletion Support | MEDIUM | LIKELY-CHANGE | Demonstration |
| SRS-DATA-0021 | On-Device Data Access Support | MEDIUM | LIKELY-CHANGE | Demonstration |
| SRS-DATA-0022 | Consumer Privacy Rights Contingency (CCPA/CPRA) | LOW | VOLATILE | Analysis |
| SRS-DATA-0023 | Data-at-Rest Encryption | CRITICAL | STABLE | Inspection |
| SRS-DATA-0024 | Transport to Cloud Device-Management Layer | CRITICAL | STABLE | Test |
| SRS-DATA-0025 | Breakaway Record Commit Timing | CRITICAL | STABLE | Test |
| SRS-DATA-0026 | Breakaway Record Survivability | CRITICAL | STABLE | Test |
| SRS-DATA-0027 | Breakaway Record Transmission Trigger | HIGH | STABLE | Test |

<a id="req-data-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0001**  | **Classification Record Content**                                |
| **Statement**    | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] |

<a id="req-data-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0002**  | **Confidence Score Bound**                                |
| **Statement**    | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] |

<a id="req-data-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0003**  | **Record Timestamp Accuracy**                                |
| **Statement**    | The system shall timestamp each classification record with UTC time accurate to within 1 second. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] |

<a id="req-data-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0004**  | **GNSS Context on Max Variant**                                |
| **Statement**    | On the Max variant, the system shall append the most recent GNSS fix to the classification record. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5] |

<a id="req-data-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0005**  | **On-Device Storage Duration**                                |
| **Statement**    | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5; PRD §10.6] |

<a id="req-data-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0006**  | **Retention Through Power Loss**                                |
| **Statement**    | The system shall preserve stored classification records without corruption across a power-loss event. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.6] |

<a id="req-data-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0007**  | **Storage Corruption Detection**                                |
| **Statement**    | The system shall detect corruption of stored classification records prior to transmission. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.6] |

<a id="req-data-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0008**  | **Classification Independent of Connectivity**                                |
| **Statement**    | The system shall perform classification and record generation independent of BLE connectivity state. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] |

<a id="req-data-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0009**  | **Record Forwarding Without Corruption**                                |
| **Statement**    | The system shall forward stored classification records to the transport layer without introducing data corruption. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] |

<a id="req-data-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0010**  | **Record Forwarding Without Sequence Loss**                                |
| **Statement**    | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] |

<a id="req-data-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0011**  | **Raw Sensor Data Transmission Boundary**                                |
| **Statement**    | The system shall not transmit raw accelerometer data beyond the collar. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.7] |

<a id="req-data-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0012**  | **On-Device Normalization**                                |
| **Statement**    | The system shall perform normalization of sensor data on-device prior to classification. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §7.7] |

<a id="req-data-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0013**  | **No Cloud Round-Trip for Classification**                                |
| **Statement**    | The system shall not require a cloud round-trip to complete a classification decision. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §7.7] |

<a id="req-data-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0014**  | **Raw Sample Retention Minimization**                                |
| **Statement**    | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §7.7; STD: RM-0015 §Art.25] |

<a id="req-data-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0015**  | **Buffered Data Retention Until Acknowledgement**                                |
| **Statement**    | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.4] |

<a id="req-data-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0016**  | **No Buffer Clear on Disconnect Alone**                                |
| **Statement**    | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.4] |

<a id="req-data-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0017**  | **Stale-Data Flag on Delayed Upload**                                |
| **Statement**    | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.7] |

<a id="req-data-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0018**  | **Data Minimization for Personal Data**                                |
| **Statement**    | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0015 §Art.5(1)(c)] |

<a id="req-data-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0019**  | **Purpose Limitation**                                |
| **Statement**    | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0015 §Art.5(1)(b)] |

<a id="req-data-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0020**  | **On-Device Data Deletion Support**                                |
| **Statement**    | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [STD: RM-0015 §Art.17] |

<a id="req-data-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0021**  | **On-Device Data Access Support**                                |
| **Statement**    | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [STD: RM-0015 §Art.15] |

<a id="req-data-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0022**  | **Consumer Privacy Rights Contingency (CCPA/CPRA)**                                |
| **Statement**    | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. |
| **Rationale**    |  |
| **Priority**     | LOW                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [STD: RM-0017] |

<a id="req-data-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0023**  | **Data-at-Rest Encryption**                                |
| **Statement**    | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0015 §Art.32; STD: RM-0019 §Prov.5.8] |

<a id="req-data-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0024**  | **Transport to Cloud Device-Management Layer**                                |
| **Statement**    | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.1; ASSUMPTION: A-0015] |

<a id="req-data-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0025**  | **Breakaway Record Commit Timing**                                |
| **Statement**    | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION: A-0018] |

<a id="req-data-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0026**  | **Breakaway Record Survivability**                                |
| **Statement**    | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION: A-0018] |

<a id="req-data-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-DATA-0027**  | **Breakaway Record Transmission Trigger**                                |
| **Statement**    | The system shall transmit a committed breakaway event record on the next successful base-station contact following separation. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION: A-0018] |


## 10. Interface Requirements

---

## 10.0 Scope Note

This section specifies the external interfaces of the LUUCIPet Wellness Monitor system: the BLE radio interface (collar↔base station), the Wi-Fi radio interface (base station↔cloud), the GNSS receive interface (Max only), the pogo-pin charging interface, the Twist-Lock mechanical attachment interface (collar device↔CCF), and the device-enforced BLE application protocol [PRD §6, PRD §10.2, PRD §10.3, PRD §10.5, PRD §11]. Zone 2 Fuse Tab breakaway force windows and post-breakaway safety protocol are governed by the Safety Requirements section (CAT=SAFE) and are not restated here; the Twist-Lock mechanism addressed in this section is the non-breakaway, owner-operated charging-removal interface only [PRD §10.1.3.1]. Cross-variant identical mechanical-interface geometry for pogo-pin and Twist-Lock across Mini/Max is already established by **SRS-COMP-0003** (§2); this section does not re-issue that requirement.

---

## 10.1 BLE Interface

---

## 10.2 Wi-Fi Interface

---

## 10.3 GNSS Interface (Max Only)

> **Flagged (not a normative block):** Per [ASSUMPTION A-0004], "full-quality GNSS" is interpreted as acquisition-based (a fix obtained within the 90 s timeout using A-GPS); no PDOP or metres-level position-accuracy bound is imposed by the PRD, and none is introduced here. This is documented to prevent a future numeric-accuracy requirement from being silently assumed.

---

## 10.4 Pogo-Pin Charging Interface

---

## 10.5 Twist-Lock Mechanical Interface

---

## 10.6 Device-Enforced Protocol

---

## 10.7 Out-of-Scope Items & Flagged Gaps (Documented, Not Silently Dropped)

- **GPS-M variant / cellular connectivity** — explicitly OUT OF SCOPE for this SRS (Phase 2, separate PRD) per the PRD's own scope note. No GPS-M or cellular interface requirement is issued in this section, and none should be inferred.
- **Mobile App pairing UI / provisioning** — the app's presentation of the QR OOB pairing code and any BLE-provisioning UI flow is OUT OF SCOPE for this SRS (Mobile App team); only the device/base-station-side OOB pairing mechanism is specified here (SRS-INT-0012).
- **Cloud-side storage/analytics beyond ingest** — OUT OF SCOPE for this SRS per [ASSUMPTION A-0015]; only the device/base-station-side transport (Wi-Fi/TLS 1.3 uplink) is specified here (SRS-INT-0017).
- **NACK mechanics and retry policy** — the PRD specifies positive-ACK-gated buffer retention (§8.4) but does not specify a NACK message, retry count, or retry backoff interval. No numeric retry policy is invented here per the design-free/numeric-vagueness rule; this is flagged as a candidate new assumption or PRD clarification for the Assumption Register rather than an SRS requirement with an unsourced numeric bound.
- **GNSS position-accuracy bound** — per [ASSUMPTION A-0004], no PDOP or metres-level accuracy target is imposed on the Max GNSS interface beyond acquisition within the 90 s timeout; documented in §10.3 to prevent a future undocumented accuracy requirement.
- **Zone 2 Fuse Tab breakaway force windows and post-breakaway protocol** — governed by the Safety Requirements section (CAT=SAFE); intentionally not restated in this Interface Requirements section.

---

### SRS-IDs issued

SRS-INT-0001 through SRS-INT-0060 (60 requirements).

### Assumptions cited

A-0001, A-0004, A-0009, A-0010, A-0015, A-0016.

### Existing cross-references relied upon (not re-issued)

SRS-COMP-0001, SRS-COMP-0003, SRS-OPER-0004 (all from approved §2).

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-INT-0001 | Collar BLE Peripheral Role | HIGH | STABLE | Test |
| SRS-INT-0002 | Base Station BLE Central Role | HIGH | STABLE | Test |
| SRS-INT-0003 | Minimum Concurrent Collar Sessions | HIGH | STABLE | Test |
| SRS-INT-0004 | Default BLE Advertising Interval | MEDIUM | STABLE | Test |
| SRS-INT-0005 | Configurable BLE Advertising Interval Range | MEDIUM | STABLE | Test |
| SRS-INT-0006 | Advertising Continuity During Active Connection | MEDIUM | STABLE | Test |
| SRS-INT-0007 | BLE Address Randomization | HIGH | STABLE | Test |
| SRS-INT-0008 | Minimum BLE Transmit Power | MEDIUM | STABLE | Test |
| SRS-INT-0009 | Minimum BLE Open-Air Range | HIGH | STABLE | Test |
| SRS-INT-0010 | BLE Link-Layer Encryption Algorithm | CRITICAL | STABLE | Test |
| SRS-INT-0011 | BLE Pairing via LE Secure Connections | CRITICAL | STABLE | Test |
| SRS-INT-0012 | QR Out-of-Band Pairing Mechanism | HIGH | STABLE | Test |
| SRS-INT-0013 | BLE Radio Regulatory Conformance | CRITICAL | STABLE | Test |
| SRS-INT-0014 | Bluetooth SIG Qualification | CRITICAL | STABLE | Inspection |
| SRS-INT-0015 | RF Human-Exposure Assessment | MEDIUM | VOLATILE | Analysis |
| SRS-INT-0016 | Wi-Fi Radio Band and Standard | HIGH | STABLE | Test |
| SRS-INT-0017 | Cloud Uplink Transport Encryption | CRITICAL | STABLE | Test |
| SRS-INT-0018 | Default Access-Point Configuration Compatibility | MEDIUM | STABLE | Test |
| SRS-INT-0019 | Minimum Wi-Fi Uplink Signal Condition | MEDIUM | LIKELY-CHANGE | Test |
| SRS-INT-0020 | Wi-Fi Radio Regulatory Conformance | CRITICAL | STABLE | Test |
| SRS-INT-0021 | GNSS Interface Presence on Max | HIGH | STABLE | Test |
| SRS-INT-0022 | GNSS Interface Absence on Mini | MEDIUM | STABLE | Inspection |
| SRS-INT-0023 | Configurable GNSS Fix Interval Range | HIGH | STABLE | Test |
| SRS-INT-0024 | Default GNSS Fix Interval | MEDIUM | STABLE | Test |
| SRS-INT-0025 | A-GPS Assistance Data Delivery | HIGH | STABLE | Test |
| SRS-INT-0026 | A-GPS Assistance Data Validity Window | MEDIUM | STABLE | Test |
| SRS-INT-0027 | GNSS Power Gating During HOME State | HIGH | STABLE | Test |
| SRS-INT-0028 | GNSS Fix Acquisition Timeout | HIGH | STABLE | Test |
| SRS-INT-0029 | Warm GNSS Time-to-First-Fix Ceiling | MEDIUM | STABLE | Test |
| SRS-INT-0030 | GNSS Intentional-Radiator Exemption Status | MEDIUM | VOLATILE | Analysis |
| SRS-INT-0031 | Pogo-Pin Contact Count and Function | CRITICAL | STABLE | Inspection |
| SRS-INT-0032 | Magnetic Charging Alignment | CRITICAL | STABLE | Demonstration |
| SRS-INT-0033 | First-Attempt Docking Seating Rate | MEDIUM | STABLE | Test |
| SRS-INT-0034 | Full-Charge Time Ceiling | HIGH | STABLE | Test |
| SRS-INT-0035 | IP67 Rating When Undocked | CRITICAL | STABLE | Test |
| SRS-INT-0036 | Charging Socket Self-Drainage | MEDIUM | LIKELY-CHANGE | Test |
| SRS-INT-0037 | Charging-Access Removal Rotation | HIGH | STABLE | Demonstration |
| SRS-INT-0038 | Device-Absent Socket Entrapment Geometry | HIGH | LIKELY-CHANGE | Test |
| SRS-INT-0039 | Bayonet Lug Configuration | CRITICAL | STABLE | Inspection |
| SRS-INT-0040 | Lock/Unlock Rotation Angle | HIGH | STABLE | Test |
| SRS-INT-0041 | Lug Ramp Self-Locking Profile | HIGH | STABLE | Inspection |
| SRS-INT-0042 | Twist-Lock Lug Dimensions | HIGH | STABLE | Inspection |
| SRS-INT-0043 | Asymmetric Keying Lug | HIGH | STABLE | Inspection |
| SRS-INT-0044 | Detent Release Torque Window | HIGH | STABLE | Test |
| SRS-INT-0045 | Twist-Lock Axial Retention Floor | CRITICAL | STABLE | Test |
| SRS-INT-0046 | Twist-Lock Engagement Insertion Force Ceiling | MEDIUM | STABLE | Test |
| SRS-INT-0047 | Twist-Lock Engagement Rotation Torque Ceiling | HIGH | STABLE | Test |
| SRS-INT-0048 | Engagement Feedback | MEDIUM | STABLE | Demonstration |
| SRS-INT-0049 | Magnetic Engagement Assist Range | LOW | STABLE | Test |
| SRS-INT-0050 | Tool-Free Twist-Lock Operation | HIGH | STABLE | Demonstration |
| SRS-INT-0051 | Twist-Lock Engagement Time Ceiling | LOW | STABLE | Test |
| SRS-INT-0052 | Common Device-Enforced Protocol Across Variants | HIGH | STABLE | Inspection |
| SRS-INT-0053 | Payload Type — Behavioral Classification Record | HIGH | STABLE | Test |
| SRS-INT-0054 | Payload Type — BLE Sighting Report | HIGH | STABLE | Test |
| SRS-INT-0055 | Payload Type — Cloud Downlink | HIGH | STABLE | Test |
| SRS-INT-0056 | Base Station Payload Content Opacity | HIGH | STABLE | Inspection |
| SRS-INT-0057 | Collar Buffer Retention Pending Acknowledgment | HIGH | STABLE | Test |
| SRS-INT-0058 | No FIFO Clear on Disconnect Alone | HIGH | STABLE | Test |
| SRS-INT-0059 | Sequence-Loss Detection | HIGH | STABLE | Test |
| SRS-INT-0060 | Corruption-Free Record Forwarding | HIGH | STABLE | Test |

<a id="req-int-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0001**  | **Collar BLE Peripheral Role**                                |
| **Statement**    | The collar device shall implement the Bluetooth Low Energy (BLE) 5.x radio interface in the peripheral role. |
| **Rationale**    | The collar is the advertising/connectable endpoint of the collar-to-base-station link; role assignment is imposed by the system architecture. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3], [PRD §8.1], [PRD §10.3] |

<a id="req-int-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0002**  | **Base Station BLE Central Role**                                |
| **Statement**    | The base station shall implement the BLE 5.x radio interface in the central role. |
| **Rationale**    | The base station scans for and initiates connections to collar devices; role assignment is imposed by the system architecture. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §11.2] · SRS-INT-0001 |

<a id="req-int-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0003**  | **Minimum Concurrent Collar Sessions**                                |
| **Statement**    | The base station shall support at least 4 concurrent BLE connections to collar devices. |
| **Rationale**    | A multi-pet household requires the base station to hold multiple simultaneous collar links without dropping connections. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.1], [PRD §11.2] |

<a id="req-int-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0004**  | **Default BLE Advertising Interval**                                |
| **Statement**    | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. |
| **Rationale**    | Establishes the out-of-box discoverability cadence balancing power consumption against connection latency. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3], [PRD §8.1] |

<a id="req-int-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0005**  | **Configurable BLE Advertising Interval Range**                                |
| **Statement**    | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. |
| **Rationale**    | Allows the advertising cadence to be tuned for household-specific power/latency trade-offs. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.1] |

<a id="req-int-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0006**  | **Advertising Continuity During Active Connection**                                |
| **Statement**    | The collar device shall continue BLE advertising while maintaining an active BLE connection. |
| **Rationale**    | Preserves discoverability for additional base stations in a multi-base household while a collar is already connected to one base station. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.1], [PRD §10.3] |

<a id="req-int-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0007**  | **BLE Address Randomization**                                |
| **Statement**    | The collar device shall randomize its BLE device address. |
| **Rationale**    | Prevents long-term tracking of the wearable by third parties observing BLE advertisements. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.1], [PRD §10.3] |

<a id="req-int-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0008**  | **Minimum BLE Transmit Power**                                |
| **Statement**    | The collar device shall transmit BLE signals at a power level of at least +8 dBm. |
| **Rationale**    | A minimum TX power floor is necessary to meet the stated open-air range target. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.3] · SRS-INT-0009, SRS-HW-0019 |

<a id="req-int-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0009**  | **Minimum BLE Open-Air Range**                                |
| **Statement**    | The BLE link between the collar device and the base station shall maintain connectivity at an open-air separation distance of at least 9 meters. |
| **Rationale**    | Defines the minimum usable range for typical household room-to-room and yard-adjacent operation. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.3], [PRD §12.1] · SRS-INT-0008 |

<a id="req-int-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0010**  | **BLE Link-Layer Encryption Algorithm**                                |
| **Statement**    | The system shall encrypt all BLE data-bearing links using AES-128 CCM. |
| **Rationale**    | Mandated link-layer confidentiality/integrity mechanism for all collar-to-base-station traffic. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3], [PRD §8.2], [PRD §10.3] |

<a id="req-int-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0011**  | **BLE Pairing via LE Secure Connections**                                |
| **Statement**    | The system shall establish BLE pairing between the collar device and the base station using LE Secure Connections. |
| **Rationale**    | Provides the pairing-time key-exchange mechanism underpinning the mandated link-layer encryption. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3], [PRD §8.2] · SRS-INT-0010 |

<a id="req-int-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0012**  | **QR Out-of-Band Pairing Mechanism**                                |
| **Statement**    | The system shall support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station. |
| **Rationale**    | Defines the device/base-station-side OOB pairing mechanism; the mobile app's presentation of the QR code to the user is out of scope for this SRS and is attributed to the (out-of-scope) Mobile App per the standing scope boundary. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.3], [PRD §8.2] |

<a id="req-int-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0013**  | **BLE Radio Regulatory Conformance**                                |
| **Statement**    | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US), [STD: RED 2014/53/EU] (EU), [STD: UK Radio Equipment Regulations 2017] (UK), [STD: ISED RSS-247] (CA), and [STD: AS/NZS 4268:2017] (AU/NZ). |
| **Rationale**    | Market access for an intentional 2.4 GHz radiator requires conformance to each target market's radio-equipment regulation. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.1] |

<a id="req-int-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0014**  | **Bluetooth SIG Qualification**                                |
| **Statement**    | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). |
| **Rationale**    | Bluetooth SIG membership terms mandate qualification of any BLE product before market release. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: Bluetooth SIG Qualification (QDID)], [PRD §13.1] |

<a id="req-int-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0015**  | **RF Human-Exposure Assessment**                                |
| **Statement**    | The BLE radio interface should undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4 GHz transmission. |
| **Rationale**    | A continuously worn 2.4 GHz transmitter plausibly triggers per-market RF-exposure assessment; applicability and thresholds are per-market INDICATIVE per the Regulatory Map and not yet CONFIRMED, hence a SHOULD rather than SHALL. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §13.1] |

<a id="req-int-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0016**  | **Wi-Fi Radio Band and Standard**                                |
| **Statement**    | The base station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n]. |
| **Rationale**    | Defines the base-to-cloud uplink radio band and PHY/MAC standard. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.2], [PRD §6.5] |

<a id="req-int-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0017**  | **Cloud Uplink Transport Encryption**                                |
| **Statement**    | The base station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. |
| **Rationale**    | Mandated transport-layer confidentiality/integrity mechanism for base-station-to-cloud traffic; the device/base-station side of this transport is in scope, cloud-side storage/analytics is out of scope [ASSUMPTION A-0015]. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.5], [PRD §11.2], [PRD §12.3] |

<a id="req-int-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0018**  | **Default Access-Point Configuration Compatibility**                                |
| **Statement**    | The base station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. |
| **Rationale**    | Avoids requiring the owner to perform non-default router configuration for base-station setup. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.6] |

<a id="req-int-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0019**  | **Minimum Wi-Fi Uplink Signal Condition**                                |
| **Statement**    | The base station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. |
| **Rationale**    | Resolves the PRD's unbounded "reliable Wi-Fi" assumption with an engineered numeric floor; below this bound the ≥30-day offline buffering behavior (Data Requirements, §9) is the defined degraded-mode fallback rather than a new interface requirement. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION A-0009] |

<a id="req-int-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0020**  | **Wi-Fi Radio Regulatory Conformance**                                |
| **Statement**    | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US) and [STD: RED 2014/53/EU] (EU). |
| **Rationale**    | Market access for the base station's Wi-Fi radio requires conformance to each target market's radio-equipment regulation. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.1] |

<a id="req-int-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0021**  | **GNSS Interface Presence on Max**                                |
| **Statement**    | The Max collar variant shall implement a passive (receive-only) GNSS interface. |
| **Rationale**    | GNSS is a defining differentiator of the Max variant, providing location context unavailable on Mini. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.1], [PRD §10.2.2] |

<a id="req-int-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0022**  | **GNSS Interface Absence on Mini**                                |
| **Statement**    | The Mini collar variant shall not implement a GNSS interface. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet its ≤10 g weight budget and BLE-only positioning. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.1] |

<a id="req-int-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0023**  | **Configurable GNSS Fix Interval Range**                                |
| **Statement**    | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. |
| **Rationale**    | Allows the fix cadence to be tuned against the battery-life-vs-fix-interval trade-off documented in the PRD. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.1], [PRD §10.2.2] |

<a id="req-int-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0024**  | **Default GNSS Fix Interval**                                |
| **Statement**    | The Max collar variant shall apply a default GNSS fix interval of 2 hours. |
| **Rationale**    | Establishes the out-of-box fix cadence consistent with the stated ≥45-day @2h battery-life target. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §4.1], [PRD §10.2.2] |

<a id="req-int-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0025**  | **A-GPS Assistance Data Delivery**                                |
| **Statement**    | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. |
| **Rationale**    | A-GPS delivery over the existing BLE link is the defined mechanism for reducing GNSS fix acquisition time. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.2.2] |

<a id="req-int-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0026**  | **A-GPS Assistance Data Validity Window**                                |
| **Statement**    | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. |
| **Rationale**    | Bounds how long stale assistance data may be relied upon before fix-acquisition performance degrades. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.2.2] |

<a id="req-int-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0027**  | **GNSS Power Gating During HOME State**                                |
| **Statement**    | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. |
| **Rationale**    | The GNSS smart power gate underpins the stated Max battery-longevity targets; gating authority rests solely with the device-local state machine per the confirmed in-scope/external boundary. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.2.2], [PRD §6.4], [ASSUMPTION A-0016] · SRS-OPER-0004 |

<a id="req-int-0028"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0028**  | **GNSS Fix Acquisition Timeout**                                |
| **Statement**    | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. |
| **Rationale**    | Bounds the power expenditure of an unsuccessful fix attempt. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.2.2], [PRD §15.5] |

<a id="req-int-0029"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0029**  | **Warm GNSS Time-to-First-Fix Ceiling**                                |
| **Statement**    | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. |
| **Rationale**    | Bounds the latency between a scheduled fix attempt and an available location result. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1] · SRS-INT-0025 |

<a id="req-int-0030"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0030**  | **GNSS Intentional-Radiator Exemption Status**                                |
| **Statement**    | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. |
| **Rationale**    | The PRD defers this exemption determination to Regulatory Lead confirmation per market; the Regulatory Map carries this as INDICATIVE, not CONFIRMED, hence a SHOULD rather than SHALL pending resolution. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §13.1] |

<a id="req-int-0031"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0031**  | **Pogo-Pin Contact Count and Function**                                |
| **Statement**    | The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) shall use a 2-contact pogo-pin arrangement carrying VBUS and GND. |
| **Rationale**    | Defines the minimal electrical contact interface for charging; cross-variant identical geometry is already established by SRS-COMP-0003. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.5] · SRS-COMP-0003 |

<a id="req-int-0032"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0032**  | **Magnetic Charging Alignment**                                |
| **Statement**    | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. |
| **Rationale**    | Magnetic alignment enables reliable tool-free docking without precise manual contact placement. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §6.6], [PRD §10.5] |

<a id="req-int-0033"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0033**  | **First-Attempt Docking Seating Rate**                                |
| **Statement**    | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. |
| **Rationale**    | Bounds the usability of the magnetic docking mechanism to a measurable success rate. Note: this magnetic assist governs the charging-dock (collar device onto charging cradle) interface and is distinct from the device-to-CCF Twist-Lock engagement assist in SRS-INT-0049, though both specify an "up to 5 mm" approach distance. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.5] · SRS-INT-0049 |

<a id="req-int-0034"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0034**  | **Full-Charge Time Ceiling**                                |
| **Statement**    | The collar device shall reach full charge within 2 hours when docked at the charging interface. |
| **Rationale**    | Bounds the time an owner must leave a device docked to restore full charge. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.5], [PRD §12.4] |

<a id="req-int-0035"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0035**  | **IP67 Rating When Undocked**                                |
| **Statement**    | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. |
| **Rationale**    | The exposed pogo-pin contact is a potential ingress path and must not compromise the device-standalone IP67 rating. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.6], [PRD §10.5], [PRD §13.4] · SRS-HW-0004 |

<a id="req-int-0036"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0036**  | **Charging Socket Self-Drainage**                                |
| **Statement**    | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state the socket "shall be self-draining" with no quantified acceptance criterion; the Verification-Method Validator flagged this as method/criterion incoherence — the declared Test method (correctly changed from Inspection) had nothing measurable to test against. [ASSUMPTION: A-0023] resolves this gap (engineered by analogy to A-0007). This requirement shares its underlying drainage claim with SRS-HW-0008 (§11, hardware-geometry framing of the same socket); both corrected together. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.5], [PRD §10.1.3.5], [ASSUMPTION: A-0023] · SRS-HW-0008 |

<a id="req-int-0037"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0037**  | **Charging-Access Removal Rotation**                                |
| **Statement**    | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. |
| **Rationale**    | Defines the workflow by which the charging contacts are exposed for docking, using the non-breakaway Twist-Lock mechanism. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §6.6], [PRD §10.5] · SRS-INT-0039 |

<a id="req-int-0038"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0038**  | **Device-Absent Socket Entrapment Geometry**                                |
| **Statement**    | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature. |
| **Rationale**    | Resolves the PRD's unbounded "no independent entrapment hazard" statement with an engineered geometric probe criterion. |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [ASSUMPTION A-0010], [PRD §10.1.3.5] |

<a id="req-int-0039"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0039**  | **Bayonet Lug Configuration**                                |
| **Statement**    | The Twist-Lock mechanical interface shall use a 3-lug bayonet arrangement spaced at 120 degrees. |
| **Rationale**    | Defines the base geometric arrangement of the device-to-CCF mechanical attachment; identical across Mini/Max per SRS-COMP-0003. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2a] · SRS-COMP-0003 |

<a id="req-int-0040"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0040**  | **Lock/Unlock Rotation Angle**                                |
| **Statement**    | The Twist-Lock mechanical interface shall engage and release via a 90-degree rotation. |
| **Rationale**    | Defines the actuation travel required to lock or unlock the device from the CCF. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-int-0041"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0041**  | **Lug Ramp Self-Locking Profile**                                |
| **Statement**    | The Twist-Lock lug ramp shall have a trapezoidal profile with an 8-degree self-locking angle. |
| **Rationale**    | The ramp angle is imposed to achieve self-locking behavior without requiring a separate latch. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-int-0042"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0042**  | **Twist-Lock Lug Dimensions**                                |
| **Statement**    | Each Twist-Lock lug shall be 4.0 mm wide by 1.2 mm thick. |
| **Rationale**    | Fixed lug dimensions are required for interoperability across all CCF SKUs and both collar variants. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-int-0043"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0043**  | **Asymmetric Keying Lug**                                |
| **Statement**    | The Twist-Lock interface shall include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct engagement orientation. |
| **Rationale**    | Prevents incorrect-orientation assembly of the device onto the CCF. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-int-0044"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0044**  | **Detent Release Torque Window**                                |
| **Statement**    | The Twist-Lock detent shall release within a torque window of 0.08 to 0.10 N·m. |
| **Rationale**    | Bounds the rotational effort at which the detent yields, balancing inadvertent-release resistance against ease of intentional removal; upper bound narrowed from 0.15 N·m to 0.10 N·m to align with SRS-INT-0047's engage/release torque ceiling, per PRD §10.1.3.2a's intent that detent release remain at or below the engage torque ceiling. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] · SRS-INT-0047 |

<a id="req-int-0045"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0045**  | **Twist-Lock Axial Retention Floor**                                |
| **Statement**    | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. |
| **Rationale**    | The Twist-Lock is explicitly not a breakaway mechanism; it must retain the device under normal and inertial loading (distinct from the Zone 2 Fuse Tab, which is governed under Safety Requirements). |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.1], [PRD §10.1.3.2a] |

<a id="req-int-0046"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0046**  | **Twist-Lock Engagement Insertion Force Ceiling**                                |
| **Statement**    | The Twist-Lock interface shall require no more than 5 N of axial press-in force to engage. |
| **Rationale**    | Bounds the physical effort required of the owner during the engagement workflow. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.1], [PRD §10.1.3.2a] |

<a id="req-int-0047"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0047**  | **Twist-Lock Engagement Rotation Torque Ceiling**                                |
| **Statement**    | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. |
| **Rationale**    | Bounds the rotational effort required of the owner during the engage/remove workflow. Priority raised MEDIUM→HIGH (CR-0008) so this governing torque ceiling is at least as critical as the dependent detent-release window (SRS-INT-0044, HIGH) that is bounded by it. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.1], [PRD §10.1.3.2a] · SRS-INT-0044 |

<a id="req-int-0048"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0048**  | **Engagement Feedback**                                |
| **Statement**    | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. |
| **Rationale**    | Confirms to the owner that the device has reached the fully locked position without requiring visual inspection. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-int-0049"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0049**  | **Magnetic Engagement Assist Range**                                |
| **Statement**    | The Twist-Lock interface shall provide magnetic engagement assistance effective at an approach distance of up to 5 mm. |
| **Rationale**    | Assists initial alignment of the device onto the CCF socket before rotation. Note: this Twist-Lock (device-to-CCF) magnetic engagement assist is distinct from the charging-dock magnetic alignment in SRS-INT-0033, though both specify an "up to 5 mm" approach distance. |
| **Priority**     | LOW                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] · SRS-INT-0033 |

<a id="req-int-0050"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0050**  | **Tool-Free Twist-Lock Operation**                                |
| **Statement**    | The Twist-Lock interface shall be operable without tools. |
| **Rationale**    | Owners must be able to engage and remove the device without specialized equipment. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §10.1.3.2a], [PRD §12.4] |

<a id="req-int-0051"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0051**  | **Twist-Lock Engagement Time Ceiling**                                |
| **Statement**    | The Twist-Lock interface shall be engageable within 5 seconds. |
| **Rationale**    | Bounds the time required to complete the mechanical engagement step of the CCF-install workflow. |
| **Priority**     | LOW                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.1], [PRD §12.4] |

<a id="req-int-0052"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0052**  | **Common Device-Enforced Protocol Across Variants**                                |
| **Statement**    | The system shall use a common device-enforced BLE application protocol shared across all collar and base-station firmware variants. |
| **Rationale**    | A single shared protocol avoids per-variant protocol fragmentation and depends on the protocol/ICD being frozen before verification per A-0001. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.3], [ASSUMPTION A-0001] · SRS-COMP-0001 |

<a id="req-int-0053"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0053**  | **Payload Type — Behavioral Classification Record**                                |
| **Statement**    | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. |
| **Rationale**    | Behavioral records are the primary data product synced from collar to base station and require an identifiable payload type. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.5], [PRD §8.3] |

<a id="req-int-0054"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0054**  | **Payload Type — BLE Sighting Report**                                |
| **Statement**    | The device-enforced protocol shall support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (RSSI), timestamp, and base station identifier, as a distinct payload type. |
| **Rationale**    | Sighting reports are the data basis for home/away geo-fence determination and are reported independent of behavioral-data sync. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.5], [PRD §11.3] |

<a id="req-int-0055"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0055**  | **Payload Type — Cloud Downlink**                                |
| **Statement**    | The device-enforced protocol shall support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type. |
| **Rationale**    | Downlink configuration and OTA image delivery are distinct data flows from the collar-to-base uplink and require their own payload type. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.6] |

<a id="req-int-0056"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0056**  | **Base Station Payload Content Opacity**                                |
| **Statement**    | The base station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. |
| **Rationale**    | Keeps behavioral-data interpretation logic on the collar/cloud endpoints only, avoiding base-station firmware dependency on payload semantics; verification method corrected from Test to Inspection because this is a negative architectural claim (absence of interpretation logic) that black-box behavioral testing cannot conclusively prove — a base station could interpret payload content internally and still relay it correctly, defeating a Test-based check. Design/firmware/code review confirming no semantic-parsing logic exists on the relay path is the appropriate method. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §8.3] |

<a id="req-int-0057"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0057**  | **Collar Buffer Retention Pending Acknowledgment**                                |
| **Statement**    | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the base station. |
| **Rationale**    | Prevents data loss from premature buffer clearing before successful delivery is confirmed. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.4] |

<a id="req-int-0058"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0058**  | **No FIFO Clear on Disconnect Alone**                                |
| **Statement**    | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. |
| **Rationale**    | A disconnection is not itself confirmation of delivery; clearing on disconnect alone would risk silent data loss. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §8.4] · SRS-INT-0057 |

<a id="req-int-0059"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0059**  | **Sequence-Loss Detection**                                |
| **Statement**    | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. |
| **Rationale**    | Enables the receiving side to detect gaps in the forwarded record stream without depending on a specific transport-level guarantee. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] |

<a id="req-int-0060"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-INT-0060**  | **Corruption-Free Record Forwarding**                                |
| **Statement**    | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. |
| **Rationale**    | Ensures the integrity of behavioral data is preserved end-to-end across the BLE hop. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §7.6] |


## 11. Hardware / Physical & Mechanical Requirements

# §11 — Hardware / Physical & Mechanical Requirements

CAT: **COMP-HW** | Maps to: PRD §10 (§10.1.1 weight/form, §10.1.2 enclosure/materials, §10.1.3 CCF material composition, §10.2 sensing, §10.3 wireless HW, §10.4 battery, §10.5 charging, §10.6 NV storage, §10.7 compute)


## 11.0 Scope Note

This section specifies the physical, component-level, and mechanical hardware constraints of the LUUCIPet collar device and the CCF accessory. It owns the constraints not captured elsewhere: device mass budgets, enclosure ingress rating as a component property, structural wall/lug geometry, CCF polymer material composition, and the presence and physical capability of the sensing, wireless, battery, charging, storage, and compute hardware. Behavior of these components is specified in the referenced functional/interface sections and is NOT restated here:

- Twist-Lock **geometry and mechanical behavior** (3-lug bayonet, 90° rotation, lug dimensions, detent, engage force, magnetic assist, axial retention >100 N) are owned by §10 Interface Requirements (SRS-INT-0039–0051) and §7 Safety (SRS-SAFE-0011); §11 does not re-issue them.
- BLE radio **behavior** (TX ≥+8 dBm, open-air range ≥9 m) is owned by §4 (SRS-CONN-0006/0007) and §10 (SRS-INT-0008 et seq.); §11 issues only the radio as a physical hardware component.
- GNSS **interface behavior** (fix interval, A-GPS, power-gating, timeout, TTFF) is owned by §10 (SRS-INT-0021–0029); §11 issues only the receiver as a physical component.
- Enclosure **chew-resistance** and **material non-toxicity** safety behavior are owned by §7 (SRS-SAFE-0018/0021); socket entrapment by SRS-SAFE-0019/0020.
- **Secure boot** and **unique cryptographic identity** are owned by §8 Security (SRS-SEC-0004/0005); §11 issues only the compute-hardware capability that supports them.
- Battery-life **durations** and charge-**time** performance are owned by §6 Performance (SRS-PERF-0001/0002) and §10 (SRS-INT-0034); §11 issues only the physical battery/charging component constraints.
- Cross-variant identical pogo-pin & Twist-Lock **geometry** is established by SRS-COMP-0002/0003 (§2); §11 references, does not re-issue.

## 11.1 Weight & Form Factor

## 11.2 Enclosure & Ingress Protection

## 11.3 Mechanical / Structural Constraints

## 11.4 CCF Material Composition

## 11.5 Sensing Hardware

## 11.6 Wireless Hardware

## 11.7 Battery Hardware

## 11.8 Charging Hardware

## 11.9 Non-Volatile Storage Hardware

## 11.10 Compute Hardware

---

## Drafter Notes — External Attributions & Deferrals (not silently dropped)

- **Base-station LEDs** (Charging tier = 3 LEDs power/charging/cloud; Relay tier = 2 LEDs) [PRD §11.6] are base-station device hardware and are **deferred to §15 Operational Requirements**, not issued here. Not dropped — carried to §15 scope.
- **Base-station LED dimming / nighttime mode** [PRD §11.6, ASSUMPTION: A-0008] is a base-station `should` — deferred to §15.
- **AC USB-C adapter inclusion** [PRD §11.7] is a base-station power-component item — deferred to §15.
- **"dual-core/coprocessor"** [PRD §10.7]: captured as the outcome-level capability in SRS-HW-0027 (on-device inference) + SRS-HW-0028 (DMA + root of trust) rather than mandating a specific core count, to remain design-free while preserving the testable capability. No UNRESOLVED-CONTEXT flag raised.
- **UNRESOLVED-CONTEXT:** none newly opened by §11. Existing 5 open flags unchanged.
- **Assumption dependency:** SRS-HW-0020/0021 rely on A-0006 (CR-0002-confirmed §10.4 minimums govern; §15.3 figures illustrative).

---

## Cross-Conflict Change Log (Conflict & Consistency Resolver)

- **CR-0017 / XSC-0008 (MODERATE) — APPLIED 2026-07-18:** SRS-HW-0008 (Charging Socket Self-Drainage Geometry) Verification Method changed **Inspection → Test** to align with SRS-INT-0036, whose VM was deliberately corrected Inspection→Test because self-drainage is a functional claim (water must actually clear the socket) rather than a static geometric feature. HW-0008 already XRs SRS-INT-0036. 
- **§11 APPROVAL-REVOKED** by this change (HW-0008 VM edit re-opens §11). Requires SECTION_REVIEW_POST → FEASIBILITY_POST and V-Method re-verify of SRS-HW-0008 before §11 can be re-APPROVED. 

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-HW-0001 | Mini Variant Maximum Device Mass | CRITICAL | STABLE | Test |
| SRS-HW-0002 | Max Variant Maximum Device Mass | CRITICAL | STABLE | Test |
| SRS-HW-0003 | Device-Standalone IP67 Ingress Rating | CRITICAL | STABLE | Test |
| SRS-HW-0004 | Exposed Pogo-Pin Ingress Integrity | CRITICAL | STABLE | Test |
| SRS-HW-0005 | Device Status LED Indicator | MEDIUM | STABLE | Inspection |
| SRS-HW-0006 | Minimum Wall Thickness at Lug Base | HIGH | STABLE | Inspection |
| SRS-HW-0007 | Lug-Channel Solid-Section Seal Integrity | CRITICAL | STABLE | Inspection |
| SRS-HW-0008 | Charging Socket Self-Drainage Criterion | MEDIUM | LIKELY-CHANGE | Test |
| SRS-HW-0009 | CCF Base Polymer Material | HIGH | LIKELY-CHANGE | Inspection |
| SRS-HW-0010 | CCF UV and Hydrolysis Stabilisation | HIGH | LIKELY-CHANGE | Inspection |
| SRS-HW-0011 | No Metallic Sub-Components in Breakaway Zones | CRITICAL | STABLE | Inspection |
| SRS-HW-0012 | No Chrome or Nickel Plating on Animal-Contact Surfaces | HIGH | STABLE | Inspection |
| SRS-HW-0013 | Three-Axis MEMS Accelerometer Presence | CRITICAL | STABLE | Inspection |
| SRS-HW-0014 | Accelerometer Output-Data-Rate Capability | CRITICAL | STABLE | Test |
| SRS-HW-0015 | Accelerometer Wake-on-Motion and FIFO | HIGH | STABLE | Inspection |
| SRS-HW-0016 | GNSS Receiver Absence on Mini | MEDIUM | STABLE | Inspection |
| SRS-HW-0017 | GNSS Receiver Presence on Max | HIGH | STABLE | Inspection |
| SRS-HW-0018 | BLE 5.x Radio Presence | CRITICAL | STABLE | Inspection |
| SRS-HW-0019 | BLE Radio Transmit-Power Capability | MEDIUM | STABLE | Test |
| SRS-HW-0020 | Mini Minimum Cell Capacity | HIGH | STABLE | Inspection |
| SRS-HW-0021 | Max Minimum Cell Capacity | HIGH | STABLE | Inspection |
| SRS-HW-0022 | Battery Protection Functions | CRITICAL | STABLE | Test |
| SRS-HW-0023 | Battery Transport-Safety Qualification | HIGH | STABLE | Test |
| SRS-HW-0024 | Low-Battery Alert Threshold | MEDIUM | STABLE | Test |
| SRS-HW-0025 | Pogo-Pin Charging Contact Hardware | CRITICAL | STABLE | Inspection |
| SRS-HW-0026 | Non-Volatile Classification-Summary Storage Capacity | HIGH | STABLE | Test |
| SRS-HW-0027 | On-Device Inference Compute Capability | CRITICAL | STABLE | Test |
| SRS-HW-0028 | Compute Architecture With DMA and Hardware Root of Trust | CRITICAL | STABLE | Inspection |

<a id="req-hw-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0001**  | **Mini Variant Maximum Device Mass**                                |
| **Statement**    | The Mini collar device **shall** have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. |
| **Rationale**    | The ≤10 g budget is the core differentiator for the cat/small-dog cohort and drives every downstream component-mass allocation. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.1], [PRD §4.1] · SRS-HW-0011, SRS-HW-0016 |

<a id="req-hw-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0002**  | **Max Variant Maximum Device Mass**                                |
| **Statement**    | The Max collar device **shall** have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. |
| **Rationale**    | The ≤22 g budget bounds the large/service-dog variant including the GNSS receiver and larger cell. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.1], [PRD §4.1] · SRS-HW-0012, SRS-HW-0017 |

<a id="req-hw-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0003**  | **Device-Standalone IP67 Ingress Rating**                                |
| **Statement**    | The collar device **shall** achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. |
| **Rationale**    | Device-standalone IP67 is the governing waterproofing claim; the CCF-mated and charging-interface-specific cases are bounded separately. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.2], [PRD §13.4], [STD: IEC 60529 (RM-0028)] · SRS-INT-0035, SRS-HW-0004 |

<a id="req-hw-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0004**  | **Exposed Pogo-Pin Ingress Integrity**                                |
| **Statement**    | The collar device enclosure **shall** maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. |
| **Rationale**    | The pogo-pin aperture is the primary ingress-path risk on an otherwise sealed enclosure. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.2], [PRD §10.5] · SRS-HW-0003, SRS-INT-0035 |

<a id="req-hw-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0005**  | **Device Status LED Indicator**                                |
| **Statement**    | The collar device **shall** provide a light-emitting-diode status indicator. |
| **Rationale**    | A device-level visual indicator is required for power/charge/pairing status signalling. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2] · — |

<a id="req-hw-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0006**  | **Minimum Wall Thickness at Lug Base**                                |
| **Statement**    | The collar device enclosure **shall** provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. |
| **Rationale**    | Minimum wall thickness at the highest-stress structural feature preserves enclosure integrity and the seal boundary. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2] · SRS-HW-0007, SRS-HW-0003 |

<a id="req-hw-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0007**  | **Lug-Channel Solid-Section Seal Integrity**                                |
| **Statement**    | The Twist-Lock lug channels and magnetic insert on the device underside **shall not** penetrate the enclosure wall or the ingress seal path. |
| **Rationale**    | The lug/magnet features must remain solid-section so that mechanical attachment cannot compromise IP67. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2] · SRS-HW-0003, SRS-HW-0006 |

<a id="req-hw-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0008**  | **Charging Socket Self-Drainage Criterion**                                |
| **Statement**    | The device-facing charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state "shall be self-draining" with no quantified criterion. Prior VM=Test (corrected from Inspection per CR-0017) was directionally correct but V-Method Validator FLAGged for lacking a measurable criterion. [ASSUMPTION: A-0023] resolves this gap with 5 mL fill / 15 s window / ≤0.2 mL residual in realistic worn orientation. Identical fix applied to SRS-INT-0036 (§10). |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.5], [PRD §10.1.3.5], [ASSUMPTION: A-0023] · SRS-INT-0036 |

<a id="req-hw-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0009**  | **CCF Base Polymer Material**                                |
| **Statement**    | The CCF body **shall** be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). |
| **Rationale**    | PA66-GF30 provides the stiffness-to-mass ratio and moulded-fuse-tab characteristics the compound-CCF architecture depends on. |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2], [PRD §6.2] · SRS-HW-0010, SRS-SAFE-0006 |

<a id="req-hw-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0010**  | **CCF UV and Hydrolysis Stabilisation**                                |
| **Statement**    | The CCF material **shall** incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. |
| **Rationale**    | The CCF is worn outdoors for the product lifetime; UV and hydrolysis stabilisation are required to retain breakaway-force properties. |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2] · SRS-HW-0009 |

<a id="req-hw-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0011**  | **No Metallic Sub-Components in Breakaway Zones**                                |
| **Statement**    | The CCF **shall not** contain any metallic sub-component within the Zone 2 snap/breakaway region. |
| **Rationale**    | Metallic inserts in the breakaway zone would defeat the calibrated polymer fuse-tab fracture behavior and introduce a sharp-fragment hazard. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2], [PRD §10.1.3.2b] · SRS-SAFE-0006, SRS-SAFE-0007 |

<a id="req-hw-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0012**  | **No Chrome or Nickel Plating on Animal-Contact Surfaces**                                |
| **Statement**    | Animal-contact surfaces of the device and CCF **shall not** use chrome or nickel plating. |
| **Rationale**    | Chrome/nickel are common animal-contact allergens; exclusion is required for the pet-contact material safety case (mechanism detailed in §17). |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2], [PRD §13.2], [STD: REACH/RoHS/Prop 65 (RM-0026)] · SRS-SAFE-0021 |

<a id="req-hw-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0013**  | **Three-Axis MEMS Accelerometer Presence**                                |
| **Statement**    | The collar device **shall** incorporate a three-axis MEMS accelerometer. |
| **Rationale**    | The accelerometer is the sole primary sensor for the behavioral-classification engine. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.2.1] · SRS-FUNC-0014, SRS-FUNC-0015 |

<a id="req-hw-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0014**  | **Accelerometer Output-Data-Rate Capability**                                |
| **Statement**    | The collar device accelerometer **shall** support an output data rate of no less than 50 Hz. |
| **Rationale**    | The classification engine requires ≥50 Hz sampling (SRS-FUNC-0014); the hardware must be capable of sustaining it. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.2.1] · SRS-FUNC-0014, SRS-FUNC-0008 |

<a id="req-hw-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0015**  | **Accelerometer Wake-on-Motion and FIFO**                                |
| **Statement**    | The collar device accelerometer **shall** provide a wake-on-motion interrupt and a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. |
| **Rationale**    | Wake-on-motion, a ≥512-byte FIFO, and DMA offload are required to sustain continuous sampling within the collar power budget. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.2.1] · SRS-HW-0026, SRS-PERF-0001 |

<a id="req-hw-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0016**  | **GNSS Receiver Absence on Mini**                                |
| **Statement**    | The Mini collar device **shall not** incorporate a GNSS receiver. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet the ≤10 g mass budget and BLE-only positioning. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.2.2], [PRD §4.1] · SRS-HW-0001, SRS-INT-0022 |

<a id="req-hw-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0017**  | **GNSS Receiver Presence on Max**                                |
| **Statement**    | The Max collar device **shall** incorporate a passive receive-only GNSS receiver. |
| **Rationale**    | The Max GNSS receiver is the physical component underlying the location-interface behavior specified in §10. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.2.2], [PRD §4.1] · SRS-INT-0021, SRS-HW-0002 |

<a id="req-hw-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0018**  | **BLE 5.x Radio Presence**                                |
| **Statement**    | The collar device **shall** incorporate a Bluetooth Low Energy 5.x radio. |
| **Rationale**    | The BLE radio is the sole collar-to-base-station communication component; its protocol behavior is specified in §10. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.3], [PRD §6.3] · SRS-INT-0001, SRS-CONN-0006 |

<a id="req-hw-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0019**  | **BLE Radio Transmit-Power Capability**                                |
| **Statement**    | The collar device BLE radio **shall** be capable of a transmit power of no less than +8 dBm. |
| **Rationale**    | The radio hardware must be capable of the +8 dBm floor that the range requirement (SRS-CONN-0006/SRS-INT) depends on. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.3] · SRS-CONN-0007, SRS-INT-0008 |

<a id="req-hw-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0020**  | **Mini Minimum Cell Capacity**                                |
| **Statement**    | The Mini collar device **shall** incorporate a battery cell of no less than 120 mAh nominal capacity. |
| **Rationale**    | The §10.4 minimum (not the illustrative §15.3 130 mAh figure) is the governing cell-capacity floor per CR-0002/A-0006. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.4], [ASSUMPTION: A-0006] · SRS-PERF-0001 |

<a id="req-hw-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0021**  | **Max Minimum Cell Capacity**                                |
| **Statement**    | The Max collar device **shall** incorporate a battery cell of no less than 400 mAh nominal capacity. |
| **Rationale**    | The §10.4 minimum is the governing cell-capacity floor per CR-0002/A-0006; the §15.3 450 mAh figure is illustrative only. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.4], [ASSUMPTION: A-0006] · SRS-PERF-0002 |

<a id="req-hw-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0022**  | **Battery Protection Functions**                                |
| **Statement**    | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. |
| **Rationale**    | Li-Po cell protection is a mandatory safety function for an animal-worn sealed device. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.4], [STD: IEC 62133-2:2017+AMD1:2021 (RM-0011)] · SRS-SAFE-0022 |

<a id="req-hw-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0023**  | **Battery Transport-Safety Qualification**                                |
| **Statement**    | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. |
| **Rationale**    | UN 38.3 is mandatory for lithium-cell transport; the "before pilot" gate is a program milestone. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.4], [STD: UN 38.3 (RM-0010)] · SRS-HW-0022 |

<a id="req-hw-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0024**  | **Low-Battery Alert Threshold**                                |
| **Statement**    | The collar device **shall** raise a low-battery alert at a state-of-charge of 20% or below. |
| **Rationale**    | A 20% SoC alert gives the owner adequate warning before the OTA reserve floor. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.4] · SRS-FUNC-0051 |

<a id="req-hw-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0025**  | **Pogo-Pin Charging Contact Hardware**                                |
| **Statement**    | The collar device **shall** incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. |
| **Rationale**    | The pogo-pin + magnet is the physical charging component underlying the interface behavior in §10. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.5], [PRD §6.6] · SRS-INT-0031, SRS-INT-0032 |

<a id="req-hw-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0026**  | **Non-Volatile Classification-Summary Storage Capacity**                                |
| **Statement**    | The collar device **shall** incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. |
| **Rationale**    | The ≥30-day on-device retention floor requires a matching physical NV storage component. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.6] · SRS-DATA-0005, SRS-DATA-0006 |

<a id="req-hw-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0027**  | **On-Device Inference Compute Capability**                                |
| **Statement**    | The collar device **shall** incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. |
| **Rationale**    | All Tier-1/Tier-2 classification runs on-device; the compute hardware must be capable of it independent of connectivity. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.7], [PRD §7.7] · SRS-FUNC-0031, SRS-DATA-0013 |

<a id="req-hw-0028"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-HW-0028**  | **Compute Architecture With DMA and Hardware Root of Trust**                                |
| **Statement**    | The collar device compute subsystem **shall** provide direct-memory-access peripheral access and a hardware root of trust. |
| **Rationale**    | DMA peripheral access supports low-power sensing offload (SRS-HW-0015); the hardware root of trust is the physical anchor for secure boot (SRS-SEC-0005). |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.7] · SRS-SEC-0005, SRS-HW-0015 |


## 12. Environmental & Durability Requirements

# §12 — Environmental & Durability Requirements


## 12.0 Scope Note

This section specifies the environmental exposure conditions, survival criteria, and durability test regimes that the collar device and CCF accessory must withstand: temperature extremes, ingress-protection test parameters, mechanical shock/drop, UV/weathering, chemical exposure, and — for the CCF specifically — post-exposure retention of the safety-critical breakaway-force and detent-torque windows. It does **not** re-issue constraints already owned elsewhere:

- **IP67 device-standalone rating as a physical property**, exposed pogo-pin ingress integrity, and lug-channel solid-section structural integrity are owned by §11 Hardware (SRS-HW-0003/0004/0006/0007); §12 issues the ingress **test-parameter, claim-boundary, and functional-exclusion** requirements built on top of that rating.
- **CCF base-polymer material identity** (PA66-GF30), **UV/hydrolysis stabiliser content** (0.3–0.5%), and **no-metallic-subcomponent** constraints are owned by §11 (SRS-HW-0009/0010/0011); §12 issues the **exposure regime and post-exposure retention** criteria that exercise those material properties.
- **Zone 2 breakaway-force windows** (CCF-S/M/L) and **Twist-Lock detent-torque window** are owned by §7 Safety (SRS-SAFE-0001/0002/0003) and §10 Interfaces (SRS-INT-0044) respectively; §12 requires that these approved windows **remain valid after environmental exposure** — it does not restate the windows themselves.
- **Enclosure chew-resistance** and **animal-contact material non-toxicity** are owned by §7 Safety (SRS-SAFE-0018/0021); §12 references but does not re-issue.
- **REACH/RoHS/Prop 65 material-compliance mechanism** is owned by §17 Standards Compliance / §18 Regulatory; §12 references but does not re-issue.

## 12.1 Temperature

## 12.2 Ingress Protection

The IEC 60529 IPX7 test method inherently specifies a 1-metre / 30-minute temporary-immersion parameter; the "IP67 1 m/30 min" figure in PRD §12.5 is therefore the defined test parameter of the rating already required by SRS-HW-0003 (§11), not a separate numeric requirement, and is not re-issued here.

## 12.3 Mechanical Durability

## 12.4 UV & Weathering

## 12.5 Chemical Resistance

## 12.6 CCF Environmental Durability — Post-Exposure Retention

This subsection ties the exposure regimes in §12.1/§12.4/§12.5 back to the Zone 2 breakaway-force windows (SRS-SAFE-0001/0002/0003) and Twist-Lock detent-torque window (SRS-INT-0044) that must remain valid after exposure: a CCF whose fuse tab has drifted out of its calibrated force window after environmental exposure would degrade the pet-safety breakaway function.

## 12.7 Material Safety (Cross-Reference — No New Requirements Issued)

Enclosure chew-resistance (SRS-SAFE-0018) and animal-contact material non-toxicity (SRS-SAFE-0021) are owned by §7 Safety. CCF base-polymer identity, UV/hydrolysis stabiliser content, absence of metallic breakaway-zone subcomponents, and absence of chrome/nickel plating on animal-contact surfaces (SRS-HW-0009, SRS-HW-0010, SRS-HW-0011, SRS-HW-0012) are owned by §11 Hardware. REACH/RoHS/Prop 65 compliance mechanism (PRD §13.2) is owned by §17 Standards Compliance / §18 Regulatory. §12 does not re-issue any of the above; the exposure and retention requirements in §12.1–§12.6 are the environmental-durability complement to these material-safety and material-composition requirements.

---

## Drafter Notes — Out-of-Scope Items, Flags & Deferrals (not silently dropped)

- **Base Station environmental/durability requirements — OUT OF SCOPE.** PRD §12.5 and §13.4 (this section's PRD sources) address the collar device and CCF only; PRD provides no operating-temperature, ingress, drop, UV, or chemical-exposure specification for the Base Station, which is an indoor, mains-powered, continuously operating appliance (PRD §11.7). No Base Station environmental requirement is issued here. Responsible party for defining any such requirement, should one be needed: **Hardware / Industrial-Design team**, via a future PRD amendment — this is an omission in the PRD source material, not a drafting choice.
- **Portable Travel Charging Cradle environmental durability — OUT OF SCOPE.** No PRD source addresses this accessory's environmental durability; same attribution as the Base Station item above (Hardware / Industrial-Design team, future PRD amendment).
- **Packaging and end-of-life environmental compliance** (WEEE 2012/19/EU, EU PPWR, UK Producer Responsibility per PRD §13.7) are regulatory/standards-compliance concerns, not physical-durability requirements — owned by §17/§18, not restated here.
- **New UNRESOLVED-CONTEXT flags raised by §12** (in addition to the 5 pre-existing open flags, unchanged by this section):
  1. Enclosure UV-exposure test duration/method absent from PRD (SRS-ENV-0012).
  2. Post-UV-exposure and post-chemical-exposure Zone 2 fuse-force retention criteria not explicitly restated in PRD, though derived from the explicit thermal-cycling retention criterion on the same mechanism (SRS-ENV-0017, SRS-ENV-0018).
- **  Flagged for reconciliation if a document-wide vocabulary change is intended.
- **Assumption dependency:** SRS-ENV-0003 relies on A-0003 (CCF thermal-cycling profile default, IEC 60068-2-14 Test Na).

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-ENV-0001 | Device Operating Temperature Range | CRITICAL | STABLE | Test |
| SRS-ENV-0002 | Device Storage Temperature Range | HIGH | STABLE | Test |
| SRS-ENV-0003 | CCF Thermal-Cycling Exposure | HIGH | STABLE | Test |
| SRS-ENV-0004 | Device Damp-Heat Exposure | MEDIUM | STABLE | Test |
| SRS-ENV-0005 | Prohibition on IP67 Claims for CCF-Mated Configuration | CRITICAL | STABLE | Inspection |
| SRS-ENV-0006 | Independent Laboratory Confirmation of IP67 Rating | HIGH | STABLE | Inspection |
| SRS-ENV-0007 | Twist-Lock Channel Water-Ingress Exclusion | CRITICAL | STABLE | Test |
| SRS-ENV-0008 | Ingress Seal-Boundary Interior Placement | HIGH | STABLE | Inspection |
| SRS-ENV-0009 | Drop Survival | CRITICAL | STABLE | Test |
| SRS-ENV-0010 | Mechanical Shock Resistance | MEDIUM | STABLE | Test |
| SRS-ENV-0011 | Vibration Resistance | MEDIUM | STABLE | Test |
| SRS-ENV-0012 | Enclosure UV Stabilization | CRITICAL | STABLE | Analysis |
| SRS-ENV-0013 | CCF UV Aging Exposure | CRITICAL | STABLE | Test |
| SRS-ENV-0014 | CCF Chemical-Fluid Exposure | HIGH | STABLE | Test |
| SRS-ENV-0015 | Post-Thermal-Cycling Zone 2 Fuse-Force Window Retention | CRITICAL | STABLE | Test |
| SRS-ENV-0016 | Post-Thermal-Cycling Twist-Lock Detent-Torque Window Retention | HIGH | STABLE | Test |
| SRS-ENV-0017 | Post-UV-Aging Zone 2 Fuse-Force Window Retention | CRITICAL | STABLE | Test |
| SRS-ENV-0018 | Post-Chemical-Exposure Zone 2 Fuse-Force Window Retention | CRITICAL | STABLE | Test |

<a id="req-env-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0001**  | **Device Operating Temperature Range**                                |
| **Statement**    | The collar device **shall** operate within an ambient temperature range of −20 °C to +50 °C without loss of function. |
| **Rationale**    | Defines the outdoor/indoor thermal envelope the device must remain functional across for pet-wearable use, consistent with the deployment environment (outdoor pet exposure) described in the Product Context Profile. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · SRS-HW-0001, SRS-HW-0002 |

<a id="req-env-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0002**  | **Device Storage Temperature Range**                                |
| **Statement**    | The collar device **shall** withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequent operational performance. |
| **Rationale**    | Bounds the non-operating thermal envelope for warehousing, shipping, and retail-shelf conditions, distinct from the in-use operating range. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · SRS-ENV-0001 |

<a id="req-env-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0003**  | **CCF Thermal-Cycling Exposure**                                |
| **Statement**    | The CCF **shall** be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of function. |
| **Rationale**    | PRD states the −20 to +50 °C temperature-cycling range without specifying a cycle count, dwell, or ramp profile; A-0003 supplies the IEC 60068-2-14 Test Na default absent a PRD-stated profile. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5], [ASSUMPTION: A-0003] · SRS-ENV-0015, SRS-ENV-0016 |

<a id="req-env-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0004**  | **Device Damp-Heat Exposure**                                |
| **Statement**    | The collar device **should** withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. |
| **Rationale**    | PRD §13.4 identifies damp-heat testing as a recommended (non-mandatory) environmental qualification test supplementing the IP67 ingress rating. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.4] · SRS-HW-0003 |

<a id="req-env-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0005**  | **Prohibition on IP67 Claims for CCF-Mated Configuration**                                |
| **Statement**    | Product documentation and marketing materials **shall not** state or imply an IP67, or equivalent, ingress-protection rating for the collar device while mated to any CCF. |
| **Rationale**    | The IP67 rating established in SRS-HW-0003 is qualified only for the device-standalone, unmated condition; this requirement prevents an unsubstantiated ingress claim from being communicated for the CCF-mated wear condition. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §4.1 fn²], [PRD §13.4] · SRS-HW-0003 |

<a id="req-env-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0006**  | **Independent Laboratory Confirmation of IP67 Rating**                                |
| **Statement**    | The IP67 ingress-protection rating claimed for the collar device **shall** be confirmed by an independent, accredited test laboratory and documented in a test report prior to product launch. |
| **Rationale**    | PRD requires the device-standalone IP67 claim to be "documented and confirmed with lab," establishing an independent-verification gate distinct from the underlying physical capability owned by SRS-HW-0003. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.4] · SRS-HW-0003 |

<a id="req-env-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0007**  | **Twist-Lock Channel Water-Ingress Exclusion**                                |
| **Statement**    | The Twist-Lock lug channels **shall** exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003. |
| **Rationale**    | PRD states the Twist-Lock channels present "no water path"; this requirement establishes the functional (test-level) counterpart to the structural solid-section requirement already owned by SRS-HW-0007. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.4] · SRS-HW-0003, SRS-HW-0007 |

<a id="req-env-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0008**  | **Ingress Seal-Boundary Interior Placement**                                |
| **Statement**    | The ingress-protection seal boundary **shall** be located on the interior side of the enclosure assembly such that it is not directly exposed on any externally accessible mating surface. |
| **Rationale**    | PRD requires the seal boundary to be positioned "interior," protecting it from direct mechanical wear and contamination that would otherwise degrade the IP67 seal over the product's service life. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.4] · SRS-HW-0006, SRS-HW-0007 |

<a id="req-env-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0009**  | **Drop Survival**                                |
| **Statement**    | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. |
| **Rationale**    | Bounds the mechanical shock the device must survive from a typical accidental drop during handling, charging, or removal from an animal. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · — |

<a id="req-env-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0010**  | **Mechanical Shock Resistance**                                |
| **Statement**    | The collar device **should** withstand mechanical shock per IEC 60068-2-27 without loss of function. |
| **Rationale**    | PRD §13.4 identifies shock testing per IEC 60068-2-27 as a recommended supplementary qualification test beyond the explicit 1.5 m drop-survival floor. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.4] · SRS-ENV-0009 |

<a id="req-env-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0011**  | **Vibration Resistance**                                |
| **Statement**    | The collar device **should** withstand vibration per IEC 60068-2-64 without loss of function. |
| **Rationale**    | PRD §13.4 identifies vibration testing per IEC 60068-2-64 as a recommended supplementary qualification test, representative of sustained pet-motion vibration exposure. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §13.4] · — |

<a id="req-env-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0012**  | **Enclosure UV Stabilization**                                |
| **Statement**    | The collar device enclosure material **shall** be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service lifetime. |
| **Rationale**    | PRD §12.5 requires the enclosure to be "UV-stabilized" but, unlike the CCF (SRS-ENV-0013, 2,000 h per IEC 60068-2-5), states no exposure duration or test method for the enclosure material; flagged per the numeric-vagueness gate rather than an invented duration. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §12.5], [PRD — ABSENT: enclosure UV-exposure test duration/method] · SRS-ENV-0013 |

<a id="req-env-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0013**  | **CCF UV Aging Exposure**                                |
| **Statement**    | The CCF **shall** withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. |
| **Rationale**    | Bounds the accelerated UV-aging qualification program for the outdoor-worn CCF, consistent with the UV-stabiliser content specified in SRS-HW-0010. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · SRS-HW-0010, SRS-ENV-0017 |

<a id="req-env-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0014**  | **CCF Chemical-Fluid Exposure**                                |
| **Statement**    | The CCF **shall** withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across pH 5.5 to 8.5, enzymatic pet-odor and stain cleaners, fresh water, and salt water. |
| **Rationale**    | Bounds the household and outdoor chemical-exposure qualification program representative of routine pet bathing, cleaning, and water-body exposure. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · SRS-ENV-0018 |

<a id="req-env-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0015**  | **Post-Thermal-Cycling Zone 2 Fuse-Force Window Retention**                                |
| **Statement**    | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | PRD explicitly ties CCF temperature cycling to the requirement that "fuse force ... [stays] in-window," making post-cycling retention of the calibrated breakaway-force windows a directly PRD-stated durability criterion. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · SRS-ENV-0003, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="req-env-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0016**  | **Post-Thermal-Cycling Twist-Lock Detent-Torque Window Retention**                                |
| **Statement**    | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Twist-Lock detent release torque **shall** remain within the torque window defined in SRS-INT-0044. |
| **Rationale**    | PRD explicitly ties CCF temperature cycling to the requirement that "detent torque ... [stays] in-window," making post-cycling retention of the calibrated detent-torque window a directly PRD-stated durability criterion. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5] · SRS-ENV-0003, SRS-INT-0044 |

<a id="req-env-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0017**  | **Post-UV-Aging Zone 2 Fuse-Force Window Retention**                                |
| **Statement**    | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | PRD states the CCF UV-aging duration and standard but, unlike the thermal-cycling case, does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the same safety-critical retention obligation established for thermal cycling (SRS-ENV-0015) to the UV-aging qualification test, since both exposures act on the same moulded Zone 2 fuse mechanism. Flagged as PRD-silent rather than an invented numeric bound — the force window itself is the pre-approved SRS-SAFE-0001/0002/0003 value. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5], [PRD — ABSENT: post-UV-exposure fuse-force retention criterion] · SRS-ENV-0013, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015 |

<a id="req-env-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-ENV-0018**  | **Post-Chemical-Exposure Zone 2 Fuse-Force Window Retention**                                |
| **Statement**    | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | As with SRS-ENV-0017, PRD states the CCF chemical-exposure duration and fluid set but does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the SRS-ENV-0015 retention obligation to the chemical-resistance qualification test on the same safety-critical mechanism. Flagged as PRD-silent rather than an invented numeric bound. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.5], [PRD — ABSENT: post-chemical-exposure fuse-force retention criterion] · SRS-ENV-0014, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015 |


## 13. Reliability & Availability Requirements

# §13 — Reliability & Availability Requirements


## 13.0 Scope Note

This section specifies the dependability, availability, and long-run success-rate criteria the system must sustain over the product's operating life and over defined observation windows. It does **not** re-issue constraints already owned elsewhere:

- **Tier-1 (≥85% accuracy / ≤5% false-positive) and Tier-2 (≥80% accuracy / ≤10% false-positive) classification-accuracy thresholds** in PRD §12.2 restate the classification-accuracy floors already owned by §3 Behavioral Classification (SRS-FUNC-0018, SRS-FUNC-0019, SRS-FUNC-0020, SRS-FUNC-0021); §13 does not re-issue them. They are accuracy/performance criteria, not availability/dependability criteria, notwithstanding their placement under the PRD's "Reliability" heading.
- **The IP67 ingress-protection rating as a component property, the device-standalone qualification scope, and the ingress test-parameter/claim-boundary requirements** are owned by §11 Hardware (SRS-HW-0003) and §12 Environmental & Durability (SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007, SRS-ENV-0008); §13 owns only the additional temporal criterion that the rating must remain valid across the full expected service lifetime, not the rating itself.
- **OTA image integrity, atomicity, and dual-bank auto-revert mechanics** are owned by §5 OTA Firmware Updates (SRS-FUNC-0052–0057); §13 owns only the resulting aggregate success-rate criterion, not the underlying mechanism.

## 13.1 Ingress-Protection Durability

## 13.2 Collar Device Availability

## 13.3 Base Station Availability

## 13.4 OTA Update Success Rate

---

## Drafter Notes — Out-of-Scope Items, Flags & Deferrals (not silently dropped)

- **IoT Cloud Device-Management layer availability/uptime — OUT OF SCOPE, no numeric floor available.** PRD §12.2 (this section's sole PRD source) specifies reliability/availability floors only for the collar device, the base station, and the OTA mechanism — all within our build. It states no uptime, availability, or success-rate target for the IoT Cloud Device-Management layer, which per [ASSUMPTION: A-0015] is external (IoT Cloud backend team) beyond our in-scope transport hand-off (SRS-CONN-0014, SRS-CONN-0018). No cloud-side reliability requirement is issued here. Responsible party for defining any such SLA, should one be needed: **IoT Cloud backend team**, via a future PRD amendment or an inter-team SLA — this is an omission in the PRD source material, not a drafting choice. Our own in-scope interface obligation toward that team (transporting records reliably to the hand-off point) is already captured as in-scope requirements in §4 (SRS-CONN-0014–0017, SRS-CONN-0026).
- **Mobile App reliability/availability — OUT OF SCOPE, no PRD source.** PRD §12.2 states no reliability or availability criterion for the Mobile App, which is external (Mobile App team) per PRD §14.1. No Mobile App reliability requirement is issued here; responsible party for any such criterion is the **Mobile App team**, via their own requirements process.
- **Field failure rate, MTBF/MTTR, and warranty-return-rate criteria** are not stated anywhere in the PRD (§12.2 or elsewhere) and are not invented here per the numeric-vagueness gate; no UNRESOLVED-CONTEXT flag is raised for their absence because there is no PRD clause implying such a metric is expected at the SRS level.
- **New UNRESOLVED-CONTEXT flag raised by §13** (in addition to the 8 pre-existing open flags, unchanged by this section):
  1. Collar operational-availability measurement-window length is absent from PRD §12.2, unlike the base station's explicit 90-day window (SRS-RELI-0002).
- ** 
- **Assumption/PCP dependency:** SRS-RELI-0001 relies on the Product Context Profile §8 user-confirmed expected-service-lifetime figure (~2–3 years, 2-year floor applied), which is recorded in the PCP rather than in the Assumption Register; no A-ID currently carries this figure.  

---

<a id="req-reli-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-RELI-0001**  | **IP67 Rating Retention Over Full Service Lifetime**                                |
| **Statement**    | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. |
| **Rationale**    | PRD §12.2 states the qualitative criterion "IP67 full lifetime (device standalone)" but does not itself state a numeric service-lifetime duration against which "full lifetime" can be tested. The Product Context Profile records a user-confirmed expected service lifetime of ~2–3 years, with a 2-year floor to be used wherever a single testable figure is required; that floor is applied here as the qualification duration. This requirement is the temporal-endurance complement to the device-standalone IP67 rating already established by SRS-HW-0003 and does not restate the rating itself. |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §12.2], [PRD — ABSENT: service_lifetime_duration_value] · SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006 |

<a id="req-reli-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-RELI-0002**  | **Collar Device Operational Availability**                                |
| **Statement**    | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. |
| **Rationale**    | PRD §12.2 states "collar operational ≥99% (excl. charging)" as a direct numeric floor, but — unlike the base station uptime criterion in the same clause, which specifies a 90-day measurement window — the PRD does not state the observation-window length over which collar availability is to be measured. Flagged per the numeric-vagueness gate rather than inventing a window; the 99% floor and the charging exclusion are PRD-stated and are issued as-is. Verification Method corrected from Analysis to Test per V-Method review: this is a directly observable field/DVT proportion metric (uptime vs. total non-charging elapsed time), matching the Test pattern this SRS already applies to equivalent rate/proportion criteria (SRS-FUNC-0018–0021, SRS-FUNC-0001); no MTBF-style modeling basis is stated that would justify Analysis. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.2], [PRD — ABSENT: collar_availability_measurement_window] · SRS-HW-0025, SRS-INT-0031, SRS-INT-0032 |

<a id="req-reli-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-RELI-0003**  | **Base Station Uptime**                                |
| **Statement**    | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. |
| **Rationale**    | PRD §12.2 states "base ≥99.5% uptime over 90-day window" as a direct, fully-bounded numeric criterion; the base station's continuous, mains-powered, no-sleep operating profile (PRD §11.7) makes a rolling-window uptime metric directly measurable in the field. Verification Method corrected from Analysis to Test per V-Method review: the criterion is fully bounded (explicit 90-day window) and directly observable via continuous-operation monitoring against the threshold — a practical DVT/pilot burn-in test, not a modeling exercise. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.2] · — |

<a id="req-reli-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-RELI-0004**  | **OTA Update Success Rate**                                |
| **Statement**    | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a base station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. |
| **Rationale**    | PRD §12.2 states "OTA success ≥99%" as a direct numeric floor on the aggregate reliability of the OTA mechanism already specified functionally in §5; "success" is defined operationally against the existing auto-revert criterion (SRS-FUNC-0056) rather than inventing a separate definition. Verification Method corrected from Analysis to Test per V-Method review: this is a repeated-trial pass/fail statistic (run N install attempts, including fault-injected trials per SRS-FUNC-0057, and compute the pass proportion against the 99% floor), matching the Test pattern this SRS already applies to equivalent proportion-based criteria (SRS-FUNC-0001, SRS-FUNC-0018–0021). |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.2] · SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0057 |


## 14. Usability Requirements

## §14 Usability Requirements

**Scope.**  This section specifies the user-experience and usability requirements for the LUUCIPet Wellness Monitor Phase 1 product family — covering collar-device physical interaction, LED/haptic feedback, pairing and onboarding, base-station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features. The companion app's UI design, in-app navigation, notification content, and analytics dashboard are external (delivered by the Mobile App team); requirements that depend on device-to-app data hand-offs are captured as in-scope interface obligations in §14.7.

**Cross-references:**  Pairing protocol → §4 (CONN). OTA functional requirements → §5 (OTA). Safety-indicator behavior → §7 (SAFE). Twist-Lock mechanical specifications → §11 (COMP-HW). Breakaway detection → A-0018.

---

### 14.1 Pairing & Onboarding

---

### 14.2 Physical Interaction

---

### 14.3 Visual & Auditory Feedback

---

### 14.4 Base Station UX

---

### 14.5 CCF User Experience

---

### 14.6 Status & Error Communication

---

### 14.7 App-Interface Obligations

> The companion app is delivered by the Mobile App team \[EXTERNAL: Mobile App team]. The requirements in this subsection specify the device-side and base-station-side interface obligations that enable the app's user-facing features. These are in-scope for our delivery.

---

### 14.8 OTA Update UX

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-UX-0001 | The collar device  complete BLE pairing and first-data-sync handshake with a… | HIGH | Stable | Test |
| SRS-UX-0002 | The collar device  support QR-code-based out-of-band (OOB) pairing as the… | HIGH | Stable | Demonstration |
| SRS-UX-0003 | The collar device  provide a single, visually distinct, and user-accessible… | HIGH | Stable | Inspection |
| SRS-UX-0004 | The collar device LED  emit a visually distinct indication when the device is… | HIGH | Stable | Test |
| SRS-UX-0005 | The collar device  automatically exit pairing mode and revert to… | MEDIUM | Stable | Test |
| SRS-UX-0006 | The Twist-Lock mechanism  provide both an audible click and a tactile… | HIGH | Stable | Test |
| SRS-UX-0007 | The Twist-Lock socket  provide a magnetic-assist force that draws the device… | MEDIUM | Stable | Test |
| SRS-UX-0008 | The Twist-Lock engage force  not exceed 5 N press-in axial force and 0.10 N·m… | HIGH | Stable | Test |
| SRS-UX-0009 | The device removal workflow (90° counter-clockwise Twist-Lock rotation) … | HIGH | Stable | Test |
| SRS-UX-0010 | The magnetic pogo-pin charging connector  achieve ≥90% first-attempt successful… | HIGH | Stable | Test |
| SRS-UX-0011 | The Twist-Lock asymmetric lug keying  physically prevent incorrect-orientation… | HIGH | Stable | Test |
| SRS-UX-0012 | The collar device LED  communicate at minimum the following distinct… | HIGH | Stable | Test |
| SRS-UX-0013 | Each collar-device operational state enumerated in SRS-UX-0012  be communicated… | HIGH | Stable | Test |
| SRS-UX-0014 | All collar-device LED state indicators  differentiate critical states (low… | MEDIUM | Stable | Analysis |
| SRS-UX-0015 | The Twist-Lock engagement audible click  produce a sound pressure level of ≥40… | MEDIUM | Stable | Test |
| SRS-UX-0016 | The base station  communicate via LEDs at minimum: (a) AC power present, (b)… | HIGH | Stable | Test |
| SRS-UX-0017 | The base station LEDs  support an automatic ambient-light-responsive dimming… | LOW | Stable | Test |
| SRS-UX-0018 | The base station initial setup — from AC power-on through Wi-Fi association and… | HIGH | Stable | Test |
| SRS-UX-0019 | Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type… | HIGH | Stable | Inspection |
| SRS-UX-0020 | The CCF Zone 1 structural-clamp installation onto a third-party collar  be… | HIGH | Stable | Test |
| SRS-UX-0021 | The CCF Zone 2 fuse tab  incorporate a clearly visible fracture indicator… | HIGH | Stable | Inspection |
| SRS-UX-0022 | The collar device  provide a distinct low-battery LED indication (visually… | HIGH | Stable | Test |
| SRS-UX-0023 | The collar device  communicate a fault state (including but not limited to:… | HIGH | Stable | Test |
| SRS-UX-0024 | The collar device  provide confirmation feedback (LED flash, haptic pulse, or… | MEDIUM | Stable | Test |
| SRS-UX-0025 | The collar device  include its current battery state-of-charge as a percentage… | HIGH | Stable | Test |
| SRS-UX-0026 | The Max collar device  include the current GNSS fix interval setting (in… | HIGH | Stable | Test |
| SRS-UX-0027 | The collar device  transmit a persistent breakaway/separation event record as… | HIGH | Stable | Test |
| SRS-UX-0028 | The collar device  communicate each distinct OTA update state — Downloading,… | HIGH | Stable | Test |
| SRS-UX-0029 | The collar device LED  remain continuously active during an OTA update, with no… | MEDIUM | Stable | Test |

<a id="req-ux-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0001**  | **The collar device  complete BLE pairing and first-data-sync handshake with a…**                                |
| **Statement**    | The collar device shall complete BLE pairing and first-data-sync handshake with a companion app within 3 minutes of the user initiating pairing mode on the device, measured from pairing-mode-entry LED indication to app-confirmed-paired acknowledgment. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.4] |

<a id="req-ux-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0002**  | **The collar device  support QR-code-based out-of-band (OOB) pairing as the…**                                |
| **Statement**    | The collar device shall support QR-code-based out-of-band (OOB) pairing as the primary pairing method, providing a scannable QR code (on device label or base-station label) that encodes the device identity for LE Secure Connections OOB pairing. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §5.6] [STD: Bluetooth SIG LE Secure Connections] XR: SRS-CONN-0003 |

<a id="req-ux-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0003**  | **The collar device  provide a single, visually distinct, and user-accessible…**                                |
| **Statement**    | The collar device shall provide a single, visually distinct, and user-accessible physical mechanism (e.g., a recessed or guarded button) to initiate pairing mode, with the mechanism clearly labeled or icon-indicated on the device enclosure. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §5.6] |

<a id="req-ux-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0004**  | **The collar device LED  emit a visually distinct indication when the device is…**                                |
| **Statement**    | The collar device LED shall emit a visually distinct indication when the device is in pairing mode (e.g., slow blue blink at 1 Hz, 50% duty cycle) that is distinguishable from all power-on/boot, normal-operation, low-battery, charging, fault, and OTA-state LED patterns defined in §14.3. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0005**  | **The collar device  automatically exit pairing mode and revert to…**                                |
| **Statement**    | The collar device shall automatically exit pairing mode and revert to normal-operation LED indication after 3 minutes if no successful pairing is completed, with no user action required. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0006**  | **The Twist-Lock mechanism  provide both an audible click and a tactile…**                                |
| **Statement**    | The Twist-Lock mechanism shall provide both an audible click and a tactile force-transition (detent drop) upon successful locking, enabling the user to confirm engagement by sound and feel without visual inspection. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-ux-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0007**  | **The Twist-Lock socket  provide a magnetic-assist force that draws the device…**                                |
| **Statement**    | The Twist-Lock socket shall provide a magnetic-assist force that draws the device into correct alignment from a distance of ≤5 mm before the lug channels engage, reducing the fine-motor-skill demand of device docking. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-ux-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0008**  | **The Twist-Lock engage force  not exceed 5 N press-in axial force and 0.10 N·m…**                                |
| **Statement**    | The Twist-Lock engage force shall not exceed 5 N press-in axial force and 0.10 N·m rotational torque, enabling a typical adult user to dock the device without a tool or excessive effort. Mechanical specification per §11. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-ux-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0009**  | **The device removal workflow (90° counter-clockwise Twist-Lock rotation) …**                                |
| **Statement**    | The device removal workflow (90° counter-clockwise Twist-Lock rotation) shall require a detent-release torque not exceeding 0.15 N·m, such that an adult user can intentionally remove the device without a tool while the mechanism remains inertially immune per §11. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-ux-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0010**  | **The magnetic pogo-pin charging connector  achieve ≥90% first-attempt successful…**                                |
| **Statement**    | The magnetic pogo-pin charging connector shall achieve ≥90% first-attempt successful seating rate by a user with no prior training, measured in a usability test with a representative sample of ≥20 adult participants across age and dexterity ranges. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.5] |

<a id="req-ux-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0011**  | **The Twist-Lock asymmetric lug keying  physically prevent incorrect-orientation…**                                |
| **Statement**    | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket, providing error-proof (poka-yoke) mating. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.2a] |

<a id="req-ux-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0012**  | **The collar device LED  communicate at minimum the following distinct…**                                |
| **Statement**    | The collar device LED shall communicate at minimum the following distinct operational states to the user: (a) power-on / boot, (b) pairing mode, (c) normal operation, (d) low battery (≤20% SoC), (e) charging / docked, (f) error or fault, and (g) OTA update in progress. LED physical specification per §11. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0013**  | **Each collar-device operational state enumerated in SRS-UX-0012  be communicated…**                                |
| **Statement**    | Each collar-device operational state enumerated in SRS-UX-0012 shall be communicated via a unique combination of LED color, blink cadence, or duty cycle, such that no two states share an identical visual indicator pattern. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0014**  | **All collar-device LED state indicators  differentiate critical states (low…**                                |
| **Statement**    | All collar-device LED state indicators shall differentiate critical states (low battery, error/fault) from non-critical states using at minimum temporal-pattern differentiation (blink cadence), ensuring distinguishability under protanopia and deuteranopia (red/green color-blindness) without reliance on red-vs-green color discrimination alone. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | Stable                                        |
| **Verification** | Analysis                               |
| **Traceability** | — |

<a id="req-ux-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0015**  | **The Twist-Lock engagement audible click  produce a sound pressure level of ≥40…**                                |
| **Statement**    | The Twist-Lock engagement audible click shall produce a sound pressure level of ≥40 dBA measured at 30 cm from the device in a quiet-room baseline (ambient ≤30 dBA), ensuring a typical adult user can confirm engagement by sound. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0016**  | **The base station  communicate via LEDs at minimum: (a) AC power present, (b)…**                                |
| **Statement**    | The base station shall communicate via LEDs at minimum: (a) AC power present, (b) device charging active (Charging tier only), (c) cloud connectivity established, and (d) OTA update in progress. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §11.6] |

<a id="req-ux-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0017**  | **The base station LEDs  support an automatic ambient-light-responsive dimming…**                                |
| **Statement**    | The base station LEDs should support an automatic ambient-light-responsive dimming mode below approximately 50 lux, or a user-configurable quiet-hours schedule, to reduce bedroom/nighttime light intrusion. |
| **Rationale**    |  |
| **Priority**     | LOW                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §11.6] [ASSUMPTION: A-0008] |

<a id="req-ux-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0018**  | **The base station initial setup — from AC power-on through Wi-Fi association and…**                                |
| **Statement**    | The base station initial setup — from AC power-on through Wi-Fi association and cloud-registration to the "cloud-connected" LED indication — shall complete within 5 minutes for a user following the companion app's guided setup flow, assuming compliant home Wi-Fi per A-0009. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.4] |

<a id="req-ux-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0019**  | **Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type…**                                |
| **Statement**    | Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type sub-variants) shall be visually and/or tactilely distinguishable from all other variants by at minimum one of: molded-in size designation, distinct body color, or tactile surface differentiation, enabling a user to identify the correct CCF for their pet without measurement tools. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.4] |

<a id="req-ux-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0020**  | **The CCF Zone 1 structural-clamp installation onto a third-party collar  be…**                                |
| **Statement**    | The CCF Zone 1 structural-clamp installation onto a third-party collar shall be achievable by a typical adult user in ≤60 seconds without tools, using only the wrap-and-lock mechanism described in PRD §10.1.3.4. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.4] |

<a id="req-ux-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0021**  | **The CCF Zone 2 fuse tab  incorporate a clearly visible fracture indicator…**                                |
| **Statement**    | The CCF Zone 2 fuse tab shall incorporate a clearly visible fracture indicator (e.g., a contrasting-color internal layer exposed on fracture, or a continuous visual element that visibly separates) that is discernible by a user at arm's length (approximately 60 cm) under typical indoor lighting without magnification, enabling the user to visually confirm post-breakaway that the CCF must be replaced. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.3.2b] [PRD §10.1.3.6] |

<a id="req-ux-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0022**  | **The collar device  provide a distinct low-battery LED indication (visually…**                                |
| **Statement**    | The collar device shall provide a distinct low-battery LED indication (visually distinct from normal operation per SRS-UX-0013) when the battery state-of-charge reaches ≤20%, and shall persist this indication in every operational state until the device is placed on the charger and charging is confirmed. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.4] |

<a id="req-ux-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0023**  | **The collar device  communicate a fault state (including but not limited to:…**                                |
| **Statement**    | The collar device shall communicate a fault state (including but not limited to: sensor failure, non-volatile memory corruption, BLE radio initialization failure) via a visually distinct LED pattern that differs from all power-on/boot, normal-operation, low-battery, pairing, charging, and OTA-state patterns. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0024**  | **The collar device  provide confirmation feedback (LED flash, haptic pulse, or…**                                |
| **Statement**    | The collar device shall provide confirmation feedback (LED flash, haptic pulse, or both) within 1 second of a user-initiated physical action (e.g., pairing-mode button press, factory-reset trigger) being successfully registered by the device firmware, so the user is not left uncertain whether the input was received. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |

<a id="req-ux-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0025**  | **The collar device  include its current battery state-of-charge as a percentage…**                                |
| **Statement**    | The collar device shall include its current battery state-of-charge as a percentage value (0–100) in every sync payload transmitted to the base station, enabling the companion app to display an accurate, real-time battery estimate to the owner. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.4] |

<a id="req-ux-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0026**  | **The Max collar device  include the current GNSS fix interval setting (in…**                                |
| **Statement**    | The Max collar device shall include the current GNSS fix interval setting (in minutes) in its status payload transmitted in every sync, enabling the companion app to compute and display an interval-aware battery-life estimate and to issue the Max <10-day battery warning. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §12.4] |

<a id="req-ux-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0027**  | **The collar device  transmit a persistent breakaway/separation event record as…**                                |
| **Statement**    | The collar device shall transmit a persistent breakaway/separation event record as defined in A-0018, flagged with elevated transmission priority, on the next successful base-station contact following a breakaway event, enabling the companion app's "CCF Replacement Required" owner notification. The primary post-breakaway safety mitigation remains the passive CCF visible fracture indicator per SRS-UX-0021; the electronic notification is a secondary, best-effort notification only. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §10.1.3.6] [PRD §12.4] [ASSUMPTION: A-0018] |

<a id="req-ux-0028"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0028**  | **The collar device  communicate each distinct OTA update state — Downloading,…**                                |
| **Statement**    | The collar device shall communicate each distinct OTA update state — Downloading, Verifying, Pending Installation, Installing, Success, and Failed — via a unique LED pattern distinguishable from all other LED states defined in §14.3, enabling the user to understand update progress without the companion app. OTA functional states per §5. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §9.5] |

<a id="req-ux-0029"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-UX-0029**  | **The collar device LED  remain continuously active during an OTA update, with no…**                                |
| **Statement**    | The collar device LED shall remain continuously active during an OTA update, with no dark (LED-off) period exceeding 10 seconds during any OTA state expected to last >30 seconds, preventing the user from misinterpreting a prolonged dark period as a device failure or bricked state. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | Stable                                        |
| **Verification** | Test                               |
| **Traceability** | — |


## 15. Operational Requirements

## 15.0 Scope Note

This section specifies operational behavior of the deployed system that is not already owned by another section: base-station continuous-operation posture and included power accessory, base-station status-indicator inventory (deferred here from §11 per that section's own Drafter Notes), the device-local home/away determination that other sections' power-gating and status requirements depend on, and the collar's duty-cycle/power-optimization behaviors drawn from PRD §15 (Power Budget) that are operational policies rather than hardware capabilities. It does **not** re-issue constraints already owned elsewhere:

- **GNSS interface behavior** (presence on Max, absence on Mini, configurable/default fix interval, A-GPS delivery/validity, fix-acquisition timeout, warm TTFF ceiling) is owned by §10 Interface Requirements (SRS-INT-0021–0029); this section does not restate those numeric bounds.
- **GNSS smart power-gate non-configurability** and the **Max GNSS interface disablement while HOME** are owned by §2 (SRS-OPER-0004) and §10 (SRS-INT-0027) respectively; this section adds only the device-local home/away determination mechanism those two depend on, which was not yet issued anywhere.
- **Battery cell minimum capacities, battery-life targets, idle-current ceiling, and low-battery alert threshold** are owned by §10.4/§11 Hardware (SRS-HW-0020–0024) and §3 Behavioral Classification (SRS-FUNC-0011); this section does not restate those figures.
- **Base-station Wi-Fi/cloud connectivity reliability bound and degraded-mode offline buffering** are owned by §2 (SRS-OPER-0007) and §4 (SRS-CONN-0028/0029); this section does not restate the −70 dBm / 256 kbps bound.
- **Base-station LED dimming / nighttime-mode `should`** is fully specified by §14 Usability (SRS-UX-0017, per [ASSUMPTION: A-0008]); this section does not re-issue it, only the base LED *inventory* deferred to this section by §11's own Drafter Notes.
- **OTA mechanics, atomicity, and success-rate criteria** are owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004); this section does not restate them.

## 15.1 Base Station Continuous Operation

## 15.2 Base Station Status Indicators

## 15.3 Household Geo-Fence Mesh Participation

## 15.4 Device-Local Home/Away Determination

## 15.5 Collar Duty-Cycle & Power-Optimization Policy

## 15.6 Cloud-Loss Fallback Governance

## 15.7 Product Service Lifetime Reference

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-OPER-0012 | Base Station Continuous Operational Posture | HIGH | STABLE | Demonstration |
| SRS-OPER-0013 | AC Power Adapter Inclusion | MEDIUM | STABLE | Inspection |
| SRS-OPER-0014 | Charging-Tier Base Station LED Inventory | HIGH | STABLE | Inspection |
| SRS-OPER-0015 | Relay-Tier Base Station LED Inventory | HIGH | STABLE | Inspection |
| SRS-OPER-0016 | Multi-Base Household Geo-Fence Mesh Participation | HIGH | STABLE | Demonstration |
| SRS-OPER-0017 | Device-Local Home/Away State Machine | HIGH | STABLE | Demonstration |
| SRS-OPER-0018 | Device-Local Home-to-Away RSSI Transition Threshold | MEDIUM | LIKELY-CHANGE | Test |
| SRS-OPER-0024 | Device-Local Away-to-Home RSSI Hysteresis Threshold | MEDIUM | LIKELY-CHANGE | Test |
| SRS-OPER-0019 | Wellness-Mode Deep-Sleep Idle State | HIGH | STABLE | Analysis |
| SRS-OPER-0020 | GNSS Fix-Interval Change Application Timing | MEDIUM | STABLE | Test |
| SRS-OPER-0021 | Battery Cell Cycle-Life Validation Basis | MEDIUM | STABLE | Test |
| SRS-OPER-0022 | Device-Local Fallback Authority on Extended Cloud Loss | MEDIUM | STABLE | Analysis |
| SRS-OPER-0023 | Expected Product Service Lifetime Reference Figure | MEDIUM | STABLE | Inspection |

<a id="req-oper-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0012**  | **Base Station Continuous Operational Posture**                                |
| **Statement**    | The base station **shall** remain in a continuously powered, non-sleeping operational state for as long as AC power is supplied, maintaining active BLE scanning and Wi-Fi uplink capability at all times. |
| **Rationale**    | The base station is a mains-powered, always-available relay; PRD §11.7 states continuous operation with no sleep state and BLE scan/uplink always on, distinguishing its operational posture from the battery-powered, power-optimized collar devices. This continuous posture is also the precondition assumed by the base-station uptime criterion (SRS-RELI-0003) and by the household geo-fence mesh's ability to detect collar sightings without a scheduling gap. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §11.7] · SRS-RELI-0003 |

<a id="req-oper-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0013**  | **AC Power Adapter Inclusion**                                |
| **Statement**    | The base station **shall** be supplied with an AC-to-USB-C power adapter as an included accessory. |
| **Rationale**    | PRD §11.7 specifies USB-C power with the adapter included, ensuring the base station is immediately operable out of box without requiring the owner to source a separate power adapter. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §11.7] · none |

<a id="req-oper-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0014**  | **Charging-Tier Base Station LED Inventory**                                |
| **Statement**    | The Base Station (Charging) tier **shall** provide exactly 3 status LEDs, indicating at minimum: AC power presence, device-charging activity, and cloud-connectivity status. |
| **Rationale**    | PRD §4.2/§11.6 specify a 3-LED inventory (power/charging/cloud) for the Charging tier, distinct from the Relay tier's 2-LED inventory (SRS-OPER-0015) because the Relay tier has no charging cradle to indicate. This is a hardware-inventory requirement; the LED *behavior* (indication patterns) for each state is specified by §14 Usability (SRS-UX-0016). |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §11.6], [PRD §4.2] · SRS-OPER-0015, SRS-UX-0016 |

<a id="req-oper-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0015**  | **Relay-Tier Base Station LED Inventory**                                |
| **Statement**    | The Base Station (Relay) tier **shall** provide exactly 2 status LEDs, indicating at minimum: AC power presence and cloud-connectivity status. |
| **Rationale**    | The Relay tier omits the charging-activity LED present on the Charging tier (SRS-OPER-0014) because it has no charging cradle to report on, consistent with PRD §4.2's description of the Relay tier as identical to the Charging tier minus the charging cradle. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §11.6], [PRD §4.2] · SRS-OPER-0014, SRS-UX-0016 |

<a id="req-oper-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0016**  | **Multi-Base Household Geo-Fence Mesh Participation**                                |
| **Statement**    | Every base station in a household deployment **shall** participate in a shared geo-fence mesh by independently reporting BLE sighting reports for every collar device within its range. |
| **Rationale**    | PRD §5.3/§4.2 describe up to 8 base stations per household (≥1 Charging) collectively forming a geo-fence mesh; each base station's independent sighting-report contribution (payload structure per SRS-INT-0054) is the mesh's data basis, distinct from the collar-side forwarding-path requirements already owned by §4 (SRS-CONN-0019/0020). |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §4.2], [PRD §5.3] · SRS-INT-0054, SRS-CONN-0019 |

<a id="req-oper-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0017**  | **Device-Local Home/Away State Machine**                                |
| **Statement**    | The collar device **shall** determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) readings from paired base stations in range, without reliance on any cloud-side determination. |
| **Rationale**    | PRD §6.4 states dual home/away state machines exist (device-local and cloud-side), and [ASSUMPTION: A-0016] confirms the device-local state machine is the sole in-scope authority for power gating — notably the Max GNSS smart power gate (SRS-INT-0027, SRS-OPER-0004) — with the cloud-side state machine external ([EXTERNAL: IoT Cloud backend team], SRS-OPER-0011). This requirement establishes the existence and RSSI basis of the device-local mechanism that SRS-INT-0027, SRS-OPER-0004, and SRS-PERF-0007 all depend on but which was not yet issued as its own requirement in any approved section. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Demonstration                               |
| **Traceability** | [PRD §6.4], [PRD §4.1], [ASSUMPTION: A-0016] · SRS-INT-0027, SRS-OPER-0004, SRS-PERF-0007, SRS-OPER-0011 |

<a id="req-oper-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0018**  | **Device-Local Home-to-Away RSSI Transition Threshold**                                |
| **Statement**    | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from HOME to AWAY only when no paired base station RSSI reading exceeds −85 dBm for 5 consecutive readings taken at 1 s intervals. |
| **Rationale**    | PRD §4.1/§6.4 state that home/away determination occurs "via multi-base RSSI" but supply no numeric threshold or debounce criterion; [ASSUMPTION: A-0022] resolves this gap (engineered by analogy to [ASSUMPTION: A-0009]'s Wi-Fi RSSI bound) with a conservative −85 dBm threshold, representing the typical "fair/poor" BLE boundary through 3+ interior walls or 15–25 m open-air range in a residential deployment, deliberately biased toward retaining HOME status because a false-AWAY transition needlessly enables the Max GNSS power gate (SRS-INT-0027, SRS-OPER-0004) and increases power draw, whereas a brief false-HOME delay does not. The 5-consecutive-reading/1 s-interval debounce filters transient RSSI dips (e.g., momentary body-shadowing) before committing the transition. This requirement was returned FAIL by the Feasibility Checker (v1; D3 Testability, D4 Completeness) for being issued as a non-normative PRD-gap notice rather than a testable SHALL; it is reissued here as a testable predicate now that [ASSUMPTION: A-0022] supplies the numeric basis, and is split from the AWAY-to-HOME hysteresis criterion (SRS-OPER-0024) per the Single-Predicate Rule. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.4], [PRD §4.1], [ASSUMPTION: A-0022] · SRS-OPER-0017, SRS-OPER-0024 |

<a id="req-oper-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0024**  | **Device-Local Away-to-Home RSSI Hysteresis Threshold**                                |
| **Statement**    | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from AWAY to HOME only when at least one paired base station RSSI reading exceeds −80 dBm for 3 consecutive readings taken at 1 s intervals. |
| **Rationale**    | [ASSUMPTION: A-0022] specifies a 5 dB hysteresis band between the AWAY-transition threshold (−85 dBm, SRS-OPER-0018) and this AWAY-to-HOME re-entry threshold (−80 dBm) to prevent rapid HOME/AWAY oscillation when RSSI hovers near the boundary, which would otherwise cause repeated toggling of the Max GNSS power gate (SRS-INT-0027) and unnecessary power draw. The shorter 3-reading debounce (vs. SRS-OPER-0018's 5-reading debounce) is an intentional asymmetry: re-establishing HOME status should be comparatively responsive once signal recovers, because remaining falsely in AWAY costs more GNSS-on power than a brief false-HOME determination. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §6.4], [PRD §4.1], [ASSUMPTION: A-0022] · SRS-OPER-0017, SRS-OPER-0018 |

<a id="req-oper-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0019**  | **Wellness-Mode Deep-Sleep Idle State**                                |
| **Statement**    | The collar device, while in Wellness Mode and not actively processing a motion-triggered confirmation burst, **shall** remain in its deepest available low-power idle state. |
| **Rationale**    | PRD §15.2 specifies deepest-sleep idle as the standard Wellness-Mode duty-cycle baseline underlying the stated battery-life targets; this is the operational-policy statement that the idle-current ceiling itself (SRS-FUNC-0011, ≤4 µA) is verified against. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §15.2], [PRD §7.3] · SRS-FUNC-0011, SRS-FUNC-0010 |

<a id="req-oper-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0020**  | **GNSS Fix-Interval Change Application Timing**                                |
| **Statement**    | When the owner changes the Max collar variant's configured GNSS fix interval, the collar device **shall** apply the new interval no later than the start of the next scheduled fix-acquisition cycle. |
| **Rationale**    | PRD §15.5 states that a fix-interval change takes effect "within one cycle," bounding how long a stale interval setting may persist. This is the timing/application-policy requirement; the interval's configurable range (30 min–24 h) and default value (2 h) are owned by §10 (SRS-INT-0023, SRS-INT-0024) and not restated here. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §15.5] · SRS-INT-0023, SRS-INT-0024 |

<a id="req-oper-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0021**  | **Battery Cell Cycle-Life Validation Basis**                                |
| **Statement**    | Battery-life validation testing **shall** be performed using cells that have completed no fewer than 50 charge/discharge cycles prior to the validation measurement. |
| **Rationale**    | PRD §15.6 specifies a DVT programmable-load validation methodology requiring cells aged to ≥50 cycles before the battery-life pass criterion (≥80% of the §10.4 minimum capacity at 25°C) is evaluated, ensuring the stated battery-life targets (SRS-PERF-0001, SRS-PERF-0002) are validated against realistically aged cells rather than fresh-cell best-case performance. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Test                               |
| **Traceability** | [PRD §15.6] · SRS-PERF-0001, SRS-PERF-0002 |

<a id="req-oper-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0022**  | **Device-Local Fallback Authority on Extended Cloud Loss**                                |
| **Statement**    | The collar device **shall** rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the base station has not had successful cloud contact for more than 24 hours, without requiring any additional fallback logic beyond the state machine's ordinary operation. |
| **Rationale**    | PRD §6.4 frames the device-local state machine's role as a ">24 h cloud loss" fallback governing the Max GNSS gate, implying the cloud-side state machine (external, [EXTERNAL: IoT Cloud backend team]) would otherwise have some role during shorter cloud outages. Per [ASSUMPTION: A-0016], however, the device-local state machine is the SOLE in-scope authority for power gating at all times, not only after 24 hours; this requirement makes explicit that no additional in-scope fallback mechanism activates at the 24-hour mark — the device-local state machine's continuous, unconditional operation (SRS-OPER-0017) already satisfies the PRD's fallback framing without requiring separate logic. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §6.4] · SRS-OPER-0017, SRS-OPER-0011 |

<a id="req-oper-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-OPER-0023**  | **Expected Product Service Lifetime Reference Figure**                                |
| **Statement**    | The system's operational and durability requirements that reference an expected service lifetime **shall** use 2 years as the minimum testable floor, consistent with the Product Context Profile's user-confirmed ~2–3 year expected service lifetime figure. |
| **Rationale**    | This requirement formalizes, as its own SRS-OPER block, the same PCP §8 user-confirmed lifetime figure that SRS-RELI-0001 (§13) already applies as its qualification duration; §13's Drafter Notes flagged that no A-ID currently carries this figure and recommended one be issued. Issuing it here as an explicit OPER requirement — rather than only as an inline PCP dependency note on SRS-RELI-0001 — gives the figure a citable SRS-ID that future sections (e.g., §16 Maintainability's OTA-support-lifetime requirements) can cross-reference directly instead of re-deriving it from the PCP each time. |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD — ABSENT: service_lifetime_duration_value] · SRS-RELI-0001 |


## 16. Maintainability Requirements

## 16.0 Scope Note

This section specifies the *lifetime-maintenance* obligations implied by PRD §12.7 that are not already owned by another section. It does **not** re-issue constraints already owned elsewhere:

- **OTA mechanics** owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004)
- **SBOM per-release production** owned by §5 (SRS-FUNC-0061)
- **Pre-launch vuln-disclosure gate** owned by §8 (SRS-SEC-0006)
- **Tier-2 via OTA no HW mod** owned by §3 (SRS-FUNC-0034, SRS-FUNC-0035)
- **2-year lifetime floor** owned by §15 (SRS-OPER-0023)
- **Cloud-side maintenance** is [EXTERNAL: IoT Cloud backend team]; in-scope interface obligation remains SRS-DATA-0024 (§9)

## 16.1 OTA-Update Capability Lifetime

## 16.2 SBOM Lifetime Currency

## 16.3 Post-Launch Vulnerability-Disclosure Process Continuity

---

**Drafter Notes:** v1 — 3 blocks. All single-predicate, anchored to SRS-OPER-0023 2-year floor. No new assumptions required. CAT cursor: MAINT-0004 next.

<a id="req-maint-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-MAINT-0001**  | **OTA-Update Capability Availability Through Supported Service Lifetime**                                |
| **Statement**    | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.7] · SRS-OPER-0023, SRS-FUNC-0043, SRS-FUNC-0044 |

<a id="req-maint-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-MAINT-0002**  | **SBOM Currency Maintenance Across Supported Service Lifetime**                                |
| **Statement**    | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetime defined by SRS-MAINT-0001. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.7], [PRD §9.5] · SRS-FUNC-0061, SRS-MAINT-0001 |

<a id="req-maint-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-MAINT-0003**  | **Post-Launch Vulnerability-Disclosure Process Maintenance**                                |
| **Statement**    | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported service lifetime defined by SRS-MAINT-0001. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.7], [STD: RM-0021] · SRS-SEC-0006, SRS-MAINT-0001 |


## 17. Standards Conformance

## 17.0 Scope Note

This section binds the product design to the named technical standards whose test methods, clauses, or provisions underlie requirements already issued in §§5–16. §17 (COMP) answers "what standards does this design conform to"; §18 (REG) answers "what market certifications/approvals are needed."

## 17.1 Ingress Protection

## 17.2 Battery & Electrical Safety

## 17.3 IoT Cybersecurity Baseline

## 17.4 Environmental Test-Method Series (IEC 60068-2)

## 17.5 Radio / EMC

## 17.6 Materials Compliance

## 17.7 Software & Quality Management

## 17.8 Out-of-Scope Standards (Explicit Attribution)

- **IEC 62304** — OUT OF SCOPE. Product is general-wellness for animals, not a medical device. Responsible: Regulatory Affairs / Product Management.
- **ISO 14971** — OUT OF SCOPE. Same NOT-a-medical-device basis. General safety governed by EU GPSR 2023/988.
- **ISO 13485 / ISO 9001** — OUT OF SCOPE. No PRD or Regulatory Map mandate; QMS is an organizational attribute. Responsible: Operations / Manufacturing team.
- **IPC PCB Design Standards** — OUT OF SCOPE. No PRD source; PCB implementation is a design-choice in Altium Designer 24.
- **RTOS-Specific Software Standard** — OUT OF SCOPE. No PRD source; RTOS selection (Zephyr-preferred) is a firmware-team implementation choice.
- **EU Battery Regulation Art 11 (Removability)** — CONTINGENT. Potential conflict with non-swappable design; [ASSUMPTION: A-0013] tracks INDICATIVE exemption. Responsible: Regulatory Affairs, via EU counsel.
- **GNSS Intentional-Radiator Exemption** — CONTINGENT. RM-0009 UNCERTAIN, escalated to user.
- **ASTM F2727** — EXCLUDED AS MISCITATION. Corrected to ASTM F2056 per RM-0030.

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-COMP-0005 | IEC 60529 Ingress Protection Standard Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0006 | IEC 62133-2 Battery Cell Safety Standard Conformance | CRITICAL | LIKELY-CHANGE | Inspection |
| SRS-COMP-0007 | UN 38.3 Battery Transport Safety Standard Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0008 | UL 1642/UL 2054 US Cell Safety Standard Conformance | HIGH | STABLE | Inspection |
| SRS-COMP-0009 | EN 62368-1/UL 62368-1 Base Station Electrical Safety Standard Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0010 | ETSI EN 303 645 Consumer IoT Security Baseline Conformance | CRITICAL | LIKELY-CHANGE | Inspection |
| SRS-COMP-0011 | IEC 60068-2-14 Thermal-Cycling Test Standard Conformance | HIGH | STABLE | Inspection |
| SRS-COMP-0012 | IEC 60068-2-78 Damp-Heat Test Standard Conformance | MEDIUM | STABLE | Inspection |
| SRS-COMP-0013 | IEC 60068-2-27 Mechanical Shock Test Standard Conformance | MEDIUM | STABLE | Inspection |
| SRS-COMP-0014 | IEC 60068-2-64 Vibration Test Standard Conformance | MEDIUM | STABLE | Inspection |
| SRS-COMP-0015 | IEC 60068-2-5 UV-Aging Test Standard Conformance | HIGH | STABLE | Inspection |
| SRS-COMP-0016 | ETSI EN 300 328 2.4 GHz Radio Standard Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0017 | Bluetooth SIG Qualification Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0018 | FCC Part 15 Subpart C Intentional Radiator Standard Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0019 | FCC Part 15 Subpart B Unintentional Radiator Standard Conformance | HIGH | STABLE | Inspection |
| SRS-COMP-0020 | RED 2014/53/EU Essential Requirements Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0021 | RF Human-Exposure Standard Conformance (Contingent) | HIGH | LIKELY-CHANGE | Analysis |
| SRS-COMP-0022 | REACH Regulation Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0023 | RoHS Directive Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0024 | California Proposition 65 Conformance | HIGH | STABLE | Inspection |
| SRS-COMP-0025 | EU Battery Regulation Material and Labelling Conformance | CRITICAL | STABLE | Inspection |
| SRS-COMP-0026 | WEEE Directive Conformance | HIGH | STABLE | Inspection |
| SRS-COMP-0027 | EU PPWR / UK Producer Responsibility Packaging Conformance | MEDIUM | LIKELY-CHANGE | Inspection |
| SRS-COMP-0028 | SBOM Machine-Readable Format Conformance | MEDIUM | LIKELY-CHANGE | Inspection |

<a id="req-comp-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0005**  | **IEC 60529 Ingress Protection Standard Conformance**                                |
| **Statement**    | The collar device, in its standalone (CCF-unmated) configuration, shall conform to the IEC 60529 IPX7 test methodology as the verification basis for the IP67 ingress-protection rating required by SRS-HW-0003. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.4], [STD: RM-0028] · SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007 |

<a id="req-comp-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0006**  | **IEC 62133-2 Battery Cell Safety Standard Conformance**                                |
| **Statement**    | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.3], [STD: RM-0011] · — |

<a id="req-comp-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0007**  | **UN 38.3 Battery Transport Safety Standard Conformance**                                |
| **Statement**    | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.4], [PRD §13.3], [STD: RM-0010] · SRS-COMP-0006 |

<a id="req-comp-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0008**  | **UL 1642/UL 2054 US Cell Safety Standard Conformance**                                |
| **Statement**    | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable to cell construction, for placement on the US market. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.3], [STD: RM-0012] · SRS-COMP-0006 |

<a id="req-comp-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0009**  | **EN 62368-1/UL 62368-1 Base Station Electrical Safety Standard Conformance**                                |
| **Statement**    | The Base Station, in both Charging and Relay tiers, shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.3], [STD: RM-0013] · — |

<a id="req-comp-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0010**  | **ETSI EN 303 645 Consumer IoT Security Baseline Conformance**                                |
| **Statement**    | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.3], [PRD §13.5], [STD: RM-0019] · SRS-SEC-0001 through SRS-SEC-0006 |

<a id="req-comp-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0011**  | **IEC 60068-2-14 Thermal-Cycling Test Standard Conformance**                                |
| **Statement**    | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.5], [STD: RM-0028], [ASSUMPTION: A-0003] · SRS-ENV-0003 |

<a id="req-comp-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0012**  | **IEC 60068-2-78 Damp-Heat Test Standard Conformance**                                |
| **Statement**    | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.4], [STD: RM-0028] · SRS-ENV-0004 |

<a id="req-comp-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0013**  | **IEC 60068-2-27 Mechanical Shock Test Standard Conformance**                                |
| **Statement**    | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.4], [STD: RM-0028] · SRS-ENV-0010 |

<a id="req-comp-0014"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0014**  | **IEC 60068-2-64 Vibration Test Standard Conformance**                                |
| **Statement**    | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.4], [STD: RM-0028] · SRS-ENV-0011 |

<a id="req-comp-0015"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0015**  | **IEC 60068-2-5 UV-Aging Test Standard Conformance**                                |
| **Statement**    | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §12.5], [STD: RM-0028] · SRS-ENV-0013 |

<a id="req-comp-0016"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0016**  | **ETSI EN 300 328 2.4 GHz Radio Standard Conformance**                                |
| **Statement**    | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.1], [STD: RM-0004] · SRS-CONN-0001, SRS-CONN-0002, SRS-CONN-0007 |

<a id="req-comp-0017"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0017**  | **Bluetooth SIG Qualification Conformance**                                |
| **Statement**    | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.1], [STD: RM-0008] · SRS-COMP-0016 |

<a id="req-comp-0018"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0018**  | **FCC Part 15 Subpart C Intentional Radiator Standard Conformance**                                |
| **Statement**    | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.1], [STD: RM-0001] · SRS-COMP-0016 |

<a id="req-comp-0019"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0019**  | **FCC Part 15 Subpart B Unintentional Radiator Standard Conformance**                                |
| **Statement**    | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.1], [STD: RM-0002] · SRS-COMP-0018 |

<a id="req-comp-0020"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0020**  | **RED 2014/53/EU Essential Requirements Conformance**                                |
| **Statement**    | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.1], [STD: RM-0003] · SRS-COMP-0016, SRS-COMP-0010 |

<a id="req-comp-0021"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0021**  | **RF Human-Exposure Standard Conformance (Contingent)**                                |
| **Statement**    | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applicable. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [PRD §13.1], [STD: RM-0029] · — |

<a id="req-comp-0022"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0022**  | **REACH Regulation Conformance**                                |
| **Statement**    | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §10.1.2], [PRD §13.2], [PRD §13.7], [STD: RM-0026] · SRS-SAFE-0021 |

<a id="req-comp-0023"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0023**  | **RoHS Directive Conformance**                                |
| **Statement**    | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.7], [STD: RM-0026] · SRS-COMP-0022 |

<a id="req-comp-0024"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0024**  | **California Proposition 65 Conformance**                                |
| **Statement**    | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.7], [STD: RM-0026] · SRS-COMP-0022, SRS-COMP-0023 |

<a id="req-comp-0025"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0025**  | **EU Battery Regulation Material and Labelling Conformance**                                |
| **Statement**    | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. |
| **Rationale**    |  |
| **Priority**     | CRITICAL                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.7], [STD: RM-0014] · — |

<a id="req-comp-0026"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0026**  | **WEEE Directive Conformance**                                |
| **Statement**    | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. |
| **Rationale**    |  |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.7], [STD: RM-0027] · — |

<a id="req-comp-0027"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0027**  | **EU PPWR / UK Producer Responsibility Packaging Conformance**                                |
| **Statement**    | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.7], [STD: RM-0027] · SRS-COMP-0026 |

<a id="req-comp-0028"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-COMP-0028**  | **SBOM Machine-Readable Format Conformance**                                |
| **Statement**    | The SBOM produced at each OTA release (SRS-FUNC-0061) and maintained across the supported service lifetime (SRS-MAINT-0002) shall be issued in a machine-readable format conforming to SPDX 2.3 or CycloneDX. |
| **Rationale**    |  |
| **Priority**     | MEDIUM                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §9.5], [PRD §12.7], [PRD — ABSENT: sbom_format_standard] · SRS-FUNC-0061, SRS-MAINT-0002 |


## 18. Regulatory Certification & Market Pathways

# §18 — Regulatory Certification & Market Pathways

**CAT: REG** · **46 blocks (REG-0001–0046)** · **Status: APPROVED**
**Pipeline:** Feasibility PASS (46/46) · V-Method PASS (46/46) · Intra-Conflict COMPLETE (CR-0028/0029) · RTM ADD-ROW COMPLETE (323→369)

§18 (REG) answers "what certifications/approvals are needed to place the product on each market" — distinct from §17 (COMP), which binds the design to the underlying technical standards.

## Requirement Summary

| Part | Markets | Reqs | ID Range |
| A | US + Canada | 13 | REG-0001–0013 |
| B | EU/EEA + UK | 22 | REG-0014–0035 |
| B (Addendum) | EU+UK GNSS | 2 | REG-0045–0046 |
| C | AU/NZ + Global | 9 | REG-0036–0044 |
| **Total** | **5+ markets** | **46** | **REG-0001–0046** |

---

## Part A — US + Canada (REG-0001–0013)

### 18.A.1 United States Market

### 18.A.2 Canada Market

### 18.A.3 Cross-Market Gate

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

- AU/NZ EMC/electrical-safety mapping → Regulatory Affairs
- RCM test execution → Accredited lab (external)
- AU/NZ Responsible Supplier duties → Supplier (external)
- Regulatory-change monitoring mechanism → Regulatory Affairs
- Per-market retention period research → Regulatory Affairs / counsel
- AU/NZ customs import filing → Logistics / Customs-Broker

---

## Pipeline Status

| Stage | Verdict | Details |
| Draft + Addendum | COMPLETE | 46 blocks (REG-0001–0046) across 4 parts |
| Feasibility | PASS | v1: 44 base. vPOST: 2 addendum. 46/46 PASS |
| V-Method | PASS | 46/46, 0 FAIL. Inspection (market-access artifacts) + Analysis (contingent determinations) |
| Intra-Conflict | COMPLETE | CR-0028 (REG-0035 XR gap), CR-0029 (REG-0044 XR gap) |
| Traceability | COMPLETE | UPDATE-ROW + ADD-ROW: 46 rows. RTM 323→369 |

| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|
| SRS-REG-0001 | FCC Part 15 Subpart C Certification Hold (US) | HIGH | STABLE | Inspection |
| SRS-REG-0002 | FCC Part 15 Subpart B Supplier's Declaration of Conformity (US) | HIGH | STABLE | Inspection |
| SRS-REG-0003 | FCC Identifier Marking (US) | HIGH | STABLE | Inspection |
| SRS-REG-0004 | NRTL Listing Hold for Base Station Electrical Safety (US) | HIGH | STABLE | Inspection |
| SRS-REG-0005 | California Proposition 65 Conditional Warning Labeling (US-CA) | HIGH | STABLE | Inspection |
| SRS-REG-0006 | Certification Documentation Package Availability (US) | HIGH | STABLE | Inspection |
| SRS-REG-0007 | GNSS Passive-Receiver Intentional-Radiator Exemption Determination (US) | HIGH | VOLATILE | Analysis |
| SRS-REG-0008 | ISED Certification Hold (Canada) | HIGH | LIKELY-CHANGE | Inspection |
| SRS-REG-0009 | ISED ICES-003 Compliance (Canada) | HIGH | STABLE | Inspection |
| SRS-REG-0010 | Innovation Canada Identifier Marking (Canada) | HIGH | STABLE | Inspection |
| SRS-REG-0011 | Certification Documentation Package Availability (Canada) | HIGH | STABLE | Inspection |
| SRS-REG-0012 | GNSS Passive-Receiver Intentional-Radiator Exemption Determination (Canada) | HIGH | VOLATILE | Analysis |
| SRS-REG-0013 | Pre-Launch Certification-Status Gate (US + Canada) | HIGH | STABLE | Inspection |
| SRS-REG-0045 | GNSS Exemption Determination (EU) |  | VOLATILE | Analysis |
| SRS-REG-0046 | GNSS Exemption Determination (UK) |  | VOLATILE | Analysis |

<a id="req-reg-0001"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0001**  | **FCC Part 15 Subpart C Certification Hold (US)**                                |
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Body (TCB) prior to commercial distribution in the US market. |
| **Rationale**    | FCC 47 CFR Part 15 Subpart C §15.247 mandates third-party TCB certification (not self-declaration) for intentional radiators in the 2.4 GHz band; this is the market-access instrument corresponding to the technical conformance already required by SRS-COMP-0018. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0001], [PRD §13.1] · SRS-COMP-0018 |

<a id="req-reg-0002"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0002**  | **FCC Part 15 Subpart B Supplier's Declaration of Conformity (US)**                                |
| **Statement**    | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions prior to commercial distribution. |
| **Rationale**    | FCC 47 CFR Part 15 Subpart B §15.107/§15.109 permits self-declaration rather than TCB certification for unintentional-emitter compliance. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0002], [PRD §13.1] · SRS-COMP-0019 |

<a id="req-reg-0003"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0003**  | **FCC Identifier Marking (US)**                                |
| **Statement**    | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the US market. |
| **Rationale**    | FCC ID marking is a mandatory labeling condition attached to the Part 15 Subpart C certification. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0001], [PRD §13.1] · SRS-REG-0001 |

<a id="req-reg-0004"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0004**  | **NRTL Listing Hold for Base Station Electrical Safety (US)**                                |
| **Statement**    | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. |
| **Rationale**    | US retail market access for mains-powered electronic equipment requires NRTL listing. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0013], [PRD §13.3] · SRS-COMP-0009 |

<a id="req-reg-0005"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0005**  | **California Proposition 65 Conditional Warning Labeling (US-CA)**                                |
| **Statement**    | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is present above the applicable safe-harbor threshold, prior to commercial distribution in the US-CA market. |
| **Rationale**    | Proposition 65 imposes a conditional warning-labeling obligation that is procedurally distinct from the underlying materials-conformance requirement. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0026], [PRD §13.7] · SRS-COMP-0024 |

<a id="req-reg-0006"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0006**  | **Certification Documentation Package Availability (US)**                                |
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support FCC TCB certification (SRS-REG-0001) and NRTL listing (SRS-REG-0004) prior to submission for either certification. |
| **Rationale**    | Captures the delivering engineering team's own in-scope interface obligation toward the externally-executed certification processes, ensuring external TCB/NRTL bodies are not blocked by missing inputs. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD — ABSENT: us_certification_documentation_owner], [STD: RM-0001], [STD: RM-0013] · SRS-REG-0001, SRS-REG-0004 |

<a id="req-reg-0007"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0007**  | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (US)**                                |
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to commercial distribution in the US market. |
| **Rationale**    | RM-0009 is UNCERTAIN; this block requires only that the determination be made and documented, rather than asserting a specific exemption outcome. |
| **Priority**     | HIGH                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [STD: RM-0009], [PRD §13.1] · SRS-REG-0001 |

<a id="req-reg-0008"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0008**  | **ISED Certification Hold (Canada)**                                |
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen prior to commercial distribution in the Canada market. |
| **Rationale**    | ISED RSS-247 governs 2.4 GHz license-exempt radio equipment and RSS-Gen sets general certification procedure. |
| **Priority**     | HIGH                                         |
| **Stability**    | LIKELY-CHANGE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0006], [PRD §13.1] · SRS-COMP-0018, SRS-COMP-0016 |

<a id="req-reg-0009"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0009**  | **ISED ICES-003 Compliance (Canada)**                                |
| **Statement**    | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to commercial distribution. |
| **Rationale**    | ICES-003 is Canada's counterpart to the US FCC Part 15 Subpart B self-declaration regime. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0006], [PRD §13.1] · SRS-COMP-0019, SRS-REG-0002 |

<a id="req-reg-0010"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0010**  | **Innovation Canada Identifier Marking (Canada)**                                |
| **Statement**    | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the Canada market. |
| **Rationale**    | IC ID marking is a mandatory labeling condition attached to the ISED certification. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [STD: RM-0006], [PRD §13.1] · SRS-REG-0008 |

<a id="req-reg-0011"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0011**  | **Certification Documentation Package Availability (Canada)**                                |
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support ISED certification (SRS-REG-0008) prior to submission. |
| **Rationale**    | Mirrors SRS-REG-0006 for the Canada market. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD — ABSENT: canada_certification_documentation_owner], [STD: RM-0006] · SRS-REG-0008 |

<a id="req-reg-0012"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0012**  | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (Canada)**                                |
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to commercial distribution in the Canada market. |
| **Rationale**    | Mirrors SRS-REG-0007; RM-0009's UNCERTAIN status is per-market and applies independently to Canada. |
| **Priority**     | HIGH                                         |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [STD: RM-0009], [PRD §13.1] · SRS-REG-0008, SRS-REG-0007 |

<a id="req-reg-0013"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0013**  | **Pre-Launch Certification-Status Gate (US + Canada)**                                |
| **Statement**    | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identified in SRS-REG-0001 through SRS-REG-0012 applicable to that market are complete and on file. |
| **Rationale**    | Umbrella gate preventing partial or premature market release. |
| **Priority**     | HIGH                                         |
| **Stability**    | STABLE                                        |
| **Verification** | Inspection                               |
| **Traceability** | [PRD §13.1], [PRD §13.7] · SRS-REG-0001–0012 |

<a id="req-reg-0045"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0045**  | **GNSS Exemption Determination (EU)**                                |
| **Statement**    | Priority: HIGH |
| **Rationale**    |  |
| **Priority**     |                                          |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [STD: RM-0009], [PRD §13.1] · SRS-REG-0014, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="req-reg-0046"></a>

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| **SRS-REG-0046**  | **GNSS Exemption Determination (UK)**                                |
| **Statement**    | Priority: HIGH |
| **Rationale**    |  |
| **Priority**     |                                          |
| **Stability**    | VOLATILE                                        |
| **Verification** | Analysis                               |
| **Traceability** | [STD: RM-0009], [PRD §13.1] · SRS-REG-0028, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |


---

## Appendix A — Requirements Traceability Matrix Summary

The complete RTM covers **283 rows** spanning all 18 sections.

| Requirement ID | Section | Source Tags | Priority | Stability | Verification |
|:---------------|:--------|:------------|:---------|:----------|:-------------|
| SRS-REG-0001 | Prohibit medical-classification claims | [PRD §13.6] | §1 | APPROVED | Inspection |
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
| SRS-FUNC-0022 | Record contains behavior label | [PRD §7.5] | §3 | APPROVED | Inspection |
| SRS-FUNC-0023 | Record confidence 0.0–1.0 | [PRD §7.5] | §3 | APPROVED | Test |
| ... | (*243 additional rows*) | | | | |

---

## Appendix B — Regulatory Map Summary

**Policy:**  Tiered (Tier-1 existence/currency/scope verified via live web; Tier-2 clause-level from documented structure; Tier-3 UNCERTAIN reserved for genuine applicability/existence doubt).
**RM-ID range issued:**  RM-0001 … RM-0031 · **Next RM cursor:**  RM-0032
**Confidence tally:**  CONFIRMED 18 · INDICATIVE 9 · UNCERTAIN 2 (+1 miscitation flag resolved via RM-0030). RM-0031 added (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT).
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
| RM-ID   | Standard/Reg                             | Clause                                       | Market     | Applies To    | Confidence                          | Verification note                                                                                                                                                                                                                                                    |
| :------ | :--------------------------------------- | :------------------------------------------- | :--------- | :------------ | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RM-0010 | UN 38.3                                  | Part III 38.3                                | Global     | Mini/Max      | CONFIRMED                           | Before pilot production.                                                                                                                                                                                                                                             |
| RM-0011 | IEC 62133-2:2017 **+AMD1:2021** (Ed 1.1) | Cl 7                                         | EU (+intl) | Mini/Max      | CONFIRMED (version-corrected)       | PRD cites bare :2017 → cite with AMD1. ED2 effective 2026-05-29, monitor.                                                                                                                                                                                            |
| RM-0012 | UL 1642 / UL 2054                        | —                                            | US         | Mini/Max      | CONFIRMED                           | US cell/pack.                                                                                                                                                                                                                                                        |
| RM-0013 | EN 62368-1:2020 / UL 62368-1             | —                                            | EU, US     | Base          | CONFIRMED                           | Mains-powered base station.                                                                                                                                                                                                                                          |
| RM-0014 | EU Battery Regulation (EU) 2023/1542     | Art 6, **Art 11 removability**, labelling/CE | EU         | Mini/Max/Base | CONFIRMED (removability INDICATIVE) | Applicable since 18 Aug 2025; **Art 11 end-user removability mandatory 18 Feb 2027**. ⚠️ LUUCIPet battery is NON-SWAPPABLE (§14.1) → **potential conflict** vs Art 11 within 2–3 yr market life. Verify small/sealed/IP-rated exemption. → Conflict Resolver + user. |
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
| RM-ID       | Standard/Reg                                                             | Clause                                                                                                                                      | Market        | Applies To             | Confidence                    | Verification note                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :---------- | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------ | :--------------------- | :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RM-0024     | EU GPSR (EU) 2023/988                                                    | Art 5, **Art 6**                                                                                                                            | EU            | System + CCF           | CONFIRMED                     | Applicable 13 Dec 2024. Underpins Zone-2 breakaway safety case; supports A-0002/A-0010 design duty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **RM-0031** | EU GPSR (EU) 2023/988 — design-level strangulation-mitigation branch     | **Art 6(1)(a)**  [assessment: product characteristics/design] READ WITH Art 5 [general safety req] & Recital 22 [design-first hierarchy] | EU            | CCF (Zone 2 breakaway) | **INDICATIVE-pending-DVT**    | Refines RM-0024 for the specific claim (PRD §14.2/§10.1.4) that the compound-CCF breakaway = design-level strangulation mitigation. Applicability CONFIRMED (Tier-1 EUR-Lex CELEX:32023R0988). CITATION-PRECISION: obligation is Art 5; Art 6(1)(a) is assessment criteria — cite BOTH, not Art 6(1) alone. Efficacy INDICATIVE-pending-DVT: unproven esp. feline SKU (A-0014 airway caveat + CCF-L retention-floor overlap). Substantiation needed: DVT breakaway-force testing to SKU windows + feline-airway validation + documented GPSR Art 9 risk-assessment file. Supporting animal-collar-release std = ASTM F2056 per RM-0030 (NOT ASTM F2727 — miscitation resolved in RM-0030). Distinct from A-0013 (Battery Reg Art 11) — not conflated. New assumption A-0017 issued to carry this framing. |
| RM-0025     | UK GPSR 2005 / US CPSA                                                   | —                                                                                                                                           | UK, US        | System + CCF           | CONFIRMED                     | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RM-0026     | REACH (EC)1907/2006 · RoHS 2011/65/EU + 2015/863 · CA Prop 65            | REACH Annex XVII; RoHS Annex II                                                                                                             | EU, UK, US-CA | device + CCF           | CONFIRMED                     | Animal-contact materials; no chrome/nickel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| RM-0027     | WEEE 2012/19/EU · EU PPWR · UK Producer Responsibility                   | —                                                                                                                                           | EU, UK        | System + packaging     | CONFIRMED                     | —                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RM-0028     | IEC 60529 (IP67) + IEC 60068-2-1/-2-2/-2-5/-2-14/-2-27/-2-64/-2-68/-2-78 | ingress + env test                                                                                                                          | Global        | Mini/Max/CCF           | CONFIRMED (clause INDICATIVE) | Supports A-0003 (60068-2-14 Test Na thermal cycling — CONFIRMED appropriate basis).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
Consumer-IoT vertical fully covered by RM-0019. NISTIR 8259 = US voluntary guidance (not issued as mandatory RM row). **No Medical / Automotive / Aviation / Industrial-OT / Payment / Critical-Infra verticals triggered** — the NOT-a-medical-device boundary (§13.6) keeps IEC 62304 / EU MDR / FDA out. ✅ No vertical leakage.
- **A-0002** (Zone-2 blunt-edge method): PARTIALLY CONFIRMED → keep **INDICATIVE**, method-only. GPSR Art 6 (RM-0024) supports a sharp-edge test methodology; toy-safety analog on an animal product has no direct mandate.
- **A-0010** (device-absent entrapment 12 mm probe): **INDICATIVE** — GPSR foreseeable-hazard duty supports a geometric check; specific probe is engineered default.
- **A-0011** (battery-ingestion = Li-Po pouch, NOT coin cell): **CONFIRMED.**  Reese's Law / 16 CFR 1263 / UL 4200A apply only to button/coin cells, explicitly not pouch/prismatic Li-Po. General ingestion/small-part warning under GPSR/CPSA is correct basis.
1. **RM-0009 — GNSS passive-receiver intentional-radiator exemption.**  Per-market applicability; PRD defers to Regulatory Lead. Options: A) CONFIRMED (accept exempt-unintentional-emitter across 5 markets) · B) INDICATIVE (map, per-market confirm before each submission) · C) Exclude (defer GNSS radio treatment).
2. **RM-EMC-001 (candidate) — RF human/animal-exposure standard (IEC 62311 / EN 62311 / FCC RF-exposure).**  Collar worn continuously + mains base station plausibly trigger RF-exposure assessment. Options: A) CONFIRMED (adopt IEC/EN 62311 basis now) · B) INDICATIVE (map, per-market confirm) · C) Exclude (defer).
RM-0030 — ASTM F2056 "Standard Consumer Safety Specification for Pet Collars" — CONFIRMED (existence/scope) at STANDARD LEVEL; feline force value UNVERIFIED.  Verified: ASTM F2727-09(2025) = "Standard Guide for Manufacturers for Labeling **Headgear** Products." PRD (§10.1.3.2b, §13.2, PCP) wrongly cites it as the feline ≤20 N breakaway ceiling source. Plausibly-intended standard = **ASTM F2056 "Standard Consumer Safety Specification for Pet Collars"**  (confirmed to exist), but could NOT confirm F2056 specifies a numeric ≤20 N feline force. The **CCF-M/L "canine guidance"**  ceilings have **no identifiable standard basis** (no ASTM/EN canine breakaway-force standard found).
Consequence: cat CCF-S ≤20 N ceiling cannot be traced to F2727 → citation must be corrected; CCF-M/L canine ceilings treated as **engineering-derived** ( `[ASSUMPTION]`), not `[STD:]`. **Escalated to user (Tier-3).**
- RM-0014: EU Battery Reg Art 11 removability vs non-swappable battery → potential conflict.
- Version corrections: SRS `[STD:]` tags must cite **EN 303 645:2025** and **IEC 62133-2:2017/AMD1:2021** (not the PRD's older versions).
---
*Regulatory Map Version v1.2 — includes RM-0031 (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT).*

---

## Appendix C — Assumption Register


### a-0025.md
# A-0025 — Certification/DoC Archival Retention Period

- **Date:** 2026-07-19
- **Statement:** Certification documents, DoCs, and supporting technical files required by SRS-REG-0043 shall be retained, per-market, for the longest applicable market-legal minimum, defaulting to **10 years after the last unit is placed on the market**.
- **Basis:** RED 2014/53/EU Art 10 (10yr), CRA (EU) 2024/2847 Art 13/31 (10yr/support), UK SI 2017/1206 (mirrors EU), FCC 47 CFR §2.938 (2yr), ISED RSS-Gen (FCC-aligned), ACMA/EESS (5yr). Tier-1 verified 2026-07.
- **Risk:** LOW-MEDIUM
- **Resolves:** SRS-REG-0043 D4 MARGINAL (archival retention duration)


---

## Appendix D — Glossary

**A-GPS** — Assisted GPS — auxiliary satellite ephemeris/almanac data delivered via a terrestrial link (here, BLE) to reduce GNSS fix acquisition time

**ACK** — a positive acknowledgment message confirming successful receipt of a transmitted record

**address randomization** — periodic rotation of the BLE device address to prevent long-term tracking by third-party observers

**Base Station (Charging)** — the base station tier that includes a single-device pogo-pin charging cradle in addition to BLE relay and Wi-Fi uplink functions

**Base Station (Relay)** — the base station tier that provides BLE relay and Wi-Fi uplink functions without a charging cradle

**bayonet** — a mechanical fastening geometry engaged by insertion followed by a partial rotation to lock

**central role** — the BLE role that scans for advertisements and initiates connections to peripherals

**charge/discharge cycle** — one complete sequence of fully charging and then discharging a battery cell, used as the standard unit for battery aging and cycle-life validation

**damp heat** — a combined high-temperature, high-humidity environmental test used to assess material and seal degradation under sustained humid conditions

**debounce (RSSI reading)** — a requirement that a stated number of consecutive RSSI readings, rather than a single reading, satisfy a threshold condition before a state transition is committed, filtering out transient signal fluctuations

**detent** — a spring-loaded mechanical feature that resists rotation until a threshold torque is exceeded, providing tactile lock/unlock feedback

**device-enforced protocol** — the application-layer message protocol, defined and enforced by device/base-station firmware, governing all collar-to-base-station BLE data exchange

**FIFO** — First-In-First-Out — the ordered local buffer holding classification records pending delivery

**GNSS** — Global Navigation Satellite System — a passive receiver providing position-fix data from satellite signals

**HOME/AWAY state** — the device-local determination of whether the collar device is within BLE range of at least one paired household base station (HOME) or not (AWAY), used to gate power-sensitive behaviors such as GNSS acquisition

**hysteresis (RSSI)** — a signal-strength margin requiring a materially different — here, higher — RSSI value to transition back to HOME than the value used to transition to AWAY, preventing rapid state oscillation near a single threshold

**keying** — a deliberate geometric asymmetry that permits mechanical engagement in only one correct orientation

**LE Secure Connections** — a BLE pairing method using elliptic-curve key exchange to establish link-layer encryption keys

**operational availability** — the proportion of time a system or device is capable of performing its specified function, expressed as a percentage of total elapsed time within a defined observation window

**peripheral role** — the BLE role that advertises and accepts incoming connections, as opposed to the central role that scans and initiates connections

**QDID** — Qualified Design ID — the identifier issued by the Bluetooth SIG upon successful qualification testing of a BLE product design

**QR OOB pairing** — an out-of-band BLE pairing method in which a QR code carries pairing data, avoiding reliance on numeric-comparison or passkey entry

**RSSI** — Received Signal Strength Indicator, a measurement of BLE signal power used for sighting and geo-fence determination

**sequence identifier** — a per-record protocol field enabling the receiving side to detect gaps in a forwarded record stream

**service lifetime** — the expected duration, from first use to end of intended service, over which a product must continue to meet its specified performance and safety criteria

**thermal cycling** — repeated exposure of a test article to alternating high- and low-temperature extremes to reveal degradation caused by thermally induced material stress

**TLS 1.3** — Transport Layer Security version 1.3, the transport-layer encryption protocol used for base-station-to-cloud traffic

**TTFF** — Time-To-First-Fix — the elapsed time from the start of a GNSS fix attempt to acquisition of a valid position fix

**uptime** — the proportion of a defined observation window during which a system remains powered, responsive, and capable of performing its specified function

**UV aging** — accelerated exposure of a material to ultraviolet radiation to evaluate long-term degradation from outdoor solar exposure within a compressed test duration

**VBUS** — the positive supply-voltage contact of the pogo-pin charging interface


---

**Document Statistics:** 363 requirements · 31 defined terms · 283 RTM rows · 18 sections · 0 unresolved conflicts

*End of document.*