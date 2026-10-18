---
slug: citrine-heights
external_id: DISC-NBO-016
wave: jafu-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 7
last_verified_at: 2026-10-17
---

# Citrine Heights (DISC-NBO-016) — discovery research

**Not in seed CSV.** Jafu Real Estate Group verification wave ([hauzisha-developers-2026-10-16.md](../discovery/hauzisha-developers-2026-10-16.md)). **Westlands Road**, opposite **Stanbic Bank Chiromo / GTC**, Westlands, Nairobi — **Jafu Real Estate Group**, off-plan / pre-handover (completion marketed **2028**).

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (no Citrine page found this pass; low-trust class). **Hauzisha** = portal / discovery only (conf ≤3); phone **0730 731 355** is **Hauzisha only** — never Jafu.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **Off-plan / UC marketing** only (**not** Ready / handed-over).

**≠** Serene Manor; **≠** Auris Residence; **≠** other Westlands towers — see **§8**. Alias **Citrine Tower** = same scheme (agents).

**`inventory_class` intent:** **`off_plan`** (Coming soon / Q3 2026 launch language + staged-sale marketing; some agents also say “under construction” — show as secondary, **`needs_verification`** vs developer progress).

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Citrine Heights** (Hauzisha + CPK) | 4 | Hauzisha; CPK — official site does **not** name Citrine this pass |
| `aliases` | secondary | **Citrine Tower**; Citrine Tower Westlands; Citrine Tower Apartments | 3 | VillaWatch; Realtors.co.ke; Habari; Ladva |
| `status` | secondary — claim set | **Off-plan / under construction** (agents); sales “launching **Q3 2026**” (VillaWatch; Realtors); **not Ready** | 3 | CPK; Craiova; Habari; VillaWatch — **`needs_verification`** (no official progress gallery) |
| `geography.city` | **CANONICAL** soft | Nairobi | 4 | All retained |
| `geography.neighbourhood` | **CANONICAL** soft | **Westlands** | 4 | Hauzisha; CPK; all agents |
| `geography.street` | secondary | **Westlands Road** — opposite **Stanbic Bank Chiromo** / next to **GTC** | 3 | CPK; Craiova; Habari; VillaWatch — **`needs_verification`** vs official pin |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** soft (trading) | → `dev-jafu-real-estate-group` (lead) | 4 | Hauzisha attribution; VillaWatch; Realtors; jafugroupkenya.com brand face (portfolio) |
| `unit_types` | secondary — claim set | **1 Bedroom**; **2 Bedroom**; **2 Bedroom + DSQ** | 3 | CPK; Craiova; Habari; VillaWatch — Hauzisha card says **1BR & 2BR** only (no DSQ on portal mix) |
| `size_by_type` | claim set — see table | **68 / 105 / 125 sqm** band | 3 | CPK; Craiova; Habari; Hauzisha **68–125 sqm** |
| `total_units` | secondary | **161** units; **7** per floor (2×1BR + 5×2BR) | 3 | Hauzisha; CPK; Ladva — **`needs_verification`** (no official Citrine page) |
| `building_specs` | secondary | **23** floors; **4** parking levels (2 basement + 2 upper) | 3 | Hauzisha / CPK floors; CPK / Craiova / Habari parking — **`needs_verification`** |
| `price_claims[]` | multi | See **§1a** — clustered **7.3 / 11 / 12.9M** vs Craiova **7.9 / 12.5 / 14.9M** | — | — |
| `currency` | **CANONICAL** soft | **KES** | 4 | All price publishers |
| `payment_plan` | secondary — must-have **not locked** | See **§1b** — developer silent; **1** agent publishes **20%** deposit — short of ≥4 | 2 | Craiova only for % |
| `completion_estimate` | claim set | **June 2028** (CPK; Habari) vs **August 2028** (Craiova); sales launch **Q3 2026** ≠ handover | 3 | Agents — **`needs_verification`** |
| `amenities` | secondary | Heated adult + kids pools; gym; cafeteria; rooftop green garden; lifts; generator; borehole; CCTV; 24hr security | 3 | CPK; Craiova; Habari; Hauzisha amenity chips |
| `roi_claim` | secondary marketing | Net yield **8.5%–10%**; “USD-linked” (agents) — no official ROI | 2 | VillaWatch; Realtors — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | none | Standalone Westlands Road tower (not a named masterplan precinct) | — | — |

### Size table (retained)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| 1 Bedroom | **68 sqm** | Multi-agent typed | 3 |
| 2 Bedroom | **105 sqm** | Multi-agent typed | 3 |
| 2 Bedroom + DSQ | **125 sqm** | Multi-agent typed | 3 |
| Hauzisha band | **68–125 sqm** | Portal | ≤2 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**No official Jafu Citrine price list** recovered this pass (homepage features **Serene Manor** only; site fetch largely blocked). Agent cluster **A** (7.3 / 11 / 12.9) vs Craiova **B** (7.9 / 12.5 / 14.9) → show both + **`needs_verification`**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | 1BR **68 sqm from KES 7.3M**; 2BR **105 from 11M**; 2BR+DSQ **125 from 12.9M** | Typed unit card; June 2028 | CPK | 3 | Densest sheet this pass |
| B | Same typed floors as A | Typed + amenities + parking | Habari Homes | 3 | Aligns with A |
| C | 1BR from **KES 7.3M**; 2BR from **11M** (+ DSQ higher) | Off-plan / Q3 2026 launch | VillaWatch (1BR + 2BR pages) | 3 | Aligns “from” with A |
| D | Band **KES 7.3M – 11M**; sizes **68–125**; **2** units available | Portal card | Hauzisha | ≤2 | Aggregator; phone is portal; no DSQ in band |
| E | From **KES 7.3M**; **23** floors / **161** units / **7**/floor | Marketing article | Ladva Realtors | 2 | Thin blog; echoes A scalars |
| F | 1BR **68 from 7.9M**; 2BR **105 from 12.5M**; 2BR+DSQ **125 from 14.9M** | Typed; Aug 2028 | Craiova Realtors | 3 | **Above** A cluster — **`needs_verification`** |
| G | “Call for price”; 1&2BR + DSQ; Jafu; opposite GTC | Soft launch blurb | Realtors.co.ke | 2 | No typed floors |

**Portal scalar:** none. Do **not** promote a single “from” until Jafu LOO / official Citrine page confirms current stock.

### 1b. Payment plan — must-have **not** triggered

No instalment schedule on jafugroupkenya.com (Citrine absent) this pass. Only **one** independent agent publishes a deposit %.

| Element | Source | Status |
|---------|--------|--------|
| **20%** deposit; balance instalments till completion | Craiova | Single agent (conf **2**) — **`needs_verification`** |
| “Flexible payment” / instalments during construction (no %) | Habari Homes | Thin — does not lock |
| CPK invites enquiry for payment plan | CPK | Not published |
| Official Jafu payment schedule for Citrine | — | **Not published** this pass |
| Hauzisha generic off-plan FAQ | Hauzisha | Portal boilerplate — ignore for lock |

**Must-have met?** **No** — need developer schedule **or** ≥**4** independent agents agreeing on a structure.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-jafu-real-estate-group` (lead / trading) |
| `legal_name` | **Unknown** this pass (Companies Registry string not recovered) |
| `trading_names` | Jafu Real Estate Group; Jafu Group; Jafu Group Kenya |
| `website` | https://jafugroupkenya.com/ |
| `evidence` | Official homepage features **Serene Manor** (20 floors, Lenana / Yaya corridor) — corroborates brand; **does not** list Citrine Heights this pass. Hauzisha + multi-agent attribute Citrine / Citrine Tower to Jafu. NRE profile links Auris (sibling). |
| `group_company_id` | **null** — none invented |
| `sales_office` | **Unknown** this pass — **no** official phone / email recovered from jafugroupkenya.com materials (homepage/contact fetches returned privacy stub or 403 from this environment) |
| `confidence` | **4** trading face (brand site live) / **0** legal SPV / **0** official sales contacts |

**Never** assign **0730 731 355 / +254 730 731 355** to Jafu — Hauzisha portal only (`ct-hauzisha-phone`).

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| CPK / Craiova / Habari / VillaWatch / Realtors.co.ke / Ladva | selling agents | Independent listing / marketing pages | 3 |
| Royal Garden (agent mention) | prior Jafu scheme (context only) | Realtors.co.ke; VillaWatch blurbs | 2 — **`needs_verification`**; not this property |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Densest typed **7.3 / 11 / 12.9**; June 2028; UC; Westlands Rd / Stanbic |
| Habari Homes | Same typed floors as CPK; June 2028; “flexible” payment |
| Craiova Realtors | Higher **7.9 / 12.5 / 14.9**; **20%** deposit; Aug 2028 |
| VillaWatch Kenya | Citrine Tower alias; from **7.3M / 11M**; Q3 2026 launch; Jafu + Royal Garden / Serene Manor |
| Realtors.co.ke | Soft launch / call-for-price; Jafu; opposite GTC |
| Ladva Realtors | Spec echo (23/161/7.3M) — thin |
| Hauzisha | Jafu attribution; **7.3–11M**; 23 floors / 161 — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://jafugroupkenya.com/ | Jafu Group Kenya | developer | **Always keep** — brand face; **Serene Manor** featured; **no Citrine page / no contacts** recovered this pass |
| 2 | https://hauzisha.co.ke/developments/citrine-heights/ | Hauzisha | portal | 23 floors / 161; 1BR&2BR; 68–125; 7.3–11M; Jafu — conf ≤2; **ignore 0730 phone** |
| 3 | https://commercialpropertykenya.com/properties/citrine-heights-westlands-nairobi/ | CPK | agent | Densest typed prices/sizes; June 2028; UC; amenities + parking |
| 4 | https://craiovarealtors.com/property/one-two-bedrooms-at-citrine-heights-in-westlands/ | Craiova Realtors | agent | Higher price sheet; **20%** deposit; Aug 2028 |
| 5 | https://habarihomes.com/property/1-bedrooms-at-citrine-tower-apartments-in-westlands/ | Habari Homes | agent | Typed **7.3 / 11 / 12.9**; June 2028; flexible payment |
| 6 | https://villawatchkenya.com/listing/citrine-tower-1-bedroom-apartment-westlands/ | VillaWatch Kenya | agent | Alias **Citrine Tower**; from 7.3M; Jafu; Q3 2026 launch |
| 7 | https://realtors.co.ke/property/citrine-tower-westlands-nairobis-premier-investment-address/ | Realtors Kenya | agent | Jafu attribution; opposite GTC; call-for-price |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://hauzisha.co.ke/developers/jafu-real-estate-group/ | Developer hub overlap with Citrine page; same **0730** CTA |
| https://villawatchkenya.com/listing/citrine-tower-2-bedroom-apartment-westlands/ | Overlaps retained VillaWatch 1BR page |
| https://ladvarealtors.com/why-citrine-tower-in-westlands-is-a-smart-investment-in-2026/ | Marketing blog; specs echo CPK without payment |
| https://nairobirealestate.co.ke/developers/jafu-real-estate-group | Auris-centric profile; Citrine not published; NRE phone ≠ Jafu |
| BuyRentKenya search (Citrine Heights / Tower) | No dedicated listing found this pass |
| Block.ke search (Citrine Heights / Tower) | No project page; low-trust class anyway |
| https://jafugroupkenya.com/contact · /serene-manor | Fetches returned privacy stub / blocked — no extra Citrine facts |
| Facebook “Jafu Group Real Estate” | 403 / unverified — no official phone captured |

**sources_evaluated 12 · sources_retained 7**

---

## 7. Open questions

1. Obtain **official Citrine** project page / brochure / LOO from Jafu (homepage silent on Citrine this pass).  
2. Official **sales phone / email** — none on recovered Jafu materials.  
3. Resolve price cluster **7.3 / 11 / 12.9** vs Craiova **7.9 / 12.5 / 14.9**.  
4. Lock **payment plan** (developer schedule or ≥4 agent echo).  
5. Resolve completion **June 2028** vs **August 2028**; separate sales-launch **Q3 2026** from handover.  
6. Confirm **inventory_class** `off_plan` vs `building` with construction evidence.  
7. Legal contracting entity / SPV; exact GPS on Westlands Road.  
8. Confirm whether **2BR+DSQ** is in the official mix (Hauzisha unit-mix omits DSQ).

---

## 8. Anti-merge

- **≠ Serene Manor** (Jafu sibling — **Kilimani** / Turbo–Lenana corridor; 1–4BR + duplex PH; completion ~**2027**).  
- **≠ Auris Residence** (Jafu sibling — Westlands **hotel + residences**, ~20 storeys; different product).  
- **≠ Serene Holding Group** schemes (Serene Boutique / Diamond Mango) — unrelated Hauzisha developer.  
- **≠ Casa Rina Heights** (Mvuli Rd Westlands — different developer; do not merge “Heights” names).  
- **≠ Pandora / Panorama West / other Westlands towers** — different brands.  
- **Citrine Heights = Citrine Tower** (marketing alias) — **do merge** under this property; keep alias claim.
