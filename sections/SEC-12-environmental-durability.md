> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# §12 — Environmental & Durability Requirements

CAT: **ENV** | Maps to: PRD §12.5 (Durability), §13.4 (Env/ingress) | Cross-refs: PRD §10.1.2 (materials), §10.1.3 (CCF architecture), §13.2 (pet-safety materials)
*(Drafter-authored; §12 v1 — 18 blocks, SRS-ENV-0001–0018.)*

## 12.0 Scope Note

This section specifies the environmental exposure conditions, survival criteria, and durability test regimes that the collar device and CCF accessory must withstand: temperature extremes, ingress-protection test parameters, mechanical shock/drop, UV/weathering, chemical exposure, and — for the CCF specifically — post-exposure retention of the safety-critical breakaway-force and detent-torque windows. It does **not** re-issue constraints already owned elsewhere:

- **IP67 device-standalone rating as a physical property**, exposed pogo-pin ingress integrity, and lug-channel solid-section structural integrity are owned by §11 Hardware (SRS-HW-0003/0004/0006/0007); §12 issues the ingress **test-parameter, claim-boundary, and functional-exclusion** requirements built on top of that rating.
- **CCF base-polymer material identity** (PA66-GF30), **UV/hydrolysis stabiliser content** (0.3–0.5%), and **no-metallic-subcomponent** constraints are owned by §11 (SRS-HW-0009/0010/0011); §12 issues the **exposure regime and post-exposure retention** criteria that exercise those material properties.
- **Zone 2 breakaway-force windows** (CCF-S/M/L) and **Twist-Lock detent-torque window** are owned by §7 Safety (SRS-SAFE-0001/0002/0003) and §10 Interfaces (SRS-INT-0044) respectively; §12 requires that these approved windows **remain valid after environmental exposure** — it does not restate the windows themselves.
- **Enclosure chew-resistance** and **animal-contact material non-toxicity** are owned by §7 Safety (SRS-SAFE-0018/0021); §12 references but does not re-issue.
- **REACH/RoHS/Prop 65 material-compliance mechanism** is owned by §17 Standards Compliance / §18 Regulatory; §12 references but does not re-issue.

## 12.1 Temperature

**SRS-ENV-0001** | Device Operating Temperature Range | The collar device **shall** operate within an ambient temperature range of −20 °C to +50 °C without loss of function. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5] | Rationale: Defines the outdoor/indoor thermal envelope the device must remain functional across for pet-wearable use, consistent with the deployment environment (outdoor pet exposure) described in the Product Context Profile. | VM: Test | XR: SRS-HW-0001, SRS-HW-0002

**SRS-ENV-0002** | Device Storage Temperature Range | The collar device **shall** withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequent operational performance. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.5] | Rationale: Bounds the non-operating thermal envelope for warehousing, shipping, and retail-shelf conditions, distinct from the in-use operating range. | VM: Test | XR: SRS-ENV-0001

**SRS-ENV-0003** | CCF Thermal-Cycling Exposure | The CCF **shall** be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of function. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.5], [ASSUMPTION: A-0003] | Rationale: PRD states the −20 to +50 °C temperature-cycling range without specifying a cycle count, dwell, or ramp profile; A-0003 supplies the IEC 60068-2-14 Test Na default absent a PRD-stated profile. | VM: Test | XR: SRS-ENV-0015, SRS-ENV-0016

[GLOSS: thermal cycling | repeated exposure of a test article to alternating high- and low-temperature extremes to reveal degradation caused by thermally induced material stress]

**SRS-ENV-0004** | Device Damp-Heat Exposure | The collar device **should** withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §13.4] | Rationale: PRD §13.4 identifies damp-heat testing as a recommended (non-mandatory) environmental qualification test supplementing the IP67 ingress rating. | VM: Test | XR: SRS-HW-0003

[GLOSS: damp heat | a combined high-temperature, high-humidity environmental test used to assess material and seal degradation under sustained humid conditions]

## 12.2 Ingress Protection

The IEC 60529 IPX7 test method inherently specifies a 1-metre / 30-minute temporary-immersion parameter; the "IP67 1 m/30 min" figure in PRD §12.5 is therefore the defined test parameter of the rating already required by SRS-HW-0003 (§11), not a separate numeric requirement, and is not re-issued here.

**SRS-ENV-0005** | Prohibition on IP67 Claims for CCF-Mated Configuration | Product documentation and marketing materials **shall not** state or imply an IP67, or equivalent, ingress-protection rating for the collar device while mated to any CCF. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §4.1 fn²], [PRD §13.4] | Rationale: The IP67 rating established in SRS-HW-0003 is qualified only for the device-standalone, unmated condition; this requirement prevents an unsubstantiated ingress claim from being communicated for the CCF-mated wear condition. | VM: Inspection | XR: SRS-HW-0003

**SRS-ENV-0006** | Independent Laboratory Confirmation of IP67 Rating | The IP67 ingress-protection rating claimed for the collar device **shall** be confirmed by an independent, accredited test laboratory and documented in a test report prior to product launch. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.4] | Rationale: PRD requires the device-standalone IP67 claim to be "documented and confirmed with lab," establishing an independent-verification gate distinct from the underlying physical capability owned by SRS-HW-0003. | VM: Inspection | XR: SRS-HW-0003

**SRS-ENV-0007** | Twist-Lock Channel Water-Ingress Exclusion | The Twist-Lock lug channels **shall** exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §13.4] | Rationale: PRD states the Twist-Lock channels present "no water path"; this requirement establishes the functional (test-level) counterpart to the structural solid-section requirement already owned by SRS-HW-0007. | VM: Test | XR: SRS-HW-0003, SRS-HW-0007

**SRS-ENV-0008** | Ingress Seal-Boundary Interior Placement | The ingress-protection seal boundary **shall** be located on the interior side of the enclosure assembly such that it is not directly exposed on any externally accessible mating surface. | Priority: HIGH | Stability: STABLE | Source: [PRD §13.4] | Rationale: PRD requires the seal boundary to be positioned "interior," protecting it from direct mechanical wear and contamination that would otherwise degrade the IP67 seal over the product's service life. | VM: Inspection | XR: SRS-HW-0006, SRS-HW-0007

## 12.3 Mechanical Durability

**SRS-ENV-0009** | Drop Survival | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5] | Rationale: Bounds the mechanical shock the device must survive from a typical accidental drop during handling, charging, or removal from an animal. | VM: Test | XR: —

**SRS-ENV-0010** | Mechanical Shock Resistance | The collar device **should** withstand mechanical shock per IEC 60068-2-27 without loss of function. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §13.4] | Rationale: PRD §13.4 identifies shock testing per IEC 60068-2-27 as a recommended supplementary qualification test beyond the explicit 1.5 m drop-survival floor. | VM: Test | XR: SRS-ENV-0009

**SRS-ENV-0011** | Vibration Resistance | The collar device **should** withstand vibration per IEC 60068-2-64 without loss of function. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §13.4] | Rationale: PRD §13.4 identifies vibration testing per IEC 60068-2-64 as a recommended supplementary qualification test, representative of sustained pet-motion vibration exposure. | VM: Test | XR: —

## 12.4 UV & Weathering

**SRS-ENV-0012** | Enclosure UV Stabilization | The collar device enclosure material **shall** be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service lifetime. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5], [PRD — ABSENT: enclosure UV-exposure test duration/method] | Rationale: PRD §12.5 requires the enclosure to be "UV-stabilized" but, unlike the CCF (SRS-ENV-0013, 2,000 h per IEC 60068-2-5), states no exposure duration or test method for the enclosure material; flagged per the numeric-vagueness gate rather than an invented duration. | VM: Analysis | XR: SRS-ENV-0013

**SRS-ENV-0013** | CCF UV Aging Exposure | The CCF **shall** withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5] | Rationale: Bounds the accelerated UV-aging qualification program for the outdoor-worn CCF, consistent with the UV-stabiliser content specified in SRS-HW-0010. | VM: Test | XR: SRS-HW-0010, SRS-ENV-0017

[GLOSS: UV aging | accelerated exposure of a material to ultraviolet radiation to evaluate long-term degradation from outdoor solar exposure within a compressed test duration]

## 12.5 Chemical Resistance

**SRS-ENV-0014** | CCF Chemical-Fluid Exposure | The CCF **shall** withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across pH 5.5 to 8.5, enzymatic pet-odor and stain cleaners, fresh water, and salt water. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.5] | Rationale: Bounds the household and outdoor chemical-exposure qualification program representative of routine pet bathing, cleaning, and water-body exposure. | VM: Test | XR: SRS-ENV-0018

## 12.6 CCF Environmental Durability — Post-Exposure Retention

This subsection ties the exposure regimes in §12.1/§12.4/§12.5 back to the Zone 2 breakaway-force windows (SRS-SAFE-0001/0002/0003) and Twist-Lock detent-torque window (SRS-INT-0044) that must remain valid after exposure: a CCF whose fuse tab has drifted out of its calibrated force window after environmental exposure would degrade the pet-safety breakaway function.

**SRS-ENV-0015** | Post-Thermal-Cycling Zone 2 Fuse-Force Window Retention | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5] | Rationale: PRD explicitly ties CCF temperature cycling to the requirement that "fuse force ... [stays] in-window," making post-cycling retention of the calibrated breakaway-force windows a directly PRD-stated durability criterion. | VM: Test | XR: SRS-ENV-0003, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003

**SRS-ENV-0016** | Post-Thermal-Cycling Twist-Lock Detent-Torque Window Retention | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Twist-Lock detent release torque **shall** remain within the torque window defined in SRS-INT-0044. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.5] | Rationale: PRD explicitly ties CCF temperature cycling to the requirement that "detent torque ... [stays] in-window," making post-cycling retention of the calibrated detent-torque window a directly PRD-stated durability criterion. | VM: Test | XR: SRS-ENV-0003, SRS-INT-0044

**SRS-ENV-0017** | Post-UV-Aging Zone 2 Fuse-Force Window Retention | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5], [PRD — ABSENT: post-UV-exposure fuse-force retention criterion] | Rationale: PRD states the CCF UV-aging duration and standard but, unlike the thermal-cycling case, does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the same safety-critical retention obligation established for thermal cycling (SRS-ENV-0015) to the UV-aging qualification test, since both exposures act on the same moulded Zone 2 fuse mechanism. Flagged as PRD-silent rather than an invented numeric bound — the force window itself is the pre-approved SRS-SAFE-0001/0002/0003 value. | VM: Test | XR: SRS-ENV-0013, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015

**SRS-ENV-0018** | Post-Chemical-Exposure Zone 2 Fuse-Force Window Retention | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.5], [PRD — ABSENT: post-chemical-exposure fuse-force retention criterion] | Rationale: As with SRS-ENV-0017, PRD states the CCF chemical-exposure duration and fluid set but does not explicitly restate a post-exposure force-window retention criterion; this requirement extends the SRS-ENV-0015 retention obligation to the chemical-resistance qualification test on the same safety-critical mechanism. Flagged as PRD-silent rather than an invented numeric bound. | VM: Test | XR: SRS-ENV-0014, SRS-SAFE-0001, SRS-SAFE-0002, SRS-SAFE-0003, SRS-ENV-0015

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
- **Format-vocabulary note for Conductor:** this section uses the established repo convention already in force across §§7/10/11 — `Priority: CRITICAL | HIGH | MEDIUM | LOW`, `Stability: STABLE | LIKELY-CHANGE | VOLATILE`, single-line `VM:`/`XR:` fields — rather than the `Essential | Conditional | Optional` / `Stable | Volatile` / `Verification:` vocabulary given in this task's dispatch instructions, to preserve terminology consistency across the assembled SRS. Flagged for reconciliation if a document-wide vocabulary change is intended.
- **Assumption dependency:** SRS-ENV-0003 relies on A-0003 (CCF thermal-cycling profile default, IEC 60068-2-14 Test Na).
