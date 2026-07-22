> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:38:48Z
> **Audience:** Hardware / Mechanical Engineering
> ⚠️ For full context, always refer to the Master SRS.

---

## 11. Hardware Physical Mechanical

## 11. Hardware Physical Mechanical

# §11 — Hardware / Physical & Mechanical Requirements

## 11.3 Mechanical / Structural Constraints |

## 11.3 Mechanical / Structural Constraints |

<a id="srs-hw-0006"></a>

| **SRS-HW-0006** | **Minimum Wall Thickness at Lug Base** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device enclosure **shall** provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. |
| **Rationale**    | Minimum wall thickness at the highest-stress structural feature preserves enclosure integrity and the seal boundary. \| VM: Inspection \| XR: SRS-HW-0007, SRS-HW-0003 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-HW-0007, SRS-HW-0003 |

<a id="srs-hw-0007"></a>

| **SRS-HW-0007** | **Lug-Channel Solid-Section Seal Integrity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock lug channels and magnetic insert on the device underside **shall not** penetrate the enclosure wall or the ingress seal path. |
| **Rationale**    | The lug/magnet features must remain solid-section so that mechanical attachment cannot compromise IP67. \| VM: Inspection \| XR: SRS-HW-0003, SRS-HW-0006 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.2 · SRS-HW-0003, SRS-HW-0006 |

<a id="srs-hw-0008"></a>

| **SRS-HW-0008** | **Charging Socket Self-Drainage Criterion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-facing charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state "shall be self-draining" with no quantified criterion. Prior VM=Test (corrected from Inspection per ) was directionally correct but V-Method Validator FLAGged for lacking a measurable criterion. [ASSUMPTION: A-0023] resolves this gap with 5 mL fill / 15 s window / ≤0.2 mL residual in realistic worn orientation. Identical fix applied to SRS-INT-0036 (§10). \| VM: Test \| XR: SRS-INT-0036<br><br>## 11.4 CCF Material Composition |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §10.5 · SRS-INT-0036

## 11.5 Sensing Hardware |

## 11.5 Sensing Hardware |

<a id="srs-hw-0013"></a>

| **SRS-HW-0013** | **Three-Axis MEMS Accelerometer Presence** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a three-axis MEMS accelerometer. |
| **Rationale**    | The accelerometer is the sole primary sensor for the behavioral-classification engine. \| VM: Inspection \| XR: SRS-FUNC-0014, SRS-FUNC-0015 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.1 · SRS-FUNC-0014, SRS-FUNC-0015 |

<a id="srs-hw-0014"></a>

| **SRS-HW-0014** | **Accelerometer Output-Data-Rate Capability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device accelerometer **shall** support an output data rate of no less than 50 Hz. |
| **Rationale**    | The classification engine requires ≥50 Hz sampling (SRS-FUNC-0014); the hardware must be capable of sustaining it. \| VM: Test \| XR: SRS-FUNC-0014, SRS-FUNC-0008 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.1 · SRS-FUNC-0014, SRS-FUNC-0008 |

<a id="srs-hw-0015"></a>

| **SRS-HW-0015** | **Accelerometer Wake-on-Motion and FIFO** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device accelerometer **shall** provide a wake-on-motion interrupt and a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. |
| **Rationale**    | Wake-on-motion, a ≥512-byte FIFO, and DMA offload are required to sustain continuous sampling within the collar power budget. \| VM: Inspection \| XR: SRS-HW-0026, SRS-PERF-0001 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.1 · SRS-HW-0026, SRS-PERF-0001 |

<a id="srs-hw-0016"></a>

| **SRS-HW-0016** | **GNSS Receiver Absence on Mini** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar device **shall not** incorporate a GNSS receiver. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet the ≤10 g mass budget and BLE-only positioning. \| VM: Inspection \| XR: SRS-HW-0001, SRS-INT-0022 |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.2 · SRS-HW-0001, SRS-INT-0022 |

<a id="srs-hw-0017"></a>

| **SRS-HW-0017** | **GNSS Receiver Presence on Max** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar device **shall** incorporate a passive receive-only GNSS receiver. |
| **Rationale**    | The Max GNSS receiver is the physical component underlying the location-interface behavior specified in §10. \| VM: Inspection \| XR: SRS-INT-0021, SRS-HW-0002<br><br>## 11.6 Wireless Hardware |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.2.2 · SRS-INT-0021, SRS-HW-0002

## 11.6 Wireless Hardware |

## 11.6 Wireless Hardware |

<a id="srs-hw-0018"></a>

| **SRS-HW-0018** | **BLE 5.x Radio Presence** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a Bluetooth Low Energy 5.x radio. |
| **Rationale**    | The BLE radio is the sole collar-to-base-station communication component; its protocol behavior is specified in §10. \| VM: Inspection \| XR: SRS-INT-0001, SRS-CONN-0006 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.3 · SRS-INT-0001, SRS-CONN-0006 |

<a id="srs-hw-0019"></a>

| **SRS-HW-0019** | **BLE Radio Transmit-Power Capability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device BLE radio **shall** be capable of a transmit power of no less than +8 dBm. |
| **Rationale**    | The radio hardware must be capable of the +8 dBm floor that the range requirement (SRS-CONN-0006/SRS-INT) depends on. \| VM: Test \| XR: SRS-CONN-0007, SRS-INT-0008<br><br>## 11.7 Battery Hardware |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-CONN-0007, SRS-INT-0008

## 11.7 Battery Hardware |

## 11.7 Battery Hardware |

<a id="srs-hw-0020"></a>

| **SRS-HW-0020** | **Mini Minimum Cell Capacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar device **shall** incorporate a battery cell of no less than 120 mAh nominal capacity. |
| **Rationale**    | The §10.4 minimum (not the illustrative §15.3 130 mAh figure) is the governing cell-capacity floor per /A-0006. \| VM: Inspection \| XR: SRS-PERF-0001 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-PERF-0001 |

<a id="srs-hw-0021"></a>

| **SRS-HW-0021** | **Max Minimum Cell Capacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar device **shall** incorporate a battery cell of no less than 400 mAh nominal capacity. |
| **Rationale**    | The §10.4 minimum is the governing cell-capacity floor per /A-0006; the §15.3 450 mAh figure is illustrative only. \| VM: Inspection \| XR: SRS-PERF-0002 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.4 · SRS-PERF-0002 |

<a id="srs-hw-0022"></a>

| **SRS-HW-0022** | **Battery Protection Functions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. |
| **Rationale**    | Li-Po cell protection is a mandatory safety function for an animal-worn sealed device. \| VM: Test \| XR: SRS-SAFE-0022 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-SAFE-0022 |

<a id="srs-hw-0023"></a>

| **SRS-HW-0023** | **Battery Transport-Safety Qualification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. |
| **Rationale**    | UN 38.3 is mandatory for lithium-cell transport; the "before pilot" gate is a program milestone. \| VM: Test \| XR: SRS-HW-0022 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-HW-0022 |

<a id="srs-hw-0024"></a>

| **SRS-HW-0024** | **Low-Battery Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** raise a low-battery alert at a state-of-charge of 20% or below. |
| **Rationale**    | A 20% SoC alert gives the owner adequate warning before the OTA reserve floor. \| VM: Test \| XR: SRS-FUNC-0051<br><br>## 11.8 Charging Hardware |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.4 · SRS-FUNC-0051

## 11.8 Charging Hardware |

## 11.8 Charging Hardware |

<a id="srs-hw-0025"></a>

| **SRS-HW-0025** | **Pogo-Pin Charging Contact Hardware** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. |
| **Rationale**    | The pogo-pin + magnet is the physical charging component underlying the interface behavior in §10. \| VM: Inspection \| XR: SRS-INT-0031, SRS-INT-0032<br><br>## 11.9 Non-Volatile Storage Hardware |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.5 · SRS-INT-0031, SRS-INT-0032

## 11.9 Non-Volatile Storage Hardware |

## 11.9 Non-Volatile Storage Hardware |

<a id="srs-hw-0026"></a>

| **SRS-HW-0026** | **Non-Volatile Classification-Summary Storage Capacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. |
| **Rationale**    | The ≥30-day on-device retention floor requires a matching physical NV storage component. \| VM: Test \| XR: SRS-DATA-0005, SRS-DATA-0006<br><br>## 11.10 Compute Hardware |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.6 · SRS-DATA-0005, SRS-DATA-0006

## 11.10 Compute Hardware |

## 11.10 Compute Hardware |

<a id="srs-hw-0027"></a>

| **SRS-HW-0027** | **On-Device Inference Compute Capability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. |
| **Rationale**    | All Tier-1/Tier-2 classification runs on-device; the compute hardware must be capable of it independent of connectivity. \| VM: Test \| XR: SRS-FUNC-0031, SRS-DATA-0013 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.7 · SRS-FUNC-0031, SRS-DATA-0013 |

<a id="srs-hw-0028"></a>

| **SRS-HW-0028** | **Compute Architecture With DMA and Hardware Root of Trust** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device compute subsystem **shall** provide direct-memory-access peripheral access and a hardware root of trust. |
| **Rationale**    | DMA peripheral access supports low-power sensing offload (SRS-HW-0015); the hardware root of trust is the physical anchor for secure boot (SRS-SEC-0005). \| VM: Inspection \| XR: SRS-SEC-0005, SRS-HW-0015<br><br>--- |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.7 · SRS-SEC-0005, SRS-HW-0015

--- |

## 12. Environmental Durability

## 12. Environmental Durability

# §12 — Environmental & Durability Requirements

## 12.3 Mechanical Durability |

## 12.3 Mechanical Durability |

<a id="srs-env-0009"></a>

| **SRS-ENV-0009** | **Drop Survival** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. |
| **Rationale**    | Bounds the mechanical shock the device must survive from a typical accidental drop during handling, charging, or removal from an animal. \| VM: Test \| XR: — |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 |

<a id="srs-env-0010"></a>

| **SRS-ENV-0010** | **Mechanical Shock Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **should** withstand mechanical shock per IEC 60068-2-27 without loss of function. |
| **Rationale**    | PRD §13.4 identifies shock testing per IEC 60068-2-27 as a recommended supplementary qualification test beyond the explicit 1.5 m drop-survival floor. \| VM: Test \| XR: SRS-ENV-0009 |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.4 · SRS-ENV-0009 |

<a id="srs-env-0011"></a>

| **SRS-ENV-0011** | **Vibration Resistance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **should** withstand vibration per IEC 60068-2-64 without loss of function. |
| **Rationale**    | PRD §13.4 identifies vibration testing per IEC 60068-2-64 as a recommended supplementary qualification test, representative of sustained pet-motion vibration exposure. \| VM: Test \| XR: —<br><br>## 12.4 UV & Weathering |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.4 · —

## 12.6 CCF Environmental Durability — Post-Exposure Retention

## 12.6 CCF Environmental Durability — Post-Exposure Retention

This subsection ties the exposure regimes in §12.1/§12.4/§12.5 back to the Zone 2 breakaway-force windows (SRS-SAFE-0001/0002/0003) and Twist-Lock detent-torque window (SRS-INT-0044) that must remain valid after exposure: a CCF whose fuse tab has drifted out of its calibrated force window after environmental exposure would degrade the pet-safety breakaway function. |

<a id="srs-env-0015"></a>

| **SRS-ENV-0015** | **Post-Thermal-Cycling Zone 2 Fuse-Force Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | PRD explicitly ties CCF temperature cycling to the requirement that "fuse force ... [stays] in-window," making post-cycling retention of the calibrated breakaway-force windows a directly PRD-stated durability criterion. \| VM: Test \| XR: SRS-ENV-0003, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0003, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003 |

<a id="srs-env-0016"></a>

| **SRS-ENV-0016** | **Post-Thermal-Cycling Twist-Lock Detent-Torque Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Twist-Lock detent release torque **shall** remain within the torque window defined in SRS-INT-0044. |
| **Rationale**    | PRD explicitly ties CCF temperature cycling to the requirement that "detent torque ... [stays] in-window," making post-cycling retention of the calibrated detent-torque window a directly PRD-stated durability criterion. \| VM: Test \| XR: SRS-ENV-0003, SRS-INT-0044 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0003, SRS-INT-0044 |

<a id="srs-env-0017"></a>

| **SRS-ENV-0017** | **Post-UV-Aging Zone 2 Fuse-Force Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | PRD states the CCF UV-aging duration and standard but, unlike the thermal-cycling case, does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the same safety-critical retention obligation established for thermal cycling (SRS-ENV-0015) to the UV-aging qualification test, since both exposures act on the same moulded Zone 2 fuse mechanism. Flagged as PRD-silent rather than an invented numeric bound — the force window itself is the pre-approved SRS-SAFE-0001/0002/0003 value. \| VM: Test \| XR: SRS-ENV-0013, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0013, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015 |

<a id="srs-env-0018"></a>

| **SRS-ENV-0018** | **Post-Chemical-Exposure Zone 2 Fuse-Force Window Retention** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. |
| **Rationale**    | As with SRS-ENV-0017, PRD states the CCF chemical-exposure duration and fluid set but does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the SRS-ENV-0015 retention obligation to the chemical-resistance qualification test on the same safety-critical mechanism. Flagged as PRD-silent rather than an invented numeric bound. \| VM: Test \| XR: SRS-ENV-0014, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015<br><br>## 12.7 Material Safety (Cross-Reference — No New Requirements Issued)<br><br>Enclosure chew-resistance (SRS-SAFE-0018) and animal-contact material non-toxicity (SRS-SAFE-0021) are owned by §7 Safety. CCF base-polymer identity, UV/hydrolysis stabiliser content, absence of metallic breakaway-zone subcomponents, and absence of chrome/nickel plating on animal-contact surfaces (SRS-HW-0009, SRS-HW-0010, SRS-HW-0011, SRS-HW-0012) are owned by §11 Hardware. REACH/RoHS/Prop 65 compliance mechanism (PRD §13.2) is owned by §17 Standards Compliance / §18 Regulatory. §12 does not re-issue any of the above; the exposure and retention requirements in §12.1–§12.6 are the environmental-durability complement to these material-safety and material-composition requirements.<br><br>--- |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.5 · SRS-ENV-0014, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015

## 13.1 Ingress-Protection Durability

## 13.1 Ingress-Protection Durability

<a id="srs-reli-0001"></a>

| **SRS-RELI-0001** | **IP67 Rating Retention Over Full Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. |
| **Rationale**    | PRD §12.2 states the qualitative criterion "IP67 full lifetime (device standalone)" but does not itself state a numeric service-lifetime duration against which "full lifetime" can be tested. The Product Context Profile records a user-confirmed expected service lifetime of ~2–3 years, with a 2-year floor to be used wherever a single testable figure is required; that floor is applied here as the qualification duration. This requirement is the temporal-endurance complement to the device-standalone IP67 rating already established by SRS-HW-0003 and does not restate the rating itself. \| Verification Method: Analysis \| Cross-References: SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006<br><br>## 13.2 Collar Device Availability |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0002"></a>

| **SRS-RELI-0002** | **Collar Device Operational Availability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. |
| **Rationale**    | PRD §12.2 states "collar operational ≥99% (excl. charging)" as a direct numeric floor, but — unlike the base station uptime criterion in the same clause, which specifies a 90-day measurement window — the PRD does not state the observation-window length over which collar availability is to be measured. Flagged per the numeric-vagueness gate rather than inventing a window; the 99% floor and the charging exclusion are PRD-stated and are issued as-is. Verification Method corrected from Analysis to Test per V-Method review: this is a directly observable field/DVT proportion metric (uptime vs. total non-charging elapsed time), matching the Test pattern this SRS already applies to equivalent rate/proportion criteria (SRS-FUNC-0018–0021, SRS-FUNC-0001); no MTBF-style modeling basis is stated that would justify Analysis. \| Verification Method: Test \| Cross-References: SRS-HW-0025, SRS-INT-0031, SRS-INT-0032<br><br>## 13.3 Base Station Availability |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0003"></a>

| **SRS-RELI-0003** | **Base Station Uptime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. |
| **Rationale**    | PRD §12.2 states "base ≥99.5% uptime over 90-day window" as a direct, fully-bounded numeric criterion; the base station's continuous, mains-powered, no-sleep operating profile (PRD §11.7) makes a rolling-window uptime metric directly measurable in the field. Verification Method corrected from Analysis to Test per V-Method review: the criterion is fully bounded (explicit 90-day window) and directly observable via continuous-operation monitoring against the threshold — a practical DVT/pilot burn-in test, not a modeling exercise. \| Verification Method: Test \| Cross-References: —<br><br>## 13.4 OTA Update Success Rate |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0004"></a>

| **SRS-RELI-0004** | **OTA Update Success Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a base station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. |
| **Rationale**    | PRD §12.2 states "OTA success ≥99%" as a direct numeric floor on the aggregate reliability of the OTA mechanism already specified functionally in §5; "success" is defined operationally against the existing auto-revert criterion (SRS-FUNC-0056) rather than inventing a separate definition. Verification Method corrected from Analysis to Test per V-Method review: this is a repeated-trial pass/fail statistic (run N install attempts, including fault-injected trials per SRS-FUNC-0057, and compute the pass proportion against the 99% floor), matching the Test pattern this SRS already applies to equivalent proportion-based criteria (SRS-FUNC-0001, SRS-FUNC-0018–0021). \| Verification Method: Test \| Cross-References: SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0057<br><br>--- |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

## 17.4 Environmental Test-Method Series (IEC 60068-2) |

## 17.4 Environmental Test-Method Series (IEC 60068-2) |

<a id="srs-comp-0011"></a>

| **SRS-COMP-0011** | **IEC 60068-2-14 Thermal-Cycling Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. |
| **Rationale**    | Derived from PRD §12.5. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.5 · SRS-ENV-0003 |

<a id="srs-comp-0012"></a>

| **SRS-COMP-0012** | **IEC 60068-2-78 Damp-Heat Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. |
| **Rationale**    | Derived from PRD §13.4. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0004 |

<a id="srs-comp-0013"></a>

| **SRS-COMP-0013** | **IEC 60068-2-27 Mechanical Shock Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. |
| **Rationale**    | Derived from PRD §13.4. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0010 |

<a id="srs-comp-0014"></a>

| **SRS-COMP-0014** | **IEC 60068-2-64 Vibration Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. |
| **Rationale**    | Derived from PRD §13.4. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §13.4 · SRS-ENV-0011 |

<a id="srs-comp-0015"></a>

| **SRS-COMP-0015** | **IEC 60068-2-5 UV-Aging Test Standard Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. |
| **Rationale**    | Derived from PRD §12.5. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.5 · SRS-ENV-0013

## Interface Requirements (HW-relevant excerpts)

## 10. Interface Requirements

**Version:** v6
**Session:** S-luucipet
**Status:** APPROVED — v6: SRS-INT-0036 reissued with quantified drainage criterion (5 mL/15 s/≤0.2 mL) per [ASSUMPTION: A-0023]; v5: cross-conflict resolutions applied per Conflict & Consistency Resolver — / (INT-0035 back-XR +SRS-HW-0004, link-only), / (INT-0008 back-XR +SRS-HW-0019, link-only), / (INT-0032 Priority HIGH→CRITICAL, aligns with HW-0025 CRITICAL framing of the pogo-pin+magnet assembly; priority field only, no text change). All three §10-side only — no approval revocation. v4: cross-section resolutions applied per Conflict & Consistency Resolver — / (INT-0027 cross-ref SRS-OPER-0005→SRS-OPER-0004 + footer relied-upon list corrected), / (INT-0008 Priority HIGH→MEDIUM, aligns with §4 SRS-CONN-0007), / (INT-0029 Priority HIGH→MEDIUM, aligns with §6 SRS-PERF-0005), / (INT-0051 Priority MEDIUM→LOW, aligns with §6 SRS-PERF-0008).  (INT-0045 vs §7 SRS-SAFE-0011) resolved §7-side (SAFE-0011 HIGH→CRITICAL by Requirements Drafter); INT-0045 remains CRITICAL, unchanged here (). v3:  (§10.4 terminology standardization),  (INT-0033↔INT-0049 reciprocal cross-refs + clarifiers),  (INT-0047 Priority MEDIUM→HIGH) applied per Conflict & Consistency Resolver. v2: torque contradiction (INT-0044/0047) and verification-method fixes (INT-0036, INT-0056) applied per Feasibility Checker & Verification-Method Validator flags

---

---

### View Coverage
Product Variants (§2.2), Hardware/Physical/Mechanical (§11), Environmental & Durability (§12), HW-relevant Performance (§6) & Interface (§10) excerpts.
