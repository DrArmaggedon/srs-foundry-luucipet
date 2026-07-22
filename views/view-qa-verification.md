# SRS-LUUCIPET — Derived View: QA / Verification

> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:30:00Z
> **Audience:** Quality Assurance, Verification & Validation, Test Engineering
> ⚠️ For full context, always refer to the Master SRS.

---

## Purpose

This view reduces every requirement in the Master SRS to its essential verification elements — **ID**, **Statement**, **Priority**, and **Verification Method** — grouped by verification method for test-planning and traceability purposes. Rationale, Stability, and Traceability fields are stripped per the QA/Verification View derivation rules. The full Requirements Traceability Matrix (RTM) follows at the end of this document.

**Total requirements catalogued:** 364

---

## Verification Method: Test

_Requirements verified through direct measurement, execution, or observation of system behavior under controlled conditions._

**Count:** 147 requirements

| Requirement ID | Statement | Priority |
| :--- | :--- | :--- |
| SRS-COMP-0001 | Base Station firmware **shall** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. | High |
| SRS-COMP-0002 | All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **shall** be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. | Critical |
| SRS-CONN-0004 | The system **shall** advertise the presence of the collar-mounted device at a default interval of 60 seconds. | Medium |
| SRS-CONN-0005 | The system **shall** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. | Medium |
| SRS-CONN-0006 | The system **shall** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. | High |
| SRS-CONN-0007 | The system **shall** transmit BLE signals at a power level of no less than +8 dBm. | Medium |
| SRS-CONN-0010 | Upon the collar-mounted device re-entering BLE range of a base station, the system **shall** automatically re-establish the BLE link without requiring manual user action. | Critical |
| SRS-CONN-0011 | Upon establishing a BLE link with a base station, the system **shall** forward stored classification records from the collar-mounted device to the base station. | Critical |
| SRS-CONN-0013 | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **shall** forward all classification records accumulated during that disconnection. | Critical |
| SRS-CONN-0014 | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. | Critical |
| SRS-CONN-0015 | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. | Critical |
| SRS-CONN-0016 | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. | Critical |
| SRS-CONN-0017 | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. | Critical |
| SRS-CONN-0019 | The system **shall** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. | High |
| SRS-CONN-0020 | The system **shall** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in range. | High |
| SRS-CONN-0022 | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. | High |
| SRS-CONN-0024 | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other classification records. | Medium |
| SRS-CONN-0025 | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix as part of classification records. | Medium |
| SRS-CONN-0028 | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. | High |
| SRS-CONN-0029 | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. | High |
| SRS-ENV-0001 | The collar device **shall** operate within an ambient temperature range of −20 °C to +50 °C without loss of function. | Critical |
| SRS-ENV-0002 | The collar device **shall** withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequent operational performance. | High |
| SRS-ENV-0003 | The CCF **shall** be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of function. | High |
| SRS-ENV-0004 | The collar device **should** withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. | Medium |
| SRS-ENV-0007 | The Twist-Lock lug channels **shall** exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003. | Critical |
| SRS-ENV-0009 | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. | Critical |
| SRS-ENV-0010 | The collar device **should** withstand mechanical shock per IEC 60068-2-27 without loss of function. | Medium |
| SRS-ENV-0011 | The collar device **should** withstand vibration per IEC 60068-2-64 without loss of function. | Medium |
| SRS-ENV-0013 | The CCF **shall** withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. | Critical |
| SRS-ENV-0014 | The CCF **shall** withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across pH 5.5 to 8.5, enzymatic pet-odor and stain cleaners, fresh water, and salt water. | High |
| SRS-ENV-0015 | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | Critical |
| SRS-ENV-0016 | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Twist-Lock detent release torque **shall** remain within the torque window defined in SRS-INT-0044. | High |
| SRS-ENV-0017 | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | Critical |
| SRS-ENV-0018 | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | Critical |
| SRS-FUNC-0001 | The collar device **shall** detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event record to non-volatile storage within 5 s of the separation event, with a false-positive rate not exceeding 0.1% per device-wear-day and a true-event... | Critical |
| SRS-FUNC-0002 | The Base Station **shall** transport a recorded breakaway/separation event to the IoT Cloud Device-Management layer on the next successful Base Station contact and cloud sync (event-triggered; no delivery-time guarantee, as post-breakaway the device may be lost, out of range, or depleted). | Critical |
| SRS-FUNC-0003 | The persisted breakaway event record **shall** survive subsequent power loss, battery depletion, and reboot without corruption, and be transmitted to the Base Station on the next successful Base Station contact. | Critical |
| SRS-FUNC-0008 | While in Insight mode, the system **shall** sample the accelerometer continuously at 50 Hz. | High |
| SRS-FUNC-0009 | The system **shall** automatically revert from Insight mode to Wellness mode without requiring a manual user action. | High |
| SRS-FUNC-0010 | Upon detecting motion, the system **shall** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. | High |
| SRS-FUNC-0011 | While in Wellness mode and outside a confirmation burst, the system **shall not** exceed an idle current draw of 4 µA. | Critical |
| SRS-FUNC-0012 | When Longevity Mode is active, the system **shall not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. | Critical |
| SRS-FUNC-0013 | When Longevity Mode is active, the system **shall not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. | Critical |
| SRS-FUNC-0014 | The system **shall** sample the accelerometer at a rate of no less than 50 Hz. | Critical |
| SRS-FUNC-0017 | The system **shall** set species-specific classification thresholds during the onboarding process. | High |
| SRS-FUNC-0018 | The system **shall** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. | Critical |
| SRS-FUNC-0019 | The system **shall not** exceed a false-positive rate of 5% for each Tier-1 behavior class. | Critical |
| SRS-FUNC-0020 | The system **shall** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. | High |
| SRS-FUNC-0021 | The system **shall not** exceed a false-positive rate of 10% for each Tier-2 behavior class. | High |
| SRS-FUNC-0023 | The system **shall** include a confidence score in the range 0.0 to 1.0 in every generated classification record. | High |
| SRS-FUNC-0024 | The system **shall** timestamp every classification record in UTC with a resolution no coarser than 1 second. | High |
| SRS-FUNC-0026 | The system **shall** retain generated classification records locally for no less than 30 days without a cloud connection. | Critical |
| SRS-FUNC-0027 | The system **shall not** discard stored classification records upon loss of connectivity. | Critical |
| SRS-FUNC-0029 | The system **shall** forward stored classification records without data corruption. | Critical |
| SRS-FUNC-0030 | The system **shall** forward stored classification records without loss of their original sequence order. | High |
| SRS-FUNC-0032 | The system **shall not** transmit raw accelerometer data off the collar. | Critical |
| SRS-FUNC-0036 | The system **shall** apply a Scratching alert threshold value received via the companion application. | High |
| SRS-FUNC-0038 | The system **shall** apply a Shaking alert threshold value received via the companion application. | High |
| SRS-FUNC-0040 | The system **shall** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. | High |
| SRS-FUNC-0045 | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. | High |
| SRS-FUNC-0046 | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. | Medium |
| SRS-FUNC-0049 | The system **shall** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. | Critical |
| SRS-FUNC-0050 | The system **shall not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. | Critical |
| SRS-FUNC-0051 | The system **shall** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. | High |
| SRS-FUNC-0053 | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. | Critical |
| SRS-FUNC-0055 | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. | Critical |
| SRS-FUNC-0056 | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. | Critical |
| SRS-FUNC-0058 | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. | Medium |
| SRS-HW-0001 | The Mini collar device **shall** have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. | Critical |
| SRS-HW-0002 | The Max collar device **shall** have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding the CCF and collar. | Critical |
| SRS-HW-0003 | The collar device **shall** achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. | Critical |
| SRS-HW-0004 | The collar device enclosure **shall** maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. | Critical |
| SRS-HW-0008 | The device-facing charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | Medium |
| SRS-HW-0014 | The collar device accelerometer **shall** support an output data rate of no less than 50 Hz. | Critical |
| SRS-HW-0019 | The collar device BLE radio **shall** be capable of a transmit power of no less than +8 dBm. | Medium |
| SRS-HW-0022 | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. | Critical |
| SRS-HW-0023 | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. | High |
| SRS-HW-0024 | The collar device **shall** raise a low-battery alert at a state-of-charge of 20% or below. | Medium |
| SRS-HW-0026 | The collar device **shall** incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. | High |
| SRS-HW-0027 | The collar device **shall** incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. | Critical |
| SRS-INT-0001 | The collar device shall implement the Bluetooth Low Energy (BLE) 5.x radio interface in the peripheral role. | High |
| SRS-INT-0002 | The base station shall implement the BLE 5.x radio interface in the central role. | High |
| SRS-INT-0003 | The base station shall support at least 4 concurrent BLE connections to collar devices. | High |
| SRS-INT-0004 | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. | Medium |
| SRS-INT-0005 | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. | Medium |
| SRS-INT-0006 | The collar device shall continue BLE advertising while maintaining an active BLE connection. | Medium |
| SRS-INT-0007 | The collar device shall randomize its BLE device address. | High |
| SRS-INT-0008 | The collar device shall transmit BLE signals at a power level of at least +8 dBm. | Medium |
| SRS-INT-0009 | The BLE link between the collar device and the base station shall maintain connectivity at an open-air separation distance of at least 9 meters. | High |
| SRS-INT-0010 | The system shall encrypt all BLE data-bearing links using AES-128 CCM. | Critical |
| SRS-INT-0011 | The system shall establish BLE pairing between the collar device and the base station using LE Secure Connections. | Critical |
| SRS-INT-0012 | The system shall support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station. | High |
| SRS-INT-0013 | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US), [STD: RED 2014/53/EU] (EU), [STD: UK Radio Equipment Regulations 2017] (UK), [STD: ISED RSS-247] (CA), and [STD: AS/NZS 4268:2017] (AU/NZ). | Critical |
| SRS-INT-0016 | The base station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n]. | High |
| SRS-INT-0017 | The base station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. | Critical |
| SRS-INT-0018 | The base station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. | Medium |
| SRS-INT-0019 | The base station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. | Medium |
| SRS-INT-0020 | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart C] (US) and [STD: RED 2014/53/EU] (EU). | Critical |
| SRS-INT-0021 | The Max collar variant shall implement a passive (receive-only) GNSS interface. | High |
| SRS-INT-0023 | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. | High |
| SRS-INT-0024 | The Max collar variant shall apply a default GNSS fix interval of 2 hours. | Medium |
| SRS-INT-0025 | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. | High |
| SRS-INT-0026 | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. | Medium |
| SRS-INT-0027 | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. | High |
| SRS-INT-0028 | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. | High |
| SRS-INT-0029 | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. | Medium |
| SRS-INT-0033 | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. | Medium |
| SRS-INT-0034 | The collar device shall reach full charge within 2 hours when docked at the charging interface. | High |
| SRS-INT-0035 | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. | Critical |
| SRS-INT-0036 | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | Medium |
| SRS-INT-0038 | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature. | High |
| SRS-INT-0040 | The Twist-Lock mechanical interface shall engage and release via a 90-degree rotation. | High |
| SRS-INT-0044 | The Twist-Lock detent shall release within a torque window of 0.08 to 0.10 N·m. | High |
| SRS-INT-0045 | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. | Critical |
| SRS-INT-0046 | The Twist-Lock interface shall require no more than 5 N of axial press-in force to engage. | Medium |
| SRS-INT-0047 | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. | High |
| SRS-INT-0049 | The Twist-Lock interface shall provide magnetic engagement assistance effective at an approach distance of up to 5 mm. | Low |
| SRS-INT-0051 | The Twist-Lock interface shall be engageable within 5 seconds. | Low |
| SRS-INT-0053 | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. | High |
| SRS-INT-0054 | The device-enforced protocol shall support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (RSSI), timestamp, and base station identifier, as a distinct payload type. | High |
| SRS-INT-0055 | The device-enforced protocol shall support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type. | High |
| SRS-INT-0057 | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the base station. | High |
| SRS-INT-0058 | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. | High |
| SRS-INT-0059 | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. | High |
| SRS-INT-0060 | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. | High |
| SRS-OPER-0002 | A household deployment **shall not** exceed 8 Base Stations, in any combination of Charging and Relay tiers. | High |
| SRS-OPER-0003 | The collar device **shall** retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. | High |
| SRS-PERF-0003 | The system **shall** produce a classification result within 2 seconds of the triggering motion event. | High |
| SRS-PERF-0004 | The base station **shall** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. | Medium |
| SRS-PERF-0006 | The collar-mounted device **shall** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. | Medium |
| SRS-PERF-0007 | The system **shall** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. | High |
| SRS-SAFE-0001 | The Zone 2 Fuse Tab of the CCF-S variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. | Critical |
| SRS-SAFE-0002 | The Zone 2 Fuse Tab of the CCF-M variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. | Critical |
| SRS-SAFE-0003 | The Zone 2 Fuse Tab of the CCF-L variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device+CCF mass does not exceed 26 g. | Critical |
| SRS-SAFE-0005 | The Zone 2 Fuse Tab **shall not** be capable of being reused or restored to a load-bearing state after fracture. | Critical |
| SRS-SAFE-0009 | The Zone 1 clamp **shall** retain axial loads of at least 50 N without structural failure. | Critical |
| SRS-SAFE-0010 | The Zone 1 clamp **shall** remain structurally intact following a Zone 2 fracture event. | Critical |
| SRS-SAFE-0011 | The Twist-Lock device-to-CCF interface **shall** retain axial loads exceeding 100 N without disengaging. | Critical |
| SRS-SAFE-0012 | The Twist-Lock **shall** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. | High |
| SRS-SAFE-0014 | The device **shall** emit a detectable separation signature upon Zone 2 breakaway. | High |
| SRS-SAFE-0016 | The Zone 2 Fuse Tab **shall not** fracture under a compressive load below 250 N. | Critical |
| SRS-SAFE-0017 | The CCF body **shall** resist penetration for at least 30 seconds under a 250 N compressive load. | High |
| SRS-SAFE-0020 | The device-absent CCF socket **shall** provide clearance verified against a 12 mm entrapment-probe criterion. | Medium |
| SRS-SEC-0001 | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. | Critical |
| SRS-SEC-0002 | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. | Critical |
| SRS-SEC-0003 | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. | Critical |
| SRS-SEC-0005 | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. | Critical |

## Verification Method: Inspection

_Requirements verified through review of design artifacts, documentation, code, or physical attributes without active system operation._

**Count:** 182 requirements

| Requirement ID | Statement | Priority |
| :--- | :--- | :--- |
| SRS-COMP-0003 | The Mini and Max collar variants **shall** exhibit equivalent behavioral-classification outputs and use an interoperable common BLE communication protocol across the Mini and Max variants. | High |
| SRS-COMP-0005 | The collar device, in its standalone (CCF-unmated) configuration, shall conform to the IEC 60529 IPX7 test methodology as the verification basis for the IP67 ingress-protection rating required by SRS-HW-0003. | Critical |
| SRS-COMP-0006 | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). | Critical |
| SRS-COMP-0007 | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. | Critical |
| SRS-COMP-0008 | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable to cell construction, for placement on the US market. | High |
| SRS-COMP-0009 | The Base Station, in both Charging and Relay tiers, shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. | Critical |
| SRS-COMP-0010 | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. | Critical |
| SRS-COMP-0011 | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. | High |
| SRS-COMP-0012 | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. | Medium |
| SRS-COMP-0013 | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. | Medium |
| SRS-COMP-0014 | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. | Medium |
| SRS-COMP-0015 | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. | High |
| SRS-COMP-0016 | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. | Critical |
| SRS-COMP-0017 | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. | Critical |
| SRS-COMP-0018 | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. | Critical |
| SRS-COMP-0019 | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. | High |
| SRS-COMP-0020 | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. | Critical |
| SRS-COMP-0022 | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. | Critical |
| SRS-COMP-0023 | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. | Critical |
| SRS-COMP-0024 | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. | High |
| SRS-COMP-0025 | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. | Critical |
| SRS-COMP-0026 | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. | High |
| SRS-COMP-0027 | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. | Medium |
| SRS-COMP-0028 | The SBOM produced at each OTA release (SRS-FUNC-0061) and maintained across the supported service lifetime (SRS-MAINT-0002) shall be issued in a machine-readable format conforming to SPDX 2.3 or CycloneDX. | Medium |
| SRS-CONN-0001 | The system **shall** operate the collar-mounted device in the BLE peripheral role relative to the base station. | High |
| SRS-CONN-0002 | The system **shall** operate the base station in the BLE central role relative to the collar-mounted device. | High |
| SRS-CONN-0003 | The system **shall** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. | High |
| SRS-CONN-0008 | The system **shall** randomize the BLE device address of the collar-mounted device. | High |
| SRS-CONN-0009 | The system **shall** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. | Critical |
| SRS-CONN-0012 | The system **shall** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. | High |
| SRS-CONN-0018 | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. | Critical |
| SRS-CONN-0021 | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household account. | High |
| SRS-CONN-0023 | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. | High |
| SRS-DATA-0001 | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. | Critical |
| SRS-DATA-0002 | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. | High |
| SRS-DATA-0003 | The system shall timestamp each classification record with UTC time accurate to within 1 second. | High |
| SRS-DATA-0004 | On the Max variant, the system shall append the most recent GNSS fix to the classification record. | High |
| SRS-DATA-0005 | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. | Critical |
| SRS-DATA-0006 | The system shall preserve stored classification records without corruption across a power-loss event. | Critical |
| SRS-DATA-0007 | The system shall detect corruption of stored classification records prior to transmission. | High |
| SRS-DATA-0008 | The system shall perform classification and record generation independent of BLE connectivity state. | Critical |
| SRS-DATA-0009 | The system shall forward stored classification records to the transport layer without introducing data corruption. | Critical |
| SRS-DATA-0010 | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. | High |
| SRS-DATA-0011 | The system shall not transmit raw accelerometer data beyond the collar. | Critical |
| SRS-DATA-0012 | The system shall perform normalization of sensor data on-device prior to classification. | High |
| SRS-DATA-0013 | The system shall not require a cloud round-trip to complete a classification decision. | High |
| SRS-DATA-0014 | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. | Medium |
| SRS-DATA-0015 | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. | Critical |
| SRS-DATA-0016 | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. | Critical |
| SRS-DATA-0017 | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. | Medium |
| SRS-DATA-0018 | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. | High |
| SRS-DATA-0019 | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. | High |
| SRS-DATA-0020 | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. | Medium |
| SRS-DATA-0021 | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. | Medium |
| SRS-DATA-0022 | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. | Low |
| SRS-DATA-0023 | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. | Critical |
| SRS-DATA-0024 | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. | Critical |
| SRS-DATA-0025 | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. | Critical |
| SRS-DATA-0026 | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. | Critical |
| SRS-DATA-0027 | The system shall transmit a committed breakaway event record on the next successful base-station contact following separation. | High |
| SRS-ENV-0005 | Product documentation and marketing materials **shall not** state or imply an IP67, or equivalent, ingress-protection rating for the collar device while mated to any CCF. | Critical |
| SRS-ENV-0006 | The IP67 ingress-protection rating claimed for the collar device **shall** be confirmed by an independent, accredited test laboratory and documented in a test report prior to product launch. | High |
| SRS-ENV-0008 | The ingress-protection seal boundary **shall** be located on the interior side of the enclosure assembly such that it is not directly exposed on any externally accessible mating surface. | High |
| SRS-FUNC-0015 | The system **shall** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. | High |
| SRS-FUNC-0016 | The system **shall** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. | Medium |
| SRS-FUNC-0022 | The system **shall** include a behavior class label in every generated classification record. | Critical |
| SRS-FUNC-0025 | On the Max product variant, the system **shall** include the most recent GNSS fix in every generated classification record. | Medium |
| SRS-FUNC-0031 | The system **shall** normalize raw accelerometer data on-device prior to classification. | High |
| SRS-FUNC-0037 | The system **shall** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. | Medium |
| SRS-FUNC-0039 | The system **shall** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. | Medium |
| SRS-FUNC-0041 | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. | High |
| SRS-FUNC-0042 | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. | High |
| SRS-FUNC-0047 | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. | Critical |
| SRS-FUNC-0052 | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. | Critical |
| SRS-FUNC-0054 | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. | Critical |
| SRS-FUNC-0059 | The Mobile App **shall** notify the user when an OTA firmware update is available. | Medium |
| SRS-FUNC-0060 | The Mobile App **shall** display the current OTA update state reported by the device. | Medium |
| SRS-FUNC-0061 | The system **shall** produce a Software Bill of Materials for every OTA firmware release. | Medium |
| SRS-FUNC-0062 | The system **shall** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. | High |
| SRS-HW-0005 | The collar device **shall** provide a light-emitting-diode status indicator. | Medium |
| SRS-HW-0006 | The collar device enclosure **shall** provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. | High |
| SRS-HW-0007 | The Twist-Lock lug channels and magnetic insert on the device underside **shall not** penetrate the enclosure wall or the ingress seal path. | Critical |
| SRS-HW-0009 | The CCF body **shall** be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). | High |
| SRS-HW-0010 | The CCF material **shall** incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. | High |
| SRS-HW-0011 | The CCF **shall not** contain any metallic sub-component within the Zone 2 snap/breakaway region. | Critical |
| SRS-HW-0012 | Animal-contact surfaces of the device and CCF **shall not** use chrome or nickel plating. | High |
| SRS-HW-0013 | The collar device **shall** incorporate a three-axis MEMS accelerometer. | Critical |
| SRS-HW-0015 | The collar device accelerometer **shall** provide a wake-on-motion interrupt and a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. | High |
| SRS-HW-0016 | The Mini collar device **shall not** incorporate a GNSS receiver. | Medium |
| SRS-HW-0017 | The Max collar device **shall** incorporate a passive receive-only GNSS receiver. | High |
| SRS-HW-0018 | The collar device **shall** incorporate a Bluetooth Low Energy 5.x radio. | Critical |
| SRS-HW-0020 | The Mini collar device **shall** incorporate a battery cell of no less than 120 mAh nominal capacity. | High |
| SRS-HW-0021 | The Max collar device **shall** incorporate a battery cell of no less than 400 mAh nominal capacity. | High |
| SRS-HW-0025 | The collar device **shall** incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. | Critical |
| SRS-HW-0028 | The collar device compute subsystem **shall** provide direct-memory-access peripheral access and a hardware root of trust. | Critical |
| SRS-INT-0014 | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). | Critical |
| SRS-INT-0022 | The Mini collar variant shall not implement a GNSS interface. | Medium |
| SRS-INT-0031 | The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) shall use a 2-contact pogo-pin arrangement carrying VBUS and GND. | Critical |
| SRS-INT-0039 | The Twist-Lock mechanical interface shall use a 3-lug bayonet arrangement spaced at 120 degrees. | Critical |
| SRS-INT-0041 | The Twist-Lock lug ramp shall have a trapezoidal profile with an 8-degree self-locking angle. | High |
| SRS-INT-0042 | Each Twist-Lock lug shall be 4.0 mm wide by 1.2 mm thick. | High |
| SRS-INT-0043 | The Twist-Lock interface shall include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct engagement orientation. | High |
| SRS-INT-0052 | The system shall use a common device-enforced BLE application protocol shared across all collar and base-station firmware variants. | High |
| SRS-INT-0056 | The base station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. | High |
| SRS-MAINT-0001 | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. | High |
| SRS-MAINT-0002 | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetime defined by SRS-MAINT-0001. | Medium |
| SRS-MAINT-0003 | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported service lifetime defined by SRS-MAINT-0001. | High |
| SRS-OPER-0001 | A household deployment **shall** include at least one Base Station of the Charging tier. | Critical |
| SRS-OPER-0004 | The Max variant's GNSS smart power gate **shall not** be configurable by the owner. | High |
| SRS-OPER-0006 | The system **shall** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. | High |
| SRS-OPER-0007 | The Base Station **shall** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. | High |
| SRS-OPER-0008 | The Mobile App **shall** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. | High |
| SRS-OPER-0009 | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's species classifier profile. | Medium |
| SRS-OPER-0010 | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. | Medium |
| SRS-OPER-0011 | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. | Medium |
| SRS-OPER-0012 | The base station **shall** remain in a continuously powered, non-sleeping operational state for as long as AC power is supplied, maintaining active BLE scanning and Wi-Fi uplink capability at all times. | High |
| SRS-OPER-0013 | The base station **shall** be supplied with an AC-to-USB-C power adapter as an included accessory. | Medium |
| SRS-OPER-0014 | The Base Station (Charging) tier **shall** provide exactly 3 status LEDs, indicating at minimum: AC power presence, device-charging activity, and cloud-connectivity status. | High |
| SRS-OPER-0015 | The Base Station (Relay) tier **shall** provide exactly 2 status LEDs, indicating at minimum: AC power presence and cloud-connectivity status. | High |
| SRS-OPER-0016 | Every base station in a household deployment **shall** participate in a shared geo-fence mesh by independently reporting BLE sighting reports for every collar device within its range. | High |
| SRS-OPER-0017 | The collar device **shall** determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) readings from paired base stations in range, without reliance on any cloud-side determination. | High |
| SRS-OPER-0018 | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from HOME to AWAY only when no paired base station RSSI reading exceeds −85 dBm for 5 consecutive readings taken at 1 s intervals. | Medium |
| SRS-OPER-0019 | The collar device, while in Wellness Mode and not actively processing a motion-triggered confirmation burst, **shall** remain in its deepest available low-power idle state. | High |
| SRS-OPER-0020 | When the owner changes the Max collar variant's configured GNSS fix interval, the collar device **shall** apply the new interval no later than the start of the next scheduled fix-acquisition cycle. | Medium |
| SRS-OPER-0021 | Battery-life validation testing **shall** be performed using cells that have completed no fewer than 50 charge/discharge cycles prior to the validation measurement. | Medium |
| SRS-OPER-0022 | The collar device **shall** rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the base station has not had successful cloud contact for more than 24 hours, without requiring any additional fallback logic beyond the state machine's ... | Medium |
| SRS-OPER-0023 | The system's operational and durability requirements that reference an expected service lifetime **shall** use 2 years as the minimum testable floor, consistent with the Product Context Profile's user-confirmed ~2–3 year expected service lifetime figure. | Medium |
| SRS-OPER-0024 | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from AWAY to HOME only when at least one paired base station RSSI reading exceeds −80 dBm for 3 consecutive readings taken at 1 s intervals. | Medium |
| SRS-PERF-0005 | On the Max product variant, the system **shall** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. | Medium |
| SRS-PERF-0008 | The system **shall** allow the Twist-Lock mechanism to be engaged within 5 seconds. | Low |
| SRS-REG-0001 | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. | Critical |
| SRS-REG-0001 | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Body (TCB) prior to commercial distribution in the US market. \ | High |
| SRS-REG-0002 | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator emissions prior to commercial distribution. \ | High |
| SRS-REG-0003 | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the US market. \ | High |
| SRS-REG-0004 | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercial distribution in the US market. \ | High |
| SRS-REG-0005 | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is present above the applicable safe-harbor threshold, prior to commercial distribution in the US-CA market. \ | High |
| SRS-REG-0006 | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support FCC TCB certification (SRS-REG-0001) and NRTL listing (SRS-REG-0004) prior to submission for either certification. \ | High |
| SRS-REG-0007 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to commercial distribution in the US market. \ | High |
| SRS-REG-0008 | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen prior to commercial distribution in the Canada market. \ | High |
| SRS-REG-0009 | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to commercial distribution. \ | High |
| SRS-REG-0010 | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physical marking is impracticable, in an accessible electronic display, prior to commercial distribution in the Canada market. \ | High |
| SRS-REG-0011 | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — sufficient to support ISED certification (SRS-REG-0008) prior to submission. \ | High |
| SRS-REG-0012 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to commercial distribution in the Canada market. \ | High |
| SRS-REG-0013 | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identified in SRS-REG-0001 through SRS-REG-0012 applicable to that market are complete and on file. \ | High |
| SRS-REG-0014 | CE marking prerequisite for radio equipment. | Critical |
| SRS-REG-0016 | On device or packaging. | High |
| SRS-REG-0017 | GPSR 2023/988 Art 5/6. | Critical |
| SRS-REG-0018 | GPSR Art 4 / RED Art 11. | High |
| SRS-REG-0019 | In-scope interface obligation. | High |
| SRS-REG-0020 | 2011/65/EU + 2015/863. | High |
| SRS-REG-0021 | Per-member-state. | High |
| SRS-REG-0022 | Annex XVII. | High |
| SRS-REG-0023 | (EU) 2023/1542 Art 6. | Critical |
| SRS-REG-0025 | (EU) 2024/2847 Annex I + Art 13–14. | Critical |
| SRS-REG-0026 | (EU) 2016/679 + Art 30. | Critical |
| SRS-REG-0027 | PPWR. | Medium |
| SRS-REG-0028 | UK SI 2017/1206. | Critical |
| SRS-REG-0030 | UK establishment requirement. | High |
| SRS-REG-0031 |  | Critical |
| SRS-REG-0032 | UK GDPR + DPA 2018. | Critical |
| SRS-REG-0033 | UK REACH, UK RoHS, UK WEEE. | High |
| SRS-REG-0034 |  | Medium |
| SRS-REG-0035 |  | Critical |
| SRS-REG-0036 | AS/NZS 4268:2017. | High |
| SRS-REG-0037 | Precondition to RCM. | High |
| SRS-REG-0038 | In-market required. | High |
| SRS-REG-0039 | In-scope interface obligation. | High |
| SRS-REG-0042 | Lifetime obligation. | High |
| SRS-REG-0043 | Per-market minimum. | High |
| SRS-REG-0044 | Consolidating gate. | Critical |
| SRS-RELI-0001 | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. | Critical |
| SRS-RELI-0002 | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. | High |
| SRS-RELI-0003 | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. | High |
| SRS-RELI-0004 | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a base station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC... | High |
| SRS-SAFE-0006 | Upon fracture, the Zone 2 Fuse Tab **shall not** produce a detached fragment separate from the CCF body. | High |
| SRS-SAFE-0007 | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **shall** be blunt, presenting no sharp edge. | High |
| SRS-SAFE-0008 | The CCF **shall** present a visible fracture indicator upon Zone 2 breakaway. | High |
| SRS-SAFE-0013 | The device **shall not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. | Critical |
| SRS-SAFE-0021 | Materials in animal-skin contact **shall** be non-toxic. | High |
| SRS-SAFE-0022 | The system **shall** provide battery-ingestion warning labeling. | High |
| SRS-SEC-0004 | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. | Critical |
| SRS-SEC-0006 | The system shall have a public vulnerability-disclosure policy in place before product launch. | High |

## Verification Method: Analysis

_Requirements verified through modeling, simulation, calculation, or logical reasoning._

**Count:** 20 requirements

| Requirement ID | Statement | Priority |
| :--- | :--- | :--- |
| SRS-COMP-0021 | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applicable. | High |
| SRS-CONN-0026 | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. | Critical |
| SRS-ENV-0012 | The collar device enclosure material **shall** be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service lifetime. | Critical |
| SRS-FUNC-0057 | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. | Critical |
| SRS-INT-0015 | The BLE radio interface should undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4 GHz transmission. | Medium |
| SRS-INT-0030 | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. | Medium |
| SRS-OPER-0005 | The in-box Standard CCF **shall** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. | Medium |
| SRS-PERF-0001 | The system's Mini variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. | High |
| SRS-PERF-0002 | The system's Max variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval settings. | High |
| SRS-REG-0002 | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. | Critical |
| SRS-REG-0015 | Conditional on harmonised standard OJ listing. | High |
| SRS-REG-0024 | Deadline 18 Feb 2027. | Critical |
| SRS-REG-0029 | Conditional. | High |
| SRS-REG-0040 | RM-0009 UNCERTAIN. | High |
| SRS-REG-0041 | Threshold-contingent. | Medium |
| SRS-REG-0045 |  | High |
| SRS-REG-0046 |  | High |
| SRS-SAFE-0004 | If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **shall** be revised upward to 30 N. | Critical |
| SRS-SAFE-0018 | Materials in animal-skin contact on the device enclosure **shall** resist chew-induced damage. | Medium |
| SRS-SAFE-0019 | The CCF socket **shall** present no independent entrapment hazard when the device is absent. | High |

## Verification Method: Demonstration

_Requirements verified through witnessing of system operation in representative scenarios._

**Count:** 15 requirements

| Requirement ID | Statement | Priority |
| :--- | :--- | :--- |
| SRS-CONN-0027 | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. | Critical |
| SRS-CONN-0030 | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **shall** retry uploading the affected buffered classification record. | High |
| SRS-FUNC-0006 | The system **shall** operate in Wellness mode as its default power-optimized classification mode. | Critical |
| SRS-FUNC-0007 | The system **shall** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. | High |
| SRS-FUNC-0028 | The system **shall** generate and record classifications independently of the current BLE connectivity state. | Critical |
| SRS-FUNC-0033 | The system **shall** produce classification decisions without requiring a round-trip to a cloud service. | Critical |
| SRS-FUNC-0034 | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. | High |
| SRS-FUNC-0035 | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. | High |
| SRS-FUNC-0043 | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). | Critical |
| SRS-FUNC-0044 | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). | Critical |
| SRS-FUNC-0048 | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. | High |
| SRS-INT-0032 | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. | Critical |
| SRS-INT-0037 | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. | High |
| SRS-INT-0048 | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. | Medium |
| SRS-INT-0050 | The Twist-Lock interface shall be operable without tools. | High |

---

## Requirements Traceability Matrix (RTM)

The full RTM is reproduced below from the Master SRS traceability artifacts.

### RTM Part A (§1–§4)

| Req-ID | Title | Source Tags | Section | Status | Verification Method |
| :--- | :--- | :--- | :--- | :--- | :--- |

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
| SRS-FUNC-0033 | No cloud round-trip for classification | [PRD §7.7] | §3 | APPROVED | Demonstration |
| SRS-FUNC-0034 | Tier-2 via OTA | [PRD §7.9] | §3 | APPROVED | Demonstration |
| SRS-FUNC-0035 | Tier-2 no HW mod | [PRD §7.9] | §3 | APPROVED | Demonstration |
| SRS-FUNC-0036 | Apply Scratching threshold | [PRD §7.8] | §3 | APPROVED | Test |
| SRS-FUNC-0037 | Scratching FW-default threshold | [PRD §7.8] | §3 | APPROVED | Inspection |
| SRS-FUNC-0038 | Apply Shaking threshold | [PRD §7.8] | §3 | APPROVED | Test |
| SRS-FUNC-0039 | Shaking FW-default threshold | [PRD §7.8] | §3 | APPROVED | Inspection |
| SRS-FUNC-0040 | Thresholds persist across OTA | [PRD §7.8] | §3 | APPROVED | Test |
| SRS-FUNC-0041 | App Scratching threshold UI | [EXTERNAL: Mobile App team] | §3 | APPROVED | Inspection-ext |
| SRS-FUNC-0042 | App Shaking threshold UI | [EXTERNAL: Mobile App team] | §3 | APPROVED | Inspection-ext |
| SRS-CONN-0001 | BLE Collar peripheral | [PRD §6.3] | §4 | APPROVED | Inspection |
| SRS-CONN-0002 | BLE Base central | [PRD §6.3] | §4 | APPROVED | Inspection |
| SRS-CONN-0003 | QR OOB pairing | [PRD §6.3] | §4 | APPROVED | Demonstration |
| SRS-CONN-0004 | Default adv 60 s | [PRD §6.3] | §4 | APPROVED | Test |
| SRS-CONN-0005 | Adv range 1–180 s | [PRD §6.3] | §4 | APPROVED | Test |
| SRS-CONN-0006 | BLE range ≥9 m | [PRD §6.3] | §4 | APPROVED | Test |
| SRS-CONN-0007 | TX ≥+8 dBm | [PRD §6.3] | §4 | APPROVED | Test |
| SRS-CONN-0008 | BLE addr randomization | [PRD §6.3] | §4 | APPROVED | Test |
| SRS-CONN-0009 | Secured BLE link (§8) | [PRD §6.3] | §4 | APPROVED | Inspection |
| SRS-CONN-0010 | Auto-reconnect on range re-entry | [PRD §6.4],[PRD §8.5] | §4 | APPROVED | Test |
| SRS-CONN-0011 | Record forwarding on BLE contact | [PRD §8],[PRD §6.4] | §4 | APPROVED | Test |
| SRS-CONN-0012 | Best-effort event-triggered transport | [PRD §8.5] | §4 | APPROVED | Inspection |
| SRS-CONN-0013 | Sync resumption after reconnection | [PRD §8],[PRD §8.5] | §4 | APPROVED | Test |
| SRS-CONN-0014 | Base upload records to cloud | [PRD §8],[PRD §6.5] | §4 | APPROVED | Test |
| SRS-CONN-0015 | Base buffer on upload-path unavailable | [PRD §8.5] | §4 | APPROVED | Test |
| SRS-CONN-0016 | Upload buffered on path restoration | [PRD §8.5] | §4 | APPROVED | Test |
| SRS-CONN-0017 | No discard pending upload | [PRD §8.5] | §4 | APPROVED | Test |
| SRS-CONN-0018 | Cloud accept and ack uploads | [EXTERNAL: IoT Cloud backend team] | §4 | APPROVED | Inspection-ext |
| SRS-CONN-0019 | Forward to any in-range paired base | [PRD §4.2],[PRD §8] | §4 | APPROVED | Test |
| SRS-CONN-0020 | Forward to first available base only | [PRD §4.2],[PRD §8] | §4 | APPROVED | Test |
| SRS-CONN-0021 | Cloud-side dedup of multi-base uploads | [EXTERNAL: IoT Cloud backend team] | §4 | APPROVED | Inspection-ext |
| SRS-CONN-0022 | Device-side Insight activation on command | [PRD §7.1],[PRD §6.4] | §4 | APPROVED | Test |
| SRS-CONN-0023 | App Insight activation command | [EXTERNAL: Mobile App team] | §4 | APPROVED | Inspection-ext |
| SRS-CONN-0024 | Location-tagged records via standard path | [PRD §7.5],[PRD §8] | §4 | APPROVED | Test |
| SRS-CONN-0025 | Sync last GNSS fix during home power-gate | [PRD §7.5],[PRD §6.3] | §4 | APPROVED | Test |
| SRS-CONN-0026 | No record loss any connectivity-loss | [PRD §8.5] | §4 | APPROVED | Analysis |
| SRS-CONN-0027 | Continue classification during BLE loss | [PRD §7.6],[PRD §8.5] | §4 | APPROVED | Demonstration |
| SRS-CONN-0028 | Degraded-mode entry below Wi-Fi bound | [ASSUMPTION: A-0009] | §4 | APPROVED | Test |
| SRS-CONN-0029 | Degraded-mode exit on Wi-Fi restoration | [ASSUMPTION: A-0009] | §4 | APPROVED | Test |
| SRS-CONN-0030 | Base upload retry on transient failure | [PRD §8.5] | §4 | APPROVED | Demonstration |

### RTM Part B (§5–§10)

| Req-ID | Title | Source Tags | Section | Status | Verification Method |
| :--- | :--- | :--- | :--- | :--- | :--- |
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
| SRS-PERF-0008 | CCF Twist-Lock Engagement Time Ceiling (≤5 s) | [PRD §12.1] | §6 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0001 | CCF-S Zone 2 Breakaway Force Window (Feline) 15-20 N | [PRD §10.1.3.2b],[PRD §13.2],[STD: EU GPSR],[ASSUMPTION: A-0017] | §7 | APPROVED | GPSR 2023/988 (RM-0024/RM-0031) | — | PASS/MARGINAL/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0002 | CCF-M Zone 2 Breakaway Force Window (Canine Med) 20-28 N | [PRD §10.1.3.2b],[PRD §13.2],[STD: EU GPSR],[ASSUMPTION: A-0017],[ASSUMPTION: A-0020] | §7 | APPROVED | GPSR 2023/988 (RM-0024/RM-0031) | — | PASS/MARGINAL/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0003 | CCF-L Zone 2 Breakaway Force Window (Canine Lg) 28-40 N | [PRD §10.1.3.2b],[PRD §10.1.4],[PRD §13.2],[STD: EU GPSR],[ASSUMPTION: A-0017],[ASSUMPTION: A-0020] | §7 | APPROVED | GPSR 2023/988 (RM-0024/RM-0031) | — | PASS/MARGINAL/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0004 | CCF-L Force-Window Contingency >26 g → floor 30 N | [PRD §10.1.4] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-SAFE-0005 | Zone 2 Single-Use Restriction | [PRD §10.1.3.2b],[PRD §13.2] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0006 | Zone 2 No-Detached-Fragment on Fracture | [PRD §10.1.3.2b] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SAFE-0007 | Zone 2 Post-Fracture Surface Bluntness | [PRD §10.1.3.2b] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SAFE-0008 | Zone 2 Visible Fracture Indicator | [PRD §10.1.3.2b],[PRD §13.2] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SAFE-0009 | Zone 1 Structural Retention Force ≥50 N | [PRD §10.1.3.1],[PRD §10.1.3.4],[PRD §13.2] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0010 | Zone 1 Survival Through Zone 2 Fracture | [PRD §10.1.3.1] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0011 | Twist-Lock Axial Retention Force >100 N | [PRD §10.1.3.1] | §7 | APPROVED | — | CR-0009 | PASS/PASS/PASS/PASS/PASS | Test | in-scope; Priority→CRITICAL per CR-0009 |
| SRS-SAFE-0012 | Twist-Lock Retention Under 50 g Pet-Motion Inertial Loading | [PRD §10.1.3.2a] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0013 | No-Wear-Without-Intact-Zone-2 | [PRD §10.1.3.6] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SAFE-0014 | Device Separation-Signature Emission | [PRD §10.1.3.6] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0015 | [EXTERNAL] CCF-Replacement-Required Notification | [PRD §10.1.3.6],[EXTERNAL: Mobile App team] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection (external conformance evidence) | EXTERNAL |
| SRS-SAFE-0016 | Zone 2 Non-Fracture Under Chew-Compressive Load <250 N | [PRD §13.2] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0017 | CCF Body Chew-Penetration Resistance ≥30 s @250 N | [PRD §13.2] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0018 | Device Enclosure Chew Resistance (qualitative) | [PRD §10.1.2],[PRD — ABSENT] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-SAFE-0019 | Device-Absent Socket Entrapment-Hazard Avoidance (qualitative) | [PRD §10.1.3.5],[PRD §13.2] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-SAFE-0020 | Device-Absent Socket Probe-Clearance Criterion (12 mm) | [PRD §10.1.3.5],[ASSUMPTION: A-0010] | §7 | APPROVED | — | — | PASS/MARGINAL/PASS/PASS/PASS | Test | in-scope |
| SRS-SAFE-0021 | Animal-Contact Material Non-Toxicity | [PRD §10.1.2],[PRD §13.2] | §7 | APPROVED | REACH/RoHS/Prop 65 → §17 (RM-0026) | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SAFE-0022 | Battery-Ingestion Warning Labeling | [PRD §13.2],[ASSUMPTION: A-0011] | §7 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SEC-0001 | BLE Link-Layer AES-128 CCM Encryption | [PRD §6.3],[PRD §6.7],[PRD §8.2],[PRD §12.3],[STD: RM-0019] | §8 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SEC-0002 | LE Secure Connections Pairing | [PRD §6.3],[PRD §6.7],[PRD §12.3],[STD: RM-0019] | §8 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SEC-0003 | TLS 1.3 Exclusivity for All Base-to-Cloud Transport | [PRD §6.5],[PRD §11.2],[PRD §12.3],[STD: RM-0019] | §8 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-SEC-0004 | Unique Cryptographic Identity at Manufacturing | [PRD §12.3],[STD: RM-0019] | §8 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-SEC-0005 | Secure Boot with Hardware Root of Trust | [PRD §12.3],[PRD §10.7],[STD: RM-0019] | §8 | APPROVED | ETSI EN 303 645:2025 (RM-0019) | — | PASS/PASS/MARGINAL/PASS/PASS | Test | in-scope; DVT watch |
| SRS-SEC-0006 | Public Vulnerability-Disclosure Policy Before Launch | [PRD §12.3],[PRD §13.5],[STD: RM-0019],[STD: RM-0021] | §8 | APPROVED | RM-0019; RM-0021 | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-DATA-0001 | Classification Record Content | [PRD §7.5] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0002 | Confidence Score Bound | [PRD §7.5] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0003 | Record Timestamp Accuracy | [PRD §7.5] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0004 | GNSS Context on Max Variant | [PRD §7.5] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0005 | On-Device Storage Duration | [PRD §7.5],[PRD §10.6] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0006 | Retention Through Power Loss | [PRD §10.6] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0007 | Storage Corruption Detection | [PRD §10.6] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0008 | Classification Independent of Connectivity | [PRD §7.6] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0009 | Record Forwarding Without Corruption | [PRD §7.6] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0010 | Record Forwarding Without Sequence Loss | [PRD §7.6] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0011 | Raw Sensor Data Transmission Boundary | [PRD §7.7] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0012 | On-Device Normalization | [PRD §7.7] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-DATA-0013 | No Cloud Round-Trip for Classification | [PRD §7.7] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-DATA-0014 | Raw Sample Retention Minimization | [PRD §7.7],[STD: RM-0015] | §9 | APPROVED | GDPR Art.25 (RM-0015) | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-DATA-0015 | Buffered Data Retention Until Acknowledgement | [PRD §8.4] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref CONN-0008 |
| SRS-DATA-0016 | No Buffer Clear on Disconnect Alone | [PRD §8.4] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref CONN-0010 |
| SRS-DATA-0017 | Stale-Data Flag on Delayed Upload | [PRD §8.7] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0018 | Data Minimization for Personal Data | [STD: RM-0015],[STD: RM-0016],[STD: RM-0018] | §9 | APPROVED | RM-0015; RM-0016; RM-0018 | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-DATA-0019 | Purpose Limitation | [STD: RM-0015],[STD: RM-0016],[STD: RM-0018] | §9 | APPROVED | RM-0015; RM-0016; RM-0018 | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-DATA-0020 | On-Device Data Deletion Support | [STD: RM-0015],[STD: RM-0016],[STD: RM-0019] | §9 | APPROVED | RM-0015; RM-0016; RM-0019 | — | MARGINAL/PASS/PASS/PASS/PASS | Demonstration | in-scope; D1-MARGINAL |
| SRS-DATA-0021 | On-Device Data Access Support | [STD: RM-0015],[STD: RM-0016],[STD: RM-0018] | §9 | APPROVED | RM-0015; RM-0016; RM-0018 | — | MARGINAL/PASS/PASS/PASS/PASS | Demonstration | in-scope; D1-MARGINAL |
| SRS-DATA-0022 | Consumer Privacy Rights Contingency (CCPA/CPRA) | [STD: RM-0017] | §9 | APPROVED | CCPA/CPRA INDICATIVE (RM-0017) | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope; contingent |
| SRS-DATA-0023 | Data-at-Rest Encryption | [STD: RM-0015],[STD: RM-0019] | §9 | APPROVED | RM-0015; RM-0019 | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-DATA-0024 | Transport to Cloud Device-Management Layer | [PRD §6.1],[ASSUMPTION: A-0015] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0025 | Breakaway Record Commit Timing | [ASSUMPTION: A-0018] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0026 | Breakaway Record Survivability | [ASSUMPTION: A-0018] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-DATA-0027 | Breakaway Record Transmission Trigger | [ASSUMPTION: A-0018] | §9 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0001 | Collar BLE Peripheral Role | [PRD §6.3], [PRD §8.1], [PRD §10.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0002 | Base Station BLE Central Role | [PRD §11.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0003 | Minimum Concurrent Collar Sessions | [PRD §8.1], [PRD §11.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0004 | Default BLE Advertising Interval | [PRD §6.3], [PRD §8.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0005 | Configurable BLE Advertising Interval Range | [PRD §8.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0006 | Advertising Continuity During Active Connection | [PRD §8.1], [PRD §10.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0007 | BLE Address Randomization | [PRD §8.1], [PRD §10.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0008 | Minimum BLE Transmit Power | [PRD §10.3] | §10 | APPROVED | — | CR-0018 (XSC-0009) | PASS/PASS/PASS/PASS/PASS | Test | in-scope; back-XR→HW-0019 per CR-0018 |
| SRS-INT-0009 | Minimum BLE Open-Air Range | [PRD §10.3], [PRD §12.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0010 | BLE Link-Layer Encryption Algorithm | [PRD §6.3], [PRD §8.2], [PRD §10.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0011 | BLE Pairing via LE Secure Connections | [PRD §6.3], [PRD §8.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0012 | QR Out-of-Band Pairing Mechanism | [PRD §6.3], [PRD §8.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0013 | BLE Radio Regulatory Conformance | [PRD §13.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0014 | Bluetooth SIG Qualification | [STD: Bluetooth SIG Qualification (QDID)], [PRD §13.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0015 | RF Human-Exposure Assessment | [PRD §13.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-INT-0016 | Wi-Fi Radio Band and Standard | [PRD §4.2], [PRD §6.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0017 | Cloud Uplink Transport Encryption | [PRD §6.5], [PRD §11.2], [PRD §12.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0018 | Default Access-Point Configuration Compatibility | [PRD §12.6] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0019 | Minimum Wi-Fi Uplink Signal Condition | [ASSUMPTION A-0009] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0020 | Wi-Fi Radio Regulatory Conformance | [PRD §13.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0021 | GNSS Interface Presence on Max | [PRD §4.1], [PRD §10.2.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0022 | GNSS Interface Absence on Mini | [PRD §4.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0023 | Configurable GNSS Fix Interval Range | [PRD §4.1], [PRD §10.2.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0024 | Default GNSS Fix Interval | [PRD §4.1], [PRD §10.2.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0025 | A-GPS Assistance Data Delivery | [PRD §10.2.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0026 | A-GPS Assistance Data Validity Window | [PRD §10.2.2] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0027 | GNSS Power Gating During HOME State | [PRD §10.2.2], [PRD §6.4], [ASSUMPTION A-0016] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0028 | GNSS Fix Acquisition Timeout | [PRD §10.2.2], [PRD §15.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0029 | Warm GNSS Time-to-First-Fix Ceiling | [PRD §12.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0030 | GNSS Intentional-Radiator Exemption Status | [PRD §13.1] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope |
| SRS-INT-0031 | Pogo-Pin Contact Count and Function | [PRD §10.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0032 | Magnetic Charging Alignment | [PRD §6.6], [PRD §10.5] | §10 | APPROVED | — | CR-0019 (XSC-0010) | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; Priority→CRITICAL per CR-0019 |
| SRS-INT-0033 | First-Attempt Docking Seating Rate | [PRD §10.1.3.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0034 | Full-Charge Time Ceiling | [PRD §10.5], [PRD §12.4] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0035 | IP67 Rating When Undocked | [PRD §6.6], [PRD §10.5], [PRD §13.4] | §10 | APPROVED | — | CR-0016 (XSC-0007) | PASS/PASS/PASS/PASS/PASS | Test | in-scope; back-XR→HW-0004 per CR-0016 |
| SRS-INT-0036 | Charging Socket Self-Drainage | [PRD §10.5], [PRD §10.1.3.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0037 | Charging-Access Removal Rotation | [PRD §6.6], [PRD §10.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-INT-0038 | Device-Absent Socket Entrapment Geometry | [ASSUMPTION A-0010], [PRD §10.1.3.5] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0039 | Bayonet Lug Configuration | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0040 | Lock/Unlock Rotation Angle | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0041 | Lug Ramp Self-Locking Profile | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0042 | Twist-Lock Lug Dimensions | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0043 | Asymmetric Keying Lug | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0044 | Detent Release Torque Window | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0045 | Twist-Lock Axial Retention Floor | [PRD §10.1.3.1], [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0046 | Twist-Lock Engagement Insertion Force Ceiling | [PRD §10.1.1], [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0047 | Twist-Lock Engagement Rotation Torque Ceiling | [PRD §10.1.1], [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0048 | Engagement Feedback | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-INT-0049 | Magnetic Engagement Assist Range | [PRD §10.1.3.2a] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0050 | Tool-Free Twist-Lock Operation | [PRD §10.1.3.2a], [PRD §12.4] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope |
| SRS-INT-0051 | Twist-Lock Engagement Time Ceiling | [PRD §12.1], [PRD §12.4] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0052 | Common Device-Enforced Protocol Across Variants | [PRD §4.3], [ASSUMPTION A-0001] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0053 | Payload Type — Behavioral Classification Record | [PRD §7.5], [PRD §8.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0054 | Payload Type — BLE Sighting Report | [PRD §8.5], [PRD §11.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0055 | Payload Type — Cloud Downlink | [PRD §8.6] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0056 | Base Station Payload Content Opacity | [PRD §8.3] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-INT-0057 | Collar Buffer Retention Pending Acknowledgment | [PRD §8.4] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0058 | No FIFO Clear on Disconnect Alone | [PRD §8.4] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0059 | Sequence-Loss Detection | [PRD §7.6] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-INT-0060 | Corruption-Free Record Forwarding | [PRD §7.6] | §10 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |


| SRS-RELI-0001 | IP67 Rating Retention Over Full Service Lifetime | [PRD §12.2] | §13 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope; CRITICAL; xref SRS-HW-0003,SRS-ENV-0005,SRS-ENV-0006 |
| SRS-RELI-0002 | Collar Device Operational Availability | [PRD §12.2] | §13 | APPROVED | — | — | PASS/MARGINAL/PASS/PASS/PASS | Test | in-scope; HIGH; MARGINAL D4: measurement window absent; xref SRS-HW-0025,SRS-INT-0031,SRS-INT-0032 |
| SRS-RELI-0003 | Base Station Uptime | [PRD §12.2] | §13 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; HIGH; 99.5% over rolling 90-day window |
| SRS-RELI-0004 | OTA Update Success Rate | [PRD §12.2] | §13 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; HIGH; xref SRS-FUNC-0055,SRS-FUNC-0056,SRS-FUNC-0057 |

| SRS-ENV-0001 | Device Operating Temperature Range | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0002 | Device Storage Temperature Range | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0003 | CCF Thermal-Cycling Exposure | [PRD §12.5], [ASSUMPTION: A-0003] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0004 | Device Damp-Heat Exposure | [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0005 | Prohibition on IP67 Claims for CCF-Mated Configuration | [PRD §4.1 fn²], [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-ENV-0006 | Independent Laboratory Confirmation of IP67 Rating | [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-ENV-0007 | Twist-Lock Channel Water-Ingress Exclusion | [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0008 | Ingress Seal-Boundary Interior Placement | [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-ENV-0009 | Drop Survival | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0010 | Mechanical Shock Resistance | [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0011 | Vibration Resistance | [PRD §13.4] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0012 | Enclosure UV Stabilization | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/MARGINAL/MARGINAL/PASS | Analysis | in-scope |
| SRS-ENV-0013 | CCF UV Aging Exposure | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0014 | CCF Chemical-Fluid Exposure | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0015 | Post-Thermal-Cycling Zone 2 Fuse-Force Window Retention | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0016 | Post-Thermal-Cycling Twist-Lock Detent-Torque Window Retention | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0017 | Post-UV-Aging Zone 2 Fuse-Force Window Retention | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-ENV-0018 | Post-Chemical-Exposure Zone 2 Fuse-Force Window Retention | [PRD §12.5] | §12 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-UX-0001 | BLE pairing + first sync within 3 min of user initiating pairing mode | [PRD §12.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-UX-0002 | QR-code OOB pairing as primary method (LE Secure Connections) | [PRD §5.6] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Demonstration | in-scope; xref SRS-CONN-0003 (§4) |
| SRS-UX-0003 | Single physical mechanism (button) to initiate pairing mode | [PRD §5.6] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope |
| SRS-UX-0004 | Distinct pairing-mode LED indication distinguishable from all other states | [PRD §5.6] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref SRS-UX-0012/0013 (§14.3); MODIFIED v3→v4 (CR-0024) |
| SRS-UX-0005 | Auto-exit pairing mode after 3 min with no pairing completion | [PRD §5.6] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-UX-0006 | Audible click + tactile detent on Twist-Lock engagement | [PRD §10.1.3.2a] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0007 | Magnetic-assist alignment force ≤5 mm before lug channel engagement | [PRD §10.1.3.2a] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0008 | Twist-Lock engage ≤5 N axial + ≤0.10 N·m rotational torque | [PRD §10.1.3.2a] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0009 | Twist-Lock removal ≤0.15 N·m detent-release torque | [PRD §10.1.3.2a] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0010 | ≥90% first-attempt pogo-pin charging seating rate (≥20 participants) | [PRD §10.1.3.5] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0011 | Asymmetric lug keying prevents incorrect-orientation insertion (poka-yoke) | [PRD §10.1.3.2a] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0012 | LED communicates 7 operational states: boot, pairing, normal, low-bat, charging, fault, OTA | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; master LED-state list; xref UX-0013/0014/0022/0023/0028 |
| SRS-UX-0013 | Each operational state = unique LED color/blink-cadence/duty-cycle pattern | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref SRS-UX-0012; priority MEDIUM→HIGH per CR-0023; MODIFIED v3→v4 (CR-0023) |
| SRS-UX-0014 | Critical/non-critical state differentiation via temporal pattern (colorblind-accessible) | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Analysis | in-scope; colorblind-accessibility; xref SRS-UX-0012 |
| SRS-UX-0015 | Twist-Lock engagement click ≥40 dBA at 30 cm (ambient ≤30 dBA) | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §11 (COMP-HW) |
| SRS-UX-0016 | Base station LEDs: AC power, charging, cloud-connected, OTA in progress | [PRD §11.6] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-UX-0017 | Base station LED auto-dimming <50 lux or user-configurable quiet-hours (should) | [PRD §11.6],[ASSUMPTION: A-0008] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; should (recommended); xref A-0008 |
| SRS-UX-0018 | Base station initial setup ≤5 min (Wi-Fi + cloud registration) | [PRD §12.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref A-0009 (Wi-Fi assumption) |
| SRS-UX-0019 | CCF variant visual/tactile differentiation (size, color, or texture) | [PRD §12.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; CCF variant differentiation |
| SRS-UX-0020 | CCF Zone 1 clamp install ≤60 s without tools (wrap-and-lock) | [PRD §12.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-UX-0021 | CCF Zone 2 visible fracture indicator discernible at 60 cm without magnification | [PRD §10.1.3.2b],[PRD §10.1.3.6] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Inspection | in-scope; xref SRS-SAFE-0008 (§7); CR-0022; VM Test→Inspection per V-Method v2 |
| SRS-UX-0022 | Distinct low-battery LED at ≤20% SoC, persists until charging confirmed | [PRD §10.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref SRS-UX-0012/0013 (§14.3); low-battery = ≤20% SoC |
| SRS-UX-0023 | Distinct fault-state LED pattern (sensor fail, NVM corruption, BLE init fail) | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref SRS-UX-0012/0013 (§14.3); MODIFIED v3→v4 (CR-0024) |
| SRS-UX-0024 | Confirmation feedback (LED/haptic) within 1 s of user physical action | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |
| SRS-UX-0025 | Battery SoC % (0–100) in every sync payload for app display | [PRD §12.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; interface obligation → EXTERNAL: Mobile App team |
| SRS-UX-0026 | GNSS fix interval in status payload every sync (Max variant, app battery estimate) | [PRD §12.4] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; Max variant only; interface obligation → EXTERNAL: Mobile App team |
| SRS-UX-0027 | Breakaway event record with elevated TX priority on next base contact | [PRD §10.1.3.6],[PRD §12.4],[ASSUMPTION: A-0018] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; secondary to UX-0021; xref A-0018, SRS-UX-0021 |
| SRS-UX-0028 | Distinct LED pattern per OTA state (Download/Verify/Pending/Install/Success/Fail) | [PRD §9.5] | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope; xref §5 (OTA functional states) |
| SRS-UX-0029 | LED continuously active during OTA; no dark period >10 s in states >30 s | — | §14 | APPROVED | — | — | PASS/PASS/PASS/PASS/PASS | Test | in-scope |

### RTM §15 — Operational Requirements

| RTM Row # | SRS ID | SRS Requirement Summary | PRD Source(s) | Parent Req(s) | Notes |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 284 | SRS-OPER-0012 | Base Station Continuous Operational Posture | [PRD §11.7] | SRS-RELI-0003 | in-scope; mains-powered always-on |
| 285 | SRS-OPER-0013 | AC Power Adapter Inclusion | [PRD §11.7] | — | in-scope; included accessory |
| 286 | SRS-OPER-0014 | Charging-Tier Base Station LED Inventory | [PRD §11.6], [PRD §4.2] | SRS-OPER-0015, SRS-UX-0016 | in-scope; 3-LED charging tier |
| 287 | SRS-OPER-0015 | Relay-Tier Base Station LED Inventory | [PRD §11.6], [PRD §4.2] | SRS-OPER-0014, SRS-UX-0016 | in-scope; 2-LED relay tier |
| 288 | SRS-OPER-0016 | Multi-Base Household Geo-Fence Mesh Participation | [PRD §4.2], [PRD §5.3] | SRS-INT-0054, SRS-CONN-0019 | in-scope; mesh sighting reports |
| 289 | SRS-OPER-0017 | Device-Local Home/Away State Machine | [PRD §6.4], [PRD §4.1], [A-0016] | SRS-INT-0027, SRS-OPER-0004, SRS-PERF-0007, SRS-OPER-0011 | in-scope; RSSI-based local authority |
| 290 | SRS-OPER-0018 | Device-Local Home-to-Away RSSI Transition Threshold | [PRD §6.4], [PRD §4.1], [A-0022] | SRS-OPER-0017, SRS-OPER-0024 | in-scope; −85 dBm / 5-reading debounce |
| 291 | SRS-OPER-0019 | Wellness-Mode Deep-Sleep Idle State | [PRD §15.2], [PRD §7.3] | SRS-FUNC-0011, SRS-FUNC-0010 | in-scope; deepest-sleep policy |
| 292 | SRS-OPER-0020 | GNSS Fix-Interval Change Application Timing | [PRD §15.5] | SRS-INT-0023, SRS-INT-0024 | in-scope; apply within next cycle |
| 293 | SRS-OPER-0021 | Battery Cell Cycle-Life Validation Basis | [PRD §15.6] | SRS-PERF-0001, SRS-PERF-0002 | in-scope; ≥50-cycle precondition |
| 294 | SRS-OPER-0022 | Device-Local Fallback Authority on Extended Cloud Loss | [PRD §6.4] | SRS-OPER-0017, SRS-OPER-0011 | in-scope; no extra fallback logic |
| 295 | SRS-OPER-0023 | Expected Product Service Lifetime Reference Figure | [PRD — ABSENT] | SRS-RELI-0001 | in-scope; 2-year floor reference |
| 296 | SRS-OPER-0024 | Device-Local Away-to-Home RSSI Hysteresis Threshold | [PRD §6.4], [PRD §4.1], [A-0022] | SRS-OPER-0017, SRS-OPER-0018 | in-scope; −80 dBm / 3-reading hysteresis |

### RTM §16 — Maintainability

| Req-ID | Title | Source Tags | Section | Status | Verification Method | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SRS-MAINT-0001 | OTA-Update Capability Availability Through Supported Service Lifetime | [PRD §12.7] | §16 | APPROVED | Inspection | in-scope |
| SRS-MAINT-0002 | SBOM Currency Maintenance Across Supported Service Lifetime | [PRD §12.7], [PRD §9.5] | §16 | APPROVED | Inspection | in-scope |
| SRS-MAINT-0003 | Post-Launch Vulnerability-Disclosure Process Maintenance | [PRD §12.7], [STD: RM-0021] | §16 | APPROVED | Inspection | in-scope |

### RTM §17 — Standards Conformance (24 rows)

Covering COMP-0005 through COMP-0028. Full 24 rows in Master SRS traceability artifacts. Refer to `traceability/rtm-17-add-row.md` for complete table.

### RTM §18 — Regulatory Certification & Market Pathways

| Req-ID | Title | Section | Status | Verification | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REG-0001 | FCC Part 15 Subpart C Certification Hold (US) | §18 | APPROVED | Inspection | In-scope |
| REG-0002 | FCC Part 15 Subpart B SDoC (US) | §18 | APPROVED | Inspection | In-scope |
| REG-0003 | FCC Identifier Marking (US) | §18 | APPROVED | Inspection | In-scope |
| REG-0004 | NRTL Listing Hold for Base Station (US) | §18 | APPROVED | Inspection | In-scope |
| REG-0005 | California Proposition 65 Warning Labeling (US-CA) | §18 | APPROVED | Inspection | In-scope |
| REG-0006 | Certification Documentation Package (US) | §18 | APPROVED | Inspection | In-scope |
| REG-0007 | GNSS Exemption Determination (US) | §18 | APPROVED | Analysis | In-scope |
| REG-0008 | ISED Certification Hold (Canada) | §18 | APPROVED | Inspection | In-scope |
| REG-0009 | ISED ICES-003 Compliance (Canada) | §18 | APPROVED | Inspection | In-scope |
| REG-0010 | Innovation Canada Identifier Marking (Canada) | §18 | APPROVED | Inspection | In-scope |
| REG-0011 | Certification Documentation Package (Canada) | §18 | APPROVED | Inspection | In-scope |
| REG-0012 | GNSS Exemption Determination (Canada) | §18 | APPROVED | Analysis | In-scope |
| REG-0013 | Pre-Launch Certification-Status Gate (US + Canada) | §18 | APPROVED | Inspection | In-scope |
| REG-0014 | RED 2014/53/EU Declaration of Conformity | §18 | APPROVED | Inspection | In-scope |
| REG-0015 | EU Notified Body Engagement Applicability | §18 | APPROVED | Analysis | In-scope |
| REG-0016 | CE Marking Physical Application | §18 | APPROVED | Inspection | In-scope |
| REG-0017 | EU GPSR General Product Safety Compliance | §18 | APPROVED | Inspection | In-scope |
| REG-0018 | EU Authorized Representative Designation | §18 | APPROVED | Inspection | In-scope |
| REG-0019 | EU Technical Documentation File Availability | §18 | APPROVED | Inspection | In-scope |
| REG-0020 | RoHS Self-Declaration | §18 | APPROVED | Inspection | In-scope |
| REG-0021 | WEEE Producer Registration | §18 | APPROVED | Inspection | In-scope |
| REG-0022 | REACH SVHC Declaration | §18 | APPROVED | Inspection | In-scope |
| REG-0023 | EU Battery Regulation Labelling and CE Marking | §18 | APPROVED | Inspection | In-scope |
| REG-0024 | EU Battery Regulation Art 11 Removability Exemption | §18 | APPROVED | Analysis | In-scope |
| REG-0025 | EU Cyber Resilience Act Compliance Declaration | §18 | APPROVED | Inspection | In-scope |
| REG-0026 | GDPR Compliance Basis | §18 | APPROVED | Inspection | In-scope |
| REG-0027 | EU PPWR Compliance Declaration | §18 | APPROVED | Inspection | In-scope |
| REG-0028 | UKCA Marking Declaration | §18 | APPROVED | Inspection | In-scope |
| REG-0029 | UK Approved Body Engagement Applicability | §18 | APPROVED | Analysis | In-scope |
| REG-0030 | UK Responsible Person Designation | §18 | APPROVED | Inspection | In-scope |
| REG-0031 | UK PSTI Act 2022 Compliance Declaration | §18 | APPROVED | Inspection | In-scope |
| REG-0032 | UK GDPR Compliance Basis | §18 | APPROVED | Inspection | In-scope |
| REG-0033 | UK Materials and Environmental Compliance | §18 | APPROVED | Inspection | In-scope |
| REG-0034 | UK Producer Responsibility Packaging Compliance | §18 | APPROVED | Inspection | In-scope |
| REG-0035 | Pre-Launch Certification-Status Gate (EU + UK) | §18 | APPROVED | Inspection | In-scope |
| REG-0036 | RCM Marking Declaration (AU/NZ) | §18 | APPROVED | Inspection | In-scope |
| REG-0037 | ACMA Supplier Code Registration | §18 | APPROVED | Inspection | In-scope |
| REG-0038 | AU/NZ Responsible Supplier Designation | §18 | APPROVED | Inspection | In-scope |
| REG-0039 | AU/NZ Certification Documentation Package | §18 | APPROVED | Inspection | In-scope |
| REG-0040 | GNSS Exemption Determination (AU/NZ) | §18 | APPROVED | Analysis | In-scope |
| REG-0041 | CCPA/CPRA Contingent Market-Access Declaration | §18 | APPROVED | Analysis | In-scope |
| REG-0042 | Post-Certification Regulatory-Change Monitoring | §18 | APPROVED | Inspection | In-scope |
| REG-0043 | Certification and DoC Archival Retention | §18 | APPROVED | Inspection | In-scope |
| REG-0044 | Pre-Launch Certification-Status Gate (All Markets) | §18 | APPROVED | Inspection | In-scope |
| REG-0045 | GNSS Exemption Determination (EU) | §18 | APPROVED | Analysis | In-scope |
| REG-0046 | GNSS Exemption Determination (UK) | §18 | APPROVED | Analysis | In-scope |

---

## Coverage Notes

- **Requirements catalogued:** 364 requirement blocks extracted from Master SRS
- **Grouped by:** Verification Method (Test: 147, Inspection: 182, Analysis: 20, Demonstration: 15)
- **Format:** Each entry reduced to ID + Statement + Priority + Verification Method (Rationale, Stability, and full Traceability stripped per QA/Verification View derivation rules)
- **RTM:** Full Traceability Matrix appended covering all 18 sections (369 rows across Parts A, B, and §15–§18 add-rows)
- **Master SRS reference:** `output/SRS-LUUCIPET-FINAL.md` — always consult for full context, rationale, stability, and cross-reference detail
- **Note:** Some requirement blocks in the RTM use verification methods of "Inspection-ext" or "Analysis-ext" for external-party attributed requirements (Mobile App team, IoT Cloud backend team). These are mapped to Inspection/Analysis respectively in the requirement tables above.

**Verification Method Distribution (Master SRS blocks only):**
- Test: 147 (40.4%)
- Inspection: 182 (50.0%)
- Analysis: 20 (5.5%)
- Demonstration: 15 (4.1%)
