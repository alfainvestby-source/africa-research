---
slug: golden-mansion
external_id: NBO-001
cycle: half-batch
pilot: false
wave: B
sources_evaluated: 14
sources_retained: 11
last_verified_at: 2026-10-16
---

# Golden Mansion (NBO-001) — half-batch research

CSV seed (unverified leads): location Muthithi Road, Westlands, Nairobi; lat/lng −1.26512, 36.80627; stage `off_plan`; completion Q2 2028; `price_from_kes` 6,180,527; sales_contact Loyd Mokaya (Block Real Estate); developer “SkyPeak Limited”.

Live research accessed **2026-10-16**. No dedicated Summit Vista project microsite recovered; **official regulatory filing** (NEMA EIA) used as primary developer/official source.

**Method locks applied:**
- Conflicts always highlighted.
- **Developer vs agents:** if developer/official sources **agree** on a field → **canonical = developer**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`**; no assumed winner.
- Co-named “Developers” (Summit Vista + Beijing XiangFeng on agent/developer-profile framing) → model as **both** `co_developer` **and** RelatedParty.
- Unproven platform/brand overlap (SkyPeak) → **`marketing_partner`** RelatedParty until proven parent/co-developer.
- **Prices:** always keep full `price_claims[]` (all options). No single scalar.
- Payment must-have if ≥4 independent agent/portal sources **or any developer source**.
- Low-confidence / agent-only / uncorroborated (sold-out, typologies absent from official filing) → **show** + **`needs_verification`**.
- CSV = unverified leads only.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = official/developer-backed when official sources **agree**. Claim set / secondary kept for conflict detection. **`needs_developer_input`** = official materials disagree — no winner. **`needs_verification`** = low confidence / agent-only / uncorroborated.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** (market name) | Golden Mansion | 4 | Agents/portals consensus; EIA title is plot-based (“proposed residential apartments… Muthithi Road”), not the marketing name |
| `aliases` | secondary | Golden Mansion Apartments; Golden Mansion Westlands; Golden Mansions (Masterways typo/plural) | 3–4 | agents |
| `status` | claim set | CSV/`off_plan`; Block “Off-plan / ongoing — For Sale”; NRE “Pre-Launch”; CPK “under construction”; SkyPeak project page “Coming Soon” | 3 | Agent/portal labels diverge — **`needs_verification`** for UC vs pre-launch |
| `geography.city` | **CANONICAL** | Nairobi (Westlands, Nairobi County) | 5 | NEMA EIA; agents |
| `geography.neighbourhood_street` | **CANONICAL** | **Muthithi Road**, Westlands; access also from **Cross Way** / Crossway Road junction | 5 | NEMA EIA; Realtors; CPK; agents |
| `geography.street_number` | secondary | **22 Muthithi Road** | 3 | SkyPeak home; NRE FAQ — **`needs_verification`** (not on EIA extract) |
| `geography.plot` | **CANONICAL** | **L.R. No. NAIROBI/BLOCK 34/424**; **0.2134 hectares**; land registered to proponent | 5 | NEMA EIA |
| `geography.lat_lng` | **CANONICAL** (official filing) | **−1.265143, 36.806272** | 5 | NEMA EIA GPS header |
| `geography.lat_lng` | secondary (CSV) | −1.26512, 36.80627 | 2 | CSV seed (matches EIA to ~1–2 m) |
| `primary_developer_id` | **CANONICAL** | → `dev-summit-vista-company-limited` | 5 | NEMA EIA proponent |
| `co_developer_ids[]` | dual model — **`needs_verification`** on corporate exactness | → `dev-xiangfeng-group` (**also** RelatedParty §4) — co-named with Summit Vista on NRE developer profile / listings as “Summit Vista / Beijing XiangFeng Group”; counsel calls Summit Vista an **affiliate** of XiangFeng | 3 | NRE; LinkedIn counsel; SkyPeak home (Xiangfeng Group Kenya expansion copy) |
| `unit_types` | **CANONICAL** (EIA bedroom mix) | **1-, 2-, and 3-bedroom** apartments | 5 | NEMA EIA (324 / 108 / 8) |
| `unit_types` | secondary — **`needs_verification`** | Agent duplex/loft types **L1–L4**; SkyPeak labels A1/A2 as “studio”; Block **Studio Type A5** + **Type A4** 2BR — not named in EIA bedroom mix | ≤3 | agents |
| `total_units` | **CANONICAL** | **440** (324×1BR + 108×2BR + 8×3BR) | 5 | NEMA EIA; Myspace echoes 440 |
| `building_specs.storeys` | claim set — soft conflict | EIA + most agents: **30-storey** / 30 floors. Counsel LinkedIn: **29-floor**. EIA also: residential units **3rd–29th**, amenities on **30th**, roof amenities — counting convention may explain 29 vs 30 | 4 (30) / 2 (29) | Prefer EIA “30-storey” as developer-filing; keep 29 as conflict + **`needs_verification`** (not official-vs-official page pair — counsel post ≠ second developer page) |
| `building_specs.parking` | **CANONICAL** (structure) | Parking on **2 basements + ground + two mezzanine** (EIA); agents commonly say **5-level** / five-storey podium parking | 5 EIA / 3 agent framing | NEMA; Block; Realtors; Myspace |
| `size_by_type` | secondary (agent tables — no size schedule in EIA extract) | See size table below | ≤3 | agents |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on materials fetched | 0 | — |
| `price_claims[]` | claim set — **keep all**; no canonical | See §1a | ≤3 | No developer price list / LOO on official filing |
| `currency` | **CANONICAL** (market) | KES | 5 | all commercial sources |
| `payment_plan.deposit` | **must-have** (agent ≥4) — no developer LOO | **20% deposit** (Block; Masterways; A-list; NRE calculator default) | 3 | Cap 3 (agent-only, no official LOO) |
| `payment_plan.reservation` | secondary — **`needs_verification`** | **KES 200,000** reservation | 2 | Block only |
| `payment_plan.instalment_schedule` | secondary — **`needs_verification`** | Masterways/A-list identical staged schedule (10%/20%/10%/10%/30%) | 2 | Two portals; may share one LOO — not ≥4 independent schedules |
| `payment_plan.balance` | soft must-have (≥4) | Flexible instalments during construction to completion | 3 | Block; Sir Francis; Realtors; Craiova; SkyPeak “flexible payment plans”; CPK |
| `completion_estimate` | claim set — no developer date | **30 April 2028** / April 2028 (Block, Sir Francis, Craiova) **vs May 2028 / 30 May 2028** (NRE, Realtors, CPK) **vs Q2 2028** (Masterways, A-list, CSV) | ≤3 | **CONFLICT** — no EIA handover date |
| `amenities` (core — multi-source / EIA) | claim set | EIA: gym, changing rooms, outdoor area (30th); swimming pool / children’s play on roof framing. Agents consensus: heated rooftop pool; gym; hotel-style lobby; mini mart; 24hr security/CCTV; backup generator; children’s play; 5-level parking | 4 EIA presence / 3 agent “highest heated rooftop pool” claim | “Highest in Nairobi” = marketing claim via agents (Block attributes to developer) — **`needs_verification`** |
| `amenities` inflated — **`needs_verification`** | secondary | Rooftop restaurant/café/lounge; sauna; mini golf; clubhouse; sky garden; six high-speed elevators; electronic fencing — denser on Realtors/KF/CPK than on Block core list or EIA extract | 1–2 | |
| `availability_claim` | secondary — **`needs_verification`** | Block: loft types “listed as sold out” (ask if released). CPK: L1, L3, L4 **SOLD OUT**. Realtors: “Show Houses: 1 & 2 Bedroom units ready for viewing” | 2 | Uncorroborated across all portals |
| `construction_progress` | secondary — **`needs_verification`** | NRE UI “Pre-Launch **8%**”; no developer tracker | 1 | Agent UI only |
| `legal_title` | secondary — **`needs_verification`** | Block: “Full title; tenure details confirmed at enquiry” | 1 | Single agent |
| `plot_size` | **CANONICAL** | **0.2134 ha** | 5 | NEMA EIA |

### Size table (agent — not on EIA extract)

| Type (agent labels) | Size (sqm) | Role / flag |
|---------------------|-----------:|-------------|
| Studio / Type A5 (Block only) | **41.22** | **`needs_verification`** — absent from other retained agents + EIA bedroom mix |
| A2 1BR | **64.40** | Multi-agent consensus |
| A1 1BR (SkyPeak: “Large Studio”) | **78.46** | Multi-agent; label conflict studio vs 1BR |
| A3 2BR corner | **107.57** | Multi-agent |
| A4 2BR (Block only) | **115.7** | **`needs_verification`** — Block-only type |
| L1 1BR duplex | **66.86–66.87** | Multi-agent |
| L2 1BR duplex | **91.53** | Multi-agent |
| L3 2BR duplex | **138** | Multi-agent |
| L4 3BR duplex | **155.1** | Multi-agent |

Do not invent gross/plinth tags.

### 1a. `price_claims[]` — keep **all** options (no canonical)

No developer-published KES schedule on NEMA filing or a Summit Vista-owned site this pass. **Portal “from” later only if high confidence and high coverage.**

| # | Claim band (KES) | Publisher | Conf | Flags |
|--:|------------------|-----------|-----:|-------|
| A | Studio A5 **6,180,527**; 1BR A2 **8,243,920**; 1BR A1 **9,574,045**; 2BR A3 **13,302,026**; 2BR A4 **12,610,888**; upper-floor ranges to ~**18.78M**; cites price list **1 Sep 2026** | Block | 3 | Dense typed table; **Studio/A4** not on other agents → those rows **`needs_verification`** |
| B | 1BR from **6.5M**; 1BR duplex from **8.2M**; 2BR from **13.5M**; 2BR duplex from **16.8M**; 3BR duplex from **23.5M** | NRE | 3 | |
| C | A2 **6.5M**; A1 **9,022,900**; L1 **9,696,150**; A3 **10,757,000**; L3 **20,010,000**; L4 **21,714,000** | Realtors.co.ke | 3 | |
| D | A2 from **8.6M**; A1 from **9.5M**; A3 from **13.3M**; range to **23.5M** | Craiova | 3 | Higher 1BR “from” than 6.5M cluster |
| E | A1 “Large Studio” **9.5M**; A2 “Compact Studio” **7.7M**; A3 **11.3M** | SkyPeak project page | 3 | First-person marketing site; studio labels; home card also “from **7.8M**” |
| F | 1BR **6.5M–9M**; 1BR duplex **9.7M–12.4M**; 2BR from **10.7M**; 2BR duplex from **20M** | Masterways | 3 | |
| G | A2 **6.5M**; A1 **9M**; A3 **10.7M**; L1 **9.7M**; L2 **12.4M**; L3 **20M**; L4 **21.8M** | A-list | 3 | Same schedule family as Masterways |
| H | A2 **7,438,200**; A1 **9,474,045**; L1 **9,696,150** (sold out); A3 **12,424,335**; L3 **20,010,000** (sold out); L4 **21,714,000** (sold out) | Commercial Property Kenya | 3 | Sold-out flags → **`needs_verification`** |
| I | Indexed KF: A2 **7.44M** (note: KF text swaps A1/A2 sizes vs other agents); A1 **9.47M**; L1 **9.70M**; A3 **12.42M**; L3 **20.01M**; L4 **21.71M** | Knight Frank hub2686160 (search-indexed; live HTML thin) | 2 | Indexed only — not retained as primary cite |
| J | CSV seed `price_from_kes` **6,180,527** | seed | 1 | Unverified lead (matches Block studio A5) |

**Canonical price:** none.

### Payment plan — ≥4-source recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **20% deposit** | Block; Masterways; A-list; NRE (calculator min/default 20%) | **4** | **Met (agents)** | **Must-have** at conf **3** (no developer LOO) |
| Flexible instalments during construction | Block; Sir Francis; Realtors; Craiova; SkyPeak home; CPK | **≥4** | Met | Soft must-have |
| Reservation **KES 200,000** | Block only | **1** | Not met | Alternate · **`needs_verification`** |
| Staged % schedule (10/20/10/10/30) | Masterways; A-list (near-identical copy) | **2** | Not met as ≥4 | **`needs_verification`** |
| Developer published LOO / FAQ schedule | None this pass | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-summit-vista-company-limited` |
| `legal_name` | **Summit Vista Company Limited** |
| `trading_names` | Summit Vista; Summit Vista Ltd |
| `website` | **No official project/corporate microsite recovered this pass** |
| `evidence` | NEMA EIA proponent (P.O. Box 748-00100, Nairobi); agents attribute Summit Vista; LinkedIn counsel: XiangFeng affiliate |
| `group_company_id` | **null as proven parent** — XiangFeng modeled as RelatedParty / dual co_developer (§3–4), not invented GroupCompany row until corporate register proves parent |
| `csv_name_note` | CSV “SkyPeak Limited” = **unverified lead / wrong primary** — SkyPeak is marketing platform (see RelatedParty), not EIA proponent |

**Primary developer = Summit Vista Company Limited (confidence 5)** via NEMA EIA.

---

## 3. GroupCompany

**None set as proven parent.** XiangFeng Group is repeatedly described as backing / affiliate / expansion brand, but no corporate-register parent proof this pass → do **not** invent GroupCompany. Capture under RelatedParty (+ dual co_developer per co-naming lock).

---

## 4. RelatedParty

| id | name | relationship_type | Linked as | Evidence |
|----|------|-------------------|-----------|----------|
| `rp-xiangfeng-group` | Beijing XiangFeng Group / XiangFeng Group (spellings vary: Xiangfeng, Xiangefng on NRE slug) | `affiliate_backing` + **dual `co_developer`** while co-named | Property + Developer | NRE “Summit Vista / Beijing XiangFeng Group”; LinkedIn John Mburu & Co.: “XiangFeng Group and its **affiliate** Summit Vista”; SkyPeak home: Xiangfeng Group Kenya expansion 2025+ |
| `rp-skypeak-limited` | The SkyPeak Limited / Skypeak Limited | **`marketing_partner`** / development platform | Property | skypeak.co.ke project + home first-person marketing; NRE FAQ: “Summit Vista Ltd and the **SkyPeak development platform**”; Block glance table wrongly lists SkyPeak as “Developer”; CSV seed lists SkyPeak as developer |

**Do not** treat SkyPeak as sole/primary developer while EIA names Summit Vista Company Limited.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate | agency | CSV sales_contact; densest typed Sep 2026 price list; 20% + KES 200k reservation | https://block.ke/property/golden-mansion-for-sale-in-westlands-nairobi/ |
| NRE Real Estate | agency / portal | Summit Vista / XiangFeng attribution; payment calculator; Pre-Launch 8% UI | https://nairobirealestate.co.ke/properties/golden-mansion |
| The SkyPeak Limited | marketing platform | Project page + home card; prices; contacts | https://skypeak.co.ke/developments/golden-mansion/ · https://skypeak.co.ke/ |
| Realtors.co.ke | portal / agent | Typed price table; May 2028; show-house claim | https://realtors.co.ke/property/golden-mansion-apartments-westlands-luxury-redefined-on-muthithi-road/ |
| Craiova Realtors | agency | Summit Vista; April 30 2028; higher 1BR from | https://craiovarealtors.com/property/golden-mansion/ |
| Masterways Real Estate | agency | Payment schedule; Q2 2028 | https://masterways.co.ke/properties/golden-mansiona |
| A-list Real Estate | agency | Near-identical payment schedule + unit table | https://a-listrealestate.ke/property/golden-mansion/ |
| Myspace Properties | agency | **440 units / 30 floors** (corroborates EIA); typology list | https://www.myspace.co.ke/property/golden-mansion/ |
| Commercial Property Kenya (CPK) | agency | Typed prices; sold-out flags; May 2028 | https://commercialpropertykenya.com/properties/golden-mansion-apartments-in-westlands/ |
| Sir Francis Homes / Marketing Ltd | agency | From 6.5M; April 30 2028 | https://sirfrancismarketingltd.co.ke/properties/golden-mansion-apartments-westlands-nairobi/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone / WhatsApp | +254 725 937 686 | Agent: Block / Loyd Mokaya (CSV) |
| email | loyd@block.ke | Agent: Block (CSV) |
| phone | +254 11 633 5555 / +254 11 633 7777 | SkyPeak (marketing platform) |
| email | sales@skypeak.co.ke | SkyPeak |
| phone | +254 141 361 320 | Agent: NRE |
| email | info@nairobirealestate.co.ke | Agent: NRE |
| phone / WhatsApp | +254 791 138 831 | Realtors.co.ke listing |
| email | sales@realtors.co.ke | Realtors.co.ke |
| phone / WhatsApp | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |
| phone | +254 722 720 812 | Agent: Sir Francis Homes |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 734 555 556 | Agent: Myspace |
| email | info@myspace.co.ke | Agent: Myspace |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| address (sales site) | 22 Muthithi Road, Westlands (marketing) | SkyPeak / NRE FAQ |
| postal (proponent) | P.O. Box 748-00100, Nairobi | Developer: Summit Vista Company Limited (EIA) |

No Summit Vista sales phone/email recovered on an official developer site this pass.

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **John Mburu & Company Advocates** (John Mburu; Kiama Lilian) | other (legal / conveyancing counsel) | LinkedIn post: supported XiangFeng + Summit Vista on Golden Mansion conveyancing, compliance, sales terms; Gala Dinner Villa Rosa Kempinski 6 Nov 2025 | 3 |
| Unnamed “reputable contractor” | contractor | NEMA EIA: proponent appointed a reputable contractor (NCA registration required) — **not named** | 1 |
| Unnamed architect / engineers / EIA experts | other | EIA references architect, engineers, appointed EIA experts — **firm names not extracted as project marketing stakeholders this pass** | 1 |

No named financing partner this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Primary developer** | CSV + Block glance: **SkyPeak Limited**. NEMA EIA: **Summit Vista Company Limited**. Agents/NRE: Summit Vista (± XiangFeng). NRE FAQ: Summit Vista + SkyPeak “development platform”. | **Canonical = Summit Vista Company Limited** (official filing). SkyPeak = **`marketing_partner`**. CSV/Block “developer = SkyPeak” = secondary wrong/lead. |
| 2 | **XiangFeng role** | “Backed by” (agents) vs “affiliate” (counsel) vs co-labeled developer string on NRE. | Dual model: **`co_developer` + RelatedParty**; **no** proven GroupCompany. |
| 3 | **Storeys** | EIA/agents **30** vs counsel LinkedIn **29**. | Prefer EIA 30-storey; keep 29 as conflict + **`needs_verification`**. Not flagged `needs_developer_input` (counsel ≠ second official developer page). |
| 4 | **Completion** | April / **30 Apr 2028** vs **May / 30 May 2028** vs **Q2 2028**. | Claim set; no developer date → no canonical. |
| 5 | **Prices** | Block Sep 2026 studio-from **6.18M** vs common agent **6.5M** vs SkyPeak **7.7–9.5M** vs Craiova **8.6M** from vs CPK **7.44M** A2, etc. | **Keep all** `price_claims[]`. No scalar. |
| 6 | **Unit typology labels** | EIA 1/2/3BR counts only. Agents add duplex L1–L4; Block Studio A5 + A4; SkyPeak “studio” for A1/A2. | EIA bedroom mix canonical for counts; agent typologies **shown** + **`needs_verification`** where absent from filing. |
| 7 | **Sold-out / show houses** | Block loft sold-out; CPK L1/L3/L4 sold out; Realtors show houses ready. | Show + **`needs_verification`**. |
| 8 | **Status** | off_plan / Pre-Launch / Coming Soon / under construction. | Claim set + **`needs_verification`**. |
| 9 | **20% vs soft flexible-only** | ≥4 sources state 20%; others only “flexible instalments”. | 20% must-have at conf 3; keep flexible-only as secondary soft claim. |
| 10 | **CSV sales_contact** | Block/Loyd ≠ SkyPeak sales phones ≠ Summit Vista (no official sales contact found). | Split Contact.owner correctly. |

---

## 8. Sources (retained **11**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **11** |

**Selection note:** Scanned ~14 candidates (NEMA EIA PDF, Block, SkyPeak project, SkyPeak home, NRE, Realtors, Craiova, Masterways, A-list, Myspace, CPK, Sir Francis, Knight Frank, LinkedIn counsel, plus CSV seed as non-web lead). **Always kept** official EIA filing (no developer microsite). Retained 11 richest / conflict-critical sources (≥5 rule). LinkedIn kept as **only evidence** for 29-floor + affiliate wording.

**Thin / skipped (not in retained list):**
- Knight Frank hub2686160 — live fetch thin/JS shell; indexed copy used only for price-claim note I
- https://sirfrancismarketingltd.co.ke/properties/golden-mansion-apartments-westlands-nairobi/ — overlaps Block/Realtors bands
- https://commercialpropertykenya.com/properties/golden-mansion-apartments-in-westlands/ — evaluated; sold-out + 7.44M band cited in §1a H; overlaps Realtors typology
- https://citiscapevaluers.com/property/golden-mansion-westlands/ — overlaps NRE-style bands
- https://villawatchkenya.com/listing/golden-mansion-1-bedroom-apartment-westlands/ — thin 1BR slice
- CSV NBO-001 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://nema.go.ke/wp-content/uploads/2025/12/SUMMIT-VISTA_00329-min.pdf | NEMA / EIA (proponent Summit Vista Company Limited) | official_filing | 2026-10-16 | **Always keep** — proponent, plot, GPS, 440 units, 30-storey stack, parking, amenities outline |
| 2 | https://block.ke/property/golden-mansion-for-sale-in-westlands-nairobi/ | Block Real Estate | agent | 2026-10-16 | Sep 2026 price list; 20%; KES 200k reservation; wrongly lists SkyPeak as Developer |
| 3 | https://skypeak.co.ke/developments/golden-mansion/ | The SkyPeak Limited | marketing_platform | 2026-10-16 | First-person project page; A1/A2/A3 prices; Coming Soon |
| 4 | https://skypeak.co.ke/ | The SkyPeak Limited | marketing_platform | 2026-10-16 | 22 Muthithi; from 7.8M; Xiangfeng Group expansion copy; contacts |
| 5 | https://nairobirealestate.co.ke/properties/golden-mansion | NRE | agent | 2026-10-16 | Summit Vista / XiangFeng; bands; 20% calculator; Pre-Launch 8% |
| 6 | https://realtors.co.ke/property/golden-mansion-apartments-westlands-luxury-redefined-on-muthithi-road/ | Realtors.co.ke | agent | 2026-10-16 | Typed prices; May 2028; Crossway junction; show houses |
| 7 | https://craiovarealtors.com/property/golden-mansion/ | Craiova Realtors | agent | 2026-10-16 | Summit Vista; Apr 30 2028; from 8.6M |
| 8 | https://masterways.co.ke/properties/golden-mansiona | Masterways | agent | 2026-10-16 | 20% + staged instalment schedule; Q2 2028 |
| 9 | https://a-listrealestate.ke/property/golden-mansion/ | A-list Real Estate | agent | 2026-10-16 | Same payment schedule family; full L1–L4 table |
| 10 | https://www.myspace.co.ke/property/golden-mansion/ | Myspace Properties | agent | 2026-10-16 | **440 / 30** corroborates EIA; typology without prices |
| 11 | https://www.linkedin.com/posts/lilian-kiama_goldenmansion-xiangfenggroup-summitvista-activity-7393681405408432128-f6FX | LinkedIn / John Mburu & Co. counsel | other | 2026-10-16 | **Conflict evidence** — 29-floor; XiangFeng affiliate of Summit Vista |

---

## 9. Field harvest

| Field | Golden Mansion status | Notes for living schema |
|-------|----------------------|-------------------------|
| `canonical_name` / aliases | OK (market name); EIA uses plot title | Marketing name vs filing title |
| `status` | Claim set | Pre-launch vs off-plan vs UC |
| geography + street + **plot LR** + **lat_lng** | OK | **GPS + plot on NEMA** — bump “GPS when official” consensus |
| `primary_developer` | OK | Summit Vista Company Limited (EIA) |
| Related brand / SkyPeak | **`marketing_partner`** | CSV/Block developer mislabel |
| XiangFeng co-name | Dual **`co_developer` + RelatedParty** | Same pattern as Porini Rendeavour/Tatu |
| `unit_types` / sizes | EIA mix canonical; agent duplex/studio tables secondary | Gross/plinth unknown |
| `total_units` | **440 CANONICAL** (EIA) | Bump unit_count consensus |
| `storeys` | 30 (EIA) vs 29 (counsel) | Claim set; not official-vs-official pages |
| `price_claims[]` | All options A–J retained | No developer LOO |
| `payment_plan` | **20% must-have via ≥4 agents** (conf 3) | No developer schedule |
| `construction_progress` | Agent UI 8% only | Not developer tracker |
| amenities core | EIA + multi-agent core | Reject uncorroborated restaurant/golf adds |
| completion_estimate | April vs May 2028 conflict | No developer date |
| Named counsel stakeholder | John Mburu & Co. | Capture when named |
| Official EIA when no microsite | **Worked** | Reinforce “always keep official filing” |

### Proposed schema consensus bumps (for coordinator / DB steward)

| Proposed extension | This project | Suggested consensus |
|--------------------|--------------|---------------------|
| `total_units` claim set / canonical when single official filing | **440** EIA | Bump toward lock (with Porini/Galaxy/Riara) |
| Official **GPS** when on EIA/filing | **−1.265143, 36.806272** | Promote when official |
| Official **plot LR + area_ha** | NAIROBI/BLOCK 34/424; 0.2134 ha | Same as Riara tenure/plot propose |
| `marketing_partner` for sales platform mislabeled as developer | SkyPeak | Astra/Riara pattern continues |
| Dual co_developer+RelatedParty for co-named foreign group | XiangFeng | Porini pattern continues |
| Payment **20%** via ≥4 agents without developer LOO | Met at conf 3 | Same as Riara half-batch |

---

## Open questions (developer / verification pass)

1. Confirm contracting entity on LOO: **Summit Vista Company Limited** vs SkyPeak Limited vs XiangFeng entity.
2. Publish current official **price list** (resolve 6.18M studio vs 6.5M vs SkyPeak 7.7M+ bands) and whether Studio A5 / A4 exist.
3. Binding **payment schedule** (20% + stages) vs agent calculators.
4. Contractual **completion** date: 30 Apr vs 30 May 2028.
5. Reconcile **29 vs 30** floor marketing with EIA stack (3–29 residential + 30 amenities).
6. Live **availability** / sold-out loft claims; show-house status.
7. Named **contractor**; official Summit Vista / XiangFeng websites and sales contacts.
