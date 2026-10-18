---
slug: galaxy-one
external_id: NBO-013
cycle: 2
pilot: false
retrofit: cycle-2-locks-2026-10-16
sources_evaluated: 13
sources_retained: 10
last_verified_at: 2026-10-16
---

# Galaxy One (NBO-013) — Cycle 2 (retrofit)

CSV seed (unverified leads): location Rhapta Road, Westlands, Nairobi; stage `under_construction`; completion Q2 2027; `price_from_kes` 5,610,000; sales_contact NRE Real Estate; developer “Lionstone”.

Live research: project microsite + Lionston corporate/project/construction pages + portals/agents accessed 2026-10-15; **Cycle 2 lock retrofit 2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume a winner** → flag **`needs_developer_input`**; no canonical until a later verification pass.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- `construction_progress`: retain as **claim set** when developer publishes (including conflicting snapshots); not portal must-have yet.
- Payment must-have if any developer source **or** ≥4 agent sources. Agent-only / uncorroborated → **`needs_verification`**. CSV = unverified leads only.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed value when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Galaxy ONE (also styled Galaxy.ONE / Galaxy One) | 5 | galaxyone.co; lionston.co |
| `aliases` | secondary | Galaxy One; Galaxy.ONE; Galaxy ONE Apartments; Galaxy ONE Residences | 4 | agents/portals; JSON-LD |
| `status` | claim set | CSV/`under_construction`; Lionston construction tracker live UC; agents “Construction ongoing” / “off-plan selling” | 4 | lionston.co/en/construction; CSV; Ravi |
| `geography.city` | **CANONICAL** | Nairobi | 5 | galaxyone.co; lionston.co |
| `geography.neighbourhood_street` | **CANONICAL** | Westlands — **147 Rhapta Road** | 5 | galaxyone.co; lionston.co (+ agents agree) |
| `geography.lat_lng` | **CANONICAL** (developer schema) | **−1.2635, 36.8029** | 5 | galaxyone.co JSON-LD / geo meta |
| `primary_developer_id` | **CANONICAL** | → `dev-lionston-real-estate` | 5 | galaxyone.co; lionston.co |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom; 3 Bedroom | 5 | galaxyone.co; lionston.co/en/galaxy-one |
| `size_by_type` | **CANONICAL** (bands — pages agree) | 1BR **57–60 sqm**; 2BR **82–91 sqm**; 3BR **142 sqm** | 5 | galaxyone.co; lionston.co |
| `size_by_type` | secondary (precise agent/portal tables) | 1BR **57.08** / **59.62**; 2BR **82.67** / **90.66**; 3BR **142.43** sqm | 4 | Ravi; NRE; Vorsa; Masterways; Knight Frank indexed copy |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched | 0 | — |
| `total_units` | claim set — **`needs_developer_input`** | **210** (galaxyone.co + several agents) **vs 266** (lionston.co product/home/construction + NRE) | 2 | Official vs official — **no assumed winner** |
| `building_specs.storeys` | claim set — **`needs_developer_input`** | Search-indexed galaxyone.co story **30-storey** **vs** Lionston product + construction **19 storeys** (“of 19”). Static HTML fetch lacked “30-storey” (SPA) → 30 also **`needs_verification`** for live hydration | 2 | Official vs official — **no assumed winner** |
| `building_specs.wings_blocks` | **CANONICAL** (presence — pages agree) | Two wings / Block A & Block B | 5 | galaxyone.co; lionston.co/en/construction |
| `price_claims[]` | claim set — **`needs_developer_input`** on dual official bands; **keep all options** | See §1a — no scalar; official A vs official B + agent tables | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | all commercial sources |
| `payment_plan.deposit` | **CANONICAL** (developer pages **agree**) | **10% deposit** to reserve | 5 | galaxyone.co; lionston.co (product + home) |
| `payment_plan.deposit` | secondary — **needs_verification** vs official | Agent/portal consensus **20% deposit** (≥4) | 3 | Ravi×2; Masterways; BuyRent/Coral; NRE; KeDwell options |
| `payment_plan.balance` | secondary soft claim | Balance over construction / flexible instalments | 3 | agents; developer “flexible payment plans” |
| `completion_estimate` | **CANONICAL** (developer framing — pages agree on late 2027) | **Late 2027** (target / handover); staged Q2–Q3 2027 finishing on timelines | 5 | lionston.co; galaxyone.co FAQ |
| `completion_estimate` | secondary | **June / Q2 2027** (multi-agent + CSV) vs **December 2027** (Hauzisha) — **CONFLICT** | ≤3 | agents/CSV |
| `amenities` (core) | **CANONICAL** | Heated rooftop infinity pool; Sky Club (~1,093 sqm on Lionston); gym; spa & sauna; private theater; piano lounge / coffee; yoga & wellness deck; rooftop art garden; indoor mini-golf; children’s play; 24/7 CCTV security; high-speed elevators | 5 | galaxyone.co JSON-LD/FAQ; lionston.co/en/galaxy-one |
| `amenities` | secondary / inflated — **needs_verification** | Vorsa adds jacuzzis, beauty parlor, basketball/padel, kids’ daycare, jogging track — not on developer materials this pass | 1 | Vorsa only |
| `construction_progress` | claim set — **`needs_developer_input`** | Product page: ~floor **12 of 19**, overall **63%**. Construction tracker: Block A **9/19**, Block B **7/19**, overall **42%** (~Sep 2026 week notes). **Retain both; do not average or pick.** | 3 | lionston.co/en/galaxy-one vs /en/construction |
| `availability_claim` | secondary | Lionston product: “**33 of 84 available**” (2BR floor-plan context); Hauzisha “3 units” — **needs_verification** | 2 | lionston; Hauzisha |
| `legal_title` | unknown | — | 0 | not found |
| `plot_size` | secondary | Half-acre (agents) | 2 | Ravi; Vorsa; KeDwell |

### 1a. Price claims — keep **all** options (no canonical)

Official vs official dual bands → **`needs_developer_input`**. Agents/CSV retained as secondary options.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Lionston product “from” cash framing | 1BR **from KES 8.0M**; 2BR **from KES 12.0M**; 3BR **from KES 18.0M** | lionston.co/en/galaxy-one | Official — **`needs_developer_input`** vs B |
| B | Galaxy ONE FAQ / JSON-LD (cash + instalment) | 1BR cash **from Ksh 5.2M**, instalment **from Ksh 6.1M**; 3BR instalment **from Ksh 16.5M** / cash **Ksh 13.9M**; meta “from Ksh 5.2M cash” | galaxyone.co | Official — **`needs_developer_input`** vs A |
| C | Knight Frank indexed listing (from + cash columns) | e.g. 57.08 sqm from **7.03M** / cash **5.32M** … 142.43 from **19M** / cash **14.38M**; **10% deposit**; Late 2027 | knightfrank.com hub2519857 (search-indexed; live HTML shell thin) | Secondary / indexed |
| D | Ravi | From **~7.62M** to **~19.02M** (cash lower) | ravihomes.co.ke | Secondary |
| E | NRE | From **KES 5.61M** (matches CSV) to higher bands; FAQ also echoes ~7.62M–19.02M | nairobirealestate.co.ke | Secondary — **needs_verification** (own page inconsistency) |
| F | Masterways | Typed list e.g. 1BR from **~6.11M** … 3BR **~16.54M** | masterways.co.ke | Secondary |
| G | Vorsa | Overlaps Masterways-style lower bands (e.g. from **~6.11M**) | vorsagroup.co.ke | Secondary |
| H | CSV seed | `price_from_kes` **5,610,000** | seed | Unverified lead |

**Canonical price:** none. Always `price_claims[]` with every option above.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **10% deposit** | galaxyone.co; lionston.co (product + home) — pages **agree**; Knight Frank indexed echoes | Developer **≥1** (agreeing) | **Met via developer** | **CANONICAL must-have** (developer-vs-agent, not official-vs-official) |
| **20% deposit** | Ravi property; Ravi developments; Masterways; BuyRentKenya/Coral; NRE; KeDwell (as an option) | **≥4** agents | Met as agent consensus | Secondary; conflicts with canonical 10% |
| Balance over construction | Multi-agent + soft developer “flexible” | ≥4 vague | Soft secondary | Exact schedule unknown |
| Developer LOO/full schedule PDF | Not opened this pass (prospectus CTA present; PDF not fetched) | 0 usable | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-lionston-real-estate` |
| `legal_name` | Lionston Real Estate Limited (meta/author on lionston.co) |
| `trading_names` | Lionston Real Estate; Lionston |
| `website` | https://www.lionston.co/ · project https://galaxyone.co/ |
| `evidence` | galaxyone.co “By Lionston Real Estate”; lionston.co Galaxy.ONE flagship; agents attribute Lionston |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV “Lionstone” treated as **typo/lead** for Lionston — not a separate entity |
| `prior_projects_mentioned` | Homepage portfolio cards (BBS Mall, Riverside Square, Five Star Paradise, Imaara Mall, G48, etc.) + “150+ Projects / $576M+ Delivered / 4 Countries / Class I Contractor” — **delivery/credentials unverified this pass** (`needs_verification`) |

**Primary developer = Lionston Real Estate Limited (confidence 5).** Not CSV “Lionstone” as distinct brand.

---

## 3. GroupCompany

**None.** No evidenced parent above Lionston. Do not invent from contractor branding or portfolio claims.

---

## 4. RelatedParty

None required (no unproven brand-overlap marketing partner analogous to Astra/Laureland).

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| NRE Real Estate | agency | CSV sales_contact; listing + payment UI | https://nairobirealestate.co.ke/properties/galaxy-one |
| Ravi Homes | agency | Listing + development hub; 20% claim; 210 units | https://ravihomes.co.ke/property/galaxy-one-apartments-westlands-rhapta-road/ · https://ravihomes.co.ke/developments/galaxy-one/ |
| VorsaGroup Real Estate | agency | Price table; floor-plan PDFs attached | https://vorsagroup.co.ke/property/galaxy-one-1-2-and-3-bedrooms-apartments-in-westlands/ |
| Masterways Real Estate | agency | Typed unit price list; 20% | https://masterways.co.ke/properties/galaxy-one |
| Hauzisha | portal | Inventory card; **Dec 2027** outlier | https://hauzisha.co.ke/developments/galaxy-one/ |
| Coral Property International Ltd (via BuyRentKenya) | agency / portal listing | 20% deposit; June 2027 | https://www.buyrentkenya.com/listings/1-bedroom-apartment-for-sale-rhapta-road-3896467 |
| Knight Frank | agency network listing | Indexed dense copy (10% deposit; price table; Late 2027); live fetch = JS shell | https://www.knightfrank.com/properties/residential/for-sale/rhapta-road-westlands/hub2519857 |

KeDwell evaluated (payment options 20/30/50/100%) — not retained (overlaps denser retained agent price tables).

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 117 222 666 | Developer sales (Lionston) |
| phone | +254 117 222 999 | Developer / project marketing |
| email | hello@lionston.co | Developer |
| email | Marketing@lionston.co | Project marketing (galaxyone.co) |
| address | 147 Rhapta Road, Westlands, Nairobi | Property / sales site |
| url | https://galaxyone.co/ | Property |
| url | https://lionston.co/en/galaxy-one | Developer project |
| url | https://lionston.co/en/construction | Developer construction tracker |
| phone | +254 141 361 320 | Agent: NRE (CSV) |
| email | info@nairobirealestate.co.ke | Agent: NRE (CSV) |
| phone | +254 105 772 200 | Agent: Ravi Homes |
| email | sales@ravihomes.co.ke | Agent: Ravi Homes |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: VorsaGroup |
| email | info@vorsagroup.co.ke | Agent: VorsaGroup |
| phone | +254 730 731 355 | Portal: Hauzisha |
| phone | +254 706 327 148 | Agent: Coral (BuyRentKenya listing) |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **CRJE** | contractor | lionston.co/en/construction — “CRJE delivering 3 floors per month with Chinese Speed construction” | 4 |
| Unnamed facility / property management | other | Marketing copy on Lionston/agents — not a named firm | 1 |

No financing partner / architect / land vendor named this pass.

---

## 7. Conflicts (explicit) — Cycle 2 lock

| # | Field | Claims | Resolution under Cycle 2 lock |
|--:|-------|--------|-------------------------------|
| 1 | **Total units** | galaxyone.co + agents: **210**. Lionston product/home/construction + NRE: **266**. | **Official vs official** → **`needs_developer_input`**. No canonical. No assumed winner. |
| 2 | **Storeys** | Indexed galaxyone.co story: **30**. Lionston product/home/construction: **19**. | **Official vs official** → **`needs_developer_input`**. Do **not** prefer 19 from tracker operationalization. 30 also **`needs_verification`** (SPA hydration). |
| 3 | **Deposit** | Developer pages **agree** on **10%**. Agents ≥4 say **20%**. | Developer vs agents → **canonical = 10%**. Keep 20% secondary. |
| 4 | **Prices (dual official + agents)** | Official A (8/12/18M) vs Official B (cash 5.2M / instalment 6.1M …) vs agent tables C–G vs CSV H. | **Official vs official** → **`needs_developer_input`**. **Keep all** `price_claims[]` options. No scalar. |
| 5 | **Completion** | Developer pages agree **late 2027**. Agents/CSV June/Q2; Hauzisha Dec. | Canonical framing = late 2027 (agreeing developer). Agent dates secondary. |
| 6 | **Construction progress % / floor** | Product: 63% / floor 12 of 19. Tracker: 42% / A9 · B7. | **Official vs official** → **`needs_developer_input`**. Retain **claim set**; do not average. |
| 7 | **CSV developer spelling** | “Lionstone” vs evidenced **Lionston**. | CSV = unverified lead / typo. |
| 8 | **CSV sales_contact** | NRE ≠ Lionston sales phones. | Split Contact.owner correctly. |
| 9 | **Amenity inflation** | Vorsa courts / parlor / daycare vs developer core list. | Core = developer only; Vorsa **`needs_verification`**. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~13** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~13 candidates (project microsite, Lionston home, Lionston Galaxy.ONE page, Lionston construction tracker, Ravi×2, NRE, Vorsa, Masterways, Hauzisha, BuyRentKenya/Coral, Knight Frank, KeDwell, plus CSV seed as non-web lead). **Always kept** developer/official project + Lionston pages. Retained 10 richest field-bearing sources (≥5 rule).

**Thin / skipped (not in retained list):**
- https://www.knightfrank.com/properties/residential/for-sale/rhapta-road-westlands/hub2519857 — live fetch = **JS shell**; dense copy only in search index → evaluated for corroboration notes, **not retained** as primary cite
- https://www.kedwell.co.ke/projects/galaxy-one-apartments-westlands-11 — overlaps retained agent tables; payment options unique but thinner than Masterways+Ravi
- https://galaxy.one/en/document-hub/ — **wrong entity** (unrelated “Galaxy One” docs hub)
- CSV NBO-013 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://galaxyone.co/ | Galaxy ONE / Lionston | project_site | 2026-10-15 | 210 units; 10% deposit; size bands; FAQ prices; GPS JSON-LD — always keep |
| 2 | https://lionston.co/en/galaxy-one | Lionston Real Estate Limited | developer | 2026-10-15 | 19 storeys; 266 apts; 10%; prices from 8/12/18M; progress claim |
| 3 | https://www.lionston.co/ | Lionston Real Estate Limited | developer | 2026-10-15 | Legal-style name; flagship summary; contacts |
| 4 | https://lionston.co/en/construction | Lionston Real Estate Limited | developer | 2026-10-15 | 19/266; CRJE; block progress; late 2027 |
| 5 | https://ravihomes.co.ke/property/galaxy-one-apartments-westlands-rhapta-road/ | Ravi Homes | agent | 2026-10-15 | 210; 20%; June 2027; price table |
| 6 | https://ravihomes.co.ke/developments/galaxy-one/ | Ravi Homes | agent | 2026-10-15 | Lionston; 20%; typed prices |
| 7 | https://nairobirealestate.co.ke/properties/galaxy-one | NRE | agent | 2026-10-15 | 266; 20% UI; from 5.61M; CSV contact |
| 8 | https://vorsagroup.co.ke/property/galaxy-one-1-2-and-3-bedrooms-apartments-in-westlands/ | VorsaGroup | agent | 2026-10-15 | Prices; floor-plan PDFs; amenity inflation |
| 9 | https://masterways.co.ke/properties/galaxy-one | Masterways | agent | 2026-10-15 | Typed prices; 20%; 210 units |
| 10 | https://hauzisha.co.ke/developments/galaxy-one/ | Hauzisha | portal | 2026-10-15 | Lionston; **Dec 2027** conflict; thin otherwise |

---

## 9. Field harvest (post Cycle 2 lock retrofit)

| Field | Galaxy One status | Notes |
|-------|-------------------|-------|
| canonical_name / aliases | OK | Developer agree |
| status | OK as claim set | UC on tracker |
| geography + street + lat_lng | OK | Developer agree / JSON-LD |
| primary_developer | OK | Lionston Real Estate Limited |
| GroupCompany | none | Correctly empty |
| unit_types / size bands | OK | Pages agree |
| `total_units` / `storeys` | Claim set + **`needs_developer_input`** | No winner |
| `price_claims[]` | All options retained (A–H) | Dual official → **`needs_developer_input`** |
| `payment_plan` | **10% canonical** (developer agree); 20% secondary | |
| `construction_progress` | Claim set retained + **`needs_developer_input`** | Coverage-gated for portal |
| amenities core | OK | Reject Vorsa adds |
| completion_estimate | Late 2027 canonical (agreeing developer) | Agent dates secondary |
| Named contractor CRJE | Captured | Stakeholder |

---

## Retrofit summary (2026-10-16)

- Official-vs-official on **210 vs 266**, **30 vs 19**, **construction %/floor**, and **dual official prices** → **`needs_developer_input`**; language that leaned toward 19 storeys removed.
- **All** price options kept in §1a (A–H); no scalar.
- `construction_progress` kept as claim set (both snapshots).
- Deposit **10%** remains canonical — developer pages **agree** (developer-vs-agent rule, not official-vs-official).

## Open questions (developer input)

1. Reconcile **210 vs 266** units and **30 vs 19** storeys across galaxyone.co vs lionston.co.
2. Which live LOO/price list: Official A (8/12/18M) or Official B (cash 5.2M / instalment 6.1M)?
3. Which construction snapshot is current (63%/floor 12 vs 42%/A9·B7)?
4. Is **10%** still the binding reservation deposit vs agent **20%** LOOs?
5. Prospectus PDF for gross/plinth tags?
6. CRJE legal entity / contract role; “150+ projects / Class I” provenance?
