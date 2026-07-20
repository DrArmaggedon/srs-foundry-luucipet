> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Session:**  S-luucipet · **Source:**  Normalized PRD (LUUCIPet Wellness Monitor v1.3.3)

## 1. Product Class

Consumer IoT animal-wellness wearable system (collar-mounted) + companion base-station gateway + mechanical safety accessory (CCF). NOT a medical/veterinary device.

## 2. Variants In Scope

- **Mini** — ≤10 g device; BLE-only; 3-axis accelerometer; all cats & dogs; in-box CCF-S (15–20 N fuse).
- **Max** — ≤22 g device; BLE + full-quality GNSS (receive-only); large dogs (>20 kg) & service dogs; in-box CCF-L (28–40 N fuse).
- **Base Station (Charging)**  and **Base Station Relay** — BLE central + Wi-Fi gateway; charging variant adds pogo-pin cradle.
- **CCF accessory family** — CCF-S/M/L width variants + -RC/-MG collar-type variants; PA66-GF30 UV; Zone 1 clamp + Zone 2 fuse tab.
- **Portable Travel Charging Cradle** — passive charging accessory.
- **OUT OF SCOPE:**  GPS-M variant, cellular, Mobile App, Cloud storage/analytics, cloud-side home/away state machine, device-app ICD.

## 3. Deployment Environment

Domestic household; up to 8 base stations/household (≥1 charging). Outdoor pet exposure: −20 to +50 °C operating; IP67 (device standalone). Home Wi-Fi 2.4 GHz 802.11 b/g/n assumed. Pet biomechanical loads up to 50 g head-shake (large dog).

## 4. Connectivity

- **BLE 5.x** collar↔base (peripheral/central), AES-128 CCM + LE Secure Connections, QR OOB pairing, adv 60 s default (1–180 s), ≥9 m open-air, TX ≥+8 dBm, address randomization.
- **Wi-Fi 2.4 GHz** base↔cloud, TLS 1.3.
- **GNSS (Max only)**  — passive receiver, A-GPS, 30 min–24 h fix interval (default 2 h), HOME power-gate.

## 5. Power / Battery

- Li-Po cells: Mini ≥120 mAh; Max ≥400 mAh (min capacities per §10.4). *[Note: §15.3 illustrative table uses 130/450 mAh — see conflict I-1.]*
- Battery lives: Mini ≥90 d typ / ≥60 min / ≥180 Longevity; Max ≥45/≥30 @2h, ≥90/≥65 @4h, ≥180/≥130 @12h.
- Idle current ≤4 µA (Wellness Mode). Full charge ≤2 h. Protection: overcharge/over-discharge/short/over-temp.

## 6. Safety-Critical Elements

- **Strangulation prevention** = Zone 2 Fuse Tab breakaway (SKU force windows: S 15–20 N, M 20–28 N, L 28–40 N). Single-use; visible fracture indicator; device SHALL NOT be worn without intact Zone 2.
- **Zone 1** structural retention ≥50 N (NOT breakaway). **Twist-Lock** >100 N axial (NOT breakaway; charging removal only).
- Chew resistance (250 N compressive, FT-09/body); non-toxic animal-contact materials; battery-ingestion warning labeling; device-absent socket entrapment assessment.
- **Assembly-mass sensitivity:**  CCF-L fuse floor derivation assumes ≤26 g assembly; revise floor to 30 N if >26 g (conflict I-2 / DVT gate).

## 7. Intended Use vs NOT-Intended Use

- **Intended:**  behavioral wellness insight (activity/rest/scratch trends), home/away awareness, GNSS behavioral-context enrichment (Max), vet conversation support.
- **NOT intended (hard boundary):**  medical diagnosis, treatment recommendation, disease detection. Labeling/marketing SHALL NOT make diagnostic claims (§13.6). Any future diagnostic-claim feature → regulatory classification review first.

## 8. Expected Lifetime & Volume (USER-CONFIRMED inputs — S-luucipet)

- **Expected service lifetime:**  ~2–3 years. Use 2-year floor where a single testable figure is needed; note 2–3 yr window. *(Resolved by user; feeds durability/endurance/reliability + IP67-lifetime + battery cycle-life requirements.)*
- **Target volume:**  ~5,000 pcs first batch. Low-volume → informs sampling-plan / AQL-style verification framing and manufacturability requirements. *(Resolved by user.)*

## 9. Regulatory-Agent-Facing Facet Table

| Facet                     | Details for standards mapping                                                                                                                               |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Radio / BLE               | BLE 5.x 2.4 GHz intentional radiator; TX ≥+8 dBm; markets US/EU/UK/CA/AU-NZ; Bluetooth SIG QDID                                                             |
| GNSS (Max)                | Passive receive-only; intentional-radiator exemption to CONFIRM per market                                                                                  |
| Wi-Fi (base)              | 2.4 GHz 802.11 b/g/n; FCC Part 15C + RED                                                                                                                    |
| Battery / Li-Po           | UN 38.3; IEC 62133-2:2017 (EU); UL 1642/2054 (US); EU Battery Reg 2023/1542                                                                                 |
| RF exposure               | Wearable proximity + base station — SAR/RF-exposure assessment per market (to confirm)                                                                      |
| Animal safety / breakaway | EU GPSR 2023/988 Art 6(1); UK GPSR 2005; US CPSA; ASTM F2727-17 (feline breakaway); canine-guidance citation GAP (CCF-M/L ceilings) → Regulatory to resolve |
| Materials                 | REACH (EC)1907/2006; RoHS 2011/65/EU + 2015/863; California Prop 65; no chrome/nickel                                                                       |
| Ingress / IP67            | IEC 60529 (device standalone, no CCF)                                                                                                                       |
| Environmental temp        | IEC 60068-2-1/-2-2; damp heat -2-78; shock/vib -2-27/-2-64; UV -2-5; dust -2-68                                                                             |
| Electrical (base)         | EN 62368-1:2020 / UL 62368-1                                                                                                                                |
| Privacy / cyber           | GDPR; UK GDPR+DPA 2018; CCPA/CPRA; PIPEDA; ETSI EN 303 645 V3.1.3; RED Delegated Act 2022/30; EU CRA 2024/2847; UK PSTI 2022; FCC Cyber Trust Mark          |
| Environmental compliance  | WEEE 2012/19/EU; EU PPWR / UK packaging                                                                                                                     |
| Medical boundary          | General wellness for animals — NOT medical device (§13.6)                                                                                                   |

---

*Conductor-authored (shared-store visibility guarantee). Confirmed user inputs folded in: lifetime 2–3 yr, volume ~5,000.*
