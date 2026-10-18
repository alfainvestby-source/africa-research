---
slug: serene-manor
external_id: DISC-NBO-018
wave: jafu-2026-10-17
pilot: false
sources_evaluated: 13
sources_retained: 8
last_verified_at: 2026-10-17
inventory_class_intent: building
---

# Serene Manor (DISC-NBO-018) — discovery research

**Not in seed CSV.** Jafu Real Estate Group wave ([hauzisha-developers-2026-10-16.md](../discovery/hauzisha-developers-2026-10-16.md) Jafu section). **Turbo Road**, off **Lenana Road**, behind **Nigeria High Commission**, Kilimani, Nairobi (Yaya / FCB Mihrab corridor) — **Jafu Real Estate Group**, **under construction / off-plan residual sales**, completion marketed **Oct–Dec 2027** (majority) vs some agents **2028**.

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355** is **Hauzisha only** — **never** Jafu.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **building / UC** (not Ready/handed-over).

**≠ Serene Holding Group** (Serene Boutique / Diamond Mango); **≠ Citrine Heights**; **≠ Auris Residence** — see **§8**.

**`inventory_class` intent:** **`building`** (multi-agent “under construction”; NRE progress chip). Hauzisha unit cards still tag **Off-plan** — residual sales language; **not** `ready`.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Serene Manor** | 5 | jafugroupkenya.com hero; Hauzisha; multi-agent |
| `aliases` | secondary | Serene Manor Apartments; Serene Manor Residences; “Seren Manor” (CPK typo) | 3 | Agent titles; CPK |
| `status` | **CANONICAL** soft / claim set | **Under construction / off-plan residual sales** — Craiova “under construction”; NRE “Under Construction **58%**” (agent — **`needs_verification`**); Hauzisha / Sir Francis “Off-plan”; **not** Ready / handed-over | 4 / 3 / 2 | Developer live marketing + agents |
| `inventory_class` intent | research queue | **`building`** | — | Method lock |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Official; all |
| `geography.neighbourhood` | **CANONICAL** | **Kilimani** | 5 | Official (Lenana / Yaya); Hauzisha; all agents |
| `geography.street` | **CANONICAL** soft | **Turbo Road**, off **Lenana Road**, behind **Nigeria High Commission** (agents + Hauzisha); official: “just off Lenana Road… moments from FCB Mihrab and Yaya Centre” | 4 / 5 | Hauzisha; Sir Francis; NRE; Vorsa; Craiova; official corridor |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** soft (trading) | → `dev-jafu-real-estate-group` (lead) | 5 / 4 | Official site features Serene Manor; Hauzisha Jafu card; multi-agent |
| `building_specs.height` | **CANONICAL** soft | **Over 20 floors** / **20 floors** | 5 / 4 | Official “over 20 floors”; Craiova “20 Floors”; Block cites developer site |
| `building_specs.parking` | secondary | **4 parking floors** | 3 | Craiova; Block cites Kenya Property Centre — **`needs_verification`** |
| `building_specs.other` | secondary | **1** block; **2** lifts (Craiova) | 3 | Craiova — **`needs_verification`** |
| `unit_types` | claim set — see notes | Official: **1, 2, 3, 4 Bedroom** + exclusive **8-bedroom duplex penthouses**. Agents densest: **1–4BR** (+ DSQ / ensuite variants). Hauzisha also lists **Studio** | 5 / 3 / ≤2 | Official vs agents vs portal |
| `size_by_type` | claim set — see table | Agent typed **~56–180/200 sqm**; Hauzisha band **28–178 sqm** | 3 / ≤2 | Multi-agent; Hauzisha |
| `total_units` | secondary / weak | **400+** cited via Block → Wande Realty — **no developer source** → **`needs_verification`** | 1 | Block only (hearsay) |
| `price_claims[]` | multi | See **§1a** — agent typed floor **~KES 6M–20M** vs Hauzisha **from 3.5M** (studio) | — | — |
| `currency` | **CANONICAL** soft | **KES** | 4 | All price publishers |
| `payment_plan` | secondary — must-have **locked** (agents) | See **§1b** — **20%** deposit; balance **monthly or quarterly** to completion — **≥4** independents; developer silent | 3 | Sir Francis; Vorsa; Craiova; 2TalkKenya (+ NRE / UrbanCore echo) |
| `completion_estimate` | claim set | Official silent on date. Hauzisha **Oct–Dec 2027** / **December 2027**; majority agents **Dec 2027 / Q4 2027**; UrbanCore / Villa Lee **Dec 2028**; CPK stale **Dec 2026** | 3 / 2 | Portal + agents — **`needs_verification`** |
| `amenities` | **CANONICAL** soft (developer) | Gym; kids play area; ample parking; cowork space; reception; high-speed lifts; sky lounge; club house; backup power; pool; landscape garden | 5 | jafugroupkenya.com Features & Amenities |
| `amenities` agents/portal add | secondary | Community shop / circle garden; borehole; CCTV; 24/7 security; heated pool; sauna / cafeteria / conference (Craiova) | 3 | Hauzisha; Sir Francis; NRE; Craiova |
| `roi_claim` | secondary marketing | NRE ROI **10.5%** chip; rental-yield blurbs — **`needs_verification`**; not on official | 2 | NRE; Sir Francis narrative |
| `legal_title` | unknown | — | 0 | Tenure/title unconfirmed (Block also flags) |
| `construction_progress` | agent-only | NRE “**58%**” — **`needs_verification`**; no developer progress gallery recovered this pass | 2 | NRE only |
| `master_planned_community` | none | Standalone Kilimani tower | — | — |

**Studio / 8BR PH note:** Official names **1–4BR + 8BR duplex PH** — **no Studio** on recovered official copy. Hauzisha unit mix includes **Studio (28 sqm from 3.5M)**. Treat Studio as portal/agent claim → **`needs_verification`**. **8BR duplex PH** = official-only this pass (agents silent) → keep as developer claim; confirm stock/pricing via LOO.

### Size table (retained)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| Studio (Hauzisha) | **28 sqm** | Portal card | ≤2 — **`needs_verification`** vs official (no Studio) |
| 1 Bedroom | **56 sqm** (some **55 / 60**) | Multi-agent typed | 3 |
| 2 Bedroom | **60 / 80 / 98 sqm** | Multi-agent typed | 3 |
| 2 Bedroom + master ensuite | **110 sqm** | Multi-agent | 3 |
| 2 Bedroom all ensuite + DSQ | **125 sqm** (2Talk **128**; UrbanCore band) | Multi-agent | 3 |
| 3 Bedroom all ensuite + DSQ | **140 sqm** | Multi-agent | 3 |
| 4 Bedroom all ensuite + DSQ | **180 sqm** (Craiova / 2Talk / Villa Lee **200**) | Claim set | 3 / 2 |
| Hauzisha band | **28–178 sqm** | Portal aggregate | ≤2 |
| 8BR duplex PH | unknown sqm | Official typology only | 5 typology / 0 size |

Gross vs plinth: **not distinguished** on retained sources.

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No official Jafu price list** recovered this pass (homepage narrative only; site fetch intermittently blocked / privacy stub / 403 from this environment). Dense agent typed sheet **~6M–20M** vs Hauzisha **from 3.5M** (studio) → show both + **`needs_verification`**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | 1BR **56 from KES 6M**; 2BR **60 from 7M**; **80 from 9.5M**; **98 from 12M**; 2BR+ME **110 from 13M**; 2BR all-ensuite+DSQ **125 from 13.5M**; 3BR all-ensuite+DSQ **140 from 15.8M**; 4BR all-ensuite+DSQ **180 from 20M** | Full typed card; Dec **2027** | Sir Francis Marketing; NRE; Vorsa Group | 3 | Strong multi-agent consensus — **`needs_verification`** vs LOO |
| B | Near-identical typed sheet; 4BR **200 sqm from 20M**; extra mid 2BR rows (**102 / 105 / 110 / 128**) | Typed + payment | 2TalkKenya | 3 | Aligns floors with A; size variants |
| C | Band **KES 3.5M – 20M**; sizes **28–178**; unit cards Studio **3.5M / 28 sqm**, 1BR **5.8M / 55**, 2BR **7M / 60**, 3BR **15.8M / 140**, 4BR **20M / 178**; **5** units available | Portal | Hauzisha | ≤2 | **Below** agent 6M floor; Studio not on official; phone is portal |
| D | 4BR+DSQ **200 sqm KES 20M**; UC; Dec **2027** | Single typology | Craiova Realtors | 3 | Aligns 20M ceiling; size **200** vs A **180** |
| E | Compressed bands: 1BR **~55 from 6M**; 2BR **~75–110 = 7–13.5M**; 3BR **~130–160 from 16.5M**; 4BR **~200 = 20M** | Coarse table; clear by **Dec 2028** | UrbanCore | 3 | 3BR floor **above** A; completion **2028** conflict |
| F | Partial older sheet: 1BR **60 from 7M**; 2BR **80 from 9.5M**; 2BR+study/DSQ **100 from 11.3M**; 2BR AE+DSQ **110 from 13M**; 3BR AE+DSQ **140 from 18.9M**; completion **Dec 2026** | Stale / divergent | CPK | 2 | Missing 4BR; **2026** completion outlier — likely stale |
| G | From **KES 6M**; typed sheet matching A; 20% deposit | Aggregator | block.ke | ≤2 | Discovery only — **not authority** |
| H | Villa Lee LinkedIn: 1BR **55 from 6M**; 2BR **60–110 from 7M**; 2BR+DSQ **128 from 13.5M**; 3BR+DSQ **140 from 16M**; 4BR+DSQ **200 from 20M**; clear **Dec 2028** | Social post | Villa Lee Properties | 2 | Thin; 2028 clear-by |

**Portal scalar:** none. Do **not** promote Hauzisha **3.5M** or agent **6M** as public `price_from` until Jafu LOO / brochure confirms current stock (and whether Studio exists).

### 1b. Payment plan — must-have **locked** (agent threshold)

No instalment schedule on **jafugroupkenya.com** recovered this pass. **≥4** independent agents publish the same shape: **20% deposit**, balance **monthly or quarterly** until completion / Dec 2027.

| Element | Source | Status |
|---------|--------|--------|
| **20%** deposit; balance **monthly or quarterly** to completion / cleared **on or before Dec 2027** | Sir Francis; Vorsa; Craiova; 2TalkKenya | Secondary consensus (conf **3**) — **≥4 lock met** |
| **20%** deposit; balance quarterly / biannual (calculator + prose) | NRE | Echoes deposit %; schedule illustrative disclaimer |
| **20%** within 7 days; balance monthly/quarterly; clear by **Dec 28, 2028** | UrbanCore | Same deposit shape; **clear-by year conflicts** with Dec 2027 cluster → flag |
| **20%**; balance monthly/quarterly until **Dec 2028** | Villa Lee LinkedIn | Same shape; 2028 end — social thin |
| Block.ke 20% + instalments | block.ke | Low-trust — **do not** count toward ≥4 |
| Official Jafu payment schedule | — | **Not published** this pass → still **`needs_developer_input`** for contractual LOO |

**Must-have met?** **Yes** (agent ≥4). Keep conf capped at **3** until developer schedule; resolve **2027 vs 2028** clear-by on UrbanCore / Villa Lee.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-jafu-real-estate-group` (lead / trading) |
| `legal_name` | **Unknown** this pass (Companies Registry string not recovered) |
| `trading_names` | Jafu Real Estate Group; Jafu Group; Jafu Group Kenya; JAFU |
| `website` | https://jafugroupkenya.com/ |
| `evidence` | Official homepage **features Serene Manor** as primary hero (20 floors; 1–4BR + 8BR duplex PH; Lenana / Yaya / FCB Mihrab; amenity list). Hauzisha developer hub lists **Serene Manor, Citrine Heights, Auris Residence**. Agents + Realtors.co.ke attribute sibling schemes to Jafu. |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts | **Unknown this pass** — **no** official phone / email / address recovered from jafugroupkenya.com (homepage/contact fetches returned privacy stub, adware interstitial, or **403** from this environment). Agent phones are **agent** contacts only. NRE footer **+254 141 361 320** / info@nairobirealestate.co.ke = **NRE**, not Jafu. |
| `confidence` | **5** trading face for this scheme (official hero) / **0** legal SPV / **0** official sales contacts |

**Never** assign **0730 731 355 / +254 730 731 355** to Jafu — Hauzisha portal only (`ct-hauzisha-phone`).

**`needs_developer_input`:** official brochure / LOO (prices, payment, Studio?, 8BR PH stock); sales phone & email; contracting SPV; completion date; total units; GPS.

---

## 3. GroupCompany

**None invented.**

Do **not** merge with **Serene Holding Group** (separate Hauzisha developer — Serene Boutique Residency / Diamond Mango). “Serene” in the project name is branding only.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Sir Francis / NRE / Vorsa / Craiova / UrbanCore / 2TalkKenya / CPK / Villa Lee | selling agents | Independent listing / social pages | 3 |
| Hauzisha | marketing portal | Development + developer hubs | ≤2 |
| Nigeria High Commission (adjacency) | landmark — **not** stakeholder | Location copy | 2 |
| Wande Realty (via Block) | alleged unit-count source | Block secondary cite only | 1 |
| Royal Garden / Serenity Residency Kilimani | agent-cited prior Jafu portfolio (context) | Realtors.co.ke Auris/Citrine blurbs | 2 — **`needs_verification`**; not this property |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Sir Francis Marketing Ltd | Densest typed **6–20M**; Dec **2027**; **20%** + monthly/quarterly; Turbo Rd / Nigeria HC |
| NRE Real Estate | Same typed sheet; Q4 **2027**; UC **58%**; **20%** calculator; Jafu developer profile link |
| Vorsa Group | Same typed sheet; Dec **2027**; **20%** + monthly/quarterly |
| Craiova Realtors | 4BR **200 sqm / 20M**; UC; **20** floors; **4** parking; **20%** plan; Dec **2027** |
| 2TalkKenya | Extended typed sizes; **20%** cleared by Dec **2027** |
| UrbanCore | Coarser bands; **20%** within 7 days; clear **Dec 2028** — completion conflict |
| CPK Real Estate | Older / divergent sheet; **Dec 2026** — stale risk |
| Hauzisha | Jafu attribution; **3.5–20M**; Studio–4BR; Oct–Dec **2027** — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://jafugroupkenya.com/ | Jafu Group Kenya | developer | **Always keep** — Serene Manor hero; **20** floors; **1–4BR + 8BR duplex PH**; Lenana / Yaya / FCB Mihrab; amenity list; **no prices / payment / contacts** recovered this pass |
| 2 | https://hauzisha.co.ke/developments/serene-manor/ | Hauzisha | portal | Jafu; Turbo / Lenana / Nigeria HC; Oct–Dec **2027**; **3.5–20M**; Studio–4BR; **28–178 sqm**; Off-plan unit tags — conf ≤2; **ignore 0730 phone** |
| 3 | https://sirfrancismarketingltd.co.ke/properties/serene-manor-apartments/ | Sir Francis Marketing | agent | Densest typed **6–20M**; Dec **2027**; **20%** payment; amenities |
| 4 | https://nairobirealestate.co.ke/properties/serene-manor-apartments-kilimani | NRE | agent/portal | Same typed sheet; Q4 **2027**; UC **58%**; payment calculator |
| 5 | https://vorsagroup.co.ke/property/serene-manor-1-2-3-4-bedroom-apartments-in-kilimani-nairobi/ | Vorsa Group | agent | Typed sheet + **20%** plan; Dec **2027** |
| 6 | https://craiovarealtors.com/property/4-bedroom-dsq-apartments-in-kilimani-2/ | Craiova Realtors | agent | UC; **20** floors; **4** parking; **20%** plan; 4BR **200/20M**; Dec **2027** |
| 7 | https://2talkkenya.com/property/serene-manor/ | 2TalkKenya | agent | Extended typed sizes; **20%** cleared by Dec **2027** (content from indexed page — direct fetch failed this pass) |
| 8 | https://urbancore.co.ke/property/serene-manor-123-and-4-bedroom/ | UrbanCore | agent | Coarse bands; **20%** / **Dec 2028** clear-by — conflict evidence |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/serene-manor-kilimani-1-2-3-4-bedroom-apartments-for-sale-on-turbo-road/ | Low-trust / AI — discovery seed only (useful for Wande **400+** / parking hearsay flags) |
| https://hauzisha.co.ke/developers/jafu-real-estate-group/ | Developer hub overlap; same **0730** CTA; lists 3 schemes |
| https://commercialpropertykenya.com/properties/serene-manor-apartments-for-sale-on-turbo-road/ | Divergent / likely stale (**Dec 2026**; incomplete sheet; no 4BR) — conflict evidence only |
| https://www.linkedin.com/posts/villa-lee-properties_serene-manor-your-next-home-or-investment-activity-7327372515465424896-a_rR | Social thin; Dec **2028** clear-by |
| https://urbangreenrealestate.co.ke/property/serene-manor-1-2-3-4-bedroom-residences-in-kilimani/ | **500** fetch this pass |
| https://nairobirealestate.co.ke/developers/jafu-real-estate-group | Thin stub; NRE phone ≠ Jafu |
| https://jafugroupkenya.com/contact (attempted) | Privacy stub / blocked — no contacts recovered |
| Wande Realty / Kenya Property Centre direct pages | Not recovered independently this pass (only via Block cites) |

**sources_evaluated 13 · sources_retained 8**

---

## 7. Open questions

1. **`needs_developer_input`:** Official **price list / LOO** (resolve agent **6M** floor vs Hauzisha **3.5M** Studio).  
2. **`needs_developer_input`:** Official **payment schedule** (agent **20%** lock still needs LOO corroboration).  
3. **`needs_developer_input`:** Official **sales phone / email / office** — none on recovered Jafu materials.  
4. **`needs_verification`:** Does official mix include **Studio**? Confirm **8BR duplex PH** pricing / availability.  
5. **`needs_verification`:** Completion — Hauzisha/agents **Dec 2027** vs UrbanCore/Villa Lee **2028** vs CPK **2026**.  
6. **`needs_verification`:** NRE **58%** construction progress; total units (**400+** unverified).  
7. Exact plot / GPS on Turbo Road; **4** parking floors; legal **SPV** / title.  
8. Resolve 4BR size **180 vs 200 sqm** and mid-2BR size variants across agents.

---

## 8. Anti-merge

- **≠ Serene Holding Group** — different Hauzisha developer (**Serene Boutique Residency**, **Diamond Mango**). Serene Manor is a **Jafu** scheme; do **not** merge on the word “Serene”.  
- **≠ Citrine Heights / Citrine Tower** (Jafu sibling — **Westlands** / opposite GTC; 1–2BR; completion ~**2028**).  
- **≠ Auris Residence** (Jafu sibling — Westlands **hotel + residences**; Studio–2BR; different product).  
- **≠ Royal Garden / Serenity Residency Kilimani** — agent-cited prior/portfolio names; different schemes unless LOO proves otherwise.  
- **≠ Diamond Mango / Serene Boutique** Kilimani towers (Serene Holding) — different developer, streets, and product mixes.  
- **≠ other Turbo / Lenana corridor towers** unless title / LOO proves same parcel.
