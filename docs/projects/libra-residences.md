---
slug: libra-residences
external_id: DISC-NBO-019
wave: hauzisha-b-2026-10-17
pilot: false
sources_evaluated: 14
sources_retained: 10
inventory_class: building
last_verified_at: 2026-10-17
---

# Libra Residences (DISC-NBO-019) — discovery research

**Not in seed CSV.** Hauzisha Wave B ([hauzisha-wave-b-prep.md](../../internal/hauzisha-wave-b-prep.md)). **George Padmore Road**, Kilimani, Nairobi — **GLBC Group**, under construction, handover **2027**.

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only if hit). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never GLBC.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **Under Construction / building** only.

**≠** Only You; **≠** GLBC Gemini Hub / Gemini Residences; **≠** Staroot Gemini Residency Phase 2 (NBO-009); **≠** Roseville Residences — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Libra Residences** | 5 | glbcgroup.co.ke/portfolio/libra-residences; projects hub |
| `aliases` | secondary | LIBRA Residences; Libra Apartments; Libra Residencies (agent spelling) | 3 | GLBC copy; NRE; CPK |
| `inventory_class` | **CANONICAL** | **`building`** — developer Status **Under Construction**; not Ready / handed-over | 5 | GLBC project + projects hub |
| `status` | **CANONICAL** soft | **Under construction** — handover **2027**; agents add Dec / Q4 / Nov 2027 | 5 / 3 | GLBC; Hauzisha; NRE; Geomara; BRK |
| `geography.city` | **CANONICAL** | Nairobi | 5 | GLBC; all |
| `geography.neighbourhood` | **CANONICAL** | **Kilimani** | 5 | GLBC; all |
| `geography.street` | **CANONICAL** | **George Padmore Road**, off Ngong Road (developer: **next to Roseville Residences**) | 5 | GLBC address block |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-glbc-group` | 5 | GLBC project + portfolio; Hauzisha attribution |
| `unit_types` | **CANONICAL** | **3B + SQ**; **4B + DSQ / SQ** (250 / 258 / 264 / 265 sqm); **5B + SQ** | 5 | GLBC Plans |
| `size_by_type` | **CANONICAL** soft | Developer plans **193 / 250 / 258 / 264 / 265 / 285 sqm**; overview band **193–284 sqm** (5BR plan **285** vs band **284** — soft conflict) | 5 / 4 | GLBC Plans vs Overview Area |
| `total_units` | **CANONICAL** soft | Developer **119**; agents often **120** | 5 / 3 | GLBC; NRE; Bellano |
| `building_specs` | secondary | **20** storeys (developer); agents: **2 lifts per block**, **2 blocks**, **0.8 acres**, **2–4 units/floor** | 5 / 2–3 | GLBC storeys; Hauzisha/Bellano extras — **`needs_verification`** |
| `price_claims[]` | multi | See **§1a** — official band **KES 17–25M** vs denser agent typed sheets | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | GLBC “KSh17mil – KSh25mil” |
| `payment_plan` | secondary — must-have **not locked** | See **§1b** — developer silent; agents “flexible” / deposit-negotiable only; NRE calculator illustrative | ≤2 | — |
| `completion_estimate` | **CANONICAL** soft | Developer **Handover 2027**; agents **December / Q4 / November 2027** | 5 / 3 | GLBC; Hauzisha; NRE; Realtors; Geomara; BRK |
| `amenities` | **CANONICAL** soft | 24-hour CCTV; children’s play area; high-speed elevator; solar lighting; landscape garden; swimming pool; intercom; community shop; modern gym; modern club house | 5 | GLBC Amenities |
| `amenities` agent extras | secondary | Adults & kids pool; borehole; backup generator; double lifts; business hub / shopping; smart lock; heated pool (Geomara) | 2–3 | Hauzisha; Realtors; Geomara; NRE — **`needs_verification`** |
| `construction_progress` | secondary | NRE “**58%**”; Bellano “**first floor stage**” — not on developer pages | 2 | NRE; Bellano — **`needs_verification`** |
| `roi_claim` | secondary marketing | NRE “ROI **10.7%**”; Realtors “rental income over **130k**/month” | 2 | NRE; Realtors — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Kilimani tower scheme | — | — |

### Size table (retained)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| 3B + SQ | **193 sqm** | Developer Plans | 5 |
| 4B + DSQ | **250 sqm** | Developer Plans | 5 |
| 4B + SQ | **258 sqm** | Developer Plans | 5 |
| 4B + SQ | **264 sqm** | Developer Plans | 5 |
| 4B + SQ | **265 sqm** | Developer Plans | 5 |
| 5B + SQ | **285 sqm** | Developer Plans | 5 |
| Overview Area band | **193 – 284 sqm** | Developer Overview (5BR ceiling **284** vs plan **285**) | 4 — soft vs Plans |
| Agent 5BR | **284 sqm** | CPK; NRE; BRK | 3 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official band:** GLBC project page **KSh17mil – KSh25mil** (no typed unit list on official page this pass). Agent sheets diverge widely — keep as secondary claims; do not force a portal scalar.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Band **KES 17M – 25M** | Developer Overview Price Range | glbcgroup.co.ke/portfolio/libra-residences | 5 | Official band only |
| B | 3BR+SQ **193** **17.76M**; 4BR+SQ **250** **23.0M**; **258** **23.46M**; **264/265** **23.92M**; 5BR+SQ **284** **25.76M** | Typed sheet | CPK | 3 | Floor aligns with A; 5BR size 284 |
| C | 3B+SQ **193** **17.8M**; 4B+SQ **258** **23.4M**; **264** **23.9M** | Partial typed | Masterways | 3 | Near B |
| D | 3BR **193 from 19.7M**; 4BR **250–265 from 25.3–26.3M**; 5BR **284 from 28M** | Typed card | NRE | 3 | Above official ceiling on mid/high; diaspora FAQ also cites **17.76 / ~23 / 25.76** — internal NRE conflict — **`needs_verification`** |
| E | 3BR+SQ **193 19.7M**; 4BR+SQ **250/258 25.3M**; **264/265 26.3M**; 5BR+SQ **258 28M** | Typed body (hero card still **32.5M**) | Realtors.co.ke | 3 | 5BR size **258** conflicts with developer **285** — **`needs_verification`**; hero **32.5M** likely stale |
| F | 3BR **193 from 19M**; 4BR **250 25.5M** / **258 26.5M** / **264 27.5M** / **265 28.5M**; 5BR **285 31M** | Typed table; deposit-negotiable | Bellano Group | 3 | 5BR **31M** above official **25M** band |
| G | 3BR **193 from 19M**; 4BR **258 from 24.8M**; **264 from 25.7M**; 5BR **284 from 27.6M** | Typed | Geomara Homes | 3 | |
| H | 3BR+DSQ **193 from 21M**; 4BR+DSQ **250/258 27M**; **264 28M**; 5BR+DSQ **284 30M** | Typed | BuyRentKenya (Sir Francis Homes) | 3 | Near Hauzisha band |
| I | Band **KES 21M – 30M**; sizes **193–285** | Portal card | Hauzisha | ≤2 | Aggregator; phone is portal |
| J | From **KES 19M** (index card only) | Listing index | Flamingo Real Estate | ≤2 | Thin — no typed sheet fetched |

**Portal scalar:** none. Prefer GLBC **17–25M** marketing band until LOO; resolve agent **~19.7–31M** sheets as live stock / floor vs stale.

### 1b. Payment plan — must-have **not met**

No instalment **%** schedule on GLBC project, contact, about, or projects pages this pass.

| Element | Source | Status |
|---------|--------|--------|
| “Flexible payment plans available during construction” | CPK | Thin — no % |
| “Flexible pricing negotiated on deposit size” / higher deposit → discount | Bellano | Thin — no % |
| “Flexible instalments… higher-deposit and full-cash options” | NRE narrative | Thin |
| NRE **Payment Plan Calculator** default **20%** deposit + quarterly remainder | NRE | **Illustrative** (“Estimates only… confirm… developer”) — **not** a published schedule |
| Staged off-plan terms “vary by development” | Hauzisha FAQ | Portal boilerplate |
| Official GLBC payment schedule | — | **Not published** this pass |

**Must-have met?** **No** — need developer schedule **or** ≥4 independent agents publishing the **same** % structure.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-glbc-group` |
| `legal_name` | **Unknown** this pass (trading **GLBC Group**; Companies Registry string not recovered) |
| `trading_names` | GLBC Group |
| `website` | https://www.glbcgroup.co.ke/ |
| `evidence` | Project page; projects hub; home portfolio; About; Contact; Hauzisha attribution |
| `group_company_id` | **null** — none invented |
| `related_trading_notes` | Site copy also mentions **Leos Realty Group** (home Off-Plan blurb; About mission) — treat as **related trading / marketing face**, not proven GroupCompany or Libra SPV this pass |
| `sales_office` / contacts | **Project page (live):** **+254 798 556 666**; **info@glbcgroup.com**. **Head office / site chrome (live):** **+254 705 81 81 81**; **+254 712 78 77 44**; **info@glbcgroup.co.ke**; Mon–Sat 9am–4pm; Nairobi, Kenya (street address not published this pass) |
| `legal_partner` (stakeholder) | **NMN Law Associates LLP** — info@nmnlaw.co.ke (GLBC home “Legal Partners”) — conf **4** portfolio-level |
| `confidence` | **5** trading face / **0** legal SPV |

**Never** assign **0730 731 355 / +254 730 731 355** to GLBC — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.** Leos Realty Group wording on glbcgroup.co.ke is insufficient to invent a parent entity.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| NMN Law Associates LLP | legal_partner (portfolio) | GLBC home Legal Partners | 4 |
| Leos Realty Group | marketing_partner / related trading face (unproven) | GLBC home + About copy | 2 — **`needs_verification`** |
| Roseville Residences | neighbour landmark only | GLBC Libra address “next to Roseville Residences” | 5 as neighbour label — **≠** this project |
| CPK / NRE / Realtors / Bellano / Geomara / Masterways / BRK / Flamingo | selling agents | Independent listing pages | 3 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Densest low typed sheet (**17.76–25.76M**); flexible payment (no %); handover 2027 |
| NRE Real Estate | Typed **19.7–28M**; Dec/Q4 2027; **58%** progress claim; illustrative 20% calculator |
| Realtors.co.ke | Typed **19.7–28M** body + stale hero **32.5M**; Q4 2027; GLBC portfolio names |
| Bellano Group | Typed **19–31M**; Dec 2027; **2 blocks / 0.8 acres**; deposit-negotiable |
| Geomara Homes | Typed **19–27.6M**; show house **July 2026**; completion **Nov 2027** |
| Masterways | Partial typed **17.8 / 23.4 / 23.9M**; Q4 2027 |
| BuyRentKenya (Sir Francis Homes) | Typed **21–30M**; show house July 2026; Nov 2027 |
| Hauzisha | GLBC attribution; **21–30M**; Dec 2027 — portal only |
| Flamingo Real Estate | Index “from **19M**” — thin |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.glbcgroup.co.ke/portfolio/libra-residences/ | GLBC Group | developer | Primary: UC; 119 units; 20 storeys; sizes/plans; amenities; **17–25M**; handover 2027; **+254 798 556 666**; info@glbcgroup.com |
| 2 | https://www.glbcgroup.co.ke/projects/ | GLBC Group | developer | Libra UC card; Gemini Residences (Mombasa Rd) distinct |
| 3 | https://www.glbcgroup.co.ke/contact-us/ | GLBC Group | developer | **+254 705 81 81 81**; **+254 712 78 77 44**; info@glbcgroup.co.ke |
| 4 | https://www.glbcgroup.co.ke/ | GLBC Group | developer | Portfolio incl. Libra; NMN Law; Leos Realty blurb; +254712787744 header |
| 5 | https://commercialpropertykenya.com/properties/libra-residences-kilimani/ | CPK | agent | Typed prices aligning to official floor; flexible payment |
| 6 | https://nairobirealestate.co.ke/properties/libra-residences-kilimani | NRE | agent | Typed mid sheet; Dec 2027; progress %; payment calculator disclaimer |
| 7 | https://realtors.co.ke/property/libra-residences-3-4-5-bedroom-apartments-for-sale-along-george-padmore-road/ | Realtors Kenya | agent | Floor plans + typed prices; Q4 2027; GLBC sibling names |
| 8 | https://www.bellanogroup.com/libra-residences.html | Bellano Group | agent | Typed **19–31M**; 2-block / acre claims; Dec 2027 |
| 9 | https://geomarahomes.co.ke/public/properties/libra-residences | Geomara Homes | agent | Typed prices; show house July 2026; Nov 2027 |
| 10 | https://hauzisha.co.ke/developments/libra-residences/ | Hauzisha | portal | GLBC name; Dec 2027; **21–30M** — conf ≤2; **ignore 0730 phone** |

### Evaluated / thin skips

| URL / lead | Why skipped or thinned |
|------------|------------------------|
| https://www.buyrentkenya.com/listings/3-bedroom-apartment-for-sale-kilimani-4030795 | Useful **21–30M** typed + Nov 2027 — overlap with Hauzisha/Geomara timing; retained as evaluated secondary (price claim H), not counted in retained 10 to avoid portal clutter |
| https://www.masterways.co.ke/properties/libr-residences | Partial typed near CPK — evaluated; claim C kept |
| https://www.flamingorealestate.co.ke/property-city/kilimani/ | Index “from 19M” only — thin |
| https://www.glbcgroup.co.ke/about/ | Trading narrative + Leos Realty; no Libra specs |
| block.ke (if present) | Low-trust — discovery only |

**sources_evaluated ~14 · sources_retained 10**

---

## 7. Open questions

1. Confirm **current** typed price list vs GLBC **17–25M** band (retire or keep agent **~19.7–31M** sheets).  
2. Obtain **official payment schedule** (LOO) — no % lock this pass.  
3. Legal contracting entity / SPV for sale agreements.  
4. Resolve **119 vs 120** units; **284 vs 285 sqm** 5BR; Realtors 5BR **258 sqm** anomaly.  
5. Verify Bellano **2 blocks / 0.8 acres / 2–4 units per floor** and Hauzisha **2 lifts per block**.  
6. Exact plot / GPS on George Padmore Road.  
7. Clarify **Leos Realty Group** relationship to GLBC (marketing vs legal).  
8. Corroborate construction **%** / “first floor” claims and show-house **July 2026**.

---

## 8. Anti-merge

- **≠ Only You / Onlyou** (separate Hauzisha Wave B scheme; EIA face **Onlyou Investments Limited** — do not merge with Libra).  
- **≠ GLBC Gemini Hub / Gemini Residences** (GLBC portfolio — **Mombasa Road**, different product/sizes; same developer, different property).  
- **≠ Staroot Gemini Residency Phase 2** (**NBO-009**) — different developer/geography; shared “Gemini” word only.  
- **≠ Roseville Residences** — **neighbour only** on GLBC Libra address line; not this development.  
- **≠** other GLBC zodiac siblings (Taurus, Aries, Leo Residences, Indesign Makumbi Park) — same developer, different sites/products.
