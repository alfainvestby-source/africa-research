---
slug: golfscape-residences
external_id: NBO-006
wave: C
cycle: scale-half
pilot: false
sources_evaluated: 15
sources_retained: 11
last_verified_at: 2026-10-16
---

# Golfscape Residences (NBO-006) — Wave C

CSV seed (unverified leads): location Muchai Drive, off Ngong Road, Nairobi; lat/lng blank; stage `off_plan`; completion Q3 2027; `price_from_kes` 4,600,000; sales_contact Loyd Mokaya (Block Real Estate); **developer blank**.

Live research: official project site golfscape.co.ke (home price list + amenities + progress + about + contact) + portals/agents. Accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages / widgets disagree): **do not assume** → **`needs_developer_input`**.
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 agent sources. Agent-only / uncorroborated → **`needs_verification`**.
- Amenities: **feature-aware** — developer core mapped to taxonomy scopes (`development` / `apartment`); agent inflation shown + **`needs_verification`**.
- CSV = unverified leads only. CSV sales_contact ≠ developer.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Golfscape Residences | 5 | golfscape.co.ke; about; Hauzisha |
| `aliases` | secondary | Golfscape Residence; Golfscape; Golfspace Residences (KCB typo); Goldscape (BuyRent project card typo) | 3 | agents; KCB; BuyRent |
| `status` | claim set | CSV/`off_plan`; site progress **Finishing (85%)**; Sep 2025 posts “7th Floor”; Highpoint portfolio card “Completed (2024–2026)” vs ongoing sales — **conflict** | 3 | golfscape progress widget; progress posts; Highpoint site; CSV |
| `geography.city` | **CANONICAL** | Nairobi | 5 | golfscape.co.ke |
| `geography.neighbourhood_street` | **CANONICAL** | **Muchai Road** off **Muchai Drive / Ngong Road**; Kilimani–Upper Hill junction; marketing adjacent to **Royal Nairobi Golf Club** | 5 | golfscape about/home (+ agents agree Muchai / Ngong) |
| `geography.lat_lng` | developer-linked map | **−1.3004784, 36.8009648** (Google Maps place linked from golfscape.co.ke) | 4 | golfscape.co.ke Maps CTA |
| `primary_developer_id` | **CANONICAL** | → `dev-wh-harmony-investment` | 5 | golfscape.co.ke/about; Hauzisha; LinkedIn company |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom; 3 Bedroom; Penthouses (typed A16P* / B16P* / Block 3 penthouse on official list) | 5 | golfscape home price list + unit nav |
| `unit_types` | secondary | Agents style penthouses as **4 Bedroom + DSQ duplex** — not labelled “4BR” on official price table (says “Penthouse”) | 3 | CPK/BuyRent WH Harmony; Sir Francis; Vorsa |
| `size_by_type` | **CANONICAL** (official list Sep 3 2025) | See §1b — Blocks 1&2 types A–E + penthouses; Block 3 1/2/3BR + penthouse | 5 | golfscape.co.ke price tables |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** | 0 | — |
| `building_specs.blocks` | **CANONICAL** (presence) | Official price list: **Block 1 & 2** + **Block 3** → **3 blocks** | 5 | golfscape.co.ke |
| `building_specs.storeys` | secondary — **needs_verification** | KCB / BuyRent WH Harmony: **17 floors**; penthouse codes **A16P*** imply floor-16 penthouses — not stated on golfscape pages fetched | 2 | KCB; BuyRent listing |
| `building_specs.units_per_floor` | secondary — **needs_verification** | **5 units per floor** (low density) | 2 | KCB; BuyRent; Capital Click |
| `building_specs.parking` | secondary — **needs_verification** | Ground + first floor + basement (KCB/BuyRent) | 2 | KCB; BuyRent |
| `total_units` | unknown | Not published on official pages fetched | 0 | — |
| `price_claims[]` | claim set — **`needs_developer_input`** on entry “from”; **keep all options** | See §1a | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | official list disclaimer |
| `payment_plan` | unknown on developer pages | FAQ meta mentions payment plans; **no % / schedule on fetched official HTML** | 0 | golfscape FAQ shell |
| `payment_plan.deposit` | secondary — **needs_verification** (agent <4 independent) | **20% deposit** + balance monthly/quarterly to completion (and/or cash balance in 2 weeks) | 2–3 | Oaklane; BuyRent WH Harmony; Capital Click |
| `payment_plan.term` | secondary — **needs_verification** | Vorsa: **24-month** instalments | 2 | Vorsa |
| `completion_estimate` | claim set — **`needs_developer_input`** | Official widgets disagree: home progress **Jun 2027** vs progress-page countdown **Feb 23, 2026** vs indexed/historical **Dec 2026**; agents Apr / Jun / Jul 2027; Hauzisha Dec 2026; CSV Q3 2027 | ≤2 | golfscape home; progress; agents; CSV |
| `amenities` (core — developer) | **CANONICAL** + feature slugs | See §1c | 5 | golfscape.co.ke amenities sections |
| `amenities` / features inflated | secondary — **needs_verification** | **Heated** pool; rooftop lounge / rooftop coffee house; mini-mart; clubhouse (Vorsa chips); “golf course views” as amenity claim | ≤2 | Vorsa; Capital Click; BuyRent; Hauzisha; Sir Francis |
| `construction_progress` | claim set — **`needs_developer_input`** / conflict | Home: **Finishing (85%)**, start **Jan 2025**, target **Jun 2027**. Progress page: interior finishes + Sep 2025 posts “**currently on the 7th Floor**” + countdown **Feb 23, 2026**. Do **not** average. | 3 | golfscape home; progress |
| `availability_claim` | secondary — **needs_verification** | Hauzisha “**3 units**”; site “show houses” / open day Oct 2025; BuyRent “show houses ready” | 2 | Hauzisha; BuyRent; site |
| `legal_title` | unknown | — | 0 | not found |
| `plot_size` | unknown | — | 0 | not found |
| `schema_metadata_conflict` | flag | Site JSON-LD Organization still names **“Royal Country Garden”** / alternate **“Capital Rise Apartments Kilimani”** while visible copy = Golfscape / WH Harmony — treat as **stale site metadata**, not a GroupCompany | 1 | golfscape.co.ke JSON-LD |

### 1a. Price claims — keep **all** options (no canonical scalar)

Hero marketing **from KES 4.65M** vs official list lowest typed price **KES 5,600,000** (Type E) → **`needs_developer_input`**.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Official hero / marketing “starting from” | **KES 4.65M** | golfscape.co.ke home | Official — **`needs_developer_input`** vs B |
| B | Official price list (effective **3 Sep 2025**) | Typed list §1b; **lowest 1BR Type E = 5,600,000**; penthouses 26.5–31M | golfscape.co.ke | Official typed — **`needs_developer_input`** vs A on entry “from” |
| C | Oaklane (mirrors official list bands) | 1BR from **5.6M** … penthouses **26.5 / 28 / 31M**; completion Dec 2026 | oaklaneproperties.co.ke | Agent |
| D | Vorsa | 1BR **46.15 from 4.6M**; other types align closer to list; completion Jul 2027; 24 mo | vorsagroup.co.ke | Agent — entry undercuts official list |
| E | Sir Francis discounted vs “original” | Discounted 1BR Type E from **4.46–4.73M** (original ~5.32–5.41M); penthouses discounted ~25.46–28.20M | sirfrancismarketingltd.co.ke | Agent — discount ladder |
| F | KCB “Golfspace” card | 1BR 46 from **4.95M**; other bands; Apr 2027; 17 floors / 3 blocks | ke.kcbgroup.com | Bank portal / agent-style — typo name |
| G | BuyRentKenya (WH Harmony International listings) | e.g. 1BR from **4.95M**; 4BR duplex ph 221 **26.52M** / 235 **28.2M**; Apr 2027 | buyrentkenya.com | Agent (developer-as-agent profile) |
| H | Hauzisha card | **KES 4.9M – 28.2M**; Dec 2026; 3 units | hauzisha.co.ke | Portal |
| I | Capital Click (LinkedIn) | From **4.95M**; Jun 2027; 20% deposit | LinkedIn post | Agent social |
| J | CSV seed | `price_from_kes` **4,600,000** | seed | Unverified lead |
| K | Habitat Realtors BuyRent card | Odd headline prices (e.g. 7.255M / 30.756M “coming soon”) | buyrentkenya.com Habitat | Thin / anomalous — **needs_verification** |

**Canonical price:** none.

### 1b. Official size × price table (claim B — developer list)

**Block 1 & 2**

| Type | Description | Area (sqm) | Price (KES) |
|------|-------------|----------:|------------:|
| A | 1-Bedroom | 57.56 | 7,500,000 |
| B | 1-Bedroom | 69.54 | 9,100,000 |
| C | 1-Bedroom | 64.55 | 7,500,000 |
| D | 1-Bedroom | 57.91 | 6,900,000 |
| E | 1-Bedroom | 46.1 | 5,600,000 |
| A16P1 | Penthouse | 234.26 | 28,000,000 |
| A16P2 | Penthouse | 221.31 | 26,500,000 |
| B16P1 | Penthouse | 221.31 | 26,500,000 |
| B16P2 | Penthouse | 234.26 | 26,500,000 |

**Block 3**

| Description | Area (sqm) | Price (KES) |
|-------------|----------:|------------:|
| 3 Bedroom | 114 | 13,500,000 |
| 2 Bedroom | 102.88 | 13,500,000 |
| 2 Bedroom | 102.14 | 12,500,000 |
| 1 Bedroom | 57.67 | 6,900,000 |
| 2 Bedroom | 88.64 | 10,500,000 |
| 3 Bedroom | 114 | 13,500,000 |
| 2 Bedroom | 80.65 | 10,500,000 |
| 2 Bedroom | 79.05 | 10,300,000 |
| Penthouse | 258.79 | 31,000,000 |

### 1c. Amenities / features (feature-aware)

**Development-scope core (canonical — golfscape.co.ke):**

| Taxonomy slug (proposed) | Source wording |
|--------------------------|----------------|
| `swimming_pool` | Swimming pool |
| `gym` | A well-equipped gym |
| `green_area` | Landscaped gardens |
| `kids_play` | Children's play area |
| `restaurant_cafe` | Coffee Bar Restaurant |
| `internet_cable` | Fibre Internet and Intercom |
| `high_speed_lifts` | High-speed lifts |
| `backup_generator` | Full power backup generator |
| `borehole` | Borehole |
| `water_storage` | Water storage tanks |
| `gated_security` | 24/7 manned security |
| `cctv` | CCTV |
| `access_control` | Biometric access |
| `changing_rooms` | Male and female changing rooms |
| `conference_room` (soft) | Multipurpose hall for meetings / birthday parties |
| `reception` / management | Management office on-site |
| — | Recreational Area (generic — keep free-text) |

**Apartment-scope (secondary / agent + typology):**

| Slug | Note |
|------|------|
| `balcony` | Agent + Sir Francis / Oaklane living-copy |
| `dsq` | Agent 4BR penthouse + DSQ (BuyRent / Sir Francis) — **needs_verification** vs official “Penthouse” label |
| `ensuite` | BuyRent “all ensuite” penthouses |
| `floor-to-ceiling windows` / high ceilings | Hauzisha unit chips |
| `built-in wardrobes` | Hauzisha |

**Reject as canonical:** heated pool, rooftop lounge, mini-mart, clubhouse — agent/portal adds not on official amenity list fetched.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold? | Status |
|---------|------------------------------|------:|------------|--------|
| Developer % schedule / LOO | Not on fetched golfscape pages (FAQ is JS shell) | 0 | — | unknown |
| **20% deposit** | Oaklane; BuyRent WH Harmony listing; Capital Click | **3** | Need ≥4 **or** developer | **Not met** — show secondary + **`needs_verification`** |
| 24-month instalments | Vorsa | 1 | — | Soft secondary |
| Flexible monthly/quarterly to completion | Oaklane; BuyRent | 2 | — | Soft secondary |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-wh-harmony-investment` |
| `legal_name` | WH Harmony Investment Co. Ltd (as styled on golfscape about + Hauzisha) |
| `trading_names` | WH Harmony; WH Harmony International Investment Company Limited (BuyRent agent profile — **needs_verification** as same legal entity) |
| `website` | Project: https://golfscape.co.ke/ — no standalone corporate WH Harmony site found this pass |
| `evidence` | about page: “brought to life by WH Harmony Investment Co. Ltd”; Hauzisha attribution; LinkedIn Golfscape company “premier development by WH Harmony” |
| `group_company_id` | **null** — do **not** invent from stale JSON-LD “Royal Country Garden” / “Capital Rise” |
| `csv_name_note` | CSV developer **blank** |
| `prior_projects_mentioned` | About: **Highpoint 336**. BuyRent WH Harmony copy lists Chelezo, Urban Park, Riziki, Cherrywood, Mpuuga Gardens, Villa Lavender, Kingstone — **delivery unverified** (`needs_verification`) |

**Primary developer = WH Harmony Investment Co. Ltd (confidence 5).**

---

## 3. GroupCompany

**None.** JSON-LD “Royal Country Garden” / “Capital Rise Apartments Kilimani” treated as **stale WordPress/schema leftover**, not evidenced parent.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Conf |
|------|-------------------|----------|-----:|
| **Highpoint Residences LTD** / Highpoint 336 brand | `marketing_partner` (unproven legal identity vs WH Harmony) | golfscape about: WH Harmony developing Highpoint 336; highpointresidencesltd.com portfolio lists **Golfscape Residences** (“Completed 2024–2026”); LinkedIn “WH Harmony (Highpoint Developers)” | 3 |

Do **not** set as GroupCompany until registry/parent evidence exists.

---

## 5. Agents + Contacts

### Agents / portals

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate | agency | CSV sales_contact; **no dedicated Golfscape listing URL found this pass** | CSV only |
| VorsaGroup Real Estate | agency | Price table; 24 mo; Jul 2027; from 4.6M | https://vorsagroup.co.ke/property/golfscape-residences-1-2-3-4-bedroom-apartments-off-ngong-road-2/ |
| Oaklane Properties | agency | Mirrors official list; **20%** deposit; Dec 2026 | https://oaklaneproperties.co.ke/properties/golfscape-residence-kilimani/ |
| Sir Francis Homes | agency | Discounted vs original ladder; from 4.46M | https://sirfrancismarketingltd.co.ke/properties/golfscape-residences-kilimani/ |
| Hauzisha | portal | WH Harmony; Dec 2026; 3 units | https://hauzisha.co.ke/developments/golfscape-residences/ |
| KCB properties hub | bank portal | “Golfspace”; 17 floors / 3 blocks; Apr 2027 | https://ke.kcbgroup.com/properties/golfspace-residences |
| WH Harmony via BuyRentKenya | developer-as-lister | Dense overview + **20%** plan; Apr 2027 | https://www.buyrentkenya.com/listings/4-bedroom-apartment-for-sale-kilimani-10003719 (+ sibling unit cards) |
| Capital Click Properties | agency | LinkedIn: 20%; Jun 2027; 5/floor | LinkedIn post 2026-09-02 |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 788 357 336 | Property sales (golfscape.co.ke) |
| phone | +254 115 666 777 | Property sales (site alternate / Office Line) |
| phone | +254 714 668 888 | Property sales (Office Line 2 on home) |
| email | info@golfscape.co.ke | Property |
| url | https://golfscape.co.ke/ | Property |
| address | Muchai Road off Muchai Drive / Ngong Road, Nairobi | Property |
| phone | +254 725 937 686 | Agent: Block / Loyd (CSV) |
| email | sales@block.ke | Agent: Block (CSV) |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: Vorsa |
| email | info@vorsagroup.co.ke | Agent: Vorsa |
| phone | +254 785 855 855 / +254 752 035 655 | Agent: Oaklane |
| email | oaklanepropertieske@gmail.com | Agent: Oaklane |
| phone | +254 722 720 812 | Agent: Sir Francis |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 730 731 355 | Portal: Hauzisha |
| phone | +254 798 471 848 | KCB property inquiry line (portal) |

---

## 6. Stakeholders

None named (contractor / architect / financier) on materials fetched this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Entry price “from”** | Hero **4.65M** vs official list lowest **5.6M** (Type E) vs agents 4.46–4.95M | **Official vs official** on 4.65 vs 5.6 → **`needs_developer_input`**. Keep all `price_claims[]`. |
| 2 | **Completion** | Home widget **Jun 2027** vs progress countdown **Feb 23, 2026** vs indexed Dec 2026 vs agents Apr/Jun/Jul 2027 vs CSV Q3 2027 | **Official vs official** → **`needs_developer_input`**. No canonical. |
| 3 | **Construction progress** | **85% finishing** vs Sep 2025 “**7th floor**” posts | Retain claim set; do not reconcile without developer input. |
| 4 | **Status complete vs selling** | Highpoint portfolio “Completed (2024–2026)” vs live off-plan/finishing marketing | Flag; Highpoint claim **`needs_verification`**. |
| 5 | **Storeys / density** | Agent/KCB **17 floors / 5 per floor** vs silent official pages | Secondary + **`needs_verification`**. |
| 6 | **Penthouse typology** | Official “Penthouse” vs agents **4BR + DSQ duplex** | Show agent label + **`needs_verification`**. |
| 7 | **Payment deposit %** | Agents 20% (3 sources); developer silent | Not threshold-met; secondary NV. |
| 8 | **Schema brand leftovers** | JSON-LD Royal Country Garden / Capital Rise vs WH Harmony / Golfscape | Not GroupCompany; metadata conflict flag. |
| 9 | **CSV developer blank / Block contact** | ≠ WH Harmony / golfscape phones | Split Contact.owner. |
| 10 | **Amenities inflation** | Heated pool / rooftop / mini-mart vs official list | Core = official; extras NV. |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~15** |
| `sources_retained` | **11** |

**Selection note:** Scanned golfscape home, about, progress, FAQ, contact, photos; Hauzisha; Vorsa; Oaklane; Sir Francis; KCB; BuyRent WH Harmony; Capital Click LinkedIn; Highpoint portfolio; Block (missing listing); Habitat BuyRent thin; CSV. **Always kept** developer site. Retained 11 richest (≥5 rule).

**Thin / skipped:**
- https://golfscape.co.ke/golfscape-residences-faq/ — JS Q&A shell (meta only); not field-dense
- https://golfscape.co.ke/golfscape-residences-photos/ — gallery; low structured fields
- Habitat BuyRent “coming soon” card — anomalous prices
- Block.ke — no dedicated Golfscape URL recovered
- CSV NBO-006 — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://golfscape.co.ke/ | Golfscape / WH Harmony | project_site | 2026-10-16 | Price list Sep 2025; amenities; progress **85% / Jun 2027**; from **4.65M** hero; GPS Maps link — **always keep** |
| 2 | https://golfscape.co.ke/about-golfscape-residences/ | Golfscape | project_site | 2026-10-16 | **WH Harmony Investment Co. Ltd**; Highpoint 336 |
| 3 | https://golfscape.co.ke/golfscape-residences-progress/ | Golfscape | project_site | 2026-10-16 | Feb 23 2026 countdown; 7th-floor posts Sep 2025 |
| 4 | https://golfscape.co.ke/contact-page/ | Golfscape | project_site | 2026-10-16 | +254 788 357 336; info@golfscape.co.ke |
| 5 | https://hauzisha.co.ke/developments/golfscape-residences/ | Hauzisha | portal | 2026-10-16 | WH Harmony; Dec 2026; 3 units |
| 6 | https://vorsagroup.co.ke/property/golfscape-residences-1-2-3-4-bedroom-apartments-off-ngong-road-2/ | VorsaGroup | agent | 2026-10-16 | From 4.6M; 24 mo; Jul 2027 |
| 7 | https://oaklaneproperties.co.ke/properties/golfscape-residence-kilimani/ | Oaklane | agent | 2026-10-16 | Mirrors list; **20%** deposit |
| 8 | https://sirfrancismarketingltd.co.ke/properties/golfscape-residences-kilimani/ | Sir Francis | agent | 2026-10-16 | Discount ladder from **4.46M** |
| 9 | https://ke.kcbgroup.com/properties/golfspace-residences | KCB | portal | 2026-10-16 | 17 floors; 3 blocks; Apr 2027; typo “Golfspace” |
| 10 | https://www.buyrentkenya.com/listings/4-bedroom-apartment-for-sale-kilimani-10003719 | WH Harmony via BuyRent | agent | 2026-10-16 | 20% plan; 17 floors; prior-project list |
| 11 | https://www.highpointresidencesltd.com/projects/highpoint-366-residence | Highpoint Residences LTD | related_party | 2026-10-16 | Portfolio lists Golfscape; RelatedParty evidence |

**Also cited:** Capital Click LinkedIn (20% / Jun 2027); golfscape JSON-LD schema conflict (Royal Country Garden / Capital Rise).

---

## 9. Field harvest → must-have / taxonomy notes

| Field | Golfscape status | Harvest note |
|-------|------------------|--------------|
| canonical_name / aliases | OK | Watch Golfspace/Goldscape typos |
| status | Claim set | 85% finishing vs 7th-floor posts vs Highpoint “completed” |
| geography + developer Maps GPS | OK | Promote Maps-linked lat/lng when on official CTA |
| primary_developer | OK | CSV blank → WH Harmony Investment Co. Ltd |
| RelatedParty Highpoint | Captured | `marketing_partner` until registry |
| `unit_types` + official typed sizes | OK | Dense Sep 2025 list |
| `block_count` | **3** on official list | Reinforces block_count claim-set proposal |
| `storeys` / units_per_floor | Agent/KCB only | Keep claim set |
| `price_claims[]` | A–K retained | Official **4.65M vs 5.6M** → **`needs_developer_input`** |
| `payment_plan` | Not threshold-met | 20% only **3** agent sources; developer silent |
| `completion_estimate` | **`needs_developer_input`** | Jun 2027 vs Feb 2026 vs Dec 2026 |
| `construction_progress` | Claim set retained | Widget vs diary posts |
| amenities / **feature taxonomy** | Core mapped (§1c) | Heated/rooftop/mini-mart = NV |
| Stale schema brands | Flag only | Do not invent GroupCompany |

**Consensus bump suggestions:**
- Official hero “from” vs typed price-list lowest → same **`needs_developer_input`** pattern as Diamond Bay / Galaxy
- Developer construction **progress widget + diary** without agreeing completion → progress + completion both claim sets
- Feature-aware amenities: map developer bullets to `development` slugs; keep agent “heated” / rooftop as NV apartment/development extras
- Site JSON-LD brand leftovers → harvest “schema_stale_entity” QA flag for DB steward

---

## Open questions (developer input)

1. Reconcile marketing **from KES 4.65M** with official list lowest **KES 5.6M** (and agent discount ladders).
2. Which completion is binding: **Jun 2027**, **Feb 23 2026**, or **Dec 2026**?
3. Reconcile **85% finishing** with Sep 2025 “**7th floor**” progress posts.
4. Publish storeys / units-per-floor / total units on golfscape.co.ke?
5. Binding payment schedule (deposit %)?
6. Are penthouses officially **4BR + DSQ duplexes**?
7. Legal identity: WH Harmony Investment Co. Ltd vs WH Harmony International vs Highpoint Residences LTD?
8. Clean JSON-LD Organization (remove Royal Country Garden / Capital Rise leftovers)?
