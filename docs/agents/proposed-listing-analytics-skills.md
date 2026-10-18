# Proposed skills — listing site + agent analytics

Inspired by feature taxonomy + Rightmove / Plus-class needs.  
Goal: stronger **public facets** and a **Plus analytical layer** for estate agents (comparables, inventory, risk, coverage).

## Already in motion
- Feature taxonomy (development / apartment / house / community)
- Coverage & field promotion
- Product surface map + Majengo2 intel
- DB steward

## A. Listing-site data skills (facets & detail)

| Skill | What it adds | Why valuable | Priority |
|-------|--------------|--------------|----------|
| **Payment-plan normalizer** | Structured deposit %, tenor, cash vs instalment, booking fees as analytics-ready rows | Agents quote plans constantly; powers filters + affordability tools | **P0** |
| **Price observation time series** | Dated price claims (first seen / last seen), sold-out flags | “Price changed”, history for Plus; avoid stale scalars | **P0** |
| **Inventory & availability tracker** | Units left, sold-out typologies, showhouse status | Listing truth + urgency signals for agents | **P0** |
| **Document / brochure intelligence** | PDF floor plans → sizes, features, disclaimers | Dense Kenya sources are PDFs; feeds taxonomy + sizes | **P0** |
| **Media asset steward** | Gallery, brochure pages, plan images with provenance | Public gallery + Admin QA | P1 |
| **Geo / POI enricher** | Neighbourhood hierarchy, landmarks, commute corridors, estate boundaries | Search facets + map; Tatu/SEZ context | P1 |
| **Spec & parking normalizer** | Parking bays/ratio, finishes, storeys as structured specs | Filters + agent pitch sheets | P1 |
| **Legal / tenure pack** | Freehold/leasehold, plot IDs, NEMA/Gazette refs | Trust + Admin; already appearing in NEMA dossiers | P1 |

## B. Analytical / Plus skills (for estate agents)

| Skill | What it adds | Why valuable for agents | Priority |
|-------|--------------|-------------------------|----------|
| **Entity resolution / party graph** | Dedupe Lionston/Lionstone, Procmura traps, agent networks | Clean CRM-like graph; who sells what | **P0** |
| **Cross-portal listing matcher** | Same project across Block/NRE/Own It/etc. | “Where else is this listed?” + copy conflicts | **P0** |
| **Area comps / PSF analytics** | Neighbourhood price bands from our corpus (KES/sqm when sizes exist) | Advice-grade comps without inventing external prices | **P0** |
| **Developer portfolio intelligence** | All projects per developer + delivery track record claims | Pitch credibility; risk | P1 |
| **Construction progress series** | Time-stamped % / floor from developer trackers | Timeline risk for buyers/agents | P1 |
| **Agency coverage map** | Which agencies cover which projects/areas | Lead routing, competitive intel for agencies | P1 |
| **Data quality / risk scorer** | Score projects by NDI density, weak developer, source thinness | Plus “trust” badge inputs; Admin triage | **Done** — [data-quality-scores.md](../db/data-quality-scores.md) |
| **Verification queue owner** | Work `needs_developer_input` / `needs_verification` systematically | Clears public blockers | **P0** |
| **Client-match feature packs** | Bundles (family / investor / expat) from taxonomy | Plus matching without new raw facts | P2 |
| **Rental yield context** (careful) | Only from sourced rental comps if we add that corpus later | Investment Plus — **do not invent yields** | P2 deferred |

## C. Suggested launch order
1. ~~Payment-plan normalizer~~ **Done**  
2. ~~Entity resolution~~ **Done**  
3. ~~Area comps / PSF~~ **Active**  
4. ~~Data quality / risk scorer~~ **Done** — [data-quality-scores.md](../db/data-quality-scores.md)  

**Next:** **Product readiness reviewer** ([product-readiness-reviewer.md](product-readiness-reviewer.md)) → Verification queue owner (consumes quality triage) → document intelligence → inventory tracker → cross-portal matcher.

## Rules for all analytics skills
- No invented market facts — analytics only over **sourced claims** in our DB  
- Always retain provenance + confidence  
- Public never shows low-coverage or NDI fields; Plus may show with badges  
