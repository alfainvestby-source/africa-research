---
title: Product readiness scorecard
skill: product-readiness-reviewer
version: 0.1.0
updated: 2026-10-16
pass: first-review-slice-block-wave1
---

# Product readiness scorecard

**Agent:** Product Readiness Reviewer ([spec](../agents/product-readiness-reviewer.md))  
**Pass date:** 2026-10-16  
**Question:** Are we ready for a Kenya Rightmove (public) + Admin + Plus/pro hub — and what’s still missing?

**Rules:** No invented facts. Developments only. Block.ke never public-canonical. Public = high confidence **and** high coverage.

Related: [surface-map.md](surface-map.md) · [field-promotion.md](../db/field-promotion.md) · [data-quality-scores.md](../db/data-quality-scores.md) · [gap-backlog.md](gap-backlog.md) · [verification-queue.md](../db/verification-queue.md) · [plus-readiness.md](plus-readiness.md)

---

## 1. Inventory (R5)

| Bucket | n | Notes |
|--------|--:|-------|
| **Method-complete dossiers** (claim tables + `sources_retained` ≥5) | **30** | 27 seeded in [corpus-rollup](../db/seed/corpus-rollup.md) + Block wave-1 **DISC-NBO-007/008/009** |
| **Seeded in `properties.csv`** | **27** | Wave-1 Block three **not yet seeded** |
| **Photo manifests present** | **26** | Lesonia gap; **wave-1 three have no media folder yet** |
| **Geo pins** | **26/27** seeded | ELD-001 unknown; wave-1 three **unpinned** |
| **Discovery-only / not dossiered** | Block Tier A remainder + national leads | **Not** public inventory |
| **Hold / contamination** | Karura Forest Views etc. | Stay off public forever until independent name exists |

**Denominator for this scorecard’s public %:** method-complete dossiers only. Thin leads and Block-only names do not vote fields onto the portal.

**Prior DQ / promotion pass** still covers the original **11** Wave-B method-complete set ([data-quality-scores](../db/data-quality-scores.md)). This review **extends** with Block wave-1 + corpus-wide product lights; a full DQ recompute over all 30 is queued as follow-up (see backlog P1).

---

## 2. Traffic lights — Block wave-1 (stress test)

Legend: **G** pass · **A** amber / partial · **R** fail for that tier · **—** not assessed

| ID | Project | Public | Admin | Plus | Risk band (est.) | One-line |
|----|---------|:------:|:-----:|:----:|------------------|----------|
| DISC-NBO-007 | [237 Lulu](../projects/237-lulu.md) | **A** | **G** | **G** | **P3** (~17) | Strong Mi Vida payment + place; **official from-price NDI** blocks public hero price; no media/geo yet |
| DISC-NBO-008 | [Highpoint 336](../projects/highpoint-336.md) | **R/A** | **G** | **A** | **P1** (~45) | Microsite **500**; progress **8% vs 40%** NDI; deposit near-threshold (3 agents); developer string NV |
| DISC-NBO-009 | [Jabali Towers](../projects/jabali-towers.md) | **A** | **G** | **G** | **P3** (~20) | Rendeavour FAQ dense (payment/Dec 2028/tenure); **official size schedules NDI**; thin media |

### Dimension detail (wave-1)

#### Public (consumer card)

| Dimension | 237 Lulu | Highpoint 336 | Jabali |
|-----------|----------|---------------|--------|
| Identity | **G** | **G** | **G** |
| Place (nbhd) | **G** Garden City | **G** Kilimani/Adams | **G** Tatu Central |
| Developer conf ≥4 | **G** Mi Vida (5) | **A** Highpoint Dev Ltd (4; name string NV) | **G** Rendeavour (5) |
| Product / unit types | **G** | **A** agent matrices | **G** types; **R** sizes (NDI) |
| Commercial (no NDI hero) | **R** 4.4M vs typed | **A** 9.9M indexed only | **A** typed KES from FAQ OK as multi, no single portal scalar |
| Media ≥1 verified | **R** not collected | **R** | **R** |
| Trust (≥5 non-Block) | **G** 8 retained | **A** 7; official live down | **G** 7 |

**Verdict:** None of wave-1 is **public-shippable as a full Rightmove card** yet — identity/place/developer are close, but **media + hero-price policy + Highpoint live official** block ship. Jabali and Lulu are the closest once media + NDI clears.

#### Admin (ops)

All three: **G** — conflicts explicit, sources counted, parties separated, open questions actionable. Ready for Admin conflict browser / queues.

#### Plus (agent hub)

| Dimension | 237 Lulu | Highpoint | Jabali |
|-----------|----------|-----------|--------|
| Multi-price table | **G** (≥4 claims) | **G** (NRE/Malluu/official) | **G** (KES + USD bands) |
| Payment normalized | **G** developer type-based | **A** 20% near-threshold | **G** 10% / 36-mo |
| Agent graph ≥2 | **G** | **G** | **A** (more master-plan than multi-agency) |
| Comps hook (size+price) | **G** | **G** sqm aligned | **R** until size NDI clears |
| Trust signal | High | Medium/Low | High |

---

## 3. Corpus baseline (seeded 11 DQ + pattern read)

From [data-quality-scores.md](../db/data-quality-scores.md) (11-dossier pass):

| Band | Count | Examples |
|------|------:|----------|
| **P0** | 1 | Misty Springs (weak developer + agent-only commercial) |
| **P1** | 2 | Berkeley Homes; Galaxy One |
| **P2** | 6 | Astra, Pandora, Golden, Porini, Riara, Gemini |
| **P3** | 2 | Longines; Diamond Bay |

**Public shortlist fields** (still locked from [field-promotion](../db/field-promotion.md)): canonical name, neighbourhood, primary developer (conf≥4), developer amenities core, canonical unit types, developer sizes when agreed, status summary, completion when not NDI, payment deposit when threshold + stable.

**Still non-public corpus-wide:** `price_from` hero, lat/lng, construction %, unit_count/storeys scalars, full agent WhatsApp graph.

**Wave C / discovery pattern (not fully re-scored):** many strong identities (CANTO, Capricorn, Sensei) but recurring blockers — payment unmet (CANTO, DIA-001, ELD-001, Ankori deposit %), weak/unknown developer (Polaris, Misty, Brookside legal NV), official price NDI (Golfscape, Luna Oak, Brookside Oak, NAK-001).

---

## 4. Surface capability snapshot (R2)

Against [surface-map.md](surface-map.md):

| Cap | Gap now | Evidence |
|-----|---------|----------|
| A1–A3 Search area/dev/beds | **partial** | Modeled; wave-1 not seeded; geo pins missing for wave-1 |
| A4 Price filter / hero | **partial / blocked** | Multi claims exist; public hero blocked on NDI (Lulu, many corpus) |
| A7 Identity page | **ok** (data) | Dossiers ready; UI not in this store |
| A9 Media gallery | **partial** | 26 manifests; **0** for wave-1; Lesonia empty |
| A10 Map pin | **partial** | 26/27 seeded; wave-1 unpinned |
| B2–B3 Verification queues | **partial → improving** | This pass creates [verification-queue.md](../db/verification-queue.md) |
| C1–C3 Plus price/payment/agents | **partial** | Strong on Lulu/Jabali; payment CSV still 11-prop seed |
| C9 Yield / comps tools | **deferred / sparse** | Area comps exist Plus-only; wave-1 Jabali size NDI blocks |

---

## 5. Exec summary

1. **We can run Admin today** on the researched corpus — claim hygiene is the strength.  
2. **Public MVP is not shippable** on a clean Rightmove bar: hero price policy + coverage gates + missing media/geo on newest dossiers + several weak-developer rows (Misty, Polaris).  
3. **Plus is closer than public** for strong-developer projects (Lulu, Jabali, Porini, Galaxy, Diamond Bay) — multi-price + payment + agent graphs already exist in dossiers.  
4. **Next lever is verification, not more raw discovery** for P0/P1 facts — then seed wave-1 + photos + geo — then continue Block Tier A (Balkis / Hephé in flight).

**Recommended next agents:** Verification queue owner (clear P0/P1) · Photo collector on wave-1 · Geo enricher on wave-1 · Seed ingest for DISC-NBO-007/008/009 · Continue research wave-2.
