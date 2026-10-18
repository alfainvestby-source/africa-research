---
slug: riara-oasis
external_id: NBO-003
wave: half-batch
sources_evaluated: 13
sources_retained: 10
last_verified_at: 2026-10-16
---

# Riara Oasis (NBO-003) — half-batch research

CSV seed (unverified leads): location Riara Road, Lavington, Nairobi; stage `under_construction`; completion Q4 2027; `price_from_kes` 5,200,000; sales_contact Loyd Mokaya (Block Real Estate); developer blank.

Live research accessed **2026-10-16**. No developer-owned commercial microsite found. Strongest official materials = **NEMA EIA Study Report** for proponent **Riara Oasis Limited**. Marketing surfaces = AIMASI (Netlify + LinkedIn) + multi-agent portals.

**Method locks applied:**
- Developer / official outweigh agents; agent-only consensus caps at conf **3**.
- If developer/official sources **agree** on a field → **canonical = official**; agents secondary.
- **Official vs official** disagreement → **`needs_developer_input`**; no assumed winner.
- Prices always **`price_claims[]`** (all options). No forced scalar.
- Payment must-have if **≥4 independent agent/portal sources** agree **or** any developer source.
- Agent-only / uncorroborated (studios, sold-out, amenity adds) → **show** + **`needs_verification`**.
- Unproven brand/parent (Oasis Group; AIMASI vs SPV) → **`marketing_partner`**, not GroupCompany.
- CSV = unverified leads only.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = official/developer-backed when sources **agree**. Claim set / secondary kept for conflict detection. **`needs_developer_input`** = official pages disagree (none found here between two developer sites — NEMA is single official filing). **`needs_verification`** = low-confidence / agent-only.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Riara Oasis | 5 | NEMA title/proponent project; Block; multi-agent |
| `aliases` | secondary | Riara Oasis Residences; Riara Oasis Residency; Riara Oasis Apartments | 3 | Craiova; CPK; portals |
| `status` | claim set | CSV/`under_construction`; Block “offplan and under construction”; Craiova “under construction”; NRE **Pre-Launch** (+ UI “Construction Progress Pre-Launch 35%”) — **CONFLICT** | ≤3 | CSV; Block; Craiova; NRE |
| `geography.city` | **CANONICAL** | Nairobi | 5 | NEMA; all agents |
| `geography.neighbourhood_street` | **CANONICAL** (street + plot) + claim set (area label) | **Riara Road**; Plot **Nairobi/Block 15/121**; NEMA area **Thompson**; agents market **Lavington** and/or **Kilimani** | 5 (street/plot) / 3 (label) | NEMA; Block; NRE; A-list; AIMASI |
| `geography.plot_size` | **CANONICAL** | **0.3339 hectares** freehold (≈ **0.83 acres** — matches agent acreage) | 5 | NEMA; Sir Francis / A-list 0.83 acres |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.298579, 36.767794** (`geo_method=geocode`) | 2 | Nominatim Riara Road Thompson 2026-10-16; NEMA plot known, no filing GPS — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-riara-oasis-limited` | 5 | NEMA proponent + registered proprietor |
| `unit_types` | **CANONICAL** (official program) | **1BR, 2BR, 3BR** only on NEMA (no studios in filing) | 5 | NEMA |
| `unit_types` | secondary — **`needs_verification`** | Studio + 1/2/3 BR marketed by Block, AIMASI, NRE lead copy | 2 | Block; AIMASI; NRE intro |
| `unit_mix_counts` | **CANONICAL** | **328** one-bed; **132** two-bed; **88** three-bed | 5 | NEMA |
| `total_units` | **CANONICAL** | **548** apartments | 5 | NEMA |
| `parking_bays` | **CANONICAL** | **321** parking bays (B1 81 + B2 81 + B3 75 + GF 84) | 5 | NEMA |
| `size_by_type` | secondary (agent tables diverge) | Common agent band: 1BR **50–68/72 sqm**; 2BR **88–104/128 sqm**; 3BR **120–135 sqm**; Block studios **50 & 55 sqm** | ≤3 | Block; Sir Francis; NRE; CPK; Craiova; A-list |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** | 0 | — |
| `building_specs.storeys` | claim set — official vs agents | NEMA: **23-storey** residential building (B1–B3, GF, 1st, typical **2nd–22nd**). Agents: **22-storey / 22-floor** (often **three** towers) | 4 (NEMA program) / 3 (agent 22) | NEMA vs multi-agent |
| `building_specs.form` | claim set — **`needs_verification`** on “three towers” | NEMA: singular **building** (3 staircases, 6 lift shafts). Agents: **three U-shaped 22-floor towers** | 2 | NEMA vs NRE/CPK/Sir Francis |
| `price_claims[]` | claim set — **keep all**; no canonical | See §1a | ≤3 | agents/AIMASI/CSV |
| `currency` | **CANONICAL** | KES | 5 | all commercial sources |
| `payment_plan.deposit` | must-have via **≥4 agents** (no developer payment source) | **20%** deposit (often with optional 30%/50%); balance over construction / to completion | 3 | Block; AIMASI; Sir Francis; A-list; NRE; CPK; Craiova; BuyRent soft |
| `completion_estimate` | claim set (no developer date) | Multi-agent **December / Q4 2027**; A-list **June 2027**; Craiova **March 2028**; CPK page also slips **December 2025** in two sentences — **CONFLICT** | ≤3 | see conflicts |
| `amenities` (core — official) | **CANONICAL** core | Swimming pool; gym; parking; landscaped garden; onsite borehole planned; rainwater harvest; 750 m³ storage tanks (NEMA) | 5 | NEMA |
| `amenities` (multi-agent corroboration) | secondary | Kids play area; high-speed lifts; backup generator; CCTV / intercom; 24/7 security; “4-level” parking language | 3 | Block; Sir Francis; A-list; BuyRent; AIMASI; NRE |
| `amenities` (inflated / single-source) | **`needs_verification`** | AIMASI: rooftop BBQ; conference room; courtyard. AIMASI site “for rent from” copy mixed into sales page | 1 | AIMASI Netlify / LinkedIn |
| `construction_progress` | unknown / soft agent UI | No developer tracker. NRE UI “Pre-Launch 35%” — **`needs_verification`** | 1 | NRE only |
| `legal_title` | **CANONICAL** (tenure) | **Freehold** interest; proprietor Riara Oasis Limited | 5 | NEMA |
| `legal_approvals` | secondary | Change of Use approval cited: NCC Ref. **PLUPA-COU-002454-N** | 4 | NEMA |
| `availability_claim` | unknown | No verified sold-out / remaining-count this pass | 0 | — |

### 1a. Price claims — keep **all** options (no canonical)

No developer price list. All bands are agent / marketer claims.

| # | Claim band | Value (KES) | Publisher | Flag |
|--:|------------|-------------|-----------|------|
| A | Block “developer list” table | Studio 50/55 sqm **from 5.2M**; 1BR 60 **6.9–7.2M**, 65 **7.4M**, 68 **7.5M**, 72 **7.7M**; 2BR 88 **9.7M**, 104 **10.7M**, 128 **14.2M**; 3BR 120 **13.2M**, 135 **14.7M** | block.ke | Secondary; matches CSV from |
| B | Sir Francis / A-list / BuyRent-style band | 1BR **5.5–7M** (50–68 sqm, 6 layouts); 2BR **9.5–10M** (88–95); 3BR **13.5–15M** (120–135) | Sir Francis; A-list; BuyRent/Coral; NRE typed table | Secondary |
| C | CPK cash table | 1BR 50 **4.9M**, 52 **5.4M**, 60/65 **7.1M**, 68 **7.4M**, 72 **7.6M**; 2BR 88 **9.6M**, 104 **10.6M**, 128 **13.6M**; 3BR 120 **12.2M**, 135 **13.7M**; headline from **4.9M** | commercialpropertykenya.com | Secondary — **needs_verification** vs higher bands |
| D | AIMASI LinkedIn | Studio **5.0M**; 1BR **6.2M**; 2BR **9.2M**; 3BR **12.7M** | AIMASI posts | Secondary — marketer; studio vs NEMA |
| E | AIMASI Netlify hero | “1, 2 & 3 Bedroom Units From **KES 5.5M**” (page also mixes rental language) | aimasi.netlify.app | Secondary |
| F | NRE FAQ vs body | Body/table ≈ Band B; FAQ “indicative” 1BR **5.2–5.8M**, 2BR **7.4–9M**, 3BR ~**13M** — **in-page conflict** | nairobirealestate.co.ke | Secondary — **needs_verification** |
| G | Craiova table | Labels 50/55 sqm as “studios”; 60–72 1BR **7.7–8.2M**; 2BR 88 **9M**, 104 **9.5M**, 128 **14.2M**; 3BR 120 **13.2M**, 135 **14.7M** | craiovarealtors.com | Secondary |
| H | CSV seed | `price_from_kes` **5,200,000** | seed | Unverified lead |

**Canonical price:** none.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **20% deposit** | Block; AIMASI LinkedIn; Sir Francis; A-list; NRE; CPK (20% + 30%/50% options); Craiova | **≥4** agents/marketers | **Met via agents** | Must-have field; conf **3** (no developer LOO/FAQ) |
| Optional **30% / 50%** deposit | Sir Francis; A-list; CPK; NRE calculator max 50% | ≥3 | Soft secondary | Show as option claim |
| Balance over construction / to completion | Block; AIMASI; Sir Francis; NRE; Craiova | ≥4 | Soft secondary | Exact milestone calendar unknown |
| Developer LOO / official schedule | None found | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-riara-oasis-limited` |
| `legal_name` | Riara Oasis Limited |
| `trading_names` | Riara Oasis (project brand) |
| `website` | **None found** for the Limited company this pass |
| `evidence` | NEMA EIA Study Report (EIA 2264 SR 3407): project proponent **and** registered proprietor of Nairobi/Block 15/121; P.O. Box 100803-00101, Nairobi |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV developer cell **blank** — correct as lead; do not fill from agents without filing |

**Primary developer = Riara Oasis Limited (confidence 5)** as land proprietor / EIA proponent. Marketing sellers (AIMASI, Block, etc.) are **not** the legal developer without further evidence.

### Developer proposal
Keep **Riara Oasis Limited** as primary. Confirm with human whether AIMASI or “Oasis Group” has equity/construction role — currently modeled as RelatedParty `marketing_partner` only.

---

## 3. GroupCompany

**None.** Block’s Mogotio Oasis page names an **“Oasis Group”** portfolio that includes Riara Oasis / Riara One — **unproven parent**. Do **not** set GroupCompany.

---

## 4. RelatedParty

| id | name | relationship_type | Evidence | Conf |
|----|------|-------------------|----------|-----:|
| `rp-aimasi-real-estate` | AIMASI Real Estate Limited | `marketing_partner` | LinkedIn posts market Riara Oasis with prices/payment/contacts; Netlify `aimasi.netlify.app` project page; GoAfricaOnline directory points at Netlify | 3 |
| `rp-oasis-group` | Oasis Group (name as marketed) | `marketing_partner` | Block Mogotio Oasis page: “Oasis Group, whose earlier projects include … **Riara Oasis**, Riara One …” — **unproven** legal parent/alias | 2 |

Riara One Residency appears in NEMA as a **nearby** 18-level development (Plate 2.2), not as this project’s developer entity. Block says Riara Oasis is from the “same developer as the earlier Riara One” without naming the company — keep as diligence lead, not a separate GroupCompany.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate | agency / portal | CSV sales_contact; densest typed price list; 20% LOO | https://block.ke/property/studios1-2-3-bedroom-apartments-for-sale-in-lavington-at-riara-oasis/ |
| NRE Real Estate | agency | Listing + payment calculator; Pre-Launch status | https://nairobirealestate.co.ke/properties/riara-oasis |
| CPK Real Estate (Commercial Property Kenya) | agency | Cash price table; groundbreaking Apr 2025 claim | https://commercialpropertykenya.com/properties/riara-oasis-apartments-on-riara-road-lavington-nairobi/ |
| Sir Francis Homes / Sir Francis Marketing Ltd | agency | Dense unit/payment summary | https://sirfrancismarketingltd.co.ke/properties/riara-oasis/ |
| A-list Real Estate | agency | June 2027 completion outlier | https://a-listrealestate.ke/property/riara-oasis/ |
| Craiova Realtors | agency | March 2028 completion outlier; studio labeling | https://craiovarealtors.com/property/riara-oasis-residences-1-2-3-bedroom-apartments/ |
| Coral Property International Ltd (via BuyRentKenya) | agency / portal listing | Amenities + Band B prices | https://www.buyrentkenya.com/listings/1-bedroom-apartment-for-sale-lavington-3805807 |
| AIMASI Real Estate Limited | marketer (RelatedParty) | Social + Netlify sales surface | LinkedIn posts; https://aimasi.netlify.app |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| email | riaraoasis@gmail.com | Property sales (AIMASI posts) |
| phone | +254 116 333 444 | Property sales (AIMASI) |
| url | https://aimasi.netlify.app | RelatedParty marketing site |
| phone | +254 725 937 686 | Agent: Block (CSV Loyd Mokaya) |
| email | loyd@block.ke | Agent: Block (CSV) |
| phone | +254 141 361 320 | Agent: NRE |
| email | info@nairobirealestate.co.ke | Agent: NRE |
| phone | +254 784 448 888 | Agent: CPK / Kenneth Ikiara |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 722 720 812 | Agent: Sir Francis Homes |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |
| phone | +254 706 327 148 | Agent: Coral (BuyRentKenya listing) |
| postal | P.O. Box 100803-00101, Nairobi | Developer: Riara Oasis Limited (NEMA) |
| postal | P.O. Box 157-00600, Nairobi | Stakeholder: Space Planners Ltd (NEMA) |

**CSV sales_contact = Block agent**, not the developer SPV. Split Contact.owner accordingly.

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Space Planners Ltd** | other (EIA firm of experts) | NEMA cover: EIA Firm of Experts | 5 |
| Unnamed architect / structural engineers / contractor | other | NEMA mentions consultants/contractor generically; **no firm names** for builder this pass | 0 |

No financing partner named this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Neighbourhood label** | NEMA **Thompson**; agents **Lavington**; AIMASI/A-list/Craiova also **Kilimani** | Street + plot **canonical** from NEMA. Area labels = claim set; do not collapse. |
| 2 | **Storeys** | NEMA **23-storey** (floors through 22nd typical) vs agents **22-storey/22-floor** | Official filing vs agents → prefer NEMA for program description; keep agent 22 as secondary claim. Not two disagreeing developer sites → not `needs_developer_input`, but buyer should confirm floor-count convention. |
| 3 | **Building form** | NEMA singular building vs agents **three U-shaped towers** | Show both; three-tower claim **`needs_verification`** (may be wings). |
| 4 | **Unit types / studios** | NEMA **no studios** (328/132/88) vs Block/AIMASI/NRE studio marketing | **Canonical unit program = NEMA**. Studios **`needs_verification`**. |
| 5 | **Prices** | Bands A–H diverge (from **4.9M** to **5.5M** typed 1BR; AIMASI studio **5M** vs Block studio **5.2M**) | **Keep all** `price_claims[]`. No canonical. |
| 6 | **Completion** | Dec/Q4 2027 (multi) vs **June 2027** (A-list) vs **March 2028** (Craiova) vs CPK in-page **Dec 2025** slips | No developer date → claim set; Dec 2027 is modal agent claim only (conf ≤3). |
| 7 | **Status** | under_construction / off-plan / Pre-Launch | Claim set; CSV lead ≠ NRE Pre-Launch. |
| 8 | **Payment options** | Flat **20%** vs **20/30/50%** menus | Must-have **20%** met via ≥4; options secondary. |
| 9 | **CPK completion year typos** | Same CPK page: Dec **2027** timeline vs “completed in December **2025**” exit copy | Flag CPK 2025 as conflict/error candidate — **`needs_verification`**. |
| 10 | **Developer brand** | Riara Oasis Limited (NEMA) vs AIMASI marketing vs Block “Oasis Group” / “same as Riara One” | Legal SPV = Limited. Others = RelatedParty / diligence leads. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~13** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~13 candidates (NEMA PDF, Block listing, NRE, CPK, Sir Francis, A-list, Craiova, BuyRent/Coral, AIMASI LinkedIn, AIMASI Netlify, GoAfricaOnline, Block Mogotio Oasis portfolio note, Concrete City, CSV). **Always kept** official NEMA filing (no developer microsite). Retained 10 densest field-bearing sources (≥5 rule).

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://nema.go.ke/wp-content/uploads/2025/03/EIA-2264-SR-3407-RIARA-OASIS-LTD-min.pdf | NEMA / Riara Oasis Limited (proponent) | official_filing | 2026-10-16 | **Always keep** — 548 units; 328/132/88; 23-storey; 321 parking; freehold 0.3339 ha; Thompson; Space Planners |
| 2 | https://block.ke/property/studios1-2-3-bedroom-apartments-for-sale-in-lavington-at-riara-oasis/ | Block Real Estate | agent | 2026-10-16 | Dense price table; 20%; Dec 2027; Riara One same-developer claim; CSV lead |
| 3 | https://nairobirealestate.co.ke/properties/riara-oasis | NRE Real Estate | agent | 2026-10-16 | Unit bands; Pre-Launch; payment calculator; in-page FAQ price conflict |
| 4 | https://commercialpropertykenya.com/properties/riara-oasis-apartments-on-riara-road-lavington-nairobi/ | CPK Real Estate | agent | 2026-10-16 | Cash table from 4.9M; groundbreaking Apr 2025; Dec 2025 typo conflict |
| 5 | https://sirfrancismarketingltd.co.ke/properties/riara-oasis/ | Sir Francis Homes | agent | 2026-10-16 | 0.83 acres; 20/30/50%; Dec 2027; Band B |
| 6 | https://a-listrealestate.ke/property/riara-oasis/ | A-list Real Estate | agent | 2026-10-16 | **June 2027** outlier; Kilimani label |
| 7 | https://craiovarealtors.com/property/riara-oasis-residences-1-2-3-bedroom-apartments/ | Craiova Realtors | agent | 2026-10-16 | **March 2028** outlier; studio labeling on 50/55 sqm |
| 8 | https://www.buyrentkenya.com/listings/1-bedroom-apartment-for-sale-lavington-3805807 | Coral / BuyRentKenya | agent | 2026-10-16 | Amenities + Band B; flexible plans |
| 9 | https://www.linkedin.com/posts/aimasi-real-estate-limited_aimasirealestate-riaraoasis-kilimani-activity-7434849508322131968-h4ix | AIMASI Real Estate Limited | social / marketer | 2026-10-16 | Studio–3BR price card; 20%; Dec 2027; contacts |
| 10 | https://aimasi.netlify.app | AIMASI | marketer_site | 2026-10-16 | Amenities; from 5.5M; mixed rent copy — keep as marketing surface |

### Evaluated but not retained (thin / duplicate / off-project)

| url | Why skipped |
|-----|-------------|
| https://www.goafricaonline.com/ke/1233749-riara-oasis | Thin directory card (points at Netlify); no commercial fields |
| https://concretecityproperties.com/property/riara-oasis-lavington-1br-from-ksh-5-5m/ | Fetch thin/failed this pass; overlaps Band B |
| https://block.ke/property/mogotio-oasis-studio-1-2-3-bed-luxury-apartments-on-mogotio-road-westlands-from-kes-5-8m/ | **Other project**; used only as Oasis Group RelatedParty lead — not retained as Riara Oasis source row |
| Duplicate AIMASI LinkedIn posts (same price card) | Redundant with retained post |
| CSV NBO-003 row | Lead only |

---

## 9. Field harvest → must-have extension proposals

| Proposed / reinforced field | Riara Oasis evidence | Consensus note |
|----------------------------|----------------------|----------------|
| Official **EIA / NEMA filing** as developer-weight source when microsite absent | Full program, tenure, parking, unit mix | Reinforce: always keep official filing |
| `total_units` + typed `unit_mix_counts` claim set | **548** / 328·132·88 on NEMA | Strengthen propose-must (C2 already 2/2) |
| `parking_bays` when official | **321** | Propose optional → must when filing/brochure states |
| `plot_size` + `tenure` (freehold/leasehold) | 0.3339 ha freehold | Propose legal claim set |
| `storeys` claim set | 23 (NEMA) vs 22 (agents) | Bump storeys propose consensus |
| `building_form` / wings vs towers | Singular NEMA vs three-tower agents | Capture when conflicted |
| RelatedParty `marketing_partner` | AIMASI + unproven Oasis Group | Bump Astra-style capture consensus |
| Agent-threshold `payment_plan` without developer LOO | ≥4 on **20%** | Conf capped at 3 — pattern holds |
| Neighbourhood **label claim set** (Thompson / Lavington / Kilimani) | Official vs marketing labels | Geography nuance for portal later |
| Studios absent from official mix | Agent studios **`needs_verification`** | Reinforces low-confidence show rule |

---

## Open questions (developer / verification pass)

1. Confirm legal/commercial relationship: **Riara Oasis Limited** vs **AIMASI** vs marketed **Oasis Group** / Riara One team.  
2. Are marketed **studios** real SKUs or mislabeled small 1BRs? (Absent from NEMA mix.)  
3. One building vs **three towers** — confirm architectural form.  
4. Binding **price list** and **LOO** deposit (20% vs 30/50 menus).  
5. Contractual **completion** date (Dec 2027 vs June 2027 vs March 2028).  
6. Current construction status vs NRE “Pre-Launch 35%”.  
7. Named main **contractor** / architect beyond Space Planners (EIA firm).
