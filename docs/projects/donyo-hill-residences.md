---
slug: donyo-hill-residences
external_id: DISC-NBO-013
wave: elegant-2026-10-16
pilot: false
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-16
---

# Donyo Hill Residences (DISC-NBO-013) — discovery research

**Hauzisha inventory lead** (Elegant Properties). Corner **Donyo Sabuk Avenue × Peponi Road**, Westlands, **Elegant Properties**, off-plan / under construction, completion **end-2027 / December 2027** cluster.

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only — discovery / anti-merge note; prices/payment not used as public-canonical).

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.

**≠ Donyo Ridge** · **≠ Donyo Manor** · **≠ Spring Valley** mislabels — see **§8**.

**Contact lock:** Elegant sales = **`+254 700 004 449`** / **`info@elegantproperties.co.ke`**. **`0730 731 355` = Hauzisha only** — never attribute to developer.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Donyo Hill Residences** (official short: **Donyo Hill**) | 5 | elegantproperties.co.ke/donyo-hill; Featured-Properties; Hauzisha |
| `aliases` | secondary | Donyo Hill Residence; Donyo Hill Apartments | 4 | CPK; Calpha |
| `status` | **CANONICAL** soft | **Off-plan / under construction** — official construction-progress galleries **March 2025** + **November 2025** | 5 | elegantproperties.co.ke/donyo-hill |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Elegant; all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** (Peponi / Donyo Sabuk corridor; Karura Forest edge marketing) | 5 | Elegant; Hauzisha; CPK |
| `geography.street` | **CANONICAL** | Corner **Donyo Sabuk Avenue & Peponi Road** | 5 | Elegant project + Featured; Hauzisha copy |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-elegant-properties` | 5 | Official site; Hauzisha attribution; portfolio |
| `unit_types` | **CANONICAL** | **2 Bedroom**; **3 Bedroom**; **4 Bedroom** high-end apartments | 5 | Elegant; Featured; Hauzisha; CPK; Calpha |
| `size_by_type` | claim set — see table | Official band **2,450–5,920 sqft** (~**228–550 sqm**); typed agent sizes below | 5 / 3 | Featured (sqft); Hauzisha/CPK/Calpha (sqm) |
| `size_measure_tag` | soft | Official Featured publishes **sqft**; agents publish **sqm** — convert carefully (~10.76) | 4 | Featured vs CPK |
| `total_units` | unknown | — | 0 | not found |
| `building_specs.storeys` | secondary — **`needs_verification`** | **14**-storey (agent only) | 2 | CPK — **not** on Elegant pages this pass |
| `price_claims[]` | multi | See **§1a** — official “from” vs agent typed / portal band | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | Elegant; all |
| `payment_plan` | secondary — **must-have NOT met** | See **§1b** — no developer schedule; &lt;4 independent agents | 2 | CPK only typed schedule |
| `completion_estimate` | claim set | **End 2027** (CPK / Block echo) vs **December 2027** (Hauzisha) — year agrees | 3 / 3 | Agents/portal — **not** on Elegant Featured card this pass |
| `amenities` (official) | **CANONICAL** soft | Lavish bedrooms / large closets & bathrooms; very large balconies; large floor-to-ceiling heights & windows; designer Italian kitchens with in-built appliances; premium German sanitary fittings; grand entrance lobby with 24/7 security; panoramic rooftop terrace (Karura Forest views) | 5 | elegantproperties.co.ke/donyo-hill |
| `amenities` (agent denser) | secondary — **`needs_verification`** | Heated pool; gym + steam; jogging track; kids trampoline/playground; on-site café; entertainment hall; landscaped terrace; borehole; backup generator; CCTV | 2–3 | CPK; Hauzisha amenity chips |
| `roi_claim` | unknown | — | 0 | not found this pass |
| `legal_title` | unknown | Block “full title” / enquiry — **not retained as authority** | 0 | — |
| `inventory_note` | secondary portal | Hauzisha: **3** units available; **7** floor plans | 2 | Hauzisha |

### Size table (retained)

| Type | Official / Featured | Agent typed (sqm) | Role | Conf |
|------|---------------------|-------------------|------|-----:|
| Band (all) | **2,450–5,920 sqft** | **228–550** | Official Featured + Hauzisha span | 5 / 4 |
| 2 Bedroom | ~2,450 sqft entry | **228**; **236** | CPK; Calpha 228 @ 27.9M | 3 |
| 3 Bedroom | (within band) | **275**; **292**; **293**; **335** | CPK typed | 3 |
| 4 Bedroom | ~5,920 sqft top | **550** | CPK; Calpha | 3 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official “from” agrees** across Elegant project page + Featured (**KES 27.9M**). Agent typed matrices and Hauzisha portal band diverge — show all; resolve unit-level with Elegant sales / LOO.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 27.9M**; 2 / 3 / 4BR | Developer hub | elegantproperties.co.ke/donyo-hill | 5 | Official “from” |
| B | From **2,450–5,920 sqft**; from **Kshs 27.9m** | Featured card | elegantproperties.co.ke/Featured-Properties | 5 | Official size + from |
| C | Portal band **KES 29.9M – 70M**; copy still says “Starting from Ksh 27.9M” | Aggregator card | hauzisha.co.ke/developments/donyo-hill-residences/ | 2 | Band conflicts with A on floor; **`needs_verification`** |
| D | 2BR **228 from 28.9M** / **236 from 28.8M**; 3BR **275/38.5M**, **292/37.6M**, **293/35.7M**, **335/39.9M**; 4BR **550 from 69M** | Typed agent matrix | CPK main listing | 3 | Agent · **`needs_verification`** |
| E | 4BR **550 = KES 67M** (same agent family) | Unit listing | CPK 4BR page | 2 | Conflicts with D on 4BR · **`needs_verification`** |
| F | 2BR **228 = 27.9M**; 3BR **292 = 35M**; 4BR **550 = 67M** | Agent cards | Calpha Westlands archive + listing slugs | 3 | Aligns with A on 2BR from; 4BR aligns with E |

**Portal scalar:** none canonical. Prefer Elegant **27.9M from** for marketing floor; do not collapse typed agent rows.

### 1b. Payment plan — must-have **not met**

No instalment % on Elegant project / Featured / About this pass. Independent agents with a **typed** schedule: **CPK only** (same publisher across main + type pages). Block: “personalised … at enquiry” (not retained as authority). Hauzisha: generic staged language only.

| Element | Source | Status |
|---------|--------|--------|
| **20%** deposit · **60%** equal quarterly · **20%** on completion · completion end **2027** | CPK (main + 3BR + 4BR pages) | Secondary — single-agent family → **`needs_verification`** / **`needs_developer_input`** |
| Personalised plans at enquiry | Block.ke | Ignored as authority |
| “Staged across build; terms vary” | Hauzisha FAQ | Non-specific — not a schedule |

**Must-have gate:** developer schedule **absent** · independent agents with schedule **&lt;4** → payment **not** public-canonical this pass.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-elegant-properties` |
| `legal_name` | **Unknown** this pass (trading **Elegant Properties** / **Elegant Properties Kenya**; Companies Registry string not recovered) |
| `trading_names` | Elegant Properties; Elegant Properties Kenya |
| `website` | https://www.elegantproperties.co.ke/ |
| `evidence` | Project page + Featured + Portfolio + About (“over 30 years”; family-run); Hauzisha names Elegant |
| `group_company_id` | **null** — none invented |
| `sales_office` | Site contact: **+254 700 004 449**; **info@elegantproperties.co.ke** (project + About + Featured). Secondary Elegant line in seed/brochure corpus: **+254 731 286 286** (not on Donyo Hill page this pass). |
| `confidence` | **5** trading face / **0** legal SPV |

**Never** list **0730 731 355** / **+254 730 731 355** as Elegant — that number is **Hauzisha portal only**.

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Hauzisha | inventory portal / lead source | Development page; Elegant directory | 2 |
| CPK Real Estate | secondary agent | Typed prices + payment + amenities | 3 |
| Calpha Homes | secondary agent | Typed from-prices; Spring Valley title mislabel | 2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Hauzisha | Elegant attribution; Dec 2027; band 29.9–70M; 228–550 sqm |
| CPK Real Estate | Typed size/price matrix; 20/60/20; 14-storey claim; End 2027 |
| Calpha Homes | 27.9 / 35 / 67M typed cards; Spring Valley mislabel on 2BR title |
| Block.ke | Low-trust seed — end-2027 / Ridge anti-merge FAQ only (not authority) |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.elegantproperties.co.ke/donyo-hill | Elegant Properties | developer | Primary — location, from-price, amenities, UC progress |
| 2 | https://www.elegantproperties.co.ke/Featured-Properties | Elegant Properties | developer | Size band sqft + from 27.9m |
| 3 | https://www.elegantproperties.co.ke/about-us | Elegant Properties | developer | Trading face; **700 004 449** / email |
| 4 | https://www.elegantproperties.co.ke/our-portfolio | Elegant Properties | developer | Donyo Hill vs other Donyo / Peponi products |
| 5 | https://www.elegantproperties.co.ke/Launching-Soon-Properties | Elegant Properties | developer | **Donyo Manor** anti-merge (4BR from ~60M; Aug 2027) |
| 6 | https://hauzisha.co.ke/developments/donyo-hill-residences/ | Hauzisha | portal | Elegant; Dec 2027; band; **0730 731 355** portal-only |
| 7 | https://commercialpropertykenya.com/properties/donyo-hill-residence-spring-valley-westlands/ | CPK | agent | Typed prices; payment; 14-storey; Spring Valley title mislabel |
| 8 | https://calphahomes.co.ke/area/westlands/ | Calpha Homes | agent | 2/3/4BR from-prices; Spring Valley mislabel on 2BR card |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/donyo-hill-prestigious-2-3-4-bedroom-apartments-in-westlands/ | Low-trust / AI-prone — seed + Ridge FAQ only |
| CPK 3BR / 4BR unit pages (same publisher as #7) | Overlap reprints of CPK matrix / payment |
| Calpha individual `/property/donyo-hill-residence-…` slugs | Thin / empty extract this pass; archive card retained |
| https://www.flamingorealestate.co.ke/property/donyo-ridge-apartments/ | **Donyo Ridge** anti-merge only (≠ Hill) |
| Forestview Elegant brochure (mentions DONYO HILL in portfolio strip) | Thin — not Hill-specific specs |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. Confirm typed payment **20 / 60 quarterly / 20 completion** with Elegant sales / LOO (**`needs_developer_input`**).  
2. Legal contracting entity / SPV for LOO.  
3. Confirm **14** storeys and total unit count.  
4. Resolve Hauzisha band floor (**29.9M**) vs official from (**27.9M**) and CPK 4BR **67M vs 69M**.  
5. Exact GPS / LR number at Donyo Sabuk × Peponi.  
6. Featured card omits completion for Hill — confirm **Dec / end 2027** with developer.

---

## 8. Anti-merge

- **≠ Donyo Ridge** — separate Westlands scheme on Donyo Sabuk (agents: from ~**KES 16–17.5M**, completion **June 2029**, different unit sizes ~119–287 sqm). Not an Elegant Featured product this pass. Do not merge prices, payment (Ridge agents cite 10% + 10% quarterly), or completion into Hill.  
- **≠ Donyo Manor** — Elegant **Launching Soon**: **4BR only**, **4,553–5,295 sqft**, from **Kshs 60m**, Donyo Sabuk Avenue, completion **August 2027**. Different product from Hill’s 2/3/4BR from **27.9M**.  
- **≠ Spring Valley** — CPK listing title (“Spring valley Westlands”) and Calpha 2BR card (“Spring Valley Off Peponi Road”) are **agent mislabels**; canonical street is **Donyo Sabuk Avenue & Peponi Road, Westlands** per Elegant. Do not re-home the scheme to Spring Valley.  
- **≠ Golden Hill / other Donyo Sabuk Avenue products** (e.g. Skypeak Golden Hill) — different developer/scheme.  
- **≠** other Elegant Peponi / Karura products (Forestview, 48 Treehouse, Oakland, Casa Karura, Canopy Forest, Lofts @ Karura).
