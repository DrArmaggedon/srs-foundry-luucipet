> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**CAT: SEC** | Maps to: PRD §6.7, §12.3; supporting anchor PRD §10.7

**Scope note:**  Supplies the "secured connection" referenced by SRS-CONN-0009 (§4) and SRS-FUNC-0047 (§5), closing both orphans. Does NOT restate §5 OTA signature/anti-rollback chain.

## 8.1 BLE Link-Layer Security (closes CONN-0009 / FUNC-0047)

**SRS-SEC-0001** | Mandatory Link-Layer Encryption on Collar↔Base BLE Data-Bearing Links | The system shall encrypt every data-bearing BLE link between the collar-mounted device and the base station using AES-128 CCM. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §6.7], [PRD §8.2], [PRD §12.3], [STD: ETSI EN 303 645:2025] | Rationale: Baseline protecting behavioral, location, and event data in transit over the wireless collar↔base channel. The "secured connection" / "secured BLE link" that SRS-CONN-0009 and SRS-FUNC-0047 forward-reference. | VM: Test | XR: SRS-CONN-0009, SRS-FUNC-0047

**SRS-SEC-0002** | Mandatory LE Secure Connections Pairing Method | The system shall establish the BLE pairing key exchange between the collar-mounted device and the base station using the LE Secure Connections method. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §6.3], [PRD §8.2], [STD: ETSI EN 303 645:2025] | Rationale: Underpins SEC-0001 encryption; weaker legacy pairing would undermine the confidentiality guarantee. | VM: Test | XR: SRS-SEC-0001, SRS-CONN-0003, SRS-CONN-0009

## 8.2 Cloud-Bound Transport Security

**SRS-SEC-0003** | TLS 1.3 Exclusivity for Base-to-Cloud Data Transport | The system shall use TLS version 1.3 exclusively for all data transport between the base station and the cloud. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §6.5], [PRD §12.3], [STD: ETSI EN 303 645:2025] | Rationale: Generalizes the TLS-1.3-exclusive posture (already applied to OTA via FUNC-0045 per CR-0005) to all base↔cloud channels. | VM: Test | XR: SRS-CONN-0014, SRS-FUNC-0045

## 8.3 OTA Firmware Trust Chain (architectural — no new obligation)

No firmware image may be installed without passing the §5 verification chain (SRS-FUNC-0052/0053/0054). Carried by reference, not a duplicate obligation.

## 8.4 Device Identity & Platform Trust

**SRS-SEC-0004** | Unique Cryptographic Identity at Manufacturing | The system shall provision each manufactured device with a unique cryptographic identity at the time of manufacturing. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §12.3] | Rationale: Per-device unique identity underpins secure boot attestation and per-device compromise containment. | VM: Inspection | XR: SRS-SEC-0005

**SRS-SEC-0005** | Secure Boot Anchored in Hardware Root of Trust | The device shall verify its own firmware integrity at boot using a hardware root of trust before executing application code. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.7] | Rationale: Prevents execution of unauthorized firmware from non-OTA write paths. Boot-time integrity checking consumes part of the PERF-0006 ≤3 s budget — distinct dimensions, flagged for cross-section awareness. | VM: Test | XR: SRS-SEC-0004, SRS-FUNC-0053, SRS-PERF-0006

## 8.5 Vulnerability Disclosure (pre-launch gate only)

**SRS-SEC-0006** | Public Vulnerability-Disclosure Policy in Place Before Launch | The system shall have a public vulnerability-disclosure policy in place before product launch. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.3], [PRD §13.5], [STD: ETSI EN 303 645:2025], [STD: EU CRA (EU) 2024/2847 Art 13-14] | Rationale: Published disclosure channel must exist at launch. Lifetime maintenance in §16. | VM: Inspection | XR: —

### SRS-ID Inventory: 6 blocks, SRS-SEC-0001…0006. Orphans closed: CONN-0009, FUNC-0047. Next free: SRS-SEC-0007.
