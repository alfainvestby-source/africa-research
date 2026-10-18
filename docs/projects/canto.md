---
slug: canto
external_id: DISC-NBO-001
wave: discovery
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# CANTO (DISC-NBO-001) — discovery research

**Not in seed CSV.** Discovery lead from [kenya-offplan-leads.md](../discovery/kenya-offplan-leads.md) (priority batch **#1**): Westlands (near Sarit), **VAAL Real Estate**, under construction, completion **Apr 2028**.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume** → **`needs_developer_input`**.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agent sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**.
- Unproven parent brand → not invented GroupCompany.
- Catalogue PDF on agent CDN treated as **developer-attributed** only where copy/plans align with VAAL pages — not conf 5.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner. **`needs_verification`** = low-conf / agent-only / uncorroborated.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **CANTO** / CANTO Westlands | 5 | vaal.co.ke/canto/; launch article |
| `aliases` | secondary | Canto Westlands; Canto Apartments; CANTO Westlands \| Studio / 1 Bedroom | 4 | agents; VAAL unit cards |
| `status` | claim set | Launch: **construction already underway**; homepage inventory **59% Sold Out**; agents off-plan / selling | 5 / 3 | launch; vaal.co.ke home; agents |
| `geography.city` | **CANONICAL** | Nairobi | 5 | VAAL; all agents |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** | 5 | VAAL; agents |
| `geography.street` | **CANONICAL** (street) / secondary (number) | **School Lane**; near / steps from **Sarit Centre**. CPK: **34 School Lane** | 5 / 3 | VAAL studio/1BR pages + launch; CPK number |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.257683, 36.794544** (`geo_method=geocode`) | 3 | Nominatim 34 School Lane Westlands 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-vaal-real-estate` (VAAL Real Estate) | 5 | vaal.co.ke; launch |
| `unit_types` | **CANONICAL** | **Studio** and **1 Bedroom** | 5 | canto page; launch; unit cards; agents agree |
| `size_by_type` | secondary — developer-attributed catalogue (agent CDN) | See size table — **gross vs net** tagged | 4 | Vorsa-hosted catalogue (copy aligns with VAAL) |
| `size_by_type` | secondary agent summaries | Studios **36–39 sqm**; 1BR **56–57 sqm** (some quote single 38 / 56) | 3 | CPK; Vorsa; Austine; KF snippet |
| `building_specs.storeys` | **CANONICAL** | **25**-floor tower | 5 | launch article; agents + catalogue echo |
| `building_specs.units_per_floor` | secondary consensus | **11** units/floor (**4** studio + **7** 1BR) | 3 | GNA; CPK; Vorsa; KF snippet |
| `total_units` | secondary — **`needs_verification`** | **275** (single LinkedIn promo) | 1 | Tessa Thiga LinkedIn only |
| `price_claims[]` | multi — developer “from” + agent bands | See **§1a** | 5 / ≤3 | VAAL + agents |
| `currency` | **CANONICAL** | **USD** on VAAL cards; agents also quote **KES** | 5 | VAAL; agents |
| `payment_plan.deposit` | secondary — **below ≥4** | Agent cluster **30% deposit** then instalments | ≤3 | Austine; KF snippet; LinkedIn — **not** must-have yet |
| `payment_plan.tenor` | secondary — **`needs_verification`** | **Up to 36 months** / **3 years** vs KF “Cash upfront to **27 months**” | 2 | Vorsa; Austine; KF — conflict |
| `payment_plan.cash` | secondary | Cash upfront option | 3 | Vorsa; KF snippet |
| `completion_estimate` | **CANONICAL** | **April 2028** | 5 | VAAL launch article |
| `completion_estimate` | secondary | **Q4 2028** / **December 2028** | 3 | GNA; Austine; LinkedIn |
| `amenities` (core) | **CANONICAL** (launch + canto page agree on lifestyle set) | Heated infinity pool; rooftop gym; mini golf lounge; coffee bar; indoor cinema; co-working; BBQ terrace / sky lounge; rooftops + lounges framing | 5 | launch; canto page |
| `amenities` | secondary denser lists | 1st floor: lounge, prayer room, management office, co-working, game room, cinema, outdoor seating, mini basketball; rooftop: his/hers steam & sauna, washrooms; **5 levels parking** | 3 | GNA; CPK; catalogue; KF snippet |
| `amenities` inflated — **`needs_verification`** | secondary | Vorsa feature chips: club house, kids play, retail centre, “open chicken” — not on VAAL launch list | 1 | Vorsa chips |
| `roi_claim` | secondary marketing | Expected ROI **22–25%** | 3 | launch; CPK; catalogue; agents |
| `service_charge` | secondary — **`needs_verification`** | One-off **KES 32,000 per sqm** (KF snippet) | 1 | Knight Frank indexed copy only |
| `availability_claim` | secondary | VAAL home: **59% Sold Out** | 3 | vaal.co.ke homepage |
| `legal_title` | unknown | — | 0 | not found |
| `construction_progress` | soft | “Construction already underway” (no % tracker found) | 4 | launch |

### Size table (catalogue — agent CDN; gross / net)

Hosted at Vorsa uploads; unit blurbs match VAAL canto page. Treat as **developer-attributed**, conf **4** (not on vaal.co.ke domain).

| Type | Gross sqm | Net sqm | Role |
|------|----------:|--------:|------|
| Type B Studio | **36** | **29.76** | Catalogue |
| Type H / I Studio | **39** | **32.05 / 32** | Catalogue |
| Type J Studio | **38** | **31.33** | Catalogue |
| Type A / E / F / K 1BR | **57** | **46.15** | Catalogue |
| Type C / D 1BR | **56** | **45.88 / 45.89** | Catalogue |
| Type G 1BR | **56** | **45.44** | Catalogue |

Do not mix gross and net in one portal field.

### 1a. `price_claims[]` — keep **all** options (no canonical scalar collapse)

Developer publishes USD “from” figures that **agree** across canto hub + unit cards → those rows can be treated as **developer-backed options** (still keep agent bands; no single portal `price_from`).

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Studio from **USD 49,000** | Hub + studio product card | vaal.co.ke/canto/; studio apartment URL | 5 | Developer |
| B | 1BR from **USD 68,000** | Hub + 1BR product card | vaal.co.ke/canto/; 1BR apartment URL | 5 | Developer |
| C | Studio from **USD 49,590** (KES **~6.39–6.41M**); 1BR from **USD 68,040** (KES **~8.77M**) | Typed agent table | CPK | 3 | Near developer; FX conversion |
| D | Studio **USD 49,590–60,000** (from KES **6.41M**); 1BR **USD 69,225–87,000** (from KES **8.95M**) | Range bands | GNA | 3 | Upper band above developer |
| E | Studio from **USD 50,000**; 1BR from **USD 70,000**; card **KES 6.45M** | Early-bird framing | Vorsa | 3 | |
| F | Studio from **USD 60,000**; 1BR from **USD 87,000**; card **KES 6.41M** | Promo | Austine; LinkedIn Tessa | 2 | **`needs_verification`** — higher “from” vs developer 49k/68k |
| G | Studio from **USD 55,000**; 1BR from **USD 70,000** | Indexed listing | Knight Frank hub2696809 (search snippet; live shell thin) | 2 | **`needs_verification`** |

**Canonical price scalar:** none for portal. Developer **A/B** are the official “from” options when a developer-backed band is needed.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| Flexible / cash + instalment **exists** | Vorsa; CPK (“flexible… discounts”); KF cash option | ≥2 agents | Soft only — **no developer % schedule** | Soft secondary |
| **30% deposit** | Austine; KF snippet; LinkedIn Tessa | **3** | **Not met** (<4; no developer %) | Show + **`needs_verification`** |
| Tenor **36 months / 3 years** | Austine; Vorsa; LinkedIn | 3 | Soft | Secondary |
| Tenor **to 27 months** | KF snippet only | 1 | — | Conflicts with 36-mo cluster → **`needs_verification`** |
| Developer LOO / FAQ deposit % | Not on canto / launch / unit pages this pass | 0 | — | unknown |

**Must-have deposit %:** **not locked** this pass.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-vaal-real-estate` |
| `legal_name` | **VAAL Real Estate** (Kenya trading on vaal.co.ke). Global footer lead: **VAAL Real Estate Limited** (vaal.africa — HTTP **403** this pass; name from search/cached copy only) |
| `trading_names` | VAAL; VAAL Kenya; VAAL Real Estate |
| `website` | https://vaal.co.ke/ |
| `evidence` | Project + launch + unit cards on vaal.co.ke; About: international developer; prior Kenya deliveries cited (Elite Residence, Moon Valley) |
| `group_company_id` | **null — none invented** (VAAL Group branding on global site not proven as registered parent of Kenya SPV this pass) |
| `leadership_named` | Launch quotes **Ashraf Hamam**, CEO of VAAL Real Estate. About page also cites CEO **Majeed Saad** (older copy) — leadership naming **claim set / soft** |
| `sales_office` | Keystone Park, **95 Riverside Drive**, P.O. Box 20227-00100 Nairobi; **+254 725 111 444**; info@vaal.co.ke |

**Primary developer = VAAL Real Estate (confidence 5 for trading brand on project materials).** Exact Kenya company-register string for the CANTO SPV **unknown** this pass.

---

## 3. GroupCompany

**None set.** Do not invent a parent from “VAAL Group” marketing without register/evidence linking to this SPV.

---

## 4. RelatedParty

None evidenced beyond VAAL’s own letting/management claims (in-house, not a separate related brand like Laureland).

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role notes | Evidence URL |
|-------|------|------------|--------------|
| GNA Real Estate | agency | Dense amenities + typology + price ranges | https://gna.co.ke/project/canto-westlands-luxurious-studios-and-1-bedrooms/ |
| CPK Real Estate (Commercial Property Kenya) | agency | 34 School Lane; typed prices; amenity floors | https://commercialpropertykenya.com/properties/canto-westlands-apartments/ |
| Vorsa Group | agency | Prices; 3-yr instalments; hosts catalogue PDF | https://vorsagroup.co.ke/property/canto-apartments-studio-1-bedroom-in-westlands/ |
| Austine Realtors | agency | 30% / 36 mo; higher USD “from”; Dec 2028 | https://austinerealtors.co.ke/property/canto-westlands-studio-apartments/ |
| Knight Frank | agency network | Indexed hub2696809 — payment + sizes + service charge | https://www.knightfrank.co.uk/properties/residential/for-sale/westlands-school-lane/hub2696809 |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 725 111 444 | Developer VAAL |
| email | info@vaal.co.ke | Developer VAAL |
| office | Keystone Park, 95 Riverside Drive, Nairobi | Developer VAAL |
| phone / WhatsApp | +254 712 406 060 / +254 782 406 060 | GNA |
| email | support@gna.co.ke | GNA |
| phone | 078 444 8888 (+254 784 448 888) | CPK / Kenneth Ikiara |
| phone / WhatsApp | +254 717 945 199 / +254 755 745 140 | Vorsa |
| email | info@vorsagroup.co.ke | Vorsa |
| phone / WhatsApp | +254 704 350 354 | Austine Realtors |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| — | — | No named contractor / architect / financier on VAAL pages this pass | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Conflict | Resolution |
|---|-------|----------|------------|
| 1 | **Completion** | VAAL launch **April 2028** vs agents **Q4 / Dec 2028** | **Canonical = April 2028** (developer). Agent dates secondary. |
| 2 | **Prices** | Developer studio/1BR **49k / 68k USD** vs agent “from” **55–60k / 70–87k** and KES conversions | Keep **all** `price_claims[]`. Developer A/B = official options. Higher agent “from” → **`needs_verification`**. |
| 3 | **Payment tenor** | 36 months / 3 years (multi-agent) vs KF **27 months** | Claim set; **`needs_verification`**. No developer calendar. |
| 4 | **Deposit %** | 30% on 3 agent/snippet sources; developer silent | Show + **`needs_verification`**; **must-have not met**. |
| 5 | **Street number** | “School Lane” (developer) vs **34 School Lane** (CPK) | Neighbourhood/street canonical; number secondary. |
| 6 | **Total units 275** | LinkedIn only | **`needs_verification`**. |
| 7 | **Service charge KES 32k/sqm** | KF only | **`needs_verification`**. |
| 8 | **CEO naming** | Ashraf Hamam (launch) vs Majeed Saad (About) | Soft claim set — not project fact. |

No **official-vs-official** price or typology conflict on VAAL pages this pass (hub + unit cards agree on 49k/68k and studio+1BR). **`needs_developer_input`** not applied to those fields.

---

## 8. Sources

| Meta | Value |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

### Retained

| # | URL | Publisher | Type | Accessed | Why kept |
|--:|-----|-----------|------|----------|----------|
| 1 | https://vaal.co.ke/canto/ | VAAL Real Estate | project_site | 2026-10-16 | Official hub — name, typology, USD from, amenities framing |
| 2 | https://vaal.co.ke/vaal-real-estate-launches-canto-westlands-its-8th-landmark-project-in-nairobi/ | VAAL Real Estate | developer | 2026-10-16 | Launch — 25 floors, Apr 2028, UC, amenities, CEO quote |
| 3 | https://vaal.co.ke/apartments/canto-westlands-studio-apartment/ | VAAL Real Estate | developer | 2026-10-16 | Studio **$49,000**; School Lane |
| 4 | https://vaal.co.ke/apartments/canto-westlands-1-bedroom-apartment/ | VAAL Real Estate | developer | 2026-10-16 | 1BR **$68,000**; School Lane |
| 5 | https://vaal.co.ke/ | VAAL Real Estate | developer | 2026-10-16 | **59% Sold Out** inventory chip; unit cards |
| 6 | https://vaal.co.ke/about-us/ | VAAL Real Estate | developer | 2026-10-16 | Developer identity / track record |
| 7 | https://gna.co.ke/project/canto-westlands-luxurious-studios-and-1-bedrooms/ | GNA | agent | 2026-10-16 | Dense amenities, mix, price ranges, Q4 2028 |
| 8 | https://commercialpropertykenya.com/properties/canto-westlands-apartments/ | CPK | agent | 2026-10-16 | 34 School Lane; 38/56 sqm; typed USD/KES |
| 9 | https://vorsagroup.co.ke/property/canto-apartments-studio-1-bedroom-in-westlands/ + https://vorsagroup.co.ke/wp-content/uploads/2026/04/Canto-Westland-Catalogue.pdf | Vorsa | agent / brochure | 2026-10-16 | Payment framing; **gross/net** plan sizes |
| 10 | https://austinerealtors.co.ke/property/canto-westlands-studio-apartments/ | Austine Realtors | agent | 2026-10-16 | 30% / 36 mo; Dec 2028; higher USD from |

### Evaluated but not retained (thin / shell / overlap)

- https://www.knightfrank.co.uk/properties/residential/for-sale/westlands-school-lane/hub2696809 — live HTML shell; **search-index snippet used** for payment/service-charge conflict notes only (not a retained dense page)
- https://www.linkedin.com/posts/tessa-thiga-559947360_… — thin promo (275 units; Dec 2028; 30%/36); corroboration only
- https://africatimesnetwork.co.ke/…canto… — press reprint of launch (overlap)
- https://vaal.co.ke/vaal-developments/ — hub card thin for CANTO fields
- https://vaal.africa/ — HTTP **403**
- https://nairobirealestate.co.ke/?s=canto / https://block.ke/?s=canto — no usable dedicated listing this pass

**Selection note:** Scanned ~14 candidates (VAAL hub/launch/units/home/about, developments hub, GNA, CPK, Vorsa+PDF, Austine, KF, LinkedIn, Africa Times, NRE/Block search, vaal.africa). **Always kept** developer project + launch + unit cards. Retained 10 densest (≥5 rule).

---

## 9. Field harvest

| Field | Outcome | Modeling note |
|-------|---------|---------------|
| Developer USD “from” dual studio/1BR | Strong | Keep as multi `price_observation` with `publisher_class=developer` |
| Gross vs net sizes | Catalogue win | Reinforce measure tags |
| Completion Apr 2028 | Canonical developer | Agent Q4/Dec secondary |
| Payment 30% | **Not** must-have (<4; no developer %) | Plus/Admin only until threshold |
| 25 storeys + studio/1BR | Canonical | |
| units/floor 11 | Agent consensus | Proposed claim; not public scalar |
| 59% sold | Developer homepage chip | Inventory claim |
| GroupCompany | Correctly null | |

### Proposed must-have / schema notes (coordinator — not auto-locked)

- Capture **USD + KES** dual currency observations when developer prices in USD.
- `payment_plan.exists` soft vs `deposit_pct` (Diamond/Longines pattern) — developer silent on %.
- Agent catalogue PDFs with plan pages: source_type `brochure` + `developer_attributed` when copy matches official site.

---

## Open questions (developer input)

1. Binding LOO: deposit % and instalment calendar (30%/36 vs 27 months)?
2. Kenya company-register name / SPV for CANTO (vs trading “VAAL Real Estate”)?
3. Confirm **34 School Lane** plot number and publish GPS.
4. Official brochure on vaal.co.ke CDN (validate Vorsa catalogue sizes)?
5. Total unit count (275?) and which floors are residential vs amenity/parking.
6. Clarify homepage **59% Sold Out** inventory vs unit-card availability.
