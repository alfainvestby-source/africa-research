---
slug: 237-lulu
external_id: DISC-NBO-007
wave: block-2028-wave1
pilot: false
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-16
---

# 237 Lulu (DISC-NBO-007) — discovery research

**Seeded** (`properties.csv` DISC-NBO-007, changelog **0.1.20**). Block 2028 process-rerun Tier A #1 ([block-2028-process-rerun-batch.md](../discovery/block-2028-process-rerun-batch.md)). Garden City / Thika Road, **Mi Vida Homes**, off-plan / pre-construction, completion **Q3 2028** cluster.

Live research accessed **2026-10-16**. **Block.ke ignored as authority** (low-trust lead only).

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.

**≠** other Mi Vida Garden City products (Amaiya; prior 237 phases sold out) — same precinct, different product.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **237 Lulu** | 5 | mividahomes.com/developments/237-lulu/; gardencityliving.co.ke/237-lulu/ |
| `aliases` | secondary | 237 Lulu Garden City; Lulu at Garden City | 4 | agents; Hauzisha |
| `status` | **CANONICAL** | **Off-plan**; construction to begin **Q3 / July 2026** (developer instalment + CPK) | 5 / 4 | Mi Vida instalment copy; CPK |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Mi Vida; all |
| `geography.neighbourhood` | **CANONICAL** | **Garden City** (Ruaraka / Thika Road corridor) | 5 | Mi Vida; Garden City Living |
| `geography.street` | **CANONICAL** (corridor) | **Thika Superhighway / Exit 7**, within Garden City precinct | 5 | Mi Vida office address; Garden City Living |
| `geography.lat_lng` | unknown this pass | — | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-mi-vida-homes` | 5 | Mi Vida project + About; Garden City Living |
| `unit_types` | **CANONICAL** | **Mini 1** (also called Studio / Deluxe Studio in agents), **1 Bedroom**, **2 Bedroom**, **3 Bedroom** | 5 | Mi Vida unit cards + FAQ; brochure; CPK; WAC; M-Val |
| `size_by_type` | claim set — see table | Mini ~**41** sqm; 1BR ~**50**; 2BR ~**73**; 3BR ~**102** | 4 | Mi Vida typed cards (50/73/102); CPK/WAC 41/50/73/102; Hauzisha 41–102 |
| `total_units` | secondary — **`needs_verification`** | **237** units (agent claim; name echo) | 2 | Westlands Avenue Consult only — **not** on Mi Vida page this pass |
| `building_specs` | unknown | Storeys / blocks not stated on retained sources | 0 | — |
| `price_claims[]` | multi | See **§1a** — **official “from” conflict** | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | Mi Vida |
| `payment_plan` | **CANONICAL** structure | See **§1b** (developer schedule on project page) | 5 | mividahomes.com/237-lulu/ |
| `completion_estimate` | claim set | **Q3 2028** (developer) vs **July 2028** (CPK) vs **July–August 2028** (WAC) vs **August 2028** (Hauzisha) | 5 / 3 | Agree year; month band secondary |
| `amenities` (project + precinct) | **CANONICAL** soft | 24/7 security; backup generator; gym; landscaped gardens; swimming pool; high-speed elevators; IFC **EDGE** + “conventional home technology” (Mi Vida FAQ) | 4 | Mi Vida amenities + FAQ |
| `amenities` precinct | secondary | Garden City Mall / Business Park / 47-acre masterplan; clubhouse; two pools; trails (agent denser lists) | 3 | Garden City Living; CPK; M-Val |
| `roi_claim` | secondary marketing | Up to **9%** unfurnished / **18%** short-stay (prior precinct phases) | 2 | Garden City Living; CPK — **`needs_verification`** |
| `legal_title` | unknown | — | 0 | not found |
| `master_planned_community` | **CANONICAL** soft | Inside **Garden City** mixed-use precinct | 5 | Mi Vida; Garden City Living |

### Size table (retained)

| Type | Size (sqm) | Role | Conf |
|------|----------:|------|-----:|
| Mini 1 / Studio | **41** | CPK; WAC; Hauzisha range start | 4 |
| 1 Bedroom | **50** | Mi Vida typed card; CPK; WAC | 5 |
| 2 Bedroom | **73** | Mi Vida typed card; CPK; WAC | 5 |
| 3 Bedroom | **102** | Mi Vida typed card; CPK; WAC | 5 |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

**Official conflict:** Mi Vida hero/FAQ “from **KES 4.4M**” vs typed product cards **1BR from 6.93M / 2BR 9.57M / 3BR 13.9M** on the **same** developer page → **`needs_developer_input`**.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 4.4M** (hero / FAQ “1-bedroom … from 4.4M”) | Developer hub | mividahomes.com/237-lulu/ | 5 | Official — conflicts with B |
| B | 1BR **50 sqm from KES 6.93M**; 2BR **73 from 9.57M**; 3BR **102 from 13.9M** | Typed cards on same page | mividahomes.com/237-lulu/ | 5 | Official — conflicts with A; disclaimer “estimates” |
| C | Mini 1 **41 sqm from 4.8M**; 1BR **6.3M**; 2BR **8.5M**; 3BR **12.5M** | Agent price list | CPK; WAC | 3 | Between A and B |
| D | Mini **4.4M**; 1BR **5.7M**; 2BR **7.65M**; 3BR **10.7M** | Agent summary | M-Val | 3 | |
| E | Band **KES 6.0M – 13.9M** | Portal card | Hauzisha | 2 | Aggregator |

**Portal scalar:** none. Resolve A vs B with Mi Vida sales / LOO before any “from” field.

### 1b. Payment plan — developer must-have **met**

| Element | Source | Status |
|---------|--------|--------|
| Instalment deposits by type: Studio/Mini **30%** OL; 1BR **20%** OL; 2BR **15%** OL; 3BR **15%** OL; then **10%** on Sale Agreement; balance monthly/quarterly over **24 months** from **Q3 2026** | Mi Vida project page | **CANONICAL** structure (conf 5) |
| Cash: **10%** OL + **10%** SA + **80%** 90 days after SA | Mi Vida project page | **CANONICAL** cash path (conf 5) |
| Agent “**20%** deposit” simplification | WAC FAQ | Secondary — **over-simplifies** developer type-based % → show as agent summary only |
| CPK payment echo (30/20/15 + 10% SA + 24 mo from July 2026) | CPK | Aligns with developer (conf 4) |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-mi-vida-homes` |
| `legal_name` | **Unknown** this pass (trading **Mi Vida Homes**; Companies Registry string not recovered) |
| `trading_names` | Mi Vida; Mi Vida Homes |
| `website` | https://mividahomes.com/ |
| `evidence` | Project page + About (“We Deliver On Time. Every Time.”); Garden City Living co-branded copy; Hauzisha/CPK/WAC attribute Mi Vida |
| `group_company_id` | **null** — none invented |
| `sales_office` | 1st Floor Business Park, Garden City, Off Exit 7 Thika Superhighway; P.O. Box 43233-00100 Nairobi; **+254 722 123 000** / **+254 722 200 032**; info@mividahomes.com |
| `confidence` | **5** trading face / **0** legal SPV |

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Garden City Living / gardencityliving.co.ke | precinct / marketing co-brand | Parallel project page; shared phones | 3 |
| Garden City master developer (precinct owner) | master-plan host | Not named as Lulu SPV this pass | 0 for Lulu contracting |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| CPK Real Estate | Detailed price + payment echo |
| Westlands Avenue Consult | Price table + 237 units claim |
| Hauzisha | Mi Vida attribution; Aug 2028 |
| M-Val | Alternate from-prices |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://mividahomes.com/developments/237-lulu/ | Mi Vida Homes | developer | Primary — prices/payment/completion |
| 2 | https://gardencityliving.co.ke/237-lulu/ | Garden City Living | related / co-brand | Precinct narrative |
| 3 | https://mividahomes.com/wp-content/uploads/2026/03/237-LULU_BROCHURE.pdf | Mi Vida | brochure | Unit mix; contacts |
| 4 | https://commercialpropertykenya.com/properties/237-lulu-apartments-at-garden-city/ | CPK | agent | Prices; July 2026 start / July 2028 |
| 5 | https://westlands-consult.co.ke/property/apartment/237-lulu-garden-city-apartments-for-sale/ | WAC | agent | 4.8/6.3/8.5/12.5; 237 units claim |
| 6 | https://hauzisha.co.ke/developments/237-lulu-garden-city/ | Hauzisha | portal | Mi Vida; Aug 2028 |
| 7 | https://m-val.co.ke/237-lulu-garden-city/ | M-Val | agent | 4.4/5.7/7.65/10.7 |
| 8 | https://mividahomes.com/about/ | Mi Vida | developer | Track-record framing |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| Block.ke project/listings | Low-trust / AI — discovery seed only |
| Agent one-line reprints of Mi Vida FAQ | Overlap |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. Resolve official **from-price** A (4.4M) vs typed cards B (6.93M+).  
2. Legal contracting entity / SPV for LOO.  
3. Confirm **237** total units.  
4. Building storeys / block count.  
5. Exact plot / GPS within Garden City.

---

## 8. Anti-merge

- **≠ Amaiya** (Mi Vida Garden City — higher product).  
- **≠ prior 237 Garden City phases** (sold out per Mi Vida).  
- **≠ KEZA Riruta / KEZA Laika** (same developer, different sites).
