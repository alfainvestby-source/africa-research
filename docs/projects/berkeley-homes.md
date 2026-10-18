---
slug: berkeley-homes
external_id: NBO-010
cycle: scale-half
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Berkeley Homes (NBO-010)

CSV seed (unverified leads): location Kileleshwa, Nairobi; stage `under_construction`; completion blank; `price_from_kes` 4,200,000; sales_contact NRE Real Estate; developer “Procmura”.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer known and developer/official sources **agree** → **canonical = developer/official**; agents secondary.
- **Official vs official** disagreements → **`needs_developer_input`**; no assumed winner.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- Payment must-have if any developer source **or** ≥4 independent agent/portal sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**. CSV = unverified leads only.
- Scan ~10; retain ≥5 densest; always keep project marketing site + official NEMA ESIA PDF.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer/official-backed when sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official materials disagree or marketing name vs ESIA identity needs developer confirmation.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** (marketing consensus) | Berkeley Homes | 4 | berkelyresidence.com (“Berkeley”); Block; NRE; Space; Ravi; multi-agent |
| `aliases` | secondary | Berkeley Homes Apartments; Berkeley Residence / Berkeley Homes Residency; Berkely (domain spelling berkelyresidence.com) | 3 | Foresee; Ravi; project domain |
| `status` | claim set | CSV/`under_construction`; Space footage Jan–Sep 2026; NRE “Under Construction” + **58%** progress estimate; agents “off-plan / construction ongoing” | 4 | Space; NRE; Block; CSV |
| `geography.city` | **CANONICAL** | Nairobi | 5 | ESIA; marketing site; agents |
| `geography.neighbourhood_street` | **CANONICAL** | Kileleshwa — **Oloitoktok Road** / Kirichwa Creek access; Dagoretti North Sub-County | 5 | ESIA; berkelyresidence.com; Block; NRE; Ravi |
| `geography.plot` | **CANONICAL** (ESIA) | **L.R. Nairobi/Block 23/895**; ~**0.1983 ha**; adjacent Hillgate Court / Kieni (ESIA neighbours) | 5 | NEMA ESIA |
| `geography.lat_lng` | **CANONICAL** (ESIA fact sheet) | **−1.28050, 36.78997** | 5 | NEMA ESIA fact sheet (note: body text once swaps lat/long labels — fact sheet used) |
| `geography.lat_lng` | secondary | −1.2814, 36.7897 | 3 | Nefroon map |
| `primary_developer_id` | **CANONICAL** (legal proponent + portal attribution) | → `dev-rarlon-estate-development` | 4 | NEMA ESIA; NRE; Nefroon — see §2 (marketing site silent; ESIA omits marketing name) |
| `unit_types` | **CANONICAL** (types agree) | Studio; 1 Bedroom; 2 Bedroom | 5 | ESIA mix; berkelyresidence.com; agents |
| `unit_mix_counts` | claim set — **`needs_developer_input`** vs agent 360 | ESIA: Studio **38**; 1BR **152**; 2BR **171** (= **361**) | 4 | NEMA ESIA |
| `total_units` | claim set — **`needs_developer_input`** | Official ESIA **361** vs agent/portal consensus **360** (Space, Craiova, NRE, Nefroon, East Properties, GNA, Ravi) | 2 | Official vs marketing consensus — **no assumed winner** |
| `building_specs.storeys` | **CANONICAL** (agree) | **19** residential storeys / floors | 5 | ESIA; Space; NRE; Ravi; Craiova; multi-agent |
| `building_specs.parking_levels` | **CANONICAL** (agree on 4 levels) | **4** parking levels — ESIA: Basement −3/−2/−1 (48 bays each) + Ground (53 bays) | 5 | ESIA; Space; agents “4 parking levels” |
| `building_specs.wings_blocks` | secondary — **`needs_verification`** | Sir Francis: **two towers** Block A & B, 19 floors apiece. ESIA describes **one** 19-storey residential block with typical floors. Nefroon unit labels use A/B apartment codes (not proven as two towers) | 2 | Sir Francis vs ESIA |
| `size_by_type` | secondary (agent tables; no ESIA sizes) | Studio ~**40–46** (floor plans ~39.76–46) sqm; 1BR ~**48–65** (plans ~48.6–64.84); 2BR ~**73–101** (plans ~73.69–100.77) sqm | 3 | Block; Realtors.co.ke floor plans; Ravi; Craiova; Foresee |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched | 0 | — |
| `price_claims[]` | claim set — **keep all**; no canonical | See §1a | ≤3 | |
| `currency` | **CANONICAL** | KES | 5 | all commercial sources |
| `payment_plan.deposit` | **must-have** (agent ≥4; **no developer payment page**) | **20% deposit** to secure / on booking | 3 | Block; Ravi; Vorsa; GNA; Realtors.co.ke; NRE; Sir Francis |
| `payment_plan.balance` | secondary soft | Balance over remaining construction / up to completion; Vorsa “up to 36 months”; Sir Francis detailed cash + staged instalment schedule | 3 | multi-agent — exact LOO unknown |
| `completion_estimate` | secondary consensus — **`needs_verification`** (no developer schedule page) | **April 2028** / **Q2 2028** | 3 | Block; Space; NRE; Craiova; East Properties; GNA; Realtors |
| `amenities` (core) | **CANONICAL** where ESIA + marketing agree | Rooftop / roof **swimming pool**; **gym**; **restaurant** / café; common/lounge spaces; garden; borehole (ESIA recommends onsite); backup generator; parking; security/CCTV (ESIA EMP) | 5 | ESIA roof plan + utilities; berkelyresidence.com |
| `amenities` | secondary marketing extras | Patio gaming zone / pool table area; kids play; terrace deck; courtyard; high-speed lifts; smart lock; reception; telecom — on marketing site / agents; kids play not named on ESIA roof list | 3–4 | berkelyresidence.com; agents |
| `amenities` | inflated — **`needs_verification`** | Sir Francis: co-working, solar water heating, air conditioning, “all ensuite”, wooden flooring as amenity list items — not on ESIA/marketing core | 1 | Sir Francis only |
| `construction_progress` | secondary — **`needs_verification`** | NRE backend **58%**; Space “Under construction” with footage dated Jan 2026–Sep 2026. No developer construction tracker found | 2 | NRE; Space |
| `legal_title` / plot tenure | secondary (ESIA) | Leasehold to Rarlon Estate Development Company Limited (ESIA statement) | 4 | NEMA ESIA |
| `project_cost_claim` | secondary | ESIA BQ **KES 810,000,000** | 4 | NEMA ESIA |
| `csv_developer_lead` | reject as developer | “Procmura” = **PROCMURA** NGO (Programme for Christian-Muslim Relations in Africa, Westlands/Kileleshwa office). NRE developer hub links PROCMURA to a **Berkeley Residency** groundbreaking news item — **different project** (Westlands). Not the Berkeley Homes developer | 1 | NRE developers; PROCMURA public sites; CSV |

### 1a. Price claims — keep **all** options (no canonical)

No developer price list on berkelyresidence.com or in ESIA. All commercial figures are agent/portal.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Block typed list (matches GNA / Realtors / NRE) | Studio 40 sqm **KES 4.2M**; 1BR 50 **5.3M** / 60 **6.23M**; 2BR 73 **6.5M** … 101 **9.39M** | block.ke | Secondary |
| B | Ravi typed table | Studio from **KES 4.25M** (40/46/50); 1BR from **5M**; 2BR from **6.95M** (to ~9.3M) | ravihomes.co.ke | Secondary |
| C | Craiova / Foresee bands | Studio from **4.2M**; 1BR from **5.11M**; 2BR from **7.15M** / **9.21M** | Craiova; Foresee | Secondary |
| D | Vorsa “from” | Studio from **KES 3.99M**; 1BR from **6.23M**; 2BR from **7.15M** | vorsagroup.co.ke | Secondary — **needs_verification** (outlier low) |
| E | Sir Francis entry | Studio from **KES 3.7M**; 1BR from **4.7M**; 2BR from **6.3M** | sirfrancismarketingltd.co.ke | Secondary — **needs_verification** (outlier low; also two-tower claim) |
| F | Nefroon range | Starting from **KES 4,980,000** to **9,510,000** | nefroonhomes.com | Secondary — conflicts with 4.2M “from” |
| G | CSV seed | `price_from_kes` **4,200,000** | seed | Unverified lead |

**Canonical price:** none. Always `price_claims[]`.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **20% deposit** | Block; Ravi; Vorsa; GNA; Realtors.co.ke; NRE; Sir Francis | **≥4** agents | **Met via agents** | Must-have at conf **3** (no developer payment page) |
| Balance over construction / to completion | Multi-agent soft language | ≥4 vague | Soft secondary | Exact LOO unknown |
| Sir Francis staged % schedule | Sir Francis only | 1 | — | **needs_verification** |
| Vorsa “up to 36 months” | Vorsa only | 1 | — | **needs_verification** |
| Developer LOO / payment PDF | Not found on berkelyresidence.com this pass | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-rarlon-estate-development` |
| `legal_name` | **Rarlon Estate Development Company Limited** |
| `trading_names` | Rarlon Estate Development; Rarlon Estate Developers (NRE/Hauzisha styling) |
| `website` | No independent developer corporate site confirmed this pass. Project marketing: https://berkelyresidence.com/ (does **not** name legal developer in fetched copy) |
| `evidence` | (1) **NEMA ESIA** (Oct 2025) names Rarlon Estate Development Company Limited as proponent for 19-storey / 361-unit apartments on Nairobi/Block 23/895, Oloitoktok Road, Kileleshwa — GPS −1.28050, 36.78997; roof amenities match marketing. ESIA title does **not** say “Berkeley Homes”. (2) NRE property page: “Rarlon Estate Developers is identified as the project developer.” (3) Nefroon developer profile attributes Berkeley Homes Kileleshwa to Rarlon Estate Development. |
| `group_company_id` | **null — none invented** |
| `csv_name_note` | CSV “Procmura” is a **false lead** (NGO PROCMURA; NRE links it to Berkeley **Residency** Westlands news). Do **not** set as developer. |
| `identity_gap` | Marketing site silent on legal name; ESIA silent on “Berkeley Homes” brand → developer–project link confidence **4**, not 5. Flag for advocate/title confirmation. |

**Primary developer = Rarlon Estate Development Company Limited (confidence 4).**

---

## 3. GroupCompany

**None.** No evidenced parent above Rarlon.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Conf |
|------|-------------------|----------|-----:|
| PROCMURA (Programme for Christian-Muslim Relations in Africa) | **not linked** (CSV trap) | CSV developer cell; NRE “Procmura” profile describes NGO + Berkeley **Residency** groundbreaking news — wrong project | 1 |

No `marketing_partner` / GroupCompany invented from Berkeley Residency brand overlap. Separate Westlands project (Berkeley Residency / Rhapta) also attributed to Rarlon on Nefroon/Hauzisha — **out of scope** for NBO-010 except as developer portfolio context.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| NRE Real Estate | agency | CSV sales_contact; dense buyer guide; Rarlon attribution; 20%; 58% progress | https://nairobirealestate.co.ke/properties/berkeley-homes |
| Block Real Estate | agency | Typed price list; April 2028; 20% | https://block.ke/property/berkeley-homes-apartments-luxury-living-redefined/ |
| Ravi Homes | agency | Typed prices; 20%; 360/19 | https://ravihomes.co.ke/developments/berkeley/ |
| VorsaGroup Real Estate | agency | Price bands; 20% / 36 mo; brochure PDF link | https://vorsagroup.co.ke/property/berkeley-homes-1-2-bedroom-apartments-for-sale-in-kileleshwa/ |
| Craiova Realtors | agency | Price bands; 360/19; April 2028 | https://craiovarealtors.com/property/elegant-apartments-in-kileleshwa-studios-1-2-br/ |
| Foresee Realtors | agency | “Berkeley Residence” alias; overlapping bands | https://foreseerealtors.com/portfolio/berkeley-residence-kileleshwa/ |
| Space Kenya | portal | Construction footage; 360/19; April 2028 | https://space.ke/projects/berkeley-homes/ |
| Nefroon | portal | Rarlon attribution; GPS; price from ~4.98M | https://nefroonhomes.com/projects/berkeley-homes-2957aa6f |
| GNA Real Estate | agency | Price table twin of Block; 20% | https://gna.co.ke/project/berkeley-homes-kileleshwa-studios-1-and-2-bedrooms/ |
| Sir Francis Marketing | agency | Outlier prices; two-tower claim; detailed instalment % | https://sirfrancismarketingltd.co.ke/properties/berkeley-homes/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| url | https://berkelyresidence.com/ | Property marketing site |
| url | NEMA ESIA PDF (see Sources #1) | Official / proponent filing |
| phone | +254 113 222 666 (0113222666) | Listed as “Call Developer” on Nefroon project card — **needs_verification** (aggregator) |
| phone | +254 729 869 849 | Nefroon Rarlon developer profile “Call Office” — **needs_verification** |
| email | zendrychebayi20@gmail.com | Nefroon Rarlon / project enquiry — **needs_verification** (aggregator) |
| phone | +254 141 361 320 | Agent: NRE (CSV) |
| email | info@nairobirealestate.co.ke | Agent: NRE (CSV) |
| phone | +254 725 937 686 | Agent: Block (Loyd Mokaya) |
| email | loyd@block.ke | Agent: Block |
| phone | +254 105 772 200 | Agent: Ravi Homes |
| email | sales@ravihomes.co.ke | Agent: Ravi Homes |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: VorsaGroup |
| email | info@vorsagroup.co.ke | Agent: VorsaGroup |
| phone | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |
| phone | +254 743 555 777 / +254 743 101 010 | Agent: Foresee |
| email | info@foreseerealtors.com | Agent: Foresee |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Green Builders & Planning Consultants Limited** | other (EIA firm of experts) | NEMA ESIA cover / fact sheet — NEMA Firm Reg No. 9571; contact 0704 707 633 | 4 |

No financing partner / main contractor / architect named on marketing materials this pass. ESIA recommends borehole + backup generator (utility design, not named vendors).

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Developer identity** | CSV **Procmura** vs ESIA/NRE/Nefroon **Rarlon Estate Development Company Limited** vs silent marketing site | CSV = false lead (NGO). Canonical developer = **Rarlon** (conf 4). Marketing silence + ESIA missing brand name → advocate confirm. |
| 2 | **Total units** | ESIA **361** vs agents/portals **360** | **Official vs marketing** → treat as claim set; prefer ESIA for legal description but **do not silence** 360; flag **`needs_developer_input`** for sales inventory count. |
| 3 | **Prices** | 3.7M / 3.99M / 4.2M / 4.25M / 4.98M “from” bands | **Keep all** `price_claims[]`. No canonical. Outliers D/E **needs_verification**. |
| 4 | **Towers** | Sir Francis two×19-storey towers vs ESIA single 19-storey block | Agent claim **needs_verification**; ESIA structure description preferred for building form until contradicted by developer drawings. |
| 5 | **Completion** | April / Q2 2028 multi-agent; no developer schedule page | Secondary consensus conf 3; not developer-canonical. |
| 6 | **Payment duration** | Soft “to completion” vs Vorsa 36 months vs Sir Francis staged % | 20% deposit locked via ≥4 agents; schedules secondary. |
| 7 | **CSV sales_contact** | NRE ≠ Nefroon “developer” phones | Split Contact.owner correctly. |
| 8 | **Berkeley Residency (Westlands)** | Separate Rarlon-attributed project on Rhapta | **Do not merge** into NBO-010. |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned project marketing site, NEMA ESIA PDF, NRE property + developer hub, Block, Space, Ravi, Nefroon project + developer, Vorsa, Craiova, Foresee, GNA, Sir Francis, East Properties, Realtors.co.ke, PROCMURA/CSV trap pages. **Always kept** berkelyresidence.com + NEMA ESIA. Retained 10 richest (≥5 rule).

**Thin / skipped (not in retained list):**
- https://eastproperties.co.ke/property/berkeley-homes-kileleshwa/ — overlaps Craiova amenity/rent copy; thinner commercial table
- https://realtors.co.ke/property/berkeley-homes-stylish-studio-1-2-bedroom-apartments-in-kileleshwa-nairobi/ — near-duplicate of GNA/Block price table (used for floor-plan size corroboration notes only)
- https://nairobirealestate.co.ke/developers — Procmura/Rarlon hub stubs; evaluated for CSV trap, not retained as project source
- https://berkeleyresidence.weebly.com/contact.html — **wrong entity** (non-Kenya contact)
- CSV NBO-010 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://nema.go.ke/wp-content/uploads/2025/12/SR-00234-ESIA-RESIDENTIAL-KILELESHWA.pdf-Rarlon-Estate-Development-Company-Limited-min.pdf | NEMA / Rarlon Estate Development Company Limited (proponent) | official_esia | 2026-10-16 | Legal name; 19 storeys; **361** units; plot; GPS; roof amenities; parking; **always keep** |
| 2 | https://berkelyresidence.com/ | Berkeley marketing site | project_site | 2026-10-16 | Amenities; Kileleshwa; no legal developer name; domain spelling Berkely — **always keep** |
| 3 | https://nairobirealestate.co.ke/properties/berkeley-homes | NRE Real Estate | agent | 2026-10-16 | Rarlon attribution; prices; 20%; April 2028; 58% progress; CSV channel |
| 4 | https://block.ke/property/berkeley-homes-apartments-luxury-living-redefined/ | Block Real Estate | agent | 2026-10-16 | Full typed price list; 20%; April 2028 |
| 5 | https://space.ke/projects/berkeley-homes/ | Space Kenya | portal | 2026-10-16 | UC footage; 360/19; April 2028 |
| 6 | https://ravihomes.co.ke/developments/berkeley/ | Ravi Homes | agent | 2026-10-16 | Typed prices; 20%; Kirichwa Creek |
| 7 | https://nefroonhomes.com/projects/berkeley-homes-2957aa6f | Nefroon | portal | 2026-10-16 | From ~4.98M; GPS; developer link |
| 8 | https://nefroonhomes.com/developers/rarlon-estate-29ffe458 | Nefroon | portal | 2026-10-16 | Rarlon ↔ Berkeley Homes attribution; contacts |
| 9 | https://vorsagroup.co.ke/property/berkeley-homes-1-2-bedroom-apartments-for-sale-in-kileleshwa/ | VorsaGroup | agent | 2026-10-16 | 3.99M from; 20%/36 mo; brochure CTA |
| 10 | https://craiovarealtors.com/property/elegant-apartments-in-kileleshwa-studios-1-2-br/ | Craiova Realtors | agent | 2026-10-16 | 360/19; price bands; April 2028 |

**Corroboration-only (not retained):** GNA (Block twin); Sir Francis (conflicts); Foresee (Craiova twin); East Properties.

---

## 9. Field harvest

| Field | Berkeley Homes status | Notes for living schema |
|-------|----------------------|-------------------------|
| canonical_name / aliases | OK | Domain spelling Berkely ≠ brand Berkeley |
| status | OK as claim set | UC + Space footage |
| geography street + plot + lat_lng | **Strong** | ESIA plot + GPS — promote GPS when official |
| primary_developer | OK at conf 4 | Rarlon; CSV Procmura rejected |
| GroupCompany | none | Correctly empty |
| `total_units` | Claim set + **`needs_developer_input`** | **361 ESIA vs 360 agents** — reinforces C2 unit_count proposal |
| `storeys` | OK canonical 19 | ESIA + agents agree |
| `parking_levels` / bay counts | **New harvest** | ESIA 3×48 + 53 bays — propose capture when ESIA/approvals publish |
| `unit_mix_counts` by typology | **New harvest** | ESIA 38/152/171 — propose when official |
| `price_claims[]` | All options retained (A–G) | No developer price list |
| `payment_plan` | **20%** must-have via ≥4 agents | No developer payment page → conf capped at 3 |
| amenities core | OK | ESIA roof + marketing overlap |
| completion_estimate | Agent consensus April/Q2 2028 | Not developer-canonical |
| `construction_progress` | Agent-only 58% | Candidate field; needs developer tracker |
| Named EIA consultant | Captured | Green Builders & Planning Consultants Limited |
| Wrong-CSV developer trap | Documented | PROCMURA NGO ≠ developer |

### Proposed schema bumps (for coordinator — not auto-locked)

| Proposed extension | This project | Consensus note |
|--------------------|--------------|----------------|
| `total_units` claim set | **Yes** (361 vs 360) | Aligns C2 Galaxy/Porini |
| Official ESIA / approvals as Source.type | **Yes** | High-value when marketing site thin |
| `unit_mix_counts` (studio/1BR/2BR) | **Yes** when ESIA/approvals | |
| `parking_bays` / `parking_levels` | **Yes** when ESIA | |
| Reject CSV developer when NGO/wrong-project | Process note | Procmura trap |

---

## Open questions (developer / advocate input)

1. Confirm marketing name **Berkeley Homes** maps 1:1 to ESIA plot **Nairobi/Block 23/895** / Rarlon Estate Development Company Limited.
2. Sales inventory: **360 or 361** units?
3. Publish current LOO price list and binding deposit % (agent 20% unverified against developer).
4. One tower vs Sir Francis two-tower claim — share approved drawings.
5. Corporate site / official sales phones beyond Nefroon aggregator contacts?
6. Gross vs plinth size tags; Vorsa brochure PDF contents?
