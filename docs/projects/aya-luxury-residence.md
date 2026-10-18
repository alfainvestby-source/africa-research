---
slug: aya-luxury-residence
external_id: DISC-NBO-023
wave: hauzisha-b-2026-10-17
pilot: false
sources_evaluated: 14
sources_retained: 10
inventory_class: building
last_verified_at: 2026-10-17
---

# AYA Luxury Residence (DISC-NBO-023) — discovery research

**Not in seed CSV / not already dossiered.** Hauzisha Wave B ([hauzisha-wave-b-prep.md](../../internal/hauzisha-wave-b-prep.md)) · Block process-rerun Tier A ([block-2028-process-rerun-batch.md](../discovery/block-2028-process-rerun-batch.md)). **Othaya Road × Makueni Road**, Kileleshwa, Nairobi — launched by **AAD Real Estate**, now trading as **Whitehorse Real Estate**; mixed apartments + duplexes + garden / sky villas; completion **Dec 2028 / Q3 2028** cluster.

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never AAD / Whitehorse.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **Under construction / building** (off-plan sales still open); **not** Ready / handed-over.
- **Sandoral** naming on NRE → **resolve early, do not invent winner** (§2 / §4 / §7).

**≠** Ambra Heights; **≠** Rosewood Park; **≠** Grand Premier (sibling AAD / Whitehorse portfolio — mention only); **≠** Aria Park (Karen / Sandoral) — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **AYA Luxury Residence** (also Aya Luxury Residences / AYA Residence) | 5 / 4 | whitehorserealestate.ke; aad.ke launch (indexed); Hauzisha; GNA; Own It |
| `aliases` | secondary | Aya Residences; AYA Residence; Aya Luxury Residences Kileleshwa | 3 | GNA; NRE; Sir Francis; CPK |
| `inventory_class` | **CANONICAL** | **`building`** — under construction / off-plan sales; **not** Ready. Hauzisha “4 units for sale” = stock count only (do **not** invent Ready) | 5 | NRE UC; Whitehorse UC narrative; Hauzisha Dec 2028; Own It “Off-Plan” |
| `status` | **CANONICAL** soft | **Under construction** with active off-plan marketing; Whitehorse LinkedIn construction update **Oct 2025**; NRE “UC **92%**” unverified | 5 / 2 | Whitehorse; NRE — progress % **`needs_verification`** |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** | **Kileleshwa** | 5 | Whitehorse; Hauzisha; GNA; NRE; Own It |
| `geography.street` | **CANONICAL** soft | Junction of **Othaya Road** and **Makueni Road** (agents also “off Othaya”; CPK also “Makueni × Nyando” — soft conflict) | 5 / 2 | GNA; NRE; Own It; Sir Francis; CPK Nyando — **`needs_verification`** on Nyando |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** soft (trading) + conflict | → `dev-whitehorse-real-estate` (**ex-AAD Real Estate**). **Sandoral Developers** appears on NRE only — **not** adopted as primary; **`needs_developer_input`** on legal SPV | 5 / 1 | aad.ke rebrand; whitehorse portfolio; Hauzisha AAD; NRE Sandoral unverified |
| `unit_types` | **CANONICAL** soft | Mini / studio **1BR**; **2BR**; **3BR + DSQ**; **4BR + DSQ**; **3BR / 4BR duplex + DSQ**; **3BR / 4BR / 6BR duplex garden villas**; **5BR / 6BR duplex sky villas**; **5BR triplex sky villas** (+/− DSQ / BBQ / garden) | 4 | GNA; NRE; Own It; Sir Francis; AAD launch product mix |
| `size_by_type` | claim set | Dense agent matrix **49–740 sqm** (see size table); Hauzisha band **49–262** incomplete vs villa sizes | 4 / 2 | GNA; NRE; Own It; Sir Francis vs Hauzisha |
| `size_measure_tag` | soft | Own It labels **plinth**; peers publish sqm without gross/net tag | 3 | Own It |
| `total_units` | unknown | — | 0 | not found (Hauzisha “4 available” ≠ total stock) |
| `building_specs` | secondary | AAD launch: **~2-acre** site; CPK: **11-storey**; amenities cite **8** high-speed lifts | 4 / 2 / 3 | AAD launch indexed; CPK; GNA/NRE/Hauzisha lifts |
| `price_claims[]` | multi | See **§1a** — no single official typed list on live Whitehorse home this pass | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan` | secondary — must-have **soft-triggered** | See **§1b** — developer **4-year / 0%** (launch + agents); deposit **30%** agent-heavy | 4 / 3 | AAD launch; Sir Francis; GNA; Stacy LinkedIn |
| `completion_estimate` | claim set — **`needs_developer_input`** | **December 2028** vs **Q3 2028** vs NRE **Q1 2026** (reject as stale / conflict) | 3 / 3 / 1 | Hauzisha; Own It; Kenya4u vs GNA vs NRE |
| `amenities` | **CANONICAL** soft | Heated / infinity pool + sunken lounge; gym / fitness; kids’ play; yoga garden; water features; on-site restaurant + supermarket; 8 high-speed lifts (access cards); solar water heating; full backup generator; 24hr security + video intercom / CCTV | 5 / 4 | AAD launch; Whitehorse LinkedIn; GNA; NRE; Own It; Sir Francis |
| `amenities` finishes | secondary | Turkish finishes; smart home; all-ensuite; walk-in closets; his-and-hers basins; double-volume ceilings; private gardens / BBQ on select villas | 3–4 | GNA; NRE; Own It |
| `construction_progress` | secondary | NRE “**92%**”; Whitehorse social “underway / Oct 2025 progress” — no % on developer site | 2 | NRE; Whitehorse LinkedIn — **`needs_verification`** |
| `roi_claim` | secondary marketing | Kenya4u ~**9–11%** + rent bands; NRE demand copy — uncorroborated | 2 | Kenya4u; NRE — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Kileleshwa scheme | — | — |

### Size table (retained — agent consensus matrix)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| Mini 1BR / studio | **49 sqm** | GNA; NRE; Own It; Sir Francis | 4 |
| 2BR | **125 sqm** | GNA; NRE; Own It; Sir Francis | 4 |
| 3BR + DSQ | **208 sqm** | GNA; NRE; Own It; Sir Francis | 4 |
| 4BR + DSQ | **262 sqm** | GNA; NRE; Own It; Sir Francis | 4 |
| 3BR duplex + DSQ | **221 / 265 / 280 sqm** | GNA; NRE; Own It | 4 |
| 4BR duplex + DSQ | **400 sqm** | GNA; NRE; Own It | 4 |
| 3BR duplex garden villa | **255 / 347 sqm** | GNA; NRE; Own It | 4 |
| 4BR duplex garden villa | **609 sqm** | GNA; NRE; Own It | 4 |
| 6BR duplex garden villa | **740 sqm** | GNA; NRE; Own It; Sir Francis | 4 |
| 5BR duplex sky villa + DSQ + BBQ + garden | **488 sqm** | GNA; NRE; Own It | 4 |
| 6BR duplex sky villa + DSQ + BBQ + garden | **503 sqm** | GNA; NRE; Own It | 4 |
| 5BR triplex sky villa (+/− DSQ / BBQ / garden) | **360 / 418 / 580 sqm** | GNA; NRE; Own It | 4 |
| Hauzisha size band | **49–262 sqm** | Portal incomplete vs villa matrix | ≤2 |
| CPK 3BR+DSQ card | **180 m²** | Older thin sheet — conflicts with **208** | 2 — **`needs_verification`** |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

No live Whitehorse typed price PDF recovered this pass. Homepage “**Starting from Ksh 19M**” is portfolio chrome (may span projects) — keep secondary. Dense GNA / NRE / Own It / Sir Francis matrices align on an **~8.5–98M** ladder; Finlay / CPK / Whitehorse social floors diverge → multi-claim only.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Typed ladder: Mini **1BR 49 sqm from 8.5M**; **2BR 125 from 16.5M**; **3BR+DSQ 208 from 27M**; **4BR+DSQ 262 from 34M**; duplexes **29–53M**; garden villas **33–98M**; sky / triplex **48–77M** | Full matrix | GNA; NRE (body) | 3 | Strong agent consensus shape |
| B | Same ladder shape; Own It studio card **10M** (vs **8.5M** peers); 2BR **16M** (vs **16.5M**) | Typed + Dec 2028 | Own It Kenya | 3 | Soft floor conflict vs A |
| C | From **8.5M**; condensed typed echoing A; payment **30% / 48 mo 0%** | Agent card (updated 2026-10-01) | Sir Francis Homes | 3 | Aligns A |
| D | Whitehorse LinkedIn “Starting from **Kes 7.5M**” | Developer social | Whitehorse Real Estate LinkedIn | 4 | Official “from” floor — below A |
| E | Hauzisha band **KES 7M – 28M**; unit cards from **7M** | Portal | Hauzisha | ≤2 | Aggregator; incomplete vs villa highs |
| F | Finlay typed floors **~6.5 / 13 / 21 / … / 70M** (hero band **13–65M**) | Older / negotiable sheet | Finlay Real Estate | 2 | Well below A — likely stale — **`needs_verification`** |
| G | CPK: **2BR 21M**; **3BR+DSQ 36M**; duplex **43M**; **4BR+DSQ 34M**; **6BR duplex 100M** | Older thin sheet; Makueni/Nyando | CPK | 2 | Conflicts A; location Nyando anomaly |
| H | NRE hero “From **KES 27M**” vs body ladder from **8.5M** | Internal NRE conflict | NRE | 2 | Hero vs table — **`needs_verification`** |
| I | Whitehorse site chrome “Starting from **Ksh 19M**” | Homepage (not AYA-only proven) | whitehorserealestate.ke | 2 | Portfolio-level — **`needs_verification`** |
| J | Block.ke unit ads (studio–4BR) | Discovery seed only | block.ke | ≤1 | **Not authority** |

**Portal scalar:** none. Prefer resolving live LOO against Whitehorse **7.5M** social floor vs agent **8.5M** ladder; retire Finlay/CPK sheets if LOO confirms A.

### 1b. Payment plan — must-have **soft-met** (developer + multi-agent; deposit % still soft)

| Element | Source | Status |
|---------|--------|--------|
| **4-year payment plan at 0% interest** | AAD Sankara launch (indexed 2024); Sir Francis **48 months / zero interest**; Stacy Moraa LinkedIn (Whitehorse-branded pitch) | Soft developer + agent echo — conf **4** structure |
| **30%** deposit; balance over remaining construction / up to **48 months** | Sir Francis; GNA; CPK (“30% deposit and balance on occupation”) | Agent consensus on **30%** (conf **3**) — launch text did **not** publish deposit % this pass |
| Cash / 1- / 2- / 3-year plan options + 4-year 0% | Stacy Moraa LinkedIn | Secondary — **`needs_verification`** vs LOO |
| NRE calculator **20%** deposit + 24-month remainder | NRE | **Illustrative** (“Estimates only… confirm… developer”) — **ignore** as published plan |
| Hauzisha “staged across the build… terms vary” | Hauzisha FAQ | Portal boilerplate |
| Live Whitehorse / AAD page with full % schedule | — | **Not recovered** this pass (launch URL **404**/captcha; Whitehorse home silent on %) |

**Must-have met?** **Soft yes** — developer-indexed **4-year / 0%** + ≥3 agents on **30% / ≤48 mo**. Flag **`needs_verification`** for exact deposit % and whether “balance on occupation” (CPK) is still current vs construction-period instalments.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-whitehorse-real-estate` (trading); legacy face `dev-aad-real-estate` |
| `legal_name` | **Unknown** this pass (Companies Registry string not recovered; **do not invent SPV**) |
| `trading_names` | **Whitehorse Real Estate** (current); **AAD Real Estate** (pre-rebrand / Hauzisha still labels AAD) |
| `website` | https://whitehorserealestate.ke/ · rebrand bridge https://aad.ke/ |
| `evidence` | aad.ke “We have Evolved — AAD is now Whitehorse”; Whitehorse home lists **AYA** first in portfolio; Hauzisha developer directory still **AAD**; Sankara launch coverage (AAD, Aug 2024 — URL **404**/captcha this pass, still indexed); Kenya4u names White Horse + sibling projects |
| `group_company_id` | **null** — none invented |
| `sandoral_conflict` | NRE labels developer **Sandoral Developers** with status **“Not yet independently confirmed”** (reviewed 4 Oct 2026). NRE Sandoral profile: Aria Park (Karen) has official Sandoral evidence; **AYA association explicitly buyer-verification required**. **No winner invented** → keep Whitehorse/AAD as marketing/trading primary; Sandoral as **unverified RelatedParty** + **`needs_developer_input`** |
| `sales_office` / contacts (**live**) | **Jahazi Building, James Gichuru Road, 3rd Floor, Lavington, Nairobi**; **+254 704 191919** (same as **0704 191 919**); **info@whitehorserealestate.ke**; Whitehorse LinkedIn sales pitch also **sales@whitehorserealestate.ke** |
| `legacy contacts` | Indexed AAD launch / contact: **sales@aad.ke**; **0704 191 919** / **+254 704 19 19 19**. Live aad.ke/contact fetch returned **theme placeholder** junk (tyler.com) this pass — treat sales@aad.ke as **legacy lead**, prefer Whitehorse emails |
| `confidence` | **5** Whitehorse trading face / **0** legal SPV / **1** Sandoral |

**Never** assign **0730 731 355 / +254 730 731 355** to AAD or Whitehorse — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.** AAD → Whitehorse is a **rebrand / renewed identity**, not a proven parent/subsidiary graph this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| AAD Real Estate | prior trading name / rebrand predecessor | aad.ke homepage; Hauzisha directory; Sankara launch | 5 as prior face |
| Sandoral Developers | **unverified** developer attribution | NRE project + Sandoral profile (“not independently confirmed”; Aria Park ≠ proof for AYA) | 1 — **`needs_developer_input`** |
| Ambra Heights / Rosewood Park / Grand Premier (/ Haven Villas) | sibling Whitehorse / AAD portfolio only | whitehorserealestate.ke; Hauzisha AAD Coming soon cards | 4 as siblings — **≠** this property |
| GNA / NRE / Own It / Sir Francis / Finlay / CPK / Kenya4u | selling agents / portals | Independent listing pages | 3 |
| Stacy Moraa (LinkedIn) | agent pitch under Whitehorse branding | LinkedIn post | 2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| GNA Real Estate | Densest typed ladder **8.5–98M**; **Q3 2028**; **30%** deposit + construction-period balance |
| NRE Real Estate | Same ladder; UC; Sandoral label; hero **27M** vs body **8.5M**; completion **Q1 2026** conflict; **20%** calculator illustrative |
| Own It Kenya | Typed ladder + **Dec 2028**; Off-Plan framing; soft price floor differences |
| Sir Francis Homes | From **8.5M**; **30% / 48 mo 0%**; Othaya Rd; updated **2026-10-01** |
| Finlay Real Estate | Lower typed sheet **~6.5–70M** — likely stale |
| CPK Real Estate | Older **21–100M** sheet; **30%** + balance on occupation; Nyando Rd wording |
| Kenya4u | White Horse developer name; **Dec 2028**; USD band + ROI claims |
| Hauzisha | AAD attribution; **Dec 2028**; **7–28M** — portal only |
| Whitehorse LinkedIn / Stacy Moraa | Developer/agent social corroboration of brand + payment options |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://aad.ke/ | AAD → Whitehorse | developer | Live rebrand bridge; **+254 704 191919**; Jahazi / James Gichuru; points to whitehorserealestate.ke |
| 2 | https://whitehorserealestate.ke/ | Whitehorse Real Estate | developer | **AYA Luxury Residence \| Kileleshwa** portfolio lead; siblings Ambra / Rosewood / Grand Premier / Haven; contacts **+254 704 191919**; **info@whitehorserealestate.ke** |
| 3 | https://aad.ke/aad-real-estate-unveils-aya-luxury-residence-project-at-sankara-hotel/ | AAD Real Estate | developer (launch) | Sankara launch **30 Aug 2024**; product mix; amenities; **2-acre**; **sales@aad.ke**; **0704191919**; **4-year 0%**. Live fetch **404**/captcha this pass — retained via indexed developer text + prior lead |
| 4 | https://gna.co.ke/project/aya-residence-kileleshwa-apartments-duplexes-triplex-villas/ | GNA | agent | Full typed matrix; Othaya × Makueni; **Q3 2028**; **30%** deposit |
| 5 | https://nairobirealestate.co.ke/properties/aya-residence | NRE | agent | Same matrix; UC; Sandoral conflict; completion **Q1 2026** conflict; ignore calculator **20%** |
| 6 | https://ownitkenya.com/property/aya-luxury-residence-kileleshwa/ | Own It Kenya | agent | Off-plan; typed sizes/prices; **December 2028** |
| 7 | https://sirfrancismarketingltd.co.ke/properties/aya-luxury-residences-kileleshwa/ | Sir Francis Homes | agent | From **8.5M**; **30% / 48 mo 0%**; updated 2026-10-01 |
| 8 | https://finlay.co.ke/listings/aya-luxury-residence | Finlay | agent | Alternate lower price sheet — conflict evidence |
| 9 | https://kenya4u.com/en/aya-luxury-residences-kileleshwa/ | Kenya 4 You | agent/portal | White Horse developer; Dec 2028; Othaya × Makueni |
| 10 | https://hauzisha.co.ke/developments/aya-luxury-residence/ | Hauzisha | portal | AAD name; Dec 2028; **7–28M** — conf ≤2; **ignore 0730 phone** |

### Evaluated / thin skips

| URL / lead | Why skipped or thinned |
|------------|------------------------|
| https://commercialpropertykenya.com/properties/3-bed-plus-dsq-flat-apartment-for-sale-in-kileleshwa/ | Older CPK sheet; useful conflict prices + **30%** payment — evaluated; not counted in top-10 density |
| https://nairobirealestate.co.ke/developers/sandoral-developers | Sandoral conflict evidence only (Aria Park ≠ AYA proof) |
| https://hauzisha.co.ke/developers/aad-real-estate/ | AAD directory + Ambra/Rosewood/Grand Premier Coming soon — sibling anti-merge |
| https://whitehorserealestate.ke/projects/ | Search-indexed projects hub; live fetch **404**/captcha this pass |
| https://aad.ke/contact/ | Live fetch returned theme placeholder (non-Kenya) — unreliable this pass |
| Whitehorse / Stacy Moraa LinkedIn posts | Useful for sales@whitehorse + construction narrative — social secondary |
| https://block.ke/project/aya-residence/ | Low-trust — discovery seed only |

**sources_evaluated ~14 · sources_retained 10**

---

## 7. Open questions

1. **Legal contracting entity / SPV** — Whitehorse vs legacy AAD vs **Sandoral** (NRE unverified). **`needs_developer_input`** — do **not** invent a winner.  
2. Confirm **current** typed price list vs Whitehorse social **7.5M** floor, agent **8.5M** ladder, Finlay/CPK lower/older sheets, Hauzisha **7–28M** band.  
3. Lock **payment**: deposit % (**30%** agents vs silent launch) + whether instalments run **to handover** or **fixed 48 months**; retire NRE **20%** calculator.  
4. Resolve completion: **Dec 2028** vs **Q3 2028** vs discard NRE **Q1 2026**.  
5. Corroborate NRE construction **92%** and CPK **11-storey** / **Nyando Rd** wording.  
6. Exact plot / GPS at Othaya × Makueni.  
7. Total unit count / blocks (beyond Hauzisha “4 available”).  
8. Whether **sales@aad.ke** remains monitored post-rebrand vs **sales@ / info@whitehorserealestate.ke** only.

---

## 8. Anti-merge

- **≠ Ambra Heights** — Whitehorse / Hauzisha sibling (Whitehorse: handed over & occupied; Hauzisha still “Coming soon” — sibling conflict, not this dossier).  
- **≠ Rosewood Park** — sibling (Kilimani / Hauzisha Coming soon).  
- **≠ Grand Premier** (Grand Premiere spelling on Whitehorse) — sibling Coming soon / Lavington–Kilimani marketing.  
- **≠ Haven Villas** — Whitehorse Lavington triplex product.  
- **≠ Aria Park** (Karen) — NRE Sandoral portfolio neighbour; **not** AYA.  
- **≠** other Othaya / Makueni Kileleshwa schemes (e.g. Diamond Oak, Silver Oak, Venus Oak on nearby corridors) — different products.  
- **Not already in corpus** — no prior `aya-luxury-residence` dossier before this wave.
