---
slug: balkis-residences
external_id: DISC-NBO-010
wave: block-2028-wave2
pilot: false
sources_evaluated: 14
sources_retained: 8
last_verified_at: 2026-10-16
---

# Balkis Residences (DISC-NBO-010) — discovery research

**Seeded** (`properties.csv` DISC-NBO-010, changelog **0.1.20**). Block 2028 process-rerun wave-2. **Riverside Drive / Riverside Grove**, Nairobi (Westlands Blue Zone), off-plan / under construction claims, completion **2028** cluster (**March** vs **Q4**).

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only — discovery seed; prices/payment not used as public-canonical).

**Method locks applied:**
- Developer vs agents: developer/official agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.

**≠ Seasons Riverside** (KP Housing / duplex product) · **≠ Cheval Riverside** (Pinecrest / 20–23 storey glass tower) — same corridor, different schemes (§8).

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Balkis Residences** (also **Balkis Residences Riverside**) | 5 | balkisriverside.com; e-brochure; multi-agent |
| `aliases` | secondary | Balkis Riverside; Balkis Residences Riverside Drive | 4 | CPK; Pakfront; agents |
| `status` | secondary | **Off-plan** / under construction / groundbreaking (agent language) | 3 | CPK; Craiova; Own It — **`needs_verification`** vs LOO |
| `geography.city` | **CANONICAL** | Nairobi | 5 | official; all |
| `geography.neighbourhood` | **CANONICAL** | **Riverside** (Westlands / diplomatic Blue Zone) | 5 | balkisriverside.com/location; all |
| `geography.street` | **CANONICAL** soft | **End of Riverside Grove** / **Riverside Drive** corridor | 5 / 4 | official contact (“End of Riverside Grove”); agents “Riverside Drive” |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **lead** — **`needs_verification`** | → `dev-sunmon-group` (**proposed**) | 2 | **Hauzisha only** names Sunmon; **official site silent** on corporate developer / SPV |
| `project_sales_face` | **CANONICAL** soft | Project brand site **balkisriverside.com** (+254 798 999 111; info@balkisriverside.com) | 5 | official home + contact; e-brochure header |
| `unit_types` | **CANONICAL** soft | **1 Bedroom**; **1 Bedroom + Study** (official); **2 Bedroom**; **2 Bedroom + DSQ**; **2 Bedroom + Study + DSQ**; **3 Bedroom + DSQ** | 5 / 4 | official unit-type page; agents (study 1BR mainly on official / May brochure) |
| `size_by_type` | claim set — **`needs_developer_input`** | See **size table** — **official / May brochure** vs **older e-brochure / agent matrix** disagree | — | — |
| `size_measure_tag` | soft | Brochures publish **net** + **gross**; agent “from” tables track **gross**-like bands | 4 | Oaklane/Vorsa e-brochure; May brochure |
| `total_units` | unknown | — | 0 | not found |
| `building_specs.storeys` | unknown | — | 0 | not on retained sources |
| `price_claims[]` | multi | See **§1a** — **no official price list** this pass | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | agents; official silent on price |
| `payment_plan` | secondary must-have (**≥4 agents**; no developer %) | See **§1b** | 3 | A-list; Craiova; Oaklane; Habari (+ peers) |
| `completion_estimate` | claim set | **March 2028** vs **Q4 2028** (year agrees) | 3 / 2 | Hauzisha/Masterways/Craiova/Vorsa vs Own It/Habari/A-list/Pakfront |
| `amenities` (core) | secondary consensus | Rooftop infinity pool; gym; Zen garden / landscaped courtyard; kids play; hotel-style lobby; restaurant/café; convenience store; borehole; backup generator; high-speed lifts; 24/7 CCTV; parking | 4 | official amenities copy via brochure + site narrative; multi-agent |
| `amenities` soft extras | secondary — **`needs_verification`** | Outdoor water bar; padel court (May brochure / Block copy); concierge / smart home (Pakfront) | 2 | brochure variants; Pakfront |
| `roi_claim` | secondary marketing | Vorsa **8–10%** yield / **12–15%** appreciation; other agents vague “strong yields” | 1–2 | Vorsa; marketing pages — **`needs_verification`** |
| `early_bird` | secondary | **KES 500,000** early-bird discount | 2 | CPK; Vorsa; Sir Francis — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `tenure` | unknown | Block: “confirmed at enquiry” (not retained as authority) | 0 | — |

### Size table — official vs agent → **`needs_developer_input`**

Do **not** collapse to one matrix until sales office / LOO confirms which schedule is current.

| Type | Official unit-type page / May e-brochure (gross sqm) | Older Oaklane/Vorsa e-brochure (gross sqm) | Common agent “from” band (sqm) |
|------|------------------------------------------------------:|-------------------------------------------:|--------------------------------|
| 1BR | **A03 66**; **B 65** | **66.3–66.8** | **66–69** |
| 1BR + Study | **84** (official + May) | — (not in older brochure extract) | rarely listed |
| 2BR | **A04 111–117**; **A05 117–123** (odd/even) | **109–119** | **109–114** |
| 2BR + DSQ | **C02 132–139** | **128–133** | **128–133** |
| 2BR + Study + DSQ | **A02 157–163** | **149–154** | **149–155** |
| 3BR + DSQ | **C01/C03 212–219** | **200–205** | **200–210** |

Hauzisha portal size span **66–219** aligns with the **official upper** band; agent typed lists still reprint the **older** mid-matrix.

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No prices on balkisriverside.com** this pass → commercial “from” figures are **agent/portal only** → show + **`needs_verification`**. **Do not** use Block.ke price rows as public-canonical.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | 1BR **66–69 from KES 7.9M**; 2BR **109–114 from 12.7M**; 2BR+DSQ **128–133 from 15.2M**; 2BR+Study+DSQ **149–155 from 17.25M**; 3BR+DSQ **200–210 from 23.3M** | Typed agent matrix (dominant reprint) | CPK; Own It; Craiova; Masterways; Habari; A-list; Vorsa | 3 | Agent consensus · sizes conflict with official · **`needs_verification`** |
| B | 1BR **66 from 7.9M**; 2BR **118 from 13M**; 2BR+DSQ **133 from 15M**; 2BR+DSQ+Study **154 from 17M**; 3BR+DSQ+Study **205 from 24M** | Alternate typed table | Oaklane agent page | 2 | Diverges from A on mid/upper · **`needs_verification`** |
| C | Band **KES 7.9M – 24.1M** | Portal card | Hauzisha | 2 | Portal; upper above A’s 23.3M |
| D | Early-bird **KES 500,000** off | Promo | CPK; Vorsa; Sir Francis | 2 | Offer · **`needs_verification`** |
| E | Official site | **No KES list published** | balkisriverside.com | — | Call/email for details |

**Portal scalar:** none canonical. Prefer retaining A as the densest agent claim set; resolve vs LOO and vs official size schedule before any product “from” field.

### 1b. Payment plan — must-have **met via ≥4 agents** (no developer %)

| Element | Agreeing independent sources | Count | Status |
|---------|------------------------------|------:|--------|
| **~20% deposit** + balance in instalments during construction / to completion | A-list; Craiova; Oaklane; Habari (+ denser A-list schedule below) | **≥4** | Must-have at conf **3**; **`needs_verification`** vs LOO — **not** on official site |
| A-list staged schedule: **20%** within 7 days → **10%** @ 3 mo → **20%** @ 6 mo → **10%** @ 8 mo → **10%** @ 12 mo → **30%** by completion | A-list only (dense) | 1 | Show as agent detail · **`needs_verification`** |
| Cash: **20%** then balance in **2 weeks** (Craiova) vs **30 days** (A-list) | Craiova; A-list | 2 | Claim set conflict |
| Mortgage: **≥20%** / 20% in 7 days; balance financed after completion | Craiova; A-list | 2 | Secondary |
| Pakfront “**10%** on reservation” | Pakfront alone | 1 | **Outlier** vs 20% cluster — do not promote |
| Developer / official % schedule | — | 0 | **unknown** this pass |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-sunmon-group` (**proposed**) |
| `legal_name` | **Unknown** this pass (Companies Registry string not recovered) |
| `trading_names` | **Sunmon Group** (Hauzisha attribution only); project brand **Balkis Residences / Balkis Riverside** |
| `website` | **No Sunmon corporate site found.** Project sales site: https://www.balkisriverside.com/ |
| `evidence` | Hauzisha development FAQ: “developed by Sunmon Group” + Hauzisha developer hub lists Sunmon portfolio (Lesto; Balkis; Atreus Brookside; Aether). **Official project site and e-brochure do not name Sunmon or any Ltd SPV.** GoAfricaOnline directory lists “Balkis Riverside” as a real-estate developer entry pointing at the same phone/domain — soft, not a legal-entity proof. |
| `group_company_id` | **null** — none invented |
| `sales_office` | End of Riverside Grove, Westlands, Nairobi; **+254 798 999 111**; info@balkisriverside.com; Mon–Fri 9–5, Sat 9–1 |
| `confidence` | **2** corporate Sunmon · **5** project sales face (domain/phone) · **0** legal SPV |

**Do not** treat CPK, Own It, Oaklane, A-list, Habari, Masterways, Vorsa, Pakfront, or Block as the developer.

---

## 3. GroupCompany

**None invented.** No parent / holding company evidenced beyond the unverified “Sunmon Group” trading label.

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Hauzisha | portal claiming direct developer feed | Attributes Sunmon; lists Balkis under Sunmon hub | 2 for developer ID only |
| GoAfricaOnline “Balkis Riverside” | directory “Real Estate Developers” listing | Mirrors balkisriverside.com phone | 1 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Typed price list; early-bird 500k; 2028 completion |
| Craiova Realtors | Price matrix; March 2028; dense payment (instalment / cash / mortgage) |
| A-list Real Estate | Price matrix; **staged % schedule**; Q4 2028 |
| Own It Kenya | Price matrix; Q4 2028 |
| Habari Homes | Price matrix; 20% deposit; Q4 2028 |
| Oaklane Properties | Alternate price table; 20% deposit; hosts 2026 e-brochure |
| Masterways / Vorsa (supporting) | March 2028; matrix / brochure host |

---

## 6. Sources

### Retained (≥5 rule; always keep official when found)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.balkisriverside.com/ (+ /unit-type-1, /contact-us, /location) | Balkis Residences (project) | **official project** | Primary sales face; address; phone; **gross sizes**; no prices / payment / Sunmon / completion on pages fetched |
| 2 | https://oaklaneproperties.co.ke/wp-content/uploads/2026/04/Balkis-Residences-Riverside-E-brochure-2026-1.pdf | Project e-brochure (hosted by Oaklane) | brochure | Header **www.balkisriverside.com** / **+254 798 999 111**; net+gross sizes (**older** schedule); amenities |
| 3 | https://hauzisha.co.ke/developments/balkis-residences-riverside/ | Hauzisha | portal | **Sunmon Group** attribution; March 2028; 7.9–24.1M; 66–219 sqm |
| 4 | https://commercialpropertykenya.com/properties/balkis-riverside-12-3-bed-apartments-in-westlands/ | CPK | agent | Dominant price matrix; early-bird; groundbreaking / 2028 |
| 5 | https://craiovarealtors.com/property/one-two-three-bedroom-apartments-on-the-riverside-drive/ | Craiova | agent | Matrix; March 2028; payment paths |
| 6 | https://a-listrealestate.ke/property/balkis-residences/ | A-list | agent | Matrix; **detailed instalment %**; Q4 2028 |
| 7 | https://ownitkenya.com/property/apartments-for-sale-in-riverside-nairobi/balkis-residences-riverside/ | Own It Kenya | agent | Typed size/price table; Q4 2028 |
| 8 | https://habarihomes.com/property/1-bedrooms-at-balkis-residences-apartments-in-riverside/ | Habari Homes | agent | Matrix; **20%** deposit; Q4 2028 |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/balkis-residences-beyond-living-on-riverside-drive/ (+ May e-brochure PDF hosted there) | **Block.ke low-trust** — discovery only; size text overlaps official unit-type page but **not** retained as authority / conf ≥3 |
| https://www.pakfront.co.ke/projects/balkis-riverside | Seed — thin; **10%** booking conflicts with 20% cluster |
| https://oaklaneproperties.co.ke/properties/balkis-residences-riverside/ | Overlaps retained brochure; alternate prices noted in §1a B without separate retain row |
| https://www.masterways.co.ke/properties/balkis-residences | Matrix duplicate of A |
| https://vorsagroup.co.ke/property/balkis-residences-riverside-1-2-3-bedroom-apartments/ | Brochure host + ROI inflation; matrix overlap |
| https://sirfrancismarketingltd.co.ke/properties/balkis-residences-riverside/ | Matrix + early-bird reprint |
| https://amaliproperties.co.ke/… | HTTP 500 this pass |
| https://farmanrealestate.com/listing/balkis-residences | Thin; USD “from 51k”; “Developer Balkis” nonsense |
| https://almasirealty.com/property/balkis-riverside/ | Thin; completion TBD |
| https://www.goafricaonline.com/ke/1233821-balkis-riverside | Directory mirror of project phone — soft RelatedParty only |
| https://hauzisha.co.ke/developers/ (Sunmon card) | Evaluated for portfolio attribution; not a Balkis field source |
| sunmon.com | Unrelated industrial site — **not** Kenya Balkis developer |

**sources_evaluated ~14 · sources_retained 8**

---

## 7. Open questions

1. **Legal contracting entity / SPV** for LOO — official site silent; Sunmon Group unconfirmed outside Hauzisha.  
2. Confirm **Sunmon Group** (or other) as developer with sales office / SPA header.  
3. Resolve **size schedule** official/May (**65–219 gross**) vs older brochure / agent matrix (**66–210** bands) → **`needs_developer_input`**.  
4. Publish **current price list** from developer (none on official site).  
5. Confirm **payment % schedule** (A-list staged vs simple 20% + flexible).  
6. Lock **completion month**: March 2028 vs Q4 2028.  
7. Storeys / total units / title tenure.  
8. Exact plot GPS on Riverside Grove.

---

## 8. Anti-merge

- **≠ Seasons Riverside** — KP Housing Development (Hauzisha); **1/2BR + 2/4BR duplexes**; from ~**8.8M**; different product mix (duplex blocks); completion ~Aug/Dec **2028**.  
- **≠ Cheval Riverside** — Pinecrest Paradise / Cheval Riverside Company Limited (NEMA ESIA: **NAIROBI/BLOCK 22/70**); **~20–23 storey** mixed-use glass tower; 1–2BR focus; different SPV.  
- **≠ The Saruni** / other Riverside Drive schemes co-listed on Pakfront “More in Riverside”.  
- **≠ Balqis Residences (UAE / IFA)** — different country product; name collision only.  
- Same Hauzisha “Sunmon” card also lists **Lesto Residences**, **Aether Residences**, **Atreus Brookside** — **different sites/products**; do not merge. Note Hauzisha Atreus page also says “Lesto Residence Developer” — portfolio attribution messy; reinforces Sunmon **`needs_verification`**.
