# Payment-plan normalizer

**Skill:** [payment-plan-normalizer.md](../agents/payment-plan-normalizer.md)  
**Date:** 2026-10-16  
**Seed:** [`seed/payment_plan_claims.csv`](seed/payment_plan_claims.csv)  
**Rule:** Every row is sourced from a research dossier. **No invented plans.** Agent-only consensus caps at **conf ≤3** without developer corroboration. Must-have when **any developer source** OR **≥4 independent agents**.

Related: [schema.md](schema.md) (`payment_plan_claim`) · [decisions.md](../decisions.md) · [field-promotion.md](field-promotion.md)

---

## Corpus

| Bucket | n | Payment extract |
|--------|--:|-----------------|
| Method-complete (seeded properties) | **11** | Full rows in CSV |
| Premature stubs | **3** | Golfscape / Luna Oak = **no usable plan**; Lesonia = thin search “from 20%” only — **not** seeded (incomplete method pass) |

---

## Element vocabulary

| `element` | Meaning |
|-----------|---------|
| `deposit_pct` | Reservation / booking deposit as % of price |
| `tenor_months` | Instalment duration in months (or “up to”) |
| `booking_fee` / `reservation_fee` | Fixed fee (KES or USD) |
| `balance_rule` | Soft schedule language, staged %, cash tiers, plan-exists |
| `sharia_available` | Islamic financing availability claim |

| `cash_vs_instalment` | Meaning |
|----------------------|---------|
| `cash` | Claim describes cash / lump tiers |
| `instalment` | Staged / construction-linked |
| `both` | Explicit dual framing |
| `unknown` | Deposit/fee without cash vs instalment distinction |

---

## Rollup by property

### Pandora Residences — NBO-002 (`prop-pandora-residences`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **20%** | 3 | no | — | **yes** (≥4 agents) | Block; NRE; Ladva; Sydia |
| balance_rule | Balance / flexible to completion | 3 | no | — | soft yes | Same + Ravi |
| tenor_months | **36** quarterly | 2 | no | **NV** | no | Ladva only |

No developer payment schedule → **no canonical plan**.

### Astra Bay Residence — NBO-005 (`prop-astra-bay-residence`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **20%** | 3 | no | — | **yes** | Block; Vorsa; Craiova; A-list |
| balance_rule | Balance over construction | 3 | no | — | soft yes | Same |
| booking_fee | **~KES 100,000** | 2 | no | **NV** | no | Block only |

Cash vs instalment dual columns: **not published** this pass.

### Porini Point — NBO-004 (`prop-porini-point`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| balance_rule | Plans **exist** (cash + instalment) | 5 | **yes** (existence) | — | **yes** (developer) | Launch news; packs |
| tenor_months | **24 / 2 years** | 5 | **no** | **NDI** | field met; tenor not collapsed | Launch news; info-pack; agents |
| tenor_months | **Up to 3 years** | 5 | **no** | **NDI** | — | Property pack |
| deposit_pct | **10%** after reservation | 1 | no | **NV** | no | FAQ 404 snippet |
| reservation_fee | **USD 1,550** | 1 | no | **NV** | no | FAQ 404 snippet |
| deposit_pct | **~20%** estimate | 2 | no | **NV** | no | Block |
| sharia_available | Available (terms unknown) | 5 | **yes** (availability) | — | soft | Launch news |
| balance_rule | Cash incentives / up to 10.7% | 4/1 | no | **NV** on % | no | Launch news; FAQ 404 |

**Lock:** official tenor conflict → keep **both**; **no** assumed canonical tenor.

### Galaxy ONE — NBO-013 (`prop-galaxy-one`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **10%** to reserve | 5 | **yes** | — | **yes** (developer) | galaxyone.co; lionston.co |
| deposit_pct | **20%** | 3 | no | **NV** | agent threshold | Ravi; Masterways; Coral; NRE; … |
| balance_rule | Flexible / over construction | 3 | no | — | soft | Agents + developer copy |
| balance_rule | Official **cash vs instalment** price columns | 5 | no | **NDI** (vs other official bands) | — | FAQ / JSON-LD |

### Riara Oasis — NBO-003 (`prop-riara-oasis`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **20%** | 3 | no | — | **yes** (≥4) | Block; AIMASI; Sir Francis; A-list; NRE; CPK; Craiova |
| deposit_pct | Optional **30%** | 3 | no | — | no | Sir Francis; A-list; CPK |
| deposit_pct | Optional **50%** | 3 | no | — | no | Sir Francis; A-list; CPK; NRE |
| balance_rule | Balance over construction | 3 | no | — | soft yes | Multi-agent |

No developer LOO.

### Gemini Residency Phase 2 — NBO-009 (`prop-gemini-residency-phase-2`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **Min 20%** | 5 | **yes** | — | **yes** (developer) | staroot contact FAQ |
| deposit_pct | Select cases **10%** | 5 | no (select) | — | with min 20% | Same FAQ |
| deposit_pct | Agent **20%** | 3 | no | — | aligns | CPK; KeDwell; Malluug; NRE |
| balance_rule | **30/50/20** (Phase 1 / NRE) | 2 | no | **NV** | no | BD Phase 1; NRE |
| tenor_months | Up to **36** | 3 | no | — | soft | BD Phase 2; Staroot |
| balance_rule | Cash tiers 20/50/100% (CPK P1-style) | 2 | no | **NV** | no | CPK |

### Diamond Bay Residences — NBO-007 (`prop-diamond-bay-residences`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| balance_rule | Instalment plans **exist** | 4 | **yes** (existence) | — | **yes** (developer) | henbon.co/about |
| deposit_pct | **20%** | 3 | no | **NV** | **yes** (≥4 agents) | CPK; Azipa; Flamingo; Ace |
| tenor_months | Up to **24** | 2 | no | **NV** | no | Sir Francis; … |
| balance_rule | Azipa staged 20→10×3→20→30 | 2 | no | **NV** | no | Azipa |
| balance_rule | CPK cash 20/30/balance 60d | 2 | no | **NV** | no | CPK |
| balance_rule | Realtors **5%/15%** | 1 | no | **NV** | no | Realtors.co.ke |

Distinguish **`payment_plan.exists`** (canonical soft) vs **`deposit_pct`** (agent NV).

### Misty Springs — NBO-017 (`prop-misty-springs`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **30%** | 3 | no | **NV** | **yes** (≥4; no developer) | Own It; Klin; Flamingo; Azipa; … |
| tenor_months | **~30 mo / 2½ yrs** | 3 | no | **NV** | soft yes | Multi-agent |
| balance_rule | Balance within **60 days** | 1 | no | **NV** | no | A-list outlier |

### Golden Mansion — NBO-001 (`prop-golden-mansion`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **20%** | 3 | no | — | **yes** (≥4) | Block; Masterways; A-list; NRE |
| balance_rule | Flexible instalments to completion | 3 | no | — | soft yes | ≥4 incl. SkyPeak |
| reservation_fee | **KES 200,000** | 2 | no | **NV** | no | Block |
| balance_rule | Staged **10/20/10/10/30** | 2 | no | **NV** | no | Masterways; A-list |

### Longines Bay — NBO-008 (`prop-longines-bay-kilimani`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| balance_rule | Staged construction-linked plans | 5 | **yes** (existence) | — | **yes** (developer FAQ) | longinesbay.com FAQ |
| deposit_pct | **20/50/100%** cash tiers | 3 | no | **NV** | **no** (only 2 agents) | CPK; NRE |

### Berkeley Homes — NBO-010 (`prop-berkeley-homes`)

| Element | Value | Conf | Canonical? | needs_* | Must-have? | Sources |
|---------|-------|-----:|:----------:|---------|:----------:|---------|
| deposit_pct | **20%** | 3 | no | **NV** | **yes** (≥4) | Block; Ravi; Vorsa; GNA; Realtors; NRE; Sir Francis |
| balance_rule | Balance to completion | 3 | no | — | soft yes | Multi-agent |
| tenor_months | Up to **36** | 2 | no | **NV** | no | Vorsa |
| balance_rule | Sir Francis staged % | 2 | no | **NV** | no | Sir Francis |

---

## Analytics summary

| Metric | Count / note |
|--------|----------------|
| Seed rows | **47** claims across **11** properties |
| Canonical deposits | Galaxy **10%**; Gemini min **20%** (+ select 10%) |
| Canonical plan-existence (no %) | Porini; Diamond; Longines |
| Must-have via agents only (conf 3) | Pandora; Astra; Riara; Misty **30%**; Golden; Berkeley; Diamond deposit |
| Official-vs-official (**NDI**) | Porini tenor 24 vs 36; Galaxy cash/instalment price framing |
| Booking / reservation fees | Astra KES 100k; Golden KES 200k; Porini USD 1,550 (404) — all sparse / NV |
| Dominant deposit band | **20%** on most Nairobi towers; Misty **30%**; Galaxy official **10%** |

### Plus / Admin / Public (ties to field-promotion)

| Surface | What to show |
|---------|----------------|
| **`public`** | Only stable must-have deposit when not NDI and (developer **or** ≥4 agents); prefer developer % when present |
| **`plus`** | Full multi-row plan set; cash vs instalment; tenor options; booking fees |
| **`admin`** | All rows + `needs_*` + source lists + threshold math |

---

## Corrections vs prior seed

- Porini **24-month** tenor: was marked `is_canonical=true` — **corrected to false** + `needs_developer_input` (official conflict with 3-year pack).
- Added missing Riara / schedule / fee / cash-tier rows from half-batch dossiers.
- Extended CSV with `external_id`, `cash_vs_instalment`, `sources` for analytics joins.

---

## Out of scope / not invented

- Binding LOO PDFs not fetched → no fabricated milestone calendars.
- Stub dossiers (Golfscape, Lesonia, Luna Oak) not promoted into seed rows.
- Mortgage product APRs, bank names — only when dossiers name them (none as structured claims this pass except Porini sharia **availability**).
