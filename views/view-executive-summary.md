> **DERIVED VIEW** — Filtered excerpt of Master SRS
> **Source:** SRS-LUUCIPET-001, Revision 1.0, July 2026
> **Master SRS:** `output/SRS-LUUCIPET-FINAL.md`
> **View Generated:** 2026-07-22T21:00:00Z
⚠️ For full context, always refer to the Master SRS.

---

## Executive Summary

The **LUUCIPet Wellness Monitor** is a collar-mounted behavioral wellness system for cats and dogs, comprising the Mini and Max collar devices, Base Station family (Charging and Relay tiers), and Collar Connection Fixture (CCF) accessory family. The system continuously classifies pet behavior on-device, relays data to the LUUCI IoT Cloud via household Base Stations, and supports over-the-air firmware and classifier updates. The product is strictly a general wellness device for animals — it does not perform medical diagnosis.

### Product Variants

| Variant | Weight | Radio | Battery Life | Target |
|---------|--------|-------|-------------|--------|
| Mini | ≤10 g | BLE only | ≥90 days (≥180 Longevity) | All cats and dogs |
| Max | ≤22 g | BLE + GNSS | ≥45 days @2h GNSS | Large dogs (>20 kg), service dogs |
| Base Station (Charging) | — | BLE + Wi-Fi | Mains powered | Household hub + charger |
| Base Station (Relay) | — | BLE + Wi-Fi | Mains powered | Household mesh extender |
| CCF-S | — | — | 15–20 N breakaway | Cats and small dogs |
| CCF-M | — | — | 20–28 N breakaway | Medium dogs |
| CCF-L | — | — | 28–40 N breakaway | Large dogs |

### System Architecture

Each collar communicates with household Base Stations over BLE (AES-128 CCM encrypted, LE Secure Connections). Base Stations relay behavioral data, geo-fencing sighting reports, and OTA firmware to/from the LUUCI IoT Cloud Device-Management layer over Wi-Fi (TLS 1.3). The collar attaches to the pet's own collar via the CCF, which provides Zone 1 structural retention (≥50 N) and Zone 2 strangulation-prevention breakaway (calibrated force windows per SKU). The device engages the CCF through a Twist-Lock interface (>100 N axial retention).

### Key Differentiators

1. **On-Device Behavioral Classification** — Tier-1 classifiers (Rest/Sleep, Active/Awake) factory-loaded; Tier-2 classifiers (Walking, Running, Scratching, etc.) delivered post-launch via OTA. All classification runs on-device with no cloud dependency.

2. **CCF Safety Architecture** — Compound mechanical accessory with single-use Zone 2 Fuse Tab that fractures at calibrated forces to prevent strangulation, while Zone 1 maintains structural integrity.

3. **Secure OTA Updates** — Firmware images signed (256-bit ECDSA/RSA-2048), delivered over TLS 1.3, installed atomically with dual-bank auto-revert. Tier-2 classifiers delivered post-launch without hardware modification.

4. **Multi-Base Household Mesh** — Up to 8 Base Stations per household form a shared geo-fence mesh, independently reporting BLE sightings.

5. **Wellness-Not-Medical** — Strict general wellness device. No diagnostic or disease-detection claims. Any diagnostic-adjacent features require regulatory classification review.

### Deployment

Domestic households with ≥1 Charging-tier Base Station (up to 8 total). Device-local home/away state machine gates GNSS power based on RSSI from paired base stations. Expected service lifetime ~2–3 years (2-year testable floor). Target volume ~5,000 units first batch.

### Standards & Markets

IEEE 830 / ISO/IEC/IEEE 29148. 364 requirements across 18 sections. 31 regulatory instruments mapped across 5 target markets (US, EU/EEA, UK, CA, AU/NZ). 25 documented assumptions.

### Out of Scope (Documented)

- GPS-M variant + cellular (Phase 2)
- LUUCI Mobile App (Mobile App team)
- IoT Cloud data storage/analytics (IoT Cloud backend team)
- Cloud-side home/away state machine (IoT Cloud backend team)
