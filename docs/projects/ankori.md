---
slug: ankori
external_id: DISC-NBO-004
discovery: true
discovery_source: kenya-offplan-leads.md
cycle: discovery-batch
pilot: false
sources_evaluated: 12
sources_retained: 7
last_verified_at: 2026-10-16
not_galaxy_one: true
---

# Ankori (DISC-NBO-004) — Discovery batch (method-locked)

**Not in CSV seed NBO-001…017.** Discovery lead from [kenya-offplan-leads.md](../discovery/kenya-offplan-leads.md). Discovery ID `DISC-NBO-004` until NBO allocation policy set (same scheme as Nouveau DISC-NBO-005).

**≠ Galaxy One (NBO-013):** same **Rhapta Road / Westlands** corridor, different product. Galaxy One = Lionston, **147 Rhapta Road**, two wings, late-2027 target. Ankori = HassConsult-marketed **urban resort**, **~1.9 acres**, **Blocks A/B/C**, completion **Q4 2028**. Do not merge entities.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer/official sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official:** do not assume a winner → **`needs_developer_input`**.
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents. Below that → nice-to-have / **`needs_verification`**.
- Agent-only / uncorroborated → show + **`needs_verification`**.
- Unproven legal SPV → do **not** invent Limited name.
- Wrong-entity Rhapta EIAs / foreign “Ankori” brands → evaluate + skip.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = official Hass sources **agree**. Claim set / secondary = conflict detection. **`needs_developer_input`** = official pages disagree — no winner.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Ankori** | 5 | hassconsult.com/ankori; Hass blog; Investment Collection (“Westlands \| Art of Urban Resort Living”); LinkedIn/Space tours |
| `aliases` | secondary | Ankori Westlands; Ankori Urban Resort Residences; “The Art of Urban Resort Living” (tagline) | 4 | official pages; Space.ke video titles |
| `status` | claim set | Investment Collection: **Recently Launched** (not listed under “Under Construction”). Hass LinkedIn (Mar 2026) + Space tours market as **off-plan** investment. No live construction tracker found this pass | 4 | investment-collection; LinkedIn; Space |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all Hass pages |
| `geography.neighbourhood_street` | **CANONICAL** | Westlands — **Rhapta Road** (no street number published this pass) | 5 | ankori page; blog; TMK |
| `geography.plot_size` | **CANONICAL** | **~1.9 acres** | 5 | ankori page (“1.9 acres”); blog (“approximately 1.9 acres”) |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.264493, 36.789855** (`geo_method=geocode`) | 2 | Nominatim Rhapta Road Westlands 2026-10-16; no street number — **do not reuse** Galaxy JSON-LD — [geo-enrichment.md](../db/geo-enrichment.md) |
| `geography.landmarks_nearby` | secondary (marketing) | ABC Place; ArtCaffe Market; Playon Padel; Chandarana Foodplus; Carrefour; schools St. Mary’s, Loreto Convent Msongari, St. Austin’s; TMK: walk to “Raphta Mall” | 3 | ankori page; TMK |
| `primary_developer_id` | trading / conceptualizer — **legal SPV unknown** | → `dev-hassconsult-real-estate` (see §2) | 4 (trading face) / **0 (legal SPV)** | Hass “conceptualized by our development team”; Space.ke labels HassConsult as developer of Ankori tours |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom; 3 Bedroom | 5 | ankori; blog; Investment Collection |
| `unit_concept` | **CANONICAL** | Dual living: **City Side** (1–2 bed) and **Valley Side** (1–3 bed) | 5 | ankori; blog; LinkedIn |
| `building_specs.wings_blocks` | **CANONICAL** | **Three** residential blocks — **A, B, and C**; central landscaped courtyard | 5 | ankori; blog |
| `size_by_type` | unknown | Floorplans CTA on official page (**“View Floorplans”**) — sizes **not** published in static HTML this pass; PDF/modal not fetched | 0 | ankori |
| `size_measure_tag` | unknown | — | 0 | — |
| `total_units` | unknown | **Not published** on official pages this pass | 0 | — |
| `building_specs.storeys` | unknown | **Not published** on official pages this pass | 0 | — |
| `price_claims[]` | claim set — **keep all**; official “from” agrees across Hass surfaces | See §1a | ≤4 | |
| `currency` | **CANONICAL** (KES on Hass); agent also quotes EUR | **KES** primary | 5 | ankori; Investment Collection |
| `payment_plan.duration` | **CANONICAL** (developer surfaces agree) | Payment over **30 months** | 5 | ankori summary strip; Investment Collection framing |
| `payment_plan.deposit` | secondary — **`needs_verification`** | Agent **20%** deposit (TMK only this pass) — **not** on Hass HTML; **payment must-have for deposit % not met** (&lt;4 agents; no developer %) | 2 | TMK only |
| `payment_plan.balance` | secondary soft | TMK: balance monthly until Dec 2028 delivery | 2 | TMK |
| `completion_estimate` | **CANONICAL** (Hass pages agree) | **Q4 2028** | 5 | ankori; Investment Collection |
| `completion_estimate` | secondary | TMK: **December 2028** (aligns with Q4) | 3 | TMK |
| `amenities` (core) | **CANONICAL** (from Hass page + blog; show union of agreeing official copy) | Coffee bar / Provisions Store; Fitness / Gym & Wellness Studio; Rooftop Oasis; heated infinity pools (blog); Home Cinema; Gaming Lounge; Residents Lounge; Sky Terrace / Signature Terrace; 360° Panorama Sky Club (blog); Cascades / Peace Garden / Golden Lawn; indoor + outdoor kids play; Elevate resident-experience hub (fitness, wellness, dining, kids club, entertainment, workspaces); landscaped gardens / courtyard | 5 | ankori; blog |
| `amenities` | secondary | TMK echoes rooftop pool, gym, lounges, private cinema, gardens — aligns with core | 3 | TMK |
| `investment_claim` | secondary marketing — **`needs_verification`** | Blog: projected rental returns **~13%** for 1-bedroom units | 1 | Hass blog only |
| `construction_progress` | unknown | No % / floor tracker on official pages this pass; status = Recently Launched | 0 | — |
| `legal_title` | unknown | — | 0 | — |
| `parking` | unknown | Not quantified on Ankori pages this pass | 0 | — |

### 1a. Price claims — keep **all** options (no canonical scalar)

Official Hass “from **KSh 6.5M**” agrees across project page + Investment Collection. No typed 1/2/3BR KES table on static HTML. Floorplans CTA not opened.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Official “from” | **From KSh 6,500,000** (1/2/3 bed product) | hassconsult.com/ankori | Official — agreeing with B |
| B | Investment Collection | Westlands \| Art of Urban Resort Living — **from KShs 6,500,000** | hassconsult.com/investment-collection | Official — agrees with A |
| C | TMK typed EUR bands | 1BR from **€42,000**; 2BR from **€90,000**; 3BR from **€178,500** | tmk-invest.com/listings/ankori/ | Secondary agent — FX/date not stated; **`needs_verification`** vs KES 6.5M “from” |
| D | Hass pricing-sheets hub | Live fetch = **thin JS shell**; search snippets not treated as facts | hassconsult.com/pricing-sheets | Evaluated — **not retained** as price evidence |

**Canonical price:** none (no typed official unit table). Official **from 6.5M KES** is the densest agreeing “from” claim (A=B) but still stored as `price_claims[]`, not a forced portal scalar.

### Payment plan — threshold recount

| Element | Agreeing sources | Count | Threshold? | Status |
|---------|------------------|------:|------------|--------|
| **Payment over 30 months** | ankori page strip; Investment Collection card context | Developer **≥1** (agreeing Hass surfaces) | **Met via developer** | **CANONICAL** duration |
| **Deposit %** | TMK **20%** only | **1** agent | **Not met** (≥4 agents or developer %) | Secondary **`needs_verification`** |
| Full LOO / schedule PDF | Pricing-sheets / floorplans CTAs not usable this pass | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-hassconsult-real-estate` |
| `legal_name` | **Unknown** this pass (no Companies Registry / NEMA proponent naming Ankori) |
| `trading_names` | HassConsult Real Estate; HassConsult; Hass Consult |
| `website` | https://www.hassconsult.com/ · project https://www.hassconsult.com/ankori |
| `role_evidence` | Home: developments “**conceptualized by our development team**”; Ankori on Latest Launches; Space.ke: “HassConsult is the **developer** this tour features”; also long-tenured **brokerage** + Hass Property Index publisher |
| `group_company_id` | **null — none invented** |
| `spv_note` | **Legal project SPV not recovered.** Do not invent. Hass may be developer and/or marketing/sales steward — treat as **primary commercial face** (conf 4) until SPV/NEMA name match |
| `address` | ABC Place, Waiyaki Way, P.O. Box 14090-00800 Nairobi |
| `phone` | +254 709 479 000 |
| `email` | HELLO@HASSCONSULT.COM |

**Primary commercial developer face = HassConsult Real Estate (confidence 4 trading / 0 legal SPV).**

---

## 3. GroupCompany

**None evidenced** above HassConsult for Ankori. Do not invent.

---

## 4. RelatedParty

None required this pass (no separate marketing_partner brand analogous to Proxima/Staroot). If a land SPV or co-developer surfaces later → RelatedParty / dual co_developer per Cycle 2 lock.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| HassConsult Real Estate | developer / sales | Official project + Investment Collection + contacts | https://www.hassconsult.com/ankori |
| TMK-Invest | overseas / agency listing | EUR price bands; 20% deposit; Dec 2028 | https://tmk-invest.com/listings/ankori/ |
| Space Kenya | verified video portal | HassConsult-attributed Ankori tours | https://space.ke/videos/bi7D6ykq7-w/ · https://space.ke/developers/hassconsult/ |

African Vibes reprint evaluated (copies Hass blurb) — **not retained** (wrong geo pin “Mkoko Close / Muthangari”; thin).

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 709 479 000 | HassConsult |
| email | HELLO@HASSCONSULT.COM | HassConsult |
| address | ABC Place, Waiyaki Way, P.O. Box 14090-00800 Nairobi | HassConsult |
| url | https://www.hassconsult.com/ankori | Property |
| url | https://www.hassconsult.com/ | Developer / broker |
| email | projects@spacekenya.com | Space Kenya (portal) |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Elevate** (amenity / experience hub brand) | other / program | Ankori page: resident experience hub | 3 |
| Architect / contractor / financing | — | **Not named** this pass | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Entity vs Galaxy One** | Both on Rhapta Road / Westlands | **Different projects** — document ≠; never merge with NBO-013 |
| 2 | **Deposit %** | Hass: 30-month payment, **no %**. TMK: **20%** | Developer duration canonical; deposit **`needs_verification`** (threshold unmet) |
| 3 | **Price currency / bands** | Hass from **KES 6.5M** vs TMK **EUR** typed 1/2/3BR | Keep all `price_claims[]`; TMK **`needs_verification`** |
| 4 | **Legal developer / SPV** | Hass conceptualizer/sales face vs unknown land SPV | Trading face conf 4; legal **0** — chase NEMA/registry |
| 5 | **Status** | Recently Launched vs agent “nouveau projet” off-plan | Claim set; no UC % invented |
| 6 | **Wrong Rhapta EIA** | NEMA ENVIS-00497 / EIA-2453: **Procmura Properties Ltd**, Nairobi/Block **4/613**, **two** 18-storey blocks, **321** units | **Not Ankori** (Ankori = **three** blocks / 1.9 acres). Evaluated + **skipped** — do not attach |
| 7 | **Foreign Ankori** | ankori.gt (Guatemala Zona 10) | Wrong country — skipped |
| 8 | **Jumuika 6.5M Westlands** | Amenity list (mini-golf, basketball, 30%/32 mo) looks **CANTO/VAAL-like**, not Hass Ankori | Evaluated — **likely wrong entity**; not retained |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~12** |
| `sources_retained` | **7** |

**Selection note:** Scanned Hass project page, Hass blog, Investment Collection, Hass home, pricing-sheets shell, TMK-Invest, Space video + Hass developer hub, LinkedIn carousel, African Vibes reprint, NEMA Rhapta EIA (Procmura), ankori.gt, Jumuika Westlands card. **Always kept** official Hass Ankori surfaces. Retained **7** densest (≥5 rule).

**Thin / skipped (not retained):**
- https://www.hassconsult.com/pricing-sheets — JS shell; no usable Ankori table in fetch
- https://africanvibes.com/real-estate/one-two-three-bed-apartments-from-ksh-6-5m/ — Hass copy reprint + **wrong address** (Mkoko Close)
- https://nema.go.ke/wp-content/uploads/2026/03/ENVIS-00497-EIA-2453.pdf — **Procmura / 2×18 / 321** ≠ Ankori 3-block product
- https://ankori.gt/ — Guatemala project
- https://jumuika.co.ke/properties/1br-off-plan-with-heated-pool-cinema-westlands — amenity conflation risk
- BuyRentKenya Rhapta listings for Galaxy One / Santorini — other projects

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://www.hassconsult.com/ankori | HassConsult | project_site | 2026-10-16 | 1.9 acres; blocks A–C; City/Valley; from 6.5M; Q4 2028; 30 months; amenities — **always keep** |
| 2 | https://www.hassconsult.com/post/ankori-a-new-perspective-on-urban-living-in-westlands | HassConsult | developer_blog | 2026-10-16 | Concept; ~13% yield claim; heated infinity pools; Sky Club |
| 3 | https://www.hassconsult.com/investment-collection | HassConsult | developer | 2026-10-16 | Recently Launched; from 6.5M; Westlands urban resort card |
| 4 | https://www.hassconsult.com/ | HassConsult | developer | 2026-10-16 | Ankori on Latest Launches; “conceptualized by our development team” |
| 5 | https://tmk-invest.com/listings/ankori/ | TMK-Invest | agent | 2026-10-16 | EUR bands; 20% deposit; Dec 2028 |
| 6 | https://space.ke/videos/bi7D6ykq7-w/ | Space Kenya | portal_video | 2026-10-16 | HassConsult-attributed Ankori tour (Mar 2026) |
| 7 | https://space.ke/developers/hassconsult/ | Space Kenya | portal | 2026-10-16 | Hass = brokerage + development; ABC Place; Ankori in video list |

---

## 9. Field harvest

| Field | Ankori status | Notes |
|-------|---------------|-------|
| canonical_name / aliases | OK | Hass agree |
| status | Claim set | Recently Launched / off-plan |
| geography + plot 1.9 acres + 3 blocks | OK | Hass agree |
| lat_lng / street number | Missing | Chase GPS / plot |
| primary_developer trading face | OK (conf 4) | Legal SPV **0** |
| unit_types + City/Valley concept | OK | |
| sizes / storeys / unit count | Missing | Floorplans CTA unfetched |
| `price_claims[]` | Official from 6.5M + TMK EUR | No typed KES table |
| payment duration 30 mo | **Canonical** (developer) | |
| deposit % | Threshold **not** met | TMK 20% only |
| amenities core | OK | Elevate hub named |
| ≠ Galaxy One | Documented | Critical corridor disambiguation |
| NEMA | No Ankori-named filing found | Procmura EIA explicitly **not** linked |

---

## Open questions (developer / verification)

1. **Legal SPV** / land title / NEMA proponent name for Ankori (not Procmura Block 4/613).
2. Typed **unit sizes**, **storeys**, **total units**, parking bays (open floorplans / pricing sheet).
3. Binding **deposit %** and LOO schedule vs agent 20%.
4. Exact **Rhapta Road** street number / GPS for geo enrichment.
5. Confirm construction start / progress snapshot (Recently Launched vs active UC).
6. Is HassConsult sole developer or marketing steward for a separate landowner SPV?
