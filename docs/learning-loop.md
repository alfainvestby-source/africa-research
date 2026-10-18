# Learning loop log

## Cycle 0 — setup (2026-10-15)
- Process: 1–2 pilot → review → +2 → review + retrofit → half remainder → rest
- Confidence: internal/model only; not public UI initially
- Relational entities: Property, Developer, GroupCompany, Agent, Contact, Stakeholder, Source, Claim
- Seed: `internal/nairobi_off_plan_projects.csv` (leads only)

## Cycle 1 — pilots reviewed (partial lock 2026-10-15)

| Pilot | Dossier | Developer |
|-------|---------|-----------|
| Pandora Residences (NBO-002) | [pandora-residences.md](/cursor/stores/self/docs/projects/pandora-residences.md) — **retrofit applied** (canonical=developer; payment ≥4 recount; no GroupCompany) | A-One / A1 Corporation (5) |
| Astra Bay Residence (NBO-005) | [astra-bay-residence.md](/cursor/stores/self/docs/projects/astra-bay-residence.md) | Wimax Homes Limited (5) |

### Locked method changes
1. **Related brand / unclear group** (e.g. Laureland↔Wimax): type as **`marketing_partner`** until proven parent/alias/co-developer. Do not set as GroupCompany or sole developer.
2. **Official vs agent / official vs official conflicts:** always **highlight the conflict**. If developer identity is confident **and** we have developer data sources for that field, **canonical/true value = developer**. Agents remain secondary claims.
3. **Payment plan:** must-have when **≥4 independent agent/portal sources** agree (or any developer source). Below that → nice-to-have / unknown.
4. **Must-have list:** living document — **extend as new evidence appears**; each list item shows **consensus** (how many pilots/sources support it as must-have). See schema.
5. **Sources:** evaluate ~**10** candidates; **retain ≥5** richest (most fields / least effort). Always prioritize **developer/official site** (and official PDF). Skip thin/low-info pages early. Show counts on [master index](/cursor/stores/self/docs/nairobi-master-index.md); full lists in each dossier Sources section.

### Locked (continued)
6. **Low-confidence / agent-only claims (incl. typologies, sold-out):** **show** them, but mark **`needs_verification`** when confidence is low — e.g. sold-out not corroborated, typology not on developer site, or not listed on other independent sources. Do not hide; do not treat as canonical.

### Method candidates still provisional
- Prefer developer PDF floor plans over agent size tables
- CSV sales_contact often = agent → split Contact.owner
- Price as `price_claims[]` with availability context
- Tag size measure: gross vs plinth

## Cycle 2 — Galaxy One (NBO-013) (2026-10-15)

| Project | Dossier | Developer |
|---------|---------|-----------|
| Galaxy One (NBO-013) | [galaxy-one.md](/cursor/stores/self/docs/projects/galaxy-one.md) | Lionston Real Estate Limited (5); CSV “Lionstone” = typo/lead |

### What worked
- Developer stack dense: project microsite + corporate + product + **live construction tracker** (named contractor **CRJE**).
- Payment lock clear: **any developer source** → canonical **10% deposit**; ≥4 agents still claim **20%** (kept secondary + conflict).
- GPS present on developer JSON-LD (−1.2635, 36.8029) — rare win vs CSV blank.
- Entity split: CSV NRE contact ≠ Lionston sales phones.

### New stress on locks
- **Official vs official** is the dominant pattern here (not only agent vs official): **210 vs 266** units; **30 vs 19** storeys; **price bands disagree** across galaxyone.co FAQ vs lionston.co product; construction **63%/floor 12** vs tracker **42%/A9·B7**.
- Rule still holds: highlight all; **do not invent a winner** when developer sources conflict; only set canonical when developer sources **agree**.
- Search-indexed SPA copy (“30-storey”) may not appear in static HTML fetch — mark **`needs_verification`** when hydration differs.

### Field harvest → proposed must-have extensions
See dossier §9 and schema living table. Bumped against Porini Cycle 2 twin where overlapping:

| Proposed extension | Consensus | Note |
|--------------------|-----------|------|
| `total_units` / `unit_count` claim set | **2/2 C2** (Galaxy + Porini) | Never collapse conflicting official counts (Galaxy 210 vs 266) |
| `storeys` claim set | **1/2 C2** (Galaxy) | Official 30 vs 19 |
| `construction_progress` when developer tracker exists | **1/2 C2** (Galaxy) | Include conflicting official snapshots |
| Named `contractor` Stakeholder | **1/2 C2** (Galaxy: CRJE) | Capture when named on developer site |
| Cash vs instalment dual `price_claims` | **2/2 C2** | galaxyone FAQ + Porini packs |
| Developer-sourced `lat_lng` | **1/2 C2** (Galaxy JSON-LD) | Promote when on official schema/geo |

### Still open
- Prospectus PDF not fetched (CTA present) → gross/plinth still unknown.
- Knight Frank live page = JS shell; indexed copy useful but not retained as primary source.
- Wrong-domain trap: `galaxy.one` ≠ `galaxyone.co`.

## Cycle 2 — Porini Point (NBO-004) (2026-10-15)

| Project | Dossier | Developer |
|---------|---------|-----------|
| Porini Point (NBO-004) | [porini-point.md](/cursor/stores/self/docs/projects/porini-point.md) | Rendeavour (5); Tatu City Limited → RelatedParty (pack names both “Developers”) |

### What worked / reinforced
1. **Developer-first** held: porinipoint.com + brochures + Tatu City launch news supplied scale (570 / 24 / 58,000 sqm), amenities, completion Q1 2027–Sep 2029, and **24-month** payment — payment must-have met via **developer source** (not only agent ≥4).
2. **Official vs official conflicts** appeared again (price_from 7.61M site vs 7.5M press vs older packs 5.9M; **24-mo vs property-pack “up to 3 years”**) — highlight rule essential; do not silently average.
3. **404 official FAQ** still yields search-index snippets (10% deposit, reservation USD 1,550, Jan 2026 start) — record as **`needs_verification`**, do **not** retain 404 URL as a live source.
4. **CSV sales_contact = agent** (Block) again ≠ official PoriniSales@tatucity.com / +254 709 441 144.
5. Agent price bands (Vorsa 5.99M, Craiova 6.4M, Ladva 6.71M) diverge from live site — keep in `price_claims[]` with **`needs_verification`** for “current from”.

### Field-harvest proposals (consensus to bump after review)
- `unit_count` + `block_count` (+ optional `built_up_area_sqm`) when on developer launch materials  
- Dual **cash vs instalment** columns inside `price_claims[]`  
- Geography extension: `master_planned_community` (Tatu City / SEZ)  
- Named press architects → Stakeholder (Makrem Ben Khemis)  
- Deposit/reservation fields remain nice-to-have until live FAQ/LOO  

## Cycle 2 — review locks (2026-10-16)
7. **Co-named developers** (Rendeavour + Tatu City Limited): model as **both** `co_developer` and RelatedParty; propose update later if patterns simplify.
8. **Official vs official:** never assume a winner → flag **`needs_developer_input`**; resolve in later verification passes when confidence rises.
9. **Prices:** always multiple options; portal fields later = high confidence **and** high coverage across listings (~½ missing → not public).
10. **construction_progress:** capture when developer publishes; coverage-gated for portal (coordinator call).
11. Goal/approach plain language: `/cursor/stores/self/docs/goal-and-approach.md`

## Cycle 2 — pair status
| Project | external_id | Status |
|---------|-------------|--------|
| Porini Point | NBO-004 | retrofit for C2 locks |
| Galaxy One | NBO-013 | retrofit for C2 locks |

Next: retrofit all four → confirm goal alignment with user → ~half of remaining CSV.

## Half-batch — Riara Oasis (NBO-003) (2026-10-16)

| Project | Dossier | Developer |
|---------|---------|-----------|
| Riara Oasis (NBO-003) | [riara-oasis.md](/cursor/stores/self/docs/projects/riara-oasis.md) | Riara Oasis Limited (5 via NEMA); AIMASI + Oasis Group → RelatedParty `marketing_partner` |

### What worked
- **Official filing without microsite:** NEMA EIA supplied canonical scale (548; 328/132/88; 321 parking; 23-storey; freehold 0.3339 ha; Thompson / Riara Road).
- Payment must-have met via **≥4 agents** on **20%** (no developer LOO) — conf capped at 3.
- CSV Block contact correctly split from SPV; blank CSV developer filled only from filing.

### Field harvest (see dossier §9 + schema living table)
- Propose `parking_bays` when official; bump `total_units` / `storeys` / marketing_partner / neighbourhood-label claim set.
- Studios + three-tower marketing vs NEMA program → show + **`needs_verification`** (not silent drop).

## Product readiness — first review pass (2026-10-16)

| Deliverable | Path |
|-------------|------|
| Readiness scorecard | [product/readiness-scorecard.md](/cursor/stores/self/docs/product/readiness-scorecard.md) |
| Gap backlog | [product/gap-backlog.md](/cursor/stores/self/docs/product/gap-backlog.md) |
| Plus readiness | [product/plus-readiness.md](/cursor/stores/self/docs/product/plus-readiness.md) |
| Verification queue | [db/verification-queue.md](/cursor/stores/self/docs/db/verification-queue.md) |

### Verdict
- **Admin:** operable on researched corpus.
- **Plus:** closer than public for strong-developer rows (Lulu, Jabali, Galaxy, Porini, Diamond Bay).
- **Public MVP:** not shippable yet — hero-price NDI policy, weak-developer rows, wave-1 missing media/geo/seed.

### Parallel
- Block wave-2 research in flight: **Balkis Residences** (DISC-NBO-010), **Hephé Palace** (DISC-NBO-011).
