> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

CAT: **FUNC** | Maps to: PRD §7 (Behavioral Classification), PRD §4.4 (Class Taxonomy)
*(Drafter-authored; Conductor-persisted to shared store for reviewer visibility.)*

## 3.1 Operating Modes

**SRS-FUNC-0006** | Wellness Mode as Default Operating Mode | The system **shall** operate in Wellness mode as its default power-optimized classification mode. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.1] | VM: Demonstration | XR: SRS-FUNC-0011

**SRS-FUNC-0007** | Insight Mode Availability On Demand | The system **shall** provide an Insight mode that can be activated on demand as an alternative to Wellness mode. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.1] | VM: Demonstration | XR: SRS-FUNC-0008, SRS-FUNC-0009

**SRS-FUNC-0008** | Insight Mode Continuous Sampling Rate | While in Insight mode, the system **shall** sample the accelerometer continuously at 50 Hz. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.1] | VM: Test | XR: SRS-FUNC-0007, SRS-FUNC-0014

**SRS-FUNC-0009** | Insight Mode Auto-Revert to Wellness | The system **shall** automatically revert from Insight mode to Wellness mode without requiring a manual user action. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.3] | VM: Test | XR: SRS-FUNC-0006, SRS-FUNC-0007

**SRS-FUNC-0010** | Wellness Mode Motion-Triggered Confirmation Burst | Upon detecting motion, the system **shall** initiate a confirmation sampling burst of 15 minutes duration while in Wellness mode. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.3] | VM: Test | XR: SRS-FUNC-0011

**SRS-FUNC-0011** | Wellness Mode Idle Current Ceiling | While in Wellness mode and outside a confirmation burst, the system **shall not** exceed an idle current draw of 4 µA. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.3] | VM: Test | XR: SRS-FUNC-0006, SRS-FUNC-0010

**SRS-FUNC-0012** | Longevity Mode Shall Not Reduce Classification Sampling Rate | When Longevity Mode is active, the system **shall not** reduce the classification accelerometer sampling rate below the rate used outside Longevity Mode. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.10] | VM: Test | XR: SRS-FUNC-0014

**SRS-FUNC-0013** | Longevity Mode Shall Not Reduce Classification Accuracy | When Longevity Mode is active, the system **shall not** reduce per-class classification accuracy below the applicable Tier-1 or Tier-2 accuracy threshold. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.10] | VM: Test | XR: SRS-FUNC-0018, SRS-FUNC-0020

## 3.2 Sensing & Classification Pipeline

**SRS-FUNC-0014** | Minimum Accelerometer Output Data Rate | The system **shall** sample the accelerometer at a rate of no less than 50 Hz. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.2] | VM: Test | XR: SRS-FUNC-0008, SRS-FUNC-0015

**SRS-FUNC-0015** | No Auxiliary Sensors for Tier-1 Classification | The system **shall** classify Tier-1 behavior classes using accelerometer data only, without reliance on auxiliary sensors. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.2] | VM: Inspection | XR: SRS-FUNC-0014

**SRS-FUNC-0016** | Unified Classification Pipeline Across Tiers | The system **shall** process Tier-1 and Tier-2 behavior classes through a single onboard classification pipeline. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §7.2] | VM: Inspection | XR: SRS-FUNC-0034

**SRS-FUNC-0017** | Species-Specific Threshold Assignment at Onboarding | The system **shall** set species-specific classification thresholds during the onboarding process. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.2] | VM: Test | XR: SRS-OPER-0003

## 3.3 Classification Accuracy & False-Positive Bounds

**SRS-FUNC-0018** | Tier-1 Per-Class Accuracy Minimum | The system **shall** achieve a classification accuracy of no less than 85% for each Tier-1 behavior class. | Priority: CRITICAL | Stability: LIKELY-CHANGE | Source: [PRD §7.4] | VM: Test | XR: SRS-FUNC-0019

**SRS-FUNC-0019** | Tier-1 Per-Class False-Positive Ceiling | The system **shall not** exceed a false-positive rate of 5% for each Tier-1 behavior class. | Priority: CRITICAL | Stability: LIKELY-CHANGE | Source: [PRD §7.4] | VM: Test | XR: SRS-FUNC-0018

**SRS-FUNC-0020** | Tier-2 Per-Class Accuracy Minimum | The system **shall** achieve a classification accuracy of no less than 80% for each Tier-2 behavior class. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [PRD §7.4] | VM: Test | XR: SRS-FUNC-0021

**SRS-FUNC-0021** | Tier-2 Per-Class False-Positive Ceiling | The system **shall not** exceed a false-positive rate of 10% for each Tier-2 behavior class. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [PRD §7.4] | VM: Test | XR: SRS-FUNC-0020

## 3.4 Classification Records & Local Storage

**SRS-FUNC-0022** | Classification Record Contains Behavior Label | The system **shall** include a behavior class label in every generated classification record. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.5] | VM: Inspection | XR: SRS-FUNC-0023, SRS-FUNC-0024

**SRS-FUNC-0023** | Classification Record Contains Confidence Score | The system **shall** include a confidence score in the range 0.0 to 1.0 in every generated classification record. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.5] | VM: Test | XR: SRS-FUNC-0022

**SRS-FUNC-0024** | Classification Record Timestamp Resolution | The system **shall** timestamp every classification record in UTC with a resolution no coarser than 1 second. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.5] | VM: Test | XR: SRS-FUNC-0022

**SRS-FUNC-0025** | Classification Record GNSS Fix on Max Variant | On the Max product variant, the system **shall** include the most recent GNSS fix in every generated classification record. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §7.5] | VM: Inspection | XR: SRS-FUNC-0022

**SRS-FUNC-0026** | Minimum Local Retention of Classification Records | The system **shall** retain generated classification records locally for no less than 30 days without a cloud connection. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.5] | VM: Test | XR: SRS-FUNC-0027

**SRS-FUNC-0027** | No Record Discard on Connectivity Loss | The system **shall not** discard stored classification records upon loss of connectivity. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.5] | VM: Test | XR: SRS-FUNC-0026

**SRS-FUNC-0028** | Classification Generation Independent of BLE Connectivity | The system **shall** generate and record classifications independently of the current BLE connectivity state. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.6] | VM: Demonstration | XR: SRS-FUNC-0029

**SRS-FUNC-0029** | Record Forwarding Without Corruption | The system **shall** forward stored classification records without data corruption. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.6] | VM: Test | XR: SRS-FUNC-0030

**SRS-FUNC-0030** | Record Forwarding Without Sequence Loss | The system **shall** forward stored classification records without loss of their original sequence order. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.6] | VM: Test | XR: SRS-FUNC-0029

## 3.5 Data Locality & On-Device Processing

**SRS-FUNC-0031** | On-Device Signal Normalization | The system **shall** normalize raw accelerometer data on-device prior to classification. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.7] | VM: Inspection | XR: SRS-FUNC-0032, SRS-FUNC-0033

**SRS-FUNC-0032** | Raw Accelerometer Data Shall Not Leave the Collar | The system **shall not** transmit raw accelerometer data off the collar. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.7] | VM: Test | XR: SRS-FUNC-0031, SRS-FUNC-0033

**SRS-FUNC-0033** | No Cloud Round-Trip for Classification Decisions | The system **shall** produce classification decisions without requiring a round-trip to a cloud service. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.7] | VM: Demonstration | XR: SRS-FUNC-0028, SRS-FUNC-0032

## 3.6 Tier-2 Extensibility via OTA

**SRS-FUNC-0034** | Tier-2 Classifier Delivery via OTA | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.9] | VM: Demonstration | XR: SRS-FUNC-0016, SRS-FUNC-0035

**SRS-FUNC-0035** | Tier-2 Deployment Without Hardware Modification or Service Event | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.9] | VM: Demonstration | XR: SRS-FUNC-0034

## 3.7 Configurable Alert Thresholds (Scratching & Shaking)

**SRS-FUNC-0036** | Device Application of Configured Scratching Alert Threshold | The system **shall** apply a Scratching alert threshold value received via the companion application. | Priority: HIGH | Stability: VOLATILE | Source: [PRD §7.8] | VM: Test | XR: SRS-FUNC-0037, SRS-FUNC-0041

**SRS-FUNC-0037** | Firmware-Default Scratching Alert Threshold | The system **shall** apply a conservative firmware-defined default Scratching alert threshold when no user-configured value has been received. | Priority: MEDIUM | Stability: VOLATILE | Source: [PRD §7.8] | VM: Inspection | XR: SRS-FUNC-0036

**SRS-FUNC-0038** | Device Application of Configured Shaking Alert Threshold | The system **shall** apply a Shaking alert threshold value received via the companion application. | Priority: HIGH | Stability: VOLATILE | Source: [PRD §7.8] | VM: Test | XR: SRS-FUNC-0039, SRS-FUNC-0042

**SRS-FUNC-0039** | Firmware-Default Shaking Alert Threshold | The system **shall** apply a conservative firmware-defined default Shaking alert threshold when no user-configured value has been received. | Priority: MEDIUM | Stability: VOLATILE | Source: [PRD §7.8] | VM: Inspection | XR: SRS-FUNC-0038

**SRS-FUNC-0040** | Alert Threshold Persistence Across OTA Updates | The system **shall** retain configured Scratching and Shaking alert threshold values across OTA firmware updates. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.8] | VM: Test | XR: SRS-FUNC-0036, SRS-FUNC-0038

**SRS-FUNC-0041** | App-Side Scratching Threshold Configuration UI (external) | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.8], [EXTERNAL: Mobile App team] | VM: Inspection (external conformance evidence) | XR: SRS-FUNC-0036

**SRS-FUNC-0042** | App-Side Shaking Threshold Configuration UI (external) | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.8], [EXTERNAL: Mobile App team] | VM: Inspection (external conformance evidence) | XR: SRS-FUNC-0038

---

### SRS-ID inventory (§3 v1)
**In-scope (35):** SRS-FUNC-0006 … SRS-FUNC-0040.
**External (2):** SRS-FUNC-0041, SRS-FUNC-0042 ([EXTERNAL: Mobile App team]).
**Total: 37 blocks.** Next free FUNC ID = SRS-FUNC-0043.
