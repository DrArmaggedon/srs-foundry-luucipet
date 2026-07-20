> 🔄 Migrated from legacy SRS Foundry format (old session: [S-luuci01]) by SRS Foundry Migrator. Date: 2026-07-20.

**Source:**  LUUCIPet Wellness Monitor PRD v1.3.3 (June 2026), KB doc `docs_KoeGZ63cKfyaE2FX`. Original 15-section numbering preserved so `[PRD §x.x]` tags resolve directly.
**Scope note:**  GPS-M variant and cellular connectivity are OUT OF SCOPE (Phase 2, separate PRD). Mobile App and LUUCI IoT Cloud storage/analytics are OUT OF SCOPE. In-scope: Mini & Max collars (HW+FW), Base Station (Charging & Relay), device-enforced protocol, Portable Travel Charging Cradle, CCF accessory family, IoT Cloud Device-Management layer.

## §1 Product Vision & Overview

Collar-mounted behavioral wellness system for cats and dogs: ultra-light wearable + companion base station; accelerometer classification, BLE, cloud sync. **Wellness positioning — NOT medical diagnosis.**  Attaches to a third-party collar via a **Collar Connection Fixture (CCF)**  accessory; device engages CCF via 3-lug Twist-Lock (bayonet). Strangulation prevention = **Zone 2 Fuse Tab** (scored polymer breakaway, SKU-specific force window). At breakaway, CCF+device release; collar stays on animal. Standard CCF in every box; other CCFs sold separately. Phase 1 = 2 Tier-1 classifiers factory-loaded (Rest/Sleep, Active/Awake); Tier-2 set via OTA post-launch.

- **Mini** ≤10 g, all cats & dogs, BLE-only, ≥90 d typical / ≥180 d Longevity.
- **Max** ≤22 g, large dogs (>20 kg) + service dogs, BLE+full-quality GNSS, ≥45 d @2h fix / ≥90 d @4h fix. 25×25 mm RHCP patch antenna + ≥400 mAh Li-Po. HOME state disables GNSS (power gate).
- Shared: classification engine (species thresholds at onboarding), BLE sync, base-station compat, OTA path, Twist-Lock geometry.

## §2 Problem Statement & Opportunity

Two underserved cohorts: (a) cats/small dogs — weight gap (competitors ≥25 g); (b) large/service dogs — GNSS-vs-battery/classification-depth gap. Competitors: FitBark 2 (10 g, no home/away, shallow classification); Whistle/Fi/Tractive (25–28 g, subscription). Category ~12% CAGR.

## §3 Target Users & Personas

P1 Single-Pet Owner (Mini primary); P2 Multi-Pet Household (mixed Mini/Max); P3 Allergy/Skin-Concern (fine scratch logging); P4 Active-Lifestyle Large-Dog (Max primary, GNSS context); P5 Veterinary Professional (support tool, NOT diagnosis); P6 Service Dog Handler (welfare monitoring).

## §4 Variant Definition Matrix

### §4.1 Collar variants (key values)

- Weight: Mini ≤10 g; Max ≤22 g (PCB+battery+enclosure+Twist-Lock receiver; CCF & collar excluded).
- Motion: 3-axis accelerometer (both). Location: Mini none; Max full-quality GNSS.
- GNSS fix interval (Max): user 30 min–24 h; **factory default 2 h**.
- Connectivity: BLE primary (both). Battery: Mini ≥90 d typ / ≥60 d min / ≥180 d Longevity; Max ≥45 d typ / ≥30 d min @2h, ≥90 d @4h.
- Home/Away: BLE geo-fence via multi-base RSSI; Max disables GNSS when HOME.
- Sync: opportunistic BLE. Base station required (both). IP67 device standalone (CCF excluded). Op temp −20 to +50 °C. Charging pogo-pin magnetic. OTA over BLE via base station.
- Collar attachment: compound CCF; 3-lug Twist-Lock device-to-CCF; Zone 2 Fuse Tab CCF-to-collar breakaway. Mini→CCF-S 15–20 N in-box; Max→CCF-L 28–40 N in-box; CCF-M 20–28 N sold separately.
- **[§4.1 fn ²]**  IP67 tested with NO CCF mated (device standalone only).

**§4.1.1 Max battery-life-vs-fix-interval table:**  HOME≥80% @2h→≥45 d; @4h→≥90 d; @6h→≥120 d; @12h Longevity→≥180 d; mixed(~50%)@2h→≥30 d; AWAY-dominant@2h→≥22 d; 30-min→≥10 d.

### §4.2 Base station variants

- **Base Station (Charging):**  BLE relay + Wi-Fi uplink + single-device pogo-pin charging cradle; 3 LEDs (power/charging/cloud). **Base Station Relay:**  same minus charging cradle; 2 LEDs.
- Both: multi-device BLE (Mini+Max), geo-fence mesh, OTA relay, self-OTA over Wi-Fi, Wi-Fi 2.4 GHz + TLS 1.3, ≥30 d offline buffer, app+QR pairing, AC via USB-C (adapter incl.). Max 8 stations/household; ≥1 charging required.

### §4.3 Common platform: shared classification engine; common BLE protocol/framing; base-station compat; unified OTA (cloud→base→collar/BLE); IP67 device standalone; identical pogo-pin & Twist-Lock geometry across Mini/Max and all CCF variants.

### §4.4 Classifiers

- **Tier-1 (factory):**  Rest/Sleep; Active/Awake.
- **Tier-2 (OTA):**  Walking, Running, Shaking, Scratching, Licking/Grooming, Eating/Drinking, Jumping, Panting ( **dog only**), Head-Shaking.

### §4.5 SKU deployment constraints: ≥1 charging base station (app-enforced); ≤8 stations; species lock at onboarding (re-onboarding supported); GNSS smart power gate (Max, non-configurable); collar-agnostic base station FW; CCF bundling (CCF-S/Mini, CCF-L/Max).

## §5 Use Cases & User Stories

§5.1 daily activity/rest summary; multi-pet compare; ≥30-day trend graph; HOME/AWAY status. §5.2 per-classifier configurable alert thresholds; escape (AWAY) alert; last-seen base station+timestamp. §5.3 up to 8 stations any mix, ≥1 charging. §5.4 shareable multi-week vet summary (export/in-app share). §5.5 Max GNSS behavioral-context enrichment. §5.6 BLE+QR pairing; silent background OTA; ≥30-day local buffer.

## §6 System Architecture Overview

§6.1 Context: Collar ↔(BLE AES-128 CCM)↔ Base Station ↔(Wi-Fi TLS 1.3)↔ Cloud DM(sep PRD) ↔ Cloud Analytics/Storage(OOS); App(OOS). §6.2 CCF stack: neck→collar webbing(3rd-party)→Zone 1 clamp (≥50 N)→Zone 2 Fuse Tab (SKU force)→CCF body (PA66-GF30 UV)→Twist-Lock 3-lug socket→device. §6.3 BLE 5.x peripheral; AES-128 CCM + LE Secure Connections; QR OOB pairing; default adv 60 s. §6.4 dual home/away state machines (device-local + cloud); device-local fallback after >24 h cloud loss governs Max GNSS gate. §6.5 Wi-Fi 2.4 GHz 802.11 b/g/n + TLS 1.3; ≥30-day buffer; chronological upload w/ stale-data flag. §6.6 pogo-pin magnetic charging; 90° CCW to remove device, CCF stays; IP67 when undocked & un-mated. §6.7 security baseline ETSI EN 303 645; link-layer encryption; TLS 1.3; signed OTA + anti-rollback; unique crypto identity at manufacturing.

## §7 Functional Requirements — Behavioral Classification

§7.1 two modes: Wellness (default, power-optimized) + Insight (on-demand continuous 50 Hz). §7.2 unified pipeline, species thresholds at onboarding; **species flag SHALL survive FW updates/power cycles/factory resets** unless user re-onboards; accelerometer ≥50 Hz; NO auxiliary sensors for Tier-1. §7.3 Wellness: motion-triggered, 15-min confirmation bursts, **idle current SHALL NOT exceed 4 µA**; Insight: continuous 50 Hz, auto-revert. §7.4 Tier-1 ≥85% acc / ≤5% FP per class; Tier-2 ≥80% / ≤10%. §7.5 record = label + confidence (0.0–1.0) + UTC ts (≤1 s) + (Max) recent GNSS fix; store ≥30 d without cloud; not discarded on connectivity loss. §7.6 classify/record independent of BLE; forward without corruption/sequence loss. §7.7 on-device normalization; raw accel SHALL NOT leave collar; no cloud round-trip. §7.8 Scratching & Shaking configurable alert thresholds via app; firmware defaults; persist across OTA. §7.9 Tier-2 via OTA — no HW mod / factory reprogram / service event. §7.10 Longevity Mode adjusts BLE adv + sync (+ Max GNSS interval); SHALL NOT reduce classification sampling/accuracy.

## §8 Functional Requirements — Data Sync & Connectivity

§8.1 BLE 5.x peripheral; default adv 60 s (user 1–180 s); adv persists during connections; address randomization; ≥4 concurrent collar sessions per base station. §8.2 AES-128 CCM on all data-bearing links; LE Secure Connections + QR OOB. §8.3 opportunistic sync; summary-delta only; base annotates receipt ts; SHALL NOT semantically interpret payloads. §8.4 retain buffered data until positive ACK; SHALL NOT clear FIFO on disconnect alone. §8.5 report each advertisement (device_id, RSSI, ts, base_station_id) to cloud independent of sync. §8.6 accept cloud downlink (config + OTA images). §8.7 offline: collar classifies/stores independent of BLE; base buffers ≥30 d; chronological upload w/ stale-data flag.

## §9 Functional Requirements — OTA Firmware Updates

§9.1 OTA mandatory all collar variants + base tiers. §9.2 cloud→base over Wi-Fi ( **TLS 1.2 or higher**), staged at base, to collar over BLE AES-128 CCM; **install only when docked in charging cradle; SHALL NOT be bypassable by any remote command**. §9.3 images signed ≥256-bit ECDSA or RSA-2048; verify before commit/execute; anti-rollback via monotonic version counter in secure storage. §9.4 atomic install; dual-bank auto-revert on boot failure; power loss / BLE drop SHALL NOT brick. §9.5 app notifies updates; states Downloading/Verifying/Pending Installation/Installing/Success/Failed; SBOM maintained; Tier-2 models delivered only as embedded OTA components.

## §10 Hardware Requirements

### §10.1.1 Weight/form (Table 10-1): Mini ≤10 g; Max ≤22 g; IP67 device standalone; op −20 to +50 °C; Twist-Lock engage ≤5 N press-in / ≤0.10 N·m rotation; Zone 2 CCF-S 15–20 N, CCF-L 28–40 N; in-box CCF-S(8–19 mm)/Mini, CCF-L(32–50 mm)/Max.

### §10.1.2 Enclosure/materials: IP67 per IEC 60529 incl. exposed pogo-pin & un-mated; **materials in animal-skin contact SHALL be non-toxic & chew-resistant**; LED indicator; underside 3 lug channels (120°, trapezoidal, 8° ramp) + magnetic insert = solid-section, SHALL NOT penetrate wall / seal path; min wall ≥1.5 mm at lug base. **CCF material:**  PA66-GF30 UV; UV stabiliser 0.3–0.5% + hydrolysis stabiliser; Zone 2 integral to moulding — no metallic sub-components in snap/breakaway zones; animal-contact surfaces non-toxic per REACH/RoHS; no chrome/nickel plating.

### §10.1.3 CCF Compound Architecture

- **§10.1.3.1** single moulded part; Zone 1 (structural clamp ≥50 N, NOT breakaway, survives Zone 2 fracture, tool-free install/remove) + Zone 2 (scored polymer fuse tab, SKU force window, single-use, releases CCF+device; collar stays). Twist-Lock = owner-operated charging removal, >100 N axial, inertially immune, NOT breakaway.
- **§10.1.3.2a Twist-Lock spec:**  3-lug bayonet 120°; 90° lock/unlock; trapezoidal 8° ramp self-lock; lug 4.0 mm wide × 1.2 mm thick; one asymmetric lug (7.5 vs 5.0 mm) keying; detent 0.08–0.15 N·m release; axial retention >100 N; inertial immunity (50 g × 22 g = 10.8 N; ≤0.12 N·m vs 0.15 N·m detent = 0.03 N·m margin; DVT TL-05 gate); engage ≤5 N; rotation ≤0.10 N·m; audible+tactile click; magnetic assist ≤5 mm; no tool; IP67 tested device standalone; identical Mini/Max.
- **§10.1.3.2b Zone 2 Fuse Tab:**  weakest link in CCF-to-collar path; fracture before load transfers to neck. Floor = 2× peak inertial load; Ceiling = physiological airway-compromise onset. Windows (26 g assembly basis): CCF-S 25 g accel→6.4 N load→floor 12.8 N / ceiling ≤20 N (feline, ASTM F2727-17) → **15–20 N** (1.33:1); CCF-M 35 g→8.9 N→17.8 N / ≤28 N → **20–28 N** (1.40:1, EU GPSR + canine guidance); CCF-L 50 g→12.75 N→25.5 N / ≤40 N → **28–40 N** (1.43:1). Fuse mechanisms: S scored cantilever (t 0.35–0.40, w 3.0, L 6.0, V-notch 60°, Kt≈3.2); M dual shear-plane (t 0.45–0.50×2, w 3.5, spacing 2.0); L shear-lug post (d_neck 1.0–1.1, notch mid-height, Kt≈3.5, 0.6 mm shroud). Post-fracture: no detached fragment (stub bonded); blunt surfaces; single-use; visible fracture indicator required.
- **§10.1.3.3** CCF variant matrix: width S(8–19)/M(19–32)/L(32–50) + collar-type -RC(round)/-MG(martingale) sold separately; force window set by width SKU; universal Twist-Lock geometry.
- **§10.1.3.4 Zone 1:**  wrap-and-lock ±2 mm; flat & narrow-tubular; no permanent collar mod; ≥50 N axial (DVT retention only); tool-free; NOT breakaway.
- **§10.1.3.5** self-draining socket; magnetic insert ≥90% first-attempt seating ≤5 mm; device-absent socket recessed, no independent entrapment hazard.
- **§10.1.3.6 Post-breakaway protocol:**  retrieve device+CCF; Twist-Lock undamaged; owner SHALL install replacement CCF before re-use; app "CCF Replacement Required" on separation signature; replacement CCFs via retail; **device SHALL NOT be worn without functional CCF w/ intact Zone 2**.
- **§10.1.3.7 DVT plan:**  Module FT (FT-01…FT-09 incl. FT-08 Cpk≥1.33, FT-09 250 N chew); Module TL (TL-01…TL-09 incl. TL-05 shock, TL-09 ≥90% blind seating); Module CS (CS-01…CS-05 system breakaway/retention/chew/Zone1/post-breakaway); IP67 device standalone no-CCF.
- **§10.1.4 Justification:**  single-window snap can't serve cats+large dogs (dog-shake retention floor 25.5 N > cat ceiling ~20 N); compound CCF selected. Regulatory framing EU GPSR 2023/988 Art. 6(1) design-level mitigation. Residual risks incl. owner re-use, CCF-S Cpk, **CCF-L inadvertent fracture if assembled mass >26 g (revise floor to 30 N if >26 g)** , Zone 2 chew, detent margin.

### §10.2 Sensing: §10.2.1 3-axis MEMS accel, ODR ≥50 Hz, wake-on-motion, DMA, FIFO ≥512 bytes. §10.2.2 (Max) GNSS fix 30 min–24 h (default 2 h); A-GPS via BLE sync; power-gated off when HOME; A-GPS ≤72 h w/o cloud; fix timeout 90 s.

### §10.3 Wireless: BLE 5.x; TX ≥+8 dBm; open-air range ≥9 m; peripheral concurrent adv+connection; address randomization; AES-128 CCM.

### §10.4 Battery (Table 10-2): Mini ≥90 typ/≥60 min/≥180 Longevity; Max@2h ≥45/≥30; @4h ≥90/≥65; @12h ≥180/≥130. **Min cell capacity: Mini ≥120 mAh; Max ≥400 mAh.**  Protection: overcharge/over-discharge/short-circuit/over-temp. UN 38.3 before pilot. Low-batt alert ≤20% SoC; ≥10% SoC reserve for OTA.

### §10.5 Charging: 2-contact pogo-pin magnetic (VBUS+GND); full charge ≤2 h; IP67 undocked & un-mated; Twist-Lock workflow (90° CCW off / CW on); self-draining socket.

### §10.6 NV storage: ≥30 d classification summary; retained through power loss without corruption.

### §10.7 Compute: DMA peripheral access; on-device inference w/o cloud; OTA over BLE + signature verify + anti-rollback + dual-bank; secure boot HW root of trust; unique crypto identity at manufacturing; dual-core/coprocessor.

## §11 Base Station Requirements

§11.1 tier comparison (Charging vs Relay per §4.2). §11.2 BLE 5.x central; ≥4 concurrent collar sessions; cloud traffic TLS 1.3. §11.3 transmit collar behavioral + GNSS (Max) + sighting (device_id, RSSI, timestamp, base_station_id). §11.4 ≥30-day buffer; stale-data flag; buffer NOT discarded during self-OTA. §11.5 self-OTA over Wi-Fi w/o user; dual-bank; signed+verified. §11.6 LEDs: Power (solid ON when AC), Charging (charging tier only), Cloud Sync; **LED dimming/nighttime mode SHOULD be implemented**. §11.7 AC-USB-C adapter incl.; continuous operation, no sleep; BLE scan + uplink always on.

## §12 Non-Functional Requirements

### §12.1 Performance (Table 12-1): battery lives (per §10.4); BLE range ≥9 m; classification latency <2 s; base cloud-upload latency <30 s; GNSS TTFF (warm, A-GPS) <60 s; collar boot <3 s; home/away update ≤adv interval + 10 s; CCF Twist-Lock engage ≤5 s.

### §12.2 Reliability: Tier-1 ≥85%/≤5%; Tier-2 ≥80%/≤10%; IP67 full lifetime (device standalone); collar operational ≥99% (excl. charging); base ≥99.5% uptime over 90-day window; OTA success ≥99%.

### §12.3 Security: AES-128 CCM mandatory; TLS 1.3 exclusively cloud-bound; signed OTA + verify; anti-rollback; unique crypto identity; ETSI EN 303 645; public vuln-disclosure policy before launch.

### §12.4 Usability: pairing ≤3 min; charge ≤2 h; CCF install ≤60 s tool-free + Twist-Lock ≤5 s + click; base setup ≤5 min; app battery estimate (Max reflects fix interval + home/away); app warns Max <10 d battery; app CCF selection guidance (flat/round/martingale) + replacement guidance; CCF SKU visually distinguishable (color/moulded designation); app "CCF Replacement Required" on breakaway signature.

### §12.5 Durability: op −20 to +50 °C; storage −30 to +60 °C; IP67 1 m/30 min (device standalone); drop survival 1.5 m hard surface; enclosure non-toxic/chew-resistant/UV-stabilized; CCF UV aging 2,000 h per IEC 60068-2-5; CCF chemical resistance 24 h (pet shampoo pH 5.5–8.5, enzyme cleaners, fresh/salt water); CCF temp cycling −20 to +50 °C (fuse force + detent torque in-window).

### §12.6 Compatibility: 802.11 b/g/n routers default config; app iOS 12+ / Android 6.0+; Mini/Max protocol-compat all base variants; all CCF mechanically compat both devices.

### §12.7 Maintainability: OTA-updatable through supported lifetime; Tier-2 via OTA no HW mod; SBOM per release; public vuln-disclosure by launch.

## §13 Regulatory & Safety Requirements

Attaches to 3rd-party collar via CCF; no collar supplied; strangulation prevention = Zone 2 Fuse Tab (LUUCIPet-controlled).

- **§13.1 Wireless certs (collar):**  US FCC 47 CFR Part 15 Subpart C (BLE intentional) + Subpart B (unintentional); EU RED 2014/53/EU (3.1a,3.1b,3.2); ETSI EN 300 328 v2.2.2; UK Radio Equipment Regs 2017 (UKCA); CA ISED RSS-247 Issue 2 + RSS-Gen Issue 5; AU/NZ AS/NZS 4268:2017 (RCM). Max GNSS passive receive-only — intentional-radiator exemption CONFIRM w/ Regulatory Lead per market. CCF passive — no wireless cert; if sold separately needs independent conformity. Base station: FCC Part 15C + RED for Wi-Fi; Bluetooth SIG QDID for all BLE products.
- **§13.2 Pet safety:**  EU GPSR 2023/988, UK GPSR 2005, US CPSA; material REACH/RoHS/Prop 65 (device + CCF, no chrome/nickel); Zone 2 breakaway CCF-S 15–20 / M 20–28 / L 28–40 N (DVT §10.1.3.7); Zone 1 ≥50 N (not breakaway); CCF single-use post-fracture; chew — Zone 2 no fracture <250 N compressive (FT-09), body resists penetration ≥30 s @250 N; device-absent socket recessed/smooth (entrapment assessed); **battery-ingestion warning mandatory labeling**.
- **§13.3 Battery/electrical:**  UN 38.3 (transport); IEC 62133-2:2017 (EU cell); UL 1642 / UL 2054 (US cell); protection per IEC 62133-2; base station EN 62368-1:2020 / UL 62368-1.
- **§13.4 Env/ingress:**  IP67 device-standalone only (no CCF), documented + confirmed w/ lab; Twist-Lock channels no water path; seal boundary interior. IEC 60529; op temp IEC 60068-2-1/-2-2; damp heat IEC 60068-2-78 (recommended); shock/vib IEC 60068-2-27/-2-64 (recommended).
- **§13.5 Privacy/cyber:**  GDPR 2016/679; UK GDPR + DPA 2018; CCPA/CPRA (if thresholds); PIPEDA; ETSI EN 303 645 V3.1.3; RED Delegated Act (EU) 2022/30 (from 1 Aug 2025); EU CRA 2024/2847 (vuln reporting from 11 Sep 2026, full 11 Dec 2027); UK PSTI Act 2022 (SI 2023/1007); FCC Cyber Trust Mark (voluntary).
- **§13.6 Vet/medical classification:**  general wellness device for animals — NOT medical; labeling/marketing SHALL NOT include diagnostic/treatment/disease-detection claims; post-launch diagnostic-claim features → regulatory classification review first.
- **§13.7 Environmental compliance:**  RoHS 2011/65/EU + (EU) 2015/863; REACH; WEEE 2012/19/EU; EU Battery Regulation 2023/1542/EU; California Prop 65; EU PPWR / UK Producer Responsibility (packaging).

## §14 Out-of-Scope, Assumptions, Roadmap & Glossary

### §14.1 Out of scope (Phase 1): Mobile App; IoT Cloud backend; cellular (Phase 2 GPS-M); edge-AI processor; room-level accuracy; swappable battery; species beyond cats/dogs; GPS-M collar; cloud-side home/away state machine; app device-app ICD; medium-dog BLE-only GNSS.

### §14.2 Key PRD assumptions (author-stated): protocol stable before base FW; cloud DM supports mutual-TLS + ingest endpoint; app supports BLE provisioning + QR OOB; **home Wi-Fi provides reliable 2.4 GHz coverage**; owner has iOS 12+/Android 6+ w/ BLE 4.0+; classifier accuracy validated on representative populations; device-app ICD before base FW; GPS-M OOS; CCF SKU selection via owner measurement + app guidance (in-box appropriate for ≥80% at launch); Standard CCF flat-webbing default; **compound CCF provides design-level strangulation prevention per GPSR Art 6(1) — CONFIRM w/ Regulatory Lead before DVT**; post-breakaway CCF single-use, device/Zone 1 undamaged, replacements via retail.

### §14.3 Roadmap: GPS-M; swappable battery; Ethernet base; multi-device dock; Smart Wellness Dock; room-level accuracy; more species; Veterinary API; edge-AI; CCF-*-RC / CCF-*-MG (Phase 1.1).

### §14.4 Glossary: full glossary retained in source PRD §14.4 (LUUCIPet Wellness Monitor, Mini, Max, GPS-M, CCF, Standard/CCF-S/M/L, CCF-*-RC/-MG, Compound CCF Architecture, Zone 1, Zone 2, Twist-Lock, Single-Use Breakaway CCF, Device Weight Budget, Base Station/Relay, Tier-1/Tier-2, Home/Away Geo-Fencing, BLE Sighting, Device-Enforced Protocol, OTA, Pogo-Pin Magnetic Charging, GNSS Smart Power Gate, Portable Travel Charging Cradle, SBOM, Longevity Mode, HOME/AWAY-dominant).

## §15 Power Budget

§15.1 device-level budget for Mini/Max; battery targets in §10.4/§12.1 derived from & must be consistent with this section. §15.2 standard duty cycle (idle deepest-sleep; ~200 motion events/day @2 s; 15-min confirmation; 60 s adv; ~5 min/day sync; Max 12 fixes/day @2h, 2 min/fix, HOME≥50%). §15.3 L_days = (C_nom × 0.70) / I_avg. **§15.3 Table 15-2 uses illustrative cells: Mini 130 mAh, Max 450 mAh AND Max 400 mAh** (note discrepancy vs §10.4 minimums Mini ≥120 / Max ≥400 → tracked as conflict I-1). §15.4 power-optimisation SHALLs (adaptive adv; minimal sync ≤10 s; interrupt-driven idle; efficient bursts; short confirmation; GNSS abandon 90 s). §15.5 Max GNSS constraints (smart gate primary, non-configurable; app estimates + <10-day warning; A-GPS shortest fix, abandon 90 s; interval change within one cycle). §15.6 validation: DVT programmable load per §15.2; pass ≥80% of §10.4 minimum @25 °C, cells ≥50 cycles.

---

*Normalized by Conductor from full PRD v1.3.3 (Conductor-authored to guarantee shared-store visibility). Downstream agents: read this + PCP; cite `[PRD §x.x]` against these numbers.*
