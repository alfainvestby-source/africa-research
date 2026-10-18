---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Finding originals instead of stripping watermarks — 2026-10-18

**Rule:** do **not** remove watermarks. Prefer public **developer / project / cleaner listing** copies of the same renders.

Script: [official-gallery-refresh-2026-10-18.py](official-gallery-refresh-2026-10-18.py) · Results CSV: [official-gallery-refresh-results-2026-10-18.csv](official-gallery-refresh-results-2026-10-18.csv)

---

## What we found

| Source | Pattern |
|--------|---------|
| **Hauzisha CDN** (`new-hauzisha-pull.b-cdn.net`) | Center “hauzisha” house watermark — e.g. Rhapta One |
| **Some agents** (e.g. Ladva) | Logo + phone overlay banners — e.g. Auris amenity renders |
| **Developer / CPK / NRE** | Often same marketing renders **without** Hauzisha mark |

Only **5** files in the corpus were Hauzisha-CDN hosted (all Rhapta One). Agent brand overlays are more common and harder to auto-detect without OCR.

---

## What we did

1. Flagged Hauzisha-host rows as `watermark_risk=true` in manifests.  
2. Public-search + dossier **official / cleaner** page refresh for 15 priority projects.  
3. Prefer `official_refresh` / non-risk images as **hero** in `media_assets.csv` / `property_media.csv`.  
4. Kept watermarked files on disk for Admin evidence, demoted in gallery order.

### Wins (new cleaner pulls)

| Project | New clean images | Notes |
|---------|-----------------:|-------|
| rhapta-one | **35** | CPK/Oaklane copies; **5** Hauzisha marked risk |
| berkeley-homes | **35** | Nefroon/CPK (official site SSL timeout) |
| auris-residence | **27** | Jafu/CPK/NRE/GNA |
| 237-lulu | **33** | Mi Vida / Garden City Living |
| citrine-heights | **14** | Jafu/CPK |
| highpoint-336 | **10** | NRE (microsite down) |
| serene-manor | **8** | Jafu/NRE |
| libra-residences | **7** | GLBC |

### Thin / blocked this pass

Pandora, Only You, AYA, Diplomat (502), Gaia, Hephé, Montbleu — official pages returned few new distinct hashes (already had copies, or site errors).

---

## Limits (honest)

- No Google Lens / TinEye API in this environment → **no bulk reverse-image match** of all 1500+ files.  
- We match by **project + official URL harvest**, not pixel-for-pixel reverse search.  
- Agent overlays (Ladva-style) need per-image review or OCR later.  
- Never strip marks from portal files.

---

## Seed after refresh

- `docs/db/seed/media_assets.csv` — **1585** rows (+ `watermark_risk`)  
- Heroes with `watermark_risk=true`: **0**
