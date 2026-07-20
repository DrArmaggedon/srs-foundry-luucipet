> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

## 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

## 1.2 Scope

**In scope:**  Mini & Max collar HW+FW; Base Station (Charging & Relay) HW+FW; the device-enforced BLE/base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S/M/L, collar-types -RC/-MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract.
**Out of scope (PRD §6.1, §14.1):**  GPS-M variant + cellular (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage/analytics backend; cloud-side home/away state machine; device-app ICD.

## 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

## 1.4 Wellness-Not-Medical Boundary

**SRS-REG-0001** | Prohibit medical-classification claims in labeling and marketing | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.6] | VM: Inspection | XR: SRS-REG-0002

**SRS-REG-0002** | Require regulatory classification review before releasing diagnostic-adjacent features | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.6] | VM: Analysis | XR: SRS-REG-0001

## 1.5 Definitions and References

Full term definitions are maintained in the Glossary appendix (derived from PRD §14.4). Standards/regulatory instruments are enumerated in the Regulatory Map and cited inline using the closed source-tag set only: `[PRD §x.x]`, `[STD: ID §clause]`, `[ASSUMPTION: A-NNNN]`, `[CONFLICT-RES: CR-NNNN]`, `[PRD — ABSENT: field]`.

---

**SRS-IDs issued:**  SRS-REG-0001, SRS-REG-0002.
