
## 4. Functional Requirements — Data Sync and Connectivity

This section specifies the requirements governing the data synchronization and connectivity behavior across the collar device, Base Station, and cloud device-management layer. It defines the BLE device-to-base link, record forwarding and synchronization, base-to-cloud gateway behavior, multi-base-station operation, Insight-mode activation over connectivity, GNSS location data synchronization (Max variant), and connectivity-loss degraded behavior.

### 4.1 BLE Device-to-Base Link and Pairing

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0001 | The system shall operate the collar-mounted device in the BLE peripheral role relative to the Base Station. | HIGH | STABLE | Inspection |
| SRS-CONN-0002 | The system shall operate the Base Station in the BLE central role relative to the collar-mounted device. | HIGH | STABLE | Inspection |
| SRS-CONN-0003 | The system shall support pairing between the collar-mounted device and the Base Station using QR-code out-of-band exchange. | HIGH | STABLE | Demonstration |
| SRS-CONN-0004 | The system shall advertise the presence of the collar-mounted device at a default interval of 60 seconds. | MEDIUM | STABLE | Test |
| SRS-CONN-0005 | The system shall support configuration of the BLE advertising interval within the range of 1 to 180 seconds. | MEDIUM | STABLE | Test |
| SRS-CONN-0006 | The system shall maintain a BLE link between the collar-mounted device and the Base Station across an open-air separation distance of no less than 9 meters. | HIGH | STABLE | Test |
| SRS-CONN-0007 | The system shall transmit BLE signals at a power level of no less than +8 dBm. | MEDIUM | STABLE | Test |
| SRS-CONN-0008 | The system shall randomize the BLE device address of the collar-mounted device. | HIGH | STABLE | Test |
| SRS-CONN-0009 | The system shall establish the BLE link between the collar-mounted device and the Base Station over the secured connection defined in Section 8 (Security). | CRITICAL | STABLE | Inspection |
| SRS-CONN-0010 | Upon the collar-mounted device re-entering BLE range of a Base Station, the system shall automatically re-establish the BLE link without requiring manual user action. | CRITICAL | STABLE | Test |

### 4.2 Record Forwarding and Synchronization

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0011 | Upon establishing a BLE link with a Base Station, the system shall forward stored classification records from the collar-mounted device to the Base Station. | CRITICAL | STABLE | Test |
| SRS-CONN-0012 | The system shall forward stored classification records to the Base Station using a best-effort, event-triggered transport pattern. | HIGH | STABLE | Inspection |
| SRS-CONN-0013 | Upon regaining BLE connectivity to a Base Station following a period of disconnection, the system shall forward all classification records accumulated during that disconnection. | CRITICAL | STABLE | Test |

### 4.3 Base-to-Cloud Gateway and Upload

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0014 | The Base Station shall transmit received classification records to the cloud endpoint over the secured Wi-Fi link. | CRITICAL | STABLE | Test |
| SRS-CONN-0015 | When the Wi-Fi or cloud connection is unavailable, the Base Station shall buffer received classification records pending upload. | CRITICAL | STABLE | Test |
| SRS-CONN-0016 | Upon restoration of the Wi-Fi or cloud connection, the Base Station shall upload all buffered classification records. | CRITICAL | STABLE | Test |
| SRS-CONN-0017 | The Base Station shall not discard a received classification record while that record is pending upload to the cloud. | CRITICAL | STABLE | Test |
| SRS-CONN-0018 | The IoT Cloud backend shall accept and acknowledge classification records uploaded by the Base Station. (External: IoT Cloud backend team.) | CRITICAL | STABLE | Inspection — external conformance evidence |
| SRS-CONN-0030 | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the Base Station shall retry uploading the affected buffered classification record. | HIGH | VOLATILE | Demonstration |

### 4.4 Multi-Base-Station Behavior and Handover

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0019 | The system shall forward stored classification records to any paired Base Station currently in BLE range, without requiring a specific designated Base Station. | HIGH | STABLE | Test |
| SRS-CONN-0020 | The system shall forward each classification record to only the first paired Base Station through which it establishes a BLE link, among those in range. | HIGH | STABLE | Test |
| SRS-CONN-0021 | The IoT Cloud backend shall deduplicate classification records that may be uploaded from more than one Base Station within the same household account. (External: IoT Cloud backend team.) | HIGH | STABLE | Inspection — external conformance evidence |

### 4.5 Insight-Mode Activation over Connectivity

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0022 | Upon receiving an Insight-mode activation command over the BLE link, the system shall activate Insight mode. | HIGH | STABLE | Test |
| SRS-CONN-0023 | The Mobile App shall issue the Insight-mode activation command to the collar-mounted device. (External: Mobile App team.) | HIGH | STABLE | Inspection — external conformance evidence |

### 4.6 GNSS Location Data Synchronization (Max Variant)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0024 | On the Max product variant, the system shall forward location-tagged classification records through the same record-forwarding path used for other classification records. | MEDIUM | STABLE | Test |
| SRS-CONN-0025 | While the GNSS smart power gate suspends fix acquisition in the HOME state, the system shall continue to synchronize the most recently acquired GNSS fix as part of classification records. | MEDIUM | STABLE | Test |

### 4.7 Connectivity-Loss and Degraded Behavior

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-CONN-0026 | The system shall not lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. | CRITICAL | STABLE | Analysis |
| SRS-CONN-0027 | Upon loss of the BLE link to all Base Stations, the system shall continue local classification and storage without interruption. | CRITICAL | STABLE | Demonstration |
| SRS-CONN-0028 | The system shall enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. | HIGH | STABLE | Test |
| SRS-CONN-0029 | The system shall exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. | HIGH | STABLE | Test |

---

## 5. Functional Requirements — OTA Firmware Updates

This section specifies the requirements for over-the-air firmware update capability across all collar device variants and Base Station tiers. It defines OTA applicability, delivery path and transport security, collar install preconditions, image integrity and anti-rollback mechanisms, install resilience, update notification and status reporting, and release-artifact obligations.

### 5.1 OTA Applicability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0043 | The system shall provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). | CRITICAL | STABLE | Demonstration |
| SRS-FUNC-0044 | The system shall provide over-the-air firmware update capability on every Base Station tier (Charging and Relay). | CRITICAL | STABLE | Demonstration |

### 5.2 OTA Delivery Path and Transport

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0045 | The system shall transport OTA firmware images from the cloud to the Base Station over Wi-Fi using TLS version 1.3. | HIGH | STABLE | Test |
| SRS-FUNC-0046 | The system shall stage a received collar OTA firmware image at the Base Station prior to delivery of that image to the collar-mounted device. | MEDIUM | STABLE | Test |
| SRS-FUNC-0047 | The system shall deliver a staged OTA firmware image from the Base Station to the collar-mounted device over the secured BLE link defined in Section 8 (Security). | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0048 | The system shall update Base Station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. | HIGH | STABLE | Demonstration |

### 5.3 Collar Install Preconditions

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0049 | The system shall install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. | CRITICAL | STABLE | Test |
| SRS-FUNC-0050 | The system shall not allow the charging-cradle-docked install precondition to be bypassed by any remote command. | CRITICAL | STABLE | Test |
| SRS-FUNC-0051 | The system shall require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. | HIGH | STABLE | Test |

### 5.4 OTA Image Integrity and Anti-Rollback

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0052 | The system shall require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. | CRITICAL | STABLE | Inspection |
| SRS-FUNC-0053 | The system shall verify the signature of an OTA firmware image before committing or executing that image. | CRITICAL | STABLE | Test |
| SRS-FUNC-0054 | The system shall prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. | CRITICAL | STABLE | Test |

### 5.5 Install Resilience

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0055 | The system shall install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. | CRITICAL | STABLE | Test |
| SRS-FUNC-0056 | The system shall automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. | CRITICAL | STABLE | Test |
| SRS-FUNC-0057 | The system shall not enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. | CRITICAL | STABLE | Analysis |

### 5.6 Update Notification and Status

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0058 | The system shall report the current OTA update state as one of: Downloading, Verifying, Pending Installation, Installing, Success, or Failed. | MEDIUM | STABLE | Test |
| SRS-FUNC-0059 | The Mobile App shall notify the user when an OTA firmware update is available. (External: Mobile App team.) | MEDIUM | STABLE | Inspection — external conformance evidence |
| SRS-FUNC-0060 | The Mobile App shall display the current OTA update state reported by the device. (External: Mobile App team.) | MEDIUM | STABLE | Inspection — external conformance evidence |

### 5.7 Release Artifacts and Tier-2 Delivery Channel

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-FUNC-0061 | The system shall produce a Software Bill of Materials for every OTA firmware release. | MEDIUM | STABLE | Inspection |
| SRS-FUNC-0062 | The system shall deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. | HIGH | STABLE | Inspection |

---

## 6. Performance Requirements

This section specifies the quantitative performance criteria the system must meet. It addresses battery-life performance across collar variants, classification and data-path latency, location-acquisition timing, system startup timing, and physical-interaction timing.

### 6.1 Battery-Life Performance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0001 | The system's Mini variant shall meet or exceed the battery-life minimums specified in Section 11.7 (Table 11-2) across typical-use, minimum, and Longevity Mode operating conditions. | HIGH | STABLE | Analysis |
| SRS-PERF-0002 | The system's Max variant shall meet or exceed the battery-life minimums specified in Section 11.7 (Table 11-2) across all supported GNSS fix-interval settings. | HIGH | STABLE | Analysis |

### 6.2 Classification and Data-Path Latency

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0003 | The system shall produce a classification result within 2 seconds of the triggering motion event. | HIGH | STABLE | Test |
| SRS-PERF-0004 | The Base Station shall upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. | MEDIUM | STABLE | Test |

### 6.3 Location and Startup Timing (Max Variant)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0005 | On the Max product variant, the system shall acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. | MEDIUM | STABLE | Test |

### 6.4 Startup and Physical-Interaction Timing

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-PERF-0006 | The collar-mounted device shall complete boot within 3 seconds under cold power-on and wake-from-reset conditions. | MEDIUM | STABLE | Test |
| SRS-PERF-0007 | The system shall update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. | HIGH | STABLE | Test |
| SRS-PERF-0008 | The system shall allow the Twist-Lock mechanism to be engaged within 5 seconds. | LOW | STABLE | Test |

---

## 7. Safety Requirements

This section specifies the safety requirements for the LUUCIPet system, with emphasis on the CCF compound-architecture: Zone 2 Fuse Tab strangulation-prevention breakaway (the primary pet-safety mechanism), Zone 1 structural retention, Twist-Lock charging-removal retention, post-breakaway protocol and re-use prevention, chew resistance, device-absent socket entrapment prevention, animal-contact material safety, and battery-ingestion warning.

### 7.1 Zone 2 Fuse Tab — Strangulation-Prevention Breakaway

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0001 | The Zone 2 Fuse Tab of the CCF-S variant shall fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 15 N to 20 N. | CRITICAL | STABLE | Test |
| SRS-SAFE-0002 | The Zone 2 Fuse Tab of the CCF-M variant shall fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 20 N to 28 N. | CRITICAL | STABLE | Test |
| SRS-SAFE-0003 | The Zone 2 Fuse Tab of the CCF-L variant shall fracture and release the CCF body and device from the Zone 1 clamp when the axial load applied to it is within the range of 28 N to 40 N, under the design-basis condition that the assembled device-plus-CCF mass does not exceed 26 g. | CRITICAL | STABLE | Test |
| SRS-SAFE-0004 | If the assembled device-plus-CCF-L mass exceeds 26 g, the CCF-L Zone 2 breakaway force floor shall be revised upward to 30 N. | CRITICAL | LIKELY-CHANGE | Analysis |
| SRS-SAFE-0005 | The Zone 2 Fuse Tab shall not be capable of being reused or restored to a load-bearing state after fracture. | CRITICAL | STABLE | Test |
| SRS-SAFE-0006 | Upon fracture, the Zone 2 Fuse Tab shall not produce a detached fragment separate from the CCF body. | HIGH | STABLE | Inspection |
| SRS-SAFE-0007 | The fracture surfaces of the Zone 2 Fuse Tab remaining after breakaway shall be blunt, presenting no sharp edge. | HIGH | STABLE | Inspection |
| SRS-SAFE-0008 | The CCF shall present a visible fracture indicator upon Zone 2 breakaway. | HIGH | STABLE | Inspection |

### 7.2 Zone 1 — Structural Retention (Non-Breakaway)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0009 | The Zone 1 clamp shall retain axial loads of at least 50 N without structural failure. | CRITICAL | STABLE | Test |
| SRS-SAFE-0010 | The Zone 1 clamp shall remain structurally intact following a Zone 2 fracture event. | CRITICAL | STABLE | Test |

### 7.3 Twist-Lock — Retention Safety (Non-Breakaway)

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0011 | The Twist-Lock device-to-CCF interface shall retain axial loads exceeding 100 N without disengaging. | CRITICAL | STABLE | Test |
| SRS-SAFE-0012 | The Twist-Lock shall remain engaged under inertial loads generated by pet head-shake motion up to 50 g. | HIGH | STABLE | Test |

### 7.4 Post-Breakaway Protocol and Re-Use Prevention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0013 | The device shall not be worn on an animal without a CCF that has an intact (unfractured) Zone 2 Fuse Tab. | CRITICAL | STABLE | Inspection |
| SRS-SAFE-0014 | The device shall emit a detectable separation signature upon Zone 2 breakaway. | HIGH | STABLE | Test |
| SRS-SAFE-0015 | The Mobile App shall notify the owner that CCF replacement is required upon receiving a device separation signature. (External: Mobile App team.) | HIGH | STABLE | Inspection — external conformance evidence |

### 7.5 Chew Resistance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0016 | The Zone 2 Fuse Tab shall not fracture under a compressive load below 250 N. | CRITICAL | STABLE | Test |
| SRS-SAFE-0017 | The CCF body shall resist penetration for at least 30 seconds under a 250 N compressive load. | HIGH | STABLE | Test |
| SRS-SAFE-0018 | Materials in animal-skin contact on the device enclosure shall resist chew-induced damage. | MEDIUM | LIKELY-CHANGE | Analysis |

### 7.6 Device-Absent Socket — Entrapment Prevention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0019 | The CCF socket shall present no independent entrapment hazard when the device is absent. | HIGH | STABLE | Analysis |
| SRS-SAFE-0020 | The device-absent CCF socket shall provide clearance verified against a 12 mm entrapment-probe criterion. | MEDIUM | LIKELY-CHANGE | Test |

### 7.7 Animal-Contact Material Safety

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0021 | Materials in animal-skin contact shall be non-toxic. | HIGH | STABLE | Inspection |

### 7.8 Battery-Ingestion Warning

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SAFE-0022 | The system shall provide battery-ingestion warning labeling. | HIGH | STABLE | Inspection |

---

## 8. Security Requirements

This section specifies the security requirements governing the LUUCIPet system. It defines BLE link-layer security, cloud-bound transport security, device identity and platform trust (including secure boot anchored in a hardware root of trust), and the vulnerability-disclosure policy gate.

### 8.1 BLE Link-Layer Security

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0001 | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the Base Station using AES-128 CCM. | CRITICAL | STABLE | Test |
| SRS-SEC-0002 | The system shall establish the BLE pairing key exchange between the collar-mounted device and the Base Station using the LE Secure Connections method. | CRITICAL | STABLE | Test |

### 8.2 Cloud-Bound Transport Security

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0003 | The system shall use TLS version 1.3 exclusively for all data transport between the Base Station and the cloud. | CRITICAL | STABLE | Test |

### 8.3 OTA Firmware Trust Chain

No firmware image may be installed without passing the Section 5 verification chain (SRS-FUNC-0052, SRS-FUNC-0053, SRS-FUNC-0054). This architectural constraint is carried by reference to those requirements.

### 8.4 Device Identity and Platform Trust

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0004 | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. | CRITICAL | STABLE | Inspection |
| SRS-SEC-0005 | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. | CRITICAL | STABLE | Test |

### 8.5 Vulnerability Disclosure

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-SEC-0006 | The system shall have a public vulnerability-disclosure policy in place before product launch. | HIGH | STABLE | Inspection |

