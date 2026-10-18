---
slug: auris-residence
external_id: DISC-NBO-017
wave: jafu-2026-10-17
pilot: false
sources_evaluated: 11
sources_retained: 8
last_verified_at: 2026-10-17
inventory_class_intent: building
---

# Auris Residence (DISC-NBO-017) — discovery research

**Not in seed CSV.** Jafu Real Estate Group wave ([hauzisha-developers-2026-10-16.md](../discovery/hauzisha-developers-2026-10-16.md) Jafu section). **Westlands** (Westlands Avenue / Westlands Road marketing), Nairobi — **Jafu Real Estate Group**, hotel+residences hybrid, **under construction / off-plan sales**, completion claims **Dec 2027 vs May–Q4 2028** (conflict).

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355** is **Hauzisha only** — **never** Jafu.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **building / UC** (not Ready/handed-over).

**≠** Citrine Heights / Citrine Tower; **≠** Serene Manor; **≠** Serene Holding Group products; **≠** other Westlands hotel-residences unless proven same — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Auris Residence** | 4 | Hauzisha hub; Ace; Craiova; NRE; Ladva; Ravi; Realtors.co.ke — **no official Auris microsite this pass** |
| `aliases` | secondary | Auris Residence Westlands; Auris Residences (rare plural); “Hotel + Residences” Westlands | 3 | Agent titles |
| `status` | secondary | **Under construction / off-plan sales** — agents: “under construction”, “Off-Plan / Ongoing”; NRE “Under Construction **58%**” (agent progress — **`needs_verification`**); **not** Ready / handed-over | 3 | Craiova; NRE; Block discovery; Hauzisha stock cards |
| `inventory_class` intent | research queue | **`building`** (UC with residual instalment marketing). **Not** `ready`. | — | Method lock |
| `geography.city` | **CANONICAL** soft | Nairobi | 4 | All retained |
| `geography.neighbourhood` | **CANONICAL** soft | **Westlands** | 4 | Hauzisha; all agents |
| `geography.street` | claim set — conflict soft | **Westlands Avenue** (Ace; Realtors; Craiova adjacency narrative) vs **Westlands Road** (NRE; Ravi) — likely same corridor; exact plot **unknown** → **`needs_verification`** | 3 / 2 | Agents only |
| `geography.landmarks` | secondary marketing | Adjacent / steps from **Park Inn by Radisson**; near Oracle, Microsoft; walk to Sarit Centre, Westgate, GTC | 3 | Ace; Craiova; Realtors; NRE |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** soft (trading) | → **Jafu Real Estate Group** (`dev-lead-jafu-real-estate-group` until official contacts/SPV promote) | 4 / 3 | Hauzisha attribution; Realtors.co.ke names Jafu; NRE developer profile; Ace/Ravi portfolio narrative (Serene Manor / Royal Garden / Serenity) — **official site currently features Serene Manor only, not Auris** |
| `concept` | secondary | **Hotel + Residences** hybrid: floors **1–10** hotel operations; floors **11–20** residences for sale; shared hotel amenities | 3 | Ace; Craiova; Realtors; Ravi; Hauzisha |
| `building_specs.height` | claim set | **20-storey** (majority + Hauzisha) vs **21 floors/storeys** (NRE; Ravi; Block) → **`needs_verification`** | 3 / 2 | — |
| `unit_types` | secondary consensus | **Studio**; **1 Bedroom**; **2 Bedroom** | 3 | Hauzisha; Ace; Craiova; NRE; Ladva; Ravi |
| `size_by_type` | claim set — see table | Studio **36 sqm**; 1BR **72 / 75 sqm**; 2BR **105 / 110 sqm** (Hauzisha size band **36–105** omits 110) | 3 | Multi-agent; Hauzisha |
| `total_units` | unknown | — | 0 | Hauzisha “**3** units available” = stock snapshot only — **not** total inventory |
| `price_claims[]` | multi | See **§1a** — typed floor **KES 5.5M–14M** (agent consensus); Hauzisha band **5.5–13.5M** | — | — |
| `currency` | secondary | **KES** | 3 | All price publishers |
| `payment_plan` | secondary — must-have **not locked** | See **§1b** — **30% / balance over 3 yrs @ 0%** (3 agents) vs **20% deposit, balance by May 2028** (Craiova) — conflict; no developer schedule | 2–3 | Ace; Ladva; Ravi vs Craiova |
| `completion_estimate` | claim set — **conflict** | Hauzisha **December 2027** vs Craiova **May 2028** vs Ace/Ladva/Ravi/NRE **end of 2028 / Q4 2028** → **`needs_verification`** + **`needs_developer_input`** | 2 / 3 | Hauzisha vs agents |
| `amenities` | secondary (agent/portal) | Infinity-edge rooftop pool; rooftop gym; yoga/wellness deck; spa/sauna; 8-seat cinema; 20 m indoor mini-golf; leisure lounge (6 m ceilings); reading lounge; coffee lounge + BBQ; kids’ play; business/conference; landscaped art gardens; backup generator; high-speed lifts; 2.5-level parking (2 basement + half-ground); 24/7 CCTV security; smart lock (Craiova) | 3 | Ace; Craiova; NRE; Ravi; Ladva (subset) |
| `amenities` Hauzisha chips | portal only | 2 lifts/block; borehole; built-in wardrobes; floor-to-ceiling windows; heated pool; gym; CCTV; generator — conf ≤2 | ≤2 | Hauzisha |
| `roi_claim` | marketing | Short-stay / Airbnb / corporate rental narratives; NRE ROI chip on developer card — **`needs_verification`**; not quantified on developer official | 1–2 | NRE; Ace; Ravi |
| `legal_title` | unknown | — | 0 | not found |
| `construction_progress` | agent-only | NRE “**58%**” — **`needs_verification`**; no developer progress page this pass | 2 | NRE only |

### Size table (retained)

| Type | Size | Role | Conf |
|------|-----:|------|-----:|
| Studio | **36 sqm** | Multi-agent typed | 3 |
| 1 Bedroom | **72 sqm** | Multi-agent | 3 |
| 1 Bedroom | **75 sqm** | Multi-agent | 3 |
| 2 Bedroom | **105 sqm** | Multi-agent | 3 |
| 2 Bedroom | **110 sqm** | Multi-agent (omitted from Hauzisha 36–105 band) | 3 |
| Hauzisha band | **36–105 sqm** | Portal aggregate | ≤2 |

Gross vs plinth: **not distinguished** on retained sources.

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No developer official price list** recovered this pass (jafugroupkenya.com features **Serene Manor**, not Auris). Typed agent sheet is dense and largely agrees — still cap at conf **3** without official corroboration.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Studio **36 sqm from KES 5.5M**; 1BR **72 from 9.3M**; 1BR **75 from 9.8M**; 2BR **105 from 13.5M**; 2BR **110 from 14M** | Full typed card | Ace Realtors; Craiova; Ladva; Ravi Homes; NRE | 3 | Strong multi-agent consensus — **`needs_verification`** vs LOO |
| B | Band **KES 5.5M – 13.5M**; sizes **36–105 sqm**; **3** units available | Portal card | Hauzisha | ≤2 | Omits **14M** / **110 sqm**; aggregator; phone is portal |
| C | From **KES 5.5M**; Call for Price (no typed sheet) | Soft ask | Realtors.co.ke | 2 | Names **Jafu** explicitly |
| D | From **KES 5.5M**; unit cards Studio **5.5M** / 1BR **9.3M** / 2BR **13.5M** | Aggregator | block.ke | ≤2 | Discovery only — **not authority** |
| E | NRE payment calculator defaults deposit **20%** on **5.5M** studio | Interactive estimate | NRE | ≤2 | Page states “Estimates only… Confirm the schedule” — **not** a published plan |

**Portal scalar:** none. Do not promote a single public `price_from` until developer LOO / brochure.

### 1b. Payment plan — must-have **not locked**

No instalment schedule on **jafugroupkenya.com** for Auris this pass. Agent claims **conflict**.

| Element | Source | Status |
|---------|--------|--------|
| **30%** deposit; balance over **3 years** at **0%** interest | Ace; Ladva; Ravi Homes | Secondary cluster (conf **3**) — only **3** independents → **short of ≥4 lock** |
| **20%** deposit; balance cleared **on or before May 2028** | Craiova | **Conflicts** with 30%/3yr cluster — **`needs_verification`** |
| Block.ke echoes 30%/3yr/0% | block.ke | Low-trust — **do not** count toward ≥4 |
| NRE calculator default 20% quarterly | NRE | Illustrative disclaimer — ignore for lock |
| Official Jafu / Auris payment schedule | — | **Not published** this pass → **`needs_developer_input`** |

**Must-have met?** **No** — need developer schedule **or** a **4th** independent agent echoing the **same** structure (and resolve 20% vs 30% conflict).

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-lead-jafu-real-estate-group` (Hauzisha lead — promote only after official contacts / registry) |
| `legal_name` | **Unknown** this pass (trading **Jafu Real Estate Group** / **Jafu Group**; Companies Registry string not recovered) |
| `trading_names` | Jafu Real Estate Group; Jafu Group; JAFU |
| `website` | https://jafugroupkenya.com/ |
| `evidence` | Official site live — currently hero **Serene Manor** (Lenana / Yaya; 1–4BR + 8BR duplex PH); Hauzisha developer card lists **Serene Manor, Citrine Heights, Auris Residence**; Realtors.co.ke + NRE attribute Auris to Jafu; agents cite prior **Serenity Residency Kilimani**, **Serene Manor**, **Royal Garden** |
| `group_company_id` | **null** — none invented (≠ California “Jafu Group Inc” filing; ≠ Serene Holding Group) |
| `sales_office` / contacts | **Unknown this pass** — no phone/email recovered from official Jafu pages. Agent phones are **agent** contacts only. |
| `confidence` | **4** trading face (multi-source brand) / **0** legal SPV / **0** official sales contacts |

**Never** assign **0730 731 355 / +254 730 731 355** to Jafu — that is **Hauzisha portal CTA only**.

**`needs_developer_input`:** official Auris project page / brochure / LOO; sales phone & email; contracting SPV; payment schedule; completion date; storey count; exact plot.

---

## 3. GroupCompany

**None invented.**

No parent holding company evidenced on retained sources. Do **not** merge with **Serene Holding Group** (separate Hauzisha developer: Serene Boutique / Diamond Mango).

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Ace / Craiova / Ladva / Ravi / Realtors.co.ke / NRE | selling agents / portals | Independent listing pages | 3 |
| Hauzisha | marketing portal | Development hub | ≤2 |
| Park Inn by Radisson (adjacency) | landmark neighbour — **not** co-developer | Agent location copy | 2 |
| Hotel operator (floors 1–10) | unknown | Concept only — operator unnamed | 0 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Ace Realtors | Full typed prices; **30%/3yr/0%**; end-2028; Westlands Avenue; hotel floors 1–10 |
| Craiova Realtors | Same typed prices; **20%** by May **2028**; 20-storey concept |
| Ladva Realtors | Same typed prices; **30%/3yr/0%**; end-2028 |
| Ravi Homes | Same typed prices; **30%/3yr/0%**; Q4/end-2028; **21-storey**; Westlands Road/Avenue mix |
| NRE Real Estate | Same typed prices; Q4 2028; **21 floors**; Jafu developer profile link; UC **58%** claim; verification “not independently confirmed” |
| Realtors.co.ke | Names **Jafu Real Estate Group**; 20-storey hotel+residences; Call for Price; Westlands Avenue |
| Hauzisha | Jafu attribution; Dec **2027**; band 5.5–13.5M — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://jafugroupkenya.com/ | Jafu / JAFU | developer | Brand surface; **Serene Manor** featured — **no Auris page** this pass; site intermittently 403/500 to fetchers |
| 2 | https://hauzisha.co.ke/developments/auris-residence/ | Hauzisha | portal | Jafu; 20-storey hotel+residences; Studio/1/2BR; Dec **2027**; 5.5–13.5M; **ignore 0730 phone** |
| 3 | https://www.acerealtorsltd.com/properties/auris-residence-studio-2-bedroom-hotel-residences-westlands | Ace Realtors | agent | Densest typed sheet + **30%/3yr/0%**; end-2028 |
| 4 | https://craiovarealtors.com/property/auris-residence-hotel-residences-in-westlands/ | Craiova Realtors | agent | Same typed prices; **20%** / May **2028** — payment conflict |
| 5 | https://nairobirealestate.co.ke/properties/auris-residence-westlands-apartments | NRE | agent/portal | Typed prices; Q4 2028; 21 floors; UC 58%; Jafu named |
| 6 | https://ladvarealtors.com/auris-residence-westlands-apartments-for-sale-a-smart-guide-to-modern-living-and-property-investment-in-nairobi/ | Ladva Realtors | agent | Typed prices + **30%/3yr/0%**; end-2028 |
| 7 | https://ravihomes.co.ke/property/auris-residence-westlands-hotel-inspired-luxurystudio1-and-2-bedrooms/ | Ravi Homes | agent | Typed prices + **30%/3yr/0%**; Q4 2028; 21-storey (copy also slips “Marble West” — ignore as paste error) |
| 8 | https://realtors.co.ke/property/auris-residence-westlands-a-new-era-of-hotel-grade-living/ | Realtors Kenya | agent | Explicit **Jafu Real Estate Group**; concept + Westlands Avenue; Call for Price |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/auris-residence-westlands-studio-1-2-bedroom-apartments-for-sale/ | Low-trust / AI — discovery seed only (echoes 30%/3yr + Q4 2028) |
| https://nairobirealestate.co.ke/developers/jafu-real-estate-group | Thin developer stub; overlaps NRE project page |
| Hauzisha “3 units for sale” cards | Unit-ad depth only; do not invent Ready |
| California “Jafu Group Inc” biz filings | Unrelated foreign entity — discard |

**sources_evaluated ~11 · sources_retained 8**

---

## 7. Open questions

1. **`needs_developer_input`:** Publish / recover official **Auris** page, brochure, or LOO on jafugroupkenya.com (or sales office materials).  
2. **`needs_developer_input`:** Official **sales contacts** (phone/email/address) — none found outside agents / Hauzisha CTA.  
3. **`needs_verification` + `needs_developer_input`:** Resolve completion **Dec 2027** (Hauzisha) vs **May 2028** (Craiova) vs **end/Q4 2028** (Ace/Ladva/Ravi/NRE).  
4. **`needs_verification`:** Payment — lock **30%/3yr/0%** vs **20% by May 2028** (need developer schedule or 4th agreeing agent + retire conflict).  
5. **`needs_verification`:** Height **20** vs **21** storeys/floors.  
6. Exact street / plot / GPS (Westlands Avenue vs Westlands Road).  
7. Legal contracting **SPV** / Companies Registry name.  
8. Total residences for sale (floors 11–20) and hotel operator identity.  
9. NRE **58%** construction claim — corroborate with developer progress media.  
10. Confirm Hauzisha **3 units available** is listing stock only (not scheme total).

---

## 8. Anti-merge

- **≠ Citrine Heights / Citrine Tower** (same Jafu wave, Westlands — opposite GTC / different product; do **not** merge hotel+residences Auris with Citrine).  
- **≠ Serene Manor** (Jafu — **Kilimani** / Lenana–Turbo corridor; 1–4BR + duplex PH; featured on jafugroupkenya.com).  
- **≠ Serene Holding Group** products (**Serene Boutique Residency**, **Diamond Mango**) — unrelated Hauzisha developer.  
- **≠ Royal Garden / Serenity Residency Kilimani** — agent-cited prior Jafu portfolio siblings, different schemes.  
- **≠ Marble West** — Ravi Homes payment blurb paste error; not this project.  
- **≠ other Westlands hotel-residences / Park Inn adjacency schemes** unless LOO / title proves same parcel.  
- **≠** California **Jafu Group Inc** — unrelated.
