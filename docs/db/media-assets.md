# Media assets — listing photo collection

Skill: [photo-collector.md](../agents/photo-collector.md)  
Schema: `media_asset` + `property_media` (v0.1.11) — [schema.md](schema.md) · [changelog.md](changelog.md)  
Store root: `/cursor/stores/self/media/projects/<slug>/` + `manifest.csv`

**No invented images.** First collection pass: **2026-10-16**. Refresh: **2026-10-18** (card-facets harvest / remaining discovery slugs).

## Method (first pass)
1. Enumerate all `docs/projects/*.md`.  
2. Parse retained Sources table URLs (skip PDFs).  
3. Fetch pages → extract `img` / `srcset` / `og:image` → prefer largest CDN/WP variants.  
4. Download, SHA-256 dedup, keep best resolution; cap ~35–40/project.  
5. Hard kill **>60s** per project (rapid-fire). Lesonia official host SSL expired → retry with SSL verify off + agent pages; space-in-URL official imgs still failed.

## Rollup

| Meta | Count |
|------|------:|
| Projects covered | **50** / 51 dossiers (gap: jabali-towers) |
| Total images kept | **1533** |
| Seed CSVs | `seed/media_assets.csv` + `seed/property_media.csv` (v0.1.21) |
| Projects at cap (≥35) | 14 |
| Thin (&lt;15) | gemini-residency-phase-2 (10), kai-diani (14) |
| Gaps noted | Lesonia official CDN **space-in-filename** URLs failed (agent pages filled to 35); Capricorn microsite refused; some SSL/timeout page misses |

### Per project

| slug | images | notes |
|------|-------:|-------|
| 108-residences-diani | 40 | |
| alba-apartments | 40 | |
| ankori | 40 | |
| astra-bay-residence | 40 | |
| berkeley-homes | 40 | official timeout; agents filled |
| brookside-oak | 31 | |
| canto | 32 | |
| capricorn-kilimani | 35 | capricorn.co.ke connection refused |
| diamond-bay-residences | 35 | |
| galaxy-one | 21 | |
| gemini-residency-phase-2 | 10 | thin |
| golden-mansion | 30 | |
| golfscape-residences | 33 | |
| kai-diani | 14 | thin |
| kings-square-eldoret-ph2 | 35 | unicode URL encode issue on one page |
| kings-summit-nakuru | 21 | |
| lesonia-residences | 35 | SSL unverified + agent pages; spaced official URLs failed |
| longines-bay-kilimani | 35 | |
| luna-oak-residency | 35 | |
| misty-springs | 35 | |
| nouveau | 24 | |
| pandora-residences | 35 | |
| plumeria-residency | 18 | |
| polaris-residency | 27 | |
| porini-point | 32 | |
| riara-oasis | 28 | |
| sensei-nyali | 17 | |

## Paths
- Folders: `/cursor/stores/self/media/projects/<slug>/{exterior,interior,amenities,plans,progress,other}/`
- Manifests: `/cursor/stores/self/media/projects/<slug>/manifest.csv`
- Run summary: `/cursor/stores/self/media/projects/_collection-summary.csv`
- Runner: `/cursor/stores/self/internal/photo-collector-run.py`

## Next (not this pass)
- Quote-encode spaced filenames on Lesonia official CDN  
- PDF brochure page rasters (document intelligence)  
- Seed CSV extract of `media_asset` / `property_media` for DB steward  
- JS-gallery hydration for SPA shells  
