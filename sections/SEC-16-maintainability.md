> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

CAT: **MAINT** | Maps to: PRD §12.7 (Maintainability) | Cross-refs: PRD §9.5 (SBOM), §13.5, §14.1, §14.2(8)

*(Drafter-authored; §16 v1 — 3 blocks, SRS-MAINT-0001–0003. First draft.)*

## 16.0 Scope Note

This section specifies the *lifetime-maintenance* obligations implied by PRD §12.7 that are not already owned by another section. It does **not** re-issue constraints already owned elsewhere:

- **OTA mechanics** owned by §5 (SRS-FUNC-0043–0062) and §13 (SRS-RELI-0004)
- **SBOM per-release production** owned by §5 (SRS-FUNC-0061)
- **Pre-launch vuln-disclosure gate** owned by §8 (SRS-SEC-0006)
- **Tier-2 via OTA no HW mod** owned by §3 (SRS-FUNC-0034, SRS-FUNC-0035)
- **2-year lifetime floor** owned by §15 (SRS-OPER-0023)
- **Cloud-side maintenance** is [EXTERNAL: IoT Cloud backend team]; in-scope interface obligation remains SRS-DATA-0024 (§9)

## 16.1 OTA-Update Capability Lifetime

**SRS-MAINT-0001** | OTA-Update Capability Availability Through Supported Service Lifetime | The system **shall** retain OTA update capability, for both collar variants and both base station tiers, for no less than 2 years from product launch. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.7] | Verification Method: Inspection | Cross-References: SRS-OPER-0023, SRS-FUNC-0043, SRS-FUNC-0044

## 16.2 SBOM Lifetime Currency

**SRS-MAINT-0002** | SBOM Currency Maintenance Across Supported Service Lifetime | The system's software bill of materials **shall** be kept current for each in-support firmware version throughout the 2-year supported service lifetime defined by SRS-MAINT-0001. | Priority: MEDIUM | Stability: STABLE | Source: [PRD §12.7], [PRD §9.5] | Verification Method: Inspection | Cross-References: SRS-FUNC-0061, SRS-MAINT-0001

## 16.3 Post-Launch Vulnerability-Disclosure Process Continuity

**SRS-MAINT-0003** | Post-Launch Vulnerability-Disclosure Process Maintenance | The public vulnerability-disclosure policy required by SRS-SEC-0006 **shall** remain active and operational for no less than the 2-year supported service lifetime defined by SRS-MAINT-0001. | Priority: HIGH | Stability: STABLE | Source: [PRD §12.7], [STD: RM-0021] | Verification Method: Inspection | Cross-References: SRS-SEC-0006, SRS-MAINT-0001

---

**Drafter Notes:** v1 — 3 blocks. All single-predicate, anchored to SRS-OPER-0023 2-year floor. No new assumptions required. CAT cursor: MAINT-0004 next.
