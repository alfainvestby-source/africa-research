---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Rightmove-style columns → property grain + 70% Kenya reality

**Input:** Zoopla/RM listing column groups (core / price / place / property / content / material_info / agent).  
**Lens:** Our product is **development-first** (lock 2B), not UK unit ads. Grain = **property** (development) vs **unit_type** / **listing** snapshot.  
**Evidence:** coverage pass n=51 ([db-coverage-pass-2026-10-18.md](db-coverage-pass-2026-10-18.md)) + Zoopla→Kenya locks.

Legend for **70% confidence**:
- **YES** — already ≥70% in seed, or reliably extractable today without inventing
- **SOON** — often published; harvest/geo pass can push over 70%
- **NO** — sparse, UK-only, or wrong grain for developments

---

## 1. Property-level (development master) — keep / adapt

| Group | Columns that belong on **property** | 70%? | Kenya note |
|-------|-------------------------------------|------|------------|
| **core** | `title` → `canonical_name`; `status` → `status_label` + `inventory_class`; `category` → residential; `display_address` → neighbourhood + street; `summary` / `description_html` (developer blurb when sourced) | **YES** name/status/IC/geo; summary **SOON** | Drop UK `section`/`member_type` as primary — use `inventory_class` + publisher on listing/contact |
| **price** | Hero display only: **From / X–Y / POA** + `currency`; keep full history in `price_observations[]` | **YES** (98% have observations; display rule locked) | Drop `rent_frequency`, `price_weekly`, auction as v1. `price_changes[]` rare on off-plan → Admin later |
| **place** | `lat`/`lng` (tiered), city, neighbourhood, county/region soft, country=`ke`, `nearest_stations[]` → **POI** (mall/CBD/airport) | **YES** map-any 100%; exact pin **NO** (16%); approx+area always | Drop UK outcode/incode. Exact GPS **SOON** with geo enrichment |
| **property** | Development-level: `property_type` mix summary (apartment/mixed); **beds min–max** (from unit_types); tenure claim when official | beds range **YES**; type mix **YES**; tenure **NO** public yet | **baths** development min–max = derived later; not 70% today (4%). Skip receptions, EPC, chain_free, retirement, shared_ownership, furnished |
| **content** | Development `features[]` (amenity core); `images[]` / brochure `documents[]` when collected | features **YES** (90%); media **SOON** (seed thin) | Floorplans/videos often typology- or brochure-scoped |
| **material_info** | Kenya utilities as **features**: generator, borehole, solar, fibre, security, parking | **YES** as feature chips (already 90% feature rows) | Drop council_tax, UK broadband_speed/mobile_coverage. `deposit` → **payment_plan**, not council tax |
| **agent** | Public: developer / project CTA (`is_developer` brand). Branch phone graph → Plus | Developer conf≥4 **YES** (82%); phones Plus-only | Multi-agent coverage **YES** (86% have property_agents) |

---

## 2. Not property-level — put on **unit_type** or **listing**

| Columns | Grain | Why |
|---------|-------|-----|
| `listing_id`, `published_at`, `updated_at`, `member_type` | **listing** | Ad snapshot from retained URL (2B) |
| Single `price` / `qualifier` for one offer | **listing** + mirrored into `price_observations` | Development hero is From/X–Y/POA aggregated |
| `beds`, `baths`, `size_sqft`→**sqm**, `size_source` | **unit_type** | One typology, not whole scheme |
| `receptions`, `furnished` | **listing** or skip | Rare / rent-skewed |
| `floorplans[]`, typology `images[]` | **unit_type** / `media` | Often plan-per-type |
| `features[]` in-unit (balcony, DSQ, ensuite) | **unit_type_feature** | vs development amenities |
| Agent `branch_*`, `phone`, `ad_package` | **agent** / **listing_agent** | Plus surface |

---

## 3. Drop or demote for Kenya developments v1

| Column | Verdict |
|--------|---------|
| `outcode`, `incode`, `epc_rating`, `council_tax_band` | **Drop** UK compliance |
| `receptions`, `chain_free`, `retirement`, `shared_ownership` | **Drop** / optional tag only |
| `rent_frequency`, `price_weekly`, `furnished` | **Defer** (sale/off-plan first) |
| `is_auction` | **Optional** rare |
| `broadband_speed`, `mobile_coverage`, `water`/`heating`/`electricity`/`sewerage` as UK enums | **Replace** with Kenya chips (generator, borehole, solar, fibre) |
| `letting_arrangements` | **Defer** |

---

## 4. What we can already hit at ≥70% with high confidence

**Ship-ready property public facets (corpus-proven):**

1. Name + aliases  
2. Status summary + `inventory_class`  
3. City + neighbourhood (+ street when known)  
4. Map always (exact / Approximate / Area only)  
5. Primary developer when conf ≥4  
6. Unit-type table: labels + beds (+ sizes when developer-backed) — **not** baths yet as required  
7. Amenity / feature core  
8. Hero price From / X–Y / POA  
9. Payment deposit when must-have threshold met (rows exist 98%; stable public subset smaller)  
10. Developer/project CTA (not full agent phones)

**Do not promise as public 70% yet:** bathrooms, exact lat/lng, tenure, EPC-class energy rating, construction %, floorplan gallery completeness, council-tax-style material blocks.

**Highest-ROI harvest to grow public surface:** (1) geo for 23 area-only → more Approximate/exact, (2) media/floorplan seed, (3) explicit bathroom counts only when brochure/plan says so.

---

## 5. One-line model

> UK listing row ≈ our **`listing`** (typology ad).  
> UK “new homes development” card ≈ our **`property`** + aggregated **unit_types** + hero price rule + feature chips + tiered map.
