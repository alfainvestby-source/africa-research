---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# DB quality locks — final (user 2026-10-18)

Explainer: [db-quality-decisions-explained-2026-10-18.md](db-quality-decisions-explained-2026-10-18.md) · Flags: [db-quality-ask-flags-2026-10-17.md](db-quality-ask-flags-2026-10-17.md)

Evidence: Zoopla price + **qualifier** (incl. **POA**) · Rightmove New Homes ADF **price-min / price-max** on development · Zillow/RM always map a location (exact or area).

---

## 1. Public hero price — **best-practice lock**

Leading portals never invent a single wrong number, and they rarely leave the price slot blank forever.

| Situation | Public card shows | Like |
|-----------|-------------------|------|
| Developer (or agreed multi-source) **one clear floor** | **From KES X** | Zoopla/RM “from” |
| Several real claims, **no official-vs-official fight** | **KES X–Y** (min–max of retained trustworthy claims) | Rightmove ADF development `price-min` / `price-max` |
| Official-vs-official **NDI** (e.g. Lulu 4.4M vs 6.93M on same site) | **POA** (“Price on application”) — **not** 4.4M alone | Zoopla `POA` qualifier |
| Only thin single-agent / Block | **POA** | Same |

**Plus / Admin:** always the full `price_observation` table + `needs_*`.  
**Never:** pick one NDI claim as the silent hero (anti-goal).

---

## 2. Steward order — confirmed

1. Seed dossiers **007–011**  
2. Backfill **`inventory_class`**  
3. Media → seed  
4. Typology **`listing`** snapshots  

---

## 3. Bathrooms — **two fields** (yes)

| Field | Grain | Example |
|-------|-------|---------|
| `unit_type.bathrooms` | **One typology** (the “unit listing” shape) | 2BR+DSQ → **2** |
| `property.bathrooms_min` / `property.bathrooms_max` (or derived view) | **Whole development** range for filters/cards | **1–3** |

Fill only when **explicit** (brochure / floorplan / “2 bathrooms”). Derive development range from filled unit_types. Do not invent from bedroom count alone.

Schema note for steward: add nullable `bathrooms_min` / `bathrooms_max` on `property` **or** document as computed view — prefer **computed view** first (no duplicate invent); materialize columns only if query cost needs it.

---

## 4. Map — **absolute necessity** (revised)

Public **always** has a map location. Online tools are **option 1**; physical visit only if online fails.

| Confidence | Public map | Label |
|------------|------------|-------|
| **≥4** developer / EIA / verified street pin | Exact marker | — |
| **2–3** online geocode from street + landmarks (Google Maps/Places, Nominatim) agrees with dossier street | Marker | **Approximate location** |
| **≤1** neighbourhood-only | Neighbourhood centroid | **Area only — confirm on visit** |

**Tools (option 1 online):** developer/brochure map → NEMA EIA lat/lng → Google Maps/Places (name + street + landmark) → OSM/Nominatim → (later) Geocoding API. Portals = corroboration only, never sole conf≥4.

**Option 2:** physical geolocate when online cannot place the street.

---

## 5–7 — confirmed

| # | Lock |
|---|------|
| 5 | Weak developer (Misty/Polaris…) → **admin-only** until conf ≥4 |
| 6 | Public field = **≥70% fill** + developer **or** ≥2 independent agents; no single-agent AI gap-fill |
| 7 | **CSV seeds now**; Postgres when shipping UI |

---

## Executed 2026-10-18

1. ~~Coverage pass @ 70% gate~~ → [db-coverage-pass-2026-10-18.md](db-coverage-pass-2026-10-18.md)  
2. ~~Seed 007–011~~ + `inventory_class` backfill → corpus **51**  
3. Invent nothing to chase coverage — **held** (bathrooms / exact GPS / progress still FAIL)
