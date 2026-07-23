> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-23T02:00:00Z
⚠️ For full context, always refer to the Master SRS.

---

## QA/Verification View

**368** requirements across **4** verification methods.

### Test (149 requirements)

| ID | Statement | Priority | § |
|---|---|---|---|
| SRS-SRS-COMP-0001 | Base Station firmware **shall** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variant | High | §2 |
| SRS-SRS-COMP-0002 | All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **shall** be mechanically compatible with both Mini and Max collar devices via the com | Critical | §2 |
| SRS-SRS-CONN-0004 | The system **shall** advertise the presence of the collar-mounted device at a default interval of 60 seconds. | Medium | §4 |
| SRS-SRS-CONN-0005 | The system **shall** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. | Medium | §4 |
| SRS-SRS-CONN-0006 | The system **shall** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than | High | §4 |
| SRS-SRS-CONN-0007 | The system **shall** transmit BLE signals at a power level of no less than +8 dBm. | Medium | §4 |
| SRS-SRS-CONN-0010 | Upon the collar-mounted device re-entering BLE range of a base station, the system **shall** automatically re-establish the BLE link without requiring | Critical | §4 |
| SRS-SRS-CONN-0011 | Upon establishing a BLE link with a base station, the system **shall** forward stored classification records from the collar-mounted device to the bas | Critical | §4 |
| SRS-SRS-CONN-0013 | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **shall** forward all classification records accumul | Critical | §4 |
| SRS-SRS-CONN-0014 | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. | Critical | §4 |
| SRS-SRS-CONN-0015 | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. | Critical | §4 |
| SRS-SRS-CONN-0016 | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. | Critical | §4 |
| SRS-SRS-CONN-0017 | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. | Critical | §4 |
| SRS-SRS-CONN-0019 | The system **shall** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated  | High | §4 |
| SRS-SRS-CONN-0020 | The system **shall** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in  | High | §4 |
| SRS-SRS-CONN-0022 | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. | High | §4 |
| SRS-SRS-CONN-0024 | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other | Medium | §4 |
| SRS-SRS-CONN-0025 | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix  | Medium | §4 |
| SRS-SRS-CONN-0028 | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. | High | §4 |
| SRS-SRS-CONN-0029 | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. | High | §4 |
| SRS-SRS-ENV-0001 | The collar device **shall** operate within an ambient temperature range of −20 °C to +50 °C without loss of function. | Critical | §12 |
| SRS-SRS-ENV-0002 | The collar device **shall** withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequen | High | §12 |
| SRS-SRS-ENV-0003 | The CCF **shall** be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of | High | §12 |
| SRS-SRS-ENV-0004 | The collar device **should** withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. | Medium | §12 |
| SRS-SRS-ENV-0007 | The Twist-Lock lug channels **shall** exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003 | Critical | §12 |
| SRS-SRS-ENV-0009 | The collar device **shall** survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. | Critical | §12 |
| SRS-SRS-ENV-0010 | The collar device **should** withstand mechanical shock per IEC 60068-2-27 without loss of function. | Medium | §12 |
| SRS-SRS-ENV-0011 | The collar device **should** withstand vibration per IEC 60068-2-64 without loss of function. | Medium | §12 |
| SRS-SRS-ENV-0013 | The CCF **shall** withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. | Critical | §12 |
| SRS-SRS-ENV-0014 | The CCF **shall** withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across  | High | §12 |
| SRS-SRS-ENV-0015 | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-sp | Critical | §12 |
| SRS-SRS-ENV-0016 | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Twist-Lock detent release torque **shall** remain within the torqu | High | §12 |
| SRS-SRS-ENV-0017 | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-specific  | Critical | §12 |
| SRS-SRS-ENV-0018 | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force **shall** remain within its SKU-spe | Critical | §12 |
| SRS-SRS-FUNC-0001 | The collar device **shall** detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event re | Critical | §2 |
| SRS-SRS-FUNC-0002 | The Base Station **shall** transport a recorded breakaway/separation event to the IoT Cloud Device-Management layer on the next successful Base Statio | Critical | §2 |
| SRS-SRS-FUNC-0003 | The persisted breakaway event record **shall** survive subsequent power loss, battery depletion, and reboot without corruption. | Critical | §2 |
| SRS-SRS-FUNC-0008 | While in Insight mode, the system **shall** sample the accelerometer continuously at 50 Hz. | High | §3 |
| SRS-SRS-FUNC-0009 | The system **shall** automatically revert from Insight mode to Wellness mode without requiring a manual user action. | High | §3 |
| SRS-SRS-FUNC-0010 | Upon detecting motion, the system **shall** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. | High | §3 |
| SRS-SRS-FUNC-0011 | While in Wellness mode and outside a confirmation burst, the system **shall not** exceed an idle current draw of 4 µA. | Critical | §3 |
| SRS-SRS-FUNC-0012 | When Longevity Mode is active, the system **shall not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mo | Critical | §3 |
| SRS-SRS-FUNC-0013 | When Longevity Mode is active, the system **shall not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy thresh | Critical | §3 |
| SRS-SRS-FUNC-0014 | The system **shall** sample the accelerometer at a rate of no less than 50 Hz. | Critical | §3 |
| SRS-SRS-FUNC-0017 | The system **shall** set species-specific classification thresholds during the onboarding process. | High | §3 |
| SRS-SRS-FUNC-0018 | The system **shall** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. | Critical | §3 |
| SRS-SRS-FUNC-0019 | The system **shall not** exceed a false-positive rate of 5% for each Tier-1 behavior class. | Critical | §3 |
| SRS-SRS-FUNC-0020 | The system **shall** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. | High | §3 |
| SRS-SRS-FUNC-0021 | The system **shall not** exceed a false-positive rate of 10% for each Tier-2 behavior class. | High | §3 |
| SRS-SRS-FUNC-0023 | The system **shall** include a confidence score in the range 0.0 to 1.0 in every generated classification record. | High | §3 |
| SRS-SRS-FUNC-0024 | The system **shall** timestamp every classification record in UTC with a resolution no coarser than 1 second. | High | §3 |
| SRS-SRS-FUNC-0026 | The system **shall** retain generated classification records locally for no less than 30 days without a cloud connection. | Critical | §3 |
| SRS-SRS-FUNC-0027 | The system **shall not** discard stored classification records upon loss of connectivity. | Critical | §3 |
| SRS-SRS-FUNC-0029 | The system **shall** forward stored classification records without data corruption. | Critical | §3 |
| SRS-SRS-FUNC-0030 | The system **shall** forward stored classification records without loss of their original sequence order. | High | §3 |
| SRS-SRS-FUNC-0032 | The system **shall not** transmit raw accelerometer data off the collar. | Critical | §3 |
| SRS-SRS-FUNC-0036 | The system **shall** apply a Scratching alert threshold value received via the companion application. | High | §3 |
| SRS-SRS-FUNC-0038 | The system **shall** apply a Shaking alert threshold value received via the companion application. | High | §3 |
| SRS-SRS-FUNC-0040 | The system **shall** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. | High | §3 |
| SRS-SRS-FUNC-0045 | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. | High | §5 |
| SRS-SRS-FUNC-0046 | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. | Medium | §5 |
| SRS-SRS-FUNC-0049 | The system **shall** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. | Critical | §5 |
| SRS-SRS-FUNC-0050 | The system **shall not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. | Critical | §5 |
| SRS-SRS-FUNC-0051 | The system **shall** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. | High | §5 |
| SRS-SRS-FUNC-0053 | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. | Critical | §5 |
| SRS-SRS-FUNC-0055 | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image  | Critical | §5 |
| SRS-SRS-FUNC-0056 | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. | Critical | §5 |
| SRS-SRS-FUNC-0058 | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. | Medium | §5 |
| SRS-SRS-FUNC-0062 | The persisted breakaway event record **shall** be transmitted to the Base Station on the next successful Base Station contact. | Critical | §2 |
| SRS-SRS-HW-0001 | The Mini collar device **shall** have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excludin | Critical | §11 |
| SRS-SRS-HW-0002 | The Max collar device **shall** have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, and excluding | Critical | §11 |
| SRS-SRS-HW-0003 | The collar device **shall** achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. | Critical | §11 |
| SRS-SRS-HW-0004 | The collar device enclosure **shall** maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. | Critical | §11 |
| SRS-SRS-HW-0008 | The device-facing charging socket **shall** drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, wi | Medium | §11 |
| SRS-SRS-HW-0014 | The collar device accelerometer **shall** support an output data rate of no less than 50 Hz. | Critical | §11 |
| SRS-SRS-HW-0019 | The collar device BLE radio **shall** be capable of a transmit power of no less than +8 dBm. | Medium | §11 |
| SRS-SRS-HW-0022 | The collar device battery subsystem **shall** provide overcharge, over-discharge, short-circuit, and over-temperature protection. | Critical | §11 |
| SRS-SRS-HW-0023 | The collar device battery **shall** pass UN 38.3 qualification testing before pilot production. | High | §11 |
| SRS-SRS-HW-0024 | The collar device **shall** raise a low-battery alert at a state-of-charge of 20% or below. | Medium | §11 |
| SRS-SRS-HW-0026 | The collar device **shall** incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. | High | §11 |
| SRS-SRS-HW-0027 | The collar device **shall** incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud conne | Critical | §11 |
| SRS-SRS-INT-0001 | The collar device shall implement the Bluetooth Low Energy (BLE) 5.x radio interface in the peripheral role. | High | §10 |
| SRS-SRS-INT-0002 | The base station shall implement the BLE 5.x radio interface in the central role. | High | §10 |
| SRS-SRS-INT-0003 | The base station shall support at least 4 concurrent BLE connections to collar devices. | High | §10 |
| SRS-SRS-INT-0004 | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. | Medium | §10 |
| SRS-SRS-INT-0005 | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. | Medium | §10 |
| SRS-SRS-INT-0006 | The collar device shall continue BLE advertising while maintaining an active BLE connection. | Medium | §10 |
| SRS-SRS-INT-0007 | The collar device shall randomize its BLE device address. | High | §10 |
| SRS-SRS-INT-0008 | The collar device shall transmit BLE signals at a power level of at least +8 dBm. | Medium | §10 |
| SRS-SRS-INT-0009 | The BLE link between the collar device and the base station shall maintain connectivity at an open-air separation distance of at least 9 meters. | High | §10 |
| SRS-SRS-INT-0010 | The system shall encrypt all BLE data-bearing links using AES-128 CCM. | Critical | §10 |
| SRS-SRS-INT-0011 | The system shall establish BLE pairing between the collar device and the base station using LE Secure Connections. | Critical | §10 |
| SRS-SRS-INT-0012 | The system shall support out-of-band (OOB) BLE pairing initiated via a QR-code-based exchange between the collar device and the base station. | High | §10 |
| SRS-SRS-INT-0013 | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpart  | Critical | §10 |
| SRS-SRS-INT-0016 | The base station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to [STD: IEEE 802.11 b/g/n]. | High | §10 |
| SRS-SRS-INT-0017 | The base station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. | Critical | §10 |
| SRS-SRS-INT-0018 | The base station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. | Medium | §10 |
| SRS-SRS-INT-0019 | The base station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sust | Medium | §10 |
| SRS-SRS-INT-0020 | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including [STD: FCC 47 CFR Part 15 Subpar | Critical | §10 |
| SRS-SRS-INT-0021 | The Max collar variant shall implement a passive (receive-only) GNSS interface. | High | §10 |
| SRS-SRS-INT-0023 | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. | High | §10 |
| SRS-SRS-INT-0024 | The Max collar variant shall apply a default GNSS fix interval of 2 hours. | Medium | §10 |
| SRS-SRS-INT-0025 | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. | High | §10 |
| SRS-SRS-INT-0026 | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. | Medium | §10 |
| SRS-SRS-INT-0027 | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. | High | §10 |
| SRS-SRS-INT-0028 | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. | High | §10 |
| SRS-SRS-INT-0029 | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. | Medium | §10 |
| SRS-SRS-INT-0033 | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to  | Medium | §10 |
| SRS-SRS-INT-0034 | The collar device shall reach full charge within 2 hours when docked at the charging interface. | High | §10 |
| SRS-SRS-INT-0035 | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. | Critical | §10 |
| SRS-SRS-INT-0036 | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar devi | Medium | §10 |
| SRS-SRS-INT-0038 | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment f | High | §10 |
| SRS-SRS-INT-0040 | The Twist-Lock mechanical interface shall engage and release via a 90-degree rotation. | High | §10 |
| SRS-SRS-INT-0044 | The Twist-Lock detent shall release within a torque window of 0.08 to 0.10 N·m. | High | §10 |
| SRS-SRS-INT-0045 | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. | Critical | §10 |
| SRS-SRS-INT-0046 | The Twist-Lock interface shall require no more than 5 N of axial press-in force to engage. | Medium | §10 |
| SRS-SRS-INT-0047 | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. | High | §10 |
| SRS-SRS-INT-0049 | The Twist-Lock interface shall provide magnetic engagement assistance effective at an approach distance of up to 5 mm. | Low | §10 |
| SRS-SRS-INT-0051 | The Twist-Lock interface shall be engageable within 5 seconds. | Low | §10 |
| SRS-SRS-INT-0053 | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. | High | §10 |
| SRS-SRS-INT-0054 | The device-enforced protocol shall support transport of BLE sighting reports, each comprising device identifier, received signal strength indicator (R | High | §10 |
| SRS-SRS-INT-0055 | The device-enforced protocol **shall** support transport of cloud-originated configuration data as a distinct payload type. | High | §10 |
| SRS-SRS-INT-0057 | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record fr | High | §10 |
| SRS-SRS-INT-0058 | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. | High | §10 |
| SRS-SRS-INT-0059 | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. | High | §10 |
| SRS-SRS-INT-0060 | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. | High | §10 |
| SRS-SRS-INT-0061 | The device-enforced protocol **shall** support transport of OTA firmware images as a distinct payload type. | High | §10 |
| SRS-SRS-OPER-0002 | A household deployment **shall not** exceed 8 Base Stations, in any combination of Charging and Relay tiers. | High | §2 |
| SRS-SRS-OPER-0003 | The collar device **shall** retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. | High | §2 |
| SRS-SRS-PERF-0003 | The system **shall** produce a classification result within 2 seconds of the triggering motion event. | High | §6 |
| SRS-SRS-PERF-0004 | The base station **shall** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. | Medium | §6 |
| SRS-SRS-PERF-0006 | The collar-mounted device **shall** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. | Medium | §6 |
| SRS-SRS-PERF-0007 | The system **shall** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/a | High | §6 |
| SRS-SRS-SAFE-0001 | The Zone 2 Fuse Tab of the CCF-S variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to i | Critical | §7 |
| SRS-SRS-SAFE-0002 | The Zone 2 Fuse Tab of the CCF-M variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to i | Critical | §7 |
| SRS-SRS-SAFE-0003 | The Zone 2 Fuse Tab of the CCF-L variant **shall** fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to i | Critical | §7 |
| SRS-SRS-SAFE-0005 | The Zone 2 Fuse Tab **shall not** be capable of being reused or restored to a load-bearing state after fracture. | Critical | §7 |
| SRS-SRS-SAFE-0009 | The Zone 1 clamp **shall** retain axial loads of at least 50 N without structural failure. | Critical | §7 |
| SRS-SRS-SAFE-0010 | The Zone 1 clamp **shall** remain structurally intact following a Zone 2 fracture event. | Critical | §7 |
| SRS-SRS-SAFE-0011 | The Twist-Lock device-to-CCF interface **shall** retain axial loads exceeding 100 N without disengaging. | Critical | §7 |
| SRS-SRS-SAFE-0012 | The Twist-Lock **shall** remain engaged under inertial loads generated by pet head-shake motion up to 50 g. | High | §7 |
| SRS-SRS-SAFE-0014 | The device **shall** emit a detectable separation signature upon Zone 2 breakaway. | High | §7 |
| SRS-SRS-SAFE-0016 | The Zone 2 Fuse Tab **shall not** fracture under a compressive load below 250 N. | Critical | §7 |
| SRS-SRS-SAFE-0017 | The CCF body **shall** resist penetration for at least 30 seconds under a 250 N compressive load. | High | §7 |
| SRS-SRS-SAFE-0020 | The device-absent CCF socket **shall** provide clearance verified against a 12 mm entrapment-probe criterion. | Medium | §7 |
| SRS-SRS-SEC-0001 | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. | Critical | §8 |
| SRS-SRS-SEC-0002 | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. | Critical | §8 |
| SRS-SRS-SEC-0003 | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. | Critical | §8 |
| SRS-SRS-SEC-0005 | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. | Critical | §8 |

### Inspection (184 requirements)

| ID | Statement | Priority | § |
|---|---|---|---|
| SRS-SRS-COMP-0003 | The Mini and Max collar variants **shall** exhibit equivalent behavioral-classification outputs. | High | §2 |
| SRS-SRS-COMP-0005 | The collar device, in its standalone (CCF-unmated) configuration, shall conform to the IEC 60529 IPX7 test methodology as the verification basis for t | Critical | §17 |
| SRS-SRS-COMP-0006 | The Li-Po battery cells used in the Mini and Max collar variants shall conform to IEC 62133-2:2017 with Amendment 1:2021 (Edition 1.1). | Critical | §17 |
| SRS-SRS-COMP-0007 | The Li-Po battery cells shall conform to the UN Manual of Tests and Criteria, Part III, Section 38.3, prior to pilot production. | Critical | §17 |
| SRS-SRS-COMP-0008 | The Li-Po battery cells shall conform to UL 1642 or UL 2054, as applicable to cell construction, for placement on the US market. | High | §17 |
| SRS-SRS-COMP-0009 | The Base Station, in both Charging and Relay tiers, shall conform to EN 62368-1:2020 or UL 62368-1, as applicable to the target market. | Critical | §17 |
| SRS-SRS-COMP-0010 | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. | Critical | §17 |
| SRS-SRS-COMP-0011 | The CCF's thermal-cycling exposure qualification (SRS-ENV-0003) shall be conducted per IEC 60068-2-14 Test Na. | High | §17 |
| SRS-SRS-COMP-0012 | The collar device's damp-heat exposure qualification (SRS-ENV-0004) shall be conducted per IEC 60068-2-78. | Medium | §17 |
| SRS-SRS-COMP-0013 | The collar device's mechanical-shock exposure qualification (SRS-ENV-0010) shall be conducted per IEC 60068-2-27. | Medium | §17 |
| SRS-SRS-COMP-0014 | The collar device's vibration exposure qualification (SRS-ENV-0011) shall be conducted per IEC 60068-2-64. | Medium | §17 |
| SRS-SRS-COMP-0015 | The CCF's UV-aging exposure qualification (SRS-ENV-0013) shall be conducted per IEC 60068-2-5. | High | §17 |
| SRS-SRS-COMP-0016 | The BLE 5.x radio interface shall conform to ETSI EN 300 328 as the applicable EU harmonised standard for 2.4 GHz wideband transmission systems. | Critical | §17 |
| SRS-SRS-COMP-0017 | Each collar variant and Base Station tier shall hold a valid Bluetooth SIG Qualified Design ID (QDID) prior to product launch. | Critical | §17 |
| SRS-SRS-COMP-0018 | The BLE radio interface shall conform to FCC 47 CFR Part 15 Subpart C §15.247 for the US market. | Critical | §17 |
| SRS-SRS-COMP-0019 | The system shall conform to FCC 47 CFR Part 15 Subpart B §15.107/§15.109 for the US market. | High | §17 |
| SRS-SRS-COMP-0020 | The collar devices and Base Station shall conform to RED 2014/53/EU Articles 3.1(a), 3.1(b), and 3.2. | Critical | §17 |
| SRS-SRS-COMP-0022 | Materials used in the device enclosure and CCF accessory family shall conform to REACH (EC) 1907/2006 Annex XVII substance restrictions. | Critical | §17 |
| SRS-SRS-COMP-0023 | Electronic components and materials shall conform to RoHS 2011/65/EU as amended by 2015/863, Annex II restricted-substance limits. | Critical | §17 |
| SRS-SRS-COMP-0024 | The system shall conform to California Proposition 65 warning and substance-disclosure requirements for the US-CA market. | High | §17 |
| SRS-SRS-COMP-0025 | The Li-Po battery cells shall conform to EU Battery Regulation (EU) 2023/1542 Article 6 material-content and labelling provisions. | Critical | §17 |
| SRS-SRS-COMP-0026 | The system and packaging shall conform to WEEE 2012/19/EU end-of-life electronic-waste collection and marking requirements. | High | §17 |
| SRS-SRS-COMP-0027 | Product packaging shall conform to EU PPWR and UK Producer Responsibility requirements. | Medium | §17 |
| SRS-SRS-COMP-0028 | The SBOM produced at each OTA release (SRS-FUNC-0061) and maintained across the supported service lifetime (SRS-MAINT-0002) shall be issued in a machi | Medium | §17 |
| SRS-SRS-COMP-0031 | The Mini and Max collar variants **shall** use an interoperable common BLE communication protocol. | High | §2 |
| SRS-SRS-CONN-0001 | The system **shall** operate the collar-mounted device in the BLE peripheral role relative to the base station. | High | §4 |
| SRS-SRS-CONN-0002 | The system **shall** operate the base station in the BLE central role relative to the collar-mounted device. | High | §4 |
| SRS-SRS-CONN-0003 | The system **shall** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. | High | §4 |
| SRS-SRS-CONN-0008 | The system **shall** randomize the BLE device address of the collar-mounted device. | High | §4 |
| SRS-SRS-CONN-0009 | The system **shall** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. | Critical | §4 |
| SRS-SRS-CONN-0012 | The system **shall** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. | High | §4 |
| SRS-SRS-CONN-0018 | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. | Critical | §4 |
| SRS-SRS-CONN-0021 | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household acco | High | §4 |
| SRS-SRS-CONN-0023 | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. | High | §4 |
| SRS-SRS-DATA-0001 | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each cla | Critical | §9 |
| SRS-SRS-DATA-0002 | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. | High | §9 |
| SRS-SRS-DATA-0003 | The system shall timestamp each classification record with UTC time accurate to within 1 second. | High | §9 |
| SRS-SRS-DATA-0004 | On the Max variant, the system shall append the most recent GNSS fix to the classification record. | High | §9 |
| SRS-SRS-DATA-0005 | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. | Critical | §9 |
| SRS-SRS-DATA-0006 | The system shall preserve stored classification records without corruption across a power-loss event. | Critical | §9 |
| SRS-SRS-DATA-0007 | The system shall detect corruption of stored classification records prior to transmission. | High | §9 |
| SRS-SRS-DATA-0008 | The system shall perform classification and record generation independent of BLE connectivity state. | Critical | §9 |
| SRS-SRS-DATA-0009 | The system shall forward stored classification records to the transport layer without introducing data corruption. | Critical | §9 |
| SRS-SRS-DATA-0010 | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. | High | §9 |
| SRS-SRS-DATA-0011 | The system shall not transmit raw accelerometer data beyond the collar. | Critical | §9 |
| SRS-SRS-DATA-0012 | The system shall perform normalization of sensor data on-device prior to classification. | High | §9 |
| SRS-SRS-DATA-0013 | The system shall not require a cloud round-trip to complete a classification decision. | High | §9 |
| SRS-SRS-DATA-0014 | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. | Medium | §9 |
| SRS-SRS-DATA-0015 | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. | Critical | §9 |
| SRS-SRS-DATA-0016 | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. | Critical | §9 |
| SRS-SRS-DATA-0017 | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. | Medium | §9 |
| SRS-SRS-DATA-0018 | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, cla | High | §9 |
| SRS-SRS-DATA-0019 | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event pu | High | §9 |
| SRS-SRS-DATA-0020 | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. | Medium | §9 |
| SRS-SRS-DATA-0021 | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. | Medium | §9 |
| SRS-SRS-DATA-0022 | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent w | Low | §9 |
| SRS-SRS-DATA-0023 | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit  | Critical | §9 |
| SRS-SRS-DATA-0024 | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management laye | Critical | §9 |
| SRS-SRS-DATA-0025 | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. | Critical | §9 |
| SRS-SRS-DATA-0026 | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. | Critical | §9 |
| SRS-SRS-DATA-0027 | The system shall transmit a committed breakaway event record on the next successful base-station contact following separation. | High | §9 |
| SRS-SRS-ENV-0005 | Product documentation and marketing materials **shall not** state or imply an IP67, or equivalent, ingress-protection rating for the collar device whi | Critical | §12 |
| SRS-SRS-ENV-0006 | The IP67 ingress-protection rating claimed for the collar device **shall** be confirmed by an independent, accredited test laboratory and documented i | High | §12 |
| SRS-SRS-ENV-0008 | The ingress-protection seal boundary **shall** be located on the interior side of the enclosure assembly such that it is not directly exposed on any e | High | §12 |
| SRS-SRS-FUNC-0015 | The system **shall** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. | High | §3 |
| SRS-SRS-FUNC-0016 | The system **shall** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. | Medium | §3 |
| SRS-SRS-FUNC-0022 | The system **shall** include a behavior class label in every generated classification record. | Critical | §3 |
| SRS-SRS-FUNC-0025 | On the Max product variant, the system **shall** include the most recent GNSS fix in every generated classification record. | Medium | §3 |
| SRS-SRS-FUNC-0031 | The system **shall** normalize raw accelerometer data on-device prior to classification. | High | §3 |
| SRS-SRS-FUNC-0037 | The system **shall** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. | Medium | §3 |
| SRS-SRS-FUNC-0039 | The system **shall** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. | Medium | §3 |
| SRS-SRS-FUNC-0041 | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. | High | §3 |
| SRS-SRS-FUNC-0042 | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. | High | §3 |
| SRS-SRS-FUNC-0047 | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Se | Critical | §5 |
| SRS-SRS-FUNC-0052 | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. | Critical | §5 |
| SRS-SRS-FUNC-0054 | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in sec | Critical | §5 |
| SRS-SRS-FUNC-0059 | The Mobile App **shall** notify the user when an OTA firmware update is available. | Medium | §5 |
| SRS-SRS-FUNC-0060 | The Mobile App **shall** display the current OTA update state reported by the device. | Medium | §5 |
| SRS-SRS-FUNC-0061 | The system **shall** produce a Software Bill of Materials for every OTA firmware release. | Medium | §5 |
| SRS-SRS-FUNC-0062 | The system **shall** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. | High | §5 |
| SRS-SRS-HW-0005 | The collar device **shall** provide a light-emitting-diode status indicator. | Medium | §11 |
| SRS-SRS-HW-0006 | The collar device enclosure **shall** provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. | High | §11 |
| SRS-SRS-HW-0007 | The Twist-Lock lug channels and magnetic insert on the device underside **shall not** penetrate the enclosure wall or the ingress seal path. | Critical | §11 |
| SRS-SRS-HW-0009 | The CCF body **shall** be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). | High | §11 |
| SRS-SRS-HW-0010 | The CCF material **shall** incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. | High | §11 |
| SRS-SRS-HW-0011 | The CCF **shall not** contain any metallic sub-component within the Zone 2 snap/breakaway region. | Critical | §11 |
| SRS-SRS-HW-0012 | Animal-contact surfaces of the device and CCF **shall not** use chrome or nickel plating. | High | §11 |
| SRS-SRS-HW-0013 | The collar device **shall** incorporate a three-axis MEMS accelerometer. | Critical | §11 |
| SRS-SRS-HW-0015 | The collar device accelerometer **shall** provide a wake-on-motion interrupt. | High | §11 |
| SRS-SRS-HW-0016 | The Mini collar device **shall not** incorporate a GNSS receiver. | Medium | §11 |
| SRS-SRS-HW-0017 | The Max collar device **shall** incorporate a passive receive-only GNSS receiver. | High | §11 |
| SRS-SRS-HW-0018 | The collar device **shall** incorporate a Bluetooth Low Energy 5.x radio. | Critical | §11 |
| SRS-SRS-HW-0020 | The Mini collar device **shall** incorporate a battery cell of no less than 120 mAh nominal capacity. | High | §11 |
| SRS-SRS-HW-0021 | The Max collar device **shall** incorporate a battery cell of no less than 400 mAh nominal capacity. | High | §11 |
| SRS-SRS-HW-0025 | The collar device **shall** incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. | Critical | §11 |
| SRS-SRS-HW-0028 | The collar device compute subsystem **shall** provide direct-memory-access peripheral access and a hardware root of trust. | Critical | §11 |
| SRS-SRS-HW-0029 | The collar device accelerometer **shall** provide a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. | High | §11 |
| SRS-SRS-INT-0014 | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). | Critical | §10 |
| SRS-SRS-INT-0022 | The Mini collar variant shall not implement a GNSS interface. | Medium | §10 |
| SRS-SRS-INT-0031 | The charging interface between the collar device and the charging cradle (base station charging cradle or Portable Travel Charging Cradle) shall provi | Critical | §10 |
| SRS-SRS-INT-0039 | The Twist-Lock mechanical interface shall employ a Twist-Lock mechanical retention interface with three equally-spaced lugs at 120-degree radial separ | Critical | §10 |
| SRS-SRS-INT-0041 | The Twist-Lock lug ramp shall have a trapezoidal profile with an 8-degree self-locking angle. | High | §10 |
| SRS-SRS-INT-0042 | Each Twist-Lock lug shall be 4.0 mm wide by 1.2 mm thick. | High | §10 |
| SRS-SRS-INT-0043 | The Twist-Lock interface shall include one asymmetric lug sized to differ from the other two lugs (7.5 mm versus 5.0 mm) to enforce a single correct e | High | §10 |
| SRS-SRS-INT-0052 | The system shall implement a single, cross-variant BLE application protocol governing all collar-to-base-station communication shared across all colla | High | §10 |
| SRS-SRS-INT-0056 | The base station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. | High | §10 |
| SRS-SRS-MAINT-0001 | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. | High | §16 |
| SRS-SRS-MAINT-0002 | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetim | Medium | §16 |
| SRS-SRS-MAINT-0003 | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported serv | High | §16 |
| SRS-SRS-OPER-0001 | A household deployment **shall** include at least one Base Station of the Charging tier. | Critical | §2 |
| SRS-SRS-OPER-0004 | The Max variant's GNSS smart power gate **shall not** be configurable by the owner. | High | §2 |
| SRS-SRS-OPER-0006 | The system **shall** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. | High | §2 |
| SRS-SRS-OPER-0007 | The Base Station **shall** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dB | High | §2 |
| SRS-SRS-OPER-0008 | The Mobile App **shall** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakawa | High | §2 |
| SRS-SRS-OPER-0009 | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's species classifier profile. | Medium | §2 |
| SRS-SRS-OPER-0010 | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. | Medium | §2 |
| SRS-SRS-OPER-0011 | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. | Medium | §2 |
| SRS-SRS-OPER-0012 | The base station **shall** remain in a continuously powered, non-sleeping operational state for as long as AC power is supplied, maintaining active BL | High | §15 |
| SRS-SRS-OPER-0013 | The base station **shall** be supplied with an AC-to-USB-C power adapter as an included accessory. | Medium | §15 |
| SRS-SRS-OPER-0014 | The Base Station (Charging) tier **shall** provide exactly 3 status LEDs, indicating at minimum: AC power presence, device-charging activity, and clou | High | §15 |
| SRS-SRS-OPER-0015 | The Base Station (Relay) tier **shall** provide exactly 2 status LEDs, indicating at minimum: AC power presence and cloud-connectivity status. | High | §15 |
| SRS-SRS-OPER-0016 | Every base station in a household deployment **shall** participate in a shared geo-fence mesh by independently reporting BLE sighting reports for ever | High | §15 |
| SRS-SRS-OPER-0017 | The collar device **shall** determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) | High | §15 |
| SRS-SRS-OPER-0018 | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from HOME to AWAY only when no paired base station RSSI  | Medium | §15 |
| SRS-SRS-OPER-0019 | The collar device, while in Wellness Mode and not actively processing a motion-triggered confirmation burst, **shall** remain in its deepest available | High | §15 |
| SRS-SRS-OPER-0020 | When the owner changes the Max collar variant's configured GNSS fix interval, the collar device **shall** apply the new interval no later than the sta | Medium | §15 |
| SRS-SRS-OPER-0021 | Battery-life validation testing **shall** be performed using cells that have completed no fewer than 50 charge/discharge cycles prior to the validatio | Medium | §15 |
| SRS-SRS-OPER-0022 | The collar device **shall** rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the ba | Medium | §15 |
| SRS-SRS-OPER-0023 | The system's operational and durability requirements that reference an expected service lifetime **shall** use 2 years as the minimum testable floor,  | Medium | §15 |
| SRS-SRS-OPER-0024 | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from AWAY to HOME only when at least one paired base sta | Medium | §15 |
| SRS-SRS-PERF-0005 | On the Max product variant, the system **shall** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. | Medium | §6 |
| SRS-SRS-PERF-0008 | The system **shall** allow the Twist-Lock mechanism to be engaged within 5 seconds. | Low | §6 |
| SRS-SRS-REG-0001 | The system's labeling and marketing materials **shall not** include diagnostic, treatment, or disease-detection claims. | Critical | §1 |
| SRS-SRS-REG-0001 | The BLE and Wi-Fi radio modules shall hold a valid FCC Part 15 Subpart C certification granted by an FCC-recognized Telecommunication Certification Bo | High | §18 |
| SRS-SRS-REG-0002 | The system shall be placed on the US market under a Supplier's Declaration of Conformity (SDoC) covering FCC Part 15 Subpart B unintentional-radiator  | High | §18 |
| SRS-SRS-REG-0003 | Each collar variant and Base Station tier shall bear a unique FCC Identifier (FCC ID) on the device enclosure or, where physical marking is impractica | High | §18 |
| SRS-SRS-REG-0004 | Each Base Station tier shall hold a valid Nationally Recognized Testing Laboratory (NRTL) listing evidencing UL 62368-1 conformance prior to commercia | High | §18 |
| SRS-SRS-REG-0005 | The system shall bear a California Proposition 65 warning label on packaging or point-of-sale materials if any Proposition 65-listed substance is pres | High | §18 |
| SRS-SRS-REG-0006 | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — suffi | High | §18 |
| SRS-SRS-REG-0007 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for FCC intentional-radiator exemption prior to comm | High | §18 |
| SRS-SRS-REG-0008 | The BLE and Wi-Fi radio modules shall hold a valid Innovation, Science and Economic Development Canada (ISED) certification under RSS-247 and RSS-Gen  | High | §18 |
| SRS-SRS-REG-0009 | The system shall be placed on the Canada market under a Declaration of Conformity to ISED ICES-003 for unintentional-radiator emissions prior to comme | High | §18 |
| SRS-SRS-REG-0010 | Each collar variant and Base Station tier shall bear a unique Innovation Canada certification number (IC ID) on the device enclosure or, where physica | High | §18 |
| SRS-SRS-REG-0011 | The system shall be accompanied by a complete technical documentation package — including radio test reports, schematics, and labeling artwork — suffi | High | §18 |
| SRS-SRS-REG-0012 | The Max variant's GNSS receive-only module shall undergo a documented applicability determination for ISED intentional-radiator exemption prior to com | High | §18 |
| SRS-SRS-REG-0013 | The system shall not be released for commercial distribution into the US or Canada market until all certifications, declarations, and markings identif | High | §18 |
| SRS-SRS-REG-0014 | CE marking prerequisite for radio equipment. | Critical | §18 |
| SRS-SRS-REG-0016 | On device or packaging. | High | §18 |
| SRS-SRS-REG-0017 | GPSR 2023/988 Art 5/6. | Critical | §18 |
| SRS-SRS-REG-0018 | GPSR Art 4 / RED Art 11. | High | §18 |
| SRS-SRS-REG-0019 | In-scope interface obligation. | High | §18 |
| SRS-SRS-REG-0020 | 2011/65/EU + 2015/863. | High | §18 |
| SRS-SRS-REG-0021 | Per-member-state. | High | §18 |
| SRS-SRS-REG-0022 | Annex XVII. | High | §18 |
| SRS-SRS-REG-0023 | (EU) 2023/1542 Art 6. | Critical | §18 |
| SRS-SRS-REG-0025 | (EU) 2024/2847 Annex I + Art 13–14. | Critical | §18 |
| SRS-SRS-REG-0026 | (EU) 2016/679 + Art 30. | Critical | §18 |
| SRS-SRS-REG-0027 | PPWR. | Medium | §18 |
| SRS-SRS-REG-0028 | UK SI 2017/1206. | Critical | §18 |
| SRS-SRS-REG-0030 | UK establishment requirement. | High | §18 |
| SRS-SRS-REG-0031 | \| | Critical | §18 |
| SRS-SRS-REG-0032 | UK GDPR + DPA 2018. | Critical | §18 |
| SRS-SRS-REG-0033 | UK REACH, UK RoHS, UK WEEE. | High | §18 |
| SRS-SRS-REG-0034 | \| | Medium | §18 |
| SRS-SRS-REG-0035 | \| | Critical | §18 |
| SRS-SRS-REG-0036 | AS/NZS 4268:2017. | High | §18 |
| SRS-SRS-REG-0037 | Precondition to RCM. | High | §18 |
| SRS-SRS-REG-0038 | In-market required. | High | §18 |
| SRS-SRS-REG-0039 | In-scope interface obligation. | High | §18 |
| SRS-SRS-REG-0042 | Lifetime obligation. | High | §18 |
| SRS-SRS-REG-0043 | Per-market minimum. | High | §18 |
| SRS-SRS-REG-0044 | Consolidating gate. | Critical | §18 |
| SRS-SRS-RELI-0001 | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of  | Critical | §13 |
| SRS-SRS-RELI-0002 | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging | High | §13 |
| SRS-SRS-RELI-0003 | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. | High | §13 |
| SRS-SRS-RELI-0004 | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempt | High | §13 |
| SRS-SRS-SAFE-0006 | Upon fracture, the Zone 2 Fuse Tab **shall not** produce a detached fragment separate from the CCF body. | High | §7 |
| SRS-SRS-SAFE-0007 | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway **shall** be blunt, presenting no sharp edge. | High | §7 |
| SRS-SRS-SAFE-0008 | The CCF **shall** present a visible fracture indicator upon Zone 2 breakaway. | High | §7 |
| SRS-SRS-SAFE-0013 | The device **shall not** be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. | Critical | §7 |
| SRS-SRS-SAFE-0021 | Materials in animal-skin contact **shall** be non-toxic. | High | §7 |
| SRS-SRS-SAFE-0022 | The system **shall** provide battery-ingestion warning labeling. | High | §7 |
| SRS-SRS-SEC-0004 | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. | Critical | §8 |
| SRS-SRS-SEC-0006 | The system shall have a public vulnerability-disclosure policy in place before product launch. | High | §8 |

### Analysis (20 requirements)

| ID | Statement | Priority | § |
|---|---|---|---|
| SRS-SRS-COMP-0021 | The system shall conform to IEC 62311 / EN 62311, or applicable per-market RF human-exposure standard, if RF-exposure assessment is determined applica | High | §17 |
| SRS-SRS-CONN-0026 | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. | Critical | §4 |
| SRS-SRS-ENV-0012 | The collar device enclosure material **shall** be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service | Critical | §12 |
| SRS-SRS-FUNC-0057 | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA  | Critical | §5 |
| SRS-SRS-INT-0015 | The BLE radio interface should undergo an RF human-exposure assessment against [STD: IEC 62311] / [STD: FCC 47 CFR §1.1310] for continuously worn 2.4  | Medium | §10 |
| SRS-SRS-INT-0030 | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-ma | Medium | §10 |
| SRS-SRS-OPER-0005 | The in-box Standard CCF **shall** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. | Medium | §2 |
| SRS-SRS-PERF-0001 | The system's Mini variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevit | High | §6 |
| SRS-SRS-PERF-0002 | The system's Max variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval set | High | §6 |
| SRS-SRS-REG-0002 | Any post-launch feature that could constitute a diagnostic claim **shall** undergo regulatory classification review before release. | Critical | §1 |
| SRS-SRS-REG-0015 | Conditional on harmonised standard OJ listing. | High | §18 |
| SRS-SRS-REG-0024 | Deadline 18 Feb 2027. | Critical | §18 |
| SRS-SRS-REG-0029 | Conditional. | High | §18 |
| SRS-SRS-REG-0040 | RM-0009 UNCERTAIN. | High | §18 |
| SRS-SRS-REG-0041 | Threshold-contingent. | Medium | §18 |
| SRS-SRS-REG-0045 | \| | High | §18 |
| SRS-SRS-REG-0046 | \| | High | §18 |
| SRS-SRS-SAFE-0004 | If the assembled device+CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor **shall** be revised upward to 30 N. | Critical | §7 |
| SRS-SRS-SAFE-0018 | Materials in animal-skin contact on the device enclosure **shall** resist chew-induced damage. | Medium | §7 |
| SRS-SRS-SAFE-0019 | The CCF socket **shall** present no independent entrapment hazard when the device is absent. | High | §7 |

### Demonstration (15 requirements)

| ID | Statement | Priority | § |
|---|---|---|---|
| SRS-SRS-CONN-0027 | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. | Critical | §4 |
| SRS-SRS-CONN-0030 | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **shall** retry uploading the affected  | High | §4 |
| SRS-SRS-FUNC-0006 | The system **shall** operate in Wellness mode as its default power-optimized classification mode. | Critical | §3 |
| SRS-SRS-FUNC-0007 | The system **shall** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. | High | §3 |
| SRS-SRS-FUNC-0028 | The system **shall** generate and record classifications independently of the current BLE connectivity state. | Critical | §3 |
| SRS-SRS-FUNC-0033 | The system **shall** produce classification decisions without requiring a round-trip to a cloud service. | Critical | §3 |
| SRS-SRS-FUNC-0034 | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. | High | §3 |
| SRS-SRS-FUNC-0035 | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. | High | §3 |
| SRS-SRS-FUNC-0043 | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). | Critical | §5 |
| SRS-SRS-FUNC-0044 | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). | Critical | §5 |
| SRS-SRS-FUNC-0048 | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. | High | §5 |
| SRS-SRS-INT-0032 | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. | Critical | §10 |
| SRS-SRS-INT-0037 | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. | High | §10 |
| SRS-SRS-INT-0048 | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. | Medium | §10 |
| SRS-SRS-INT-0050 | The Twist-Lock interface shall be operable without tools. | High | §10 |

