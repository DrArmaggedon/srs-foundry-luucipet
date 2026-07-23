> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T21:00:00Z
⚠️ For full context, always refer to the Master SRS.

---


## 3. Behavioral Classification



## 3.1 Operating Modes

<a id="srs-func-0006"></a>

| **SRS-FUNC-0006** | **Wellness Mode as Default Operating Mode** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** operate in Wellness mode as its default power-optimized classification mode. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.1 · SRS-FUNC-0011 |

<a id="srs-func-0007"></a>

| **SRS-FUNC-0007** | **Insight Mode Availability On Demand** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.1 · SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="srs-func-0008"></a>

| **SRS-FUNC-0008** | **Insight Mode Continuous Sampling Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While in Insight mode, the system **shall** sample the accelerometer continuously at 50 Hz. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.1 · SRS-FUNC-0007, SRS-FUNC-0014 |

<a id="srs-func-0009"></a>

| **SRS-FUNC-0009** | **Insight Mode Auto-Revert to Wellness** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** automatically revert from Insight mode to Wellness mode without requiring a manual user action. |
| **Rationale**    | Derived from PRD §7.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0006, SRS-FUNC-0007 |

<a id="srs-func-0010"></a>

| **SRS-FUNC-0010** | **Wellness Mode Motion-Triggered Confirmation Burst** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon detecting motion, the system **shall** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. |
| **Rationale**    | Derived from PRD §7.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0011 |

<a id="srs-func-0011"></a>

| **SRS-FUNC-0011** | **Wellness Mode Idle Current Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While in Wellness mode and outside a confirmation burst, the system **shall not** exceed an idle current draw of 4 µA. |
| **Rationale**    | Derived from PRD §7.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.3 · SRS-FUNC-0006, SRS-FUNC-0010 |

<a id="srs-func-0012"></a>

| **SRS-FUNC-0012** | **Longevity Mode Shall Not Reduce Classification Sampling Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When Longevity Mode is active, the system **shall not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. |
| **Rationale**    | Derived from PRD §7.10. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.10 · SRS-FUNC-0014 |

<a id="srs-func-0013"></a>

| **SRS-FUNC-0013** | **Longevity Mode Shall Not Reduce Classification Accuracy** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When Longevity Mode is active, the system **shall not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. |
| **Rationale**    | Derived from PRD §7.10. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.10 · SRS-FUNC-0018, SRS-FUNC-0020

## 3.2 Sensing & Classification Pipeline |

<a id="srs-func-0014"></a>

| **SRS-FUNC-0014** | **Minimum Accelerometer Output Data Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** sample the accelerometer at a rate of no less than 50 Hz. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.2 · SRS-FUNC-0008, SRS-FUNC-0015 |

<a id="srs-func-0015"></a>

| **SRS-FUNC-0015** | **No Auxiliary Sensors for Tier-1 Classification** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.2 · SRS-FUNC-0014 |

<a id="srs-func-0016"></a>

| **SRS-FUNC-0016** | **Unified Classification Pipeline Across Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.2 · SRS-FUNC-0034 |

<a id="srs-func-0017"></a>

| **SRS-FUNC-0017** | **Species-Specific Threshold Assignment at Onboarding** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** set species-specific classification thresholds during the onboarding process. |
| **Rationale**    | Derived from PRD §7.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.2 · SRS-OPER-0003

## 3.3 Classification Accuracy & False-Positive Bounds |

<a id="srs-func-0018"></a>

| **SRS-FUNC-0018** | **Tier-1 Per-Class Accuracy Minimum** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0019 |

<a id="srs-func-0019"></a>

| **SRS-FUNC-0019** | **Tier-1 Per-Class False-Positive Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** exceed a false-positive rate of 5% for each Tier-1 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0018 |

<a id="srs-func-0020"></a>

| **SRS-FUNC-0020** | **Tier-2 Per-Class Accuracy Minimum** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0021 |

<a id="srs-func-0021"></a>

| **SRS-FUNC-0021** | **Tier-2 Per-Class False-Positive Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** exceed a false-positive rate of 10% for each Tier-2 behavior class. |
| **Rationale**    | Derived from PRD §7.4. | **Priority**     | High |
| **Stability**    | Likely-Change |
| **Verification** | Test |
| **Traceability** | PRD §7.4 · SRS-FUNC-0020

## 3.4 Classification Records & Local Storage |

<a id="srs-func-0022"></a>

| **SRS-FUNC-0022** | **Classification Record Contains Behavior Label** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** include a behavior class label in every generated classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 · SRS-FUNC-0023, SRS-FUNC-0024 |

<a id="srs-func-0023"></a>

| **SRS-FUNC-0023** | **Classification Record Contains Confidence Score** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** include a confidence score in the range 0.0 to 1.0 in every generated classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0024"></a>

| **SRS-FUNC-0024** | **Classification Record Timestamp Resolution** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** timestamp every classification record in UTC with a resolution no coarser than 1 second. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0025"></a>

| **SRS-FUNC-0025** | **Classification Record GNSS Fix on Max Variant** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** include the most recent GNSS fix in every generated classification record. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.5 · SRS-FUNC-0022 |

<a id="srs-func-0026"></a>

| **SRS-FUNC-0026** | **Minimum Local Retention of Classification Records** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** retain generated classification records locally for no less than 30 days without a cloud connection. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0027 |

<a id="srs-func-0027"></a>

| **SRS-FUNC-0027** | **No Record Discard on Connectivity Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** discard stored classification records upon loss of connectivity. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0026 |

<a id="srs-func-0028"></a>

| **SRS-FUNC-0028** | **Classification Generation Independent of BLE Connectivity** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** generate and record classifications independently of the current BLE connectivity state. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.6 · SRS-FUNC-0029 |

<a id="srs-func-0029"></a>

| **SRS-FUNC-0029** | **Record Forwarding Without Corruption** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records without data corruption. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 · SRS-FUNC-0030 |

<a id="srs-func-0030"></a>

| **SRS-FUNC-0030** | **Record Forwarding Without Sequence Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records without loss of their original sequence order. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.6 · SRS-FUNC-0029

## 3.5 Data Locality & On-Device Processing |

<a id="srs-func-0031"></a>

| **SRS-FUNC-0031** | **On-Device Signal Normalization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** normalize raw accelerometer data on-device prior to classification. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.7 · SRS-FUNC-0032, SRS-FUNC-0033 |

<a id="srs-func-0032"></a>

| **SRS-FUNC-0032** | **Raw Accelerometer Data Shall Not Leave the Collar** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** transmit raw accelerometer data off the collar. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.7 · SRS-FUNC-0031, SRS-FUNC-0033 |

<a id="srs-func-0033"></a>

| **SRS-FUNC-0033** | **No Cloud Round-Trip for Classification Decisions** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** produce classification decisions without requiring a round-trip to a cloud service. |
| **Rationale**    | Derived from PRD §7.7. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.7 · SRS-FUNC-0028, SRS-FUNC-0032

## 3.6 Tier-2 Extensibility via OTA |

<a id="srs-func-0034"></a>

| **SRS-FUNC-0034** | **Tier-2 Classifier Delivery via OTA** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. |
| **Rationale**    | Derived from PRD §7.9. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0016, SRS-FUNC-0035 |

<a id="srs-func-0035"></a>

| **SRS-FUNC-0035** | **Tier-2 Deployment Without Hardware Modification or Service Event** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. |
| **Rationale**    | Derived from PRD §7.9. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0034

## 3.7 Configurable Alert Thresholds (Scratching & Shaking) |

<a id="srs-func-0036"></a>

| **SRS-FUNC-0036** | **Device Application of Configured Scratching Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a Scratching alert threshold value received via the companion application. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0037, SRS-FUNC-0041 |

<a id="srs-func-0037"></a>

| **SRS-FUNC-0037** | **Firmware-Default Scratching Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036 |

<a id="srs-func-0038"></a>

| **SRS-FUNC-0038** | **Device Application of Configured Shaking Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a Shaking alert threshold value received via the companion application. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0039, SRS-FUNC-0042 |

<a id="srs-func-0039"></a>

| **SRS-FUNC-0039** | **Firmware-Default Shaking Alert Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | Medium |
| **Stability**    | Volatile |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0038 |

<a id="srs-func-0040"></a>

| **SRS-FUNC-0040** | **Alert Threshold Persistence Across OTA Updates** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036, SRS-FUNC-0038 |

<a id="srs-func-0041"></a>

| **SRS-FUNC-0041** | **App-Side Scratching Threshold Configuration UI (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036 |

<a id="srs-func-0042"></a>

| **SRS-FUNC-0042** | **App-Side Shaking Threshold Configuration UI (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0038

---

### SRS-ID inventory (§3 v1)
**In-scope (35):** SRS-FUNC-0006 … SRS-FUNC-0040.
**External (2):** SRS-FUNC-0041, SRS-FUNC-0042 ([EXTERNAL: Mobile App team]).
**Total: 37 blocks.** Next free FUNC ID = SRS-FUNC-0043. |

## 4. Data Sync Connectivity



## 4.1 BLE Device↔Base Link & Pairing

<a id="srs-conn-0001"></a>

| **SRS-CONN-0001** | **BLE Role Assignment — Collar as Peripheral** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** operate the collar-mounted device in the BLE peripheral role relative to the base station. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · SRS-CONN-0002 |

<a id="srs-conn-0002"></a>

| **SRS-CONN-0002** | **BLE Role Assignment — Base Station as Central** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** operate the base station in the BLE central role relative to the collar-mounted device. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · SRS-CONN-0001 |

<a id="srs-conn-0003"></a>

| **SRS-CONN-0003** | **QR-Code Out-of-Band Pairing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** support pairing between the collar-mounted device and the base station using QR-code out-of-band exchange. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 |

<a id="srs-conn-0004"></a>

| **SRS-CONN-0004** | **Default BLE Advertising Interval** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** advertise the presence of the collar-mounted device at a default interval of 60 seconds. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0005 |

<a id="srs-conn-0005"></a>

| **SRS-CONN-0005** | **Configurable Advertising Interval Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** support configuration of the BLE advertising interval within the range of 1 to 180 seconds. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0004 |

<a id="srs-conn-0006"></a>

| **SRS-CONN-0006** | **Minimum Open-Air BLE Range** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** maintain a BLE link between the collar-mounted device and the base station across an open-air separation distance of no less than 9 meters. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0007 |

<a id="srs-conn-0007"></a>

| **SRS-CONN-0007** | **Minimum BLE Transmit Power** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** transmit BLE signals at a power level of no less than +8 dBm. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-CONN-0006 |

<a id="srs-conn-0008"></a>

| **SRS-CONN-0008** | **BLE Address Randomization** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** randomize the BLE device address of the collar-mounted device. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 |

<a id="srs-conn-0009"></a>

| **SRS-CONN-0009** | **Secured BLE Link Establishment** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** establish the BLE link between the collar-mounted device and the base station over the secured connection defined in §8 Security. |
| **Rationale**    | Derived from PRD §6.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.3 · — (§8 Security, not yet drafted) |

<a id="srs-conn-0010"></a>

| **SRS-CONN-0010** | **Automatic BLE Reconnection on Range Re-Entry** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon the collar-mounted device re-entering BLE range of a base station, the system **shall** automatically re-establish the BLE link without requiring manual user action. |
| **Rationale**    | Derived from PRD §6.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.4 · SRS-CONN-0001, SRS-CONN-0002

## 4.2 Record Forwarding & Sync |

<a id="srs-conn-0011"></a>

| **SRS-CONN-0011** | **Classification Record Forwarding on BLE Contact** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon establishing a BLE link with a base station, the system **shall** forward stored classification records from the collar-mounted device to the base station. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-FUNC-0026, SRS-FUNC-0028 |

<a id="srs-conn-0012"></a>

| **SRS-CONN-0012** | **Best-Effort Event-Triggered Record Transport** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records to the base station using a best-effort, event-triggered transport pattern. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8.5 · SRS-FUNC-0002, SRS-FUNC-0003 |

<a id="srs-conn-0013"></a>

| **SRS-CONN-0013** | **Sync Resumption of Accumulated Records After Reconnection** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon regaining BLE connectivity to a base station following a period of disconnection, the system **shall** forward all classification records accumulated during that disconnection. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-FUNC-0027, SRS-CONN-0011

## 4.3 Base↔Cloud Gateway & Upload |

<a id="srs-conn-0014"></a>

| **SRS-CONN-0014** | **Base Station Upload of Received Records to Cloud** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-CONN-0011, SRS-CONN-0009 |

<a id="srs-conn-0015"></a>

| **SRS-CONN-0015** | **Base Station Buffering on Upload-Path Unavailability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0016 |

<a id="srs-conn-0016"></a>

| **SRS-CONN-0016** | **Buffered Record Upload on Path Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0015 |

<a id="srs-conn-0017"></a>

| **SRS-CONN-0017** | **No Discard of Received Records Pending Upload** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0015 |

<a id="srs-conn-0018"></a>

| **SRS-CONN-0018** | **Cloud Acceptance and Acknowledgment of Uploaded Records (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8 · SRS-CONN-0014 |

<a id="srs-conn-0030"></a>

| **SRS-CONN-0030** | **Base Station Upload Retry on Transient Failure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Following a failed upload attempt while the Wi-Fi or cloud connection is otherwise available, the base station **shall** retry uploading the affected buffered classification record. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | High |
| **Stability**    | Volatile |
| **Verification** | Demonstration |
| **Traceability** | PRD §8.5 · SRS-CONN-0015, SRS-CONN-0016

## 4.4 Multi-Base-Station Behavior & Handover |

<a id="srs-conn-0019"></a>

| **SRS-CONN-0019** | **Collar Forwarding to Any In-Range Paired Base Station** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward stored classification records to any paired base station currently in BLE range, without requiring a specific designated base station. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 · SRS-CONN-0011 |

<a id="srs-conn-0020"></a>

| **SRS-CONN-0020** | **Single Forwarding of Each Record to First Available Base Station** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** forward each classification record to only the first paired base station through which it establishes a BLE link, among those in range. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §4.2 · SRS-CONN-0019, SRS-CONN-0021 |

<a id="srs-conn-0021"></a>

| **SRS-CONN-0021** | **Cloud-Side Deduplication of Multi-Base Uploads (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household account. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.2 · SRS-CONN-0020, SRS-CONN-0018

## 4.5 Insight-Mode Activation over Connectivity |

<a id="srs-conn-0022"></a>

| **SRS-CONN-0022** | **Device-Side Insight-Mode Activation on Command Receipt** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.1 · SRS-FUNC-0007, SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="srs-conn-0023"></a>

| **SRS-CONN-0023** | **Mobile App Issuance of Insight-Mode Activation Command (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.1 · SRS-CONN-0022

## 4.6 GNSS Location Data Sync (Max Variant) |

<a id="srs-conn-0024"></a>

| **SRS-CONN-0024** | **Sync of Location-Tagged Records via Standard Forwarding Path** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other classification records. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0025, SRS-CONN-0011 |

<a id="srs-conn-0025"></a>

| **SRS-CONN-0025** | **Sync of Most-Recent GNSS Fix During Home Power-Gate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix as part of classification records. |
| **Rationale**    | Derived from PRD §7.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0025, SRS-OPER-0004

## 4.7 Connectivity-Loss & Degraded Behavior |

<a id="srs-conn-0026"></a>

| **SRS-CONN-0026** | **No Record Loss Due to Any Connectivity-Loss Condition** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0017 |

<a id="srs-conn-0027"></a>

| **SRS-CONN-0027** | **Continued Local Classification During BLE Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. |
| **Rationale**    | Derived from PRD §7.6. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.6 · SRS-FUNC-0028, SRS-FUNC-0027 |

<a id="srs-conn-0028"></a>

| **SRS-CONN-0028** | **Degraded-Mode Entry Below Home Wi-Fi Reliability Bound** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007 |

<a id="srs-conn-0029"></a>

| **SRS-CONN-0029** | **Degraded-Mode Exit on Wi-Fi Reliability Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007, SRS-CONN-0028

--- |

## 5. Ota Firmware Updates



## 5.1 OTA Applicability

<a id="srs-func-0043"></a>

| **SRS-FUNC-0043** | **OTA Capability Mandatory on All Collar Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). |
| **Rationale**    | Derived from PRD §9.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0034 |

<a id="srs-func-0044"></a>

| **SRS-FUNC-0044** | **OTA Capability Mandatory on All Base Station Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). |
| **Rationale**    | Derived from PRD §9.1. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0043

## 5.2 OTA Delivery Path & Transport |

<a id="srs-func-0045"></a>

| **SRS-FUNC-0045** | **Cloud-to-Base OTA Transport Protocol** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-CONN-0014 |

<a id="srs-func-0046"></a>

| **SRS-FUNC-0046** | **Base Station Staging of Collar OTA Images** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0047 |

<a id="srs-func-0047"></a>

| **SRS-FUNC-0047** | **Base-to-Collar OTA Image Delivery Over Secured BLE Link** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.2 · SRS-CONN-0009 |

<a id="srs-func-0048"></a>

| **SRS-FUNC-0048** | **Base Station Self-OTA Without User Action** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. |
| **Rationale**    | Derived from PRD §11.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §11.5 · SRS-FUNC-0044

## 5.3 Collar Install Preconditions |

<a id="srs-func-0049"></a>

| **SRS-FUNC-0049** | **Collar OTA Install Restricted to Charging-Cradle-Docked State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0050, SRS-FUNC-0056 |

<a id="srs-func-0050"></a>

| **SRS-FUNC-0050** | **Docked-Install Gate Shall Not Be Remotely Bypassable** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0049 |

<a id="srs-func-0051"></a>

| **SRS-FUNC-0051** | **Minimum Battery Reserve Before OTA Install** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. |
| **Rationale**    | Derived from PRD §9.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0049, SRS-FUNC-0057

## 5.4 OTA Image Integrity & Anti-Rollback |

<a id="srs-func-0052"></a>

| **SRS-FUNC-0052** | **Minimum OTA Image Signature Strength** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. |
| **Rationale**    | Derived from PRD §9.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.3 · SRS-FUNC-0053 |

<a id="srs-func-0053"></a>

| **SRS-FUNC-0053** | **OTA Image Signature Verification Before Commit** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. |
| **Rationale**    | Derived from PRD §9.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.3 · SRS-FUNC-0052 |

<a id="srs-func-0054"></a>

| **SRS-FUNC-0054** | **Anti-Rollback via Monotonic Version Counter** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. |
| **Rationale**    | Derived from PRD §9.3. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.3 |

<a id="srs-func-0055"></a>

| **SRS-FUNC-0055** | **Atomic OTA Installation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. |
| **Rationale**    | Derived from PRD §9.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0056 |

<a id="srs-func-0056"></a>

| **SRS-FUNC-0056** | **Dual-Bank Auto-Revert on Boot Failure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. |
| **Rationale**    | Derived from PRD §9.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0057 |

<a id="srs-func-0057"></a>

| **SRS-FUNC-0057** | **No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. |
| **Rationale**    | Derived from PRD §9.4. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0051

## 5.6 Update Notification & Status |

<a id="srs-func-0058"></a>

| **SRS-FUNC-0058** | **Device-Side OTA Update State Reporting** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.5 · SRS-FUNC-0059, SRS-FUNC-0060 |

<a id="srs-func-0059"></a>

| **SRS-FUNC-0059** | **App Notification of Available OTA Update (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** notify the user when an OTA firmware update is available. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0043, SRS-FUNC-0044 |

<a id="srs-func-0060"></a>

| **SRS-FUNC-0060** | **App Display of OTA Update State (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** display the current OTA update state reported by the device. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0058

## 5.7 Release Artifacts & Tier-2 Delivery Channel |

<a id="srs-func-0061"></a>

| **SRS-FUNC-0061** | **SBOM Production Per OTA Release** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** produce a Software Bill of Materials for every OTA firmware release. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 |

<a id="srs-func-0062"></a>

| **SRS-FUNC-0062** | **Tier-2 Classifier Delivery Restricted to Embedded OTA Components** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.5 · SRS-FUNC-0034, SRS-FUNC-0035, SRS-FUNC-0052

--- |

## 8. Security

**
**Scope note:**  Supplies the "secured connection" referenced by SRS-CONN-0009 (§4) and SRS-FUNC-0047 (§5), closing both orphans. Does NOT restate §5 OTA signature/anti-rollback chain.

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)

<a id="srs-sec-0001"></a>

| **SRS-SEC-0001** | **Mandatory Link-Layer Encryption on Collar↔Base BLE Data-Bearing Links** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. |
| **Rationale**    | Baseline protecting behavioral, location, and event data in transit over the wireless collar↔base channel. The "secured connection" / "secured BLE link" that SRS-CONN-0009 and SRS-FUNC-0047 forward-reference.
| **Verification** | Test |
| **Traceability** | SRS-CONN-0009, SRS-FUNC-0047 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.7 · SRS-CONN-0009, SRS-FUNC-0047 |

<a id="srs-sec-0002"></a>

| **SRS-SEC-0002** | **Mandatory LE Secure Connections Pairing Method** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. |
| **Rationale**    | Underpins SEC-0001 encryption; weaker legacy pairing would undermine the confidentiality guarantee.
| **Verification** | Test |
| **Traceability** | SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009<br><br>## 8.2 Cloud-Bound Transport Security | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009

## 8.2 Cloud-Bound Transport Security |

<a id="srs-sec-0003"></a>

| **SRS-SEC-0003** | **TLS 1.3 Exclusivity for Base-to-Cloud Data Transport** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. |
| **Rationale**    | Generalizes the TLS-1.3-exclusive posture (already applied to OTA via FUNC-0045 per ) to all base↔cloud channels.
| **Verification** | Test |
| **Traceability** | SRS-CONN-0014, SRS-FUNC-0045<br><br>## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)<br><br>No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.<br><br>## 8.4 Device Identity & Platform Trust | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.5 · SRS-CONN-0014, SRS-FUNC-0045

## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.

## 8.4 Device Identity & Platform Trust |

<a id="srs-sec-0004"></a>

| **SRS-SEC-0004** | **Unique Cryptographic Identity at Manufacturing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. |
| **Rationale**    | Per-device unique identity underpins secure boot attestation and per-device compromise containment.
| **Verification** | Inspection |
| **Traceability** | SRS-SEC-0005 | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 · SRS-SEC-0005 |

<a id="srs-sec-0005"></a>

| **SRS-SEC-0005** | **Secure Boot Anchored in Hardware Root of Trust** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. |
| **Rationale**    | Prevents execution of unauthorized firmware from non-OTA write paths. Boot-time integrity checking consumes part of the PERF-0006 ≤3 s budget — distinct dimensions, flagged for cross-section awareness.
| **Verification** | Test |
| **Traceability** | SRS-SEC-0004, SRS-FUNC-0053, SRS-PERF-0006<br><br>## 8.5 Vulnerability Disclosure (pre-launch gate only) | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §10.7 · SRS-SEC-0004, SRS-FUNC-0053, SRS-PERF-0006

## 8.5 Vulnerability Disclosure (pre-launch gate only) |

<a id="srs-sec-0006"></a>

| **SRS-SEC-0006** | **Public Vulnerability-Disclosure Policy in Place Before Launch** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall have a public vulnerability-disclosure policy in place before product launch. |
| **Rationale**    | Published disclosure channel must exist at launch. Lifetime maintenance in §16.
| **Verification** | Inspection |
| **Traceability** | — | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 |

## 6. Performance (Firmware-Relevant)



## 6.1 Battery-Life Performance (Firmware-Relevant)

<a id="srs-perf-0001"></a>

| **SRS-PERF-0001** | **Mini Variant Battery-Life Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's Mini variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across typical-use, minimum, and Longevity Mode operating conditions. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §12.1 · SRS-FUNC-0012, SRS-FUNC-0013 |

<a id="srs-perf-0002"></a>

| **SRS-PERF-0002** | **Max Variant Battery-Life Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's Max variant **shall** meet or exceed the battery-life minimums specified in §10.4 (Table 10-2) across all supported GNSS fix-interval settings. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §12.1 · SRS-FUNC-0012, SRS-FUNC-0013

## 6.2 Classification & Data-Path Latency | (Firmware-Relevant)

<a id="srs-perf-0003"></a>

| **SRS-PERF-0003** | **Classification Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** produce a classification result within 2 seconds of the triggering motion event. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-FUNC-0016 |

<a id="srs-perf-0004"></a>

| **SRS-PERF-0004** | **Base Station Cloud-Upload Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** upload a received classification record to the cloud within 30 seconds of receipt, when the cloud connection is available. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-CONN-0014, SRS-CONN-0015

## 6.3 Location & Startup Timing (Max Variant / System) | (Firmware-Relevant)

<a id="srs-perf-0005"></a>

| **SRS-PERF-0005** | **GNSS Time-to-First-Fix Ceiling (Warm, A-GPS)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** acquire a GNSS fix within 60 seconds under warm-start, A-GPS-assisted conditions. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.1 |

<a id="srs-perf-0006"></a>

| **SRS-PERF-0006** | **Collar Boot-Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar-mounted device **shall** complete boot within 3 seconds under cold power-on and wake-from-reset conditions. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-FUNC-0056 |

<a id="srs-perf-0007"></a>

| **SRS-PERF-0007** | **Home/Away Status Update Latency Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** update the reported home/away status within the currently configured BLE advertising interval plus 10 seconds of an actual home/away state transition. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §12.1 · SRS-CONN-0004, SRS-CONN-0005 |

<a id="srs-perf-0008"></a>

| **SRS-PERF-0008** | **CCF Twist-Lock Engagement Time Ceiling** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** allow the Twist-Lock mechanism to be engaged within 5 seconds. |
| **Rationale**    | Derived from PRD §12.1. | **Priority**     | Low |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.1 |
