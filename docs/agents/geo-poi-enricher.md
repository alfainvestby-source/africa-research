# Skill: Geo / POI enricher

## Purpose
Add **GPS** and **proximity** context to developments for map pins, search, and Plus analytics — without inventing locations.

## Allowed sources (prefer in order)
1. **Developer / official** lat-lng or map embed (canonical when present) — conf 5  
2. **NEMA / Gazette / ESIA** coordinates in filings — conf 4–5  
3. **Geocoding** of sourced street + neighbourhood + city (Google Geocoding, Mapbox, or **OSM Nominatim** if no Google key) — conf 2–3; always flag `geo_method=geocode`  
4. **CSV seed lat/lng** — conf 2 until corroborated  

Never invent a pin. If address is too vague → `unknown`.

## Proximity / related data
Using Places / OSM / similar (when available):
- Distance/time to CBD / Westlands / major nodes (document route basis)
- Nearby: malls, hospitals, schools, transit (typed POIs)
- Estate / master-plan boundary cues when mapped (e.g. Tatu City)

Store as `geo_place`, `property.lat/lng`, `poi`, `property_poi(distance_m, source, confidence)` — propose DDL with DB steward.

## Rules
- Google Maps / Places / similar **allowed for enrichment** when keys or public endpoints exist; prefer OSM if no credentials  
- Public map pin: only conf ≥4 **or** geocode with visible “approx” badge (product decision)  
- Plus/Admin: show method + confidence always  
- Respect API ToS; cache results; record `accessed_at` + provider  

## Deliverables
- `docs/db/geo-enrichment.md` — method + per-property results  
- Seed updates for lat/lng + sample POIs for corpus  
- Schema proposals for POI tables  

## Status (2026-10-16)
**Done** for corpus GPS pass — see [geo-enrichment.md](../db/geo-enrichment.md).  
Coverage: **26/27** pinned · **1 unknown** (ELD-001) · schema **v0.1.13** (`geo_pin`, `poi`, `property_poi`) · seeds `geo_pins.csv` + light `pois.csv` / `property_pois.csv`.  
Next: plot chase for ELD-001 / Longines / Ankori street number; Google key if available; route-times.
