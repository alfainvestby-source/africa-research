---
slug: marina-bay-2
external_id: DISC-NBO-027
wave: hauzisha-c-2026-10-17
pilot: false
sources_evaluated: 14
sources_retained: 9
last_verified_at: 2026-10-17
inventory_class_intent: building
---

# Marina Bay 2 / Marina Bay Phase 2 (DISC-NBO-027) — discovery research

**Not in seed CSV.** Hauzisha Slice C ([hauzisha-slice-c.md](../discovery/hauzisha-slice-c.md)). **Sports Road**, Westlands, Nairobi — **M-Group Developer**, off-plan / under construction, completion claims **December 2026** (majority) vs **Q1 2027** occupation (GNA).

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355 / +254 730 731 355** is **Hauzisha only** — **never** M-Group.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV for Phase 2.
- Skip Ready inventory — this project is **building / UC** (not Ready/handed-over). Phase 1 sibling is Ready-to-let — **not** this dossier.

**≠** Marina Bay Phase 1 / Marina Bay Square; **≠** Marina Bay 3; **≠** Montbleu Westlands; **≠** Auris Residence — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Marina Bay Phase 2** (portal short **Marina Bay 2**) | 4 | GNA; Farman; Sydia; CPK; A-list; Craiova; Hauzisha “Marina Bay 2” — **no official M-Group project microsite this pass** |
| `aliases` | secondary | Marina Bay 2; Marina Bay II; Marina Bay Phase II; Marina Bay Westlands (Phase 2) | 3 | Hauzisha; Masterways; agents |
| `status` | secondary | **Under construction / off-plan sales** — A-list: construction began **Nov 2023**; Sydia site update **24 Sep 2026**; Farman/Sydia/Craiova “1BR sold out”; **not** Ready | 3 | Multi-agent; Hauzisha stock cards |
| `inventory_class` intent | research queue | **`building`** (UC with residual instalment marketing; target Dec 2026). **Not** `ready`. | — | Method lock |
| `geography.city` | **CANONICAL** soft | Nairobi | 4 | All retained |
| `geography.neighbourhood` | **CANONICAL** soft | **Westlands** | 4 | All retained |
| `geography.street` | **CANONICAL** soft | **Sports Road** (behind / just behind **Park Inn by Radisson**) | 4 | GNA; Farman; Sydia; CPK; LinkedIn wilons; EIA sibling corridor |
| `geography.landmarks` | secondary | Behind Park Inn by Radisson; near GTC, Sarit, Westgate, Waiyaki Way | 3 | GNA; CPK; LinkedIn |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** soft (trading) | → **M-Group Developer** (`dev-lead-m-group-developer` until official contacts/SPV promote) | 4 / 2 | Hauzisha attribution; agent “earlier phases” narrative — **no official M-Group Kenya sales page recovered this pass** |
| `unit_types` | secondary consensus | **1 Bedroom**; **2 Bedroom + DSQ**; **3 Bedroom + DSQ** (1BR widely marked sold out on agents) | 3–4 | GNA; Farman; Sydia; CPK; A-list; Craiova; Hauzisha 1/2/3BR |
| `size_by_type` | claim set — see table | 1BR **67 / 70 sqm**; 2BR+DSQ **130 / 135 / 145 sqm**; 3BR+DSQ **198 sqm**; Hauzisha band **67–198 sqm** | 3–4 | Multi-agent agree on typology sizes |
| `building_specs.height` | secondary | **18 floors** (Farman; Sydia; A-list floor bands to 18th) | 3 | Agents only — **`needs_verification`** |
| `building_specs.blocks` | secondary | **2 blocks** (GNA copy — may echo Phase 1 amenity paste) | 2 | GNA — **`needs_verification`** |
| `total_units` | unknown | — | 0 | Hauzisha “**3** units available” = stock snapshot only — **not** scheme total |
| `price_claims[]` | multi | See **§1a** — marketing floor ~**KES 9M**; live 2/3BR sheets mostly **~14.45–23.95M** | — | — |
| `currency` | secondary | **KES** | 3 | All price publishers |
| `payment_plan` | secondary — must-have **locked** (≥4 agents) | See **§1b** — **10% / 10% / 75% / 5%** cash instalment consensus; Masterways **20/75/5** outlier | 3 | Farman; Sydia; A-list; Craiova (+ Realtors echo) |
| `completion_estimate` | claim set — soft conflict | Majority **December 2026** vs GNA **Q1 2027** occupation vs one Realtors 1BR card **November 2026** → **`needs_verification`** | 3 / 2 | Hauzisha; Farman; Sydia; CPK; A-list; Craiova vs GNA |
| `amenities` | secondary (agent/portal) | Rooftop pool; rooftop/fully equipped gym; sky lounge; kids’ play; conference / board room; restaurant café; mini mart; social club house; reception lobby; **4** high-speed lifts; borehole; solar water heating; full backup generator; CCTV; electric fence; video intercom; internet; ample parking; sauna (subset); fingerprint lock (A-list/Masterways) | 3 | GNA densest; Farman; Sydia; CPK; Hauzisha chips |
| `roi_claim` | marketing | Corporate / furnished / Phase 1 rental benchmark narratives — **`needs_verification`**; not quantified on developer official | 1–2 | LinkedIn wilons; CPK; Farman |
| `legal_title` | secondary agent claim | A-list: **99-year leasehold from August 2019** — single agent → **`needs_verification`** | 2 | A-list only |
| `construction_progress` | secondary | Sydia “Latest Construction Update” **24 Sep 2026**; LinkedIn Phase 2 proof / Phase 1 operating benchmark — no % complete on developer page | 2–3 | Sydia; LinkedIn |
| `master_planned_community` | sibling cluster | Part of **Marina Bay** Sports Road cluster (Phase 1 Ready; Phase 2 UC; Phase 3 later) — **do not merge** phases | — | GNA Phase 1/2 pages; Hauzisha MB3 |

### Size table (retained)

| Type | Size | Role | Conf |
|------|-----:|------|-----:|
| 1 Bedroom | **67 sqm** | Multi-agent typed | 4 |
| 1 Bedroom (premium) | **70 sqm** | Multi-agent typed | 4 |
| 2 Bedroom + DSQ | **130 sqm** | Multi-agent typed | 4 |
| 2 Bedroom + DSQ | **135 sqm** | Multi-agent typed | 4 |
| 2 Bedroom + DSQ | **145 sqm** | Multi-agent typed | 4 |
| 3 Bedroom + DSQ | **198 sqm** | Multi-agent typed | 4 |
| Hauzisha band | **67–198 sqm** | Portal aggregate | ≤2 |

Gross vs plinth: **not distinguished** on retained sources.

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No developer official price list** recovered this pass. Typed agent sheets are dense but diverge on floors and “sold out” status — cap at conf **3** without LOO.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | 1BR **67 from 9–9.8M**; 1BR **70 from 9.2–10M**; 2BR+DSQ **130 from 14.45–15.45M**; **135 from 15.15–16.15M**; **145 from 16.45–17.45M**; 3BR+DSQ **198 from 22.55–23.95M** | Full typed card; from **~9M** hero | GNA | 3 | Aligns with Farman/Craiova on 2/3BR |
| B | 1BR **sold out**; 2BR+DSQ **130 14.45–15.45M**; **135 15.15–16.15M**; **145 16.45–17.45M**; 3BR+DSQ **198 22.55–23.95M**; **18 floors**; Dec **2026** | Typed + payment | Farman Real Estate | 3 | Search-indexed listing (fetch 404 this pass — content retained from index) |
| C | Same shape as B on older crawl; live page **28 Sep 2026** shows higher 2/3BR floors (**15.45–16.45 / 15.85–16.85 / 17.25–18.25 / 23.55–24.95M**); 1BR sold out; Dec **2026**; showhouses 145 & 198 | Updated typed card | Sydia Realty | 3 | Price drift vs B/A — **`needs_verification`** which sheet is live LOO |
| D | 1BR **67 from 9M**; **70 from 9.5M**; 2BR+DSQ **130 from 14.95M**; **135 from 15.65M**; **145 from 16.95M**; 3BR+DSQ **198 from 23.25M**; Dec **2026** | Typed “from” singles | CPK | 3 | Mid-band vs A/B |
| E | 1BR **67 from 9M**; **70 from 9.2M**; 2BR+DSQ **130 from 9.4–10M**; **135 from 15.15M**; **145 from 15.65M**; 3BR+DSQ **198 from 22.55M** (floors to **23.25 / 23.95M**) | Typed + payment + tenure | A-list | 2–3 | **130 sqm “from 9.4–10M” anomalous** (≈1BR band) — **`needs_verification`** (likely paste error; Masterways copies same) |
| F | 2BR+DSQ **130 14.45–15.45**; **135 15.15–16.15**; **145 16.45–17.45**; 3BR+DSQ **198 22.55–23.95**; Dec **2026** | Typed + **10/10/75/5** | Craiova Realtors | 3 | Matches A/B 2/3BR |
| G | 2BR+DSQ **130 from 14.55M**; **135 from 15.55M**; **145 from 16.55M**; 3BR+DSQ **198 from 22.75M** | Compressed “from” | Foresee Realtors | 3 | Slightly above A floors |
| H | Band **KES 9M – 23.3M**; sizes **67–198**; **3** units available; Dec **2026** | Portal card | Hauzisha | ≤2 | Aggregator; phone is portal |
| I | Same anomalous sheet as E (incl. 130 sqm **9.4–10M**) + payment **20%/75%/5%** | Agent card | Masterways | 2 | Payment conflicts §1b majority |
| J | Phase 1 rental / Ready — **not** Phase 2 sale prices | Rent lead | Block.ke; GNA Phase 1 | ≤1 | Anti-merge / discovery only |

**Portal scalar:** none. Treat **~9M** as historical/marketing 1BR floor only; resolve live stock (1BR sold-out vs still listed) via LOO.

### 1b. Payment plan — must-have **triggered** and **structure locked** (≥4 independent agents)

No instalment schedule on an official M-Group Phase 2 page this pass. **Four** independent agents publish the same cash shape:

| Element | Source | Status |
|---------|--------|--------|
| **10%** booking / deposit; **10%** on signing sale agreement; **75%** over construction (**within 30 months** on A-list); **5%** on completion | Farman; Sydia; A-list; Craiova | Secondary consensus (conf **3**) — locked under ≥4-agent rule; still **`needs_verification`** vs developer LOO |
| Mortgage option: **30%** deposit / **70%** bank finance | A-list; Masterways | Secondary |
| **20%** deposit; **75%** construction; **5%** completion (no separate signing 10%) | Masterways | Outlier — **do not** merge into lock |
| GNA “flexible… after deposit” (no %) | GNA | Thin — does not weaken 10/10/75/5 lock |
| Official M-Group payment schedule | — | **Not published** this pass → **`needs_developer_input`** for LOO confirmation |

**Must-have met?** **Yes** (agent ≥4) — cash **10/10/75/5**. Official confirmation still open.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-lead-m-group-developer` |
| `legal_name` | **Unknown** this pass for Phase 2 (Companies Registry string not recovered). Phase 1 EIA names **Marina Bay Square Development Ltd** — **sibling evidence only**; **not** assumed Phase 2 SPV |
| `trading_names` | M-Group Developer; M Group Developers (NRE face) |
| `website` | **Unknown** this pass — no working official Kenya project site recovered (mgroupinc.com unrelated / blocked) |
| `evidence` | Hauzisha attribution on Marina Bay 2/3 + Montbleu; multi-agent Phase 2 sales pages; Phase 1 GNA “Phase 2 and 3 available for sale” |
| `group_company_id` | **null** — none invented |
| `sales_office` | **Unknown** official — agent contacts only (see **§5** / contacts summary). **Never** assign **0730 731 355** |
| `confidence` | **4** trading face via portal/agents / **0** Phase 2 legal SPV |

---

## 3. GroupCompany

**None invented.**

Forum/marketing chatter that the same investors sit behind Marina Bay 1/2, Marble West, and Montbleu → at most **unverified RelatedParty cluster** — **not** a GroupCompany this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| **Marina Bay Square Development Ltd** | Phase 1 EIA proponent (sibling) | NEMA EIA Plot **L.R. 1870/X/34**, David Osieli × Sports Road — **14**-floor 1&2BR scheme | 4 for Phase 1 identity / **0** as Phase 2 SPV until proven |
| Muthithi Square Development Ltd | Montbleu official face (sibling portfolio) | montbleu.co.ke “Developer” line | 3 for Montbleu — **≠** this project |
| GNA / Farman / CPK / A-list / Sydia / Craiova / Foresee / Masterways | selling agents | Independent listing pages | 3 |
| LinkedIn (wilons Phase 2 narrative) | marketing / site-proof media | Sports Road Phase 2 + Phase 1 rental benchmark post | 2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role / contacts (agent-only) |
|----------------|------------------------------|
| **GNA Real Estate** | Densest typology + Phase 1 rent cross-link; from **9M**; Q1 **2027**; **+254 712 406 060** / **+254 782 406 060**; support@gna.co.ke |
| **Farman Real Estate** | 18 floors; 1BR sold out; **10/10/75/5**; Stacy Wasonga **+254 701 908 464**; stacyw@farmanrealestate.com |
| **CPK Real Estate** | Typed mid-band prices; Dec **2026**; viewing **0784 448 888** / info@commercialpropertykenya.com |
| **Sydia Realty** | Updated prices; showhouses; site update Sep **2026**; **+254 700 437 505** / **+254 759 333 300**; info@sydiarealty.com |
| **A-list Real Estate** | Payment + tenure; anomalous 130 sqm floor; **+254 769 117 788** / **+254 711 942 900** |
| **Craiova Realtors** | 2/3BR sheet + **10/10/75/5**; **+254 720 004 631** |
| **Foresee Realtors** | Slightly higher “from” floors; Sports Road |
| **Hauzisha** | M-Group name; **9–23.3M**; Dec **2026** — portal only; **ignore 0730 phone** |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://hauzisha.co.ke/developments/marina-bay-2/ | Hauzisha | portal | M-Group; Dec 2026; **9–23.3M**; 67–198 sqm — conf ≤2; **ignore 0730 phone** |
| 2 | https://gna.co.ke/project/marina-bay-phase-2-westlands-1-beds-2-and-3-beds-plus-dsq/ | GNA | agent | Sports Rd; Park Inn; full price table; Q1 2027; flexible payment (no %) |
| 3 | https://farmanrealestate.com/listing/marina-bay-phase-2-luxury-apartments-sports-road-westlands | Farman | agent | 18 floors; sold-out 1BR; **10/10/75/5**; Dec 2026 (indexed; direct fetch 404 this pass) |
| 4 | https://sydiarealty.com/estate_property/marina-bay-phase-2-elegant-living-in-westlands/ | Sydia | agent | Updated prices; payment; showhouses; Sep 2026 site update |
| 5 | https://commercialpropertykenya.com/properties/marina-bay-phase-2-westlands/ | CPK | agent | Typed prices; Dec 2026; Sports Road |
| 6 | https://a-listrealestate.ke/property/marina-bay/ | A-list | agent | Payment + mortgage + leasehold claim; Nov 2023 start |
| 7 | https://craiovarealtors.com/property/2-3-bedroom-plus-sq-apartments-in-westlands/ | Craiova | agent | 2/3BR + **10/10/75/5** (4th payment lock) |
| 8 | https://foreseerealtors.com/portfolio/marina-bay-westlands-2/ | Foresee | agent | Sports Road; alternate “from” floors |
| 9 | https://www.linkedin.com/posts/wilons_airbnbinvestment-kenyarealestate-diasporainvestment-activity-7464548333483798528-40rI | LinkedIn (wilons) | media | Phase 2 Sports Road narrative; Phase 1 operating/rental proof |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://gna.co.ke/project/marina-bay-square-westlands-phase-1-modern-1-and-2-beds/ | **Phase 1** Ready-to-let sibling — anti-merge evidence only |
| https://nema.go.ke/wp-content/uploads/2025/03/EIA_1929-WESTLANDS-MARINA-BAY_SR-2492-min.pdf | Phase 1 EIA (**Marina Bay Square Development Ltd**, 14 floors, 1&2BR) — not Phase 2 sales authority |
| https://hauzisha.co.ke/developments/marina-bay-3/ | **Phase 3** sibling (Mar 2029; studio–4BR) — defer |
| https://masterways.co.ke/properties/marina-bay-ii | Overlaps A-list anomalous prices; payment **20/75/5** outlier |
| https://block.ke/property/marina-bay-westlands-1-2-bedroom-apartments-to-rent/ | Phase 1 rent; Block low-trust |
| https://realtors.co.ke/property/elegant-premium-1-bedroom-apartment-in-westlands/ | Thin 1BR card; older **8.8M** floors; Nov 2026 |
| https://www.montbleu.co.ke/ | **Montbleu** — different scheme (Muthithi / Plot 37) |
| https://cribhunter.africa/property/marina-bay-square/ | Mixed Phase 1 rent + Phase 2 table; thin vs GNA/Farman |
| Musilli / Azipa Phase 1 sale-rent cards | Stale or Phase 1 — not Phase 2 authority |
| LinkedIn “Marina 2 – Block A, B & C” sea/mountain viz | Different product geography — reject |

**sources_evaluated 14 · sources_retained 9**

---

## 7. Open questions

1. **`needs_developer_input`:** Official **M-Group** Phase 2 page / brochure / LOO (prices, payment, contacts, SPV).  
2. **`needs_developer_input`:** Confirm whether Phase 2 contracts under **Marina Bay Square Development Ltd** (Phase 1 EIA) or a **separate** entity — **do not assume**.  
3. **`needs_verification`:** Live price list — GNA/Farman/Craiova **~14.45–23.95M** vs Sydia **higher** floors vs A-list/Masterways **anomalous 130 sqm ~9.4–10M**.  
4. **`needs_verification`:** 1BR **sold out** (Farman/Sydia) vs Hauzisha/GNA still marketing **from ~9M**.  
5. **`needs_verification`:** Completion **Dec 2026** vs GNA **Q1 2027** occupation vs Realtors **Nov 2026**.  
6. Confirm **18 floors** / block count / total units.  
7. Exact plot / GPS on Sports Road (Phase 1 EIA is **L.R. 1870/X/34** Osieli×Sports — Phase 2 parcel unknown).  
8. Official sales phone/email/address — agent-only this pass.

---

## 8. Anti-merge

- **≠ Marina Bay Phase 1 / Marina Bay Square** — **Ready to let** (sold out for sale per GNA); **1&2BR** only; junction **David Osieli × Sports Road**; EIA **Marina Bay Square Development Ltd**, **14**-floor / 224-unit scheme. Rental listings (Block, GNA) are Phase 1 — **do not** fold into Phase 2 sale inventory.  
- **≠ Marina Bay 3 / Marina Phase 3** — Hauzisha: studio–4BR, **~6.0–26.9M**, completion **March 2029**; separate dossier later.  
- **≠ Montbleu Westlands** — **Muthithi Road Plot 37**; official face often **Muthithi Square Development Ltd**; completion **~Dec 2027**; different product (montbleu.co.ke). Same-investor forum chatter ≠ merge.  
- **≠ Auris Residence** (DISC-NBO-017) — **Jafu** hotel+residences near Park Inn / Westlands Avenue; studio–2BR from ~**5.5M**; **≠** M-Group Marina Bay Sports Road phases.  
- **≠ Marble West** — portfolio sibling chatter only; different scheme.  
- **≠** coastal / foreign “Marina 2” LinkedIn viz with sea/mountain views.
