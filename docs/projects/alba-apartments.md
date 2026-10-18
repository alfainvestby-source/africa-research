---
slug: alba-apartments
external_id: NBO-014
cycle: wave-c
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Alba Apartments (NBO-014) — Wave C research

CSV seed (unverified leads): location **Wanyee Road, off Naivasha Road, Dagoretti, Nairobi**; stage `off_plan`; completion **Q2 2026 (check status)**; `price_from_kes` **1,900,000**; sales_contact **Own It Kenya** (+254 722 716 182, sales@ownitkenya.com); developer **blank**.

Live research accessed **2026-10-16**. **No dedicated Alba Apartments project microsite** found this pass. Closest developer-brand stack = **albagarden.ke** (Alba Garden / Nanchang) — live fetches returned **500** this pass; searchable developer copy evaluated but **not retained** as a primary live cite. Commercial claims are overwhelmingly **agent/portal**.

**Method locks applied:**
- Developer vs agents: if developer known **and** developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official:** **do not assume** → **`needs_developer_input`**.
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **≥4 independent agent/portal sources** agree **or** any developer source.
- Agent-only / uncorroborated → **show** + **`needs_verification`**. CSV = unverified leads only.
- Seed **Own It Kenya = agent**, not developer (same trap as Misty Springs / other Own It CSV rows).

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** only when developer-backed sources **agree**. Here there is **no live developer price/LOO page** → commercial fields are mostly agent claim sets (conf ≤3). Hauzisha attributes the project to a named developer (portal-mediated).

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | secondary multi-source | Alba Apartments | 4 | Own It; Block; GNA; Hauzisha; multi-agent |
| `aliases` | secondary | Alba; Alba Apartments Dagoretti; Alba Apartments Riruta; Alba Apartment (singular) | 3 | Block; agents |
| `status` | claim set — **CONFLICT** · **`needs_verification`** | CSV `off_plan` / Q2 2026 check; many agents still sell with **completion Mar/Apr/Jan/Q3 2026**; **GNA** “Phase 1 ready for occupation”; **Block** “Newly built (2026) — move-in ready”; **Klin** status tags **Ready For Occupation** while copy still says April 2026 | ≤2 | See §7 |
| `geography.city` | secondary multi-source | Nairobi | 4 | all retained |
| `geography.neighbourhood_street` | secondary multi-source | **Wanyee Road**, off **Naivasha Road**, **Dagoretti** / **Riruta** (Dagoretti) | 4 | Own It; Block; GNA; CPK; Azipa; Hauzisha |
| `geography.landmark` | secondary | Near **The Junction Mall** (~2–5 min claims) | 3 | GNA; Musilli; Azipa; Ace (indexed) |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.297700, 36.754006** (`geo_method=geocode`) | 2 | Nominatim Wanyee Road Dagoretti 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **lead** — **`needs_verification`** | → `dev-nanchang-investment` (**proposed**, conf **3**) | 3 | Hauzisha development + developer hub (claims direct developer feed); search-indexed albagarden.ke/developer lists **Alba Apartments** under Nanchang interests (live site **500** this pass) |
| `unit_types` | secondary agent consensus | Studio; Junior 1 Bedroom (balcony inside/outside); 1 Bedroom (Big); 2 Bedroom (1 toilet / 2 toilets) — typed A–G on several agents | 3 | Own It; A-list; Klin; GNA; Azipa; Musilli; CPK; Block |
| `size_by_type` | secondary — Own It tags **plinth** on some rows | Studio **22–23 sqm**; Junior 1BR **31–32**; 1BR **40–46.5**; 2BR **53–61** (bands align across ≥4 agents) | 3 | Own It (plinth on selected); multi-agent |
| `size_measure_tag` | secondary (Own It only for explicit tag) | **Plinth** on Own It 40 / 46.5 / 54 / 56 / 61 sqm lines; other agents “sqm” unlabelled | 3 / 0 | Own It vs others |
| `total_units` | unknown | — | 0 | not published on retained sources |
| `building_specs.site_acres` | secondary agent consensus | **5.2 acres** | 3 | Own It; GNA; A-list; Klin; Musilli; CPK; Azipa (≥4) — **`needs_verification`** (no developer acreage page live) |
| `building_specs.phase1_blocks` | secondary agent consensus | Phase 1 = **two blocks** | 3 | Own It; GNA; A-list; Klin; Musilli; CPK; Azipa |
| `building_specs.storeys` | unknown | — | 0 | not found on retained sources |
| `price_claims[]` | claim set — **keep all**; no canonical | See **§1a** | ≤3 | |
| `currency` | secondary | KES | 5 | all commercial sources |
| `payment_plan.deposit` | secondary must-have (**≥4 agents**; no live developer %) | **20% deposit**; balance monthly/quarterly within completion period; optional **100% cash within 2 weeks** | 3 | Own It; A-list; Klin; Musilli×2; CPK — threshold **met via ≥4**; still **`needs_verification`** vs live LOO |
| `completion_estimate` | claim set — **CONFLICT** | **April 2026** (Own It, A-list body, Klin, Musilli-1, CPK body); **March 2026** (Hauzisha; Musilli-1 “Phase 1 March”; CPK detail line); **January 2026** (A-list footer); **Q3 2026** (Musilli-2); CSV **Q2 2026 check** | ≤2 | **`needs_verification`** / no developer-agreeing date |
| `amenities` (core agent consensus) | secondary | Swimming pool; gym; **2 high-speed lifts per block**; kids’ play; rooftop BBQ; backup generator; borehole; CCTV/security | 3 | Own It; GNA; A-list; Klin; Musilli; Azipa; Block (partial) |
| `amenities` | secondary soft | Block separates “confirmed” (security, generator, borehole, lift, parking, rooftop social, management) vs pool/gym/kids “referenced by developer — confirm” | 2 | Block only nuance |
| `construction_progress` | unknown | No developer tracker; status conflict substitutes | 0 | — |
| `availability_claim` | secondary | Hauzisha **3 units** listed; GNA/Block sale+rent inventory language | 2 | Hauzisha; GNA; Block — **`needs_verification`** |
| `legal_title` | unknown | Block: “to be confirmed at enquiry” | 0 | — |
| `rental_asks` | secondary (not purchase must-have) | Unfurnished studio from **~30k**/mo; 1BR **40–45k**; 2BR **50–55k** (GNA/Block) | 2 | GNA; Block rent twin |

### 1a. `price_claims[]` (always multi — no canonical scalar)

No live developer price list. Own It **1.9M** studio aligns with CSV and “cash/groundbreaking” agent offers; standard studio **from 2.3M** is the broader agent consensus. Hauzisha portal band **2.3M–5.4M** (caps below agent 6.2M 2BR).

| # | Claim (KES) | Unit / band | Source | Conf | Flags |
|--:|-------------|-------------|--------|-----:|-------|
| A | Studio from **1,900,000** (cash / groundbreaking) | Studio 22–23 sqm | Own It; Klin; Musilli-1; CSV | 3 | Cash-special framing · **`needs_verification`** as current |
| B | Studio from **2,300,000** | Studio 22–23 sqm | A-list; Klin; GNA; Azipa; Block; Musilli-2; Hauzisha from; CPK | 3 | Multi-agent “standard from” |
| C | Junior 1BR from **3,100,000** (inside/outside balcony) | 31–32 sqm | Own It; A-list; Klin; GNA; Azipa; Musilli | 3 | |
| D | 1BR (40–46 sqm) from **~3.6M–4.5M**; typed **4.0M** / **4.47M** (46.5) | Big 1BR | Own It (4.0 / 4.47 plinth); A-list; Klin; GNA; Azipa; CPK; Block | 3 | Floor-dependent language on Klin/Musilli |
| E | 2BR from **5.36M / 5.64M / 6.2M** | 53–54 / 56 / 61 sqm | Own It; A-list; Klin; GNA; Azipa; Musilli; CPK; Block | 3 | |
| F | Hauzisha portal range | **2.3M – 5.4M** (3 units) | hauzisha.co.ke | 3 | Portal “developer feed” claim; upper band **below** agent 6.2M → conflict soft |
| G | CSV seed | `price_from_kes` **1,900,000** | seed | Unverified lead (matches cash studio claim A) |

**Canonical price:** none. Keep all rows.

### Payment plan — ≥4-source recount

| Element | Agreeing independent sources | Count | Threshold (≥4 or developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **20% deposit** + balance monthly/quarterly to completion | Own It; A-list; Klin; Musilli (both pages); CPK | **≥5** | **Met via ≥4 agents** | Must-have at conf **3**; **`needs_verification`** vs LOO (no developer % page live) |
| **100% cash within 2 weeks** | Own It; A-list; Klin; Musilli; CPK | ≥4 | Met as agent consensus | Secondary cash path |
| Developer LOO / brochure PDF | Not fetched / not found live | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-nanchang-investment` (**proposed**) |
| `legal_name` | **Nanchang Investment Company Limited** (as named by Hauzisha; search-indexed albagarden.ke) |
| `trading_names` | Nanchang Investment; Alba brand family (Alba Garden / Alba Apartments) |
| `website` | No live Alba Apartments microsite. Brand/corporate pages at **albagarden.ke** (500 this pass) |
| `evidence` | Hauzisha development page “by Nanchang Investment Company Limited” + developer hub (operating Nairobi since 2011; parent **Nanchang Foreign Engineering Company (K) Limited**). Search-indexed albagarden.ke/developer lists **Alba Apartments** under “Our Interests” alongside Alba Garden and Nanchang Hotel Westlands |
| `group_company_id` | → `grp-nanchang-foreign-engineering` (**proposed parent**, conf **2–3**) — portal + indexed brand copy only |
| `csv_name_note` | CSV developer blank; CSV sales_contact **Own It ≠ developer** |

**Developer confidence capped at 3** (portal attribution + indexed brand site; no live developer commercial/LOO stack agreeing on prices). Do **not** treat Own It, Block, CPK, or GNA as developers.

---

## 3. GroupCompany

| Field | Value |
|-------|-------|
| `id` | `grp-nanchang-foreign-engineering` |
| `name` | Nanchang Foreign Engineering Company (Kenya) Limited / Nanchang Foreign Engineering Company (K) Limited |
| `website` | Presented via albagarden.ke (unreachable live this pass) |
| `evidence` | Hauzisha developer hub: parent company partnership. Indexed albagarden.ke: incorporated **2010**; NCA category claims (Building / Civil / Electrical / Mechanical) — **credentials unverified** this pass |

Parent link = **proposed** (conf ≤3). Kenya Law judgment naming Nanchang Foreign Engineering Company Limited exists historically but is **not** used here as property evidence for Alba Apartments.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Notes |
|------|-------------------|----------|-------|
| **Alba Garden** (Kilimani, Kasuku Lane / Lenana Rd) | related_brand_project | Indexed albagarden.ke; FAQ acreage **1.12 acres** Kilimani | **Different asset** from Wanyee/Dagoretti Alba Apartments — do not merge |
| Own It Kenya | marketing_agent | CSV + Own It off-plan page | Agent only |

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Own It Kenya | agency | CSV sales_contact; off-plan roundup with plinth sizes + 20% | https://ownitkenya.com/off-plan-apartments-for-sale-in-nairobi/ |
| Hauzisha | portal | Developer attribution; Mar 2026; 2.3–5.4M; 3 units | https://hauzisha.co.ke/developments/alba-apartments/ |
| Block Real Estate | agency | Sale listing; newly built / move-in framing; price table | https://block.ke/property/alba-apartments-riruta-studios-1-2-bed-from-kes-2-3m/ |
| GNA Real Estate | agency | Phase 1 ready; sale + rent asks | https://gna.co.ke/project/alba-apartments-dagoretti-studios-one-and-two-bedrooms/ |
| A-list Real Estate | agency | Typed A–G prices; 20%; Apr vs Jan conflict | https://a-listrealestate.ke/property/alba-apartments/ |
| Klin Properties | agency | 1.9M cash offer; 20%; Ready For Occupation tag | https://klinproperties.co.ke/property/realestate/ |
| CPK Real Estate | agency | 20%/100% plan; price table; Kilimani title vs Dagoretti body | https://commercialpropertykenya.com/properties/alba-apartments-affordable-housing-in-kilimani/ |
| Musilli Homes | agency | Two pages (Apr/Mar vs Q3 2026) | https://musillihomes.co.ke/property/alba-apartments/ · https://musillihomes.co.ke/property/alba-apartments-2/ |
| Azipa Real Estate | agency | Typed A–G prices; amenities | https://aziparealestate.co.ke/property/alba-wanyee-road-dagoretti/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 722 716 182 | Agent: Own It (CSV) |
| phone | +254 720 469 282 | Agent: Own It |
| email | sales@ownitkenya.com | Agent: Own It (CSV) |
| phone | +254 730 731 355 | Portal: Hauzisha |
| phone | +254 725 937 686 | Agent: Block |
| email | loyd@block.ke | Agent: Block |
| phone | +254 712 406 060 / +254 782 406 060 | Agent: GNA |
| email | support@gna.co.ke | Agent: GNA |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 721 687 339 | Agent: Klin |
| email | propertiesklin@gmail.com | Agent: Klin |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 729 678 773 | Agent: Musilli |
| phone | +254 742 880 335 / +254 796 007 755 | Agent: Azipa |
| email | azipahomes@gmail.com / info@aziparealestate.co.ke | Agent: Azipa |
| phone | +254 735 939 999 / +254 799 000 222 | Indexed brand site albagarden.ke (developer office — **live page 500 this pass**) | Brand / developer lead |

---

## 6. Stakeholders

None named on retained live sources this pass (no architect / contractor / financier on agent pages). Indexed albagarden.ke NCA parent claims → **not** promoted to Stakeholder without live corroboration.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Status / readiness** | Off-plan / completion 2026 dates **vs** GNA Phase 1 ready **vs** Block newly built move-in **vs** Klin Ready For Occupation | Claim set · **`needs_verification`**. No developer status page agreeing. |
| 2 | **Completion date** | Apr 2026 · Mar 2026 · Jan 2026 (A-list footer) · Q3 2026 (Musilli-2) · CSV Q2 2026 | Claim set · **`needs_verification`**. No canonical. |
| 3 | **Studio from-price** | Cash **1.9M** (Own It/Klin/Musilli/CSV) **vs** standard **2.3M** (multi-agent + Hauzisha from) | Keep both in `price_claims[]`. |
| 4 | **Hauzisha max vs agent 2BR** | Portal **to 5.4M** **vs** agents **to 6.2M** | Keep both; inventory may differ. |
| 5 | **CPK title “Kilimani”** | URL/title Kilimani **vs** body Dagoretti/Wanyee | Geography = Dagoretti/Riruta from multi-source body; Kilimani title = labeling error · **`needs_verification`** only if someone treats title as geo |
| 6 | **A-list internal dates** | Body **April 2026** **vs** footer **January 2026** | Same publisher conflict · **`needs_verification`** |
| 7 | **Musilli pages** | Page 1 Apr/Mar **vs** Page 2 **Q3 2026** | Same agency conflict · show both |
| 8 | **CSV Own It** | Seed contact ≠ developer | Split Contact.owner; Own It is agent |
| 9 | **Alba Garden vs Alba Apartments** | Same Nanchang brand family; different sites (Kilimani vs Dagoretti) | RelatedParty / related project only |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 candidates (Own It off-plan, Hauzisha development, Hauzisha developer hub, Block sale, Block rent twin, GNA, A-list, Klin, CPK, Musilli×2, Azipa, Ace 404, Austine 404, albagarden.ke 500, 2Talk 500, CSV). No live developer project microsite. Retained 10 densest field-bearing live pages.

**Thin / skipped (not in retained list):**
- https://block.ke/property/alba-apartments-riruta-studio-1-2-bed-units-to-rent-from-kes-30k/ — rent twin of retained Block sale page
- https://www.acerealtorsltd.com/...Alba-Apartments... — **404** this pass (search-indexed only)
- https://austinerealtors.co.ke/alba-apartment-in-naivasha-road-nairobi-studio-1-2-bedroom/ — **404**
- https://2talkkenya.com/property/alba-apartments-studios/ — **500** this pass
- https://albagarden.ke/developer/ · https://albagarden.ke/faq.php — **500** this pass; search-indexed copy used for developer lead notes only, **not retained** as live primary cite
- CSV NBO-014 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://ownitkenya.com/off-plan-apartments-for-sale-in-nairobi/ | Own It Kenya | agent | 2026-10-16 | CSV channel; 1.9M; plinth sizes; 20%; April 2026; 5.2 acres / 2 blocks |
| 2 | https://hauzisha.co.ke/developments/alba-apartments/ | Hauzisha | portal | 2026-10-16 | **Nanchang Investment Company Limited**; Mar 2026; 2.3–5.4M; 3 units |
| 3 | https://hauzisha.co.ke/developers/nanchang-investment-company-limited/ | Hauzisha | portal | 2026-10-16 | Parent **Nanchang Foreign Engineering (K)**; since 2011 |
| 4 | https://block.ke/property/alba-apartments-riruta-studios-1-2-bed-from-kes-2-3m/ | Block Real Estate | agent | 2026-10-16 | Newly built / move-in; price table; amenity confirm nuance |
| 5 | https://gna.co.ke/project/alba-apartments-dagoretti-studios-one-and-two-bedrooms/ | GNA Real Estate | agent | 2026-10-16 | Phase 1 ready; sale + rent |
| 6 | https://a-listrealestate.ke/property/alba-apartments/ | A-list Real Estate | agent | 2026-10-16 | Typed prices; 20%; Apr vs Jan conflict |
| 7 | https://klinproperties.co.ke/property/realestate/ | Klin Properties | agent | 2026-10-16 | 1.9M cash; 20%; Ready For Occupation tag |
| 8 | https://commercialpropertykenya.com/properties/alba-apartments-affordable-housing-in-kilimani/ | CPK Real Estate | agent | 2026-10-16 | 20%/100%; price table; Kilimani title vs Dagoretti body |
| 9 | https://musillihomes.co.ke/property/alba-apartments/ | Musilli Homes | agent | 2026-10-16 | 1.9M cash; Apr/Mar completion language |
| 10 | https://musillihomes.co.ke/property/alba-apartments-2/ | Musilli Homes | agent | 2026-10-16 | **Q3 2026** conflict; 2.3M from; same payment plan |

**Also evaluated (Azipa denser amenities/location — overlaps retained price tables):** https://aziparealestate.co.ke/property/alba-wanyee-road-dagoretti/ — corroboration for A–G types; not counted above to keep retained = 10 densest distinct claims (Musilli conflict pair prioritized).

---

## 9. Field harvest

| Field | Alba Apartments status | Notes for living schema |
|-------|------------------------|-------------------------|
| canonical_name / aliases | OK | Riruta alias useful |
| status | Claim set + strong conflict | Ready vs off-plan / 2026 dates |
| geography street | OK multi-agent | Wanyee / Naivasha / Dagoretti–Riruta |
| primary_developer | Lead conf 3 | Nanchang Investment; Own It ≠ developer |
| GroupCompany | Proposed parent | Nanchang Foreign Engineering (K) |
| unit_types / sizes | OK agent consensus | Own It **plinth** tags on some rows |
| `total_units` / storeys | unknown | Gap vs Berkeley/Galaxy harvest |
| `price_claims[]` | All options A–G | 1.9M cash vs 2.3M standard |
| `payment_plan` | **20%** via ≥4 agents | Conf capped 3 — no developer % |
| amenities core | OK agent cluster | Block soft-flags pool/gym/kids |
| completion_estimate | Conflicted claim set | Apr/Mar/Jan/Q3/Q2 |
| Related Alba Garden | Capture | Do not merge with NBO-014 |
| CSV Own It trap | Documented | Process note (Wave C Own It rows) |

### Proposed schema bumps (for coordinator — not auto-locked)

| Proposed extension | This project | Consensus note |
|--------------------|--------------|----------------|
| Explicit `phase` / `phase1_block_count` | **Yes** (Phase 1 = 2 blocks) | When multi-phase agent copy repeats |
| Cash-special vs instalment dual `price_claims` | **Yes** (1.9M cash vs 2.3M) | Aligns Galaxy/Porini dual-column lesson |
| Status ready-vs-off-plan claim set | **Yes** | Same stress as Misty Springs |
| Own It CSV contact = agent (never developer) | Process lock reinforce | Wave C Own It cohort |
| Brand-family RelatedParty (Alba Garden) | Capture | Parallel assets under Nanchang |

---

## Open questions (developer / advocate input)

1. Confirm legal developer **Nanchang Investment Company Limited** for the Wanyee Road scheme; publish a live project page / LOO.
2. Is Phase 1 **complete / OC issued**, or still off-plan to **Mar/Apr/Q3 2026**?
3. Binding studio pricing: cash **1.9M** vs standard **2.3M**; full typed list through 2BR **6.2M**.
4. Binding deposit % and instalment schedule (agents say **20%**).
5. Total unit count, storeys, and approved plans / NEMA / title docs.
6. Which amenities are operational vs marketing (pool/gym/kids per Block caveat)?
7. Relationship of **Alba Garden** (Kilimani) sales contacts (+254 735 939 999) to Alba Apartments Dagoretti sales.
