---
slug: kings-summit-nakuru
external_id: NAK-001
geography_scope: rift-valley / nakuru
cycle: discovery-research
pilot: false
wave: discovery
sources_evaluated: 13
sources_retained: 10
last_verified_at: 2026-10-16
---

# Kings Summit (NAK-001) — Nakuru / discovery research

**New geography:** Milimani, **Nakuru** (Rift Valley) — first Nakuru dossier in the corpus. Not in Nairobi seed CSV.

Discovery lead: [`kenya-offplan-leads.md`](../discovery/kenya-offplan-leads.md) — Kings Developers Ltd; under construction / sold off-plan; URLs: kingsdevelopers.com/projects/ · RealtorKenya listing.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume a winner** → flag **`needs_developer_input`**; no canonical until a later verification pass.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- Payment must-have if any developer source **or** ≥4 agent sources. Agent-only / uncorroborated → **`needs_verification`**.
- Unproven brand/parent: only set **GroupCompany** when evidenced (here: Royal Group on developer about + group site).
- Discovery lead URLs = discovery only until corroborated in this pass.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Kings Summit | 5 | kingsdevelopers.com/project/kings-summit_49/; milimani location; projects hub |
| `aliases` | secondary | Kings Summit View; Kings Summit Apartments | 3 | Craiova; Jumuika; KPC snippets |
| `status` | **CANONICAL** (developer badge) | **Under-Construction**; sold **off-plan** with flexible payment plans | 5 | milimani-nakuru UC badge; project page; RealtorKenya (posted by Kings Developers Ltd) |
| `geography.city` | **CANONICAL** | Nakuru | 5 | developer; all |
| `geography.county` | **CANONICAL** | Nakuru County (Rift Valley) | 5 | context + developer Nakuru materials |
| `geography.neighbourhood` | **CANONICAL** | Milimani (agents: **Lower Milimani**) | 5 / 3 | developer Milimani; Craiova Lower Milimani |
| `geography.street` | secondary — **needs_verification** | **Maragoli Road**, Lower Milimani (Craiova). KPC/search: “Near Alps Hotel”, Nakuru East — agent labels | 2 | Craiova; KPC snippet |
| `geography.lat_lng` | geocode — **needs_verification** | **−0.263170, 36.078867** (`geo_method=geocode`) | 2 | Nominatim Maragoli Road Milimani Nakuru 2026-10-16 (Craiova-only street NV) — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-kings-developers-ltd` | 5 | project page; aboutus; milimani location; RealtorKenya |
| `unit_types` | **CANONICAL** | **3 Bedroom** only marketed on developer Summit pages | 5 | project page; location card |
| `bathrooms` | **CANONICAL** | **2** | 5 | project page |
| `size_by_type` | **CANONICAL** (band agree) | **120 sqm** (≈ **1,300 sq ft** on same page) | 5 | project page; RealtorKenya; agents |
| `size_measure_tag` | secondary | Craiova: **“Plinth area : 120 sqm”** — tag **plinth** (agent). Developer does not label gross vs plinth | 3 | Craiova |
| `total_units` | unknown | Not published this pass | 0 | — |
| `building_specs.storeys` | secondary — **needs_verification** | Agents: **13 floors** / “13-floor tower”. **Not** on developer Summit page this pass | 2 | Craiova; Jumuika; KPC snippet |
| `building_specs.blocks` | soft | “2 high-speed elevators **per block**” implies ≥1 block; block count unknown | 2 | developer key features |
| `price_claims[]` | claim set — **`needs_developer_input`** on dual official “from” | See §1a — no scalar | ≤3 | |
| `currency` | **CANONICAL** | KES / Ksh | 5 | all |
| `payment_plan` | soft developer | **Flexible off-plan** instalments during construction (project page; about “flexible payment plans”) | 4 | project; aboutus |
| `payment_plan.deposit` | secondary — portfolio / agents — **needs_verification** for Summit binding % | Developer diaspora page: “as little as **10%** down” (portfolio financing, not Summit-specific). Agents: **20%** deposit (Craiova; Jumuika; KPC copy) — **&lt;4 independent** agencies this pass | ≤3 | diaspora; agents |
| `completion_estimate` | secondary — **needs_verification** | Developer Summit page: **no date**. Agents: **Last Quarter 2026** (Craiova Summit) **vs December 2026 / early 2027** (Craiova twin + Jumuika) | 2 | agents only |
| `amenities` (core) | **CANONICAL** | Solar street lighting; 1 parking per apartment; 24h controlled-access security + boundary wall; balcony with lake view; backup generator (common areas); branded fixtures; **2 high-speed elevators per block**; cabro driveways; borehole; anti-termite foundation; water storage; retail shops within complex | 5 | project key features; RealtorKenya echoes |
| `amenities` | secondary / inflated — **needs_verification** | Heated pool; gym; kids play; community hall; green landscaping — on agent pages, **not** on developer Summit key-features list this pass | 1 | Craiova; Jumuika |
| `showhouse` | secondary | Craiova: **showhouse ready** | 2 | Craiova |
| `legal_title` | unknown | — | 0 | not found |
| `investment_return_claims` | marketing only | Diaspora/blog appreciation language — **not** verified yields | 0 | — |

### 1a. Price claims — keep **all** options (no canonical scalar)

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Project + location + projects hub “From” | **Ksh 9,000,000** | kingsdevelopers.com/project/kings-summit_49/; /location/milimani-nakuru; /projects/ | Official — **`needs_developer_input`** vs B |
| B | Developer blog “Guide price” | **From KSh 8,000,000** | /blog-page/why-nakuru-real-estate…_62/ (Sep 2025) | Official — conflicts with A |
| C | RealtorKenya (developer-posted) | from **Ksh 9,000,000** | realtorkenya.com | Aligns with A (developer channel) |
| D | Craiova / Jumuika / KPC | **KES 9,000,000** (Craiova: “negotiable”) | agents | Secondary |
| E | Discovery lead | no seed price | kenya-offplan-leads.md | Lead only |

**Canonical price:** none. Official A vs B → **`needs_developer_input`**.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **Flexible off-plan / instalments during construction** | Summit project page; aboutus; RealtorKenya (Kings-posted) | Developer **≥1** | **Met via developer** | Must-have **field** present; soft structure |
| **10% down** (portfolio) | diaspora-investment page | Developer **≥1** general | Met as soft portfolio claim | **Not** Summit-canonical; **needs_verification** for this project |
| **20% deposit** | Craiova; Jumuika; KPC listing copy | **3** agencies (Craiova counted once) | **Not met** (≥4) | Secondary + **needs_verification** |
| Exact LOO / brochure schedule | Brochure CTA on project page; PDF **not fetched** this pass | 0 usable | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-kings-developers-ltd` |
| `legal_name` | **Kings Developers Ltd** (also styled **Kings Developers Limited (KDL)** on Royal Group site) |
| `trading_names` | Kings Developers; KDL |
| `website` | https://kingsdevelopers.com/ |
| `evidence` | Summit project “Presented by Kings Developers”; aboutus “Kings Developers Ltd (KDL)… Established in 2004”; milimani location “Kings Developers Ltd”; RealtorKenya poster Kings Developers Ltd |
| `group_company_id` | → `gc-royal-group-of-companies` |
| `established` | claim set — **`needs_developer_input`** | aboutus: **2004** **vs** Royal Group construction page: Kings Developers Limited **Founded 2009** |
| `track_record_claims` | 21+ years; 45+ projects; 8,000+ homes; 5,000+ units under construction — **marketing credentials; delivery unverified this pass** (`needs_verification`) |
| `nakuru_prior_projects_mentioned` | Milimani Heights Ph1/Ph2; Kings Bayview; Kings Sapphire (Bondeni) — listed on projects hub / RealtorKenya; not independently visited this pass |
| `office` | Nairobi / Karen Road (RealtorKenya company + Royal Group contact); sales +254 700 090 060 |

**Primary developer = Kings Developers Ltd (confidence 5).**

---

## 3. GroupCompany

| Field | Value |
|-------|-------|
| `id` | `gc-royal-group-of-companies` |
| `name` | Royal Group of Companies (Royal Group Kenya) |
| `website` | https://royalgroupkenya.com/ |
| `evidence` | kingsdevelopers.com/aboutus: “KDL is part of the Royal Group of Companies… roots tracing back to 1954”. royalgroupkenya.com/extensions/construction-services/: “Kings Developers Limited (KDL)” as real-estate/construction arm |
| `notes` | Founding-year conflict (2004 vs 2009) does **not** undo parent link; flag separately |

---

## 4. RelatedParty

| id | name | relationship_type | Evidence | Conf |
|----|------|-------------------|----------|-----:|
| `rp-elp-kenya` | Enhance Properly Lifestyle (ELP) Kenya | other (property management) | Diaspora/about FAQ: property management via ELP Kenya — not Summit-specific sales partner | 3 |

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Kings Developers Ltd (direct) | developer sales | Project page + RealtorKenya post | https://kingsdevelopers.com/project/kings-summit_49/ · https://www.realtorkenya.com/properties/kings-summit-3-bedroom-apartments-in-milimani-nakuru |
| Craiova Realtors | agency | Two listings (Summit + Summit View twin copy); Maragoli Rd; 20%; completion dates; plinth; amenity adds | https://craiovarealtors.com/property/kings-summit-view-three-bedroom-apartments-in-nakuru/ · https://craiovarealtors.com/property/three-bedroom-apartments-in-milimani-nakuru/ |
| Jumuika / Rashford Properties | portal / agent | 13-floor; 20%; Dec 2026/early 2027; heated-pool copy | https://jumuika.co.ke/properties/3br-apartment-with-heated-pool-lake-views-lower-milimani |
| Kenya Property Centre | portal | “Kings Summit View”; Near Alps Hotel; 20% — **Cloudflare block** on live fetch; search/index copy used for corroboration only | https://kenyapropertycentre.com/for-sale/flats-apartments/nakuru/nakuru-east/51219-kings-summit-view-apartments |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 700 090 060 | Developer: Kings Developers |
| email | sales@kingsdevelopers.com | Developer sales |
| email | info@kingsdevelopers.com / info@kingsdevelopers.co.ke | Developer |
| url | https://kingsdevelopers.com/project/kings-summit_49/ | Property |
| url | https://kingsdevelopers.com/ | Developer |
| address | Karen Road / Royal Group campus (company listings) | Developer HQ |
| phone | +254 702 858 609 | GroupCompany: Royal Group Kenya |
| email | info@royalgroupkenya.com | GroupCompany |
| phone | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |

---

## 6. Stakeholders

None named (contractor / architect / financing) for Kings Summit specifically this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Price from** | Official project/location **9M** **vs** official blog guide **8M** | **Official vs official** → **`needs_developer_input`**. Keep all `price_claims[]` |
| 2 | **Deposit %** | Diaspora portfolio **10%** **vs** agents **20%** (3 agencies) | No Summit-canonical %. Flexible off-plan = developer soft plan. Agent 20% **needs_verification** (threshold not met) |
| 3 | **Completion** | Agents Q4 2026 vs Dec 2026/early 2027; developer page silent | Secondary claim set; **needs_verification** |
| 4 | **Storeys** | Agents 13 floors; developer silent | **needs_verification** |
| 5 | **Amenities** | Agent heated pool/gym/play vs developer core list without those | Core = developer; agent adds **needs_verification** |
| 6 | **Parking** | Developer **1** per apt **vs** agent meta **2** garages/parking | Canonical parking count = **1** (developer). Agent 2 secondary |
| 7 | **Street / landmark** | Maragoli Rd vs Near Alps Hotel / Solai Rongai geo tag on Jumuika | Street **needs_verification**; neighbourhood Milimani canonical |
| 8 | **KDL founding year** | aboutus **2004** vs Royal Group page **2009** | **`needs_developer_input`** on year; GroupCompany link still evidenced |
| 9 | **Name** | Kings Summit vs Kings Summit View | Canonical = **Kings Summit** (developer) |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~13** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~13 candidates (Summit project, projects hub, milimani location, aboutus, Nakuru blog, diaspora, RealtorKenya listing, Craiova×2, Jumuika, KPC listing, Royal Group construction page). **Always kept** developer Summit + about + location. Retained 10 densest (≥5 rule).

**Thin / skipped (not in retained list):**
- https://kingsdevelopers.com/projects/ — hub card only; denser Summit + milimani pages kept
- https://kenyapropertycentre.com/for-sale/flats-apartments/nakuru/nakuru-east/51219-kings-summit-view-apartments — **Cloudflare bot wall** on fetch; index copy used for 20%/13-floor corroboration notes only
- Brochure PDF behind “Download Brochure” CTA — **not fetched** this pass
- Discovery lead row — superseded by this dossier

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://kingsdevelopers.com/project/kings-summit_49/ | Kings Developers Ltd | project_site | 2026-10-16 | From 9M; 3BR/2bath/120 sqm; amenities; flexible off-plan — always keep |
| 2 | https://kingsdevelopers.com/location/milimani-nakuru | Kings Developers Ltd | developer | 2026-10-16 | **Under-Construction** badge; from 9M |
| 3 | https://kingsdevelopers.com/aboutus | Kings Developers Ltd | developer | 2026-10-16 | KDL legal-style name; Royal Group parent; 2004 established |
| 4 | https://kingsdevelopers.com/blog-page/why-nakuru-real-estate-offers-top-investment-opportunities_62/ | Kings Developers Ltd | developer / blog | 2026-10-16 | Guide price **from 8M** — official price conflict |
| 5 | https://kingsdevelopers.com/diaspora-investment | Kings Developers Ltd | developer | 2026-10-16 | Portfolio “as little as 10% down”; ELP management |
| 6 | https://www.realtorkenya.com/properties/kings-summit-3-bedroom-apartments-in-milimani-nakuru | RealtorKenya / Kings Developers Ltd | portal (developer-posted) | 2026-10-16 | UC/off-plan; amenities echo; discovery URL |
| 7 | https://craiovarealtors.com/property/kings-summit-view-three-bedroom-apartments-in-nakuru/ | Craiova Realtors | agent | 2026-10-16 | Maragoli Rd; plinth 120; Q4 2026; 20%; amenity adds |
| 8 | https://craiovarealtors.com/property/three-bedroom-apartments-in-milimani-nakuru/ | Craiova Realtors | agent | 2026-10-16 | 13 floors; Dec 2026/early 2027; 20%; heated pool |
| 9 | https://jumuika.co.ke/properties/3br-apartment-with-heated-pool-lake-views-lower-milimani | Jumuika (Rashford) | portal / agent | 2026-10-16 | 13-floor; 20%; Dec 2026/early 2027 |
| 10 | https://royalgroupkenya.com/extensions/construction-services/ | Royal Group of Companies | group | 2026-10-16 | GroupCompany evidence; KDL “Founded 2009” conflict |

---

## 9. Field harvest

| Field | Kings Summit status | Notes / consensus bump |
|-------|---------------------|------------------------|
| canonical_name / aliases | OK | Summit View = agent alias |
| status UC + off-plan | OK | Developer UC badge |
| geography city/neighbourhood | OK | **First Nakuru** — extend geography scope beyond Nairobi |
| street / GPS | Weak | Maragoli / Alps — verify |
| primary_developer + GroupCompany | OK | KDL + Royal Group evidenced |
| unit_types / size 120 sqm | OK | Plinth tag from agent |
| `storeys` / `total_units` | Missing on developer | Agent 13-floor only |
| `price_claims[]` | Dual official 9M vs 8M | **`needs_developer_input`** |
| `payment_plan` | Flexible off-plan met via developer; deposit % unsettled | Strengthen when Summit LOO/brochure fetched |
| completion_estimate | Agent-only | **needs_verification** |
| amenities core | OK | Reject agent pool/gym as canonical |
| Brochure PDF | Not opened | Next pass for sizes/payment |

### Proposed extensions (this project)

| Proposed extension | Evidence here | Consensus note |
|--------------------|---------------|----------------|
| Geography scope: **city + county** outside Nairobi | Nakuru County / Milimani | Master index needs national/Rift section |
| `size_measure_tag` = **plinth** when agent labels | Craiova “Plinth area” | Keep tagging rule |
| GroupCompany when developer + parent site both name link | Royal Group | Prefer dual evidence |
| Portfolio deposit % ≠ project deposit | Diaspora 10% vs agent 20% | Do not auto-apply portfolio % to one project |

---

## Open questions (developer input)

1. Binding **from** price: **9M** (project pages) or **8M** (blog guide)?
2. Summit-specific deposit: **10%** (diaspora portfolio) vs agent **20%** — publish LOO/brochure schedule.
3. Completion date and storey/unit count (confirm or correct agent **13 floors** / Q4 2026–early 2027)?
4. Exact plot address (Maragoli Road?) + GPS; are heated pool/gym in the final amenity package?
5. Reconcile KDL **founded 2004** (aboutus) vs **2009** (Royal Group page).
6. Fetch/share Kings Summit brochure PDF.
