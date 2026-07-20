> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

# SRS §9 — Data Requirements (v2)

## 9.1 Introduction and Scope Boundary

This section specifies requirements governing the **content, storage, integrity, privacy, and protection** of data produced by the LUUCIPet Wellness Monitor collar (Mini and Max variants). It covers what classification and event data *is* and how it must be handled on-device — not the transport protocol mechanics, which are specified in SRS §4 (CONN), nor the classification algorithm itself, which is specified in SRS §3 (FUNC), nor transport-layer cryptography, which is specified in SRS §8 (SEC). Where a data-layer requirement is closely coupled to an existing connectivity requirement, a cross-reference is given rather than a duplicate statement.

Per the standing scope model, functions performed by parties outside this build (Mobile App team, IoT Cloud backend team) are documented as non-normative boundary notes in §9.11 rather than silently omitted.

Applicable regulatory instruments for this section (from the Regulatory Map) are GDPR (EU) 2016/679, UK GDPR + DPA 2018, PIPEDA, CCPA/CPRA (indicative), and the data-protection-relevant provisions of ETSI EN 303 645:2025. Cybersecurity vulnerability-management obligations under the RED Delegated Act, EU CRA, and UK PSTI Act are addressed in SRS §8 (SEC) and are not repeated here.

---

## 9.2 Classification Record Format & Schema

**SRS-DATA-0001** | Classification Record Content | The system shall generate a classification record containing a Tier-1 or Tier-2 behavioral label, a confidence score, and a UTC timestamp for each classification event. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.5] | VM: Test

**SRS-DATA-0002** | Confidence Score Bound | The system shall express the classification confidence value as a normalized decimal in the range 0.0 to 1.0 inclusive. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.5] | VM: Test

**SRS-DATA-0003** | Record Timestamp Accuracy | The system shall timestamp each classification record with UTC time accurate to within 1 second. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.5] | VM: Test

**SRS-DATA-0004** | GNSS Context on Max Variant | On the Max variant, the system shall append the most recent GNSS fix to the classification record. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.5] | VM: Test

## 9.3 On-Device Storage & Retention

**SRS-DATA-0005** | On-Device Storage Duration | The system shall retain classification records in on-device non-volatile storage for a minimum of 30 days without dependency on cloud connectivity. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.5; PRD §10.6] | VM: Test

**SRS-DATA-0006** | Retention Through Power Loss | The system shall preserve stored classification records without corruption across a power-loss event. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.6] | VM: Test

**SRS-DATA-0007** | Storage Corruption Detection | The system shall detect corruption of stored classification records prior to transmission. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [PRD §10.6] | VM: Test

## 9.4 Data Integrity

**SRS-DATA-0008** | Classification Independent of Connectivity | The system shall perform classification and record generation independent of BLE connectivity state. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.6] | VM: Test

**SRS-DATA-0009** | Record Forwarding Without Corruption | The system shall forward stored classification records to the transport layer without introducing data corruption. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.6] | VM: Test

**SRS-DATA-0010** | Record Forwarding Without Sequence Loss | The system shall forward stored classification records to the transport layer in chronological sequence without gaps. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.6] | VM: Test

## 9.5 Raw Data Boundary & Processing Locality

**SRS-DATA-0011** | Raw Sensor Data Transmission Boundary | The system shall not transmit raw accelerometer data beyond the collar. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §7.7] | VM: Test

**SRS-DATA-0012** | On-Device Normalization | The system shall perform normalization of sensor data on-device prior to classification. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.7] | VM: Analysis

**SRS-DATA-0013** | No Cloud Round-Trip for Classification | The system shall not require a cloud round-trip to complete a classification decision. | Priority: HIGH | Stability: STABLE | Source: [PRD §7.7] | VM: Demonstration

**SRS-DATA-0014** | Raw Sample Retention Minimization | The system shall limit on-device retention of raw accelerometer samples to the minimum duration necessary to complete on-device classification. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [PRD §7.7; STD: RM-0015 §Art.25] | VM: Analysis

## 9.6 Buffered Data Persistence

**SRS-DATA-0015** | Buffered Data Retention Until Acknowledgement | The system shall retain buffered classification and event records until a positive delivery acknowledgement is received from the Cloud DM layer. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.4] | VM: Test

**SRS-DATA-0016** | No Buffer Clear on Disconnect Alone | The system shall not clear the buffered-data queue solely as a result of a BLE disconnect event. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.4] | VM: Test

**SRS-DATA-0017** | Stale-Data Flag on Delayed Upload | The system shall flag a buffered record as stale when it is uploaded outside its original chronological order. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §8.7] | VM: Test

## 9.7 Privacy Regime — Data Handling Obligations

**SRS-DATA-0018** | Data Minimization for Personal Data | The system shall limit stored personal data fields to those required for wellness monitoring and safety functions: owner-linked device identifier, classification records, and (Max variant) GNSS fixes. | Priority: HIGH | Stability: LIKELY-CHANGE | Source: [STD: RM-0015 §Art.5(1)(c)] | VM: Inspection

**SRS-DATA-0019** | Purpose Limitation | The system shall restrict processing of owner-linked personal data and Max-variant location data to the stated wellness-monitoring and safety-event purposes. | Priority: HIGH | Stability: STABLE | Source: [STD: RM-0015 §Art.5(1)(b)] | VM: Inspection

**SRS-DATA-0020** | On-Device Data Deletion Support | The system shall support deletion of on-device stored personal data upon an authenticated owner-initiated request. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [STD: RM-0015 §Art.17] | VM: Demonstration

**SRS-DATA-0021** | On-Device Data Access Support | The system shall support retrieval of on-device stored personal data upon an authenticated owner-initiated request. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [STD: RM-0015 §Art.15] | VM: Demonstration

**SRS-DATA-0022** | Consumer Privacy Rights Contingency (CCPA/CPRA) | Where applicable CCPA/CPRA unit-volume or revenue thresholds are met, the system shall support consumer data access and deletion requests consistent with SRS-DATA-0020 and SRS-DATA-0021. | Priority: LOW | Stability: VOLATILE | Source: [STD: RM-0017] | VM: Analysis

## 9.8 Data-at-Rest Protection

**SRS-DATA-0023** | Data-at-Rest Encryption | The system shall encrypt classification records and GNSS fixes stored in on-device non-volatile storage using an algorithm providing at least 128-bit equivalent cryptographic strength. | Priority: CRITICAL | Stability: STABLE | Source: [STD: RM-0015 §Art.32; STD: RM-0019 §Prov.5.8] | VM: Inspection

## 9.9 External Data Transport Interface

**SRS-DATA-0024** | Transport to Cloud Device-Management Layer | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §6.1; ASSUMPTION: A-0015] | VM: Test

## 9.10 Breakaway Event Record Persistence

**SRS-DATA-0025** | Breakaway Record Commit Timing | The system shall commit a breakaway event record to persistent storage within 5 seconds of separation detection. | Priority: CRITICAL | Stability: STABLE | Source: [ASSUMPTION: A-0018] | VM: Test

**SRS-DATA-0026** | Breakaway Record Survivability | The system shall preserve a committed breakaway event record across power loss, battery depletion, and device reboot. | Priority: CRITICAL | Stability: STABLE | Source: [ASSUMPTION: A-0018] | VM: Test

**SRS-DATA-0027** | Breakaway Record Transmission Trigger | The system shall transmit a committed breakaway event record on the next successful base-station contact following separation. | Priority: HIGH | Stability: STABLE | Source: [ASSUMPTION: A-0018] | VM: Test

## 9.11 Out-of-Scope Data Functions (Boundary Notes — Non-Normative)

The following data-related functions are outside this system's build scope but are documented here, not silently dropped, per the group scope model:

- **Cloud-side storage and analytics** of the data transported under SRS-DATA-0024 is performed by the **[EXTERNAL: IoT Cloud backend team]**. This system's data obligation ends at successful, acknowledged transport to the Device-Management layer.
- **Mobile App presentation/display** of wellness records, classification history, and breakaway alerts is performed by the **[EXTERNAL: Mobile App team]**. No display, formatting, or rendering requirement is levied on the collar/base-station system.
- **Cloud-side home/away state machine** (per A-0016) is **[EXTERNAL: IoT Cloud backend team]**-owned; the device-local home/away state machine referenced elsewhere in this SRS is the sole in-scope authority for power gating, and no data requirement beyond the transport obligation in SRS-DATA-0024 applies here.
