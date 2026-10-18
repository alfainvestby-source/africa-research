# Agent roster — skills we need

North star: Rightmove-class **public / Admin / Plus**.  
Preference: propose agents with **new skills**, not only more research clones.  
Full proposal: [proposed-listing-analytics-skills.md](agents/proposed-listing-analytics-skills.md)  
Decisions: [decisions.md](decisions.md)

## Active

| Skill | Status |
|-------|--------|
| Off-plan research | Wave B done (11/17); Wave C pending |
| Proptech DB modeling | [DB steward](bc-1bdc7ab6-93cc-513e-a234-3ba81ab0f03b) |
| Coverage & field promotion | [field-promotion.md](db/field-promotion.md) |
| Product surface mapping | [surface-map.md](product/surface-map.md) |
| Feature taxonomy | [Feature taxonomy steward](bc-613b6e10-8496-5343-85b3-05e1fca42ad9) |
| Majengo2 competitive intel | **Awaiting Project access** — Majengo2 = Cursor Project (not majengo.co.ke). Stub: [product/majengo2-intel.md](product/majengo2-intel.md). ([agent](bc-87598a24-51a1-5474-ae85-1eeff2f22c06)) |
| Entity resolution / party graph | **Done** — [db/entity-resolution.md](db/entity-resolution.md) v0.1.0 · Lionston/Procmura/SkyPeak/Block hubs |
| Area comps / PSF analytics | **Active** — [db/area-comps-psf.md](db/area-comps-psf.md) v0.1 · Plus-only neighbourhood bands; no majengo.co.ke |
| Payment-plan normalizer | **Done** — [db/payment-plans.md](db/payment-plans.md) · [seed/payment_plan_claims.csv](db/seed/payment_plan_claims.csv) (47 claims / 11 props) · [agent](bc-2a4a2b29-ba1b-5f07-97de-db4468ea4b4d) |
| **Data quality / risk scorer** | **Done** — [db/data-quality-scores.md](db/data-quality-scores.md) ([spec](agents/data-quality-scorer.md)) · Admin P0–P3 triage over 11 dossiers |
| **Photo / image collector** | **Active** — [agents/photo-collector.md](agents/photo-collector.md) · [db/media-assets.md](db/media-assets.md) · `media/projects/<slug>/` + schema v0.1.11 |
| **Geo / POI enricher** | **Done** — [db/geo-enrichment.md](db/geo-enrichment.md) · [seed/geo_pins.csv](db/seed/geo_pins.csv) · schema **v0.1.13** · **26/27 pinned** (6 conf≥4; 18 geocode; 2 CSV; **1 unknown** ELD-001) · light POI sample |

## Proposed next (listing + agent analytics)

### Launch now (recommended)
| Skill | Value |
|-------|--------|
| **Product readiness reviewer** | **Active — first pass done** · [readiness-scorecard.md](product/readiness-scorecard.md) · [gap-backlog.md](product/gap-backlog.md) · [plus-readiness.md](product/plus-readiness.md) · [verification-queue.md](db/verification-queue.md) · [spec](agents/product-readiness-reviewer.md) |
| **Verification queue owner** | **Next** — clear P0/P1 in [verification-queue.md](db/verification-queue.md) (execution twin of readiness reviewer) |

### Soon after
| Skill | Value |
|-------|--------|
| Document / brochure intelligence | PDF → sizes & features |
| Inventory & availability tracker | Sold-out / units left |
| Cross-portal listing matcher | Same project across agencies |
| Price observation time series | Staleness & history |
| Spec & parking normalizer | Parking ratios, finishes |
| Legal / tenure pack | Plot IDs, freehold/leasehold |
| Developer portfolio intelligence | Cross-project developer view |
| Construction progress series | Timeline risk |
| Agency coverage map | Who sells where |

### Later / careful
| Skill | Note |
|-------|------|
| Client-match feature packs | Bundles from taxonomy |
| Rental yield context | Only if we source rental corpus — never invent |
| Independent QA audit | Spot-check after each wave |

## Specs
Under `docs/agents/`. New skills get a short spec before launch.
