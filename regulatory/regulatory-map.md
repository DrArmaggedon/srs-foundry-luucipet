> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Session:**  S-luucipet · **Product:**  LUUCIPet Wellness Monitor v1.3.3 · **Verification date:**  2026-07-13
**Policy:**  Tiered (Tier-1 existence/currency/scope verified via live web; Tier-2 clause-level from documented structure; Tier-3 UNCERTAIN reserved for genuine applicability/existence doubt).
**RM-ID range issued:**  RM-0001 … RM-0031 · **Next RM cursor:**  RM-0032
**Confidence tally:**  CONFIRMED 18 · INDICATIVE 9 · UNCERTAIN 2 (+1 miscitation flag resolved via RM-0030). RM-0031 added (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT).

## A. Horizontal — Radio / Wireless

| **RM-0001** | **FCC 47 CFR Part 15 Subpart C** |
|-------------|----------------------------|
| **Clause** | §15.247 |
| **Market** | US |
| **Applies To** | Mini/Max/Base |
| **Confidence** | CONFIRMED |
| **Verification note** | BLE 2.4 GHz intentional radiator. |

| **RM-0002** | **FCC 47 CFR Part 15 Subpart B** |
|-------------|----------------------------|
| **Clause** | §15.107/.109 |
| **Market** | US |
| **Applies To** | System |
| **Confidence** | CONFIRMED |
| **Verification note** | Unintentional emissions. |

| **RM-0003** | **RED Directive 2014/53/EU** |
|-------------|------------------------|
| **Clause** | Art 3.1(a),3.1(b),3.2 |
| **Market** | EU |
| **Applies To** | Mini/Max/Base |
| **Confidence** | CONFIRMED |
| **Verification note** | Current. |

| **RM-0004** | **ETSI EN 300 328** |
|-------------|---------------|
| **Clause** | §4.3 |
| **Market** | EU |
| **Applies To** | Mini/Max/Base |
| **Confidence** | INDICATIVE |
| **Verification note** | Correct 2.4 GHz RED HS; PRD cites v2.2.2 — verify exact OJ-listed version. |

| **RM-0005** | **UK Radio Equipment Regs 2017 (SI 2017/1206)** |
|-------------|-------------------------------------------|
| **Clause** | — |
| **Market** | UK |
| **Applies To** | Mini/Max/Base |
| **Confidence** | CONFIRMED |
| **Verification note** | UKCA. |

| **RM-0006** | **ISED RSS-247 Issue 2 + RSS-Gen Issue 5** |
|-------------|--------------------------------------|
| **Clause** | — |
| **Market** | CA |
| **Applies To** | Mini/Max/Base |
| **Confidence** | INDICATIVE |
| **Verification note** | Verify current issue numbers at submission. |

| **RM-0007** | **AS/NZS 4268:2017** |
|-------------|----------------|
| **Clause** | — |
| **Market** | AU/NZ |
| **Applies To** | Mini/Max/Base |
| **Confidence** | INDICATIVE |
| **Verification note** | RCM; verify no newer edition. |

| **RM-0008** | **Bluetooth SIG Qualification (QDID)** |
|-------------|----------------------------------|
| **Clause** | — |
| **Market** | Global |
| **Applies To** | all BLE |
| **Confidence** | CONFIRMED |
| **Verification note** | Mandatory per Bluetooth SIG. |

| **RM-0009** | **GNSS passive-receiver intentional-radiator exemption** |
|-------------|----------------------------------------------------|
| **Clause** | — |
| **Market** | US/EU/UK/CA/AU-NZ |
| **Applies To** | Max |
| **Confidence** | INDICATIVE |
| **Verification note** | Per-market; PRD §13.1 defers to Regulatory Lead. **Escalated to user.** |

| **RM-0029** | **IEC 62311 / EN 62311 (RF human-exposure) + FCC RF-exposure rules (47 CFR §1.1310/§2.1093)** |
|-------------|-----------------------------------------------------------------------------------------|
| **Clause** | — |
| **Market** | EU/UK/US (+ per-market) |
| **Applies To** | Mini/Max/Base |
| **Confidence** | INDICATIVE |
| **Verification note** | USER DECISION: map now, confirm per-market applicability/thresholds. Tier-1: standards exist/current. Animal-worn 2.4 GHz TX (≥+8 dBm) + mains base station plausibly trigger RF-exposure assessment; low-power animal-worn category & exact thresholds per-market. Annotate derived reqs [INDICATIVE]. |


## B. Horizontal — Battery / Electrical Safety

| **RM-0010** | **UN 38.3** |
|-------------|----------|
| **Clause** | Part III 38.3 |
| **Market** | Global |
| **Applies To** | Mini/Max |
| **Confidence** | CONFIRMED |
| **Verification note** | Before pilot production. |

| **RM-0011** | **IEC 62133-2:2017 **+AMD1:2021** (Ed 1.1)** |
|-------------|----------------------------------------|
| **Clause** | Cl 7 |
| **Market** | EU (+intl) |
| **Applies To** | Mini/Max |
| **Confidence** | CONFIRMED (version-corrected) |
| **Verification note** | PRD cites bare :2017 → cite with AMD1. ED2 effective 2026-05-29, monitor. |

| **RM-0012** | **UL 1642 / UL 2054** |
|-------------|-----------------|
| **Clause** | — |
| **Market** | US |
| **Applies To** | Mini/Max |
| **Confidence** | CONFIRMED |
| **Verification note** | US cell/pack. |

| **RM-0013** | **EN 62368-1:2020 / UL 62368-1** |
|-------------|----------------------------|
| **Clause** | — |
| **Market** | EU, US |
| **Applies To** | Base |
| **Confidence** | CONFIRMED |
| **Verification note** | Mains-powered base station. |

| **RM-0014** | **EU Battery Regulation (EU) 2023/1542** |
|-------------|------------------------------------|
| **Clause** | Art 6, **Art 11 removability**, labelling/CE |
| **Market** | EU |
| **Applies To** | Mini/Max/Base |
| **Confidence** | CONFIRMED (removability INDICATIVE) |
| **Verification note** | Applicable since 18 Aug 2025; **Art 11 end-user removability mandatory 18 Feb 2027**. ⚠️ LUUCIPet battery is NON-SWAPPABLE (§14.1) → **potential conflict** vs Art 11 within 2–3 yr market life. Verify small/sealed/IP-rated exemption. → Conflict Resolver + user. |


## C. Horizontal — Privacy / Cybersecurity

| **RM-0015** | **GDPR (EU) 2016/679** |
|-------------|------------------|
| **Clause** | Art 5,25,32 |
| **Market** | EU |
| **Applies To** | System |
| **Confidence** | CONFIRMED |
| **Verification note** | Owner PII + Max GNSS location = personal data. |

| **RM-0016** | **UK GDPR + DPA 2018** |
|-------------|------------------|
| **Clause** | — |
| **Market** | UK |
| **Applies To** | System |
| **Confidence** | CONFIRMED |
| **Verification note** | — |

| **RM-0017** | **CCPA/CPRA** |
|-------------|----------|
| **Clause** | — |
| **Market** | US-CA |
| **Applies To** | System |
| **Confidence** | INDICATIVE |
| **Verification note** | Applies if thresholds met; ~5,000 units may not initially meet. |

| **RM-0018** | **PIPEDA** |
|-------------|----------|
| **Clause** | — |
| **Market** | CA |
| **Applies To** | System |
| **Confidence** | CONFIRMED |
| **Verification note** | — |

| **RM-0019** | ****ETSI EN 303 645:2025**** |
|-------------|------------------------|
| **Clause** | Prov 5.1–5.13 |
| **Market** | EU, UK |
| **Applies To** | System |
| **Confidence** | CONFIRMED (version-corrected — PRD STALE) |
| **Verification note** | 🔴 PRD cites V3.1.3; **EN 303 645:2025** now RED-harmonised & mandatory for EU (~1 Jul 2026). Cite :2025. Clause-level INDICATIVE. |

| **RM-0020** | **RED Delegated Reg (EU) 2022/30** |
|-------------|------------------------------|
| **Clause** | Art 3.3(d)(e)(f) |
| **Market** | EU |
| **Applies To** | Mini/Max/Base |
| **Confidence** | CONFIRMED (transitional) |
| **Verification note** | Applicable 1 Aug 2025; being repealed in favor of CRA — align to CRA. |

| **RM-0021** | **EU Cyber Resilience Act (EU) 2024/2847** |
|-------------|--------------------------------------|
| **Clause** | Annex I; Art 13–14 |
| **Market** | EU |
| **Applies To** | System |
| **Confidence** | CONFIRMED |
| **Verification note** | Vuln reporting 11 Sep 2026; full 11 Dec 2027 (PRD dates correct). |

| **RM-0022** | **UK PSTI Act 2022 (+ SI 2023/1007)** |
|-------------|---------------------------------|
| **Clause** | security schedule |
| **Market** | UK |
| **Applies To** | System |
| **Confidence** | CONFIRMED |
| **Verification note** | In force. |

| **RM-0023** | **FCC Cyber Trust Mark** |
|-------------|--------------------|
| **Clause** | — |
| **Market** | US |
| **Applies To** | System |
| **Confidence** | INDICATIVE |
| **Verification note** | Voluntary. |


## D. Horizontal — Materials / Environmental / Ingress / Product Safety

| **RM-0024** | **EU GPSR (EU) 2023/988** |
|-------------|---------------------|
| **Clause** | Art 5, **Art 6** |
| **Market** | EU |
| **Applies To** | System + CCF |
| **Confidence** | CONFIRMED |
| **Verification note** | Applicable 13 Dec 2024. Underpins Zone-2 breakaway safety case; supports A-0002/A-0010 design duty. |

| ****RM-0031**** | **EU GPSR (EU) 2023/988 — design-level strangulation-mitigation branch** |
|-------------|--------------------------------------------------------------------|
| **Clause** | **Art 6(1)(a)**  [assessment: product characteristics/design] READ WITH Art 5 [general safety req] & Recital 22 [design-first hierarchy] |
| **Market** | EU |
| **Applies To** | CCF (Zone 2 breakaway) |
| **Confidence** | **INDICATIVE-pending-DVT** |
| **Verification note** | Refines RM-0024 for the specific claim (PRD §14.2/§10.1.4) that the compound-CCF breakaway = design-level strangulation mitigation. Applicability CONFIRMED (Tier-1 EUR-Lex CELEX:32023R0988). CITATION-PRECISION: obligation is Art 5; Art 6(1)(a) is assessment criteria — cite BOTH, not Art 6(1) alone. Efficacy INDICATIVE-pending-DVT: unproven esp. feline SKU (A-0014 airway caveat + CCF-L retention-floor overlap). Substantiation needed: DVT breakaway-force testing to SKU windows + feline-airway validation + documented GPSR Art 9 risk-assessment file. Supporting animal-collar-release std = ASTM F2056 per RM-0030 (NOT ASTM F2727 — miscitation resolved in RM-0030). Distinct from A-0013 (Battery Reg Art 11) — not conflated. New assumption A-0017 issued to carry this framing. |

| **RM-0025** | **UK GPSR 2005 / US CPSA** |
|-------------|----------------------|
| **Clause** | — |
| **Market** | UK, US |
| **Applies To** | System + CCF |
| **Confidence** | CONFIRMED |
| **Verification note** | — |

| **RM-0026** | **REACH (EC)1907/2006 · RoHS 2011/65/EU + 2015/863 · CA Prop 65** |
|-------------|-------------------------------------------------------------|
| **Clause** | REACH Annex XVII; RoHS Annex II |
| **Market** | EU, UK, US-CA |
| **Applies To** | device + CCF |
| **Confidence** | CONFIRMED |
| **Verification note** | Animal-contact materials; no chrome/nickel. |

| **RM-0027** | **WEEE 2012/19/EU · EU PPWR · UK Producer Responsibility** |
|-------------|------------------------------------------------------|
| **Clause** | — |
| **Market** | EU, UK |
| **Applies To** | System + packaging |
| **Confidence** | CONFIRMED |
| **Verification note** | — |

| **RM-0028** | **IEC 60529 (IP67) + IEC 60068-2-1/-2-2/-2-5/-2-14/-2-27/-2-64/-2-68/-2-78** |
|-------------|------------------------------------------------------------------------|
| **Clause** | ingress + env test |
| **Market** | Global |
| **Applies To** | Mini/Max/CCF |
| **Confidence** | CONFIRMED (clause INDICATIVE) |
| **Verification note** | Supports A-0003 (60068-2-14 Test Na thermal cycling — CONFIRMED appropriate basis). |


## E. Vertical Scan

Consumer-IoT vertical fully covered by RM-0019. NISTIR 8259 = US voluntary guidance (not issued as mandatory RM row). **No Medical / Automotive / Aviation / Industrial-OT / Payment / Critical-Infra verticals triggered** — the NOT-a-medical-device boundary (§13.6) keeps IEC 62304 / EU MDR / FDA out. ✅ No vertical leakage.

## Assumption Confirmations

- **A-0002** (Zone-2 blunt-edge method): PARTIALLY CONFIRMED → keep **INDICATIVE**, method-only. GPSR Art 6 (RM-0024) supports a sharp-edge test methodology; toy-safety analog on an animal product has no direct mandate.
- **A-0010** (device-absent entrapment 12 mm probe): **INDICATIVE** — GPSR foreseeable-hazard duty supports a geometric check; specific probe is engineered default.
- **A-0011** (battery-ingestion = Li-Po pouch, NOT coin cell): **CONFIRMED.**  Reese's Law / 16 CFR 1263 / UL 4200A apply only to button/coin cells, explicitly not pouch/prismatic Li-Po. General ingestion/small-part warning under GPSR/CPSA is correct basis.

## 🔴 UNCERTAIN — needs user decision (batched, FULL mode)

1. **RM-0009 — GNSS passive-receiver intentional-radiator exemption.**  Per-market applicability; PRD defers to Regulatory Lead. Options: A) CONFIRMED (accept exempt-unintentional-emitter across 5 markets) · B) INDICATIVE (map, per-market confirm before each submission) · C) Exclude (defer GNSS radio treatment).
2. **RM-EMC-001 (candidate) — RF human/animal-exposure standard (IEC 62311 / EN 62311 / FCC RF-exposure).**  Collar worn continuously + mains base station plausibly trigger RF-exposure assessment. Options: A) CONFIRMED (adopt IEC/EN 62311 basis now) · B) INDICATIVE (map, per-market confirm) · C) Exclude (defer).

## 🟥 Breakaway-Force Citation — RESOLVED (user: anchor to ASTM F2056)

RM-0030 — ASTM F2056 "Standard Consumer Safety Specification for Pet Collars" — CONFIRMED (existence/scope) at STANDARD LEVEL; feline force value UNVERIFIED.  Verified: ASTM F2727-09(2025) = "Standard Guide for Manufacturers for Labeling **Headgear** Products." PRD (§10.1.3.2b, §13.2, PCP) wrongly cites it as the feline ≤20 N breakaway ceiling source. Plausibly-intended standard = **ASTM F2056 "Standard Consumer Safety Specification for Pet Collars"**  (confirmed to exist), but could NOT confirm F2056 specifies a numeric ≤20 N feline force. The **CCF-M/L "canine guidance"**  ceilings have **no identifiable standard basis** (no ASTM/EN canine breakaway-force standard found).
Consequence: cat CCF-S ≤20 N ceiling cannot be traced to F2727 → citation must be corrected; CCF-M/L canine ceilings treated as **engineering-derived** ( `[ASSUMPTION]`), not `[STD:]`. **Escalated to user (Tier-3).**

## Routing to Conflict & Consistency Resolver

- RM-0014: EU Battery Reg Art 11 removability vs non-swappable battery → potential conflict.
- Version corrections: SRS `[STD:]` tags must cite **EN 303 645:2025** and **IEC 62133-2:2017/AMD1:2021** (not the PRD's older versions).

---

*Regulatory Agent-authored (inline), Conductor-persisted to shared store per standing fix. Map Version v1.2 — added RM-0031 (GPSR Art 6(1)(a)/Art 5 design-mitigation branch, INDICATIVE-pending-DVT) from targeted determination during §2 drafting; header/cursor/tally reconciled.*
