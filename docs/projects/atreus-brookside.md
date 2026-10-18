---
slug: atreus-brookside
external_id: DISC-NBO-028
wave: hauzisha-c-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 9
last_verified_at: 2026-10-17
inventory_class_intent: off_plan
---

# Atreus Brookside (DISC-NBO-028) — discovery research

**Not in seed CSV.** Hauzisha Slice C ([hauzisha-slice-c.md](../discovery/hauzisha-slice-c.md)). **Brookside Grove** off Waiyaki Way, Westlands, Nairobi — **Atreus Ventures Limited** (NEMA EIA proponent), off-plan / under construction claims, completion **~June / July 2027** (agent month conflict; year mostly agrees).

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355** is **Hauzisha only** — **never** Atreus / Sunmon / Lesto.

**Method locks applied:**
- Developer vs agents: developer/official (EIA) agreeing → **canonical** for identity / plot / unit count; agents secondary for commercial claims.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany; **do not** invent Sunmon / Lesto as primary.
- Skip Ready inventory — this project is **`off_plan`** / UC only (not Ready/handed-over).

**≠ Gaia Brookside** · **≠ Brookside Oak** · **≠ Balkis Residences** · **≠ Lesto Residences / Aether** unless proven same parcel — see **§8**. Same Sunmon-cluster attribution traps as [balkis-residences.md](balkis-residences.md).

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Atreus Brookside** | 5 | Multi-agent; Hauzisha; EIA scheme location (Brookside Grove) |
| `aliases` | secondary | ATREUS Brookside; Atreus Brookside Apartments; The Atreus Brookside | 4 | Vorsa; Craiova; GNA; Realtors |
| `status` | secondary | **Off-plan** / **under construction** (agent language). Pakfront **Off-plan**. Hauzisha lists **3** units available — stock count, **not** Ready whole-scheme. **Not** Ready / handed-over | 4 / 3 | Pakfront; Craiova; multi-agent — **`needs_verification`** vs site progress |
| `inventory_class` intent | research queue | **`off_plan`** (instalment marketing; completion mid/late **2027**; residual UC wording). **Not** `ready`. | — | Method lock + Slice C |
| `geography.city` | **CANONICAL** | Nairobi | 5 | EIA; all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** — Brookside enclave | 5 | EIA; Hauzisha; multi-agent |
| `geography.street` | **CANONICAL** | **Brookside Grove** off **Waiyaki Way** (some agents say Brookside Drive — corridor soft) | 5 / 3 | EIA; CPK/agents |
| `geography.lat_lng` | **CANONICAL** soft | **−1.258837, 36.791879** | 5 | NEMA EIA GPS |
| `plot` | **CANONICAL** | **L.R. No. Nairobi/Block 5/244** | 5 | NEMA EIA |
| `primary_developer_id` | **CANONICAL** soft (SPV) | → `dev-atreus-ventures-ltd` — **Atreus Ventures Limited** | 5 | NEMA EIA proponent |
| `project_sales_face` | unknown this pass | **No** dedicated Atreus / project sales microsite recovered | 0 | — |
| `unit_types` | **CANONICAL** soft | EIA: **1BR**; **1BR + Study**; **2BR**; **2BR + Study**; **2BR + DSQ**; **3BR + DSQ**. Agents echo same mix (± “extra space” 2BR label) | 5 / 4 | EIA unit schedule; CPK; Vorsa; Craiova; A-list |
| `size_by_type` | claim set — agent | Dominant agent matrix **65–169 sqm**; alternate sheets diverge — see size table | 3 | Multi-agent — **`needs_verification`** vs LOO (EIA silent on sqm) |
| `total_units` | **CANONICAL** | **198** | 5 | EIA schedule (18+36+18+54+36+36) |
| `building_specs` | **CANONICAL** soft / claim noise | EIA primary: **two** residential blocks; **2** basements + ground + mezzanine parking; residential **2nd–19th** floors; rooftop pool / gym / children / garden. Same EIA also has boilerplate “three blocks / five basements / eighteen levels” elsewhere → treat primary schedule as preferred; flag conflict | 4 / 1 | EIA §exec + §4.1 vs stray boilerplate — **`needs_verification`** |
| `price_claims[]` | multi | See **§1a** — **no developer price list**; floors ~**8.4–8.5M** dominate | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all agents |
| `payment_plan` | secondary must-have (**≥4 agents**; no developer %) | See **§1b** | 3 | A-list; Craiova; Realtors; GNA (+ peers) |
| `completion_estimate` | claim set | **June 2027** vs **July 2027** vs **Q3 2027** vs **Q4 2027** (year mostly **2027**) | 3 / 2 | Vorsa/Masterways/Realtors vs CPK/Craiova/Hauzisha/Pakfront vs A-list vs GNA |
| `amenities` (core) | secondary consensus | Rooftop pool / infinity pool; gym; sauna / wellness; sky lounge / rooftop garden; kids play; borehole; backup generator; CCTV / 24/7 security; parking; high-speed lifts; retail / café (many agents) | 4 | EIA rooftop set; multi-agent |
| `amenities` soft extras | secondary — **`needs_verification`** | Concierge; smart home; game room; zen garden; on-site shops (agent-only density varies) | 2 | Pakfront; Craiova; Hauzisha amenity list |
| `roi_claim` | secondary marketing | Vague “high rental demand / appreciation” — no quantified developer ROI | 1–2 | CPK; Vorsa — **`needs_verification`** |
| `early_bird` | secondary | CPK: prices rise **KES 500,000** after pre-sale | 2 | CPK only — **`needs_verification`** |
| `legal_title` | claim set | EIA: land “registered in the name of the **proponent**” (exec) vs “**Joint Venture Partner**” + CR12 (§4.3) | 2 | EIA internal — **`needs_developer_input`** / title pack |
| `master_planned_community` | none | Standalone Brookside Grove scheme | — | — |

### Size table (retained agent claims; EIA has counts, not sqm)

| Type | Dominant agent band (sqm) | Alternate claims | Role |
|------|--------------------------:|------------------|------|
| 1BR | **65** | Splendor/search sheet **71–79**; A-list **769 sqft (~71)** | Agent |
| 1BR + Study | **73** | A-list **846 sqft (~79)** | Agent |
| 2BR | **88** / **101** / **105** (“extra”) | A-list **983 / 1108 / 1151 sqft**; Realtors aligns 88–105 | Agent |
| 2BR + Study | **112** (some cards **105–112**) | A-list **1219 sqft**; Craiova newer from **15.08M** at 112 | Agent |
| 2BR + DSQ | **132** | Splendor band **91–131**; A-list **1415 sqft** | Agent |
| 3BR + DSQ | **169** | Splendor **163**; A-list **1750 sqft**; Hauzisha upper **169** | Agent |
| Hauzisha portal span | **65–169** | — | Portal |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No prices on EIA / no developer sales site** this pass → commercial “from” figures are **agent/portal only** → show + **`needs_verification`**. Lead marketing floor ~**KES 8.4–8.5M**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | 1BR **65 from KES 8.4M**; 1BR+Study **73 from 9.5M**; 2BR **88 from 11.5M** / **101 from 13M**; 2BR+Study **105–112 from 13.5M**; 2BR+DSQ **132 from 16.5M**; 3BR+DSQ **169 from 22.5M**; +**500k** post pre-sale | Typed matrix; July 2027 | CPK | 3 | Agent · floor **8.4M** · **`needs_verification`** |
| B | Same size ladder as A with 1BR floor **8.5M**; 2BR+Study split **105 @ 13.5M** / **112 @ 14.5M**; 3BR+DSQ **22.5M** | Typed matrix; June/July 2027 | Vorsa; Craiova (Jan 2026 page); Masterways; Realtors; GNA | 3 | Dominant **8.5M** reprint |
| C | 1BR **769 sqft from 8.4M**; 1BR+Study **846 from 9.3M**; 2BR **983/1108/1151 from 11 / 12.5 / 13M**; 2BR+Study **1219 from 14M**; 2BR+DSQ **1415 from 16M**; 3BR+DSQ **1750 from 20.3M** | Sqft card; Q3 2027 | A-list | 3 | Lower mid/upper vs B · **`needs_verification`** |
| D | 2BR **88–105 from 11.88M**; 2BR+Study **112 from 15.08M**; 2BR+DSQ **132 from 16.54M**; 3BR+DSQ **169 from 23.28M** | Newer typed 2/3BR pages; July 2027 | Craiova (Aug 2026 updates) | 3 | Above B on several rows · claim-set drift |
| E | 1BR **71–79 from 7.9–8.8M**; 2BR+DSQ **91–131 from 10.5–15.5M**; 3BR+DSQ **163 from 19.8M** | Compressed alternate sheet; June 2027 | Splendor (search extract); overlapping Realtors older copy in web index | 2 | Diverges from A/B sizes · **`needs_verification`** |
| F | Band **KES 8.2M – 23.3M**; sizes **65–169**; July 2027; **3** units available | Portal card | Hauzisha | ≤2 | Aggregator; phone is portal |
| G | From **KES 8.5M**; July 2027; Off-plan | Project card | Pakfront | ≤2 | Thin; payment outlier (§1b) |
| H | From **KES 8.5M**; occupation **Q4 2027** | Agent card | GNA | 3 | Completion outlier vs June/July |

**Portal scalar:** none. Prefer retaining **A/B** as densest typed claim sets; resolve vs LOO before any product “from” field. Do **not** collapse 8.4 vs 8.5.

### 1b. Payment plan — must-have **met via ≥4 agents** (no developer %)

| Element | Agreeing independent sources | Count | Status |
|---------|------------------------------|------:|--------|
| **~20% deposit** + balance in instalments during construction / to completion | A-list (**20% / 80%**); Realtors; GNA; Craiova (**20% / 70% / 10%**); Splendor (search: 20% + construction) | **≥4** | Must-have at conf **3**; **`needs_verification`** vs LOO — **not** on EIA / no sales site |
| Dense **20% / 70% construction / 10% completion** | Craiova (multiple unit pages) | 1 publisher | Show as agent detail · **`needs_verification`** |
| **20%** then **80%** instalments to completion | A-list | 1 | Claim-set vs Craiova 20/70/10 |
| Pakfront “**10%** on reservation” + flexible to completion | Pakfront alone | 1 | **Outlier** vs 20% cluster — do not promote (same trap as Balkis) |
| Developer / EIA % schedule | — | 0 | **unknown** this pass |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-atreus-ventures-ltd` |
| `legal_name` | **Atreus Ventures Limited** |
| `trading_names` | Atreus Ventures Limited; project brand **Atreus Brookside** |
| `website` | **None found** this pass (no corporate / project sales site recovered) |
| `evidence` | NEMA EIA Study Report **NEMA/EIA/SR/3416** (proponent block + certification); P.O. Box **25389-00100**, Nairobi |
| `group_company_id` | **null** — none invented. Hauzisha **Sunmon Group** / **Lesto Residence Developer** faces → **RelatedParty only** until SPA / Companies Registry / LOO proves link |
| `sales_office` | **Unknown** this pass (agent phones only; Hauzisha **0730** is portal) |
| `confidence` | **5** EIA legal SPV · **0** sales face / trading website · **0** Sunmon/Lesto as primary |

**Do not** treat CPK, Vorsa, Craiova, A-list, Masterways, Realtors, GNA, Pakfront, Splendor, or Block as the developer.

**Never** assign **0730 731 355 / +254 730 731 355** to Atreus Ventures.

---

## 3. GroupCompany

**None invented.** No parent / holding company evidenced beyond unverified Hauzisha “Sunmon Group” / “Lesto Residence Developer” labels (conf **2**, portal-only — same pattern as Balkis).

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| **Sunmon Group** | claimed developer / portfolio face (Hauzisha) | Hauzisha developers hub lists Atreus Brookside under Sunmon; live development page has flip-flopped between Sunmon FAQ and Lesto face across crawls | 2 — **RelatedParty until proven**; **not** primary |
| **Lesto Residence Developer** | claimed developer face (Hauzisha) | Alternate Hauzisha attribution on Atreus Brookside card/FAQ in some crawls; **≠** Lesto Residences (Ojijo Close) product | 2 — **RelatedParty until proven** |
| Hauzisha | portal claiming direct developer feed | Attributes Sunmon and/or Lesto; **0730** phone | 2 for developer ID only |
| Joint Venture Partner (unnamed) | possible land title party | EIA §4.3 ownership + CR12 reference vs exec “proponent” ownership | 2 — **`needs_developer_input`** |
| Selling agents (sample) | agents | Independent listing pages | 3 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Typed **8.4M** matrix; July 2027; early-bird +500k note |
| Vorsa Group | Typed **8.5M** matrix; June 2027 |
| Craiova Realtors | Typed **8.5M** matrix + newer higher 2/3BR asks; **20/70/10** payment; July 2027 |
| A-list Real Estate | Sqft/price sheet (lower mid); **20/80** payment; Q3 2027 |
| Masterways | Compressed **8.5–22.5M** bands; June 2027 |
| Realtors Platform | **8.5M** typed ladder; **20%** deposit + construction; June 2027 |
| GNA Real Estate | **8.5M** ladder; **20%** deposit; **Q4 2027** occupation |
| Pakfront | From **8.5M**; July 2027; Off-plan; **10%** reservation outlier |
| Hauzisha | **8.2–23.3M**; July 2027; Sunmon/Lesto attribution — portal only |

---

## 6. Sources

### Retained (≥5 rule; always keep official/EIA when found)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://nema.go.ke/wp-content/uploads/2025/03/EIA-2269-SR-3416-ATREUS-VENTURES-LTD-min.pdf | NEMA / Atreus Ventures Ltd | **official EIA** | Proponent **Atreus Ventures Limited**; Block **5/244**; GPS; **198** units; block/storey schedule; amenities; no prices/payment |
| 2 | https://hauzisha.co.ke/developments/atreus-brookside/ | Hauzisha | portal | **8.2–23.3M**; **65–169** sqm; July 2027; Sunmon **and/or** Lesto face (unstable); **ignore 0730 phone** |
| 3 | https://commercialpropertykenya.com/properties/atreus-brookside-apartment-along-brookside-grove-westlands/ | CPK | agent | Densest **8.4M** typed matrix; July 2027; +500k note |
| 4 | https://vorsagroup.co.ke/property/atreus-brookside-1-2-3-bedroom-apartments-brookside-grove-westlands/ | Vorsa | agent | **8.5M** typed matrix; June 2027 |
| 5 | https://craiovarealtors.com/property/the-atreus-brookside-one-two-three-bedroom-apartments/ (+ /atreus-brookside-2-3-br-apartments-in-westlands/) | Craiova | agent | Matrix + **20/70/10** payment; July 2027; newer higher asks |
| 6 | https://a-listrealestate.ke/property/atreus-brookside/ | A-list | agent | Sqft prices; **20/80** payment; Q3 2027 |
| 7 | https://masterways.co.ke/properties/atreus-brookside | Masterways | agent | Compressed bands; June 2027 |
| 8 | https://realtors.co.ke/property/atreus-brookside-apartments-for-sale-in-brookside/ | Realtors Platform | agent | **8.5M** ladder; **20%** + construction; June 2027 |
| 9 | https://gna.co.ke/project/atreus-brookside-1-2-and-3-bedrooms-plus-dsq-in-westlands/ | GNA | agent | **8.5M** ladder; **20%** deposit; **Q4 2027** |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://www.pakfront.co.ke/projects/atreus-brookside | Useful Off-plan / July 2027 / **10%** payment outlier — noted in §1b; not retained as authority (≥ conf 3) |
| https://splendorholdings.co.ke/properties/atreus-brookside/ | Fetch timeout this pass; search extract = alternate **7.9–19.8M** sheet — logged as claim **E** only |
| https://hauzisha.co.ke/developers/ (Sunmon card) | Portfolio attribution only; not a field source |
| https://hauzisha.co.ke/developments/lesto-residences/ | **≠** this scheme — Ojijo Close / Sunmon Lesto product (anti-merge) |
| https://block.ke/property/lesto-residences-westlands-1-2-bedroom-apartments/ | Block low-trust + wrong product (Lesto) |
| Atreus corporate / project microsite | **Not found** this pass |
| sunmon.com | Unrelated industrial site — **not** Kenya Atreus developer (same skip as Balkis) |

**sources_evaluated ~12 · sources_retained 9**

---

## 7. Open questions

1. Confirm **SPA / LOO contracting entity** = **Atreus Ventures Limited** vs any Sunmon / Lesto / other sales face.  
2. Resolve Hauzisha **Sunmon vs Lesto Residence Developer** attribution (RelatedParty only until proven).  
3. Publish **current price list** from developer (none official this pass) — retire or keep **8.4 vs 8.5** floors and Craiova **11.88–23.28M** drift.  
4. Lock **payment %** (A-list **20/80** vs Craiova **20/70/10** vs Pakfront **10%**).  
5. Lock **completion month**: June vs July vs Q3 vs Q4 **2027**.  
6. Resolve EIA **title** wording: proponent vs **Joint Venture Partner** + CR12.  
7. Confirm **storeys / basements / block count** (EIA primary vs boilerplate conflict).  
8. Obtain **sqm schedule** from LOO (EIA silent; agents **65–169** dominant).  
9. Construction progress / inventory_class confirm (`off_plan` vs `building`).

---

## 8. Anti-merge

- **≠ Gaia Brookside (DISC-NBO-021)** — **Wonder Properties**; **Brookside Gardens Drive**; Gaia / Gaia Brookside Forest branding; different developer + street.  
- **≠ Brookside Oak (DISC-NBO-006)** — **Muguga Green** / Oak Developer; different product and plot family.  
- **≠ Balkis Residences (DISC-NBO-010)** — **Riverside Grove / Riverside Drive**; Balkis brand site; same Hauzisha **Sunmon** cluster trap but **different scheme** ([balkis-residences.md](balkis-residences.md)).  
- **≠ Lesto Residences** — **Ojijo Close**, Westlands; Hauzisha Sunmon **Lesto** product (~96 units / 14 floors) — **not** Atreus Brookside even when Hauzisha mislabels Atreus as “Lesto Residence Developer”.  
- **≠ Aether** (Sunmon hub sibling on Hauzisha) — do not merge without parcel proof.  
- **≠ Oasis Brookside One / Forest One / Riverside One** — Oasis “One” family; different developer.  
- **≠ Gemini Residency** (also Brookside Grove / Matundu corridor on some portals) — separate scheme.
