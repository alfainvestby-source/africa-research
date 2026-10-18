---
slug: forestview-residences
external_id: DISC-NBO-012
wave: elegant-2026-10-16
pilot: false
sources_evaluated: 12
sources_retained: 9
last_verified_at: 2026-10-16
---

# Forestview Residences (DISC-NBO-012) — discovery research

**Not in seed CSV.** Elegant Properties verification wave ([elegant-properties-verification.md](../discovery/elegant-properties-verification.md)). **Eldama Ravine Road**, Karura Forest edge, Westlands, Nairobi — **Elegant Properties**, off-plan / under construction, completion **~June 2027**.

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never Elegant.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **Off-plan / UC** only.

**≠** Oasis Forest One; **≠** Casa Karura; **≠** Lofts @ Karura; **≠** Oak & Ivy — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Forestview Residences** | 5 | elegantproperties.co.ke/Forestview-Residences; Featured-Properties; brochure PDF |
| `aliases` | secondary | ForestView Residences; Forestview Residence (singular); Spring Valley Westlands (agent corridor label) | 3 | CPK; BuyRentKenya |
| `status` | **CANONICAL** soft | **Off-plan / under construction** — site progress gallery on developer page (captions **March–Nov 2025**, **June 2026**); not Ready | 5 / 4 | Elegant project page construction gallery; Featured completion target |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Elegant; all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** — Karura Forest edge (Spring Valley / Peponi corridor marketing on some agents) | 5 | Elegant; brochure location map |
| `geography.street` | **CANONICAL** | **Eldama Ravine Road** (directly facing / edge of **Karura Forest**) | 5 | Elegant project + Featured; brochure |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-elegant-properties` | 5 | Elegant project + About + brochure “A Development By”; Hauzisha attribution |
| `unit_types` | **CANONICAL** soft | **2 Bedroom**; **2 Bedroom + DSQ**; **3 Bedroom**; **3 Bedroom + DSQ** | 4 | Elegant “2 & 3-bedroom”; A-list / CPK / Flamingo typed cards; brochure Unit 01–07 plans |
| `size_by_type` | claim set — see table | Brochure gross areas **~193–340 sqm**; Featured band **2,098–3,658 sqft** | 5 / 4 | Brochure; Featured; A-list sqm/sqft |
| `total_units` | unknown this pass | — | 0 | not stated on retained developer pages |
| `building_specs` | secondary — brochure | **3** panoramic passenger lifts + **1** service lift; central atriums/skylights; rooftop amenity deck; generator backup all areas; borehole; CCTV + electric fence; dedicated + visitor parking | 4 | Brochure amenity/spec block; A-list echo |
| `price_claims[]` | multi | See **§1a** — official “from **29.5M**” vs older agent **27.1M** sheets | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | Elegant “Kshs 29.5m” |
| `payment_plan` | secondary — must-have **not locked** | See **§1b** — developer silent; **3** agents share **20/60/20** (short of ≥4) → **`needs_verification`** | 3 | CPK; A-list; BuyRentKenya |
| `completion_estimate` | **CANONICAL** soft | **June 2027** (Elegant Featured) vs agent “**end of 2027**” (CPK; Citiscape; one BRK) | 5 / 3 | Featured wins month; year agreed |
| `amenities` | **CANONICAL** soft | Heated swimming pool + expansive deck; gym with ladies’ & gents’ steam rooms; jogging track; lawn games; kids’ play area; events hall; manicured gardens / rooftop lawn; grand lobby + 24/7 security | 5 | Elegant project page; brochure “Sky-High Living”; Featured narrative |
| `amenities` finishes | **CANONICAL** soft | Large balconies; floor-to-ceiling heights/windows; designer Italian kitchens with in-built appliances; premium German sanitary fittings; large closet bedrooms | 5 | Elegant amenities bullets; brochure |
| `roi_claim` | secondary marketing | “UN Blue Zone” / high rental demand (agents) — no quantified ROI on developer pages | 2 | A-list; Flamingo — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone forest-edge scheme (not a named masterplan precinct) | — | — |

### Size table (retained)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| Unit 01 (brochure) | **192.78 sqm** | Developer brochure gross | 5 |
| Unit 02 | **194.89 sqm** | Brochure | 5 |
| Unit 03 | **243.72 sqm** | Brochure | 5 |
| Unit 05 | **215.75 sqm** | Brochure | 5 |
| Unit 07 | **269.83 sqm** | Brochure | 5 |
| Unit 06 | **337.84 sqm** | Brochure | 5 |
| Unit 04 | **339.77 sqm** | Brochure | 5 |
| Featured marketing band | **2,098 – 3,658 sqft** | Developer Featured card | 5 |
| Agent typed (A-list) | 2BR **193 / 195 sqm**; 2BR+DSQ **216**; 3BR **244**; 3BR+DSQ **270 / 338 / 340** | Aligns with brochure ± rounding | 4 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official “from”:** Elegant project page + Featured both **From Kshs 29.5m** — **agree** (no official-vs-official conflict this pass). Agent sheets still show older **27.1M** floors and denser typed cards → keep as secondary claims.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 29.5M** | Developer hub + Featured | elegantproperties.co.ke/Forestview-Residences; Featured-Properties | 5 | Official “from” |
| B | Size band **2,098–3,658 sqft** with from **29.5M**; completion **June 2027** | Featured card | Featured-Properties | 5 | Official |
| C | 2BR **193/195 sqm from 29.5M**; 2BR+DSQ **216 from 34.1M**; 3BR **244 from 35.7M**; 3BR+DSQ **270 from 33.6M** / **338 from 47.1M** / **340 from 42.9M** | Typed unit card | A-list Real Estate | 3 | Aligns “from” with A; internal 3BR+DSQ lows &lt; plain 3BR — **`needs_verification`** |
| D | 2BR **193/195 from 27.1M**; 2BR+DSQ **216 from 28.9M**; 3BR **244 from 33.0M**; 3BR+DSQ **270/338/340 from 30.9M** | Older typed sheet | CPK | 3 | Below official from; 3BR+DSQ &lt; 3BR anomaly |
| E | Same shape as D with 3BR+DSQ **340 from 38.9M** | Agent card | Flamingo Real Estate | 3 | |
| F | 2 Bed **2,077 sqft Ksh 27.1M–31.1M**; 3 Bed+DSQ **3,658 sqft 38.9M–50.1M** | Compressed ranges | Citiscape; BRK Karura listing | 3 | Conflicts with A on floor |
| G | 2BR from **29.5M**; 2BR+DSQ from **33.9M**; 3BR from **35.7M**; 3BR+DSQ from **33.6M** + narrative “from 34M” | Mixed hero vs table | BuyRentKenya Westlands listing | 3 | Table near C; hero “34M” messy |
| H | Band **KES 34.1M – 47M**; sizes **193–270 sqm**; **2** units available | Portal card | Hauzisha | ≤2 | Aggregator; phone is portal |
| I | 3BR+DSQ **~330 sqm from KES 45M** | Single typology ask | Masterways | 3 | |
| J | From **KES 29.5M**; payment “at enquiry” | Aggregator | block.ke | ≤2 | Discovery only — **not authority** |

**Portal scalar:** none. Use Elegant **29.5M** as marketing floor only after LOO confirms current stock; resolve agent **27.1M** sheets as stale vs live.

### 1b. Payment plan — must-have **triggered** (developer project) but **structure not locked**

No instalment schedule on Elegant project page, Featured, or brochure this pass. **Three** independent agents publish the same **20% / 60% quarterly / 20% handover** shape — **short of the ≥4-agent lock**.

| Element | Source | Status |
|---------|--------|--------|
| **20%** initial deposit; **60%** equal quarterly instalments; **20%** upon completion / handover | CPK; A-list; BuyRentKenya (Westlands listing) | Secondary consensus (conf **3**) — **`needs_verification`** vs Elegant LOO |
| “Flexible payment plans” without % split | Flamingo | Thin — does not strengthen the 20/60/20 lock |
| Official Elegant payment schedule | — | **Not published** this pass |
| Block.ke calculator default 20% | block.ke | Illustrative; listing admits schedule not stated — ignore |

**Must-have met?** **No** — need developer schedule **or** a **4th** independent agent echoing 20/60/20.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-elegant-properties` |
| `legal_name` | **Unknown** this pass (trading **Elegant Properties** / **Elegant Properties Kenya**; Companies Registry string not recovered) |
| `trading_names` | Elegant Properties; Elegant Properties Kenya |
| `website` | https://www.elegantproperties.co.ke/ |
| `evidence` | Project page; Featured-Properties; portfolio card; About (“family-run… over 30 years”); brochure “A Development By” + Tel/email; seed contacts |
| `group_company_id` | **null** — none invented |
| `sales_office` | 8th Floor, Valley View Office Park, City Park Drive; P.O. Box 32705–00600 Nairobi; **+254 700 004 449**; **+254 731 286 286** (brochure Tel); **info@elegantproperties.co.ke** |
| `confidence` | **5** trading face / **0** legal SPV |

**Never** assign **0730 731 355 / +254 730 731 355** to Elegant — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.**

Brochure line “Voted as a Superbrand OTHER DEVELOPMENTS by CityBlue” and About testimonial (CityBlue Hotels managing Skynest rentals) → at most **marketing / ops partner** elsewhere in portfolio — **not** a GroupCompany for Forestview this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| CityBlue (hotels / Superbrand mention) | marketing_partner / ops (portfolio-level) | Brochure Superbrand line; About Skynest rental testimonial | 2 — **not** Forestview SPV |
| A-list / CPK / Flamingo / BRK / Masterways / Citiscape | selling agents | Independent listing pages | 3 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| A-list Real Estate | Typed sizes/prices aligned to ~29.5M; June 2027; **20/60/20** payment |
| CPK Real Estate | Older **27.1M** sheet; end-2027; **20/60/20** |
| BuyRentKenya (Westlands listing) | Typed ~29.5M+; **20/60/20**; end-2027 |
| Flamingo Real Estate | **27.1M** typed sheet; “flexible” payment (no %) |
| Citiscape Valuers | **27.1–31.1M / 38.9–50.1M** bands; end-2027 |
| Masterways | Single 3BR+DSQ from **45M**; June 2027 |
| Hauzisha | Elegant attribution; **34.1–47M**; June 2027 — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.elegantproperties.co.ke/Forestview-Residences | Elegant Properties | developer | Primary narrative; from 29.5M; amenities; UC gallery; Elegant phone/email |
| 2 | https://www.elegantproperties.co.ke/Featured-Properties | Elegant Properties | developer | From 2,098–3,658 sqft; from 29.5M; **Completion June 2027** |
| 3 | https://www.elegantproperties.co.ke/Forestivew%20Residences%20E-Brochure%20copy.pdf | Elegant Properties | brochure | Unit gross areas; finishes; lifts; contacts **731 286 286 / 700 004 449** |
| 4 | https://www.elegantproperties.co.ke/about-us | Elegant Properties | developer | Trading face; **+254 700 004 449**; info@ |
| 5 | https://www.elegantproperties.co.ke/contact | Elegant Properties | developer | Valley View Office Park address + hours |
| 6 | https://a-listrealestate.ke/property/forestview-residences/ | A-list Real Estate | agent | Densest typed price/size + payment + June 2027 |
| 7 | https://commercialpropertykenya.com/properties/forestview-residences-spring-valley-westlands/ | CPK | agent | Older prices; payment; end-2027 |
| 8 | https://www.buyrentkenya.com/listings/2-bedroom-apartment-for-sale-westlands-area-4032755 | BuyRentKenya | agent/portal | Typed prices + **20/60/20** |
| 9 | https://hauzisha.co.ke/developments/forestview-residences/ | Hauzisha | portal | Elegant name; June 2027; price band — conf ≤2; **ignore 0730 phone** |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/forestview-residences-luxury-2-3-bedroom-apartments-in-westlands/ | Low-trust / AI — discovery seed only |
| https://www.elegantproperties.co.ke/our-portfolio | Name-only card (overlap with Featured) |
| https://www.flamingorealestate.co.ke/property/forestview-residences-luxury-apartments-in-westlands/ | Useful prices but payment % missing — overlap with CPK sheet |
| https://citiscapevaluers.com/property/forestview-residences-westlands/ | Price bands only; no payment |
| https://www.masterways.co.ke/properties/forestview-residences | Thin single-typology ask |
| https://www.buyrentkenya.com/listings/2-bedroom-apartment-for-sale-karura-4052584 | Overlaps Citiscape/Flamingo **27.1M** ranges; no payment % |
| BRES Property / social blurbs | Marketing only |

**sources_evaluated ~12 · sources_retained 9**

---

## 7. Open questions

1. Confirm **current** price list vs Elegant **29.5M** floor (retire or keep agent **27.1M** sheets).  
2. Obtain **official payment schedule** (LOO) — agent **20/60/20** needs a **4th** independent echo **or** developer page.  
3. Legal contracting entity / SPV for sale agreements.  
4. **Total units** / storeys / block count.  
5. Exact plot / GPS on Eldama Ravine Road.  
6. Resolve agent anomalies where some **3BR+DSQ** “from” prices sit **below** plain **3BR**.

---

## 8. Anti-merge

- **≠ Oasis Forest One** (different product / branding — do not merge forest-edge Westlands names).  
- **≠ Casa Karura** (Elegant Featured — 3&4BR private collection, from ~**44–88M**, completion **Nov 2029**).  
- **≠ Lofts @ Karura** (Elegant portfolio — **1&2BR loft-style** on Eldama Ravine, different product).  
- **≠ Oak & Ivy** (Elegant — **Loresho** gated 4&5BR homes; Ready-leaning inventory hold).  
- **≠ Forest One Residency** (separate Eldama Ravine listing family, from ~**KES 8.7M**, 1–3BR — not Elegant Forestview).  
- **≠ 48 Treehouse / Donyo Hill / Oakland Residences** (same developer, different sites/products).
