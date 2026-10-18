---
slug: lesonia-residences
external_id: NBO-011
cycle: half-batch
pilot: false
wave: C
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Lesonia Residences (NBO-011) — Wave C / half-batch

CSV seed (unverified leads): location Gatundu Road / Tinderet Avenue, Kileleshwa, Nairobi; stage `under_construction`; completion Q3 2028; `price_from_kes` 5,500,000; sales_contact NRE Real Estate; developer **blank**.

Live research: official project site (homepage, about, terms, tools, blog) + multi-agent portals accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer pages disagree): **do not assume a winner** → flag **`needs_developer_input`**; no canonical until a later verification pass.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- Payment must-have if any developer source **or** ≥4 agent sources. Agent-only / uncorroborated → **`needs_verification`**. CSV = unverified leads only.
- Unproven brand/shared-team claims → show + **`needs_verification`**; do **not** invent GroupCompany or legal co-developer.
- No legal company registry / NEMA proponent recovered this pass — do **not** invent a Limited name.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official pages disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Lesonia Residences (site brand **Lesonia Residency**) | 5 | lesoniaresidency.co.ke; agents |
| `aliases` | secondary | Lesonia Residency; Lesonia Residence; Lesonia Residencies; Lesonia Apartments (schema alternateName) | 4 | site; Austine; Splendor title; JSON-LD |
| `status` | claim set | CSV/`under_construction`; NRE **Under Construction** (+ UI “58%”); Westlands “Under Construction (Active Off-Plan)”; Austine “Off-plan / Newly launched”; official site markets **off-plan** through Dec 2028 | 3 | CSV; NRE; Westlands; Austine; site |
| `geography.city` | **CANONICAL** | Nairobi | 5 | site; all |
| `geography.neighbourhood_street` | **CANONICAL** | Kileleshwa — intersection of **Gatundu Road** and **Tinderet Avenue** | 5 | homepage; about JSON-LD streetAddress; multi-agent |
| `geography.landmark` | **CANONICAL** (official spelling) | Directly opposite **Kenton International School** | 5 | homepage; about |
| `geography.landmark` | secondary spelling — **needs_verification** | Agents also write **Kento** International School | 2 | Austine; Splendor search |
| `geography.plot_size` | **CANONICAL** | **0.75-acre** estate | 5 | homepage; about |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.278414, 36.785502** (`geo_method=geocode`) | 3 | Midpoint Gatundu Rd + Tinderet Ave Nominatim 2026-10-16; intersection query NONE — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | trading brand only — **legal entity unknown** | → `dev-lesonia-residency` (**trading name**; conf on **legal** name = 0) | 3 (trading) / 0 (legal) | terms “real estate development company”; site; no Limited / NEMA proponent found |
| `unit_types` | **CANONICAL** | 1 Bedroom; 2 Bedroom; 3 Bedroom | 5 | homepage; about; terms |
| `size_by_type` | **CANONICAL** (band on homepage table) | 1BR **55–68 sqm**; 2BR **110–115 sqm**; 3BR **150–155 sqm** | 5 | homepage unit table (agrees with about/price framing from 5.5M) |
| `size_by_type` | secondary | Typed agent rows: 55 / 65 / 68; 110 / 115; 150 / 155. NRE card also shows 2BR **110–118** once | 3 | Austine; CPK; Sydia; NRE |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** | 0 | — |
| `total_units` / `storeys` | unknown | **Not published** on official pages or densest agents this pass | 0 | — |
| `price_claims[]` | claim set — **`needs_developer_input`** on dual/triple official bands; **keep all** | See §1a — no scalar | ≤3 | |
| `currency` | **CANONICAL** | KES (terms: payments in KES) | 5 | terms; all |
| `payment_plan.deposit` | **CANONICAL** (developer pages **agree**) | **Minimum / initial 20%** deposit to reserve | 5 | homepage; about; terms; blog; mortgage tool |
| `payment_plan.balance_structure` | claim set — **`needs_developer_input`** | Homepage/about: remaining **80%** flexible **monthly or quarterly** to Dec 2028. Kenton blog: **20% / 60% construction / 20% handover**. Terms also allow “construction-linked **or** post-completion” options | 2 | Official vs official schedule shapes |
| `payment_plan.deposit` | secondary agent variants | Austine: **20–30%** deposit. Multi-agent echo **20%** / 20/80 | ≤3 | Austine; Westlands; NRE; Sydia |
| `completion_estimate` | **CANONICAL** (developer agree) | **December 2028** handover | 5 | homepage; about; terms; blogs |
| `completion_estimate` | secondary | CSV / NRE header **Q3 2028** vs body **December 2028** — Dec is **Q4**, not Q3 → agent/CSV conflict | 2 | CSV; NRE |
| `amenities` (core) | **CANONICAL** | Heated infinity pool; modern gym; sauna; yoga studio; children’s play area; business center; meeting room; reading area; co-working; art-space café/bar; rooftop lounge & garden; open floor garden; 24/7 CCTV; access control; parking + visitor/Uber parking; backup generator; borehole; EV charging stations | 5 | homepage amenity sections |
| `amenities` | secondary / inflated — **needs_verification** | Austine/Westlands add wellness spa, clubhouse, indoor games, rooftop BBQ, restaurant — not all itemised identically on homepage core list | 2 | Austine; Westlands; Sydia |
| `design_concept` | secondary | “Balcony garden” concept (agents + CPK); private balcony garden per unit | 3 | Westlands; CPK; Sydia |
| `construction_progress` | secondary — **needs_verification** | NRE UI “Under Construction **58%**” (no developer tracker). Sydia links “Latest Site Update – 24th April 2026” photo album (not quantified %) | 1 | NRE; Sydia |
| `legal_title` / tenure | secondary — **needs_verification** | Westlands table: **Leasehold** (agent only). Official LOO/title not published this pass | 1 | Westlands |
| `reservation_fee` | soft | Homepage purchase process: reserve with a **reservation fee** (applied to purchase) — amount unknown | 2 | homepage |

### 1a. Price claims — keep **all** options (no canonical scalar)

**Official vs official** on the same developer site → **`needs_developer_input`**. Agents largely echo the homepage unit table (from 5.5M).

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Homepage **unit price table** | 1BR 55–68 sqm **5.5M–8.0M**; 2BR 110–115 **12.5M–15.0M**; 3BR 150–155 **17.1M–18.3M**; overview “from KSh 5.5 Million” | lesoniaresidency.co.ke/ | Official — **`needs_developer_input`** vs B/C/D |
| B | Homepage “Apartment Prices at Lesonia” prose | 1BR **from KES 8.5M**; 2BR **KES 12M–18M**; 3BR **from KES 18M** | same homepage | Official — conflicts with A |
| C | Mortgage calculator cards | 1BR **KES 8.5M** (deposit 1.7M); 2BR **12.5M**; 3BR **17.1M** | /tools/mortgage-calculator | Official — conflicts with A (and partly B) |
| D | Affordable-blog unit/tenant table | 1BR **5.5M**; 2BR **8.5M**; 3BR **12.5M** (same blog also states starting **5.5M**) | /blog/affordable-off-plan-houses-sale-nairobi-2028 | Official — conflicts with A/B/C |
| E | About “Starting from KSh 5.5 Million” | from **5.5M** | /about-us | Aligns with A |
| F | NRE | 1BR **5.5–8.0M**; 2BR **12.5–15.0M**; 3BR **17.1–18.3M** (FAQ softens upper 1/2BR) | nairobirealestate.co.ke | Secondary |
| G | Austine / Sydia typed sizes | 55 **5.5–6.6M**; 65 **6.5–7.7M**; 68 **7.0–8.0M**; 110 **12.5–14M**; 115 **13–15M**; 150 **17.1–18M**; 155 **17.3–18.3M** | Austine; Sydia | Secondary |
| H | CPK “from” list | 55 from **5.6M**; 65 **6.5M**; 68 **7.0M**; 110 **12.5M**; 115 **13.0M**; 150 **17.1M**; 155 **17.3M** | commercialpropertykenya.com | Secondary (5.6M vs 5.5M) |
| I | Westlands summary bands | 1BR **5.5–8.0M**; 2BR **12.5–15.0M**; 3BR **17.1–18.3M** | westlands-consult.co.ke | Secondary |
| J | CSV seed | `price_from_kes` **5,500,000** | seed | Unverified lead |

**Canonical price:** none. Always `price_claims[]`.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **20% initial / minimum deposit** | Homepage; about; terms; blog(s); mortgage tool | Developer **≥1** (agreeing) | **Met via developer** | **CANONICAL must-have** |
| **80% balance** monthly/quarterly to handover | Homepage; about | Developer agree on soft structure | Met as soft balance claim | Secondary detail; conflicts with 20/60/20 blog |
| **20 / 60 / 20** schedule | Kenton school blog | 1 official blog | — | Claim set + **`needs_developer_input`** vs 20/80 |
| Agent **20%** / 20/80 | Westlands; NRE; Sydia; CPK (implied); ≥4 with Austine 20–30 | **≥4** | Met as agent consensus | Aligns with canonical 20% |
| Austine **20–30%** | Austine only | 1 | — | Secondary **needs_verification** |
| Full SPA / LOO PDF | Not fetched | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-lesonia-residency` |
| `legal_name` | **unknown** — no “Limited” / registry / NEMA proponent recovered this pass |
| `trading_names` | Lesonia Residency; Lesonia Residences; Lesonia Apartments |
| `website` | https://lesoniaresidency.co.ke/ |
| `evidence` | Terms §2: “Lesonia Residency is a real estate development company operating in Kenya”; about + homepage project materials; JSON-LD `@type: RealEstateAgent` name “Lesonia Residency” |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV developer cell **blank** — correct lead (no named legal entity in seed) |
| `riara_one_team_claim` | Austine + Westlands: “team behind / developers of **Riara One** Apartments (Kilimani)” — **agent-only**, **`needs_verification`**. Do **not** merge with Riara Oasis Limited (NBO-003) or invent shared SPV |

**Primary developer trading brand = Lesonia Residency (confidence 3).** Legal entity remains the top open gap.

---

## 3. GroupCompany

**None.** No evidenced parent.

---

## 4. RelatedParty

None required. Unproven “Riara One team” claim is **not** modelled as GroupCompany or co-developer; kept as developer note + conflict with **`needs_verification`**.

Westlands Avenue Consult self-styles as “exclusive selling agent” — captured under Agents (role claim), not RelatedParty parent.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| NRE Real Estate | agency | CSV sales_contact; listing + 20% calculator; UC 58% UI | https://nairobirealestate.co.ke/properties/lesonia-residences |
| Westlands Avenue Consult | agency | Dense listing; claims **exclusive selling agent**; 20/80; Riara One team claim | https://westlands-consult.co.ke/property/apartment/lesonia-residency/ |
| Austine Realtors | agency | Typed prices; 20–30% deposit; Riara One team claim | https://austinerealtors.co.ke/property/lesonia-residence/ |
| CPK Real Estate (Kenneth Ikiara) | agency | Typed “from” prices (5.6M start); Dec 2028 | https://commercialpropertykenya.com/properties/lesonia-residences-kileleshwa/ |
| Sydia Realty | agency | Typed prices; Dec 2028; site-update photo links (Apr 2026) | https://sydiarealty.com/estate_property/lesonia-residences-luxury-living-surrounded-by-nature-in-kileleshwa/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 704 043 466 | Property sales office / Lesonia Residency site |
| email | info@lesoniaresidency.co.ke | Property / trading developer |
| address | Lesonia Residency, Kileleshwa, Nairobi (terms); street = Gatundu & Tinderet intersection | Property |
| url | https://lesoniaresidency.co.ke/ | Property |
| url | https://lesoniaresidency.co.ke/about-us | Property |
| url | https://lesoniaresidency.co.ke/terms-and-conditions | Property |
| phone | +254 141 361 320 | Agent: NRE (CSV) |
| email | info@nairobirealestate.co.ke | Agent: NRE (CSV) |
| phone | +254 722 218 039 | Agent: Westlands Avenue Consult |
| email | info@westlands-consult.co.ke | Agent: Westlands Avenue Consult |
| phone | +254 704 350 354 | Agent: Austine Realtors |
| phone | +254 784 448 888 | Agent: CPK / Kenneth Ikiara |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 700 437 505 / +254 759 333 300 | Agent: Sydia Realty |
| email | info@sydiarealty.com | Agent: Sydia Realty |

**CSV sales_contact = NRE ≠ Lesonia project phones** — split Contact.owner correctly.

---

## 6. Stakeholders

None named (contractor / architect / financing) on official materials this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Prices (official)** | Homepage table from **5.5M** **vs** homepage prose from **8.5M** **vs** mortgage cards **8.5 / 12.5 / 17.1M** **vs** affordable-blog 2BR **8.5M** / 3BR **12.5M** | **Official vs official** → **`needs_developer_input`**. Keep **all** `price_claims[]`. No scalar |
| 2 | **Payment schedule shape** | Official 20% + **80%** flexible **vs** Kenton blog **20/60/20** **vs** terms allowing construction-linked **or** post-completion | Deposit **20%** canonical (agreeing). Schedule shape → **`needs_developer_input`** |
| 3 | **Completion quarter label** | Developer **December 2028** **vs** CSV/NRE header **Q3 2028** | Canonical = **December 2028** (developer agree). Q3 label secondary / wrong-quarter |
| 4 | **Legal developer name** | Trading **Lesonia Residency** only; agents “Riara One team”; CSV blank | Legal entity **unknown**. Riara One claim **`needs_verification`**. No invented Limited |
| 5 | **School spelling** | Official **Kenton** vs agent **Kento** | Canonical landmark spelling = **Kenton** |
| 6 | **Status / progress %** | Off-plan marketing vs UC; NRE **58%** unverified | Claim set; % **`needs_verification`** |
| 7 | **CSV sales_contact** | NRE ≠ project +254 704 043 466 | Split Contact.owner |
| 8 | **CPK from 5.6M** | vs official table 5.5M | Secondary price claim H |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 candidates (homepage, about-us, terms, mortgage calculator, affordable blog, Kenton blog, NRE, Westlands Consult, Austine, CPK, Sydia, Concrete City, Splendor, Farman PDF, CSV). **Always kept** official project site pages. Retained 10 densest (≥5 rule).

**Thin / skipped (not in retained list):**
- https://concretecityproperties.com/property/lesonia-residences-kileleshwa-1-2-3-bedroom-apartments-from-ksh-5-5m/ — **parked / redirect shell** (not usable listing content)
- https://splendorholdings.co.ke/properties/lesonia-residencies-kileleshwa/ — **HTTP 500** this pass; search snippets only
- https://farmanrealestate.com/pdf/lesonia-residences-kileleshwa — **404**
- https://lesoniaresidency.co.ke/blog/affordable-off-plan-houses-sale-nairobi-2028 — evaluated for price conflict D; denser schedule evidence kept via Kenton blog + homepage (not double-counted in retained 10)
- CSV NBO-011 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://lesoniaresidency.co.ke/ | Lesonia Residency | project_site | 2026-10-16 | Unit table; amenities; 20%/80%; Dec 2028; **price prose conflict** — always keep |
| 2 | https://lesoniaresidency.co.ke/about-us | Lesonia Residency | project_site | 2026-10-16 | 0.75 acre; Gatundu/Tinderet; Kenton; 20%; from 5.5M; JSON-LD address |
| 3 | https://lesoniaresidency.co.ke/terms-and-conditions | Lesonia Residency | project_site | 2026-10-16 | “development company”; min 20% deposit; KES; contacts |
| 4 | https://lesoniaresidency.co.ke/tools/mortgage-calculator | Lesonia Residency | project_site | 2026-10-16 | Cards 8.5 / 12.5 / 17.1M; 20% min — official price conflict |
| 5 | https://lesoniaresidency.co.ke/blog/real-estate-kenton-international-school-kileleshwa | Lesonia Residency | project_site / blog | 2026-10-16 | **20/60/20** schedule claim |
| 6 | https://nairobirealestate.co.ke/properties/lesonia-residences | NRE | agent | 2026-10-16 | CSV contact; price bands; Q3 vs Dec; 58% UI |
| 7 | https://westlands-consult.co.ke/property/apartment/lesonia-residency/ | Westlands Avenue Consult | agent | 2026-10-16 | Exclusive-agent claim; 20/80; Riara One team; leasehold note |
| 8 | https://austinerealtors.co.ke/property/lesonia-residence/ | Austine Realtors | agent | 2026-10-16 | Typed prices; 20–30%; Riara One team; Kento spelling |
| 9 | https://commercialpropertykenya.com/properties/lesonia-residences-kileleshwa/ | CPK Real Estate | agent | 2026-10-16 | From 5.6M typed list; Dec 2028 |
| 10 | https://sydiarealty.com/estate_property/lesonia-residences-luxury-living-surrounded-by-nature-in-kileleshwa/ | Sydia Realty | agent | 2026-10-16 | Typed prices; site-update album link Apr 2026 |

---

## 9. Field harvest

| Field | Lesonia status | Notes / consensus bump |
|-------|----------------|------------------------|
| canonical_name / aliases | OK | Residences vs Residency branding |
| status | Claim set | Off-plan + UC labels |
| geography street + school landmark | OK | Gatundu & Tinderet; Kenton canonical |
| `plot_size` acres | OK (0.75) | Developer agree |
| primary_developer **legal** | **Gap** | Trading brand only — propose insist on LOO/company docs / NEMA search |
| GroupCompany | none | Correct |
| unit_types / size bands | OK | Developer table |
| `total_units` / `storeys` | Missing | Still unknown — no bump |
| `price_claims[]` | All A–J retained | Strong **official-vs-official** example → **`needs_developer_input`** |
| cash vs instalment columns | Weak | Not dual-column LOO this pass |
| `payment_plan.deposit` | **20% canonical** | Must-have met via developer |
| `payment_plan` schedule shape | **`needs_developer_input`** | 20/80 vs 20/60/20 |
| completion_estimate | **Dec 2028 canonical** | Q3 CSV/NRE secondary |
| amenities core | OK | Reject uncorroborated spa/clubhouse adds as canonical |
| `construction_progress` | Agent UI only | No developer tracker % |
| Named stakeholders | none | — |

### Proposed must-have / process extensions (this project)

| Proposed extension | Evidence here | Consensus note |
|--------------------|---------------|----------------|
| Persist **official-vs-official price conflicts on a single microsite** as `needs_developer_input` | Homepage table vs prose vs mortgage vs blog | Reinforces Cycle 2 lock |
| `payment_plan` as **claim set** (deposit % vs full schedule) | 20% agree; 20/80 vs 20/60/20 disagree | Deposit can be canonical while schedule stays claim set |
| **Legal-entity chase** when site is brand-only | Lesonia Residency ≠ proven Limited | Coordinator: NEMA/registry pass for Wave C gaps |
| Landmark spelling conflicts | Kenton vs Kento | Canonical = developer spelling |

---

## Open questions (developer input)

1. What is the **registered legal developer** (company name / SPV) and any NEMA EIA reference?
2. Which live price list is binding: homepage table (**from 5.5M**) vs prose/mortgage (**from 8.5M**) vs blog 2BR/3BR figures?
3. Binding payment schedule: **20% + 80%** flexible vs **20/60/20**?
4. Total **units** and **storeys**?
5. Is the “team behind **Riara One**” claim true, and under which legal entities?
6. Exact plot/LR number and public GPS?
