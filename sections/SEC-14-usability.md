> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

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

### V-Method Revision Log

| Version | Change | Reason |
| :------ | :----- | :----- |
| v1 → v2 | SRS-UX-0021: VM Test→Inspection. Summary: Inspection 2→3, Test→25. | V-Method Validator FLAG. |
| v2 → v3 | SRS-UX-0002: VM Test→Demonstration + XR SRS-CONN-0003. Summary: Test 25→24, Demonstration 0→1. | CR-0022 (XSC-0011). |
| v3 → v4 | SRS-UX-0013: Priority MEDIUM→HIGH (matches SRS-UX-0012 master + dependent HIGH indicators UX-0022/0023). SRS-UX-0004, SRS-UX-0023: added "power-on/boot" to LED-differentiation lists to align with SRS-UX-0012's 7-state master (also clears Feasibility D4 marginals). Summary: Priority HIGH 22→23, MEDIUM 6→5. | CR-0023 (MODERATE, priority coherence) + CR-0024 (MINOR, completeness drift) — Conflict & Consistency Resolver intra-§14 review, Conductor ACK'd. |
