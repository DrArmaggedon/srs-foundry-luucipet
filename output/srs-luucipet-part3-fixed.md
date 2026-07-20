
## 9. Data Requirements

This section specifies requirements governing the content, storage, integrity, privacy, and protection of data produced by the LUUCIPet collar device (Mini and Max variants). It addresses what classification and event data is and how it must be handled on-device — not the transport protocol mechanics (Section 4), the classification algorithm itself (Section 3), or transport-layer cryptography (Section 8).

### 9.1 Scope Boundary

Applicable regulatory instruments for this section are GDPR (EU) 2016/679, UK GDPR and Data Protection Act 2018, PIPEDA, CCPA/CPRA (indicative), and the data-protection-relevant provisions of ETSI EN 303 645:2025. Cybersecurity vulnerability-management obligations are addressed in Section 8.

Functions performed by parties outside this build (Mobile App team, IoT Cloud backend team) are documented as boundary notes in this section rather than silently omitted.

### 9.2 Classification Record Format and Schema

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0001 | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. | CRITICAL | STABLE | Test |
| SRS-DATA-0002 | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. | HIGH | STABLE | Test |
| SRS-DATA-0003 | The system shall timestamp each classification record with UTC time accurate to within 1 second. | HIGH | STABLE | Test |
| SRS-DATA-0004 | On the Max variant, the system shall append the most recent GNSS fix to the classification record. | HIGH | STABLE | Test |

### 9.3 On-Device Storage and Retention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0005 | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. | CRITICAL | STABLE | Test |
| SRS-DATA-0006 | The system shall preserve stored classification records without corruption across a power-loss event. | CRITICAL | STABLE | Test |
| SRS-DATA-0007 | The system shall detect corruption of stored classification records prior to transmission. | HIGH | LIKELY-CHANGE | Test |

### 9.4 Data Integrity

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0008 | The system shall perform classification and record generation independent of BLE connectivity state. | CRITICAL | STABLE | Test |
| SRS-DATA-0009 | The system shall forward stored classification records to the transport layer without introducing data corruption. | CRITICAL | STABLE | Test |
| SRS-DATA-0010 | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. | HIGH | STABLE | Test |

### 9.5 Raw Data Boundary and Processing Locality

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0011 | The system shall not transmit raw accelerometer data beyond the collar. | CRITICAL | STABLE | Test |
| SRS-DATA-0012 | The system shall perform normalization of sensor data on-device prior to classification. | HIGH | STABLE | Analysis |
| SRS-DATA-0013 | The system shall not require a cloud round-trip to complete a classification decision. | HIGH | STABLE | Demonstration |
| SRS-DATA-0014 | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. | MEDIUM | LIKELY-CHANGE | Analysis |

### 9.6 Buffered Data Persistence

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0015 | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud Device-Management layer. | CRITICAL | STABLE | Test |
| SRS-DATA-0016 | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. | CRITICAL | STABLE | Test |
| SRS-DATA-0017 | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. | MEDIUM | STABLE | Test |

### 9.7 Privacy Regime — Data Handling Obligations

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0018 | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. | HIGH | LIKELY-CHANGE | Inspection |
| SRS-DATA-0019 | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. | HIGH | STABLE | Inspection |
| SRS-DATA-0020 | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. | MEDIUM | LIKELY-CHANGE | Demonstration |
| SRS-DATA-0021 | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. | MEDIUM | LIKELY-CHANGE | Demonstration |
| SRS-DATA-0022 | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. | LOW | VOLATILE | Analysis |

### 9.8 Data-at-Rest Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0023 | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. | CRITICAL | STABLE | Inspection |

### 9.9 External Data Transport Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0024 | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established Base Station sync interface. | CRITICAL | STABLE | Test |

### 9.10 Breakaway Event Record Persistence

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-DATA-0025 | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. | CRITICAL | STABLE | Test |
| SRS-DATA-0026 | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. | CRITICAL | STABLE | Test |
| SRS-DATA-0027 | The system shall transmit a committed breakaway event record on the next successful Base Station contact following separation. | HIGH | STABLE | Test |

### 9.11 Out-of-Scope Data Functions

The following data-related functions are outside this system's build scope:

- **Cloud-side storage and analytics** of the data transported under SRS-DATA-0024 is performed by the IoT Cloud backend team. This system's data obligation ends at successful, acknowledged transport to the Device-Management layer.
- **Mobile App presentation/display** of wellness records, classification history, and breakaway alerts is performed by the Mobile App team.
- **Cloud-side home/away state machine** is owned by the IoT Cloud backend team; the device-local home/away state machine referenced elsewhere in this SRS is the sole in-scope authority for power gating.

---

## 10. Interface Requirements

This section specifies the external interfaces of the LUUCIPet Wellness Monitor system: the BLE radio interface (collar-to-Base Station), the Wi-Fi radio interface (Base Station-to-cloud), the GNSS receive interface (Max only), the pogo-pin charging interface, the Twist-Lock mechanical attachment interface (collar device-to-CCF), and the device-enforced BLE application protocol. Zone 2 Fuse Tab breakaway force windows and post-breakaway safety protocol are governed by Section 7 (Safety) and are not restated here. Cross-variant identical mechanical-interface geometry for pogo-pin and Twist-Lock across Mini and Max is established by SRS-COMP-0002 and SRS-COMP-0003 (Section 2).

### 10.1 BLE Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0001 | The collar device shall implement the BLE 5.x radio interface in the peripheral role. | HIGH | STABLE | Test |
| SRS-INT-0002 | The Base Station shall implement the BLE 5.x radio interface in the central role. | HIGH | STABLE | Test |
| SRS-INT-0003 | The Base Station shall support at least 4 concurrent BLE connections to collar devices. | HIGH | STABLE | Test |
| SRS-INT-0004 | The collar device shall advertise via BLE with a default advertising interval of 60 seconds. | MEDIUM | STABLE | Test |
| SRS-INT-0005 | The collar device shall support a user-configurable BLE advertising interval between 1 second and 180 seconds inclusive. | MEDIUM | STABLE | Test |
| SRS-INT-0006 | The collar device shall continue BLE advertising while maintaining an active BLE connection. | MEDIUM | STABLE | Test |
| SRS-INT-0007 | The collar device shall randomize its BLE device address. | HIGH | STABLE | Test |
| SRS-INT-0008 | The collar device shall transmit BLE signals at a power level of at least +8 dBm. | MEDIUM | STABLE | Test |
| SRS-INT-0009 | The BLE link between the collar device and the Base Station shall maintain connectivity at an open-air separation distance of at least 9 meters. | HIGH | STABLE | Test |
| SRS-INT-0010 | The system shall encrypt all BLE data-bearing links using AES-128 CCM. | CRITICAL | STABLE | Test |
| SRS-INT-0011 | The system shall establish BLE pairing between the collar device and the Base Station using LE Secure Connections. | CRITICAL | STABLE | Test |
| SRS-INT-0012 | The system shall support out-of-band BLE pairing initiated via a QR-code-based exchange between the collar device and the Base Station. | HIGH | STABLE | Test |
| SRS-INT-0013 | The BLE radio interface shall conform to the radio-equipment regulations applicable in each target market, including FCC 47 CFR Part 15 Subpart C (US), RED 2014/53/EU (EU), UK Radio Equipment Regulations 2017 (UK), ISED RSS-247 (CA), and AS/NZS 4268:2017 (AU/NZ). | CRITICAL | STABLE | Test |
| SRS-INT-0014 | The BLE radio interface shall hold a Bluetooth SIG Qualified Design ID (QDID). | CRITICAL | STABLE | Inspection |
| SRS-INT-0015 | The BLE radio interface should undergo an RF human-exposure assessment against IEC 62311 / FCC 47 CFR §1.1310 for continuously worn 2.4 GHz transmission. | MEDIUM | VOLATILE | Analysis |

### 10.2 Wi-Fi Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0016 | The Base Station shall implement a Wi-Fi radio interface operating in the 2.4 GHz band conforming to IEEE 802.11 b/g/n. | HIGH | STABLE | Test |
| SRS-INT-0017 | The Base Station shall encrypt all Wi-Fi-based cloud uplink traffic using TLS 1.3. | CRITICAL | STABLE | Test |
| SRS-INT-0018 | The Base Station shall establish a Wi-Fi connection using default configuration settings of an IEEE 802.11 b/g/n access point. | MEDIUM | STABLE | Test |
| SRS-INT-0019 | The Base Station shall maintain cloud connectivity under a home Wi-Fi signal condition of at least −70 dBm RSSI at 2.4 GHz with at least 256 kbps sustained uplink throughput. | MEDIUM | LIKELY-CHANGE | Test |
| SRS-INT-0020 | The Wi-Fi radio interface shall conform to the radio-equipment regulations applicable in each target market, including FCC 47 CFR Part 15 Subpart C (US) and RED 2014/53/EU (EU). | CRITICAL | STABLE | Test |

### 10.3 GNSS Interface (Max Only)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0021 | The Max collar variant shall implement a passive (receive-only) GNSS interface. | HIGH | STABLE | Test |
| SRS-INT-0022 | The Mini collar variant shall not implement a GNSS interface. | MEDIUM | STABLE | Inspection |
| SRS-INT-0023 | The Max collar variant shall support a user-configurable GNSS fix interval between 30 minutes and 24 hours inclusive. | HIGH | STABLE | Test |
| SRS-INT-0024 | The Max collar variant shall apply a default GNSS fix interval of 2 hours. | MEDIUM | STABLE | Test |
| SRS-INT-0025 | The Max collar variant shall receive Assisted-GPS (A-GPS) assistance data via the BLE synchronization interface. | HIGH | STABLE | Test |
| SRS-INT-0026 | The Max collar variant shall treat A-GPS assistance data as valid for up to 72 hours without a refresh from the cloud. | MEDIUM | STABLE | Test |
| SRS-INT-0027 | The Max collar variant shall disable the GNSS interface while the device-local home/away state machine determines the HOME state. | HIGH | STABLE | Test |
| SRS-INT-0028 | The Max collar variant shall abandon a GNSS fix acquisition attempt after 90 seconds without a successful fix. | HIGH | STABLE | Test |
| SRS-INT-0029 | The Max collar variant shall acquire a warm GNSS fix using A-GPS assistance within 60 seconds. | MEDIUM | STABLE | Test |
| SRS-INT-0030 | The GNSS receive-only interface should be treated as exempt from intentional-radiator certification requirements in each target market, pending per-market confirmation. | MEDIUM | VOLATILE | Analysis |

### 10.4 Pogo-Pin Charging Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0031 | The charging interface between the collar device and the charging cradle shall use a 2-contact pogo-pin arrangement carrying VBUS and GND. | CRITICAL | STABLE | Inspection |
| SRS-INT-0032 | The charging interface shall employ magnetic alignment to seat the collar device onto the charging contacts. | CRITICAL | STABLE | Demonstration |
| SRS-INT-0033 | The magnetic charging alignment shall achieve correct first-attempt seating in at least 90% of docking attempts made at an approach distance of up to 5 mm. | MEDIUM | STABLE | Test |
| SRS-INT-0034 | The collar device shall reach full charge within 2 hours when docked at the charging interface. | HIGH | STABLE | Test |
| SRS-INT-0035 | The collar device shall maintain IP67 ingress protection at the charging interface when undocked and unmated from any CCF. | CRITICAL | STABLE | Test |
| SRS-INT-0036 | The charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | MEDIUM | LIKELY-CHANGE | Test |
| SRS-INT-0037 | The collar device shall be removed from the CCF via a 90-degree counter-clockwise Twist-Lock rotation to access the charging interface. | HIGH | STABLE | Demonstration |
| SRS-INT-0038 | The exposed Twist-Lock/charging socket, when the collar device is absent, shall not admit a 12 mm probe to a depth that creates a snag or entrapment feature. | HIGH | LIKELY-CHANGE | Test |

### 10.5 Twist-Lock Mechanical Interface

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0039 | The Twist-Lock interface shall consist of three lugs arranged at 120-degree spacing with asymmetric keying for correct-orientation insertion. | CRITICAL | STABLE | Inspection |
| SRS-INT-0040 | The Twist-Lock engagement shall require a 90-degree clockwise rotation from insertion to fully locked position. | HIGH | STABLE | Test |
| SRS-INT-0041 | Each Twist-Lock lug shall have a width of 3.5 mm ± 0.1 mm, a depth of 1.8 mm ± 0.1 mm, and a root radius of 0.5 mm minimum. | HIGH | STABLE | Inspection |
| SRS-INT-0042 | The Twist-Lock shall incorporate a spring-loaded detent that provides tactile confirmation of full engagement at the 90-degree locked position. | HIGH | STABLE | Test |
| SRS-INT-0043 | The Twist-Lock shall not require an axial press-in force exceeding 5 N nor a rotational torque exceeding 0.10 N·m for full engagement. | HIGH | STABLE | Test |
| SRS-INT-0044 | The Twist-Lock detent shall release at a torque within the range of 0.05 N·m to 0.10 N·m inclusive. | HIGH | STABLE | Test |
| SRS-INT-0045 | The Twist-Lock interface shall withstand an axial pull-off force greater than 100 N without releasing. | CRITICAL | STABLE | Test |
| SRS-INT-0046 | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket. | HIGH | STABLE | Test |
| SRS-INT-0047 | The Twist-Lock interface shall require no more than 0.10 N·m of rotational torque to engage or release. | HIGH | STABLE | Test |
| SRS-INT-0048 | The Twist-Lock interface shall provide an audible and tactile click upon full engagement. | MEDIUM | STABLE | Demonstration |
| SRS-INT-0049 | A magnetic insert shall draw the device into Twist-Lock alignment from a distance of up to 5 mm before lug-channel engagement. | MEDIUM | STABLE | Test |
| SRS-INT-0050 | The Twist-Lock interface shall be operable without tools. | HIGH | STABLE | Demonstration |
| SRS-INT-0051 | The Twist-Lock mechanism shall be engageable within 5 seconds. | LOW | STABLE | Test |

### 10.6 Device-Enforced BLE Application Protocol

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-INT-0052 | The system shall use a common device-enforced BLE application protocol shared across all collar and Base Station firmware variants. | HIGH | STABLE | Inspection |
| SRS-INT-0053 | The device-enforced protocol shall support transport of behavioral classification records as a distinct payload type. | HIGH | STABLE | Test |
| SRS-INT-0054 | The Base Station shall include in each BLE sighting report: the collar device identifier, RSSI value, and UTC timestamp. | HIGH | STABLE | Test |
| SRS-INT-0055 | The device-enforced protocol shall support transport of cloud-originated downlink payloads, comprising configuration data and OTA firmware images, as a distinct payload type. | HIGH | STABLE | Test |
| SRS-INT-0056 | The Base Station shall relay collar behavioral payloads to the cloud without semantically interpreting their content. | HIGH | STABLE | Inspection |
| SRS-INT-0057 | The collar device shall retain a buffered classification record in its local FIFO until it receives a positive acknowledgment (ACK) for that record from the Base Station. | HIGH | STABLE | Test |
| SRS-INT-0058 | The collar device shall not clear a buffered classification record from its FIFO solely as a result of a BLE disconnection. | HIGH | STABLE | Test |
| SRS-INT-0059 | The device-enforced protocol shall include sequence identifiers sufficient to detect loss of a classification record during forwarding over BLE. | HIGH | STABLE | Test |
| SRS-INT-0060 | The device-enforced protocol shall forward classification records over BLE without introducing data corruption. | HIGH | STABLE | Test |

---

## 11. Hardware, Physical, and Mechanical Requirements

This section specifies the physical, component-level, and mechanical hardware constraints of the LUUCIPet collar device and the CCF accessory. Behavior of components is specified in the referenced functional and interface sections.

### 11.1 Weight and Form Factor

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0001 | The Mini collar device shall have a total mass of no more than 10 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, excluding the CCF and collar. | CRITICAL | STABLE | Test |
| SRS-HW-0002 | The Max collar device shall have a total mass of no more than 22 grams, comprising PCB, battery, enclosure, and Twist-Lock receiver, excluding the CCF and collar. | CRITICAL | STABLE | Test |

### 11.2 Enclosure and Ingress Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0003 | The collar device shall achieve an IP67 ingress-protection rating per IEC 60529 when standalone, undocked, and unmated from any CCF. | CRITICAL | STABLE | Test |
| SRS-HW-0004 | The collar device enclosure shall maintain the IP67 seal boundary across the exposed pogo-pin charging contacts when undocked. | CRITICAL | STABLE | Test |
| SRS-HW-0005 | The collar device shall provide a light-emitting-diode (LED) status indicator. | MEDIUM | STABLE | Inspection |

### 11.3 Mechanical and Structural Constraints

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0006 | The collar device enclosure shall provide a wall thickness of no less than 1.5 millimeters at the base of each Twist-Lock lug channel. | HIGH | STABLE | Inspection |
| SRS-HW-0007 | The Twist-Lock lug channels and magnetic insert on the device underside shall not penetrate the enclosure wall or the ingress seal path. | CRITICAL | STABLE | Inspection |
| SRS-HW-0008 | The device-facing charging socket shall drain to no more than 0.2 mL of residual water within 15 seconds after being filled with 5 mL of water, with the collar device held in its normal worn orientation (socket facing 0 to 45 degrees from vertical). | MEDIUM | LIKELY-CHANGE | Test |

### 11.4 CCF Material Composition

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0009 | The CCF body shall be moulded from glass-fibre-reinforced polyamide 66 (PA66-GF30). | HIGH | LIKELY-CHANGE | Inspection |
| SRS-HW-0010 | The CCF material shall incorporate a UV stabiliser at a concentration of 0.3% to 0.5% by mass together with a hydrolysis stabiliser. | HIGH | LIKELY-CHANGE | Inspection |
| SRS-HW-0011 | The CCF shall not contain any metallic sub-component within the Zone 2 snap/breakaway region. | CRITICAL | STABLE | Inspection |
| SRS-HW-0012 | Animal-contact surfaces of the device and CCF shall not use chrome or nickel plating. | HIGH | STABLE | Inspection |

### 11.5 Sensing Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0013 | The collar device shall incorporate a three-axis MEMS accelerometer. | CRITICAL | STABLE | Inspection |
| SRS-HW-0014 | The collar device accelerometer shall support an output data rate of no less than 50 Hz. | CRITICAL | STABLE | Test |
| SRS-HW-0015 | The collar device accelerometer shall provide a wake-on-motion interrupt and a hardware FIFO buffer of no less than 512 bytes accessible via direct memory access. | HIGH | STABLE | Inspection |
| SRS-HW-0016 | The Mini collar device shall not incorporate a GNSS receiver. | MEDIUM | STABLE | Inspection |
| SRS-HW-0017 | The Max collar device shall incorporate a passive receive-only GNSS receiver. | HIGH | STABLE | Inspection |

### 11.6 Wireless Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0018 | The collar device shall incorporate a Bluetooth Low Energy 5.x radio. | CRITICAL | STABLE | Inspection |
| SRS-HW-0019 | The collar device BLE radio shall be capable of a transmit power of no less than +8 dBm. | MEDIUM | STABLE | Test |

### 11.7 Battery Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0020 | The Mini collar device shall incorporate a battery cell of no less than 120 mAh nominal capacity. | HIGH | STABLE | Inspection |
| SRS-HW-0021 | The Max collar device shall incorporate a battery cell of no less than 400 mAh nominal capacity. | HIGH | STABLE | Inspection |
| SRS-HW-0022 | The collar device battery subsystem shall provide overcharge, over-discharge, short-circuit, and over-temperature protection. | CRITICAL | STABLE | Test |
| SRS-HW-0023 | The collar device battery shall pass UN 38.3 qualification testing before pilot production. | HIGH | STABLE | Test |
| SRS-HW-0024 | The collar device shall raise a low-battery alert at a state-of-charge of 20% or below. | MEDIUM | STABLE | Test |

### 11.8 Charging Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0025 | The collar device shall incorporate a 2-contact pogo-pin charging arrangement carrying VBUS and GND with a magnetic-alignment insert. | CRITICAL | STABLE | Inspection |

### 11.9 Non-Volatile Storage Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0026 | The collar device shall incorporate non-volatile storage sufficient to retain no less than 30 days of behavioral-classification summary data. | HIGH | STABLE | Test |

### 11.10 Compute Hardware

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-HW-0027 | The collar device shall incorporate a compute subsystem capable of executing the behavioral-classification inference on-device without cloud connectivity. | CRITICAL | STABLE | Test |
| SRS-HW-0028 | The collar device compute subsystem shall provide direct-memory-access peripheral access and a hardware root of trust. | CRITICAL | STABLE | Inspection |

