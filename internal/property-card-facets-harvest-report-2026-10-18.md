---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Property card facets harvest — 2026-10-18

**Changelog:** DB **0.1.21** · Script: [property-card-facets-harvest-2026-10-18.py](property-card-facets-harvest-2026-10-18.py)  
**Prior:** [db-coverage-pass-2026-10-18.md](db-coverage-pass-2026-10-18.md) · [rm-columns-property-vs-70pct-2026-10-18.md](rm-columns-property-vs-70pct-2026-10-18.md)

No invented facts. Derived from seed + dossier streets + Nominatim geocode + existing media manifests.

---

## Added on `properties.csv` (n=51)

| Field | Filled | Example |
|-------|-------:|---------|
| `property_type` | 51/51 | Libra → `apartment` |
| `beds_min` / `beds_max` | 50/51 | Auris → `0`–`2` (studio–2BR) |
| `size_sqm_min` / `size_sqm_max` | 43/51 | 237 Lulu → `41`–`102` |
| `hero_price_qualifier` + min/max | 51/51 | Libra → `range` 17M–25M; Lulu → `POA` |
| `deposit_pct` (must-have only) | 26/51 | Serene Manor → `20` |
| `summary` | 51/51 | `237 Lulu in Thika Superhighway / Exit 7, Garden City, Nairobi — off_plan apartment (studio–3BR).` |
| `map_tier` | 51/51 | 8 `exact` / 43 `approximate` |
| `street_label` | 28/51 | `George Padmore Road…` |

Hero mix: **31** range · **6** from · **14** POA.

---

## Harvested

| Deliverable | Result |
|-------------|--------|
| `geo_pins.csv` | **57** rows · **51/51** properties have map location |
| `property_utility_chips.csv` | **152** chips · **41/51** props (generator/borehole/solar/parking/security…) |
| `media_assets.csv` + `property_media.csv` | **1533** images · **50/51** props (gap: **jabali-towers** — collector kept 0) |

---

## Rules applied

- Hero **POA** when `needs_developer_input` or no amounts  
- Deposit only when `meets_must_have`  
- Exact lat/lng on `property` unchanged (conf≥4 only); new pins = `geocode` conf 2–3 + **Approximate**  
- Summaries = canonical compose (name + place + IC + type + beds) — no CSV-lead junk  

---

## Still not 70% public

Bathrooms, tenure, construction %, exact GPS on all cards — unchanged; do not invent.
