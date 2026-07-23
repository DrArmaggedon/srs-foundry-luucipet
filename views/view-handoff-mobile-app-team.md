> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T21:00:00Z
⚠️ For full context, always refer to the Master SRS.

---

## Handoff Document — Mobile App Team

This document contains requirements relevant to the Mobile App team, including [EXTERNAL: Mobile App team] obligations from the LUUCIPet SRS.

### External-Party Requirements

<a id="srs-oper-0008"></a>

| **SRS-OPER-0008** | **Mobile App post-breakaway owner alert (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** display a "CCF Replacement Required" notification directing the owner to obtain a replacement CCF, upon receipt of a breakaway/separation-signature event delivered from the device via the cloud. |
| **Rationale**    | Derived from PRD §10.1.3.6. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §10.1.3.6 · SRS-FUNC-0001, SRS-FUNC-0002 |

<a id="srs-oper-0009"></a>

| **SRS-OPER-0009** | **Mobile App species re-onboarding flow (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a species re-onboarding flow that re-assigns the device's species classifier profile. |
| **Rationale**    | Derived from PRD §4.5. | **Priority**     | Medium |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.5 · SRS-OPER-0003 |

<a id="srs-oper-0010"></a>

| **SRS-OPER-0010** | **Mobile App CCF fitment/sizing guidance (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide owner-facing CCF sizing and fitment guidance to help the owner select the correct CCF SKU. |
| **Rationale**    | Derived from PRD §14.2. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | PRD §14.2 · SRS-OPER-0005 |

<a id="srs-func-0041"></a>

| **SRS-FUNC-0041** | **App-Side Scratching Threshold Configuration UI (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Scratching alert threshold. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0036 |

<a id="srs-func-0042"></a>

| **SRS-FUNC-0042** | **App-Side Shaking Threshold Configuration UI (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** provide a user interface for configuring the Shaking alert threshold. |
| **Rationale**    | Derived from PRD §7.8. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.8 · SRS-FUNC-0038

---

<a id="srs-conn-0023"></a>

| **SRS-CONN-0023** | **Mobile App Issuance of Insight-Mode Activation Command (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The Mobile App **shall** issue the Insight-mode activation command to the collar-mounted device. |
| **Rationale**    | Derived from PRD §7.1. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §7.1 · SRS-CONN-0022

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

