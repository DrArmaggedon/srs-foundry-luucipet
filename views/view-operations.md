# SRS-LUUCIPET — Derived View: Operations & Support

> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T10:30:00Z
> **Audience:** Operations Engineering, Support Engineering, Reliability Engineering, QA, Product Management
> ⚠️ For full context, always refer to the Master SRS.

---

## 1.1 Purpose

This System Requirements Specification (SRS) defines the requirements for the LUUCIPet Wellness Monitor Phase 1 product family — the Mini and Max collar devices, the Base Station family (Charging and Relay tiers), the Collar Connection Fixture (CCF) accessory family, and the Portable Travel Charging Cradle. It translates the LUUCIPet Wellness Monitor PRD v1.3.3 into formally structured, verifiable requirements conforming to IEEE 830 / ISO/IEC/IEEE 29148, to support design, verification, and regulatory conformance.

## 1.2 Scope

**In scope:**  Mini & Max collar HW+FW; Base Station (Charging & Relay) HW+FW; the device-enforced BLE/base-to-cloud protocol (device-management layer interface); the CCF accessory family (widths S/M/L, collar-types -RC/-MG); the Portable Travel Charging Cradle; the LUUCI IoT Cloud Device-Management layer insofar as it defines the collar/base-station-facing interface contract.
**Out of scope (PRD §6.1, §14.1):**  GPS-M variant + cellular (Phase 2, separate PRD); LUUCI Mobile App; IoT Cloud data storage/analytics backend; cloud-side home/away state machine; device-app ICD.

## 1.3 Product Perspective

Collar-mounted behavioral wellness system. Each collar communicates with household Base Stations over BLE; Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi. The collar attaches to the pet's own collar via the CCF, which provides structural retention (Zone 1) and species-appropriate strangulation-prevention breakaway (Zone 2 Fuse Tab). The device engages the CCF through a Twist-Lock interface for charging removal.

---

## 13. Reliability Availability

# §13 — Reliability & Availability Requirements


## 13.0 Scope Note

This section specifies the dependability, availability, and long-run success-rate criteria the system must sustain over the product's operating life and over defined observation windows. It does **not** re-issue constraints already owned elsewhere:

- **Tier-1 (≥85% accuracy / ≤5% false-positive) and Tier-2 (≥80% accuracy / ≤10% false-positive) classification-accuracy thresholds** in PRD §12.2 restate the classification-accuracy floors already owned by §3 Behavioral Classification (SRS-FUNC-0018, SRS-FUNC-0019, SRS-FUNC-0020, SRS-FUNC-0021); §13 does not re-issue them. They are accuracy/performance criteria, not availability/dependability criteria, notwithstanding their placement under the PRD's "Reliability" heading.
- **The IP67 ingress-protection rating as a component property, the device-standalone qualification scope, and the ingress test-parameter/claim-boundary requirements** are owned by §11 Hardware (SRS-HW-0003) and §12 Environmental & Durability (SRS-ENV-0005, SRS-ENV-0006, SRS-ENV-0007, SRS-ENV-0008); §13 owns only the additional temporal criterion that the rating must remain valid across the full expected service lifetime, not the rating itself.
- **OTA image integrity, atomicity, and dual-bank auto-revert mechanics** are owned by §5 OTA Firmware Updates (SRS-FUNC-0052–0057); §13 owns only the resulting aggregate success-rate criterion, not the underlying mechanism.

## 13.1 Ingress-Protection Durability

<a id="srs-reli-0001"></a>

| **SRS-RELI-0001** | **IP67 Rating Retention Over Full Service Lifetime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, standalone and unmated from any CCF, **shall** retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. |
| **Rationale**    | PRD §12.2 states the qualitative criterion "IP67 full lifetime (device standalone)" but does not itself state a numeric service-lifetime duration against which "full lifetime" can be tested. The Product Context Profile records a user-confirmed expected service lifetime of ~2–3 years, with a 2-year floor to be used wherever a single testable figure is required; that floor is applied here as the qualification duration. This requirement is the temporal-endurance complement to the device-standalone IP67 rating already established by SRS-HW-0003 and does not restate the rating itself. \| Verification Method: Analysis \| Cross-References: SRS-HW-0003, SRS-ENV-0005, SRS-ENV-0006<br><br>## 13.2 Collar Device Availability |
| **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0002"></a>

| **SRS-RELI-0002** | **Collar Device Operational Availability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. |
| **Rationale**    | PRD §12.2 states "collar operational ≥99% (excl. charging)" as a direct numeric floor, but — unlike the base station uptime criterion in the same clause, which specifies a 90-day measurement window — the PRD does not state the observation-window length over which collar availability is to be measured. Flagged per the numeric-vagueness gate rather than inventing a window; the 99% floor and the charging exclusion are PRD-stated and are issued as-is. Verification Method corrected from Analysis to Test per V-Method review: this is a directly observable field/DVT proportion metric (uptime vs. total non-charging elapsed time), matching the Test pattern this SRS already applies to equivalent rate/proportion criteria (SRS-FUNC-0018–0021, SRS-FUNC-0001); no MTBF-style modeling basis is stated that would justify Analysis. \| Verification Method: Test \| Cross-References: SRS-HW-0025, SRS-INT-0031, SRS-INT-0032<br><br>## 13.3 Base Station Availability |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0003"></a>

| **SRS-RELI-0003** | **Base Station Uptime** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. |
| **Rationale**    | PRD §12.2 states "base ≥99.5% uptime over 90-day window" as a direct, fully-bounded numeric criterion; the base station's continuous, mains-powered, no-sleep operating profile (PRD §11.7) makes a rolling-window uptime metric directly measurable in the field. Verification Method corrected from Analysis to Test per V-Method review: the criterion is fully bounded (explicit 90-day window) and directly observable via continuous-operation monitoring against the threshold — a practical DVT/pilot burn-in test, not a modeling exercise. \| Verification Method: Test \| Cross-References: —<br><br>## 13.4 OTA Update Success Rate |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |

<a id="srs-reli-0004"></a>

| **SRS-RELI-0004** | **OTA Update Success Rate** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system **shall** achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a base station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. |
| **Rationale**    | PRD §12.2 states "OTA success ≥99%" as a direct numeric floor on the aggregate reliability of the OTA mechanism already specified functionally in §5; "success" is defined operationally against the existing auto-revert criterion (SRS-FUNC-0056) rather than inventing a separate definition. Verification Method corrected from Analysis to Test per V-Method review: this is a repeated-trial pass/fail statistic (run N install attempts, including fault-injected trials per SRS-FUNC-0057, and compute the pass proportion against the 99% floor), matching the Test pattern this SRS already applies to equivalent proportion-based criteria (SRS-FUNC-0001, SRS-FUNC-0018–0021). \| Verification Method: Test \| Cross-References: SRS-FUNC-0055, SRS-FUNC-0056, SRS-FUNC-0057<br><br>--- |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §12.2 |


---
## 14. Usability

## §14 Usability Requirements

**Scope.**  This section specifies the user-experience and usability requirements for the LUUCIPet Wellness Monitor Phase 1 product family — covering collar-device physical interaction, LED/haptic feedback, pairing and onboarding, base-station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features. The companion app's UI design, in-app navigation, notification content, and analytics dashboard are external (delivered by the Mobile App team); requirements that depend on device-to-app data hand-offs are captured as in-scope interface obligations in §14.7.

**Cross-references:**  Pairing protocol → §4 (CONN). OTA functional requirements → §5 (OTA). Safety-indicator behavior → §7 (SAFE). Twist-Lock mechanical specifications → §11 (COMP-HW). Breakaway detection → A-0018.

---

### 14.1 Pairing & Onboarding

| ID              | Requirement                                                                                                                                                                                                                                                                      | Attributes                                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |

## §14 Usability Requirements

**Scope.**  This section specifies the user-experience and usability requirements for the LUUCIPet Wellness Monitor Phase 1 product family — covering collar-device physical interaction, LED/haptic feedback, pairing and onboarding, base-station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features. The companion app's UI design, in-app navigation, notification content, and analytics dashboard are external (delivered by the Mobile App team); requirements that depend on device-to-app data hand-offs are captured as in-scope interface obligations in §14.7.

**Cross-references:**  Pairing protocol → §4 (CONN). OTA functional requirements → §5 (OTA). Safety-indicator behavior → §7 (SAFE). Twist-Lock mechanical specifications → §11 (COMP-HW). Breakaway detection → A-0018.

---

### 14.1 Pairing & Onboarding

| ID              | Requirement                                                                                                                                                                                                                                                                      | Attributes                                                                                                   |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| **SRS-UX-0001** | The collar device shall complete BLE pairing and first-data-sync handshake with a companion app within 3 minutes of the user initiating pairing mode on the device, measured from pairing-mode-entry LED indication to app-confirmed-paired acknowledgment.                      | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                                            |
| **SRS-UX-0002** | The collar device shall support QR-code-based out-of-band (OOB) pairing as the primary pairing method, providing a scannable QR code (on device label or base-station label) that encodes the device identity for LE Secure Connections OOB pairing.                             | CAT=UX PRIORITY=HIGH STABILITY=FIXED **VM=Demonstration** Source: \[PRD §5.6] \[STD: Bluetooth SIG LE Secure Connections] **XR: SRS-CONN-0003** |
| **SRS-UX-0003** | The collar device shall provide a single, visually distinct, and user-accessible physical mechanism (e.g., a recessed or guarded button) to initiate pairing mode, with the mechanism clearly labeled or icon-indicated on the device enclosure.                                 | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Inspection Source: \[PRD §5.6]                                       |
| **SRS-UX-0004** | The collar device LED shall emit a visually distinct indication when the device is in pairing mode (e.g., slow blue blink at 1 Hz, 50% duty cycle) that is distinguishable from all power-on/boot, normal-operation, low-battery, charging, fault, and OTA-state LED patterns defined in §14.3. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test                                                                 |
| **SRS-UX-0005** | The collar device shall automatically exit pairing mode and revert to normal-operation LED indication after 3 minutes if no successful pairing is completed, with no user action required.                                                                                       | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test                                                               |

---

### 14.2 Physical Interaction

| ID              | Requirement                                                                                                                                                                                                                                                             | Attributes                                                               |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| **SRS-UX-0006** | The Twist-Lock mechanism shall provide both an audible click and a tactile force-transition (detent drop) upon successful locking, enabling the user to confirm engagement by sound and feel without visual inspection.                                                 | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |
| **SRS-UX-0007** | The Twist-Lock socket shall provide a magnetic-assist force that draws the device into correct alignment from a distance of ≤5 mm before the lug channels engage, reducing the fine-motor-skill demand of device docking.                                               | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a] |
| **SRS-UX-0008** | The Twist-Lock engage force shall not exceed 5 N press-in axial force and 0.10 N·m rotational torque, enabling a typical adult user to dock the device without a tool or excessive effort. Mechanical specification per §11.                                            | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |
| **SRS-UX-0009** | The device removal workflow (90° counter-clockwise Twist-Lock rotation) shall require a detent-release torque not exceeding 0.15 N·m, such that an adult user can intentionally remove the device without a tool while the mechanism remains inertially immune per §11. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |
| **SRS-UX-0010** | The magnetic pogo-pin charging connector shall achieve ≥90% first-attempt successful seating rate by a user with no prior training, measured in a usability test with a representative sample of ≥20 adult participants across age and dexterity ranges.                | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.5]    |
| **SRS-UX-0011** | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket, providing error-proof (poka-yoke) mating.                                                                                              | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.2a]   |

---

### 14.3 Visual & Auditory Feedback

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                              | Attributes                                         |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| **SRS-UX-0012** | The collar device LED shall communicate at minimum the following distinct operational states to the user: (a) power-on / boot, (b) pairing mode, (c) normal operation, (d) low battery (≤20% SoC), (e) charging / docked, (f) error or fault, and (g) OTA update in progress. LED physical specification per §11.                                        | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test       |
| **SRS-UX-0013** | Each collar-device operational state enumerated in SRS-UX-0012 shall be communicated via a unique combination of LED color, blink cadence, or duty cycle, such that no two states share an identical visual indicator pattern.                                                                                                                           | CAT=UX **PRIORITY=HIGH** STABILITY=FIXED VM=Test     |
| **SRS-UX-0014** | All collar-device LED state indicators shall differentiate critical states (low battery, error/fault) from non-critical states using at minimum temporal-pattern differentiation (blink cadence), ensuring distinguishability under protanopia and deuteranopia (red/green color-blindness) without reliance on red-vs-green color discrimination alone. | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Analysis |
| **SRS-UX-0015** | The Twist-Lock engagement audible click shall produce a sound pressure level of ≥40 dBA measured at 30 cm from the device in a quiet-room baseline (ambient ≤30 dBA), ensuring a typical adult user can confirm engagement by sound.                                                                                                                     | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test     |

---

### 14.4 Base Station UX

| ID              | Requirement                                                                                                                                                                                                                                                                        | Attributes                                                                             |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| **SRS-UX-0016** | The base station shall communicate via LEDs at minimum: (a) AC power present, (b) device charging active (Charging tier only), (c) cloud connectivity established, and (d) OTA update in progress.                                                                                 | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §11.6]                      |
| **SRS-UX-0017** | The base station LEDs should support an automatic ambient-light-responsive dimming mode below approximately 50 lux, or a user-configurable quiet-hours schedule, to reduce bedroom/nighttime light intrusion.                                                                      | CAT=UX PRIORITY=LOW STABILITY=FIXED VM=Test Source: \[PRD §11.6] \[ASSUMPTION: A-0008] |
| **SRS-UX-0018** | The base station initial setup — from AC power-on through Wi-Fi association and cloud-registration to the "cloud-connected" LED indication — shall complete within 5 minutes for a user following the companion app's guided setup flow, assuming compliant home Wi-Fi per A-0009. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                      |

---

### 14.5 CCF User Experience

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                                                                                       | Attributes                                                                              |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- |
| **SRS-UX-0019** | Each CCF variant (CCF-S, CCF-M, CCF-L, and their -RC/-MG collar-type sub-variants) shall be visually and/or tactilely distinguishable from all other variants by at minimum one of: molded-in size designation, distinct body color, or tactile surface differentiation, enabling a user to identify the correct CCF for their pet without measurement tools.                                                     | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Inspection Source: \[PRD §12.4]                 |
| **SRS-UX-0020** | The CCF Zone 1 structural-clamp installation onto a third-party collar shall be achievable by a typical adult user in ≤60 seconds without tools, using only the wrap-and-lock mechanism described in PRD §10.1.3.4.                                                                                                                                                                                               | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                       |
| **SRS-UX-0021** | The CCF Zone 2 fuse tab shall incorporate a clearly visible fracture indicator (e.g., a contrasting-color internal layer exposed on fracture, or a continuous visual element that visibly separates) that is discernible by a user at arm's length (approximately 60 cm) under typical indoor lighting without magnification, enabling the user to visually confirm post-breakaway that the CCF must be replaced. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Inspection Source: \[PRD §10.1.3.2b] \[PRD §10.1.3.6] |

---

### 14.6 Status & Error Communication

| ID              | Requirement                                                                                                                                                                                                                                                                                                                   | Attributes                                                        |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| **SRS-UX-0022** | The collar device shall provide a distinct low-battery LED indication (visually distinct from normal operation per SRS-UX-0013) when the battery state-of-charge reaches ≤20%, and shall persist this indication in every operational state until the device is placed on the charger and charging is confirmed.              | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.4] |
| **SRS-UX-0023** | The collar device shall communicate a fault state (including but not limited to: sensor failure, non-volatile memory corruption, BLE radio initialization failure) via a visually distinct LED pattern that differs from all power-on/boot, normal-operation, low-battery, pairing, charging, and OTA-state patterns.                        | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test                      |
| **SRS-UX-0024** | The collar device shall provide confirmation feedback (LED flash, haptic pulse, or both) within 1 second of a user-initiated physical action (e.g., pairing-mode button press, factory-reset trigger) being successfully registered by the device firmware, so the user is not left uncertain whether the input was received. | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test                    |

---

### 14.7 App-Interface Obligations

> The companion app is delivered by the Mobile App team \[EXTERNAL: Mobile App team]. The requirements in this subsection specify the device-side and base-station-side interface obligations that enable the app's user-facing features. These are in-scope for our delivery.

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Attributes                                                                                               |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **SRS-UX-0025** | The collar device shall include its current battery state-of-charge as a percentage value (0–100) in every sync payload transmitted to the base station, enabling the companion app to display an accurate, real-time battery estimate to the owner.                                                                                                                                                                                                                                                | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                                        |
| **SRS-UX-0026** | The Max collar device shall include the current GNSS fix interval setting (in minutes) in its status payload transmitted in every sync, enabling the companion app to compute and display an interval-aware battery-life estimate and to issue the Max <10-day battery warning.                                                                                                                                                                                                                     | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §12.4]                                        |
| **SRS-UX-0027** | The collar device shall transmit a persistent breakaway/separation event record as defined in A-0018, flagged with elevated transmission priority, on the next successful base-station contact following a breakaway event, enabling the companion app's "CCF Replacement Required" owner notification. The primary post-breakaway safety mitigation remains the passive CCF visible fracture indicator per SRS-UX-0021; the electronic notification is a secondary, best-effort notification only. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §10.1.3.6] \[PRD §12.4] \[ASSUMPTION: A-0018] |

---

### 14.8 OTA Update UX

| ID              | Requirement                                                                                                                                                                                                                                                                                                                                        | Attributes                                                       |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| **SRS-UX-0028** | The collar device shall communicate each distinct OTA update state — Downloading, Verifying, Pending Installation, Installing, Success, and Failed — via a unique LED pattern distinguishable from all other LED states defined in §14.3, enabling the user to understand update progress without the companion app. OTA functional states per §5. | CAT=UX PRIORITY=HIGH STABILITY=FIXED VM=Test Source: \[PRD §9.5] |
| **SRS-UX-0029** | The collar device LED shall remain continuously active during an OTA update, with no dark (LED-off) period exceeding 10 seconds during any OTA state expected to last >30 seconds, preventing the user from misinterpreting a prolonged dark period as a device failure or bricked state.                                                          | CAT=UX PRIORITY=MEDIUM STABILITY=FIXED VM=Test                   |

---

### Summary

| Metric               | Count                                                 |
| :------------------- | :---------------------------------------------------- |
| Total requirements   | 29 (SRS-UX-0001 – SRS-UX-0029)                        |
| Shall (mandatory)    | 28                                                    |
| Should (recommended) | 1 (SRS-UX-0017)                                       |
| Priority: HIGH       | 23                                                    |
| Priority: MEDIUM     | 5                                                     |
| Priority: LOW        | 1 (SRS-UX-0017)                                       |
| VM: Test             | 24                                                    |
| VM: Inspection       | 3 (SRS-UX-0003, SRS-UX-0019, SRS-UX-0021)             |
| VM: Analysis         | 1 (SRS-UX-0014)                                       |
| VM: Demonstration    | 1 (SRS-UX-0002)                                       |
| EXTERNAL attribution | Mobile App team                                       |
| ID range consumed    | SRS-UX-0001 – SRS-UX-0029                             |

---
## 15. Operational Requirements


## 15.0 Scope Note

This section specifies operational behavior of the deployed system that is not already owned by another section: base-station continuous-operation posture and included power accessory, base-station status-indicator inventory (deferred here from §11 per that section's own Drafter Notes), the device-local home/away determination that other sections' power-gating and status requirements depend on, and the collar's duty-cycle/power-optimization behaviors drawn from PRD §15 (Power Budget) that are operational policies rather than hardware capabilities. It does **not** re-issue constraints already owned elsewhere:

- **GNSS interface behavior** (presence on Max, absence on Mini, configurable/default fix interval, A-GPS delivery/validity, fix-acquisition timeout, warm TTFF ceiling) is owned by §10 Interface Requirements (SRS-INT-0021–0029); this section does not restate those numeric bounds.
- **GNSS smart power-gate non-configurability** and the **Max GNSS interface disablement while HOME** are owned by §2 (SRS-OPER-0004) and §10 (SRS-INT-0027) respectively; this section adds only the device-local home/away determination mechanism those two depend on, which was not yet issued anywhere.
- **Battery cell minimum capacities, battery-life targets, idle-current ceiling, and low-battery alert threshold** are owned by §10.4/§11 Hardware (SRS-HW-0020–0024) and §3 Behavioral Classification (SRS-FUNC-0011); this section does not restate those figures.
- **Base-station Wi-Fi/cloud connectivity reliability bound and degraded-mode offline buffering** are owned by §2 (SRS-OPER-0007) and §4 (SRS-CONN-0028/0029); this section does not restate the −70 dBm / 256 kbps bound.
- **Base-station LED dimming / nighttime-mode `SHOULD`** is fully specified by §14 Usability (SRS-UX-0017, per [ASSUMPTION: A-0008]); this section does not re-issue it, only the base LED *inventory* deferred to this section by §11's own Drafter Notes.
- **OTA mechanics, atomicity, and success-rate criteria** are owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004); this section does not restate them.

## 15.1 Base Station Continuous Operation

<a id="srs-oper-0012"></a>

| **SRS-OPER-0012** | **Base Station Continuous Operational Posture** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** remain in a continuously powered, non-sleeping operational state for as long as AC power is supplied, maintaining active BLE scanning and Wi-Fi uplink capability at all times. |
| **Rationale**    | The base station is a mains-powered, always-available relay; PRD §11.7 states continuous operation with no sleep state and BLE scan/uplink always on, distinguishing its operational posture from the battery-powered, power-optimized collar devices. This continuous posture is also the precondition assumed by the base-station uptime criterion (SRS-RELI-0003) and by the household geo-fence mesh's ability to detect collar sightings without a scheduling gap. \| Verification Method: Demonstration \| Cross-References: SRS-RELI-0003 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.7 |

<a id="srs-oper-0013"></a>

| **SRS-OPER-0013** | **AC Power Adapter Inclusion** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** be supplied with an AC-to-USB-C power adapter as an included accessory. |
| **Rationale**    | PRD §11.7 specifies USB-C power with the adapter included, ensuring the base station is immediately operable out of box without requiring the owner to source a separate power adapter. \| Verification Method: Inspection \| Cross-References: none<br><br>## 15.2 Base Station Status Indicators |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.7 |

<a id="srs-oper-0014"></a>

| **SRS-OPER-0014** | **Charging-Tier Base Station LED Inventory** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station (Charging) tier **shall** provide exactly 3 status LEDs, indicating at minimum: AC power presence, device-charging activity, and cloud-connectivity status. |
| **Rationale**    | PRD §4.2/§11.6 specify a 3-LED inventory (power/charging/cloud) for the Charging tier, distinct from the Relay tier's 2-LED inventory (SRS-OPER-0015) because the Relay tier has no charging cradle to indicate. This is a hardware-inventory requirement; the LED *behavior* (indication patterns) for each state is specified by §14 Usability (SRS-UX-0016). \| Verification Method: Inspection \| Cross-References: SRS-OPER-0015, SRS-UX-0016 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.6 |

<a id="srs-oper-0015"></a>

| **SRS-OPER-0015** | **Relay-Tier Base Station LED Inventory** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Base Station (Relay) tier **shall** provide exactly 2 status LEDs, indicating at minimum: AC power presence and cloud-connectivity status. |
| **Rationale**    | The Relay tier omits the charging-activity LED present on the Charging tier (SRS-OPER-0014) because it has no charging cradle to report on, consistent with PRD §4.2's description of the Relay tier as identical to the Charging tier minus the charging cradle. \| Verification Method: Inspection \| Cross-References: SRS-OPER-0014, SRS-UX-0016<br><br>## 15.3 Household Geo-Fence Mesh Participation |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §11.6 |

<a id="srs-oper-0016"></a>

| **SRS-OPER-0016** | **Multi-Base Household Geo-Fence Mesh Participation** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Every base station in a household deployment **shall** participate in a shared geo-fence mesh by independently reporting BLE sighting reports for every collar device within its range. |
| **Rationale**    | PRD §5.3/§4.2 describe up to 8 base stations per household (≥1 Charging) collectively forming a geo-fence mesh; each base station's independent sighting-report contribution (payload structure per SRS-INT-0054) is the mesh's data basis, distinct from the collar-side forwarding-path requirements already owned by §4 (SRS-CONN-0019/0020). \| Verification Method: Demonstration \| Cross-References: SRS-INT-0054, SRS-CONN-0019<br><br>## 15.4 Device-Local Home/Away Determination |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.2 |

<a id="srs-oper-0017"></a>

| **SRS-OPER-0017** | **Device-Local Home/Away State Machine** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** determine its own HOME or AWAY state using a device-local state machine based on Received Signal Strength Indicator (RSSI) readings from paired base stations in range, without reliance on any cloud-side determination. |
| **Rationale**    | PRD §6.4 states dual home/away state machines exist (device-local and cloud-side), and [ASSUMPTION: A-0016] confirms the device-local state machine is the sole in-scope authority for power gating — notably the Max GNSS smart power gate (SRS-INT-0027, SRS-OPER-0004) — with the cloud-side state machine external ([EXTERNAL: IoT Cloud backend team], SRS-OPER-0011). This requirement establishes the existence and RSSI basis of the device-local mechanism that SRS-INT-0027, SRS-OPER-0004, and SRS-PERF-0007 all depend on but which was not yet issued as its own requirement in any approved section. \| Verification Method: Demonstration \| Cross-References: SRS-INT-0027, SRS-OPER-0004, SRS-PERF-0007, SRS-OPER-0011 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0018"></a>

| **SRS-OPER-0018** | **Device-Local Home-to-Away RSSI Transition Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from HOME to AWAY only when no paired base station RSSI reading exceeds −85 dBm for 5 consecutive readings taken at 1 s intervals. |
| **Rationale**    | PRD §4.1/§6.4 state that home/away determination occurs "via multi-base RSSI" but supply no numeric threshold or debounce criterion; [ASSUMPTION: A-0022] resolves this gap (engineered by analogy to [ASSUMPTION: A-0009]'s Wi-Fi RSSI bound) with a conservative −85 dBm threshold, representing the typical "fair/poor" BLE boundary through 3+ interior walls or 15–25 m open-air range in a residential deployment, deliberately biased toward retaining HOME status because a false-AWAY transition needlessly enables the Max GNSS power gate (SRS-INT-0027, SRS-OPER-0004) and increases power draw, whereas a brief false-HOME delay does not. The 5-consecutive-reading/1 s-interval debounce filters transient RSSI dips (e.g., momentary body-shadowing) before committing the transition. This requirement was returned FAIL by the Feasibility Checker (v1; D3 Testability, D4 Completeness) for being issued as a non-normative PRD-gap notice rather than a testable SHALL; it is reissued here as a testable predicate now that [ASSUMPTION: A-0022] supplies the numeric basis, and is split from the AWAY-to-HOME hysteresis criterion (SRS-OPER-0024) per the Single-Predicate Rule. \| Verification Method: Test \| Cross-References: SRS-OPER-0017, SRS-OPER-0024 |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0024"></a>

| **SRS-OPER-0024** | **Device-Local Away-to-Home RSSI Hysteresis Threshold** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device's device-local home/away state machine (SRS-OPER-0017) **shall** transition from AWAY to HOME only when at least one paired base station RSSI reading exceeds −80 dBm for 3 consecutive readings taken at 1 s intervals. |
| **Rationale**    | [ASSUMPTION: A-0022] specifies a 5 dB hysteresis band between the AWAY-transition threshold (−85 dBm, SRS-OPER-0018) and this AWAY-to-HOME re-entry threshold (−80 dBm) to prevent rapid HOME/AWAY oscillation when RSSI hovers near the boundary, which would otherwise cause repeated toggling of the Max GNSS power gate (SRS-INT-0027) and unnecessary power draw. The shorter 3-reading debounce (vs. SRS-OPER-0018's 5-reading debounce) is an intentional asymmetry: re-establishing HOME status should be comparatively responsive once signal recovers, because remaining falsely in AWAY costs more GNSS-on power than a brief false-HOME determination. \| Verification Method: Test \| Cross-References: SRS-OPER-0017, SRS-OPER-0018<br><br>## 15.5 Collar Duty-Cycle & Power-Optimization Policy |
| **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0019"></a>

| **SRS-OPER-0019** | **Wellness-Mode Deep-Sleep Idle State** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device, while in Wellness Mode and not actively processing a motion-triggered confirmation burst, **shall** remain in its deepest available low-power idle state. |
| **Rationale**    | PRD §15.2 specifies deepest-sleep idle as the standard Wellness-Mode duty-cycle baseline underlying the stated battery-life targets; this is the operational-policy statement that the idle-current ceiling itself (SRS-FUNC-0011, ≤4 µA) is verified against. \| Verification Method: Analysis \| Cross-References: SRS-FUNC-0011, SRS-FUNC-0010 |
| **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §15.2 |

<a id="srs-oper-0020"></a>

| **SRS-OPER-0020** | **GNSS Fix-Interval Change Application Timing** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When the owner changes the Max collar variant's configured GNSS fix interval, the collar device **shall** apply the new interval no later than the start of the next scheduled fix-acquisition cycle. |
| **Rationale**    | PRD §15.5 states that a fix-interval change takes effect "within one cycle," bounding how long a stale interval setting may persist. This is the timing/application-policy requirement; the interval's configurable range (30 min–24 h) and default value (2 h) are owned by §10 (SRS-INT-0023, SRS-INT-0024) and not restated here. \| Verification Method: Test \| Cross-References: SRS-INT-0023, SRS-INT-0024 |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §15.5 |

<a id="srs-oper-0021"></a>

| **SRS-OPER-0021** | **Battery Cell Cycle-Life Validation Basis** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Battery-life validation testing **shall** be performed using cells that have completed no fewer than 50 charge/discharge cycles prior to the validation measurement. |
| **Rationale**    | PRD §15.6 specifies a DVT programmable-load validation methodology requiring cells aged to ≥50 cycles before the battery-life pass criterion (≥80% of the §10.4 minimum capacity at 25°C) is evaluated, ensuring the stated battery-life targets (SRS-PERF-0001, SRS-PERF-0002) are validated against realistically aged cells rather than fresh-cell best-case performance. \| Verification Method: Test \| Cross-References: SRS-PERF-0001, SRS-PERF-0002<br><br>## 15.6 Cloud-Loss Fallback Governance |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §15.6 |

<a id="srs-oper-0022"></a>

| **SRS-OPER-0022** | **Device-Local Fallback Authority on Extended Cloud Loss** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The collar device **shall** rely solely on its device-local home/away state machine (SRS-OPER-0017) for all in-scope power-gating behavior when the base station has not had successful cloud contact for more than 24 hours, without requiring any additional fallback logic beyond the state machine's ordinary operation. |
| **Rationale**    | PRD §6.4 frames the device-local state machine's role as a ">24 h cloud loss" fallback governing the Max GNSS gate, implying the cloud-side state machine (external, [EXTERNAL: IoT Cloud backend team]) would otherwise have some role during shorter cloud outages. Per [ASSUMPTION: A-0016], however, the device-local state machine is the SOLE in-scope authority for power gating at all times, not only after 24 hours; this requirement makes explicit that no additional in-scope fallback mechanism activates at the 24-hour mark — the device-local state machine's continuous, unconditional operation (SRS-OPER-0017) already satisfies the PRD's fallback framing without requiring separate logic. \| Verification Method: Analysis \| Cross-References: SRS-OPER-0017, SRS-OPER-0011<br><br>## 15.7 Product Service Lifetime Reference |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.4 |

<a id="srs-oper-0023"></a>

| **SRS-OPER-0023** | **Expected Product Service Lifetime Reference Figure** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system's operational and durability requirements that reference an expected service lifetime **shall** use 2 years as the minimum testable floor, consistent with the Product Context Profile's user-confirmed ~2–3 year expected service lifetime figure. |
| **Rationale**    | This requirement formalizes, as its own SRS-OPER block, the same PCP §8 user-confirmed lifetime figure that SRS-RELI-0001 (§13) already applies as its qualification duration; §13's Drafter Notes flagged that no A-ID currently carries this figure and recommended one be issued. Issuing it here as an explicit OPER requirement — rather than only as an inline PCP dependency note on SRS-RELI-0001 — gives the figure a citable SRS-ID that future sections (e.g., §16 Maintainability's OTA-support-lifetime requirements) can cross-reference directly instead of re-deriving it from the PCP each time. \| Verification Method: Inspection \| Cross-References: SRS-RELI-0001 |
| **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD — ABSENT: service_lifetime_duration_value |


---
## 16. Maintainability


## 16.0 Scope Note

This section specifies the *lifetime-maintenance* obligations implied by PRD §12.7 that are not already owned by another section. It does **not** re-issue constraints already owned elsewhere:

- **OTA mechanics** owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004)
- **SBOM per-release production** owned by §5 (SRS-FUNC-0061)
- **Pre-launch vuln-disclosure gate** owned by §8 (SRS-SEC-0006)
- **Tier-2 via OTA no HW mod** owned by §3 (SRS-FUNC-0034, SRS-FUNC-0035)
- **2-year lifetime floor** owned by §15 (SRS-OPER-0023)
- **Cloud-side maintenance** is [EXTERNAL: IoT Cloud backend team]; in-scope interface obligation remains SRS-DATA-0024 (§9)

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



---

## Coverage Notes

- **§13 Reliability & Availability:** SRS-RELI-0001 through SRS-RELI-0004 (IP67 lifetime retention, collar availability, base station uptime, OTA success rate)
- **§14 Usability:** SRS-UX-0001 through SRS-UX-0029 (pairing/onboarding, physical interaction, LED/haptic feedback, base station UX, CCF UX, status/error communication, app-interface obligations, OTA update UX)
- **§15 Operational Requirements:** SRS-OPER-0001 through SRS-OPER-0023 (base station operation, device-idle profiles, species persistence, home/away state machine, GNSS interval timing, battery validation, cloud-loss fallback, service lifetime reference)
- **§16 Maintainability:** SRS-MAINT-0001 through SRS-MAINT-0003 (OTA capability lifetime, SBOM currency, vulnerability-disclosure process maintenance)
- **Total requirement blocks:** 59 (4 RELI + 29 UX + 23 OPER + 3 MAINT)
- **Note:** SRS-OPER-0008 through SRS-OPER-0011 are attributed to EXTERNAL parties (Mobile App team, IoT Cloud backend team) and are included for interface-awareness.
