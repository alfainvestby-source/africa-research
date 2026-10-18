---
title: Zoopla → Kenya field gap evaluation
date: 2026-10-17
corpus: 39 seeded properties (corpus-rollup)
adapted_fields: kenya-listing-fields.md
schema: db/schema.md v0.1.14
---

# Zoopla → Kenya gap evaluation

Compares [kenya-listing-fields.md](kenya-listing-fields.md) to what we actually capture in schema + dossiers/seeds. **No invented property facts** — coverage from seed CSVs + prior promotion/DQ passes.

Related: [zoopla-listing-fields-source.md](zoopla-listing-fields-source.md) · [schema.md](../db/schema.md) · [feature-taxonomy.md](../db/feature-taxonomy.md) · [field-promotion.md](../db/field-promotion.md) · [readiness-scorecard.md](readiness-scorecard.md) · [surface-map.md](surface-map.md) · [corpus-rollup.md](../db/seed/corpus-rollup.md)

---

## Open questions — RESOLVED 2026-10-17

All eight locks written in [zoopla-kenya-product-decisions.md](zoopla-kenya-product-decisions.md) + [decisions.md](../decisions.md). Evidence for #2/#5: [zillow-rightmove-model-study.md](zillow-rightmove-model-study.md).

| # | Lock |
|---|------|
| 1 | Off-plan/`building` first; Ready+resale easy later |
| 2 | **2B** development-first + typology `listing` snapshots (retained URLs only) |
| 3 | Kenya energy vocab; no EPC chase |
| 4 | Buyer-costs guide; per-project when developer publishes |
| 5 | Bathrooms first-class; fill when sourced; never invent |
| 6 | `tenure` claim; Admin/Plus; public conf≥4 official |
| 7 | Agent phones **Plus only** |
| 8 | **8B** Ready on Plus+Admin (badge); public off-plan/UC |

2. **Public hero price?** — earlier multi-claim lock unchanged (not in this checklist).

---

## Method snapshot

| Input | Used as |
|-------|---------|
| Seed corpus | **39** properties; unit_types **38/39**; prices **38/39**; payments **38/39**; features **39/39**; property_agents **37/39** |
| GPS on property row | **7/39** lat filled (more pins in `geo_pins` with mixed conf) |
| `inventory_class` filled | **12/39** (backfill remaining is process debt, not a Zoopla gap) |
| Bathrooms on unit_type | **0** filled |
| Media seed CSVs | **none** in `seed/` (DDL exists; photo manifests elsewhere per readiness) |
| Listing rows | Lead CSV only (`listings_hauzisha_inventory_leads.csv`) — not full `listing` graph |
| Field promotion public shortlist | Name, neighbourhood, developer≥4, amenities core, canonical units/sizes, status summary, completion (non-NDI), payment when threshold |

---

## Have with good coverage

Fields we model **and** routinely capture for off-plan/UC developments.

| Adapted field | Where we store it | Coverage signal |
|---------------|-------------------|-----------------|
| Development identity (name, aliases, slug) | `property`, `property_alias` | **39/39** |
| City / neighbourhood / street hierarchy | `geo_place`, property FKs | Near-universal neighbourhood; streets common |
| Primary developer (+ co_dev / marketing_partner) | `developer`, `property_developer`, `related_party` | **37/39** primary (Only You null-by-lock; Polaris unknown) |
| Currency default KES (+ USD when primary) | `property.currency_default`, price rows | KES default; USD e.g. CANTO |
| Multi price claims | `price_observation` | **38/39** props |
| Payment deposit / tenor / reservation | `payment_plan_claim` | **38/39**; must-have met on a subset |
| Beds + typology labels (+ DSQ/study) | `unit_type` | **38/39**; sizes often present |
| Size sqm (+ measure tags) | `unit_type.size_*` | High when developer/brochure |
| Amenities / feature chips | `feature` taxonomy + `property_feature` | **39/39** linked |
| Status summary / UC vs off-plan language | `property.status_label` + claims | Universal (often conflicted → Admin) |
| Completion / handover window | claims / dossier | High presence; quality varies |
| Agency coverage graph | `property_agent`, `agent`, `contact` | **37/39** |
| Research provenance | `research_pass`, sources in dossiers | Seeded for corpus |
| inventory_class (when set) | `property` / `listing` | Modeled; **12/39** backfilled so far |
| Master-planned community | `geo_place.is_master_planned` | When applicable (Tatu) |

These align with the **public shortlist** in [field-promotion.md](../db/field-promotion.md) (with per-row canonical gates).

---

## Have but thin / low confidence

Modeled (or partially modeled) but fail public gates or sparse in seeds.

| Adapted field | Gap | Why thin |
|---------------|-----|----------|
| Lat/lng map pin | Schema + `geo_pin` | Only **7/39** on property row; many NV/CSV; public GPS blocked |
| Construction progress % | `construction_progress` | **10** props / 15 rows; agent UI % often NV; NDI when official conflicts |
| Unit count / storeys / blocks | claims | Frequent NDI/NV — Admin claim-set only |
| Hero / from price as single card number | `price_observation` | Intentionally multi; official NDI common |
| Payment plan **stable** public deposit | payment rows | Many agent-only conf≤3; threshold unmet on several discovery rows |
| Related parties / GroupCompany | RP table | Sparse; GroupCompany correctly rare |
| Named `agent_person` | DDL | Almost unused — no invented people |
| POI / nearest landmarks | `poi`, `property_poi` | Tiny seed (~7 POIs) vs Zoopla transports |
| Buyer incentives | free-text in dossiers / payment notes | Not a first-class structured object |
| Service charge | occasional dossier prose | Not normalized |
| Tenure / sectional title | dossier prose (~14 files) | **No structured seed column** |
| Media gallery / floorplans / brochure | `media_asset` DDL | **No media seed CSV**; readiness notes photo manifests elsewhere — not rolled into seed graph |
| `listing` unit/ad snapshots | `listing` DDL | Lead inventory CSV only; not dossier-URL listings at scale |
| Bathrooms | `unit_type.bathrooms` | Column exists; **2/180** filled (hygiene 2026-10-17: Kings Summit=2 conf5; 48 Treehouse=5 conf3 NV). Rest blank — no invent from “all ensuite” |
| Living rooms / receptions | — | Not modeled; low Kenya marketing density |
| Dual cash vs instalment prices | `price_basis` | Present on some (Porini/Galaxy pattern); low coverage |
| inventory_class backfill | property column | **27/39** still empty string in seed |

---

## Missing — should try to find

Prioritized for a **Kenya off-plan / new-developments** product (not general resale classifieds). Schema “missing” vs research “not chased” both count.

| Priority | Field | Why chase | Suggested home |
|---------|-------|-----------|----------------|
| **P0** | **Media gallery + floor plans + brochure PDFs** | Zoopla cards are media-first; readiness already flags media as ship-blocker | `media_asset` / `property_media` seed + research checklist |
| **P0** | **Bathrooms (per unit type)** | Zoopla core attribute; buyers expect baths with beds/size | Fill `unit_type.bathrooms` when plans/agents state them |
| **P1** | **Tenure / sectional title / freehold** | Material-info analog; appears in some FAQs/EIAs | New claim key + optional property column; Admin until coverage |
| **P1** | **Structured `listing` rows** (portal/unit ads) | Zoopla parity for search cards; enables Ready store-without-dossier | Seed from retained dossier URLs — no invented ads |
| **P1** | **POI distances** (mall, transit, CBD, airport) | Replaces UK nearestStations; Plus proximity chips | Expand `poi` / `property_poi` with method+conf |
| **P2** | **Buyer incentives** (0% interest, free kitchen, etc.) | Zoopla new-build `buyerIncentives`; common Kenya marketing | Structured claim or payment companion object |
| **P2** | **Service charge (est.)** | Ongoing cost; Zoopla-ish material info | Claim key when brochure/FAQ states |
| **P2** | **Developer-canonical payment schedule** (not only agent ≥4) | Product trust; many rows agent-only | LOO / brochure chase in verification queue |
| **P3** | **Videos / virtual tours** | Zoopla embeddedContent | media_asset type video/tour |
| **P3** | **Price history / reduced badges** | Zoopla sale UX | Later unit-ad surface |

### Top 5 to chase now

1. **Media + floorplans + brochures**  
2. **Bathrooms on unit types**  
3. **Tenure / sectional title** (when published)  
4. **Listing/ad snapshots** from retained URLs  
5. **POI / nearest landmark distances**

---

## N/A or low priority for Kenya off-plan

| Zoopla field | Verdict |
|--------------|---------|
| UK postcode outcode/incode/postalArea | **N/A** — use county/city/neighbourhood/street |
| Council tax band | **N/A** — optional land rates/NMS only if sourced |
| EPC rating / hasEpc | **Low** — rare; optional green claims only |
| Chain-free | **N/A** — off-plan primary sales |
| Shared ownership | **N/A** — UK product |
| Rent pcm / pw / furnishedState / availableFrom / letting_arrangements | **Deferred** — rent surface later |
| Administration fees (UK lettings) | **N/A** |
| UPRN + HM Land Registry sold history / zindex | **Deferred** — Ready comps later |
| Google Street View as must-have | **Low** — UC sites often unavailable |
| UK propertyType terrace / semi_detached / bungalow as default enum | **Remap** — apartment/townhouse/villa first |
| Auction flag | **Low** |
| Agent ad-package ecommerce variant | **Plus/ops later** |

---

## Surface alignment (quick)

| Tier | Zoopla-like expectation | Our state |
|------|-------------------------|-----------|
| **Public** | Clean card: place, beds, from-price, photos, agent/dev CTA | Identity/place/developer/amenities/units **strong**; **media + hero price policy** still block ship ([readiness-scorecard](readiness-scorecard.md)) |
| **Admin** | Full material info + history | Conflicts/NDI/NV/sources **strong**; media attach/OCR and tenure claim keys weak |
| **Plus** | Multi prices, incentives, agent graph, transports | Multi prices + agents **good**; POI + incentives + listing ads **thin** |

---

## Recommended next moves (non-blocking on Slice C)

1. Add research checklist items: **bathrooms**, **tenure**, **floorplan/brochure URL**, **service charge**, **incentives** — extract when present; never invent.  
2. Seed **media_asset** links for developments that already have photo manifests.  
3. Backfill `inventory_class` on the **27** properties still blank (process, from dossier tags).  
4. Pilot **listing** rows from a handful of retained agent URLs (Alba pattern in schema notes).  
5. Re-run field-promotion / DQ after media+baths land — public shortlist may grow.

---

## Document index

| Doc | Path |
|-----|------|
| Kenya-adapted fields | [`docs/product/kenya-listing-fields.md`](kenya-listing-fields.md) |
| This gap eval | [`docs/product/zoopla-kenya-gap-eval.md`](zoopla-kenya-gap-eval.md) |
| Zoopla source | [`docs/product/zoopla-listing-fields-source.md`](zoopla-listing-fields-source.md) |
