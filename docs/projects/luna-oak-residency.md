---
slug: luna-oak-residency
external_id: NBO-012
wave: C
cycle: scale-half
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Luna Oak Residency (NBO-012) — Wave C / scale

CSV seed (unverified leads): location **Kilungu Road, off Elgeyo Marakwet Road, Kilimani, Nairobi**; stage `under_construction`; completion **Q3 2029**; `price_from_kes` **11,500,000**; sales_contact **NRE Real Estate** (+254 141 361 320, info@nairobirealestate.co.ke); developer **blank**.

Live research accessed **2026-10-16**: Oak Group Residences project site + NEMA ESIA Full Study (Dec 2025) + multi-agent/portal listings.

**Method locks applied:**
- Developer vs agents: if developer/official sources **agree** → **canonical = developer/official**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`**; no assumed winner.
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agent sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**.
- CSV = unverified leads only. CSV sales_contact ≠ developer.
- Unproven brand vs legal proponent → **`marketing_partner`** (not GroupCompany).

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = official/developer sources **agree**. Claim set / secondary = conflict detection. **`needs_developer_input`** = official pages/filings disagree.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** (marketing brand) | Luna Oak Residency | 5 | oakgroup.co.ke; multi-agent |
| `aliases` | secondary | Luna Oak; Luna Oak Residences; Luna Oak Kilimani | 4 | agents; CPK images; forum |
| `status` | claim set | CSV/`under_construction`; NRE **Under Construction ~10%** (agent widget); Oak Group **Ongoing Developments**; agents off-plan / new development | 3 | NRE; oakgroup ongoing; CSV — 10% progress **`needs_verification`** (single agent UI) |
| `geography.city` | **CANONICAL** | Nairobi | 5 | NEMA ESIA; oakgroup |
| `geography.neighbourhood_street` | **CANONICAL** | Kilimani — **Kilungu Road** (CSV also: off **Elgeyo Marakwet Road**; NEMA: access via **Elgeyo** and Kilungu; opposite **Oyster Bay**; neighboring **Cavina School**) | 5 | NEMA; oakgroup; agents; CSV |
| `geography.plot` | **CANONICAL** (filing) | **L.R. No. Nairobi/Block 17/283** | 5 | NEMA ESIA |
| `geography.lat_lng` | **CANONICAL** (official filing) | **−1.293751, 36.777031** | 5 | NEMA ESIA GPS |
| `geography.site_area_sqm` | **CANONICAL** (filing) | **4,046.43 sqm** | 5 | NEMA Table 4 |
| `primary_developer_id` | **CANONICAL** (filing proponent) | → `dev-mingland-company` (**Mingland Company Limited**) | 5 | NEMA ESIA Client/proponent |
| `marketing_brand` | RelatedParty | **Oak Group Residences** (oakgroup.co.ke) — see §4 | 4 | oakgroup; agents “OAK Collection” |
| `unit_types` | **CANONICAL** (band — filing + marketing agree on 2/3/4 BR) | **2 Bedroom; 3 Bedroom; 4 Bedroom** (select **+ DSQ**) | 5 | NEMA (“4, 3 and 2 bedrooms”); oakgroup; agents |
| `size_by_type` | secondary agent tables (no size schedule on oakgroup HTML) | 2BR **115 sqm**; 3BR **153 / 158 / 160 sqm**; 3BR+DSQ **209 / 211 sqm**; 4BR+DSQ **247 / 256 sqm** | 3 | NRE; Vorsa; Rose; Flamingo; CPK; BuyRent |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched; brochure CTA not opened | 0 | — |
| `total_units` | **CANONICAL** (filing + marketing **agree**) | **294** | 5 | NEMA; oakgroup; multi-agent |
| `building_specs.storeys` | **CANONICAL** (filing + marketing **agree** on 25) | **25** floors / storeys; units from **3rd to 25th** (oakgroup) | 5 | NEMA; oakgroup |
| `building_specs.towers_blocks` | claim set — **`needs_developer_input`** / detail | NEMA narrative: **twin-tower**, each 25 floors + **2 basement** levels. NEMA Table 4 also schedules **Tower A / B / C / D** areas (same filing). Marketing often “25-storey **tower**” (singular) | 3 | Official internal wording density — flag; do not invent which “twin” vs A–D is marketing-facing |
| `built_up_area_sqm` | **CANONICAL** (filing) | **73,997.02** total built-up (NEMA Table 4) | 5 | NEMA |
| `parking` | claim set — **CONFLICT** | NEMA: **two levels of basement parking**. Agents: **five levels** of secure parking | 2 | Official vs agent — canonical basement **2** from NEMA; agent “5 levels” **`needs_verification`** |
| `price_claims[]` | claim set — keep **all**; Oak Group “from” conflict → **`needs_developer_input`** | See **§1a** | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | all commercial |
| `payment_plan.deposit` | secondary — threshold **not met** | Agent claims **20% deposit**, balance over construction (NRE; BuyRentKenya). Others only “flexible”. **No developer payment text** on oakgroup page this pass | ≤3 | **Below** ≥4 agent agree **and** no developer source → **not** locked must-have |
| `completion_estimate` | claim set — **CONFLICT** | NRE/CPK/BuyRent: **September 2029**; CSV **Q3 2029**; Vorsa **Q4 2028**; Own It **2028**; Rose **TBA**. Oak Group HTML **silent** this pass | ≤3 | No agreeing developer date → no canonical |
| `amenities` (core — Oak Group page) | **CANONICAL** (developer marketing list) | Central community garden; courtyard garden; elegant main lobby; fully equipped gym; game room; **heated swimming pool**; indoor kids play; landscaped walking paths; multi-purpose hall; outdoor children’s play; private cinema; yoga room | 5 | oakgroup.co.ke/properties/luna-oak-residency |
| `amenities` | secondary agent adds — **`needs_verification`** where not on Oak list | Jogging track; clubhouse/lounge; borehole; backup generator; high-speed lifts; 24/7 CCTV (NRE/Vorsa/CPK/Flamingo) | ≤3 | Show; prefer Oak list as core |
| `project_cost_estimate` | secondary filing | **KES 2,408,649,520** total estimated cost (NEMA) | 4 | NEMA §1.9 |
| `legal_title` / tenure | unknown on marketing | Land-use change from single-dwelling to multi-dwelling applied (NEMA) — not a title claim | 2 | NEMA narrative |
| `construction_progress` | secondary | NRE widget **10%** — **`needs_verification`** | 1 | NRE only |

### 1a. Price claims — keep **all** options (no canonical scalar)

Oak Group live “from” figures **disagree across own surfaces** (project page fetch **14.8M** vs listings/ongoing/search **11.9M**) → **`needs_developer_input`**. Agents diverge into lower (~11.5M) and higher (~12.2M / 14.8M+) bands.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Oak Group project page (live fetch 2026-10-16) | **From KES 14,800,000** | oakgroup.co.ke/properties/luna-oak-residency | Official — **`needs_developer_input`** vs B |
| B | Oak Group listings / ongoing / agent card | **From KES 11,900,000** | oakgroup.co.ke/listings/apartments; /ongoing-developments; /agents/luna-oak-residency | Official — **`needs_developer_input`** vs A |
| C | NRE / Vorsa / Rose / Flamingo (aligned lower table) | 2BR 115 **from 11.5M**; 3BR 153 **14.3M** / 158 **15.8M** / 160 **16M**; 3+DSQ 209 **20.9M** / 211 **21.1M**; 4+DSQ 247 **24.7M** / 256 **25.6M** | nairobirealestate; vorsagroup; rosehomes; flamingo | Secondary |
| D | CPK (modified 2026-09-27) | 2BR 115 **from 12.2M**; 3BR 153 **14.8M** / 158 **16.7M** / 160 **17M**; 3+DSQ **22.2 / 22.4M**; 4+DSQ **26.2 / 27.1M** | commercialpropertykenya.com | Secondary |
| E | BuyRentKenya (Leonard Kamau) | Same **higher** band as D (no 2BR row; 3BR from **14.8M**) | buyrentkenya.com | Secondary |
| F | CSV seed | `price_from_kes` **11,500,000** | seed | Unverified lead |

**Canonical price:** none.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **20% deposit** + balance over construction | NRE; BuyRentKenya | **2** | **Not met** | Secondary; **`needs_verification`** |
| “Flexible” off-plan / during construction (no %) | CPK; Vorsa; Flamingo; Own It; Rose (vague) | ≥4 vague | Vague ≠ deposit % lock | Soft secondary only |
| Developer LOO / oakgroup payment schedule | **None** on fetched HTML (brochure CTA present, PDF not fetched) | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-mingland-company` |
| `legal_name` | **Mingland Company Limited** |
| `trading_names` | none evidenced beyond legal name |
| `website` | **none found** under Mingland this pass |
| `address` | P.O. Box **25050-00603**, Nairobi (NEMA Client block) |
| `evidence` | NEMA ESIA Full Study (Dec 2025) — Client / proponent for 25-storey / 294-unit scheme on **Nairobi/Block 17/283**, Kilungu Road. SkyscraperCity thread titles the same plot/spec as **Luna Oak** and names Mingland as developer (forum corroboration of brand↔filing link). |
| `group_company_id` | **null — none invented** |
| `developer_confidence` | **5** as **filing proponent**; brand packaging via Oak Group is separate (§4) |

**CSV developer blank** — correct; do not invent from NRE.

---

## 3. GroupCompany

**None.** No evidenced parent above Mingland or Oak Group.

---

## 4. RelatedParty

| Name | `relationship_type` | Evidence | Conf |
|------|---------------------|----------|-----:|
| **Oak Group Residences** (oakgroup.co.ke) | **`marketing_partner`** (locked default until parent/alias/co-developer proven) | Project microsite; “Talk To The Developer” contacts; lists Luna Oak under Ongoing Developments; agents cite “OAK Collection” | 4 |

Do **not** treat Oak Group as proven legal parent of Mingland without filings. Dual listing as `co_developer` **not** applied — no co-named “Developers” block like Porini; Oak is marketing brand, Mingland is EIA proponent.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| NRE Real Estate | agency | CSV sales_contact; price table; Sep 2029; 20% calculator; 10% progress UI | https://nairobirealestate.co.ke/properties/luna-oak-residency |
| VorsaGroup Real Estate | agency | Full price table; **Q4 2028** completion | https://vorsagroup.co.ke/property/luna-oak-residency-luxury-2-3-4-bedroom-apartments-for-sale-in-kilimani-nairobi/ |
| Rose Homes | agency | Detailed typed prices; completion TBA | https://rosehomes.co.ke/luna-oak-residency-apartments-for-sale-in-kilimani |
| CPK Real Estate | agency | Higher price band; Sep 2029 | https://commercialpropertykenya.com/properties/luna-oak-residency-in-kilimani/ |
| BuyRentKenya / Leonard Kamau | portal listing | Higher band; **20%** deposit; Sep 2029 | https://www.buyrentkenya.com/listings/3-bedroom-apartment-for-sale-kilimani-4041025 |
| Flamingo Real Estate | agency | Lower price bands; flexible plans | https://www.flamingorealestate.co.ke/property/luna-oak-residency-apartments-kilimani/ |
| Own It Kenya | agency / blog | 2028 completion; flexible plans; 11.5M framing | https://ownitkenya.com/off-plan-apartments-in-kilimani/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| email | oakgroup2010@gmail.com | Oak Group / project sales (developer marketing) |
| phone | +254 110 378 960 (Wally) | Oak Group |
| phone | +254 725 365 466 (Mei) | Oak Group |
| phone | +254 796 362 145 (Sue) | Oak Group |
| phone | +254 798 868 888 | Luna Oak / Oak Group listing contact |
| email | info@oakgroup.co.ke | Oak Group (agent card) |
| url | https://oakgroup.co.ke/properties/luna-oak-residency/ | Property marketing |
| address | P.O. Box 25050-00603, Nairobi | Developer: Mingland (NEMA) |
| phone | +254 141 361 320 | Agent: NRE (CSV) |
| email | info@nairobirealestate.co.ke | Agent: NRE (CSV) |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: VorsaGroup |
| email | info@vorsagroup.co.ke | Agent: VorsaGroup |
| phone | +254 700 051 765 | Agent: Rose Homes |
| email | laizzwamboi@gmail.com | Agent: Rose Homes |
| phone | +254 784 448 888 | Agent: CPK |
| phone | +254 706 327 148 | BuyRentKenya listing agent |
| phone | +254 714 737 748 | Agent: Flamingo |
| phone | +254 722 716 182 / +254 720 469 282 | Agent: Own It |
| email | sales@ownitkenya.com | Agent: Own It |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Lakers Consultancy Limited** (LCL; email k.musiega@lakersconsultancy.co.ke) | other (NEMA lead expert / ESIA consultant) | NEMA ESIA “Prepared By” / appointed firm of experts | 4 |
| Unnamed contractor | — | Not named this pass | 0 |

No financing partner / architect named this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Legal developer vs marketing brand** | NEMA proponent **Mingland Company Limited** vs Oak Group “Talk To The Developer” | Canonical **filing proponent = Mingland**. Oak Group = **`marketing_partner`**. Relationship unproven. |
| 2 | **Oak Group “price from”** | Live project page **14.8M** vs listings/ongoing **11.9M** | **Official vs official** → **`needs_developer_input`**. Keep both in `price_claims[]`. |
| 3 | **Agent price tables** | Lower band ~11.5–25.6M (NRE/Vorsa/Rose/Flamingo) vs higher ~12.2–27.1M (CPK/BuyRent) | Keep **all** options; no scalar. |
| 4 | **Completion** | Sep/Q3 2029 vs Q4 2028 / 2028 vs TBA; developer page silent | Claim set; **`needs_verification`** / later developer input. |
| 5 | **Parking levels** | NEMA **2 basement** vs agents **5 levels** | Canonical structural = **2 basement** (filing). Agent 5 **`needs_verification`**. |
| 6 | **Tower count wording** | NEMA “twin-tower” + Table 4 Towers A–D vs marketing singular “tower” | Flag filing complexity; **`needs_developer_input`** for public block-count wording. |
| 7 | **Payment** | 20% (2 agents) vs flexible-only (≥4) vs unknown on developer HTML | Must-have **not** met; show 20% as secondary. |
| 8 | **Construction progress** | NRE 10% only | **`needs_verification`**. |
| 9 | **CSV sales_contact** | NRE ≠ Oak Group / Mingland phones | Split Contact.owner. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned Oak Group project + listings/ongoing, NEMA ESIA PDF, NRE, Vorsa, Rose, CPK, BuyRentKenya, Flamingo, Own It, SkyscraperCity forum, Oak Group agent card, plus CSV. **Always kept** developer marketing site + official NEMA filing. Retained 10 densest (≥5 rule).

**Thin / skipped (not in retained list):**
- https://www.skyscrapercity.com/threads/luna-oak-kilimani-25-25-fl-u-c.2445348/ — useful Mingland↔Luna name corroboration; forum not retained as primary cite (noted in §2)
- https://oakgroup.co.ke/agents/luna-oak-residency/ — contact duplicate of listings
- Brochure PDF behind oakgroup “Download Brochure” — **not fetched** this pass
- CSV NBO-012 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://oakgroup.co.ke/properties/luna-oak-residency/ | Oak Group Residences | developer_marketing | 2026-10-16 | 294 units; 25 floors; amenities; live **from 14.8M**; contacts — always keep |
| 2 | https://nema.go.ke/wp-content/uploads/2026/02/ENVIS-00400-EIA-2423_Apartments-in-Kilimani-Nairobi.pdf | NEMA / Mingland / Lakers Consultancy | official_filing | 2026-10-16 | ESIA Dec 2025; Mingland; Block 17/283; 294/25; GPS; BUA 73,997 — always keep |
| 3 | https://oakgroup.co.ke/listings/apartments/ | Oak Group Residences | developer_marketing | 2026-10-16 | **From 11.9M** conflict vs project page |
| 4 | https://nairobirealestate.co.ke/properties/luna-oak-residency | NRE | agent | 2026-10-16 | CSV contact; price table; Sep 2029; 20%; 10% UI |
| 5 | https://vorsagroup.co.ke/property/luna-oak-residency-luxury-2-3-4-bedroom-apartments-for-sale-in-kilimani-nairobi/ | VorsaGroup | agent | 2026-10-16 | Full price table; **Q4 2028** |
| 6 | https://rosehomes.co.ke/luna-oak-residency-apartments-for-sale-in-kilimani | Rose Homes | agent | 2026-10-16 | Typed prices; TBA completion |
| 7 | https://commercialpropertykenya.com/properties/luna-oak-residency-in-kilimani/ | CPK | agent | 2026-10-16 | Higher price band; Sep 2029 |
| 8 | https://www.buyrentkenya.com/listings/3-bedroom-apartment-for-sale-kilimani-4041025 | BuyRentKenya | portal | 2026-10-16 | Higher band; **20%** deposit; Sep 2029 |
| 9 | https://www.flamingorealestate.co.ke/property/luna-oak-residency-apartments-kilimani/ | Flamingo | agent | 2026-10-16 | Lower price bands; flexible plans |
| 10 | https://ownitkenya.com/off-plan-apartments-in-kilimani/ | Own It Kenya | agent | 2026-10-16 | 2028 completion; flexible; 11.5M framing |

---

## 9. Field harvest

| Field | Luna Oak status | Notes |
|-------|-----------------|-------|
| canonical_name / aliases | OK | Oak Group + agents |
| status | Claim set | UC; NRE 10% weak |
| geography + plot + lat_lng | OK (NEMA) | GPS developer/filing-sourced — promote must when official |
| primary_developer | OK | **Mingland Company Limited** (filing) |
| Oak Group | `marketing_partner` | Unproven Mingland link |
| unit_types / total_units / storeys | OK agree | 2/3/4 BR; **294**; **25** |
| towers / parking | Claim set / conflict | Twin vs A–D; 2 basement vs agent 5 |
| `built_up_area_sqm` | OK filing | 73,997 |
| `price_claims[]` | A–F retained | Official from 14.8 vs 11.9 → **`needs_developer_input`** |
| `payment_plan` | **Not** must-have yet | Only 2 clear 20% sources |
| amenities core | OK Oak list | Reject uncorroborated agent adds as canonical |
| completion_estimate | Conflicted claim set | No developer date on HTML |
| Named ESIA consultant | Captured | Lakers Consultancy |

### Proposed consensus bumps (coordinator / schema)

| Proposed | This project | Note |
|----------|--------------|------|
| Official **NEMA/ESIA** when no Mingland microsite | Luna Oak | Reinforce “always keep filing” |
| Filing **GPS** + **plot LR** + **BUA** | Luna | GPS must-when-official; BUA optional→propose |
| Brand site vs filing proponent → `marketing_partner` | Oak Group vs Mingland | Same pattern as unproven brand overlap |
| Payment **not** locked when only 2 agents name % | Luna 20% | Negative example vs Misty ≥4 |

---

## Open questions (verification / developer input)

1. Prove **Oak Group ↔ Mingland** relationship (same SPV, affiliate, or sales agent only)?
2. Reconcile Oak Group **from 11.9M vs 14.8M** (and agent lower vs higher tables).
3. Publish binding **payment plan** / LOO (is **20%** real?).
4. Confirm **completion** (Sep 2029 vs Q4 2028).
5. Clarify **twin-tower vs Towers A–D** marketing description; parking **2 basement vs 5 levels**.
6. Fetch **brochure PDF** for gross/plinth size tags and amenity schedule.
7. Named **contractor** / architect?
