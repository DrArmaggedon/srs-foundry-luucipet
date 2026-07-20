
## 12. Environmental and Durability Requirements

This section specifies the environmental exposure conditions, survival criteria, and durability test regimes that the collar device and CCF accessory must withstand: temperature extremes, ingress-protection test parameters, mechanical shock and drop, UV and weathering, chemical exposure, and — for the CCF — post-exposure retention of the safety-critical breakaway-force and detent-torque windows.

### 12.1 Temperature

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0001 | The collar device shall operate within an ambient temperature range of −20 °C to +50 °C without loss of function. | CRITICAL | STABLE | Test |
| SRS-ENV-0002 | The collar device shall withstand storage, while non-operating, at ambient temperatures between −30 °C and +60 °C without degradation of subsequent operational performance. | HIGH | STABLE | Test |
| SRS-ENV-0003 | The CCF shall be subjected to a thermal-cycling exposure regime spanning −20 °C to +50 °C, per the IEC 60068-2-14 Test Na profile, without loss of function. | HIGH | STABLE | Test |
| SRS-ENV-0004 | The collar device should withstand a damp-heat exposure per IEC 60068-2-78 without loss of function. | MEDIUM | STABLE | Test |

### 12.2 Ingress Protection

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0005 | Product documentation and marketing materials shall not state or imply an IP67, or equivalent, ingress-protection rating for the collar device while mated to any CCF. | CRITICAL | STABLE | Inspection |
| SRS-ENV-0006 | The IP67 ingress-protection rating claimed for the collar device shall be confirmed by an independent, accredited test laboratory and documented in a test report prior to product launch. | HIGH | STABLE | Inspection |
| SRS-ENV-0007 | The Twist-Lock lug channels shall exclude water ingress along the channel path when subjected to the IP67 immersion test applicable to SRS-HW-0003. | CRITICAL | STABLE | Test |
| SRS-ENV-0008 | The ingress-protection seal boundary shall be located on the interior side of the enclosure assembly such that it is not directly exposed on any externally accessible mating surface. | HIGH | STABLE | Inspection |

### 12.3 Mechanical Durability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0009 | The collar device shall survive a free-fall drop of 1.5 meters onto a hard surface without loss of function. | CRITICAL | STABLE | Test |
| SRS-ENV-0010 | The collar device should withstand mechanical shock per IEC 60068-2-27 without loss of function. | MEDIUM | STABLE | Test |
| SRS-ENV-0011 | The collar device should withstand vibration per IEC 60068-2-64 without loss of function. | MEDIUM | STABLE | Test |

### 12.4 UV and Weathering

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0012 | The collar device enclosure material shall be UV-stabilized to resist degradation from prolonged outdoor solar exposure over the product's service lifetime. | CRITICAL | STABLE | Analysis |
| SRS-ENV-0013 | The CCF shall withstand 2,000 hours of ultraviolet exposure per IEC 60068-2-5 without loss of function. | CRITICAL | STABLE | Test |

### 12.5 Chemical Resistance

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0014 | The CCF shall withstand 24 hours of continuous exposure to each of the following fluids without loss of function: pet shampoo formulations across pH 5.5 to 8.5, enzymatic pet-odor and stain cleaners, fresh water, and salt water. | HIGH | STABLE | Test |

### 12.6 CCF Environmental Durability — Post-Exposure Retention

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-ENV-0015 | Following completion of the thermal-cycling exposure specified in SRS-ENV-0003, the Zone 2 Fuse Tab breakaway force shall remain within its SKU-specific force window as defined in SRS-SAFE-0001, SRS-SAFE-0002, and SRS-SAFE-0003. | CRITICAL | STABLE | Test |
| SRS-ENV-0016 | Following completion of the thermal-cycling exposure, the Twist-Lock detent release torque shall remain within the torque window defined in SRS-INT-0044. | HIGH | STABLE | Test |
| SRS-ENV-0017 | Following completion of the UV-aging exposure specified in SRS-ENV-0013, the Zone 2 Fuse Tab breakaway force shall remain within its SKU-specific force window. | CRITICAL | STABLE | Test |
| SRS-ENV-0018 | Following completion of the chemical-fluid exposure specified in SRS-ENV-0014, the Zone 2 Fuse Tab breakaway force shall remain within its SKU-specific force window. | CRITICAL | STABLE | Test |

---

## 13. Reliability and Availability Requirements

This section specifies the dependability, availability, and long-run success-rate criteria the system must sustain over the product's operating life. Classification-accuracy thresholds are owned by Section 3; OTA mechanics by Section 5; ingress rating as a component property by Section 11.

### 13.1 Ingress-Protection Durability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0001 | The collar device, standalone and unmated from any CCF, shall retain its IP67 ingress-protection rating (SRS-HW-0003) for no less than 2 years of expected service life. | CRITICAL | STABLE | Analysis |

### 13.2 Collar Device Availability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0002 | The collar device shall achieve an operational availability of no less than 99%, excluding any time during which the device is docked and charging. | HIGH | STABLE | Test |

### 13.3 Base Station Availability

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0003 | The Base Station shall achieve an uptime of no less than 99.5%, measured over any rolling 90-day window. | HIGH | STABLE | Test |

### 13.4 OTA Update Success Rate

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-RELI-0004 | The system shall achieve an OTA firmware update success rate of no less than 99%, measured as the proportion of initiated OTA installation attempts — on either a collar-mounted device or a Base Station — that complete successfully without invoking the dual-bank auto-revert defined in SRS-FUNC-0056. | HIGH | STABLE | Test |

---

## 14. Usability Requirements

This section specifies user-experience and usability requirements covering collar-device physical interaction, LED and haptic feedback, pairing and onboarding, Base Station setup and indicators, CCF accessory user experience, status and error communication, OTA update user experience, and device-side data obligations that enable the companion app's user-facing features.

### 14.1 Pairing and Onboarding

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0001 | The collar device shall complete BLE pairing and first-data-sync handshake with a companion app within 3 minutes of the user initiating pairing mode on the device. | HIGH | STABLE | Test |
| SRS-UX-0002 | The collar device shall support QR-code-based out-of-band (OOB) pairing as the primary pairing method. | HIGH | STABLE | Demonstration |
| SRS-UX-0003 | The collar device shall provide a single, visually distinct, and user-accessible physical mechanism to initiate pairing mode. | HIGH | STABLE | Inspection |
| SRS-UX-0004 | The collar device LED shall emit a visually distinct indication when the device is in pairing mode, distinguishable from all other operational-state LED patterns. | HIGH | STABLE | Test |
| SRS-UX-0005 | The collar device shall automatically exit pairing mode and revert to normal-operation LED indication after 3 minutes if no successful pairing is completed. | MEDIUM | STABLE | Test |

### 14.2 Physical Interaction

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0006 | The Twist-Lock mechanism shall provide both an audible click and a tactile force-transition (detent drop) upon successful locking. | HIGH | STABLE | Test |
| SRS-UX-0007 | The Twist-Lock socket shall provide a magnetic-assist force that draws the device into correct alignment from a distance of 5 mm or less before the lug channels engage. | MEDIUM | STABLE | Test |
| SRS-UX-0008 | The Twist-Lock engage force shall not exceed 5 N press-in axial force and 0.10 N·m rotational torque. | HIGH | STABLE | Test |
| SRS-UX-0009 | The device removal workflow (90° counter-clockwise Twist-Lock rotation) shall require a detent-release torque not exceeding 0.15 N·m. | HIGH | STABLE | Test |
| SRS-UX-0010 | The magnetic pogo-pin charging connector shall achieve a 90% or greater first-attempt successful seating rate by a user with no prior training. | HIGH | STABLE | Test |
| SRS-UX-0011 | The Twist-Lock asymmetric lug keying shall physically prevent incorrect-orientation insertion of the device into the CCF socket. | HIGH | STABLE | Test |

### 14.3 Visual and Auditory Feedback

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0012 | The collar device LED shall communicate at minimum the following distinct operational states: power-on/boot, pairing mode, normal operation, low battery (20% SoC or below), charging/docked, error or fault, and OTA update in progress. | HIGH | STABLE | Test |
| SRS-UX-0013 | Each collar-device operational state shall be communicated via a unique combination of LED color, blink cadence, or duty cycle, such that no two states share an identical visual indicator pattern. | HIGH | STABLE | Test |
| SRS-UX-0014 | All collar-device LED state indicators shall differentiate critical states (low battery, error/fault) from non-critical states using at minimum temporal-pattern differentiation, ensuring distinguishability under red/green color-blindness. | MEDIUM | STABLE | Analysis |
| SRS-UX-0015 | The Twist-Lock engagement audible click shall produce a sound pressure level of 40 dBA or greater measured at 30 cm from the device in a quiet-room baseline (ambient 30 dBA or below). | MEDIUM | STABLE | Test |

### 14.4 Base Station UX

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0016 | The Base Station shall communicate via LEDs at minimum: AC power present, device charging active (Charging tier only), cloud connectivity established, and OTA update in progress. | HIGH | STABLE | Test |
| SRS-UX-0017 | The Base Station LEDs should support an automatic ambient-light-responsive dimming mode below approximately 50 lux, or a user-configurable quiet-hours schedule. | LOW | STABLE | Test |
| SRS-UX-0018 | The Base Station initial setup — from AC power-on through Wi-Fi association and cloud-registration to the "cloud-connected" LED indication — shall complete within 5 minutes. | HIGH | STABLE | Test |

### 14.5 CCF User Experience

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0019 | Each CCF variant shall be visually and/or tactilely distinguishable from all other variants, enabling a user to identify the correct CCF for their pet without measurement tools. | HIGH | STABLE | Inspection |
| SRS-UX-0020 | The CCF Zone 1 structural-clamp installation onto a third-party collar shall be achievable by a typical adult user in 60 seconds or less without tools. | HIGH | STABLE | Test |
| SRS-UX-0021 | The CCF Zone 2 fuse tab shall incorporate a clearly visible fracture indicator discernible by a user at arm's length (approximately 60 cm) under typical indoor lighting without magnification. | HIGH | STABLE | Inspection |

### 14.6 Status and Error Communication

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0022 | The collar device shall provide a distinct low-battery LED indication when battery state-of-charge reaches 20% or below, and shall persist this indication in every operational state until the device is placed on the charger and charging is confirmed. | HIGH | STABLE | Test |
| SRS-UX-0023 | The collar device shall communicate a fault state via a visually distinct LED pattern that differs from all other operational-state patterns. | HIGH | STABLE | Test |
| SRS-UX-0024 | The collar device shall provide confirmation feedback (LED flash, haptic pulse, or both) within 1 second of a user-initiated physical action being successfully registered by the device firmware. | MEDIUM | STABLE | Test |

### 14.7 App-Interface Obligations

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0025 | The collar device shall include its current battery state-of-charge as a percentage value (0–100) in every sync payload transmitted to the Base Station. | HIGH | STABLE | Test |
| SRS-UX-0026 | The Max collar device shall include the current GNSS fix interval setting (in minutes) in its status payload transmitted in every sync. | HIGH | STABLE | Test |
| SRS-UX-0027 | The collar device shall transmit a persistent breakaway/separation event record, flagged with elevated transmission priority, on the next successful Base Station contact following a breakaway event. | HIGH | STABLE | Test |

### 14.8 OTA Update UX

| ID | Requirement | Priority | Stability | Verification Method |
| :-- | :---------- | :------- | :-------- | :------------------ |
| SRS-UX-0028 | The collar device shall communicate each distinct OTA update state — Downloading, Verifying, Pending Installation, Installing, Success, and Failed — via a unique LED pattern distinguishable from all other LED states. | HIGH | STABLE | Test |
| SRS-UX-0029 | The collar device LED shall remain continuously active during an OTA update, with no dark (LED-off) period exceeding 10 seconds during any OTA state expected to last more than 30 seconds. | MEDIUM | STABLE | Test |

