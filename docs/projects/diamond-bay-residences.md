---
slug: diamond-bay-residences
external_id: NBO-007
wave: B
cycle: scale-half
pilot: false
sources_evaluated: 16
sources_retained: 12
last_verified_at: 2026-10-16
---

# Diamond Bay Residences (NBO-007) — Wave B / scale

CSV seed (unverified leads): location Westlands Road, Westlands, Nairobi; lat/lng −1.26750, 36.81202; stage `under_construction`; completion Q3 2027; `price_from_kes` 8,840,000; sales_contact Loyd Mokaya (Block Real Estate); **developer blank**.

Live research: Henbon Company LTD developer site (henbon.co) + product pages + amenities/about + agent/portal listings + Henbon LinkedIn progress posts. Accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume** → **`needs_developer_input`**.
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 agent sources. Agent-only / uncorroborated → **`needs_verification`**.
- Low-confidence typologies / sold-out / availability: **show** + **`needs_verification`**.
- CSV = unverified leads only. CSV sales_contact ≠ developer.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Diamond Bay Residences | 5 | henbon.co (copyright + ongoing); Hauzisha |
| `aliases` | secondary | Diamond Bay Residence; Diamond Bay; DIAMOND BAY | 4 | henbon ongoing; agents; LinkedIn |
| `status` | claim set | CSV/`under_construction`; henbon ongoing “off-plan”; LinkedIn Jul 2026 shell complete / interiors; agents “under construction” / off-plan selling | 4 | henbon; LinkedIn; CSV; agents |
| `geography.city` | **CANONICAL** | Nairobi | 5 | henbon.co |
| `geography.neighbourhood_street` | **CANONICAL** | Westlands — **Westlands Road**, adjacent to / next to **GTC** | 5 | henbon product + ongoing (+ agents agree) |
| `geography.street_number` | developer social | **20 Westlands Road** | 4 | Henbon LinkedIn posts (Jan/Apr 2026) |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.267701, 36.806566** (`geo_method=geocode`) | 3 | Nominatim `20 Westlands Road` 2026-10-16 — prefer over CSV |
| `geography.lat_lng` | CSV lead — secondary | −1.26750, 36.81202 | 1 | CSV seed (~600 m E of geocode) — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-henbon-company-ltd` | 5 | henbon.co/about; Hauzisha “Henbon Company LTD” |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom; 3-Bedroom Penthouse/duplex; 4-Bedroom Penthouse + Study; 4-Bedroom Penthouse + Study + DSQ; 5-Bedroom Duplex / Penthouse + DSQ + Study | 5 | henbon ongoing + product pages |
| `unit_types` | secondary — **needs_verification** | Agent-only **3 Bedroom Duplex – Silver (127 sqm)** not on henbon product pages fetched | 2 | CPK; GNA; Flamingo |
| `size_by_type` | **CANONICAL** (developer product pages) | 1BR **68** sqm; 2BR **115–145** sqm; 3BR penthouse **134** sqm; 4BR+study **211** sqm; 4BR+study+DSQ **253** sqm; 5BR duplex **265** sqm | 5 | henbon product pages |
| `size_by_type` | secondary (agent splits / extras) | 2BR named **115 / 145 (ProMax+DSQ) / 146 (Golden+DSQ)**; 3BR Silver **127** sqm | 3 | CPK; GNA; Sir Francis; Thamana |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched | 0 | — |
| `building_specs.storeys` | claim set — **conflict** | Henbon LinkedIn: **25th and final floor** (shell) **vs** multi-agent **two 23-storey/floor towers** **vs** CPK **22 storey towers** | ≤3 | LinkedIn developer; Sir Francis; GNA; Thamana; CPK |
| `building_specs.wings_blocks` | secondary (agent consensus) | **Two** towers/blocks; **7 units per floor**; **3 basement** parking levels | 3 | Sir Francis; GNA; Amali (search); Thamana; CPK amenities |
| `total_units` | unknown | Not published on henbon pages fetched; agent “7/floor × floors” not computed here | 0 | — |
| `price_claims[]` | claim set — **`needs_developer_input`** on official “from”; **keep all options** | See §1a | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | henbon; all commercial |
| `payment_plan` | soft **CANONICAL** (existence) | Henbon About: pre-sale, mortgage, **installment plans** (no % schedule on site) | 4 | henbon.co/about |
| `payment_plan.deposit` | secondary — agent ≥4 — **needs_verification** vs developer (no %) | **20% deposit** (cash and/or instalment framing) | 3 | CPK; Azipa; Flamingo; Ace (indexed); Sir Francis “24 months” soft |
| `payment_plan.instalment_schedule` | secondary — **needs_verification** | Azipa detailed: 20% book → 10%×3 (3/5/8 mo) → 20% at 12 mo → 30% on completion (Dec 2027). CPK cash: 20%/30%/balance 60 days. Realtors.co.ke **5%/15%** plan diverges | ≤2 | Azipa; CPK; Realtors |
| `completion_estimate` | **CANONICAL** (product pages **agree**) | **September 2027** | 5 | henbon 1BR / 2BR / 3BR / 4BR / 5BR product pages |
| `completion_estimate` | secondary | Ongoing page “**2027**”; LinkedIn **Q3 2027**; agents Aug / Oct / Dec 2027; CSV Q3 2027 | ≤3 | henbon ongoing; LinkedIn; CPK; Hauzisha; Azipa; CSV |
| `amenities` (core) | **CANONICAL** | Cafés; heated pool; yoga room; fully fitted gym; reception + dedicated concierge; supermarket & shop; high-speed lifts; resident lounge; kids’ play area; ample parking; 24/7 CCTV; water borehole; 24/7 manned entrance security (product copy) | 5 | henbon.co/amenities; product pages |
| `amenities` | secondary / agent adds — **needs_verification** | Rooftop lounge; pharmacy/chemist; AI/smart toilets/automated curtains (CPK); face-scan (multi-agent, not on henbon amenities list fetched) | ≤2 | CPK; Sir Francis; GNA; Flamingo |
| `construction_progress` | claim set (developer LinkedIn) | Jan 2026: **7th floor**; Apr 2026: **17th floor** (“8 more to go”); Jul 2026: **25th and final floor** — shell complete, interiors next, on track Q3 2027 | 4 | Henbon Company LinkedIn |
| `availability_claim` | claim set — **conflict / needs_verification** | henbon ongoing: **80% of units remaining** **vs** Hauzisha “**2 units**” available | 2 | henbon; Hauzisha |
| `legal_title` | unknown | — | 0 | not found |
| `plot_size` | unknown | — | 0 | not found |

### 1a. Price claims — keep **all** options (no canonical scalar)

Official entry “from” disagrees across henbon pages → **`needs_developer_input`**. Typed product-page “starts from” values retained as developer options; agents retained separately.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Henbon ongoing “Prices Starting From” | **KES 8.84M** (also USD 68,264); “80% of units remaining”; completion 2027 | henbon.co/ongoing-projects | Official — **`needs_developer_input`** vs B |
| B | Henbon 1BR product “Price starts from” | 1BR **KES 9,340,000** (68 sqm); Sept 2027 | henbon.co/project/diamond-bay-1-bedroom | Official — **`needs_developer_input`** vs A |
| C | Henbon typed product pages (agree on these unit “from”s) | 2BR **15,375,000** (115–145 sqm); 3BR penthouse **17,420,000** (134); 4BR+study **27,430,000** (211); 4BR+study+DSQ **32,890,000** (253); 5BR duplex **34,450,000** (265); all Sept 2027 | henbon product URLs | Official typed “from” — keep; entry “from” still conflicted with A |
| D | Henbon LinkedIn Apr 2026 | 1BR 68 **9.34M**; 2BR 115 **14.87M**; 145 **17.9M**; 146 **18.02M**; Q3 2027; 17th floor | linkedin.com/company/henbon-company | Developer social (snapshot) |
| E | Henbon LinkedIn Jan 2026 (older) | 1BR from **8.8M**; 2BR 115 **14.3M**; 145 **17.4M**; 146 **17.5M**; 7th floor | LinkedIn | Older developer social — retain as historical option |
| F | CPK “Updated Standard Pricing (cash price)” | 1BR 68 from **8.84M**; 2BR 115 **14.875M**; Pro Max+DSQ 145 **17.9M**; Gold+DSQ 146 **18.02M**; 3BR Silver 127 **16.51M**; 3BR Gold 134 **17.42M**; 4BR+study 211 **27.43M**; 4BR+study+DSQ 253 **32.89M**; 5BR+study+DSQ 265 **34.45M**; completion Aug 2027 | commercialpropertykenya.com | Agent — dense; Silver **needs_verification** |
| G | GNA / Flamingo range tables | 1BR **8.84–9.84M**; 2BR 115 **14.375–15.675M**; Golden 146 **16.35–18.22M**; ProMax 145 **17.4–18.5M**; duplexes match F point prices; occupation Q3 2027 | gna.co.ke; flamingorealestate.co.ke | Agent |
| H | Sir Francis / Amali-style “from 8.7M” | 1BR from **8.7M**; 2BR 115 **14.8M**; 145 **18.2M**; 146 **18.5M**; up to 24 months | sirfrancismarketingltd.co.ke (+ Amali 500 skip) | Agent |
| I | Thamana | 1BR from **9.3M**; 2BR 115 **14.8M**; 145 **17.9M**; 146 **18.0M**; Aug 2027 | thamanamarketingagency.co.ke | Agent |
| J | Azipa | 1BR from **9.8M**; 2BR 115 **15.3M**; 145 **18.4M**; 146 **18.5M** | aziparealestate.co.ke | Agent |
| K | Hauzisha portal card | **KES 8.3M – 15.4M**; 1BR & 2BR only; Oct 2027; 2 units | hauzisha.co.ke | Portal — incomplete mix vs developer |
| L | CSV seed | `price_from_kes` **8,840,000** | seed | Unverified lead |
| M | Block.ke cross-mention | “from KES 8.7M” (on Golden Mansion related list only) | block.ke | Thin lead — CSV agent; no dedicated listing URL found |

**Canonical price:** none. Always `price_claims[]`.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| Installment / flexible plan **exists** | henbon.co/about (“installment plans”); multi-agent | Developer **≥1** | **Met via developer** | Soft **CANONICAL** (existence only; no %) |
| **20% deposit** | CPK (cash); Azipa schedule; Flamingo; Ace indexed snippet | **≥4** agents | Met as agent consensus | Secondary; **needs_verification** (developer silent on %) |
| Up to **24 months** | Sir Francis; Amali search; Realtors (variant) | ~2–3 | Below 4 alone | Soft secondary |
| Detailed Azipa schedule (10/10/10/20/30) | Azipa (+ Ace-like) | <4 independent dense | — | **needs_verification** |
| Developer LOO / % PDF | Not found on henbon this pass | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-henbon-company-ltd` |
| `legal_name` | Henbon Company LTD (as styled on henbon.co/about and Hauzisha) |
| `trading_names` | Henbon; Diamond Bay Residences (site brand — pages often speak as “Diamond Bay Residences” while About names Henbon Company LTD) |
| `website` | https://henbon.co/ |
| `evidence` | About: “Founded in 2011, Henbon Company LTD…”; Hauzisha “by Henbon Company LTD”; LinkedIn company henbon-company; prior projects listed on About |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV developer **blank** — filled from research, not seed |
| `prior_projects_mentioned` | Kadeya Villas (Ngong, 2012); Mideya Gardens (Riara Lane, 2015–2018); Diamond Homes (Othaya Road, 2017–2019); Nandwa Ivy Residence (Kileleshwa, 2024); Diamond Ivy Residence (Mandera Road, scheduled 2025 on About) — **delivery claims not independently verified this pass** (`needs_verification`) |
| `office_hint` | About: “Find Us at Nandwa Residence, Kileleshwa” |

**Primary developer = Henbon Company LTD (confidence 5).** Not CPK, Block, or other agents.

---

## 3. GroupCompany

**None.** No evidenced parent above Henbon. Do not invent from Instagram/TikTok “diamond.investment_” / “diamond_investments” handles without corporate proof.

---

## 4. RelatedParty

None required (no unproven brand-overlap marketing partner analogous to Astra/Laureland). Social handles noted under Sources evaluated/skipped only.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate (Loyd Mokaya) | agency | CSV sales_contact; **no dedicated Diamond Bay listing URL found** — only cross-mention “from KES 8.7M” on Golden Mansion page | https://block.ke/property/golden-mansion-for-sale-in-westlands-nairobi/ |
| CPK Real Estate | agency | Dense cash price list + cash payment plan; Aug 2027; “22 storey” | https://commercialpropertykenya.com/properties/diamond-bay-residence-westlands/ |
| Sir Francis Homes / Sir Francis Marketing | agency | Two 23-floor blocks; from 8.7M; up to 24 months | https://sirfrancismarketingltd.co.ke/properties/diamond-bay-residence-westlands/ |
| GNA Real Estate | agency | Full range + duplex table; Q3 2027 | https://gna.co.ke/project/diamond-bay-residence-1-2-3-4-and-5-beds-dsq-and-duplexes/ |
| Flamingo Real Estate | agency | Near-duplicate dense table; 20% deposit claim | https://www.flamingorealestate.co.ke/property/diamond-bay-residence/ |
| Azipa Real Estate | agency | Higher “from”; detailed instalment schedule to Dec 2027 | https://aziparealestate.co.ke/property/diamond-bay-residence-1-2-bedroom-apartments-for-sale-in-westlands-nairobi/ |
| Thamana Marketing Agency | agency | From 9.3M; 23-storey; Aug 2027 | https://thamanamarketingagency.co.ke/property/diamond-bay/ |
| Hauzisha | portal | Henbon Company LTD; Oct 2027; 8.3–15.4M; 2 units; 1–2BR only | https://hauzisha.co.ke/developments/diamond-bay-residences/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 716 333 355 | Developer (henbon.co footer) |
| email | Marketing@henbon.co | Developer |
| email | info@henbon.com | Developer (appears on some henbon page footers in search/index) |
| phone | +254 768 008 888 | Developer / project (search-indexed ongoing footer; LinkedIn Jan) |
| phone | +254 726 998 888 / +254 712 000 088 / +254 700 330 486 | Developer social (LinkedIn posts — verify current) |
| url | https://henbon.co/ | Developer |
| url | https://henbon.co/ongoing-projects | Property |
| address | 20 Westlands Road, Westlands, Nairobi | Property (LinkedIn) |
| phone | +254 725 937 686 | Agent: Block / Loyd Mokaya (CSV) |
| email | loyd@block.ke | Agent: Block (CSV) |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 722 720 812 | Agent: Sir Francis |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 712 406 060 / +254 782 406 060 | Agent: GNA |
| email | support@gna.co.ke | Agent: GNA |
| phone | +254 714 737 748 | Agent: Flamingo |
| email | info@flamingorealestate.co.ke | Agent: Flamingo |
| phone | +254 742 880 335 / +254 796 007 755 | Agent: Azipa |
| email | info@aziparealestate.co.ke / azipahomes@gmail.com | Agent: Azipa |
| phone | +254 795 343 833 | Agent: Thamana |
| phone | +254 730 731 355 | Portal: Hauzisha |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| — | — | No named contractor / architect / financier / land vendor on henbon pages this pass | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Entry price “from”** | henbon ongoing **8.84M** vs henbon 1BR product **9.34M** | **Official vs official** → **`needs_developer_input`**. No canonical scalar. |
| 2 | **Typed prices over time** | LinkedIn Jan (8.8 / 14.3…) vs Apr (9.34 / 14.87…) vs live product pages (9.34 / 15.375…) vs agents 8.7–9.8M | Keep all in `price_claims[]`; prefer live henbon product pages as current developer typed claims but do not collapse entry “from”. |
| 3 | **Storeys / floors** | LinkedIn **25th final floor** vs agents **23** vs CPK **22** | Highlight all; no website storeys page. No invented winner. |
| 4 | **Completion month** | Product pages **September 2027** (agree) vs agents Aug/Oct/Dec vs ongoing “2027” | **Canonical = September 2027** (agreeing product pages). Agents secondary. |
| 5 | **Unit mix completeness** | Developer 1–5 BR + penthouses/duplexes vs Hauzisha **1BR & 2BR only** | Canonical mix = developer; Hauzisha incomplete. |
| 6 | **3BR Silver 127 sqm / 16.51M** | Agents only; not on henbon product pages fetched | **Show** + **`needs_verification`** |
| 7 | **Availability** | henbon **80% remaining** vs Hauzisha **2 units** | Conflict; both **needs_verification** for live inventory |
| 8 | **Deposit %** | Agents ≥4 say **20%**; developer silent on % | Soft installment existence = developer; **20%** secondary |
| 9 | **CSV developer blank / Block contact** | Seed ≠ Henbon | Split Contact.owner; CSV lead only |
| 10 | **Amenities inflation** | CPK AI toilets/curtains; face-scan multi-agent vs henbon amenities list | Core = henbon amenities; extras **needs_verification** |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~16** |
| `sources_retained` | **12** |

**Selection note:** Scanned henbon home, about, amenities, ongoing, six product pages, LinkedIn progress posts, CPK, Sir Francis, GNA, Flamingo, Azipa, Thamana, Hauzisha, Block cross-link, Amali (500), Ace (404), Realtors.co.ke (anomalous 5% plan), CSV seed. **Always kept** developer henbon stack. Retained 12 richest (≥5 rule).

**Thin / skipped (not in retained list):**
- https://amaliproperties.co.ke/property/diamond-bay-residence-westlands/ — **HTTP 500** this pass
- Ace Realtors URL from search — **404** this pass (indexed payment snippet used only as corroboration note, not retained)
- https://realtors.co.ke/property/chic-city-living-2-bedroom-apartment-in-prime-westlands/ — anomalous **5%/15%** cash plan; thinner than CPK/Azipa
- https://block.ke/…golden-mansion… — CSV agent cross-mention only; no dedicated Diamond Bay page
- https://henbon.co/ — home softer than ongoing + about + amenities (fields covered by retained developer URLs)
- CSV NBO-007 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://henbon.co/ongoing-projects | Henbon Company LTD | developer | 2026-10-16 | Off-plan framing; from **8.84M**; 80% remaining; unit-type index; Westlands/GTC |
| 2 | https://henbon.co/about | Henbon Company LTD | developer | 2026-10-16 | Legal-style **Henbon Company LTD**; track record; installment language |
| 3 | https://henbon.co/amenities | Henbon Company LTD | developer | 2026-10-16 | Core amenity list — always keep |
| 4 | https://henbon.co/project/diamond-bay-1-bedroom | Henbon | developer | 2026-10-16 | 68 sqm; from **9.34M**; Sept 2027 |
| 5 | https://henbon.co/project/diamond-bay-2-bedroom | Henbon | developer | 2026-10-16 | 115–145 sqm; from **15.375M**; Sept 2027 |
| 6 | https://henbon.co/project/diamond-bay-3-bedroom-penthouse | Henbon | developer | 2026-10-16 | 134 sqm; from **17.42M**; Sept 2027 |
| 7 | https://henbon.co/project/diamond-bay-4-bedroom-penthouse-study | Henbon | developer | 2026-10-16 | 211 sqm; from **27.43M** |
| 8 | https://henbon.co/project/diamond-bay-4-bedroom-penthouse-study-dsq | Henbon | developer | 2026-10-16 | 253 sqm; from **32.89M** |
| 9 | https://henbon.co/project/diamond-bay-5-bedroom-duplex | Henbon | developer | 2026-10-16 | 265 sqm; from **34.45M** |
| 10 | https://commercialpropertykenya.com/properties/diamond-bay-residence-westlands/ | CPK Real Estate | agent | 2026-10-16 | Full cash price table; cash plan; 22-storey claim |
| 11 | https://sirfrancismarketingltd.co.ke/properties/diamond-bay-residence-westlands/ | Sir Francis Homes | agent | 2026-10-16 | Two **23**-floor blocks; 7/floor; 24 months; from 8.7M |
| 12 | https://hauzisha.co.ke/developments/diamond-bay-residences/ | Hauzisha | portal | 2026-10-16 | **Henbon Company LTD**; Oct 2027; inventory “2 units” |

**Also used for claims (cited in body; not double-counted in retained 12):**
- https://gna.co.ke/project/diamond-bay-residence-1-2-3-4-and-5-beds-dsq-and-duplexes/ — duplex ranges (overlaps Flamingo/CPK)
- https://www.flamingorealestate.co.ke/property/diamond-bay-residence/ — 20% deposit corroboration
- https://aziparealestate.co.ke/property/diamond-bay-residence-1-2-bedroom-apartments-for-sale-in-westlands-nairobi/ — instalment schedule
- https://thamanamarketingagency.co.ke/property/diamond-bay/ — 9.3M / 23-storey
- Henbon LinkedIn posts (company henbon-company): address **20 Westlands Road**; floor progress 7 → 17 → 25; price snapshots — retained as **construction_progress** evidence (developer social)

---

## 9. Field harvest → must-have extension proposals

| Field | Diamond Bay status | Harvest note |
|-------|-------------------|--------------|
| `canonical_name` / aliases | OK | Residences vs Residence |
| `status` | OK as claim set | Shell complete (LinkedIn) vs still marketed off-plan |
| `geography` street + landmark (GTC) | OK | Street number **20** from developer LinkedIn — propose promote when on official web too |
| `geography.lat_lng` | CSV only | Do **not** promote; needs developer geo |
| `primary_developer` | OK | CSV blank → Henbon Company LTD (5) |
| GroupCompany | none | Correctly empty |
| `unit_types` + penthouse/duplex variants | OK | Developer product matrix dense |
| `size_by_type` | OK | All major types on henbon product pages |
| `size_measure_tag` | unknown | Still missing |
| `storeys` / floors | Claim set | LinkedIn 25 vs agent 23 vs CPK 22 — reinforces **storeys as claim set** proposal |
| `price_claims[]` | All options A–M | Official **8.84M vs 9.34M** → **`needs_developer_input`**; strengthens dual-band / multi-claim rule |
| `payment_plan` | Soft existence canonical; **20%** agent ≥4 | Developer installment language without % — harvest: distinguish `payment_plan.exists` vs `deposit_pct` |
| `completion_estimate` | **September 2027** canonical | Product pages agree |
| `construction_progress` | LinkedIn timeline retained | Reinforces candidate must-have when developer publishes progress (here via social, not tracker page) |
| `availability_claim` | 80% vs 2 units | Show + verify; do not collapse |
| amenities core | OK | Reject uncorroborated agent adds |
| Named contractor | none | — |
| `street_number` when developer-sourced | **Propose** capture | 20 Westlands Road (LinkedIn) |

**Consensus bump suggestions (for coordinator / schema living table):**
- `storeys` claim set: Diamond Bay adds evidence → toward **2/n** with Galaxy
- `construction_progress`: LinkedIn milestones count when no tracker microsite
- Split **payment_plan.exists** (developer soft OK) vs **deposit_pct** (needs % or ≥4 agents)
- Official entry-price conflict pattern (ongoing vs product page) → same **`needs_developer_input`** treatment as Galaxy dual bands

---

## Open questions (developer input)

1. Reconcile live entry **from KES 8.84M** (ongoing) vs **9.34M** (1BR product page) and publish one LOO/price list.
2. Confirm **storeys**: 22 vs 23 vs **25** (LinkedIn final floor)?
3. Is **3BR Silver 127 sqm / 16.51M** a current official type?
4. Binding **deposit %** and instalment schedule (PDF/LOO)?
5. Live inventory: **80% remaining** vs Hauzisha **2 units**?
6. Publish **gross vs plinth** size tags; confirm GPS for 20 Westlands Road.
7. Legal entity spelling **LTD** vs Limited; Companies Registry name; relationship of diamond.investment social handles.
