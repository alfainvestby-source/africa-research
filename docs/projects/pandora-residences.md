---
slug: pandora-residences
external_id: NBO-002
cycle: 1
pilot: true
retrofit: cycle-2-locks
needs_verification_rule: applied
needs_developer_input_rule: applied
last_verified_at: 2026-10-18
---

# Pandora Residences (NBO-002) — Cycle 1 pilot (Cycle 2 lock retrofit)

CSV seed (unverified leads): location Muthangari Drive, Westlands; stage `off_plan`; completion Q4 2028; `price_from_kes` 12,910,000; sales_contact Block/Loyd Mokaya; developer “A1 Corporation”.

Live research: official site + official brochure PDF + portals/agents accessed 2026-10-15.  
**2026-10-18:** Official project URL reconfirmed as user-provided **https://pandora.co.ke/** (live OK). Google Maps CID `12900601372674958277` **browser-resolved** → place **Pandora**, PGQ+M66 Muthangari Dr, Nairobi (−1.260829, 36.780513); site match pandora.co.ke.  
**Locks:** developer-vs-agent → **canonical = developer** when developer sources **agree**; **official-vs-official** → show both + **`needs_developer_input`** (no assumed winner); prices always **`price_claims[]`** (no forced portal scalar); low-conf/agent-only → show + **`needs_verification`**. No invented GroupCompany.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed **and** developer sources agree. Secondary = agent/portal. **`needs_verification`** = low-conf agent-only / uncorroborated. **`needs_developer_input`** = official materials disagree — do not pick a canonical.

| Field | Role | Value | Conf | Flag | Sources |
|-------|------|-------|-----:|------|---------|
| `canonical_name` | **CANONICAL** | Pandora Residences | 5 | — | pandora.co.ke, brochure |
| `aliases` | secondary | Pandora; A-One Pandora; A1 Pandora; Pandora Residence; A-One Pandora Residences | 4 | — | portals/agents |
| `status` | claim set | CSV/`off_plan`/selling; NRE “Pre-Launch” — **CONFLICT** (labels) | 4 | — | CSV, NRE, agents |
| `geography.city` | **CANONICAL** | Nairobi | 5 | — | site, brochure |
| `geography.neighbourhood_street` | **CANONICAL** | Westlands — Muthangari Drive, opposite The Address Offices | 5 | — | site, brochure (+ agents agree) |
| `geography.lat_lng` | **CANONICAL** (Maps place) | **−1.260829, 36.780513** (`geo_method=official`, provider `google_maps_place`) | 4 | User Maps CID `12900601372674958277` browser-resolved 2026-10-18: place **Pandora**, PGQ+M66 Muthangari Dr, Nairobi; website pandora.co.ke. Nominatim −1.259691, 36.785148 secondary (demoted). On `properties.lat/lng` — see [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-a-one-corporation` | 5 | — | site |
| `unit_types` | claim set — **OFFICIAL vs OFFICIAL** | (A) site + brochure p.5: **2, 3 & 4 BR**; (B) brochure p.2: **3, 4 & 5 BR**; (C) brochure p.19 plan: **5BR+DSQ** | 2 | **`needs_developer_input`** | site vs brochure |
| `size_by_type` | **CANONICAL** (brochure floor-plan pages agree) | 3BR+study+DSQ **152.68 sqm**; 4BR+DSQ **194.32 sqm**; 5BR+DSQ **291.21 sqm** | 5 | — | brochure pp.18–19 |
| `size_by_type` (agent 2BR bands) | secondary | 2BR 85.34–108.8; 2BR+study 129.14 | 3 | **needs_verification** | Ravi, Sydia, Block, Property Box |
| `size_by_type` (agent 3/4 BR) | secondary | 3BR ~155.82–160.65; 4BR ~199.56–213 (vs brochure) | 3 | — (secondary vs canonical sizes) | Ravi, Sydia, Block, NRE, Ladva |
| `inventory.2BR_sold_out` | secondary | Block + Ladva: sold out; Ravi/Sydia still list 2BR; site still shows 2BR plan | 2 | **needs_verification** | Block, Ladva vs Ravi, Sydia, site |
| `price_claims[]` | multi-claim only — **no canonical / no forced scalar** | See §1a | ≤3 | per-row flags | agents/portals; no developer prices |
| `currency` | **CANONICAL** (implied KES; agents explicit) | KES | 5 | — | portals |
| `payment_plan.deposit` | secondary → must-have (≥4 agents) | **20% deposit** | 3 | — | Block, NRE, Ladva, Sydia |
| `payment_plan.tenor` | secondary | **36 months** / quarterly | 2 | **needs_verification** | Ladva |
| `completion_estimate` | secondary consensus | **December 2028** / CSV Q4 2028 | 4 | — | Block, Hauzisha, NRE, Ladva, Ravi, Sydia, CSV |
| `amenities` (core) | **CANONICAL** (site + brochure agree) | Pool, spa/sauna, fitness, co-working, lounge, restaurant/café, retail boulevard, smart home, children’s play, games room, double-height ceilings, concierge, terraces/balconies, zen garden / courtyard | 5 | — | site + brochure |
| `building_specs.retail` presence | **CANONICAL** (site + brochure agree) | Retail boulevard / mall | 5 | — | brochure, site |
| `building_specs.retail` 1.7-acre | secondary | 1.7-acre shopping mall | 3 | **needs_verification** | Block/agents |
| `building_specs.garden` 3,000 m² | secondary | 3,000 m² central garden | 3 | **needs_verification** | Block/agents |
| `building_specs.floors` | secondary | 17 floors | 2 | **needs_verification** | Property Box |
| `legal_title` | secondary | Leasehold | 2 | **needs_verification** | Property Box |
| `showroom` | secondary | Ready 4BR showroom opposite The Address | 3 | **needs_verification** | Ravi, Sydia |

### 1a. `price_claims[]` (always multi — no portal scalar)

No developer prices on site or brochure extract → **no canonical price**.

| # | Claim (KES) | Context | Conf | Flag | Sources |
|--:|-------------|---------|-----:|------|---------|
| 1 | from **12.91M** | Historic / sold-out standard 2BR (85–108 sqm per Block FAQ) | 2 | **needs_verification** | Block FAQ, CSV NBO-002 |
| 2 | **12.91M – 18.09M** | 2BR size ladder still listed | 3 | **needs_verification** (availability contested) | Ravi, Sydia |
| 3 | **19.17M – 21.11M** | 2BR + study (~129.14 sqm) | 3 | — | Block, Ravi, Sydia |
| 4 | **24.61M – 28.11M** | 3BR + study + DSQ (~155–160 sqm) | 3 | — | Block, NRE, Ladva, Ravi, Sydia |
| 5 | **31.53M – 37.27M** | 4BR + DSQ (~199–213 sqm; bands diverge) | 3 | — | Block, NRE, Ladva, Sydia |
| 6 | **14M – 33.6M** | Aggregated “from–to” band | 2 | **needs_verification** (outlier “from”; not echoed) | Hauzisha |

Do **not** collapse to a single `price_from` for portal/index until confidence + coverage rules allow.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-a-one-corporation` |
| `legal_name` | A-One Corporation |
| `trading_names` | A1 Corporation; A-ONE; A-One Developments (Ravi wording only — secondary) |
| `website` | Project: **https://pandora.co.ke/** (user-provided official; live 2026-10-18; no separate corporate homepage confirmed) |
| `evidence` | pandora.co.ke “Developer / A-ONE CORPORATION”; brochure on same domain; user confirm 2026-10-18 |
| `group_company_id` | **null — none invented** |
| `prior_projects_mentioned` | Panorama West (official site); NRE also lists A1 Acacia (agent portfolio link, not handover proof) |

**Proposal:** Original developer = **A-One Corporation / A1 Corporation** (confidence **5**).

---

## 3. GroupCompany

**None.** No parent entity evidenced. Do not invent.

---

## 4. RelatedParty

None required for Pandora (no unproven brand-overlap partner analogous to Astra/Laureland).

Karim CG Visuals stays under **Stakeholders** (named on developer site), not GroupCompany.

---

## 5. Agents + Contacts

### Agents / portals

| Agent | Type | Role | URL |
|-------|------|------|-----|
| Block Real Estate | agency / aggregator | CSV sales_contact; article + FAQ | https://block.ke/investment-intelligence/pandora-residences-on-muthangari-drive/30451/ |
| Hauzisha | portal | Inventory summary | https://hauzisha.co.ke/developments/pandora/ |
| NRE Real Estate | agency | Listing + developer profile | https://nairobirealestate.co.ke/properties/pandora-residence |
| Ladva Realtors | agency | Sales page | https://ladvarealtors.com/a-one-pandora-residences-luxury-apartments-for-sale-in-westlands/ |
| Ravi Homes | agency | Price table + showroom | https://ravihomes.co.ke/developments/a-one-pandora/ |
| Sydia Realty | agency | Price table + showhouse updates | https://sydiarealty.com/estate_property/a1-pandora-redefining-luxury-living-in-nairobi/ |
| Property Box | portal | Uses developer sales contacts; floors/tenure claims | https://propertybox.co.ke/developments/pandora-residences/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 113 111 888 | Property sales office |
| email | sales@pandora.co.ke | Property sales office |
| email | sales@pandora.ke | Property sales office (alias) |
| url | https://pandora.co.ke/ | Property (official — user-provided 2026-10-18) |
| url | https://pandora.co.ke/assets/brochure.pdf | Property (official brochure) |
| phone | +254 725 937 686 | Agent: Block / Loyd Mokaya (CSV) |
| email | loyd@block.ke | Agent: Block (CSV) |
| phone | +254 730 731 355 | Portal: Hauzisha |
| phone | +254 141 361 320 | Agent: NRE |
| email | info@nairobirealestate.co.ke | Agent: NRE |
| phone | +254 729 088 853 / +254 721 473 518 | Agent: Ladva |
| email | info@ladvarealtors.com | Agent: Ladva |
| phone | +254 105 772 200 | Agent: Ravi |
| email | sales@ravihomes.co.ke | Agent: Ravi |
| phone | +254 700 437 505 / +254 759 333 300 | Agent: Sydia |
| email | info@sydiarealty.com | Agent: Sydia |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| Karim CG Visuals | other (concept & marketing / visuals) | pandora.co.ke “The team Behind”; `analytics.karimexclusives.com` on site | 5 |
| Unnamed design firm | architect/design | Official “region’s leading real estate design firm” — unnamed | 1 |

No financing / contractor / land vendor named.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Unit mix (official vs official)** | Site + brochure p.5: **2, 3 & 4 BR**. Brochure p.2: **3, 4 & 5 BR**. Brochure p.19: **5BR+DSQ**. | Show all. Flag **`needs_developer_input`**. **No canonical mix** until developer clarifies. Agent sold-out is separate inventory claim. |
| 2 | **Sizes (developer vs agent)** | Brochure floor plans agree: 152.68 / 194.32 / 291.21. Agents: ~155–160 / ~199–213 (+ 2BR bands). | **Canonical = brochure** (developer sources agree on plan pages). Agents secondary; agent 2BR bands **`needs_verification`**. |
| 3 | **Prices** | Multi options §1a (12.91M … 37.27M + Hauzisha 14M). | **No canonical / no forced scalar.** Keep full `price_claims[]`; row-level **`needs_verification`** where low-conf. |
| 4 | **2BR sold-out / availability** | Site shows 2BR; Block/Ladva: sold out; Ravi/Sydia still price 2BR. | Show all; **`needs_verification`**. |
| 5 | **Floors / tenure** | Property Box: 17 floors; leasehold. | Secondary + **`needs_verification`**. |
| 6 | **Completion** | Multi-agent Dec 2028; not in brochure text extract. | Consensus (conf 4); not developer-canonical until on developer material. |
| 7 | Brochure disclaimer | Illustrations may change; not binding. | Always flag. |

### Payment plan source recount (threshold ≥4)

| Element | Sources stating it | Count | Meets must-have? |
|---------|-------------------|------:|------------------|
| **20% deposit** | Block; NRE; Ladva; Sydia | **4** independent agent/portal | **Yes** (agent threshold; conf capped at 3 — no developer schedule) |
| Balance over construction / to completion | Block; NRE; Ladva; Sydia; Ravi (“flexible”) | ≥4 vague “instalments” | Yes as soft claim; exact schedule unknown |
| **36-month tenor** / quarterly | Ladva (explicit); others unspecified | **1** clear | **No** — nice-to-have / unknown for tenor |
| Developer LOO/schedule | Not found on site or brochure extract | 0 | — |

**Canonical payment plan:** none (no developer source).  
**Must-have secondary claim:** 20% deposit (4 agents).  
**Not must-have:** 36-month tenor.

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~12** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~12 candidates (official site, brochure PDF, Block, Hauzisha, NRE listing, NRE developer profile, Ladva, Ravi, Sydia, Property Box, The Africa Nomad, plus CSV seed as non-web lead). **Always kept** developer site + official brochure. Retained 10 richest field-bearing pages (≥5 rule).

**Thin / skipped (not in retained list):**
- https://theafricanomad.com/real-estate/pandora-residences-muthangari-drive-westlands/ — earlier search hit; **HTTP 500 on re-fetch** → dropped as unreliable
- CSV NBO-002 row — seed lead only (not an independent published source)
- Facebook/Instagram search hits — not opened as full pages this pass (thin social discovery only)

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://pandora.co.ke/ | Pandora Residences | project_site | 2026-10-18 | Official project site — user-provided; live re-fetch OK; always keep |
| 2 | https://pandora.co.ke/assets/brochure.pdf | Pandora Residences | project_site | 2026-10-15 | Official PDF — canonical sizes |
| 3 | https://block.ke/investment-intelligence/pandora-residences-on-muthangari-drive/30451/ | Block | portal | 2026-10-15 | 20%; prices; Dec 2028 |
| 4 | https://hauzisha.co.ke/developments/pandora/ | Hauzisha | portal | 2026-10-15 | Price band outlier |
| 5 | https://nairobirealestate.co.ke/properties/pandora-residence | NRE | agent | 2026-10-15 | 20% example |
| 6 | https://nairobirealestate.co.ke/developers/a-one-corporation | NRE | agent | 2026-10-15 | Developer profile |
| 7 | https://ladvarealtors.com/a-one-pandora-residences-luxury-apartments-for-sale-in-westlands/ | Ladva | agent | 2026-10-15 | 20% + 36 months |
| 8 | https://ravihomes.co.ke/developments/a-one-pandora/ | Ravi Homes | agent | 2026-10-15 | Size/price table |
| 9 | https://sydiarealty.com/estate_property/a1-pandora-redefining-luxury-living-in-nairobi/ | Sydia | agent | 2026-10-15 | 20%; showhouse |
| 10 | https://propertybox.co.ke/developments/pandora-residences/ | Property Box | portal | 2026-10-15 | Floors/tenure (weak but unique claims) |

---

## 9. Field harvest (aligned to locked living must-haves)

| Field | Pandora status | Notes |
|-------|----------------|-------|
| canonical_name / aliases | OK | Developer |
| status | OK as claim set | Label conflict |
| geography | OK | Developer |
| primary_developer | OK | Developer |
| unit_types claim set | Official vs official | **`needs_developer_input`** (C2 lock #8) |
| size + measure tag | Brochure plan pages agree → canonical | gross/plinth unknown |
| amenities core | OK | Developer sources agree |
| completion_estimate | Multi-agent | Not on brochure extract |
| price_claims[] | Multi-row §1a — **no scalar** | C2 lock #9 |
| payment_plan | **20% must-have via ≥4 agents**; tenor **`needs_verification`** | |
| sources / agents / contacts | OK | Relational split |
| GroupCompany | none | Correctly empty |
| Low-conf / agent-only / sold-out | **Shown** + **`needs_verification`** | method #6 |
| Official vs official | **`needs_developer_input`** | unit_types |

---

## Retrofit summary (Cycle 2 locks)

- **Canonical** only where developer sources **agree**: name, geography, developer, brochure floor-plan sizes, core amenities, retail presence.  
- **Official vs official** unit mix → **`needs_developer_input`** (not collapsed to `needs_verification` alone).  
- Prices → multi **`price_claims[]`** (§1a); no forced `price_from` scalar.  
- Agent sold-out / thin claims still **shown** + **`needs_verification`**.  
- GroupCompany null. No new projects.
