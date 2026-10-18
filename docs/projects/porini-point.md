---
slug: porini-point
external_id: NBO-004
cycle: 2
pilot: false
retrofit: cycle-2-locks-2026-10-16
sources_evaluated: 13
sources_retained: 10
last_verified_at: 2026-10-16
---

# Porini Point (NBO-004) — Cycle 2 (retrofit)

CSV seed (unverified leads): location Tatu City, Ruiru, Kiambu County; lat/lng −1.15703, 36.88792; stage `off_plan`; completion Q1 2027 (final phase Q3 2029); `price_from_kes` 7,610,000; sales_contact Block/Loyd Mokaya; developer “Rendeavour (Tatu City)”.

Live research: official project site + official brochures/packs + Tatu City launch release + agents/portals accessed **2026-10-15**; **Cycle 2 locks retrofit 2026-10-16**.

**Method locks applied:**
- Conflicts always highlighted.
- **Developer vs agents:** if developer sources **agree** on a field → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume a winner** → flag **`needs_developer_input`**; no canonical among disagreeing official figures until verification resolves it.
- Co-named “Developers” (Rendeavour + Tatu City Limited) → model as **both** `co_developer` **and** RelatedParty.
- **Prices:** always keep full `price_claims[]` (all options).
- Payment must-have if ≥4 independent agent/portal sources **or any developer source**.
- Low-confidence / agent-only / uncorroborated → show with **`needs_verification`**. No invented GroupCompany.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed value only where official sources **agree**. Official disagreements → claim set + **`needs_developer_input`** (no assumed canonical). Secondary = agent/portal claims.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Porini Point | 5 | porinipoint.com, brochures, Tatu City news |
| `aliases` | secondary | Porini Point apartments; Porini Point Tatu City | 4 | agents / press |
| `status` | claim set | CSV `off_plan`; Tatu City news: launched 19 Nov 2025, **“first phase sold out on launch night”**; Craiova “under construction”; FAQ search-index: construction start Jan 2026 (**page 404**) | 4 launch / 2 UC label / 1 FAQ start | See §7 |
| `geography.city_context` | **CANONICAL** | Within **Tatu City** (5,000-acre master-planned city / SEZ framing on official copy) | 5 | site, brochures, news |
| `geography.neighbourhood` | **CANONICAL** | Hillside at edge of planned **Tatu Wildlife Sanctuary** (~160 acres per launch news) | 5 | site, brochures, news |
| `geography.county` | secondary consensus | **Kiambu County** (Ruiru / Thika corridor) — CSV + Block + Vorsa; not a single county line on porinipoint.com HTML extract | 3–4 | CSV, Block, Vorsa |
| `geography.lat_lng` | CSV — **needs_verification** | **−1.15703, 36.88792** (`geo_method=csv`) | 2 | CSV seed; not developer-sourced — [geo-enrichment.md](../db/geo-enrichment.md) |
| `geography.lat_lng` | geocode check (not recommended) | −1.150814, 36.901062 | 1 | Tatu City suburb centroid — too coarse for plot |
| `primary_developer_id` | **CANONICAL** | → `dev-rendeavour` | 5 | brochures; launch news |
| `co_developer_ids[]` | **locked dual model** | → `dev-tatu-city-limited` (**also** RelatedParty §4) | 4 | Property-pack disclaimer: both “the Developers” |
| `unit_types` | **CANONICAL** | **1-, 2-, and 3-bedroom** apartments | 5 | site, brochures, news |
| `unit_count` | **CANONICAL** | **570** units | 5 | launch news (+ agents echo) |
| `building_specs.blocks` | **CANONICAL** | **24** apartment buildings / blocks, landscaped courtyard | 5 | brochures, news |
| `building_specs.floors` | secondary — **`needs_verification`** | **G+4** (Block; also FAQ search-index while live FAQ **404**) | 2 | Not in brochure text extract / launch HTML |
| `building_specs.built_up_area` | **CANONICAL** | **~58,000 sqm** total built-up | 5 | launch news |
| `size_by_type` | **CANONICAL** (brochure / info-pack “Total area”) | 1BR **54 sqm**; 2BR **90 sqm** (Type 01 & 02); 3BR **145 sqm**. Measure tag **gross vs plinth: unknown** (materials say “Total area” only) | 5 | brochures; info-pack |
| `price_claims[]` | claim set — **OFFICIAL vs OFFICIAL** → **`needs_developer_input`** | **No single canonical price_from.** Keep **all** options (see §7 table). Live site from **KES 7,610,000**; launch news from **KES 7.5M**; info-pack cash/2-yr tables; property pack from **KES 5.9M**; plus agent bands | ≤5 per claim; no winner among official | |
| `currency` | **CANONICAL** | KES (also USD/GBP/EUR columns on info-pack) | 5 | site, packs |
| `payment_plan.tenor` | claim set — **OFFICIAL vs OFFICIAL** → **`needs_developer_input`** | **24-month / 2-year** (launch news, info-pack, agents) **vs** property pack **up to 3 years**. Must-have **met** (developer publishes payment plans); **no assumed canonical tenor** among disagreeing official figures | 5 each official claim; no collapsed canonical | |
| `payment_plan.cash_incentives` | soft developer claim | Cash incentives / discounts (launch news); FAQ-index up to 10.7% (**404**) → % **`needs_verification`** | 4 / 1 | |
| `payment_plan.sharia` | developer availability claim | Sharia-compliant financing options available (launch news) | 5 availability / terms unknown | |
| `payment_plan.deposit` | secondary / **`needs_verification`** | FAQ search-index (page **404**): reservation **USD 1,550** then **10% deposit** within 14 days. Block **~20%** estimate — agent-only | 1 FAQ / 2 Block | |
| `completion_estimate` | **CANONICAL** | First apartments **Q1 2027**; entire development **September 2029** | 5 | launch news (no conflicting official date found) |
| `completion_estimate` | secondary — **CONFLICT / `needs_verification`** | Craiova: Phase 1 **Dec 2026**, Phase 2 Dec 2027; CSV “final phase Q3 2029” vs official Sep 2029 | 2 | |
| `amenities` (core) | **CANONICAL** | Clubhouse; gym; swimming pool (+ sun deck on brochure); barbecue area; children’s play zone; parking; 24/7 CCTV / gated security; landscaped courtyards / paths | 5 | launch news + brochures |
| `amenities` non-canonical | reject from core | Vorsa feature tags: heated pool, high-speed lifts, library, retail centre, open chicken restaurant — **not on developer materials** | 1 | Vorsa only |
| `interior_finishes` | **CANONICAL** | Fitted kitchen hob/hood/oven; quartz countertops; SPC parquet; contemporary bathrooms; private balconies | 5 | launch news; brochure |
| `legal_title` | partial / **`needs_verification`** for project-specific lease | Info-pack: foreigners own under **leasehold**, max **99 years** (Constitution Art. 65(1) cited). FAQ search-index lease wording truncated (**404**). Block: confirm tenure in sale agreement | 3 general / 1 project deed | |
| `foreign_ownership` | **CANONICAL** (marketing claim) | Fully eligible for foreign ownership under Kenyan law (brochure) | 5 claim / legal diligence TBD | brochure |
| `showroom / sales` | **CANONICAL** contact channel | **Tatu Experience Centre**; PoriniSales@tatucity.com; +254 709 441 144 | 5 | brochures, site |

### Size table (measure tag)

| Unit | Total area (sqm) | Source | Canonical? | Gross/plinth |
|------|-----------------:|--------|------------|--------------|
| 1 Bedroom | **54** | Brochure + info-pack | Yes | **unknown** — labeled “Total area” only |
| 2 Bedroom (Type 01 / 02) | **90** | Brochure + info-pack | Yes | unknown |
| 3 Bedroom | **145** | Brochure + info-pack | Yes | unknown |

### Payment plan — must-have recount

| Element | Agreeing sources | Count / type | Threshold (≥4 agents **or any developer**)? | Status |
|---------|------------------|--------------|-----------------------------------------------|--------|
| Payment plans exist (instalments / cash) | Launch news; property pack; info-pack; Block; Vorsa; Craiova | Developer + agents | **Met via developer** | Must-have **field** yes |
| **24-month / 2-year** tenor | Launch news; info-pack; Block; Vorsa; Craiova | Official + agents | Official claim retained | **Not sole canonical** — conflicts with pack |
| **Up to 3 years** tenor | Property pack (Rendeavour/Tatu CDN) | 1 official pack | Official claim retained | **Not sole canonical** — conflicts with 24-mo |
| Cash incentives / discounts | Launch news; FAQ search-index (up to 10.7% — **404**) | Developer + weak FAQ | Soft claim | % **`needs_verification`** |
| Sharia-compliant options | Launch news; Block | Developer | Availability claim | Terms unknown |
| Reservation USD 1,550 + **10% deposit** | FAQ search-index only (404) | 0 live pages | Not met for deposit % | **`needs_verification`** |
| ~**20% deposit** | Block estimate only | 1 agent | Not met | Non-canonical |

**Payment summary (post-lock):** Developer materials confirm flexible payment / instalment options → must-have **satisfied**. Among **official** tenor figures (**24-month / 2-year** vs **up to 3 years**) → **`needs_developer_input`**; **no assumed canonical tenor**. Deposit % unknown on live pages.

---

## 2. Developer (primary)

| Field | Value |
|-------|-------|
| `id` | `dev-rendeavour` |
| `legal_name` | Rendeavour *(full registered entity string not confirmed this pass)* |
| `trading_names` | Rendeavour |
| `website` | https://www.rendeavour.com/ (corporate); project https://porinipoint.com/ |
| `group_company_id` | **null** — no parent invented |
| `evidence` | Brochure: “Porini Point is being developed by Rendeavour, the owner and master developer of Tatu City”; launch news; info-pack |
| `prior_projects_mentioned` | Jabali Towers (press/FAQ framing); other Rendeavour cities on brochure map (Jigna, Alaro, Appolonia, Kiswishi, Roma Park, King City) — **delivery unverified this pass** |
| `sales_office` | Tatu Experience Centre |

**Primary developer = Rendeavour (confidence 5).**

### Co-developer (also RelatedParty)

| Field | Value |
|-------|-------|
| `id` | `dev-tatu-city-limited` |
| `legal_name` | Tatu City Limited |
| `role_on_property` | **`co_developer`** (Cycle 2 lock — co-named “Developers” on property pack) |
| `also_modeled_as` | RelatedParty §4 (same entity, dual modeling) |
| `evidence` | Property pack disclaimer: “Rendeavour and Tatu City Limited (herein after referred to as the Developers)” |
| `confidence` | 4 |

---

## 3. GroupCompany

**None invented.** Do not create a GroupCompany from “Tatu City” branding. Tatu City Limited is co_developer + RelatedParty, not a parent above Rendeavour.

---

## 4. RelatedParty

| Field | Value |
|-------|-------|
| `id` | `rp-tatu-city-limited` |
| `name` | Tatu City Limited |
| `relationship_type` | **`co_developer` + RelatedParty** (Cycle 2 lock: model as **both**; revise later if patterns simplify). **Not** GroupCompany; **not** `marketing_partner` (pack explicitly names both as Developers). |
| `same_as_developer_id` | `dev-tatu-city-limited` |
| `website` | https://www.tatucity.com/ |
| `linked_to` | Property Porini Point; Developer Rendeavour |
| `evidence` | (1) Property pack disclaimer (tatucity.com CDN); (2) PoriniSales@tatucity.com / Tatu Experience Centre on project brochure; (3) Launch press on tatucity.com naming Tatu City executives |
| `confidence` | 4 |
| `not` | Not sole developer; not invented parent of Rendeavour |

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate | agency / portal | CSV sales_contact; detailed price/payment article | https://block.ke/investment-intelligence/porini-point-wake-up-to-giraffes-nairobis-only-apartments-overlooking-a-wildlife-sanctuary/30487/ |
| VorsaGroup Real Estate | agency | Listing + price table (low outlier) | https://vorsagroup.co.ke/property/porini-point-apartments-1-2-3-bedroom-in-tatu-city/ |
| Craiova Realtors | agency | Listing; cash/plan prices; Dec 2026 phase claim | https://craiovarealtors.com/property/1-2-3-bedroom-apartments-at-tatu-city/ |
| Ladva Realtors | agency | Article + from-prices | https://ladvarealtors.com/why-porini-point-tatu-city-apartments-are-becoming-a-smart-choice-for-modern-homebuyers-and-property-investors/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 709 441 144 | Property / Tatu sales (Porini) |
| email | PoriniSales@tatucity.com | Property / Tatu sales |
| url | https://porinipoint.com/ | Property |
| url | https://porinipoint.com/wp-content/uploads/2026/03/Porini-Point-1.pdf | Property (brochure) |
| office | Tatu Experience Centre | Property sales |
| phone | +254 725 937 686 | Agent: Block / Loyd Mokaya (CSV + Block article) |
| email | loyd@block.ke / info@block.ke | Agent: Block |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: VorsaGroup |
| email | info@vorsagroup.co.ke | Agent: VorsaGroup |
| phone / WhatsApp | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |
| phone | +254 725 474 747 / +254 739 474 747 | Agent: Ladva |
| email | info@ladvarealtors.com | Agent: Ladva |

CSV `sales_contact` = Block agent ≠ official Porini/Tatu sales office.

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| Makrem Ben Khemis | architect (Group Architect, Rendeavour) | Named on Tatu City launch press photo caption | 5 named / role as project designer **not** separately proven |
| Preston Mendenhall | other (Group COO / Country Head Kenya, Rendeavour) | Launch press quote | 5 (executive, not construction stakeholder) |
| Erskine Kiliru | other (Sales Director, Tatu City) | Launch press caption | 5 |
| Linda Nyaseda | other (Head of City Management and DCC, Tatu City) | Launch press caption | 5 |
| Unnamed | financing / contractor / land vendor | Not found | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under Cycle 2 lock |
|--:|-------|--------|-------------------------------|
| 1 | **price_from / price tables** | Live site from KES **7,610,000**; launch news from **7.5M**; info-pack cash 7.18/11.07/17.6M + 2-yr 8.7/13.2/21.0M; property pack from **5.9M** (USD 46k); Block cash/24-mo tables; Vorsa 5.99/10.07/16.2M; Craiova cash/plan; Ladva 6.71/10.4/16.7M; CSV 7,610,000 | **Official vs official** → **`needs_developer_input`**. **No assumed canonical** among disagreeing official figures. **Keep all** `price_claims[]`. Agents secondary / **`needs_verification`** for “current from”. |
| 2 | **Payment tenor** | Launch news + info-pack + agents: **24 months / 2 years**. Property pack: **up to 3 years** | **Official vs official** → **`needs_developer_input`**. Must-have field met; **no assumed canonical tenor**. |
| 3 | **Deposit %** | FAQ search-index **10%** (+ USD 1,550 reservation) vs Block **~20%** estimate. Live FAQ **404** | No live developer deposit schedule → **no canonical deposit %**. Both **`needs_verification`**. |
| 4 | **Completion** | Launch news Q1 2027 / Sep 2029. Craiova Phase 1 Dec 2026. CSV final phase Q3 2029 | **Canonical = launch news** (no conflicting *official* date). Agents/CSV secondary. |
| 5 | **Sold-out / phase inventory** | Launch news: first phase sold out on launch night. Live site still markets available homes. Agents still selling | Show developer sold-out **launch claim**; current inventory **`needs_verification`**. |
| 6 | **Floors G+4** | Block + FAQ search-index; absent from brochure extract / launch HTML | **`needs_verification`** |
| 7 | **Construction start Jan 2026** | FAQ search-index only (404) | **`needs_verification`** |
| 8 | **Amenity inflation** | Vorsa heated pool / lifts / library / retail / restaurant | Reject from core; developer list only |
| 9 | **Tatu City Limited vs Rendeavour** | Both “Developers” on pack; brochures emphasize Rendeavour | **Primary** = Rendeavour; Tatu City Limited = **`co_developer` + RelatedParty** (locked dual model) |
| 10 | Brochure / pack disclaimers | Plans subject to change | Always flag |

### Price claim snapshot — **all options retained** (for DB)

| Source type | 1BR from (KES) | 2BR | 3BR | Flag |
|-------------|----------------:|----:|----:|------|
| porinipoint.com hero | 7,610,000 | — | — | Official — **`needs_developer_input`** (vs other official) |
| Launch news | 7,500,000 | — | — | Official — **`needs_developer_input`** |
| Info-pack cash | 7,180,000 | 11,070,000 | 17,600,000 | Official-attributed — **`needs_developer_input`** |
| Info-pack 2-yr | 8,700,000 | 13,200,000 | 21,000,000 | Official-attributed — **`needs_developer_input`** |
| Property pack | 5,900,000 | — | — | Official — **`needs_developer_input`** |
| Block cash / 24-mo | 7,460,000 / 8,720,000 | 11,290,000 / 13,210,000 | 17,950,000 / 21,000,000 | Agent (cites pack) |
| Vorsa | 5,990,000 | 10,070,000 | 16,200,000 | Agent — **`needs_verification`** |
| Craiova cash / plan | 6,400,000 / 7,400,000 | 10,500,000 / 12,500,000 | 16,700,000 / 16,700,000 | Agent — **`needs_verification`** |
| Ladva | 6,710,000 | 10,400,000 | 16,700,000 | Agent — **`needs_verification`** |
| CSV seed | 7,610,000 | — | — | Unverified lead only |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~13** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~13 candidates (project site, two brochure PDFs, launch news, property pack, info-pack, Block, Vorsa, Craiova, Ladva, FAQ URL, LinkedIn post, Rendeavour Tatu page, CSV lead). **Always kept** developer/official project site + official PDFs/news. Retained 10 densest field-bearing sources (≥5 rule).

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://porinipoint.com/ | Porini Point | project_site | 2026-10-15 | Microsite — from KES 7,610,000 (one official price claim) |
| 2 | https://porinipoint.com/wp-content/uploads/2026/03/Porini-Point-1.pdf | Porini Point / Rendeavour | developer | 2026-10-15 | Brochure: sizes, amenities, Rendeavour, contacts |
| 3 | https://www.tatucity.com/wp-content/uploads/2025/08/2025.08.07-Porini-Point-Brochure.pdf | Tatu City / Rendeavour | developer | 2026-10-15 | Official brochure mirror on tatucity CDN |
| 4 | https://www.tatucity.com/news/porini-point-apartments-launch-at-tatu-city-with-sanctuary-views/ | Tatu City | developer | 2026-10-15 | Launch 19 Nov 2025; 570/24/58k sqm; Q1 2027–Sep 2029; 7.5M; 24-mo; sold-out claim; architect named |
| 5 | https://www.tatucity.com/wp-content/uploads/2025/08/2025.08.01-Tatu-City-Rendeavour-Property-Pack.pdf | Rendeavour / Tatu City Limited | developer | 2026-10-15 | From 5.9M; up to 3-yr plan; dual-Developer disclaimer |
| 6 | https://streamlinefeed.tech/storage/v1/object/public/media/c54a66eb-818a-481f-9aff-d789a9d141a1/0e305e06-9618-42ce-ae37-d051ca6371b1.pdf | Porini-branded pack (third-party host) | developer_attributed | 2026-10-15 | Cash vs 2-yr tables; leasehold 99y; contacts match official — host not on porinipoint/tatu domain |
| 7 | https://block.ke/investment-intelligence/porini-point-wake-up-to-giraffes-nairobis-only-apartments-overlooking-a-wildlife-sanctuary/30487/ | Block | portal | 2026-10-15 | Full price table; 24-mo; ~20% deposit estimate; G+4 |
| 8 | https://vorsagroup.co.ke/property/porini-point-apartments-1-2-3-bedroom-in-tatu-city/ | VorsaGroup | agent | 2026-10-15 | Low price outlier; 24-mo; amenity inflation |
| 9 | https://craiovarealtors.com/property/1-2-3-bedroom-apartments-at-tatu-city/ | Craiova | agent | 2026-10-15 | Cash/plan prices; Dec 2026 phase conflict |
| 10 | https://ladvarealtors.com/why-porini-point-tatu-city-apartments-are-becoming-a-smart-choice-for-modern-homebuyers-and-property-investors/ | Ladva | agent | 2026-10-15 | From 6.71M band; amenities echo |

### Evaluated but not retained (thin / failed / duplicate social)

| url | Why skipped |
|-----|-------------|
| https://www.tatucity.com/porini-faqs/ | **HTTP 404** on 2026-10-15 — search-index snippets only as **`needs_verification`** leads; not a live retained source |
| https://www.linkedin.com/posts/tatu-city-limited_porini-point-places-you-at-the-edge-of-a-activity-7408811144087224320-7KUj | Thin social; from KES 6.4M covered by richer price conflicts |
| https://www.rendeavour.com/projects/tatu/ | Fetch returned essentially empty content this pass |
| https://www.tatucity.com/test-2/ | Official but labeled “Test”; amenities duplicate brochure — skipped |
| CSV NBO-004 seed row | Lead only — not a publishable research URL |

---

## 9. Field harvest → must-have extension proposals

| Proposed field | Porini evidence | Consensus note |
|----------------|-----------------|----------------|
| `unit_count` + `block_count` | 570 / 24 on developer launch | Propose must-have when developer states scale |
| `built_up_area_sqm` | 58,000 on launch news | Optional until broader coverage |
| `price_claims[]` with **cash vs instalment columns** | Info-pack + Block dual tables | Strengthen; **never collapse** when official figures disagree → **`needs_developer_input`** |
| `payment_plan.tenor` claim set | 24-mo vs up-to-3-yr official | Must-have field yes; canonical tenor only when official sources **agree** |
| `reservation_fee` + `deposit_pct` | FAQ-only this pass | Nice-to-have until live FAQ/LOO |
| `master_planned_community` | Tatu City framing | Geography extension |
| Named group architect on press | Makrem Ben Khemis | Stakeholder when named on developer press |
| `foreign_ownership` / leasehold 99y | Brochure + info-pack | Legal claim set when marketed |

---

## 10. Retrofit summary (Cycle 2 locks 2026-10-16)

- **Tatu City Limited** = **`co_developer` and RelatedParty** (dual model); primary remains Rendeavour; GroupCompany still null.  
- **Official price conflicts** → **`needs_developer_input`**; **all** `price_claims[]` kept; **no** assumed canonical `price_from`.  
- **Official tenor conflicts** (24-mo / 2-yr vs up to 3 years) → **`needs_developer_input`**; payment must-have still met as a field; **no** assumed canonical tenor.  
- Completion Q1 2027 / Sep 2029 remains canonical (single agreeing official line).  
- Open questions 2–4 from prior draft **resolved by locks**; remaining: FAQ re-fetch; sold-out vs available inventory display.

### Remaining questions

1. Re-fetch **https://www.tatucity.com/porini-faqs/** when live — deposit / reservation / Jan 2026 start still **`needs_verification`**.  
2. Treat launch-night **phase sold-out** as historical claim only, or show as current inventory + **`needs_verification`**?
