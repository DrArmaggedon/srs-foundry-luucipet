> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Version:** v6
**Session:** S-luucipet
**Status:** APPROVED — v6: SRS-INT-0036 reissued with quantified drainage criterion (5 mL/15 s/≤0.2 mL) per [ASSUMPTION: A-0023]; v5: cross-conflict resolutions applied per Conflict & Consistency Resolver — CR-0016/XSC-0007 (INT-0035 back-XR +SRS-HW-0004, link-only), CR-0018/XSC-0009 (INT-0008 back-XR +SRS-HW-0019, link-only), CR-0019/XSC-0010 (INT-0032 Priority HIGH→CRITICAL, aligns with HW-0025 CRITICAL framing of the pogo-pin+magnet assembly; priority field only, no text change). All three §10-side only — no approval revocation. v4: cross-section resolutions applied per Conflict & Consistency Resolver — CR-0010/XSC-0002 (INT-0027 cross-ref SRS-OPER-0005→SRS-OPER-0004 + footer relied-upon list corrected), CR-0011/XSC-0003 (INT-0008 Priority HIGH→MEDIUM, aligns with §4 SRS-CONN-0007), CR-0012/XSC-0004 (INT-0029 Priority HIGH→MEDIUM, aligns with §6 SRS-PERF-0005), CR-0013/XSC-0006 (INT-0051 Priority MEDIUM→LOW, aligns with §6 SRS-PERF-0008). XSC-0005 (INT-0045 vs §7 SRS-SAFE-0011) resolved §7-side (SAFE-0011 HIGH→CRITICAL by Requirements Drafter); INT-0045 remains CRITICAL, unchanged here (CR-0009). v3: CR-0006 (§10.4 terminology standardization), CR-0007 (INT-0033↔INT-0049 reciprocal cross-refs + clarifiers), CR-0008 (INT-0047 Priority MEDIUM→HIGH) applied per Conflict & Consistency Resolver. v2: torque contradiction (INT-0044/0047) and verification-method fixes (INT-0036, INT-0056) applied per Feasibility Checker & Verification-Method Validator flags

---

## 10.0 Scope Note

This section specifies the external interfaces of the LUUCIPet Wellness Monitor system: the BLE radio interface (collar↔base station), the Wi-Fi radio interface (base station↔cloud), the GNSS receive interface (Max only), the pogo-pin charging interface, the Twist-Lock mechanical attachment interface (collar device↔CCF), and the device-enforced BLE application protocol [PRD §6, PRD §10.2, PRD §10.3, PRD §10.5, PRD §11]. Zone 2 Fuse Tab breakaway force windows and post-breakaway safety protocol are governed by the Safety Requirements section (CAT=SAFE) and are not restated here; the Twist-Lock mechanism addressed in this section is the non-breakaway, owner-operated charging-removal interface only [PRD §10.1.3.1]. Cross-variant identical mechanical-interface geometry for pogo-pin and Twist-Lock across Mini/Max is already established by **SRS-COMP-0003** (§2); this section does not re-issue that requirement.

---

## 10.1 BLE Interface

```plain
ID:                  SRS-INT-0001
Title:               Collar BLE Peripheral Role
Statement:           The collar device shall implement the Bluetooth Low Energy (BLE) 5.x radio interface in the peripheral role.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §6.3], [PRD §8.1], [PRD §10.3]
Rationale:           The collar is the advertising/connectable endpoint of the collar-to-base-station link; role assignment is imposed by the system architecture.
Verification Method: Test
Cross-References:    none
```
[GLOSS: peripheral role | the BLE role that advertises and accepts incoming connections, as opposed to the central role that scans and initiates connections]

```plain
ID:                  SRS-INT-0002
Title:               Base Station BLE Central Role
Statement:           The base station shall implement the BLE 5.x radio interface in the central role.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §11.2]
Rationale:           The base station scans for and initiates connections to collar devices; role assignment is imposed by the system architecture.
Verification Method: Test
Cross-References:    SRS-INT-0001
```
[GLOSS: central role | the BLE role that scans for advertisements and initiates connections to peripherals]

```plain
ID:                  SRS-INT-0003
Title:               Minimum Concurrent Collar Sessions
Statement:           The base station shall support at least 4 concurrent BLE connections to collar devices.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.1], [PRD §11.2]
Rationale:           A multi-pet household requires the base station to hold multiple simultaneous collar links without dropping connections.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0004
Title:               Default BLE Advertising Interval
Statement:           The collar device shall advertise via BLE with a default advertising interval of 60 seconds.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §6.3], [PRD §8.1]
Rationale:           Establishes the out-of-box discoverability cadence balancing power consumption against connection latency.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0005
Title:               Configurable BLE Advertising Interval Range
Statement:           The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §8.1]
Rationale:           Allows the advertising cadence to be tuned for household-specific power/latency trade-offs.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0006
Title:               Advertising Continuity During Active Connection
Statement:           The collar device shall continue BLE advertising while maintaining an active BLE connection.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §8.1], [PRD §10.3]
Rationale:           Preserves discoverability for additional base stations in a multi-base household while a collar is already connected to one base station.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0007
Title:               BLE Address Randomization
Statement:           The collar device shall randomize its BLE device address.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.1], [PRD §10.3]
Rationale:           Prevents long-term tracking of the wearable by third parties observing BLE advertisements.
Verification Method: Test
Cross-References:    none
```
[GLOSS: address randomization | periodic rotation of the BLE device address to prevent long-term tracking by third-party observers]

```plain
ID:                  SRS-INT-0008
Title:               Minimum BLE Transmit Power
Statement:           The collar device shall transmit BLE signals at a power level of at least +8 dBm.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §10.3]
Rationale:           A minimum TX power floor is necessary to meet the stated open-air range target.
Verification Method: Test
Cross-References:    SRS-INT-0009, SRS-HW-0019
```

```plain
ID:                  SRS-INT-0009
Title:               Minimum BLE Open-Air Range
Statement:           The BLE link between the collar device and the base station shall maintain connectivity at an open-air separation distance of at least 9 meters.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.3], [PRD §12.1]
Rationale:           Defines the minimum usable range for typical household room-to-room and yard-adjacent operation.
Verification Method: Test
Cross-References:    SRS-INT-0008
```

```plain
ID:                  SRS-INT-0010
Title:               BLE Link-Layer Encryption Algorithm
Statement:           The system shall encrypt all BLE data-bearing links using AES-128 CCM.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §6.3], [PRD §8.2], [PRD §10.3]
Rationale:           Mandated link-layer confidentiality/integrity mechanism for all collar-to-base-station traffic.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0011
Title:               BLE Pairing via LE Secure Connections
Statement:           The system shall establish BLE pairing between the collar device and the base station using LE Secure Connections.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §6.3], [PRD §8.2]
Rationale:           Provides the pairing-time key-exchange mechanism underpinning the mandated link-layer encryption.
Verification Method: Test
Cross-References:    SRS-INT-0010
```
[GLOSS: LE Secure Connections | a BLE pairing method using elliptic-curve key exchange to establish link-layer encryption keys]

```plain
ID:                  SRS-INT-0012
Title:               QR Out-of-Band Pairing Mechanism
Statement:           The system shall support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §6.3], [PRD §8.2]
Rationale:           Defines the device/base-station-side OOB pairing mechanism; the mobile app's presentation of the QR code to the user is out of scope for this SRS and is attributed to the (out-of-scope) Mobile App per the standing scope boundary.
Verification Method: Test
Cross-References:    none
```
[GLOSS: QR OOB pairing | an out-of-band BLE pairing method in which a QR code carries pairing data, avoiding reliance on numeric-comparison or passkey entry]

```plain
ID:                  SRS-INT-0013
Title:               BLE Radio Regulatory Conformance
Statement:           The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US), [STD: RED 2014/53/EU] (EU), [STD: UK Radio Equipment Regulations 2017] (UK), [STD: ISED RSS-247] (CA), and [STD: AS/NZS 4268:2017] (AU/NZ).
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §13.1]
Rationale:           Market access for an intentional 2.4 GHz radiator requires conformance to each target market's radio-equipment regulation.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0014
Title:               Bluetooth SIG Qualification
Statement:           The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID).
Priority:            CRITICAL
Stability:           STABLE
Source:              [STD: Bluetooth SIG Qualification (QDID)], [PRD §13.1]
Rationale:           Bluetooth SIG membership terms mandate qualification of any BLE product before market release.
Verification Method: Inspection
Cross-References:    none
```
[GLOSS: QDID | Qualified Design ID — the identifier issued by the Bluetooth SIG upon successful qualification testing of a BLE product design]

```plain
ID:                  SRS-INT-0015
Title:               RF Human-Exposure Assessment
Statement:           The BLE radio interface should undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4 GHz transmission.
Priority:            MEDIUM
Stability:           VOLATILE
Source:              [PRD §13.1]
Rationale:           A continuously worn 2.4 GHz transmitter plausibly triggers per-market RF-exposure assessment; applicability and thresholds are per-market INDICATIVE per the Regulatory Map and not yet CONFIRMED, hence a SHOULD rather than SHALL.
Verification Method: Analysis
Cross-References:    none
```

---

## 10.2 Wi-Fi Interface

```plain
ID:                  SRS-INT-0016
Title:               Wi-Fi Radio Band and Standard
Statement:           The base station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n].
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §4.2], [PRD §6.5]
Rationale:           Defines the base-to-cloud uplink radio band and PHY/MAC standard.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0017
Title:               Cloud Uplink Transport Encryption
Statement:           The base station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §6.5], [PRD §11.2], [PRD §12.3]
Rationale:           Mandated transport-layer confidentiality/integrity mechanism for base-station-to-cloud traffic; the device/base-station side of this transport is in scope, cloud-side storage/analytics is out of scope [ASSUMPTION A-0015].
Verification Method: Test
Cross-References:    none
```
[GLOSS: TLS 1.3 | Transport Layer Security version 1.3, the transport-layer encryption protocol used for base-station-to-cloud traffic]

```plain
ID:                  SRS-INT-0018
Title:               Default Access-Point Configuration Compatibility
Statement:           The base station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §12.6]
Rationale:           Avoids requiring the owner to perform non-default router configuration for base-station setup.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0019
Title:               Minimum Wi-Fi Uplink Signal Condition
Statement:           The base station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput.
Priority:            MEDIUM
Stability:           LIKELY-CHANGE
Source:              [ASSUMPTION A-0009]
Rationale:           Resolves the PRD's unbounded "reliable Wi-Fi" assumption with an engineered numeric floor; below this bound the ≥30-day offline buffering behavior (Data Requirements, §9) is the defined degraded-mode fallback rather than a new interface requirement.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0020
Title:               Wi-Fi Radio Regulatory Conformance
Statement:           The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US) and [STD: RED 2014/53/EU] (EU).
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §13.1]
Rationale:           Market access for the base station's Wi-Fi radio requires conformance to each target market's radio-equipment regulation.
Verification Method: Test
Cross-References:    none
```

---

## 10.3 GNSS Interface (Max Only)

```plain
ID:                  SRS-INT-0021
Title:               GNSS Interface Presence on Max
Statement:           The Max collar variant shall implement a passive (receive-only) GNSS interface.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §4.1], [PRD §10.2.2]
Rationale:           GNSS is a defining differentiator of the Max variant, providing location context unavailable on Mini.
Verification Method: Test
Cross-References:    none
```
[GLOSS: GNSS | Global Navigation Satellite System — a passive receiver providing position-fix data from satellite signals]

```plain
ID:                  SRS-INT-0022
Title:               GNSS Interface Absence on Mini
Statement:           The Mini collar variant shall not implement a GNSS interface.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §4.1]
Rationale:           GNSS hardware is excluded from Mini to meet its ≤10 g weight budget and BLE-only positioning.
Verification Method: Inspection
Cross-References:    none
```

```plain
ID:                  SRS-INT-0023
Title:               Configurable GNSS Fix Interval Range
Statement:           The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §4.1], [PRD §10.2.2]
Rationale:           Allows the fix cadence to be tuned against the battery-life-vs-fix-interval trade-off documented in the PRD.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0024
Title:               Default GNSS Fix Interval
Statement:           The Max collar variant shall apply a default GNSS fix interval of 2 hours.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §4.1], [PRD §10.2.2]
Rationale:           Establishes the out-of-box fix cadence consistent with the stated ≥45-day @2h battery-life target.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0025
Title:               A-GPS Assistance Data Delivery
Statement:           The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.2.2]
Rationale:           A-GPS delivery over the existing BLE link is the defined mechanism for reducing GNSS fix acquisition time.
Verification Method: Test
Cross-References:    none
```
[GLOSS: A-GPS | Assisted GPS — auxiliary satellite ephemeris/almanac data delivered via a terrestrial link (here, BLE) to reduce GNSS fix acquisition time]

```plain
ID:                  SRS-INT-0026
Title:               A-GPS Assistance Data Validity Window
Statement:           The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §10.2.2]
Rationale:           Bounds how long stale assistance data may be relied upon before fix-acquisition performance degrades.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0027
Title:               GNSS Power Gating During HOME State
Statement:           The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.2.2], [PRD §6.4], [ASSUMPTION A-0016]
Rationale:           The GNSS smart power gate underpins the stated Max battery-longevity targets; gating authority rests solely with the device-local state machine per the confirmed in-scope/external boundary.
Verification Method: Test
Cross-References:    SRS-OPER-0004
```

```plain
ID:                  SRS-INT-0028
Title:               GNSS Fix Acquisition Timeout
Statement:           The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.2.2], [PRD §15.5]
Rationale:           Bounds the power expenditure of an unsuccessful fix attempt.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0029
Title:               Warm GNSS Time-to-First-Fix Ceiling
Statement:           The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §12.1]
Rationale:           Bounds the latency between a scheduled fix attempt and an available location result.
Verification Method: Test
Cross-References:    SRS-INT-0025
```
[GLOSS: TTFF | Time-To-First-Fix — the elapsed time from the start of a GNSS fix attempt to acquisition of a valid position fix]

```plain
ID:                  SRS-INT-0030
Title:               GNSS Intentional-Radiator Exemption Status
Statement:           The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation.
Priority:            MEDIUM
Stability:           VOLATILE
Source:              [PRD §13.1]
Rationale:           The PRD defers this exemption determination to Regulatory Lead confirmation per market; the Regulatory Map carries this as INDICATIVE, not CONFIRMED, hence a SHOULD rather than SHALL pending resolution.
Verification Method: Analysis
Cross-References:    none
```

> **Flagged (not a normative block):** Per [ASSUMPTION A-0004], "full-quality GNSS" is interpreted as acquisition-based (a fix obtained within the 90 s timeout using A-GPS); no PDOP or metres-level position-accuracy bound is imposed by the PRD, and none is introduced here. This is documented to prevent a future numeric-accuracy requirement from being silently assumed.

---

## 10.4 Pogo-Pin Charging Interface

```plain
ID:                  SRS-INT-0031
Title:               Pogo-Pin Contact Count and Function
Statement:           The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) shall use a 2-contact pogo-pin arrangement carrying VBUS and GND.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §10.5]
Rationale:           Defines the minimal electrical contact interface for charging; cross-variant identical geometry is already established by SRS-COMP-0003.
Verification Method: Inspection
Cross-References:    SRS-COMP-0003
```
[GLOSS: VBUS | the positive supply-voltage contact of the pogo-pin charging interface]

```plain
ID:                  SRS-INT-0032
Title:               Magnetic Charging Alignment
Statement:           The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §6.6], [PRD §10.5]
Rationale:           Magnetic alignment enables reliable tool-free docking without precise manual contact placement.
Verification Method: Demonstration
Cross-References:    none
```

```plain
ID:                  SRS-INT-0033
Title:               First-Attempt Docking Seating Rate
Statement:           The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §10.1.3.5]
Rationale:           Bounds the usability of the magnetic docking mechanism to a measurable success rate. Note: this magnetic assist governs the charging-dock (collar device onto charging cradle) interface and is distinct from the device-to-CCF Twist-Lock engagement assist in SRS-INT-0049, though both specify an "up to 5 mm" approach distance.
Verification Method: Test
Cross-References:    SRS-INT-0049
```

```plain
ID:                  SRS-INT-0034
Title:               Full-Charge Time Ceiling
Statement:           The collar device shall reach full charge within 2 hours when docked at the charging interface.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.5], [PRD §12.4]
Rationale:           Bounds the time an owner must leave a device docked to restore full charge.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0035
Title:               IP67 Rating When Undocked
Statement:           The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §6.6], [PRD §10.5], [PRD §13.4]
Rationale:           The exposed pogo-pin contact is a potential ingress path and must not compromise the device-standalone IP67 rating.
Verification Method: Test
Cross-References:    SRS-HW-0004
```

```plain
ID:                  SRS-INT-0036
Title:               Charging Socket Self-Drainage
Statement:           The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical).
Priority:            MEDIUM
Stability:           LIKELY-CHANGE
Source:              [PRD §10.5], [PRD §10.1.3.5], [ASSUMPTION: A-0023]
Rationale:           PRD §10.5/§10.1.3.5 state the socket "shall be self-draining" with no quantified acceptance criterion; the Verification-Method Validator flagged this as method/criterion incoherence — the declared Test method (correctly changed from Inspection) had nothing measurable to test against. [ASSUMPTION: A-0023] resolves this gap (engineered by analogy to A-0007). This requirement shares its underlying drainage claim with SRS-HW-0008 (§11, hardware-geometry framing of the same socket); both corrected together.
Verification Method: Test
Cross-References:    SRS-HW-0008
```

```plain
ID:                  SRS-INT-0037
Title:               Charging-Access Removal Rotation
Statement:           The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §6.6], [PRD §10.5]
Rationale:           Defines the workflow by which the charging contacts are exposed for docking, using the non-breakaway Twist-Lock mechanism.
Verification Method: Demonstration
Cross-References:    SRS-INT-0039
```

```plain
ID:                  SRS-INT-0038
Title:               Device-Absent Socket Entrapment Geometry
Statement:           The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature.
Priority:            HIGH
Stability:           LIKELY-CHANGE
Source:              [ASSUMPTION A-0010], [PRD §10.1.3.5]
Rationale:           Resolves the PRD's unbounded "no independent entrapment hazard" statement with an engineered geometric probe criterion.
Verification Method: Test
Cross-References:    none
```

---

## 10.5 Twist-Lock Mechanical Interface

```plain
ID:                  SRS-INT-0039
Title:               Bayonet Lug Configuration
Statement:           The Twist-Lock mechanical interface shall use a 3-lug bayonet arrangement spaced at 120 degrees.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Defines the base geometric arrangement of the device-to-CCF mechanical attachment; identical across Mini/Max per SRS-COMP-0003.
Verification Method: Inspection
Cross-References:    SRS-COMP-0003
```
[GLOSS: bayonet | a mechanical fastening geometry engaged by insertion followed by a partial rotation to lock]

```plain
ID:                  SRS-INT-0040
Title:               Lock/Unlock Rotation Angle
Statement:           The Twist-Lock mechanical interface shall engage and release via a 90-degree rotation.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Defines the actuation travel required to lock or unlock the device from the CCF.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0041
Title:               Lug Ramp Self-Locking Profile
Statement:           The Twist-Lock lug ramp shall have a trapezoidal profile with an 8-degree self-locking angle.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           The ramp angle is imposed to achieve self-locking behavior without requiring a separate latch.
Verification Method: Inspection
Cross-References:    none
```

```plain
ID:                  SRS-INT-0042
Title:               Twist-Lock Lug Dimensions
Statement:           Each Twist-Lock lug shall be 4.0 mm wide by 1.2 mm thick.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Fixed lug dimensions are required for interoperability across all CCF SKUs and both collar variants.
Verification Method: Inspection
Cross-References:    none
```

```plain
ID:                  SRS-INT-0043
Title:               Asymmetric Keying Lug
Statement:           The Twist-Lock interface shall include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct engagement orientation.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Prevents incorrect-orientation assembly of the device onto the CCF.
Verification Method: Inspection
Cross-References:    none
```
[GLOSS: keying | a deliberate geometric asymmetry that permits mechanical engagement in only one correct orientation]

```plain
ID:                  SRS-INT-0044
Title:               Detent Release Torque Window
Statement:           The Twist-Lock detent shall release within a torque window of 0.08 to 0.10 N·m.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Bounds the rotational effort at which the detent yields, balancing inadvertent-release resistance against ease of intentional removal; upper bound narrowed from 0.15 N·m to 0.10 N·m to align with SRS-INT-0047's engage/release torque ceiling, per PRD §10.1.3.2a's intent that detent release remain at or below the engage torque ceiling.
Verification Method: Test
Cross-References:    SRS-INT-0047
```
[GLOSS: detent | a spring-loaded mechanical feature that resists rotation until a threshold torque is exceeded, providing tactile lock/unlock feedback]

```plain
ID:                  SRS-INT-0045
Title:               Twist-Lock Axial Retention Floor
Statement:           The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing.
Priority:            CRITICAL
Stability:           STABLE
Source:              [PRD §10.1.3.1], [PRD §10.1.3.2a]
Rationale:           The Twist-Lock is explicitly not a breakaway mechanism; it must retain the device under normal and inertial loading (distinct from the Zone 2 Fuse Tab, which is governed under Safety Requirements).
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0046
Title:               Twist-Lock Engagement Insertion Force Ceiling
Statement:           The Twist-Lock interface shall require no more than 5 N of axial press-in force to engage.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §10.1.1], [PRD §10.1.3.2a]
Rationale:           Bounds the physical effort required of the owner during the engagement workflow.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0047
Title:               Twist-Lock Engagement Rotation Torque Ceiling
Statement:           The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.1], [PRD §10.1.3.2a]
Rationale:           Bounds the rotational effort required of the owner during the engage/remove workflow. Priority raised MEDIUM→HIGH (CR-0008) so this governing torque ceiling is at least as critical as the dependent detent-release window (SRS-INT-0044, HIGH) that is bounded by it.
Verification Method: Test
Cross-References:    SRS-INT-0044
```

```plain
ID:                  SRS-INT-0048
Title:               Engagement Feedback
Statement:           The Twist-Lock interface shall provide an audible and tactile click upon full engagement.
Priority:            MEDIUM
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Confirms to the owner that the device has reached the fully locked position without requiring visual inspection.
Verification Method: Demonstration
Cross-References:    none
```

```plain
ID:                  SRS-INT-0049
Title:               Magnetic Engagement Assist Range
Statement:           The Twist-Lock interface shall provide magnetic engagement assistance effective at an approach distance of up to 5 mm.
Priority:            LOW
Stability:           STABLE
Source:              [PRD §10.1.3.2a]
Rationale:           Assists initial alignment of the device onto the CCF socket before rotation. Note: this Twist-Lock (device-to-CCF) magnetic engagement assist is distinct from the charging-dock magnetic alignment in SRS-INT-0033, though both specify an "up to 5 mm" approach distance.
Verification Method: Test
Cross-References:    SRS-INT-0033
```

```plain
ID:                  SRS-INT-0050
Title:               Tool-Free Twist-Lock Operation
Statement:           The Twist-Lock interface shall be operable without tools.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §10.1.3.2a], [PRD §12.4]
Rationale:           Owners must be able to engage and remove the device without specialized equipment.
Verification Method: Demonstration
Cross-References:    none
```

```plain
ID:                  SRS-INT-0051
Title:               Twist-Lock Engagement Time Ceiling
Statement:           The Twist-Lock interface shall be engageable within 5 seconds.
Priority:            LOW
Stability:           STABLE
Source:              [PRD §12.1], [PRD §12.4]
Rationale:           Bounds the time required to complete the mechanical engagement step of the CCF-install workflow.
Verification Method: Test
Cross-References:    none
```

---

## 10.6 Device-Enforced Protocol

```plain
ID:                  SRS-INT-0052
Title:               Common Device-Enforced Protocol Across Variants
Statement:           The system shall use a common device-enforced BLE application protocol shared across all collar and base-station firmware variants.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §4.3], [ASSUMPTION A-0001]
Rationale:           A single shared protocol avoids per-variant protocol fragmentation and depends on the protocol/ICD being frozen before verification per A-0001.
Verification Method: Inspection
Cross-References:    SRS-COMP-0001
```
[GLOSS: device-enforced protocol | the application-layer message protocol, defined and enforced by device/base-station firmware, governing all collar-to-base-station BLE data exchange]

```plain
ID:                  SRS-INT-0053
Title:               Payload Type — Behavioral Classification Record
Statement:           The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §7.5], [PRD §8.3]
Rationale:           Behavioral records are the primary data product synced from collar to base station and require an identifiable payload type.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0054
Title:               Payload Type — BLE Sighting Report
Statement:           The device-enforced protocol shall support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (RSSI), timestamp, and base station identifier, as a distinct payload type.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.5], [PRD §11.3]
Rationale:           Sighting reports are the data basis for home/away geo-fence determination and are reported independent of behavioral-data sync.
Verification Method: Test
Cross-References:    none
```
[GLOSS: RSSI | Received Signal Strength Indicator, a measurement of BLE signal power used for sighting and geo-fence determination]

```plain
ID:                  SRS-INT-0055
Title:               Payload Type — Cloud Downlink
Statement:           The device-enforced protocol shall support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.6]
Rationale:           Downlink configuration and OTA image delivery are distinct data flows from the collar-to-base uplink and require their own payload type.
Verification Method: Test
Cross-References:    none
```

```plain
ID:                  SRS-INT-0056
Title:               Base Station Payload Content Opacity
Statement:           The base station shall relay collar behavioral payloads to the cloud without semantically interpreting their content.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.3]
Rationale:           Keeps behavioral-data interpretation logic on the collar/cloud endpoints only, avoiding base-station firmware dependency on payload semantics; verification method corrected from Test to Inspection because this is a negative architectural claim (absence of interpretation logic) that black-box behavioral testing cannot conclusively prove — a base station could interpret payload content internally and still relay it correctly, defeating a Test-based check. Design/firmware/code review confirming no semantic-parsing logic exists on the relay path is the appropriate method.
Verification Method: Inspection
Cross-References:    none
```

```plain
ID:                  SRS-INT-0057
Title:               Collar Buffer Retention Pending Acknowledgment
Statement:           The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the base station.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.4]
Rationale:           Prevents data loss from premature buffer clearing before successful delivery is confirmed.
Verification Method: Test
Cross-References:    none
```
[GLOSS: ACK | a positive acknowledgment message confirming successful receipt of a transmitted record]
[GLOSS: FIFO | First-In-First-Out — the ordered local buffer holding classification records pending delivery]

```plain
ID:                  SRS-INT-0058
Title:               No FIFO Clear on Disconnect Alone
Statement:           The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §8.4]
Rationale:           A disconnection is not itself confirmation of delivery; clearing on disconnect alone would risk silent data loss.
Verification Method: Test
Cross-References:    SRS-INT-0057
```

```plain
ID:                  SRS-INT-0059
Title:               Sequence-Loss Detection
Statement:           The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §7.6]
Rationale:           Enables the receiving side to detect gaps in the forwarded record stream without depending on a specific transport-level guarantee.
Verification Method: Test
Cross-References:    none
```
[GLOSS: sequence identifier | a per-record protocol field enabling the receiving side to detect gaps in a forwarded record stream]

```plain
ID:                  SRS-INT-0060
Title:               Corruption-Free Record Forwarding
Statement:           The device-enforced protocol shall forward classification records over BLE without introducing data corruption.
Priority:            HIGH
Stability:           STABLE
Source:              [PRD §7.6]
Rationale:           Ensures the integrity of behavioral data is preserved end-to-end across the BLE hop.
Verification Method: Test
Cross-References:    none
```

---

## 10.7 Out-of-Scope Items & Flagged Gaps (Documented, Not Silently Dropped)

- **GPS-M variant / cellular connectivity** — explicitly OUT OF SCOPE for this SRS (Phase 2, separate PRD) per the PRD's own scope note. No GPS-M or cellular interface requirement is issued in this section, and none should be inferred.
- **Mobile App pairing UI / provisioning** — the app's presentation of the QR OOB pairing code and any BLE-provisioning UI flow is OUT OF SCOPE for this SRS (Mobile App team); only the device/base-station-side OOB pairing mechanism is specified here (SRS-INT-0012).
- **Cloud-side storage/analytics beyond ingest** — OUT OF SCOPE for this SRS per [ASSUMPTION A-0015]; only the device/base-station-side transport (Wi-Fi/TLS 1.3 uplink) is specified here (SRS-INT-0017).
- **NACK mechanics and retry policy** — the PRD specifies positive-ACK-gated buffer retention (§8.4) but does not specify a NACK message, retry count, or retry backoff interval. No numeric retry policy is invented here per the design-free/numeric-vagueness rule; this is flagged as a candidate new assumption or PRD clarification for the Conductor/Assumption Register rather than an SRS requirement with an unsourced numeric bound.
- **GNSS position-accuracy bound** — per [ASSUMPTION A-0004], no PDOP or metres-level accuracy target is imposed on the Max GNSS interface beyond acquisition within the 90 s timeout; documented in §10.3 to prevent a future undocumented accuracy requirement.
- **Zone 2 Fuse Tab breakaway force windows and post-breakaway protocol** — governed by the Safety Requirements section (CAT=SAFE); intentionally not restated in this Interface Requirements section.

---

### SRS-IDs issued

SRS-INT-0001 through SRS-INT-0060 (60 requirements).

### Assumptions cited

A-0001, A-0004, A-0009, A-0010, A-0015, A-0016.

### Existing cross-references relied upon (not re-issued)

SRS-COMP-0001, SRS-COMP-0003, SRS-OPER-0004 (all from approved §2).
