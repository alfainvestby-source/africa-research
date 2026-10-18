---
slug: rosewood-park
external_id: DISC-NBO-030
wave: hauzisha-c-2026-10-17
pilot: false
sources_evaluated: 14
sources_retained: 9
inventory_class: off_plan
last_verified_at: 2026-10-17
---

# Rosewood Park (DISC-NBO-030) — discovery research

**Not in seed CSV / not already dossiered.** Hauzisha Slice C ([hauzisha-slice-c.md](../discovery/hauzisha-slice-c.md)). **Rose Avenue**, Kilimani, Nairobi — **Whitehorse Real Estate** (ex-**AAD Real Estate**); Hauzisha **Coming soon** → `off_plan` lead; developer blogs + agents also claim **ready-to-move-in / Complete** with active rentals — **status conflict** (§1 / §7).

Live research accessed **2026-10-17**. **Block.ke ignored as authority**. **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never AAD / Whitehorse.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Hauzisha **Coming soon** → treat as **`off_plan`** for this wave (portal rule); do **not** invent Ready from agent “Complete” alone — but surface Ready lean + rentals as conflict.
- **≠** AYA Luxury Residence; **≠** Grand Premier; **≠** Ambra Heights — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Rosewood Park** (also Rosewood Park Apartments; Rosewood Apartments) | 5 / 4 | whitehorserealestate.ke; Hauzisha; Milligan; CPK; Capital Click |
| `aliases` | secondary | Rosewood; Rosewood Apartments Kilimani; Rosewood Avenue (street misspell on some cards) | 3 | Brilliant; CPK; Capital Click |
| `inventory_class` | **claim conflict** — wave lead **`off_plan`** | Hauzisha directory **Coming soon** → map **`off_plan`**. Soft Ready lean: AAD/Whitehorse blogs **“ready-to-move-in”**; CPK feature **Complete**; multi-agent **for rent** (A-list **150k**/mo). Whitehorse home does **not** say “handed over” (unlike Ambra). **`needs_developer_input`** before promoting to `ready` | 3 / 2 | Hauzisha Coming soon vs AAD/Whitehorse blogs vs CPK Complete vs A-list rent |
| `status` | secondary — conflict | Portal: Coming soon / no units listed. Developer narrative: ready-to-move-in (indexed **2023–2024** blogs). Agents: active sale + rent. **Not** Ready-skipped this pass (no portal Ready tag) | 3 / 2 | Hauzisha; AAD/Whitehorse blogs; CPK; Capital Click; A-list |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** | **Kilimani** (not Kileleshwa / Lavington — those are sibling schemes) | 5 | Whitehorse; Milligan; CPK; Capital Click; Hauzisha Plus Code area |
| `geography.street` | **CANONICAL** soft | **Rose Avenue** (opp. Waridi Hotel on Capital Click; near Yaya / Argwings Kodhek / Ngong Rd corridor) | 5 / 4 | Milligan; CPK; Capital Click; Whitehorse Kilimani narrative |
| `geography.lat_lng` | soft Plus Code | Hauzisha **PQ3W+R6P** — approximate; geo agent later | 2 | Hauzisha |
| `primary_developer_id` | **CANONICAL** soft (trading) | → `dev-whitehorse-real-estate` (**ex-AAD Real Estate**) | 5 | whitehorserealestate.ke portfolio; aad.ke rebrand; Hauzisha AAD; AAD LinkedIn |
| `unit_types` | **CANONICAL** soft | **3 Bedroom all-en-suite + DSQ** (six layout types A–F on Milligan / Capital Click) | 5 / 4 | Whitehorse; Hauzisha; Milligan; CPK; Capital Click |
| `size_by_type` | claim set | See size table — **~194–230 sqm** typed; CPK **203 sqm**; Milligan hero **2,476 ft²** | 4 / 3 | Milligan; CPK |
| `total_units` | secondary | **70** units (one tower) — Capital Click + Brilliant | 3 | Capital Click; Brilliant — **`needs_verification`** vs LOO |
| `building_specs` | secondary | Capital Click: **1** tower; **140** parking (+ visitor); **4** high-speed lifts; six layouts. Amenities cite rooftop heated pool | 3 | Capital Click; Whitehorse amenities |
| `price_claims[]` | multi | See **§1a** — official “from **25M**” (blog) vs portfolio chrome **19M** vs agent **18–28.8M** ladder | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan` | unknown this pass | No developer % schedule recovered; Brilliant **20%** figure is **mortgage calculator** only — **ignore**. Cash-discount asks (CPK) ≠ instalment plan. Must-have **not met** | 0 | — |
| `completion_estimate` | unknown / Ready lean | No future completion date on retained sources; Ready-language + rentals imply delivered stock — **`needs_developer_input`** | 1 | — |
| `amenities` | **CANONICAL** soft | Heated / rooftop swimming pool; fitted gym; landscaped gardens; BBQ / entertainment; children’s play; high-speed lifts; solar water heating; borehole; full backup generator; CCTV + 24hr security / electric fence; video intercom; multiple balconies; cable TV / internet ready | 5 / 4 | Whitehorse home; AAD/Whitehorse blogs; Milligan; CPK; Capital Click; A-list |
| `amenities` finishes | secondary | Turkish / world-class finishes; fully fitted / closed American kitchen; all-en-suite; visitor cloakroom (Milligan); smart home (Milligan) | 3–4 | Brilliant; Capital Click; Milligan; Whitehorse |
| `roi_claim` | secondary marketing | Capital Click / AAD LinkedIn “projected returns” / high rental demand — uncorroborated % | 2 | Capital Click; AAD LinkedIn — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Kilimani Rose Avenue scheme | — | — |

### Size table (retained)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| Milligan Type A | **202 sqm** | Typed sale card | 3 |
| Milligan Type B | **206 sqm** | Typed | 3 |
| Milligan Type C | **196 sqm** | Typed | 3 |
| Milligan Type D | **204 sqm** | Typed | 3 |
| Milligan Type E | **230 sqm** | Typed | 3 |
| Milligan Type F | **194 sqm** | Typed | 3 |
| CPK 3BR+DSQ | **203 sqm** | Agent card | 3 |
| Milligan hero | **2,476 ft²** (~230 sqm) | Listing header — aligns Type E band | 3 |
| Capital Click | six unique layouts (sizes not published on retained snippet) | Spec narrative only | 2 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

No live Whitehorse typed price PDF recovered this pass. Homepage “**Starting from Ksh 19M**” is **portfolio chrome** (same banner as AYA wave) — keep secondary, not Rosewood-only proven. Developer blog floor **25M** vs agent cash discounts **18–18.5M** and Milligan typed **21.5–28.8M**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 25M** (3BR + DSQ) | Developer blog “starting from a competitive price of **25 M KSH**” | aad.ke/kilimani-apartments-for-rent (indexed; live **404**); whitehorserealestate.ke/kilimani-apartments-for-rent (indexed **2024-04-19**) | 4 | Official “from” — Ready-to-move-in framing |
| B | Whitehorse site chrome “Starting from **Ksh 19M**” | Homepage (not Rosewood-only proven) | whitehorserealestate.ke | 2 | Portfolio-level — **`needs_verification`** |
| C | Typed: Type A **202 sqm 24.0M**; B **206 / 28.8M**; C **196 / 24.9M**; D **204 / 27.0M**; E **230 / 26.8M**; F **194 / 21.5M**; hero **24M** | Full typed ladder | Milligan Valuers | 3 | Densest typed sheet |
| D | 3BR+DSQ **203 sqm Kes 25M** (discounted to **18M** cash); card hero **19M** | Sale + cash discount | CPK Real Estate | 3 | Aligns A on list; cash floor below A |
| E | **KES 18.5M** ask; **70** units; Hot Offer | Agent sale card | Capital Click Properties | 3 | Near CPK cash floor |
| F | **KES 23M**; **70** units; Rose Avenue | Agent card (updated **2025-08-31**) | Brilliant Elite Homes | 3 | Mid ladder |
| G | Hauzisha: no price / no units listed; Coming soon | Portal | Hauzisha | ≤2 | Aggregator; **ignore 0730** |
| H | Rent **KES 150,000**/mo 3BR (A-list; Azipa indexed) | Rental market evidence | A-list; Azipa | 2 | Occupancy / Ready lean — not sale authority |

**Portal scalar:** none. Prefer resolving live LOO against developer blog **25M** vs Milligan typed **21.5–28.8M** vs cash **18–18.5M** asks.

### 1b. Payment plan — must-have **not met**

No instalment schedule on Whitehorse home, AAD/Whitehorse Rosewood blogs, or ≥4 agents this pass.

| Element | Source | Status |
|---------|--------|--------|
| Official Whitehorse / AAD % schedule | — | **Not published** this pass |
| CPK cash discount (**25M → 18M**) | CPK | Pricing tactic — **not** a staged plan |
| Brilliant Homes mortgage calculator **20%** down / 20yr / 12% | Brilliant | **Illustrative finance calc** — ignore as developer plan |
| Hauzisha FAQ “staged across the build… terms vary” | Hauzisha | Portal boilerplate only |

**Must-have met?** **No** — need developer schedule **or** ≥4 independent agents agreeing on a structure.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-whitehorse-real-estate` (trading); legacy face `dev-aad-real-estate` |
| `legal_name` | **Unknown** this pass (Companies Registry string not recovered; **do not invent SPV**) |
| `trading_names` | **Whitehorse Real Estate** (current); **AAD Real Estate** (pre-rebrand / Hauzisha still labels AAD) |
| `website` | https://whitehorserealestate.ke/ · rebrand bridge https://aad.ke/ |
| `evidence` | aad.ke “We have Evolved — AAD is now Whitehorse”; Whitehorse home lists **ROSEWOOD PARK** in portfolio (Kilimani 3BR narrative); Hauzisha developer directory still **AAD**; AAD LinkedIn showhouse posts **2023**; Kilimani blog under both AAD and Whitehorse brands |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts (**live**) | **Jahazi Building, James Gichuru Road, 3rd Floor, Lavington, Nairobi**; **+254 704 191919** (same as **0704 191 919**); **info@whitehorserealestate.ke** |
| `legacy contacts` | Indexed AAD blog / LinkedIn: **sales@aad.ke**; **0704 191 919** / **+254 704 19 19 19**. Prefer Whitehorse emails post-rebrand |
| `confidence` | **5** Whitehorse trading face / **0** legal SPV |

**Never** assign **0730 731 355 / +254 730 731 355** to AAD or Whitehorse — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.** AAD → Whitehorse is a **rebrand / renewed identity**, not a proven parent/subsidiary graph this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| AAD Real Estate | prior trading name / rebrand predecessor | aad.ke homepage; Hauzisha directory; LinkedIn; Kilimani blog | 5 as prior face |
| AYA Luxury Residence / Ambra Heights / Grand Premier (/ Haven Villas) | sibling Whitehorse / AAD portfolio only | whitehorserealestate.ke; Hauzisha AAD cards | 4 as siblings — **≠** this property |
| Milligan / CPK / Capital Click / Brilliant / A-list / Azipa | selling / letting agents | Independent listing pages | 3 |
| CPK “Somali developer” tag | unverified ethnicity/origin label | CPK feature chip only | 1 — **ignore** as identity; **`needs_verification`** if ever used |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Milligan Valuers | Densest typed size/price ladder **194–230 sqm / 21.5–28.8M**; Rose Avenue |
| CPK Real Estate | **25M** list / **18M** cash; **Complete** tag; **203 sqm**; modified **2026-03-18** |
| Capital Click Properties | **18.5M**; **70** units; **140** parking; **4** lifts; six layouts; opp. Waridi |
| Brilliant Elite Homes | **23M**; **70** units; Turkish finishes (updated **2025-08**) |
| A-list Real Estate | Rent **150k**/mo; “newly built” — Ready lean |
| Azipa Real Estate | Rent **150k** echo (indexed) |
| Hauzisha | AAD attribution; Coming soon; **3BR+DSQ**; no stock — portal only |
| AAD LinkedIn | 2023 showhouse / ROI marketing — social secondary |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://whitehorserealestate.ke/ | Whitehorse Real Estate | developer | **ROSEWOOD PARK** Kilimani 3BR all-en-suite narrative; amenities; contacts **+254 704 191919**; **info@whitehorserealestate.ke**; portfolio chrome from **19M** |
| 2 | https://aad.ke/ | AAD → Whitehorse | developer | Live rebrand bridge; **+254 704 191919**; Jahazi / James Gichuru |
| 3 | https://aad.ke/kilimani-apartments-for-rent/ | AAD Real Estate | developer (blog) | Indexed **2023-12-01**; **ready-to-move-in**; from **25M**; amenities; **sales@aad.ke**; **0704191919**. Live fetch **404** this pass — retained via indexed developer text |
| 4 | https://whitehorserealestate.ke/kilimani-apartments-for-rent/ | Whitehorse | developer (blog) | Same Rosewood narrative under Whitehorse (**2024-04-19** indexed); from **25M**; ready-to-move-in |
| 5 | https://hauzisha.co.ke/developments/rosewood-park/ | Hauzisha | portal | AAD; **Coming soon**; **3BR+DSQ**; Plus Code **PQ3W+R6P**; ready-to-move-in body copy vs Coming soon tag — conf ≤2; **ignore 0730** |
| 6 | https://milliganvaluers.com/rosewood-park-apartments/ | Milligan Valuers | agent | Typed Types A–F sizes + prices; Rose Avenue; amenities |
| 7 | https://commercialpropertykenya.com/properties/rosewood-park-apartments-3-bedskilimani/ | CPK | agent | **25M / 18M cash**; **203 sqm**; **Complete**; published **2021-12**, modified **2026-03** |
| 8 | https://capitalclick.co.ke/property/rosewood-apartments-kilimani-luxury-3-bedroom-sq-for-sale-rose-avenue/ | Capital Click | agent | **18.5M**; **70** units; **140** parking; **4** lifts; six layouts; opp. Waridi (live fetch **403** — retained via search-indexed full card) |
| 9 | https://a-listrealestate.ke/property/rosewood-park/ | A-list | agent (rent) | **150k**/mo; newly built; amenities corroboration |

### Evaluated / thin skips

| URL / lead | Why skipped or thinned |
|------------|------------------------|
| https://whitehorserealestate.ke/projects/ | Search-indexed projects hub lists Rosewood; live fetch **404** this pass — thin name-only |
| https://brilliantelitehomes.com/properties/rosewood/ | Useful **70** units / **23M** — live **404**; overlap Capital Click density |
| https://hauzisha.co.ke/developers/aad-real-estate/ | AAD directory + Ambra/Grand Premier Coming soon — sibling anti-merge |
| https://aziparealestate.co.ke/property/rosewood-park-kilimani-nairobi/ | Rent **150k** echo of A-list — thin duplicate |
| https://www.buyrentkenya.com/listings/furnished-3-bedroom-apartment-for-rent-kilimani-3820076 | Indexed rent **230k/160k**; live listing gone this pass |
| AAD LinkedIn (linkedin.com/company/aadkenya) | 2023 showhouse / ROI posts — social secondary |
| Knight Frank Rosewood Park to-let | Thin rent amenity echo |
| block.ke (if any) | Low-trust — discovery only |

**sources_evaluated ~14 · sources_retained 9**

---

## 7. Open questions

1. **Inventory class lock** — Hauzisha **Coming soon** (`off_plan`) vs developer **ready-to-move-in** + CPK **Complete** + active rentals. Confirm with Whitehorse whether remaining stock is developer leftover **ready**, **resale**, or still marketed off-plan. **`needs_developer_input`**.  
2. Confirm **current** typed price list vs blog **25M**, Milligan **21.5–28.8M**, cash **18–18.5M**, portfolio chrome **19M**.  
3. Obtain **official payment schedule** (LOO) — none locked this pass.  
4. **Legal contracting entity / SPV** — Whitehorse vs legacy AAD. **`needs_developer_input`** — do **not** invent.  
5. Corroborate **70** units / **140** parking / **4** lifts (Capital Click + Brilliant).  
6. Exact plot / GPS on Rose Avenue (beyond Hauzisha **PQ3W+R6P**).  
7. Whether **sales@aad.ke** remains monitored vs **info@whitehorserealestate.ke** only.

---

## 8. Anti-merge

- **≠ AYA Luxury Residence** (DISC-NBO-023) — Kileleshwa Othaya × Makueni; mixed studios–sky villas; **≠** Kilimani Rose Avenue 3BR+DSQ.  
- **≠ Grand Premier** (Grand Premiere spelling on Whitehorse) — Lavington / Argwings Kodhek sibling Coming soon.  
- **≠ Ambra Heights** — Kileleshwa / Kikambala; Whitehorse says **handed over & occupied**; Hauzisha still Coming soon — sibling only.  
- **≠ Haven Villas** — Whitehorse Lavington triplex product.  
- **≠** other Rose Avenue / Kilimani schemes (do not merge on street name alone).  
- **Not already in corpus** — no prior `rosewood-park` dossier before this wave.
