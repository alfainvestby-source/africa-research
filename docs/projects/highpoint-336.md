---
slug: highpoint-336
external_id: DISC-NBO-008
wave: block-2028-wave1
pilot: false
sources_evaluated: 12
sources_retained: 7
last_verified_at: 2026-10-16
---

# Highpoint 336 Residences (DISC-NBO-008) — discovery research

**Seeded** (`properties.csv` DISC-NBO-008, changelog **0.1.20**). Block 2028 process-rerun Tier A #3. **Kilimani Road** (Adams), **Highpoint Development / Developers Ltd**, off-plan / UC claims, completion **Q2 / June 2028** cluster (conflicts noted).

Live research accessed **2026-10-16**. Official microsite **highpoint336.co.ke** returned **HTTP 500** this pass — retained via search-indexed official copy + agents. **Block.ke ignored as authority.**

**Method locks applied** (same as corpus).

**≠ Golfscape Residences (NBO-006)** — Golfscape lists Highpoint Residences LTD as `marketing_partner`; do **not** assume same SPV as Highpoint 336 without evidence.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | **Highpoint 336 Residences** | 5 | highpoint336.co.ke (indexed); NRE; BuyRent; Malluu |
| `aliases` | secondary | Highpoint 336; Highpoint 336 Residencies | 4 | NRE spelling; agents |
| `status` | claim set | Off-plan / Pre-Launch (NRE **8%**) vs BuyRent **40% completion** → **`needs_developer_input`** | 2–3 | NRE vs BuyRent |
| `geography.city` | **CANONICAL** | Nairobi | 5 | all |
| `geography.neighbourhood` | **CANONICAL** | **Kilimani** (Adams pocket) | 5 | NRE; official indexed |
| `geography.street` | **CANONICAL** soft | **Kilimani Road**, opposite **Applewood Adams Rear** | 4 | NRE FAQ; official indexed address |
| `geography.parcel` | secondary | **1.11 acres** | 3 | NRE |
| `geography.lat_lng` | unknown | — | 0 | — |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-highpoint-development-ltd` | 4 | BuyRent “Highpoint Development Ltd”; Dial&Move / Malluu “Highpoint Developers Ltd”; LinkedIn Highpoint Development Ltd |
| `unit_types` | **CANONICAL** soft | **2 Bedroom** (multiple types); **3 Bedroom** (± DSQ); **4 Bedroom + DSQ duplex penthouse**; **6 Bedroom + DSQ duplex penthouse** | 4 | NRE; Malluu; Realtors tables |
| `size_by_type` | claim set | See size/price tables — agent matrices agree on sqm labels more than on KES | 3–4 | NRE; Malluu; Realtors |
| `price_claims[]` | multi | See **§1a** — wide agent spread vs official **from 9.9M** | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan.deposit` | secondary — threshold | **20%** deposit (NRE; Malluu; Dial&Move citing developer) — **≥3 agents**, **not** live on microsite this pass (500) → show + treat as **near must-have**; confirm on LOO | 3 | NRE; Malluu; Dial&Move |
| `payment_plan.tenor` | secondary | Balance in instalments to **June 2028**; LinkedIn “**2-year** payment plan”; mortgage via Equity/KCB/Coop/HFCK/Absa (agent) | 2–3 | Malluu; LinkedIn; Dial&Move |
| `completion_estimate` | claim set — **`needs_developer_input`** | **Q2 2028** (NRE) vs **June 2028** (BuyRent/Malluu) vs older **July 2027** search noise | 3 | Prefer 2028 cluster; month NDI vs July 2027 outlier |
| `amenities` | secondary consensus | Pool; gym; sauna; kids play; generator; borehole; CCTV; lifts; coffee/restaurant (lists vary) | 3 | NRE; Malluu; BuyRent |
| `service_charge` | secondary — **`needs_verification`** | ~**KES 8,000** / 2BR; **12,000** / 3BR; **20,000** / penthouse | 2 | Malluu; Dial&Move |
| `legal_title` | unknown | — | 0 | — |

### Size / typed price matrices (agent — keep as claims)

**NRE matrix (conf 3):**

| Type | Size (sqm) | From KES |
|------|----------:|---------:|
| 2BR | 99.1 | 10,110,000 |
| 2BR | 107.53 | 10,970,000 |
| 2BR | 111.17 | 11,420,000 |
| 2BR | 141.21 | 14,410,000 |
| 3BR | 217.1 | 22,140,000 |
| 4BR+DSQ PH | 288.66 | 29,410,000 |
| 6BR+DSQ PH | 433.22 | 44,200,000 |

**Malluu matrix (conf 3) — same sqm labels, higher KES:**

| Type | Size (sqm) | KES |
|------|----------:|----:|
| 2BR Type C | 99.1 | **11.89M** |
| 2BR Type E | 107.53 | **12.90M** |
| 2BR Type D | 111.17 | **13.34M** |
| 3BR Type A | 141.21 | **16.95M** |
| 3BR+DSQ Type B | 217.1 | **26.05M** |
| 4BR+DSQ PH | 288.66 | **34.60M** |
| 6BR+DSQ PH | 433.22 | **52.00M** |

Sqm labels align → likely same product; **KES disagree** → all stay in `price_claims[]`.

### 1a. `price_claims[]`

| # | Claim | Publisher | Conf | Flags |
|--:|-------|-----------|-----:|-------|
| A | From **KES 9.9M** (introductory off-plan) | highpoint336.co.ke (indexed); BuyRent | 4 | Official/portal — microsite live **500** this pass |
| B | NRE typed from **10.11M–44.2M** | nairobirealestate.co.ke | 3 | |
| C | Malluu typed **11.89M–52M** | malluugrealtykenya.com | 3 | Higher than B |
| D | Realtors table from **10.11M** (2BR Type C) | realtors.co.ke (JS-challenged fetch) | 2 | Search/prior snippet |
| E | FAQ “2BR from about **9.9–11.89M**” | NRE FAQ prose | 3 | Bridges A–C |

**No canonical scalar.** Official **9.9M from** is best developer-attributed floor when microsite recovers.

### Payment

| Element | Count / source | Threshold? | Status |
|---------|----------------|------------|--------|
| **20%** deposit | NRE calculator + FAQ; Malluu; Dial&Move (cites Highpoint Developers Ltd) | 3 agents; official page down | Show — **not locked conf 5**; upgrade when microsite/LOO confirms |
| Instalments to completion / 2-year plan | Malluu; LinkedIn Highpoint Development Ltd | Soft | Secondary |
| Mortgage bank list | Malluu; Dial&Move | Soft | Secondary |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-highpoint-development-ltd` |
| `legal_name` | **Highpoint Development Ltd** / **Highpoint Developers Ltd** (string variants — **`needs_verification`** which is registered) |
| `trading_names` | Highpoint; HighPoint Developers Ltd |
| `website` | https://highpoint336.co.ke/ (project; **500** this pass) |
| `evidence` | BuyRent developer field; Dial&Move “seller of record”; LinkedIn company Highpoint Development Ltd; Malluu payment cites Highpoint Developers Ltd |
| `group_company_id` | **null** |
| `sales_contacts` | Indexed: **+254 705 998 888** / **+254 794 779 999**; info@highpoint336.co.ke; BuyRent also **+254 706 327 148** |
| `confidence` | **4** trading / **0** Companies Registry confirmation |

**Do not** merge with Golfscape’s Highpoint Residences LTD marketing_partner without shared-entity evidence.

---

## 3. GroupCompany / RelatedParty

**None invented.** Dial and Move Kenya = relocation/referral partner only (explicitly not payment collector) — optional RelatedParty `marketing_partner` conf 2 if modeled later.

---

## 4. Sources

### Retained

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://highpoint336.co.ke/ | Highpoint | developer | **500** live; retained via search index (from 9.9M, Kilimani Rd, contacts) |
| 2 | https://nairobirealestate.co.ke/properties/highpoint-336-residencies | NRE | agent | Sizes/prices; Q2 2028; 20% calculator |
| 3 | https://www.buyrentkenya.com/project/highpoint-336-residences-kilimani | BuyRent | portal | From 9.9M; June 2028; 40% progress; Highpoint Development Ltd |
| 4 | https://malluugrealtykenya.com/new-developments/highpoint-336-residences/ | Malluu | agent | Higher price matrix; 20%; June 2028; service charge |
| 5 | https://www.affordablemovers.co.ke/2026/06/dial-and-move-kenya-vs-highpoint-336.html | Dial&Move | partner FAQ | Seller-of-record naming; 20%/80%; banks; service charge |
| 6 | https://www.linkedin.com/posts/highpoint-development-ltd_… | Highpoint Development Ltd | developer social | 2-year payment plan claim |
| 7 | https://realtors.co.ke/property/highpoint-336-residencies/ | Realtors | agent | Price table (fetch JS-blocked; search retained lightly) |

### Thin skips

| Item | Why |
|------|-----|
| Block.ke | Low trust |
| CPK Highpoint URL | **403** this pass |
| July 2027 completion snippets without live page | Outlier — do not promote |

**sources_evaluated ~12 · sources_retained 7**

---

## 5. Open questions

1. Recover live **highpoint336.co.ke** (or PDF) for canonical prices/payment.  
2. Registered legal name: Development Ltd vs Developers Ltd.  
3. Construction progress: **8%** vs **40%**.  
4. Completion: **Q2 vs June 2028** (and discard 2027 unless developer restates).  
5. Relation (if any) to Golfscape’s Highpoint Residences LTD.  
6. GPS / LR number for Kilimani Road parcel.

---

## 6. Anti-merge

- **≠ Golfscape (NBO-006)** despite “Highpoint” marketing name overlap.  
- **≠** other Kilimani “336” or Adams Road projects without Kilimani Road / Applewood Adams Rear address match.
