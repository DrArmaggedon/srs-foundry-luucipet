# Software Requirements Specification

## LUUCIPet Wellness Monitor — Phase 1

| | |
|---|---|
| **Document ID** | SRS-LUUCIPET-001 |
| **Revision** | 1.0 |
| **Date** | July 2026 |
| **Project** | LUUCIPet Wellness Monitor |
| **Product Family** | Mini · Max · Base Station (Charging, Relay) · CCF (S/M/L, -RC/-MG) · Portable Travel Charging Cradle |
| **Source PRD** | LUUCIPet Wellness Monitor PRD v1.3.3 |
| **Standards Basis** | IEEE 830 / ISO/IEC/IEEE 29148 |
| **Classification** | Proprietary — For Authorized Recipients Only |

### Document Control

| Role | Responsibility |
|---|---|
| **Systems Engineering Team** | Authoring, requirements management, traceability |
| **Regulatory Affairs** | Regulatory-map ownership, market-pathway analysis |
| **Hardware Engineering** | Physical, mechanical, and component-level specifications |
| **Firmware Engineering** | Behavioral classification, OTA, connectivity, security implementation |
| **Quality Assurance** | Verification-method validation, test-plan alignment |
| **Product Management** | PRD ownership, market-requirements approval |

### Revision History

| Revision | Date | Author | Description |
|---|---|---|---|
| 1.0 | July 2026 | Systems Engineering Team | Initial release — full pipeline assembly (18 sections, 397 requirements) |

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

- A. Requirements Traceability Matrix (RTM)
- B. Regulatory Map
- C. Assumption Register
- D. Glossary

---



## 1. Introduction

<a id="srs-reg-0001"></a>

| **SRS-REG-0001** | **Prohibit medical-classification claims in labeling and marketing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's labeling and marketing materials **SHALL not** include diagnostic, treatment, or disease-detection claims. |
| **Rationale**    | The system's labeling and marketing materials **SHALL not** include diagnostic, treatment, or disease-detection claims. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.6 · SRS-REG-0002 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **Require regulatory classification review before releasing diagnostic-adjacent features** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Any post-launch feature that could constitute a diagnostic claim **SHALL** undergo regulatory classification review before release. |
| **Rationale**    | Any post-launch feature that could constitute a diagnostic claim **SHALL** undergo regulatory classification review before release. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §13.6 · SRS-REG-0001 |


## 2. Overall Description

<a id="srs-oper-0001"></a>

| **SRS-OPER-0001** | **Require at least one Charging-tier base station per household** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | A household deployment **SHALL** include at least one Base Station of the Charging tier. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §4.2], [PRD §4.5] \| VM: Inspection \| XR: SRS-OPER-0002



**SRS-OPER-0004** \| Prohibit owner configuration of the GNSS smart power gate \| The Max variant's GNSS smart power gate **SHALL not** be configurable by the owner. |
| **Rationale**    | A household deployment **SHALL** include at least one Base Station of the Charging tier. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §4.2], [PRD §4.5] \| VM: Inspection \| XR: SRS-OPER-0002<br><br>**SRS-OPER-0002** \| Limit base stations per household deployment \| A household deployment **SHALL not** exceed 8 Base Stations, in any combination of Charging and Relay tiers. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.2], [PRD §4.5] \| VM: Test \| XR: SRS-OPER-0001<br><br>**SRS-OPER-0003** \| Persist species assignment across resets \| The collar device **SHALL** retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.5], [PRD §7.2] \| VM: Test \| XR: SRS-OPER-0009<br><br>**SRS-OPER-0004** \| Prohibit owner configuration of the GNSS smart power gate \| The Max variant's GNSS smart power gate **SHALL not** be configurable by the owner. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.5 |

<a id="srs-oper-0005"></a>

| **SRS-OPER-0005** | **Bound in-box CCF fitment coverage** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The in-box Standard CCF **SHALL** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. |
| **Rationale**    | The in-box Standard CCF **SHALL** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. |
| **Priority**     | Medium |
| **Stability**    | Likely-change |
| **Verification** | Analysis |
| **Traceability** | PRD §14.2 · SRS-OPER-0006, SRS-OPER-0010 |

<a id="srs-oper-0006"></a>

| **SRS-OPER-0006** | **Default to Standard CCF as in-box accessory** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.1], [PRD §14.2] \| VM: Inspection \| XR: SRS-OPER-0005

**SRS-OPER-0007** \| Define degraded-mode behavior below the home Wi-Fi reliability bound \| The Base Station **SHALL** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. |
| **Rationale**    | The system **SHALL** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.1], [PRD §14.2] \| VM: Inspection \| XR: SRS-OPER-0005<br><br>**SRS-OPER-0007** \| Define degraded-mode behavior below the home Wi-Fi reliability bound \| The Base Station **SHALL** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 |

<a id="srs-oper-0008"></a>

| **SRS-OPER-0008** | **Mobile App post-breakaway owner alert (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **SHALL** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §10.1.3.6], [EXTERNAL: Mobile App team] \| VM: Analysis — external conformance evidence \| XR: SRS-FUNC-0001, SRS-FUNC-0002






**SRS-COMP-0003** \| Require a shared classification engine and protocol across collar variants \| The Mini and Max collar variants **SHALL** exhibit equivalent behavioral-classification outputs and use an interoperable common BLE communication protocol across the Mini and Max variants. |
| **Rationale**    | The Mobile App **SHALL** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §10.1.3.6], [EXTERNAL: Mobile App team] \| VM: Analysis — external conformance evidence \| XR: SRS-FUNC-0001, SRS-FUNC-0002<br><br>**SRS-OPER-0009** \| Mobile App species re-onboarding flow (external) \| The Mobile App **SHALL** provide a species re-onboarding flow that re-assigns the device's species classifier profile. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §4.5], [EXTERNAL: Mobile App team] \| VM: Analysis — external conformance evidence \| XR: SRS-OPER-0003<br><br>**SRS-OPER-0010** \| Mobile App CCF fitment/sizing guidance (external) \| The Mobile App **SHALL** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. \| Priority: MEDIUM \| Stability: LIKELY-CHANGE \| Source: [PRD §14.2], [EXTERNAL: Mobile App team] \| VM: Analysis — external conformance evidence \| XR: SRS-OPER-0005<br><br>**SRS-OPER-0011** \| Cloud-side home/away state machine for owner geofence alerting (external) \| The IoT Cloud Device-Management layer **SHALL** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. \| Priority: MEDIUM \| Stability: LIKELY-CHANGE \| Source: , [EXTERNAL: IoT Cloud backend team] \| VM: Analysis — external conformance evidence \| XR: SRS-OPER-0004<br><br>**SRS-COMP-0001** \| Require collar-agnostic base station firmware \| Base Station firmware **SHALL** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.3], [PRD §4.5] \| VM: Test \| XR: SRS-COMP-0002<br><br>**SRS-COMP-0002** \| Require universal CCF-to-device mechanical compatibility \| All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **SHALL** be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §4.1], [PRD §4.3] \| VM: Test \| XR: SRS-COMP-0001<br><br>**SRS-COMP-0003** \| Require a shared classification engine and protocol across collar variants \| The Mini and Max collar variants **SHALL** exhibit equivalent behavioral-classification outputs and use an interoperable common BLE communication protocol across the Mini and Max variants. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0001 |


## 3. Behavioral Classification

<a id="srs-func-0006"></a>

| **SRS-FUNC-0006** | **Wellness Mode as Default Operating Mode** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** operate in Wellness mode as its default power-optimized classification mode. |
| **Rationale**    | The system **SHALL** operate in Wellness mode as its default power-optimized classification mode. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.1 · SRS-FUNC-0011 |

<a id="srs-func-0007"></a>

| **SRS-FUNC-0007** | **Insight Mode Availability On Demand** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. |
| **Rationale**    | The system **SHALL** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.1 · SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="srs-func-0008"></a>

| **SRS-FUNC-0008** | **Insight Mode Continuous Sampling Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While in Insight mode, the system **SHALL** sample the accelerometer continuously at 50 Hz. |
| **Rationale**    | While in Insight mode, the system **SHALL** sample the accelerometer continuously at 50 Hz. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.1 · SRS-FUNC-0007, SRS-FUNC-0014 |

<a id="srs-func-0009"></a>

| **SRS-FUNC-0009** | **Insight Mode Auto-Revert to Wellness** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** automatically revert from Insight mode to Wellness mode without requiring a manual user action. |
| **Rationale**    | The system **SHALL** automatically revert from Insight mode to Wellness mode without requiring a manual user action. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0006, SRS-FUNC-0007 |

<a id="srs-func-0010"></a>

| **SRS-FUNC-0010** | **Wellness Mode Motion-Triggered Confirmation Burst** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon detecting motion, the system **SHALL** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. |
| **Rationale**    | Upon detecting motion, the system **SHALL** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0011 |

<a id="srs-func-0011"></a>

| **SRS-FUNC-0011** | **Wellness Mode Idle Current Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While in Wellness mode and outside a confirmation burst, the system **SHALL not** exceed an idle current draw of 4 µA. |
| **Rationale**    | While in Wellness mode and outside a confirmation burst, the system **SHALL not** exceed an idle current draw of 4 µA. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0006, SRS-FUNC-0010 |

<a id="srs-func-0012"></a>

| **SRS-FUNC-0012** | **Longevity Mode Shall Not Reduce Classification Sampling Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When Longevity Mode is active, the system **SHALL not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. |
| **Rationale**    | When Longevity Mode is active, the system **SHALL not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.10 · SRS-FUNC-0014 |

<a id="srs-func-0013"></a>

| **SRS-FUNC-0013** | **Longevity Mode Shall Not Reduce Classification Accuracy** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When Longevity Mode is active, the system **SHALL not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. |
| **Rationale**    | When Longevity Mode is active, the system **SHALL not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.10 · SRS-FUNC-0018, SRS-FUNC-0020 |

<a id="srs-func-0014"></a>

| **SRS-FUNC-0014** | **Minimum Accelerometer Output Data Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** sample the accelerometer at a rate of no less than 50 Hz. |
| **Rationale**    | The system **SHALL** sample the accelerometer at a rate of no less than 50 Hz. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.2 · SRS-FUNC-0008, SRS-FUNC-0015 |

<a id="srs-func-0015"></a>

| **SRS-FUNC-0015** | **No Auxiliary Sensors for Tier-1 Classification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. |
| **Rationale**    | The system **SHALL** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.2 · SRS-FUNC-0014 |

<a id="srs-func-0016"></a>

| **SRS-FUNC-0016** | **Unified Classification Pipeline Across Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. |
| **Rationale**    | The system **SHALL** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.2 · SRS-FUNC-0034 |

<a id="srs-func-0017"></a>

| **SRS-FUNC-0017** | **Species-Specific Threshold Assignment at Onboarding** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** set species-specific classification thresholds during the onboarding process. |
| **Rationale**    | The system **SHALL** set species-specific classification thresholds during the onboarding process. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.2 · SRS-OPER-0003 |

<a id="srs-func-0018"></a>

| **SRS-FUNC-0018** | **Tier-1 Per-Class Accuracy Minimum** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. |
| **Rationale**    | The system **SHALL** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. |
| **Priority**     | Critical |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0019 |

<a id="srs-func-0019"></a>

| **SRS-FUNC-0019** | **Tier-1 Per-Class False-Positive Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL not** exceed a false-positive rate of 5% for each Tier-1 behavior class. |
| **Rationale**    | The system **SHALL not** exceed a false-positive rate of 5% for each Tier-1 behavior class. |
| **Priority**     | Critical |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0018 |

<a id="srs-func-0020"></a>

| **SRS-FUNC-0020** | **Tier-2 Per-Class Accuracy Minimum** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. |
| **Rationale**    | The system **SHALL** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. |
| **Priority**     | High |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0021 |

<a id="srs-func-0021"></a>

| **SRS-FUNC-0021** | **Tier-2 Per-Class False-Positive Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL not** exceed a false-positive rate of 10% for each Tier-2 behavior class. |
| **Rationale**    | The system **SHALL not** exceed a false-positive rate of 10% for each Tier-2 behavior class. |
| **Priority**     | High |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0020 |

<a id="srs-func-0022"></a>

| **SRS-FUNC-0022** | **Classification Record Contains Behavior Label** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** include a behavior class label in every generated classification record. |
| **Rationale**    | The system **SHALL** include a behavior class label in every generated classification record. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 · SRS-FUNC-0023, SRS-FUNC-0024 |

<a id="srs-func-0023"></a>

| **SRS-FUNC-0023** | **Classification Record Contains Confidence Score** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** include a confidence score in the range 0.0 to 1.0 in every generated classification record. |
| **Rationale**    | The system **SHALL** include a confidence score in the range 0.0 to 1.0 in every generated classification record. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0024"></a>

| **SRS-FUNC-0024** | **Classification Record Timestamp Resolution** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** timestamp every classification record in UTC with a resolution no coarser than 1 second. |
| **Rationale**    | The system **SHALL** timestamp every classification record in UTC with a resolution no coarser than 1 second. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0025"></a>

| **SRS-FUNC-0025** | **Classification Record GNSS Fix on Max Variant** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **SHALL** include the most recent GNSS fix in every generated classification record. |
| **Rationale**    | On the Max product variant, the system **SHALL** include the most recent GNSS fix in every generated classification record. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0026"></a>

| **SRS-FUNC-0026** | **Minimum Local Retention of Classification Records** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** retain generated classification records locally for no less than 30 days without a cloud connection. |
| **Rationale**    | The system **SHALL** retain generated classification records locally for no less than 30 days without a cloud connection. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0027 |

<a id="srs-func-0027"></a>

| **SRS-FUNC-0027** | **No Record Discard on Connectivity Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL not** discard stored classification records upon loss of connectivity. |
| **Rationale**    | The system **SHALL not** discard stored classification records upon loss of connectivity. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0026 |

<a id="srs-func-0028"></a>

| **SRS-FUNC-0028** | **Classification Generation Independent of BLE Connectivity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** generate and record classifications independently of the current BLE connectivity state. |
| **Rationale**    | The system **SHALL** generate and record classifications independently of the current BLE connectivity state. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.6 · SRS-FUNC-0029 |

<a id="srs-func-0029"></a>

| **SRS-FUNC-0029** | **Record Forwarding Without Corruption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** forward stored classification records without data corruption. |
| **Rationale**    | The system **SHALL** forward stored classification records without data corruption. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 · SRS-FUNC-0030 |

<a id="srs-func-0030"></a>

| **SRS-FUNC-0030** | **Record Forwarding Without Sequence Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** forward stored classification records without loss of their original sequence order. |
| **Rationale**    | The system **SHALL** forward stored classification records without loss of their original sequence order. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 · SRS-FUNC-0029 |

<a id="srs-func-0031"></a>

| **SRS-FUNC-0031** | **On-Device Signal Normalization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** normalize raw accelerometer data on-device prior to classification. |
| **Rationale**    | The system **SHALL** normalize raw accelerometer data on-device prior to classification. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7 · SRS-FUNC-0032, SRS-FUNC-0033 |

<a id="srs-func-0032"></a>

| **SRS-FUNC-0032** | **Raw Accelerometer Data Shall Not Leave the Collar** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL not** transmit raw accelerometer data off the collar. |
| **Rationale**    | The system **SHALL not** transmit raw accelerometer data off the collar. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.7 · SRS-FUNC-0031, SRS-FUNC-0033 |

<a id="srs-func-0033"></a>

| **SRS-FUNC-0033** | **No Cloud Round-Trip for Classification Decisions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** produce classification decisions without requiring a round-trip to a cloud service. |
| **Rationale**    | The system **SHALL** produce classification decisions without requiring a round-trip to a cloud service. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.7 · SRS-FUNC-0028, SRS-FUNC-0032 |

<a id="srs-func-0034"></a>

| **SRS-FUNC-0034** | **Tier-2 Classifier Delivery via OTA** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** receive new Tier-2 behavior classifiers via over-the-air update. |
| **Rationale**    | The system **SHALL** receive new Tier-2 behavior classifiers via over-the-air update. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0016, SRS-FUNC-0035 |

<a id="srs-func-0035"></a>

| **SRS-FUNC-0035** | **Tier-2 Deployment Without Hardware Modification or Service Event** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL not** require hardware modification or a service event to deploy a new Tier-2 classifier. |
| **Rationale**    | The system **SHALL not** require hardware modification or a service event to deploy a new Tier-2 classifier. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0034 |

<a id="srs-func-0036"></a>

| **SRS-FUNC-0036** | **Device Application of Configured Scratching Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** apply a Scratching alert threshold value received via the companion application. |
| **Rationale**    | The system **SHALL** apply a Scratching alert threshold value received via the companion application. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0037, SRS-FUNC-0041 |

<a id="srs-func-0037"></a>

| **SRS-FUNC-0037** | **Firmware-Default Scratching Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. |
| **Rationale**    | The system **SHALL** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. |
| **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036 |

<a id="srs-func-0038"></a>

| **SRS-FUNC-0038** | **Device Application of Configured Shaking Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** apply a Shaking alert threshold value received via the companion application. |
| **Rationale**    | The system **SHALL** apply a Shaking alert threshold value received via the companion application. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0039, SRS-FUNC-0042 |

<a id="srs-func-0039"></a>

| **SRS-FUNC-0039** | **Firmware-Default Shaking Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. |
| **Rationale**    | The system **SHALL** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. |
| **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0038 |

<a id="srs-func-0040"></a>

| **SRS-FUNC-0040** | **Alert Threshold Persistence Across OTA Updates** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. |
| **Rationale**    | The system **SHALL** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036, SRS-FUNC-0038 |


## 4. Data Sync Connectivity

<a id="srs-conn-0001"></a>

| **SRS-CONN-0001** | **BLE Role Assignment — Collar as Peripheral** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** operate the collar-mounted device in the BLE peripheral role relative to the base station. |
| **Rationale**    | The system **SHALL** operate the collar-mounted device in the BLE peripheral role relative to the base station. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · SRS-CONN-0002 |

<a id="srs-conn-0002"></a>

| **SRS-CONN-0002** | **BLE Role Assignment — Base Station as Central** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** operate the base station in the BLE central role relative to the collar-mounted device. |
| **Rationale**    | The system **SHALL** operate the base station in the BLE central role relative to the collar-mounted device. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · SRS-CONN-0001 |

<a id="srs-conn-0003"></a>

| **SRS-CONN-0003** | **QR-Code Out-of-Band Pairing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. |
| **Rationale**    | The system **SHALL** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.3 |

<a id="srs-conn-0004"></a>

| **SRS-CONN-0004** | **Default BLE Advertising Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** advertise the presence of the collar-mounted device at a default interval of 60 seconds. |
| **Rationale**    | The system **SHALL** advertise the presence of the collar-mounted device at a default interval of 60 seconds. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0005 |

<a id="srs-conn-0005"></a>

| **SRS-CONN-0005** | **Configurable Advertising Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. |
| **Rationale**    | The system **SHALL** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0004 |

<a id="srs-conn-0006"></a>

| **SRS-CONN-0006** | **Minimum Open-Air BLE Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. |
| **Rationale**    | The system **SHALL** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0007 |

<a id="srs-conn-0007"></a>

| **SRS-CONN-0007** | **Minimum BLE Transmit Power** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** transmit BLE signals at a power level of no less than +8 dBm. |
| **Rationale**    | The system **SHALL** transmit BLE signals at a power level of no less than +8 dBm. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0006 |

<a id="srs-conn-0008"></a>

| **SRS-CONN-0008** | **BLE Address Randomization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** randomize the BLE device address of the collar-mounted device. |
| **Rationale**    | The system **SHALL** randomize the BLE device address of the collar-mounted device. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-conn-0009"></a>

| **SRS-CONN-0009** | **Secured BLE Link Establishment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. |
| **Rationale**    | The system **SHALL** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · — (§8 Security, not yet drafted) |

<a id="srs-conn-0010"></a>

| **SRS-CONN-0010** | **Automatic BLE Reconnection on Range Re-Entry** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon the collar-mounted device re-entering BLE range of a base station, the system **SHALL** automatically re-establish the BLE link without requiring manual user action. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §6.4], [PRD §8.5] \| VM: Test \| XR: SRS-CONN-0001, SRS-CONN-0002

## 4.2 Record Forwarding & Sync


**SRS-CONN-0012** \| Best-Effort Event-Triggered Record Transport \| The system **SHALL** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. |
| **Rationale**    | Upon the collar-mounted device re-entering BLE range of a base station, the system **SHALL** automatically re-establish the BLE link without requiring manual user action. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §6.4], [PRD §8.5] \| VM: Test \| XR: SRS-CONN-0001, SRS-CONN-0002<br><br>## 4.2 Record Forwarding & Sync<br><br>**SRS-CONN-0011** \| Classification Record Forwarding on BLE Contact \| Upon establishing a BLE link with a base station, the system **SHALL** forward stored classification records from the collar-mounted device to the base station. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §8], [PRD §6.4] \| VM: Test \| XR: SRS-FUNC-0026, SRS-FUNC-0028<br><br>**SRS-CONN-0012** \| Best-Effort Event-Triggered Record Transport \| The system **SHALL** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.5 · SRS-FUNC-0002, SRS-FUNC-0003 |

<a id="srs-conn-0013"></a>

| **SRS-CONN-0013** | **Sync Resumption of Accumulated Records After Reconnection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **SHALL** forward all classification records accumulated during that disconnection. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §8], [PRD §8.5] \| VM: Test \| XR: SRS-FUNC-0027, SRS-CONN-0011

## 4.3 Base↔Cloud Gateway & Upload


**SRS-CONN-0015** \| Base Station Buffering on Upload-Path Unavailability \| When the Wi-Fi or cloud connection is unavailable, the base station **SHALL** buffer received classification records pending upload. |
| **Rationale**    | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **SHALL** forward all classification records accumulated during that disconnection. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §8], [PRD §8.5] \| VM: Test \| XR: SRS-FUNC-0027, SRS-CONN-0011<br><br>## 4.3 Base↔Cloud Gateway & Upload<br><br>**SRS-CONN-0014** \| Base Station Upload of Received Records to Cloud \| The base station **SHALL** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §8], [PRD §6.5] \| VM: Test \| XR: SRS-CONN-0011, SRS-CONN-0009<br><br>**SRS-CONN-0015** \| Base Station Buffering on Upload-Path Unavailability \| When the Wi-Fi or cloud connection is unavailable, the base station **SHALL** buffer received classification records pending upload. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0016 |

<a id="srs-conn-0016"></a>

| **SRS-CONN-0016** | **Buffered Record Upload on Path Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon restoration of the Wi-Fi or cloud connection, the base station **SHALL** upload all buffered classification records. |
| **Rationale**    | Upon restoration of the Wi-Fi or cloud connection, the base station **SHALL** upload all buffered classification records. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0015 |

<a id="srs-conn-0017"></a>

| **SRS-CONN-0017** | **No Discard of Received Records Pending Upload** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **SHALL not** discard a received classification record while that record is pending upload to the cloud. |
| **Rationale**    | The base station **SHALL not** discard a received classification record while that record is pending upload to the cloud. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0015 |

<a id="srs-conn-0018"></a>

| **SRS-CONN-0018** | **Cloud Acceptance and Acknowledgment of Uploaded Records (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **SHALL** accept and acknowledge classification records uploaded by the base station. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §8], [EXTERNAL: IoT Cloud backend team] \| VM: Inspection (external conformance evidence) \| XR: SRS-CONN-0014

**SRS-CONN-0030** \| Base Station Upload Retry on Transient Failure \| Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **SHALL** retry uploading the affected buffered classification record. |
| **Rationale**    | The IoT Cloud backend **SHALL** accept and acknowledge classification records uploaded by the base station. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §8], [EXTERNAL: IoT Cloud backend team] \| VM: Inspection (external conformance evidence) \| XR: SRS-CONN-0014<br><br>**SRS-CONN-0030** \| Base Station Upload Retry on Transient Failure \| Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **SHALL** retry uploading the affected buffered classification record. |
| **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Demonstration |
| **Traceability** | PRD §8.5 · SRS-CONN-0015, SRS-CONN-0016 |

<a id="srs-conn-0019"></a>

| **SRS-CONN-0019** | **Collar Forwarding to Any In-Range Paired Base Station** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.2], [PRD §8] \| VM: Test \| XR: SRS-CONN-0011



## 4.5 Insight-Mode Activation over Connectivity



## 4.6 GNSS Location Data Sync (Max Variant)



## 4.7 Connectivity-Loss & Degraded Behavior

**SRS-CONN-0026** \| No Record Loss Due to Any Connectivity-Loss Condition \| The system **SHALL not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. |
| **Rationale**    | The system **SHALL** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.2], [PRD §8] \| VM: Test \| XR: SRS-CONN-0011<br><br>**SRS-CONN-0020** \| Single Forwarding of Each Record to First Available Base Station \| The system **SHALL** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in range. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.2], [PRD §8] \| VM: Test \| XR: SRS-CONN-0019, SRS-CONN-0021<br><br>**SRS-CONN-0021** \| Cloud-Side Deduplication of Multi-Base Uploads (external) \| The IoT Cloud backend **SHALL** deduplicate classification records that MAY be uploaded from more than one base station within the same household account. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §4.2], [EXTERNAL: IoT Cloud backend team] \| VM: Inspection (external conformance evidence) \| XR: SRS-CONN-0020, SRS-CONN-0018<br><br>## 4.5 Insight-Mode Activation over Connectivity<br><br>**SRS-CONN-0022** \| Device-Side Insight-Mode Activation on Command Receipt \| Upon receiving an Insight-mode activation command over the BLE link, the system **SHALL** activate Insight mode. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §7.1], [PRD §6.4] \| VM: Test \| XR: SRS-FUNC-0007, SRS-FUNC-0008, SRS-FUNC-0009<br><br>**SRS-CONN-0023** \| Mobile App Issuance of Insight-Mode Activation Command (external) \| The Mobile App **SHALL** issue the Insight-mode activation command to the collar-mounted device. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §7.1], [EXTERNAL: Mobile App team] \| VM: Inspection (external conformance evidence) \| XR: SRS-CONN-0022<br><br>## 4.6 GNSS Location Data Sync (Max Variant)<br><br>**SRS-CONN-0024** \| Sync of Location-Tagged Records via Standard Forwarding Path \| On the Max product variant, the system **SHALL** forward location-tagged classification records through the same record-forwarding path used for other classification records. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §7.5], [PRD §8] \| VM: Test \| XR: SRS-FUNC-0025, SRS-CONN-0011<br><br>**SRS-CONN-0025** \| Sync of Most-Recent GNSS Fix During Home Power-Gate \| While the GNSS smart power gate suspends fix acquisition in the home state, the system **SHALL** continue to sync the most recently acquired GNSS fix as part of classification records. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §7.5], [PRD §6.3] \| VM: Test \| XR: SRS-FUNC-0025, SRS-OPER-0004<br><br>## 4.7 Connectivity-Loss & Degraded Behavior<br><br>**SRS-CONN-0026** \| No Record Loss Due to Any Connectivity-Loss Condition \| The system **SHALL not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0017 |

<a id="srs-conn-0027"></a>

| **SRS-CONN-0027** | **Continued Local Classification During BLE Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon loss of the BLE link to all base stations, the system **SHALL** continue local classification and storage without interruption. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §7.6], [PRD §8.5] \| VM: Demonstration \| XR: SRS-FUNC-0028, SRS-FUNC-0027

**SRS-CONN-0028** \| Degraded-Mode Entry Below Home Wi-Fi Reliability Bound \| The system **SHALL** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. |
| **Rationale**    | Upon loss of the BLE link to all base stations, the system **SHALL** continue local classification and storage without interruption. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §7.6], [PRD §8.5] \| VM: Demonstration \| XR: SRS-FUNC-0028, SRS-FUNC-0027<br><br>**SRS-CONN-0028** \| Degraded-Mode Entry Below Home Wi-Fi Reliability Bound \| The system **SHALL** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007 |

<a id="srs-conn-0029"></a>

| **SRS-CONN-0029** | **Degraded-Mode Exit on Wi-Fi Reliability Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. |
| **Rationale**    | The system **SHALL** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007, SRS-CONN-0028 |


## 5. Ota Firmware Updates

<a id="srs-func-0043"></a>

| **SRS-FUNC-0043** | **OTA Capability Mandatory on All Collar Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). |
| **Rationale**    | The system **SHALL** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0034 |

<a id="srs-func-0044"></a>

| **SRS-FUNC-0044** | **OTA Capability Mandatory on All Base Station Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** provide over-the-air firmware update capability on every base station tier (Charging and Relay). |
| **Rationale**    | The system **SHALL** provide over-the-air firmware update capability on every base station tier (Charging and Relay). |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0043 |

<a id="srs-func-0045"></a>

| **SRS-FUNC-0045** | **Cloud-to-Base OTA Transport Protocol** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §9.2], [PRD §6.5], [PRD §11.2], [STD: ETSI EN 303 645:2025] \| VM: Test \| XR: SRS-CONN-0014

**SRS-FUNC-0046** \| Base Station Staging of Collar OTA Images \| The system **SHALL** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. |
| **Rationale**    | The system **SHALL** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §9.2], [PRD §6.5], [PRD §11.2], [STD: ETSI EN 303 645:2025] \| VM: Test \| XR: SRS-CONN-0014<br><br>**SRS-FUNC-0046** \| Base Station Staging of Collar OTA Images \| The system **SHALL** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0047 |

<a id="srs-func-0047"></a>

| **SRS-FUNC-0047** | **Base-to-Collar OTA Image Delivery Over Secured BLE Link** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. |
| **Rationale**    | The system **SHALL** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.2 · SRS-CONN-0009 |

<a id="srs-func-0048"></a>

| **SRS-FUNC-0048** | **Base Station Self-OTA Without User Action** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. |
| **Rationale**    | The system **SHALL** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §11.5 · SRS-FUNC-0044 |

<a id="srs-func-0049"></a>

| **SRS-FUNC-0049** | **Collar OTA Install Restricted to Charging-Cradle-Docked State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. |
| **Rationale**    | The system **SHALL** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0050, SRS-FUNC-0056 |

<a id="srs-func-0050"></a>

| **SRS-FUNC-0050** | **Docked-Install Gate Shall Not Be Remotely Bypassable** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. |
| **Rationale**    | The system **SHALL not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0049 |

<a id="srs-func-0051"></a>

| **SRS-FUNC-0051** | **Minimum Battery Reserve Before OTA Install** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §9.2], [PRD §10.4] \| VM: Test \| XR: SRS-FUNC-0049, SRS-FUNC-0057

## 5.4 OTA Image Integrity & Anti-Rollback




## 5.5 Install Resilience

**SRS-FUNC-0055** \| Atomic OTA Installation \| The system **SHALL** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. |
| **Rationale**    | The system **SHALL** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §9.2], [PRD §10.4] \| VM: Test \| XR: SRS-FUNC-0049, SRS-FUNC-0057<br><br>## 5.4 OTA Image Integrity & Anti-Rollback<br><br>**SRS-FUNC-0052** \| Minimum OTA Image Signature Strength \| The system **SHALL** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §9.3], [STD: ETSI EN 303 645:2025] \| VM: Inspection \| XR: SRS-FUNC-0053<br><br>**SRS-FUNC-0053** \| OTA Image Signature Verification Before Commit \| The system **SHALL** verify the signature of an OTA firmware image before committing or executing that image. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §9.3], [STD: ETSI EN 303 645:2025] \| VM: Test \| XR: SRS-FUNC-0052<br><br>**SRS-FUNC-0054** \| Anti-Rollback via Monotonic Version Counter \| The system **SHALL** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §9.3], [STD: EU CRA (EU) 2024/2847] \| VM: Test<br><br>## 5.5 Install Resilience<br><br>**SRS-FUNC-0055** \| Atomic OTA Installation \| The system **SHALL** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0056 |

<a id="srs-func-0056"></a>

| **SRS-FUNC-0056** | **Dual-Bank Auto-Revert on Boot Failure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §9.4], [PRD §11.5] \| VM: Test \| XR: SRS-FUNC-0055, SRS-FUNC-0057

**SRS-FUNC-0057** \| No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install \| The system **SHALL not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. |
| **Rationale**    | The system **SHALL** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §9.4], [PRD §11.5] \| VM: Test \| XR: SRS-FUNC-0055, SRS-FUNC-0057<br><br>**SRS-FUNC-0057** \| No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install \| The system **SHALL not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0051 |

<a id="srs-func-0058"></a>

| **SRS-FUNC-0058** | **Device-Side OTA Update State Reporting** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. |
| **Rationale**    | The system **SHALL** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.5 · SRS-FUNC-0059, SRS-FUNC-0060 |

<a id="srs-func-0059"></a>

| **SRS-FUNC-0059** | **App Notification of Available OTA Update (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **SHALL** notify the user when an OTA firmware update is available. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §9.5], [EXTERNAL: Mobile App team] \| VM: Inspection (external conformance evidence) \| XR: SRS-FUNC-0043, SRS-FUNC-0044


## 5.7 Release Artifacts & Tier-2 Delivery Channel

**SRS-FUNC-0061** \| SBOM Production Per OTA Release \| The system **SHALL** produce a Software Bill of Materials for every OTA firmware release. |
| **Rationale**    | The Mobile App **SHALL** notify the user when an OTA firmware update is available. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §9.5], [EXTERNAL: Mobile App team] \| VM: Inspection (external conformance evidence) \| XR: SRS-FUNC-0043, SRS-FUNC-0044<br><br>**SRS-FUNC-0060** \| App Display of OTA Update State (external) \| The Mobile App **SHALL** display the current OTA update state reported by the device. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §9.5], [EXTERNAL: Mobile App team] \| VM: Inspection (external conformance evidence) \| XR: SRS-FUNC-0058<br><br>## 5.7 Release Artifacts & Tier-2 Delivery Channel<br><br>**SRS-FUNC-0061** \| SBOM Production Per OTA Release \| The system **SHALL** produce a Software Bill of Materials for every OTA firmware release. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 |

<a id="srs-func-0062"></a>

| **SRS-FUNC-0062** | **Tier-2 Classifier Delivery Restricted to Embedded OTA Components** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. |
| **Rationale**    | The system **SHALL** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0034, SRS-FUNC-0035, SRS-FUNC-0052 |


## 6. Performance

<a id="srs-perf-0001"></a>

| **SRS-PERF-0001** | **Mini Variant Battery-Life Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's Mini variant **SHALL** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §12.1], [PRD §10.4], [—], [PRD §15.6] \| VM: Analysis \| XR: SRS-FUNC-0012, SRS-FUNC-0013


## 6.2 Classification & Data-Path Latency

**SRS-PERF-0003** \| Classification Latency Ceiling \| The system **SHALL** produce a classification result within 2 seconds of the triggering motion event. |
| **Rationale**    | The system's Mini variant **SHALL** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §12.1], [PRD §10.4], [—], [PRD §15.6] \| VM: Analysis \| XR: SRS-FUNC-0012, SRS-FUNC-0013<br><br>**SRS-PERF-0002** \| Max Variant Battery-Life Conformance \| The system's Max variant **SHALL** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval settings. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §12.1], [PRD §10.4], [—], [PRD §15.6] \| VM: Analysis \| XR: SRS-FUNC-0012, SRS-FUNC-0013<br><br>## 6.2 Classification & Data-Path Latency<br><br>**SRS-PERF-0003** \| Classification Latency Ceiling \| The system **SHALL** produce a classification result within 2 seconds of the triggering motion event. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-FUNC-0016 |

<a id="srs-perf-0004"></a>

| **SRS-PERF-0004** | **Base Station Cloud-Upload Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **SHALL** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. |
| **Rationale**    | The base station **SHALL** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-CONN-0014, SRS-CONN-0015 |

<a id="srs-perf-0005"></a>

| **SRS-PERF-0005** | **GNSS Time-to-First-Fix Ceiling (Warm, A-GPS)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **SHALL** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. |
| **Rationale**    | On the Max product variant, the system **SHALL** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 |

<a id="srs-perf-0006"></a>

| **SRS-PERF-0006** | **Collar Boot-Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar-mounted device **SHALL** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §12.1],  \| VM: Test \| XR: SRS-FUNC-0056

**SRS-PERF-0007** \| Home/Away Status Update Latency Ceiling \| The system **SHALL** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. |
| **Rationale**    | The collar-mounted device **SHALL** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. \| Priority: MEDIUM \| Stability: STABLE \| Source: [PRD §12.1],  \| VM: Test \| XR: SRS-FUNC-0056<br><br>**SRS-PERF-0007** \| Home/Away Status Update Latency Ceiling \| The system **SHALL** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-CONN-0004, SRS-CONN-0005 |

<a id="srs-perf-0008"></a>

| **SRS-PERF-0008** | **CCF Twist-Lock Engagement Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **SHALL** allow the Twist-Lock mechanism to be engaged within 5 seconds. |
| **Rationale**    | The system **SHALL** allow the Twist-Lock mechanism to be engaged within 5 seconds. |
| **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 |


## 7. Safety

<a id="srs-safe-0001"></a>

| **SRS-SAFE-0001** | **CCF-S Zone 2 Breakaway Force Window (Feline)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-S variant **SHALL** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)],  \| VM: Test \| XR: SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008



**SRS-SAFE-0004** \| CCF-L Force-Window Contingency for Assembled Mass Exceeding 26 g \| If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **SHALL** be revised upward to 30 N. |
| **Rationale**    | The Zone 2 Fuse Tab of the CCF-S variant **SHALL** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)],  \| VM: Test \| XR: SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008<br><br>**SRS-SAFE-0002** \| CCF-M Zone 2 Breakaway Force Window (Canine, Medium) \| The Zone 2 Fuse Tab of the CCF-M variant **SHALL** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)], ,  \| VM: Test \| XR: SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008<br><br>**SRS-SAFE-0003** \| CCF-L Zone 2 Breakaway Force Window (Canine, Large) \| The Zone 2 Fuse Tab of the CCF-L variant **SHALL** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device+CCF mass does not exceed 26 g. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §10.1.4], [PRD §13.2], [STD: EU GPSR (EU) 2023/988 Art 5 & Art 6(1)(a)], ,  \| VM: Test \| XR: SRS-SAFE-0004, SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008<br><br>**SRS-SAFE-0004** \| CCF-L Force-Window Contingency for Assembled Mass Exceeding 26 g \| If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **SHALL** be revised upward to 30 N. |
| **Priority**     | Critical |
| **Stability**    | Likely-change |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.4 · SRS-SAFE-0003 |

<a id="srs-safe-0005"></a>

| **SRS-SAFE-0005** | **Zone 2 Single-Use Restriction** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab **SHALL not** be capable of being reused or restored to a load-bearing state after fracture. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2] \| VM: Test \| XR: SRS-SAFE-0013

**SRS-SAFE-0006** \| Zone 2 No-Detached-Fragment on Fracture \| Upon fracture, the Zone 2 Fuse Tab **SHALL not** produce a detached fragment separate from the CCF body. |
| **Rationale**    | The Zone 2 Fuse Tab **SHALL not** be capable of being reused or restored to a load-bearing state after fracture. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2] \| VM: Test \| XR: SRS-SAFE-0013<br><br>**SRS-SAFE-0006** \| Zone 2 No-Detached-Fragment on Fracture \| Upon fracture, the Zone 2 Fuse Tab **SHALL not** produce a detached fragment separate from the CCF body. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b |

<a id="srs-safe-0007"></a>

| **SRS-SAFE-0007** | **Zone 2 Post-Fracture Surface Bluntness** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **SHALL** be blunt, presenting no sharp edge. |
| **Rationale**    | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **SHALL** be blunt, presenting no sharp edge. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b |

<a id="srs-safe-0008"></a>

| **SRS-SAFE-0008** | **Zone 2 Visible Fracture Indicator** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **SHALL** present a visible fracture indicator upon Zone 2 breakaway. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2] \| VM: Inspection \| XR: SRS-SAFE-0013

## 7.2 Zone 1 — Structural Retention (Non-Breakaway)


**SRS-SAFE-0010** \| Zone 1 Survival Through Zone 2 Fracture \| The Zone 1 clamp **SHALL** remain structurally intact following a Zone 2 fracture event. |
| **Rationale**    | The CCF **SHALL** present a visible fracture indicator upon Zone 2 breakaway. \| Priority: HIGH \| Stability: STABLE \| Source: [PRD §10.1.3.2b], [PRD §13.2] \| VM: Inspection \| XR: SRS-SAFE-0013<br><br>## 7.2 Zone 1 — Structural Retention (Non-Breakaway)<br><br>**SRS-SAFE-0009** \| Zone 1 Structural Retention Force \| The Zone 1 clamp **SHALL** retain axial loads of at least 50 N without structural failure. \| Priority: CRITICAL \| Stability: STABLE \| Source: [PRD §10.1.3.1], [PRD §10.1.3.4], [PRD §13.2] \| VM: Test \| XR: SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003<br><br>**SRS-SAFE-0010** \| Zone 1 Survival Through Zone 2 Fracture \| The Zone 1 clamp **SHALL** remain structurally intact following a Zone 2 fracture event. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-SAFE-0009, SRS-SAFE-0013 |

<a id="srs-safe-0011"></a>

| **SRS-SAFE-0011** | **Twist-Lock Axial Retention Force** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock device-to-CCF interface **SHALL** retain axial loads exceeding 100 N without disengaging. |
| **Rationale**    | The Twist-Lock device-to-CCF interface **SHALL** retain axial loads exceeding 100 N without disengaging. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-PERF-0008 \| Rationale: SAFE-0011 is the last mechanical line of defense preventing device separation from the wearer during a pet escape attempt. Failure of this retention means the device detaches entirely, losing all monitoring, safety tracking, and breakaway-event signaling. This aligns it with SRS-INT-0045 (§10) which already carries CRITICAL for the same >100 N requirement. |

<a id="srs-safe-0012"></a>

| **SRS-SAFE-0012** | **Twist-Lock Retention Under Pet-Motion Inertial Loading** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock **SHALL** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. |
| **Rationale**    | The Twist-Lock **SHALL** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-SAFE-0011 |

<a id="srs-safe-0013"></a>

| **SRS-SAFE-0013** | **No-Wear-Without-Intact-Zone-2** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device **SHALL not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. |
| **Rationale**    | The device **SHALL not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.6 · SRS-SAFE-0005, SRS-SAFE-0008 |

<a id="srs-safe-0014"></a>

| **SRS-SAFE-0014** | **Device Separation-Signature Emission** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device **SHALL** emit a detectable separation signature upon Zone 2 breakaway. |
| **Rationale**    | The device **SHALL** emit a detectable separation signature upon Zone 2 breakaway. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · SRS-SAFE-0015 |

<a id="srs-safe-0016"></a>

| **SRS-SAFE-0016** | **Zone 2 Non-Fracture Under Chew-Compressive Load** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab **SHALL not** fracture under a compressive load below 250 N. |
| **Rationale**    | The Zone 2 Fuse Tab **SHALL not** fracture under a compressive load below 250 N. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.2 · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-safe-0017"></a>

| **SRS-SAFE-0017** | **CCF Body Chew-Penetration Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF body **SHALL** resist penetration for at least 30 seconds under a 250 N compressive load. |
| **Rationale**    | The CCF body **SHALL** resist penetration for at least 30 seconds under a 250 N compressive load. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.2 |


## 8. Security

**CAT: SEC** | Maps to: PRD §6.7, §12.3; supporting anchor PRD §10.7

**Scope note:**  Supplies the "secured connection" referenced by SRS-CONN-0009 (§4) and SRS-FUNC-0047 (§5), closing both orphans. Does NOT restate §5 OTA signature/anti-rollback chain.

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)



## 8.2 Cloud-Bound Transport Security


## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

No firmware image MAY be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.

## 8.4 Device Identity & Platform Trust



## 8.5 Vulnerability Disclosure (pre-launch gate only)

**SRS-SEC-0006** | Public Vulnerability-Disclosure Policy in Place Before Launch | The system SHALL have a public vulnerability-disclosure policy in place before product launch. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.3], [PRD §13.5], [STD: ETSI EN 303 645:2025], [STD: EU CRA (EU) 2024/2847 Art 13-14] | Rationale: Published disclosure channel must exist at launch. Lifetime maintenance in §16. | VM: Inspection | XR: —

## 9. Data Requirements

<a id="srs-data-0001"></a>

| **SRS-DATA-0001** | **Classification Record Content** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. |
| **Rationale**    | The system SHALL generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0002"></a>

| **SRS-DATA-0002** | **Confidence Score Bound** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. |
| **Rationale**    | The system SHALL express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0003"></a>

| **SRS-DATA-0003** | **Record Timestamp Accuracy** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL timestamp each classification record with UTC time accurate to within 1 second. |
| **Rationale**    | The system SHALL timestamp each classification record with UTC time accurate to within 1 second. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0004"></a>

| **SRS-DATA-0004** | **GNSS Context on Max Variant** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max variant, the system SHALL append the most recent GNSS fix to the classification record. |
| **Rationale**    | On the Max variant, the system SHALL append the most recent GNSS fix to the classification record. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0005"></a>

| **SRS-DATA-0005** | **On-Device Storage Duration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. |
| **Rationale**    | The system SHALL retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5; PRD §10.6 |

<a id="srs-data-0006"></a>

| **SRS-DATA-0006** | **Retention Through Power Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL preserve stored classification records without corruption across a power-loss event. |
| **Rationale**    | The system SHALL preserve stored classification records without corruption across a power-loss event. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.6 |

<a id="srs-data-0007"></a>

| **SRS-DATA-0007** | **Storage Corruption Detection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL detect corruption of stored classification records prior to transmission. |
| **Rationale**    | The system SHALL detect corruption of stored classification records prior to transmission. |
| **Priority**     | High |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | PRD §10.6 |

<a id="srs-data-0008"></a>

| **SRS-DATA-0008** | **Classification Independent of Connectivity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL perform classification and record generation independent of BLE connectivity state. |
| **Rationale**    | The system SHALL perform classification and record generation independent of BLE connectivity state. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |

<a id="srs-data-0009"></a>

| **SRS-DATA-0009** | **Record Forwarding Without Corruption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL forward stored classification records to the transport layer without introducing data corruption. |
| **Rationale**    | The system SHALL forward stored classification records to the transport layer without introducing data corruption. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |

<a id="srs-data-0010"></a>

| **SRS-DATA-0010** | **Record Forwarding Without Sequence Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL forward stored classification records to the transport layer in chronological sequence without gaps. |
| **Rationale**    | The system SHALL forward stored classification records to the transport layer in chronological sequence without gaps. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |

<a id="srs-data-0011"></a>

| **SRS-DATA-0011** | **Raw Sensor Data Transmission Boundary** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL not transmit raw accelerometer data beyond the collar. |
| **Rationale**    | The system SHALL not transmit raw accelerometer data beyond the collar. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.7 |

<a id="srs-data-0012"></a>

| **SRS-DATA-0012** | **On-Device Normalization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL perform normalization of sensor data on-device prior to classification. |
| **Rationale**    | The system SHALL perform normalization of sensor data on-device prior to classification. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §7.7 |

<a id="srs-data-0013"></a>

| **SRS-DATA-0013** | **No Cloud Round-Trip for Classification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL not require a cloud round-trip to complete a classification decision. |
| **Rationale**    | The system SHALL not require a cloud round-trip to complete a classification decision. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.7 |

<a id="srs-data-0014"></a>

| **SRS-DATA-0014** | **Raw Sample Retention Minimization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. |
| **Rationale**    | The system SHALL limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. |
| **Priority**     | Medium |
| **Stability**    | Likely-change |
| **Verification** | Analysis |
| **Traceability** | PRD §7.7; STD: RM-0015 §Art.25 |

<a id="srs-data-0015"></a>

| **SRS-DATA-0015** | **Buffered Data Retention Until Acknowledgement** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. |
| **Rationale**    | The system SHALL retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 |

<a id="srs-data-0016"></a>

| **SRS-DATA-0016** | **No Buffer Clear on Disconnect Alone** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL not clear the buffered-data queue solely as a result of a BLE disconnect event. |
| **Rationale**    | The system SHALL not clear the buffered-data queue solely as a result of a BLE disconnect event. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 |

<a id="srs-data-0017"></a>

| **SRS-DATA-0017** | **Stale-Data Flag on Delayed Upload** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL flag a buffered record as stale when it is uploaded outside its original chronological order. |
| **Rationale**    | The system SHALL flag a buffered record as stale when it is uploaded outside its original chronological order. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.7 |

<a id="srs-data-0018"></a>

| **SRS-DATA-0018** | **Data Minimization for Personal Data** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. |
| **Rationale**    | The system SHALL limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. |
| **Priority**     | High |
| **Stability**    | Likely-change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.5(1)(c) |

<a id="srs-data-0019"></a>

| **SRS-DATA-0019** | **Purpose Limitation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. |
| **Rationale**    | The system SHALL restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.5(1)(b) |

<a id="srs-data-0020"></a>

| **SRS-DATA-0020** | **On-Device Data Deletion Support** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL support deletion of on-device stored personal data upon an authenticated owner-initiated request. |
| **Rationale**    | The system SHALL support deletion of on-device stored personal data upon an authenticated owner-initiated request. |
| **Priority**     | Medium |
| **Stability**    | Likely-change |
| **Verification** | Demonstration |
| **Traceability** | STD: RM-0015 §Art.17 |

<a id="srs-data-0021"></a>

| **SRS-DATA-0021** | **On-Device Data Access Support** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL support retrieval of on-device stored personal data upon an authenticated owner-initiated request. |
| **Rationale**    | The system SHALL support retrieval of on-device stored personal data upon an authenticated owner-initiated request. |
| **Priority**     | Medium |
| **Stability**    | Likely-change |
| **Verification** | Demonstration |
| **Traceability** | STD: RM-0015 §Art.15 |

<a id="srs-data-0022"></a>

| **SRS-DATA-0022** | **Consumer Privacy Rights Contingency (CCPA/CPRA)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system SHALL support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. |
| **Rationale**    | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system SHALL support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. |
| **Priority**     | Low |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0017 |

<a id="srs-data-0023"></a>

| **SRS-DATA-0023** | **Data-at-Rest Encryption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. |
| **Rationale**    | The system SHALL encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.32; STD: RM-0019 §Prov.5.8 |

<a id="srs-data-0024"></a>

| **SRS-DATA-0024** | **Transport to Cloud Device-Management Layer** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. |
| **Rationale**    | The system SHALL transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.1; ASSUMPTION: A-0015 |

<a id="srs-data-0025"></a>

| **SRS-DATA-0025** | **Breakaway Record Commit Timing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL commit a breakaway event record to persistent storage within 5 seconds of separation detection. |
| **Rationale**    | The system SHALL commit a breakaway event record to persistent storage within 5 seconds of separation detection. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0018 |

<a id="srs-data-0026"></a>

| **SRS-DATA-0026** | **Breakaway Record Survivability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL preserve a committed breakaway event record across power loss, battery depletion, and device reboot. |
| **Rationale**    | The system SHALL preserve a committed breakaway event record across power loss, battery depletion, and device reboot. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0018 |

<a id="srs-data-0027"></a>

| **SRS-DATA-0027** | **Breakaway Record Transmission Trigger** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL transmit a committed breakaway event record on the next successful base-station contact following separation. |
| **Rationale**    | The system SHALL transmit a committed breakaway event record on the next successful base-station contact following separation. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0018 |


## 10. Interface Requirements

<a id="srs-int-0001"></a>

| **SRS-INT-0001** | **Collar BLE Peripheral Role** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL implement the Bluetooth Low Energy (BLE) 5.x radio interface in the peripheral role. |
| **Rationale**    | The collar is the advertising/connectable endpoint of the collar-to-base-station link; role assignment is imposed by the system architecture. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0002"></a>

| **SRS-INT-0002** | **Base Station BLE Central Role** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL implement the BLE 5.x radio interface in the central role. |
| **Rationale**    | The base station scans for and initiates connections to collar devices; role assignment is imposed by the system architecture. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §11.2 · SRS-INT-0001 |

<a id="srs-int-0003"></a>

| **SRS-INT-0003** | **Minimum Concurrent Collar Sessions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL support at least 4 concurrent BLE connections to collar devices. |
| **Rationale**    | A multi-pet household requires the base station to hold multiple simultaneous collar links without dropping connections. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0004"></a>

| **SRS-INT-0004** | **Default BLE Advertising Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL advertise via BLE with a default advertising interval of 60 seconds. |
| **Rationale**    | Establishes the out-of-box discoverability cadence balancing power consumption against connection latency. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0005"></a>

| **SRS-INT-0005** | **Configurable BLE Advertising Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. |
| **Rationale**    | Allows the advertising cadence to be tuned for household-specific power/latency trade-offs. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0006"></a>

| **SRS-INT-0006** | **Advertising Continuity During Active Connection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL continue BLE advertising while maintaining an active BLE connection. |
| **Rationale**    | Preserves discoverability for additional base stations in a multi-base household while a collar is already connected to one base station. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0007"></a>

| **SRS-INT-0007** | **BLE Address Randomization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL randomize its BLE device address. |
| **Rationale**    | Prevents long-term tracking of the wearable by third parties observing BLE advertisements. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0008"></a>

| **SRS-INT-0008** | **Minimum BLE Transmit Power** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL transmit BLE signals at a power level of at least +8 dBm. |
| **Rationale**    | A minimum TX power floor is necessary to meet the stated open-air range target. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-INT-0009, SRS-HW-0019 |

<a id="srs-int-0009"></a>

| **SRS-INT-0009** | **Minimum BLE Open-Air Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE link between the collar device and the base station SHALL maintain connectivity at an open-air separation distance of at least 9 meters. |
| **Rationale**    | Defines the minimum usable range for typical household room-to-room and yard-adjacent operation. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-INT-0008 |

<a id="srs-int-0010"></a>

| **SRS-INT-0010** | **BLE Link-Layer Encryption Algorithm** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL encrypt all BLE data-bearing links using AES-128 CCM. |
| **Rationale**    | Mandated link-layer confidentiality/integrity mechanism for all collar-to-base-station traffic. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0011"></a>

| **SRS-INT-0011** | **BLE Pairing via LE Secure Connections** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL establish BLE pairing between the collar device and the base station using LE Secure Connections. |
| **Rationale**    | Provides the pairing-time key-exchange mechanism underpinning the mandated link-layer encryption. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-INT-0010 |

<a id="srs-int-0012"></a>

| **SRS-INT-0012** | **QR Out-of-Band Pairing Mechanism** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station. |
| **Rationale**    | Defines the device/base-station-side OOB pairing mechanism; the mobile app's presentation of the QR code to the user is out of scope for this SRS and is attributed to the (out-of-scope) Mobile App per the standing scope boundary. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0013"></a>

| **SRS-INT-0013** | **BLE Radio Regulatory Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface SHALL conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US), [STD: RED 2014/53/EU] (EU), [STD: UK Radio Equipment Regulations 2017] (UK), [STD: ISED RSS-247] (CA), and [STD: AS/NZS 4268:2017] (AU/NZ). |
| **Rationale**    | Market access for an intentional 2.4 GHz radiator requires conformance to each target market's radio-equipment regulation. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0014"></a>

| **SRS-INT-0014** | **Bluetooth SIG Qualification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface SHALL hold a Bluetooth SIG Qualified Design ID (QDID). |
| **Rationale**    | Bluetooth SIG membership terms mandate qualification of any BLE product before market release. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: Bluetooth SIG Qualification (QDID) |

<a id="srs-int-0015"></a>

| **SRS-INT-0015** | **RF Human-Exposure Assessment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface SHOULD undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4 GHz transmission. |
| **Rationale**    | A continuously worn 2.4 GHz transmitter plausibly triggers per-market RF-exposure assessment; applicability and thresholds are per-market INDICATIVE per the Regulatory Map and not yet CONFIRMED, hence a SHOULD rather than SHALL. |
| **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0016"></a>

| **SRS-INT-0016** | **Wi-Fi Radio Band and Standard** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n]. |
| **Rationale**    | Defines the base-to-cloud uplink radio band and PHY/MAC standard. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 |

<a id="srs-int-0017"></a>

| **SRS-INT-0017** | **Cloud Uplink Transport Encryption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. |
| **Rationale**    | Mandated transport-layer confidentiality/integrity mechanism for base-station-to-cloud traffic; the device/base-station side of this transport is in scope, cloud-side storage/analytics is out of scope [ASSUMPTION A-0015]. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.5 |

<a id="srs-int-0018"></a>

| **SRS-INT-0018** | **Default Access-Point Configuration Compatibility** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. |
| **Rationale**    | Avoids requiring the owner to perform non-default router configuration for base-station setup. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.6 |

<a id="srs-int-0019"></a>

| **SRS-INT-0019** | **Minimum Wi-Fi Uplink Signal Condition** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. |
| **Rationale**    | Resolves the PRD's unbounded "reliable Wi-Fi" assumption with an engineered numeric floor; below this bound the ≥30-day offline buffering behavior (Data Requirements, §9) is the defined degraded-mode fallback rather than a new interface requirement. |
| **Priority**     | Medium |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | ASSUMPTION A-0009 |

<a id="srs-int-0020"></a>

| **SRS-INT-0020** | **Wi-Fi Radio Regulatory Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Wi-Fi radio interface SHALL conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US) and [STD: RED 2014/53/EU] (EU). |
| **Rationale**    | Market access for the base station's Wi-Fi radio requires conformance to each target market's radio-equipment regulation. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0021"></a>

| **SRS-INT-0021** | **GNSS Interface Presence on Max** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL implement a passive (receive-only) GNSS interface. |
| **Rationale**    | GNSS is a defining differentiator of the Max variant, providing location context unavailable on Mini. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0022"></a>

| **SRS-INT-0022** | **GNSS Interface Absence on Mini** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar variant SHALL not implement a GNSS interface. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet its ≤10 g weight budget and BLE-only positioning. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0023"></a>

| **SRS-INT-0023** | **Configurable GNSS Fix Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. |
| **Rationale**    | Allows the fix cadence to be tuned against the battery-life-vs-fix-interval trade-off documented in the PRD. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0024"></a>

| **SRS-INT-0024** | **Default GNSS Fix Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL apply a default GNSS fix interval of 2 hours. |
| **Rationale**    | Establishes the out-of-box fix cadence consistent with the stated ≥45-day @2h battery-life target. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0025"></a>

| **SRS-INT-0025** | **A-GPS Assistance Data Delivery** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. |
| **Rationale**    | A-GPS delivery over the existing BLE link is the defined mechanism for reducing GNSS fix acquisition time. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0026"></a>

| **SRS-INT-0026** | **A-GPS Assistance Data Validity Window** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. |
| **Rationale**    | Bounds how long stale assistance data MAY be relied upon before fix-acquisition performance degrades. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0027"></a>

| **SRS-INT-0027** | **GNSS Power Gating During HOME State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL disable the GNSS interface while the device-local home/away state machine determines the HOME state. |
| **Rationale**    | The GNSS smart power gate underpins the stated Max battery-longevity targets; gating authority rests solely with the device-local state machine per the confirmed in-scope/external boundary. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 · SRS-OPER-0004 |

<a id="srs-int-0028"></a>

| **SRS-INT-0028** | **GNSS Fix Acquisition Timeout** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. |
| **Rationale**    | Bounds the power expenditure of an unsuccessful fix attempt. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0029"></a>

| **SRS-INT-0029** | **Warm GNSS Time-to-First-Fix Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant SHALL acquire a warm GNSS fix using A-GPS assistance within 60 seconds. |
| **Rationale**    | Bounds the latency between a scheduled fix attempt and an available location result. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-INT-0025 |

<a id="srs-int-0030"></a>

| **SRS-INT-0030** | **GNSS Intentional-Radiator Exemption Status** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The GNSS receive-only interface SHOULD be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. |
| **Rationale**    | The PRD defers this exemption determination to Regulatory Lead confirmation per market; the Regulatory Map carries this as INDICATIVE, not CONFIRMED, hence a SHOULD rather than SHALL pending resolution. |
| **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0031"></a>

| **SRS-INT-0031** | **Pogo-Pin Contact Count and Function** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) SHALL use a 2-contact pogo-pin arrangement carrying VBUS and GND. |
| **Rationale**    | Defines the minimal electrical contact interface for charging; cross-variant identical geometry is already established by SRS-COMP-0003. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.5 · SRS-COMP-0003 |

<a id="srs-int-0032"></a>

| **SRS-INT-0032** | **Magnetic Charging Alignment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging interface SHALL employ magnetic alignment to seat the collar device onto the charging contacts. |
| **Rationale**    | Magnetic alignment enables reliable tool-free docking without precise manual contact placement. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.6 |

<a id="srs-int-0033"></a>

| **SRS-INT-0033** | **First-Attempt Docking Seating Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The magnetic charging alignment SHALL achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. |
| **Rationale**    | Bounds the usability of the magnetic docking mechanism to a measurable success rate. Note: this magnetic assist governs the charging-dock (collar device onto charging cradle) interface and is distinct from the device-to-CCF Twist-Lock engagement assist in SRS-INT-0049, though both specify an "up to 5 mm" approach distance. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.5 · SRS-INT-0049 |

<a id="srs-int-0034"></a>

| **SRS-INT-0034** | **Full-Charge Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL reach full charge within 2 hours when docked at the charging interface. |
| **Rationale**    | Bounds the time an owner must leave a device docked to restore full charge. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.5 |

<a id="srs-int-0035"></a>

| **SRS-INT-0035** | **IP67 Rating When Undocked** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. |
| **Rationale**    | The exposed pogo-pin contact is a potential ingress path and must not compromise the device-standalone IP67 rating. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.6 · SRS-HW-0004 |

<a id="srs-int-0036"></a>

| **SRS-INT-0036** | **Charging Socket Self-Drainage** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging socket SHALL drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state the socket "SHALL be self-draining" with no quantified acceptance criterion; the Verification-Method Validator flagged this as method/criterion incoherence — the declared Test method (correctly changed from Inspection) had nothing measurable to test against.  resolves this gap (engineered by analogy to A-0007). This requirement shares its underlying drainage claim with SRS-HW-0008 (§11, hardware-geometry framing of the same socket); both corrected together. |
| **Priority**     | Medium |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | PRD §10.5 · SRS-HW-0008 |

<a id="srs-int-0037"></a>

| **SRS-INT-0037** | **Charging-Access Removal Rotation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. |
| **Rationale**    | Defines the workflow by which the charging contacts are exposed for docking, using the non-breakaway Twist-Lock mechanism. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.6 · SRS-INT-0039 |

<a id="srs-int-0038"></a>

| **SRS-INT-0038** | **Device-Absent Socket Entrapment Geometry** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The exposed Twist-Lock/charging socket, when the collar device is absent, SHALL not admit a 12 mm probe to a depth that creates a snag or entrapment feature. |
| **Rationale**    | Resolves the PRD's unbounded "no independent entrapment hazard" statement with an engineered geometric probe criterion. |
| **Priority**     | High |
| **Stability**    | Likely-change |
| **Verification** | Test |
| **Traceability** | ASSUMPTION A-0010 |

<a id="srs-int-0039"></a>

| **SRS-INT-0039** | **Bayonet Lug Configuration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock mechanical interface SHALL use a 3-lug bayonet arrangement spaced at 120 degrees. |
| **Rationale**    | Defines the base geometric arrangement of the device-to-CCF mechanical attachment; identical across Mini/Max per SRS-COMP-0003. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a · SRS-COMP-0003 |

<a id="srs-int-0040"></a>

| **SRS-INT-0040** | **Lock/Unlock Rotation Angle** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock mechanical interface SHALL engage and release via a 90-degree rotation. |
| **Rationale**    | Defines the actuation travel required to lock or unlock the device from the CCF. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0041"></a>

| **SRS-INT-0041** | **Lug Ramp Self-Locking Profile** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock lug ramp SHALL have a trapezoidal profile with an 8-degree self-locking angle. |
| **Rationale**    | The ramp angle is imposed to achieve self-locking behavior without requiring a separate latch. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0042"></a>

| **SRS-INT-0042** | **Twist-Lock Lug Dimensions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each Twist-Lock lug SHALL be 4.0 mm wide by 1.2 mm thick. |
| **Rationale**    | Fixed lug dimensions are required for interoperability across all CCF SKUs and both collar variants. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0043"></a>

| **SRS-INT-0043** | **Asymmetric Keying Lug** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct engagement orientation. |
| **Rationale**    | Prevents incorrect-orientation assembly of the device onto the CCF. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0044"></a>

| **SRS-INT-0044** | **Detent Release Torque Window** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock detent SHALL release within a torque window of 0.08 to 0.10 N·m. |
| **Rationale**    | Bounds the rotational effort at which the detent yields, balancing inadvertent-release resistance against ease of intentional removal; upper bound narrowed from 0.15 N·m to 0.10 N·m to align with SRS-INT-0047's engage/release torque ceiling, per PRD §10.1.3.2a's intent that detent release remain at or below the engage torque ceiling. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-INT-0047 |

<a id="srs-int-0045"></a>

| **SRS-INT-0045** | **Twist-Lock Axial Retention Floor** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL withstand an axial pull-off force greater than 100 N without releasing. |
| **Rationale**    | The Twist-Lock is explicitly not a breakaway mechanism; it must retain the device under normal and inertial loading (distinct from the Zone 2 Fuse Tab, which is governed under Safety Requirements). |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 |

<a id="srs-int-0046"></a>

| **SRS-INT-0046** | **Twist-Lock Engagement Insertion Force Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL require no more than 5 N of axial press-in force to engage. |
| **Rationale**    | Bounds the physical effort required of the owner during the engagement workflow. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 |

<a id="srs-int-0047"></a>

| **SRS-INT-0047** | **Twist-Lock Engagement Rotation Torque Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL require no more than 0.10 N·m of rotational torque to engage or release. |
| **Rationale**    | Bounds the rotational effort required of the owner during the engage/remove workflow. Priority raised MEDIUM→HIGH (—) so this governing torque ceiling is at least as critical as the dependent detent-release window (SRS-INT-0044, HIGH) that is bounded by it. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 · SRS-INT-0044 |

<a id="srs-int-0048"></a>

| **SRS-INT-0048** | **Engagement Feedback** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL provide an audible and tactile click upon full engagement. |
| **Rationale**    | Confirms to the owner that the device has reached the fully locked position without requiring visual inspection. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0049"></a>

| **SRS-INT-0049** | **Magnetic Engagement Assist Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL provide magnetic engagement assistance effective at an approach distance of up to 5 mm. |
| **Rationale**    | Assists initial alignment of the device onto the CCF socket before rotation. Note: this Twist-Lock (device-to-CCF) magnetic engagement assist is distinct from the charging-dock magnetic alignment in SRS-INT-0033, though both specify an "up to 5 mm" approach distance. |
| **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-INT-0033 |

<a id="srs-int-0050"></a>

| **SRS-INT-0050** | **Tool-Free Twist-Lock Operation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL be operable without tools. |
| **Rationale**    | Owners must be able to engage and remove the device without specialized equipment. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0051"></a>

| **SRS-INT-0051** | **Twist-Lock Engagement Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface SHALL be engageable within 5 seconds. |
| **Rationale**    | Bounds the time required to complete the mechanical engagement step of the CCF-install workflow. |
| **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 |

<a id="srs-int-0052"></a>

| **SRS-INT-0052** | **Common Device-Enforced Protocol Across Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system SHALL use a common device-enforced BLE application protocol shared across all collar and base-station firmware variants. |
| **Rationale**    | A single shared protocol avoids per-variant protocol fragmentation and depends on the protocol/ICD being frozen before verification per A-0001. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0001 |

<a id="srs-int-0053"></a>

| **SRS-INT-0053** | **Payload Type — Behavioral Classification Record** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol SHALL support transport of behavioral classification records as a distinct payload type. |
| **Rationale**    | Behavioral records are the primary data product synced from collar to base station and require an identifiable payload type. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-int-0054"></a>

| **SRS-INT-0054** | **Payload Type — BLE Sighting Report** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol SHALL support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (RSSI), timestamp, and base station identifier, as a distinct payload type. |
| **Rationale**    | Sighting reports are the data basis for home/away geo-fence determination and are reported independent of behavioral-data sync. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 |

<a id="srs-int-0055"></a>

| **SRS-INT-0055** | **Payload Type — Cloud Downlink** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol SHALL support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type. |
| **Rationale**    | Downlink configuration and OTA image delivery are distinct data flows from the collar-to-base uplink and require their own payload type. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.6 |

<a id="srs-int-0056"></a>

| **SRS-INT-0056** | **Base Station Payload Content Opacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station SHALL relay collar behavioral payloads to the cloud without semantically interpreting their content. |
| **Rationale**    | Keeps behavioral-data interpretation logic on the collar/cloud endpoints only, avoiding base-station firmware dependency on payload semantics; verification method corrected from Test to Inspection because this is a negative architectural claim (absence of interpretation logic) that black-box behavioral testing cannot conclusively prove — a base station could interpret payload content internally and still relay it correctly, defeating a Test-based check. Design/firmware/code review confirming no semantic-parsing logic exists on the relay path is the appropriate method. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.3 |

<a id="srs-int-0057"></a>

| **SRS-INT-0057** | **Collar Buffer Retention Pending Acknowledgment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the base station. |
| **Rationale**    | Prevents data loss from premature buffer clearing before successful delivery is confirmed. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 |

<a id="srs-int-0058"></a>

| **SRS-INT-0058** | **No FIFO Clear on Disconnect Alone** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. |
| **Rationale**    | A disconnection is not itself confirmation of delivery; clearing on disconnect alone would risk silent data loss. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 · SRS-INT-0057 |

<a id="srs-int-0059"></a>

| **SRS-INT-0059** | **Sequence-Loss Detection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol SHALL include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. |
| **Rationale**    | Enables the receiving side to detect gaps in the forwarded record stream without depending on a specific transport-level guarantee. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |

<a id="srs-int-0060"></a>

| **SRS-INT-0060** | **Corruption-Free Record Forwarding** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol SHALL forward classification records over BLE without introducing data corruption. |
| **Rationale**    | Ensures the integrity of behavioral data is preserved end-to-end across the BLE hop. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |


## 11. Hardware Physical Mechanical

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

---

## 12. Environmental Durability

# §12 — Environmental & Durability Requirements

CAT: **ENV** | Maps to: PRD §12.5 (Durability), §13.4 (Env/ingress) | Cross-refs: PRD §10.1.2 (materials), §10.1.3 (CCF architecture), §13.2 (pet-safety materials)

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

## 13. Reliability Availability

# §13 — Reliability & Availability Requirements

CAT: **RELI** | Maps to: PRD §12.2 (Reliability) | Cross-refs: PRD §10.1.2/§13.4 (IP67), PRD §7.4 (classification accuracy), PRD §9 (OTA), PRD §11.7 (base station continuous operation)

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

---

## 14. Usability

<a id="srs-ux-0001"></a>

| **SRS-UX-0001** | **The collar device SHALL complete BLE pairing and first-data-sync handshake with** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL complete BLE pairing and first-data-sync handshake with a companion app within 3 minutes of the user initiating pairing mode on the device, measured from pairing-mode-entry LED indication to app-confirmed-paired acknowledgment. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §12.4 · — |

<a id="srs-ux-0002"></a>

| **SRS-UX-0002** | **The collar device SHALL support QR-code-based out-of-band (OOB) pairing as the p** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL support QR-code-based out-of-band (OOB) pairing as the primary pairing method, providing a scannable QR code (on device label or base-station label) that encodes the device identity for LE Secure Connections OOB pairing.                             \| CAT=UX PRIORITY=HIGH STABILITY=FIXED **VM=Demonstration** Source: \[PRD §5.6] \[STD: Bluetooth SIG LE Secure Connections] **XR: SRS-CONN-0003** \|
\| **SRS-UX-0003** \| The collar device SHALL provide a single, visually distinct, and user-accessible physical mechanism (e.g., a recessed or guarded button) to initiate pairing mode, with the mechanism clearly labeled or icon-indicated on the device enclosure. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Inspection |
| **Traceability** | PRD §5.6 · — |

<a id="srs-ux-0004"></a>

| **SRS-UX-0004** | **The collar device LED SHALL emit a visually distinct indication when the device** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device LED SHALL emit a visually distinct indication when the device is in pairing mode (e.g., slow blue blink at 1 Hz, 50% duty cycle) that is distinguishable from all power-on/boot, normal-operation, low-battery, charging, fault, and OTA-state LED patterns defined in §14.3. \| CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test                                                                 \|
\| 
---

### 14.2 Physical Interaction

\| ID              \| Requirement                                                                                                                                                                                                                                                             \| Attributes                                                               \|
\| :-------------- \| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- \| :----------------------------------------------------------------------- \|
\| **SRS-UX-0006** \| The Twist-Lock mechanism SHALL provide both an audible click and a tactile force-transition (detent drop) upon successful locking, enabling the user to confirm engagement by sound and feel without visual inspection. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · — |

<a id="srs-ux-0007"></a>

| **SRS-UX-0007** | **The Twist-Lock socket SHALL provide a magnetic-assist force that draws the devic** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock socket SHALL provide a magnetic-assist force that draws the device into correct alignment from a distance of ≤5 mm before the lug channels engage, reducing the fine-motor-skill demand of device docking. |
| **Rationale**    | — |
| **Priority**     | Medium |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · — |

<a id="srs-ux-0008"></a>

| **SRS-UX-0008** | **The Twist-Lock engage force SHALL not exceed 5 N press-in axial force and 0** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock engage force SHALL not exceed 5 N press-in axial force and 0.10 N·m rotational torque, enabling a typical adult user to dock the device without a tool or excessive effort. Mechanical specification per §11. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · — |

<a id="srs-ux-0009"></a>

| **SRS-UX-0009** | **The device removal workflow (90° counter-clockwise Twist-Lock rotation) SHALL re** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device removal workflow (90° counter-clockwise Twist-Lock rotation) SHALL require a detent-release torque not exceeding 0.15 N·m, such that an adult user can intentionally remove the device without a tool while the mechanism remains inertially immune per §11. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · — |

<a id="srs-ux-0010"></a>

| **SRS-UX-0010** | **The magnetic pogo-pin charging connector SHALL achieve ≥90% first-attempt succes** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The magnetic pogo-pin charging connector SHALL achieve ≥90% first-attempt successful seating rate by a user with no prior training, measured in a usability test with a representative sample of ≥20 adult participants across age and dexterity ranges. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.5 · — |

<a id="srs-ux-0011"></a>

| **SRS-UX-0011** | **The Twist-Lock asymmetric lug keying SHALL physically prevent incorrect-orientat** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock asymmetric lug keying SHALL physically prevent incorrect-orientation insertion of the device into the CCF socket, providing error-proof (poka-yoke) mating. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · — |

<a id="srs-ux-0012"></a>

| **SRS-UX-0012** | **The collar device LED SHALL communicate at minimum the following distinct operat** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device LED SHALL communicate at minimum the following distinct operational states to the user: (a) power-on / boot, (b) pairing mode, (c) normal operation, (d) low battery (≤20% SoC), (e) charging / docked, (f) error or fault, and (g) OTA update in progress. LED physical specification per §11.                                        \| CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test       \|
\| \| \| 
---

### 14.4 Base Station UX

\| ID              \| Requirement                                                                                                                                                                                                                                                                        \| Attributes                                                                             \|
\| :-------------- \| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- \| :------------------------------------------------------------------------------------- \|
\| **SRS-UX-0016** \| The base station SHALL communicate via LEDs at minimum: (a) AC power present, (b) device charging active (Charging tier only), (c) cloud connectivity established, and (d) OTA update in progress. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §11.6 · — |

<a id="srs-ux-0017"></a>

| **SRS-UX-0017** | **The base station LEDs SHOULD support an automatic ambient-light-responsive dimmi** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station LEDs SHOULD support an automatic ambient-light-responsive dimming mode below approximately 50 lux, or a user-configurable quiet-hours schedule, to reduce bedroom/nighttime light intrusion. |
| **Rationale**    | — |
| **Priority**     | Low |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §11.6 · — |

<a id="srs-ux-0018"></a>

| **SRS-UX-0018** | **The base station initial setup — from AC power-on through Wi-Fi association and** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station initial setup — from AC power-on through Wi-Fi association and cloud-registration to the "cloud-connected" LED indication — SHALL complete within 5 minutes for a user following the companion app's guided setup flow, assuming compliant home Wi-Fi per A-0009. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §12.4 · — |

<a id="srs-ux-0019"></a>

| **SRS-UX-0019** | **Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type sub-variant** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type sub-variants) SHALL be visually and/or tactilely distinguishable from all other variants by at minimum one of: molded-in size designation, distinct body color, or tactile surface differentiation, enabling a user to identify the correct CCF for their pet without measurement tools. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Inspection |
| **Traceability** | PRD §12.4 · — |

<a id="srs-ux-0020"></a>

| **SRS-UX-0020** | **The CCF Zone 1 structural-clamp installation onto a third-party collar SHALL be** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF Zone 1 structural-clamp installation onto a third-party collar SHALL be achievable by a typical adult user in ≤60 seconds without tools, using only the wrap-and-lock mechanism described in PRD §10.1.3.4. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §12.4 · — |

<a id="srs-ux-0021"></a>

| **SRS-UX-0021** | **The CCF Zone 2 fuse tab SHALL incorporate a clearly visible fracture indicator (** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF Zone 2 fuse tab SHALL incorporate a clearly visible fracture indicator (e.g., a contrasting-color internal layer exposed on fracture, or a continuous visual element that visibly separates) that is discernible by a user at arm's length (approximately 60 cm) under typical indoor lighting without magnification, enabling the user to visually confirm post-breakaway that the CCF must be replaced. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b · — |

<a id="srs-ux-0022"></a>

| **SRS-UX-0022** | **The collar device SHALL provide a distinct low-battery LED indication (visually** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL provide a distinct low-battery LED indication (visually distinct from normal operation per SRS-UX-0013) when the battery state-of-charge reaches ≤20%, and SHALL persist this indication in every operational state until the device is placed on the charger and charging is confirmed. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · — |

<a id="srs-ux-0023"></a>

| **SRS-UX-0023** | **The collar device SHALL communicate a fault state (including but not limited to:** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL communicate a fault state (including but not limited to: sensor failure, non-volatile memory corruption, BLE radio initialization failure) via a visually distinct LED pattern that differs from all power-on/boot, normal-operation, low-battery, pairing, charging, and OTA-state patterns.                        \| CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test                      \|
\| 
---

### 14.7 App-Interface Obligations

> The companion app is delivered by the Mobile App team \[EXTERNAL: Mobile App team]. The requirements in this subsection specify the device-side and base-station-side interface obligations that enable the app's user-facing features. These are in-scope for our delivery.

\| ID              \| Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         \| Attributes                                                                                               \|
\| :-------------- \| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- \| :------------------------------------------------------------------------------------------------------- \|
\| **SRS-UX-0025** \| The collar device SHALL include its current battery state-of-charge as a percentage value (0–100) in every sync payload transmitted to the base station, enabling the companion app to display an accurate, real-time battery estimate to the owner. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §12.4 · — |

<a id="srs-ux-0026"></a>

| **SRS-UX-0026** | **The Max collar device SHALL include the current GNSS fix interval setting (in mi** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar device SHALL include the current GNSS fix interval setting (in minutes) in its status payload transmitted in every sync, enabling the companion app to compute and display an interval-aware battery-life estimate and to issue the Max <10-day battery warning. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §12.4 · — |

<a id="srs-ux-0027"></a>

| **SRS-UX-0027** | **The collar device SHALL transmit a persistent breakaway/separation event record** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL transmit a persistent breakaway/separation event record as defined in A-0018, flagged with elevated transmission priority, on the next successful base-station contact following a breakaway event, enabling the companion app's "CCF Replacement Required" owner notification. The primary post-breakaway safety mitigation remains the passive CCF visible fracture indicator per SRS-UX-0021; the electronic notification is a secondary, best-effort notification only. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · — |

<a id="srs-ux-0028"></a>

| **SRS-UX-0028** | **The collar device SHALL communicate each distinct OTA update state — Downloading** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device SHALL communicate each distinct OTA update state — Downloading, Verifying, Pending Installation, Installing, Success, and Failed — via a unique LED pattern distinguishable from all other LED states defined in §14.3, enabling the user to understand update progress without the companion app. OTA functional states per §5. |
| **Rationale**    | — |
| **Priority**     | High |
| **Stability**    | Fixed |
| **Verification** | Test |
| **Traceability** | PRD §9.5 · — |


## 15. Operational Requirements

CAT: **OPER** | Maps to: PRD §6.4 (home/away state machines), §11.6–§11.7 (base station operational profile), §15 (Power Budget: §15.1–§15.6) | Cross-refs: PRD §4.1/§4.2 (variant deployment), §10.2.2 (GNSS interface), §12.1 (performance ceilings)

## 15.0 Scope Note

This section specifies operational behavior of the deployed system that is not already owned by another section: base-station continuous-operation posture and included power accessory, base-station status-indicator inventory (deferred here from §11 per that section's own Drafter Notes), the device-local home/away determination that other sections' power-gating and status requirements depend on, and the collar's duty-cycle/power-optimization behaviors drawn from PRD §15 (Power Budget) that are operational policies rather than hardware capabilities. It does **not** re-issue constraints already owned elsewhere:

- **GNSS interface behavior** (presence on Max, absence on Mini, configurable/default fix interval, A-GPS delivery/validity, fix-acquisition timeout, warm TTFF ceiling) is owned by §10 Interface Requirements (SRS-INT-0021–0029); this section does not restate those numeric bounds.
- **GNSS smart power-gate non-configurability** and the **Max GNSS interface disablement while HOME** are owned by §2 (SRS-OPER-0004) and §10 (SRS-INT-0027) respectively; this section adds only the device-local home/away determination mechanism those two depend on, which was not yet issued anywhere.
- **Battery cell minimum capacities, battery-life targets, idle-current ceiling, and low-battery alert threshold** are owned by §10.4/§11 Hardware (SRS-HW-0020–0024) and §3 Behavioral Classification (SRS-FUNC-0011); this section does not restate those figures.
- **Base-station Wi-Fi/cloud connectivity reliability bound and degraded-mode offline buffering** are owned by §2 (SRS-OPER-0007) and §4 (SRS-CONN-0028/0029); this section does not restate the −70 dBm / 256 kbps bound.
- **Base-station LED dimming / nighttime-mode `SHOULD`** is fully specified by §14 Usability (SRS-UX-0017, per ); this section does not re-issue it, only the base LED *inventory* deferred to this section by §11's own Drafter Notes.
- **OTA mechanics, atomicity, and success-rate criteria** are owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004); this section does not restate them.

## 15.1 Base Station Continuous Operation



## 15.2 Base Station Status Indicators







## 15.3 Household Geo-Fence Mesh Participation


## 15.4 Device-Local Home/Away Determination










## 15.5 Collar Duty-Cycle & Power-Optimization Policy






## 15.6 Cloud-Loss Fallback Governance


## 15.7 Product Service Lifetime Reference

**SRS-OPER-0023** | Expected Product Service Lifetime Reference Figure | The system's operational and durability requirements that reference an expected service lifetime **SHALL** use 2 years as the minimum testable floor, consistent with the Product Context Profile's user-confirmed ~2–3 year expected service lifetime figure. | Priority: MEDIUM | Stability: STABLE | Source:  | Rationale: This requirement formalizes, as its own SRS-OPER block, the same PCP §8 user-confirmed lifetime figure that SRS-RELI-0001 (§13) already applies as its qualification duration; §13's Drafter Notes flagged that no A-ID currently carries this figure and recommended one be issued. Issuing it here as an explicit OPER requirement — rather than only as an inline PCP dependency note on SRS-RELI-0001 — gives the figure a citable SRS-ID that future sections (e.g., §16 Maintainability's OTA-support-lifetime requirements) can cross-reference directly instead of re-deriving it from the PCP each time. | Verification Method: Inspection | Cross-References: SRS-RELI-0001

## 16. Maintainability

CAT: **MAINT** | Maps to: PRD §12.7 (Maintainability) | Cross-refs: PRD §9.5 (SBOM), §13.5, §14.1, §14.2(8)

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

## 17. Standards Conformance

CAT: **COMP** | Maps to: PRD §13.1, §13.3, §13.4, §13.7, §12.6, §9.5

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
- **EU Battery Regulation Art 11 (Removability)** — CONTINGENT. Potential conflict with non-swappable design;  tracks INDICATIVE exemption. Responsible: Regulatory Affairs, via EU counsel.
- **GNSS Intentional-Radiator Exemption** — CONTINGENT. RM-0009 UNCERTAIN, escalated to user.
- **ASTM F2727** — EXCLUDED AS MISCITATION. Corrected to ASTM F2056 per RM-0030.

## 18. Regulatory

# §18 — Regulatory Certification & Market Pathways

**CAT: REG** · **46 blocks (REG-0001–0046)** · **Status: APPROVED**
**Pipeline:** Feasibility PASS (46/46) · V-Method PASS (46/46) · Intra-Conflict COMPLETE (—/0029) · RTM ADD-ROW COMPLETE (323→369)

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















### 18.B.2 United Kingdom Market








### 18.B.3 Cross-Market Gate


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






### 18.C.2 Global Cross-Cutting Obligations




### 18.C.3 Global Cross-Market Gate


### 18.C.4 Out-of-Scope (6 items)

- AU/NZ EMC/electrical-safety mapping → Regulatory Agent (no RM-ID)
- RCM test execution → Accredited lab (external)
- AU/NZ Responsible Supplier duties → Supplier (external)
- Regulatory-change monitoring mechanism → Regulatory Affairs
- Per-market retention period research → Regulatory Affairs / counsel
- AU/NZ customs import filing → Logistics / Customs-Broker

---

---

## Appendix A. Requirements Traceability Matrix (RTM)

The RTM is maintained in two parts. Refer to the project repository for machine-readable CSV versions.

### Part A (§1–§4)

```
# 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.
# [S-luucipet] RTM — Part A (§1–§4)

*Combined authoritative row count = 283 (Part A: 89 · Part B: 194).*

| Req-ID | Title | Source Tags | Section | Status | Verification Method |
|---|---|---|---|---|---|
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
| SRS-FUNC-0024 | Timestamp UTC ≤1 s | [PRD §7.5] | §3 | APPROVED | Test |
| SRS-FUNC-0025 | Record GNSS fix on Max | [PRD §7.5] | §3 | APPROVED | Inspection |
| SRS-FUNC-0026 | Local retention ≥30 d | [PRD §7.5] | §3 | APPROVED | Test |
| SRS-FUNC-0027 | No discard on connectivity loss | [PRD §7.5] | §3 | APPROVED | Test |
| SRS-FUNC-0028 | Classification independent of BLE | [PRD §7.6] | §3 | APPROVED | Demonstration |
| SRS-FUNC-0029 | Forward without corruption | [PRD §7.6] | §3 | APPROVED | Test |
| SRS-FUNC-0030 | Forward without sequence loss | [PRD §7.6] | §3 | APPROVED | Test |
| SRS-FUNC-0031 | On-device normalization | [PRD §7.7] | §3 | APPROVED | Inspection |
| SRS-FUNC-0032 | Raw accel not leave collar | [PRD §7.7] | §3 | APPROVED | Test |
| SRS-FUNC-0033 | No cloud round-trip for classification | [PRD §7.7] | §3
```

### Part B (§5–§18)

```
# 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.
# [S-luucipet] RTM — Part B (§5–§10)

| Req-ID | Title | Source Tags | Section | Status | Linked Standards | Conflict IDs | Feasibility Score (D1–D5) | Verification Method | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SRS-FUNC-0043 | OTA Capability Mandatory on All Collar Variants | [PRD §9.1] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref FUNC-0034 |
| SRS-FUNC-0044 | OTA Capability Mandatory on All Base Station Tiers | [PRD §9.1] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref FUNC-0043 |
| SRS-FUNC-0045 | Cloud-to-Base OTA Transport Protocol (TLS 1.3) | [PRD §9.2],[PRD §6.5],[PRD §11.2] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | CR-0005 | PASS/PASS/PASS/PASS/PASS | Test | in-scope; TLS 1.3 per CR-0005; xref CONN-0014 |
| SRS-FUNC-0046 | Base Station Staging of Collar OTA Images | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref FUNC-0047 |
| SRS-FUNC-0047 | Base-to-Collar OTA Image Delivery Over Secured BLE Link | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; xref CONN-0009, SEC-0001, SEC-0002 |
| SRS-FUNC-0048 | Base Station Self-OTA Without User Action | [PRD §11.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-FUNC-0049 | Collar OTA Install Restricted to Charging-Cradle-Docked State | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0050 | Docked-Install Gate Shall Not Be Remotely Bypassable | [PRD §9.2] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0051 | Minimum Battery Reserve Before OTA Install (≥10% SoC) | [PRD §9.2],[PRD §10.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0052 | Minimum OTA Image Signature Strength (≥256-bit ECDSA/RSA-2048) | [PRD §9.3] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-FUNC-0053 | OTA Image Signature Verification Before Commit | [PRD §9.3] | §5 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0054 | Anti-Rollback via Monotonic Version Counter | [PRD §9.3] | §5 | APPROVED | EU CRA 2024/2847 (RM-0021) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0055 | Atomic OTA Installation | [PRD §9.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0056 | Dual-Bank Auto-Revert on Boot Failure | [PRD §9.4],[PRD §11.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0057 | No Unrecoverable State on Power/Connection Loss During Install | [PRD §9.4] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-FUNC-0058 | Device-Side OTA Update State Reporting | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-FUNC-0059 | App Notification of Available OTA Update | [PRD §9.5],[EXTERNAL: Mobile App team] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-FUNC-0060 | App Display of OTA Update State | [PRD §9.5],[EXTERNAL: Mobile App team] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-FUNC-0061 | SBOM Production Per OTA Release | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; lifetime SBOM → §16 |
| SRS-FUNC-0062 | Tier-2 Classifier Delivery Restricted to Embedded OTA Components | [PRD §9.5] | §5 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-PERF-0001 | Mini Variant Battery-Life Conformance | [PRD §12.1],[PRD §10.4],[CR-0002],[PRD §15.6] | §6 | APPROVED | — | CR-0002 | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-PERF-0002 | Max Variant Battery-Life Conformance | [PRD §12.1],[PRD §10.4],[CR-0002],[PRD §15.6] | §6 | APPROVED | — | CR-0002 | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-PERF-0003 | Classification Latency Ceiling (<2 s) | [PRD §12.1] | §6 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-PERF-0004 | Base Station Cloud-Upload Latency Ceiling (<30 s) | [PRD §12.1] | §6 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-PERF-0005 | GNSS Time-to-First-Fix Ceiling (<60 s, warm/A-GPS) | [PRD §12.1] | §6 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-PERF-0006 | Collar Boot-Time Ceiling (<3 s) | [PRD §12.1],[ASSUMPTION: A-0019] | §6 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-PERF-0007 | Home/Away Status Update Latency Ceiling (≤adv interval + 10 s) | [PRD §12.1] | §6 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-PERF-0008
```

*Full RTM CSVs: 369 rows total (Part A: 89 rows · Part B: 280 rows).*

---

## Appendix B. Regulatory Map

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
| RM-0005 | UK Radio Equipment Regs 2017 (SI 2017/1206)                                               | —                     | UK                      | Mini/Max/Base | CONFIRMED  | UKCA.                                                                                                                                                                                                                                                                                                    |
| RM-0006 | ISED RSS-247 Issue 2 + RSS-Gen Issue 5                                                    | —                     | CA                      | Mini/Max/Base | INDICATIVE | Verify current issue numbers at submission.                                                                                                                                                                                                                                                              |
| RM-0007 | AS/NZS 4268:2017                                                                          | —                     | AU/NZ                   | Mini/Max/Base | INDICATIVE | RCM; verify no newer edition.                                                                                                                                                                                                           
```

*Full Regulatory Map: 31 instrument entries, 5 target markets.*

---

## Appendix C. Assumption Register

```
> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# [S-luucipet] Assumption Register

**Session:** S-luucipet · A-ID cursor consumed: A-0001 … A-0025 · Next free: **A-0026**

| ID | Statement | Basis | Risk |
| :-- | :-------- | :---- | :--- |
| A-0025 | Certification/DoC archival retention = 10 years after last unit placed on market (longest-obligation-dominates across all 5 markets). Anchored in SRS-REG-0043; resolves D4 MARGINAL. | RED Art 10 (10yr), CRA Art 13/31 (10yr/support), FCC §2.938 (2yr), ISED RSS-Gen, ACMA/EESS (5yr). Tier-1 verified 2026-07. | LOW-MEDIUM |
| A-0024 | SBOM machine-readable format = SPDX 2.3 or CycloneDX. Anchored in SRS-COMP-0028. | Standard-derived default. EU CRA Annex I + US EO 14028. | LOW-MEDIUM |

(A-0001 through A-0023 retained in master Assumption Register.)

```

---

## Appendix D. Glossary

### A

- **A-GPS** — Assisted GPS; auxiliary satellite ephemeris/almanac data delivered via a terrestrial link (here, BLE) to reduce GNSS fix acquisition time.
- **Address Randomization** — Periodic rotation of the BLE device address to prevent long-term tracking by third-party observers.

### B

- **Base Station (Charging)** — The base station tier that includes a single-device pogo-pin charging cradle in addition to BLE relay and Wi-Fi uplink functions.
- **Base Station (Relay)** — The base station tier that provides BLE relay and Wi-Fi uplink functions without a charging cradle.

### C

- **CCF (Collar Connection Fixture)** — A compound mechanical accessory that attaches the collar device to the pet's own collar, providing Zone 1 structural retention and Zone 2 strangulation-prevention breakaway.
- **Central Role** — The BLE role that scans for advertisements and initiates connections to peripherals.
- **Charge/Discharge Cycle** — One complete sequence of fully charging and then discharging a battery cell, used as the standard unit for battery aging and cycle-life validation.
- **Classification Record** — A data record containing a behavioral label, confidence score, and UTC timestamp generated by the on-device classification engine.

### D

- **Damp Heat** — A combined high-temperature, high-humidity environmental test used to assess material and seal degradation under sustained humid conditions.
- **Debounce (RSSI Reading)** — A requirement that a stated number of consecutive RSSI readings, rather than a single reading, satisfy a threshold condition before a state transition is committed.

### G

- **GNSS** — Global Navigation Satellite System; a passive receiver providing position-fix data from satellite signals.

### H

- **HOME/AWAY State** — The device-local determination of whether the collar device is within BLE range of at least one paired household base station (HOME) or not (AWAY), used to gate power-sensitive behaviors such as GNSS acquisition.
- **Hysteresis (RSSI)** — A signal-strength margin requiring a materially different RSSI value to transition back to HOME than the value used to transition to AWAY, preventing rapid state oscillation.

### I

- **IP67** — An ingress protection rating per IEC 60529 signifying the device is dust-tight (6) and protected against temporary immersion in water up to 1 metre for 30 minutes (7).

### L

- **LE Secure Connections** — A BLE pairing method using elliptic-curve key exchange to establish link-layer encryption keys.

### O

- **Operational Availability** — The proportion of time a system or device is capable of performing its specified function, expressed as a percentage of total elapsed time within a defined observation window.

### P

- **Peripheral Role** — The BLE role that advertises and accepts incoming connections, as opposed to the central role that scans and initiates connections.

### Q

- **QDID** — Qualified Design ID; the identifier issued by the Bluetooth SIG upon successful qualification testing of a BLE product design.
- **QR OOB Pairing** — An out-of-band BLE pairing method in which a QR code carries pairing data, avoiding reliance on numeric-comparison or passkey entry.

### S

- **Service Lifetime** — The expected duration, from first use to end of intended service, over which a product must continue to meet its specified performance and safety criteria.

### T

- **Thermal Cycling** — Repeated exposure of a test article to alternating high- and low-temperature extremes to reveal degradation caused by thermally induced material stress.
- **TLS 1.3** — Transport Layer Security version 1.3; the transport-layer encryption protocol used for base-station-to-cloud traffic.
- **TTFF** — Time-To-First-Fix; the elapsed time from the start of a GNSS fix attempt to acquisition of a valid position fix.

### U

- **Uptime** — The proportion of a defined observation window during which a system remains powered, responsive, and capable of performing its specified function.
- **UV Aging** — Accelerated exposure of a material to ultraviolet radiation to evaluate long-term degradation from outdoor solar exposure within a compressed test duration.

### V

- **VBUS** — The positive supply-voltage contact of the pogo-pin charging interface.

### Z

- **Zone 1** — The structural retention zone of the CCF (non-breakaway), responsible for attaching the CCF body to the pet's collar.
- **Zone 2** — The Fuse Tab zone of the CCF, a single-use, species/size-appropriate strangulation-prevention breakaway that fractures at a calibrated force.

---

## Appendix E. Document Summary

| Attribute | Value |
|---|---|
| **Total Sections** | 18 |
| **Total Requirements** | 337 |
| **Traceability Rows** | 369 |
| **Standards Basis** | IEEE 830 / ISO/IEC/IEEE 29148 |
| **Conflicts Resolved** | 29 (CR-0001–CR-0029) |
| **Cross-Section Resolutions** | 16 (XSC-0002–XSC-0016) |
| **Assumptions** | 25 (A-0001–A-0025) |
| **Regulatory Instruments** | 31 (RM-0001–RM-0031) |
| **Product Lifetime** | 2–3 years (2-year testable floor) |
| **Target Volume** | ~5,000 units (first batch) |

---

*End of Document — SRS-LUUCIPET-001, Revision 1.0*

*Authoring: Systems Engineering Team · Conforms to IEEE 830 / ISO/IEC/IEEE 29148*
