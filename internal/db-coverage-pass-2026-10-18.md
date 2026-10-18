---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# DB coverage pass — 70% gate (2026-10-18)

**Denominator:** **51** rows in `properties.csv` (all researched dossiers, including DISC-NBO-007…011).  
**Locks:** [db-quality-locks-2026-10-18.md](db-quality-locks-2026-10-18.md) · [decisions.md](../docs/decisions.md)  
**Scoreboard:** [field-promotion.md](../docs/db/field-promotion.md) · Rollup: [corpus-rollup.md](../docs/db/seed/corpus-rollup.md)

**Rule:** public field needs **≥70% fill** across the corpus **and** developer/official **or** ≥2 independent agents. Invent nothing to chase %.

---

## Steward steps done this pass

| Step | Result |
|------|--------|
| Seed DISC-NBO-007…011 | **Done** — 237 Lulu, Highpoint 336, Jabali Towers, Balkis, Hephé Palace |
| Backfill `inventory_class` | **Done** — **0** blank; **39** `building` / **12** `off_plan` |
| Coverage @ 70% | **This report** |

Media → seed and typology `listing` snapshots remain **next** in steward order (not this pass).

---

## Gate scoreboard (n=51)

| Field | Filled | % | Gate |
|-------|-------:|--:|------|
| `canonical_name` | 51/51 | 100% | **PASS** |
| `status_label` | 51/51 | 100% | **PASS** |
| `inventory_class` | 51/51 | 100% | **PASS** |
| `geo_city` | 51/51 | 100% | **PASS** |
| `geo_neighbourhood` | 51/51 | 100% | **PASS** |
| `primary_developer` (any id) | 48/51 | 94% | **PASS** |
| `primary_developer` conf ≥4 | 42/51 | 82% | **PASS** (weak stay admin) |
| Map location (exact / approx / area) | 51/51 | 100% | **PASS** (always-map lock) |
| `properties.lat/lng` (conf≥4 scalar) | 8/51 | 16% | **FAIL** as public exact pin |
| `geo_pin` row present | 26/51 | 51% | **FAIL** 70% for pin table |
| `unit_types` (≥1) | 50/51 | 98% | **PASS** (Riara Oasis still empty) |
| `unit_type.bathrooms` (≥1 filled) | 2/51 | 4% | **FAIL** — explicit-only hygiene |
| `price_observations` | 50/51 | 98% | **PASS** |
| `payment_plan_claims` | 50/51 | 98% | **PASS** |
| `property_agents` | 44/51 | 86% | **PASS** |
| `property_features` | 46/51 | 90% | **PASS** |
| `construction_progress` | 10/51 | 20% | **FAIL** — stay Admin/Plus candidate |
| `related_parties` | 26/51 | 51% | **FAIL** — capture-when-signaled |

**Authority gate:** developer conf≥4 **or** ≥2 agents → **50/51 (98%)** PASS for “may be public at all.”

---

## Public hero price (locked display)

Derived from retained `price_observations` (not invented):

| Display | Count | Rule |
|---------|------:|------|
| **KES X–Y** | 32 | Multi trustworthy amounts, no official-vs-official fight |
| **From KES X** | 5 | Single agreed floor |
| **POA** | 14 | 13 NDI + 1 no price rows (Riara Oasis) |

Plus/Admin keep the full observation table. Never promote a silent NDI winner.

---

## Map tiers (always show)

| Tier | Count | Public label |
|------|------:|--------------|
| Exact (`properties.lat/lng` conf≥4) | 8 | Marker |
| Approximate (`geo_pin` present, lower conf) | 20 | **Approximate location** |
| Area only (neighbourhood centroid) | 23 | **Area only — confirm on visit** |

Online geo enrichment still needed for the **23** area-only rows before more exact pins clear 70%.

---

## Bathrooms (two grains)

| Grain | Status |
|-------|--------|
| `unit_type.bathrooms` | **2/201** typologies filled (NAK-001 Kings Summit **2**; DISC-NBO-014 48 Treehouse **5**) — never invent |
| Development min–max | Prefer **computed view** from filled unit_types until density warrants columns |

Fails 70% by design until more explicit brochure/floorplan counts are sourced.

---

## Admin-only developer (conf &lt;4 or null)

9 properties — public may show project CTA but **not** a strong “developed by” claim until raised:

| ID | Reason |
|----|--------|
| NBO-016 Polaris | null primary |
| DISC-NBO-020 Only You | null primary |
| DISC-NBO-026 Montbleu | null primary |
| NBO-017 Misty | Tian Yu conf 2 |
| DISC-NBO-010 Balkis | Sunmon conf 2 NV |
| DISC-NBO-024 Rhapta One | Oasis conf 2 |
| NBO-011 Lesonia | trading conf 3 |
| NBO-014 Alba | Nanchang conf 3 |
| DISC-NBO-006 Brookside Oak | Van Tung conf 3 |

---

## Seeded this pass — DISC-NBO-007…011

| ID | Slug | IC | Developer | Notes |
|----|------|----|-----------|-------|
| DISC-NBO-007 | 237-lulu | `off_plan` | Mi Vida (5) | Official 4.4M vs typed 6.93M+ → **POA**; Garden City |
| DISC-NBO-008 | highpoint-336 | `building` | Highpoint Dev Ltd (4) | Microsite 500; from 9.9M indexed; ≠ Golfscape partner |
| DISC-NBO-009 | jabali-towers | `off_plan` | Rendeavour (5) | Tatu Central; Dec 2028 + 10%/36-mo; ≠ Porini |
| DISC-NBO-010 | balkis-residences | `building` | Sunmon (2) NV | Project face balkisriverside.com (5); admin-only developer gate |
| DISC-NBO-011 | hephe-palace | `building` | Sequoia (5) | Sequoia China RP; ≠ Karura Forest Views Block alias |

---

## Public shortlist after this pass

Still **intent-public** when per-listing canonical + authority gate pass:

1. Name (+ light aliases)  
2. Neighbourhood / city  
3. Primary developer when conf ≥4  
4. Status summary  
5. Inventory class (`off_plan` / `building`)  
6. Canonical unit types (+ sizes when developer-backed)  
7. Map (exact / Approximate / Area only)  
8. Hero price **From / X–Y / POA** (never raw NDI pick)  
9. Payment deposit when must-have threshold met  

**Blocked at 70% or confidence:** exact GPS scalar, bathrooms attribute, construction progress %, related-party graph, unit/storey scalars.

---

## Counts snapshot

| Table | Rows |
|-------|-----:|
| `properties.csv` | 51 |
| `developers.csv` | 37 |
| `unit_types.csv` | 201 |
| `price_observations.csv` | 190 |
| `payment_plan_claims.csv` | 116 |
| `geo_pins.csv` | 31 |
| `research_passes.csv` | 50 (Riara Oasis historically thin — no new invent) |

---

## Next (steward order)

1. Media → seed (photo-collector manifests)  
2. Typology `listing` snapshots from retained URLs only  
3. Geo enrichment for **23** area-only map tiers  
4. Bathroom harvest only from explicit sources
