> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:38:48Z
> **Audience:** Firmware / Embedded Engineering
> ⚠️ For full context, always refer to the Master SRS.

---

## 3. Behavioral Classification

## 3. Behavioral Classification

## 3.6 Tier-2 Extensibility via OTA |

## 3.6 Tier-2 Extensibility via OTA |

<a id="srs-func-0034"></a>

| **SRS-FUNC-0034** | **Tier-2 Classifier Delivery via OTA** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** receive new Tier-2 behavior classifiers via over-the-air update. |
| **Rationale**    | Derived from PRD §7.9. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0016, SRS-FUNC-0035 |

<a id="srs-func-0035"></a>

| **SRS-FUNC-0035** | **Tier-2 Deployment Without Hardware Modification or Service Event** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** require hardware modification or a service event to deploy a new Tier-2 classifier. |
| **Rationale**    | Derived from PRD §7.9. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.9 · SRS-FUNC-0034

## 4. Data Sync Connectivity

## 4. Data Sync Connectivity

## 4.5 Insight-Mode Activation over Connectivity |

## 4.5 Insight-Mode Activation over Connectivity |

<a id="srs-conn-0022"></a>

| **SRS-CONN-0022** | **Device-Side Insight-Mode Activation on Command Receipt** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon receiving an Insight-mode activation command over the BLE link, the system **shall** activate Insight mode. |
| **Rationale**    | Derived from PRD §7.1. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.1 · SRS-FUNC-0007, SRS-FUNC-0008, SRS-FUNC-0009 |

<a id="srs-conn-0023"></a>

| **SRS-CONN-0023** | **Mobile App Issuance of Insight-Mode Activation Command (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. |
| **Rationale**    | Derived from PRD §7.1. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.1 · SRS-CONN-0022

## 4.6 GNSS Location Data Sync (Max Variant) |

## 4.6 GNSS Location Data Sync (Max Variant) |

<a id="srs-conn-0024"></a>

| **SRS-CONN-0024** | **Sync of Location-Tagged Records via Standard Forwarding Path** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | On the Max product variant, the system **shall** forward location-tagged classification records through the same record-forwarding path used for other classification records. |
| **Rationale**    | Derived from PRD §7.5. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0025, SRS-CONN-0011 |

<a id="srs-conn-0025"></a>

| **SRS-CONN-0025** | **Sync of Most-Recent GNSS Fix During Home Power-Gate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | While the GNSS smart power gate suspends fix acquisition in the home state, the system **shall** continue to sync the most recently acquired GNSS fix as part of classification records. |
| **Rationale**    | Derived from PRD §7.5. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §7.5 · SRS-FUNC-0025, SRS-OPER-0004

## 4.7 Connectivity-Loss & Degraded Behavior |

## 4.7 Connectivity-Loss & Degraded Behavior |

<a id="srs-conn-0026"></a>

| **SRS-CONN-0026** | **No Record Loss Due to Any Connectivity-Loss Condition** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** lose a classification record as a result of any connectivity-loss condition between the collar-mounted device and the cloud. |
| **Rationale**    | Derived from PRD §8.5. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0017 |

<a id="srs-conn-0027"></a>

| **SRS-CONN-0027** | **Continued Local Classification During BLE Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon loss of the BLE link to all base stations, the system **shall** continue local classification and storage without interruption. |
| **Rationale**    | Derived from PRD §7.6. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §7.6 · SRS-FUNC-0028, SRS-FUNC-0027 |

<a id="srs-conn-0028"></a>

| **SRS-CONN-0028** | **Degraded-Mode Entry Below Home Wi-Fi Reliability Bound** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** enter degraded mode when home Wi-Fi reliability falls below the bound defined in SRS-OPER-0007. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007 |

<a id="srs-conn-0029"></a>

| **SRS-CONN-0029** | **Degraded-Mode Exit on Wi-Fi Reliability Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** exit degraded mode when home Wi-Fi reliability is restored to or above the bound defined in SRS-OPER-0007. |
| **Rationale**    | Derived from ASSUMPTION: A-0009. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | ASSUMPTION: A-0009 · SRS-OPER-0007, SRS-CONN-0028

--- |

## 5. Ota Firmware Updates

## 5. Ota Firmware Updates

## 5.1 OTA Applicability

## 5.1 OTA Applicability

<a id="srs-func-0043"></a>

| **SRS-FUNC-0043** | **OTA Capability Mandatory on All Collar Variants** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). |
| **Rationale**    | Derived from PRD §9.1. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0034 |

<a id="srs-func-0044"></a>

| **SRS-FUNC-0044** | **OTA Capability Mandatory on All Base Station Tiers** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). |
| **Rationale**    | Derived from PRD §9.1. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §9.1 · SRS-FUNC-0043

## 5.2 OTA Delivery Path & Transport |

## 5.2 OTA Delivery Path & Transport |

<a id="srs-func-0045"></a>

| **SRS-FUNC-0045** | **Cloud-to-Base OTA Transport Protocol** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. |
| **Rationale**    | Derived from PRD §9.2. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-CONN-0014 |

<a id="srs-func-0046"></a>

| **SRS-FUNC-0046** | **Base Station Staging of Collar OTA Images** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. |
| **Rationale**    | Derived from PRD §9.2. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.2 · SRS-FUNC-0047 |

<a id="srs-func-0047"></a>

| **SRS-FUNC-0047** | **Base-to-Collar OTA Image Delivery Over Secured BLE Link** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. |
| **Rationale**    | Derived from PRD §9.2. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.2 · SRS-CONN-0009 |

<a id="srs-func-0048"></a>

| **SRS-FUNC-0048** | **Base Station Self-OTA Without User Action** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. |
| **Rationale**    | Derived from PRD §11.5. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Demonstration |
| **Traceability** | PRD §11.5 · SRS-FUNC-0044

## 5.4 OTA Image Integrity & Anti-Rollback |

## 5.4 OTA Image Integrity & Anti-Rollback |

<a id="srs-func-0052"></a>

| **SRS-FUNC-0052** | **Minimum OTA Image Signature Strength** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. |
| **Rationale**    | Derived from PRD §9.3. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.3 · SRS-FUNC-0053 |

<a id="srs-func-0053"></a>

| **SRS-FUNC-0053** | **OTA Image Signature Verification Before Commit** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. |
| **Rationale**    | Derived from PRD §9.3. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.3 · SRS-FUNC-0052 |

<a id="srs-func-0054"></a>

| **SRS-FUNC-0054** | **Anti-Rollback via Monotonic Version Counter** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. |
| **Rationale**    | Derived from PRD §9.3. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §9.3 |

<a id="srs-func-0055"></a>

| **SRS-FUNC-0055** | **Atomic OTA Installation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. |
| **Rationale**    | Derived from PRD §9.4. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0056 |

<a id="srs-func-0056"></a>

| **SRS-FUNC-0056** | **Dual-Bank Auto-Revert on Boot Failure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. |
| **Rationale**    | Derived from PRD §9.4. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0057 |

<a id="srs-func-0057"></a>

| **SRS-FUNC-0057** | **No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. |
| **Rationale**    | Derived from PRD §9.4. |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Analysis |
| **Traceability** | PRD §9.4 · SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0051

## 8. Security

## 8. Security

**
**Scope note:**  Supplies the "secured connection" referenced by SRS-CONN-0009 (§4) and SRS-FUNC-0047 (§5), closing both orphans. Does NOT restate §5 OTA signature/anti-rollback chain.

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)

<a id="srs-sec-0001"></a>

| **SRS-SEC-0001** | **Mandatory Link-Layer Encryption on Collar↔Base BLE Data-Bearing Links** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. |
| **Rationale**    | Baseline protecting behavioral, location, and event data in transit over the wireless collar↔base channel. The "secured connection" / "secured BLE link" that SRS-CONN-0009 and SRS-FUNC-0047 forward-reference. \| VM: Test \| XR: SRS-CONN-0009, SRS-FUNC-0047 |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.7 · SRS-CONN-0009, SRS-FUNC-0047 |

<a id="srs-sec-0002"></a>

| **SRS-SEC-0002** | **Mandatory LE Secure Connections Pairing Method** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. |
| **Rationale**    | Underpins SEC-0001 encryption; weaker legacy pairing would undermine the confidentiality guarantee. \| VM: Test \| XR: SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009<br><br>## 8.2 Cloud-Bound Transport Security |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.3 · SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009

## 8.2 Cloud-Bound Transport Security |

## 8.2 Cloud-Bound Transport Security |

<a id="srs-sec-0003"></a>

| **SRS-SEC-0003** | **TLS 1.3 Exclusivity for Base-to-Cloud Data Transport** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. |
| **Rationale**    | Generalizes the TLS-1.3-exclusive posture (already applied to OTA via FUNC-0045 per ) to all base↔cloud channels. \| VM: Test \| XR: SRS-CONN-0014, SRS-FUNC-0045<br><br>## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)<br><br>No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.<br><br>## 8.4 Device Identity & Platform Trust |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §6.5 · SRS-CONN-0014, SRS-FUNC-0045

## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.

## 16.1 OTA-Update Capability Lifetime

## 16.1 OTA-Update Capability Lifetime

<a id="srs-maint-0001"></a>

| **SRS-MAINT-0001** | **OTA-Update Capability Availability Through Supported Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. |
| **Rationale**    | Derived from PRD §12.7. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.7 |

<a id="srs-maint-0002"></a>

| **SRS-MAINT-0002** | **SBOM Currency Maintenance Across Supported Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetime defined by SRS-MAINT-0001. |
| **Rationale**    | Derived from PRD §12.7. |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.7 |

<a id="srs-maint-0003"></a>

| **SRS-MAINT-0003** | **Post-Launch Vulnerability-Disclosure Process Maintenance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported service lifetime defined by SRS-MAINT-0001. |
| **Rationale**    | Derived from PRD §12.7. |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.7 |

## 17.3 IoT Cybersecurity Baseline |

## 17.3 IoT Cybersecurity Baseline |

<a id="srs-comp-0010"></a>

| **SRS-COMP-0010** | **ETSI EN 303 645 Consumer IoT Security Baseline Conformance** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall conform to ETSI EN 303 645:2025 as the consumer-IoT cybersecurity baseline standard underlying the security requirements of §8. |
| **Rationale**    | Derived from PRD §12.3. |
| **Priority**     | Critical |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §12.3 · SRS-SEC-0001 through SRS-SEC-0006

---

### View Coverage
Behavioral Classification (§3), Data Sync & Connectivity (§4), OTA/Firmware Updates (§5), Security (§8), FW-relevant Performance excerpts from §6.
