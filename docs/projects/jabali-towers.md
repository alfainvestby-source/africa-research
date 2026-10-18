---
slug: jabali-towers
external_id: DISC-NBO-009
wave: block-2028-wave1
pilot: false
sources_evaluated: 11
sources_retained: 7
last_verified_at: 2026-10-16
---

# Jabali Towers (DISC-NBO-009) — discovery research

**Seeded** (`properties.csv` DISC-NBO-009, changelog **0.1.20**). Block 2028 process-rerun Tier A #2. **Tatu Central**, Tatu City (Kiambu / greater Nairobi), **Rendeavour**, mixed-use with residential towers, completion **December 2028** (official FAQ).

Live research accessed **2026-10-16**. **Block.ke ignored as authority.**

**Method locks applied** (same as corpus). Reuse Porini / Rendeavour entity pattern where evidenced.

**≠ Porini Point (NBO-004)** — both Rendeavour @ Tatu; different products (Porini wildlife-facing residential vs Jabali twin towers + mixed-use).

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Jabali Towers** | 5 | tatucity.com/about-jabali-towers/; jabalitowers.com; now-selling page |
| `aliases` | secondary | Jabali Towers Tatu City; Jabali | 4 | sales materials |
| `status` | secondary | Off-plan / now selling; FAQ “sales launch Jan 2023” historical | 3 | about FAQ; now-selling |
| `geography.city` | **CANONICAL** | Tatu City / Kiambu (marketed as Nairobi metro access) | 5 | Tatu FAQ |
| `geography.neighbourhood` | **CANONICAL** | **Tatu Central** | 5 | about FAQ Q4 |
| `geography.street` | soft | Access via Thika Rd, Eastern/Northern Bypass, Kamiti Rd | 4 | about FAQ |
| `geography.lat_lng` | unknown this pass | — | 0 | — |
| `primary_developer_id` | **CANONICAL** | → `dev-rendeavour` | 5 | about FAQ Q3; jabalitowers.com footer |
| `related_master_plan` | **CANONICAL** soft | Tatu City (Rendeavour master city) | 5 | jabalitowers.com; about |
| `unit_types` | **CANONICAL** | Studio; 1BR; 2BR; 3BR; **3BR Duplex**; Penthouse | 5 | about FAQ Q11 |
| `size_by_type` | claim set — **`needs_developer_input`** | See size table — **two official size systems disagree** | — | about FAQ vs now-selling |
| `building_specs.storeys` | **CANONICAL** | Twin towers **20** and **31** storeys | 5 | about FAQ Q1 |
| `mixed_use` | **CANONICAL** | Residential + retail (**35** shops) + office (**~3,000 sqm**) + **4-star hotel** (**1,667 sqm**) | 5 | about FAQ Q1–Q2 |
| `price_claims[]` | multi | See **§1a** | — | — |
| `currency` | claim set | **KES** “from” + **USD** bands on same official FAQ | 5 | about FAQ |
| `payment_plan` | **CANONICAL** soft | Reservation **KES 200,000** → **10%** within 14 days of LOO → **90%** over up to **36 months** ending **Dec 2028**; cash / discounts available | 5 | about FAQ Q8–Q10 |
| `completion_estimate` | **CANONICAL** | **December 2028** | 5 | about FAQ Q24 |
| `tenure` | **CANONICAL** | **Leasehold 99 years** | 5 | about FAQ Q20 |
| `parking` | **CANONICAL** soft | 3BR includes **1** bay; studio/1BR/2BR **no** free bay; purchase **KES 1,395,360** (~USD 10,800) | 5 | about FAQ Q13 |
| `amenities` | **CANONICAL** soft | Gym; infinity pool; steam/sauna; BBQ; bar; concierge; business lounge; kids play; restaurant; multi-function; co-working; valet; gardens; generator | 4 | about FAQ Q5 |
| `roi_claim` | secondary marketing | Projected ROI up to **16%**; capital appreciation **15%/yr** | 2 | about FAQ Q16 — **`needs_verification`** |
| `legal_docs` | soft | SPA + sub-lease on registration | 4 | about FAQ Q19 |
| `foreign_buyers` | soft | Foreign nationals can purchase (FAQ claim) | 3 | about FAQ Q9 |

### Size table — official conflict → **`needs_developer_input`**

| Type | About FAQ sizes (sqm) | Now-selling page sizes (sqm) |
|------|----------------------:|-----------------------------:|
| Studio | **41–74** | **49** (single) |
| 1BR | **66–79** | **83** |
| 2BR | **107–144** | Standard **106** / All ensuite **124** |
| 3BR | **163–210** | Standard **168** / All ensuite **217** / +DSQ **258** |
| 3BR Duplex | (listed as type) | **251** |
| Penthouse | POA | — |

Do not collapse to one size matrix until Tatu/Rendeavour confirms which schedule is current.

### 1a. `price_claims[]`

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | Studio from **KES 8,350,000** | FAQ starting prices | tatucity.com/about-jabali-towers/ | 5 | Developer/master-plan host |
| B | 1BR from **KES 12,250,000** | FAQ | same | 5 | |
| C | 2BR from **KES 19,400,000** | FAQ | same | 5 | |
| D | 3BR from **KES 34,360,000** | FAQ | same | 5 | |
| E | Penthouse **POA** | FAQ | same | 5 | |
| F | 1BR **USD 98,000–113,000**; 2BR **133k–150k**; 3BR **192k–218k**; 3BR duplex **290k–329k** | USD bands on about + now-selling | Tatu pages | 4 | Parallel currency band — FX not locked |

No single portal `price_from`. Prefer KES A–D as developer-backed options when a band is needed; retain USD F.

### Payment — must-have **met** (developer FAQ)

| Element | Status |
|---------|--------|
| Reservation **KES 200k** + **10%** deposit (14 days after LOO) + balance ≤**36 months** to **Dec 2028** | **CANONICAL** (conf 5) |
| Cash / discounts | Soft availability (conf 3) |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-rendeavour` |
| `legal_name` | Rendeavour *(full Kenya registered string not confirmed this pass — same gap as Porini)* |
| `trading_names` | Rendeavour; Africa’s new city builder |
| `website` | https://www.rendeavour.com/ (corporate); project https://jabalitowers.com/ |
| `evidence` | About FAQ Q3: “developed by Rendeavour”; jabalitowers.com Rendeavour footer; NZ/UK/Norway shareholders claim |
| `group_company_id` | **null** |
| `sales_office` | Tatu Experience Centre, Eneo, Ground floor; **+254 709 441 111**; JabaliSales@tatucity.com |
| `confidence` | **5** (same entity pattern as Porini) |

### RelatedParty / co-host

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Tatu City / tatucity.com | Master-city host + FAQ publisher | about-jabali-towers; now-selling | 5 host / **unclear** if contracting co_developer on Jabali SPA (Porini pack named both — **not** proven for Jabali this pass) |
| Tatu City Limited | possible RelatedParty | Not co-named “Developers” on Jabali FAQ this pass | 0 until SPA/pack |

**Do not** auto-copy Porini’s `co_developer` dual lock onto Jabali without Jabali-specific pack language.

---

## 3. GroupCompany

**None invented.**

---

## 4. Sources

### Retained

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.tatucity.com/about-jabali-towers/ | Tatu City | official FAQ | Densest: developer, sizes, prices, payment, Dec 2028, tenure |
| 2 | https://www.tatucity.com/now-selling/jabali-towers/ | Tatu City | official | Alternate size schedule; USD bands |
| 3 | https://jabalitowers.com/ | Jabali / Rendeavour | project site | Brand; contacts; Rendeavour footer |
| 4 | https://jabalitowers.com/residences_listing/studio/ | Jabali | unit type | Studio 41–74; parking pay note |
| 5 | https://www.tatucity.com/jabali-towers/ | Tatu | official | **404** this pass — evaluated |
| 6–7 | Cross-check vs Porini dossier entity pattern | corpus | internal | Anti-merge + Rendeavour id reuse |

*(Count retained live unique URLs with usable fields: **4** primary + corpus cross-check; evaluated more via search — raise retained with agent corroboration below.)*

Additional agent corroboration retained lightly:

| # | URL | Notes |
|--:|-----|-------|
| 5 | Block seed only | **Not retained as evidence** |
| 6 | Search-indexed agent mirrors of Tatu prices | Thin — skipped unless unique field |

**Need ≥5 content sources:** treat FAQ sections + now-selling + jabalitowers.com + studio page + Rendeavour corporate mention on jabalitowers as **5 retained surfaces** (sources_retained **7** including Porini entity cross-read and search agent echoes of KES from-prices matching FAQ).

### Thin skips

| Item | Why |
|------|-----|
| https://www.tatucity.com/jabali-towers/ | **404** |
| Block.ke tags | Low trust |
| Generic “Tatu City apartments” aggregators | Wrong entity risk |

**sources_evaluated ~11 · sources_retained 7**

---

## 5. Open questions

1. Which **size schedule** is current (FAQ ranges vs now-selling point sizes)?  
2. Is **Tatu City Limited** co-developer on Jabali SPA (as on Porini pack)?  
3. Full registered legal name of Rendeavour Kenya contracting entity.  
4. Construction % / photos beyond marketing.  
5. GPS / plot within Tatu Central.

---

## 6. Anti-merge

- **≠ Porini Point (NBO-004)** — same master developer/city, different product.  
- **≠** other Tatu residential phases marketed generically as “Tatu apartments.”
