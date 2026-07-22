# SRS-LUUCIPET — Derived View: Safety

> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:30:00Z
> **Audience:** Safety Engineers, Regulatory Affairs, Hardware Engineering, Firmware Engineering
> ⚠️ For full context, always refer to the Master SRS.

---

## 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

## 1.2 Scope

**In scope:**  Mini & Max collar HW+FW; Base Station (Charging & Relay) HW+FW; the device-enforced BLE/base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S/M/L, collar-types -RC/-MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract.
**Out of scope (PRD §6.1, §14.1):**  GPS-M variant + cellular (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage/analytics backend; cloud-side home/away state machine; device-app ICD.

## 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

## 1.4 Wellness-Not-Medical Boundary

This section defines the regulatory boundary between wellness monitoring and medical diagnosis — a foundational safety concern for the product's market positioning.

| **SRS-REG-0001** | **Prohibit medical-classification claims in labeling and marketing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. |
| **Rationale**    | Derived from PRD §13.6. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.6 · SRS-REG-0002 |

| **SRS-REG-0002** | **Require regulatory classification review before releasing diagnostic-adjacent features** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. |
| **Rationale**    | Derived from PRD §13.6. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §13.6 · SRS-REG-0001 |

---

## 7. Safety

# §7 — Safety Requirements


## 7.1 Zone 2 Fuse Tab — Strangulation-Prevention Breakaway

<a id="srs-safe-0001"></a>

| **SRS-SAFE-0001** | **CCF-S Zone 2 Breakaway Force Window (Feline)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-S variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="srs-safe-0002"></a>

| **SRS-SAFE-0002** | **CCF-M Zone 2 Breakaway Force Window (Canine, Medium)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-M variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="srs-safe-0003"></a>

| **SRS-SAFE-0003** | **CCF-L Zone 2 Breakaway Force Window (Canine, Large)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab of the CCF-L variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device+CCF mass does not exceed 26 g. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0004, SRS-SAFE-0005, SRS-SAFE-0006, SRS-SAFE-0007, SRS-SAFE-0008 |

<a id="srs-safe-0004"></a>

| **SRS-SAFE-0004** | **CCF-L Force-Window Contingency for Assembled Mass Exceeding 26 g** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **shall** be revised upward to 30 N. |
| **Rationale**    | Derived from PRD §10.1.4. |
| **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.4 · SRS-SAFE-0003 |

<a id="srs-safe-0005"></a>

| **SRS-SAFE-0005** | **Zone 2 Single-Use Restriction** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab **shall not** be capable of being reused or restored to a load-bearing state after fracture. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0013 |

<a id="srs-safe-0006"></a>

| **SRS-SAFE-0006** | **Zone 2 No-Detached-Fragment on Fracture** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon fracture, the Zone 2 Fuse Tab **shall not** produce a detached fragment separate from the CCF body. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b |

<a id="srs-safe-0007"></a>

| **SRS-SAFE-0007** | **Zone 2 Post-Fracture Surface Bluntness** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **shall** be blunt, presenting no sharp edge. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b |

<a id="srs-safe-0008"></a>

| **SRS-SAFE-0008** | **Zone 2 Visible Fracture Indicator** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall** present a visible fracture indicator upon Zone 2 breakaway. |
| **Rationale**    | Derived from PRD §10.1.3.2b. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2b · SRS-SAFE-0013

## 7.2 Zone 1 — Structural Retention (Non-Breakaway) |

<a id="srs-safe-0009"></a>

| **SRS-SAFE-0009** | **Zone 1 Structural Retention Force** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 1 clamp **shall** retain axial loads of at least 50 N without structural failure. |
| **Rationale**    | Derived from PRD §10.1.3.1. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-safe-0010"></a>

| **SRS-SAFE-0010** | **Zone 1 Survival Through Zone 2 Fracture** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 1 clamp **shall** remain structurally intact following a Zone 2 fracture event. |
| **Rationale**    | Derived from PRD §10.1.3.1. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-SAFE-0009, SRS-SAFE-0013

## 7.3 Twist-Lock — Retention Safety (Non-Breakaway) |

<a id="srs-safe-0011"></a>

| **SRS-SAFE-0011** | **Twist-Lock Axial Retention Force** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock device-to-CCF interface **shall** retain axial loads exceeding 100 N without disengaging. |
| **Rationale**    | SAFE-0011 is the last mechanical line of defense preventing device separation from the wearer during a pet escape attempt. Failure of this retention means the device detaches entirely, losing all monitoring, safety tracking, and breakaway-event signaling. This aligns it with SRS-INT-0045 (§10) which already carries CRITICAL for the same >100 N requirement. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 · SRS-PERF-0008 |

<a id="srs-safe-0012"></a>

| **SRS-SAFE-0012** | **Twist-Lock Retention Under Pet-Motion Inertial Loading** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock **shall** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. |
| **Rationale**    | Derived from PRD §10.1.3.2a. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-SAFE-0011

## 7.4 Post-Breakaway Protocol & Re-Use Prevention |

<a id="srs-safe-0013"></a>

| **SRS-SAFE-0013** | **No-Wear-Without-Intact-Zone-2** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device **shall not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. |
| **Rationale**    | Derived from PRD §10.1.3.6. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.6 · SRS-SAFE-0005, SRS-SAFE-0008 |

<a id="srs-safe-0014"></a>

| **SRS-SAFE-0014** | **Device Separation-Signature Emission** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device **shall** emit a detectable separation signature upon Zone 2 breakaway. |
| **Rationale**    | Derived from PRD §10.1.3.6. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.6 · SRS-SAFE-0015 |

<a id="srs-safe-0016"></a>

| **SRS-SAFE-0016** | **Zone 2 Non-Fracture Under Chew-Compressive Load** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Zone 2 Fuse Tab **shall not** fracture under a compressive load below 250 N. |
| **Rationale**    | Derived from PRD §13.2. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.2 · SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-safe-0017"></a>

| **SRS-SAFE-0017** | **CCF Body Chew-Penetration Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF body **shall** resist penetration for at least 30 seconds under a 250 N compressive load. |
| **Rationale**    | Derived from PRD §13.2. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.2 |

<a id="srs-safe-0018"></a>

| **SRS-SAFE-0018** | **Device Enclosure Chew Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials in animal-skin contact on the device enclosure **shall** resist chew-induced damage. |
| **Rationale**    | Derived from PRD §10.1.2. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0016, SRS-SAFE-0017

## 7.6 Device-Absent Socket — Entrapment Prevention |

<a id="srs-safe-0019"></a>

| **SRS-SAFE-0019** | **Device-Absent Socket Entrapment-Hazard Avoidance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF socket **shall** present no independent entrapment hazard when the device is absent. |
| **Rationale**    | Derived from PRD §10.1.3.5. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §10.1.3.5 · SRS-SAFE-0020 |

<a id="srs-safe-0020"></a>

| **SRS-SAFE-0020** | **Device-Absent Socket Probe-Clearance Criterion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-absent CCF socket **shall** provide clearance verified against a 12 mm entrapment-probe criterion. |
| **Rationale**    | Derived from PRD §10.1.3.5. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.5 · SRS-SAFE-0019

## 7.7 Animal-Contact Material Safety |

<a id="srs-safe-0021"></a>

| **SRS-SAFE-0021** | **Animal-Contact Material Non-Toxicity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials in animal-skin contact **shall** be non-toxic. |
| **Rationale**    | Derived from PRD §10.1.2. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · — (see §17 for REACH/RoHS/Prop 65 mechanism)

## 7.8 Battery-Ingestion Warning |

<a id="srs-safe-0022"></a>

| **SRS-SAFE-0022** | **Battery-Ingestion Warning Labeling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide battery-ingestion warning labeling. |
| **Rationale**    | Derived from PRD §13.2. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.2 · —

--- |



---

## Safety-Relevant Blocks from Other Sections

The following blocks from elsewhere in the Master SRS are safety-relevant through direct cross-reference or content overlap with safety requirements. They are reproduced verbatim from their source sections for convenience; consult the Master SRS for full section context.

### From §11 Hardware — Battery Protection Functions

| **SRS-HW-0022** | **Battery Protection Functions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. |
| **Rationale**    | Li-Po cell protection is a mandatory safety function for an animal-worn sealed device. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-SAFE-0022 |

### From §11 Hardware — Battery Transport-Safety

| **SRS-HW-0023** | **Battery Transport-Safety Qualification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. |
| **Rationale**    | UN 38.3 is mandatory for lithium-cell transport; the "before pilot" gate is a program milestone. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-HW-0022 |

### From §11 Hardware — Animal-Contact Material Restrictions

| **SRS-HW-0012** | **No Chrome or Nickel Plating on Animal-Contact Surfaces** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Animal-contact surfaces of the device and CCF **shall not** use chrome or nickel plating. |
| **Rationale**    | Chrome/nickel are common animal-contact allergens; exclusion is required for the pet-contact material safety case (mechanism detailed in §17). |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0021 |

### From §11 Hardware — CCF Material Restrictions

| **SRS-HW-0011** | **No Metallic Sub-Components in Breakaway Zones** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF **shall not** contain any metallic sub-component within the Zone 2 snap/breakaway region. |
| **Rationale**    | Metallic inserts in the breakaway zone would defeat the calibrated polymer fuse-tab fracture behavior and introduce a sharp-fragment hazard. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0006, SRS-SAFE-0007 |

### From §17 Standards Conformance — Material Safety Standards

| **SRS-COMP-0022** | **REACH Regulation Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. |
| **Priority**     | Critical |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-SAFE-0021 |

| **SRS-COMP-0023** | **RoHS Directive Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. |
| **Priority**     | Critical |
| **Verification** | Inspection |
| **Traceability** | PRD §13.7 · SRS-COMP-0022 |

### From §17 Standards Conformance — Battery Safety Standards

| **SRS-COMP-0006** | **IEC 62133-2 Battery Cell Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). |
| **Priority**     | Critical |
| **Verification** | Inspection |
| **Traceability** | PRD §13.3 |

| **SRS-COMP-0007** | **UN 38.3 Battery Transport Safety Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. |
| **Priority**     | Critical |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-COMP-0006 |

---

## Coverage Notes

- **Primary section:** §7 Safety Requirements (SRS-SAFE-0001 through SRS-SAFE-0022) — in full
- **Pulled-in safety blocks:** SRS-REG-0001, SRS-REG-0002 (§1.4 — Wellness-Not-Medical Boundary), SRS-HW-0011, SRS-HW-0012, SRS-HW-0022, SRS-HW-0023 (§11 — safety-relevant hardware constraints), SRS-COMP-0006, SRS-COMP-0007, SRS-COMP-0022, SRS-COMP-0023 (§17 — material/battery safety standards)
- **Safety themes:** Strangulation prevention (Zone 2 Fuse Tab breakaway), structural retention (Zone 1, Twist-Lock), post-breakaway protocol, entrapment prevention, material non-toxicity/allergen exclusion, battery safety (protection, transport, ingestion warning), regulatory wellness-medical boundary
- **No SRS-SAFE-* block omitted** — all 22 SAFE blocks from §7 included.
