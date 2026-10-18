---
slug: ivy-myst
external_id: DISC-NBO-032
wave: user-lead-2026-10-18
pilot: false
sources_evaluated: 11
sources_retained: 7
inventory_class: building
last_verified_at: 2026-10-18
---

# Ivy Myst / Ivy Myst Residence (DISC-NBO-032) — discovery research

**New project** — not in seed corpus except thin Block lead. User-provided site + unit/payment/amenity claims; live research accessed **2026-10-18**.

**Project microsite:** https://ivymyst.ke/ (JS shell this pass — title/analytics only; Karim analytics tag)  
**Developer hub (field-rich):** https://www.ivygroup.ke/ivy-myst · https://www.ivygroup.ke/  
**Brochure (Karim-branded PDF):** https://nairobirealty.co.ke/wp-content/uploads/2026/08/Ivy-Myst-Residence-Brochure.pdf

**Block.ke ignored as authority** (low-trust — [block.ke/project/ivy-myst/](https://block.ke/project/ivy-myst/)). **Never** Hauzisha `0730 731 355` as developer phone.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`**.
- Prices: always **`price_claims[]`**.
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented legal SPV.
- Skip Ready — **not** Ready-tagged; groundbreaking done / UC / completion **2029**.

**≠** Spectre Residences (AYA / Westlands Rd); **≠** Ivy Park / Blossoms Ivy / Luckinn Ivy (sibling Ivy Group portfolio — mention only); **≠** AYA Luxury / Whitehorse — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Flag | Sources |
|-------|------|-------|-----:|------|---------|
| `canonical_name` | **CANONICAL** soft | **Ivy Myst Residence** / **Ivy Myst** | 5 | — | ivygroup.ke; brochure; agents |
| `aliases` | secondary | Ivy Myst Kileleshwa; Kenya’s first true wellness residence (marketing) | 4 / 2 | Positioning phrase | User; NRE; Realtors |
| `inventory_class` | **CANONICAL** soft | **`building`** — groundbreaking complete; construction underway / sales open; completion **2029**; **not** Ready | 4 | — | Ivy Group; user; agents Off-plan sales |
| `status` | **CANONICAL** soft | Under construction / early-stage sales after groundbreaking | 4 | — | ivygroup.ke |
| `geography.city` | **CANONICAL** | Nairobi | 5 | — | all |
| `geography.neighbourhood` | **CANONICAL** | **Kileleshwa** | 5 | — | Ivy Group; brochure; agents |
| `geography.street` | **CANONICAL** | **Gatundu Road** / Gatundu Rd, Kileleshwa — “Nairobi's Most Coveted Address” (marketing); agents: opposite Finnlemm Sacco — soft | 5 / 3 / 2 | Finnlemm **needs_verification** | User; Ivy Group; brochure; Realtors |
| `geography.lat_lng` | **CANONICAL** soft (Maps place) | **−1.2774498, 36.7854601** (`geo_method=official`, Google Maps place **IVY MYST RESIDENCE**) | 4 | Building place — promote exact | User short link → Maps 2026-10-18 |
| `geography.lat_lng` (secondary) | geocode | **−1.278297, 36.784821** (`geo_method=geocode`) | 2 | Street approx; demoted when Maps place resolved | Nominatim Gatundu Road Kileleshwa 2026-10-18 |
| `primary_developer_id` | **CANONICAL** (trading) | → **`dev-ivy-group`** (**The Ivy Group**; part of **R-Sun Properties**) — promote from Hauzisha lead | 5 | Legal SPV unknown | ivygroup.ke |
| `conceptualizer` | RelatedParty | **Karim Real Estate** / Karim Exclusives — brochure “Conceptualised by Karim Real Estate”; ivymyst.ke analytics | 5 | **≠ primary developer** | brochure; agents inflate to “developed by Karim” |
| `unit_types` | **CANONICAL** | **1BR**; **2BR**; **3BR + DSQ** (select) | 5 | — | Ivy Group; brochure |
| `size_by_type` | **CANONICAL** | **1BR 78–84 m²**; **2BR 121–159 m²**; **3BR+DSQ 169–231 m²** | 5 | — | Ivy Group; brochure; user **match** |
| `building_specs.storeys` | claim set — **NDI** | Ivy Group **22** floors vs brochure rooftop labels **23rd–25th** vs Realtors **24** floors | 4 / 3 / 2 | **`needs_developer_input`** | ivygroup.ke vs brochure vs Realtors |
| `building_specs.units` | **CANONICAL** soft | **448** residences; **2 wings** A & B | 5 | — | Ivy Group; Realtors |
| `building_specs.parking` | **CANONICAL** soft | Basement parking | 5 | — | Ivy Group |
| `price_claims[]` | multi — floors conflict | See **§1a** | ≤5 | **`needs_developer_input`** on 1BR/3BR floors | Ivy Group vs brochure/agents vs user |
| `currency` | **CANONICAL** | **KES** | 5 | — | all |
| `payment_plan` | detailed = brochure + agents; Ivy Group soft | See **§1b** — user schedule **matches brochure / NRE** | 4 / 3 | Soft vs Ivy Group one-liner | brochure; NRE; Ivy Group |
| `completion_estimate` | **CANONICAL** soft | **August 2029** / year **2029** | 5 / 4 | — | Ivy Group; user year |
| `amenities` | **CANONICAL** | Mezzanine + rooftop lists — user list **confirmed** on brochure; feature map **§1d** | 5 | — | brochure; Ivy Group amenity gallery |
| `positioning` | secondary marketing | “Kenya’s first true wellness residence”; living gardens on balconies; natural light; calming finishes | 3 | Marketing | User; brochure; agents |
| `roi_claim` | secondary marketing | Furnished / unfurnished ROI tables (to ~19.75%) | 2 | **needs_verification** | Ivy Group; brochure |
| `legal_title` | unknown | — | 0 | — | — |
| `master_planned_community` | none | Standalone Gatundu Rd tower (Ivy portfolio peer of Blossoms on same road) | — | — | — |

### 1a. `price_claims[]` — keep **all** (no forced scalar)

**Sizes:** user **78–84 / 121–159 / 169–231 m²** **match** Ivy Group + brochure.

**Starting floors — partial match / conflicts:**

| # | Claim (KES) | Context | Conf | Flag | Sources |
|--:|-------------|---------|-----:|------|---------|
| 1 | **1BR 8.8M–10.5M**; **2BR 14.2M–20.4M**; **3BR+DSQ 19.8M–29.6M**; hero from **8.8M** | Developer hub typed bands | 5 | — | ivygroup.ke/ivy-myst |
| 2 | **1BR 7.9M–10.5M**; **2BR 14.2M–20.4M**; **3BR 19.8M–29.6M**; ROI sample prices **7.9M / 14.242M / 19.898M** | Karim brochure typed + ROI table | 4 | **`needs_developer_input`** vs #1 on 1BR floor | brochure PDF |
| 3 | Same bands as #2; hero from **7.9M** | Agent cards | 3 | Aligns #2 | NRE; Realtors |
| 4 | User: from **8.8M / 14.2M / 19.6M** | User lead | 3 | 1BR/2BR align #1; **3BR 19.6 vs official 19.8** soft | User |

**User vs official:** sizes **match**; 1BR/2BR **from** floors match **Ivy Group** (8.8 / 14.2); 3BR user **19.6M** vs Ivy Group/brochure **19.8M** — soft mismatch. Brochure/agents **7.9M** 1BR floor fights Ivy Group **8.8M** → **`needs_developer_input`**. Portal scalar: **POA** until reconciled.

### 1b. Payment plan

| Element | User / brochure / NRE | Ivy Group page | Conf |
|---------|----------------------|----------------|-----:|
| Deposit | **20%** within **7 days** of offer letter | “Typically a **20%** deposit” | 5 / 3 |
| Quarterly | **10%** every quarter × **5** quarters (50%) | Silent (balance “through construction”) | 4 |
| Completion balance | **30%** on/before completion | Silent | 4 |
| Cash alt | 20% in 7 days + **80%** within 30 days | Soft flexible | 4 |

**User payment schedule matches brochure + Nairobi Realty exactly.** Ivy Group does not publish the 10%×5 / 30% split — does not contradict. Treat detailed plan as **must-have soft-met** (brochure project marketing + multi-agent; developer soft corroborates 20%). Flag tenor detail **`needs_verification`** against live Ivy Group LOO.

### 1c. Map / geo

| Candidate | lat | lng | method | conf | notes |
|-----------|-----|-----|--------|-----:|-------|
| Google Maps place **IVY MYST RESIDENCE** | **−1.2774498** | **36.7854601** | official (`google_maps_place`) | **4** | User short link [maps.app.goo.gl/fszDSCcurNBVF1va9](https://maps.app.goo.gl/fszDSCcurNBVF1va9) → place name **IVY MYST RESIDENCE**; CID `16200090799603607907` (`0xe0d248c01f726963`); **recommended** — promote `properties.lat/lng`, `map_tier=exact` |
| Nominatim `Gatundu Road, Kileleshwa, Nairobi` | −1.278297 | 36.784821 | geocode | 2 | Street approx; **secondary** after Maps place resolve |
| Address claim | — | — | — | 5 / 3 | **Gatundu Rd, Kileleshwa** — “Nairobi's Most Coveted Address” (user marketing) |

### 1d. Amenities — user list × brochure × feature taxonomy

Brochure **MEZZANINE** and **ROOFTOP** lists match user leads. Ivy Group gallery names overlap (Celestial Pool, Fire-Pit Lounge, Indoor Heated Pool, Gym & Yoga, Children’s Play, Co-Working, etc.).

**Mezzanine**

| Label | `feature.slug` | Conf |
|-------|----------------|-----:|
| Courtyard | `green_area` | 5 |
| Indoor Zen Garden | `green_area` (indoor zen / sky garden variant) | 5 |
| Thermal Heated Pool | `swimming_pool` (heated / thermal) | 5 |
| Work Sanctuary | `coworking` | 5 |
| Kids Play Room | `kids_play` | 5 |
| Strength Gym | `gym` | 5 |
| Sauna and Massage Room | `sauna` + `spa` | 5 |

**Rooftop (brochure floor labels 23rd–25th — storeys NDI)**

| Label | Floor (brochure) | `feature.slug` | Conf |
|-------|------------------|----------------|-----:|
| Aqua Sky Bar | 23rd | `restaurant_cafe` (bar variant) | 5 |
| Upper Water Lounge | 24th | `lounge` | 5 |
| Fire-pit Lounge | 24th | `lounge` + `fire_pit` | 5 |
| Celestial Pool | 25th | `swimming_pool` (celestial / infinity variant) | 5 |
| Cardio Gym | 25th | `gym` | 5 |
| Sky Yoga | 25th | `yoga` | 5 |
| Sky Restaurant | 25th | `restaurant_cafe` | 5 |

Also: living garden balconies → `balcony` + `green_area` (apartment/development); grand reception → `reception`.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | **`dev-ivy-group`** (promote `dev-lead-ivy-group-kenya`) |
| `legal_name` / trading | **The Ivy Group** (Hauzisha “Ivy Group Kenya”); legal SPV for Ivy Myst **unknown** |
| `website` | https://www.ivygroup.ke/ |
| `group_company_id` | → **`gc-r-sun-properties`** candidate — ivygroup.ke “part of **R-Sun Properties**” (conf 4); email domain `rsunproperty.net` |
| `evidence` | Self-describes as Nairobi residential developer; portfolio includes Ivy Myst |
| `confidence` | **5** trading |

**Proposal:** Primary = **The Ivy Group** (conf **5**). **Do not** set Karim as primary despite agent/EHS wording.

---

## 3. GroupCompany

| Field | Value |
|-------|-------|
| `id` | **`gc-r-sun-properties`** (new candidate) |
| `name` | R-Sun Properties |
| `evidence` | ivygroup.ke “part of R-Sun Properties”; marketing@`rsunproperty.net` |
| `confidence` | **4** |

---

## 4. RelatedParty

| Name | Type | Conf | Evidence |
|------|------|-----:|----------|
| **Karim Real Estate** / **Karim Exclusives** | **`marketing_partner`** (conceptualizer + brochure sales) | 5 | Brochure “Conceptualised by Karim Real Estate”; footer karimexclusives.com / +254 140 000 700; ivymyst.ke Karim analytics |
| Agent claim “Developed by Karim Exclusives / Built by Karim Real Estate” | conflict | 1–2 | Realtors / NRE — **reject as primary** |

May share brand family with Spectre Karim RP / `stk-karim-cg` — steward **do not auto-merge** without review.

---

## 5. Agents + Contacts

| Party | Role | URL / contact |
|-------|------|----------------|
| The Ivy Group | Developer sales | +254 118 266 666; marketing.ivy-group@rsunproperty.net; Ivy Park suite Kirichwa Rd |
| Karim Exclusives | Brochure / conceptualizer sales | +254 140 000 700; +254 750 070 053; sales@ / info@ karimexclusives.com |
| Nairobi Realty | Agent | https://nairobirealty.co.ke/listing/ivy-myst-residence-kenyas-first-true-wellness-residence/ · +254 700 624 620 |
| Realtors.co.ke | Agent | https://realtors.co.ke/property/ivy-myst-kileleshwa-kenyas-first-wellness-residence/ · +254 791 138 831 |
| Block | Aggregator — **not authority** | https://block.ke/project/ivy-myst/ |

---

## 6. Stakeholders

None named beyond Karim conceptualizer (modeled as RelatedParty) this pass. Architect / contractor unpublished on Ivy Group HTML.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution |
|--:|-------|--------|------------|
| 1 | **1BR starting price** | Ivy Group **8.8M** vs brochure/agents **7.9M** vs user **8.8M** | Multi `price_claims[]`; **`needs_developer_input`** |
| 2 | **3BR starting price** | User **19.6M** vs Ivy Group/brochure **19.8M** | Soft; show both; prefer published official **19.8** band until LOO |
| 3 | **Storeys / amenity floors** | Ivy Group **22** vs brochure **23rd–25th** rooftop labels vs Realtors **24** | **`needs_developer_input`** |
| 4 | **Developer identity** | Ivy Group (+ R-Sun) vs agents “Karim developed” | **Canonical = Ivy Group**; Karim = marketing_partner / conceptualizer |
| 5 | **Payment detail** | Brochure/NRE full schedule vs Ivy Group soft 20% | Show detailed + soft; verify on LOO |
| 6 | **ivymyst.ke** | User official URL but JS-thin this pass | Always retain URL; harvest from Ivy Group + brochure |

---

## 8. Disambiguation

| Other | Why distinct |
|-------|----------------|
| **Spectre Residences** DISC-NBO-031 | AYA Real Estate; Westlands Rd; different scheme (shared Karim sales brand possible) |
| **Ivy Park / Blossoms Ivy / Luckinn Ivy** | Same Ivy Group portfolio; different sites/completions |
| **AYA Luxury Residence** DISC-NBO-023 | Whitehorse; Othaya×Makueni — name “AYA” only coincidence vs AYA RE on Spectre |
| **Lesonia** (Gatundu Rd area) | Different developer |

---

## 9. Sources (retained **7**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~11** |
| `sources_retained` | **7** |

**Always kept:** ivymyst.ke (even thin) + ivygroup.ke/ivy-myst + brochure PDF.

**Thin / skipped:** Block hub; EHS Karim-as-developer blurb; Hauzisha directory card (lead only); social-only stubs.

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://ivymyst.ke/ | Ivy Myst / Karim analytics | project_site | 2026-10-18 | User official; JS shell — always keep |
| 2 | https://www.ivygroup.ke/ivy-myst | The Ivy Group | developer | 2026-10-18 | 22 fl / 448 / Aug 2029 / price bands from 8.8M |
| 3 | https://www.ivygroup.ke/ | The Ivy Group | developer | 2026-10-18 | R-Sun parent; portfolio |
| 4 | https://nairobirealty.co.ke/wp-content/uploads/2026/08/Ivy-Myst-Residence-Brochure.pdf | Karim / project brochure | project_site | 2026-10-18 | Amenities floors; payment 20/10×5/30; prices from 7.9M |
| 5 | https://nairobirealty.co.ke/listing/ivy-myst-residence-kenyas-first-true-wellness-residence/ | Nairobi Realty | agent | 2026-10-18 | Payment detail; mezz/rooftop copy |
| 6 | https://realtors.co.ke/property/ivy-myst-kileleshwa-kenyas-first-wellness-residence/ | Realtors | agent | 2026-10-18 | 24 floors claim; 7.9M; floor plans |
| 7 | https://www.karimexclusives.com | Karim Exclusives | marketing_partner | 2026-10-18 | Brand home (brochure CTA) |

---

## 10. Field harvest

| Field | Status | Notes |
|-------|--------|-------|
| Name / geo / developer | OK | Ivy Group + Gatundu / Kileleshwa |
| Sizes | OK | User match |
| Prices | Multi NDI | User ≈ Ivy Group floors; brochure 7.9M fight |
| Payment | Soft-met | User **matches** brochure/NRE |
| Amenities | OK | User lists confirmed + taxonomy |
| Completion | OK | Aug / 2029 |
| Storeys | NDI | 22 vs 23–25 labels vs 24 |
| Map | OK exact | Maps place IVY MYST RESIDENCE (user short link) |

---

## Steward notes

- Promote `dev-lead-ivy-group-kenya` → `dev-ivy-group`; add `gc-r-sun-properties`.
- Karim = `marketing_partner` (conceptualizer); do not merge blindly with Spectre Karim RP.
- Prefer ivygroup.ke + brochure media over agent rehosts.
- `geo_pin` Maps place **IVY MYST RESIDENCE** conf **4** exact (user short link); Nominatim Gatundu Rd conf 2 secondary.
- Public hero **POA** until 7.9 vs 8.8 and 19.6 vs 19.8 reconciled.
