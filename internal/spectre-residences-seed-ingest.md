---
cursor:
  subagentId: "bc-1bdc7ab6-93cc-513e-a234-3ba81ab0f03b"
---

# Spectre Residences seed ingest — complete

**Date:** 2026-10-18  
**Changelog:** **0.1.26**  
**Final corpus property count: 52**

## Seeded

| ID | Slug | inventory_class | Developer |
|----|------|-----------------|-----------|
| DISC-NBO-031 | spectre-residences | `off_plan` | **`dev-aya-real-estate`** (NEW, conf 5) |

## Entities

| Entity | Action |
|--------|--------|
| `dev-aya-real-estate` | NEW — ≠ `dev-whitehorse-real-estate` / `prop-aya-luxury-residence` |
| `rp-karim-exclusives-spectre` | marketing_partner (exclusive sales + concept) |
| `stk-blink-studio` | architect |
| `stk-metrix-integrated-spectre` | structural (`other`) — ≠ Kai `stk-metrix-engineers` |
| `stk-miller-company-advocates` | counsel (`other`) |
| `agent-nairobi-realty` / `agent-karim-exclusives` | NEW agents; reuse `agent-cpk`, `agent-block` |
| `geo-au-close-westlands` | street place |
| `pin-spectre-nominatim-westlands-rd` | conf **2** street centroid; CID pending — no lat/lng on property |

## Seed row counts (this property)

| Table | Rows |
|-------|-----:|
| unit_types | 3 (50 / 65 / 100 sqm; bathrooms blank) |
| price_observations | 8 (spectre.ke + AYA hub + agents; all NDI / NV as flagged) |
| payment_plan_claims | 3 (reservation 100K; deposit 20%; tenor 36 — developer canonical) |
| property_features | 16 (12 user + extended) |
| contacts | 11 (user-locked AYA + Karim + secondary agents) |

## Locks respected

- Never `0730` as developer phone  
- Block.ke low-trust only  
- Official vs official prices → show all + `needs_developer_input`; public **POA**  
- Do not merge Karim with `stk-karim-cg`  
- No invented Maps coords; Nominatim only until CID resolves  

## Docs updated

- `docs/db/seed/corpus-rollup.md` → **52**  
- `docs/db/seed/README.md`  
- `docs/db/changelog.md` **0.1.26**  
- `docs/decisions.md` one-liner  

## Sources

- Handoff: [`spectre-residences-steward-handoff-2026-10-18.md`](spectre-residences-steward-handoff-2026-10-18.md)  
- Dossier: [`../docs/projects/spectre-residences.md`](../docs/projects/spectre-residences.md)  
