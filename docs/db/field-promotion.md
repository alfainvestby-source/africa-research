# Field promotion scoreboard

**Skill:** Corpus coverage & field promotion ([spec](../agents/coverage-field-promotion.md))  
**Date:** 2026-10-18 (refresh) · prior pass 2026-10-16 (n=11)  
**Rule (locked):** **`public`** only if **≥70% corpus fill** **and** developer/official **or** ≥2 independent agents. No invented facts. Weak developer (conf&lt;4) → admin-only for “developed by.”

Related: [schema.md](schema.md) · [must_have_fields.csv](seed/must_have_fields.csv) · [decisions.md](../decisions.md) · [coverage pass](../../internal/db-coverage-pass-2026-10-18.md) · [locks](../../internal/db-quality-locks-2026-10-18.md)

---

## Corpus under review

| Bucket | n | Notes |
|--------|--:|-------|
| **Full seeded corpus** | **51** | All `properties.csv` rows — NBO-001…017 + national/DISC including **007…011** |
| `inventory_class` | 39 `building` / 12 `off_plan` | **0** blank after backfill |
| Prior method-complete slice | 11 | Historical scoreboard below kept for pattern memory |

**Denominator for coverage % = 51.** Gate band: **PASS ≥70%** (36/51).

---

## Coverage bands (this pass)

| Band | Definition |
|------|------------|
| **PASS** | ≥ **36/51** (≥70%) |
| **FAIL** | &lt; 70% — not public (unless N/A per-listing) |

“Present” = substantive seed value. Empty / unknown / null = **not** present. Do not invent to chase %.

---

## Scoreboard (n=51)

| Field key | Coverage | Gate | Recommended tier | Notes |
|-----------|----------|------|------------------|-------|
| `canonical_name` (+ aliases) | **51/51** | **PASS** | **`public`** | |
| `status` (summary) | **51/51** | **PASS** | **`public`** summary; conflict set → **`admin`** | |
| `inventory_class` | **51/51** | **PASS** | **`public`** (`off_plan` / `building`) | Ready not in research corpus |
| `geography.city` / neighbourhood | **51/51** | **PASS** | **`public`** | |
| Map location (exact / approx / area) | **51/51** | **PASS** | **`public`** always — label by conf | Lock: map absolute necessity |
| `properties.lat/lng` (≥4 scalar) | **8/51** | **FAIL** | Exact pin only when conf≥4 | 23 still area-only |
| `geo_pin` row | **26/51** | **FAIL** | Enrichment backlog | |
| `primary_developer` | **48/51** | **PASS** | **`public`** when conf≥4; else **`admin`** | 9 weak/null admin-only |
| `primary_developer` conf≥4 | **42/51** | **PASS** | Authority for public “by …” | |
| `related_party` | **26/51** | **FAIL** | **`admin`/`plus`** | |
| `unit_types` | **50/51** | **PASS** | **`public`** canonical; NDI → admin | Riara Oasis empty |
| `unit_type.bathrooms` | **2/51** props / **2/201** UTs | **FAIL** | Card attribute when sourced; never invent | Two-grain: + derived min–max |
| `size_by_type` | high among UTs | **PASS** pattern | **`public`** when developer-backed | |
| `amenities` / `property_features` | **46/51** | **PASS** | **`public`** developer core | |
| `price_observations[]` | **50/51** | **PASS** | Full table **`admin`/`plus`** | |
| Public hero **From / X–Y / POA** | display rule | **PASS** intent | **`public`** display only | 32 range · 5 From · 14 POA |
| `payment_plan` | **50/51** | **PASS** | **`public`** when threshold + stable | |
| `property_agents` | **44/51** | **PASS** | Graph **`plus`**; public CTA only | |
| `construction_progress` | **10/51** | **FAIL** | **`admin`/`plus`** candidate | |
| Developer≥4 or ≥2 agents | **50/51** | **PASS** | Listing may surface publicly | |

---

## Public shortlist (locked intent)

1. `canonical_name` (+ light aliases)  
2. `geography.neighbourhood` + city (+ `street_label` when sourced)  
3. Map — exact / **Approximate** / **Area only** by `map_tier` (**51/51** mapped after 0.1.21)  
4. `primary_developer` when conf ≥4  
5. `inventory_class` + `property_type`  
6. `status` single summary + card `summary`  
7. `beds_min`–`beds_max` (+ size range when present)  
8. Amenities / Kenya utility chips  
9. Hero price **From X** / **X–Y** / **POA** (`hero_price_*` columns)  
10. Payment deposit when `deposit_meets_must_have`  

Harvest detail: [property-card-facets-harvest-report-2026-10-18.md](../../internal/property-card-facets-harvest-report-2026-10-18.md) 

### Explicit non-public (gate or confidence)

| Field | Why blocked |
|-------|-------------|
| Exact GPS on all cards | Only 8/51 conf≥4 scalars; use area/approx labels |
| `unit_type.bathrooms` as required card facet | 2/201 filled — explicit harvest only |
| Development bathrooms min–max column | Prefer derived view until density rises |
| `construction_progress` % | 20% coverage + conflicts |
| Related-party / stakeholder graphs | Sparse |
| Full agent phones | Plus only |
| Raw `price_from` scalar from NDI | Use **POA** |

---

## Hero price snapshot

| Display | n |
|---------|--:|
| KES X–Y | 32 |
| From KES X | 5 |
| POA | 14 |

---

## Changelog hook

Recorded as DB model **0.1.20** in [changelog.md](changelog.md).
