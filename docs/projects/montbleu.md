---
slug: montbleu
external_id: DISC-NBO-026
wave: hauzisha-c-2026-10-17
pilot: false
sources_evaluated: 14
sources_retained: 9
last_verified_at: 2026-10-17
inventory_class: off_plan
---

# Montbleu Westlands (DISC-NBO-026) — discovery research

**Not in seed CSV.** Hauzisha Slice C ([hauzisha-slice-c.md](../discovery/hauzisha-slice-c.md)). **Plot 37, Muthithi Road**, Westlands, Nairobi — off-plan / under construction, completion **Nov / Dec 2027**.

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never assign to developer / SPV.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- **No invented `primary_developer`.** Hauzisha says **M-Group Developer**; official project site names **Muthithi Square Development Ltd** → flag conflict → **`needs_developer_input`**. Model M-Group as **`RelatedParty` / marketing_partner** until proven.
- Skip Ready inventory — this project is **Off-plan / UC** only.

**≠** Marina Bay (any phase); **≠** Marble West — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Montbleu Westlands** | 5 | montbleu.co.ke; Hauzisha; CPK; Citiscape |
| `aliases` | secondary | MontBleu; Montbleu Apartments; Montbleu Residences; Montebleu (agent typo); Muthithi Square (forum/marketing alias — **not** a separate scheme) | 3–4 | Agents; SkyscraperCity; official “Developer” label |
| `status` | **CANONICAL** soft | **Off-plan / under construction** — agent “under construction”; construction start cited **Nov 2024**; completion **2027** | 4 | Craiova; Musilli timeline; Flamingo; Hauzisha |
| `inventory_class` | **CANONICAL** soft | **`off_plan`** (UC / not Ready-tagged) | 5 | Method + all retained sources |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** | 5 | Official; all agents |
| `geography.street` | **CANONICAL** | **Muthithi Road** — Plot **37**; marketing: opp. Hyatt Regency / near GTC, Kempinski, Sarit | 5 | Hauzisha; CPK; Citiscape; GoAfrica |
| `geography.plot` | **CANONICAL** soft | **Plot 37, Muthithi Road** | 5 | Hauzisha; CPK |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **UNRESOLVED** | **null this pass** — **`needs_developer_input`** (official **Muthithi Square Development Ltd** vs Hauzisha **M-Group Developer**) | 0 | See **§2** |
| `unit_types` | **CANONICAL** soft | **Standard 1BR** (Type B & F); **Premium 1BR** (Type C & G); **Standard 2BR** (Type D & H); **Premium 2BR + DSQ** (Type A & E) | 5 / 4 | montbleu.co.ke floor-plan labels; Citiscape typed types |
| `size_by_type` | claim set — see table | **60 / 61 / 104 / 116 sqm** (gross) — stable across official + agents | 5 / 4 | Official 60 sqm Type B&F; multi-agent typed cards |
| `total_units` | unknown this pass | — | 0 | not stated on retained pages |
| `building_specs.storeys` | secondary — official | **23** floors (montbleu.co.ke amenity chip) | 4 | Official site |
| `building_specs` other | secondary | **4** high-speed lifts; rooftop pool + gym; sky lounge; borehole; solar water heating; backup power; hotel-style amenities | 4–5 | Official amenity grid; Citiscape; CPK |
| `price_claims[]` | multi | See **§1a** — **no official price list** on montbleu.co.ke this pass; agent sheets span **~6.75M → ~15.45M** by vintage | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan` | secondary — must-have **triggered** (dense agents) but **structure not locked** | See **§1b** — competing **10/10/75/5** vs **20% + balance / 3 years** shapes → **`needs_verification`** | 3 | Musilli; Craiova; Citiscape; CPK; Sydia |
| `completion_estimate` | claim set | **November 2027** vs **December 2027** — agree year; month soft | 4 / 3 | Musilli; Sydia; CIG; Flamingo vs Hauzisha; CPK; Craiova |
| `amenities` | **CANONICAL** soft | Rooftop pool; rooftop fitted gym; sky lounge; children’s play area; conference room; reception lobby; social clubhouse; restaurant café; mini-mart; spa/salon space; 4 high-speed lifts; CCTV; smart access; borehole; solar water heating; power backup; car parking; smart-home features | 5 | montbleu.co.ke; Citiscape amenity list |
| `roi_claim` | secondary marketing | CPK “recover investment in as fast as **6 years**”; Flamingo rental-yield language — unquantified / agent — **`needs_verification`** | 2 | CPK; Flamingo |
| `legal_title` | soft — agent | Main title **leasehold 99 years from 1 Apr 2003**; change of use for multi-dwelling; sectional titles on completion (agents) — **`needs_verification`** vs LOO | 3 | Musilli; CPK |
| `master_planned_community` | none | Standalone Muthithi Road tower (not a named masterplan precinct) | — | — |

### Size table (retained)

| Type | Size | Role | Conf |
|------|-----:|------|-----:|
| Standard 1BR (Type B & F) | **60 sqm** | Official floor-plan card + multi-agent | 5 |
| Premium 1BR (Type C & G) | **61 sqm** | Multi-agent typed; aligns with official “Premium One Bedroom” | 4 |
| Standard 2BR (Type D & H) | **104 sqm** | Multi-agent | 4 |
| Premium 2BR + DSQ (Type A & E) | **116 sqm** | Multi-agent | 4 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No developer price list** on montbleu.co.ke this pass → all asking prices are agent / portal claims → **`needs_verification`**. Sheets show clear vintage inflation from late-2024 floors (~**6.75–6.95M**) through mid-band (~**7.15M**) to 2026 agent ranges from **~8.15M** (matches Hauzisha narrative “from 8.15 million”).

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Std 1BR **60** from **6.75M**; Prem 1BR **61** **6.95M**; Std 2BR **104** **11.85M**; Prem 2BR **116** from **12.95M** | Early typed sheet (updated Nov 2024) | Musilli Homes | 3 | Oldest floor retained |
| B | Std 1BR **60** from **6.95M**; Prem **61** **7.15M**; Std 2BR **104** **11.95M**; Prem 2BR+DSQ **116** **13.05M** | Typed typology + Type letters | Citiscape | 3 | Dense shared mid-sheet |
| C | Same shape as B: **6.95 / 7.15 / 11.95 / 13.05** | Typed bands | Flamingo; Lumi Realty | 3 | Aligns with B |
| D | **7.15 / 7.35 / 11.95 / 13.05**; Plot 37; Dec 2027 | Typed + location | CPK Real Estate | 3 | Prem 1BR **+0.2M** vs B |
| E | **7.15 / 7.35 / 11.95 / 13.05**; completion Nov 2027 | Typed | Sydia Realty | 3 | Same as D |
| F | 1BR band **6.95–7.15**; 2BR **11.95–13.05** (compressed) | Marketing band | Splendor Holdings (search/snippet); Flamingo hero | 3 | Collapses A–C |
| G | Std 1BR **8.15–9.15**; Prem **8.35–9.35**; Std 2BR **12.95–13.95**; Prem **13.95–14.95**; Dec 2027 | Higher range card (updated Feb 2026) | Craiova Realtors | 3 | Matches Hauzisha “from 8.15M” narrative |
| H | Std 1BR **8.65–9.65**; Prem **8.85–9.85**; Std 2BR **13.45–14.45**; Prem+DSQ **14.45–15.45**; Nov 2027 | Highest typed ranges (page updated Oct 2026); **hero card still Ksh 6.95M** | Realtors Platform | 3 | Hero vs body conflict — **`needs_verification`** |
| I | Narrative “prices starting from **8.15 million**”; card **KES 12.9M**; sizes **60–116 sqm**; Dec 2027 | Portal development page | Hauzisha | ≤2 | Aggregator; **ignore 0730 phone** |
| J | 1BR **60** **6.95M**; 2BR **116** **16.0M** (compressed / anomalous 2BR) | Thin table | CIG Real Estate | 2 | 2BR **16M** outlier vs all other sheets |
| K | Block project hub “Montbleu Residences” | Aggregator | block.ke | ≤2 | Discovery only — **not authority** |

**Portal scalar:** none. Do **not** publish a single “from” until sales LOO confirms current stock; treat **6.75–6.95M** sheets as likely stale vs **8.15M+** 2026 cards.

### 1b. Payment plan — must-have **triggered** (≥4 agents publish *a* plan) but **no single structure locked**

Official montbleu.co.ke is **silent** on instalments this pass. Agents disagree on deposit shape:

| Element | Source | Status |
|---------|--------|--------|
| Cash: **10%** booking + **10%** on sale agreement + **75%** during construction + **5%** on completion | Musilli; Craiova | Secondary consensus (conf **3**) — **2** independents only |
| Mortgage path: **10%** booking + **20%** on agreement + **70%** on completion via mortgage | Musilli | Single agent |
| **20%** deposit; balance within **3 years** at **0%** interest | Citiscape | Competing shape |
| **10%** deposit; balance over **3-year** construction period | CPK | Thin / incomplete vs Musilli split |
| **20%** initial deposit; balance to Nov 2027 | Sydia | Competing **20%** family |
| Official Montbleu payment schedule | — | **Not published** this pass |

**Must-have met?** **Structure not locked** — need developer LOO **or** ≥4 independents echoing **one** schedule. Flag **`needs_verification`**.

---

## 2. Developer — SPV resolution (**unresolved**)

| Field | Value |
|-------|-------|
| `id` | **null this pass** — do **not** invent `dev-m-group` or `dev-muthithi-square` as primary |
| `legal_name` | **Muthithi Square Development Ltd** — named on **official** project site as “Developer”; Companies Registry string / sale-contract SPV **not** independently verified this pass |
| `trading_names` | **Montbleu** (project brand); Hauzisha trading attribution **M-Group Developer** (unproven as contracting entity) |
| `website` | https://www.montbleu.co.ke/ (project official) |
| `evidence` | Official Team: “Developer — **Muthithi square development ltd**”; Hauzisha: “by **M-Group Developer**” + FAQ “developed by M-Group Developer”; seed shortlist notes entity conflict; SkyscraperCity OP claims same investors as Marina Bay / Marble West and “also known as Muthithi Square” (anecdotal, conf **1**) |
| `group_company_id` | **null** — none invented; do **not** assume M-Group parent of Muthithi Square |
| `sales_office` / contacts | **+254 707 599 999**; **sales@montbleu.ke** / **sales@montbleu.co.ke** (official site). GoAfrica directory: Plot 37 Muthithi Rd, Nairobi 00800; same phone family |
| `confidence` | **5** official SPV *label* on project site / **0** primary_developer lock / **2** M-Group as RelatedParty only |

### Resolution rule (this pass)

1. Keep **`primary_developer_id` null** + **`needs_developer_input`**.  
2. Treat **Muthithi Square Development Ltd** as **named official face / likely legal SPV** (RelatedParty or future Developer row when registry + LOO confirm).  
3. Model **M-Group Developer** as **`marketing_partner` / RelatedParty** (Hauzisha attribution; Marina Bay / Marble West cluster association **unproven** for this SPV).  
4. **Never** invent a winner between M-Group and Muthithi Square.

**Never** assign **0730 731 355 / +254 730 731 355** to Muthithi Square, M-Group, or Montbleu sales — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.** Forum claim that Marina Bay / Marble West / Montbleu share “same investors” is **not** elevated to a GroupCompany row this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| **Muthithi Square Development Ltd** | **named developer / likely SPV** (unverified registry) | montbleu.co.ke Team “Developer” | 4 label / **0** primary lock — **`needs_developer_input`** |
| **M-Group Developer** | **`marketing_partner`** / portal face (unproven) | Hauzisha development + developer directory; Slice C seed | 2 — **`needs_developer_input`** |
| **KARIM CG VISUALS** | development concept & marketing design | montbleu.co.ke Team (“Powered by karimcg\|\|visuals”) | 4 |
| CPK / Citiscape / Musilli / Craiova / Flamingo / Lumi / Sydia / Realtors / CIG | selling agents | Independent listing pages | 3 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Citiscape Valuers | Typed **6.95–13.05M** + Type letters; **20% / 3yr 0%** payment |
| CPK Real Estate | Plot 37; **7.15–13.05M**; Dec 2027; **10%** + 3yr balance; title claim |
| Musilli Homes | Oldest typed **6.75–12.95M**; full **10/10/75/5** + mortgage path; Nov 2024–Nov 2027 timeline |
| Craiova Realtors | Higher **8.15–14.95M** ranges; Dec 2027; **10/10/75/5** |
| Flamingo Real Estate | Mid-band **6.95–13.05**; handover Dec 2027 |
| Lumi Realty | Mid-band typed; hosts “Montbleu_Westlands_brochure” document link |
| Sydia Realty | **7.15–13.05**; Nov 2027; **20%** deposit language; site-update Aug 2025 |
| Realtors Platform | Highest 2026 ranges; stale hero **6.95M** |
| Hauzisha | M-Group attribution; Plot 37; from **8.15M**; Dec 2027 — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.montbleu.co.ke/ | Muthithi Square / Montbleu project | developer | Official face; floor-plan types; 23 floors; amenities; **Developer = Muthithi square development ltd**; **+254707599999**; sales@montbleu.ke; KARIM CG |
| 2 | https://hauzisha.co.ke/developments/montbleu-westlands/ | Hauzisha | portal | Plot 37; M-Group; from 8.15M; Dec 2027; 60–116 sqm — conf ≤2; **ignore 0730 phone** |
| 3 | https://citiscapevaluers.com/property/montbleu-westlands/ | Citiscape | agent | Densest typed typology + Type A–H; payment **20%/3yr** |
| 4 | https://commercialpropertykenya.com/properties/montbleu-apartment-to-buy-in-westlands/ | CPK | agent | Plot 37; Dec 2027; **7.15–13.05M**; title lease claim |
| 5 | https://musillihomes.co.ke/property/montbleu-apartments/ | Musilli Homes | agent | Early prices; **10/10/75/5** + mortgage; Nov 2024 start / Nov 2027 |
| 6 | https://craiovarealtors.com/property/montebleu-westlands-1-2-bedrooms/ | Craiova Realtors | agent | Higher **8.15M+** sheet; Dec 2027; **10/10/75/5** |
| 7 | https://www.flamingorealestate.co.ke/property/montbleu-apartments-in-westlands-luxury-living-awaits/ | Flamingo | agent | Mid-band prices; Dec 2027 handover; UC |
| 8 | https://lumirealty.co.ke/estate_property/montbleu-westlands-1-2-bed-apartments/ | Lumi Realty | agent | Mid-band; brochure document reference |
| 9 | https://sydiarealty.com/estate_property/montbleu-residences-refined-urban-living-in-westlands/ | Sydia Realty | agent | **7.15–13.05**; Nov 2027; **20%** deposit; Aug 2025 site update |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/project/montbleu-residences/ | Low-trust / empty project hub — discovery seed only |
| https://realtors.co.ke/property/montbleu-apartments-on-muthithi-road-westlands/ | Useful high-range prices but hero **6.95M** vs body conflict; payment % missing — overlap with Craiova vintage |
| https://cig.co.ke/properties/montbleu | Thin; anomalous 2BR **16M** |
| https://splendorholdings.co.ke/properties/montbleu-westlands/ | Fetch timeout / overlap mid-band |
| https://www.goafricaonline.com/ke/1233699-montbleu | Directory contact corroboration only (Plot 37 + phone) |
| https://www.skyscrapercity.com/threads/montbleu-westlands-25-fl-u-c.2428289/ | Forum anecdote (investor cluster / Muthithi Square alias) — not authority |
| https://villawatchkenya.com/listing/montbleu-westlands-apartments/ | Thin marketing echo |

**sources_evaluated ~14 · sources_retained 9**

---

## 7. Open questions

1. **`needs_developer_input` — primary developer / SPV:** Confirm whether **Muthithi Square Development Ltd**, **M-Group Developer**, both (co-dev / parent–SPV), or another entity contracts sales. Do **not** invent a winner.  
2. Confirm **current** price list vs agent vintage (**6.75–6.95M** → **8.15M+**).  
3. Obtain **official payment schedule** (LOO) — resolve **10/10/75/5** vs **20% + 3yr** conflict.  
4. Lock completion month: **November** vs **December 2027**.  
5. **Total units** / blocks / basement count.  
6. Companies Registry string for Muthithi Square Development Ltd; any registered link to M-Group.  
7. Verify agent leasehold **99 years from 1 Apr 2003** claim against mother title / LOO.

---

## 8. Anti-merge

- **≠ Marina Bay / Marina Bay 2 / Marina Bay 3** (M-Group Hauzisha cluster — **Sports Road** / different phases; do **not** merge because of shared portal developer label).  
- **≠ Marble West** (separate M-Group Hauzisha Westlands product — different scheme).  
- **≠ “Muthithi Square” as a second project** — treat as **alias / SPV face** for Montbleu on Plot 37 until proven otherwise.  
- **≠ Skye Towers** (forum: prior unbuilt proposal on same Plot 37 — historical only).  
- **≠** other Muthithi Road towers (e.g. GTC Residence) — different products.
