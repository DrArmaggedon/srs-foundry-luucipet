> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T21:00:00Z
⚠️ For full context, always refer to the Master SRS.

---


## 2. Overall Description (Product Variants)


## 2.1 Product Functions (Product Variants)


## 2.2 Product Variants & Configurations (Product Variants)

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


## 2.3 User Characteristics / Personas (Product Variants)


## 2.4 General Constraints (Product Variants)


## 2.5 Assumptions & Dependencies (Product Variants)


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
