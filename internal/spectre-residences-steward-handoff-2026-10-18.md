---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Steward handoff — Spectre Residences (DISC-NBO-031)

**Date:** 2026-10-18  
**Dossier:** [`docs/projects/spectre-residences.md`](../docs/projects/spectre-residences.md)  
**Master index:** row added under Discovery / national research

## Seed status — **applied 2026-10-18** (corpus **52**; changelog **0.1.26**)

Ingest report: [`spectre-residences-seed-ingest.md`](spectre-residences-seed-ingest.md)

### Originally queued (dossier + handoff)

| ID | Slug | Path | notes |
|----|------|------|-------|
| DISC-NBO-031 | spectre-residences | `docs/projects/spectre-residences.md` | `inventory_class=off_plan` |

### New / reuse entities

| Entity | Action |
|--------|--------|
| `dev-aya-real-estate` | **NEW** — AYA Real Estate Ltd / AYA Real Estate; website ayarealestateltd.com; **≠** `dev-whitehorse-real-estate` / DISC-NBO-023 |
| RelatedParty Karim Real Estate Elevated / Karim Exclusives | **`marketing_partner`** (exclusive sales + concept); contacts +254 140 000 700 / sales@karimexclusives.com |
| Stakeholder Blink Studio Limited | architect |
| Stakeholder Metrix Integrated Consultancy LLP | structural_engineer |
| Stakeholder Miller & Company Advocates | project advocate / counsel |
| `stk-karim-cg` | Do **not** auto-merge — different role evidence |

### Contacts (developer / project)

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 140 000 444 | developer / property |
| phone | +254 752 000 444 | developer (AYA corporate; on ayarealestateltd.com) |
| email | info@ayarealestateltd.com | developer |
| url | https://spectre.ke/ | property |
| url | https://www.ayarealestateltd.com/ | developer |

### Prices (multi-claim — NDI)

| Source | 1BR 50 | 1BR 65 | 2BR 100 |
|--------|-------:|-------:|--------:|
| spectre.ke (matches user) | 9.7M | 12.4M | 18.4M |
| AYA developments hub | 8.8M | 11.2M | 16.7M |
| Agents (CPK / Nairobi Realty) | from 8.8M | — | from 16.7M |

Payment (developer canonical): reservation **100K** + **20%** on signing + **36 months**.

### Features (taxonomy — official)

Map user/site amenities → `lounge`, `kids_play`, `conference_room`, `yoga`, `parking` (valet), `restaurant_cafe`, `spa`, `sauna`, `gym`, `swimming_pool`, `concierge`, `cinema` (+ extended sky terrace / coworking / indoor_gaming on steward pass).

### Geo

Maps CID `8594377129674105266` — browser resolve in flight (curl fails like Pandora). Nominatim Westlands Road fallback conf 2 only if CID fails. **No invent.**

### Locks

- Never `0730` as developer phone  
- Block.ke low-trust only  
- Prefer spectre.ke official media  
- Skip Ready (not tagged)
