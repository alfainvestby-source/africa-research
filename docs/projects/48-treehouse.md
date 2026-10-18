---
slug: 48-treehouse
external_id: DISC-NBO-014
wave: elegant-2026-10-16
pilot: false
sources_evaluated: 11
sources_retained: 7
last_verified_at: 2026-10-16
---

# 48 Treehouse (DISC-NBO-014) — discovery research

**Elegant Properties wave** ([elegant-properties-verification.md](../discovery/elegant-properties-verification.md)). Peponi Road, Westlands / Karura Forest edge, **Elegant Properties**, ultra-premium **4BR** off-plan / under construction, completion **Dec 2027** cluster, from **~KES 77.9M**.

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha phone `0730 731 355` never used as developer contact.**

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.

**≠ Oakland Residences** (same Peponi / Karura Elegant corridor; 3&4BR; rental stock live) · **≠ Forestview Residences** (Eldama Ravine; 2&3BR from ~29.5M) · **≠ Casa Karura** (54 units; 3&4BR; Nov 2029) — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **48 Treehouse** (site styling **48Treehouse**) | 5 | elegantproperties.co.ke/48-treehouse; Featured; brochure |
| `aliases` | secondary | 48Treehouse; 48 Treehouse Apartments; 48 Treehouse Peponi | 4 | Realtor Kenya; Hauzisha; Block slug |
| `status` | claim set | **Off-plan / under construction** — Featured completion **Dec 2027**; project page construction-gallery captions **Mar / Jun / Jul / Nov 2025** imply site works underway → show both; UC secondary | 5 / 3 | Featured; project page gallery |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** — Karura Forest edge | 5 | project page; brochure; Featured |
| `geography.street` | **CANONICAL** | **Peponi Road** | 5 | project page; Featured; brochure |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-elegant-properties` | 5 | Elegant project + portfolio + About; Hauzisha attribution |
| `unit_types` | **CANONICAL** | **4 Bedroom** only (single typology marketing) | 5 | project page; Featured; brochure; Realtor Kenya |
| `size_by_type` | claim set — see table | Band **~5,200–5,455 sqft**; official “from” conflict | 4–5 | Brochure plans; Featured; project page |
| `total_units` | **CANONICAL** soft | **48** | 5 | Project page (“48 grand… apartments”); brochure (“48 stylish… apartments”) |
| `building_specs` | secondary | **One apartment per floor**; **2** glass-back elevators **per block**; brochure floor plans label **Wing C** / **Wing D** → multi-wing; storey count not stated | 4 / 0 | Brochure highlights + unit plans |
| `bathrooms` | secondary | **5** baths (agent/portal) | 3 | Hauzisha; Block — **`needs_verification`** |
| `price_claims[]` | multi | See **§1a** — official **77.9M** vs portal **73M** | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | Featured |
| `payment_plan` | unknown — must-have **not met** | No developer schedule; &lt;4 agents with concrete terms → **`needs_developer_input`** | 0 | See **§1b** |
| `completion_estimate` | **CANONICAL** soft | **December 2027** (Featured + Hauzisha + Realtor Kenya echo) | 5 / 3 | Featured (conf 5); agents secondary |
| `amenities` (unit + finishes) | **CANONICAL** soft | Spanish large-format porcelain tiles; **3.5m** ceilings; solid teak joinery / bedroom flooring; designer Italian kitchens with large islands; premium **Bosch** in-built appliances (fully fitted); German sanitary; full home automation (motorised curtains, smart locks, smart lighting & music); gas fireplaces on balconies; private lobby per apartment | 5 | Project page amenities; brochure |
| `amenities` (rooftop / shared) | **CANONICAL** soft | Heated pool + baby pool; gymnasium; children’s playground; jogging track; entertainment hall; green lawns; lawn chess; trampoline; hammocks; landscape garden; sit-out decks; steam; sauna | 5 | Brochure amenity list |
| `roi_claim` | unknown | — | 0 | not found |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Elegant scheme on Peponi (not a named multi-phase precinct) | — | — |

### Size table (retained)

| Type | Size | Role | Conf |
|------|------|------|-----:|
| 4BR Wing C Plan 02 | **5,280 sqft** | Brochure typed unit plan | 5 |
| 4BR Wing D Plan 04 | **5,455 sqft** | Brochure typed unit plan | 5 |
| 4BR “from” (Featured) | **From 5,338 sqft** | Official Featured card | 5 | Conflicts with Wing C 5,280 → **`needs_developer_input`** |
| 4BR marketing floor | **Over 5,200 sqft** (~**483+ sqm**) | Project page; brochure highlight | 5 |
| 4BR agent band | **5,280–5,455 sqft** | Hauzisha; Realtor Kenya starts 5,280 | 4 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official “from”:** Featured Properties **From Kshs 77.9 million**. Portal **KES 73M** conflicts → keep both; resolve with Elegant sales / LOO (**`needs_developer_input`** for any public “from” that prefers 73M).

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 77.9M** | Featured card (4-Bed) | elegantproperties.co.ke/Featured-Properties | 5 | Official “from” |
| B | From **KES 77.9M** / **KSh 77.9 million** | Agent pages echoing developer | Realtor Kenya; Block.ke | 3 / ≤2 | Echo of A; Block not authority |
| C | **KES 73M** (development + unit card; 1 unit listed) | Portal inventory | hauzisha.co.ke/developments/48-treehouse/ | 2 | Conflicts with A — **`needs_verification`**; phone on page is Hauzisha — **ignored** |

**Portal scalar:** none for public canonical. Prefer A until Elegant confirms whether 73M is a live ask, older list, or error.

### 1b. Payment plan — must-have **not met**

| Element | Source | Status |
|---------|--------|--------|
| Developer instalment / cash schedule on project page, Featured, or brochure | — | **Not published** this pass → **`needs_developer_input`** |
| Hauzisha FAQ: staged across build; “terms vary” | Hauzisha | Generic — no % / tenor — not countable toward ≥4-agent lock |
| Block “confirmed at enquiry” + illustrative 20% calculator | block.ke | Discovery / UI only — **not retained as authority** |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-elegant-properties` |
| `legal_name` | **Unknown** this pass (trading **Elegant Properties** / **Elegant Properties Kenya**; Companies Registry string not recovered) |
| `trading_names` | Elegant Properties; Elegant Properties Kenya |
| `website` | https://www.elegantproperties.co.ke/ |
| `evidence` | Dedicated project page; Featured; portfolio row; About (“over 30 years”; family-run); brochure “A DEVELOPMENT BY” + contacts |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts | **+254 700 004 449**; brochure also **+254 731 286 286**; **info@elegantproperties.co.ke**; www.elegantproperties.co.ke — **never** Hauzisha **0730 731 355** |
| `confidence` | **5** trading face / **0** legal SPV |

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| CityBlue (testimonials / other schemes) | brand adjacency on Elegant About | Skynest rental-management testimonial — **not** named as 48 Treehouse SPV | 0 for Treehouse contracting |
| Karura Forest Reserve | location amenity (2,500 acres; trails) | Brochure + project narrative | 3 location context only |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Realtor Kenya | Echoes Elegant: from **5,280 sqft**, from **KSh 77.9M**, completion **Dec 2027** (posted as Elegant Properties) |
| Hauzisha | Elegant attribution; sizes **5280–5455**; completion **Dec 2027**; price **73M** (conflict); **phone discarded** |
| Block.ke | Discovery seed only — 77.9M / 48 units / Peponi (not authority) |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.elegantproperties.co.ke/48-treehouse | Elegant Properties | developer | Primary narrative; 48 units; finishes; Peponi; gallery dates |
| 2 | https://www.elegantproperties.co.ke/Featured-Properties | Elegant Properties | developer | From **5,338 sqft**; from **KES 77.9M**; completion **Dec 2027** |
| 3 | https://www.elegantproperties.co.ke/48%20Treehouse/48TREEHOUSE%20BROCHURE%20-2-.pdf | Elegant Properties | brochure | Unit plans 5,280 / 5,455; amenities; phones **731 286 286** / **700 004 449** |
| 4 | https://www.elegantproperties.co.ke/our-portfolio | Elegant Properties | developer | Portfolio name + Peponi / Karura; separates Oakland |
| 5 | https://www.elegantproperties.co.ke/about-us | Elegant Properties | developer | Trading face; **+254 700 004 449**; info@ |
| 6 | https://www.realtorkenya.com/properties/48treehouse-4-bedroom-apartments-peponi-road-westlands | Realtor Kenya | agent | 5,280 / 77.9M / Dec 2027 |
| 7 | https://hauzisha.co.ke/developments/48-treehouse/ | Hauzisha | portal | 73M claim; size band; Dec 2027 — phone **ignored** |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/48treehouse-ultra-luxury-4-bedroom-apartments-on-peponi-road-westlands/ | Low-trust / AI-heavy — discovery seed only |
| https://www.elegantproperties.co.ke/Forestview-Residences (+ Forestview e-brochure map pin “48 TREEHOUSE”) | Anti-merge only — different scheme |
| https://www.elegantproperties.co.ke/rentals (Oakland Residences rental card) | Anti-merge — completed rental inventory |
| https://gdproperties.co.ke/property/oakland-residences/ | Anti-merge Oakland (3&4BR; ~4,465 sqft 4BR rent) |
| “48 Treehouse Corp” Brooklyn NY license result | Irrelevant foreign entity |

**sources_evaluated ~11 · sources_retained 7**

---

## 7. Open questions

1. Resolve official size “from **5,338 sqft**” vs brochure Wing C **5,280** / Wing D **5,455**.  
2. Resolve price **77.9M** (Featured) vs Hauzisha **73M**.  
3. Publish payment / instalment schedule (developer LOO).  
4. Legal contracting entity / SPV for LOO.  
5. Exact wing / block / storey count and plot / GPS on Peponi.  
6. Confirm bathroom count (agent **5**) and DSQ claims (Hauzisha amenity list).

---

## 8. Anti-merge

- **≠ Oakland Residences** — same Elegant developer + Peponi / Karura edge; portfolio lists separately as **3 & 4-Bed**; Elegant **rentals** already list Oakland 4BR unfurnished; Greenday cites ~**4,465 sqft** 4BR — smaller typology / different (mature) product from 48-unit Treehouse. Brochure map even labels Oakland near Treehouse as a **neighbor**, not the same scheme.  
- **≠ Forestview Residences** — **Eldama Ravine Road**; **2 & 3BR** from **~KES 29.5M**; Featured completion **June 2027**. Forestview e-brochure map pins **48 TREEHOUSE** as a distinct nearby label.  
- **≠ Casa Karura** — Featured: **54** residences; **3 & 4BR**; **KES 44–88M**; completion **November 2029** — different count, mix, price band, and year.
