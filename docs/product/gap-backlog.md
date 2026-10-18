---
title: Product gap backlog
skill: product-readiness-reviewer
version: 0.1.0
updated: 2026-10-16
---

# Gap backlog — public MVP vs Plus MVP

Prioritized from first readiness pass ([readiness-scorecard.md](readiness-scorecard.md)). Tied to [surface-map.md](surface-map.md) IDs. **No invented facts.**

---

## P0 — blocks public MVP or Admin trust

| # | Gap | Blocks | Action / skill | Evidence |
|--:|-----|--------|----------------|----------|
| 1 | **Hero / filter price policy unenforced in product** | A4 | Keep multi `price_claims[]`; never emit single `price_from` when NDI | Lulu 4.4M vs typed; Diamond Bay; Porini; Golfscape; Luna Oak; Brookside |
| 2 | **Verification queues not operated** | B2–B3 | Launch **Verification queue owner** on [verification-queue.md](../db/verification-queue.md) | Misty P0; Highpoint progress NDI; Galaxy official duals |
| 3 | **Weak / unknown developer on public candidates** | A2, trust | Verify or keep **admin-only** until conf ≥4 | Misty (2); Polaris (0); Alba (3); Brookside legal NV |
| 4 | **Wave-1 not seeded + no media/geo** | A7–A10 | Seed ingest DISC-NBO-007/008/009; photo collector; geo enricher | Scorecard §1 |
| 5 | **Highpoint official surface down** | A4, C2 | Recover highpoint336.co.ke / PDF; else keep NV on payment | Microsite HTTP 500 |

## P1 — blocks Plus usefulness or public depth

| # | Gap | Blocks | Action / skill | Evidence |
|--:|-----|--------|----------------|----------|
| 6 | **Payment normalizer seed stuck at 11 props** | C2 | Re-run payment-plan normalizer over all 30 dossiers | Wave-1 Lulu/Jabali strong but not in CSV |
| 7 | **Official-vs-official size / unit mix NDI** | A3, C6, comps | Document intel + developer chase | Jabali FAQ vs now-selling; Pandora mix; Kai taxonomy |
| 8 | **Full DQ / coverage recompute over 30 dossiers** | D9, B8 | Refresh DQ scorer + field-promotion denominator | Still 11-dossier baseline |
| 9 | **Brochure / PDF schedules trapped** | A9, C1–C2 | Document / brochure intelligence | Lulu brochure kept; many PDFs unfetched |
| 10 | **Entity resolution for new trading names** | C3–C4 | ER pass: Mi Vida, Highpoint Dev Ltd, Sunmon (wave-2), Sequoia | New wave entities |

## P2 — enrich / later

| # | Gap | Blocks | Action |
|--:|-----|--------|--------|
| 11 | Construction progress series | C5 | Capture when developer tracker exists; never invent % |
| 12 | Agency coverage map | C10 | Who sells which corridor |
| 13 | Inventory / units left | Plus sales | Only if multi-source reliable |
| 14 | Similar developments / yield | A12, C9 | Deferred — needs rules + rental corpus |
| 15 | Block Tier A remainder | Corpus growth | After verification capacity: AYA, Gamil, KEZA Ph2, … |

## Optional later (do not implement now)

| # | Item | Notes |
|--:|------|-------|
| O1 | **Allow Ready dossier research later** | Today: `inventory_class=ready` is **stored but never dossiered**. Revisit only if product wants handed-over / Ready stock in the research corpus. Schema already has the mark ([schema.md](../db/schema.md) v0.1.14). Also noted in [verification-queue.md](../db/verification-queue.md). |

---

## Explicit non-gaps (do not work)

- Ingesting Block.ke apartment listings as inventory  
- Publishing Karura Forest Views as a development  
- Inventing comps, yields, or GPS  
- Dossiering Ready-tagged Hauzisha/portal inventory (until O1)  

---

## Ordered work plan (coordinator)

1. **Verification queue owner** clears Misty / Highpoint / Galaxy / Lulu price NDI slice.  
2. **Seed + photo + geo** for Block wave-1.  
3. **Finish wave-2 research** (Balkis, Hephé) then AYA.  
4. **Payment + DQ refresh** over full method-complete set.  
5. Only then expand discovery waves aggressively.
