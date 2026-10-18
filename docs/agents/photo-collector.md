# Skill: Photo / image collector

## Purpose
Collect **listing photos** for researched developments into **per-project media folders**, from **multiple real sources**, preferring **largest** images — with full provenance. **No invented or AI-generated images.**

## Store layout

```
/cursor/stores/self/media/projects/<project-slug>/
  exterior/   # facade, tower, site, renders of building exterior
  interior/   # unit interiors, show flats
  amenities/  # pool, gym, lobby, gardens
  plans/      # floor plans, site plans (raster)
  progress/   # construction progress photos
  other/      # uncategorizable / mixed
  manifest.csv
```

- `project-slug` = dossier filename without `.md` (e.g. `galaxy-one`, `polaris-residency`).
- Create category subfolders only when used (or create all empty — prefer create-on-write).
- Path root is always under `/cursor/stores/self/media/projects/`.

## Source priority (prefer in order)

| Priority | Type | Confidence (typical) |
|---------:|------|----------------------|
| 1 | Developer / official project site (+ CDN on same origin) | 5 |
| 2 | Official brochure / flyer / EIA figures (raster only; PDF page renders optional later) | 4–5 |
| 3 | Marketing partner / related_party project pages | 3–4 |
| 4 | Named selling agents | 3 |
| 5 | Aggregator portals | 2–3 |

Pull image URLs from **retained sources** listed in each dossier Sources section first. Optionally scan evaluated-but-skipped pages only when retained pages yield &lt;10 usable photos.

## Image selection rules

1. **Prefer largest** — parse `srcset` / `data-srcset` and pick the highest width descriptor; expand common CDN/WordPress size suffixes (`-150x150`, `-300x200`, `-scaled`) to the full-size sibling when reachable.
2. **Skip** favicons, logos-only sprites, tracking pixels, SVG icons, and thumbnails **when a larger variant of the same asset exists**.
3. **Minimum useful size:** prefer ≥800px on the long edge; allow ≥400px only if no larger exists for that project.
4. **Dedup** by **SHA-256 content hash**. On hash collision, keep the file with greater `width×height` (or bytes if dimensions unknown); update manifest to the winner.
5. **Cap** ~**30–40** best images per project after ranking (priority tier → resolution → bytes). Note gaps in `media-assets.md`.
6. **Category** heuristic from URL/path/alt/filename (`exterior|interior|amenities|plans|progress|other`); default `other`. Do not invent captions.

## Provenance — `manifest.csv`

One row per kept file. Columns:

| Column | Meaning |
|--------|---------|
| `filename` | Relative path under project folder (e.g. `exterior/01-abc123.jpg`) |
| `source_url` | Direct image URL downloaded |
| `page_url` | HTML page (or dossier source) where the image was discovered |
| `width` | Pixels (0 if unknown) |
| `height` | Pixels (0 if unknown) |
| `bytes` | File size |
| `content_hash` | SHA-256 hex |
| `category` | exterior / interior / amenities / plans / progress / other |
| `accessed_at` | ISO date of download |
| `confidence` | 0–5 per source priority + official flag |
| `publisher` | Optional short publisher from dossier Sources |
| `notes` | Optional (e.g. srcset pick, thumbnail upgraded) |

## Hard rules

- **No invented facts / images.** Only download URLs found on real pages (or linked from retained dossier sources).
- Respect robots/ToS reasonably; use a normal browser User-Agent; do not hammer hosts (small delay between requests).
- Do **not** invent GPS or do geo work — that is [geo-poi-enricher.md](geo-poi-enricher.md).
- Record failures/gaps (JS-only galleries, Cloudflare, hotlink blocks) in the rollup — do not fabricate fillers.

## Deliverables

- Per-project folders + `manifest.csv`
- Rollup: [media-assets.md](../db/media-assets.md)
- Schema: `media_asset` + `property_media` (see [schema.md](../db/schema.md))
- Roster row: Photo / image collector = Active

## First-pass method (this skill run)

1. Enumerate `docs/projects/*.md` slugs.  
2. Parse Sources tables for http(s) URLs.  
3. Fetch pages → extract images → download largest → dedup → cap 40 → write manifest.  
4. Update rollup counts.
