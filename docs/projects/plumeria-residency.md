---
slug: plumeria-residency
external_id: NBO-015
wave: C
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Plumeria Residency (NBO-015) — Wave C research

CSV seed (unverified leads): location Riara Road, Kilimani, Nairobi; stage `off_plan`; completion **Q4 2026 (check status)**; `price_from_kes` 10,000,000; sales_contact Own It Kenya (+254 722 716 182, sales@ownitkenya.com); developer blank.

Live research accessed **2026-10-16**. No developer-owned commercial microsite found. Strongest official materials = **NEMA EIA** for proponent **Riara Plumeria Development Limited** (Plot L.R. No. **330/179**, Riara Road). Marketing = Own It Kenya (CSV) + multi-agent portals. Hauzisha “Golden Apple” attribution conflicts with a **different** NEMA project on another Riara Road plot — do not merge entities.

**Method locks applied:**
- Developer / official outweigh agents; agent-only consensus caps at conf **3**.
- If developer/official sources **agree** on a field → **canonical = official**; agents secondary.
- **Official vs official** disagreement → **`needs_developer_input`**; no assumed winner.
- Prices always **`price_claims[]`** (all options). No forced scalar.
- Payment must-have if **≥4 independent agent/portal sources** agree **or** any developer source.
- Agent-only / uncorroborated (penthouses, amenity adds, sold-out) → **show** + **`needs_verification`**.
- Unproven brand/parent → **`marketing_partner`**, not GroupCompany. Wrong-entity leads flagged, not invented as developer.
- CSV = unverified leads only.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = official/developer-backed when sources **agree**. Claim set / secondary kept for conflict detection. **`needs_verification`** = low-confidence / agent-only.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Plumeria Residency (NEMA title: Plumeria Apartments) | 5 | NEMA; Own It; multi-agent |
| `aliases` | secondary | Riara Plumeria Residency; Plumeria Apartments; Plumeria Residency Kilimani | 3 | CPK; NEMA; portals |
| `status` | claim set | CSV `off_plan`; NRE **Finishing** (+ UI “Finishing **88%**”); agents “under construction” / “almost ready” / show house ready — **CONFLICT** on readiness language | ≤3 | CSV; NRE; GNA; Flamingo |
| `geography.city` | **CANONICAL** | Nairobi | 5 | NEMA; all agents |
| `geography.neighbourhood_street` | **CANONICAL** (street + plot) + claim set (area label) | **Riara Road** at / near **King’ara Road** junction; Plot **L.R. No. 330/179**; NEMA **Dagoretti North**; agents **Kilimani** / **Lavington** border | 5 (street/plot) / 3 (label) | NEMA; Own It; NRE; GNA |
| `geography.lat_lng` | **CANONICAL** (official filing) | **−1.2974, 36.7606** | 5 | NEMA §2.1 |
| `geography.plot_size` | secondary | Agents ≈ **1 acre**; NEMA ownership stated but **hectare figure not extracted** this pass | 2 | Sir Francis; A-list; Flamingo; Miamu (indexed) |
| `primary_developer_id` | **CANONICAL** | → `dev-riara-plumeria-development` | 5 | NEMA proponent + registered proprietor (transferee) |
| `unit_types` | **CANONICAL** (official program) | **2-bedroom and 3-bedroom** housing units | 5 | NEMA |
| `unit_types` | secondary — **`needs_verification`** | **4BR / 5BR penthouses** marketed widely | 2 | Sir Francis; Flamingo; UrbanCore; GNA; NRE; Zyve indexed |
| `total_units` | **CANONICAL** | **332** units (floors 1–16 × **20**/floor + floor 17 × **12**) | 5 | NEMA |
| `block_count` | **CANONICAL** (presence) | **Four blocks** | 5 | NEMA; agents A–D |
| `building_specs.storeys` | **CANONICAL** (program) | **17** floors (typical 1st–16th + 17th); **3** basement parking levels | 5 | NEMA; multi-agent agree |
| `building_specs.units_per_floor` | claim set (reconciles) | NEMA: **20 units/floor** (floors 1–16). Agents: **5 units per floor** per block → 5×4 = 20 — consistent if read as per-block | 4 | NEMA; Sir Francis; A-list; Flamingo |
| `size_by_type` | secondary (agent tables) | Common: 2BR **105 / 110 / 130 sqm**; 3BR **130 / 160–167 sqm**; penthouse **233–260 sqm** (agent) | ≤3 | Own It; NRE; GNA; Sir Francis; CPK; Flamingo |
| `size_measure_tag` | secondary | Own It labels sizes as **plinth area** | 3 | ownitkenya.com |
| `price_claims[]` | claim set — **keep all**; no canonical | See §1a | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | all commercial sources |
| `payment_plan.deposit` | must-have via **≥4 agents** (no developer LOO) | **30%** deposit / reserve; **70%** over remaining construction | 3 | GNA; Sir Francis; A-list; UrbanCore; CPK; NRE plan text |
| `payment_plan.deposit` | secondary — **needs_verification** | **20%** on LOO (Flamingo); NRE calculator defaults 20% while FAQ says 30% — in-page conflict | 2 | Flamingo; NRE UI |
| `completion_estimate` | claim set (no developer date) | Modal: **October / Q4 / December 2026**; CSV Q4 2026 | ≤3 | Own It; Sir Francis; A-list; NRE; GNA; CPK; Flamingo |
| `amenities` (core — official) | **CANONICAL** core | Swimming pool; gym; children’s playing room; rooftop terrace; basement parking (B1–B3); ground parking; security room; gated perimeter | 5 | NEMA |
| `amenities` (multi-agent) | secondary | Heated pool; borehole; full backup generator; CCTV / intercom; high-speed lifts (2/block claimed); BBQ / garden | 3 | Own It; NRE; GNA; Sir Francis; Flamingo |
| `amenities` (inflated) | **`needs_verification`** | Flamingo feature tags (home theater, club house, etc.); NRE “jogging track” | 1 | Flamingo; NRE FAQ |
| `construction_progress` | secondary — **`needs_verification`** | NRE UI “Finishing **88%**”; show house ready (multi-agent) — no developer tracker | 2 | NRE; GNA; Flamingo |
| `legal_title` | unknown | Tenure (freehold/leasehold) **not stated** in NEMA excerpts fetched; proprietor = Riara Plumeria Development Limited | 0 / 5 (owner name) | NEMA |
| `availability_claim` | secondary | Hauzisha “1 unit available” — **`needs_verification`** | 1 | Hauzisha |

### 1a. Price claims — keep **all** options (no canonical)

No developer price list. All bands are agent / marketer claims.

| # | Claim band | Value (KES) | Publisher | Flag |
|--:|------------|-------------|-----------|------|
| A | Modal typed table (105–167 sqm) | 2BR 105 **10.7–12.7M**; 110 **11.2–13.7/13.8M**; 130 all-ensuite **13.7–15.8M** (or from **14.2M**); 3BR 130 **13.7–15.8M**; 167 **17.1–18.9M**; 4BR PH **26.7M**; 5BR PH **28.3M** | NRE; GNA; Flamingo; Sir Francis (upper); Miamu indexed | Secondary |
| B | Own It / A-list “from 10M” band | 2BR from **10M**; 3BR from **13M** / **16M** (160 sqm); Own It **plinth** tags; completion Oct 2026 | ownitkenya.com; A-list | Secondary; matches CSV from |
| C | CPK cash-from list | 105 **10.7M**; 110 **12.2M**; 130 2BR **14.2M**; 130 3BR **13.7M**; 167 **17.1M**; also soft “from 10M / 13M” | commercialpropertykenya.com | Secondary |
| D | Sir Francis dual framing | Table from **10.7M** … PH **28.3M**; body also repeats Own It-style **from 10M / 13M / 16M** | sirfrancismarketingltd.co.ke | Secondary — in-page dual |
| E | UrbanCore higher outliers | 2BR from **12M** / **15M**; 3BR **15M** / **18.5M**; PH **32M** / **35M** | urbancore.co.ke | Secondary — **needs_verification** |
| F | Hauzisha card | Headline **KES 7M** | hauzisha.co.ke | Outlier — **needs_verification** |
| G | CSV seed | `price_from_kes` **10,000,000** | seed | Unverified lead |

**Canonical price:** none.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **30% deposit** + 70% over construction | GNA; Sir Francis; A-list; UrbanCore; CPK; NRE (plan + FAQ text) | **≥4** | **Met via agents** | Must-have field; conf **3** (no developer LOO) |
| **20% deposit** | Flamingo LOO; NRE calculator default (conflicts own FAQ) | 1–2 | Below threshold as canonical | Secondary conflict |
| CPK quarterly **5%** after 30% | CPK only | 1 | Soft | **`needs_verification`** |
| Developer LOO / official schedule | None found | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-riara-plumeria-development` |
| `legal_name` | Riara Plumeria Development Limited |
| `trading_names` | Plumeria Residency; Plumeria Apartments (project brand) |
| `website` | **None found** for the Limited company this pass |
| `evidence` | NEMA EIA Study Report (EIA 2142 SR 3089 / NEMA/TOR/5/2/615): proponent **and** registered proprietor (transferee) of L.R. No. 330/179; P.O. Box 598-00217, Nairobi |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV developer cell **blank** — filled only from NEMA filing |

**Primary developer = Riara Plumeria Development Limited (confidence 5).**

### Developer proposal
Keep **Riara Plumeria Development Limited**. **Do not** treat Hauzisha “Golden Apple” as this project’s developer: Golden Apple Development Co. Ltd has a **separate** NEMA filing on **Nairobi/Block 14/374 (L.R. 330/94)** — different plot/entity.

---

## 3. GroupCompany

**None.** No evidenced parent above Riara Plumeria Development Limited.

---

## 4. RelatedParty

| id | name | relationship_type | Evidence | Conf |
|----|------|-------------------|----------|-----:|
| — | Golden Apple / Golden Apple Development Co. Ltd | **Not linked** (wrong-entity lead) | Hauzisha attributes Plumeria to “Golden Apple”; separate NEMA PDF for Golden Apple on **different** Riara Road plot (330/94) — **do not model as developer or GroupCompany** | 1 (as Plumeria claim) |

No unproven marketing_partner with brand-overlap evidence analogous to Astra/Laureland this pass (Miamu Properties markets the project on LinkedIn as agent/marketer only — listed under Agents).

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Own It Kenya | agency | CSV sales_contact; plinth-tagged prices from 10M | https://ownitkenya.com/property/plumeria-residency-luxury-2-3-bedroom-apartments-for-sale-on-riara-road-kilimani/ |
| NRE Real Estate | agency | Dense listing; Finishing 88%; 30% FAQ vs 20% calculator | https://nairobirealestate.co.ke/properties/plumeria-residency |
| GNA Real Estate | agency | 30% deposit; typed prices; show house | https://gna.co.ke/project/plumeria-residency-riara-road-kilimani-2-and-3-bedrooms/ |
| Sir Francis Homes | agency | Dense typology + Oct 2026 + 30% | https://sirfrancismarketingltd.co.ke/properties/plumeria-residency/ |
| CPK Real Estate | agency | Cash table; 30% + quarterly 5% | https://commercialpropertykenya.com/properties/the-riara-plumeria-residency-apartment-for-sale-in-kilimani/ |
| Flamingo Real Estate | agency | **20%** LOO conflict; penthouse prices | https://www.flamingorealestate.co.ke/property/plumeria-residency-apartments-lavington/ |
| UrbanCore | agency | Higher price outliers; 30% | https://urbancore.co.ke/property/plumeria-residency-234-and-5-bedroom/ |
| A-list Real Estate | agency | 30%; from 10M band; Oct 2026 | https://a-listrealestate.ke/property/plumeria-residency/ |
| Hauzisha | portal | Golden Apple false lead; 7M / 1-unit card | https://hauzisha.co.ke/developments/plumeria-residency/ |
| Miamu Properties Limited | agency / social | Typed Type A–E + PH prices (search-indexed post) | LinkedIn activity-7404097484219748353 |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 722 716 182 | Agent: Own It Kenya (CSV) |
| phone | +254 720 469 282 | Agent: Own It Kenya |
| email | sales@ownitkenya.com | Agent: Own It Kenya (CSV) |
| phone | +254 141 361 320 | Agent: NRE |
| email | info@nairobirealestate.co.ke | Agent: NRE |
| phone | +254 712 406 060 / +254 782 406 060 | Agent: GNA |
| email | support@gna.co.ke | Agent: GNA |
| phone | +254 722 720 812 | Agent: Sir Francis |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 714 737 748 | Agent: Flamingo |
| phone | +254 743 701 113 | Agent: UrbanCore |
| email | sales@urbancore.co.ke / daniel@urbancore.co.ke | Agent: UrbanCore |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 730 731 355 | Portal: Hauzisha |
| postal | P.O. Box 598-00217, Nairobi | Developer: Riara Plumeria Development Limited (NEMA) |

**CSV sales_contact = Own It Kenya agent**, not the developer SPV.

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Dr. Ezekiel Ndunda** (Reg. No. 7867) | other (EIA lead expert) | NEMA document authentication | 5 |
| Unnamed project architect / engineers / contractor | other | NEMA mentions architect provided plans; **no firm names** for builder this pass | 0 |

No financing partner named this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Developer identity** | NEMA **Riara Plumeria Development Limited** vs Hauzisha **Golden Apple** | Canonical = NEMA SPV. Golden Apple = **wrong-entity** (separate NEMA on plot 330/94). |
| 2 | **Neighbourhood label** | NEMA Dagoretti North vs Kilimani / Lavington marketing | Street + plot + GPS **canonical**; labels claim set. |
| 3 | **Deposit** | **30%** (≥4 agents) vs **20%** (Flamingo + NRE calculator) | Must-have **30%** via agent threshold (conf 3). Keep 20% secondary. |
| 4 | **Prices** | From **7M** (Hauzisha) / **10M** (Own It/CSV) / **10.7M** modal / UrbanCore **12M+** / PH up to **35M** | **Keep all** `price_claims[]`. No canonical. |
| 5 | **Penthouses** | Agents market 4/5BR PH; NEMA program text = 2BR & 3BR only | Official unit types = 2/3BR. Penthouses **`needs_verification`**. |
| 6 | **Status / progress** | off_plan vs Finishing 88% vs Dec 2026 “this year” | Claim set; no developer tracker. |
| 7 | **Completion month** | Oct vs Q4 vs Dec 2026 | Soft agent consensus late 2026; no developer date. |
| 8 | **Units per floor phrasing** | 5/floor (agents) vs 20/floor (NEMA) | Reconciles as 5×4 blocks if agents mean per block — record both. |
| 9 | **NRE payment UI** | Calculator 20% vs FAQ/plan 30% | In-page conflict; prefer explicit plan text with other ≥4 agents on 30%. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 candidates (NEMA Plumeria EIA, Own It, NRE, GNA, Sir Francis, CPK, Flamingo, UrbanCore, A-list, Hauzisha, Zyve, Miamu LinkedIn, Westlands Avenue Consult, Golden Apple NEMA on other plot, CSV). **Always kept** official NEMA filing. Retained 10 densest field-bearing sources (≥5 rule).

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://nema.go.ke/wp-content/uploads/2025/03/EIA-2142-SR-3089-PLUMERIA-APARTMENTS-DEVELOPMENT-min.pdf | NEMA / Riara Plumeria Development Limited | official_filing | 2026-10-16 | **Always keep** — 332 units; 4 blocks; 17 floors; GPS −1.2974, 36.7606; plot 330/179 |
| 2 | https://ownitkenya.com/property/plumeria-residency-luxury-2-3-bedroom-apartments-for-sale-on-riara-road-kilimani/ | Own It Kenya | agent | 2026-10-16 | CSV contact; **plinth** sizes; from 10M; Oct 2026 |
| 3 | https://nairobirealestate.co.ke/properties/plumeria-residency | NRE Real Estate | agent | 2026-10-16 | Finishing 88%; typed prices; 30% plan vs 20% calculator |
| 4 | https://gna.co.ke/project/plumeria-residency-riara-road-kilimani-2-and-3-bedrooms/ | GNA Real Estate | agent | 2026-10-16 | 30% deposit; Q4 2026; show house |
| 5 | https://sirfrancismarketingltd.co.ke/properties/plumeria-residency/ | Sir Francis Homes | agent | 2026-10-16 | Dense table to PH 28.3M; 30%; Oct 2026 |
| 6 | https://commercialpropertykenya.com/properties/the-riara-plumeria-residency-apartment-for-sale-in-kilimani/ | CPK Real Estate | agent | 2026-10-16 | Cash table; 30% + quarterly 5% |
| 7 | https://www.flamingorealestate.co.ke/property/plumeria-residency-apartments-lavington/ | Flamingo Real Estate | agent | 2026-10-16 | **20%** conflict; Type A–E + PH |
| 8 | https://urbancore.co.ke/property/plumeria-residency-234-and-5-bedroom/ | UrbanCore | agent | 2026-10-16 | Higher price outliers; 30% |
| 9 | https://a-listrealestate.ke/property/plumeria-residency/ | A-list Real Estate | agent | 2026-10-16 | 30%; from 10M band; Oct 2026 |
| 10 | https://hauzisha.co.ke/developments/plumeria-residency/ | Hauzisha | portal | 2026-10-16 | Golden Apple false lead; 7M / 1-unit card |

### Evaluated but not retained (thin / wrong entity / overlap)

| url | Why skipped |
|-----|-------------|
| https://zyveafrica.co.ke/index.php/property/kilimani-riara-road-off-plan-5-4-3-2-bedroom-apartments/ | Fetch timeout; overlaps retained price tables |
| https://www.linkedin.com/posts/miamu-properties-limited_miamuproperties-plumeriaresidency-luxuryliving-activity-7404097484219748353-tVP9 | Fetch timeout; price card covered by retained agents |
| https://westlands-consult.co.ke/property/apartment/plumeria-residency-kilimani-nairobi-apartments-for-sale/ | Template placeholders (“Insert Developer Name”) — thin |
| https://nema.go.ke/wp-content/uploads/2025/12/Golden-Apple-Development-Co.-Limited_00267-min.pdf | **Wrong project** (plot 330/94 / Block 14/374) — evaluated only to reject Hauzisha merge |
| CSV NBO-015 row | Lead only |

---

## 9. Field harvest → must-have extension proposals

| Proposed / reinforced field | Plumeria evidence | Consensus note |
|----------------------------|-------------------|----------------|
| Official **EIA/NEMA filing** when no microsite | Full program + GPS + SPV | Reinforce (with Riara Oasis / Berkeley pattern) |
| `total_units` + `block_count` | **332** / **4** on NEMA | Strengthen propose-must |
| Developer-sourced `lat_lng` | NEMA **−1.2974, 36.7606** | Bump GPS propose when official |
| `size_measure_tag` **plinth** | Own It “Plinth area” | Rare agent-side tag — capture |
| Payment via **≥4 agents** without developer LOO | **30%** met; conf 3 | Pattern holds |
| Wrong-entity developer leads | Golden Apple ≠ this SPV | Capture + reject merge (like Procmura/Berkeley) |
| Penthouses absent from official unit text | Agent 4/5BR PH | Show + **`needs_verification`** |
| `construction_progress` agent UI only | NRE 88% | Not developer tracker — keep soft |

---

## Open questions (developer / verification pass)

1. Binding LOO: **30%** vs Flamingo/NRE-calculator **20%**?  
2. Are **4/5BR penthouses** in the approved scheme or marketing-only?  
3. Current contractual **completion** (Oct vs Dec 2026) and true construction %.  
4. Legal **tenure** (freehold/leasehold) and plot area in title docs.  
5. Named main **contractor** / architect firm.  
6. Any real link between **Riara Plumeria Development Limited** and marketed “Golden Apple” brands (beyond Hauzisha error)?
