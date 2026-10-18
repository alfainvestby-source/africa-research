---
slug: grand-premier
external_id: DISC-NBO-029
wave: hauzisha-c-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 8
inventory_class: off_plan
last_verified_at: 2026-10-17
---

# Grand Premier (DISC-NBO-029) — discovery research

**Not in seed CSV / not already dossiered.** Hauzisha Slice C ([hauzisha-slice-c.md](../discovery/hauzisha-slice-c.md)). **Argwings Kodhek Road** / Bernard (Benard) Estate behind Valley Arcade, **Lavington** (Hauzisha corridor label **Kilimani**), Nairobi — **Whitehorse Real Estate** (ex-**AAD Real Estate**); Hauzisha **Coming soon** → process as **`off_plan`**; 1–3BR + duplex marketing.

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only; no Block page retained). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never AAD / Whitehorse.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory when **tagged** Ready / handed-over — Hauzisha tags **Coming soon** (not Ready); Whitehorse homepage does **not** say “handed over” (unlike Ambra). Secondary complete/ready-to-move claims → show + **`needs_developer_input`** on class (do **not** invent Ready-skip).

**≠** AYA Luxury Residence; **≠** Ambra Heights; **≠** Rosewood Park; **≠** Haven Villas — see **§8**.

**`inventory_class` intent:** **`off_plan`** (Hauzisha **Coming soon** → locked Coming-soon map). Strong agent + Whitehorse LinkedIn “ready-to-move / complete” cluster conflicts — **`needs_developer_input`** before promoting to `ready` / Ready-skip.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Grand Premier** (Whitehorse nav also **GRAND PREMIERE**) | 5 / 4 | whitehorserealestate.ke; indexed aad.ke/grand-premier; Hauzisha; CPK; Samambo |
| `aliases` | secondary | Grand Premiere; Grand Premier Apartments; Grand Premier Residence; Grand Premier Apartment-Lavington | 3 | Whitehorse spelling; CJ Luxe LinkedIn; CPK title |
| `inventory_class` | process lock + conflict | **`off_plan`** via Hauzisha **Coming soon**. Agents (CPK “Complete”; kenyaproperty “Completed”; Rayabbay “Year Built **2019**”) + Whitehorse LinkedIn “**ready-to-move**” unit → **`needs_developer_input`** (do not invent Ready) | 4 / 2 | Hauzisha AAD directory; CPK; kenyaproperty; Rayabbay; Whitehorse LinkedIn |
| `status` | claim set — **`needs_developer_input`** | Coming soon / release language (Hauzisha) vs **complete / open to move in** (CPK) vs ready-to-move sales (Whitehorse LinkedIn) vs older Apex “UC → **2021**” | 3 / 3 / 4 / 1 | Hauzisha; CPK; LinkedIn; Apex |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** soft + soft conflict | **Lavington** (Whitehorse; CPK; Samambo; indexed AAD) vs Hauzisha **Kilimani** label | 5 / 2 | Whitehorse wins neighbourhood; Hauzisha Kilimani — **`needs_verification`** |
| `geography.street` | **CANONICAL** soft | **Argwings Kodhek Road** (AAD spelling “Arwings”); Bernard / Benard / “Benerd” Estate behind **Valley Arcade** | 5 / 3 | Indexed AAD; CPK; Rayabbay; Samambo; Apex |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** soft (trading) | → `dev-whitehorse-real-estate` (**ex-AAD Real Estate**). Hauzisha still labels **AAD** | 5 | aad.ke rebrand; whitehorse portfolio; Hauzisha AAD |
| `unit_types` | **CANONICAL** soft | **1BR**; **2BR** (+/− SQ); **3BR** (+/− DSQ); **3BR duplex** (Hauzisha / AAD). Agents also **4BR penthouse + DSQ** (kenyaproperty) — secondary | 5 / 2 | Indexed AAD; Hauzisha; Whitehorse narrative; kenyaproperty penthouse — **`needs_verification`** |
| `size_by_type` | claim set | See size table — Samambo / CPK ~**73.8 / 139.8 / 183–184 sqm**; Apex alternate **74.4 / 143.7**; kenyaproperty **75 / 140 / 175** | 3–4 | Samambo; CPK; Apex; kenyaproperty |
| `total_units` | claim set — conflict | Samambo **156** vs Apex **130** (two-tower gated) — **`needs_verification`** | 2 | Samambo; Apex |
| `building_specs` | secondary | Two towers (agents); CPK **4** high-speed lifts; heated / infinity pool; rooftop lounge / BBQ; gym; borehole; full backup generator; electric fence / 24hr security | 3–4 | Whitehorse amenity narrative; CPK; Samambo; Rayabbay; indexed AAD |
| `price_claims[]` | multi | See **§1a** — official indexed “from **10M**” vs Samambo **12.5 / 19.5 / 25.5M** vs CPK remaining-stock **8.5 / 18 / 23M** vs older Apex ladder | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan` | unknown this pass | See **§1b** — no Grand Premier % schedule recovered; do **not** import AYA’s 4-year 0% | 0 | — |
| `completion_estimate` | claim set — stale / conflict | Apex target **2021**; Kenya Insights dispute narrative expected **Dec 2023** / incomplete as of **Nov 2024** (news, conf low); CPK “now complete” (2025–2026 listing) | 1 / 1 / 3 | Apex; Kenya Insights; CPK — **`needs_developer_input`** |
| `amenities` | **CANONICAL** soft | Rooftop terraces; heated swimming pool; lounge deck; fully equipped gym; exceptional security / convenience (Whitehorse). Agents add BBQ / VIP lounge; solar water heating; high-speed lifts; kids’ play; borehole; generator | 5 / 3–4 | Whitehorse; CPK; Samambo; Rayabbay |
| `amenities` finishes | secondary | Expansive balconies; fitted kitchens; all-en-suite bedrooms (Whitehorse); Turkish interiors / smart home / Bosch (agents) — agent finishes **`needs_verification`** | 5 / 2 | Whitehorse vs CPK / kenyaproperty |
| `roi_claim` | unknown / thin | Investor copy only — no quantified ROI on developer pages | 1 | CPK / kenyaproperty marketing |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Lavington / Argwings scheme | — | — |

### Size table (retained)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| 1BR (Samambo / CPK) | **73.8 sqm** (~794 sqft) | Agent typed | 4 |
| 1BR (Apex) | **74.4 sqm** (~800 sqft) | Older directory | 2 |
| 1BR (kenyaproperty) | **75 sqm** | Completed sheet | 3 |
| 2BR + SQ (Samambo) | **139.8 sqm** (~1,505 sqft) | Agent typed | 4 |
| 2BR (CPK) | **139.8 sqm** | Remaining stock | 4 |
| 2BR (Apex) | **143.7 sqm** | Older directory | 2 |
| 2BR (kenyaproperty) | **140 sqm** | Completed sheet | 3 |
| 3BR + DSQ (Samambo) | **183.4 sqm** (~1,974 sqft) | Agent typed | 4 |
| 3BR + DSQ (CPK) | **183.9 sqm** | Remaining stock | 4 |
| 3BR + DSQ (kenyaproperty) | **175 sqm** | Completed sheet | 3 |
| 4BR penthouse + DSQ | unknown size | kenyaproperty only | 2 — **`needs_verification`** |
| Duplex (product mix) | size unknown this pass | AAD / Hauzisha name duplex; no retained sqm | 0 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

Live Whitehorse homepage has **no** Grand Premier-only typed list (portfolio chrome “Starting from **Ksh 19M**” may span projects). Indexed AAD project page “Starting price **10 M KSH**” is the densest official “from”. Agent ladders diverge sharply → multi-claim only.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Starting price **KES 10M**; 1 / 2 / 3BR + 3BR duplex | Indexed official project page | aad.ke/grand-premier (live **404**/captcha this pass; retained via index) | 4 | Official “from” — marketing era may be stale |
| B | 1BR **73.8 sqm from 12.5M**; 2BR+SQ **139.8 from 19.5M**; 3BR+SQ **183.4 from 25.5M**; **156** units / two towers | Typed agent card | Samambo Housing | 3 | Above A on 1BR floor |
| C | Remaining stock: 1BR **8.5M** (1 unit); 2BR **18M** (3); 3BR+DSQ **23M** (1); **complete / move-in** | Typed remaining-stock sheet | CPK Real Estate | 3 | Below A; complete tag — **`needs_verification`** vs Coming soon |
| D | Sale from **8M**; 1BR **8M** / 2BR **17M** / 3BR+DSQ **23M** / 4BR penthouse **40M**; rent from **75k** | “Completed” portal sheet | kenyaproperty.co.ke | 2 | Aligns C on 3BR; 1BR/2BR floors differ |
| E | From **KES 9.7M** hero; typed **1BR 7.5M / 2BR 14.1M / 3BR 21.2M**; UC→**2021** | Older directory | Apex Business Pages | 2 | Stale UC narrative — **`needs_verification`** |
| F | Whitehorse LinkedIn: 2BR **ready-to-move** for sale/rent (no ask in snippet) | Developer social | Whitehorse Real Estate LinkedIn | 4 | Status signal; price silent |
| G | 2BR ask **KES 15M** | Agent social | CJ Luxe Realtors LinkedIn | 2 | Single typology |
| H | Rayabbay USD **~$66,467** card + Year Built **2019** | Thin agent card | Rayabbay Realtors | 2 | USD convert messy; year conflicts Coming soon |
| I | Whitehorse site chrome “Starting from **Ksh 19M**” | Homepage (not GP-only proven) | whitehorserealestate.ke | 2 | Portfolio-level — **`needs_verification`** |
| J | Hauzisha: no units / no price; **Coming soon** | Portal | Hauzisha | ≤2 | Aggregator; **ignore 0730 phone** |

**Portal scalar:** none. Prefer LOO vs indexed AAD **10M** floor; treat CPK/kenyaproperty **8–8.5M** remaining-stock floors as secondary until developer confirms whether inventory is residual Ready vs still off-plan marketing.

### 1b. Payment plan — must-have **not met**

| Element | Source | Status |
|---------|--------|--------|
| Official Grand Premier instalment / deposit % | — | **Not published** on live Whitehorse home or indexed AAD GP page this pass |
| Hauzisha FAQ “staged across the build… terms vary” | Hauzisha | Portal boilerplate — not a plan |
| AYA “4-year / 0%” | AAD Sankara launch (sibling) | **Do not import** to Grand Premier |
| Agent % schedules | — | **None** recovered this pass |

**Must-have met?** **No** — need developer schedule **or** ≥4 independent agents.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-whitehorse-real-estate` (trading); legacy face `dev-aad-real-estate` |
| `legal_name` | **Unknown** this pass (Companies Registry string not recovered; **do not invent SPV**) |
| `trading_names` | **Whitehorse Real Estate** (current); **AAD Real Estate** (pre-rebrand / Hauzisha still labels AAD) |
| `website` | https://whitehorserealestate.ke/ · rebrand bridge https://aad.ke/ |
| `evidence` | aad.ke “We have Evolved — AAD is now Whitehorse”; Whitehorse home lists **GRAND PREMIER / PREMIERE** in portfolio; Hauzisha developer directory **AAD** + Coming soon card; indexed aad.ke/grand-premier project page |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts (**live**) | **Jahazi Building, James Gichuru Road, 3rd Floor, Lavington, Nairobi**; **+254 704 191919** (same as **0704 191 919** / **+254 704 19 19 19**); **info@whitehorserealestate.ke**; LinkedIn pitch also **sales@whitehorserealestate.ke** |
| `legacy contacts` | Indexed AAD GP page: **sales@aad.ke**; **+254 704 19 19 19**. Prefer Whitehorse emails post-rebrand |
| `confidence` | **5** Whitehorse trading face / **0** legal SPV |

**Never** assign **0730 731 355 / +254 730 731 355** to AAD or Whitehorse — Hauzisha portal only.

---

## 3. GroupCompany

**None invented.** AAD → Whitehorse is a **rebrand / renewed identity**, not a proven parent/subsidiary graph this pass.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| AAD Real Estate | prior trading name / rebrand predecessor | aad.ke homepage; Hauzisha directory; indexed GP page | 5 as prior face |
| AYA / Ambra Heights / Rosewood Park / Haven Villas | sibling Whitehorse / AAD portfolio only | whitehorserealestate.ke; Hauzisha AAD cards | 4 as siblings — **≠** this property |
| CPK / Samambo / Rayabbay / kenyaproperty / CJ Luxe | selling agents / portals | Independent listing pages / posts | 3 |
| Kenya Insights (Nov 2024) investor–delivery dispute naming Grand Premier | news / litigation cover — **not** SPV proof | kenyainsights.com | 1 — **`needs_verification`**; do not treat as developer status authority |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Densest live typed remaining-stock sheet; Argwings / Bernard Estate; **Complete** tag; **8.5 / 18 / 23M** |
| Samambo Housing | Dense typed **12.5 / 19.5 / 25.5M** + sizes; **156** units — live fetch **403** this pass; retained via indexed text |
| Rayabbay Realtors | Argwings; AAD attribution; amenities; Year Built **2019** |
| kenyaproperty.co.ke | Completed / ready-for-occupation sheet; sale + rent bands |
| Hauzisha | AAD attribution; **Coming soon**; 1–3BR + duplex; no units — portal only |
| Whitehorse LinkedIn | Developer social: ready-to-move 2BR; **0704191919**; sales@whitehorse |
| CJ Luxe LinkedIn | 2BR **15M** ask — thin social |
| Apex Business Pages | Older from **9.7M** / typed **7.5–21.2M**; **130** units; UC→2021 |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://whitehorserealestate.ke/ | Whitehorse Real Estate | developer | Live portfolio **GRAND PREMIER** Lavington narrative + amenities; contacts **+254 704 191919**; **info@**; siblings AYA / Ambra / Rosewood / Haven |
| 2 | https://aad.ke/ | AAD → Whitehorse | developer | Live rebrand bridge; same phone + Jahazi / James Gichuru; points to whitehorserealestate.ke |
| 3 | https://aad.ke/grand-premier/ | AAD Real Estate | developer (project) | Indexed: 1–3BR + duplex; from **10M**; Argwings / Lavington; **sales@aad.ke**; **+254 704 19 19 19**. Live fetch **404**/captcha this pass — retained via indexed developer text |
| 4 | https://hauzisha.co.ke/developments/grand-premier/ | Hauzisha | portal | AAD; unit mix; no stock; Coming-soon release language — conf ≤2; **ignore 0730** |
| 5 | https://hauzisha.co.ke/developers/aad-real-estate/ | Hauzisha | portal | Explicit **Grand Premier … Coming soon** tag among AAD four |
| 6 | https://commercialpropertykenya.com/properties/grand-premier-apartment-lavington-nairobi/ | CPK | agent | Argwings / Bernard Estate; complete; typed **8.5 / 18 / 23M**; amenities |
| 7 | https://samambohousing.com/property-item/grand-premier-lavington/ | Samambo | agent | Typed **12.5 / 19.5 / 25.5M**; sizes; **156** units. Live **403** this pass — retained via search-indexed body |
| 8 | https://realtors.rayabbay.com/apartment/grand-premier/ | Rayabbay | agent | Argwings; AAD; amenities; Year Built **2019** conflict evidence |

### Evaluated / thin skips

| URL / lead | Why skipped or thinned |
|------------|------------------------|
| https://whitehorserealestate.ke/projects/ | Search-indexed projects hub (lists Grand Premier); live fetch **404**/captcha — overlap with home |
| https://kenyaproperty.co.ke/properties/grand-premier-apartments-for-sale-and-rent-in-lavington-nairobi/ | Useful Completed + price/rent sheet — evaluated; density below CPK/Samambo for retain count |
| https://www.apexbusinesspages.com/listing/aad-ke-grand-premier-lavington/ | Stale UC→2021 + alternate ladder — conflict evidence only |
| Whitehorse / CJ Luxe LinkedIn posts | Status / single-ask corroboration — social secondary |
| https://www.buyrentkenya.com/listings/3-bedroom-apartment-for-rent-kilimani-3773677 | Prior rental at “Grand Premier, Kilimani” — listing gone this pass |
| https://kenyainsights.com/real-estate-firm-aad-accounts-frozen-over-sh134m-property-row-with-investor | Litigation cover naming Grand Premier — not dossier authority |
| block.ke | Low-trust — not used as authority |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. **`inventory_class` lock** — confirm with Whitehorse whether scheme is still **Coming soon / off_plan** or **handed over / ready** (CPK Complete + LinkedIn ready-to-move vs Hauzisha Coming soon). **`needs_developer_input`**. If developer tags Ready → Ready-skip / mark `ready` and leave research queue.  
2. Confirm **current** price list vs indexed AAD **10M**, Samambo **12.5–25.5M**, CPK remaining **8.5–23M**, kenyaproperty **8–40M**.  
3. Obtain **official payment schedule** (none found this pass).  
4. Resolve neighbourhood label: Whitehorse **Lavington** vs Hauzisha **Kilimani**.  
5. Resolve total units **156** vs **130**; duplex / penthouse sizes.  
6. Exact plot / GPS on Argwings Kodhek / Bernard Estate.  
7. Legal contracting entity / SPV (Whitehorse vs legacy AAD).  
8. Whether **sales@aad.ke** remains monitored vs **sales@ / info@whitehorserealestate.ke** only.  
9. Optional: verify Kenya Insights delivery-dispute narrative vs current site status (do not treat news as master status).

---

## 8. Anti-merge

- **≠ AYA Luxury Residence** (DISC-NBO-023) — Kileleshwa Othaya × Makueni; mixed villas / duplexes; **building** class sibling under same Whitehorse/AAD family.  
- **≠ Ambra Heights** — Kileleshwa sibling (Whitehorse: handed over & occupied; Hauzisha still Coming soon).  
- **≠ Rosewood Park** (DISC-NBO-030 sibling) — Kilimani Whitehorse/AAD Coming soon — **do not merge**.  
- **≠ Haven Villas** — Whitehorse Lavington triplex product.  
- **≠** other Argwings Kodhek / Valley Arcade schemes — different products.  
- Spelling **Grand Premiere** (Whitehorse nav) = same scheme, not a separate project.  
- **Not already in corpus** — no prior `grand-premier` dossier before this wave.
