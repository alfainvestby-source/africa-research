---
slug: alina-valley
external_id: DISC-NBO-025
wave: hauzisha-c-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-17
inventory_class_intent: building
---

# Alina Valley (DISC-NBO-025) — discovery research

**Not in seed CSV.** Hauzisha Slice C ([hauzisha-slice-c.md](../discovery/hauzisha-slice-c.md)). **Likoni Lane**, off **Dennis Pritt Road**, Kilimani, Nairobi — **Wonder Properties**, off-plan sales / under construction (excavation-stage marketing), completion claims **Q2 / May 2027** cluster vs **Q1 2027** vs **Dec 2026** vs **Mar 2028** vs older **2026** sheets (conflict).

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (no dedicated Alina Valley listing recovered this pass; low-trust if appears). **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355** is **Hauzisha only** — **never** Wonder.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — **this** project is **`building` / UC–excavation** (Wonder hub **OFF-PLAN**). **Not** Ready/handed-over.

**≠ Alina Harbour** (may be Ready / Ongoing — **do not merge**); **≠ Alina Ridge**; **≠ Gaia Brookside**; **≠ Diplomat Residencies** — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Alina Valley** | 5 | Wonder hub (“Alina Valley (OFF-PLAN)”); Hauzisha; multi-agent |
| `aliases` | secondary | Alina Valley Apartments; Alina Valley Kilimani | 4 | Westlands Consult; GNA; Vorsa; A-list; Klin |
| `status` | claim set | **Off-plan sales / under construction** — Wonder hub tags **OFF-PLAN**; Westlands “excavation stage”; A-Luxe “OFFPLAN/ONGOING”. **Not** Ready / handed-over | 5 / 4 / 3 | Wonder; Westlands; A-Luxe |
| `inventory_class` intent | research queue | **`building`** (excavation / UC with residual off-plan instalment marketing; Wonder still labels OFF-PLAN on hub). **Not** `ready`. | — | Method lock + Slice C lead |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Wonder; all |
| `geography.neighbourhood` | **CANONICAL** | **Kilimani** | 5 | Wonder framing; Hauzisha; multi-agent |
| `geography.street` | **CANONICAL** soft | **Likoni Lane**, off **Dennis Pritt Road** (Denis Pritt spelling on some portals) | 5 / 4 | Hauzisha; Westlands; GNA; A-list; Vorsa; CPK |
| `geography.landmarks` | secondary | River / city-view marketing; Yaya / Prestige / Junction catchment (agents) | 3 | Westlands; A-Luxe; CPK |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-wonder-properties` (proposed) — **Wonder Properties** / Wonder Properties Kenya | 5 | Wonder hub Alina Valley line + shared Alina Valley phone label; Hauzisha attribution; multi-agent |
| `unit_types` | **CANONICAL** soft | **2 Bedroom**; **2 Bedroom + Study / DSQ**; **3 Bedroom**; **4 Bedroom**; **4 Bedroom + DSQ** | 4 | Wonder “modern apartment” hero thin; dense agent typologies |
| `size_by_type` | claim set — see table | Common band **~100–211 sqm**; densest sheets centre on **100.4 / 102.4 / 112.5 / 119.2 / 127.4 / 131.9–132 / 147–147.5 / 155.7–156 / 174.2–175 / 211** | 3 | Multi-agent; Hauzisha **100.4–174.2** (portal truncates top) |
| `total_units` | unknown this pass | Hauzisha “**15** floor plans” ≠ scheme total; no unit count on Wonder HTML | 0 / 1 | — |
| `building_specs.storeys` | secondary — **conflict** | **15** floors (GNA; Klin; A-Luxe; Own It) vs **17** (Vorsa; CPK) vs Westlands “**15 to 17**” — **`needs_verification`** | ≤3 | Agents |
| `building_specs.basements` | secondary | **3** basement parking levels (GNA; Klin; A-Luxe; Own It) | 3 | Multi-agent |
| `price_claims[]` | multi | See **§1a** — marketing floors **from ~10.7M** vs **11.1M** vs **11.3M**; upper **~21.2–22M** | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan` | secondary — **must-have met** (≥4 agents) | See **§1b** — **20%** deposit + **80%** during construction / ~2 years; Wonder HTML silent → **`needs_verification`** vs LOO | 3 | Westlands; Vorsa; A-list; A-Luxe; CPK |
| `completion_estimate` | claim set — **conflict** | **Q2 / May 2027** cluster vs **Q1 2027** vs **Dec 2026** vs **Mar 2028** vs older **Mar / Q3 2026** — **`needs_developer_input`** (no plaintext completion on Wonder HTML this pass) | ≤3 | See §1c |
| `amenities` | **CANONICAL** soft (agent consensus; Wonder page thin) | Coffee house; kids’ playroom + reading room; gym; family/events room; landscaped Zen garden; swimming pool (heated on some sheets); rooftop football field + recreation; fingerprint locks; CCTV; backup generator; borehole; high-speed lifts; fitted kitchen (hood/cooker/oven); ample parking | 4 / 3 | Multi-agent amenity lists agree; Wonder project detail page not extractable this pass |
| `amenities` extras | secondary | Rubber jogging track (A-list); service charge **KES 12,000**/mo (Vorsa; CPK) — **`needs_verification`** | ≤3 | Agents |
| `roi_claim` | secondary marketing | A-Luxe rent **130–190k** / yield **8–10%** on 3BR — agent only | 2 | A-Luxe — **`needs_verification`** |
| `legal_title` | unknown / weak | Westlands AI snapshot says “Leasehold” — single agent, not on Wonder → **`needs_verification`** | 1 | Westlands |
| `master_planned_community` | none | Standalone Likoni Lane scheme (Wonder “Alina” naming family ≠ same parcel) | — | — |

### Size table (retained claim set)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| 2BR | **100.4 / 102.4 / 112.5 sqm** (some sheets **100–116.4**) | Densest typed entry | 3 |
| 2BR + Study | **119.2 sqm** | Multi-agent (A-list labels +DSQ; GNA/Vorsa “study”) | 3 |
| 2BR + DSQ | **127.4 sqm** | Vorsa; CPK | 3 |
| 3BR | **131.9 / 132 sqm** | Multi-agent | 3 |
| 4BR (no DSQ) | **155.7 / 156 sqm** | Multi-agent | 3 |
| 4BR + DSQ | **147 / 147.5**; **174.2 / 175**; **211 sqm** | Multi-agent | 3 |
| Hauzisha band | **100.4–174.2 sqm** | Portal (omits **211** top) | ≤2 |
| Wonder official sizes | not published in plaintext this pass | Hub name-only for Alina Valley | 0 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

Wonder HTML this pass does **not** publish a typed Alina Valley price list (SPA hub + hero only). Keep agent+portal claim set.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 10.7M** (2BR); 3BR from **13.9M**; 4BR band from **14.8M** up to **~22M** | Compressed + excavation narrative | Westlands Avenue Consult | 3 | Lowest “from” floor this pass |
| B | Hero from **KES 11M**; typed 2BR **11.1–12.8 / 11–12.9M**; study **13.2–13.6M**; 3BR **13.9–14.3M**; 4BR / +DSQ **14.8–21.6M** | Dense typed ranges | GNA Real Estate | 3 | Strong mid-band sheet |
| C | From **KES 11.3M**; 2BR **102.4 → 11.3M**; study **119.2 → 13.2M**; +DSQ **127.4 → 13.5M**; 3BR **132 → 13.9M**; 4BR+DSQ **147 → 14.8M** | Partial typed + **Q2 2027** | Vorsa Group | 3 | Higher 2BR floor than A/B |
| D | From **KES 11.1M**; typed **100.4 → 11.1M**; **102.4 → 11.3M**; **112.5 → 12.4M**; study/+DSQ **119.2 → 13.2M**; 3BR **131.9 → 13.9M**; 4BR+DSQ **147.5 / 174.2 / 211 → 14.8 / 17.5 / 21.2M**; 4BR **155.7 → 15.6M** | Full typed card | A-list Real Estate | 3 | Densest single sheet |
| E | Same shape as D/B mid-band; from **11.3M**; + **155.7 / 174.2 / 211** rows; service charge **12k** | Typed + **Dec 2026** | CPK | 3 | Completion outlier vs Q2 2027 |
| F | 3BR **131.9 from 13.9M**; May / **Q2 2027**; **20%** deposit | Single-typology deep page | A-Luxe Realty | 3 | Aligns 3BR with D |
| G | From **11.1M** / **11M**; typed near B; completion **Q3 2026** | Agent card | Klin Properties | 3 | Stale completion; page also embeds **Alina Harbour** video — do not merge |
| H | From **11.1M**; 2BR **100.4–112.5 → 11.1M**; 3BR **131.9 → 13.9M**; 4BR+DSQ from **14.8M**; completion **Mar 2026** | Compressed | Own It Kenya | 2 | Likely stale date |
| I | Sizes **100.4–174.2**; **Mar 2028**; **no** unit prices listed (“call when released”) | Development hub | Hauzisha | ≤2 | Aggregator; **ignore 0730 phone** |
| J | Wonder hub / inquire UX | Official name + OFF-PLAN + phone label | wonderpropertykenya.com | 5 (identity) / 0 (prices) | No typed list this pass |

**Portal scalar:** none. Do not collapse to a single `price_from` — keep **10.7M / 11.1M / 11.3M** floors as competing claims until Wonder LOO.

### 1b. Payment plan — must-have **met** (≥4 independent agents); structure **not** developer-locked

No instalment schedule on Wonder HTML this pass.

| Element | Source | Status |
|---------|--------|--------|
| **20%** deposit; remaining **80%** over construction / remaining build period | Vorsa; A-list; A-Luxe; CPK | Secondary consensus (conf **3**) |
| **20%** min deposit; balance within **~2 years**; early-bird discount narrative (e.g. 50% deposit → 10% off) | Westlands Consult | Variant schedule + discount — **`needs_verification`** |
| Official Wonder payment schedule | — | **Not published** in plaintext this pass |
| Block.ke | — | No dedicated listing recovered — N/A |

**Must-have met?** **Yes** (agent threshold ≥4) — still flag **`needs_verification`** until developer schedule / LOO.

### 1c. Completion — **conflict** (flag; no silent winner)

| Claim | Sources | Notes |
|-------|---------|-------|
| **Q2 2027** / **May 2027** | Vorsa; A-list; A-Luxe | Current densest marketing cluster |
| **Q1 2027** | GNA | Near cluster |
| **December 2026** | CPK | Earlier than Q2 2027 cluster |
| **March 2028** | Hauzisha | Portal outlier vs agent 2027 cluster |
| **Q3 2026** | Klin | Older sheet |
| **March 2026** | Own It Kenya | Stale / unlikely given excavation framing |
| “**24 months** from launch” | Westlands | Relative; no absolute month |

→ **`needs_developer_input`**: contractual / programme date from Wonder LOO or plaintext project page. Do **not** invent a canonical month.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-wonder-properties` (proposed lead → promote when registry/SPV confirmed) |
| `legal_name` | **Unknown** this pass (trading **Wonder Properties** / **Wonder Properties Kenya**; Companies Registry string not recovered) |
| `trading_names` | Wonder Properties; Wonder Properties Kenya |
| `website` | https://www.wonderpropertykenya.com/ |
| `project_page` | Hub card only this pass — dedicated `/projects/alina*` path returned SPA shell (same as home); no Alina Valley brochure PDF recovered |
| `evidence` | Hub lists **Alina Valley (OFF-PLAN)** alongside Gaia / Diplomat / Harbour / Ridge / Ndemi; footer labels **ALINA VALLEY: +254 116 100 600**; Hauzisha Wonder developer attribution; multi-agent |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts | See **§2a** |
| `confidence` | **5** trading face / **0** legal SPV |

### 2a. Wonder contacts (official site — **not** Hauzisha)

Reuse verified Wonder-site pattern from Gaia / Diplomat dossiers — **never invent**.

| Contact | Value | Provenance | Conf |
|---------|-------|------------|-----:|
| Phone (Alina Valley–labelled + shared Gaia / Harbour lines) | **+254 116 100 600** | Footer / tel labels on wonderpropertykenya.com (“ALINA VALLEY”) | 5 |
| Email | **wonderproperties3@gmail.com** | Site footer + inquire mailto | 5 |
| Address | **Kirichwa Road, Off Argwings Kodhek, Kilimani, Nairobi** | Site contact copy (Gaia dossier harvest; same Wonder host) | 4 |
| Secondary Wonder phones (Diplomat microsite / brochure; not Alina Valley–exclusive) | **+254 116 126 666**; **+254 702 818 888**; **+254 792 696 666**; **+254 701 818 888** | Diplomat dossier — verify if still live for Valley inquiries | 3 |
| Secondary email (Diplomat microsite) | **info@wonderpropertykenya.com** | Diplomat Team block | 3 |
| Social | facebook.com/wonderpropertiesofficial · youtube.com/@wonderpropertieskenya · instagram.com/wonderproperties · linkedin.com/company/wonderpropertieskenya | Site links (Gaia harvest) | 4 |

**Never** assign **0730 731 355 / +254 730 731 355** to Wonder — Hauzisha portal only.

**Portfolio siblings on Wonder hub (do not merge):** Gaia Brookside (OFF-PLAN); Diplomat Residences (OFF-PLAN); **Alina Harbour (Ongoing)**; **Alina Ridge (Sold Out)**; Ndemi Gardens (Sold Out).

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Karim CG Visuals | site/creative partner | “Powered by karimcgvisuals” on Wonder site | 2 |
| Westlands Avenue Consult | selling agent (claims “exclusive” — **`needs_verification`**) | Dense Kilimani listing | 3 / 2 |
| GNA / Vorsa / A-list / A-Luxe / CPK / Klin | selling agents | Independent listing pages | 3 |
| Hauzisha | listing portal | Development page | ≤2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Westlands Avenue Consult | Excavation narrative; from **10.7M**; **20%** / ~2 yr; 15–17 floors |
| GNA Real Estate | Dense typed **11.1–21.6M**; **Q1 2027**; 15 floors / 3 basements |
| Vorsa Group | From **11.3M**; **20%/80%**; **Q2 2027**; 17-storey claim |
| A-list Real Estate | Densest typed sheet from **11.1M**; **20%/80%**; **Q2 2027** |
| CPK | Typed near A-list; **20%**; **Dec 2026**; service charge **12k** |
| A-Luxe Realty | 3BR deep page **13.9M**; May/**Q2 2027**; **20%**; Wonder attribution |
| Klin Properties | Typed mid-band; **Q3 2026**; Harbour video contamination — secondary only |
| Hauzisha | Wonder attribution; **Mar 2028**; sizes **100.4–174.2** — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.wonderpropertykenya.com/ | Wonder Properties | developer | Hub; **Alina Valley (OFF-PLAN)**; phone **+254 116 100 600** (Alina Valley label); email **wonderproperties3@gmail.com** |
| 2 | https://westlands-consult.co.ke/property/apartment/alina-valley-apartments-kilimani-nairobi/ | Westlands Avenue Consult | agent | Excavation; from **10.7M**; Likoni / Dennis Pritt; payment + amenity narrative |
| 3 | https://gna.co.ke/project/alina-valley-apartments-kilimani-2-3-and-4-bedrooms/ | GNA Real Estate | agent | Densest typed ranges; **Q1 2027**; 15 floors / 3 basements |
| 4 | https://vorsagroup.co.ke/property/alina-valley-apartments-2-3-4-bedroom-apartments-in-kilimani/ | Vorsa Group | agent | From **11.3M**; **20%/80%**; **Q2 2027** |
| 5 | https://a-listrealestate.ke/property/alina-valley/ | A-list Real Estate | agent | Full typed price card from **11.1M**; **20%/80%**; **Q2 2027** |
| 6 | https://commercialpropertykenya.com/properties/alina-valley-apartment-for-sale-on-denis-pritt-road/ | CPK | agent | Typed sheet; **Dec 2026**; **20%**; service charge |
| 7 | https://a-luxerealty.ke/properties/3-bedroom-apartment-kilimani-nairobi-ba460176 | A-Luxe Realty | agent | 3BR **13.9M**; Wonder; May/**Q2 2027**; **20%** |
| 8 | https://hauzisha.co.ke/developments/alina-valley/ | Hauzisha | portal | Wonder; Likoni Ln; **Mar 2028**; 100.4–174.2 sqm — conf ≤2; **ignore 0730 phone** |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://klinproperties.co.ke/property/realestate-2-bedroom-apartment-for-sale-in-nairobi/ | Useful typed prices but **Q3 2026** + embeds **Alina Harbour** video — facts folded into §1a/§1c; anti-merge caution |
| https://ownitkenya.com/property/alina-valley-apartments/ | Stale **Mar 2026** completion; compressed prices only |
| https://www.wonderpropertykenya.com/projects/alina | SPA shell — no extractable Alina Valley fields beyond hub |
| https://www.wonderpropertykenya.com/contact | Same SPA shell / footer contacts already retained via hub |
| block.ke Alina Valley | No dedicated listing recovered this pass — discovery N/A |
| Space.ke / GNA Alina Harbour “Ready” / completed tour pages | **≠ this project** — Harbour Ready-leaning sibling only |
| CPK Alina Ridge Kileleshwa Ready card | **≠ this project** — Ridge Sold Out / Ready sibling |
| Wonder YouTube “Alina Valley” shorts | Marketing only; no typed LOO |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. **`needs_developer_input`:** Official **completion** date — resolve **Q2/May 2027** vs **Q1 2027** vs **Dec 2026** vs Hauzisha **Mar 2028** vs older **2026** sheets against LOO / construction programme.  
2. **`needs_verification`:** Official **price list** — retire or keep competing **10.7M / 11.1M / 11.3M** floors.  
3. **`needs_verification`:** Payment — lock agent **20% + 80% during construction** (and Westlands 2-year / early-bird discount variants) vs Wonder LOO.  
4. **`needs_verification`:** Height **15 vs 17** floors; confirm **3** basements.  
5. Legal contracting entity / SPV (Companies Registry); tenure (Westlands “leasehold” alone is weak).  
6. Exact plot / GPS on Likoni Lane; total units / storey plans.  
7. Publish dedicated Wonder project page / brochure (hub-only this pass).  
8. Westlands “exclusive selling agent” claim — corroborate or demote.  
9. Ready-sibling watch: **Alina Harbour** (Ongoing on Wonder; Ready/completed tours elsewhere) — store/skip if researched as Ready; **never merge** into this dossier.

---

## 8. Anti-merge

| Dimension | **Alina Valley** (this dossier, DISC-NBO-025) | **Alina Harbour** (sibling — Ready-leaning) | **Alina Ridge** (sibling) |
|-----------|-----------------------------------------------|---------------------------------------------|---------------------------|
| Wonder hub tag | **OFF-PLAN** | **Ongoing** | **Sold Out** |
| Street / pocket | **Likoni Lane** off Dennis Pritt, Kilimani | **Kirichwa Rd** off Argwings Kodhek, Kilimani | **Oloitoktok / Kileleshwa** corridor |
| Product | **2 / 3 / 4 BR** (+ study/DSQ); from ~**10.7–11.3M** | **2 / 3 BR** (+DSQ); Ready/rent/resale marketing | Studio–3BR Ready / sold-out stock |
| Status this pass | Excavation / UC / off-plan sales | May be **Ready** — dossier **store/skip** if tagged Ready | Sold out / Ready — **not** this scheme |

- **≠ Alina Harbour** — same Wonder developer and overlapping amenity language (rooftop football, Zen garden, coffee house); **different street** (Kirichwa vs Likoni); Harbour **Ongoing/Ready-leaning**. **Do not merge** even when Klin/other pages cross-link Harbour video onto Valley.  
- **≠ Alina Ridge** — Wonder Sold Out; Kileleshwa / Oloitoktok; Ready inventory.  
- **≠ Gaia Brookside (DISC-NBO-021)** — Wonder sibling; **Brookside Gardens Drive**, Westlands; **3/4/5 BR** from ~**23–25.3M**.  
- **≠ Diplomat Residencies (DISC-NBO-022)** — Wonder sibling; **Peponi Road**; **1 & 2 BR** from ~**5M**.  
- **≠ Ndemi Gardens** — Wonder Sold Out Kilimani peer.  
- **≠ Crystal Oak** / other Dennis Pritt or Likoni towers unless LOO proves same parcel.
