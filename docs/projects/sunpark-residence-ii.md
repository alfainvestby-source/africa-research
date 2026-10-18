---
slug: sunpark-residence-ii
external_id: DISC-NBO-015
wave: elegant-2026-10-16
pilot: false
sources_evaluated: 14
sources_retained: 9
last_verified_at: 2026-10-16
---

# Sunpark Residence II (DISC-NBO-015) — discovery research

**Elegant Properties wave** ([elegant-properties-verification.md](../discovery/elegant-properties-verification.md)). **Phase II only.** Syokimau / Chady Road corridor, **Elegant Properties**, late under-construction / near-handover cluster (agent completion dates diverge).

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha CTA `0730 731 355` never attributed to Elegant.**

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.

**≠ Sunpark Residence I** (handed over / Ready — context + anti-merge only). **≠** GLBC Gemini Residences / Azure Apex Syokimau / cheap Syokimau 1BR Ready portal ads (§8).

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Sunpark Residence II** | 5 | elegantproperties.co.ke/Sunpark-Residence-II; Featured-Properties |
| `aliases` | secondary | Sunpark Residence Phase II / Phase 2; **Sunpark Residences** (Hauzisha singular — disambiguate to **II**); Sunpark Housing Residence (SIC Prime) | 4 | Hauzisha; Complete Circle; CPK; Craiova; SIC Prime |
| `status` | claim set — **`needs_verification`** on handover date | Official: **active Phase II** with construction-progress gallery through **Feb 2026** (also Nov 2025 / Aug 2025 / “Fitness Fort”). Featured: Phase **I completed and handed over**; II is the live product. Agents: **under construction** / **almost complete** / **Ready for Occupation** / completion **Dec 2025** · **Apr 2026** · **Jun 2026** | 4 / 2 | Elegant II + Featured; Complete Circle; Hauzisha; RealtorKenya; Craiova; GNA |
| `geography.city` | **CANONICAL** | Nairobi metro / **Syokimau** (Machakos side in portals) | 5 | Elegant; Hauzisha; all agents |
| `geography.neighbourhood` | **CANONICAL** | **Syokimau** (behind Gateway Mall) | 5 | Elegant; agents |
| `geography.street` | **CANONICAL** soft | **Chady Road** / **Syokimau Airport Road**, off **Mombasa Road**, behind **Gateway Mall** | 5 | Elegant II + Featured; agents echo Chady |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-elegant-properties` | 5 | Elegant project + About + Featured; Hauzisha attribution |
| `unit_types` | **CANONICAL** soft + agent overlay | Official: **2 Bedroom** & **3 Bedroom**. Agents also list **1 Bedroom**, **2BR + DSQ**, **3BR + DSQ** — **`needs_verification`** (not on Elegant II page this pass) | 5 / 3 | Elegant II + Featured; CPK; Complete Circle; Golden Years; Craiova; GNA |
| `size_by_type` | claim set — see table | Official entry **from 1,150 sqft**. Agent Phase II table: 1BR ~1,108–1,109 sqft / ~103 m²; 2BR ~1,152 / ~107; 2+DSQ ~1,302 / ~121; 3BR ~1,615 / ~150; 3+DSQ ~1,819 / ~169 | 5 / 3 | Featured; agent tables |
| `total_units` (Phase II) | secondary — **`needs_verification`** | SIC Prime: Phase 1 **360** complete; Phase 2 **342** “still available” — **not** on Elegant pages this pass | 2 | SIC Prime only |
| `building_specs` | secondary soft | Elevators per block (agents + Phase I-era Elegant copy); storeys / block count for **II** not stated on retained official pages | 2 | agents; legacy Phase I page (context) |
| `site_acres` | **CANONICAL** vs agent bleed | Official II + Featured: **10 acres**. Agents/Hauzisha often **6.2 acres** (= **Phase I** acreage per Construction Review 2021 + legacy Elegant Sunpark page) → treat 6.2 as **I-bleed**, not official conflict | 5 / 2 | Elegant II; Featured; vs agents |
| `price_claims[]` | multi | See **§1a** — official “from **8M**” vs typed agent ladders | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | Elegant |
| `payment_plan` | agent-only — **must-have not met** | See **§1b** | 2 | CPK; Craiova; Complete Circle (vague) |
| `completion_estimate` | claim set — **`needs_verification`** | Official: **no dated handover** on II / Featured this pass (progress to Feb 2026). Agents: **Dec 2025** (Complete Circle; Craiova; GNA era copy) · **April 2026** (Hauzisha; RealtorKenya) · **June 2026** (expired BRK listing snippet) | 0 / 2 | Elegant silence; agents |
| `amenities` | **CANONICAL** soft | Clubhouse / events hall; **2-level gym** (aerobics + spin); kids’ park; football pitch + tennis court; **semi-Olympic pool** + jacuzzi; sauna; open-plan fitted kitchen & wardrobes | 5 | Elegant II page |
| `amenities` agent denser | secondary | 24/7 security / CCTV; electric fence; borehole(s); backup generator; elevators; visitor parking; on-site shops | 3 | Complete Circle; CPK; Craiova |
| `roi_claim` | unknown / marketing fluff | SIC Prime “compelling ROI” — no figure retained | 0 | skip as claim |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | secondary | Gated multi-block estate on Chady Rd; Phase I adjacent / prior | 3 | Elegant Featured; agents |

### Size table (retained)

| Type | Size | Role | Conf |
|------|------|------|-----:|
| Entry (official) | **From 1,150 sqft** | Featured + II narrative | 5 |
| 1 Bedroom | **~1,108–1,109 sqft / ~103 m²** | Agent Phase II tables only | 3 |
| 2 Bedroom | **~1,150–1,152 sqft / ~107 m²** | Official floor + agents | 4 |
| 2 Bedroom + DSQ | **~1,302 sqft / ~121 m²** | Agents | 3 |
| 3 Bedroom | **~1,550–1,615 sqft / ~144–150 m²** | Agents (SIC also 1,550 / 144) | 3 |
| 3 Bedroom + DSQ | **~1,819 sqft / ~169 m²** | Agents | 3 |

Hauzisha band **72.65–145 sqm** overlaps agent 1–3BR plinths; treat as portal summary (conf 2).

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official “from”:** Elegant II + Featured agree **from KES 8M** (2 & 3BR marketing). Typed per-type ladders are **agent-only** this pass → show + **`needs_verification`**. Do **not** collapse to Hauzisha **6.5–10.5M** or agent “from 6.5M” (Phase I Ready bleed).

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 8M**; from **1,150 sqft**; 2 & 3BR | Developer hub + Featured | elegantproperties.co.ke/Sunpark-Residence-II; Featured-Properties | 5 | Official “from” — no typed ladder |
| B | 2BR **9.0M**; 2BR+DSQ **9.5M**; 3BR **11.5M**; 3BR+DSQ **12.5M** | Agent price list (no 1BR) | Complete Circle | 3 | Aligns mid of C |
| C | 1BR **7.5M** (1,108 / 103 m²); 2BR **9.0M**; 2+DSQ **9.5M**; 3BR **11.5M**; 3+DSQ **12.5M** | Phase II table | CPK; Golden Years (search-retained); Craiova (7.5M ladder page) | 3 | Agent; 1BR not on Elegant II |
| D | 1BR **7.0M**; 2BR **8.5M**; 2+DSQ **9.0M**; 3BR **11.0M**; 3+DSQ **12.0M** | Later / alternate agent ladder | GNA; Craiova “kilimani” Syokimau page | 3 | Softened vs C |
| E | Band **KES 6.5M – 10.5M** | Portal card | Hauzisha “Sunpark Residences” | 2 | Aggregator; **6.5M** likely Phase I Ready bleed |
| F | From **KES 6.5M** | Agent / co-op card | Golden Years header; SIC Prime | 2 | Conflicts with A; Phase I bleed risk |

**Portal scalar:** none. Use **A** as official marketing floor only; resolve typed 1BR/DSQ and 7.0 vs 7.5 / 8.5 vs 9.0 with Elegant sales / LOO before any typed `price_from`.

### 1b. Payment plan — must-have **not met**

No Elegant payment schedule on Sunpark-Residence-II / Featured / About this pass.

| Element | Source | Status |
|---------|--------|--------|
| Phase II: **25%** deposit; remaining **75%** quarterly until occupation | CPK | Agent-only — **`needs_verification`** |
| **25%** deposit; balance by **Dec 2025** | Craiova | Agent-only; date may be stale vs Feb 2026 progress |
| “Construction-linked” / “flexible” / cash & mortgage | Complete Circle; SIC Prime; GNA | Vague — not a schedule |
| Phase I Ready: **30%** + **70%** on occupation | CPK (Phase **I** context) | **Not** this property |

Fewer than **4** independent agents with a concrete schedule → payment must-have **fails**. Flag **`needs_developer_input`**.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-elegant-properties` |
| `legal_name` | **Unknown** this pass (trading **Elegant Properties** / Elegant Properties Kenya; Companies Registry string not recovered) |
| `trading_names` | Elegant Properties; Elegant Properties Kenya |
| `website` | https://www.elegantproperties.co.ke/ |
| `evidence` | Project page + Featured (Phase I handover → II) + portfolio Chady Rd listing + About (“30+ years”; family-run marketing) |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts | **+254 700 004 449**; **info@elegantproperties.co.ke** (official site / About / Featured / II). Brochure-era **+254 731 286 286** noted on Elegant verification pass — secondary. **`0730 731 355` = Hauzisha portal only — never developer.** |
| `confidence` | **5** trading face / **0** legal SPV |

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Hauzisha | portal / discovery | Singular “Sunpark Residences” page; Elegant attribution; own CTA phone | 3 portal / 0 as Elegant sales |
| Safaricom Investment Cooperative (SIC Prime) | marketing / sales channel (unproven SPV) | Project card; unit counts | 2 — **`marketing_partner`** candidate only |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Complete Circle Properties | Phase II prices; Dec 2025; 6.2-acre bleed; amenities echo |
| CPK Real Estate | Phase I Ready vs Phase II tables + payment % |
| Hauzisha | Singular name; from 8M copy + 6.5–10.5M band; Apr 2026 |
| Golden Years Realty | Typed Phase II ladder (page flaky this pass; search-retained) |
| Craiova Realtors | Typed ladder + 25% deposit; Ready / Dec 2025 tags |
| GNA Real Estate | Softened price ladder; Ready marketing |
| RealtorKenya | Elegant-attributed summary (8M / 1,150 sqft / Apr 2026; wrongly 6.2 acres) |
| SIC Prime | 10-acre + Phase 1 **360** / Phase 2 **342** claim |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.elegantproperties.co.ke/Sunpark-Residence-II | Elegant Properties | developer | Primary — location, from 8M, 10 acres, amenities, progress gallery |
| 2 | https://www.elegantproperties.co.ke/Featured-Properties | Elegant | developer | Phase I handed over; II from 1,150 sqft / 8M / 10 acres |
| 3 | https://www.elegantproperties.co.ke/about-us | Elegant | developer | Trading face; **700 004 449**; Sunpark testimonial (phase-agnostic) |
| 4 | https://www.elegantproperties.co.ke/our-portfolio | Elegant | developer | Chady Rd 2 & 3BR portfolio line |
| 5 | https://completecircleproperties.com/sunpark-residence-phase-ii/ | Complete Circle | agent | Typed 2/3 + DSQ prices; Dec 2025; 6.2-acre bleed |
| 6 | https://commercialpropertykenya.com/properties/sunpark-residence-in-syokimau/ | CPK | agent | Phase I vs II split; Phase II payment 25/75 |
| 7 | https://hauzisha.co.ke/developments/sunpark-residences/ | Hauzisha | portal | Singular name → II; Elegant; **ignore 0730 phone** |
| 8 | https://www.realtorkenya.com/properties/sunpark-residence-ii-2-and-3-bedroom-apartments-on-chady-road-syokimau | RealtorKenya | agent / reprint | Elegant-sourced 8M / Apr 2026; acreage bleed |
| 9 | https://www.sicprime.co.ke/buy/sunpark-residence | SIC Prime | agent / channel | 10 acres; 360 / 342 unit claim; from 6.5M bleed |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://www.elegantproperties.co.ke/sunpark-residence-I-gallery | Phase **I** gallery only — status note / anti-merge, not II claims |
| https://www.elegantproperties.co.ke/our-properties/sunpark-residence | Legacy Phase I page (6.2 acres; 2022–2024 progress) — 404 this pass; search snippet used for I-bleed context only |
| https://constructionreviewonline.com/sunpark-residence-development-in-syokimau-machakos-county-kenya/ | Dec 2021 Phase I 6.2-acre article — historical context, not II |
| https://www.goldenyearsrealty.co.ke/property/sunpark-residence-phase-i/ | HTTP 500 this pass — price table retained from search only (not counted in retained ≥5) |
| https://craiovarealtors.com/property/sunpark-residence-phase-2-… | 404 this pass; alternate Syokimau page retained as evaluated agent echo |
| https://gna.co.ke/project/sunpark-residence-syokimau-1-2-3-beds-plus-dsq/ | Overlaps CPK/Craiova ladders; Ready/rent mix — thin secondary |
| BuyRentKenya Syokimau 3783785 | Listing gone; June 2026 snippet only |
| Block.ke / cheap Syokimau 1BR Ready unit ads | Low-trust / wrong inventory class / anti-merge |
| Hauzisha 0730 731 355 | Portal CTA — **not** Elegant |

**sources_evaluated ~14 · sources_retained 9**

---

## 7. Open questions

1. Confirm **completion / handover** date with Elegant (official silent; agents Dec 2025–Jun 2026).  
2. Publish typed **price list** for II (1BR / DSQ inclusion vs official 2 & 3 only).  
3. Recover **payment schedule** from developer (agent 25% only).  
4. Confirm Phase II **total units** (SIC 342) and block/storey count.  
5. Legal contracting entity / SPV for LOO.  
6. Exact plot / GPS on Chady Rd (vs Phase I parcel).  
7. Whether agent **6.2-acre** copy is pure Phase I bleed or a shared-masterplan label.

---

## 8. Anti-merge

- **≠ Sunpark Residence I** — Elegant Featured: **completed and handed over**; Ready inventory / gallery only. Do **not** dossier I; do **not** use I Ready “from 6.5M” / 782 sqft 1BR as II prices.  
- **≠ Hauzisha singular “Sunpark Residences”** as a third scheme — same Elegant product; map to **II** (active), not I.  
- **≠ GLBC Gemini Residences** — also behind Gateway Mall / Mombasa Rd, but **Mwananchi Road**, developer **GLBC Group**, studio–4BR, different scheme.  
- **≠ Azure Apex Syokimau** — Old Mombasa Rd mixed-use / mall scheme; studios from ~3.8M; different developer and timeline.  
- **≠ cheap Syokimau 1BR Ready unit ads** (Five Star, Muthama Rd parks, Luxore, etc.) — corridor noise, not Elegant Sunpark II.  
- **≠** Elegant Westlands products (Forestview, Donyo Hill, 48 Treehouse, Oak & Ivy) — same developer, different sites.
