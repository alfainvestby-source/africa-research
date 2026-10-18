# Skill: Feature taxonomy (amenities + unit features)

## Problem
We currently store free-text amenity lists (`amenities.core`). We need a **controlled feature catalog** that covers more than communal amenities — including **apartment features**, **house features**, and other dwelling-type scopes.

## Feature scopes (v1)
| Scope | Examples | Typical use |
|-------|----------|-------------|
| `development` / building | Gym, pool, padel court, co-working, concierge, CCTV | Estate/building facets |
| `apartment` | Balcony, ensuite, fitted kitchen, DSQ, study, smart home, double-height ceiling | Unit-type / listing facets |
| `house` | Private garden, compound, staff quarters, borehole (unit-level), parking bay | House/townhouse facets |
| `community` | Clubhouse, sanctuary access, retail boulevard, school within estate | Master-plan / Tatu-style |
| `tenure_or_spec` (optional later) | Freehold, generator, borehole (building) | Only when sourced as feature-like |

A single catalog `feature(slug, name, scope[], synonyms[])`; link via `property_feature` and optionally `unit_type_feature` when the feature applies only to certain typologies (e.g. 3BR has DSQ).

## Industry patterns (inspiration — user lock 2026-10-16)

Take inspiration from major listing sites / proptech classifieds when shaping the catalog and filter vs detail split. **Do not copy their feature lists blindly** — only normalize what our dossiers actually source.

| Pattern source | What they do | What we borrow |
|----------------|--------------|----------------|
| **Bayut / Property Finder** (MENA) | Split **building amenities** (gym, pool, parking, security) from **in-unit property features** (balcony, fitted kitchen, wardrobes); rich amenity filters + synonym/autocomplete | Our `development` vs `apartment`/`house` scopes; synonym map for filters |
| **Rightmove / Zoopla** (UK) | Fewer amenity chips; strong property-attribute facets (garden, parking, balcony) + free-text “key features” | Keep high-coverage attributes filterable; long-tail amenities = detail / Admin–Plus until coverage proves out |
| **Local Kenya portals** (BuyRentKenya, agency sites) | Generator, borehole, CCTV, DSQ, plinth sizes common; amenity chip inflation common | Kenya-specific slugs (`backup_generator`, `borehole`, `dsq`); agent-only chips → `needs_verification` |
| **Majengo** ([majengo2-intel](../product/majengo2-intel.md)) | Fixed amenity chips (WiFi, Parking, Backup Generator, Borehole, Pool, Gym, 24/7 Security, CCTV, Balcony, Furnished, Elevator) + custom free-text; **rent/PMS**, not off-plan | Seed chip labels as synonyms/slugs into development/apartment scopes; **do not** invent property links; reject custom free-text for public filters |

**Adapted for Kenya off-plan master data:** catalog is development-centric (not classified ad-centric); provenance (developer canonical vs agent NV) beats portal marketing completeness; official-vs-official amenity wording stays claim-set / NDI where relevant; public filters later gated by coverage agent. Majengo informs **vocabulary**, not our product shape.

## Rules
- Extract from dossier/developer text; **no invented features**
- Developer-backed = canonical; agent-only = `needs_verification`
- Normalize synonyms (co-working / coworking; sauna / spa&sauna split when evidence allows)
- Public facets = high coverage + high confidence; richer sets stay Admin/Plus
- **Industry patterns inform structure only** — never invent a feature because Bayut/Rightmove lists it

## Deliverables
1. `docs/db/feature-taxonomy.md` — catalog + synonym map + scope tags + **industry patterns used** + proposed DDL  
2. Schema handoff: `feature`, `property_feature`, `unit_type_feature` for DB steward merge into `docs/db/schema.md`  
3. Seed rows under `docs/db/seed/` from existing dossiers only  

## Handoff
Coordinate with Proptech DB steward for DDL; Coverage agent for which features become public filters.
