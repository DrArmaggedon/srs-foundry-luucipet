> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

CAT: **CONN** | Maps to: PRD §8 (Data Sync), §6.3–§6.5 (Connectivity), §10.3 (Radios)
*(Drafter-authored; Conductor-persisted to shared store. §4 v1 COMPLETE — 30 blocks, SRS-CONN-0001…0030.)*

## 4.1 BLE Device↔Base Link & Pairing

**SRS-CONN-0001** | BLE Role Assignment — Collar as Peripheral | The system **shall** operate the collar-mounted device in the BLE peripheral role relative to the base station. | Priority: HIGH | Stability: STABLE | Source: [PRD §6.3] | VM: Inspection | XR: SRS-CONN-0002

**SRS-CONN-0002** | BLE Role Assignment — Base Station as Central | The system **shall** operate the base station in the BLE central role relative to the collar-mounted device. | Priority: HIGH | Stability: STABLE | Source: [PRD §6.3] | VM: Inspection | XR: SRS-CONN-0001

**SRS-CONN-0003** | QR-Code Out-of-Band Pairing | The system **shall** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. | Priority: HIGH | Stability: STABLE | Source: [PRD §6.3] | VM: Demonstration

**SRS-CONN-0004** | Default BLE Advertising Interval | The system **shall** advertise the presence of the collar-mounted device at a default interval of 60 seconds. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §6.3] | VM: Test | XR: SRS-CONN-0005

**SRS-CONN-0005** | Configurable Advertising Interval Range | The system **shall** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §6.3] | VM: Test | XR: SRS-CONN-0004

**SRS-CONN-0006** | Minimum Open-Air BLE Range | The system **shall** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. | Priority: HIGH | Stability: STABLE | Source: [PRD §6.3] | VM: Test | XR: SRS-CONN-0007

**SRS-CONN-0007** | Minimum BLE Transmit Power | The system **shall** transmit BLE signals at a power level of no less than +8 dBm. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §6.3] | VM: Test | XR: SRS-CONN-0006

**SRS-CONN-0008** | BLE Address Randomization | The system **shall** randomize the BLE device address of the collar-mounted device. | Priority: HIGH | Stability: STABLE | Source: [PRD §6.3] | VM: Test

**SRS-CONN-0009** | Secured BLE Link Establishment | The system **shall** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §6.3] | VM: Inspection | XR: — (§8 Security, not yet drafted)

**SRS-CONN-0010** | Automatic BLE Reconnection on Range Re-Entry | Upon the collar-mounted device re-entering BLE range of a base station, the system **shall** automatically re-establish the BLE link without requiring manual user action. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §6.4], [PRD §8.5] | VM: Test | XR: SRS-CONN-0001, SRS-CONN-0002

## 4.2 Record Forwarding & Sync

**SRS-CONN-0011** | Classification Record Forwarding on BLE Contact | Upon establishing a BLE link with a base station, the system **shall** forward stored classification records from the collar-mounted device to the base station. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8], [PRD §6.4] | VM: Test | XR: SRS-FUNC-0026, SRS-FUNC-0028

**SRS-CONN-0012** | Best-Effort Event-Triggered Record Transport | The system **shall** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. | Priority: HIGH | Stability: STABLE | Source: [PRD §8.5] | VM: Inspection | XR: SRS-FUNC-0002, SRS-FUNC-0003

**SRS-CONN-0013** | Sync Resumption of Accumulated Records After Reconnection | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **shall** forward all classification records accumulated during that disconnection. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8], [PRD §8.5] | VM: Test | XR: SRS-FUNC-0027, SRS-CONN-0011

## 4.3 Base↔Cloud Gateway & Upload

**SRS-CONN-0014** | Base Station Upload of Received Records to Cloud | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8], [PRD §6.5] | VM: Test | XR: SRS-CONN-0011, SRS-CONN-0009

**SRS-CONN-0015** | Base Station Buffering on Upload-Path Unavailability | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.5] | VM: Test | XR: SRS-CONN-0016

**SRS-CONN-0016** | Buffered Record Upload on Path Restoration | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.5] | VM: Test | XR: SRS-CONN-0015

**SRS-CONN-0017** | No Discard of Received Records Pending Upload | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.5] | VM: Test | XR: SRS-FUNC-0027, SRS-CONN-0015

**SRS-CONN-0018** | Cloud Acceptance and Acknowledgment of Uploaded Records (external) | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8], [EXTERNAL: IoT Cloud backend team] | VM: Inspection (external conformance evidence) | XR: SRS-CONN-0014

**SRS-CONN-0030** | Base Station Upload Retry on Transient Failure | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **shall** retry uploading the affected buffered classification record. | Priority: HIGH | Stability: VOLATILE | Source: [PRD §8.5] | VM: Demonstration | XR: SRS-CONN-0015, SRS-CONN-0016

## 4.4 Multi-Base-Station Behavior & Handover

**SRS-CONN-0019** | Collar Forwarding to Any In-Range Paired Base Station | The system **shall** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.2], [PRD §8] | VM: Test | XR: SRS-CONN-0011

**SRS-CONN-0020** | Single Forwarding of Each Record to First Available Base Station | The system **shall** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in range. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.2], [PRD §8] | VM: Test | XR: SRS-CONN-0019, SRS-CONN-0021

**SRS-CONN-0021** | Cloud-Side Deduplication of Multi-Base Uploads (external) | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household account. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.2], [EXTERNAL: IoT Cloud backend team] | VM: Inspection (external conformance evidence) | XR: SRS-CONN-0020, SRS-CONN-0018

## 4.5 Insight-Mode Activation over Connectivity

**SRS-CONN-0022** | Device-Side Insight-Mode Activation on Command Receipt | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.1], [PRD §6.4] | VM: Test | XR: SRS-FUNC-0007, SRS-FUNC-0008, SRS-FUNC-0009

**SRS-CONN-0023** | Mobile App Issuance of Insight-Mode Activation Command (external) | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.1], [EXTERNAL: Mobile App team] | VM: Inspection (external conformance evidence) | XR: SRS-CONN-0022

## 4.6 GNSS Location Data Sync (Max Variant)

**SRS-CONN-0024** | Sync of Location-Tagged Records via Standard Forwarding Path | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other classification records. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §7.5], [PRD §8] | VM: Test | XR: SRS-FUNC-0025, SRS-CONN-0011

**SRS-CONN-0025** | Sync of Most-Recent GNSS Fix During Home Power-Gate | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix as part of classification records. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §7.5], [PRD §6.3] | VM: Test | XR: SRS-FUNC-0025, SRS-OPER-0004

## 4.7 Connectivity-Loss & Degraded Behavior

**SRS-CONN-0026** | No Record Loss Due to Any Connectivity-Loss Condition | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.5] | VM: Analysis | XR: SRS-FUNC-0027, SRS-CONN-0017

**SRS-CONN-0027** | Continued Local Classification During BLE Loss | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.6], [PRD §8.5] | VM: Demonstration | XR: SRS-FUNC-0028, SRS-FUNC-0027

**SRS-CONN-0028** | Degraded-Mode Entry Below Home Wi-Fi Reliability Bound | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. | Priority: HIGH | Stability: STABLE | Source: [ASSUMPTION: A-0009] | VM: Test | XR: SRS-OPER-0007

**SRS-CONN-0029** | Degraded-Mode Exit on Wi-Fi Reliability Restoration | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. | Priority: HIGH | Stability: STABLE | Source: [ASSUMPTION: A-0009] | VM: Test | XR: SRS-OPER-0007, SRS-CONN-0028

---

### SRS-ID Inventory & Draft Status (§4 v1 — COMPLETE)
- **§4 v1 fully drafted: 30 blocks, SRS-CONN-0001 … SRS-CONN-0030.**
- **26 in-scope + 4 external:** external = SRS-CONN-0018, SRS-CONN-0021 ([EXTERNAL: IoT Cloud backend team]); SRS-CONN-0023 ([EXTERNAL: Mobile App team]).
- Next free CONN ID = **SRS-CONN-0031**.
