> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-23T01:00:00Z
⚠️ For full context, always refer to the Master SRS.

---

## Handoff Document — Mobile App Team

This document contains **all** requirements from the LUUCIPet SRS relevant to the Mobile App team — both [EXTERNAL: Mobile App team] deliverables and in-scope device-side interface obligations.

---

## §5 — OTA Firmware Updates

### [EXTERNAL: Mobile App team]

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

### In-Scope Interface Obligations (Device Side)

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

<a id="srs-func-0058"></a>

| **SRS-FUNC-0058** | **Device-Side OTA Update State Reporting** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. |
| **Rationale**    | Derived from PRD §9.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §9.5 · SRS-FUNC-0059, SRS-FUNC-0060 |

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

