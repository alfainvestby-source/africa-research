---
slug: hephe-palace
external_id: DISC-NBO-011
wave: block-2028-wave2
pilot: false
sources_evaluated: 13
sources_retained: 9
last_verified_at: 2026-10-16
---

# Hephé Palace (DISC-NBO-011) — discovery research

**Seeded** (`properties.csv` DISC-NBO-011, changelog **0.1.20**). Block 2028 process-rerun Tier A ([block-2028-process-rerun-batch.md](../discovery/block-2028-process-rerun-batch.md)). **Ring Road Westlands** / Peponi corridor (opp. The Oval, next to Kingfisher Hotel), **Sequoia Real Estate** (trading) / **Sequoia China Limited** (legal claim), off-plan / under construction, completion **September / Q3 2028** cluster.

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only; never conf ≥3 / never public-canonical).

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.

**≠ “Karura Forest Views”** — Block-only / likely AI alias clustering forest-view language onto Hephé and other Peponi products. See **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Hephé Palace** | 5 | hephepalace.ke; NRE; Crown; CIG; Own It |
| `aliases` | secondary | Hephe Palace; Hephe’ Palace; Hephé’ Palace; Hephé Palace Apartments | 4 | SkyscraperCity title; agents; Block slug |
| `status` | claim set | **Off-plan / pre-sales** (agents; NRE “Pre-Launch”) vs **under construction** (SSC thread + site photos Sep–Oct 2025; Kenya4u “en cours de construction”) → show both; UC secondary | 3–4 | NRE vs SSC / Kenya4u |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** (Ring Road / Parklands–Highridge edge; Peponi corridor marketing) | 5 | hephepalace.ke Location; EIA notice; agents |
| `geography.street` | **CANONICAL** (corridor) | **Ring Road Westlands** — next to **Kingfisher Hotel**, opposite **The Oval**; ~150–200 m Westgate | 5 | hephepalace.ke; NRE; Crown; Masterways; EIA “Ring Road Parklands/Highridge” |
| `geography.plot` | secondary — regulatory | **L.R. No. 1870/85** (Nairobi/Block **7/57**) | 4 | NEMA EIA public-comments text via SSC |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-sequoia-real-estate` | 5 | hephepalace.ke Team (“Developer — Sequoia Real Estate”) |
| `unit_types` | **CANONICAL** soft (marketing) | **Studio**; **1 Bedroom** (67 / 69 / 72 sqm variants); **1 Bedroom + Study**; **2 Bedroom**; **2 Bedroom + Study**; **3 Bedroom + DSQ**; **Penthouses** (POR) | 4 | hephepalace.ke Residences nav; NRE; Crown; CIG; Masterways |
| `unit_mix_eia` | secondary — regulatory | EIA: **98** studio; **316** 1BR; **124** 2BR; **100** 3BR; **2** 3BR duplex; **4** 4BR duplex (= **644**) | 4 | NEMA EIA notice via SSC — marketing mix does not list 4BR duplex / duplex counts |
| `size_by_type` | claim set — see table | Studio **48**; 1BR **67–72**; 1BR+Study **87**; 2BR **109**; 2BR+Study **130**; 3BR+DSQ **158–168** | 4 | Multi-agent price cards (aligned); not published as scalars on hephepalace.ke this pass |
| `total_units` | secondary | **644** | 4 | EIA; NRE “Units 644”; O’Bang counsel bio |
| `building_specs.storeys` | secondary | **28** residential floors (+ **ground** + **mezzanine** + **2** basements per EIA); SSC OP: **five** blocks of 28 (not three) | 4 / 3 | EIA; SSC #14/#26–#28 — block count **`needs_verification`** |
| `price_claims[]` | multi | See **§1a** — **no official price list** on developer site this pass | — | — |
| `currency` | **CANONICAL** soft | **KES** (agents also quote USD at ~130) | 4 | Crown; Masterways; SSC |
| `payment_plan` | secondary — **must-have met** (≥4 agents) | See **§1b** — **`needs_verification`** vs developer LOO (not on hephepalace.ke this pass) | 4 | Crown; Masterways; Own It; NRE; My Crib; SSC |
| `completion_estimate` | claim set | **September 2028** (agents / SSC) vs **Q3 2028** (NRE) — agree year/quarter band | 4 / 3 | Crown; Masterways; Own It; Kenya4u; NRE |
| `amenities` | **CANONICAL** soft | Rooftop / courtyard pool(s); gym; yoga studio; game room; rooftop open-air cinema; sky garden / “Terrera”; restaurant + bar; café / mini-mart; kids’ play; concierge; **10** lifts; CCTV; backup generator; borehole (agents) | 4 | hephepalace.ke Amenities; NRE; Crown |
| `amenities` agent extras | secondary | Mini golf; padel court; billiards — denser agent / SSC lists | 2 | Crown; Own It; SSC — **`needs_verification`** |
| `roi_claim` | secondary marketing | Unfurnished ~**17–18%**; furnished ~**23–24%**; Airbnb up to ~**25–33%** (60% occupancy assumptions) | 2 | Crown; Masterways; Own It; SSC — **`needs_verification`** |
| `legal_title` | soft | Plot cited in EIA; tenure / mother-title path not recovered this pass | 2 | EIA plot only |
| `master_planned_community` | none | Standalone high-rise (not a named masterplan precinct) | — | — |

### Size table (retained — agent-aligned)

| Type | Size (sqm) | Role | Conf |
|------|----------:|------|-----:|
| Studio | **48** | Crown; CIG; Masterways; NRE | 4 |
| 1 Bedroom | **67 / 69 / 72** | Multi-agent typed bands | 4 |
| 1 Bedroom + Study | **87** | Multi-agent | 4 |
| 2 Bedroom | **109** | Multi-agent | 4 |
| 2 Bedroom + Study | **130** | Multi-agent | 4 |
| 3 Bedroom + DSQ | **158–168** | Multi-agent | 4 |
| Penthouses | unknown | POR / “Luxury Penthouses” | 2 | NRE; Own It |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No developer price list** on hephepalace.ke this pass → all prices are agent / portal claims → **`needs_verification`**. Band is tightly copied across agents (likely shared sales sheet).

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Studio **48** **KES 6.2M – 6.9M**; 1BR **67** **8.2–8.9**; **69** **7.5–8.25**; **72** **8.8–9.7**; 1BR+Study **87** **9.95–10.85**; 2BR **109** **13.8–14.99**; 2BR+Study **130** **17.2–18.3**; 3BR+DSQ **158** **19.8–20.95**; **168** **21.8–22.95** | Full typed ranges | Crown; Masterways; SSC OP | 3 | Shared sheet pattern |
| B | “From” floors: Studio **6.2M**; 1BR **7.5M**; 1BR+Study **9.95M**; 2BR **13.8M**; 2BR+Study **17.2M**; 3BR+DSQ **19.8M**; penthouses POR | FAQ / summary | NRE | 3 | Collapses ranges to lows |
| C | Upper-band singles: Studio **6.9M**; 1BR **8.9 / 8.25 / 9.7**; 1BR+Study **10.85**; 2BR **14.99**; 2BR+Study **18.3**; 3BR **20.95 / 22.95** | Table of highs | CIG | 3 | Looks like top of A |
| D | Compressed: Studio **6.2–6.9**; 1BR **7.5–9.7**; 1BR+Study **9.95–10.85**; 2BR **13.8–18.3**; 3BR+DSQ **19.8–22.95** | Summary table | Own It | 3 | Merges 2BR + study into one row |
| E | Hero “from **KES 6.2M**” / portal from **6.9M** | Marketing floor | Crown; CIG card | 3 | |
| F | Block listings 1BR+Study from **9.95M**; 2BR from **13.8M**; 3BR+DSQ from **19.8M**; completion Sep 2028 | Aggregator | block.ke | ≤2 | Discovery only — **not retained as authority** |

**Portal scalar:** none for public canonical. Resolve with Sequoia sales / LOO before any “from” field.

### 1b. Payment plan — ≥4-agent must-have **met** (developer page silent)

| Element | Source | Status |
|---------|--------|--------|
| Deposit options **20% / 30% / 50% / 100%** to reserve; deposit-linked discounts (agents say up to **10%**) | Crown; Masterways; My Crib; SSC; Own It (20–50%); NRE (20–100%) | Secondary structure — conf **4** consensus; **`needs_verification`** |
| Balance over **36 months** at **0%** interest; monthly or quarterly | Crown; Masterways; NRE; My Crib; Own It; SSC | Same |
| NRE on-page calculator example: **20%** deposit + quarterly to **Q3 2028** | nairobirealestate.co.ke | Illustrative only — “Estimates only… Confirm… developer” |
| Official hephepalace.ke payment schedule | — | **Not published** this pass |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-sequoia-real-estate` |
| `legal_name` | **Sequoia China Limited** — **locked at conf 4** (EIA proponent + counsel bio); **not** named on hephepalace.ke Team (trading brand only) → Companies Registry string / LOO still **`needs_verification`** |
| `trading_names` | **Sequoia Real Estate**; Sequoia Real Estate Development (NRE note) |
| `website` | https://www.hephepalace.ke/ (project); sales **sales@hephepalace.co.ke** |
| `evidence` | Official Team: “Developer — Sequoia Real Estate”; NEMA EIA public-comments notice names proponent **Sequoia China Limited** for L.R. 1870/85 / 644-unit scheme; O’Bang Law partner bio: advised **“Sequioa China Limited”** on acquisition + managing **644-unit Hephé Palace**; NRE attaches Sequoia China Limited (self-flags unverified) |
| `group_company_id` | **null** — none invented; Kenya4u China-portfolio / “Liu Yongguang” claim **not** elevated |
| `sales_office` / contacts | Project phones **+254 727 555 581** / **+254 727 555 591**; sales@hephepalace.co.ke (official). Concept/marketing design: **KARIM CG VISUALS** (hephepalace.ke Team) |
| `confidence` | **5** trading face / **4** legal name (EIA + counsel) / **0** invented parent |

**Note:** Official site does **not** print “Sequoia China Limited”. Legal lock rests on **regulatory + counsel** corroboration of the NRE allegation — not on inventing an SPV.

---

## 3. GroupCompany

**None invented.** No proven parent / HongShan link (NRE explicitly disclaims). China-side companies named only on Kenya4u → ignore for entity graph this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| KARIM CG VISUALS | development concept & marketing design | hephepalace.ke Team; SSC mention | 4 |
| Ong’anya Ombo Advocates LLP (O’Bang Law) | counsel / acquisition + project management support (self-described) | obang.law lawyer bio | 3 |
| Agents (Crown, CIG, Masterways, Own It, NRE, My Crib, Kenya4u, …) | sales intermediaries | Project pages | 3 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| NRE (nairobirealestate.co.ke) | Dense mix + payment + Sequoia China Limited label (flagged unverified by NRE itself) |
| Crown Real Estate Group | Full price ranges + 36-mo payment + Sep 2028 |
| CIG Real Estate | Upper-band price table |
| Masterways Real Estate | Full ranges + payment echo |
| Own It Kenya | Summary prices + payment + Sep 2028 |
| My Crib Kenya | Payment + from-prices |
| Kenya 4 You | Sequoia Real Estate attribution; UC status |
| SkyscraperCity (forum OP) | Marketing sheet + EIA paste + UC photos (not an agent) |

---

## 6. Sources

### Retained (≥5 rule; developer kept)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.hephepalace.ke/ | Sequoia Real Estate (project) | developer | Primary — name, location narrative, amenities, Team, contacts |
| 2 | https://www.skyscrapercity.com/threads/hephe%E2%80%99-palace-westlands-28-28-28-fl-u-c.2441628/ | SkyscraperCity | forum / UC + EIA paste | 28 fl; 5 blocks claim; EIA proponent + 644 mix; construction photos |
| 3 | https://obang.law/lawyer/ombo-malumbe/ | O’Bang Law | counsel | Sequoia China Limited ↔ Hephé Palace 644 units |
| 4 | https://nairobirealestate.co.ke/properties/hephe-palace | NRE | agent / portal | Prices; Q3 2028; payment; 644 units; developer label |
| 5 | https://crownrealty.co.ke/property/hephe-palace-apartments-westlands/ | Crown | agent | Full ranges; 36-mo plan; Sep 2028 |
| 6 | https://cig.co.ke/properties/hephe-palace | CIG | agent | Upper-band table |
| 7 | https://masterways.co.ke/properties/hephe-palace | Masterways | agent | Ranges + payment |
| 8 | https://ownitkenya.com/property/hephe-palace/ | Own It Kenya | agent | Summary prices + payment |
| 9 | https://kenya4u.com/en/hephe-palace/ | Kenya 4 You | agent / diaspora | Sequoia Real Estate; UC; Sep 2028 |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/project/hephe-palace/ (+ unit listings) | Low-trust / AI — discovery seed only; conf ≤2 |
| https://block.ke/project/karura-forest-views/ | Alias / unrelated twin-tower product — anti-merge only |
| https://splendorholdings.co.ke/properties/hephe-palace-apartment-in-westlands/ | HTTP 500 this pass |
| https://mycribkenya.co.ke/properties/hephe-palace-apartment/ | Payment echo — overlap with retained agents (counted in evaluated) |
| https://nairobirealestate.co.ke/developers/sequoia-china-limited | Meta profile; folds into NRE |
| LinkedIn Wilons post | Thin marketing reprint |
| Chestone Properties unit URLs (via NRE notes) | Unit-listing grain; not development dossier primary |

**sources_evaluated ~13 · sources_retained 9**

---

## 7. Open questions

1. Confirm **Sequoia China Limited** on Companies Registry / LOO / SPA contracting face (vs trading **Sequoia Real Estate** only).  
2. Publish official **price list** + **payment calendar** on developer channel (currently agent-only).  
3. Confirm **block count** (SSC: five × 28 vs early “28,28,28” title) and exact tower geometry.  
4. Reconcile marketing unit types vs EIA duplex / **4BR** counts.  
5. Current **construction %** / milestone photos vs NRE “Pre-Launch 8%”.  
6. Exact GPS / site entrance on Ring Road (opp. Oval — SSC still triangulating).  
7. Tenure, service charge, parking allocation, foreign-buyer path.

---

## 8. Anti-merge

- **≠ “Karura Forest Views”** (Block project slug `karura-forest-views`) — **no independent project** under that name in non-Block sources this pass. Block copy: twin towers on **Ring Road at Eldama Ravine Roundabout**; **3 / 4 / 5 bed** from ~**KES 17.03M / 19.61M / 28.51M**; completion **December 2028**; amenities include rooftop running track. Shared “Karura Forest views” marketing language is the clustering trap — **do not merge** into Hephé (studio–3BR+DSQ from ~**6.2M**, **Sept/Q3 2028**, Sequoia, **644** units, opp. **The Oval** / Kingfisher). Discovery batch already holds Karura Forest Views as likely Block alias.  
- **≠ Forest One Residency / Forestview Residences** (Eldama Ravine Road forest-front products).  
- **≠ Tree Tops Forest Apartments / 48 Treehouse** (Peponi Road forest products).  
- **≠ Golden Hill** (Donyo Sabuk / Upper Westlands forest edge).  
- **≠ Diplomat / Amani** and other Ring Road / Oval-adjacent towers (SSC neighbours — different schemes).  
- **≠** any Block “Hephe” unit listing treated as the development entity (developments-only rule).
