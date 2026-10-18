---
slug: longines-bay-kilimani
external_id: NBO-008
cycle: scale-half
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Longines Bay Kilimani (NBO-008)

CSV seed (unverified leads): location “Karbanet Road, off Ngong Road, Kilimani, Nairobi”; stage `off_plan`; completion **2029**; `price_from_kes` **3,700,000**; sales_contact Loyd Mokaya / Ricky Wekesa (Block Real Estate), +254 725 937 686; developer “Nanchong International”.

Live research accessed **2026-10-16**. Replaces earlier thin Wave B stub (no official microsite found then).

**Method locks applied:**
- Developer vs agents: if developer known and developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** (developer marketing vs NEMA filing, or disagreeing developer pages): **do not assume** → **`needs_developer_input`**.
- Prices: always keep **all** options in `price_claims[]` (no single scalar).
- Payment must-have if any developer source **or** ≥4 independent agent/portal sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**. CSV = unverified leads only.
- Scan ~10; retain ≥5 densest; **always keep** developer/official project site.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer-backed when developer sources **agree**. Claim set / secondary = kept for conflict detection. **`needs_developer_input`** = official materials disagree — no winner assumed.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Longines Bay | 5 | longinesbay.com; Block; multi-agent |
| `aliases` | secondary | Longines Bay Kilimani; Longines Bay Apartments; Longines Bay Residences; **Logines Bay** (Craiova typo) | 4 / 2 | Block; NRE; Craiova |
| `status` | claim set | Developer FAQ: **construction underway**; homepage **off-plan** framing; CSV `off_plan`; agents **under construction**; contact page **“Launching 2026”** (sales framing) | 4 | longinesbay.com FAQ/contact; CSV; NRE; Craiova |
| `geography.city` | **CANONICAL** | Nairobi | 5 | longinesbay.com; NEMA summary |
| `geography.neighbourhood_street` | **CANONICAL** (street presence) | **Karbanet Road** / **Kabarnet Road**, off Ngong Road (Kilimani / Kibra planning area in news) | 5 | longinesbay.com (both spellings); NEMA/Vellum **Kabarnet**; agents |
| `geography.landmark` | secondary | Near Sudan Embassy (agents + CPK “official brochure”) | 3 | CPK; Block travel table; agents |
| `geography.lat_lng` | geocode — **needs_verification** (recommended) | **−1.303258, 36.788463** (`geo_method=geocode`) | 2 | Nominatim Kabarnet Road 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `geography.lat_lng` | developer JSON-LD — **`needs_verification`** (not recommended) | **−1.3635, 36.7719** (longinesbay.com schema) | 2 | Far south of Kabarnet/Ngong grid — reject as map default; do not invent a correction |
| `primary_developer_id` | **CANONICAL** (legal Kenya SPV) | → `dev-nanchong-longines-bay-limited` | 5 | NEMA/Gazette + Kenya Times |
| `developer_trading` | **CANONICAL** (marketing agree) | **Nanchong International** / **Nanchong China** (African debut of residential portfolio) | 5 | longinesbay.com home/about; Block |
| `unit_types` | **CANONICAL** | Studio; 1 Bedroom; 2 Bedroom; Premium 3- & 5-bedroom duplexes; retail/commercial; hotel-managed investment units (**Block 2** only) | 5 | longinesbay.com residences + FAQ |
| `size_by_type` | **CANONICAL** (developer residences + FAQ **agree**) | Studio **39–48 sqm**; 1BR **72 sqm**; 2BR **87–94 sqm**; duplex **132–179 sqm** | 5 | longinesbay.com/residences; FAQ |
| `size_by_type` | secondary — **needs_verification** | Agent tables: 3BR duplex **142 sqm** (vs official **132**); 5BR **174–187** (vs official **176–179**); Mestates 3BR **132** / 5BR **176–179** (closer to official) | ≤3 | Vorsa; Block; Sir Francis; Craiova; Mestates |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched | 0 | — |
| `total_units` / `block_count` | claim set — **`needs_developer_input`** | NEMA / Gazette / Kenya Times: **three 18-storey blocks**, **601 apartments**. Marketing site: singular **18-storey** mixed-use on **1.5-acre** site — **does not publish 601 or three blocks** | 2 | Official filing vs official marketing — **no assumed winner** |
| `building_specs.storeys` | claim set — **`needs_developer_input`** | Marketing + agents + NEMA: **18 storeys** (16 residential + 2 commercial on marketing). Journal construction post: **“24th floor” topping out** — conflicts with 18 | 2 | Official vs official — **no assumed winner**; 24th also **`needs_verification`** (possible placeholder copy) |
| `building_specs.site_acres` | **CANONICAL** (marketing agree across pages) | **1.5 acres** | 5 | longinesbay.com; Block; NRE |
| `building_specs.landscaped_acres` | secondary — **needs_verification** | ~**0.9 acres** landscaping/gardens | 2 | CPK only (“developer setting aside”) |
| `price_claims[]` | claim set — keep **all**; developer residences bands are strongest but **not** collapsed to one scalar | See §1a | ≤5 | |
| `currency` | **CANONICAL** | KES | 5 | all commercial sources |
| `payment_plan` | **CANONICAL** (developer FAQ) | **Staged construction-linked payment plans** for registered buyers; financing introductions on request | 5 | longinesbay.com FAQ |
| `payment_plan.deposit_pct` | secondary — **needs_verification** | Agent/portal claim **20% / 50% / 100%** cash tiers (CPK “latest developer pricing”); NRE calculator min **20%** | ≤3 | Only **2** independent agent sources — **below ≥4** threshold for agent must-have |
| `completion_estimate` | **CANONICAL** (developer FAQ + homepage KPI agree on 2029) | **Q4 2029** anticipated handover (FAQ); homepage KPI **2029** Anticipated Handover; multi-agent **2029** | 5 | longinesbay.com; Block; Vorsa; Craiova; NRE; CSV |
| `completion_estimate` | secondary soft conflict | Contact page **“Launching 2026”** (sales/show-suite framing, not clearly handover) | 2 | longinesbay.com/contact |
| `amenities` (core) | **CANONICAL** | Official **15**: swimming pool; indoor cinema; outdoor cinema (+ BBQ); sky padel; wellness gym; co-working; coffee lounge; pool room; pet-friendly facilities; sky golf; fingerprint door locks; 24-hour laundry; premium hotel restaurant; indoor children’s playroom; 24/7 CCTV | 5 | longinesbay.com/amenities |
| `amenities` | secondary / inflated — **needs_verification** | FAQ wording **“Olympic swimming pool”** (amenities page = “full-length”); agents add **borehole**, **backup generator**, fingerprint access already on official, “sports centre” umbrella | ≤3 | FAQ vs amenities page mild wording; borehole/generator agent-only vs core 15 |
| `hotel_managed_program` | **CANONICAL** (presence + caveats) | Block 2 only; **5-year** income arrangement; targeted **~11% ROI**; subject to applicable agreement | 5 | longinesbay.com home/FAQ |
| `retail` | **CANONICAL** | Shops **27–180 sqm**; commercial “World Food Avenue”; indicative rates from **KES 223 / sq.ft** (GF) / **178 / sq.ft** (1F) | 5 | longinesbay.com FAQ + commercial |
| `construction_progress` | secondary — **needs_verification** | NRE UI **“Under Construction 58%”** — not on developer tracker | 1 | NRE only |
| `availability_claim` | unknown | — | 0 | no inventory counts on developer |
| `legal_title` | unknown | — | 0 | not found |
| `nema_ref` | claim (filing) | **NEMA/ENVIS/SR/00719** — residential cum commercial, Kabarnet Road off Ngong Road, Kibra | 4 | Vellum Gazette summary |

### 1a. Price claims — keep **all** options (no canonical scalar)

Developer residences page publishes typed bands (strongest). Agent tables often match studios/1BR but diverge on 2BR floors/prices and duplex sizes. Sir Francis listing header **KES 3.5M** conflicts with body **3.7M**. CSV matches studio-from **3.7M**.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Developer residences — studios | 39 sqm **3.7–4.5M**; 40 furnished **4.5–4.9M**; 48 furnished **5.3–5.8M** | longinesbay.com/residences | Official |
| B | Developer residences — 1BR | 72 sqm **6.7–7.7M** | longinesbay.com/residences | Official |
| C | Developer residences — 2BR | 87 **8.5–9.4M**; 89 **8.82–10.3M**; 94 **8.9–10.5M**; 94 furnished **9.9–10.9M** (page also summarizes **8.5–10.9M**) | longinesbay.com/residences | Official — note **89 sqm** layout (agents often say **88**) |
| D | Developer residences — duplex | 3BR **132 sqm from 16.1M**; 5BR **176–179 sqm from 21M** | longinesbay.com/residences | Official |
| E | Developer meta / FAQ “from” | **KES 3.7M+** / studios from **3.7M** | JSON-LD; FAQ | Official |
| F | Agent consensus table (studio/1BR/2BR/duplex) | Studios same as A; 1BR **6.7–7.7M**; 2BR **87: 8.7–9.6M**; **88: 8.9–10.6M**; **94: 8.9–11.1M**; 3BR duplex **142 sqm from 16M**; 5BR **174–187 from 21M** | Block; Vorsa; Sir Francis; CPK; Craiova (partial) | Secondary — **2BR & duplex sizes/prices diverge from C/D** → **`needs_verification`** as “current” |
| G | Sir Francis header | From **KES 3,500,000** | sirfrancismarketingltd.co.ke | Secondary — conflicts with 3.7M body / official → **`needs_verification`** |
| H | CSV seed | `price_from_kes` **3,700,000** | seed | Unverified lead (matches official from) |
| I | Commercial rates | GF from **KES 223/sq.ft**; 1F from **178/sq.ft**; spaces **291–9,687 sq.ft** | longinesbay.com/commercial | Official commercial (indicative) |

**Canonical price:** none as a single portal scalar. Prefer developer bands A–E when citing “developer-backed”; retain F–H as alternate claims.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| Staged / construction-linked plans | longinesbay.com FAQ (+ soft “flexible” on Sir Francis) | Developer **≥1** | **Met via developer** | **CANONICAL must-have** (exact schedule unknown) |
| **20% / 50% / 100%** tier discounts | CPK (explicit); NRE calculator (min 20%) | **2** agents | Below ≥4 | Secondary · **`needs_verification`** |
| Binding LOO / full schedule PDF | Not published on site (brochure CTA / enquire) | 0 usable | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-nanchong-longines-bay-limited` |
| `legal_name` | **Nanchong Longines Bay Limited** |
| `trading_names` | Nanchong International; Nanchong China; Longines Bay (project brand) |
| `website` | https://longinesbay.com/ |
| `evidence` | NEMA public-comment summary (Vellum / Kenya Times) names SPV as proponent; longinesbay.com “African debut of Nanchong International”; About “By Nanchong China” |
| `group_company_id` | → `grp-nanchong-group` (see §3) |
| `csv_name_note` | CSV “Nanchong International” = **trading name lead** — matches marketing; legal Kenya entity from NEMA is **Nanchong Longines Bay Limited** |
| `prior_projects_mentioned` | About: **17** projects; **13,000+** units; **3.06M m²**; landmark **Jiangshan Yin** (~3,200 units) — China portfolio credentials **unverified this pass** (`needs_verification`) |

**Primary developer = Nanchong Longines Bay Limited (confidence 5 for legal identity).** Marketing brand = Nanchong International / Nanchong China.

---

## 3. GroupCompany

| Field | Value |
|-------|-------|
| `id` | `grp-nanchong-group` |
| `name` | Nanchong Group (also styled Nanchong China on site) |
| `website` | Presented via https://longinesbay.com/about (no separate group URL fetched) |
| `evidence` | About page: founded **2010** Fuzhou, Jiangxi; HQ **Nanchang**; portfolio real estate / construction / hotels; Longines Bay framed as African residential debut |

Parent relationship is **developer-stated** on the project site (conf **4**). Do not invent additional holding companies.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Notes |
|------|-------------------|----------|-------|
| **Nanchong Longines Island Limited** | related_filing_entity (not this property) | Same Kenya Times / Vellum Gazette wave — **Westlands Avenue**, 19-storey / 152 units | **Different project** — do not merge into NBO-008 |

No unproven marketing_partner analogous to Astra/Laureland.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate | agency | CSV sales_contact; dense snapshot + price table | https://block.ke/property/longines-bay-kilimani-apartments-for-sale-off-ngong-road/ |
| CPK Real Estate | agency | Dense amenities + **20/50/100%** payment claim; brochure language | https://commercialpropertykenya.com/properties/longines-bay-apartments-off-ngong-road-nairobi/ |
| VorsaGroup Real Estate | agency | Full typed price table; 2029 | https://vorsagroup.co.ke/property/longines-bay-apartments-studio-1-2-duplex-off-ngong-road/ |
| NRE Real Estate | agency | Price bands; payment calculator; **58%** progress UI | https://nairobirealestate.co.ke/properties/longines-bay-residences |
| Sir Francis Marketing Ltd | agency | Price table; “from 3.5M” header conflict | https://sirfrancismarketingltd.co.ke/properties/longines-bay/ |
| Craiova Realtors | agency | “Logines” typo; studio-focused; 2029 | https://craiovarealtors.com/property/studios-1-2-br-apartments-at-logines-bay-kilimani/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 101 666 888 | Property sales gallery (developer site) |
| email | longinesbay888@gmail.com | Property sales (developer site) |
| address | Off Ngong Road, Karbanet Road, Nairobi, Kenya | Sales gallery |
| hours | Mon–Sat 9am–6pm; Sundays by appointment | longinesbay.com/contact |
| url | https://longinesbay.com/ | Property |
| url | https://maps.app.goo.gl/CqD1ur1fM4hShufNA | Maps link on developer site |
| instagram | https://www.instagram.com/LonginesBay/ | Brand social |
| phone | +254 725 937 686 | Agent: Block (CSV) |
| phone | +254 784 448 888 | Agent: CPK / Kenneth Ikiara |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: VorsaGroup |
| email | info@vorsagroup.co.ke | Agent: VorsaGroup |
| phone | +254 141 361 320 | Agent: NRE |
| email | info@nairobirealestate.co.ke | Agent: NRE |
| phone | +254 722 720 812 | Agent: Sir Francis |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |

CSV Block contact ≠ developer sales gallery phones — split Contact.owner correctly.

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Studio Riccardi** (Milan) | architect | longinesbay.com/about — “Lead Architects · Milan” | 4 |
| **Tessera Interiors** (Singapore) | other (interior architecture) | longinesbay.com/about | 4 |
| **Liu Wei** | other (group chairman named) | longinesbay.com/about | 3 |
| Unnamed hotel/property management operator | other | Hotel-managed Block 2 marketing — firm not named | 1 |

No financing partner / contractor named this pass. NEMA ESIA PDF not fetched (Gazette summary only).

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Total units / blocks** | NEMA/Gazette/Kenya Times: **601** units, **three** 18-storey blocks. Marketing site: singular **18-storey** / **1.5 acre**, no 601. | **Official vs official** → **`needs_developer_input`**. No canonical unit_count. |
| 2 | **Storeys** | Marketing/NEMA/agents: **18**. Journal: **24th floor** topping-out post. | **Official vs official** → **`needs_developer_input`**. 24th also **`needs_verification`**. |
| 3 | **3BR duplex size** | Developer residences: **132 sqm**. Multi-agent: **142 sqm**. | Developer vs agents → **canonical size = 132** when citing developer; keep 142 secondary. |
| 4 | **2BR layouts / prices** | Developer: 87 / **89** / 94 and bands from **8.5M**. Agents: 87 / **88** / 94 and bands from **8.7M**. | Keep all in `price_claims[]`; developer bands preferred for canonical typology sizes. |
| 5 | **Street spelling** | Developer uses **Karbanet** and **Kabarnet**; NEMA/news **Kabarnet**; CSV **Karbanet**. | Record both; do not “correct”. |
| 6 | **GPS** | Developer JSON-LD **−1.3635, 36.7719**. | Show + **`needs_verification`** (possible schema error). |
| 7 | **Deposit %** | Developer: staged plans (no %). CPK/NRE: **20%** (and 50/100). | Canonical = staged (developer). 20% secondary below agent threshold. |
| 8 | **Amenities extras** | Official 15 vs agent borehole/generator; FAQ “Olympic” vs page “full-length” pool. | Core = amenities page 15; extras / Olympic wording **`needs_verification`**. |
| 9 | **Sir Francis from-price** | Header **3.5M** vs body/official **3.7M**. | Keep in price_claims; **`needs_verification`**. |
| 10 | **CSV sales_contact** | Block ≠ developer gallery. | Split contacts. |
| 11 | **Related Nanchong entity** | Longines **Island** (Westlands) ≠ Longines **Bay**. | RelatedParty only — do not merge. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 candidates (longinesbay.com home, residences, amenities, about, commercial, contact; Vellum Gazette NEMA summary; Kenya Times; Block; CPK; Vorsa; NRE; Sir Francis; Craiova; plus thin Mestates / RealEstateKenya / Instagram / CSV). **Always kept** developer site pages. Retained 10 richest field-bearing sources (≥5 rule).

**Thin / skipped (not in retained list):**
- https://craiovarealtors.com/property/studios-1-2-br-apartments-at-logines-bay-kilimani/ — typo “Logines”; overlaps denser Vorsa/Block tables (evaluated for alias only)
- https://www.mestatess.com/property/longines-bay-1235.html — near-duplicate agent paste
- https://www.realestatekenya.ke/properties/luxurious-studio-apartments-in-ngong-road-along-karbanet-road — studio-only thin card
- https://www.instagram.com/LonginesBay/ — social shell
- CSV NBO-008 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://longinesbay.com/ | Longines Bay / Nanchong | project_site | 2026-10-16 | 18-storey; 1.5 acre; 2029 KPI; Block 2 hotel program; JSON-LD GPS + 3.7M+ — **always keep** |
| 2 | https://longinesbay.com/residences | Longines Bay / Nanchong | project_site | 2026-10-16 | Typed size/price bands incl. duplex 132 / 176–179 — **always keep** |
| 3 | https://longinesbay.com/amenities | Longines Bay / Nanchong | project_site | 2026-10-16 | Canonical 15 amenities |
| 4 | https://longinesbay.com/about | Longines Bay / Nanchong | developer | 2026-10-16 | Nanchong Group; Studio Riccardi; Tessera; sales contacts |
| 5 | https://vellum.co.ke/kenya-gazette-week-ended-11th-september-2026/ | Vellum (Gazette summary) | official_nema_summary | 2026-10-16 | Nanchong Longines Bay Limited; 3×18-storey; **601**; Ref **NEMA/ENVIS/SR/00719** |
| 6 | https://thekenyatimes.com/economy/nairobi-highrise-project/ | The Kenya Times | news | 2026-10-16 | Same SPV / 601 / three blocks; distinguishes Longines Island |
| 7 | https://block.ke/property/longines-bay-kilimani-apartments-for-sale-off-ngong-road/ | Block Real Estate | agent | 2026-10-16 | CSV channel; Nanchong International; full price table; 2029 |
| 8 | https://commercialpropertykenya.com/properties/longines-bay-apartments-off-ngong-road-nairobi/ | CPK Real Estate | agent | 2026-10-16 | 20/50/100% payment claim; 0.9-acre garden claim; amenity list |
| 9 | https://vorsagroup.co.ke/property/longines-bay-apartments-studio-1-2-duplex-off-ngong-road/ | VorsaGroup | agent | 2026-10-16 | Typed prices; 2029; hotel ROI copy |
| 10 | https://nairobirealestate.co.ke/properties/longines-bay-residences | NRE Real Estate | agent | 2026-10-16 | Price bands; 20% calculator; **58%** progress UI |

**Also used for FAQ answers (same publisher as #1, not double-counted):** homepage FAQ strings in site JS — Q4 2029; staged payment; unit mix 132–179 sqm. Commercial page https://longinesbay.com/commercial retained as part of developer stack evidence for retail rates (cited in §1; densest commercial claims).

---

## 9. Field harvest

| Field | Longines Bay status | Notes for living schema |
|-------|---------------------|-------------------------|
| canonical_name / aliases | OK | Include Logines typo as alias only |
| status | OK as claim set | UC underway + off-plan selling + “Launching 2026” soft |
| geography street | OK | Dual Kabarnet/Karbanet spelling on official |
| geography.lat_lng | Published but weak | JSON-LD present → still **`needs_verification`** |
| primary_developer | OK | Legal SPV + trading names split |
| GroupCompany | Captured | Nanchong Group from About |
| unit_types / size bands | OK | Developer residences + FAQ agree |
| `total_units` / `block_count` | Claim set + **`needs_developer_input`** | 601/3 blocks (NEMA) vs marketing silence |
| `storeys` | Claim set + **`needs_developer_input`** | 18 vs journal 24th floor |
| `price_claims[]` | All options retained (A–I) | Developer typed bands + agent divergences |
| `payment_plan` | **Staged plans canonical** (developer FAQ); 20% secondary | Agent 20% below ≥4 |
| amenities core | OK | Official 15; reject uncorroborated borehole/generator as canonical |
| completion_estimate | **Q4 2029** canonical (FAQ) | Agent 2029 agrees |
| `construction_progress` | Agent-only 58% | Candidate field; no developer tracker |
| Named architect / interiors | Captured | Studio Riccardi; Tessera Interiors |
| Hotel-managed Block 2 program | Captured | 5-yr / ~11% — agreement-gated |
| Wrong-entity trap | Documented | Longines Island ≠ Bay |

### Proposed schema bumps (for coordinator — not auto-locked)

| Proposed extension | This project | Consensus note |
|--------------------|--------------|----------------|
| `total_units` / `block_count` claim set | **Yes** (601 / 3 vs marketing) | Aligns C2 Galaxy/Porini + Berkeley |
| `storeys` claim set when official conflict | **Yes** (18 vs 24th-floor journal) | Aligns Galaxy |
| Developer JSON-LD `lat_lng` even if suspicious | Show + **`needs_verification`** | Do not auto-canonical if coords implausible |
| Legal SPV vs trading name split | **Yes** | NEMA name ≠ CSV trading string |
| Hotel-managed / leaseback program fields | Capture when developer publishes | Block 2 / ROI / term |
| Named architect on developer About | Stakeholder capture | Studio Riccardi pattern |

---

## Open questions (developer input)

1. Reconcile NEMA **601 units / three blocks** with marketing’s singular **18-storey / 1.5-acre** description — which inventory is live for sale?
2. Is the journal **“24th floor”** topping-out post accurate, placeholder, or a different asset?
3. Publish binding LOO: deposit % (agent **20/50/100** vs FAQ “staged” only) and full instalment schedule.
4. Confirm 3BR duplex **132 vs 142 sqm** and 2BR **88 vs 89 sqm** / price bands on the live price list.
5. Correct or confirm JSON-LD GPS **−1.3635, 36.7719**.
6. Which amenities are in approved plans vs marketing (borehole/generator; “Olympic” pool wording)?
7. Name of hotel-management operator for Block 2; sample management agreement terms.
