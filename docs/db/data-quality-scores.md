# Data quality / risk scores

**Skill:** Data quality / risk scorer ([spec](../agents/data-quality-scorer.md))  
**Date:** 2026-10-16  
**Corpus:** **11** method-complete dossiers (same denominator as [field-promotion.md](field-promotion.md))  
**Purpose:** Admin triage queue + Plus trust-signal inputs. **No invented facts** — scores only over dossier flags and meta.

Related: [decisions.md](../decisions.md) · [nairobi-master-index.md](../nairobi-master-index.md) · [schema.md](schema.md)

---

## Rubric (v1)

### Input metrics (per property)

| Metric | Definition |
|--------|------------|
| `ndi_count` | Distinct **substantive fields** carrying **`needs_developer_input`** (claim rows + conflict resolutions that apply the flag). Legend/method boilerplate ignored. |
| `nv_count` | Distinct **topic themes** carrying **`needs_verification`** (deduped: e.g. many 2BR price rows → one typology/price theme). |
| `developer_conf` | Primary-developer confidence **0–5** from dossier. |
| `sources_retained` | Dossier `sources_retained` (process floor ≥5). |
| `agent_only_commercial` | Count of commercial pillars **{price, payment_deposit, completion}** with **no developer-backed canonical** (agent/portal only). Pillars with developer material but **`needs_developer_input`** count under NDI, not here. |

### Composite `risk_score` (0–100, higher = more Admin urgency)

| Component | Points |
|-----------|--------|
| NDI density | `min(32, ndi_count × 8)` |
| NV density | `min(24, nv_count × 2)` |
| Weak developer | conf ≤2 → **25**; =3 → **15**; =4 → **8**; =5 → **0** |
| Thin sources | retained &lt;8 → **10**; 8–9 → **5**; ≥10 → **0** |
| Agent-only commercial | `agent_only_commercial × 5` (max **15**) |

`risk_score` = sum of components, capped at **100**.

### Triage bands (Admin)

| Band | `risk_score` | Meaning |
|------|-------------:|---------|
| **P0 — Critical** | ≥ **55** | Weak developer identity and/or extreme unresolved risk; verification first |
| **P1 — High** | **40–54** | Multiple NDI or weak commercial provenance; clear before promoting public columns |
| **P2 — Medium** | **25–39** | Manageable; agent-only commercial and/or moderate NV |
| **P3 — Monitor** | ≤ **24** | Stronger developer stack; residual NV/NDI tracked |

**Plus trust signal (derived, not shown on public):**  
`trust = clamp(100 − risk_score, 0, 100)` → High ≥75 · Medium 50–74 · Low &lt;50.

---

## Canonical triage ranking

| Rank | Band | external_id | Project | risk | trust | NDI | NV | Dev | Src | AO-comm | Top blockers |
|-----:|------|-------------|---------|-----:|------:|----:|---:|----:|----:|--------:|--------------|
| 1 | **P0** | NBO-017 | [Misty Springs](../projects/misty-springs.md) | **66** | 34 | 0 | 8 | **2** | 10 | **3** | Developer lead only (Tian Yu); all commercial agent-only; status/completion conflict |
| 2 | **P1** | NBO-010 | [Berkeley Homes](../projects/berkeley-homes.md) | **41** | 59 | 1 | 5 | **4** | 10 | **3** | ESIA 361 vs agents 360; marketing site silent on legal name; agent-only commercial |
| 3 | **P1** | NBO-013 | [Galaxy One](../projects/galaxy-one.md) | **40** | 60 | **4** | 4 | 5 | 10 | 0 | Official-vs-official: units, storeys, dual prices, construction % |
| 4 | **P2** | NBO-005 | [Astra Bay Residence](../projects/astra-bay-residence.md) | **36** | 64 | 0 | 8 | 5 | **9** | **3** | No developer KES/date; heavy NV typology/prices |
| 5 | **P2** | NBO-002 | [Pandora Residences](../projects/pandora-residences.md) | **28** | 72 | 1 | 5 | 5 | 10 | **2** | Official unit-mix NDI; agent payment; completion not on brochure extract |
| 6 | **P2** | NBO-001 | [Golden Mansion](../projects/golden-mansion.md) | **27** | 73 | 0 | 6 | 5 | 11 | **3** | EIA identity strong; commercial agent-only |
| 7 | **P2** | NBO-004 | [Porini Point](../projects/porini-point.md) | **26** | 74 | **2** | 5 | 5 | 10 | 0 | Official price_from + payment-tenor NDI |
| 8 | **P2** | NBO-003 | [Riara Oasis](../projects/riara-oasis.md) | **25** | 75 | 0 | 5 | 5 | 10 | **3** | NEMA strong; commercial stack agent-side |
| 9 | **P2** | NBO-009 | [Gemini Residency Phase 2](../projects/gemini-residency-phase-2.md) | **25** | 75 | 1 | 6 | 5 | 10 | 1 | Site Mar 2029 vs LinkedIn 2026–2028 NDI; agent prices |
| 10 | **P3** | NBO-008 | [Longines Bay Kilimani](../projects/longines-bay-kilimani.md) | **24** | 76 | **2** | 4 | 5 | 10 | 0 | NEMA 601/3-blocks vs marketing; 18 vs “24th floor” NDI |
| 11 | **P3** | NBO-007 | [Diamond Bay Residences](../projects/diamond-bay-residences.md) | **18** | 82 | 1 | 5 | 5 | **12** | 0 | Official 8.84M vs 9.34M NDI; densest retained sources |

**AO-comm** = `agent_only_commercial` (0–3).

### Component arithmetic

| external_id | NDI pts | NV pts | Dev pts | Src pts | AO pts | risk |
|-------------|--------:|-------:|--------:|--------:|-------:|-----:|
| NBO-017 | 0 | 16 | 25 | 0 | 15 | **66** |
| NBO-010 | 8 | 10 | 8 | 0 | 15 | **41** |
| NBO-013 | 32 | 8 | 0 | 0 | 0 | **40** |
| NBO-005 | 0 | 16 | 0 | 5 | 15 | **36** |
| NBO-002 | 8 | 10 | 0 | 0 | 10 | **28** |
| NBO-001 | 0 | 12 | 0 | 0 | 15 | **27** |
| NBO-004 | 16 | 10 | 0 | 0 | 0 | **26** |
| NBO-003 | 0 | 10 | 0 | 0 | 15 | **25** |
| NBO-009 | 8 | 12 | 0 | 0 | 5 | **25** |
| NBO-008 | 16 | 8 | 0 | 0 | 0 | **24** |
| NBO-007 | 8 | 10 | 0 | 0 | 0 | **18** |

---

## Metric detail

### NDI fields counted

| external_id | Fields |
|-------------|--------|
| NBO-017 | *(none — no developer commercial stack to conflict)* |
| NBO-010 | `total_units` (361 ESIA vs 360 agents) |
| NBO-013 | `total_units`; `storeys`; `price_claims[]` (dual official); `construction_progress` |
| NBO-005 | *(none this pass)* |
| NBO-002 | `unit_types` / unit mix (official vs official) |
| NBO-001 | *(none — 29 vs 30 storeys kept as NV, not second official page)* |
| NBO-004 | `price_from` / price tables; `payment_plan.tenor` |
| NBO-003 | *(none — 23 vs 22 = filing vs agents, not dual official)* |
| NBO-009 | `completion_estimate` Phase 2 (site vs LinkedIn About) |
| NBO-008 | `total_units`/`block_count`; `storeys` (18 vs journal 24th) |
| NBO-007 | `price_claims[]` entry-from (8.84M vs 9.34M official) |

### Agent-only commercial pillars

| external_id | price | payment_deposit | completion | AO count |
|-------------|-------|-----------------|------------|---------:|
| NBO-017 | agent | agent (30% ≥4) | agent | 3 |
| NBO-010 | agent | agent (20% ≥4) | agent | 3 |
| NBO-013 | NDI (official dual) | **developer 10%** | **developer** | 0 |
| NBO-005 | agent | agent (20% ≥4) | agent | 3 |
| NBO-002 | developer brochure bands (not AO) | agent | agent | 2 |
| NBO-001 | agent | agent (20% ≥4) | agent | 3 |
| NBO-004 | NDI | developer soft / deposit NV | **developer** | 0 |
| NBO-003 | agent | agent (20% ≥4) | agent | 3 |
| NBO-009 | agent | **developer min 20%** | NDI | 1 |
| NBO-008 | developer bands | **developer staged** | developer/marketing | 0 |
| NBO-007 | NDI | developer soft (existence) | **developer** | 0 |

---

## Admin action queue

| Priority | Action | Properties |
|----------|--------|------------|
| **P0** | Verify legal developer (registry / LOO letterhead); freeze public developer badge | **Misty Springs** |
| **P1** | Confirm ESIA plot ↔ Berkeley Homes brand; publish unit count + LOO | **Berkeley Homes** |
| **P1** | Developer input pack: units, storeys, binding price list, construction snapshot | **Galaxy One** |
| **P2** | Obtain developer price list + completion letter | Astra, Pandora, Golden, Riara, Gemini |
| **P2** | Resolve official price/tenor / scale conflicts | Porini, Longines, Diamond |
| **P3** | Monitor residual NV after price NDI cleared | Diamond Bay |

Hand off cleared NDI/NV items to **Verification queue owner** (proposed) when that skill launches.

---

## Plus trust signals (product use)

| Signal | Source | Suggested Plus use |
|--------|--------|-------------------|
| `trust` 0–100 | `100 − risk_score` | Sort / filter “data confidence” |
| `ndi_count` | above | Badge: “Developer confirmation needed” if &gt;0 |
| `developer_conf` | above | Hide weak IDs from pitch sheets until ≥4 |
| `agent_only_commercial` | above | Label price/payment as “agency-reported” |
| `sources_retained` | above | Research-depth meta (Admin + Plus) |

**Public portal:** do **not** show raw risk scores or NDI dumps (confidence internal). Use scores only to **gate** which fields surface ([field-promotion.md](field-promotion.md)).

---

## Excluded

| Slug | Reason |
|------|--------|
| Golfscape · Lesonia · Luna Oak | Premature Wave-B stubs — not method-complete |

Re-score after each research wave or verification pass.

---

## Change log

| Date | Note |
|------|------|
| 2026-10-16 | v1 rubric + first pass over 11 method-complete dossiers |
