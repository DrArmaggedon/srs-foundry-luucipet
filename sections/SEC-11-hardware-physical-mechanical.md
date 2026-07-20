> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# §11 — Hardware / Physical & Mechanical Requirements

CAT: **COMP-HW** | Maps to: PRD §10 (§10.1.1 weight/form, §10.1.2 enclosure/materials, §10.1.3 CCF material composition, §10.2 sensing, §10.3 wireless HW, §10.4 battery, §10.5 charging, §10.6 NV storage, §10.7 compute)
*(Drafter-authored; §11 v1 — 28 blocks, SRS-HW-0001–0028.)*

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

**SRS-HW-0001** | Mini Variant Maximum Device Mass | The Mini collar device **shall** have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.1], [PRD §4.1] | Rationale: The ≤10 g budget is the core differentiator for the cat/small-dog cohort and drives every downstream component-mass allocation. | VM: Test | XR: SRS-HW-0011, SRS-HW-0016

**SRS-HW-0002** | Max Variant Maximum Device Mass | The Max collar device **shall** have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.1], [PRD §4.1] | Rationale: The ≤22 g budget bounds the large/service-dog variant including the GNSS receiver and larger cell. | VM: Test | XR: SRS-HW-0012, SRS-HW-0017

## 11.2 Enclosure & Ingress Protection

**SRS-HW-0003** | Device-Standalone IP67 Ingress Rating | The collar device **shall** achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.2], [PRD §13.4], [STD: IEC 60529 (RM-0028)] | Rationale: Device-standalone IP67 is the governing waterproofing claim; the CCF-mated and charging-interface-specific cases are bounded separately. | VM: Test | XR: SRS-INT-0035, SRS-HW-0004

**SRS-HW-0004** | Exposed Pogo-Pin Ingress Integrity | The collar device enclosure **shall** maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.2], [PRD §10.5] | Rationale: The pogo-pin aperture is the primary ingress-path risk on an otherwise sealed enclosure. | VM: Test | XR: SRS-HW-0003, SRS-INT-0035

**SRS-HW-0005** | Device Status LED Indicator | The collar device **shall** provide a light-emitting-diode status indicator. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §10.1.2] | Rationale: A device-level visual indicator is required for power/charge/pairing status signalling. | VM: Inspection | XR: —

## 11.3 Mechanical / Structural Constraints

**SRS-HW-0006** | Minimum Wall Thickness at Lug Base | The collar device enclosure **shall** provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.1.2] | Rationale: Minimum wall thickness at the highest-stress structural feature preserves enclosure integrity and the seal boundary. | VM: Inspection | XR: SRS-HW-0007, SRS-HW-0003

**SRS-HW-0007** | Lug-Channel Solid-Section Seal Integrity | The Twist-Lock lug channels and magnetic insert on the device underside **shall not** penetrate the enclosure wall or the ingress seal path. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.2] | Rationale: The lug/magnet features must remain solid-section so that mechanical attachment cannot compromise IP67. | VM: Inspection | XR: SRS-HW-0003, SRS-HW-0006

**SRS-HW-0008** | Charging Socket Self-Drainage Criterion | The device-facing charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [PRD §10.5], [PRD §10.1.3.5], [ASSUMPTION: A-0023] | Rationale: PRD §10.5/§10.1.3.5 state "shall be self-draining" with no quantified criterion. Prior VM=Test (corrected from Inspection per CR-0017) was directionally correct but V-Method Validator FLAGged for lacking a measurable criterion. [ASSUMPTION: A-0023] resolves this gap with 5 mL fill / 15 s window / ≤0.2 mL residual in realistic worn orientation. Identical fix applied to SRS-INT-0036 (§10). | VM: Test | XR: SRS-INT-0036

## 11.4 CCF Material Composition

**SRS-HW-0009** | CCF Base Polymer Material | The CCF body **shall** be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [PRD §10.1.2], [PRD §6.2] | Rationale: PA66-GF30 provides the stiffness-to-mass ratio and moulded-fuse-tab characteristics the compound-CCF architecture depends on. | VM: Inspection | XR: SRS-HW-0010, SRS-SAFE-0006

**SRS-HW-0010** | CCF UV and Hydrolysis Stabilisation | The CCF material **shall** incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [PRD §10.1.2] | Rationale: The CCF is worn outdoors for the product lifetime; UV and hydrolysis stabilisation are required to retain breakaway-force properties. | VM: Inspection | XR: SRS-HW-0009

**SRS-HW-0011** | No Metallic Sub-Components in Breakaway Zones | The CCF **shall not** contain any metallic sub-component within the Zone 2 snap/breakaway region. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.2], [PRD §10.1.3.2b] | Rationale: Metallic inserts in the breakaway zone would defeat the calibrated polymer fuse-tab fracture behavior and introduce a sharp-fragment hazard. | VM: Inspection | XR: SRS-SAFE-0006, SRS-SAFE-0007

**SRS-HW-0012** | No Chrome or Nickel Plating on Animal-Contact Surfaces | Animal-contact surfaces of the device and CCF **shall not** use chrome or nickel plating. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.1.2], [PRD §13.2], [STD: REACH/RoHS/Prop 65 (RM-0026)] | Rationale: Chrome/nickel are common animal-contact allergens; exclusion is required for the pet-contact material safety case (mechanism detailed in §17). | VM: Inspection | XR: SRS-SAFE-0021

## 11.5 Sensing Hardware

**SRS-HW-0013** | Three-Axis MEMS Accelerometer Presence | The collar device **shall** incorporate a three-axis MEMS accelerometer. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.2.1] | Rationale: The accelerometer is the sole primary sensor for the behavioral-classification engine. | VM: Inspection | XR: SRS-FUNC-0014, SRS-FUNC-0015

**SRS-HW-0014** | Accelerometer Output-Data-Rate Capability | The collar device accelerometer **shall** support an output data rate of no less than 50 Hz. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.2.1] | Rationale: The classification engine requires ≥50 Hz sampling (SRS-FUNC-0014); the hardware must be capable of sustaining it. | VM: Test | XR: SRS-FUNC-0014, SRS-FUNC-0008

**SRS-HW-0015** | Accelerometer Wake-on-Motion and FIFO | The collar device accelerometer **shall** provide a wake-on-motion interrupt and a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.2.1] | Rationale: Wake-on-motion, a ≥512-byte FIFO, and DMA offload are required to sustain continuous sampling within the collar power budget. | VM: Inspection | XR: SRS-HW-0026, SRS-PERF-0001

**SRS-HW-0016** | GNSS Receiver Absence on Mini | The Mini collar device **shall not** incorporate a GNSS receiver. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §10.2.2], [PRD §4.1] | Rationale: GNSS hardware is excluded from Mini to meet the ≤10 g mass budget and BLE-only positioning. | VM: Inspection | XR: SRS-HW-0001, SRS-INT-0022

**SRS-HW-0017** | GNSS Receiver Presence on Max | The Max collar device **shall** incorporate a passive receive-only GNSS receiver. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.2.2], [PRD §4.1] | Rationale: The Max GNSS receiver is the physical component underlying the location-interface behavior specified in §10. | VM: Inspection | XR: SRS-INT-0021, SRS-HW-0002

## 11.6 Wireless Hardware

**SRS-HW-0018** | BLE 5.x Radio Presence | The collar device **shall** incorporate a Bluetooth Low Energy 5.x radio. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.3], [PRD §6.3] | Rationale: The BLE radio is the sole collar-to-base-station communication component; its protocol behavior is specified in §10. | VM: Inspection | XR: SRS-INT-0001, SRS-CONN-0006

**SRS-HW-0019** | BLE Radio Transmit-Power Capability | The collar device BLE radio **shall** be capable of a transmit power of no less than +8 dBm. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §10.3] | Rationale: The radio hardware must be capable of the +8 dBm floor that the range requirement (SRS-CONN-0006/SRS-INT) depends on. | VM: Test | XR: SRS-CONN-0007, SRS-INT-0008

## 11.7 Battery Hardware

**SRS-HW-0020** | Mini Minimum Cell Capacity | The Mini collar device **shall** incorporate a battery cell of no less than 120 mAh nominal capacity. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.4], [ASSUMPTION: A-0006] | Rationale: The §10.4 minimum (not the illustrative §15.3 130 mAh figure) is the governing cell-capacity floor per CR-0002/A-0006. | VM: Inspection | XR: SRS-PERF-0001

**SRS-HW-0021** | Max Minimum Cell Capacity | The Max collar device **shall** incorporate a battery cell of no less than 400 mAh nominal capacity. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.4], [ASSUMPTION: A-0006] | Rationale: The §10.4 minimum is the governing cell-capacity floor per CR-0002/A-0006; the §15.3 450 mAh figure is illustrative only. | VM: Inspection | XR: SRS-PERF-0002

**SRS-HW-0022** | Battery Protection Functions | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.4], [STD: IEC 62133-2:2017+AMD1:2021 (RM-0011)] | Rationale: Li-Po cell protection is a mandatory safety function for an animal-worn sealed device. | VM: Test | XR: SRS-SAFE-0022

**SRS-HW-0023** | Battery Transport-Safety Qualification | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.4], [STD: UN 38.3 (RM-0010)] | Rationale: UN 38.3 is mandatory for lithium-cell transport; the "before pilot" gate is a program milestone. | VM: Test | XR: SRS-HW-0022

**SRS-HW-0024** | Low-Battery Alert Threshold | The collar device **shall** raise a low-battery alert at a state-of-charge of 20% or below. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §10.4] | Rationale: A 20% SoC alert gives the owner adequate warning before the OTA reserve floor. | VM: Test | XR: SRS-FUNC-0051

## 11.8 Charging Hardware

**SRS-HW-0025** | Pogo-Pin Charging Contact Hardware | The collar device **shall** incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.5], [PRD §6.6] | Rationale: The pogo-pin + magnet is the physical charging component underlying the interface behavior in §10. | VM: Inspection | XR: SRS-INT-0031, SRS-INT-0032

## 11.9 Non-Volatile Storage Hardware

**SRS-HW-0026** | Non-Volatile Classification-Summary Storage Capacity | The collar device **shall** incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.6] | Rationale: The ≥30-day on-device retention floor requires a matching physical NV storage component. | VM: Test | XR: SRS-DATA-0005, SRS-DATA-0006

## 11.10 Compute Hardware

**SRS-HW-0027** | On-Device Inference Compute Capability | The collar device **shall** incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.7], [PRD §7.7] | Rationale: All Tier-1/Tier-2 classification runs on-device; the compute hardware must be capable of it independent of connectivity. | VM: Test | XR: SRS-FUNC-0031, SRS-DATA-0013

**SRS-HW-0028** | Compute Architecture With DMA and Hardware Root of Trust | The collar device compute subsystem **shall** provide direct-memory-access peripheral access and a hardware root of trust. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.7] | Rationale: DMA peripheral access supports low-power sensing offload (SRS-HW-0015); the hardware root of trust is the physical anchor for secure boot (SRS-SEC-0005). | VM: Inspection | XR: SRS-SEC-0005, SRS-HW-0015

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

- **CR-0017 / XSC-0008 (MODERATE) — APPLIED 2026-07-18:** SRS-HW-0008 (Charging Socket Self-Drainage Geometry) Verification Method changed **Inspection → Test** to align with SRS-INT-0036, whose VM was deliberately corrected Inspection→Test because self-drainage is a functional claim (water must actually clear the socket) rather than a static geometric feature. HW-0008 already XRs SRS-INT-0036. (Conductor authorized the VM alignment only for CR-0017; the optional INT-0036→HW-0008 back-XR was NOT part of this decision and is left for a future link-integrity pass if desired.)
- **§11 APPROVAL-REVOKED** by this change (HW-0008 VM edit re-opens §11). Requires SECTION_REVIEW_POST → FEASIBILITY_POST and V-Method re-verify of SRS-HW-0008 before §11 can be re-APPROVED. Signalled to Conductor.
