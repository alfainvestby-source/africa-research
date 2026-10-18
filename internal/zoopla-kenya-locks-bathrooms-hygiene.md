---
cursor:
  subagentId: "bc-1bdc7ab6-93cc-513e-a234-3ba81ab0f03b"
---

# Zoopla→Kenya locks #2–8 + bathrooms hygiene

**Date:** 2026-10-17  
**Agent:** bc-1bdc7ab6-93cc-513e-a234-3ba81ab0f03b

## Locks written

| Path | Update |
|------|--------|
| `/cursor/stores/self/docs/decisions.md` | #2–8 LOCKED bullets (2B, Kenya energy, buyer costs, bathrooms, tenure, Plus phones, 8B) |
| `/cursor/stores/self/docs/product/zoopla-kenya-product-decisions.md` | status ALL #1–8 LOCKED; checklist answers |
| `/cursor/stores/self/docs/product/zoopla-kenya-gap-eval.md` | open Qs RESOLVED; bathrooms coverage **2/180** |
| `/cursor/stores/self/docs/product/surface-map.md` | public/Plus/Admin aligned; bathrooms P2 done |
| `/cursor/stores/self/preferences.md` | 2B, Plus contacts, 8B, Kenya energy vocab, bathrooms card |
| `/cursor/stores/self/docs/db/schema.md` | v0.1.15 — tenure claim guidance + bathrooms card lock (no DDL column add) |
| `/cursor/stores/self/docs/db/changelog.md` | **0.1.19** — locks + hygiene stats |

**Evidence for 2B / #5:** [`docs/product/zillow-rightmove-model-study.md`](../docs/product/zillow-rightmove-model-study.md)

## Bathrooms extract pass

| Metric | Value |
|--------|-------|
| `unit_types` rows after restore | **180** |
| Explicit `bathrooms` filled | **2** |
| Left blank (no invent) | **178** |
| Properties with typologies | 45 / 46 (`prop-riara-oasis` never had unit_types) |
| Price FK unresolved | **0** |
| `unit_type_features` FK unresolved | **0** |

### Fills

| unit_type_id | bathrooms | conf | NV | Source |
|--------------|-----------|------|----|--------|
| `ut-kings-summit-3br` | **2** | 5 | false | Developer project page (`kings-summit-nakuru.md`) |
| `ut-48th-4br` | **5** | 3 (claim) / row NV | true | Agent/portal Hauzisha + Block (`48-treehouse.md`) |

### Not filled (examples of refuse-to-invent)

- “All ensuite” / ensuite variants (Serene Manor, AYA, Plumeria, Berkeley, Golfscape, Jabali) — no numeric count → leave blank
- Marketing “bathrooms” amenity prose without a count (Donyo, Porini)

### Incident

Mid-pass `unit_types.csv` truncated to **61** rows (write opened before fieldnames settled). Restored from transcript + Wave B ingest payloads to **180** rows with empty `bathrooms` column inserted after `bedrooms`, then applied the two explicit fills above.

## Steward handoff (optional)

- Future research checklist: **bathrooms** when plans/agents state an **explicit integer**; never derive from “all ensuite”.
- Seed CSV is already updated — no further CSV migration needed for this pass.
- Still chase bathrooms on new dossiers; coverage remains sparse (2/180).
