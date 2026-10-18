---
slug: gemini-residency-phase-2
external_id: NBO-009
cycle: half-batch
pilot: false
wave: B
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Gemini Residency Phase 2 (NBO-009) — half-batch

CSV seed (unverified leads): location Matundu Lane, Brookside, Westlands, Nairobi; stage `under_construction`; completion Q1 2029; `price_from_kes` 9,500,000; sales_contact NRE Real Estate; developer Staroot Real Estate.

Live research: Staroot project pages + contact FAQ + Business Daily sponsored coverage + portals/agents accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume a winner** → flag **`needs_developer_input`**; no canonical until a later verification pass.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- `construction_progress`: retain as **claim set** when developer publishes; not a portal must-have yet.
- Payment must-have if any developer source **or** ≥4 agent sources. Agent-only / uncorroborated → **`needs_verification`**. CSV = unverified leads only.
- Unproven brand/sales partnership → **`marketing_partner`**, not GroupCompany.
- Phase 1 vs Phase 2 scope: isolate Phase 2 claims; keep Phase 1 figures as **context / secondary** with clear labels.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed value when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Gemini Residency Phase 2 | 5 | staroot.co.ke/gemini2; BD Phase 2; agents |
| `aliases` | secondary | Gemini Phase 2; Gemini II; Gemini 2; Gemini Residences (phase context); Gemini Square (amenity label on Staroot) | 4 | Hauzisha; Space.ke; Staroot amenity copy |
| `status` | claim set | CSV/`under_construction`; Staroot LinkedIn (Aug 2026): Phase 2 **97% excavation**; agents “off-plan” / under construction | 4 | CSV; LinkedIn Staroot; NRE; Space.ke |
| `geography.city` | **CANONICAL** | Nairobi | 5 | staroot.co.ke; all |
| `geography.neighbourhood` | **CANONICAL** | Brookside, Westlands | 5 | staroot.co.ke/gemini · gemini2 |
| `geography.street` | claim set — **needs_verification** on exact street label | **Matundu Lane / Matundu Road / Matundu Close** (CSV, Hauzisha, Malluug, CPK, L2B snippet) **vs Brookside Grove** (NRE) **vs Brookside Drive** (KeDwell/CPK body) — same Brookside pocket; plot pin unconfirmed | 3 | multi-agent + CSV; developer pages say “Brookside” without street |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.259416, 36.793132** (`geo_method=geocode`) | 2 | Nominatim Matundu Lane Brookside 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `geography.lat_lng` | secondary — **needs_verification** | L2B snippet ≈ **−1.26619, 36.80911** (1°15'58.3"S 36°48'32.8"E) | 1 | L2B search snippet only; street label conflict |
| `primary_developer_id` | **CANONICAL** | → `dev-staroot-real-estate` | 5 | staroot.co.ke; BD; Hauzisha; Space.ke |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom | 5 | staroot.co.ke/gemini · gemini2; BD Phase 2 |
| `size_by_type` | secondary (agent/portal tables; not on Staroot size schedule this pass) | Common Phase 2 bands: 1BR **58 / 67 sqm**; 2BR **90 / 110 / 122 sqm**. Malluug also lists Phase 2 1BR **56 sqm**. Hauzisha band **58–122 sqm** | 3 | CPK; KeDwell; Hauzisha; Malluug; realtors |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched | 0 | — |
| `total_units` (Phase 2) | secondary — **needs_verification** | Malluug: Phase 2 **260** units; combined **628**. realtors: Phase 1 **368** / total **628**. Developer site **does not publish** Phase 2 unit count this pass. Phase 1 **368** is BD/Space-backed (Phase 1 context) | 2 | Malluug; realtors; BD Phase 1 (368 Phase 1 only) |
| `building_specs.storeys` | claim set — **needs_verification** / Phase mix | Staroot amenity copy: **“30th-floor”** rooftop padel. realtors floor-plan copy: Phase 2 residential **2nd–27th**, rooftop amenities **28th**, padel **29th**; “25 floors high” header conflict. KeDwell: **29** floors. Phase 1 context: **27 floors / 368 units** (BD Phase 1; Space.ke) | 2 | Staroot; realtors; KeDwell; BD Phase 1 |
| `building_specs.form` | secondary | L-shaped; Phase 2 connected to Phase 1 G–3; commercial hub in Phase 2 | 3 | BD Phase 2; CPK; KeDwell; Malluug |
| `plot_coverage` | secondary (Phase 2 BD) | Towers cover **37%** of the land (BD Phase 2 / Staroot CEO quote) | 3 | BD Phase 2 |
| `price_claims[]` | claim set — **keep all options**; developer “from” vs agent tables conflict | See §1a — no portal scalar | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | all commercial sources |
| `payment_plan.deposit` | **CANONICAL** (developer FAQ) | **Minimum 20%** to reserve; **select cases 10%** also offered (Staroot contact FAQ). LinkedIn Staroot: lock-in with **20%–30%** deposit — consistent with min 20% | 5 | staroot.co.ke/contact; LinkedIn Staroot |
| `payment_plan.deposit` | secondary — Phase 1 context / agent variants | Phase 1 BD: **30% / 50% / 20%** schedule. Agents ≥4 claim **20%** for Phase 2. NRE same page also publishes **30/50/20** and a **20%** calculator — **needs_verification** | ≤3 | BD Phase 1; CPK; KeDwell; NRE; Malluug |
| `payment_plan.tenor` | secondary (developer soft) | BD Phase 2 sponsored: flexible plans **up to 36 months**. Staroot project pages: “flexible payment plans” (no tenor on gemini pages) | 3 | BD Phase 2; staroot.co.ke |
| `completion_estimate` (Phase 2) | claim set — **`needs_developer_input`** | Staroot gemini/gemini2 FAQ **agree: Phase 2 March 2029**. Developments card: completion **2029**. LinkedIn company About lists **Gemini Phase II (2026–2028)**. Agents: **Q4 / Dec 2028**. CSV: **Q1 2029**. **Do not assume winner** between official March 2029 vs LinkedIn 2026–2028 framing | 2 | staroot.co.ke vs LinkedIn About vs agents |
| `completion_estimate` (Phase 1 context) | secondary | Phase 1: **December 2027** (Staroot FAQ agrees across gemini pages) | 5 | staroot.co.ke — Phase 1 only |
| `amenities` (core) | **CANONICAL** (developer amenity set) | Gemini Square / retail convenience; **Serenity Spa** (partnership); reception; courtyard pool; courtyard garden; cinema; gym; yoga; separate male/female saunas; co-working; kids play; heated rooftop infinity pool; fire pit; BBQ; sky lounge; sky-high padel court. BD Phase 2 commercial hub: convenience store, pharmacy, restaurants, cafés, serviced co-working, Serenity Spa | 5 | staroot.co.ke/gemini · gemini2; BD Phase 2 |
| `amenities` | secondary / agent adds — **needs_verification** | Artcaffe Market/Restaurant; **1,000 sqm** co-working; **400 sqm** gym; CityBlue short-stay management; Kone lifts; 5 parking floors (3 podium + 2 basement); dry cleaning / guest room — dense on CPK/KeDwell/Malluug/realtors, not itemised identically on Staroot pages | 2 | CPK; KeDwell; Malluug; realtors |
| `construction_progress` | claim set (developer social) | Staroot LinkedIn (as of **31 Aug 2026**): Phase 2 **97% excavation**. Phase 1 progress also posted (elevations 100%; plastering/gypsum/masonry floors) — Phase 1 context only | 4 | LinkedIn Staroot post |
| `availability_claim` | secondary — **needs_verification** | Hauzisha: **2 units** available. realtors: several types marked **SOLD OUT** (mixed phase page). Do not treat as canonical inventory | 1 | Hauzisha; realtors |
| `legal_title` | soft developer FAQ | Contact FAQ: sectional title via **ardisasa** platform at completion — general Staroot process, not Phase-2-specific LOO | 2 | staroot.co.ke/contact |
| `investment_return_claims` | marketing only — **not product facts** | BD/Staroot marketing: up to **35%** appreciation / **9.5–18%** annual returns — **do not store as verified yields** | 0 | BD Phase 2; staroot copy |

### 1a. Price claims — keep **all** options (no canonical scalar)

Developer “Starting From **Kshs. 10,000,000**” (gemini + gemini2 agree) **vs** multi-agent tables from **~8.7M**. Keep every option; portal must not collapse to one `price_from`.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Staroot project “Starting From” / 1BR from | **KES 10,000,000** | staroot.co.ke/gemini · gemini2 | Official — conflicts with agent “from 8.7M” |
| B | CPK Phase 2 typed list | 1BR 58 sqm **8.7M**; 67 **9.2M**; 2BR 90 **13.5M**; 110 **15.5M**; 122 **17.1M** | commercialpropertykenya.com Phase 2 | Secondary |
| C | KeDwell Phase 2 table | Same bands as B (122 row size shows **110** — table typo) | kedwell.co.ke | Secondary / overlap B |
| D | Hauzisha Gemini 2 band | **KES 9.5M – 14.5M** | hauzisha.co.ke/developments/gemini-2/ | Secondary |
| E | NRE (mixed phase page) | 1BR 58: **8.7M** (100%) / **9.5M** (20%); 2BR 90: **13.5M** / **14.5M**; FAQ also cites other sizes | nairobirealestate.co.ke | Secondary — phase mix; page-internal conflict |
| F | CPK Phase 1-style deposit tiers (not Phase-2-only page) | 1BR 58: 20% **9.5M** / 50% **9.1M** / 100% **8.7M**; 2BR 90 similar | commercialpropertykenya.com gemini-westlands-apartment | Secondary — Phase 1 framing; **needs_verification** for Phase 2 |
| G | Malluug Phase 2 list | 1BR 56 **from 9M**; 67 **9.5M**; 2BR 90 **14M**; 110 **15.9M**; 122 **17.6M** | malluugrealtykenya.com | Secondary — **needs_verification** |
| H | realtors (mixed) | Listed from **~9.2M**; larger 2BR from **16.4M / 18M**; several types SOLD OUT | realtors.co.ke | Secondary — **needs_verification** |
| I | CSV seed | `price_from_kes` **9,500,000** | seed | Unverified lead |
| J | Phase 1 launch (context only) | 1BR **8.3M** / 2BR **13M** at Phase 1 unveil | BD Phase 1 | Historical Phase 1 — not Phase 2 current |

**Canonical price:** none. Always `price_claims[]`.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **Min 20% deposit** (select **10%**) | staroot.co.ke/contact FAQ; LinkedIn Staroot 20–30% | Developer **≥1** | **Met via developer** | **CANONICAL must-have** (min 20%; 10% as select-case claim) |
| **Up to 36 months** tenor | BD Phase 2 sponsored (Staroot) | Developer-adjacent **≥1** | Met as soft tenor claim | Secondary soft; exact instalment calendar unknown |
| **20% deposit** (agents) | CPK Phase 2; KeDwell; Malluug; NRE calculator | **≥4** | Met as agent consensus | Aligns with developer min 20% |
| Phase 1 **30/50/20** | BD Phase 1 | Phase 1 only | — | Do **not** auto-apply to Phase 2 |
| NRE **30/50/20** vs **20%** UI | Same NRE page | Internal conflict | — | **needs_verification** |
| Full LOO / PDF schedule | Not fetched this pass | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-staroot-real-estate` |
| `legal_name` | unknown (trading **Staroot Real Estate** / “Staroot Real Estate Company” on Hauzisha — legal suffix not evidenced this pass) |
| `trading_names` | Staroot Real Estate; Staroot |
| `website` | https://staroot.co.ke/ · project https://staroot.co.ke/gemini2 · https://staroot.co.ke/gemini |
| `evidence` | Official Gemini pages; BD sponsored Phase 2 launch naming Staroot; Hauzisha “by Staroot Real Estate Company”; Space.ke “by Staroot Real Estate” |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV “Staroot Real Estate” matches evidenced developer |
| `named_officers_in_press` | BD Phase 2 photo credits: CEO **Amir Ahmed**; Directors **Zhang Chi**, **Xie Xiaohan** (roles as captioned — not independently verified) |
| `office` | Principal Place, Westlands, Nairobi (Staroot contact) |
| `prior_projects_mentioned` | LinkedIn About / BD Phase 1 cite Kilimani deliveries (Bric, White Oak, Silver Oak, Staroot Residency, Platinum Oak, Neptune, Venus Oak, Capricorn, etc.) — **delivery claims unverified this pass** (`needs_verification`) |

**Primary developer = Staroot Real Estate (confidence 5).**

---

## 3. GroupCompany

**None.** No evidenced parent above Staroot. Chinese Developers Association chair appearing in launch photos ≠ corporate parent.

---

## 4. RelatedParty

| id | name | relationship_type | Evidence | Conf |
|----|------|-------------------|----------|-----:|
| `rp-proxima-real-estate` | Proxima Real Estate | **`marketing_partner`** | BD Phase 1: Staroot “in partnership with Proxima Real Estate” for unveil/sales. Proxima insight page. Phase 2 BD captions Amir Ahmed as **CEO at Staroot** (role shift vs Phase 1 “Proxima Director”) — do **not** upgrade Proxima to co-developer | 4 |

Serenity Spa = amenity/operating partner named on Staroot amenity copy (capture under Stakeholder / amenity partnership, not GroupCompany).

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| NRE Real Estate | agency | CSV sales_contact; mixed-phase listing + payment UI | https://nairobirealestate.co.ke/properties/gemini-residency |
| Hauzisha | portal | Gemini 2 card; Staroot attribution; price band; 2 units | https://hauzisha.co.ke/developments/gemini-2/ |
| CPK Real Estate (Kenneth Ikiara) | agency | Dense Phase 2 listing; typed prices; 20% | https://commercialpropertykenya.com/properties/gemini-residency-phase-2-in-westlands/ |
| KeDwell / Ace realtors Ltd | portal / agent | Phase 2 table; 29 floors; 20% — overlaps CPK copy | https://www.kedwell.co.ke/projects/gemini-residency-phase-2-brookside-westlands-16 |
| The Realtors Platform | agency | Floor-plan gallery; 368/628; sold-out flags | https://realtors.co.ke/property/gemini-residency-apartments-westlands/ |
| Malluug Realty Kenya | agency | Phase 2 **260** / total **628**; Matundu Lane; 20% | https://malluugrealtykenya.com/new-developments/gemini-residency/ |
| Proxima Real Estate | agency / marketing partner | Phase 1 launch narrative | https://proxima.co.ke/insights/gemini-where-stars-live |
| Space Kenya | editorial / portal | Construction footage hub; Phase 1 scale echo; Gemini II videos | https://space.ke/projects/gemini/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 710 999 111 | Developer: Staroot |
| email | hello@staroot.co.ke | Developer: Staroot |
| address | Principal Place, Westlands, Nairobi | Developer |
| url | https://staroot.co.ke/gemini2 | Property (Phase 2) |
| url | https://staroot.co.ke/gemini | Property (joint phases) |
| url | https://staroot.co.ke/contact/ | Developer |
| phone | +254 141 361 320 | Agent: NRE (CSV) |
| email | info@nairobirealestate.co.ke | Agent: NRE (CSV) |
| phone | +254 730 731 355 | Portal: Hauzisha |
| phone | +254 784 448 888 | Agent: CPK / Kenneth Ikiara |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 791 138 831 | Agent: Realtors Platform |
| email | sales@realtors.co.ke / info@realtors.co.ke | Agent: Realtors Platform |
| phone | +254 783 886 142 | Agent: Malluug Realty |
| email | info@malluugrealtykenya.com | Agent: Malluug Realty |
| phone | +254 752 444 999 / +254 788 444 999 | RelatedParty: Proxima |
| email | info@proxima.co.ke | RelatedParty: Proxima |

**CSV sales_contact = NRE ≠ Staroot developer phones** — split Contact.owner correctly.

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Serenity Spa** | other (amenity / wellness partner) | Staroot amenity copy “In partnership with Serenity Spa”; BD Phase 2 commercial hub | 4 |
| **Karim CG Visuals** (Amman Karim) | other (visuals) | Named in BD Phase 2 launch photo caption | 3 |
| **CityBlue** | other (optional short-stay management) | CPK / KeDwell marketing — **needs_verification** | 1 |
| **Artcaffe** | other (named commercial tenant claim) | CPK / Malluug — **needs_verification** | 1 |
| **Staroot Management** | other (property management claim) | Malluug — **needs_verification** | 1 |
| Architect “Vincent” | architect | Named only in BD Phase 1 launch photo caption — Phase 2 role unknown | 1 |

No financing partner / contractor legal entity named for Phase 2 this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Phase 2 completion** | Staroot gemini pages: **March 2029**. LinkedIn About: Phase II **(2026–2028)**. Agents: **Q4/Dec 2028**. CSV: **Q1 2029** | **Official vs official** (site vs LinkedIn About) → **`needs_developer_input`**. No assumed canonical. Agent/CSV secondary |
| 2 | **Prices** | Official from **10M** vs agent from **8.7M** / Hauzisha **9.5–14.5M** / Malluug & realtors higher bands | Keep **all** `price_claims[]`. No scalar. Agent “current from” **`needs_verification`** vs developer 10M |
| 3 | **Street label** | Matundu Lane/Road/Close vs Brookside Grove vs Brookside Drive | Same pocket likely; exact plot **needs_verification**. Canonical neighbourhood = Brookside, Westlands (developer) |
| 4 | **Unit count Phase 2** | Malluug **260** / total **628**; realtors 368+628 framing; developer silent | Show agent claims + **`needs_verification`**. No canonical Phase 2 count |
| 5 | **Storeys / padel floor** | Staroot “30th-floor” padel vs realtors 29th padel / 28th amenities / “25 floors” header vs KeDwell 29 vs Phase 1 BD 27 | Claim set; Phase mix risk; **needs_verification** |
| 6 | **Deposit schedule detail** | Developer FAQ min **20%** (select **10%**); LinkedIn **20–30%**; agents **20%**; Phase 1 BD **30/50/20**; NRE page conflicts 20% vs 30/50/20 | Canonical **min 20%** (developer FAQ). Keep other schedules secondary / Phase 1 context |
| 7 | **CSV sales_contact** | NRE ≠ Staroot | Split Contact.owner |
| 8 | **Sold-out / availability** | Hauzisha 2 units; realtors SOLD OUT flags | Show + **`needs_verification`** |
| 9 | **Wrong domain** | gemini-residency.com = travel/listing park, **not** this project | Discarded |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 candidates (Staroot gemini, gemini2, contact, developments; BD Phase 2; BD Phase 1; Hauzisha; NRE; CPK Phase 2; KeDwell; realtors; Malluug; Space.ke; Proxima insight; L2B; LinkedIn construction; wrong-domain gemini-residency.com; CSV). **Always kept** Staroot project + contact. Retained 10 densest field-bearing sources (≥5 rule).

**Thin / skipped (not in retained list):**
- https://www.kedwell.co.ke/projects/gemini-residency-phase-2-brookside-westlands-16 — near-duplicate of CPK Phase 2 copy (Ace realtors); evaluated for 29-floor + table corroboration only
- https://space.ke/projects/gemini/ — footage hub; Phase 1 368/27 echo; thin on Phase 2 commercial fields
- https://proxima.co.ke/insights/gemini-where-stars-live — Phase 1 narrative; denser evidence in BD Phase 1
- https://www.staroot.co.ke/developments — SPA thin on direct fetch; search snippets used for card “COMPLETION 2029” note only
- https://www.l2b.co.za/projects/gemini-residency-kenya-phase-2/37839 — paywalled/thin; GPS only in search snippet
- https://www.linkedin.com/posts/staroot-real-estate_gemini-thejourneycontinues-starootrealestate-activity-7502708522866860032-1oCQ — used for `construction_progress` claim; not counted in retained 10 (social post)
- https://gemini-residency.com/ — **wrong entity** (travel aggregator park)
- https://commercialpropertykenya.com/properties/gemini-westlands-apartment/ — Phase 1-leaning twin; price tiers kept as claim F only
- CSV NBO-009 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://staroot.co.ke/gemini2 | Staroot Real Estate | project_site | 2026-10-16 | Phase 2 URL; from 10M; Phase 2 Mar 2029; amenities — always keep |
| 2 | https://staroot.co.ke/gemini | Staroot Real Estate | project_site | 2026-10-16 | Joint phases FAQ; same completion + from 10M |
| 3 | https://staroot.co.ke/contact/ | Staroot Real Estate | developer | 2026-10-16 | Deposit FAQ min 20% / select 10%; Principal Place; contacts |
| 4 | https://www.businessdailyafrica.com/bd/sponsored/staroot-real-estate-launches-10th-project-in-westlands-nairobi-with-gemini-phase-2-setting-a-new-benchmark-for-modern-living--5432454 | Business Daily (sponsored) | news / developer-adjacent | 2026-10-16 | Phase 2 commercial hub; 37% coverage; 36-mo plans; Staroot officers |
| 5 | https://www.businessdailyafrica.com/bd/sponsored/gemini-investors-snap-up-westlands-luxury-project-4836428 | Business Daily (sponsored) | news / developer-adjacent | 2026-10-16 | Phase 1: 368 units / 27 floors; Proxima partnership; 30/50/20 |
| 6 | https://hauzisha.co.ke/developments/gemini-2/ | Hauzisha | portal | 2026-10-16 | Staroot; Matundu Road; 58–122 sqm; 9.5–14.5M; 2 units |
| 7 | https://nairobirealestate.co.ke/properties/gemini-residency | NRE | agent | 2026-10-16 | CSV contact; Brookside Grove; payment UI conflicts; mixed phase |
| 8 | https://commercialpropertykenya.com/properties/gemini-residency-phase-2-in-westlands/ | CPK Real Estate | agent | 2026-10-16 | Dense Phase 2 amenities + typed prices; 20%; Matundu Close |
| 9 | https://realtors.co.ke/property/gemini-residency-apartments-westlands/ | The Realtors Platform | agent | 2026-10-16 | Floor-plan copy Phase 1/2 floors; 368/628; sold-out flags |
| 10 | https://malluugrealtykenya.com/new-developments/gemini-residency/ | Malluug Realty Kenya | agent | 2026-10-16 | Phase 2 **260** / total **628**; Matundu Lane; Q1 2029 full project; 20% |

---

## 9. Field harvest

| Field | Gemini Phase 2 status | Notes / consensus bump |
|-------|----------------------|------------------------|
| canonical_name / aliases | OK | Phase 2 naming clear on Staroot + BD |
| status | OK as claim set | UC + excavation progress |
| geography neighbourhood | OK | Brookside, Westlands canonical |
| geography street / GPS | Weak | Street label conflict; GPS only L2B snippet |
| primary_developer | OK | Staroot Real Estate (5) |
| RelatedParty `marketing_partner` | OK | Proxima (Phase 1 partnership; not co-dev) |
| GroupCompany | none | Correctly empty |
| unit_types | OK | 1BR / 2BR developer agree |
| size_by_type + gross/plinth | Partial | Agent tables only; measure tag unknown |
| `total_units` / Phase 2 count | Agent-only **260** / **628** total | Reinforces proposed must-have **unit_count claim set**; developer silent → **needs_verification** |
| `storeys` claim set | Conflicting agent/official floor labels | Reinforces proposed `storeys` claim set |
| `price_claims[]` | All options A–J retained | Developer from 10M ≠ agent from 8.7M |
| cash vs instalment dual columns | Partial (NRE/CPK Phase 1 tiers) | Strengthen when Phase-2-specific LOO appears |
| `payment_plan` | **Min 20% canonical** (developer FAQ); 10% select; 36-mo soft | Must-have met via **developer source** |
| `completion_estimate` | Official ambiguity → **`needs_developer_input`** | Site Mar 2029 vs LinkedIn 2026–2028 |
| `construction_progress` | Developer LinkedIn excavation % | Reinforces proposed capture when developer publishes |
| amenities core | OK | Reject uncorroborated Artcaffe/CityBlue as canonical |
| Named commercial / spa partners | Serenity Spa captured | Stakeholder pattern |
| `legal` / sectional title process | Soft FAQ (ardisasa) | Nice-to-have until Phase-2 LOO |

### Proposed must-have extensions (this project)

| Proposed extension | Evidence here | Consensus note |
|--------------------|---------------|----------------|
| `unit_count` claim set (phase-aware) | Phase 2 260 / total 628 (agents); Phase 1 368 (BD) | Bump toward must-have; never invent Phase 2 count from subtraction alone without a source that states it |
| `storeys` / amenity-floor claim set | 30th padel vs 29/28/25/27 labels | Keep as claim set; Phase 1≠Phase 2 |
| `construction_progress` when developer posts | 97% excavation (LinkedIn) | Candidate must-have; coverage-gated |
| `payment_plan.deposit` with select-case band | FAQ min 20% / select 10% | Store range, not forced single % |
| Street-level geography + GPS | Matundu* vs Grove/Drive; L2B DMS | Promote GPS only when developer-sourced |

---

## Open questions (developer input)

1. Reconcile Phase 2 completion: website **March 2029** vs LinkedIn About **(2026–2028)** vs agent **Q4 2028**.
2. Publish Phase 2 **unit count** and **storey** schedule (confirm or correct 260 / 628 and padel floor number).
3. Binding **price list** vs marketing “from 10M” vs agent tables from 8.7M — which LOO is current?
4. Exact **plot address** (Matundu Lane vs Brookside Grove) + public GPS.
5. Is Proxima still a Phase 2 sales partner, or only historical Phase 1 `marketing_partner`?
6. Phase-2-specific payment calendar (beyond FAQ min 20% / select 10% / up to 36 months)?
