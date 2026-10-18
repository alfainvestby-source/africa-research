---
slug: nouveau
external_id: DISC-NBO-005
wave: discovery
pilot: false
sources_evaluated: 13
sources_retained: 9
last_verified_at: 2026-10-16
---

# Nouveau (DISC-NBO-005) — discovery research

**Not in seed CSV.** Discovery lead from [kenya-offplan-leads.md](../discovery/kenya-offplan-leads.md) (priority batch #5): Lenana Road (Hurlingham), HassConsult, explicit off-plan, UC, Q4 2028.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer/official sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (HassConsult pages / channels disagree): **do not assume** → **`needs_developer_input`**.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- Payment must-have if any developer source **or** ≥4 independent agent sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**.
- Unproven brand/parent (e.g. HassConcept hashtag) → not GroupCompany; capture as alias / related brand only when evidenced.
- No invented legal SPV / NEMA filing — none matched this pass.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer/official-backed when sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official channels disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Nouveau | 5 | hassconsult.com/nouveau; Investment Collection; posts |
| `aliases` | secondary | Nouveau \| Lenana Road \| Future of City Living; “nü-vō” pronunciation on project page; HassConcept (LinkedIn hashtag only) | 3 | project page; LinkedIn |
| `status` | claim set | Official: **off plan** + “construction currently ongoing”; Investment Collection **Under Construction**; Space.ke HassConsult tours Nov 2024–Jul 2025 | 5 | nouveau; investment-collection; Space videos |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all HassConsult |
| `geography.neighbourhood` | claim set — **needs_verification** on label | **Hurlingham** (HassConsult project + blog) **vs Kilimani** (Altra listing title) — Lenana Road corridor | 4 / 2 | Hass vs Altra |
| `geography.street` | **CANONICAL** | **Lenana Road** | 5 | nouveau; Investment Collection “LENANA ROAD”; blogs |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.289054, 36.783741** (`geo_method=geocode`) | 2 | Nominatim Lenana Road Hurlingham 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** (marketing/developer-of-record) | → `dev-hass-consult-limited` | 4 | See §2 — legal SPV / EIA not found |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom | 5 | nouveau; Investment Collection |
| `unit_types` | secondary — **needs_verification** | Blog rent table mentions **“mini one-bedroom”** separately from one-bedroom — not listed as a sales typology on project page | 2 | nouveau investment blog |
| `size_by_type` | secondary — **needs_verification** | Altra: example **51 sqm** 1BR. No HassConsult size schedule fetched (floorplans CTA on Investment Collection; pricing-sheets page empty this pass) | 2 | Altra only |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** | 0 | — |
| `total_units` | unknown | Not published on HassConsult materials fetched | 0 | — |
| `building_specs.storeys` | secondary — **needs_verification** | Altra: **22 storey** mixed-use — **2 retail floors + 20 residential + rooftop amenities floor**; **4 basement parking** levels with separate retail/residential entrances. **Not on hassconsult.com/nouveau HTML this pass** | 2 | Altra only |
| `building_specs.use` | **CANONICAL** (presence) | Mixed-use: residential + curated retail (2 floors claimed on Hass blogs) + rooftop amenities | 5 | nouveau; mixed-use post; investment blog |
| `price_claims[]` | claim set — **keep all**; soft official “from” conflict | See §1a | ≤4 | |
| `currency` | **CANONICAL** | KES (KShs) | 5 | HassConsult |
| `payment_plan.deposit` | claim set — **`needs_developer_input`** vs tenor pages | LinkedIn HassConsult (Feb 2025): **10% down payment**. Live project page fetch did **not** restate deposit % in text extracted this pass | 3 | LinkedIn official post |
| `payment_plan.tenor` | claim set — **`needs_developer_input`** | Official channels disagree: project page extract **“PAYMENT OVER 28 MONTHS”**; investment blog **28-month** plan; LinkedIn **30-month** plan; search-indexed project page also showed **21 MONTHS** (SPA/index conflict) → **no assumed winner** | 2 | nouveau; blog; LinkedIn; search index |
| `completion_estimate` | **CANONICAL** (HassConsult project pages agree) | **Q4 2028** | 5 | nouveau; Investment Collection framing |
| `completion_estimate` | secondary — **needs_verification** | Altra: commencement **Q1 2025**, anticipated completion **Q1 2028** | 2 | Altra |
| `amenities` (core) | **CANONICAL** | Two floors of curated retail (restaurants, supermarket, boutiques, cafes, salons, pharmacy, etc.); rooftop **cold plunge**; relaxation deck; rooftop lounge / “skyline socials” | 5 | nouveau; mixed-use post; investment blog |
| `amenities` | secondary — **needs_verification** | Altra feature chips: CCTV, gym, lift, parking, swimming pool — **gym / full pool** not named on HassConsult Nouveau pages this pass (cold plunge ≠ lap pool) | 1 | Altra |
| `availability_claim` | secondary — **needs_verification** | HassConsult mixed-use post: **“85% of units already sold”** — uncorroborated inventory | 2 | mixed-use post only |
| `yield_claims` | secondary marketing — **needs_verification** (not product facts) | Blog: projected monthly rents ~70k / 90k / 140k (mini-1BR / 1BR / 2BR). Mixed-use post: estimated yields **10%** (1BR) / **9.5%** (2BR) unfurnished. LinkedIn: **35%** capital appreciation in 2 years; reshare cites up to **13.5%** yield | 1 | Hass blogs / LinkedIn — never invent; show as marketing claims only |
| `legal_title` / plot | unknown | No NEMA ESIA / plot LR matched to Nouveau this pass (wrong-entity 22-storey Two Rivers filing discarded) | 0 | — |
| `facilities_management` | secondary | Altra: developer-appointed management team **minimum 3 years** post-completion | 2 | Altra |

### 1a. Price claims — keep **all** options (no canonical scalar)

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Project page + Investment Collection “from” | **KES 6,500,000** / KSh 6.5M (1 & 2 bed from) | hassconsult.com/nouveau; investment-collection | Official “from” |
| B | LinkedIn HassConsult launch post | Starting at **Kshs. 6M** | LinkedIn activity 7295042730416611328 (Feb 2025) | Official channel — **conflicts with 6.5M** → keep both; soft **`needs_developer_input`** on current from-price |
| C | Altra example unit | €48,100 for 51 sqm 1BR (FX-dependent; not a KES list) | altrarenditaimmobiliare.it | Secondary / non-KES — **needs_verification** |

**Canonical price:** none as portal scalar. Prefer citing official A when quoting “from”; retain B–C.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| Payment plan **exists** (instalments over construction) | nouveau page; investment blog; LinkedIn | Developer **≥1** | **Met via developer** | Must-have **existence** |
| **10% deposit** | LinkedIn HassConsult post | Developer channel **1** | Met via developer for deposit **claim** | Claim retained; **not** restated on live nouveau page extract → confirm LOO |
| Tenor **28 months** | nouveau extract; investment blog | Official | — | Part of **`needs_developer_input`** set |
| Tenor **30 months** | LinkedIn HassConsult | Official | — | Part of **`needs_developer_input`** set |
| Tenor **21 months** | Search-indexed nouveau page (not confirmed in this pass’s static extract) | Indexed | — | **`needs_verification`** + include in NDI set if live hydration shows it |
| ≥4 independent **agents** on same plan | Not found (thin agent corpus) | 0 | — | N/A |

**Canonical deposit/tenor:** **no single canonical tenor** (official disagreement). Deposit **10%** is the only explicit % on an official HassConsult channel this pass — keep as developer claim; flag for LOO confirmation because project page extract omitted %.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-hass-consult-limited` |
| `legal_name` | **Hass Consult Limited** (trading **HassConsult Real Estate**) |
| `trading_names` | HassConsult; HassConsult Real Estate; Hass Consult |
| `website` | https://www.hassconsult.com/ · project https://www.hassconsult.com/nouveau |
| `evidence` | (1) Project page + Investment Collection list Nouveau under HassConsult UC portfolio. (2) Homepage: developments “conceptualized by our development team”. (3) Investment blog: “Conceptualized by HassConsult Real Estate”. (4) Space.ke verified tours label **HassConsult** as the developer featured. (5) Public directories / case style use **Hass Consult Limited** (ABC Place, Waiyaki Way). |
| `group_company_id` | **null — none invented** |
| `identity_gap` | No project-specific SPV / NEMA proponent / sale-agreement party name recovered for Nouveau this pass. HassConsult historically also acts as **sales agent** on third-party developments (e.g. court materials re Westpointe) — for Nouveau, official materials present HassConsult as conceptualizer/seller of record, but **advocate should confirm contracting entity** on LOO. Confidence **4**, not 5. |
| `hassconcept_note` | LinkedIn hashtags `#hassconcept` — **not** modeled as GroupCompany; unproven brand arm |

**Primary developer / developer-of-record for research = Hass Consult Limited / HassConsult Real Estate (confidence 4).**

---

## 3. GroupCompany

**None.** No evidenced parent above Hass Consult Limited.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Conf |
|------|-------------------|----------|-----:|
| HassConcept | related_brand (unproven) | LinkedIn hashtags on Nouveau posts only | 1 |

No `marketing_partner` required analogous to Laureland/SkyPeak — HassConsult is the selling/conceptualizing party on its own pages.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Party | Type | Role | Evidence URL |
|-------|------|------|--------------|
| HassConsult Real Estate | developer / sales office | Project microsite; Investment Collection; blogs; LinkedIn | https://www.hassconsult.com/nouveau |
| Space Kenya | portal (video) | Verified HassConsult tours; attributes HassConsult as developer | https://space.ke/videos/RLhV-2kolgA/ (+ other Nouveau tour URLs) |
| Altra Rendita Immobiliare | foreign agent / portal | Dense building-spec copy (22 storey / 4 basement); Q1 2028; 51 sqm example | https://altrarenditaimmobiliare.it/property/nouveau/ |

Independent Kenya agent portals (Block, NRE, Vorsa, Hauzisha project cards) **not found** this pass — commercial corroboration is HassConsult-heavy.

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| url | https://www.hassconsult.com/nouveau | Property |
| url | https://www.hassconsult.com/investment-collection | Developer portfolio |
| phone | +254 709 479 000 | HassConsult |
| email | hello@hassconsult.com | HassConsult |
| address | ABC Place, Waiyaki Way; P.O. Box 14090 – 00800 Nairobi | HassConsult |
| phone | +39 351 064 2728 | Agent: Altra |
| email | contact@altrarenditaimmobiliare.it | Agent: Altra |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| Unnamed “developer appointed” facilities management (min. 3 years) | other | Altra additional details | 1 |

No named contractor / architect / financing partner on materials fetched.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Payment tenor** | 28 months (project extract + blog) vs **30 months** (LinkedIn) vs indexed **21 months** | **Official vs official** → **`needs_developer_input`**. No canonical tenor. |
| 2 | **Deposit %** | LinkedIn **10%**; not restated on nouveau page extract | Developer claim retained; confirm against live LOO / pricing sheet |
| 3 | **Price from** | Official **6.5M** vs LinkedIn **6M** | Keep both in `price_claims[]`; soft official conflict — do not force scalar |
| 4 | **Completion** | HassConsult **Q4 2028** vs Altra **Q1 2028** | **Canonical = Q4 2028** (agreeing HassConsult project materials). Altra secondary + **needs_verification** |
| 5 | **Storeys / parking** | Altra 22-storey + 4 basements vs silent project HTML | Show Altra + **`needs_verification`** until HassConsult publishes specs |
| 6 | **Neighbourhood label** | Hurlingham vs Kilimani | Claim set; street Lenana Rd canonical |
| 7 | **Sold-out / 85%** | Single HassConsult blog | Show + **`needs_verification`** |
| 8 | **Yield / appreciation marketing** | 9.5–13.5% / 35% claims | Marketing only; **needs_verification**; never public as fact |
| 9 | **Contracting entity** | HassConsult conceptualizer vs possible unnamed SPV | Conf 4; advocate confirm on LOO |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~13** |
| `sources_retained` | **9** |

**Selection note:** Scanned HassConsult nouveau, Investment Collection, homepage, developments hub, pricing-sheets, two Hass blogs, LinkedIn payment post, Altra listing, Space.ke tours, company-directory/case hits for legal name, wrong NEMA 22-storey Two Rivers filing. **Always kept** hassconsult.com/nouveau. Retained 9 densest (≥5 rule).

**Thin / skipped (not in retained list):**
- https://www.hassconsult.com/pricing-sheets — empty shell this pass (no usable price table)
- https://www.hassconsult.com/developments — thin portfolio shell
- https://nema.go.ke/.../SR-00108-TRIFIC-TWIN-TOWER... — **wrong entity** (Two Rivers Vantage Point office)
- https://www.linkedin.com/posts/steve-gasigwa-... — reshare of HassConsult post (overlap)
- Directory stubs (Listingster / Ouzl / Bektu) — legal-name corroboration only; not project-dense
- Seed CSV — **N/A** (discovery lead)

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://www.hassconsult.com/nouveau | HassConsult | project_site | 2026-10-16 | Off-plan; from 6.5M; Q4 2028; payment over months; amenities — **always keep** |
| 2 | https://www.hassconsult.com/investment-collection | HassConsult | developer | 2026-10-16 | UC row Lenana Road from 6.5M; 1&2 bed |
| 3 | https://www.hassconsult.com/ | HassConsult | developer | 2026-10-16 | “Conceptualized by our development team”; Nouveau card |
| 4 | https://www.hassconsult.com/post/nouveau-where-smart-investors-meet-the-future-of-city-living | HassConsult | developer | 2026-10-16 | 28-mo plan; rents; conceptualized by HassConsult |
| 5 | https://www.hassconsult.com/post/the-rise-of-mixed-use-living | HassConsult | developer | 2026-10-16 | Retail floors; 85% sold; yield estimates |
| 6 | https://www.linkedin.com/posts/hass-consult_nouveau-payment-plan-details-activity-7295042730416611328-GhgY | HassConsult | developer_social | 2026-10-16 | **10%** + **30-month**; from 6M |
| 7 | https://altrarenditaimmobiliare.it/property/nouveau/ | Altra Rendita | agent | 2026-10-16 | 22-storey / 4 basement; Q1 2028; 51 sqm |
| 8 | https://space.ke/videos/RLhV-2kolgA/ | Space Kenya | portal | 2026-10-16 | Jul 2025 tour; labels HassConsult developer |
| 9 | https://space.ke/videos/SnbQDo3KTxk/ | Space Kenya | portal | 2026-10-16 | Nov 2024 tour (construction-era media) |

---

## 9. Field harvest

| Field | Nouveau status | Notes |
|-------|----------------|-------|
| canonical_name / aliases | OK | HassConcept hashtag only |
| status | OK as claim set | Off-plan + UC ongoing |
| geography street | OK | Lenana Rd; Hurlingham/Kilimani label soft |
| primary_developer | OK at conf **4** | Hass Consult Limited; SPV/EIA gap |
| GroupCompany | none | Correctly empty |
| unit_types | OK 1&2BR | Mini-1BR rent line NV |
| `storeys` / parking | Agent-only dense (Altra) | Propose capture when official publishes |
| `price_claims[]` | 6.5M vs 6M official channels | Multi-claim; no scalar |
| `payment_plan` | Existence met via developer; **tenor NDI** | 21/28/30; 10% LinkedIn |
| completion | **Q4 2028 canonical** (Hass agree) | Altra Q1 2028 secondary |
| amenities core | OK | Cold plunge + retail + rooftop lounge |
| availability 85% | NV | Single blog |
| Named contractor | none | — |

### Proposed schema / process notes
- Discovery IDs (`DISC-NBO-*`) for non-CSV Nairobi leads until NBO allocation policy set.
- HassConsult dual role (developer-of-record vs pure agent on other schemes) → entity-resolution watchlist.
- Official payment-tenor drift across SPA/social → same **`needs_developer_input`** pattern as Galaxy/Porini.

---

## Open questions (developer / advocate)

1. Contracting party on LOO — Hass Consult Limited vs project SPV?
2. Binding payment schedule: **10%** + which tenor (**21 / 28 / 30** months)?
3. Current list “from” — **6.0M or 6.5M**?
4. Publish storeys, unit count, size schedule, parking bays on hassconsult.com/nouveau?
5. NEMA / County approvals + plot LR for Lenana Rd site?
6. Is **85% sold** still accurate; remaining typology mix?
7. Gross vs plinth tags on floorplans (Investment Collection CTA)?
