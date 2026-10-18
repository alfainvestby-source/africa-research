---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# DB quality ask-flags — before field standardization

**Date:** 2026-10-17  
**Role:** Proptech DB review (goal + Rightmove/Zoopla + corpus)  
**Rule:** Flag first; **do not standardize** until you answer the asks below.

Related: [goal-and-approach.md](../docs/goal-and-approach.md) · [zoopla-kenya-product-decisions.md](../docs/product/zoopla-kenya-product-decisions.md) · [zillow-rightmove-model-study.md](../docs/product/zillow-rightmove-model-study.md) · [surface-map.md](../docs/product/surface-map.md) · [zoopla-kenya-gap-eval.md](../docs/product/zoopla-kenya-gap-eval.md) · [verification-queue.md](../docs/db/verification-queue.md) · [schema.md](../docs/db/schema.md)

---

## North star (recap)

| Surface | Analogy | Our grain |
|---------|---------|-----------|
| **Public** | Rightmove consumer | **Development-first** (Zoopla lock **2B**); typology-linked listings from retained URLs only; no fake flat IDs |
| **Admin** | Rightmove Admin | Full claims, conflicts, both `needs_*`, sources |
| **Plus** | Rightmove Plus | Multi prices, payment options, agent graphs; agent phones **Plus only** (#7) |

Zoopla is ad-centric; Rightmove New Homes is development + plot/unit feed partner-side. We correctly chose **master property + unit_type + optional listing snapshots** — closer to Rightmove New Homes / Zillow “community” than Zoopla SERP of unit ads.

---

## Corpus snapshot (today)

| Metric | Count | Note |
|--------|------:|------|
| Method dossiers on disk | **51** | `docs/projects/` |
| Seeded `properties.csv` | **46** | **5 dossiers not seeded:** 237 Lulu, Highpoint 336, Jabali, Balkis, Hephé |
| `inventory_class` blank | **27/46** | Process debt |
| `unit_type.bathrooms` filled | **2/180** | Lock #5 — almost empty |
| Lat on property row | **~7/46** | More in `geo_pins` mixed conf |
| Media seed CSV | **0** | DDL exists; photo manifests not rolled into seed graph |
| Real `listing` rows (typology offers) | **~0** | Only Hauzisha lead CSV |
| Named `agent_person` | ~unused | Correct (no invent) |
| Verification queue | **open** | Misty/Polaris/Galaxy/Lulu/… uncleared |

---

## FLAG SET A — Important for the goal, **missing or unusable** for public

These block a Rightmove-class **public** development card even when dossiers exist.

| # | Field / relationship / view | Why it matters (RM/Zoopla) | Our state | Quality |
|--:|----------------------------|----------------------------|-----------|---------|
| A1 | **Public hero / filter price** | RM/Zoopla SERP needs a display price | Multi `price_observation` exists; many **official NDI** | Bad for public scalar — by design until policy enforced in product |
| A2 | **Map pin (verified lat/lng)** | Map search is table-stakes | Sparse on property; CSV GPS often NV | Thin / unsafe for public |
| A3 | **Media gallery** (hero photo, floorplans, brochure) | Every RM/Zoopla card | DDL + some manifests; **no media seed graph** | Missing in DB path |
| A4 | **Bathrooms on unit_type** | Lock #5; filter/card | Column exists; **2/180** | Missing data |
| A5 | **`inventory_class` on every property** | Off-plan/UC vs Ready browse (locks #1/#8) | **27/46** blank | Incomplete |
| A6 | **Canonical developer conf ≥4** | Trust + developer search | Misty conf2, Polaris unknown, Only You/Montbleu null-by-lock | Bad rows must stay admin-only |
| A7 | **Completion window (developer-backed)** | “Available from” filters | Often agent-only / conflicting | Thin for public facets |
| A8 | **Payment when must-have met** | Plus + serious buyers | Many props agent-only &lt;4 | Partial |
| A9 | **Seed sync for wave-1/2 dossiers** | Admin/Plus can’t query unseeded | Lulu/Highpoint/Jabali/Balkis/Hephé **dossier-only** | Pipeline gap |
| A10 | **`listing` typology offers (2B)** | Soft Zoopla cards without fake units | Lead CSV only | Missing product data |

---

## FLAG SET B — Important for Admin / Plus, **modeled but low quality**

| # | Item | State |
|--:|------|-------|
| B1 | Official-vs-official **size / units / storeys / from-price** | Many NDI still open in verification queue |
| B2 | Construction progress % | Sparse; agent UI % often NV |
| B3 | Tenure / sectional title | Lock #6; prose only — almost no structured claims |
| B4 | Service charge / buyer costs per project | Guide OK (#4); per-project rare |
| B5 | POI / transit / schools | Tiny seed (~7 POIs) vs Zoopla “nearby” |
| B6 | GroupCompany / legal SPV | Correctly rare; many trading-only faces (Jafu, Wonder, Oasis) |
| B7 | Feature taxonomy vs free-text amenities | Linked for 39+; synonym noise / scope still messy |
| B8 | Contact ownership (portal 0730 ≠ developer) | Rule locked; QA still manual |
| B9 | Similar developments / yield comps | Missing by design until rules + rental corpus |

---

## FLAG SET C — Views / products we need but don’t have yet

| View | Purpose | Blocked by |
|------|---------|------------|
| **Public SERP row** | name, nbhd, developer, beds range, from-price-or-band, status, hero image | A1–A6, A9 |
| **Public development page** | canonical claims + typology table + CTA | A1, A3, A4, B1 |
| **Admin conflict browser** | claim_conflict workbench | Queue not operated; UI missing |
| **Admin verification worklist** | B2/B3 from surface-map | Queue file exists; owner not clearing |
| **Plus multi-price + payment matrix** | pro tool | Payment normalizer not refreshed over full corpus |
| **Plus agent corridor map** | who sells what | Graph partial; phones Plus-only OK |
| **Coverage / promotion dashboard** | which fields pass public gate | DQ still ~11-dossier baseline; corpus now 46–51 |

---

## ASKS — **ANSWERED 2026-10-18**

Full plain-language locks + examples: [db-quality-decisions-explained-2026-10-18.md](db-quality-decisions-explained-2026-10-18.md)

| Ask | Lock |
|-----|------|
| 1 Hero price | **From X** / **X–Y** / **POA** (Zoopla+RM); never silent NDI pick — [locks](db-quality-locks-2026-10-18.md) |
| 2 Steward order | Seed 007–011 → inventory_class → media → listings |
| 3 Bathrooms | **`unit_type.bathrooms`** + development **min–max** (derived); explicit only |
| 4 Map | **Always show**; online tools first; exact / approx / area badge by conf |
| 5 Weak developer | **Admin-only** until conf≥4 |
| 6 Standardize | **≥70% fill + developer/≥2 agents**; measure then promote |
| 7 DB target | **CSV seeds now**; Postgres when shipping UI |

### Original asks (archive)

### Ask 1 — Public hero price policy (enforce now?)
When official `from` conflicts with typed developer cards (e.g. Lulu 4.4M vs 6.93M+), public should show:

- **1A** Band / “from X (verify)” + no sort-by-price  
- **1B** Suppress price on card until NDI clears (identity-only card)  
- **1C** Show highest-confidence single claim with Admin badge (not recommended)

### Ask 2 — Seed pipeline priority
Next DB steward work should be:

- **2A** Seed the **5 missing** dossiers (007–011) first  
- **2B** Backfill **`inventory_class`** on 27 blank rows first  
- **2C** Build **`listing` typology snapshots** from retained dossier URLs (2B product)  
- **2D** Roll **media manifests → media_asset seed** first  
- Or a ranked order of the above

### Ask 3 — Bathrooms (#5)
Fill bathrooms only when:

- **3A** Explicit “X bathrooms” / floorplan callout (strict — current lean)  
- **3B** Infer 1 bath per ensuite bedroom when marketing says “all ensuite” (riskier)  
- **3C** Leave blank until brochure OCR pass

### Ask 4 — Map pins
Public map requires:

- **4A** Developer/EIA GPS only (conf ≥4)  
- **4B** Neighbourhood centroid OK with “approx” badge  
- **4C** Hide map until pin conf ≥4

### Ask 5 — Weak developers on public
Misty (conf 2), Polaris (unknown), similar:

- **5A** Forever admin-only until conf ≥4  
- **5B** Public with “developer unverified” badge  
- **5C** Drop from public search index entirely

### Ask 6 — Standardization scope (after your answers)
When you green-light, I will propose **field dictionaries** (enums, measure tags, status labels, payment shapes) from gathered data — **without inventing values**. Confirm scope:

- **6A** Status + inventory_class + unit_type labels only  
- **6B** + price_basis / payment_plan shapes  
- **6C** + feature synonym cleanup  
- **6D** Full A–C above

### Ask 7 — Live PostgreSQL vs seed CSVs
Is the next “high quality DB” target:

- **7A** Keep improving **seed CSV + logical schema** (current)  
- **7B** Stand up a real Postgres (or Prisma Composer) and migrate seeds  
- **7C** Spec the migration only; don’t deploy yet

---

## What I will **not** do until you answer

- Collapse multi prices into one portal scalar  
- Invent bathrooms, GPS, SPVs, or flat IDs  
- Promote Misty/Polaris-class rows to public  
- Treat Hauzisha `0730` as developer contact  
- Rewrite schema enums that Zoopla locks already settled (#1–8)

---

## Suggested order once answers land

1. Enforce Ask 1 in field-promotion + surface-map  
2. Steward: Ask 2 pipeline  
3. Normalize dictionaries per Ask 6  
4. Recompute DQ / coverage over **full** seeded set  
5. Only then expand research waves for public density
