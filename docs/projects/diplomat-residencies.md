---
slug: diplomat-residencies
external_id: DISC-NBO-022
wave: hauzisha-b-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-17
---

# Diplomat Residencies / Diplomat Residences (DISC-NBO-022) — discovery research

**Hauzisha Wave B** ([hauzisha-developers-2026-10-16.md](../discovery/hauzisha-developers-2026-10-16.md)). **Peponi Road**, Westlands (steps from Westgate Mall), **Wonder Properties**, off-plan / under construction, completion claim cluster **March / Q1–Q2 2028** vs agent **December 2027**.

Live research accessed **2026-10-17**. Official microsite **https://diplomat.wonderpropertykenya.com/** returned **502** this pass — claims from **indexed developer copy** + **official brochure PDF** (same host; HTTP 200). **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never Wonder.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **Off-plan / UC** only (**not** Ready).

**≠** Gaia Brookside; **≠** Hephé Palace; **≠** Forestview / 48 Treehouse / other Peponi schemes — see **§8**.

**`inventory_class`:** **`building`** (Space Kenya verified UC footage **Apr–Nov 2025**; agents also market off-plan sales). Not Ready-tagged.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Diplomat Residences** (microsite title / H1); Hauzisha + many agents use **Diplomat Residencies** — same scheme | 5 / 4 | diplomat.wonderpropertykenya.com (indexed); brochure “The Diplomat”; Hauzisha |
| `aliases` | secondary | Diplomat Residencies; The Diplomat; Diplomat Residency; Diplomatic Residences (search noise) | 4 / 2 | Hauzisha; Ravi; Almasi FAQ; GNA |
| `status` | **CANONICAL** soft | **Off-plan / under construction** — Space Kenya UC footage **Apr–Nov 2025**; agents “off-plan”; **not Ready** | 4 | Space Kenya; Almasi; Vorsa; Hauzisha (no Ready tag) |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Microsite; brochure; all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** | 5 | Microsite; brochure; Hauzisha |
| `geography.street` | **CANONICAL** | **Peponi Road** (marketing: steps / ~30 m from **Westgate Mall**) | 5 | Microsite; brochure; GNA; Ravi |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-wonder-properties` (lead / trading **Wonder Properties** / **Wonder Properties Kenya**) | 5 | Microsite Team; brochure “Wonder Properties”; Hauzisha |
| `unit_types` | **CANONICAL** soft | **1 Bedroom** (incl. mini / studio-labelled **43 sqm** on portals); **2 Bedroom** — official copy says “1 and 2-bedroom”; Hauzisha adds **Studio** | 5 / 3 | Microsite; Hauzisha Studio chip — **`needs_verification`** vs developer typology labels |
| `size_by_type` | claim set — agent | See size table — **43–142 sqm** band; **no sizes on official brochure/microsite** this pass | 3 | Almasi; Vorsa; GNA; Ravi; Hauzisha |
| `total_units` / storeys | secondary | Agents: **25** floors / storeys; Almasi availability widget claims **875** residences — **implausible / unverified** | 3 / 1 | GNA; Ravi; Space Kenya; Almasi — **`needs_verification`** |
| `building_specs` | secondary | Hotel-managed / hospitality-operated residences (unnamed operator); smart home; modern elevators; power + water backup; borehole | 4 | Microsite; brochure |
| `price_claims[]` | multi | See **§1a** — **no official price list** this pass | — | — |
| `currency` | **CANONICAL** soft | **KES** | 4 | Agents; Hauzisha |
| `payment_plan` | secondary — **must-have met** (≥4 agents) | See **§1b** — **20%** min deposit + balance during build / ~3 years; **not** on developer materials → **`needs_verification`** vs Wonder LOO | 3 | Almasi; Vorsa; GNA; Ravi; Knight Frank |
| `completion_estimate` | claim set — official silent | **March 2028** (Hauzisha; Almasi; Vorsa; Palmier; Block) vs **Q1 2028** (Ravi) vs **Q2 2028** (GNA; Space Kenya) vs **December 2027** (Knight Frank) | 3 / 2 | Agents — **`needs_verification`**; no date on brochure/microsite |
| `amenities` | **CANONICAL** soft | Rooftop pool / Sky Club; rooftop restaurant / café; fitness centre; wellness spa; yoga lounge; children’s playground; meeting rooms; residence lounge; concierge; courtyard garden; padel / tennis courts; ample parking; 24/7 security; smart home; heated water; borehole; power backup | 5 | Microsite amenities; brochure |
| `roi_claim` | secondary marketing | Ravi “**12–15%** annually” yield — agent only | 2 | Ravi — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Peponi scheme (Wonder portfolio peer of Gaia / Alina — not same site) | — | — |

### Size table (agent — official silent)

| Type / label | Size | Role | Conf |
|--------------|-----:|------|-----:|
| Mini 1BR / Studio / Type A | **43 sqm** | Agent + Hauzisha band floor | 3 |
| 1BR Type B | **52 sqm** | Multi-agent | 3 |
| 1BR Type C | **76 sqm** | Multi-agent; some mark **sold out** | 3 |
| 1BR Type D | **88 sqm** | Multi-agent; GNA marks **sold out** | 3 |
| 2BR Type E | **113 sqm** | Multi-agent | 3 |
| 2BR Type F / executive | **142 sqm** (one KF card also **139 sqm**) | Multi-agent; some mark **sold out** | 3 |
| Hauzisha size band | **43–142 sqm** | Portal | ≤2 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official:** microsite + brochure **do not publish** unit prices this pass → all floors are **agent / portal**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 5.0M** (43 sqm mini 1BR); typed bands **5.0–5.9M / 6.1–7.2M / 10.3–12.2M / 13.2–15.7M**; **76** & **142** sold out | Typed card + availability | Almasi Realty | 3 | Dense; sold-out flags **`needs_verification`** |
| B | 43 **from 5.0M**; 52 **6.1M**; 76 **9.0M**; 88 **10.3M**; 113 **13.2M**; 142 **16.7–19.2M** | Typed “from” sheet | Vorsa Group | 3 | 76 still priced (≠ Almasi sold-out) |
| C | Hero **from 5.5M**; mini **5.5–6.55M**; 52 **6.75–8M**; 76 & 88 & 142 **sold out**; 113 **14.6–17.3M** | Updated card | GNA Real Estate | 3 | Higher floors than A/B; stock flags conflict |
| D | Type A–F: **5M / 6.1M / 9M / 10.3M / 13.2M / 16.7M** with ups to **5.9 / 7.2 / 10.6 / 12.2 / 15.7 / 19.2M** | Typed + “available” | Ravi Homes | 3 | Aligns shape with B |
| E | Studio **43 from 5M**; 1BR **52 from 6.1M**; 2BR **113 from 13.3M**; completion **Mar 2028** | Compressed card | Palmier Properties | 3 | Thin mix |
| F | Portal band **KES 5.0M – 13.3M**; sizes **43–142**; **2** units available; **Mar 2028** | Development hub | Hauzisha | ≤2 | Aggregator; phone is portal |
| G | Typed **5M / 6.1M / 9M / 10.3M / 13.2M / 16.7M** (+ Type F **139 from 19.46M**); completion **Dec 2027** | Agent sheet | Knight Frank (BW) | 3 | **Completion outlier** |
| H | From **KES 5M**; range to **16.7M**; **Mar 2028**; 20% deposit | Aggregator | block.ke | ≤2 | Discovery only — **not authority** |

**Portal scalar:** none. Do not promote a single “from” until Wonder publishes a list or LOO.

### 1b. Payment plan — must-have **met** (≥4 independent agents); structure **not** developer-locked

No instalment schedule on Wonder microsite or brochure this pass.

| Element | Source | Status |
|---------|--------|--------|
| Minimum **20%** deposit; balance over construction / until handover | Almasi; Vorsa; GNA; Ravi; Knight Frank | Secondary consensus (conf **3**) — **`needs_verification`** vs Wonder LOO |
| Balance “over up to **three years**” / “spread over **3 years**” | Almasi; Vorsa | Variant vs “until completion” wording |
| Balance “within remaining construction period” / “flexible instalments” | GNA; Ravi; Knight Frank | Same deposit; softer schedule |
| Official Wonder payment schedule | — | **Not published** this pass |
| Block.ke 20% + calculator | block.ke | Illustrative — ignore as authority |

**Must-have met?** **Yes** (agent threshold) — still flag **`needs_verification`** until developer schedule / LOO.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-wonder-properties` (trading; Hauzisha lead `dev-lead-wonder-properties` until seed promote) |
| `legal_name` | **Unknown** this pass (trading **Wonder Properties** / **Wonder Properties Kenya**; Companies Registry string not recovered) |
| `trading_names` | Wonder Properties; Wonder Properties Kenya |
| `website` | https://www.wonderpropertykenya.com/ · project microsite https://diplomat.wonderpropertykenya.com/ |
| `evidence` | Microsite Team block; brochure “Brought to life by Wonder Properties” + contact page; Hauzisha developer attribution; portfolio peers named on microsite (Alina Harbour, Alina Ridge, Gaia Brookside) |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts | **Kirichwa Rd, Westlands**; **+254 116 126 666** (microsite Team + brochure); brochure also **+254 702 818 888**, **+254 792 696 666**, **+254 701 818 888**; **info@wonderpropertykenya.com** (microsite) |
| `confidence` | **5** trading face / **0** legal SPV |

**Verified Wonder phones this pass:** **+254 116 126 666**, **+254 702 818 888**, **+254 792 696 666**, **+254 701 818 888**. Email **info@wonderpropertykenya.com**.

**Never** assign **0730 731 355 / +254 730 731 355** to Wonder — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Unnamed “renowned hospitality group” | operator / hotel_manager (marketing) | Microsite + brochure “managed by a renowned hospitality group” | 2 — name unknown — **`needs_verification`** |
| Almasi / Vorsa / GNA / Ravi / Palmier / Knight Frank | selling agents | Independent listing pages | 3 |
| Hauzisha | portal / discovery | Development + developer hubs | ≤2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Almasi Realty | Densest typed prices + sold-out flags; **20% / ~3 yr**; Mar 2028; availability widget (treat unit totals as weak) |
| Vorsa Group | Typed 5.0M+ sheet; **20% / 3 years**; Mar 2028 |
| GNA Real Estate | Higher “from” floors; stock sold-out flags; **20%**; Q2 2028; **25** floors |
| Ravi Homes | Typed A–F card; **20%**; Q1 2028; **25** floors; yield claim |
| Palmier Properties | Thin 5 / 6.1 / 13.3M; Mar 2028 |
| Knight Frank | Typed sheet; **20%**; **Dec 2027** outlier |
| Space Kenya | UC footage Apr–Nov 2025; Q2 2028 editorial; cites Wonder microsite |
| Hauzisha | Wonder attribution; 5.0–13.3M; Mar 2028 — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://diplomat.wonderpropertykenya.com/ | Wonder Properties | developer | Primary narrative (indexed **2026-10-17**; live **502** this pass); Peponi; 1&2BR; amenities; Team contacts **116 126 666** + info@ |
| 2 | https://diplomat.wonderpropertykenya.com/static/documents/brochure.pdf | Wonder Properties | brochure | The Diplomat; Peponi; amenities; Westgate adjacency; contacts **116 / 702 / 792 / 701**; **no prices / completion date** |
| 3 | https://hauzisha.co.ke/developments/diplomat-residencies/ | Hauzisha | portal | Wonder; Studio/1/2BR; 43–142; **5.0–13.3M**; Mar 2028 — conf ≤2; **ignore 0730 phone** |
| 4 | https://space.ke/projects/diplomat/ | Space Kenya | editorial / UC media | UC footage **Apr–Nov 2025**; **25**-storey; Q2 2028; cites Wonder microsite |
| 5 | https://almasirealty.com/property/diplomat-residences/ | Almasi Realty | agent | Densest typed prices + payment + Mar 2028 |
| 6 | https://vorsagroup.co.ke/property/diplomat-residences-1-2-bedroom-apartments-in-westlands/ | Vorsa Group | agent | Typed prices; **20%/3yr**; Mar 2028 |
| 7 | https://gna.co.ke/project/diplomat-residencies-westlands-1-and-2-bedrooms/ | GNA Real Estate | agent | Price/stock variant; **20%**; Q2 2028; 25 floors |
| 8 | https://ravihomes.co.ke/developments/diplomat-residency/ | Ravi Homes | agent | Typed A–F; **20%**; Q1 2028; Wonder portfolio echo |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/diplomat-residencies-the-pinnacle-of-westlands-living/ | Low-trust / AI — discovery seed only |
| https://www.bw.knightfrank.com/properties/residential/for-sale/westlands-peponi-road/hub2536851 | Useful **Dec 2027** conflict + typed prices; thinner than Almasi/Vorsa for retention budget — conflict noted in §1 |
| https://new.palmierproperties.co.ke/estate_property/the-diplomat-peponi-road-westlands/ | Thin price card; overlaps Palmier row in claims |
| https://www.wonderpropertykenya.com/ (and /about /contact /projects) | SPA shell this pass — no extractable Diplomat fields beyond brand host |
| https://hauzisha.co.ke/developers/wonder-properties/ | Developer directory lead; Diplomat name-only card (detail page retained) |
| CPK investment-guide name-drop | Marketing list only — no Diplomat price page |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. Obtain **official price list** / LOO (developer silent this pass) — resolve agent **5.0M vs 5.5M** floors and sold-out conflicts.  
2. Confirm **completion** — **Mar / Q1–Q2 2028** cluster vs Knight Frank **Dec 2027**; official date unpublished.  
3. Lock **payment schedule** vs agent **20% + build-period / 3-year** variants.  
4. Legal contracting entity / SPV; name of hospitality **operator**.  
5. **Total units** / exact storeys (reject or confirm Almasi **875** claim).  
6. Exact plot / GPS on Peponi Road; Studio vs mini-1BR labelling.  
7. Re-fetch live microsite when **502** clears — confirm indexed copy still current.

---

## 8. Anti-merge

- **≠ Gaia Brookside** — same Wonder developer; **Brookside Gardens Dr**; **3/4/5BR** from ~**25–45M**; Hauzisha completion **June 2028** cluster — different scheme.  
- **≠ Hephé Palace** — Sequoia; **Ring Road Westlands** / Oval / Kingfisher; studio–3BR+DSQ from different price band; Sep/Q3 **2028**.  
- **≠ Forestview Residences** — Elegant; **Eldama Ravine**; 2&3BR from ~**29.5M**; June **2027**.  
- **≠ 48 Treehouse** — Elegant; Peponi / Karura; **48×4BR** from ~**77.9M**; Dec **2027**.  
- **≠ Donyo Hill Residences** — Elegant; Donyo Sabuk × Peponi; 2/3/4BR from ~**27.9M**.  
- **≠ Oakland Residences / Casa Karura / Lofts @ Karura** — other Elegant Peponi / Karura products.  
- **≠ “Karura Forest Views”** — Block-only / likely AI alias clustering forest language onto Hephé and other Peponi products.  
- **≠ Alina Harbour / Alina Ridge / Alina Valley / Executive Suite** — Wonder portfolio peers, different sites/products.
