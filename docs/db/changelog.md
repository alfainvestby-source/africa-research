# DB model changelog

## 0.1.26 — 2026-10-18 — Spectre Residences seed (DISC-NBO-031)

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-031 | Spectre Residences | `inventory_class=off_plan`; Westlands Rd / AU Close |

### Developer / parties
- **NEW** `dev-aya-real-estate` (trading conf **5**) — **≠** `dev-whitehorse-real-estate` / `prop-aya-luxury-residence` (DISC-NBO-023)
- RelatedParty `rp-karim-exclusives-spectre` = **marketing_partner** (exclusive sales + concept) — do **not** merge `stk-karim-cg`
- Stakeholders: Blink Studio (architect); Metrix Integrated (structural / `other`); Miller & Company Advocates (`other`)

### Prices / payment / contacts
- Multi `price_observations` — spectre.ke **9.7/12.4/18.4M** vs AYA hub **8.8/11.2/16.7M** → **`needs_developer_input`**; public hero **POA**
- Payment developer-canonical: reservation **100K** + **20%** + **36 mo** (must-have **met**)
- User-locked developer phones/email/URLs; Karim exclusive contacts; **never** `0730`

### Geo
- Nominatim Westlands Road pin conf **2** only (`pin-spectre-nominatim-westlands-rd`); Maps CID pending — **no** `properties.lat/lng` promote

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **52** properties (39 `building` / 13 `off_plan`)

### Docs
- Dossier [`projects/spectre-residences.md`](../projects/spectre-residences.md) · handoff [`../../internal/spectre-residences-steward-handoff-2026-10-18.md`](../../internal/spectre-residences-steward-handoff-2026-10-18.md) · ingest [`../../internal/spectre-residences-seed-ingest.md`](../../internal/spectre-residences-seed-ingest.md)

---

## 0.1.25 — 2026-10-18 — Pandora Residences official URL + Maps CID place

### Official URL (user-provided)
- **https://pandora.co.ke/** confirmed live 2026-10-18
- `developers.csv` `dev-a-one-corporation.website` — already set; note refreshed (user-provided + live check)
- `contacts.csv` `ct-pandora-url` — same URL; label + `is_primary=true`
- Dossier source #1 `accessed_at` → **2026-10-18**; developer website / contacts tables updated
- `properties.csv` — **no website column** (schema); `notes` + `last_verified_at` record official URL; related_parties N/A for Pandora
- `research_passes.csv` — `rp-pandora-2026-10-18-url`

### Maps CID (resolved via browser)
- CID `12900601372674958277` → place **Pandora**, PGQ+M66 Muthangari Dr, Nairobi; website pandora.co.ke
- **−1.260829, 36.780513** — new `pin-pandora-maps-place` (`geo_method=official`, provider `google_maps_place`, conf **4**, recommended)
- Promoted to `properties.lat/lng`; `map_tier=exact`; `street_label=Muthangari Drive`
- Nominatim `pin-pandora-geocode` demoted (secondary, conf 2)
- Note: plain HTML/curl of the CID URL alone returns US/default centers — browser place card required

### Docs
- [`projects/pandora-residences.md`](../projects/pandora-residences.md) · [geo-enrichment.md](geo-enrichment.md)  
- [`../../internal/pandora-official-url-maps-cid-2026-10-18.md`](../../internal/pandora-official-url-maps-cid-2026-10-18.md)

---

## 0.1.24 — 2026-10-18 — Apply Hauzisha `property_id` (high + multi-signal only)

### Filter
`same_property` ∧ `confidence=high` ∧ property↔hauzisha_lead ∧ ≥2 signals including developer|place|id (not name-only)

### Applied
- **17** rows in `listings_hauzisha_inventory_leads.csv` got `property_id` (16 properties; 237 Lulu ×2 lead titles)
- Notes tagged `property_id linked 2026-10-18 (dup-pass high+multi-signal)`

### Skipped
- 4 medium (Alba, Gemini 2, Gaia, Alina Valley)
- All needs_human / related_phase / false_positive / phases

### Docs
- [`duplicate-candidates.md`](duplicate-candidates.md) apply log  
- [`../../internal/property-id-link-apply-2026-10-18.csv`](../../internal/property-id-link-apply-2026-10-18.csv)

---

## 0.1.23 — 2026-10-18 — Property duplicate / relist detection

### Deliverable
- [`duplicate-candidates.md`](duplicate-candidates.md) — ranked pairs/clusters + actions  
- [`seed/duplicate_candidates.csv`](seed/duplicate_candidates.csv) — **127** pairs  
- Detector: [`../../internal/duplicate-relist-detect-2026-10-18.py`](../../internal/duplicate-relist-detect-2026-10-18.py)

### Counts
- `same_property` **38** (incl. 17 CSV identity + ~20 Hauzisha title matches)  
- `related_phase` **11** · `needs_human` **65** · `false_positive` **13** · clusters **37**

### Rules
- **No auto-merge**; propose `property_id` on Hauzisha leads only after confirm  
- Entity-resolution **v0.2.0** property↔lead section updated  

---

## 0.1.22 — 2026-10-18 — Completion/delivery card fields

### Soft columns on `property`
- `completion_display` — public card (agreed/window) or conflict confirm label  
- `completion_status` — `agreed` \| `window` \| `conflict` \| `unknown`  
- `completion_raw` — full dossier claim (Admin/Plus)  
- `completion_needs_developer_input` — true on unresolved official fights  

### Seed
- Backfilled all **51** from dossiers (no invented dates)  
- Companion: [`seed/completion_estimates.csv`](seed/completion_estimates.csv)  
- Public-eligible agreed/window ≈ **16/51**; rest conflict/unknown stay Admin until resolved  

### Watermarks (related)
- **Not stripped.** Hauzisha CDN flagged; cleaner official/listing copies preferred where found — see [watermark-originals-refresh-2026-10-18.md](../../internal/watermark-originals-refresh-2026-10-18.md)

---

## 0.1.21 — 2026-10-18 — Property card facets + geo/media/utility harvest

### Soft columns on `property` (portal card)
| Field | Source | Notes |
|-------|--------|-------|
| `property_type` | unit labels / dossier | apartment / mixed / … |
| `beds_min` / `beds_max` | derived `unit_type.bedrooms` | 50/51 |
| `size_sqm_min` / `size_sqm_max` | derived `unit_type.size_sqm` | 43/51 |
| `hero_price_qualifier` + min/max/currency | `price_observations` | **from** / **range** / **POA** lock |
| `deposit_pct` + `deposit_meets_must_have` | `payment_plan_claims` | only when must-have met (26/51) |
| `summary` | dossier blurb or canonical compose | no CSV-lead junk |
| `map_tier` | lat/lng + `geo_pin` | exact / approximate / area |
| `street_label` | dossier `geography.street` | when sourced |

### Harvest
- Nominatim geocode → **51/51** map location (8 exact / 43 approximate); never invent exact
- `property_utility_chips.csv` — generator / borehole / solar / fibre / parking / security from features
- `media_assets.csv` + `property_media.csv` — **1533** images / **50/51** props (jabali-towers gap)

### Script
- [`../../internal/property-card-facets-harvest-2026-10-18.py`](../../internal/property-card-facets-harvest-2026-10-18.py)

### Report
- [`../../internal/property-card-facets-harvest-report-2026-10-18.md`](../../internal/property-card-facets-harvest-report-2026-10-18.md)

---

## 0.1.20 — 2026-10-18 — Seed 007–011 + inventory_class backfill + 70% coverage

### Seeded (Block 2028 Tier A)
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-007 | 237 Lulu | Mi Vida (**5**); Garden City; `off_plan`; **4.4M vs 6.93M+ NDI** → public **POA** |
| DISC-NBO-008 | Highpoint 336 | Highpoint Dev Ltd (**4**); `building`; microsite 500; ≠ Golfscape partner |
| DISC-NBO-009 | Jabali Towers | Rendeavour (**5**); Tatu Central; `off_plan`; Dec 2028 + 10%/36-mo; ≠ Porini |
| DISC-NBO-010 | Balkis Residences | Sunmon (**2** NV) admin-only gate; project face conf 5; `building` |
| DISC-NBO-011 | Hephé Palace | Sequoia (**5**); Sequoia China RP; `building`; ≠ Karura Forest Views alias |

### Hygiene
- Backfilled **`inventory_class`** on all blanks → **0** blank (**39** `building` / **12** `off_plan`)
- Corpus **51** properties

### Coverage @ 70% gate
- Report: [`../../internal/db-coverage-pass-2026-10-18.md`](../../internal/db-coverage-pass-2026-10-18.md)
- Scoreboard: [`field-promotion.md`](field-promotion.md)
- **PASS:** name, status, IC, city/neighbourhood, map-any, primary dev (≥4 on 82%), unit types, prices, payments, features, agents
- **FAIL (do not invent):** bathrooms (2/201), exact GPS scalar (8/51), geo_pin density (26/51), construction progress (10/51), related parties (26/51)
- Hero display: **32** X–Y · **5** From · **14** POA

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **51** properties

### Decisions
- One-liner: coverage pass affirms 70% gate + POA/From/band + always-map; steward next = media → typology listings

---

## 0.1.19 — 2026-10-17 — Zoopla→Kenya locks #2–8 + bathrooms hygiene

### Product locks (see decisions.md + zoopla-kenya-product-decisions.md)
- **2B** development-first + typology `listing` snapshots · **3** Kenya energy vocab · **4** buyer-costs guide · **5** bathrooms card attribute · **6** `tenure` claim · **7** Plus-only agent phones · **8B** Ready on Plus+Admin
- Evidence: [zillow-rightmove-model-study.md](../product/zillow-rightmove-model-study.md)

### Schema guidance (no new columns)
- `unit_type.bathrooms` — first-class; fill only when explicit count sourced
- Claim key `tenure` = freehold \| leasehold \| sectional_title \| unknown — Admin/Plus; public conf≥4 official

### Seed hygiene — bathrooms pass
- Scanned dossiers/seeds for explicit bath counts; **2/180** filled; **178** left blank (never invent from “all ensuite”)
- `ut-kings-summit-3br` → **2** (developer project page, conf **5**)
- `ut-48th-4br` → **5** (agent/portal, conf **3**, `needs_verification=true`)
- Restored `unit_types.csv` to **180** rows after truncated write (price FKs + utf refs resolve; `prop-riara-oasis` still has no typologies — never seeded)

---

## 0.1.18 — 2026-10-17 — Hauzisha Slice C seed (DISC-NBO-024…030)

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-024 | Rhapta One | Oasis trading (**2**); `building`; payment **not** met |
| DISC-NBO-025 | Alina Valley | Wonder **reuse**; `building`; **20%** agent must-have; ≠ Harbour |
| DISC-NBO-026 | Montbleu | **`primary` null** NDI Muthithi Square vs M-Group; `off_plan` |
| DISC-NBO-027 | Marina Bay Phase 2 | M-Group trading; `building`; **10/10/75/5** must-have; ≠ Phase 1 Ready |
| DISC-NBO-028 | Atreus Brookside | Atreus Ventures EIA (**5**); Sunmon/Lesto RP only; EIA GPS; `off_plan` |
| DISC-NBO-029 | Grand Premier | Whitehorse **reuse**; Coming soon→`off_plan`; **Ready lean NDI** |
| DISC-NBO-030 | Rosewood Park | Whitehorse **reuse**; Coming soon→`off_plan`; **Ready lean NDI** |

### Developers
- New: `dev-oasis-development-company`, `dev-m-group-developer`, `dev-atreus-ventures-ltd`
- Reuse: Wonder (Alina), Whitehorse (GP + Rosewood)
- **Never** Hauzisha `0730 731 355`

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **46** properties

### Decisions
- One-liner: Slice C locks Montbleu null primary + Atreus EIA primary; GP/Rosewood Ready lean flagged

---

## 0.1.17 — 2026-10-17 — Hauzisha Wave B seed (DISC-NBO-019…023)

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-019 | Libra Residences | GLBC trading (**5**); `inventory_class=building`; George Padmore; band **17–25M**; payment **not** met |
| DISC-NBO-020 | Only You / Onlyou | **`primary_developer` null**; Onlyou Investments Ltd RelatedParty; GLBC **marketing_partner only**; EIA GPS; **20%** agent must-have; `building` |
| DISC-NBO-021 | Gaia Brookside | Wonder trading (**5**); `building`; completion **NDI**; payment **not** met |
| DISC-NBO-022 | Diplomat Residences | Wonder shared with Gaia; Peponi / Westgate; **20%** agent must-have; `building` |
| DISC-NBO-023 | AYA Luxury Residence | Whitehorse (ex-AAD) (**5**); Sandoral RelatedParty **NDI never primary**; from **7.5M** LinkedIn; 4yr/0% soft; `building` |

### Developers
- New `dev-glbc-group`, `dev-wonder-properties`, `dev-whitehorse-real-estate` (promoted from Hauzisha leads)
- **Never** Hauzisha `0730 731 355` on developer contacts
- **Skip** Gemini Hub this wave

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **39** properties

### Decisions
- One-liner: Wave B locks Only You null primary + AYA Whitehorse/Sandoral NDI; all five `inventory_class=building`

---

## 0.1.16 — 2026-10-17 — Jafu Wave A seed (DISC-NBO-016…018)

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-016 | Citrine Heights | Jafu trading (**4**); `inventory_class=off_plan`; Westlands Rd; ~7.3M agent; payment **not** met |
| DISC-NBO-017 | Auris Residence | Jafu; `building`; studio/1/2BR ~5.5M agent; completion **NDI**; payment conflict **not** met |
| DISC-NBO-018 | Serene Manor | Jafu featured on jafugroupkenya.com; `building`; **20%** agent must-have met (conf 3) |

### Developer
- New `dev-jafu-real-estate-group` (trading conf 4; legal SPV unknown) — contact = website only; **never** Hauzisha `0730 731 355`

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **34** properties

### Decisions
- One-liner: Jafu Wave A shares one trading developer; Ready skips none this wave

---

## 0.1.15 — 2026-10-16 — Elegant wave seed (DISC-NBO-012…015)

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-012 | Forestview Residences | Elegant; Eldama Ravine; from **29.5M**; `inventory_class=building` |
| DISC-NBO-013 | Donyo Hill Residences | Elegant; Peponi × Donyo Sabuk; from **27.9M**; `building` |
| DISC-NBO-014 | 48 Treehouse | Elegant; 48×4BR; **77.9 vs 73M NDI**; `building` |
| DISC-NBO-015 | Sunpark Residence II | Elegant; Syokimau; Phase **II only**; from **8M**; `building` |

### Skipped (Ready)
- Sunpark Residence I · Oak & Ivy — not dossiered / not seeded as research targets

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **31** properties; `properties.csv` gains `inventory_class` column

### Decisions
- One-liner: Elegant wave uses shared `dev-elegant-properties`; Ready siblings stay out of corpus

---

## 0.1.14 — 2026-10-16 — `inventory_class` (Ready vs research queue)

### Schema
- Add enum `inventory_class`: **`off_plan` \| `building` \| `ready` \| `resale`**
- Add `property.inventory_class` (whole developments Ready / handed-over / Off-plan / Building)
- Add `listing.inventory_class`; allow **`listing.property_id` NULL** for orphan Ready unit ads
- **Coming soon** map → **`off_plan`** (no `coming_soon` enum) — stays in discovery/review scope
- Ready = **stored, not dossiered for now** (optional backlog only)

### Seed sketch
- [`seed/listings_hauzisha_inventory_leads.csv`](seed/listings_hauzisha_inventory_leads.csv) — Hauzisha developer-page developments with `inventory_class` where inferable; Ready only when tagged

### Decisions
- One-liner: portal Ready marked on listing + property; research queue = off_plan/building; Hauzisha exports = lead lists

---

## 0.1.13 — 2026-10-16 — Geo pins + POI (`geo_pin` / `poi` / `property_poi`)

### Schema
- Add `geo_method` enum: official | nema | geocode | csv | unknown
- Add `poi_type` enum: mall | hospital | school | transit | leisure | airport | cbd | other
- Add `geo_pin` (lat/lng + method + confidence + source_url/query + provider + accessed_at; one recommended per property)
- Add `poi` + `property_poi` (distance_m, source, confidence)
- Soft lock: `properties.lat/lng` only when conf ≥4; else pin lives in `geo_pin` / claims

### Seed / deliverable
- [`geo-enrichment.md`](geo-enrichment.md) — **27/27** dossiers; **26 pinned**, **1 unknown** (ELD-001)
- [`seed/geo_pins.csv`](seed/geo_pins.csv) · [`seed/pois.csv`](seed/pois.csv) · [`seed/property_pois.csv`](seed/property_pois.csv)
- Conf ≥4 already on `properties.csv`: Golden, Golfscape, Berkeley, Luna Oak, Galaxy, Plumeria

### Decisions
- One-liner: never invent GPS; Nominatim geocodes tagged `geo_method=geocode` conf 2–3; reject Airport-as-pin and implausible Longines JSON-LD

---

## 0.1.12 — 2026-10-16 — Discovery five (Canto / Ankori / Brookside / Kai / 108)

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| DISC-NBO-001 | CANTO (School Lane) | VAAL (**5**); **USD** 49k/68k; payment deposit must-have **not** met |
| DISC-NBO-004 | Ankori (Rhapta) | HassConsult (**4**); **30-mo payment canonical**; ≠ Galaxy One |
| DISC-NBO-006 | Brookside Oak | Van Tung (**3** legal NV); Oak Group marketing_partner; **9.9M vs 8.2M NDI**; ≠ Luna Oak |
| KWA-001 | Kai (Diani) | Ayce (**5**); Hass exclusive agent RelatedParty; unit taxonomy + completion **NDI** |
| DIA-001 | 108 Residences (Diani) | Omicron (**4**); Daiga+Dunhill marketing_partners; payment must-have **not** met |

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **27** properties; prefixes **KWA** / **DIA** added

### Decisions
- One-liner: coast Kwale (KWA) + DIA ids; Hass exclusive agent ≠ primary on Kai; Oak Group sibling marketing for Brookside vs Luna

---

## 0.1.11 — 2026-10-16 — Media gallery (`media_asset` + `property_media`)

### Schema
- Expand `media_asset`: `local_path`, `category`, `width_px` / `height_px` / `bytes`, `content_hash`, `page_url`, `confidence`, `accessed_at`
- Add `media_category` enum: exterior | interior | amenities | plans | progress | other
- Add `property_media` M2M (role, sort_order, optional category override)
- Skill: [photo-collector.md](../agents/photo-collector.md) · Rollup: [media-assets.md](media-assets.md)

### Decisions
- One-liner: listing photos are first-class assets with hash dedup + source provenance; no invented images

---

## 0.1.10 — 2026-10-16 — National + discovery seed wave

### Seeded
| ID | Project | Notes |
|----|---------|-------|
| NAK-001 | Kings Summit (Nakuru) | Kings Developers Ltd (**5**) + Royal Group; price **9M vs 8M NDI** |
| MSA-001 | Sensei (Nyali) | HassConsult (**4**); **30-mo payment canonical**; first coast |
| ELD-001 | Kings Square Ph2 (Eldoret) | Kings + Royal Group; typed 4M/5M; payment must-have **not** met |
| DISC-NBO-005 | Nouveau (Lenana) | HassConsult (**4**); payment **tenor NDI** |
| DISC-CAPRICORN | Capricorn (Wood Ave) | Staroot (**5**) + Mulika **co_developer** dual + Proxima **marketing_partner** |

### Rollup
- [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **22** properties; ID scheme NBO / NAK / MSA / ELD / DISC

### Decisions
- One-liner: national prefixes NAK/MSA/ELD + discovery DISC-*; HassConsult shared conf 4; Capricorn Mulika dual co_developer

---

## 0.1.9 — 2026-10-16 — agent_person + listing (M10)

### Schema
- `agent_person`: `first_name`, `last_name`, `notes`, optional `agency_id` → `agent`
- `party_owner_type` += **`agent_person`** — phones / emails / web stay on polymorphic `contact`
- `listing`: `property_id`, nullable `unit_type_id`, `source_url`, `publisher_agent_id`, optional `agent_person_id`, `status`, `first_seen_at` / `last_seen_at`
- `listing_agent`: M2M for multi-seller ads (`agent_id` and/or `agent_person_id`)
- **`property_agent` kept** for development-level agency coverage
- `listing_status` enum; M10 → **Merged**; M13 migrate path documented

### Seed gap (no invented people)
- Today: agency-only `agent` + `contact.label` (e.g. “Loyd Mokaya CSV” on `agent-block`)
- Migrate when evidenced: split → `agent_person` + re-own contacts; optional `listing` from retained `evidence_url`
- Desk labels (“Own It CSV”) stay on `agent` until a human name appears

### Decisions
- One-liner: schema v0.1.9 splits agency vs salesperson vs listing ad; contact channels unchanged; do not invent people

---

## 0.1.8 — 2026-10-16 — Wave C corpus complete (17/17)

### Seeded (Wave C)
| ID | Project | Developer notes |
|----|---------|-----------------|
| NBO-006 | Golfscape Residences | WH Harmony Investment Co. Ltd (**5**); Highpoint marketing_partner; price/progress **NDI** |
| NBO-011 | Lesonia Residences | Trading brand only (legal **0**); official price **NDI**; deposit **20%** canonical |
| NBO-012 | Luna Oak Residency | Mingland Company Limited (**5**); Oak Group marketing_partner; from **14.8M vs 11.9M NDI** |
| NBO-014 | Alba Apartments | Nanchang Investment (**conf 3**); Own It = **agent**; parent GroupCompany proposed |
| NBO-015 | Plumeria Residency | Riara Plumeria Development Limited NEMA (**5**); Own It = agent; Golden Apple **wrong entity** |
| NBO-016 | Polaris Residency | Developer **unknown**; Own It = agent; status heavily conflicted |

### Rollup
- New inventory: [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — **17/17** dossiers seeded
- `properties.csv` covers NBO-001…017 with no gaps

### Decisions
- One-liner: Wave C complete — 17 properties seeded; Polaris has no developer; Own It never promoted to developer

---

## 0.1.7 — 2026-10-16 — Data quality / risk scores

### Deliverable
- [`data-quality-scores.md`](data-quality-scores.md) — v1 rubric + Admin triage over **11** method-complete dossiers
- Metrics: NDI count, NV count, developer conf, sources retained, agent-only commercial (0–3)
- Top triage: **P0** Misty Springs · **P1** Berkeley Homes + Galaxy One · **P3** Longines + Diamond
- Skill Active on [agent-roster.md](../agent-roster.md); Verification queue owner promoted to launch-now consumer

### Not done
- No persisted `property_quality_score` schema table yet (Admin/Plus bind later)

---

## 0.1.6 — 2026-10-16 — Payment-plan normalizer

### Deliverable
- Catalog: [`payment-plans.md`](payment-plans.md)
- Seed refresh: [`seed/payment_plan_claims.csv`](seed/payment_plan_claims.csv) — **47** rows / **11** properties
- Extra analytics columns: `external_id`, `cash_vs_instalment`, `sources`

### Corrections
- Porini 24-mo tenor: `is_canonical` **false** + `needs_developer_input` (official conflict with 3-yr pack — was incorrectly canonical)
- Added Riara / Misty / Golden / Diamond schedule & fee rows previously missing

### Rule
- No invented plans; stubs (Golfscape, Lesonia, Luna Oak) not seeded

---

## 0.1.5 — 2026-10-16 — Feature taxonomy merged

### Schema
- Merged DDL from [feature-taxonomy.md](feature-taxonomy.md):
  - `feature_scope` enum: **`development` \| `apartment` \| `house` \| `community`**
  - Tables: `feature`, `feature_scope_map`, `feature_synonym`, **`property_feature`**, **`unit_type_feature`**
- Soft rules: developer-canonical amenities; agent-only → `needs_verification`; free-text `claim(amenities.core)` additive until Coverage retires it
- Exposure: public filters coverage-gated; Admin/Plus keep full feature graphs + synonyms
- Migration M12 → **Merged**

### Seeds (taxonomy steward — confirmed linked)
- `features.csv`, `feature_scopes.csv`, `feature_synonyms.csv`, `property_features.csv`, `unit_type_features.csv`

### Decisions
- One-liner: schema v0.1.5 encodes feature scopes development/apartment/house/community

---

## 0.1.4 — 2026-10-16 — Corpus coverage & field promotion

### Coverage pass
- Living scoreboard: [`field-promotion.md`](field-promotion.md)
- Denominator: **11** method-complete dossiers (3 premature stubs excluded: Golfscape, Lesonia, Luna Oak)
- **Public shortlist (intent):** name, neighbourhood geo, primary developer (conf≥4), developer amenities core, canonical unit types + measure-tagged sizes, status summary, completion when not NDI, payment when threshold stable
- **Explicit non-public:** `price_from`, lat/lng, construction progress, unit/storey/block scalars, built-up, sparse RelatedParty/stakeholders, empty GroupCompany, full agent graph, research meta

### Decisions
- One-liner promotion lock in [decisions.md](../decisions.md) (Fields & portal promotion)

### Not done
- No `is_portal_field=true` flips in `must_have_fields.csv` this pass (intent only; product-surface mapping binds screens next)

---

## 0.1.4 — 2026-10-16 — Wave B complete seed rollup

### Ingested / confirmed
| external_id | Project | Notes |
|-------------|---------|-------|
| NBO-001 | Golden Mansion | Summit Vista (NEMA 5); XiangFeng **co_developer + RelatedParty**; SkyPeak **marketing_partner** |
| NBO-008 | Longines Bay Kilimani | Nanchong Longines Bay Limited; first **GroupCompany** (`grp-nanchong-group`); 601/3 blocks vs marketing **NDI** |
| NBO-010 | Berkeley Homes | Rarlon (4); CSV Procmura false lead; ESIA **361 vs 360** **NDI** |

### Rollup
- `seed/wave-b-rollup.md` — all 11 seeded properties (Cycle 1–2 + Wave B scale)
- `seed/group_companies.csv` added
- `seed/README.md` refreshed

### Later resolved
- Feature taxonomy merge → **0.1.5** (no longer pending)

---

## 0.1.3 — 2026-10-16 — Half-batch seed ingest (wave)

### Ingested into `seed/`
| external_id | Project | Developer notes |
|-------------|---------|-----------------|
| NBO-003 | Riara Oasis | Riara Oasis Limited via NEMA EIA; AIMASI `marketing_partner`; no microsite |
| NBO-009 | Gemini Residency Phase 2 | Staroot (5); Proxima `marketing_partner`; completion site vs LinkedIn → **NDI** |
| NBO-017 | Misty Springs | Tian Yu lead **conf 2** NV; Own It = agent; status heavily conflicted; no microsite |
| NBO-007 | Diamond Bay Residences | **Henbon Company LTD (5)**; official from **8.84M vs 9.34M** → **NDI**; Sept 2027 canonical |

### Modeling notes
- Official filing (NEMA) can stand in for microsite as developer-weight source
- Weak LinkedIn-only developer identity stays conf ≤2 + `needs_verification` (Misty)
- Own It / Block CSV contacts remain agents, never auto-promoted to developer

---

## 0.1.2 — 2026-10-16 — Rightmove-class surface tiers

### Product framing
User confirmed north star: **Rightmove + Rightmove Admin + Rightmove Plus**; strong data layer; professional calculated decisions ([goal-and-approach.md](../goal-and-approach.md)).

### Schema / docs
- `exposure_tier`: `public` \| `admin` \| `plus` \| `internal` (replaces vague public/pro)
- Surface map + cheat-sheet: public = coverage+confidence gate; Admin/Plus retain conflicts, `needs_*`, full claim sets, agent graphs
- `must_have_field` gains `exposure_public` / `exposure_admin` / `exposure_plus`
- README + er-notes aligned to three-product analogy

### Decisions
- One-liner appended to [decisions.md](../decisions.md)

---

## 0.1.1 — 2026-10-16 — Cycle 2 user locks applied

### Locks encoded (see [decisions.md](../decisions.md))
1. Co-named developers → **both** `property_developer(co_developer)` **and** RelatedParty (Tatu City Limited / Porini) — not candidate-only  
2. Official vs official → `needs_developer_input` (distinct from `needs_verification`); no winner  
3. Prices always multi; conflicting official → **no** public `price_from` + NDI  
4. Agent-only payment conf ≤3 without developer — affirmed  
5. `construction_progress` = candidate; capture when published; coverage-gated for portal  
6. Portal fields later = high conf **and** high coverage  

### Schema
- Added `needs_developer_input` on `claim`, `price_observation`, `construction_progress`, `claim_conflict`
- Dual-write rule for co-named developers; removed `co_developer_candidate` enum usage
- Portal gate columns on `must_have_field` (`is_portal_candidate`, `is_portal_field`, `coverage_notes`)
- Linked README / er-notes → decisions.md + goal-and-approach.md

### Seed refresh
- `dev-tatu-city-limited` + `property_developers` co_developer edge for Porini  
- RelatedParty Tatu typed `co_developer` (dual with M2M)  
- Official conflicting prices / unit counts / storeys / progress → `needs_developer_input`  
- Astra/Pandora agent-only payment conf capped at 3  

### Open (non-blocking)
- Later verification passes for NDI items  
- Portal field finalization after coverage analysis  
- Dual-link simplification when more co-named patterns appear  

---

## 0.1.0 — 2026-10-15 — Initial model + Cycle 1/2 ingest

### Created
- `schema.md`, `er-notes.md`, `seed/`, `README.md`

### Dossiers ingested
| external_id | Project | Cycle | Key modeling lessons |
|-------------|---------|-------|----------------------|
| NBO-002 | Pandora Residences | 1 | Official-vs-official unit mix; brochure sizes; payment 20% via ≥4 agents; Karim CG stakeholder |
| NBO-005 | Astra Bay Residence | 1 | Laureland `marketing_partner`; gross/plinth; agent 2BR NV |
| NBO-004 | Porini Point | 2 | Scale 570/24/58k; Tatu dual co_developer (applied 0.1.1); master_planned geo; dual prices |
| NBO-013 | Galaxy One | 2 | Units/storeys/progress official conflicts; deposit 10% vs 20%; CRJE; GPS |

### Not done (still)
- Live SQL migration / ORM  
- `listing` entity  
- Seed for remaining CSV / Wave-B projects  

---

## Template for future entries

```
## X.Y.Z — YYYY-MM-DD — <title>
### Ingested / changed
### Migrations proposed or applied
### Open questions
```
