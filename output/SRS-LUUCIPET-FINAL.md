# System Requirements Specification

## LUUCIPet Wellness Monitor — Phase 1

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
| 1.0 | July 2026 | Systems Engineering Team | Initial release — full pipeline assembly |

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

## 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

## 1.2 Scope

**In scope:**  Mini & Max collar HW+FW; Base Station (Charging & Relay) HW+FW; the device-enforced BLE/base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S/M/L, collar-types -RC/-MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract.
**Out of scope (PRD §6.1, §14.1):**  GPS-M variant + cellular (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage/analytics backend; cloud-side home/away state machine; device-app ICD.

## 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

## 1.4 Wellness-Not-Medical Boundary

<a id="srs-reg-0001"></a>

| **SRS-REG-0001** | **Prohibit medical-classification claims in labeling and marketing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. |
| **Rationale**    | Derived from PRD §13.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.6 · SRS-REG-0002 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **Require regulatory classification review before releasing diagnostic-adjacent features** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. |
| **Rationale**    | Derived from PRD §13.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §13.6 · SRS-REG-0001

## 1.5 Definitions and References

Full term definitions are maintained in the Glossary appendix (derived from PRD §14.4). Standards/regulatory instruments are enumerated in the Regulatory Map and cited inline using the closed source-tag set only: `[PRD §x.x]`, `[STD: ID §clause]`, `[ASSUMPTION: A-NNNN]`, ``, `[PRD — ABSENT: field]`.

---

**SRS-IDs issued:**  SRS-REG-0001, SRS-REG-0002. |


## 2. Overall Description

## 2.1 Product Functions

The LUUCIPet Wellness Monitor is a collar-mounted behavioral wellness system for cats and dogs, comprising an ultra-light wearable device, a companion household Base Station, and a mechanical Collar Connection Fixture (CCF) accessory family. The system continuously classifies pet behavior on-device (accelerometer-based classification engine), relays behavioral and location data to the LUUCI IoT Cloud Device-Management layer via the Base Station, and supports over-the-air (OTA) firmware and classifier updates. The product is positioned strictly as a general wellness device for animals; it does not perform, and is not intended to support, medical diagnosis. [PRD §1]

At launch (Phase 1), the device ships with two factory-loaded Tier-1 behavioral classifiers (Rest/Sleep, Active/Awake); a broader Tier-2 classifier set is deliverable post-launch exclusively via OTA. [PRD §1], [PRD §4.4]

**Scope-Model note on functional responsibility.**  Per the group Scope Model, product functions are delivered across our build and named external parties; both are documented here:

- **In scope (our build):**  on-device behavioral classification; collar↔base BLE sync and base↔cloud relay (device-management-layer interface); charging (Base Station + Portable Travel Charging Cradle); CCF breakaway/separation detection and event transport (SRS-FUNC-0001, SRS-FUNC-0002); device-side species-profile persistence (SRS-OPER-0003); device-local home/away determination that gates GNSS power behavior, relying solely on the device-local state machine ([ASSUMPTION: A-0016]).
- **External-party (documented, attributed):**  owner-facing Mobile App alerts/onboarding/CCF guidance/dashboards — **[EXTERNAL: Mobile App team]** (SRS-OPER-0008, SRS-OPER-0009, SRS-OPER-0010); IoT Cloud storage/analytics backend and the cloud-side home/away state machine for owner geofence alerting — **[EXTERNAL: IoT Cloud backend team]** (SRS-OPER-0011). Data transport to the cloud is our in-scope hand-off; cloud storage/analytics and app display are external ([ASSUMPTION: A-0015]).
- **Future-phase (deferred, Phase 2):**  GPS-M variant + cellular positioning — not addressed by any requirement in this SRS.

The CCF Zone 2 Fuse Tab breakaway is designed as an indicative strangulation-prevention mitigation with reference to [STD: EU GPSR 2023/988 §Art 6(1)(a) w/ §Art 5]; per [ASSUMPTION: A-0017] this framing is design-level and pending DVT (efficacy for the feline SKU is not yet confirmed). §2's treatment is intentionally light; substantive safety requirements are specified in §7.

## 2.2 Product Variants & Configurations

### 2.2.1 Collar Devices

Two collar variants share a common platform (classification engine, BLE protocol, OTA path, Twist-Lock geometry) but differ in weight class, sensing, and target population:

- **Mini** — ≤10 g; BLE-only; targets all cats and dogs; typical battery life ≥90 days (≥180 days in Longevity Mode). [PRD §1], [PRD §4.1]
- **Max** — ≤22 g; BLE plus full-quality GNSS (receive-only); targets large dogs (>20 kg) and service dogs; battery life ≥45 days at a 2-hour GNSS fix interval, ≥90 days at a 4-hour interval; GNSS is power-gated off while the device is in the HOME state. [PRD §1], [PRD §4.1]

### 2.2.2 Base Station Family

Two Base Station tiers share a common BLE-relay and Wi-Fi-uplink platform:

- **Base Station (Charging)** — BLE relay, Wi-Fi uplink, single-device pogo-pin charging cradle, 3 status LEDs. [PRD §4.2]
- **Base Station (Relay)** — identical to the Charging tier minus the charging cradle; 2 status LEDs. [PRD §4.2]

Both tiers support multi-device BLE connections (Mini and Max concurrently), participate in the household geo-fence mesh, relay OTA payloads to collars, self-update over Wi-Fi, and buffer collar data for at least 30 days during connectivity loss. [PRD §4.2]

### 2.2.3 Collar Connection Fixture (CCF) Family

The CCF is a compound mechanical accessory that attaches the collar device to the pet's own (third-party-supplied) collar. It provides two functionally distinct zones: Zone 1 (structural retention, not a breakaway feature) and Zone 2 (the Fuse Tab — a single-use, species/size-appropriate strangulation-prevention breakaway). The device engages the CCF through a 3-lug Twist-Lock bayonet interface used for charging removal. [PRD §1], [PRD §4.1]

The CCF is offered in width variants S/M/L and collar-type variants -RC (round) and -MG (martingale), sold separately from the in-box default; a Standard CCF (flat-webbing) ships in every box, sized to the collar variant (CCF-S with Mini, CCF-L with Max). [PRD §4.1], [PRD §4.5]

### 2.2.4 Classifier Tiers

- **Tier-1 (factory-loaded):**  Rest/Sleep; Active/Awake. [PRD §4.4]
- **Tier-2 (OTA-delivered, post-launch):**  Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting (dog only), Head-Shaking. [PRD §4.4]

## 2.3 User Characteristics / Personas

The system is designed around six user personas, described here as user context only; owner-facing app features are captured as attributed [EXTERNAL: Mobile App team] requirements (see §2.4), not derived directly from these personas. [PRD §3]

| Persona | Description |
|---|---|
| P1 — Single-Pet Owner | Primary user of a single Mini-equipped pet. |
| P2 — Multi-Pet Household | Manages a mix of Mini and Max devices across multiple pets. |
| P3 — Allergy/Skin-Concern Owner | Relies on fine-grained scratch-behavior logging. |
| P4 — Active-Lifestyle Large-Dog Owner | Primary user of Max, values GNSS behavioral context. |
| P5 — Veterinary Professional | Uses exported behavioral summaries as a wellness-conversation support tool |
| P6 — Service Dog Handler | Monitors welfare of a working service dog (Max). |

## 2.4 General Constraints

<a id="srs-oper-0001"></a>

| **SRS-OPER-0001** | **Require at least one Charging-tier base station per household** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | A household deployment **shall** include at least one Base Station of the Charging tier. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.2 · SRS-OPER-0002 |

<a id="srs-oper-0002"></a>

| **SRS-OPER-0002** | **Limit base stations per household deployment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | A household deployment **shall not** exceed 8 Base Stations, in any combination of Charging and Relay tiers. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 · SRS-OPER-0001 |

<a id="srs-oper-0003"></a>

| **SRS-OPER-0003** | **Persist species assignment across resets** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. |
| **Rationale**    | Derived from PRD §4.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.5 · SRS-OPER-0009 |

<a id="srs-oper-0004"></a>

| **SRS-OPER-0004** | **Prohibit owner configuration of the GNSS smart power gate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS smart power gate **shall not** be configurable by the owner. |
| **Rationale**    | Derived from PRD §4.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.5 |

<a id="srs-oper-0005"></a>

| **SRS-OPER-0005** | **Bound in-box CCF fitment coverage** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The in-box Standard CCF **shall** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. |
| **Rationale**    | Derived from PRD §14.2. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §14.2 · SRS-OPER-0006, SRS-OPER-0010 |

<a id="srs-oper-0006"></a>

| **SRS-OPER-0006** | **Default to Standard CCF as in-box accessory** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. |
| **Rationale**    | Derived from PRD §4.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.1 · SRS-OPER-0005 |

<a id="srs-oper-0007"></a>

| **SRS-OPER-0007** | **Define degraded-mode behavior below the home Wi-Fi reliability bound** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station **shall** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | ASSUMPTION: A-0009 |

<a id="srs-oper-0008"></a>

| **SRS-OPER-0008** | **Mobile App post-breakaway owner alert (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.6 · SRS-FUNC-0001, SRS-FUNC-0002 |

<a id="srs-oper-0009"></a>

| **SRS-OPER-0009** | **Mobile App species re-onboarding flow (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's species classifier profile. |
| **Rationale**    | Derived from PRD §4.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.5 · SRS-OPER-0003 |

<a id="srs-oper-0010"></a>

| **SRS-OPER-0010** | **Mobile App CCF fitment/sizing guidance (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. |
| **Rationale**    | Derived from PRD §14.2. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §14.2 · SRS-OPER-0005 |

<a id="srs-oper-0011"></a>

| **SRS-OPER-0011** | **Cloud-side home/away state machine for owner geofence alerting (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. |
| **Rationale**    | Derived from ASSUMPTION: A-0016. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | ASSUMPTION: A-0016 · SRS-OPER-0004 |

<a id="srs-comp-0001"></a>

| **SRS-COMP-0001** | **Require collar-agnostic base station firmware** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Base Station firmware **shall** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. |
| **Rationale**    | Derived from PRD §4.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.3 · SRS-COMP-0002 |

<a id="srs-comp-0002"></a>

| **SRS-COMP-0002** | **Require universal CCF-to-device mechanical compatibility** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **shall** be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. |
| **Rationale**    | Derived from PRD §4.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 · SRS-COMP-0001 |

<a id="srs-comp-0003"></a>

| **SRS-COMP-0003** | **Require equivalent behavioral-classification outputs across collar variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini and Max collar variants **shall** exhibit equivalent behavioral-classification outputs. |
| **Rationale**    | Derived from PRD §4.3 — ensures classification consistency regardless of variant. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0001 |

<a id="srs-comp-0031"></a>

| **SRS-COMP-0031** | **Require interoperable common BLE communication protocol across variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini and Max collar variants **shall** use an interoperable common BLE communication protocol. |
| **Rationale**    | Derived from PRD §4.3 — ensures cross-variant protocol compatibility. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0003 |<a id="srs-func-0001"></a>

| **SRS-FUNC-0001** | **Detect CCF breakaway/separation signature** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event record to non-volatile storage within 5 s of the separation event, with a false-positive rate not exceeding 0.1% per device-wear-day and a true-event detection rate of at least 99% under DVT drop/tension conditions. |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · SRS-FUNC-0002, SRS-FUNC-0003, SRS-OPER-0008 |

<a id="srs-func-0003"></a>

| **SRS-FUNC-0003** | **Preserve persisted breakaway event record across power-loss events** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The persisted breakaway event record **shall** survive subsequent power loss, battery depletion, and reboot without corruption. |
| **Rationale**    | Derived from PRD §8.4 — ensures breakaway events are never lost. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 · SRS-FUNC-0001 |

<a id="srs-func-0062"></a>

| **SRS-FUNC-0062** | **Transmit persisted breakaway event on next base-station contact** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The persisted breakaway event record **shall** be transmitted to the Base Station on the next successful Base Station contact. |
| **Rationale**    | Derived from PRD §8.4 — ensures timely delivery of breakaway notifications. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 · SRS-FUNC-0003 |<a id="srs-func-0002"></a>

| **SRS-FUNC-0002** | **Transport breakaway event to IoT Cloud Device-Management layer** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station **shall** transport a recorded breakaway/separation event to the IoT Cloud Device-Management layer on the next successful Base Station contact and cloud sync (event-triggered; no delivery-time guarantee, as post-breakaway the device may be lost, out of range, or depleted). |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · SRS-FUNC-0001, SRS-FUNC-0003, SRS-OPER-0008

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

### SRS-ID inventory (§2 v2)
**In-scope:** SRS-OPER-0001–0007 · SRS-COMP-0001–0003 · SRS-FUNC-0001–0003
**External-party:** SRS-OPER-0008–0011
**Total: 16 blocks** |


## 3. Behavioral Classification


## 3.1 Operating Modes

<a id="srs-func-0006"></a>

| **SRS-FUNC-0006** | **Wellness Mode as Default Operating Mode** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** operate in Wellness mode as its default power-optimized classification mode. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.1 · SRS-FUNC-0011 |

<a id="srs-func-0007"></a>

| **SRS-FUNC-0007** | **Insight Mode Availability On Demand** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.1 · SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="srs-func-0008"></a>

| **SRS-FUNC-0008** | **Insight Mode Continuous Sampling Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While in Insight mode, the system **shall** sample the accelerometer continuously at 50 Hz. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.1 · SRS-FUNC-0007, SRS-FUNC-0014 |

<a id="srs-func-0009"></a>

| **SRS-FUNC-0009** | **Insight Mode Auto-Revert to Wellness** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** automatically revert from Insight mode to Wellness mode without requiring a manual user action. |
| **Rationale**    | Derived from PRD §7.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0006, SRS-FUNC-0007 |

<a id="srs-func-0010"></a>

| **SRS-FUNC-0010** | **Wellness Mode Motion-Triggered Confirmation Burst** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon detecting motion, the system **shall** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. |
| **Rationale**    | Derived from PRD §7.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0011 |

<a id="srs-func-0011"></a>

| **SRS-FUNC-0011** | **Wellness Mode Idle Current Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While in Wellness mode and outside a confirmation burst, the system **shall not** exceed an idle current draw of 4 µA. |
| **Rationale**    | Derived from PRD §7.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0006, SRS-FUNC-0010 |

<a id="srs-func-0012"></a>

| **SRS-FUNC-0012** | **Longevity Mode Shall Not Reduce Classification Sampling Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When Longevity Mode is active, the system **shall not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. |
| **Rationale**    | Derived from PRD §7.10. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.10 · SRS-FUNC-0014 |

<a id="srs-func-0013"></a>

| **SRS-FUNC-0013** | **Longevity Mode Shall Not Reduce Classification Accuracy** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When Longevity Mode is active, the system **shall not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. |
| **Rationale**    | Derived from PRD §7.10. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.10 · SRS-FUNC-0018, SRS-FUNC-0020

## 3.2 Sensing & Classification Pipeline |

<a id="srs-func-0014"></a>

| **SRS-FUNC-0014** | **Minimum Accelerometer Output Data Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** sample the accelerometer at a rate of no less than 50 Hz. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.2 · SRS-FUNC-0008, SRS-FUNC-0015 |

<a id="srs-func-0015"></a>

| **SRS-FUNC-0015** | **No Auxiliary Sensors for Tier-1 Classification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.2 · SRS-FUNC-0014 |

<a id="srs-func-0016"></a>

| **SRS-FUNC-0016** | **Unified Classification Pipeline Across Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.2 · SRS-FUNC-0034 |

<a id="srs-func-0017"></a>

| **SRS-FUNC-0017** | **Species-Specific Threshold Assignment at Onboarding** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** set species-specific classification thresholds during the onboarding process. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.2 · SRS-OPER-0003

## 3.3 Classification Accuracy & False-Positive Bounds |

<a id="srs-func-0018"></a>

| **SRS-FUNC-0018** | **Tier-1 Per-Class Accuracy Minimum** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0019 |

<a id="srs-func-0019"></a>

| **SRS-FUNC-0019** | **Tier-1 Per-Class False-Positive Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** exceed a false-positive rate of 5% for each Tier-1 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0018 |

<a id="srs-func-0020"></a>

| **SRS-FUNC-0020** | **Tier-2 Per-Class Accuracy Minimum** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0021 |

<a id="srs-func-0021"></a>

| **SRS-FUNC-0021** | **Tier-2 Per-Class False-Positive Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** exceed a false-positive rate of 10% for each Tier-2 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0020

## 3.4 Classification Records & Local Storage |

<a id="srs-func-0022"></a>

| **SRS-FUNC-0022** | **Classification Record Contains Behavior Label** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** include a behavior class label in every generated classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 · SRS-FUNC-0023, SRS-FUNC-0024 |

<a id="srs-func-0023"></a>

| **SRS-FUNC-0023** | **Classification Record Contains Confidence Score** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** include a confidence score in the range 0.0 to 1.0 in every generated classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0024"></a>

| **SRS-FUNC-0024** | **Classification Record Timestamp Resolution** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** timestamp every classification record in UTC with a resolution no coarser than 1 second. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0025"></a>

| **SRS-FUNC-0025** | **Classification Record GNSS Fix on Max Variant** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** include the most recent GNSS fix in every generated classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0026"></a>

| **SRS-FUNC-0026** | **Minimum Local Retention of Classification Records** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** retain generated classification records locally for no less than 30 days without a cloud connection. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0027 |

<a id="srs-func-0027"></a>

| **SRS-FUNC-0027** | **No Record Discard on Connectivity Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** discard stored classification records upon loss of connectivity. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0026 |

<a id="srs-func-0028"></a>

| **SRS-FUNC-0028** | **Classification Generation Independent of BLE Connectivity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** generate and record classifications independently of the current BLE connectivity state. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.6 · SRS-FUNC-0029 |

<a id="srs-func-0029"></a>

| **SRS-FUNC-0029** | **Record Forwarding Without Corruption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records without data corruption. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 · SRS-FUNC-0030 |

<a id="srs-func-0030"></a>

| **SRS-FUNC-0030** | **Record Forwarding Without Sequence Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records without loss of their original sequence order. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 · SRS-FUNC-0029

## 3.5 Data Locality & On-Device Processing |

<a id="srs-func-0031"></a>

| **SRS-FUNC-0031** | **On-Device Signal Normalization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** normalize raw accelerometer data on-device prior to classification. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7 · SRS-FUNC-0032, SRS-FUNC-0033 |

<a id="srs-func-0032"></a>

| **SRS-FUNC-0032** | **Raw Accelerometer Data Shall Not Leave the Collar** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** transmit raw accelerometer data off the collar. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.7 · SRS-FUNC-0031, SRS-FUNC-0033 |

<a id="srs-func-0033"></a>

| **SRS-FUNC-0033** | **No Cloud Round-Trip for Classification Decisions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** produce classification decisions without requiring a round-trip to a cloud service. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.7 · SRS-FUNC-0028, SRS-FUNC-0032

## 3.6 Tier-2 Extensibility via OTA |

<a id="srs-func-0034"></a>

| **SRS-FUNC-0034** | **Tier-2 Classifier Delivery via OTA** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. |
| **Rationale**    | Derived from PRD §7.9. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0016, SRS-FUNC-0035 |

<a id="srs-func-0035"></a>

| **SRS-FUNC-0035** | **Tier-2 Deployment Without Hardware Modification or Service Event** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. |
| **Rationale**    | Derived from PRD §7.9. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0034

## 3.7 Configurable Alert Thresholds (Scratching & Shaking) |

<a id="srs-func-0036"></a>

| **SRS-FUNC-0036** | **Device Application of Configured Scratching Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a Scratching alert threshold value received via the companion application. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0037, SRS-FUNC-0041 |

<a id="srs-func-0037"></a>

| **SRS-FUNC-0037** | **Firmware-Default Scratching Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036 |

<a id="srs-func-0038"></a>

| **SRS-FUNC-0038** | **Device Application of Configured Shaking Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a Shaking alert threshold value received via the companion application. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0039, SRS-FUNC-0042 |

<a id="srs-func-0039"></a>

| **SRS-FUNC-0039** | **Firmware-Default Shaking Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0038 |

<a id="srs-func-0040"></a>

| **SRS-FUNC-0040** | **Alert Threshold Persistence Across OTA Updates** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036, SRS-FUNC-0038 |

<a id="srs-func-0041"></a>

| **SRS-FUNC-0041** | **App-Side Scratching Threshold Configuration UI (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036 |

<a id="srs-func-0042"></a>

| **SRS-FUNC-0042** | **App-Side Shaking Threshold Configuration UI (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0038

---

### SRS-ID inventory (§3 v1)
**In-scope (35):** SRS-FUNC-0006 … SRS-FUNC-0040.
**External (2):** SRS-FUNC-0041, SRS-FUNC-0042 ([EXTERNAL: Mobile App team]).
**Total: 37 blocks.** Next free FUNC ID = SRS-FUNC-0043. |


## 4. Data Sync Connectivity


## 4.1 BLE Device↔Base Link & Pairing

<a id="srs-conn-0001"></a>

| **SRS-CONN-0001** | **BLE Role Assignment — Collar as Peripheral** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** operate the collar-mounted device in the BLE peripheral role relative to the base station. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · SRS-CONN-0002 |

<a id="srs-conn-0002"></a>

| **SRS-CONN-0002** | **BLE Role Assignment — Base Station as Central** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** operate the base station in the BLE central role relative to the collar-mounted device. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · SRS-CONN-0001 |

<a id="srs-conn-0003"></a>

| **SRS-CONN-0003** | **QR-Code Out-of-Band Pairing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 |

<a id="srs-conn-0004"></a>

| **SRS-CONN-0004** | **Default BLE Advertising Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** advertise the presence of the collar-mounted device at a default interval of 60 seconds. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0005 |

<a id="srs-conn-0005"></a>

| **SRS-CONN-0005** | **Configurable Advertising Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0004 |

<a id="srs-conn-0006"></a>

| **SRS-CONN-0006** | **Minimum Open-Air BLE Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0007 |

<a id="srs-conn-0007"></a>

| **SRS-CONN-0007** | **Minimum BLE Transmit Power** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** transmit BLE signals at a power level of no less than +8 dBm. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0006 |

<a id="srs-conn-0008"></a>

| **SRS-CONN-0008** | **BLE Address Randomization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** randomize the BLE device address of the collar-mounted device. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 |

<a id="srs-conn-0009"></a>

| **SRS-CONN-0009** | **Secured BLE Link Establishment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · — (§8 Security, not yet drafted) |

<a id="srs-conn-0010"></a>

| **SRS-CONN-0010** | **Automatic BLE Reconnection on Range Re-Entry** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon the collar-mounted device re-entering BLE range of a base station, the system **shall** automatically re-establish the BLE link without requiring manual user action. |
| **Rationale**    | Derived from PRD §6.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.4 · SRS-CONN-0001, SRS-CONN-0002

## 4.2 Record Forwarding & Sync |

<a id="srs-conn-0011"></a>

| **SRS-CONN-0011** | **Classification Record Forwarding on BLE Contact** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon establishing a BLE link with a base station, the system **shall** forward stored classification records from the collar-mounted device to the base station. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-FUNC-0026, SRS-FUNC-0028 |

<a id="srs-conn-0012"></a>

| **SRS-CONN-0012** | **Best-Effort Event-Triggered Record Transport** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.5 · SRS-FUNC-0002, SRS-FUNC-0003 |

<a id="srs-conn-0013"></a>

| **SRS-CONN-0013** | **Sync Resumption of Accumulated Records After Reconnection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **shall** forward all classification records accumulated during that disconnection. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-FUNC-0027, SRS-CONN-0011

## 4.3 Base↔Cloud Gateway & Upload |

<a id="srs-conn-0014"></a>

| **SRS-CONN-0014** | **Base Station Upload of Received Records to Cloud** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-CONN-0011, SRS-CONN-0009 |

<a id="srs-conn-0015"></a>

| **SRS-CONN-0015** | **Base Station Buffering on Upload-Path Unavailability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0016 |

<a id="srs-conn-0016"></a>

| **SRS-CONN-0016** | **Buffered Record Upload on Path Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0015 |

<a id="srs-conn-0017"></a>

| **SRS-CONN-0017** | **No Discard of Received Records Pending Upload** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0015 |

<a id="srs-conn-0018"></a>

| **SRS-CONN-0018** | **Cloud Acceptance and Acknowledgment of Uploaded Records (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8 · SRS-CONN-0014 |

<a id="srs-conn-0030"></a>

| **SRS-CONN-0030** | **Base Station Upload Retry on Transient Failure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **shall** retry uploading the affected buffered classification record. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Demonstration |
| **Traceability** | PRD §8.5 · SRS-CONN-0015, SRS-CONN-0016

## 4.4 Multi-Base-Station Behavior & Handover |

<a id="srs-conn-0019"></a>

| **SRS-CONN-0019** | **Collar Forwarding to Any In-Range Paired Base Station** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 · SRS-CONN-0011 |

<a id="srs-conn-0020"></a>

| **SRS-CONN-0020** | **Single Forwarding of Each Record to First Available Base Station** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in range. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 · SRS-CONN-0019, SRS-CONN-0021 |

<a id="srs-conn-0021"></a>

| **SRS-CONN-0021** | **Cloud-Side Deduplication of Multi-Base Uploads (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household account. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.2 · SRS-CONN-0020, SRS-CONN-0018

## 4.5 Insight-Mode Activation over Connectivity |

<a id="srs-conn-0022"></a>

| **SRS-CONN-0022** | **Device-Side Insight-Mode Activation on Command Receipt** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.1 · SRS-FUNC-0007, SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="srs-conn-0023"></a>

| **SRS-CONN-0023** | **Mobile App Issuance of Insight-Mode Activation Command (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.1 · SRS-CONN-0022

## 4.6 GNSS Location Data Sync (Max Variant) |

<a id="srs-conn-0024"></a>

| **SRS-CONN-0024** | **Sync of Location-Tagged Records via Standard Forwarding Path** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other classification records. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0025, SRS-CONN-0011 |

<a id="srs-conn-0025"></a>

| **SRS-CONN-0025** | **Sync of Most-Recent GNSS Fix During Home Power-Gate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix as part of classification records. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0025, SRS-OPER-0004

## 4.7 Connectivity-Loss & Degraded Behavior |

<a id="srs-conn-0026"></a>

| **SRS-CONN-0026** | **No Record Loss Due to Any Connectivity-Loss Condition** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0017 |

<a id="srs-conn-0027"></a>

| **SRS-CONN-0027** | **Continued Local Classification During BLE Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.6 · SRS-FUNC-0028, SRS-FUNC-0027 |

<a id="srs-conn-0028"></a>

| **SRS-CONN-0028** | **Degraded-Mode Entry Below Home Wi-Fi Reliability Bound** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007 |

<a id="srs-conn-0029"></a>

| **SRS-CONN-0029** | **Degraded-Mode Exit on Wi-Fi Reliability Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007, SRS-CONN-0028

--- |


## 5. Ota Firmware Updates


## 5.1 OTA Applicability

<a id="srs-func-0043"></a>

| **SRS-FUNC-0043** | **OTA Capability Mandatory on All Collar Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). |
| **Rationale**    | Derived from PRD §9.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0034 |

<a id="srs-func-0044"></a>

| **SRS-FUNC-0044** | **OTA Capability Mandatory on All Base Station Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). |
| **Rationale**    | Derived from PRD §9.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0043

## 5.2 OTA Delivery Path & Transport |

<a id="srs-func-0045"></a>

| **SRS-FUNC-0045** | **Cloud-to-Base OTA Transport Protocol** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-CONN-0014 |

<a id="srs-func-0046"></a>

| **SRS-FUNC-0046** | **Base Station Staging of Collar OTA Images** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0047 |

<a id="srs-func-0047"></a>

| **SRS-FUNC-0047** | **Base-to-Collar OTA Image Delivery Over Secured BLE Link** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.2 · SRS-CONN-0009 |

<a id="srs-func-0048"></a>

| **SRS-FUNC-0048** | **Base Station Self-OTA Without User Action** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. |
| **Rationale**    | Derived from PRD §11.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §11.5 · SRS-FUNC-0044

## 5.3 Collar Install Preconditions |

<a id="srs-func-0049"></a>

| **SRS-FUNC-0049** | **Collar OTA Install Restricted to Charging-Cradle-Docked State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0050, SRS-FUNC-0056 |

<a id="srs-func-0050"></a>

| **SRS-FUNC-0050** | **Docked-Install Gate Shall Not Be Remotely Bypassable** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0049 |

<a id="srs-func-0051"></a>

| **SRS-FUNC-0051** | **Minimum Battery Reserve Before OTA Install** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0049, SRS-FUNC-0057

## 5.4 OTA Image Integrity & Anti-Rollback |

<a id="srs-func-0052"></a>

| **SRS-FUNC-0052** | **Minimum OTA Image Signature Strength** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. |
| **Rationale**    | Derived from PRD §9.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.3 · SRS-FUNC-0053 |

<a id="srs-func-0053"></a>

| **SRS-FUNC-0053** | **OTA Image Signature Verification Before Commit** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. |
| **Rationale**    | Derived from PRD §9.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.3 · SRS-FUNC-0052 |

<a id="srs-func-0054"></a>

| **SRS-FUNC-0054** | **Anti-Rollback via Monotonic Version Counter** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. |
| **Rationale**    | Derived from PRD §9.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.3 |

<a id="srs-func-0055"></a>

| **SRS-FUNC-0055** | **Atomic OTA Installation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. |
| **Rationale**    | Derived from PRD §9.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0056 |

<a id="srs-func-0056"></a>

| **SRS-FUNC-0056** | **Dual-Bank Auto-Revert on Boot Failure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. |
| **Rationale**    | Derived from PRD §9.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0057 |

<a id="srs-func-0057"></a>

| **SRS-FUNC-0057** | **No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. |
| **Rationale**    | Derived from PRD §9.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0051

## 5.6 Update Notification & Status |

<a id="srs-func-0058"></a>

| **SRS-FUNC-0058** | **Device-Side OTA Update State Reporting** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.5 · SRS-FUNC-0059, SRS-FUNC-0060 |

<a id="srs-func-0059"></a>

| **SRS-FUNC-0059** | **App Notification of Available OTA Update (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** notify the user when an OTA firmware update is available. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0043, SRS-FUNC-0044 |

<a id="srs-func-0060"></a>

| **SRS-FUNC-0060** | **App Display of OTA Update State (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** display the current OTA update state reported by the device. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0058

## 5.7 Release Artifacts & Tier-2 Delivery Channel |

<a id="srs-func-0061"></a>

| **SRS-FUNC-0061** | **SBOM Production Per OTA Release** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** produce a Software Bill of Materials for every OTA firmware release. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 |

<a id="srs-func-0062"></a>

| **SRS-FUNC-0062** | **Tier-2 Classifier Delivery Restricted to Embedded OTA Components** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0034, SRS-FUNC-0035, SRS-FUNC-0052

--- |


## 6. Performance


## 6.1 Battery-Life Performance

<a id="srs-perf-0001"></a>

| **SRS-PERF-0001** | **Mini Variant Battery-Life Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's Mini variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §12.1 · SRS-FUNC-0012, SRS-FUNC-0013 |

<a id="srs-perf-0002"></a>

| **SRS-PERF-0002** | **Max Variant Battery-Life Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's Max variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval settings. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §12.1 · SRS-FUNC-0012, SRS-FUNC-0013

## 6.2 Classification & Data-Path Latency |

<a id="srs-perf-0003"></a>

| **SRS-PERF-0003** | **Classification Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** produce a classification result within 2 seconds of the triggering motion event. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-FUNC-0016 |

<a id="srs-perf-0004"></a>

| **SRS-PERF-0004** | **Base Station Cloud-Upload Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-CONN-0014, SRS-CONN-0015

## 6.3 Location & Startup Timing (Max Variant / System) |

<a id="srs-perf-0005"></a>

| **SRS-PERF-0005** | **GNSS Time-to-First-Fix Ceiling (Warm, A-GPS)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.1 |

<a id="srs-perf-0006"></a>

| **SRS-PERF-0006** | **Collar Boot-Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar-mounted device **shall** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-FUNC-0056 |

<a id="srs-perf-0007"></a>

| **SRS-PERF-0007** | **Home/Away Status Update Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-CONN-0004, SRS-CONN-0005 |

<a id="srs-perf-0008"></a>

| **SRS-PERF-0008** | **CCF Twist-Lock Engagement Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** allow the Twist-Lock mechanism to be engaged within 5 seconds. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.1 |


## 7. Safety

# §7 — Safety Requirements


## 7.1 Zone 2 Fuse Tab — Strangulation-Prevention Breakaway

<a id="srs-safe-0001"></a>

| **SRS-SAFE-0001** | **CCF-S Zone 2 Breakaway Force Window (Feline)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-S variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="srs-safe-0002"></a>

| **SRS-SAFE-0002** | **CCF-M Zone 2 Breakaway Force Window (Canine, Medium)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-M variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="srs-safe-0003"></a>

| **SRS-SAFE-0003** | **CCF-L Zone 2 Breakaway Force Window (Canine, Large)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-L variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device+CCF mass does not exceed 26 g. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0004, SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="srs-safe-0004"></a>

| **SRS-SAFE-0004** | **CCF-L Force-Window Contingency for Assembled Mass Exceeding 26 g** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **shall** be revised upward to 30 N. |
| **Rationale**    | Derived from PRD §10.1.4. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.4 · SRS-SAFE-0003 |

<a id="srs-safe-0005"></a>

| **SRS-SAFE-0005** | **Zone 2 Single-Use Restriction** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab **shall not** be capable of being reused or restored to a load-bearing state after fracture. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0013 |

<a id="srs-safe-0006"></a>

| **SRS-SAFE-0006** | **Zone 2 No-Detached-Fragment on Fracture** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon fracture, the Zone 2 Fuse Tab **shall not** produce a detached fragment separate from the CCF body. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b |

<a id="srs-safe-0007"></a>

| **SRS-SAFE-0007** | **Zone 2 Post-Fracture Surface Bluntness** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **shall** be blunt, presenting no sharp edge. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b |

<a id="srs-safe-0008"></a>

| **SRS-SAFE-0008** | **Zone 2 Visible Fracture Indicator** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall** present a visible fracture indicator upon Zone 2 breakaway. |
| **Rationale**    | Derived from PRD §10.1.3.2b. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0013

## 7.2 Zone 1 — Structural Retention (Non-Breakaway) |

<a id="srs-safe-0009"></a>

| **SRS-SAFE-0009** | **Zone 1 Structural Retention Force** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 1 clamp **shall** retain axial loads of at least 50 N without structural failure. |
| **Rationale**    | Derived from PRD §10.1.3.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-safe-0010"></a>

| **SRS-SAFE-0010** | **Zone 1 Survival Through Zone 2 Fracture** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 1 clamp **shall** remain structurally intact following a Zone 2 fracture event. |
| **Rationale**    | Derived from PRD §10.1.3.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-SAFE-0009, SRS-SAFE-0013

## 7.3 Twist-Lock — Retention Safety (Non-Breakaway) |

<a id="srs-safe-0011"></a>

| **SRS-SAFE-0011** | **Twist-Lock Axial Retention Force** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock device-to-CCF interface **shall** retain axial loads exceeding 100 N without disengaging. |
| **Rationale**    | SAFE-0011 is the last mechanical line of defense preventing device separation from the wearer during a pet escape attempt. Failure of this retention means the device detaches entirely, losing all monitoring, safety tracking, and breakaway-event signaling. This aligns it with SRS-INT-0045 (§10) which already carries CRITICAL for the same >100 N requirement. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-PERF-0008 |

<a id="srs-safe-0012"></a>

| **SRS-SAFE-0012** | **Twist-Lock Retention Under Pet-Motion Inertial Loading** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock **shall** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. |
| **Rationale**    | Derived from PRD §10.1.3.2a. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-SAFE-0011

## 7.4 Post-Breakaway Protocol & Re-Use Prevention |

<a id="srs-safe-0013"></a>

| **SRS-SAFE-0013** | **No-Wear-Without-Intact-Zone-2** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device **shall not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.6 · SRS-SAFE-0005, SRS-SAFE-0008 |

<a id="srs-safe-0014"></a>

| **SRS-SAFE-0014** | **Device Separation-Signature Emission** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device **shall** emit a detectable separation signature upon Zone 2 breakaway. |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · SRS-SAFE-0015 |

<a id="srs-safe-0016"></a>

| **SRS-SAFE-0016** | **Zone 2 Non-Fracture Under Chew-Compressive Load** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab **shall not** fracture under a compressive load below 250 N. |
| **Rationale**    | Derived from PRD §13.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.2 · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-safe-0017"></a>

| **SRS-SAFE-0017** | **CCF Body Chew-Penetration Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF body **shall** resist penetration for at least 30 seconds under a 250 N compressive load. |
| **Rationale**    | Derived from PRD §13.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.2 |

<a id="srs-safe-0018"></a>

| **SRS-SAFE-0018** | **Device Enclosure Chew Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials in animal-skin contact on the device enclosure **shall** resist chew-induced damage. |
| **Rationale**    | Derived from PRD §10.1.2. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0016, SRS-SAFE-0017

## 7.6 Device-Absent Socket — Entrapment Prevention |

<a id="srs-safe-0019"></a>

| **SRS-SAFE-0019** | **Device-Absent Socket Entrapment-Hazard Avoidance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF socket **shall** present no independent entrapment hazard when the device is absent. |
| **Rationale**    | Derived from PRD §10.1.3.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.3.5 · SRS-SAFE-0020 |

<a id="srs-safe-0020"></a>

| **SRS-SAFE-0020** | **Device-Absent Socket Probe-Clearance Criterion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-absent CCF socket **shall** provide clearance verified against a 12 mm entrapment-probe criterion. |
| **Rationale**    | Derived from PRD §10.1.3.5. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.5 · SRS-SAFE-0019

## 7.7 Animal-Contact Material Safety |

<a id="srs-safe-0021"></a>

| **SRS-SAFE-0021** | **Animal-Contact Material Non-Toxicity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials in animal-skin contact **shall** be non-toxic. |
| **Rationale**    | Derived from PRD §10.1.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · — (see §17 for REACH/RoHS/Prop 65 mechanism)

## 7.8 Battery-Ingestion Warning |

<a id="srs-safe-0022"></a>

| **SRS-SAFE-0022** | **Battery-Ingestion Warning Labeling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide battery-ingestion warning labeling. |
| **Rationale**    | Derived from PRD §13.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.2 · —

--- |


## 8. Security

**
**Scope note:**  Supplies the "secured connection" referenced by SRS-CONN-0009 (§4) and SRS-FUNC-0047 (§5), closing both orphans. Does NOT restate §5 OTA signature/anti-rollback chain.

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)

<a id="srs-sec-0001"></a>

| **SRS-SEC-0001** | **Mandatory Link-Layer Encryption on Collar↔Base BLE Data-Bearing Links** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. |
| **Rationale**    | Baseline protecting behavioral, location, and event data in transit over the wireless collar↔base channel. The "secured connection" / "secured BLE link" that SRS-CONN-0009 and SRS-FUNC-0047 forward-reference.
| **Verification** | Test |
| **Traceability** | SRS-CONN-0009, SRS-FUNC-0047 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.7 · SRS-CONN-0009, SRS-FUNC-0047 |

<a id="srs-sec-0002"></a>

| **SRS-SEC-0002** | **Mandatory LE Secure Connections Pairing Method** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. |
| **Rationale**    | Underpins SEC-0001 encryption; weaker legacy pairing would undermine the confidentiality guarantee.
| **Verification** | Test |
| **Traceability** | SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009<br><br>## 8.2 Cloud-Bound Transport Security | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009

## 8.2 Cloud-Bound Transport Security |

<a id="srs-sec-0003"></a>

| **SRS-SEC-0003** | **TLS 1.3 Exclusivity for Base-to-Cloud Data Transport** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. |
| **Rationale**    | Generalizes the TLS-1.3-exclusive posture (already applied to OTA via FUNC-0045 per ) to all base↔cloud channels.
| **Verification** | Test |
| **Traceability** | SRS-CONN-0014, SRS-FUNC-0045<br><br>## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)<br><br>No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.<br><br>## 8.4 Device Identity & Platform Trust | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.5 · SRS-CONN-0014, SRS-FUNC-0045

## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.

## 8.4 Device Identity & Platform Trust |

<a id="srs-sec-0004"></a>

| **SRS-SEC-0004** | **Unique Cryptographic Identity at Manufacturing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. |
| **Rationale**    | Per-device unique identity underpins secure boot attestation and per-device compromise containment.
| **Verification** | Inspection |
| **Traceability** | SRS-SEC-0005 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 · SRS-SEC-0005 |

<a id="srs-sec-0005"></a>

| **SRS-SEC-0005** | **Secure Boot Anchored in Hardware Root of Trust** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. |
| **Rationale**    | Prevents execution of unauthorized firmware from non-OTA write paths. Boot-time integrity checking consumes part of the PERF-0006 ≤3 s budget — distinct dimensions, flagged for cross-section awareness.
| **Verification** | Test |
| **Traceability** | SRS-SEC-0004, SRS-FUNC-0053, SRS-PERF-0006<br><br>## 8.5 Vulnerability Disclosure (pre-launch gate only) | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.7 · SRS-SEC-0004, SRS-FUNC-0053, SRS-PERF-0006

## 8.5 Vulnerability Disclosure (pre-launch gate only) |

<a id="srs-sec-0006"></a>

| **SRS-SEC-0006** | **Public Vulnerability-Disclosure Policy in Place Before Launch** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall have a public vulnerability-disclosure policy in place before product launch. |
| **Rationale**    | Published disclosure channel must exist at launch. Lifetime maintenance in §16.
| **Verification** | Inspection |
| **Traceability** | — | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 |


## 9. Data Requirements

# SRS §9 — Data Requirements (v2)

## 9.1 Introduction and Scope Boundary

This section specifies requirements governing the **content, storage, integrity, privacy, and protection** of data produced by the LUUCIPet Wellness Monitor collar (Mini and Max variants). It covers what classification and event data *is* and how it must be handled on-device — not the transport protocol mechanics, which are specified in SRS §4 (CONN), nor the classification algorithm itself, which is specified in SRS §3 (FUNC), nor transport-layer cryptography, which is specified in SRS §8 (SEC). Where a data-layer requirement is closely coupled to an existing connectivity requirement, a cross-reference is given rather than a duplicate statement.

Per the standing scope model, functions performed by parties outside this build (Mobile App team, IoT Cloud backend team) are documented as non-normative boundary notes in §9.11 rather than silently omitted.

Applicable regulatory instruments for this section (from the Regulatory Map) are GDPR (EU) 2016/679, UK GDPR + DPA 2018, PIPEDA, CCPA/CPRA (indicative), and the data-protection-relevant provisions of ETSI EN 303 645:2025. Cybersecurity vulnerability-management obligations under the RED Delegated Act, EU CRA, and UK PSTI Act are addressed in SRS §8 (SEC) and are not repeated here.

---

## 9.2 Classification Record Format & Schema

<a id="srs-data-0001"></a>

| **SRS-DATA-0001** | **Classification Record Content** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0002"></a>

| **SRS-DATA-0002** | **Confidence Score Bound** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0003"></a>

| **SRS-DATA-0003** | **Record Timestamp Accuracy** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall timestamp each classification record with UTC time accurate to within 1 second. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0004"></a>

| **SRS-DATA-0004** | **GNSS Context on Max Variant** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max variant, the system shall append the most recent GNSS fix to the classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 |

<a id="srs-data-0005"></a>

| **SRS-DATA-0005** | **On-Device Storage Duration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. |
| **Rationale**    | Derived from PRD §7.5; PRD §10.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5; PRD §10.6 |

<a id="srs-data-0006"></a>

| **SRS-DATA-0006** | **Retention Through Power Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall preserve stored classification records without corruption across a power-loss event. |
| **Rationale**    | Derived from PRD §10.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.6 |

<a id="srs-data-0007"></a>

| **SRS-DATA-0007** | **Storage Corruption Detection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall detect corruption of stored classification records prior to transmission. |
| **Rationale**    | Derived from PRD §10.6. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §10.6 |

<a id="srs-data-0008"></a>

| **SRS-DATA-0008** | **Classification Independent of Connectivity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall perform classification and record generation independent of BLE connectivity state. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.6 |

<a id="srs-data-0009"></a>

| **SRS-DATA-0009** | **Record Forwarding Without Corruption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall forward stored classification records to the transport layer without introducing data corruption. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.6 |

<a id="srs-data-0010"></a>

| **SRS-DATA-0010** | **Record Forwarding Without Sequence Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.6 |

<a id="srs-data-0011"></a>

| **SRS-DATA-0011** | **Raw Sensor Data Transmission Boundary** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall not transmit raw accelerometer data beyond the collar. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7 |

<a id="srs-data-0012"></a>

| **SRS-DATA-0012** | **On-Device Normalization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall perform normalization of sensor data on-device prior to classification. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7 |

<a id="srs-data-0013"></a>

| **SRS-DATA-0013** | **No Cloud Round-Trip for Classification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall not require a cloud round-trip to complete a classification decision. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7 |

<a id="srs-data-0014"></a>

| **SRS-DATA-0014** | **Raw Sample Retention Minimization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. |
| **Rationale**    | Derived from PRD §7.7; STD: RM-0015 §Art.25. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7; STD: RM-0015 §Art.25 |

<a id="srs-data-0015"></a>

| **SRS-DATA-0015** | **Buffered Data Retention Until Acknowledgement** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. |
| **Rationale**    | Derived from PRD §8.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.4 |

<a id="srs-data-0016"></a>

| **SRS-DATA-0016** | **No Buffer Clear on Disconnect Alone** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. |
| **Rationale**    | Derived from PRD §8.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.4 |

<a id="srs-data-0017"></a>

| **SRS-DATA-0017** | **Stale-Data Flag on Delayed Upload** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. |
| **Rationale**    | Derived from PRD §8.7. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.7 |

<a id="srs-data-0018"></a>

| **SRS-DATA-0018** | **Data Minimization for Personal Data** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. |
| **Rationale**    | Derived from STD: RM-0015 §Art.5(1)(c). | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.5(1)(c) |

<a id="srs-data-0019"></a>

| **SRS-DATA-0019** | **Purpose Limitation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. |
| **Rationale**    | Derived from STD: RM-0015 §Art.5(1)(b). | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.5(1)(b) |

<a id="srs-data-0020"></a>

| **SRS-DATA-0020** | **On-Device Data Deletion Support** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. |
| **Rationale**    | Derived from STD: RM-0015 §Art.17. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.17 |

<a id="srs-data-0021"></a>

| **SRS-DATA-0021** | **On-Device Data Access Support** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. |
| **Rationale**    | Derived from STD: RM-0015 §Art.15. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.15 |

<a id="srs-data-0022"></a>

| **SRS-DATA-0022** | **Consumer Privacy Rights Contingency (CCPA/CPRA)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. |
| **Rationale**    | Derived from STD: RM-0017. | **Priority**     | Low |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0017 |

<a id="srs-data-0023"></a>

| **SRS-DATA-0023** | **Data-at-Rest Encryption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. |
| **Rationale**    | Derived from STD: RM-0015 §Art.32; STD: RM-0019 §Prov.5.8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0015 §Art.32; STD: RM-0019 §Prov.5.8 |

<a id="srs-data-0024"></a>

| **SRS-DATA-0024** | **Transport to Cloud Device-Management Layer** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. |
| **Rationale**    | Derived from PRD §6.1; ASSUMPTION: A-0015. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.1; ASSUMPTION: A-0015 |

<a id="srs-data-0025"></a>

| **SRS-DATA-0025** | **Breakaway Record Commit Timing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. |
| **Rationale**    | Derived from ASSUMPTION: A-0018. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | ASSUMPTION: A-0018 |

<a id="srs-data-0026"></a>

| **SRS-DATA-0026** | **Breakaway Record Survivability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. |
| **Rationale**    | Derived from ASSUMPTION: A-0018. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | ASSUMPTION: A-0018 |

<a id="srs-data-0027"></a>

| **SRS-DATA-0027** | **Breakaway Record Transmission Trigger** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall transmit a committed breakaway event record on the next successful base-station contact following separation. |
| **Rationale**    | Derived from ASSUMPTION: A-0018. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | ASSUMPTION: A-0018 |


## 10. Interface Requirements

**Version:** v6
**Session:** S-luucipet
**Status:** APPROVED — v6: SRS-INT-0036 reissued with quantified drainage criterion (5 mL/15 s/≤0.2 mL) per [ASSUMPTION: A-0023]; v5: cross-conflict resolutions applied per Conflict & Consistency Resolver — / (INT-0035 back-XR +SRS-HW-0004, link-only), / (INT-0008 back-XR +SRS-HW-0019, link-only), / (INT-0032 Priority HIGH→CRITICAL, aligns with HW-0025 CRITICAL framing of the pogo-pin+magnet assembly; priority field only, no text change). All three §10-side only — no approval revocation. v4: cross-section resolutions applied per Conflict & Consistency Resolver — / (INT-0027 cross-ref SRS-OPER-0005→SRS-OPER-0004 + footer relied-upon list corrected), / (INT-0008 Priority HIGH→MEDIUM, aligns with §4 SRS-CONN-0007), / (INT-0029 Priority HIGH→MEDIUM, aligns with §6 SRS-PERF-0005), / (INT-0051 Priority MEDIUM→LOW, aligns with §6 SRS-PERF-0008).  (INT-0045 vs §7 SRS-SAFE-0011) resolved §7-side (SAFE-0011 HIGH→CRITICAL by Requirements Drafter); INT-0045 remains CRITICAL, unchanged here (). v3:  (§10.4 terminology standardization),  (INT-0033↔INT-0049 reciprocal cross-refs + clarifiers),  (INT-0047 Priority MEDIUM→HIGH) applied per Conflict & Consistency Resolver. v2: torque contradiction (INT-0044/0047) and verification-method fixes (INT-0036, INT-0056) applied per Feasibility Checker & Verification-Method Validator flags

---

## 10.0 Scope Note

<a id="srs-int-0001"></a>

| **SRS-INT-0001** | **Collar BLE Peripheral Role** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall implement the Bluetooth Low Energy (BLE) 5.x radio interface in the peripheral role. |
| **Rationale**    | The collar is the advertising/connectable endpoint of the collar-to-base-station link; role assignment is imposed by the system architecture. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0002"></a>

| **SRS-INT-0002** | **Base Station BLE Central Role** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall implement the BLE 5.x radio interface in the central role. |
| **Rationale**    | The base station scans for and initiates connections to collar devices; role assignment is imposed by the system architecture. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §11.2 · SRS-INT-0001 |

<a id="srs-int-0003"></a>

| **SRS-INT-0003** | **Minimum Concurrent Collar Sessions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall support at least 4 concurrent BLE connections to collar devices. |
| **Rationale**    | A multi-pet household requires the base station to hold multiple simultaneous collar links without dropping connections. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0004"></a>

| **SRS-INT-0004** | **Default BLE Advertising Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. |
| **Rationale**    | Establishes the out-of-box discoverability cadence balancing power consumption against connection latency. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0005"></a>

| **SRS-INT-0005** | **Configurable BLE Advertising Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. |
| **Rationale**    | Allows the advertising cadence to be tuned for household-specific power/latency trade-offs. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0006"></a>

| **SRS-INT-0006** | **Advertising Continuity During Active Connection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall continue BLE advertising while maintaining an active BLE connection. |
| **Rationale**    | Preserves discoverability for additional base stations in a multi-base household while a collar is already connected to one base station. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0007"></a>

| **SRS-INT-0007** | **BLE Address Randomization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall randomize its BLE device address. |
| **Rationale**    | Prevents long-term tracking of the wearable by third parties observing BLE advertisements. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0008"></a>

| **SRS-INT-0008** | **Minimum BLE Transmit Power** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall transmit BLE signals at a power level of at least +8 dBm. |
| **Rationale**    | A minimum TX power floor is necessary to meet the stated open-air range target. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-INT-0009, SRS-HW-0019 |

<a id="srs-int-0009"></a>

| **SRS-INT-0009** | **Minimum BLE Open-Air Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE link between the collar device and the base station shall maintain connectivity at an open-air separation distance of at least 9 meters. |
| **Rationale**    | Defines the minimum usable range for typical household room-to-room and yard-adjacent operation. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-INT-0008 |

<a id="srs-int-0010"></a>

| **SRS-INT-0010** | **BLE Link-Layer Encryption Algorithm** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall encrypt all BLE data-bearing links using AES-128 CCM. |
| **Rationale**    | Mandated link-layer confidentiality/integrity mechanism for all collar-to-base-station traffic. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0011"></a>

| **SRS-INT-0011** | **BLE Pairing via LE Secure Connections** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall establish BLE pairing between the collar device and the base station using LE Secure Connections. |
| **Rationale**    | Provides the pairing-time key-exchange mechanism underpinning the mandated link-layer encryption. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-INT-0010 |

<a id="srs-int-0012"></a>

| **SRS-INT-0012** | **QR Out-of-Band Pairing Mechanism** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station. |
| **Rationale**    | Defines the device/base-station-side OOB pairing mechanism; the mobile app's presentation of the QR code to the user is out of scope for this SRS and is attributed to the (out-of-scope) Mobile App per the standing scope boundary. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0013"></a>

| **SRS-INT-0013** | **BLE Radio Regulatory Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US), [STD: RED 2014/53/EU] (EU), [STD: UK Radio Equipment Regulations 2017] (UK), [STD: ISED RSS-247] (CA), and [STD: AS/NZS 4268:2017] (AU/NZ). |
| **Rationale**    | Market access for an intentional 2.4 GHz radiator requires conformance to each target market's radio-equipment regulation. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0014"></a>

| **SRS-INT-0014** | **Bluetooth SIG Qualification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). |
| **Rationale**    | Bluetooth SIG membership terms mandate qualification of any BLE product before market release. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: Bluetooth SIG Qualification (QDID) |

<a id="srs-int-0015"></a>

| **SRS-INT-0015** | **RF Human-Exposure Assessment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface should undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4 GHz transmission. |
| **Rationale**    | A continuously worn 2.4 GHz transmitter plausibly triggers per-market RF-exposure assessment; applicability and thresholds are per-market INDICATIVE per the Regulatory Map and not yet CONFIRMED, hence a SHOULD rather than SHALL. | **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0016"></a>

| **SRS-INT-0016** | **Wi-Fi Radio Band and Standard** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n]. |
| **Rationale**    | Defines the base-to-cloud uplink radio band and PHY/MAC standard. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 |

<a id="srs-int-0017"></a>

| **SRS-INT-0017** | **Cloud Uplink Transport Encryption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. |
| **Rationale**    | Mandated transport-layer confidentiality/integrity mechanism for base-station-to-cloud traffic; the device/base-station side of this transport is in scope, cloud-side storage/analytics is out of scope [ASSUMPTION A-0015]. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.5 |

<a id="srs-int-0018"></a>

| **SRS-INT-0018** | **Default Access-Point Configuration Compatibility** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. |
| **Rationale**    | Avoids requiring the owner to perform non-default router configuration for base-station setup. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.6 |

<a id="srs-int-0019"></a>

| **SRS-INT-0019** | **Minimum Wi-Fi Uplink Signal Condition** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. |
| **Rationale**    | Resolves the PRD's unbounded "reliable Wi-Fi" assumption with an engineered numeric floor; below this bound the ≥30-day offline buffering behavior (Data Requirements, §9) is the defined degraded-mode fallback rather than a new interface requirement. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | ASSUMPTION A-0009 |

<a id="srs-int-0020"></a>

| **SRS-INT-0020** | **Wi-Fi Radio Regulatory Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US) and [STD: RED 2014/53/EU] (EU). |
| **Rationale**    | Market access for the base station's Wi-Fi radio requires conformance to each target market's radio-equipment regulation. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0021"></a>

| **SRS-INT-0021** | **GNSS Interface Presence on Max** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall implement a passive (receive-only) GNSS interface. |
| **Rationale**    | GNSS is a defining differentiator of the Max variant, providing location context unavailable on Mini. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0022"></a>

| **SRS-INT-0022** | **GNSS Interface Absence on Mini** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar variant shall not implement a GNSS interface. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet its ≤10 g weight budget and BLE-only positioning. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0023"></a>

| **SRS-INT-0023** | **Configurable GNSS Fix Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. |
| **Rationale**    | Allows the fix cadence to be tuned against the battery-life-vs-fix-interval trade-off documented in the PRD. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0024"></a>

| **SRS-INT-0024** | **Default GNSS Fix Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall apply a default GNSS fix interval of 2 hours. |
| **Rationale**    | Establishes the out-of-box fix cadence consistent with the stated ≥45-day @2h battery-life target. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0025"></a>

| **SRS-INT-0025** | **A-GPS Assistance Data Delivery** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. |
| **Rationale**    | A-GPS delivery over the existing BLE link is the defined mechanism for reducing GNSS fix acquisition time. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0026"></a>

| **SRS-INT-0026** | **A-GPS Assistance Data Validity Window** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. |
| **Rationale**    | Bounds how long stale assistance data may be relied upon before fix-acquisition performance degrades. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0027"></a>

| **SRS-INT-0027** | **GNSS Power Gating During HOME State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. |
| **Rationale**    | The GNSS smart power gate underpins the stated Max battery-longevity targets; gating authority rests solely with the device-local state machine per the confirmed in-scope/external boundary. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 · SRS-OPER-0004 |

<a id="srs-int-0028"></a>

| **SRS-INT-0028** | **GNSS Fix Acquisition Timeout** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. |
| **Rationale**    | Bounds the power expenditure of an unsuccessful fix attempt. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0029"></a>

| **SRS-INT-0029** | **Warm GNSS Time-to-First-Fix Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. |
| **Rationale**    | Bounds the latency between a scheduled fix attempt and an available location result. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-INT-0025 |

<a id="srs-int-0030"></a>

| **SRS-INT-0030** | **GNSS Intentional-Radiator Exemption Status** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. |
| **Rationale**    | The PRD defers this exemption determination to Regulatory Lead confirmation per market; the Regulatory Map carries this as INDICATIVE, not CONFIRMED, hence a SHOULD rather than SHALL pending resolution. | **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0031"></a>

| **SRS-INT-0031** | **Pogo-Pin Contact Count and Function** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) shall provide a 2-contact electrical charging interface carrying VBUS and GND. |
| **Rationale**    | Defines the minimal electrical contact interface for charging; cross-variant identical geometry is already established by SRS-COMP-0003. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.5 · SRS-COMP-0003 |

<a id="srs-int-0032"></a>

| **SRS-INT-0032** | **Magnetic Charging Alignment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. |
| **Rationale**    | Magnetic alignment enables reliable tool-free docking without precise manual contact placement. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.6 |

<a id="srs-int-0033"></a>

| **SRS-INT-0033** | **First-Attempt Docking Seating Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. |
| **Rationale**    | Bounds the usability of the magnetic docking mechanism to a measurable success rate. Note: this magnetic assist governs the charging-dock (collar device onto charging cradle) interface and is distinct from the device-to-CCF Twist-Lock engagement assist in SRS-INT-0049, though both specify an "up to 5 mm" approach distance. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.5 · SRS-INT-0049 |

<a id="srs-int-0034"></a>

| **SRS-INT-0034** | **Full-Charge Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall reach full charge within 2 hours when docked at the charging interface. |
| **Rationale**    | Bounds the time an owner must leave a device docked to restore full charge. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.5 |

<a id="srs-int-0035"></a>

| **SRS-INT-0035** | **IP67 Rating When Undocked** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. |
| **Rationale**    | The exposed pogo-pin contact is a potential ingress path and must not compromise the device-standalone IP67 rating. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.6 · SRS-HW-0004 |

<a id="srs-int-0036"></a>

| **SRS-INT-0036** | **Charging Socket Self-Drainage** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state the socket "shall be self-draining" with no quantified acceptance criterion; the Verification-Method Validator flagged this as method/criterion incoherence — the declared Test method (correctly changed from Inspection) had nothing measurable to test against. [ASSUMPTION: A-0023] resolves this gap (engineered by analogy to A-0007). This requirement shares its underlying drainage claim with SRS-HW-0008 (§11, hardware-geometry framing of the same socket); both corrected together. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §10.5 · SRS-HW-0008 |

<a id="srs-int-0037"></a>

| **SRS-INT-0037** | **Charging-Access Removal Rotation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. |
| **Rationale**    | Defines the workflow by which the charging contacts are exposed for docking, using the non-breakaway Twist-Lock mechanism. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.6 · SRS-INT-0039 |

<a id="srs-int-0038"></a>

| **SRS-INT-0038** | **Device-Absent Socket Entrapment Geometry** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature. |
| **Rationale**    | Resolves the PRD's unbounded "no independent entrapment hazard" statement with an engineered geometric probe criterion. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | ASSUMPTION A-0010 |

<a id="srs-int-0039"></a>

| **SRS-INT-0039** | **Bayonet Lug Configuration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock mechanical interface shall employ a Twist-Lock mechanical retention interface with three equally-spaced lugs at 120-degree radial separation. |
| **Rationale**    | Defines the base geometric arrangement of the device-to-CCF mechanical attachment; identical across Mini/Max per SRS-COMP-0003. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a · SRS-COMP-0003 |

<a id="srs-int-0040"></a>

| **SRS-INT-0040** | **Lock/Unlock Rotation Angle** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock mechanical interface shall engage and release via a 90-degree rotation. |
| **Rationale**    | Defines the actuation travel required to lock or unlock the device from the CCF. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0041"></a>

| **SRS-INT-0041** | **Lug Ramp Self-Locking Profile** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock lug ramp shall have a trapezoidal profile with an 8-degree self-locking angle. |
| **Rationale**    | The ramp angle is imposed to achieve self-locking behavior without requiring a separate latch. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0042"></a>

| **SRS-INT-0042** | **Twist-Lock Lug Dimensions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each Twist-Lock lug shall be 4.0 mm wide by 1.2 mm thick. |
| **Rationale**    | Fixed lug dimensions are required for interoperability across all CCF SKUs and both collar variants. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0043"></a>

| **SRS-INT-0043** | **Asymmetric Keying Lug** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct engagement orientation. |
| **Rationale**    | Prevents incorrect-orientation assembly of the device onto the CCF. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0044"></a>

| **SRS-INT-0044** | **Detent Release Torque Window** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock detent shall release within a torque window of 0.08 to 0.10 N·m. |
| **Rationale**    | Bounds the rotational effort at which the detent yields, balancing inadvertent-release resistance against ease of intentional removal; upper bound narrowed from 0.15 N·m to 0.10 N·m to align with SRS-INT-0047's engage/release torque ceiling, per PRD §10.1.3.2a's intent that detent release remain at or below the engage torque ceiling. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-INT-0047 |

<a id="srs-int-0045"></a>

| **SRS-INT-0045** | **Twist-Lock Axial Retention Floor** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. |
| **Rationale**    | The Twist-Lock is explicitly not a breakaway mechanism; it must retain the device under normal and inertial loading (distinct from the Zone 2 Fuse Tab, which is governed under Safety Requirements). | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 |

<a id="srs-int-0046"></a>

| **SRS-INT-0046** | **Twist-Lock Engagement Insertion Force Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall require no more than 5 N of axial press-in force to engage. |
| **Rationale**    | Bounds the physical effort required of the owner during the engagement workflow. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 |

<a id="srs-int-0047"></a>

| **SRS-INT-0047** | **Twist-Lock Engagement Rotation Torque Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. |
| **Rationale**    | Bounds the rotational effort required of the owner during the engage/remove workflow. Priority raised MEDIUM→HIGH () so this governing torque ceiling is at least as critical as the dependent detent-release window (SRS-INT-0044, HIGH) that is bounded by it. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 · SRS-INT-0044 |

<a id="srs-int-0048"></a>

| **SRS-INT-0048** | **Engagement Feedback** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. |
| **Rationale**    | Confirms to the owner that the device has reached the fully locked position without requiring visual inspection. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0049"></a>

| **SRS-INT-0049** | **Magnetic Engagement Assist Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall provide magnetic engagement assistance effective at an approach distance of up to 5 mm. |
| **Rationale**    | Assists initial alignment of the device onto the CCF socket before rotation. Note: this Twist-Lock (device-to-CCF) magnetic engagement assist is distinct from the charging-dock magnetic alignment in SRS-INT-0033, though both specify an "up to 5 mm" approach distance. | **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-INT-0033 |

<a id="srs-int-0050"></a>

| **SRS-INT-0050** | **Tool-Free Twist-Lock Operation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall be operable without tools. |
| **Rationale**    | Owners must be able to engage and remove the device without specialized equipment. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0051"></a>

| **SRS-INT-0051** | **Twist-Lock Engagement Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall be engageable within 5 seconds. |
| **Rationale**    | Bounds the time required to complete the mechanical engagement step of the CCF-install workflow. | **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 |

<a id="srs-int-0052"></a>

| **SRS-INT-0052** | **Common Device-Enforced Protocol Across Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall implement a single, cross-variant BLE application protocol governing all collar-to-base-station communication shared across all collar and base-station firmware variants. |
| **Rationale**    | A single shared protocol avoids per-variant protocol fragmentation and depends on the protocol/ICD being frozen before verification per A-0001. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0001 |

<a id="srs-int-0053"></a>

| **SRS-INT-0053** | **Payload Type — Behavioral Classification Record** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. |
| **Rationale**    | Behavioral records are the primary data product synced from collar to base station and require an identifiable payload type. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-int-0054"></a>

| **SRS-INT-0054** | **Payload Type — BLE Sighting Report** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (RSSI), timestamp, and base station identifier, as a distinct payload type. |
| **Rationale**    | Sighting reports are the data basis for home/away geo-fence determination and are reported independent of behavioral-data sync. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 |

<a id="srs-int-0055"></a>

| **SRS-INT-0055** | **Payload Type — Configuration Downlink** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol **shall** support transport of cloud-originated configuration data as a distinct payload type. |
| **Rationale**    | Configuration downlink is a distinct data flow from collar-to-base uplink and requires its own payload type. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.6 |

<a id="srs-int-0061"></a>

| **SRS-INT-0061** | **Payload Type — OTA Firmware Image Downlink** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol **shall** support transport of OTA firmware images as a distinct payload type. |
| **Rationale**    | OTA image delivery is a distinct data flow from collar-to-base uplink and configuration downlink, requiring its own payload type. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.6 · SRS-INT-0055 |<a id="srs-int-0056"></a>

| **SRS-INT-0056** | **Base Station Payload Content Opacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. |
| **Rationale**    | Keeps behavioral-data interpretation logic on the collar/cloud endpoints only, avoiding base-station firmware dependency on payload semantics; verification method corrected from Test to Inspection because this is a negative architectural claim (absence of interpretation logic) that black-box behavioral testing cannot conclusively prove — a base station could interpret payload content internally and still relay it correctly, defeating a Test-based check. Design/firmware/code review confirming no semantic-parsing logic exists on the relay path is the appropriate method. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.3 |

<a id="srs-int-0057"></a>

| **SRS-INT-0057** | **Collar Buffer Retention Pending Acknowledgment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the base station. |
| **Rationale**    | Prevents data loss from premature buffer clearing before successful delivery is confirmed. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 |

<a id="srs-int-0058"></a>

| **SRS-INT-0058** | **No FIFO Clear on Disconnect Alone** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. |
| **Rationale**    | A disconnection is not itself confirmation of delivery; clearing on disconnect alone would risk silent data loss. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 · SRS-INT-0057 |

<a id="srs-int-0059"></a>

| **SRS-INT-0059** | **Sequence-Loss Detection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. |
| **Rationale**    | Enables the receiving side to detect gaps in the forwarded record stream without depending on a specific transport-level guarantee. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |

<a id="srs-int-0060"></a>

| **SRS-INT-0060** | **Corruption-Free Record Forwarding** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. |
| **Rationale**    | Ensures the integrity of behavioral data is preserved end-to-end across the BLE hop. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |


## 11. Hardware Physical Mechanical

# §11 — Hardware / Physical & Mechanical Requirements


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

<a id="srs-hw-0001"></a>

| **SRS-HW-0001** | **Mini Variant Maximum Device Mass** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar device **shall** have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. |
| **Rationale**    | The ≤10 g budget is the core differentiator for the cat/small-dog cohort and drives every downstream component-mass allocation.
| **Verification** | Test |
| **Traceability** | SRS-HW-0011, SRS-HW-0016 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 · SRS-HW-0011, SRS-HW-0016 |

<a id="srs-hw-0002"></a>

| **SRS-HW-0002** | **Max Variant Maximum Device Mass** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar device **shall** have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. |
| **Rationale**    | The ≤22 g budget bounds the large/service-dog variant including the GNSS receiver and larger cell.
| **Verification** | Test |
| **Traceability** | SRS-HW-0012, SRS-HW-0017<br><br>## 11.2 Enclosure & Ingress Protection | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 · SRS-HW-0012, SRS-HW-0017

## 11.2 Enclosure & Ingress Protection |

<a id="srs-hw-0003"></a>

| **SRS-HW-0003** | **Device-Standalone IP67 Ingress Rating** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. |
| **Rationale**    | Device-standalone IP67 is the governing waterproofing claim; the CCF-mated and charging-interface-specific cases are bounded separately.
| **Verification** | Test |
| **Traceability** | SRS-INT-0035, SRS-HW-0004 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.2 · SRS-INT-0035, SRS-HW-0004 |

<a id="srs-hw-0004"></a>

| **SRS-HW-0004** | **Exposed Pogo-Pin Ingress Integrity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device enclosure **shall** maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. |
| **Rationale**    | The pogo-pin aperture is the primary ingress-path risk on an otherwise sealed enclosure.
| **Verification** | Test |
| **Traceability** | SRS-HW-0003, SRS-INT-0035 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.2 · SRS-HW-0003, SRS-INT-0035 |

<a id="srs-hw-0005"></a>

| **SRS-HW-0005** | **Device Status LED Indicator** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** provide a light-emitting-diode status indicator. |
| **Rationale**    | A device-level visual indicator is required for power/charge/pairing status signalling.
| **Verification** | Inspection |
| **Traceability** | —<br><br>## 11.3 Mechanical / Structural Constraints | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · —

## 11.3 Mechanical / Structural Constraints |

<a id="srs-hw-0006"></a>

| **SRS-HW-0006** | **Minimum Wall Thickness at Lug Base** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device enclosure **shall** provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. |
| **Rationale**    | Minimum wall thickness at the highest-stress structural feature preserves enclosure integrity and the seal boundary.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0007, SRS-HW-0003 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-HW-0007, SRS-HW-0003 |

<a id="srs-hw-0007"></a>

| **SRS-HW-0007** | **Lug-Channel Solid-Section Seal Integrity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock lug channels and magnetic insert on the device underside **shall not** penetrate the enclosure wall or the ingress seal path. |
| **Rationale**    | The lug/magnet features must remain solid-section so that mechanical attachment cannot compromise IP67.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0003, SRS-HW-0006 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-HW-0003, SRS-HW-0006 |

<a id="srs-hw-0008"></a>

| **SRS-HW-0008** | **Charging Socket Self-Drainage Criterion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-facing charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state "shall be self-draining" with no quantified criterion. Prior VM=Test (corrected from Inspection per ) was directionally correct but V-Method Validator FLAGged for lacking a measurable criterion. [ASSUMPTION: A-0023] resolves this gap with 5 mL fill / 15 s window / ≤0.2 mL residual in realistic worn orientation. Identical fix applied to SRS-INT-0036 (§10).
| **Verification** | Test |
| **Traceability** | SRS-INT-0036<br><br>## 11.4 CCF Material Composition | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §10.5 · SRS-INT-0036

## 11.4 CCF Material Composition |

<a id="srs-hw-0009"></a>

| **SRS-HW-0009** | **CCF Base Polymer Material** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF body **shall** be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). |
| **Rationale**    | PA66-GF30 provides the stiffness-to-mass ratio and moulded-fuse-tab characteristics the compound-CCF architecture depends on.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0010, SRS-SAFE-0006 | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-HW-0010, SRS-SAFE-0006 |

<a id="srs-hw-0010"></a>

| **SRS-HW-0010** | **CCF UV and Hydrolysis Stabilisation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF material **shall** incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. |
| **Rationale**    | The CCF is worn outdoors for the product lifetime; UV and hydrolysis stabilisation are required to retain breakaway-force properties.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0009 | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-HW-0009 |

<a id="srs-hw-0011"></a>

| **SRS-HW-0011** | **No Metallic Sub-Components in Breakaway Zones** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall not** contain any metallic sub-component within the Zone 2 snap/breakaway region. |
| **Rationale**    | Metallic inserts in the breakaway zone would defeat the calibrated polymer fuse-tab fracture behavior and introduce a sharp-fragment hazard.
| **Verification** | Inspection |
| **Traceability** | SRS-SAFE-0006, SRS-SAFE-0007 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0006, SRS-SAFE-0007 |

<a id="srs-hw-0012"></a>

| **SRS-HW-0012** | **No Chrome or Nickel Plating on Animal-Contact Surfaces** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Animal-contact surfaces of the device and CCF **shall not** use chrome or nickel plating. |
| **Rationale**    | Chrome/nickel are common animal-contact allergens; exclusion is required for the pet-contact material safety case (mechanism detailed in §17).
| **Verification** | Inspection |
| **Traceability** | SRS-SAFE-0021<br><br>## 11.5 Sensing Hardware | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0021

## 11.5 Sensing Hardware |

<a id="srs-hw-0013"></a>

| **SRS-HW-0013** | **Three-Axis MEMS Accelerometer Presence** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a three-axis MEMS accelerometer. |
| **Rationale**    | The accelerometer is the sole primary sensor for the behavioral-classification engine.
| **Verification** | Inspection |
| **Traceability** | SRS-FUNC-0014, SRS-FUNC-0015 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.1 · SRS-FUNC-0014, SRS-FUNC-0015 |

<a id="srs-hw-0014"></a>

| **SRS-HW-0014** | **Accelerometer Output-Data-Rate Capability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device accelerometer **shall** support an output data rate of no less than 50 Hz. |
| **Rationale**    | The classification engine requires ≥50 Hz sampling (SRS-FUNC-0014); the hardware must be capable of sustaining it.
| **Verification** | Test |
| **Traceability** | SRS-FUNC-0014, SRS-FUNC-0008 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.1 · SRS-FUNC-0014, SRS-FUNC-0008 |

<a id="srs-hw-0015"></a>

| **SRS-HW-0015** | **Accelerometer Wake-on-Motion Interrupt** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device accelerometer **shall** provide a wake-on-motion interrupt. |
| **Rationale**    | Wake-on-motion is required to sustain continuous sampling within the collar power budget. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.1 · SRS-HW-0026, SRS-PERF-0001 |

<a id="srs-hw-0029"></a>

| **SRS-HW-0029** | **Accelerometer Hardware FIFO Buffer** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device accelerometer **shall** provide a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. |
| **Rationale**    | A ≥512-byte FIFO with DMA offload is required to sustain continuous sampling within the collar power budget. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.1 · SRS-HW-0015, SRS-PERF-0001 |<a id="srs-hw-0016"></a>

| **SRS-HW-0016** | **GNSS Receiver Absence on Mini** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar device **shall not** incorporate a GNSS receiver. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet the ≤10 g mass budget and BLE-only positioning.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0001, SRS-INT-0022 | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.2 · SRS-HW-0001, SRS-INT-0022 |

<a id="srs-hw-0017"></a>

| **SRS-HW-0017** | **GNSS Receiver Presence on Max** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar device **shall** incorporate a passive receive-only GNSS receiver. |
| **Rationale**    | The Max GNSS receiver is the physical component underlying the location-interface behavior specified in §10.
| **Verification** | Inspection |
| **Traceability** | SRS-INT-0021, SRS-HW-0002<br><br>## 11.6 Wireless Hardware | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.2 · SRS-INT-0021, SRS-HW-0002

## 11.6 Wireless Hardware |

<a id="srs-hw-0018"></a>

| **SRS-HW-0018** | **BLE 5.x Radio Presence** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a Bluetooth Low Energy 5.x radio. |
| **Rationale**    | The BLE radio is the sole collar-to-base-station communication component; its protocol behavior is specified in §10.
| **Verification** | Inspection |
| **Traceability** | SRS-INT-0001, SRS-CONN-0006 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.3 · SRS-INT-0001, SRS-CONN-0006 |

<a id="srs-hw-0019"></a>

| **SRS-HW-0019** | **BLE Radio Transmit-Power Capability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device BLE radio **shall** be capable of a transmit power of no less than +8 dBm. |
| **Rationale**    | The radio hardware must be capable of the +8 dBm floor that the range requirement (SRS-CONN-0006/SRS-INT) depends on.
| **Verification** | Test |
| **Traceability** | SRS-CONN-0007, SRS-INT-0008<br><br>## 11.7 Battery Hardware | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-CONN-0007, SRS-INT-0008

## 11.7 Battery Hardware |

<a id="srs-hw-0020"></a>

| **SRS-HW-0020** | **Mini Minimum Cell Capacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar device **shall** incorporate a battery cell of no less than 120 mAh nominal capacity. |
| **Rationale**    | The §10.4 minimum (not the illustrative §15.3 130 mAh figure) is the governing cell-capacity floor per /A-0006.
| **Verification** | Inspection |
| **Traceability** | SRS-PERF-0001 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-PERF-0001 |

<a id="srs-hw-0021"></a>

| **SRS-HW-0021** | **Max Minimum Cell Capacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar device **shall** incorporate a battery cell of no less than 400 mAh nominal capacity. |
| **Rationale**    | The §10.4 minimum is the governing cell-capacity floor per /A-0006; the §15.3 450 mAh figure is illustrative only.
| **Verification** | Inspection |
| **Traceability** | SRS-PERF-0002 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-PERF-0002 |

<a id="srs-hw-0022"></a>

| **SRS-HW-0022** | **Battery Protection Functions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. |
| **Rationale**    | Li-Po cell protection is a mandatory safety function for an animal-worn sealed device.
| **Verification** | Test |
| **Traceability** | SRS-SAFE-0022 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-SAFE-0022 |

<a id="srs-hw-0023"></a>

| **SRS-HW-0023** | **Battery Transport-Safety Qualification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. |
| **Rationale**    | UN 38.3 is mandatory for lithium-cell transport; the "before pilot" gate is a program milestone.
| **Verification** | Test |
| **Traceability** | SRS-HW-0022 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-HW-0022 |

<a id="srs-hw-0024"></a>

| **SRS-HW-0024** | **Low-Battery Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** raise a low-battery alert at a state-of-charge of 20% or below. |
| **Rationale**    | A 20% SoC alert gives the owner adequate warning before the OTA reserve floor.
| **Verification** | Test |
| **Traceability** | SRS-FUNC-0051<br><br>## 11.8 Charging Hardware | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-FUNC-0051

## 11.8 Charging Hardware |

<a id="srs-hw-0025"></a>

| **SRS-HW-0025** | **Pogo-Pin Charging Contact Hardware** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. |
| **Rationale**    | The pogo-pin + magnet is the physical charging component underlying the interface behavior in §10.
| **Verification** | Inspection |
| **Traceability** | SRS-INT-0031, SRS-INT-0032<br><br>## 11.9 Non-Volatile Storage Hardware | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.5 · SRS-INT-0031, SRS-INT-0032

## 11.9 Non-Volatile Storage Hardware |

<a id="srs-hw-0026"></a>

| **SRS-HW-0026** | **Non-Volatile Classification-Summary Storage Capacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. |
| **Rationale**    | The ≥30-day on-device retention floor requires a matching physical NV storage component.
| **Verification** | Test |
| **Traceability** | SRS-DATA-0005, SRS-DATA-0006<br><br>## 11.10 Compute Hardware | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.6 · SRS-DATA-0005, SRS-DATA-0006

## 11.10 Compute Hardware |

<a id="srs-hw-0027"></a>

| **SRS-HW-0027** | **On-Device Inference Compute Capability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. |
| **Rationale**    | All Tier-1/Tier-2 classification runs on-device; the compute hardware must be capable of it independent of connectivity.
| **Verification** | Test |
| **Traceability** | SRS-FUNC-0031, SRS-DATA-0013 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.7 · SRS-FUNC-0031, SRS-DATA-0013 |

<a id="srs-hw-0028"></a>

| **SRS-HW-0028** | **Compute Architecture With DMA and Hardware Root of Trust** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device compute subsystem **shall** provide direct-memory-access peripheral access and a hardware root of trust. |
| **Rationale**    | DMA peripheral access supports low-power sensing offload (SRS-HW-0015); the hardware root of trust is the physical anchor for secure boot (SRS-SEC-0005).
| **Verification** | Inspection |
| **Traceability** | SRS-SEC-0005, SRS-HW-0015<br><br>--- | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.7 · SRS-SEC-0005, SRS-HW-0015

--- |


## 12. Environmental Durability

# §12 — Environmental & Durability Requirements


## 12.0 Scope Note

This section specifies the environmental exposure conditions, survival criteria, and durability test regimes that the collar device and CCF accessory must withstand: temperature extremes, ingress-protection test parameters, mechanical shock/drop, UV/weathering, chemical exposure, and — for the CCF specifically — post-exposure retention of the safety-critical breakaway-force and detent-torque windows. It does **not** re-issue constraints already owned elsewhere:

- **IP67 device-standalone rating as a physical property**, exposed pogo-pin ingress integrity, and lug-channel solid-section structural integrity are owned by §11 Hardware (SRS-HW-0003/0004/0006/0007); §12 issues the ingress **test-parameter, claim-boundary, and functional-exclusion** requirements built on top of that rating.
- **CCF base-polymer material identity** (PA66-GF30), **UV/hydrolysis stabiliser content** (0.3–0.5%), and **no-metallic-subcomponent** constraints are owned by §11 (SRS-HW-0009/0010/0011); §12 issues the **exposure regime and post-exposure retention** criteria that exercise those material properties.
- **Zone 2 breakaway-force windows** (CCF-S/M/L) and **Twist-Lock detent-torque window** are owned by §7 Safety (SRS-SAFE-0001/0002/0003) and §10 Interfaces (SRS-INT-0044) respectively; §12 requires that these approved windows **remain valid after environmental exposure** — it does not restate the windows themselves.
- **Enclosure chew-resistance** and **animal-contact material non-toxicity** are owned by §7 Safety (SRS-SAFE-0018/0021); §12 references but does not re-issue.
- **REACH/RoHS/Prop 65 material-compliance mechanism** is owned by §17 Standards Compliance / §18 Regulatory; §12 references but does not re-issue.

## 12.1 Temperature

<a id="srs-env-0001"></a>

| **SRS-ENV-0001** | **Device Operating Temperature Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** operate within an ambient temperature range of −20 °C to +50 °C without loss of function. |
| **Rationale**    | Defines the outdoor/indoor thermal envelope the device must remain functional across for pet-wearable use, consistent with the deployment environment (outdoor pet exposure) described in the Product Context Profile.
| **Verification** | Test |
| **Traceability** | SRS-HW-0001, SRS-HW-0002 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-HW-0001, SRS-HW-0002 |

<a id="srs-env-0002"></a>

| **SRS-ENV-0002** | **Device Storage Temperature Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequent operational performance. |
| **Rationale**    | Bounds the non-operating thermal envelope for warehousing, shipping, and retail-shelf conditions, distinct from the in-use operating range.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0001 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0001 |

<a id="srs-env-0003"></a>

| **SRS-ENV-0003** | **CCF Thermal-Cycling Exposure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall** be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of function. |
| **Rationale**    | PRD states the −20 to +50 °C temperature-cycling range without specifying a cycle count, dwell, or ramp profile; A-0003 supplies the IEC 60068-2-14 Test Na default absent a PRD-stated profile.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0015, SRS-ENV-0016 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0015, SRS-ENV-0016 |

<a id="srs-env-0004"></a>

| **SRS-ENV-0004** | **Device Damp-Heat Exposure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **should** withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. |
| **Rationale**    | PRD §13.4 identifies damp-heat testing as a recommended (non-mandatory) environmental qualification test supplementing the IP67 ingress rating.
| **Verification** | Test |
| **Traceability** | SRS-HW-0003<br><br>## 12.2 Ingress Protection<br><br>The IEC 60529 IPX7 test method inherently specifies a 1-metre / 30-minute temporary-immersion parameter; the "IP67 1 m/30 min" figure in PRD §12.5 is therefore the defined test parameter of the rating already required by SRS-HW-0003 (§11), not a separate numeric requirement, and is not re-issued here. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.4 · SRS-HW-0003

## 12.2 Ingress Protection

The IEC 60529 IPX7 test method inherently specifies a 1-metre / 30-minute temporary-immersion parameter; the "IP67 1 m/30 min" figure in PRD §12.5 is therefore the defined test parameter of the rating already required by SRS-HW-0003 (§11), not a separate numeric requirement, and is not re-issued here. |

<a id="srs-env-0005"></a>

| **SRS-ENV-0005** | **Prohibition on IP67 Claims for CCF-Mated Configuration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Product documentation and marketing materials **shall not** state or imply an IP67, or equivalent, ingress-protection rating for the collar device while mated to any CCF. |
| **Rationale**    | The IP67 rating established in SRS-HW-0003 is qualified only for the device-standalone, unmated condition; this requirement prevents an unsubstantiated ingress claim from being communicated for the CCF-mated wear condition.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0003 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.1 fn² · SRS-HW-0003 |

<a id="srs-env-0006"></a>

| **SRS-ENV-0006** | **Independent Laboratory Confirmation of IP67 Rating** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IP67 ingress-protection rating claimed for the collar device **shall** be confirmed by an independent, accredited test laboratory and documented in a test report prior to product launch. |
| **Rationale**    | PRD requires the device-standalone IP67 claim to be "documented and confirmed with lab," establishing an independent-verification gate distinct from the underlying physical capability owned by SRS-HW-0003.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0003 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-HW-0003 |

<a id="srs-env-0007"></a>

| **SRS-ENV-0007** | **Twist-Lock Channel Water-Ingress Exclusion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock lug channels **shall** exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003. |
| **Rationale**    | PRD states the Twist-Lock channels present "no water path"; this requirement establishes the functional (test-level) counterpart to the structural solid-section requirement already owned by SRS-HW-0007.
| **Verification** | Test |
| **Traceability** | SRS-HW-0003, SRS-HW-0007 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.4 · SRS-HW-0003, SRS-HW-0007 |

<a id="srs-env-0008"></a>

| **SRS-ENV-0008** | **Ingress Seal-Boundary Interior Placement** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The ingress-protection seal boundary **shall** be located on the interior side of the enclosure assembly such that it is not directly exposed on any externally accessible mating surface. |
| **Rationale**    | PRD requires the seal boundary to be positioned "interior," protecting it from direct mechanical wear and contamination that would otherwise degrade the IP67 seal over the product's service life.
| **Verification** | Inspection |
| **Traceability** | SRS-HW-0006, SRS-HW-0007<br><br>## 12.3 Mechanical Durability | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-HW-0006, SRS-HW-0007

## 12.3 Mechanical Durability |

<a id="srs-env-0009"></a>

| **SRS-ENV-0009** | **Drop Survival** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. |
| **Rationale**    | Bounds the mechanical shock the device must survive from a typical accidental drop during handling, charging, or removal from an animal.
| **Verification** | Test |
| **Traceability** | — | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 |

<a id="srs-env-0010"></a>

| **SRS-ENV-0010** | **Mechanical Shock Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **should** withstand mechanical shock per IEC 60068-2-27 without loss of function. |
| **Rationale**    | PRD §13.4 identifies shock testing per IEC 60068-2-27 as a recommended supplementary qualification test beyond the explicit 1.5 m drop-survival floor.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0009 | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.4 · SRS-ENV-0009 |

<a id="srs-env-0011"></a>

| **SRS-ENV-0011** | **Vibration Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **should** withstand vibration per IEC 60068-2-64 without loss of function. |
| **Rationale**    | PRD §13.4 identifies vibration testing per IEC 60068-2-64 as a recommended supplementary qualification test, representative of sustained pet-motion vibration exposure.
| **Verification** | Test |
| **Traceability** | —<br><br>## 12.4 UV & Weathering | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.4 · —

## 12.4 UV & Weathering |

<a id="srs-env-0012"></a>

| **SRS-ENV-0012** | **Enclosure UV Stabilization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device enclosure material **shall** be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service lifetime. |
| **Rationale**    | PRD §12.5 requires the enclosure to be "UV-stabilized" but, unlike the CCF (SRS-ENV-0013, 2,000 h per IEC 60068-2-5), states no exposure duration or test method for the enclosure material; flagged per the numeric-vagueness gate rather than an invented duration.
| **Verification** | Analysis |
| **Traceability** | SRS-ENV-0013 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §12.5 · SRS-ENV-0013 |

<a id="srs-env-0013"></a>

| **SRS-ENV-0013** | **CCF UV Aging Exposure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall** withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. |
| **Rationale**    | Bounds the accelerated UV-aging qualification program for the outdoor-worn CCF, consistent with the UV-stabiliser content specified in SRS-HW-0010.
| **Verification** | Test |
| **Traceability** | SRS-HW-0010, SRS-ENV-0017<br><br>## 12.5 Chemical Resistance | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-HW-0010, SRS-ENV-0017

## 12.5 Chemical Resistance |

<a id="srs-env-0014"></a>

| **SRS-ENV-0014** | **CCF Chemical-Fluid Exposure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall** withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across pH 5.5 to 8.5, enzymatic pet-odor and stain cleaners, fresh water, and salt water. |
| **Rationale**    | Bounds the household and outdoor chemical-exposure qualification program representative of routine pet bathing, cleaning, and water-body exposure.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0018<br><br>## 12.6 CCF Environmental Durability — Post-Exposure Retention<br><br>This subsection ties the exposure regimes in §12.1/§12.4/§12.5 back to the Zone 2 breakaway-force windows (SRS-SAFE-0001/0002/0003) and Twist-Lock detent-torque window (SRS-INT-0044) that must remain valid after exposure: a CCF whose fuse tab has drifted out of its calibrated force window after environmental exposure would degrade the pet-safety breakaway function. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0018

## 12.6 CCF Environmental Durability — Post-Exposure Retention

This subsection ties the exposure regimes in §12.1/§12.4/§12.5 back to the Zone 2 breakaway-force windows (SRS-SAFE-0001/0002/0003) and Twist-Lock detent-torque window (SRS-INT-0044) that must remain valid after exposure: a CCF whose fuse tab has drifted out of its calibrated force window after environmental exposure would degrade the pet-safety breakaway function. |

<a id="srs-env-0015"></a>

| **SRS-ENV-0015** | **Post-Thermal-Cycling Zone 2 Fuse-Force Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | PRD explicitly ties CCF temperature cycling to the requirement that "fuse force ... [stays] in-window," making post-cycling retention of the calibrated breakaway-force windows a directly PRD-stated durability criterion.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0003, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0003, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-env-0016"></a>

| **SRS-ENV-0016** | **Post-Thermal-Cycling Twist-Lock Detent-Torque Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Twist-Lock detent release torque **shall** remain within the torque window defined in SRS-INT-0044. |
| **Rationale**    | PRD explicitly ties CCF temperature cycling to the requirement that "detent torque ... [stays] in-window," making post-cycling retention of the calibrated detent-torque window a directly PRD-stated durability criterion.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0003, SRS-INT-0044 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0003, SRS-INT-0044 |

<a id="srs-env-0017"></a>

| **SRS-ENV-0017** | **Post-UV-Aging Zone 2 Fuse-Force Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | PRD states the CCF UV-aging duration and standard but, unlike the thermal-cycling case, does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the same safety-critical retention obligation established for thermal cycling (SRS-ENV-0015) to the UV-aging qualification test, since both exposures act on the same moulded Zone 2 fuse mechanism. Flagged as PRD-silent rather than an invented numeric bound — the force window itself is the pre-approved SRS-SAFE-0001/0002/0003 value.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0013, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0013, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015 |

<a id="srs-env-0018"></a>

| **SRS-ENV-0018** | **Post-Chemical-Exposure Zone 2 Fuse-Force Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | As with SRS-ENV-0017, PRD states the CCF chemical-exposure duration and fluid set but does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the SRS-ENV-0015 retention obligation to the chemical-resistance qualification test on the same safety-critical mechanism. Flagged as PRD-silent rather than an invented numeric bound.
| **Verification** | Test |
| **Traceability** | SRS-ENV-0014, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015<br><br>## 12.7 Material Safety (Cross-Reference — No New Requirements Issued)<br><br>Enclosure chew-resistance (SRS-SAFE-0018) and animal-contact material non-toxicity (SRS-SAFE-0021) are owned by §7 Safety. CCF base-polymer identity, UV/hydrolysis stabiliser content, absence of metallic breakaway-zone subcomponents, and absence of chrome/nickel plating on animal-contact surfaces (SRS-HW-0009, SRS-HW-0010, SRS-HW-0011, SRS-HW-0012) are owned by §11 Hardware. REACH/RoHS/Prop 65 compliance mechanism (PRD §13.2) is owned by §17 Standards Compliance / §18 Regulatory. §12 does not re-issue any of the above; the exposure and retention requirements in §12.1–§12.6 are the environmental-durability complement to these material-safety and material-composition requirements.<br><br>--- | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0014, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015

## 12.7 Material Safety (Cross-Reference — No New Requirements Issued)

Enclosure chew-resistance (SRS-SAFE-0018) and animal-contact material non-toxicity (SRS-SAFE-0021) are owned by §7 Safety. CCF base-polymer identity, UV/hydrolysis stabiliser content, absence of metallic breakaway-zone subcomponents, and absence of chrome/nickel plating on animal-contact surfaces (SRS-HW-0009, SRS-HW-0010, SRS-HW-0011, SRS-HW-0012) are owned by §11 Hardware. REACH/RoHS/Prop 65 compliance mechanism (PRD §13.2) is owned by §17 Standards Compliance / §18 Regulatory. §12 does not re-issue any of the above; the exposure and retention requirements in §12.1–§12.6 are the environmental-durability complement to these material-safety and material-composition requirements.

--- |


## 13. Reliability Availability

# §13 — Reliability & Availability Requirements


## 13.0 Scope Note

This section specifies the dependability, availability, and long-run success-rate criteria the system must sustain over the product's operating life and over defined observation windows. It does **not** re-issue constraints already owned elsewhere:

- **Tier-1 (≥85% accuracy / ≤5% false-positive) and Tier-2 (≥80% accuracy / ≤10% false-positive) classification-accuracy thresholds** in PRD §12.2 restate the classification-accuracy floors already owned by §3 Behavioral Classification (SRS-FUNC-0018, SRS-FUNC-0019, SRS-FUNC-0020, SRS-FUNC-0021); §13 does not re-issue them. They are accuracy/performance criteria, not availability/dependability criteria, notwithstanding their placement under the PRD's "Reliability" heading.
- **The IP67 ingress-protection rating as a component property, the device-standalone qualification scope, and the ingress test-parameter/claim-boundary requirements** are owned by §11 Hardware (SRS-HW-0003) and §12 Environmental & Durability (SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007, SRS-ENV-0008); §13 owns only the additional temporal criterion that the rating must remain valid across the full expected service lifetime, not the rating itself.
- **OTA image integrity, atomicity, and dual-bank auto-revert mechanics** are owned by §5 OTA Firmware Updates (SRS-FUNC-0052–0057); §13 owns only the resulting aggregate success-rate criterion, not the underlying mechanism.

## 13.1 Ingress-Protection Durability

<a id="srs-reli-0001"></a>

| **SRS-RELI-0001** | **IP67 Rating Retention Over Full Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. |
| **Rationale**    | PRD §12.2 states the qualitative criterion "IP67 full lifetime (device standalone)" but does not itself state a numeric service-lifetime duration against which "full lifetime" can be tested. The Product Context Profile records a user-confirmed expected service lifetime of ~2–3 years, with a 2-year floor to be used wherever a single testable figure is required; that floor is applied here as the qualification duration. This requirement is the temporal-endurance complement to the device-standalone IP67 rating already established by SRS-HW-0003 and does not restate the rating itself. \| Verification Method: Analysis \| Cross-References: SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006<br><br>## 13.2 Collar Device Availability | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0002"></a>

| **SRS-RELI-0002** | **Collar Device Operational Availability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. |
| **Rationale**    | PRD §12.2 states "collar operational ≥99% (excl. charging)" as a direct numeric floor, but — unlike the base station uptime criterion in the same clause, which specifies a 90-day measurement window — the PRD does not state the observation-window length over which collar availability is to be measured. Flagged per the numeric-vagueness gate rather than inventing a window; the 99% floor and the charging exclusion are PRD-stated and are issued as-is. Verification Method corrected from Analysis to Test per V-Method review: this is a directly observable field/DVT proportion metric (uptime vs. total non-charging elapsed time), matching the Test pattern this SRS already applies to equivalent rate/proportion criteria (SRS-FUNC-0018–0021, SRS-FUNC-0001); no MTBF-style modeling basis is stated that would justify Analysis. \| Verification Method: Test \| Cross-References: SRS-HW-0025, SRS-INT-0031, SRS-INT-0032<br><br>## 13.3 Base Station Availability | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0003"></a>

| **SRS-RELI-0003** | **Base Station Uptime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. |
| **Rationale**    | PRD §12.2 states "base ≥99.5% uptime over 90-day window" as a direct, fully-bounded numeric criterion; the base station's continuous, mains-powered, no-sleep operating profile (PRD §11.7) makes a rolling-window uptime metric directly measurable in the field. Verification Method corrected from Analysis to Test per V-Method review: the criterion is fully bounded (explicit 90-day window) and directly observable via continuous-operation monitoring against the threshold — a practical DVT/pilot burn-in test, not a modeling exercise. \| Verification Method: Test \| Cross-References: —<br><br>## 13.4 OTA Update Success Rate | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0004"></a>

| **SRS-RELI-0004** | **OTA Update Success Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a base station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. |
| **Rationale**    | PRD §12.2 states "OTA success ≥99%" as a direct numeric floor on the aggregate reliability of the OTA mechanism already specified functionally in §5; "success" is defined operationally against the existing auto-revert criterion (SRS-FUNC-0056) rather than inventing a separate definition. Verification Method corrected from Analysis to Test per V-Method review: this is a repeated-trial pass/fail statistic (run N install attempts, including fault-injected trials per SRS-FUNC-0057, and compute the pass proportion against the 99% floor), matching the Test pattern this SRS already applies to equivalent proportion-based criteria (SRS-FUNC-0001, SRS-FUNC-0018–0021). \| Verification Method: Test \| Cross-References: SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0057<br><br>--- | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |


## 14. Usability

## §14 Usability Requirements

**Scope.**  This section specifies the user-experience and usability requirements for the LUUCIPet Wellness Monitor Phase 1 product family — covering collar-device physical interaction, LED/haptic feedback, pairing and onboarding, base-station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features. The companion app's UI design, in-app navigation, notification content, and analytics dashboard are external (delivered by the Mobile App team); requirements that depend on device-to-app data hand-offs are captured as in-scope interface obligations in §14.7.

**Cross-references:**  Pairing protocol → §4 (CONN). OTA functional requirements → §5 (OTA). Safety-indicator behavior → §7 (SAFE). Twist-Lock mechanical specifications → §11 (COMP-HW). Breakaway detection → A-0018.

---

### 14.1 Pairing & Onboarding

| ID              | Requirement                                                                                                                                                                                                                                                                      | Attributes                                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |

## §14 Usability Requirements

**Scope.**  This section specifies the user-experience and usability requirements for the LUUCIPet Wellness Monitor Phase 1 product family — covering collar-device physical interaction, LED/haptic feedback, pairing and onboarding, base-station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features. The companion app's UI design, in-app navigation, notification content, and analytics dashboard are external (delivered by the Mobile App team); requirements that depend on device-to-app data hand-offs are captured as in-scope interface obligations in §14.7.

**Cross-references:**  Pairing protocol → §4 (CONN). OTA functional requirements → §5 (OTA). Safety-indicator behavior → §7 (SAFE). Twist-Lock mechanical specifications → §11 (COMP-HW). Breakaway detection → A-0018.

---

### 14.1 Pairing & Onboarding

| ID              | Requirement                                                                                                                                                                                                                                                                      | Attributes                                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **SRS-UX-0001** | The collar device shall complete BLE pairing and first-data-sync handshake with a companion app within 3 minutes of the user initiating pairing mode on the device, measured from pairing-mode-entry LED indication to app-confirmed-paired acknowledgment.                      | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                                            |
| **SRS-UX-0002** | The collar device shall support QR-code-based out-of-band (OOB) pairing as the primary pairing method, providing a scannable QR code (on device label or base-station label) that encodes the device identity for LE Secure Connections OOB pairing.                             | CAT=UX PRIORITY=HIGH STABILITY=FIXED **VM=Demonstration** Source: \[PRD §5.6] \[STD: Bluetooth SIG LE Secure Connections] **XR: SRS-CONN-0003** |
| **SRS-UX-0003** | The collar device shall provide a single, visually distinct, and user-accessible physical mechanism (e.g., a recessed or guarded button) to initiate pairing mode, with the mechanism clearly labeled or icon-indicated on the device enclosure.                                 | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Inspection Source: \[PRD §5.6]                                       |
| **SRS-UX-0004** | The collar device LED shall emit a visually distinct indication when the device is in pairing mode (e.g., slow blue blink at 1 Hz, 50% duty cycle) that is distinguishable from all power-on/boot, normal-operation, low-battery, charging, fault, and OTA-state LED patterns defined in §14.3. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test                                                                 |
| **SRS-UX-0005** | The collar device shall automatically exit pairing mode and revert to normal-operation LED indication after 3 minutes if no successful pairing is completed, with no user action required.                                                                                       | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test                                                               |

---

### 14.2 Physical Interaction

| ID              | Requirement                                                                                                                                                                                                                                                             | Attributes                                                               |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| **SRS-UX-0006** | The Twist-Lock mechanism shall provide both an audible click and a tactile force-transition (detent drop) upon successful locking, enabling the user to confirm engagement by sound and feel without visual inspection.                                                 | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |
| **SRS-UX-0007** | The Twist-Lock socket shall provide a magnetic-assist force that draws the device into correct alignment from a distance of ≤5 mm before the lug channels engage, reducing the fine-motor-skill demand of device docking.                                               | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a] |
| **SRS-UX-0008** | The Twist-Lock engage force shall not exceed 5 N press-in axial force and 0.10 N·m rotational torque, enabling a typical adult user to dock the device without a tool or excessive effort. Mechanical specification per §11.                                            | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |
| **SRS-UX-0009** | The device removal workflow (90° counter-clockwise Twist-Lock rotation) shall require a detent-release torque not exceeding 0.15 N·m, such that an adult user can intentionally remove the device without a tool while the mechanism remains inertially immune per §11. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |
| **SRS-UX-0010** | The magnetic pogo-pin charging connector shall achieve ≥90% first-attempt successful seating rate by a user with no prior training, measured in a usability test with a representative sample of ≥20 adult participants across age and dexterity ranges.                | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.5]    |
| **SRS-UX-0011** | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket, providing error-proof (poka-yoke) mating.                                                                                              | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |

---

### 14.3 Visual & Auditory Feedback

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                              | Attributes                                         |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| **SRS-UX-0012** | The collar device LED shall communicate at minimum the following distinct operational states to the user: (a) power-on / boot, (b) pairing mode, (c) normal operation, (d) low battery (≤20% SoC), (e) charging / docked, (f) error or fault, and (g) OTA update in progress. LED physical specification per §11.                                        | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test       |
| **SRS-UX-0013** | Each collar-device operational state enumerated in SRS-UX-0012 shall be communicated via a unique combination of LED color, blink cadence, or duty cycle, such that no two states share an identical visual indicator pattern.                                                                                                                           | CAT=UX **PRIORITY=HIGH** STABILITY=FIXED VM=Test     |
| **SRS-UX-0014** | All collar-device LED state indicators shall differentiate critical states (low battery, error/fault) from non-critical states using at minimum temporal-pattern differentiation (blink cadence), ensuring distinguishability under protanopia and deuteranopia (red/green color-blindness) without reliance on red-vs-green color discrimination alone. | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Analysis |
| **SRS-UX-0015** | The Twist-Lock engagement audible click shall produce a sound pressure level of ≥40 dBA measured at 30 cm from the device in a quiet-room baseline (ambient ≤30 dBA), ensuring a typical adult user can confirm engagement by sound.                                                                                                                     | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test     |

---

### 14.4 Base Station UX

| ID              | Requirement                                                                                                                                                                                                                                                                        | Attributes                                                                             |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| **SRS-UX-0016** | The base station shall communicate via LEDs at minimum: (a) AC power present, (b) device charging active (Charging tier only), (c) cloud connectivity established, and (d) OTA update in progress.                                                                                 | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §11.6]                      |
| **SRS-UX-0017** | The base station LEDs should support an automatic ambient-light-responsive dimming mode below approximately 50 lux, or a user-configurable quiet-hours schedule, to reduce bedroom/nighttime light intrusion.                                                                      | CAT=UX PRIORITY=LOW STABILITY=FIXED VM=Test Source: \[PRD §11.6] \[ASSUMPTION: A-0008] |
| **SRS-UX-0018** | The base station initial setup — from AC power-on through Wi-Fi association and cloud-registration to the "cloud-connected" LED indication — shall complete within 5 minutes for a user following the companion app's guided setup flow, assuming compliant home Wi-Fi per A-0009. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                      |

---

### 14.5 CCF User Experience

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                                                                                       | Attributes                                                                              |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **SRS-UX-0019** | Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type sub-variants) shall be visually and/or tactilely distinguishable from all other variants by at minimum one of: molded-in size designation, distinct body color, or tactile surface differentiation, enabling a user to identify the correct CCF for their pet without measurement tools.                                                     | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Inspection Source: \[PRD §12.4]                 |
| **SRS-UX-0020** | The CCF Zone 1 structural-clamp installation onto a third-party collar shall be achievable by a typical adult user in ≤60 seconds without tools, using only the wrap-and-lock mechanism described in PRD §10.1.3.4.                                                                                                                                                                                               | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                       |
| **SRS-UX-0021** | The CCF Zone 2 fuse tab shall incorporate a clearly visible fracture indicator (e.g., a contrasting-color internal layer exposed on fracture, or a continuous visual element that visibly separates) that is discernible by a user at arm's length (approximately 60 cm) under typical indoor lighting without magnification, enabling the user to visually confirm post-breakaway that the CCF must be replaced. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Inspection Source: \[PRD §10.1.3.2b] \[PRD §10.1.3.6] |

---

### 14.6 Status & Error Communication

| ID              | Requirement                                                                                                                                                                                                                                                                                                                   | Attributes                                                        |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| **SRS-UX-0022** | The collar device shall provide a distinct low-battery LED indication (visually distinct from normal operation per SRS-UX-0013) when the battery state-of-charge reaches ≤20%, and shall persist this indication in every operational state until the device is placed on the charger and charging is confirmed.              | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.4] |
| **SRS-UX-0023** | The collar device shall communicate a fault state (including but not limited to: sensor failure, non-volatile memory corruption, BLE radio initialization failure) via a visually distinct LED pattern that differs from all power-on/boot, normal-operation, low-battery, pairing, charging, and OTA-state patterns.                        | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test                      |
| **SRS-UX-0024** | The collar device shall provide confirmation feedback (LED flash, haptic pulse, or both) within 1 second of a user-initiated physical action (e.g., pairing-mode button press, factory-reset trigger) being successfully registered by the device firmware, so the user is not left uncertain whether the input was received. | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test                    |

---

### 14.7 App-Interface Obligations

> The companion app is delivered by the Mobile App team \[EXTERNAL: Mobile App team]. The requirements in this subsection specify the device-side and base-station-side interface obligations that enable the app's user-facing features. These are in-scope for our delivery.

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Attributes                                                                                               |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **SRS-UX-0025** | The collar device shall include its current battery state-of-charge as a percentage value (0–100) in every sync payload transmitted to the base station, enabling the companion app to display an accurate, real-time battery estimate to the owner.                                                                                                                                                                                                                                                | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                                        |
| **SRS-UX-0026** | The Max collar device shall include the current GNSS fix interval setting (in minutes) in its status payload transmitted in every sync, enabling the companion app to compute and display an interval-aware battery-life estimate and to issue the Max <10-day battery warning.                                                                                                                                                                                                                     | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                                        |
| **SRS-UX-0027** | The collar device shall transmit a persistent breakaway/separation event record as defined in A-0018, flagged with elevated transmission priority, on the next successful base-station contact following a breakaway event, enabling the companion app's "CCF Replacement Required" owner notification. The primary post-breakaway safety mitigation remains the passive CCF visible fracture indicator per SRS-UX-0021; the electronic notification is a secondary, best-effort notification only. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.6] \[PRD §12.4] \[ASSUMPTION: A-0018] |

---

### 14.8 OTA Update UX

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                        | Attributes                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| **SRS-UX-0028** | The collar device shall communicate each distinct OTA update state — Downloading, Verifying, Pending Installation, Installing, Success, and Failed — via a unique LED pattern distinguishable from all other LED states defined in §14.3, enabling the user to understand update progress without the companion app. OTA functional states per §5. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §9.5] |
| **SRS-UX-0029** | The collar device LED shall remain continuously active during an OTA update, with no dark (LED-off) period exceeding 10 seconds during any OTA state expected to last >30 seconds, preventing the user from misinterpreting a prolonged dark period as a device failure or bricked state.                                                          | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test                   |

---

### Summary

| Metric               | Count                                                 |
| :------------------- | :---------------------------------------------------- |
| Total requirements   | 29 (SRS-UX-0001 – SRS-UX-0029)                        |
| Shall (mandatory)    | 28                                                    |
| Should (recommended) | 1 (SRS-UX-0017)                                       |
| Priority: HIGH       | 23                                                    |
| Priority: MEDIUM     | 5                                                     |
| Priority: LOW        | 1 (SRS-UX-0017)                                       |
| VM: Test             | 24                                                    |
| VM: Inspection       | 3 (SRS-UX-0003, SRS-UX-0019, SRS-UX-0021)             |
| VM: Analysis         | 1 (SRS-UX-0014)                                       |
| VM: Demonstration    | 1 (SRS-UX-0002)                                       |
| EXTERNAL attribution | Mobile App team                                       |
| ID range consumed    | SRS-UX-0001 – SRS-UX-0029                             |

## 15. Operational Requirements


## 15.0 Scope Note

This section specifies operational behavior of the deployed system that is not already owned by another section: base-station continuous-operation posture and included power accessory, base-station status-indicator inventory (deferred here from §11 per that section's own Drafter Notes), the device-local home/away determination that other sections' power-gating and status requirements depend on, and the collar's duty-cycle/power-optimization behaviors drawn from PRD §15 (Power Budget) that are operational policies rather than hardware capabilities. It does **not** re-issue constraints already owned elsewhere:

- **GNSS interface behavior** (presence on Max, absence on Mini, configurable/default fix interval, A-GPS delivery/validity, fix-acquisition timeout, warm TTFF ceiling) is owned by §10 Interface Requirements (SRS-INT-0021–0029); this section does not restate those numeric bounds.
- **GNSS smart power-gate non-configurability** and the **Max GNSS interface disablement while HOME** are owned by §2 (SRS-OPER-0004) and §10 (SRS-INT-0027) respectively; this section adds only the device-local home/away determination mechanism those two depend on, which was not yet issued anywhere.
- **Battery cell minimum capacities, battery-life targets, idle-current ceiling, and low-battery alert threshold** are owned by §10.4/§11 Hardware (SRS-HW-0020–0024) and §3 Behavioral Classification (SRS-FUNC-0011); this section does not restate those figures.
- **Base-station Wi-Fi/cloud connectivity reliability bound and degraded-mode offline buffering** are owned by §2 (SRS-OPER-0007) and §4 (SRS-CONN-0028/0029); this section does not restate the −70 dBm / 256 kbps bound.
- **Base-station LED dimming / nighttime-mode `SHOULD`** is fully specified by §14 Usability (SRS-UX-0017, per [ASSUMPTION: A-0008]); this section does not re-issue it, only the base LED *inventory* deferred to this section by §11's own Drafter Notes.
- **OTA mechanics, atomicity, and success-rate criteria** are owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004); this section does not restate them.

## 15.1 Base Station Continuous Operation

<a id="srs-oper-0012"></a>

| **SRS-OPER-0012** | **Base Station Continuous Operational Posture** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** remain in a continuously powered, non-sleeping operational state for as long as AC power is supplied, maintaining active BLE scanning and Wi-Fi uplink capability at all times. |
| **Rationale**    | The base station is a mains-powered, always-available relay; PRD §11.7 states continuous operation with no sleep state and BLE scan/uplink always on, distinguishing its operational posture from the battery-powered, power-optimized collar devices. This continuous posture is also the precondition assumed by the base-station uptime criterion (SRS-RELI-0003) and by the household geo-fence mesh's ability to detect collar sightings without a scheduling gap. \| Verification Method: Demonstration \| Cross-References: SRS-RELI-0003 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.7 |

<a id="srs-oper-0013"></a>

| **SRS-OPER-0013** | **AC Power Adapter Inclusion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** be supplied with an AC-to-USB-C power adapter as an included accessory. |
| **Rationale**    | PRD §11.7 specifies USB-C power with the adapter included, ensuring the base station is immediately operable out of box without requiring the owner to source a separate power adapter. \| Verification Method: Inspection \| Cross-References: none<br><br>## 15.2 Base Station Status Indicators | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.7 |

<a id="srs-oper-0014"></a>

| **SRS-OPER-0014** | **Charging-Tier Base Station LED Inventory** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station (Charging) tier **shall** provide exactly 3 status LEDs, indicating at minimum: AC power presence, device-charging activity, and cloud-connectivity status. |
| **Rationale**    | PRD §4.2/§11.6 specify a 3-LED inventory (power/charging/cloud) for the Charging tier, distinct from the Relay tier's 2-LED inventory (SRS-OPER-0015) because the Relay tier has no charging cradle to indicate. This is a hardware-inventory requirement; the LED *behavior* (indication patterns) for each state is specified by §14 Usability (SRS-UX-0016). \| Verification Method: Inspection \| Cross-References: SRS-OPER-0015, SRS-UX-0016 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.6 |

<a id="srs-oper-0015"></a>

| **SRS-OPER-0015** | **Relay-Tier Base Station LED Inventory** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station (Relay) tier **shall** provide exactly 2 status LEDs, indicating at minimum: AC power presence and cloud-connectivity status. |
| **Rationale**    | The Relay tier omits the charging-activity LED present on the Charging tier (SRS-OPER-0014) because it has no charging cradle to report on, consistent with PRD §4.2's description of the Relay tier as identical to the Charging tier minus the charging cradle. \| Verification Method: Inspection \| Cross-References: SRS-OPER-0014, SRS-UX-0016<br><br>## 15.3 Household Geo-Fence Mesh Participation | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.6 |

<a id="srs-oper-0016"></a>

| **SRS-OPER-0016** | **Multi-Base Household Geo-Fence Mesh Participation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Every base station in a household deployment **shall** participate in a shared geo-fence mesh by independently reporting BLE sighting reports for every collar device within its range. |
| **Rationale**    | PRD §5.3/§4.2 describe up to 8 base stations per household (≥1 Charging) collectively forming a geo-fence mesh; each base station's independent sighting-report contribution (payload structure per SRS-INT-0054) is the mesh's data basis, distinct from the collar-side forwarding-path requirements already owned by §4 (SRS-CONN-0019/0020). \| Verification Method: Demonstration \| Cross-References: SRS-INT-0054, SRS-CONN-0019<br><br>## 15.4 Device-Local Home/Away Determination | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.2 |

<a id="srs-oper-0017"></a>

| **SRS-OPER-0017** | **Device-Local Home/Away State Machine** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) readings from paired base stations in range, without reliance on any cloud-side determination. |
| **Rationale**    | PRD §6.4 states dual home/away state machines exist (device-local and cloud-side), and [ASSUMPTION: A-0016] confirms the device-local state machine is the sole in-scope authority for power gating — notably the Max GNSS smart power gate (SRS-INT-0027, SRS-OPER-0004) — with the cloud-side state machine external ([EXTERNAL: IoT Cloud backend team], SRS-OPER-0011). This requirement establishes the existence and RSSI basis of the device-local mechanism that SRS-INT-0027, SRS-OPER-0004, and SRS-PERF-0007 all depend on but which was not yet issued as its own requirement in any approved section. \| Verification Method: Demonstration \| Cross-References: SRS-INT-0027, SRS-OPER-0004, SRS-PERF-0007, SRS-OPER-0011 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0018"></a>

| **SRS-OPER-0018** | **Device-Local Home-to-Away RSSI Transition Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from HOME to AWAY only when no paired base station RSSI reading exceeds −85 dBm for 5 consecutive readings taken at 1 s intervals. |
| **Rationale**    | PRD §4.1/§6.4 state that home/away determination occurs "via multi-base RSSI" but supply no numeric threshold or debounce criterion; [ASSUMPTION: A-0022] resolves this gap (engineered by analogy to [ASSUMPTION: A-0009]'s Wi-Fi RSSI bound) with a conservative −85 dBm threshold, representing the typical "fair/poor" BLE boundary through 3+ interior walls or 15–25 m open-air range in a residential deployment, deliberately biased toward retaining HOME status because a false-AWAY transition needlessly enables the Max GNSS power gate (SRS-INT-0027, SRS-OPER-0004) and increases power draw, whereas a brief false-HOME delay does not. The 5-consecutive-reading/1 s-interval debounce filters transient RSSI dips (e.g., momentary body-shadowing) before committing the transition. This requirement was returned FAIL by the Feasibility Checker (v1; D3 Testability, D4 Completeness) for being issued as a non-normative PRD-gap notice rather than a testable SHALL; it is reissued here as a testable predicate now that [ASSUMPTION: A-0022] supplies the numeric basis, and is split from the AWAY-to-HOME hysteresis criterion (SRS-OPER-0024) per the Single-Predicate Rule. \| Verification Method: Test \| Cross-References: SRS-OPER-0017, SRS-OPER-0024 | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0024"></a>

| **SRS-OPER-0024** | **Device-Local Away-to-Home RSSI Hysteresis Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from AWAY to HOME only when at least one paired base station RSSI reading exceeds −80 dBm for 3 consecutive readings taken at 1 s intervals. |
| **Rationale**    | [ASSUMPTION: A-0022] specifies a 5 dB hysteresis band between the AWAY-transition threshold (−85 dBm, SRS-OPER-0018) and this AWAY-to-HOME re-entry threshold (−80 dBm) to prevent rapid HOME/AWAY oscillation when RSSI hovers near the boundary, which would otherwise cause repeated toggling of the Max GNSS power gate (SRS-INT-0027) and unnecessary power draw. The shorter 3-reading debounce (vs. SRS-OPER-0018's 5-reading debounce) is an intentional asymmetry: re-establishing HOME status should be comparatively responsive once signal recovers, because remaining falsely in AWAY costs more GNSS-on power than a brief false-HOME determination. \| Verification Method: Test \| Cross-References: SRS-OPER-0017, SRS-OPER-0018<br><br>## 15.5 Collar Duty-Cycle & Power-Optimization Policy | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0019"></a>

| **SRS-OPER-0019** | **Wellness-Mode Deep-Sleep Idle State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, while in Wellness Mode and not actively processing a motion-triggered confirmation burst, **shall** remain in its deepest available low-power idle state. |
| **Rationale**    | PRD §15.2 specifies deepest-sleep idle as the standard Wellness-Mode duty-cycle baseline underlying the stated battery-life targets; this is the operational-policy statement that the idle-current ceiling itself (SRS-FUNC-0011, ≤4 µA) is verified against. \| Verification Method: Analysis \| Cross-References: SRS-FUNC-0011, SRS-FUNC-0010 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §15.2 |

<a id="srs-oper-0020"></a>

| **SRS-OPER-0020** | **GNSS Fix-Interval Change Application Timing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When the owner changes the Max collar variant's configured GNSS fix interval, the collar device **shall** apply the new interval no later than the start of the next scheduled fix-acquisition cycle. |
| **Rationale**    | PRD §15.5 states that a fix-interval change takes effect "within one cycle," bounding how long a stale interval setting may persist. This is the timing/application-policy requirement; the interval's configurable range (30 min–24 h) and default value (2 h) are owned by §10 (SRS-INT-0023, SRS-INT-0024) and not restated here. \| Verification Method: Test \| Cross-References: SRS-INT-0023, SRS-INT-0024 | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §15.5 |

<a id="srs-oper-0021"></a>

| **SRS-OPER-0021** | **Battery Cell Cycle-Life Validation Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Battery-life validation testing **shall** be performed using cells that have completed no fewer than 50 charge/discharge cycles prior to the validation measurement. |
| **Rationale**    | PRD §15.6 specifies a DVT programmable-load validation methodology requiring cells aged to ≥50 cycles before the battery-life pass criterion (≥80% of the §10.4 minimum capacity at 25°C) is evaluated, ensuring the stated battery-life targets (SRS-PERF-0001, SRS-PERF-0002) are validated against realistically aged cells rather than fresh-cell best-case performance. \| Verification Method: Test \| Cross-References: SRS-PERF-0001, SRS-PERF-0002<br><br>## 15.6 Cloud-Loss Fallback Governance | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §15.6 |

<a id="srs-oper-0022"></a>

| **SRS-OPER-0022** | **Device-Local Fallback Authority on Extended Cloud Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the base station has not had successful cloud contact for more than 24 hours, without requiring any additional fallback logic beyond the state machine's ordinary operation. |
| **Rationale**    | PRD §6.4 frames the device-local state machine's role as a ">24 h cloud loss" fallback governing the Max GNSS gate, implying the cloud-side state machine (external, [EXTERNAL: IoT Cloud backend team]) would otherwise have some role during shorter cloud outages. Per [ASSUMPTION: A-0016], however, the device-local state machine is the SOLE in-scope authority for power gating at all times, not only after 24 hours; this requirement makes explicit that no additional in-scope fallback mechanism activates at the 24-hour mark — the device-local state machine's continuous, unconditional operation (SRS-OPER-0017) already satisfies the PRD's fallback framing without requiring separate logic. \| Verification Method: Analysis \| Cross-References: SRS-OPER-0017, SRS-OPER-0011<br><br>## 15.7 Product Service Lifetime Reference | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0023"></a>

| **SRS-OPER-0023** | **Expected Product Service Lifetime Reference Figure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's operational and durability requirements that reference an expected service lifetime **shall** use 2 years as the minimum testable floor, consistent with the Product Context Profile's user-confirmed ~2–3 year expected service lifetime figure. |
| **Rationale**    | This requirement formalizes, as its own SRS-OPER block, the same PCP §8 user-confirmed lifetime figure that SRS-RELI-0001 (§13) already applies as its qualification duration; §13's Drafter Notes flagged that no A-ID currently carries this figure and recommended one be issued. Issuing it here as an explicit OPER requirement — rather than only as an inline PCP dependency note on SRS-RELI-0001 — gives the figure a citable SRS-ID that future sections (e.g., §16 Maintainability's OTA-support-lifetime requirements) can cross-reference directly instead of re-deriving it from the PCP each time. \| Verification Method: Inspection \| Cross-References: SRS-RELI-0001 | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: service_lifetime_duration_value |


## 16. Maintainability


## 16.0 Scope Note

This section specifies the *lifetime-maintenance* obligations implied by PRD §12.7 that are not already owned by another section. It does **not** re-issue constraints already owned elsewhere:

- **OTA mechanics** owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004)
- **SBOM per-release production** owned by §5 (SRS-FUNC-0061)
- **Pre-launch vuln-disclosure gate** owned by §8 (SRS-SEC-0006)
- **Tier-2 via OTA no HW mod** owned by §3 (SRS-FUNC-0034, SRS-FUNC-0035)
- **2-year lifetime floor** owned by §15 (SRS-OPER-0023)
- **Cloud-side maintenance** is [EXTERNAL: IoT Cloud backend team]; in-scope interface obligation remains SRS-DATA-0024 (§9)

## 16.1 OTA-Update Capability Lifetime

<a id="srs-maint-0001"></a>

| **SRS-MAINT-0001** | **OTA-Update Capability Availability Through Supported Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. |
| **Rationale**    | Derived from PRD §12.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.7 |

<a id="srs-maint-0002"></a>

| **SRS-MAINT-0002** | **SBOM Currency Maintenance Across Supported Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetime defined by SRS-MAINT-0001. |
| **Rationale**    | Derived from PRD §12.7. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.7 |

<a id="srs-maint-0003"></a>

| **SRS-MAINT-0003** | **Post-Launch Vulnerability-Disclosure Process Maintenance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported service lifetime defined by SRS-MAINT-0001. |
| **Rationale**    | Derived from PRD §12.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.7 |


## 17. Standards Conformance


## 17.0 Scope Note

This section binds the product design to the named technical standards whose test methods, clauses, or provisions underlie requirements already issued in §§5–16. §17 (COMP) answers "what standards does this design conform to"; §18 (REG) answers "what market certifications/approvals are needed."

## 17.1 Ingress Protection

<a id="srs-comp-0005"></a>

| **SRS-COMP-0005** | **IEC 60529 Ingress Protection Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, in its standalone (CCF-unmated) configuration, shall conform to the IEC 60529 IPX7 test methodology as the verification basis for the IP67 ingress-protection rating required by SRS-HW-0003. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007

## 17.2 Battery & Electrical Safety |

<a id="srs-comp-0006"></a>

| **SRS-COMP-0006** | **IEC 62133-2 Battery Cell Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). |
| **Rationale**    | Derived from PRD §13.3. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 |

<a id="srs-comp-0007"></a>

| **SRS-COMP-0007** | **UN 38.3 Battery Transport Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. |
| **Rationale**    | Derived from PRD §10.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-COMP-0006 |

<a id="srs-comp-0008"></a>

| **SRS-COMP-0008** | **UL 1642/UL 2054 US Cell Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable to cell construction, for placement on the US market. |
| **Rationale**    | Derived from PRD §13.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 · SRS-COMP-0006 |

<a id="srs-comp-0009"></a>

| **SRS-COMP-0009** | **EN 62368-1/UL 62368-1 Base Station Electrical Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station, in both Charging and Relay tiers, shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. |
| **Rationale**    | Derived from PRD §13.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 · —

## 17.3 IoT Cybersecurity Baseline |

<a id="srs-comp-0010"></a>

| **SRS-COMP-0010** | **ETSI EN 303 645 Consumer IoT Security Baseline Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. |
| **Rationale**    | Derived from PRD §12.3. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 · SRS-SEC-0001 through SRS-SEC-0006

## 17.4 Environmental Test-Method Series (IEC 60068-2) |

<a id="srs-comp-0011"></a>

| **SRS-COMP-0011** | **IEC 60068-2-14 Thermal-Cycling Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. |
| **Rationale**    | Derived from PRD §12.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.5 · SRS-ENV-0003 |

<a id="srs-comp-0012"></a>

| **SRS-COMP-0012** | **IEC 60068-2-78 Damp-Heat Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0004 |

<a id="srs-comp-0013"></a>

| **SRS-COMP-0013** | **IEC 60068-2-27 Mechanical Shock Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0010 |

<a id="srs-comp-0014"></a>

| **SRS-COMP-0014** | **IEC 60068-2-64 Vibration Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. |
| **Rationale**    | Derived from PRD §13.4. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0011 |

<a id="srs-comp-0015"></a>

| **SRS-COMP-0015** | **IEC 60068-2-5 UV-Aging Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. |
| **Rationale**    | Derived from PRD §12.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.5 · SRS-ENV-0013

## 17.5 Radio / EMC |

<a id="srs-comp-0016"></a>

| **SRS-COMP-0016** | **ETSI EN 300 328 2.4 GHz Radio Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-CONN-0001, SRS-CONN-0002, SRS-CONN-0007 |

<a id="srs-comp-0017"></a>

| **SRS-COMP-0017** | **Bluetooth SIG Qualification Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0016 |

<a id="srs-comp-0018"></a>

| **SRS-COMP-0018** | **FCC Part 15 Subpart C Intentional Radiator Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0016 |

<a id="srs-comp-0019"></a>

| **SRS-COMP-0019** | **FCC Part 15 Subpart B Unintentional Radiator Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0018 |

<a id="srs-comp-0020"></a>

| **SRS-COMP-0020** | **RED 2014/53/EU Essential Requirements Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 · SRS-COMP-0016, SRS-COMP-0010 |

<a id="srs-comp-0021"></a>

| **SRS-COMP-0021** | **RF Human-Exposure Standard Conformance (Contingent)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applicable. |
| **Rationale**    | Derived from PRD §13.1. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 · —

## 17.6 Materials Compliance |

<a id="srs-comp-0022"></a>

| **SRS-COMP-0022** | **REACH Regulation Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. |
| **Rationale**    | Derived from PRD §10.1.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0021 |

<a id="srs-comp-0023"></a>

| **SRS-COMP-0023** | **RoHS Directive Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0022 |

<a id="srs-comp-0024"></a>

| **SRS-COMP-0024** | **California Proposition 65 Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0022, SRS-COMP-0023 |

<a id="srs-comp-0025"></a>

| **SRS-COMP-0025** | **EU Battery Regulation Material and Labelling Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 |

<a id="srs-comp-0026"></a>

| **SRS-COMP-0026** | **WEEE Directive Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 |

<a id="srs-comp-0027"></a>

| **SRS-COMP-0027** | **EU PPWR / UK Producer Responsibility Packaging Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. |
| **Rationale**    | Derived from PRD §13.7. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0026

## 17.7 Software & Quality Management |

<a id="srs-comp-0028"></a>

| **SRS-COMP-0028** | **SBOM Machine-Readable Format Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The SBOM produced at each OTA release (SRS-FUNC-0061) and maintained across the supported service lifetime (SRS-MAINT-0002) shall be issued in a machine-readable format conforming to SPDX 2.3 or CycloneDX. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0061, SRS-MAINT-0002

## 17.8 Out-of-Scope Standards (Explicit Attribution)

- **IEC 62304** — OUT OF SCOPE. Product is general-wellness for animals, not a medical device. Responsible: Regulatory Affairs / Product Management.
- **ISO 14971** — OUT OF SCOPE. Same NOT-a-medical-device basis. General safety governed by EU GPSR 2023/988.
- **ISO 13485 / ISO 9001** — OUT OF SCOPE. No PRD or Regulatory Map mandate; QMS is an organizational attribute. Responsible: Operations / Manufacturing team.
- **IPC PCB Design Standards** — OUT OF SCOPE. No PRD source; PCB implementation is a design-choice in Altium Designer 24.
- **RTOS-Specific Software Standard** — OUT OF SCOPE. No PRD source; RTOS selection (Zephyr-preferred) is a firmware-team implementation choice.
- **EU Battery Regulation Art 11 (Removability)** — CONTINGENT. Potential conflict with non-swappable design; [ASSUMPTION: A-0013] tracks INDICATIVE exemption. Responsible: Regulatory Affairs, via EU counsel.
- **GNSS Intentional-Radiator Exemption** — CONTINGENT. RM-0009 UNCERTAIN, escalated to user.
- **ASTM F2727** — EXCLUDED AS MISCITATION. Corrected to ASTM F2056 per RM-0030. |


## 18. Regulatory

# §18 — Regulatory Certification & Market Pathways

****Pipeline:** Feasibility PASS (46/46) · V-Method PASS (46/46) · Intra-Conflict COMPLETE (/0029) · RTM ADD-ROW COMPLETE (323→369)

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

<a id="srs-reg-0001"></a>

| **SRS-REG-0001** | **FCC Part 15 Subpart C Certification Hold (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Body (TCB) prior to commercial distribution in the US market. \| |
| **Rationale**    | FCC 47 CFR Part 15 Subpart C §15.247 mandates third-party TCB certification (not self-declaration) for intentional radiators in the 2.4 GHz band; this is the market-access instrument corresponding to the technical conformance already required by SRS-COMP-0018. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0018 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0001 |

<a id="srs-reg-0002"></a>

| **SRS-REG-0002** | **FCC Part 15 Subpart B Supplier's Declaration of Conformity (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions prior to commercial distribution. \| |
| **Rationale**    | FCC 47 CFR Part 15 Subpart B §15.107/§15.109 permits self-declaration rather than TCB certification for unintentional-emitter compliance. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0019 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0002 |

<a id="srs-reg-0003"></a>

| **SRS-REG-0003** | **FCC Identifier Marking (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the US market. \| |
| **Rationale**    | FCC ID marking is a mandatory labeling condition attached to the Part 15 Subpart C certification. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0001 |

<a id="srs-reg-0004"></a>

| **SRS-REG-0004** | **NRTL Listing Hold for Base Station Electrical Safety (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. \| |
| **Rationale**    | US retail market access for mains-powered electronic equipment requires NRTL listing. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0009 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0013 |

<a id="srs-reg-0005"></a>

| **SRS-REG-0005** | **California Proposition 65 Conditional Warning Labeling (US-CA)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is present above the applicable safe-harbor threshold, prior to commercial distribution in the US-CA market. \| |
| **Rationale**    | Proposition 65 imposes a conditional warning-labeling obligation that is procedurally distinct from the underlying materials-conformance requirement. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0024 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0026 |

<a id="srs-reg-0006"></a>

| **SRS-REG-0006** | **Certification Documentation Package Availability (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support FCC TCB certification (SRS-REG-0001) and NRTL listing (SRS-REG-0004) prior to submission for either certification. \| |
| **Rationale**    | Captures the delivering engineering team's own in-scope interface obligation toward the externally-executed certification processes, ensuring external TCB/NRTL bodies are not blocked by missing inputs. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001, SRS-REG-0004 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: us_certification_documentation_owner |

<a id="srs-reg-0007"></a>

| **SRS-REG-0007** | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (US)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to commercial distribution in the US market. \| |
| **Rationale**    | RM-0009 is UNCERTAIN; this block requires only that the determination be made and documented, rather than asserting a specific exemption outcome. \| Verification Method: Analysis \| Cross-References: SRS-REG-0001 | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0009 |

<a id="srs-reg-0008"></a>

| **SRS-REG-0008** | **ISED Certification Hold (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen prior to commercial distribution in the Canada market. \| |
| **Rationale**    | ISED RSS-247 governs 2.4 GHz license-exempt radio equipment and RSS-Gen sets general certification procedure. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0018, SRS-COMP-0016 | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0009"></a>

| **SRS-REG-0009** | **ISED ICES-003 Compliance (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to commercial distribution. \| |
| **Rationale**    | ICES-003 is Canada's counterpart to the US FCC Part 15 Subpart B self-declaration regime. \| Verification Method: Inspection \| Cross-References: SRS-COMP-0019, SRS-REG-0002 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0010"></a>

| **SRS-REG-0010** | **Innovation Canada Identifier Marking (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the Canada market. \| |
| **Rationale**    | IC ID marking is a mandatory labeling condition attached to the ISED certification. \| Verification Method: Inspection \| Cross-References: SRS-REG-0008 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0006 |

<a id="srs-reg-0011"></a>

| **SRS-REG-0011** | **Certification Documentation Package Availability (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support ISED certification (SRS-REG-0008) prior to submission. \| |
| **Rationale**    | Mirrors SRS-REG-0006 for the Canada market. \| Verification Method: Inspection \| Cross-References: SRS-REG-0008 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: canada_certification_documentation_owner |

<a id="srs-reg-0012"></a>

| **SRS-REG-0012** | **GNSS Passive-Receiver Intentional-Radiator Exemption Determination (Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to commercial distribution in the Canada market. \| |
| **Rationale**    | Mirrors SRS-REG-0007; RM-0009's UNCERTAIN status is per-market and applies independently to Canada. \| Verification Method: Analysis \| Cross-References: SRS-REG-0008, SRS-REG-0007 | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | STD: RM-0009 |

<a id="srs-reg-0013"></a>

| **SRS-REG-0013** | **Pre-Launch Certification-Status Gate (US + Canada)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identified in SRS-REG-0001 through SRS-REG-0012 applicable to that market are complete and on file. \| |
| **Rationale**    | Umbrella gate preventing partial or premature market release. \| Verification Method: Inspection \| Cross-References: SRS-REG-0001–0012 | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.1 |

<a id="srs-reg-0014"></a>

| **SRS-REG-0014** | **RED 2014/53/EU Declaration of Conformity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | CE marking prerequisite for radio equipment. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0020, SRS-COMP-0016 |

<a id="srs-reg-0015"></a>

| **SRS-REG-0015** | **EU Notified Body Engagement Applicability Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Conditional on harmonised standard OJ listing. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0014 |

<a id="srs-reg-0016"></a>

| **SRS-REG-0016** | **CE Marking Physical Application** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On device or packaging. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0014, SRS-REG-0017 |

<a id="srs-reg-0017"></a>

| **SRS-REG-0017** | **EU GPSR General Product Safety Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | GPSR 2023/988 Art 5/6. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · §7 SAFE blocks |

<a id="srs-reg-0018"></a>

| **SRS-REG-0018** | **EU Authorized Representative Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | GPSR Art 4 / RED Art 11. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 |

<a id="srs-reg-0019"></a>

| **SRS-REG-0019** | **EU Technical Documentation File Availability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-scope interface obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0014, SRS-REG-0017 |

<a id="srs-reg-0020"></a>

| **SRS-REG-0020** | **RoHS Self-Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | 2011/65/EU + 2015/863. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0023 |

<a id="srs-reg-0021"></a>

| **SRS-REG-0021** | **WEEE Producer Registration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Per-member-state. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0026 |

<a id="srs-reg-0022"></a>

| **SRS-REG-0022** | **REACH SVHC Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Annex XVII. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0022 |

<a id="srs-reg-0023"></a>

| **SRS-REG-0023** | **EU Battery Regulation Labelling and CE Marking** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2023/1542 Art 6. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0025 |

<a id="srs-reg-0024"></a>

| **SRS-REG-0024** | **EU Battery Regulation Article 11 Removability Exemption Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Deadline 18 Feb 2027. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-COMP-0025, A-0013 |

<a id="srs-reg-0025"></a>

| **SRS-REG-0025** | **EU Cyber Resilience Act Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2024/2847 Annex I + Art 13–14. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0010, SRS-SEC-0006, SRS-MAINT-0003 |

<a id="srs-reg-0026"></a>

| **SRS-REG-0026** | **GDPR Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | (EU) 2016/679 + Art 30. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · §9 DATA blocks |

<a id="srs-reg-0027"></a>

| **SRS-REG-0027** | **EU Packaging and Packaging Waste Regulation Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | PPWR. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0027 |

<a id="srs-reg-0028"></a>

| **SRS-REG-0028** | **UKCA Marking Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK SI 2017/1206. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0020 |

<a id="srs-reg-0029"></a>

| **SRS-REG-0029** | **UK Approved Body Engagement Applicability Determination** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Conditional. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0028, SRS-REG-0015 |

<a id="srs-reg-0030"></a>

| **SRS-REG-0030** | **UK Responsible Person Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK establishment requirement. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0028, SRS-REG-0018 |

<a id="srs-reg-0031"></a>

| **SRS-REG-0031** | **UK PSTI Act 2022 Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0010, SRS-REG-0025 |

<a id="srs-reg-0032"></a>

| **SRS-REG-0032** | **UK GDPR Compliance Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK GDPR + DPA 2018. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0026 |

<a id="srs-reg-0033"></a>

| **SRS-REG-0033** | **UK Materials and Environmental Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | UK REACH, UK RoHS, UK WEEE. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0022/0023/0026 |

<a id="srs-reg-0034"></a>

| **SRS-REG-0034** | **UK Producer Responsibility Packaging Compliance Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0027, SRS-REG-0027 |

<a id="srs-reg-0035"></a>

| **SRS-REG-0035** | **Pre-Launch Certification-Status Gate (EU + UK)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · REG-0013, REG-0014–0034, REG-0045, REG-0046 |

<a id="srs-reg-0045"></a>

| **SRS-REG-0045** | **GNSS Exemption Determination (EU)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0009 · SRS-REG-0014, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="srs-reg-0046"></a>

| **SRS-REG-0046** | **GNSS Exemption Determination (UK)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    |  |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | STD: RM-0009 · SRS-REG-0028, SRS-REG-0007, SRS-REG-0012, SRS-REG-0040 |

<a id="srs-reg-0036"></a>

| **SRS-REG-0036** | **RCM Marking Declaration (AU/NZ)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | AS/NZS 4268:2017. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-COMP-0016 |

<a id="srs-reg-0037"></a>

| **SRS-REG-0037** | **ACMA Supplier Code Registration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Precondition to RCM. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0036 |

<a id="srs-reg-0038"></a>

| **SRS-REG-0038** | **AU/NZ Responsible Supplier Designation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-market required. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0018, SRS-REG-0030 |

<a id="srs-reg-0039"></a>

| **SRS-REG-0039** | **AU/NZ Certification Documentation Package** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | In-scope interface obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-REG-0036/0037 |

<a id="srs-reg-0040"></a>

| **SRS-REG-0040** | **GNSS Exemption Determination (AU/NZ)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | RM-0009 UNCERTAIN. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-REG-0007/0012 |

<a id="srs-reg-0041"></a>

| **SRS-REG-0041** | **CCPA/CPRA Contingent Market-Access Declaration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Threshold-contingent. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §13 · SRS-DATA-0022 |

<a id="srs-reg-0042"></a>

| **SRS-REG-0042** | **Post-Certification Regulatory-Change Monitoring** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Lifetime obligation. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · SRS-MAINT-0002/0003 |

<a id="srs-reg-0043"></a>

| **SRS-REG-0043** | **Certification and DoC Archival Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Per-market minimum. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · A-0025 |

<a id="srs-reg-0044"></a>

| **SRS-REG-0044** | **Pre-Launch Certification-Status Gate (All Markets)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Consolidating gate. |
| **Rationale**    | Market access obligation for LUUCIPet Wellness Monitor. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13 · REG-0013, REG-0035, REG-0036–0043, REG-0045, REG-0046 |


---

## Appendix A. Requirements Traceability Matrix (RTM)

The RTM is maintained in two parts. Refer to the project repository for the complete machine-readable CSV versions. Below are summaries of both parts.

### Part A (§1–§4) — 89 rows

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
| SRS-FUNC-0
```

## Part B (§5–§18) — 280 rows

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
| SRS-PERF-0001 | Mini Variant Battery-Life Conformance | [PRD §12.1],[PRD §10.4],[CR-0002],[PRD §15.6] | §6 | APPROVED | — | CR-0002 | PASS/PASS/PASS/PAS
```

*Full RTM CSVs available in the project traceability/ directory: 369 rows total.*

---

## Appendix B. Regulatory Map

The Regulatory Map enumerates 31 regulatory instruments (RM-0001–RM-0031) across five target markets. The full map is maintained in the project repository.

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
| RM-0005 | UK Radio Equipment Regs 2017 (SI 2017/1206)                                               | —                     | UK                      | Mini/Max/Base | CONFIRMED  | UKCA.                                                                                                                                                                                               
```

---

## Appendix C. Assumption Register

The Assumption Register catalogues 25 assumptions (A-0001–A-0025) that underpin the requirements formalized in this SRS.

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
- **Debounce (RSSI Reading)** — A requirement that a stated number of consecutive RSSI readings rather than a single reading satisfy a threshold condition before a state transition is committed.

### G

- **GNSS** — Global Navigation Satellite System; a passive receiver providing position-fix data from satellite signals.

### H

- **HOME/AWAY State** — The device-local determination of whether the collar device is within BLE range of at least one paired household base station (HOME) or not (AWAY).
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
| **Total Requirements (anchored)** | 364 |
| **Traceability Rows** | 369 |
| **Standards Basis** | IEEE 830 / ISO/IEC/IEEE 29148 |
| **Conflicts Resolved** | 29 |
| **Cross-Section Resolutions** | 16 |
| **Assumptions** | 25 (A-0001–A-0025) |
| **Regulatory Instruments** | 31 (RM-0001–RM-0031) |
| **Product Lifetime** | 2–3 years (2-year testable floor) |
| **Target Volume** | ~5,000 units (first batch) |

---

*End of Document — SRS-LUUCIPET-001, Revision 1.0*

*Authoring: Systems Engineering Team · Conforms to IEEE 830 / ISO/IEC/IEEE 29148*
