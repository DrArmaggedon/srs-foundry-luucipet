> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T21:00:00Z
⚠️ For full context, always refer to the Master SRS.

---

## Handoff Document — IoT Cloud Backend Team

This document contains requirements relevant to the IoT Cloud Backend team, including [EXTERNAL: IoT Cloud backend team] obligations.

### External-Party Requirements

<a id="srs-oper-0011"></a>

| **SRS-OPER-0011** | **Cloud-side home/away state machine for owner geofence alerting (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud Device-Management layer **shall** maintain a cloud-side home/away state machine to support owner-facing geofence alerting. |
| **Rationale**    | Derived from ASSUMPTION: A-0016. | **Priority**     | Medium |
| **Stability**    | Likely-Change |
| **Verification** | Inspection |
| **Traceability** | ASSUMPTION: A-0016 · SRS-OPER-0004 |

<a id="srs-conn-0018"></a>

| **SRS-CONN-0018** | **Cloud Acceptance and Acknowledgment of Uploaded Records (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **shall** accept and acknowledge classification records uploaded by the base station. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §8 · SRS-CONN-0014 |

<a id="srs-conn-0021"></a>

| **SRS-CONN-0021** | **Cloud-Side Deduplication of Multi-Base Uploads (external)** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The IoT Cloud backend **shall** deduplicate classification records that may be uploaded from more than one base station within the same household account. |
| **Rationale**    | Derived from PRD §4.2. | **Priority**     | High |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §4.2 · SRS-CONN-0020, SRS-CONN-0018

### In-Scope Interface Obligations (Device → IoT Cloud)

<a id="srs-conn-0014"></a>

| **SRS-CONN-0014** | **Base Station Upload of Received Records to Cloud** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall** transmit received classification records to the cloud endpoint over the secured Wi-Fi link. |
| **Rationale**    | Derived from PRD §8. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8 · SRS-CONN-0011, SRS-CONN-0009 |

<a id="srs-conn-0015"></a>

| **SRS-CONN-0015** | **Base Station Buffering on Upload-Path Unavailability** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | When the Wi-Fi or cloud connection is unavailable, the base station **shall** buffer received classification records pending upload. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0016 |

<a id="srs-conn-0016"></a>

| **SRS-CONN-0016** | **Buffered Record Upload on Path Restoration** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | Upon restoration of the Wi-Fi or cloud connection, the base station **shall** upload all buffered classification records. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-CONN-0015 |

<a id="srs-conn-0017"></a>

| **SRS-CONN-0017** | **No Discard of Received Records Pending Upload** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The base station **shall not** discard a received classification record while that record is pending upload to the cloud. |
| **Rationale**    | Derived from PRD §8.5. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Test |
| **Traceability** | PRD §8.5 · SRS-FUNC-0027, SRS-CONN-0015 |

<a id="srs-data-0024"></a>

| **SRS-DATA-0024** | **Transport to Cloud Device-Management Layer** |
|------------------|---------------------------------------------------------------------|
| **Statement**    | The system shall transport classification records, breakaway event records, and (Max variant) GNSS fixes to the LUUCI IoT Cloud Device-Management layer via the established base-station sync interface. |
| **Rationale**    | Derived from PRD §6.1; ASSUMPTION: A-0015. | **Priority**     | Critical |
| **Stability**    | Stable |
| **Verification** | Inspection |
| **Traceability** | PRD §6.1; ASSUMPTION: A-0015 |

