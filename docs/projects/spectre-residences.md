---
slug: spectre-residences
external_id: DISC-NBO-031
wave: user-lead-2026-10-18
pilot: false
sources_evaluated: 12
sources_retained: 8
inventory_class: off_plan
last_verified_at: 2026-10-18
---

# Spectre Residences (DISC-NBO-031) — discovery research

**New project** — not in seed corpus except thin Block lead. User-provided official site + contacts + unit claims; live research accessed **2026-10-18**.

**Official project site:** https://spectre.ke/  
**Developer site:** https://ayarealestateltd.com/ (developments hub)

**Block.ke ignored as authority** (low-trust discovery only — [block.ke/project/spectre-residences/](https://block.ke/project/spectre-residences/) thin / wrong-listing noise). **Never** use Hauzisha `0730 731 355` as developer phone (not seen on Spectre sources this pass).

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready — **not** Ready-tagged; marketing as new / off-plan residences.

**≠** `prop-aya-luxury-residence` / **DISC-NBO-023** (Whitehorse ex-AAD, Othaya × Makueni, Kileleshwa) — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Flag | Sources |
|-------|------|-------|-----:|------|---------|
| `canonical_name` | **CANONICAL** | **Spectre Residences** (site also “Spectre”; AYA hub “Spectre by AYA”) | 5 | — | spectre.ke; ayarealestateltd.com/developments |
| `aliases` | secondary | Spectre; Spectre by AYA; Spectre Westlands | 4 | — | AYA hub; agents |
| `inventory_class` | **CANONICAL** soft | **`off_plan`** — new launch / hotel-managed residences for sale; **not** Ready | 4 | — | spectre.ke; AYA hub; CPK “Off-plan” feature; no Ready tag |
| `status` | claim set | Off-plan / launching — LinkedIn launch posts **Aug–Sep 2026**; CPK Off-plan chip; **no** UC % this pass | 4 / 2 | — | AYA LinkedIn; Karim LinkedIn; CPK |
| `geography.city` | **CANONICAL** | Nairobi | 5 | — | all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** | 5 | — | spectre.ke; AYA; agents |
| `geography.street` | **CANONICAL** soft | **Westlands Road** — AYA: **AU Close, Westlands Road** (metres from Villa Rosa Kempinski; ~350 m GTC) | 5 / 4 | — | spectre.ke Location; AYA developments |
| `geography.marketing_blurb` | secondary marketing | “high-demand corridor with consistent value growth” | 2 | Marketing — not a geo fact | spectre.ke Location copy; user lead |
| `geography.lat_lng` | pending Maps CID | User CID `8594377129674105266` — **browser resolve in flight**; HTML/curl alone → US defaults only (**no invent**). Nominatim street approx secondary if CID fails: Westlands Road ≈ **−1.271911, 36.811024** (conf 2) | 0–2 | see §1c | Maps CID; Nominatim 2026-10-18 |
| `primary_developer_id` | **CANONICAL** (trading) | → **`dev-aya-real-estate`** (AYA Real Estate / AYA Real Estate Ltd) — **new** row; **≠** Whitehorse / DISC-NBO-023 | 5 | — | spectre.ke Developer; ayarealestateltd.com |
| `unit_types` | **CANONICAL** | **1 Bedroom**; **2 Bedroom** | 5 | — | spectre.ke; AYA hub |
| `size_by_type` | **CANONICAL** | **1BR 50 sqm** and **65 sqm** (band **50–65**); **2BR 100 sqm** | 5 | — | spectre.ke floor plans + summary; AYA typed sizes agree |
| `building_specs.storeys` | **CANONICAL** soft | **23** floors | 5 | — | ayarealestateltd.com/developments; Karim LinkedIn |
| `building_specs.theme` | **CANONICAL** soft | Hotel-themed / hotel-managed residential | 5 | — | AYA hub; Karim LinkedIn |
| `building_specs.density` | secondary | Karim: **9 residences per floor** | 3 | **needs_verification** | Karim LinkedIn only |
| `price_claims[]` | multi — **official vs official** | See **§1a** | ≤5 | **`needs_developer_input`** on floor | spectre.ke vs AYA hub vs agents |
| `currency` | **CANONICAL** | **KES** | 5 | — | official + agents |
| `payment_plan` | **CANONICAL** (developer) — must-have **met** | See **§1b** — reservation **KES 100K**; **20%** on signing; balance **36 months** | 5 | — | spectre.ke Terms of acquisition |
| `completion_estimate` | unknown this pass | — | 0 | — | Not on spectre.ke / AYA hub plaintext |
| `amenities` (core) | **CANONICAL** | User list **all confirmed** on spectre.ke THE AMENITIES — see **§1d** taxonomy map | 5 | — | spectre.ke |
| `amenities` (extended) | **CANONICAL** soft | Heated infinity pool; 11th-floor sky terrace / garden; 21st-floor sky lounge; fitness; spa; cinema; business / meeting; fine dining / restaurant | 5 | — | spectre.ke amenity explorer + AYA list |
| `roi_claim` | secondary marketing | spectre.ke ROI table (furnished / unfurnished / Airbnb scenarios on 3rd-floor purchase prices) — illustrative | 2 | **needs_verification** (yield assumptions) | spectre.ke |
| `legal_title` | unknown | — | 0 | — | not found |
| `master_planned_community` | none | Standalone Westlands Road tower | — | — | — |

### 1a. `price_claims[]` — keep **all** (no forced scalar)

**User lead vs official project site:** user **1BR 50–65 from 9.7M** / **2BR 100 from 18.4M** **matches** https://spectre.ke/ summary + ROI table (50 → **9.7M**; 65 → **12.4M**; 100 → **18.4M**).

**Official vs official conflict:** AYA corporate developments page still lists older typed floors (**8.8M / 11.2M / 16.7M**). Agents (CPK, Nairobi Realty) echo the **8.8M / 16.7M** ladder. → show both; flag **`needs_developer_input`**; do **not** pick a silent winner for portal scalar.

| # | Claim (KES) | Context | Conf | Flag | Sources |
|--:|-------------|---------|-----:|------|---------|
| 1 | **1BR 50 sqm → 9,700,000**; **1BR 65 → 12,400,000**; **2BR 100 → 18,400,000**; hero **from 9.7M** | Project site ROI + summary | 5 | — | spectre.ke |
| 2 | **1BR 50 → 8,800,000**; **1BR 65 → 11,200,000**; **2BR 100 → 16,700,000** | Corporate developments typed list | 4 | **`needs_developer_input`** vs #1 | ayarealestateltd.com/developments |
| 3 | From **8.8M** (1BR 50–65); 2BR from **16.7M** | Agent cards | 3 | Secondary; aligns #2 | CPK; Nairobi Realty |
| 4 | From **8.8M** (1BR) | Exclusive-sales social | 3 | Aligns #2 | Karim Exclusives LinkedIn |

**Portal scalar:** none until official floors reconcile (prefer live LOO / updated AYA hub).

### 1b. Payment plan — must-have **met** (developer)

| Element | Value | Sources | Meets must-have? |
|---------|-------|---------|------------------|
| Reservation | **KES 100,000** | spectre.ke; CPK; Nairobi Realty; Karim LinkedIn | Yes (developer) |
| Deposit / on signing | **20%** on sale agreement | spectre.ke; agents | Yes (developer) |
| Balance tenor | **36 months** monthly | spectre.ke; agents | Yes (developer) |
| Cash option | Full cash or flexible instalments | AYA hub (no typed schedule beyond “contact”) | Soft |

**Canonical payment plan:** reservation **100K** + **20%** on signing + **36-month** balance (spectre.ke). Agents corroborate; subject to LOO (CPK/Nairobi Realty caveat).

### 1c. Map / geo

| Candidate | lat | lng | method | conf | notes |
|-----------|-----|-----|--------|-----:|-------|
| Google Maps CID `8594377129674105266` | *pending browser* | *pending* | official / google_maps_place | — | Same approach as Pandora; curl HTML = US default only — **no invent** |
| Nominatim `Westlands Road, Westlands, Nairobi` | −1.271911 | 36.811024 | geocode | 2 | Street centroid; approx badge if CID fails |
| Landmark check Villa Rosa Kempinski | −1.271483 | 36.809093 | geocode | 1 | Adjacency only — **not** plot pin |

### 1d. Amenities — user list × official × feature taxonomy

All **12** user amenities appear on spectre.ke THE AMENITIES (HTML entities for `&`).

| User / site label | `feature.slug` | Scope | Conf | Notes |
|-------------------|----------------|-------|-----:|-------|
| Residents Lounge | `lounge` | development | 5 | |
| Garden Lounge | `lounge` | development | 5 | Variant note: garden lounge (also near `green_area`) |
| Play Lounge | `kids_play` | development | 5 | Play lounge / children’s play |
| Meeting Room | `conference_room` | development | 5 | |
| Yoga & Wellness | `yoga` | development | 5 | |
| Valet Parking | `parking` | development | 5 | Variant: valet |
| Fine Dining | `restaurant_cafe` | development | 5 | |
| Spa & Sauna | `spa` + `sauna` | development | 5 | Split both rows |
| Fitness Gym | `gym` | development | 5 | |
| Swimming Pool | `swimming_pool` | development | 5 | Site also heated infinity / 21st floor |
| Concierge | `concierge` | development | 5 | |
| Private Cinema | `cinema` | development | 5 | |

**Extended (official, not on user shortlist):** sky terrace / sky lounge; business centre / co-working (`coworking`); games room (`indoor_gaming`); spa floors — keep as dossier amenities; seed `property_feature` on steward pass.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | **`dev-aya-real-estate`** (**new** — do **not** reuse `dev-whitehorse-real-estate`) |
| `legal_name` | AYA Real Estate Ltd (trading **AYA Real Estate**; legal SPV for Spectre plot **unknown** — do not invent) |
| `website` | https://www.ayarealestateltd.com/ · project https://spectre.ke/ |
| `evidence` | spectre.ke “The Developer” + AYA logo/alt; ayarealestateltd.com Spectre by AYA |
| `group_company_id` | **null — none invented** |
| `confidence` | **5** (trading / brand on official materials) |

**Proposal:** Primary developer = **AYA Real Estate** (conf **5** trading). **≠** Whitehorse / AAD / Sandoral / DISC-NBO-023.

---

## 3. GroupCompany

**None.** No parent evidenced. Do not invent.

---

## 4. RelatedParty

| Name | Type | Conf | Evidence |
|------|------|-----:|----------|
| **Karim Real Estate Elevated** / **Karim Exclusives** | **`marketing_partner`** (exclusive sales + development concept & marketing) | 5 | spectre.ke team alt “Karim Real Estate Elevated”; Exclusive Sales Partner contacts; karimexclusives.com |
| EHS article calling Karim “developer behind Spectre” | conflict noise | 1 | ehsafrica.org — **reject as primary**; official site names AYA developer + Karim sales/concept |

Do **not** merge with `stk-karim-cg` (Pandora visuals) without steward review — same brand family possible, different role evidence.

---

## 5. Agents + Contacts

### Agents / portals (secondary)

| Agent | Type | Role | URL |
|-------|------|------|-----|
| CPK Real Estate | agency | Listing from 8.8M | https://commercialpropertykenya.com/properties/spectre-residences-westlands-1-2-bedrooms/ |
| Nairobi Realty | agency | Listing from 8.8M | https://nairobirealty.co.ke/listing/spectre-residences/ |
| Karim Exclusives | exclusive sales | Official sales partner | https://www.karimexclusives.com / LinkedIn |
| Block Real Estate | aggregator | Thin project hub — **not authority** | https://block.ke/project/spectre-residences/ |

### Contacts

| Channel | Value | Owner | Notes |
|---------|-------|-------|-------|
| phone | **+254 140 000 444** | Developer / project | spectre.ke + ayarealestateltd.com; **user-provided** |
| phone | **+254 752 000 444** | Developer (corporate) | **User-provided**; on **ayarealestateltd.com** (not on spectre.ke contact strip this pass) |
| email | **info@ayarealestateltd.com** | Developer | spectre.ke; user-provided |
| url | **https://www.ayarealestateltd.com/** | Developer | user www.ayarealestateltd.com |
| url | **https://spectre.ke/** | Property | Official project site |
| phone | **+254 140 000 700** | Exclusive sales (Karim) | spectre.ke |
| email | **sales@karimexclusives.com** | Exclusive sales (Karim) | spectre.ke |
| url | **https://www.karimexclusives.com** | Exclusive sales | spectre.ke |
| phone | +254 78 444 8888 | Agent: CPK | secondary |
| phone | +254 700 624 620 | Agent: Nairobi Realty | secondary |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Blink Studio Limited** | architect | spectre.ke team image alt “Blink Studio Limited”; user lead | 5 |
| Metrix Integrated Consultancy LLP | structural_engineer | spectre.ke plaintext | 5 |
| Miller & Company Advocates | other (project advocate / counsel) | spectre.ke plaintext | 5 |
| Interior Concept & Design | other | Label on spectre.ke team row — **firm name not in plaintext** this pass (likely image-only) | 1 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Sale prices (official vs official)** | spectre.ke **9.7 / 12.4 / 18.4M** vs AYA hub **8.8 / 11.2 / 16.7M**; agents echo older ladder | Show all in `price_claims[]`. **`needs_developer_input`**. No portal scalar. |
| 2 | **Street precision** | Westlands Road (project) vs **AU Close, Westlands Road** (AYA) | Prefer AYA street detail as soft-canonical with Westlands Road neighbourhood; both official. |
| 3 | **Karim as “developer” (EHS)** | EHS vs spectre.ke AYA developer + Karim sales/concept | **Canonical developer = AYA**; Karim = `marketing_partner`. |
| 4 | **Maps CID** | Browser resolve in flight; curl fails | **Do not invent**; Nominatim street only if CID fails. |
| 5 | **Completion** | Unpublished | Leave unknown. |

---

## 8. Disambiguation

| Other entity | Why distinct |
|--------------|--------------|
| **AYA Luxury Residence** (`prop-aya-luxury-residence`, DISC-NBO-023) | Whitehorse (ex-AAD); **Othaya × Makueni, Kileleshwa**; mixed villas/apts from ~7.5–8.5M agent ladder — **different developer brand + site** |
| Gaia / Diplomat (Wonder) / Citrine (Jafu) / other Westlands Rd towers | Different developers |
| Karim CG Visuals (Pandora stakeholder) | Visuals-only on Pandora; Spectre evidence is **Karim Real Estate Elevated / Karim Exclusives** sales+concept — related brand possible, **separate RelatedParty** until steward merges |

---

## 9. Sources (retained **8**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~12** |
| `sources_retained` | **8** |

**Selection note:** Scanned official project site, AYA corporate + developments, Karim exclusives / LinkedIn, CPK, Nairobi Realty, Block hub, EHS article, AYA LinkedIn, Nominatim, Maps CID. **Always kept** spectre.ke + AYA developments. Retained 8 richest (≥5 rule).

**Thin / skipped:**
- https://block.ke/project/spectre-residences/ — low-trust; empty/wrong listing noise
- https://ehsafrica.org/… — mislabels Karim as developer; thin investment blurb
- User CSV/Block lead row — not independent published source
- Social image carousels without field density

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://spectre.ke/ | Spectre / AYA | project_site | 2026-10-18 | Always keep — prices 9.7/12.4/18.4M; amenities; payment; team |
| 2 | https://ayarealestateltd.com/developments | AYA Real Estate | developer | 2026-10-18 | 23 floors; AU Close; **older** typed prices 8.8/11.2/16.7M |
| 3 | https://ayarealestateltd.com/ | AYA Real Estate | developer | 2026-10-18 | Brand + phones 140/752 |
| 4 | https://commercialpropertykenya.com/properties/spectre-residences-westlands-1-2-bedrooms/ | CPK | agent | 2026-10-18 | 8.8M ladder; payment echo |
| 5 | https://nairobirealty.co.ke/listing/spectre-residences/ | Nairobi Realty | agent | 2026-10-18 | 8.8M / 16.7M; amenity floors |
| 6 | https://www.karimexclusives.com | Karim Exclusives | marketing_partner | 2026-10-18 | Exclusive sales brand home |
| 7 | https://www.linkedin.com/posts/susan-njoka-merchant-of-happiness_nairobirealestate-westlandsnairobi-realestateinvestment-activity-7497722085507780608-7jQo | Karim Exclusives | agent_social | 2026-10-18 | 8.8M; 9/floor; payment |
| 8 | https://www.linkedin.com/posts/linkedin%2Ecom-company-ayarealestateltd_spectrebyaya-westlandsrealestate-nairobirealestate-activity-7510580623783329792-4eMQ | AYA Real Estate | developer_social | 2026-10-18 | Westlands Road launch |

---

## 10. Field harvest (must-haves)

| Field | Spectre status | Notes |
|-------|----------------|-------|
| canonical_name / aliases | OK | Developer |
| status / inventory_class | OK soft | `off_plan`; not Ready |
| geography | OK | Westlands / Westlands Road (+ AU Close) |
| primary_developer | OK | **AYA Real Estate** — new id |
| unit_types + sizes | OK | 1&2 BR; 50/65/100 |
| amenities | OK | User 12/12 + taxonomy map |
| price_claims[] | Multi — **NDI** official floors | User matches spectre.ke |
| payment_plan | **Must-have met** | Developer 100K / 20% / 36 mo |
| completion | Unknown | — |
| sources / agents / contacts | OK | |
| GroupCompany | none | |
| Map pin | CID pending | No invent |

---

## Retrofit / steward notes

- Seed **`dev-aya-real-estate`** separately from Whitehorse.
- RelatedParty **Karim** = `marketing_partner` (exclusive sales + concept).
- Stakeholders: Blink (architect), Metrix (structural), Miller & Co (advocate).
- Prefer **spectre.ke** media for galleries (official).
- After Maps CID browser success: write `geo_pin` conf ≥4 + promote `properties.lat/lng` if approach matches Pandora.
