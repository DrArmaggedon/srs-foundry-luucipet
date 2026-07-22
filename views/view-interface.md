# SRS-LUUCIPET — Derived View: Interface & Integration

> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:30:00Z
> **Audience:** Interface & Integration Stakeholders (Firmware, Hardware, Cloud DM, Systems Integration)
> ⚠️ For full context, always refer to the Master SRS.

---

## 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

## 1.2 Scope

**In scope:**  Mini & Max collar HW+FW; Base Station (Charging & Relay) HW+FW; the device-enforced BLE/base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S/M/L, collar-types -RC/-MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract.
**Out of scope (PRD §6.1, §14.1):**  GPS-M variant + cellular (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage/analytics backend; cloud-side home/away state machine; device-app ICD.

## 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

---

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
| **Rationale**    | The collar is the advertising/connectable endpoint of the collar-to-base-station link; role assignment is imposed by the system architecture. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0002"></a>

| **SRS-INT-0002** | **Base Station BLE Central Role** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall implement the BLE 5.x radio interface in the central role. |
| **Rationale**    | The base station scans for and initiates connections to collar devices; role assignment is imposed by the system architecture. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §11.2 · SRS-INT-0001 |

<a id="srs-int-0003"></a>

| **SRS-INT-0003** | **Minimum Concurrent Collar Sessions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall support at least 4 concurrent BLE connections to collar devices. |
| **Rationale**    | A multi-pet household requires the base station to hold multiple simultaneous collar links without dropping connections. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0004"></a>

| **SRS-INT-0004** | **Default BLE Advertising Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. |
| **Rationale**    | Establishes the out-of-box discoverability cadence balancing power consumption against connection latency. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0005"></a>

| **SRS-INT-0005** | **Configurable BLE Advertising Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. |
| **Rationale**    | Allows the advertising cadence to be tuned for household-specific power/latency trade-offs. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0006"></a>

| **SRS-INT-0006** | **Advertising Continuity During Active Connection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall continue BLE advertising while maintaining an active BLE connection. |
| **Rationale**    | Preserves discoverability for additional base stations in a multi-base household while a collar is already connected to one base station. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0007"></a>

| **SRS-INT-0007** | **BLE Address Randomization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall randomize its BLE device address. |
| **Rationale**    | Prevents long-term tracking of the wearable by third parties observing BLE advertisements. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.1 |

<a id="srs-int-0008"></a>

| **SRS-INT-0008** | **Minimum BLE Transmit Power** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall transmit BLE signals at a power level of at least +8 dBm. |
| **Rationale**    | A minimum TX power floor is necessary to meet the stated open-air range target. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-INT-0009, SRS-HW-0019 |

<a id="srs-int-0009"></a>

| **SRS-INT-0009** | **Minimum BLE Open-Air Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE link between the collar device and the base station shall maintain connectivity at an open-air separation distance of at least 9 meters. |
| **Rationale**    | Defines the minimum usable range for typical household room-to-room and yard-adjacent operation. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.3 · SRS-INT-0008 |

<a id="srs-int-0010"></a>

| **SRS-INT-0010** | **BLE Link-Layer Encryption Algorithm** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall encrypt all BLE data-bearing links using AES-128 CCM. |
| **Rationale**    | Mandated link-layer confidentiality/integrity mechanism for all collar-to-base-station traffic. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0011"></a>

| **SRS-INT-0011** | **BLE Pairing via LE Secure Connections** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall establish BLE pairing between the collar device and the base station using LE Secure Connections. |
| **Rationale**    | Provides the pairing-time key-exchange mechanism underpinning the mandated link-layer encryption. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-INT-0010 |

<a id="srs-int-0012"></a>

| **SRS-INT-0012** | **QR Out-of-Band Pairing Mechanism** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station. |
| **Rationale**    | Defines the device/base-station-side OOB pairing mechanism; the mobile app's presentation of the QR code to the user is out of scope for this SRS and is attributed to the (out-of-scope) Mobile App per the standing scope boundary. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 |

<a id="srs-int-0013"></a>

| **SRS-INT-0013** | **BLE Radio Regulatory Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US), [STD: RED 2014/53/EU] (EU), [STD: UK Radio Equipment Regulations 2017] (UK), [STD: ISED RSS-247] (CA), and [STD: AS/NZS 4268:2017] (AU/NZ). |
| **Rationale**    | Market access for an intentional 2.4 GHz radiator requires conformance to each target market's radio-equipment regulation. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0014"></a>

| **SRS-INT-0014** | **Bluetooth SIG Qualification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). |
| **Rationale**    | Bluetooth SIG membership terms mandate qualification of any BLE product before market release. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | STD: Bluetooth SIG Qualification (QDID) |

<a id="srs-int-0015"></a>

| **SRS-INT-0015** | **RF Human-Exposure Assessment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The BLE radio interface should undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4 GHz transmission. |
| **Rationale**    | A continuously worn 2.4 GHz transmitter plausibly triggers per-market RF-exposure assessment; applicability and thresholds are per-market INDICATIVE per the Regulatory Map and not yet CONFIRMED, hence a SHOULD rather than SHALL. |
| **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0016"></a>

| **SRS-INT-0016** | **Wi-Fi Radio Band and Standard** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n]. |
| **Rationale**    | Defines the base-to-cloud uplink radio band and PHY/MAC standard. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 |

<a id="srs-int-0017"></a>

| **SRS-INT-0017** | **Cloud Uplink Transport Encryption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. |
| **Rationale**    | Mandated transport-layer confidentiality/integrity mechanism for base-station-to-cloud traffic; the device/base-station side of this transport is in scope, cloud-side storage/analytics is out of scope [ASSUMPTION A-0015]. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.5 |

<a id="srs-int-0018"></a>

| **SRS-INT-0018** | **Default Access-Point Configuration Compatibility** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. |
| **Rationale**    | Avoids requiring the owner to perform non-default router configuration for base-station setup. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.6 |

<a id="srs-int-0019"></a>

| **SRS-INT-0019** | **Minimum Wi-Fi Uplink Signal Condition** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. |
| **Rationale**    | Resolves the PRD's unbounded "reliable Wi-Fi" assumption with an engineered numeric floor; below this bound the ≥30-day offline buffering behavior (Data Requirements, §9) is the defined degraded-mode fallback rather than a new interface requirement. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | ASSUMPTION A-0009 |

<a id="srs-int-0020"></a>

| **SRS-INT-0020** | **Wi-Fi Radio Regulatory Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US) and [STD: RED 2014/53/EU] (EU). |
| **Rationale**    | Market access for the base station's Wi-Fi radio requires conformance to each target market's radio-equipment regulation. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0021"></a>

| **SRS-INT-0021** | **GNSS Interface Presence on Max** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall implement a passive (receive-only) GNSS interface. |
| **Rationale**    | GNSS is a defining differentiator of the Max variant, providing location context unavailable on Mini. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0022"></a>

| **SRS-INT-0022** | **GNSS Interface Absence on Mini** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mini collar variant shall not implement a GNSS interface. |
| **Rationale**    | GNSS hardware is excluded from Mini to meet its ≤10 g weight budget and BLE-only positioning. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0023"></a>

| **SRS-INT-0023** | **Configurable GNSS Fix Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. |
| **Rationale**    | Allows the fix cadence to be tuned against the battery-life-vs-fix-interval trade-off documented in the PRD. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0024"></a>

| **SRS-INT-0024** | **Default GNSS Fix Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall apply a default GNSS fix interval of 2 hours. |
| **Rationale**    | Establishes the out-of-box fix cadence consistent with the stated ≥45-day @2h battery-life target. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.1 |

<a id="srs-int-0025"></a>

| **SRS-INT-0025** | **A-GPS Assistance Data Delivery** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. |
| **Rationale**    | A-GPS delivery over the existing BLE link is the defined mechanism for reducing GNSS fix acquisition time. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0026"></a>

| **SRS-INT-0026** | **A-GPS Assistance Data Validity Window** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. |
| **Rationale**    | Bounds how long stale assistance data may be relied upon before fix-acquisition performance degrades. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0027"></a>

| **SRS-INT-0027** | **GNSS Power Gating During HOME State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. |
| **Rationale**    | The GNSS smart power gate underpins the stated Max battery-longevity targets; gating authority rests solely with the device-local state machine per the confirmed in-scope/external boundary. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 · SRS-OPER-0004 |

<a id="srs-int-0028"></a>

| **SRS-INT-0028** | **GNSS Fix Acquisition Timeout** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. |
| **Rationale**    | Bounds the power expenditure of an unsuccessful fix attempt. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.2.2 |

<a id="srs-int-0029"></a>

| **SRS-INT-0029** | **Warm GNSS Time-to-First-Fix Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. |
| **Rationale**    | Bounds the latency between a scheduled fix attempt and an available location result. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-INT-0025 |

<a id="srs-int-0030"></a>

| **SRS-INT-0030** | **GNSS Intentional-Radiator Exemption Status** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. |
| **Rationale**    | The PRD defers this exemption determination to Regulatory Lead confirmation per market; the Regulatory Map carries this as INDICATIVE, not CONFIRMED, hence a SHOULD rather than SHALL pending resolution. |
| **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Analysis |
| **Traceability** | PRD §13.1 |

<a id="srs-int-0031"></a>

| **SRS-INT-0031** | **Pogo-Pin Contact Count and Function** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) shall use a 2-contact pogo-pin arrangement carrying VBUS and GND. |
| **Rationale**    | Defines the minimal electrical contact interface for charging; cross-variant identical geometry is already established by SRS-COMP-0003. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.5 · SRS-COMP-0003 |

<a id="srs-int-0032"></a>

| **SRS-INT-0032** | **Magnetic Charging Alignment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. |
| **Rationale**    | Magnetic alignment enables reliable tool-free docking without precise manual contact placement. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.6 |

<a id="srs-int-0033"></a>

| **SRS-INT-0033** | **First-Attempt Docking Seating Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. |
| **Rationale**    | Bounds the usability of the magnetic docking mechanism to a measurable success rate. Note: this magnetic assist governs the charging-dock (collar device onto charging cradle) interface and is distinct from the device-to-CCF Twist-Lock engagement assist in SRS-INT-0049, though both specify an "up to 5 mm" approach distance. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.5 · SRS-INT-0049 |

<a id="srs-int-0034"></a>

| **SRS-INT-0034** | **Full-Charge Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall reach full charge within 2 hours when docked at the charging interface. |
| **Rationale**    | Bounds the time an owner must leave a device docked to restore full charge. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.5 |

<a id="srs-int-0035"></a>

| **SRS-INT-0035** | **IP67 Rating When Undocked** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. |
| **Rationale**    | The exposed pogo-pin contact is a potential ingress path and must not compromise the device-standalone IP67 rating. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.6 · SRS-HW-0004 |

<a id="srs-int-0036"></a>

| **SRS-INT-0036** | **Charging Socket Self-Drainage** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). |
| **Rationale**    | PRD §10.5/§10.1.3.5 state the socket "shall be self-draining" with no quantified acceptance criterion; the Verification-Method Validator flagged this as method/criterion incoherence — the declared Test method (correctly changed from Inspection) had nothing measurable to test against. [ASSUMPTION: A-0023] resolves this gap (engineered by analogy to A-0007). This requirement shares its underlying drainage claim with SRS-HW-0008 (§11, hardware-geometry framing of the same socket); both corrected together. |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §10.5 · SRS-HW-0008 |

<a id="srs-int-0037"></a>

| **SRS-INT-0037** | **Charging-Access Removal Rotation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. |
| **Rationale**    | Defines the workflow by which the charging contacts are exposed for docking, using the non-breakaway Twist-Lock mechanism. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §6.6 · SRS-INT-0039 |

<a id="srs-int-0038"></a>

| **SRS-INT-0038** | **Device-Absent Socket Entrapment Geometry** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature. |
| **Rationale**    | Resolves the PRD's unbounded "no independent entrapment hazard" statement with an engineered geometric probe criterion. |
| **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | ASSUMPTION A-0010 |

<a id="srs-int-0039"></a>

| **SRS-INT-0039** | **Bayonet Lug Configuration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock mechanical interface shall use a 3-lug bayonet arrangement spaced at 120 degrees. |
| **Rationale**    | Defines the base geometric arrangement of the device-to-CCF mechanical attachment; identical across Mini/Max per SRS-COMP-0003. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a · SRS-COMP-0003 |

<a id="srs-int-0040"></a>

| **SRS-INT-0040** | **Lock/Unlock Rotation Angle** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock mechanical interface shall engage and release via a 90-degree rotation. |
| **Rationale**    | Defines the actuation travel required to lock or unlock the device from the CCF. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0041"></a>

| **SRS-INT-0041** | **Lug Ramp Self-Locking Profile** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock lug ramp shall have a trapezoidal profile with an 8-degree self-locking angle. |
| **Rationale**    | The ramp angle is imposed to achieve self-locking behavior without requiring a separate latch. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0042"></a>

| **SRS-INT-0042** | **Twist-Lock Lug Dimensions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Each Twist-Lock lug shall be 4.0 mm wide by 1.2 mm thick. |
| **Rationale**    | Fixed lug dimensions are required for interoperability across all CCF SKUs and both collar variants. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0043"></a>

| **SRS-INT-0043** | **Asymmetric Keying Lug** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct engagement orientation. |
| **Rationale**    | Prevents incorrect-orientation assembly of the device onto the CCF. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0044"></a>

| **SRS-INT-0044** | **Detent Release Torque Window** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock detent shall release within a torque window of 0.08 to 0.10 N·m. |
| **Rationale**    | Bounds the rotational effort at which the detent yields, balancing inadvertent-release resistance against ease of intentional removal; upper bound narrowed from 0.15 N·m to 0.10 N·m to align with SRS-INT-0047's engage/release torque ceiling, per PRD §10.1.3.2a's intent that detent release remain at or below the engage torque ceiling. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-INT-0047 |

<a id="srs-int-0045"></a>

| **SRS-INT-0045** | **Twist-Lock Axial Retention Floor** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. |
| **Rationale**    | The Twist-Lock is explicitly not a breakaway mechanism; it must retain the device under normal and inertial loading (distinct from the Zone 2 Fuse Tab, which is governed under Safety Requirements). |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.1 |

<a id="srs-int-0046"></a>

| **SRS-INT-0046** | **Twist-Lock Engagement Insertion Force Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall require no more than 5 N of axial press-in force to engage. |
| **Rationale**    | Bounds the physical effort required of the owner during the engagement workflow. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 |

<a id="srs-int-0047"></a>

| **SRS-INT-0047** | **Twist-Lock Engagement Rotation Torque Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. |
| **Rationale**    | Bounds the rotational effort required of the owner during the engage/remove workflow. Priority raised MEDIUM→HIGH () so this governing torque ceiling is at least as critical as the dependent detent-release window (SRS-INT-0044, HIGH) that is bounded by it. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.1 · SRS-INT-0044 |

<a id="srs-int-0048"></a>

| **SRS-INT-0048** | **Engagement Feedback** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. |
| **Rationale**    | Confirms to the owner that the device has reached the fully locked position without requiring visual inspection. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0049"></a>

| **SRS-INT-0049** | **Magnetic Engagement Assist Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall provide magnetic engagement assistance effective at an approach distance of up to 5 mm. |
| **Rationale**    | Assists initial alignment of the device onto the CCF socket before rotation. Note: this Twist-Lock (device-to-CCF) magnetic engagement assist is distinct from the charging-dock magnetic alignment in SRS-INT-0033, though both specify an "up to 5 mm" approach distance. |
| **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.1.3.2a · SRS-INT-0033 |

<a id="srs-int-0050"></a>

| **SRS-INT-0050** | **Tool-Free Twist-Lock Operation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall be operable without tools. |
| **Rationale**    | Owners must be able to engage and remove the device without specialized equipment. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §10.1.3.2a |

<a id="srs-int-0051"></a>

| **SRS-INT-0051** | **Twist-Lock Engagement Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Twist-Lock interface shall be engageable within 5 seconds. |
| **Rationale**    | Bounds the time required to complete the mechanical engagement step of the CCF-install workflow. |
| **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 |

<a id="srs-int-0052"></a>

| **SRS-INT-0052** | **Common Device-Enforced Protocol Across Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall use a common device-enforced BLE application protocol shared across all collar and base-station firmware variants. |
| **Rationale**    | A single shared protocol avoids per-variant protocol fragmentation and depends on the protocol/ICD being frozen before verification per A-0001. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.3 · SRS-COMP-0001 |

<a id="srs-int-0053"></a>

| **SRS-INT-0053** | **Payload Type — Behavioral Classification Record** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. |
| **Rationale**    | Behavioral records are the primary data product synced from collar to base station and require an identifiable payload type. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 |

<a id="srs-int-0054"></a>

| **SRS-INT-0054** | **Payload Type — BLE Sighting Report** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (RSSI), timestamp, and base station identifier, as a distinct payload type. |
| **Rationale**    | Sighting reports are the data basis for home/away geo-fence determination and are reported independent of behavioral-data sync. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 |

<a id="srs-int-0055"></a>

| **SRS-INT-0055** | **Payload Type — Cloud Downlink** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type. |
| **Rationale**    | Downlink configuration and OTA image delivery are distinct data flows from the collar-to-base uplink and require their own payload type. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.6 |

<a id="srs-int-0056"></a>

| **SRS-INT-0056** | **Base Station Payload Content Opacity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. |
| **Rationale**    | Keeps behavioral-data interpretation logic on the collar/cloud endpoints only, avoiding base-station firmware dependency on payload semantics; verification method corrected from Test to Inspection because this is a negative architectural claim (absence of interpretation logic) that black-box behavioral testing cannot conclusively prove — a base station could interpret payload content internally and still relay it correctly, defeating a Test-based check. Design/firmware/code review confirming no semantic-parsing logic exists on the relay path is the appropriate method. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.3 |

<a id="srs-int-0057"></a>

| **SRS-INT-0057** | **Collar Buffer Retention Pending Acknowledgment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the base station. |
| **Rationale**    | Prevents data loss from premature buffer clearing before successful delivery is confirmed. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 |

<a id="srs-int-0058"></a>

| **SRS-INT-0058** | **No FIFO Clear on Disconnect Alone** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. |
| **Rationale**    | A disconnection is not itself confirmation of delivery; clearing on disconnect alone would risk silent data loss. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.4 · SRS-INT-0057 |

<a id="srs-int-0059"></a>

| **SRS-INT-0059** | **Sequence-Loss Detection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. |
| **Rationale**    | Enables the receiving side to detect gaps in the forwarded record stream without depending on a specific transport-level guarantee. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |

<a id="srs-int-0060"></a>

| **SRS-INT-0060** | **Corruption-Free Record Forwarding** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. |
| **Rationale**    | Ensures the integrity of behavioral data is preserved end-to-end across the BLE hop. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 |



---

## Coverage Notes

- **Section included:** §10 Interface Requirements (in full)
- **Requirement blocks:** SRS-INT-0001 through SRS-INT-0060 (60 interface requirements)
- **Subsections covered:** 10.0 Scope Note, BLE Radio Interfaces, Wi-Fi Uplink Interfaces, GNSS Interface, Charging Interface, Twist-Lock Mechanical Interface, Device-Enforced Protocol
- **No coverage gaps** — §10 is included in its entirety as it is inherently a cross-team integration artifact.
- **Cross-reference warning:** Several INT blocks cross-reference HW (§11), SAFE (§7), PERF (§6), and CONN (§4) blocks. Consult the Master SRS for those sections.
