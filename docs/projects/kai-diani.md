---
slug: kai-diani
external_id: KWA-001
geography_scope: coast / kwale / diani
cycle: discovery-research
pilot: false
wave: discovery
sources_evaluated: 12
sources_retained: 10
last_verified_at: 2026-10-16
---

# Kai (KWA-001) — Diani / Kwale — discovery research

**New geography:** **Diani**, **Kwale County** (Kenya coast) — second Diani dossier in the corpus (after **DIA-001** 108 Residences). Not in Nairobi seed CSV. ID **KWA-001** (Kwale) to distinguish from DIA-001.

Discovery lead: [`kenya-offplan-leads.md`](../discovery/kenya-offplan-leads.md) — HassConsult + Innova / AYCE; UC (Jul 2026 progress to 3rd floor); completion **Q1 2028** (Hass); from **KSh 10.5M**; URLs: hassconsult.com/kai · investment-collection · OMT · Innova LinkedIn Jul 2026.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Conflicts always highlighted.
- **Developer vs agents:** if developer sources **agree** on a field → **canonical = developer**; agents secondary.
- **Official vs official** (developer / developer-attributed pages disagree): **do not assume a winner** → flag **`needs_developer_input`**; no canonical among disagreeing official figures until verification resolves it.
- **Prices:** always keep full `price_claims[]` (all options).
- Payment must-have if ≥4 independent agent/portal sources **or any developer source**.
- Low-confidence / agent-only / uncorroborated → show with **`needs_verification`**. No invented GroupCompany.
- HassConsult named on brochure as **Development Consultants** + **Sole and Exclusive Selling Agents** — **not** primary developer (contrast Nouveau). Innova hosts brochure / progress / “our developments” language but brochure **Developer** line = **Ayce Investments Limited**.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer / developer-attributed sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = disagreeing official / professional sources — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Kai** (also styled **KAI**) | 5 | brochure; Hass project; OMT; Innova |
| `aliases` | secondary | Kai Diani; Kai resort residences; KAI Diani Resort Style Apartments | 4 | OMT; IADA; Innova LinkedIn |
| `status` | claim set | **Under construction** (OMT; Innova Jul 2026 progress to **3rd floor**). Hass markets live sales (off-plan / UC). Innova chapter: **95% sold out** (inventory claim — **`needs_verification`**) | 5 UC / 2 sold-% | OMT; Innova LI; Hass; Innova blog |
| `geography.city_context` | **CANONICAL** | **Diani** (seaside / beach destination framing) | 5 | all |
| `geography.county` | **CANONICAL** (context) | **Kwale County** (coast south of Mombasa) | 4 | geography context; discovery lead |
| `geography.neighbourhood` | soft / **needs_verification** for plot | Northern Diani, **second row** off main road with **direct walkway to beach** (OMT). Brochure: paved **5-minute walk** to beach; near The Maji Boutique Hotel / Diani Beach Rd landmarks | 4 / 3 | OMT; brochure map |
| `geography.access` | marketing claim | **~10 mins** Ukunda / Diani Airport; **~57 mins** Moi International Airport via Dongo Kundu Bridge | 4 | brochure; Hass blog |
| `geography.lat_lng` | geocode — **needs_verification** | **−4.312492, 39.579360** (`geo_method=geocode`) | 2 | Nominatim Diani Beach settlement 2026-10-16; no street published — low precision — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-ayce-investments-limited` | 5 | brochure “Developer Ayce Investments Limited”; OMT **CLIENT AYCE investments** |
| `co_developer_ids[]` | none invented | Innova “our developments” language **does not** override brochure Developer line — see RelatedParty §4 | — | |
| `unit_types` | claim set — **`needs_developer_input`** | **Marketed:** 1- & 2-bedroom (Hass; brochure hero; Innova home). **Also on brochure floor plan:** **Mini 1 Bed**. **Architect / award:** **studio** + 1BR + 2BR + **2BR plus** (OMT; IADA). Hass blog yields name **mini-one-bedroom**. No collapsed canonical mix label | ≤5 per claim; no winner | |
| `unit_count` | **CANONICAL** (agree) | **99** apartments (+ amenities) | 5 | OMT; IADA (“99 apartment units”) |
| `unit_mix_detail` | claim set — **`needs_developer_input`** | IADA: **24 studio / 55 one-bed / 16 two-bed / 8 two-bed plus**. Arithmetic **24+55+16+8 = 103 ≠ 99** → internal math conflict on award page; do **not** invent reconciliation | 3 claim / 0 math | IADA |
| `building_specs.floors` | **CANONICAL** (agree) | **Four floors** residential + **basement** parking/services (brochure “four floors”; IADA four floors + full basement; OMT residential floors + half-sunken / basement parking) | 5 | brochure; IADA; OMT |
| `building_specs.gfa_nfa` | **CANONICAL** (architect) | Gross **11,650 sqm**; net **7,930 sqm** | 5 | OMT; IADA echoes GFA |
| `size_by_type` | **CANONICAL** (brochure floor-plan labels) | See size table — sourced **sq.ft** only. Measure tag **gross vs plinth: unknown** | 5 | Innova-hosted brochure |
| `price_claims[]` | claim set — agent/consultant only this pass | See §1a — **no developer-published price on brochure**. Hass **from KSh 10.5M** | ≤4 | Hass project + IC |
| `currency` | **CANONICAL** | KES / KSh / Kshs | 5 | Hass |
| `payment_plan.tenor` | secondary — **needs_verification** | Hass: **payment over 18 months**. **Not** on Ayce-attributed brochure extract. Threshold: **not met** via developer schedule; only **1** selling-agent channel (not ≥4 agents) | 3 | Hass kai |
| `payment_plan.deposit` | unknown | Not found this pass | 0 | — |
| `completion_estimate` | claim set — **`needs_developer_input`** | Hass project: **Q1 2028**. OMT: timeframe **2024 – 2027**. Innova blog: **Q4 2027**. Brochure silent. **No assumed canonical** among disagreeing professional / marketing sources; Ayce microsite date **not found** | ≤4 each; no winner | Hass; OMT; Innova |
| `amenities` (core) | **CANONICAL** (brochure + Hass agree) | Resort-style residents reception; hallway atriums with planted greenery; **rooftop infinity swimming pool**; sunken pool lounge; poolside lounge & bar; alfresco dining; fully equipped gym; ocean-view retreat / poolside cabanas; walkable landscaped rooftop; AC provision; backup generator; high-speed lifts; 24/7 CCTV; high-speed Wi-Fi; intercom; electric fencing; secure parking | 5 | brochure; Hass kai |
| `amenities` (architect echo) | corroborating | Rooftop gardens / shaded terrace / gym / pool; atrium; covered parking basement | 5 | OMT; IADA |
| `interior_finishes` | soft | Open-plan living; private loggias; bathtub placement claim on IADA — design narrative, not finish schedule | 3 | IADA |
| `investment_return_claims` | marketing only — **not verified** | Hass blog: furnished/serviced yield up to **16% / 14% / 13%** (mini-1BR / 1BR / 2BR); appreciation up to **25% / 15% / 10%** — projections only | 1 | Hass blog |
| `legal_title` | unknown | Not found this pass | 0 | — |
| `foreign_ownership` | unknown | Not found this pass | 0 | — |
| `showroom / sales` | **CANONICAL** contact channel | HassConsult sole exclusive selling agents (brochure); show-house finishes in progress (Innova Jul 2026: 1-bed & 2-bed show houses glazing complete) | 5 / 4 | brochure; Innova LI |
| `property_reference` | secondary | HassConsult **Property Reference No. 2336** | 4 | brochure |

### Size table (brochure floor plan — measure tag unknown)

| Label (brochure) | Area (sq.ft) | Approx sqm (÷10.764, illustrative only) | Canonical sourced? |
|------------------|-------------:|----------------------------------------:|--------------------|
| Mini 1 Bed (units 11–14) | **373–374** | ~34.7 | Yes (sq.ft) |
| 1 Bed (various) | **614–809** | ~57–75 | Yes |
| 2 Bed (various) | **1029–1093** | ~96–102 | Yes |
| 2 Bed Plus (25–26) | **1419** | ~132 | Yes |

**Note:** Brochure hero copy says “1- and 2-bedroom residences” while the same PDF labels **Mini 1 Bed** on the first-floor plan — treat as **unit-type claim set** (§7).

### 1a. Price claims — keep **all** options (no scalar canonical)

| # | Claim | Value | Publisher | Flag |
|--:|-------|-------|-----------|------|
| A | Project page “from” / “PRICES FROM” | **KSh 10,500,000** | hassconsult.com/kai | Exclusive selling agent — **needs_verification** vs developer schedule (brochure silent) |
| B | Investment Collection “DIANI \| THE ULTIMATE SEASIDE ESCAPE” | **FROM KSHS. 10,500,000** | hassconsult.com/investment-collection | Same Hass channel — corroborates A |
| C | Developer brochure | **no price** | Innova-hosted Ayce brochure | Developer-attributed silent |
| D | Discovery lead | from KSh 10.5M | kenya-offplan-leads.md | Lead only |

**Canonical price_from:** **none** (no Ayce-published figure this pass). Retain A/B as Hass exclusive-agent claims.

### Payment plan — must-have recount

| Element | Agreeing sources | Count / type | Threshold (≥4 agents **or any developer**)? | Status |
|---------|------------------|--------------|-----------------------------------------------|--------|
| **18-month** payment | Hass kai page only | 1 exclusive-agent channel | **Not met** (not developer schedule; not ≥4 agents) | Soft claim + **`needs_verification`** |
| Deposit % / LOO schedule | — | 0 | Not met | unknown |
| Brochure payment table | Brochure extract | 0 usable | — | silent |

**Payment summary:** Must-have **not locked**. Show Hass **18 months** as high-authority agent claim only; confirm on Ayce/LOO.

---

## 2. Developer (primary)

| Field | Value |
|-------|-------|
| `id` | `dev-ayce-investments-limited` |
| `legal_name` | **Ayce Investments Limited** (OMT/IADA also style **AYCE investments**) |
| `trading_names` | Ayce Investments; AYCE |
| `website` | **unknown** this pass (no Ayce-owned project microsite recovered) |
| `group_company_id` | **null** — no parent invented (do **not** invent Innova↔Ayce GroupCompany) |
| `evidence` | (1) Brochure: “Developer / Ayce Investments Limited”. (2) OMT: “CLIENT AYCE investments”. (3) IADA credits: “CLIENT: AYCE investments” |
| `prior_projects_mentioned` | Brochure list: The Cube-Riverside; City Mall-Nyali; The Greenwood-Kitisuru; Bentley Park-Kitisuru; The Residences-General Mathenge; Karen Green; The Avenue-Nyali; Emirates Business Park — **delivery unverified this pass** |
| `sales_office` | Via HassConsult (sole exclusive selling agents on brochure) |

**Primary developer = Ayce Investments Limited (confidence 5 for identity on brochure + architect client line).**

---

## 3. GroupCompany

**None invented.** Innova Properties and Ayce Investments Limited both touch Kai in public materials; **no** sourced parent/subsidiary filing linking them this pass → leave GroupCompany **null**.

---

## 4. RelatedParty

| Field | Value |
|-------|-------|
| `id` | `rp-innova-properties` |
| `name` | Innova Properties |
| `relationship_type` | **RelatedParty** — brand / progress publisher / brochure host. **Not** named Developer on brochure. **Not** `co_developer` without stronger SPV evidence. **Not** GroupCompany. Soft **`marketing_partner`-adjacent** only if later LOO confirms; this pass keep generic RelatedParty |
| `website` | https://www.innovaproperties.co.ke/ |
| `linked_to` | Property Kai; hosts developer-attributed brochure PDF |
| `evidence` | (1) Homepage Kai card. (2) Hosts https://www.innovaproperties.co.ke/wp-content/uploads/2025/06/KAI-Brochure-E-Brochure.pdf (Developer = Ayce). (3) News: “KAI, DIANI… 95% sold out. (Completion Q4 2027)”. (4) LinkedIn Jul 2026: “our coastal apartment development” + construction milestones |
| `confidence` | 4 (role as publisher/progress clear; **legal contracting role vs Ayce** → **`needs_verification`**) |
| `not` | Not sole developer on brochure; not invented parent of Ayce |

| Field | Value |
|-------|-------|
| `id` | `rp-hassconsult-kai` |
| `name` | HassConsult Real Estate Limited |
| `relationship_type` | **Development consultant** + **sole exclusive selling agent** (brochure). OMT/IADA: “DEVELOPMENT & MARKETING HassConsult”. Modeled as RelatedParty **and** Agent (§5) — **not** primary developer on this project |
| `website` | https://www.hassconsult.com/ |
| `evidence` | Brochure Development Consultants / Sole and Exclusive Selling Agents block; OMT partners list; IADA credits |
| `confidence` | 5 |
| `not` | Not `dev-*` primary for Kai (contrast corpus Nouveau where HassConsult is developer-of-record) |

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| HassConsult Real Estate Limited | exclusive selling agent + development consultant | Project microsite; Investment Collection; blog; brochure sales block | https://www.hassconsult.com/kai |
| Innova Properties | RelatedParty channel (not independent portal) | Homepage + progress posts + brochure host | https://www.innovaproperties.co.ke/ |

Independent Kenya agent portals (Block, Vorsa, Craiova, BuyRent project cards) **not found** this pass — commercial surface is HassConsult- + Innova-heavy.

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | 0709 479 000 | HassConsult (brochure) |
| sales phone | 0709 479 479 | HassConsult Sales (brochure) |
| email | hello@hassconsult.com | HassConsult |
| url | https://www.hassconsult.com/kai | Property sales |
| url | https://www.hassconsult.com/ | HassConsult |
| address | ABC Place, Waiyaki Way; P.O. Box 14090 - 00800 Nairobi | HassConsult |
| property ref | 2336 | HassConsult |
| url | https://www.innovaproperties.co.ke/ | RelatedParty Innova |
| url | https://www.innovaproperties.co.ke/wp-content/uploads/2025/06/KAI-Brochure-E-Brochure.pdf | Brochure (Ayce developer credit) |
| url | https://omt-architects.com/work/kai | Architect project page |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| studio OMT architects | architect | OMT project page; IADA Silver Winner 2026; brochure design narrative aligns | 5 |
| metrix engineers | structural engineer | OMT / IADA credits | 5 named |
| LEHEM interiors | interior (+ landscape on IADA) | OMT / IADA | 5 named |
| gamma delta eastern africa | building services | OMT / IADA | 5 named |
| Tower Cost Consultant(s) | quantity surveyor | OMT / IADA; tagged on Innova LinkedIn | 5 named |
| KARIM CG Visuals | renderings | OMT / IADA | 4 |
| OMT team (Maryem Sadek, Filip Zieliński, Hazary Nic, Leander Moons, Viva Mugambi) | design team | IADA credits | 4 |
| Unnamed | contractor / financing / land vendor | Not found as named parties this pass | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under Cycle 2 lock |
|--:|-------|--------|-------------------------------|
| 1 | **Primary developer vs Innova “our developments”** | Brochure + OMT/IADA: **Ayce / AYCE**. Innova blog/LinkedIn: Kai as Innova coastal development | **Canonical primary = Ayce**. Innova = RelatedParty; legal role **`needs_verification`**. No GroupCompany invented |
| 2 | **HassConsult role** | Brochure: consultants + exclusive agents. OMT/IADA: development & marketing. Nouveau corpus pattern = Hass as developer-of-record | **Kai-specific:** Hass = RelatedParty + Agent — **not** `dev-*` primary |
| 3 | **Unit types marketed vs architect mix** | Hass/brochure/Innova hero: **1 & 2 bed**. Brochure plan: **Mini 1 Bed**. OMT/IADA: **studio** + 1BR + 2BR + 2BR+; Hass blog: mini-one-bedroom yields | **`needs_developer_input`** on public unit-type taxonomy; keep all claims |
| 4 | **Unit mix counts** | IADA 24/55/16/8 (= **103**) vs stated **99** (OMT + IADA header) | **`needs_developer_input`**. Canonical **unit_count = 99** (agreeing total); mix breakdown unsettled |
| 5 | **Completion** | Hass **Q1 2028** vs OMT **2024–2027** vs Innova **Q4 2027**; brochure silent | **`needs_developer_input`**. No assumed canonical |
| 6 | **Price from** | Hass **10.5M**; brochure silent | Keep `price_claims[]`; **no** developer-canonical from-price → Hass claim **`needs_verification`** |
| 7 | **Payment 18 months** | Hass only | Soft; must-have **not met**; **`needs_verification`** |
| 8 | **95% sold** | Innova chapter only; Hass still marketing from-price | Show Innova claim + **`needs_verification`** for current inventory |
| 9 | **Yield / appreciation %** | Hass blog projections only | Marketing; **not** verified returns |
| 10 | Brochure disclaimer | Hass particulars not guaranteed / not an offer | Always flag |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~12** |
| `sources_retained` | **10** |

**Selection note:** Scanned Hass kai, Investment Collection, Hass Diani/Kai blog, Innova-hosted brochure PDF, Innova homepage, Innova “next chapter” news, Innova LinkedIn Jul 2026 progress, OMT project page, IADA award page, Innova May 2026 LinkedIn, LinkedIn reshares, discovery lead. **Always kept** Hass project page + Ayce-credited brochure + OMT architect page. Retained 10 densest field-bearing sources (≥5 rule).

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://www.hassconsult.com/kai | HassConsult | project_site / exclusive agent | 2026-10-16 | From 10.5M; Q1 2028; 18-mo payment; 1&2 bed; amenities — **always keep** |
| 2 | https://www.innovaproperties.co.ke/wp-content/uploads/2025/06/KAI-Brochure-E-Brochure.pdf | Ayce (Developer) / HassConsult (agents) / Innova host | developer_attributed | 2026-10-16 | Ayce developer; Hass consultants/agents; sizes sq.ft; Mini 1 Bed on plan; amenities; Property Ref 2336 — **always keep** |
| 3 | https://omt-architects.com/work/kai | studio OMT architects | architect | 2026-10-16 | 99 units; GFA/NFA; UC; 2024–2027; AYCE client; consultants list — **always keep** |
| 4 | https://ad-c.org/winner/kai-diani-resort-style-apartments-silver-winner-household-residential-building-design-iada-2026/ | IADA / Architecture & Design Community | award / architect-attributed | 2026-10-16 | 99 units; 24/55/16/8 mix; 4 floors + basement; GFA 11,650; credits |
| 5 | https://www.hassconsult.com/investment-collection | HassConsult | agent portfolio | 2026-10-16 | “DIANI \| THE ULTIMATE SEASIDE ESCAPE” from 10.5M |
| 6 | https://www.hassconsult.com/post/diani-is-kenya-s-next-property-investment-hotspot-here-s-how-kai-delivers | HassConsult | agent / blog | 2026-10-16 | Mini-1BR named; yield/appreciation projections; access times |
| 7 | https://www.innovaproperties.co.ke/ | Innova Properties | related_party | 2026-10-16 | Kai card; 1&2 bed / four floors copy |
| 8 | https://www.innovaproperties.co.ke/urban-form-and-green-space-balancing-growth-with-vitality-2/ | Innova Properties | related_party / news | 2026-10-16 | **95% sold**; completion **Q4 2027** |
| 9 | https://www.linkedin.com/posts/innova-properties-kenya_kai-diani-progress-report-activity-7489976227127107585-ZgqQ | Innova Properties | related_party / social | 2026-10-16 | Jul 2026 progress — 3rd floor; show houses; rooftop pool works |
| 10 | https://www.linkedin.com/posts/innova-properties-kenya_kai-diani-progress-update-may-2026-activity-7462844463086718976-9MEy | Innova Properties | related_party / social | 2026-10-16 | May 2026 progress — earlier 3rd-floor milestone; UC corroboration |

### Evaluated but not retained (thin / overlap / failed)

| url | Why skipped |
|-----|-------------|
| https://www.linkedin.com/posts/patrick-korir-6a6bb8102_kai-diani-progress-report-activity-7493897823327977472-S2NQ | Reshare of Innova Jul post |
| https://www.linkedin.com/posts/innova-properties-kenya_innovaproperties-realestate-innovation-activity-7447243657788866561-toR_ | Social twin of Innova news #8 |
| https://www.innovaproperties.co.ke/?s=kai | Search shell — no denser fields |
| Discovery lead row in kenya-offplan-leads.md | Lead only — superseded by this dossier |

---

## 9. Field harvest → must-have extension proposals

| Proposed field / note | Kai evidence | Consensus note |
|------------------------|--------------|----------------|
| Geography scope **city + county outside Nairobi** | Diani / Kwale | Master index national / coast section (with NAK-001) |
| `exclusive_selling_agent` distinct from `primary_developer` | Hass on brochure; Ayce developer | Critical when HassConsult is agent not developer |
| RelatedParty for **brochure host / progress brand** ≠ developer | Innova vs Ayce | Do not collapse brands without SPV evidence |
| `unit_mix_detail[]` with checksum vs `unit_count` | IADA 103 vs 99 | Flag arithmetic conflicts explicitly |
| Size in **sq.ft** with measure tag unknown | Brochure | Keep sourced unit; optional sqm conversion labeled illustrative |
| Architect GFA/NFA + UC status | OMT | Strong when developer microsite absent |
| Payment tenor from exclusive agent only | Hass 18 mo | Do **not** auto-lock must-have without developer or ≥4 agents |

---

## Open questions (developer input)

1. Binding **completion**: Hass **Q1 2028** vs OMT **2024–2027** vs Innova **Q4 2027**?
2. Public **unit types**: are studios / mini-1beds sold as distinct SKUs or folded into “1 bed”? Confirm IADA **24/55/16/8** vs **99** total.
3. Publish **price list** + **payment/deposit** schedule under Ayce (brochure currently silent; Hass from 10.5M / 18 months only).
4. Clarify **Innova Properties** legal role vs **Ayce Investments Limited** (same group? marketing only? contracting party on LOO?).
5. Current **inventory** vs Innova **95% sold** claim while Hass still markets from-price.
6. Plot GPS / exact street address (second-row northern Diani walkway).
