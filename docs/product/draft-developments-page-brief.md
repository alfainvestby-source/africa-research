# Brief: draft developments page (high-confidence data only)

**Audience:** another agent building a draft public developments UI  
**Corpus:** `/cursor/stores/self` · **51** properties in `docs/db/seed/properties.csv`  
**Locks:** development-first (2B); no invented facts; Ready not on public; agent phones Plus-only

---

## High-confidence fields to show on the public card / detail

Use these from seeds. Prefer `properties.csv` card facets; join others by `property_id` / `id`.

| UI element | Source | Rule |
|------------|--------|------|
| Name | `properties.canonical_name` | Always |
| Status chip | `inventory_class` (`off_plan` / `building`) + short `status_label` | Always |
| Neighbourhood / city | `geo_places` via `geo_city_id` / `geo_neighbourhood_id` | Always |
| Map | `lat`/`lng` + `map_tier` | Always show map; badge **Exact** / **Approximate** / **Area only** from `map_tier` |
| Street | `street_label` | When present |
| Developer | `developers` via `primary_developer_id` | Public only if developer is strong (conf≥4 in dossiers / skip weak Misty–Polaris class) |
| Hero price | `hero_price_qualifier` + min/max + `hero_price_currency` | `from` → “From X”; `range` → “X–Y”; `poa` → “POA” — never invent a single number |
| Beds | `beds_min`–`beds_max` | Always when set |
| Size | `size_sqm_min`–`size_sqm_max` | When set |
| Property type | `property_type` | e.g. apartment |
| Deposit | `deposit_pct` | Only if `deposit_meets_must_have` is true |
| Completion | `completion_display` + `completion_status` | Show clean **agreed** / **window**; for **conflict** use the display string as-is (already soft) or hide if too noisy |
| Summary | `summary` | 1–2 lines |
| Utility chips | `property_utility_chips.csv` | generator / borehole / solar / fibre / security / parking |
| Amenities | `property_features` + `features` | Developer-core amenities |
| Unit types table | `unit_types.csv` | beds, size_sqm, label — bathrooms only if filled (usually blank) |
| Gallery | `property_media` + `media_assets` → files under `media/projects/<slug>/` | Prefer non–watermark-risk / official; skip empty jabali if still empty |
| Official site | `contacts` / developer `website` when present | e.g. Pandora `https://pandora.co.ke/` |

## Do **not** put on public draft (Admin/Plus later)

- Full multi-source price claim tables  
- All agent phones / WhatsApp (public = developer CTA only)  
- Confidence scores  
- Ready / resale inventory  
- UK fields (EPC, postcode, council tax, receptions)  
- Invented bathrooms, exact GPS when `map_tier` is area-only without coords  

---

## Copy-paste prompt for the other agent

```
Build a draft Kenya off-plan DEVELOPMENTS page (list + detail) using ONLY high-confidence data from this Agent Store.

Store root: /cursor/stores/self
Primary table: docs/db/seed/properties.csv (51 rows)
Joins: developers.csv, geo_places.csv, unit_types.csv, property_features.csv + features.csv, property_utility_chips.csv, property_media.csv + media_assets.csv, media/projects/<slug>/

Product rules:
- Development-first cards (not unit classifieds).
- No invented facts. If a field is empty, omit it — do not guess.
- Public price: use hero_price_qualifier — from → "From X"; range → "X–Y"; poa → "POA". Currency from hero_price_currency / currency_default.
- Always show a map when lat/lng exist; label Exact / Approximate / Area only from map_tier.
- Show developer name only when primary_developer_id resolves to a real developer; skip weak/unknown.
- Deposit % only when deposit_meets_must_have is true.
- Amenities + Kenya utility chips (generator, borehole, solar, fibre, security, parking).
- Gallery from media/projects/<slug>/ via property_media; do not strip watermarks; prefer assets without watermark_risk.
- No agent phone numbers on public UI.
- inventory_class off_plan | building only (this corpus).

Ship: responsive list of developments + a detail page for one property (e.g. prop-pandora-residences or prop-libra-residences) including unit type table and gallery. Real copy from summary/name fields — no lorem.
```
