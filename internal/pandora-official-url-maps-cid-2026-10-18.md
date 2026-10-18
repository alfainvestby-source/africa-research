---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Pandora Residences — official URL + Maps CID (2026-10-18)

Property: `prop-pandora-residences` (NBO-002)

## Official development URL — set / refreshed

| Store | Field / row | Value | Change |
|-------|-------------|-------|--------|
| `developers.csv` | `dev-a-one-corporation.website` | `https://pandora.co.ke/` | Already present; `sales_office_note` refreshed (user-provided; live 2026-10-18) |
| `contacts.csv` | `ct-pandora-url` | `https://pandora.co.ke/` | Already present; label → Official project site (user-provided 2026-10-18); `is_primary=true` |
| `properties.csv` | — | — | **No website column** in schema; `notes` + `last_verified_at=2026-10-18` record URL |
| Dossier `pandora-residences.md` | Sources #1; Developer.website; Contacts url | `https://pandora.co.ke/` | `accessed_at` → **2026-10-18**; user-provided notes |
| `research_passes.csv` | `rp-pandora-2026-10-18-url` | retained 2 | URL + Maps place |
| `related_parties.csv` | — | — | N/A (none for Pandora) |

## Google Maps CID — resolved (browser)

| Item | Value |
|------|-------|
| CID | `12900601372674958277` |
| Place title | Pandora (apartment building) |
| Address | PGQ+M66, Muthangari Dr, Nairobi, Kenya |
| Website on card | pandora.co.ke |
| Lat / lng | **−1.260829, 36.780513** |
| Resolver | [Resolve Pandora Maps CID](bc-324bfd04-f189-5ac2-9fd4-2b51778ec120) (browser); HTML/curl alone returns US/default centers only |

### Seed writes

| Store | Change |
|-------|--------|
| `geo_pins.csv` | **New** `pin-pandora-maps-place` — `official` / conf **4** / recommended / provider `google_maps_place` |
| `geo_pins.csv` | `pin-pandora-geocode` demoted (`is_recommended=false`) |
| `properties.csv` | `lat/lng` set; `map_tier=exact`; `street_label=Muthangari Drive` |
| Dossier + geo-enrichment | NBO-002 canonical Maps place |

## Changelog

`docs/db/changelog.md` → **0.1.25**
