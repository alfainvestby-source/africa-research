---
slug: only-you
external_id: DISC-NBO-020
wave: hauzisha-b-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-17
inventory_class_intent: building
---

# Only You / Onlyou (DISC-NBO-020) — discovery research

**Not in seed CSV.** Hauzisha Wave B ([hauzisha-developers-2026-10-16.md](../discovery/hauzisha-developers-2026-10-16.md) GLBC section; [hauzisha-wave-b-prep.md](../../internal/hauzisha-wave-b-prep.md)). **Elgeyo Marakwet Road / Elgeyo Road**, Kilimani, Nairobi — **Nairobi/Block 17/287** — branded **Onlyou Elgeyo** / **Only You**, **under construction**, handover marketed **December 2026** (Hauzisha + multi-agent) vs some agents **Q1 2027**.

Live research accessed **2026-10-17**. **Block.ke ignored as authority**. **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355** is **Hauzisha only** — **never** attribute to Onlyou / GLBC / SPV.

**Method locks applied:**
- Prefer **official microsite** ([onlyounairobi.com](https://onlyounairobi.com/)) + **NEMA EIA** for canonical identity / plot / unit counts.
- Developer vs agents: developer/official agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar). Official microsite **silent on prices** this pass.
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- **No invented `primary_developer`.** Hauzisha says **GLBC Group**; EIA proponent + land title = **Onlyou Investments Limited** → flag conflict → **`needs_developer_input`**. Model GLBC as **`marketing_partner` / RelatedParty** until proven.
- Skip Ready inventory — this project is **building / UC** only (not Ready/handed-over).

**≠ Libra Residences** (GLBC, George Padmore); **≠ GLBC Gemini Hub / Gemini Residences** (Syokimau / Mombasa Rd); **≠ Staroot Gemini Residency Phase 2** (NBO-009) — see **§8**.

**`inventory_class` intent:** **`building`** (multi-agent “under construction”; NRE UC chip). Hauzisha / some agents still sell as off-plan residual — **not** `ready`.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Onlyou Elgeyo** (official microsite hero / unit hub) | 5 | onlyounairobi.com |
| `aliases` | secondary | **Only You** (Hauzisha); Onlyou; Onlyou Elgeyo Apartments; OnlyYou Residences Elgeyo | 4 / 3 | Hauzisha; agents |
| `status` | **CANONICAL** soft | **Under construction / off-plan residual sales** — agents “Under Construction”; Hauzisha Dec 2026 handover; **not** Ready / handed-over | 4 | NRE; Vorsa; Azipa; Hauzisha |
| `inventory_class` intent | research queue | **`building`** | — | Method lock |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Official; EIA; all |
| `geography.neighbourhood` | **CANONICAL** | **Kilimani** | 5 | Official; EIA; Hauzisha |
| `geography.street` | **CANONICAL** | **Elgeyo Marakwet Road** / **Elgeyo Road** (agents also “next to Cavina School”) | 5 / 3 | EIA; onlyounairobi.com; Azipa |
| `geography.plot` | **CANONICAL** | **Nairobi/Block 17/287** | 5 | NEMA EIA SR |
| `geography.lat_lng` | secondary (EIA) | **−1.29444444, 36.77886111** (EIA “lat / log”) — geo agent may refine | 4 | EIA §3.2 |
| `primary_developer_id` | **UNRESOLVED** | **null this pass** — **`needs_developer_input`** (Hauzisha GLBC vs EIA Onlyou Investments Limited; GLBC portfolio omits this project) | 0 | See **§2** |
| `legal_spv_candidate` | secondary (EIA) | **Onlyou Investments Limited** — EIA proponent + registered land owner (P.O. Box 26604–00100 Nairobi) — **not** auto-promoted to trading `primary_developer` | 5 | EIA title / §3.3 |
| `unit_types` | **CANONICAL** soft (EIA + official typology) | **3BR+DSQ**; **3BR+DSQ PLUS**; **4BR+DSQ**; **4BR+DSQ PLUS**; **5BR+DSQ**; plus **4 / 5 / 6BR penthouses** (EIA) | 5 / 4 | onlyounairobi.com unit cards; EIA mix |
| `size_by_type` | claim set — agents | Typical bands **~205–217 sqm** (3BR); **~276–302 sqm** (4BR); **~358–360 sqm** (5BR); penthouse/duplex up to **~521 sqm** (agent sheets) | 3 | CPK; Vorsa; GNA; Erysler — **`needs_verification`** vs LOO |
| `total_units` | **CANONICAL** soft | **120** housing units | 5 | EIA summary table; Almasi availability echo |
| `building_specs` | **CANONICAL** soft (EIA) | **Three blocks** of **21 floors** each; basement + podium parking (**246** spaces in exec summary / **260** elsewhere in EIA — internal conflict); typical floors 1–19; penthouses 20th + top; roof tanks | 5 / 3 | EIA overview — parking figure **`needs_verification`** |
| `storeys_marketing` | claim set | Agents: **20-storey** (Vorsa; Azipa; Kenya Property) vs **22-storey** (CPK; GNA; NRE) vs EIA **21 floors** × 3 blocks | ≤3 | Flag — **`needs_verification`** |
| `price_claims[]` | multi | See **§1a** — official silent; agent floors **~28–33M** and dense block cards | — | — |
| `currency` | **CANONICAL** soft | **KES** | 5 | All KES listings |
| `payment_plan` | secondary — must-have **partially locked** | See **§1b** — **≥4** agents: **KES 200,000** reservation + **20%** deposit + balance over construction / to Dec 2026; official microsite silent | 3 | Vorsa; Erysler; Azipa; Almasi; Kenya Property |
| `completion_estimate` | claim set | **December 2026** (Hauzisha; CPK; Erysler; Azipa; Almasi) vs **Q1 2027** (NRE; GNA) vs year-only **2026** (Vorsa) | 4 / 3 | Month majority; Q1 minority |
| `amenities` | **CANONICAL** soft | Heated swimming pool; gym + boxing area; 24-hour butler / concierge; Face ID + fingerprint + card access; CCTV | 5 | onlyounairobi.com |
| `amenities` (EIA / agents) | secondary | Playground; management office; restaurant / open-garden café; barbecue; shops; children’s play; rooftop lounge; cinema (agents) | 4 / 3 | EIA ground floor; agents |
| `roi_claim` | secondary marketing | Diplomatic / executive rental demand blurbs — no quantified ROI on official pages | 2 | CPK; GNA — **`needs_verification`** |
| `legal_title` | soft (EIA) | Land registered to **Onlyou Investments Limited**; change of use to multi-dwelling obtained (EIA narrative) — sale-contract SPV still **`needs_developer_input`** | 4 / 0 | EIA §3.3 |
| `master_planned_community` | none | Standalone Kilimani scheme | — | — |

### Unit mix (EIA — retained)

| Housing unit type | Count | Role | Conf |
|-------------------|------:|------|-----:|
| 3-bedroom units | **38** | EIA | 5 |
| 4-bedroom units | **57** | EIA | 5 |
| 5-bedroom units | **19** | EIA | 5 |
| 4-bedroom penthouses | **1** | EIA | 5 |
| 5-bedroom penthouses | **3** | EIA | 5 |
| 6-bedroom penthouses | **2** | EIA | 5 |
| **Total** | **120** | EIA | 5 |

Almasi availability chip (Sep 2026) echoes the same **38 / 57 / 19** apartment counts + top-floor penthouses — secondary corroboration (conf **3**).

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official microsite:** no unit prices this pass. Hauzisha portal band + agent typed sheets only → **no developer “from” price**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Portal band **KES 30.6M – 92.4M**; sizes **205–359 sqm**; **4** units listed | Development card | Hauzisha | ≤2 | Aggregator; **ignore 0730 phone** |
| B | 3BR+DSQ **205 sqm KES 29M**; **217 sqm 31M**; 4BR+DSQ **276 from 39M**; 4BR+study **302 = 41M**; 5BR **360 from 50M**; penthouse duplex **4BR 68M / 5BR 84M / 6BR 92M** (521 sqm) | Typed sheet | CPK | 3 | Completion Dec 2026 |
| C | Block C 3BR **32.5–36.5M** (205/217); Block B 4BR **42.5–46.5M** (276); Block A 4/5BR **42.5–56.5M**; sky 5BR+DSQ **358.5 from 48M**; duplexes **69–120M** | Dense block card | Vorsa Group | 3 | Higher floor than B |
| D | Same block/penthouse shape as C (from **32.5M**) | Agent card | Azipa | 3 | Overlaps C |
| E | 3BR+DSQ **205 from 28M**; 4BR+DSQ **302 from 37.5M**; 5BR+DSQ **358 from 48M** | Compressed “from” | GNA; NRE | 3 | Lowest 3BR floor |
| F | 3BR **216 sqm = 32.5M**; 4BR **302 = 42.4M**; 5BR **359 = 50.7M** | Unit cards | Erysler | 3 | Mid of C/E |
| G | 3BR from **33 / 36M**; 4BR **44 / 48M**; 5BR **54M**; duplexes **70–110M** | Typed + 120 units | Almasi Realty | 3 | Highest apartment floors |
| H | From **KES 30M**; **120** units | Aggregator | Lion Cab Group | ≤2 | Uses **+254 705 818 181** (shared with official / GLBC) |

**Portal scalar:** none. Resolve live LOO before any public `price_from`.

### 1b. Payment plan — must-have **triggered** (≥4 agents); official schedule **not published**

| Element | Source | Status |
|---------|--------|--------|
| **KES 200,000** reservation (often “included in purchase price”) | Vorsa; Erysler; Almasi; Kenya Property (search) | Secondary consensus (conf **3**) |
| **20%** deposit; balance over construction / **~24 months** / through **Dec 2026** | Vorsa; Erysler; Azipa; Almasi | ≥4 independent agents — **must-have met at agent level** |
| Official Onlyou / EIA payment schedule | — | **Not published** this pass → still **`needs_verification`** vs LOO |
| NRE calculator defaults **20%** | nairobirealestate.co.ke | Illustrative tool — does **not** strengthen lock alone |
| Hauzisha “staged across build” FAQ | hauzisha.co.ke | Generic portal copy — ignore |

**Must-have met?** **Yes at ≥4-agent threshold** for **20% + construction balance** (+ reservation fee on several sheets). **Not locked as developer-canonical** until Onlyou LOO / sales pack confirms.

---

## 2. Developer / SPV resolution

| Field | Value |
|-------|-------|
| `primary_developer_id` | **Unresolved** — **`needs_developer_input`** |
| Trading / brand face | **Onlyou** / **Onlyou Elgeyo** via https://onlyounairobi.com/ |
| Official sales contacts (microsite) | **Elgeyo Road, Kilimani**; **+254 705 818 181**; **Info@onlyounairobi.com** |
| Legal SPV (EIA) | **Onlyou Investments Limited**, P.O. Box **26604–00100**, Nairobi — EIA **proponent** + **land ownership** on Block 17/287 |
| Hauzisha attribution | **GLBC Group** — portal only (conf ≤2 for developer identity) |
| GLBC official portfolio | https://www.glbcgroup.co.ke/projects/ lists **Libra, Gemini Residences, Taurus, Aries** — **does not list Only You / Onlyou** this pass |
| Shared phone signal | GLBC contact **(+254) 705 81 81 81** matches Onlyou microsite phone — suggests ops/marketing overlap, **not** proof of primary developer |
| `group_company_id` | **null** — none invented |
| `confidence` | **5** brand microsite / EIA SPV string · **0** on `primary_developer` assignment |

**Do not invent `primary_developer = GLBC`.** Until LOO / Companies Registry / written confirmation resolves the graph:

1. Keep **`primary_developer_id` null** + **`needs_developer_input`**.  
2. Treat **Onlyou Investments Limited** as **legal SPV / land entity** (RelatedParty or future Developer row when trading face is confirmed).  
3. Model **GLBC Group** as **`marketing_partner`** RelatedParty (Hauzisha + shared phone; **not** on GLBC projects page).

**Never** assign **0730 731 355 / +254 730 731 355** to Onlyou, Onlyou Investments Limited, or GLBC.

---

## 3. GroupCompany

**None invented.** No proven parent above Onlyou Investments Limited / GLBC this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| **Onlyou Investments Limited** | legal_spv / land_owner (EIA proponent) | NEMA EIA title, authentication, §3.3 ownership | 5 |
| **GLBC Group** | **`marketing_partner`** (unproven) | Hauzisha “by GLBC Group”; shared **705 818 181** with microsite; **absent** from glbcgroup.co.ke/projects | 2 — **`needs_developer_input`** |
| CPK / Vorsa / Azipa / Erysler / GNA / NRE / Almasi | selling agents | Independent listing pages | 3 |
| Hauzisha | portal | Development export only | ≤2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Typed sizes/prices; Dec 2026; “flexible” payment (no %) |
| Vorsa Group | Dense block + penthouse sheet; **200k + 20% + 24 months** |
| Azipa Real Estate | Same block sheet family; **20%** to Dec 2026 |
| Erysler Realty | Typed unit asks; **200k + 20%** + monthly/quarterly |
| GNA Real Estate | Low “from 28M” sheet; Q1 2027 |
| NRE | Mirrors GNA prices; UC; calculator 20% |
| Almasi Realty | Dense price list + 120-unit availability; **200k + 20%** |
| Hauzisha | GLBC attribution; 30.6–92.4M; Dec 2026 — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://onlyounairobi.com/ | Onlyou (official microsite) | developer/brand | Canonical brand; Elgeyo Road; unit typology 3–5B+DSQ; amenities; **+254 705 818 181**; Info@onlyounairobi.com — **no prices** |
| 2 | https://nema.go.ke/wp-content/uploads/2025/03/EIA-2178-SR-3148-ONLYOU-INVESTMENTS-LIMITED-min.pdf | NEMA / Onlyou Investments Limited | official EIA | Proponent + land owner; Block **17/287**; **120** units; 3×21 floors; GPS; amenities |
| 3 | https://hauzisha.co.ke/developments/only-you/ | Hauzisha | portal | “GLBC Group”; Dec 2026; 30.6–92.4M; 3–6BR — conf ≤2; **ignore 0730 phone** |
| 4 | https://commercialpropertykenya.com/properties/onlyou-elgeyo-apartment-in-kilimani-nairobi-kenya/ | CPK | agent | Typed prices; Dec 2026; 22-storey claim |
| 5 | https://vorsagroup.co.ke/property/onlyou-elgeyo-apartments-3-4-5-bedroom-penthouses-in-kilimani/ | Vorsa Group | agent | Densest block/penthouse prices + **200k/20%/24mo** |
| 6 | https://aziparealestate.co.ke/property/onlyou-elgeyo-3-4-5-bedroom-luxury-apartments-for-sale-in-kilimani-nairobi/ | Azipa | agent | Block sheet; **20%** to Dec 2026; Cavina landmark |
| 7 | https://erysler.co.ke/property/spacious-three-bedroom-unit-dsq-216m%c2%b2-onlyou/ | Erysler | agent | Unit ask + **200k/20%**; Dec 2026 (sibling 4/5BR cards same plan) |
| 8 | https://almasirealty.com/property/onlyyou-residences-elgeyo-kilimani/ | Almasi Realty | agent | Price ladder; 120-unit mix echo; payment; Dec 2026 |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://www.glbcgroup.co.ke/projects/ | **Negative evidence** retained in §2 (Only You absent); not a project source |
| https://gna.co.ke/project/onlyou-elgeyo-apartments-3-4-and-5-beds-plus-dsq/ | Overlaps NRE “from 28M” sheet; thin payment (“flexible”) |
| https://nairobirealestate.co.ke/properties/onlyou | Same price family as GNA; calculator illustrative; “Developer on request” |
| https://kenyaproperty.co.ke/properties/onlyou-elgeyo-apartments-for-sale-in-kilimani-nairobi/ | Payment echo only; thin vs Vorsa/Erysler |
| https://lioncabgroup.com/properties/onlyou-elgeyo-22 | Aggregator; “2025 Year Built” noise; shared 705 phone |
| Erysler 4BR / 5BR sibling URLs | Same payment/plan as retained 3BR card |
| block.ke (if any) | Low-trust — discovery only |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. **`needs_developer_input` — primary developer:** Confirm whether **Onlyou Investments Limited**, **GLBC Group**, both (co-dev), or another trading entity contracts sales. GLBC portfolio omission + shared phone is unresolved.  
2. Obtain **official price list** (microsite silent) — retire or rank agent **28M vs 32.5M vs 33M** floors.  
3. Confirm **payment schedule** on LOO (agent **200k + 20% + construction balance**).  
4. Resolve **storeys** claim set: EIA **21 floors** × 3 vs agent **20 / 22**.  
5. Resolve EIA internal **parking** 246 vs 260.  
6. Companies Registry string / directors linking Onlyou Investments Limited ↔ GLBC (if any).  
7. Live availability vs Almasi “68 of 120” chip (agent — **`needs_verification`**).

---

## 8. Anti-merge

- **≠ Libra Residences** (DISC-NBO-019) — GLBC scheme on **George Padmore Road**, Kilimani; different product / street.  
- **≠ GLBC Gemini Hub / Gemini Residences** — **Syokimau / Mombasa Road** (Gateway / Mwananchi), studio–4BR, GLBC portfolio — **do not** dossier as this wave’s Only You.  
- **≠ Staroot Gemini Residency Phase 2** (NBO-009) — Staroot product; same “Gemini” word only.  
- **≠ Capricorn / other Elgeyo–Kilimani towers** — different developer brands and unit mixes.  
- **≠** any Ready Kilimani resale using “Only You” as a unit nickname without Block **17/287** / Onlyou brand match.
