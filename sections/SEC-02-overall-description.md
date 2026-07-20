> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

*(v3 — SRS-FUNC-0001 split into single-predicate blocks per Feasibility §2-v1 D4-FAIL; SRS-COMP-0001/0003 D5 rephrased to behavioral outcomes. External-Party Scope Model applied. Supersedes v2.)*

## 2.1 Product Functions

The LUUCIPet Wellness Monitor is a collar-mounted behavioral wellness system for cats and dogs, comprising an ultra-light wearable device, a companion household Base Station, and a mechanical Collar Connection Fixture (CCF) accessory family. The system continuously classifies pet behavior on-device (accelerometer-based classification engine), relays behavioral and location data to the LUUCI IoT Cloud Device-Management layer via the Base Station, and supports over-the-air (OTA) firmware and classifier updates. The product is positioned strictly as a general wellness device for animals; it does not perform, and is not intended to support, medical diagnosis. [PRD §1]

At launch (Phase 1), the device ships with two factory-loaded Tier-1 behavioral classifiers (Rest/Sleep, Active/Awake); a broader Tier-2 classifier set is deliverable post-launch exclusively via OTA. [PRD §1], [PRD §4.4]

**Scope-Model note on functional responsibility.**  Per the group Scope Model, product functions are delivered across our build and named external parties; both are documented here:

- **In scope (our build):**  on-device behavioral classification; collar↔base BLE sync and base↔cloud relay (device-management-layer interface); charging (Base Station + Portable Travel Charging Cradle); CCF breakaway/separation detection and event transport (SRS-FUNC-0001, SRS-FUNC-0002); device-side species-profile persistence (SRS-OPER-0003); device-local home/away determination that gates GNSS power behavior, relying solely on the device-local state machine ([ASSUMPTION: A-0016]).
- **External-party (documented, attributed):**  owner-facing Mobile App alerts/onboarding/CCF guidance/dashboards — **[EXTERNAL: Mobile App team]** (SRS-OPER-0008, SRS-OPER-0009, SRS-OPER-0010); IoT Cloud storage/analytics backend and the cloud-side home/away state machine for owner geofence alerting — **[EXTERNAL: IoT Cloud backend team]** (SRS-OPER-0011). Data transport to the cloud is our in-scope hand-off; cloud storage/analytics and app display are external ([ASSUMPTION: A-0015]).
- **Future-phase (deferred, Phase 2):**  GPS-M variant + cellular positioning — not addressed by any requirement in this SRS.

The CCF Zone 2 Fuse Tab breakaway is designed as an indicative strangulation-prevention mitigation with reference to [STD: EU GPSR 2023/988 §Art 6(1)(a) w/ §Art 5]; per [ASSUMPTION: A-0017] this framing is design-level and pending DVT (efficacy for the feline SKU is not yet confirmed). §2's treatment is intentionally light; substantive safety requirements are specified in §7.

## 2.2 Product Variants & Configurations

### 2.2.1 Collar Devices

Two collar variants share a common platform (classification engine, BLE protocol, OTA path, Twist-Lock geometry) but differ in weight class, sensing, and target population:

- **Mini** — ≤10 g; BLE-only; targets all cats and dogs; typical battery life ≥90 days (≥180 days in Longevity Mode). [PRD §1], [PRD §4.1]
- **Max** — ≤22 g; BLE plus full-quality GNSS (receive-only); targets large dogs (>20 kg) and service dogs; battery life ≥45 days at a 2-hour GNSS fix interval, ≥90 days at a 4-hour interval; GNSS is power-gated off while the device is in the HOME state. [PRD §1], [PRD §4.1]

### 2.2.2 Base Station Family

Two Base Station tiers share a common BLE-relay and Wi-Fi-uplink platform:

- **Base Station (Charging)** — BLE relay, Wi-Fi uplink, single-device pogo-pin charging cradle, 3 status LEDs. [PRD §4.2]
- **Base Station (Relay)** — identical to the Charging tier minus the charging cradle; 2 status LEDs. [PRD §4.2]

Both tiers support multi-device BLE connections (Mini and Max concurrently), participate in the household geo-fence mesh, relay OTA payloads to collars, self-update over Wi-Fi, and buffer collar data for at least 30 days during connectivity loss. [PRD §4.2]

### 2.2.3 Collar Connection Fixture (CCF) Family

The CCF is a compound mechanical accessory that attaches the collar device to the pet's own (third-party-supplied) collar. It provides two functionally distinct zones: Zone 1 (structural retention, not a breakaway feature) and Zone 2 (the Fuse Tab — a single-use, species/size-appropriate strangulation-prevention breakaway). The device engages the CCF through a 3-lug Twist-Lock bayonet interface used for charging removal. [PRD §1], [PRD §4.1]

The CCF is offered in width variants S/M/L and collar-type variants -RC (round) and -MG (martingale), sold separately from the in-box default; a Standard CCF (flat-webbing) ships in every box, sized to the collar variant (CCF-S with Mini, CCF-L with Max). [PRD §4.1], [PRD §4.5]

### 2.2.4 Classifier Tiers

- **Tier-1 (factory-loaded):**  Rest/Sleep; Active/Awake. [PRD §4.4]
- **Tier-2 (OTA-delivered, post-launch):**  Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting (dog only), Head-Shaking. [PRD §4.4]

## 2.3 User Characteristics / Personas

The system is designed around six user personas, described here as user context only; owner-facing app features are captured as attributed [EXTERNAL: Mobile App team] requirements (see §2.4), not derived directly from these personas. [PRD §3]

| Persona | Description |
|---|---|
| P1 — Single-Pet Owner | Primary user of a single Mini-equipped pet. |
| P2 — Multi-Pet Household | Manages a mix of Mini and Max devices across multiple pets. |
| P3 — Allergy/Skin-Concern Owner | Relies on fine-grained scratch-behavior logging. |
| P4 — Active-Lifestyle Large-Dog Owner | Primary user of Max, values GNSS behavioral context. |
| P5 — Veterinary Professional | Uses exported behavioral summaries as a wellness-conversation support tool |
| P6 — Service Dog Handler | Monitors welfare of a working service dog (Max). |

## 2.4 General Constraints

**SRS-OPER-0001** | Require at least one Charging-tier base station per household | A household deployment **shall** include at least one Base Station of the Charging tier. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §4.2], [PRD §4.5] | VM: Inspection | XR: SRS-OPER-0002

**SRS-OPER-0002** | Limit base stations per household deployment | A household deployment **shall not** exceed 8 Base Stations, in any combination of Charging and Relay tiers. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.2], [PRD §4.5] | VM: Test | XR: SRS-OPER-0001

**SRS-OPER-0003** | Persist species assignment across resets | The collar device **shall** retain the species flag assigned at onboarding across firmware updates, power cycles, and factory resets. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.5], [PRD §7.2] | VM: Test | XR: SRS-OPER-0009

**SRS-OPER-0004** | Prohibit owner configuration of the GNSS smart power gate | The Max variant's GNSS smart power gate **shall not** be configurable by the owner. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.5] | VM: Inspection

**SRS-OPER-0005** | Bound in-box CCF fitment coverage | The in-box Standard CCF **shall** be dimensionally appropriate for at least 80% of the launch population of the collar variant it ships with. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [PRD §14.2] | VM: Analysis | XR: SRS-OPER-0006, SRS-OPER-0010

**SRS-OPER-0006** | Default to Standard CCF as in-box accessory | The system **shall** ship a Standard (flat-webbing) CCF, sized to the paired collar variant, as the in-box default accessory. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.1], [PRD §14.2] | VM: Inspection | XR: SRS-OPER-0005

**SRS-OPER-0007** | Define degraded-mode behavior below the home Wi-Fi reliability bound | The Base Station **shall** enter offline-buffering mode, retaining collar data for at least 30 days, when the home Wi-Fi connection falls below −70 dBm RSSI at 2.4 GHz or below 256 kbps sustained uplink. | Priority: HIGH | Stability: STABLE | Source: [ASSUMPTION: A-0009] | VM: Test

**SRS-OPER-0008** | Mobile App post-breakaway owner alert (external) | The Mobile App **shall** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. | Priority: HIGH | Stability: STABLE | Source: [PRD §10.1.3.6], [EXTERNAL: Mobile App team] | VM: Analysis — external conformance evidence | XR: SRS-FUNC-0001, SRS-FUNC-0002

**SRS-OPER-0009** | Mobile App species re-onboarding flow (external) | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's species classifier profile. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §4.5], [EXTERNAL: Mobile App team] | VM: Analysis — external conformance evidence | XR: SRS-OPER-0003

**SRS-OPER-0010** | Mobile App CCF fitment/sizing guidance (external) | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [PRD §14.2], [EXTERNAL: Mobile App team] | VM: Analysis — external conformance evidence | XR: SRS-OPER-0005

**SRS-OPER-0011** | Cloud-side home/away state machine for owner geofence alerting (external) | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. | Priority: MEDIUM | Stability: LIKELY-CHANGE | Source: [ASSUMPTION: A-0016], [EXTERNAL: IoT Cloud backend team] | VM: Analysis — external conformance evidence | XR: SRS-OPER-0004

**SRS-COMP-0001** | Require collar-agnostic base station firmware | Base Station firmware **shall** from a single common firmware image, exhibit identical pairing and relay behavior for both Mini and Max collar variants concurrently. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.3], [PRD §4.5] | VM: Test | XR: SRS-COMP-0002

**SRS-COMP-0002** | Require universal CCF-to-device mechanical compatibility | All CCF accessory variants (widths S/M/L; collar-types -RC/-MG) **shall** be mechanically compatible with both Mini and Max collar devices via the common Twist-Lock interface geometry. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §4.1], [PRD §4.3] | VM: Test | XR: SRS-COMP-0001

**SRS-COMP-0003** | Require a shared classification engine and protocol across collar variants | The Mini and Max collar variants **shall** exhibit equivalent behavioral-classification outputs and use an interoperable common BLE communication protocol across the Mini and Max variants. | Priority: HIGH | Stability: STABLE | Source: [PRD §4.3] | VM: Inspection | XR: SRS-COMP-0001

**SRS-FUNC-0001** | Detect CCF breakaway/separation signature | The collar device **shall** detect the CCF breakaway/separation signature using accelerometer-based sensing and commit a persistent breakaway event record to non-volatile storage within 5 s of the separation event, with a false-positive rate not exceeding 0.1% per device-wear-day and a true-event detection rate of at least 99% under DVT drop/tension conditions. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.3.6], [ASSUMPTION: A-0015], [ASSUMPTION: A-0018] | VM: Test | XR: SRS-FUNC-0002, SRS-FUNC-0003, SRS-OPER-0008

**SRS-FUNC-0003** | Preserve and forward the persisted breakaway event on next base-station contact | The persisted breakaway event record **shall** survive subsequent power loss, battery depletion, and reboot without corruption, and be transmitted to the Base Station on the next successful Base Station contact. | Priority: CRITICAL | Stability: STABLE | Source: [PRD §8.4], [PRD §10.1.3.6], [ASSUMPTION: A-0018] | VM: Test | XR: SRS-FUNC-0001, SRS-FUNC-0002

**SRS-FUNC-0002** | Transport breakaway event to IoT Cloud Device-Management layer | The Base Station **shall** transport a recorded breakaway/separation event to the IoT Cloud Device-Management layer on the next successful Base Station contact and cloud sync (event-triggered; no delivery-time guarantee, as post-breakaway the device may be lost, out of range, or depleted). | Priority: CRITICAL | Stability: STABLE | Source: [PRD §10.1.3.6], [PRD §8.5], [ASSUMPTION: A-0015], [ASSUMPTION: A-0018] | VM: Test | XR: SRS-FUNC-0001, SRS-FUNC-0003, SRS-OPER-0008

## 2.5 Assumptions & Dependencies

This section's constraints depend on the following confirmed assumptions (full text in the Assumption Register):

- **[ASSUMPTION: A-0006]** — governing battery cell capacities are the §10.4 minimums
- **[ASSUMPTION: A-0009]** — home Wi-Fi reliability bound
- **[ASSUMPTION: A-0012]** — CCF assembled-mass constant (26 g)
- **[ASSUMPTION: A-0013]** — EU Battery Regulation Art. 11 removability exemption
- **[ASSUMPTION: A-0014]** — CCF-S feline breakaway force basis
- **[ASSUMPTION: A-0015]** — cloud-transport vs cloud-storage/app boundary
- **[ASSUMPTION: A-0016]** — device-local vs cloud-side home/away state machine
- **[ASSUMPTION: A-0017]** — GPSR design-level strangulation-mitigation framing

---

### SRS-ID inventory (§2 v2)
**In-scope:** SRS-OPER-0001–0007 · SRS-COMP-0001–0003 · SRS-FUNC-0001–0003
**External-party:** SRS-OPER-0008–0011
**Total: 16 blocks**
