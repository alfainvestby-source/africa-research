---
slug: capricorn-kilimani
external_id: DISC-CAPRICORN
wave: discovery
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Capricorn (Wood Avenue, Kilimani) — discovery research

**Not in CSV seed** — discovery lead from [kenya-offplan-leads.md](/cursor/stores/self/docs/discovery/kenya-offplan-leads.md). No new NBO id assigned this pass.

Live research **2026-10-16**. Official project microsite **https://capricorn.co.ke/** was **down** this pass (HTTP 500 / connection fail); **search-indexed** official copy retained + always kept. Developer surfaces: **Staroot** developments card + company contact FAQ; Proxima-hosted Capricorn PDF naming **Staroot Company Ltd** + **Mulika Garden Company Ltd**.

**Method locks applied:**
- Developer / official outweigh agents; agent-only consensus caps at conf **3**.
- If developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** disagreement → **`needs_developer_input`**; no assumed winner.
- Prices always **`price_claims[]`**. No forced scalar.
- Payment must-have if **any developer source** **or** ≥4 independent agent/portal sources.
- Co-named “Developers” on pack → **both** `co_developer` and RelatedParty until simplified later.
- Unproven brand/parent → **`marketing_partner`**, not GroupCompany.
- Agent-only sold-out / unit counts → **show** + **`needs_verification`**.
- **Staroot Residency** (completed Wood Ave 2023) ≠ this Capricorn project — wrong-entity trap.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer/official-backed when sources **agree**. Claim set / secondary kept for conflicts. **`needs_verification`** = low-confidence / agent-only.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Capricorn (styled Capricorn Apartments / Capricorn Residences) | 5 | capricorn.co.ke (indexed); staroot.co.ke/developments; Proxima PDF |
| `aliases` | secondary | Capricorn Residency; Capricorn Residences; Capricon (Hauzisha misspelling); Capricon Residences | 3 | Hauzisha; A-list; agents |
| `status` | claim set | Official microsite: **off-plan**. Staroot LinkedIn About: Capricorn **2024–2026**. Agents: under construction / “Near Completion” (CPK) | 4 | indexed capricorn.co.ke; LinkedIn Staroot (search); CPK; african.land |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood_street` | **CANONICAL** | **Wood Avenue, Kilimani** — adjacent to **CJ’s** restaurant; near Yaya Centre | 5 | staroot developments; PDF; capricorn.co.ke indexed; multi-agent |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.293717, 36.786086** (`geo_method=geocode`) | 3 | Nominatim Wood Avenue Kilimani 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-staroot-real-estate` (**Staroot Company Ltd** on PDF) | 5 | PDF; Staroot site; Hauzisha |
| `co_developer_ids[]` | claim set (pack co-name) | → `dev-mulika-garden` (**Mulika Garden Company Ltd**) — also RelatedParty | 4 | Proxima Capricorn PDF “DEVELOPER: STAROOT… MULIKA GARDEN…” |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom; 3 Bedroom | 5 | Staroot; PDF; capricorn.co.ke indexed; agents |
| `size_by_type` | **CANONICAL** (pack sizes) | 1BR **70.3 sqm**; 2BR **102.5 sqm**; 3BR **131.2 sqm** (A-list **131.1**) | 5 | Proxima PDF floor-plan pages; A-list/2Talk echo |
| `size_by_type` | secondary (imperial agent) | 1BR **750 sqft**; 2BR **1,100 sqft**; 3BR **1,400 / 1,420.84 sqft** | 3 | Jimarket; Mascott; CPK |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on pack | 0 | — |
| `total_units` | secondary — **`needs_verification`** | african.land: **400** — single aggregator; not on Staroot/PDF this pass | 1 | african.land |
| `building_specs.storeys` / blocks | unknown / soft | Hauzisha amenity “2 lifts per block” implies multi-block — **no storey count** on official materials fetched | 1 | Hauzisha |
| `price_claims[]` | claim set — **keep all**; no developer unit price list | See §1a | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | agents; Proxima card |
| `payment_plan.deposit` | **CANONICAL** (Staroot company FAQ) | **Minimum 20%** to reserve; **select cases 10%** (Staroot contact FAQ — company-wide; same FAQ used for Gemini). Live accordion **did not hydrate** this pass (SPA) — content verified same day on Staroot contact for NBO-009 | 5 | staroot.co.ke/contact |
| `payment_plan` (Capricorn-specific agent schedule) | secondary — **needs_verification** vs FAQ | **30%** deposit + **50%** every 6 months + **20%** on completion (**September 2026**) — Jimarket/Mascott; A-list/2Talk variants **30%** then balance | 3 | ≥4 agents on **30%** deposit element |
| `completion_estimate` | claim set | Staroot developments: **2026**. Agents: **September 2026** (Jimarket/Mascott) vs **November 2026** (A-list) vs year-only (Hauzisha). LinkedIn About: Capricorn **2024–2026** | ≤4 | Staroot card agrees on year; month conflicts among agents |
| `amenities` (core — official/pack) | **CANONICAL** | **20 m heated pool** (+ sunken lounge on PDF); fully equipped / fitted **gym**; **yoga studio**; adult gaming lounge / adult play area; **rooftop** lounge/terraces; landscaped gardens / central courtyards; **reception**; kids playroom (PDF); high-end finishes; automated home system (PDF highlight) | 5 | capricorn.co.ke indexed; Proxima PDF; A-list/CPK echo |
| `amenities` | secondary | Borehole; backup generator; CCTV/intercom; electric fence; fibre; parking; “Zen Garden” — multi-agent; not all on indexed official home | 3 | Mascott; Jimarket; Hauzisha |
| `availability_claim` | secondary — **`needs_verification`** | CPK: 1BR & 2BR **sold out**; 3BR listed. Hauzisha: **2 units** available | 2 | CPK; Hauzisha |
| `legal_title` | soft (company FAQ) | Staroot contact: sectional title via **ardisasa** at completion — general process, not Capricorn LOO | 2 | staroot.co.ke/contact |
| `investment_return_claims` | marketing only — **not product facts** | PDF market stats (avg price 12.6M, ROI %, rental growth) — **do not store as verified yields** | 0 | Proxima PDF |

### 1a. Price claims — keep **all** options (no canonical)

No unit price list on live Staroot Capricorn card or fetched capricorn.co.ke copy. PDF states Kilimani “average” **12,600,000** (market blurb, not a Capricorn from-price).

| # | Claim band | Value (KES) | Publisher | Flag |
|--:|------------|-------------|-----------|------|
| A | Modal agent table | 1BR **8.5M**; 2BR **12.0M**; 3BR **15.5M** | Jimarket; Mascott; CPK; 2Talk (indexed); african.land | Secondary |
| B | A-list typed (matches pack sizes) | 1BR 70.3 **10M**; 2BR 102.5 **13.5M**; 3BR 131.1 outside **15.5M** / inside **16.5M** | a-listrealestate.ke | Secondary — conflicts with 8.5/12 band |
| C | Hauzisha card | **13.5M – 15.5M** (band; omits 8.5 entry) | hauzisha.co.ke | Secondary |
| D | Proxima ongoing card | Capricorn Kilimani **15.5M** (single from) | proxima.co.ke/property/ongoing-projects | Secondary |
| E | PDF market average (not unit list) | Kilimani high-end average **12.6M** | Capricorn PDF | Not a Capricorn SKU price |

**Canonical price:** none.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold? | Status |
|---------|------------------------------|------:|------------|--------|
| **Min 20% deposit** (select **10%**) | Staroot contact FAQ (company-wide) | Developer **≥1** | **Met via developer** | **CANONICAL must-have** |
| Capricorn **30%** deposit | Jimarket; Mascott; A-list; 2TalkKenya (search-indexed; live fetch 504) | **≥4** agents | Met as agent consensus | Secondary vs FAQ min 20% |
| **30/50/20** to Sept 2026 | Jimarket; Mascott | 2 | Below ≥4 for full schedule | Soft secondary schedule |
| Attractive payment plans (no %) | Capricorn PDF highlight | Developer-attributed pack | Soft | No numeric plan on PDF |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-staroot-real-estate` |
| `legal_name` | **Staroot Company Ltd** (PDF); trading **Staroot Real Estate** / “Staroot Real Estate Company” (Hauzisha) |
| `trading_names` | Staroot Real Estate; Staroot; Capricorn (project brand) |
| `website` | https://staroot.co.ke/ · developments https://www.staroot.co.ke/developments · project microsite https://capricorn.co.ke/ |
| `evidence` | Staroot Latest Launches card for Capricorn; PDF developer line; Hauzisha attribution |
| `group_company_id` | **null — none invented** |
| `office` | Principal Place, Westlands, Nairobi |
| `contacts` | +254 710 999 111 · hello@staroot.co.ke |
| `prior_projects_on_pack` | White Oak, Silver Oak, Platinum Oak, Bric, Venus Oak, **Staroot Residency (Wood Ave — separate completed project)**, Neptune — delivery claims **`needs_verification`** |

**Primary developer = Staroot Company Ltd / Staroot Real Estate (confidence 5).**

### Co-developer (pack)

| Field | Value |
|-------|-------|
| `id` | `dev-mulika-garden` |
| `legal_name` | Mulika Garden Company Ltd |
| `role` | Co-named **DEVELOPER** on Capricorn PDF with Staroot — model as **`co_developer` + RelatedParty** (Cycle 2 lock) |
| `evidence` | Proxima PDF project team page |
| `conf` | 4 (pack); relationship detail (equity vs brand) unknown |

---

## 3. GroupCompany

**None.** Do not invent a parent above Staroot / Mulika Garden.

---

## 4. RelatedParty

| id | name | relationship_type | Evidence | Conf |
|----|------|-------------------|----------|-----:|
| `rp-mulika-garden` | Mulika Garden Company Ltd | `co_developer` (parallel RelatedParty) | PDF co-names as DEVELOPER with Staroot | 4 |
| `rp-proxima-real-estate` | Proxima Real Estate | `marketing_partner` / consultant | PDF: **DEVELOPMENT CONSULTANT**; hosts Capricorn PDF; lists Capricorn on ongoing projects | 4 |

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Proxima Real Estate | consultant / portal | Hosts official-attributed PDF; ongoing projects card | https://proxima.co.ke/project_images/1699449349_(2)%20Capricorn%20The%20heart%20of%20kilimani.pdf · https://proxima.co.ke/property/ongoing-projects |
| Jimarket | portal / agent | 8.5/12/15.5M; 30/50/20 Sept 2026 | https://jimarket.co.ke/property/capricorn/ |
| Mascott Properties | agency | Same price + payment schedule | https://mascottproperties.co.ke/properties/capricorn-apartments-kilimani/ |
| A-list Real Estate | agency | Higher price band; Nov 2026; 30% | https://a-listrealestate.ke/property/capricon-residences/ |
| CPK Real Estate | agency | Amenities; sold-out 1/2BR; Near Completion | https://commercialpropertykenya.com/properties/the-capricorn-residences-apartment-in-kilimani/ |
| Hauzisha | portal | Staroot attribution; 13.5–15.5M; 2 units | https://hauzisha.co.ke/developments/capricon/ |
| african.land | aggregator | Staroot Company Limited; 400 units; Sept 2026 | https://african.land/real-estate/new-build-properties-for-sale/capricorn-residency-luxury-living-in-the-heart-of-kilimani_i417 |
| 2TalkKenya | agency | Pack sizes + 8.5/12/15.5; 30%/70% (fetch 504 this pass) | https://2talkkenya.com/property/capricorn-residency-1-2-3-bedroom/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 710 999 111 | Developer: Staroot |
| email | hello@staroot.co.ke | Developer: Staroot |
| address | Principal Place, Westlands, Nairobi | Developer: Staroot |
| url | https://capricorn.co.ke/ | Property microsite (down this pass) |
| url | https://www.staroot.co.ke/developments | Developer launches |
| phone | +254 752 444 999 / +254 788 444 999 | RelatedParty: Proxima |
| email | info@proxima.co.ke | RelatedParty: Proxima |
| phone | +254 740 888 080 | Agent: Mascott |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 730 731 355 | Portal: Hauzisha |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Karim CG Visuals** | architect / designer | PDF: DEVELOPMENT DESIGNER | 5 |
| **Proxima Real Estate** | other (development consultant) | PDF consultant line (also RelatedParty) | 4 |
| Unnamed main contractor | other | Not named this pass | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Deposit** | Staroot FAQ **min 20%** (select 10%) vs Capricorn agents **30%** (± 30/50/20) | Developer vs agents → **canonical = min 20%**. Keep agent 30% schedules secondary. |
| 2 | **Prices** | 8.5/12/15.5 vs A-list 10/13.5/15.5–16.5 vs Hauzisha 13.5–15.5 vs Proxima 15.5 | **Keep all** `price_claims[]`. No canonical. |
| 3 | **Completion month** | Staroot year **2026**; Sept 2026 (agents) vs Nov 2026 (A-list) | Year canonical from agreeing Staroot card; month = claim set. |
| 4 | **Sold-out** | CPK 1BR/2BR sold out vs Hauzisha 2 units / others still listing 8.5M | Show + **`needs_verification`**. |
| 5 | **Unit count 400** | african.land only | **`needs_verification`**. |
| 6 | **3BR size** | PDF **131.2 sqm** vs CPK **1420.84 sqft** (~132 sqm) vs A-list **131.1** | Minor; prefer PDF sqm as official-attributed. |
| 7 | **Wrong entity** | **Staroot Residency** (completed Wood Ave) vs **Capricorn** (active 2024–2026) | Keep separate; PDF lists Staroot Residency as prior project. |
| 8 | **Microsite availability** | capricorn.co.ke down this pass | Always keep URL; use indexed official amenity/identity copy + Staroot/PDF. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 (capricorn.co.ke, Staroot developments, Staroot contact, Proxima PDF, Proxima ongoing, Jimarket, Mascott, A-list, CPK, Hauzisha, african.land, 2Talk, LinkedIn About snippet, Space.ke Staroot Residency wrong-entity). **Always kept** official Capricorn microsite + Staroot + developer-attributed PDF.

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://capricorn.co.ke/ | Capricorn Apartments | project_site | 2026-10-16 | **Always keep** — live fetch failed (500); **search-indexed** amenities + off-plan Kilimani/CJ’s copy retained |
| 2 | https://www.staroot.co.ke/developments | Staroot Real Estate | developer | 2026-10-16 | Capricorn Wood Ave; 1/2/3BR; completion **2026** |
| 3 | https://staroot.co.ke/contact/ | Staroot Real Estate | developer | 2026-10-16 | Deposit FAQ min 20% / select 10%; Principal Place; phones — SPA accordion thin this pass |
| 4 | https://proxima.co.ke/project_images/1699449349_(2)%20Capricorn%20The%20heart%20of%20kilimani.pdf | Proxima / Staroot pack | developer_attributed | 2026-10-16 | Sizes 70.3/102.5/131.2; Staroot+Mulika developers; Proxima consultant; Karim CG; amenities |
| 5 | https://proxima.co.ke/property/ongoing-projects | Proxima Real Estate | agent / consultant | 2026-10-16 | Capricorn card from **15.5M** |
| 6 | https://jimarket.co.ke/property/capricorn/ | Jimarket | agent | 2026-10-16 | 8.5/12/15.5; 30/50/20 Sept 2026 |
| 7 | https://mascottproperties.co.ke/properties/capricorn-apartments-kilimani/ | Mascott Properties | agent | 2026-10-16 | Same price + payment schedule |
| 8 | https://a-listrealestate.ke/property/capricon-residences/ | A-list Real Estate | agent | 2026-10-16 | Higher prices; **Nov 2026**; 30% |
| 9 | https://commercialpropertykenya.com/properties/the-capricorn-residences-apartment-in-kilimani/ | CPK Real Estate | agent | 2026-10-16 | Sold-out 1/2BR; amenities; Near Completion |
| 10 | https://hauzisha.co.ke/developments/capricon/ | Hauzisha | portal | 2026-10-16 | Staroot; 13.5–15.5M; 2 units; typo Capricon |

### Evaluated but not retained

| url | Why skipped |
|-----|-------------|
| https://2talkkenya.com/property/capricorn-residency-1-2-3-bedroom/ | **HTTP 504** this pass; price/payment used only as corroboration note |
| https://african.land/real-estate/new-build-properties-for-sale/capricorn-residency-luxury-living-in-the-heart-of-kilimani_i417 | Thin aggregator; 400-unit claim only unique field — noted in conflicts, not densest retain |
| https://space.ke/projects/staroot/ | **Wrong entity** (Staroot Residency completed 2023) |
| https://linkedin.com/company/staroot-real-estate | Fetch timeout; Capricorn 2024–2026 from search index only |
| Discovery lead row (kenya-offplan-leads) | Lead only |

---

## 9. Field harvest → must-have extension proposals

| Proposed / reinforced field | Capricorn evidence | Consensus note |
|----------------------------|--------------------|----------------|
| Official microsite **even when down** (keep URL + indexed copy) | capricorn.co.ke 500 this pass | Process reinforce |
| Dual **co_developer** on pack (Staroot + Mulika Garden) | PDF team page | Matches Porini co-name lock |
| Named **designer** Stakeholder | Karim CG Visuals | Capture when named (also Pandora) |
| Pack **size_by_type** sqm as developer-attributed | 70.3 / 102.5 / 131.2 | Strengthen when pack agrees with agents |
| Company FAQ deposit applies across Staroot projects | min 20% | Confirmed pattern vs Capricorn agent 30% |
| Wrong-entity prior project on same street | Staroot Residency ≠ Capricorn | Diligence note |
| Sold-out agent flags | CPK 1/2BR | Show + **`needs_verification`** |

---

## Open questions (developer / verification pass)

1. Re-fetch **https://capricorn.co.ke/** when live — prices, payment, contacts, unit count?  
2. Confirm **Mulika Garden Company Ltd** equity/role vs marketing co-name.  
3. Binding Capricorn LOO: company FAQ **min 20%** vs marketed **30/50/20**?  
4. Reconcile **8.5/12/15.5** vs A-list **10/13.5/15.5–16.5** price lists.  
5. Are 1BR/2BR actually **sold out** (CPK)?  
6. True **unit count / storeys / blocks**; is african.land **400** real?  
7. Exact contractual completion (**Sept vs Nov 2026**)?
