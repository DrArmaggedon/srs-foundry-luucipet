> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

CAT: **FUNC** (OTA) | Maps to: PRD §9 (Functional Requirements — OTA Firmware Updates)
*(Drafter-authored; Conductor-persisted. §5 v3 — 20 blocks, SRS-FUNC-0043–0062.)*

## 5.1 OTA Applicability

**SRS-FUNC-0043** | OTA Capability Mandatory on All Collar Variants | The system **shall** provide over-the-air firmware update capability on every collar-mounted device variant (Mini and Max). | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.1] | VM: Demonstration | XR: SRS-FUNC-0034

**SRS-FUNC-0044** | OTA Capability Mandatory on All Base Station Tiers | The system **shall** provide over-the-air firmware update capability on every base station tier (Charging and Relay). | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.1] | VM: Demonstration | XR: SRS-FUNC-0043

## 5.2 OTA Delivery Path & Transport

**SRS-FUNC-0045** | Cloud-to-Base OTA Transport Protocol | The system **shall** transport OTA firmware images from the cloud to the base station over Wi-Fi using TLS version 1.3. | Priority: HIGH | Stability: STABLE | Source: [PRD §9.2], [PRD §6.5], [PRD §11.2], [STD: ETSI EN 303 645:2025] | VM: Test | XR: SRS-CONN-0014

**SRS-FUNC-0046** | Base Station Staging of Collar OTA Images | The system **shall** stage a received collar OTA firmware image at the base station prior to delivery of that image to the collar-mounted device. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §9.2] | VM: Test | XR: SRS-FUNC-0047

**SRS-FUNC-0047** | Base-to-Collar OTA Image Delivery Over Secured BLE Link | The system **shall** deliver a staged OTA firmware image from the base station to the collar-mounted device over the secured BLE link defined in §8 Security. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.2] | VM: Inspection | XR: SRS-CONN-0009

**SRS-FUNC-0048** | Base Station Self-OTA Without User Action | The system **shall** update base station firmware via self-initiated OTA over the Wi-Fi link without requiring user action. | Priority: HIGH | Stability: STABLE | Source: [PRD §11.5] | VM: Demonstration | XR: SRS-FUNC-0044

## 5.3 Collar Install Preconditions

**SRS-FUNC-0049** | Collar OTA Install Restricted to Charging-Cradle-Docked State | The system **shall** install a collar OTA firmware update only while the collar-mounted device is docked in the charging cradle. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.2] | VM: Test | XR: SRS-FUNC-0050, SRS-FUNC-0056

**SRS-FUNC-0050** | Docked-Install Gate Shall Not Be Remotely Bypassable | The system **shall not** allow the charging-cradle-docked install precondition to be bypassed by any remote command. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.2] | VM: Test | XR: SRS-FUNC-0049

**SRS-FUNC-0051** | Minimum Battery Reserve Before OTA Install | The system **shall** require a state-of-charge of no less than 10% before initiating a collar OTA firmware installation. | Priority: HIGH | Stability: STABLE | Source: [PRD §9.2], [PRD §10.4] | VM: Test | XR: SRS-FUNC-0049, SRS-FUNC-0057

## 5.4 OTA Image Integrity & Anti-Rollback

**SRS-FUNC-0052** | Minimum OTA Image Signature Strength | The system **shall** require every OTA firmware image to be signed using an algorithm of no less than 256-bit ECDSA or RSA-2048 strength. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.3], [STD: ETSI EN 303 645:2025] | VM: Inspection | XR: SRS-FUNC-0053

**SRS-FUNC-0053** | OTA Image Signature Verification Before Commit | The system **shall** verify the signature of an OTA firmware image before committing or executing that image. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.3], [STD: ETSI EN 303 645:2025] | VM: Test | XR: SRS-FUNC-0052

**SRS-FUNC-0054** | Anti-Rollback via Monotonic Version Counter | The system **shall** prevent installation of an OTA firmware image whose version is lower than the current monotonic version counter value held in secure storage. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.3], [STD: EU CRA (EU) 2024/2847] | VM: Test

## 5.5 Install Resilience

**SRS-FUNC-0055** | Atomic OTA Installation | The system **shall** install an OTA firmware image atomically, such that the installation either completes in full or leaves the prior firmware image unmodified. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.4] | VM: Test | XR: SRS-FUNC-0056

**SRS-FUNC-0056** | Dual-Bank Auto-Revert on Boot Failure | The system **shall** automatically revert to the previous firmware bank if the device fails to boot successfully following an OTA installation. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.4], [PRD §11.5] | VM: Test | XR: SRS-FUNC-0055, SRS-FUNC-0057

**SRS-FUNC-0057** | No Unrecoverable State on Power Loss or Delivery-Connection Drop During Install | The system **shall not** enter an unrecoverable device state as a result of a power loss or a loss of the delivery connection occurring during an OTA installation. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §9.4] | VM: Analysis | XR: SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0051

## 5.6 Update Notification & Status

**SRS-FUNC-0058** | Device-Side OTA Update State Reporting | The system **shall** report the current OTA update state as one of Downloading, Verifying, Pending Installation, Installing, Success, or Failed. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §9.5] | VM: Test | XR: SRS-FUNC-0059, SRS-FUNC-0060

**SRS-FUNC-0059** | App Notification of Available OTA Update (external) | The Mobile App **shall** notify the user when an OTA firmware update is available. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §9.5], [EXTERNAL: Mobile App team] | VM: Inspection (external conformance evidence) | XR: SRS-FUNC-0043, SRS-FUNC-0044

**SRS-FUNC-0060** | App Display of OTA Update State (external) | The Mobile App **shall** display the current OTA update state reported by the device. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §9.5], [EXTERNAL: Mobile App team] | VM: Inspection (external conformance evidence) | XR: SRS-FUNC-0058

## 5.7 Release Artifacts & Tier-2 Delivery Channel

**SRS-FUNC-0061** | SBOM Production Per OTA Release | The system **shall** produce a Software Bill of Materials for every OTA firmware release. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §9.5] | VM: Inspection

**SRS-FUNC-0062** | Tier-2 Classifier Delivery Restricted to Embedded OTA Components | The system **shall** deliver Tier-2 behavior classifier models only as components embedded within an OTA firmware update. | Priority: HIGH | Stability: STABLE | Source: [PRD §9.5] | VM: Inspection | XR: SRS-FUNC-0034, SRS-FUNC-0035, SRS-FUNC-0052

---

### SRS-ID Inventory (§5 v1 — COMPLETE)
- **20 blocks, SRS-FUNC-0043 … SRS-FUNC-0062.** 18 in-scope + 2 external (FUNC-0059/0060).
- Next free FUNC ID = **SRS-FUNC-0063**.
