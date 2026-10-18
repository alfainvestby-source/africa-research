---
title: Product surface map — Rightmove / Admin / Plus
skill: product-surface-mapper
version: 0.1.2
updated: 2026-10-17
inputs:
  - docs/goal-and-approach.md
  - docs/decisions.md
  - docs/db/schema.md (v0.1.14+)
  - docs/db/er-notes.md
  - docs/agents/feature-taxonomy.md
  - docs/product/zoopla-kenya-product-decisions.md (#1–8 LOCKED)
---

# Surface map — public / Admin / Plus

**North star:** Kenya property product in the class of **Rightmove** (consumer), **Rightmove Admin** (ops/content), **Rightmove Plus** (pro/agent). Master DB stores once; surfaces project by `exposure_tier`.

**Rules:** No invented listing facts. Public gates = **high confidence AND high coverage**. Admin/Plus **retain** conflicts, `needs_verification`, `needs_developer_input`, multi prices, agent graphs.

**Zoopla→Kenya locks (2026-10-17):** public = development-first (**2B**); agent phones **Plus only** (#7); Ready unit cards **Plus+Admin** with badge (**8B**); bathrooms on cards when sourced (#5). See [zoopla-kenya-product-decisions.md](zoopla-kenya-product-decisions.md).

Related: [goal-and-approach](../goal-and-approach.md) · [decisions](../decisions.md) · [schema](../db/schema.md) · [ER notes](../db/er-notes.md) · [agent roster](../agent-roster.md)

---

## Tier definitions (locked)

| Tier | Analogy | What users get |
|------|---------|----------------|
| **`public`** | Rightmove | Clean development pages + search facets from **canonical / agreed** values that pass coverage+confidence; confidence scores hidden (v1); no raw conflict dumps; no invented winners on official-vs-official |
| **`admin`** | Rightmove Admin | Full claim sets, conflict groups, both `needs_*` flags, source URLs, research_pass meta, verification queues — ops resolve NDI/NV |
| **`plus`** | Rightmove Plus | Multi price tables, payment options, progress snapshots, full agent/contact graphs, pro facets; may badge `needs_*` without resolving |
| **`internal`** | Steward/QA | Seed-CSV notes, ranking experiments (may fold into admin) |

---

## Capability matrix

Legend for **Gap:** `ok` = modeled + research producing it · `partial` = modeled, sparse coverage or no UI projection · `missing` = not in schema/product yet · `deferred` = intentionally later

### A. Consumer discovery & development page (`public` core)

| # | Capability (Rightmove-class) | Entities / fields | Tier | Gap | Notes |
|--:|------------------------------|-------------------|------|-----|-------|
| A1 | Search by area / neighbourhood | `geo_place`, `property.geo_*` | public† | partial | Hierarchy modeled; corpus coverage incomplete; master-planned (Tatu) supported |
| A2 | Search by developer | `developer`, `property_developer` | public† | partial | Primary + co_developer modeled |
| A3 | Filter by beds / **baths** / unit type | `unit_type` (canonical) | public† | partial | Beds+size strong; **bathrooms** first-class when sourced (#5 LOCKED); agent-only typologies stay admin/plus + NV |
| A4 | Filter / sort by price | `price_observation` | public† / plus | partial | **Always multi-row**; public hero price **blocked** when NDI or fail gate |
| A5 | Filter by status (off-plan / UC / selling) | `claim(status)` | public† | partial | Often claim-set only; no silent winner |
| A6 | Filter by completion window | `claim(completion_estimate)` | public† | partial | Often agent-backed; developer date sparse |
| A7 | Development identity page | `property`, `property_alias`, canonical claims | public† | ok | Dossier → seed path clear |
| A8 | Amenities / key-feature filters | `claim(amenities.core)` → planned `feature` taxonomy | public† / plus | partial | Today free-text core; see **Feature scopes** below |
| A9 | Media gallery / brochure | `media_asset`, `source` | public† / plus | partial | Schema ready; PDF OCR skill not yet active |
| A10 | Map pin | `property.lat/lng` or geo claims | public† | partial | Prefer developer geo only on row; CSV GPS → NV |
| A11 | CTA — enquire / call developer sales | `contact` owner=property\|developer | public | ok (rule) | **LOCKED #7:** public = developer/project CTA only; full agent mobiles → Plus |
| A12 | “Similar developments” | — | public | missing | Needs similarity rules + coverage |
| A13 | Saved search / alerts | — | public | deferred | Out of schema v1 (accounts) |
| A14 | Typology-linked listing snapshots (**2B**) | `listing` + `unit_type` + `inventory_class` | public† / plus | partial | **LOCKED 2B:** development page canonical; listings = retained-URL typology offers (no invented flat IDs). Ready/resale store-only for research — [portal-inventory-class-research-rules.md](../discovery/portal-inventory-class-research-rules.md) |

† after coverage + confidence gate.

### B. Ops / content console (`admin`)

| # | Capability | Entities / fields | Tier | Gap | Notes |
|--:|------------|-------------------|------|-----|-------|
| B1 | Claim conflict browser | `claim_conflict`, `claim_conflict_member` | admin | partial | Modeled; no product UI; seed conflict extracts exist |
| B2 | Queue: `needs_developer_input` | `claim.needs_developer_input`, flags | admin | partial | Flag locked; worklist started → [verification-queue.md](../db/verification-queue.md) (owner skill still to execute) |
| B3 | Queue: `needs_verification` | `claim.needs_verification` | admin | partial | Same as B2 — queue v0.1.0 synthesized 2026-10-16 |
| B4 | Source library + research_pass | `source`, `research_pass`, counts | admin | ok | Dossiers + index counts; ops UI missing |
| B5 | Confidence / publisher_class view | `claim.confidence`, `publisher_class` | admin | ok | Internal; not public v1 |
| B6 | Contact ownership QA (CSV agent ≠ developer) | `contact.owner_*` | admin | partial | Soft rule locked; dedupe skill proposed |
| B7 | RelatedParty / GroupCompany typing QA | `related_party`, `group_company` | admin | ok | marketing_partner vs co_developer dual-link documented |
| B8 | Must-have / coverage dashboard | `must_have_field`, corpus scores | admin | partial | Living CSV/schema; **coverage agent** to run |
| B9 | Seed lead ingest / CSV reconcile | `property.external_id`, notes | admin / internal | partial | Seed CSV = leads only |
| B10 | Media / brochure attach + OCR review | `media_asset` | admin | missing | Document-intel skill proposed |
| B11 | Independent QA audit trail | `verification_flag` | admin | missing | QA skill proposed |

### C. Pro / agent tools (`plus`)

| # | Capability | Entities / fields | Tier | Gap | Notes |
|--:|------------|-------------------|------|-----|-------|
| C1 | Full multi-price table (cash / instalment / tenor) | `price_observation` | plus | partial | Dual basis modeled; sparse dual columns in corpus |
| C2 | Payment plan detail (deposit, booking, balance) | `payment_plan_claim` | plus | partial | Threshold lock live; tenor often NV |
| C3 | Agent graph per development | `agent`, `property_agent` | plus | partial | Captured in dossiers; brand dedupe proposed |
| C4 | WhatsApp / phone / email roster | `contact` | plus | ok (rule) | **LOCKED #7:** Plus = full agent graph; never promote Hauzisha `0730` as developer |
| C5 | Construction progress snapshots | `construction_progress` | plus / admin | partial | Candidate; coverage-gated for public |
| C6 | Unit mix incl. NV typologies (badge) | `unit_type` + flags | plus | partial | Show + NV (e.g. agent-only beds/baths) |
| C7 | Stakeholder strip (contractor, architect) | `stakeholder` | plus | partial | When named; often sparse |
| C8 | Export / CRM handoff | — | plus | missing | Product later |
| C9 | Competitive set / yield tools | — | plus | deferred | Needs rents + more corpus |
| C10 | Branch / network inventory | `agent` network types | plus | missing | Aggregator vs agency typing soft |
| C11 | Ready unit cards (thin lead stock) | `listing` where `inventory_class=ready` | plus / admin | partial | **LOCKED 8B:** show with **not research-verified** badge; public stays off-plan/UC; no auto-dossier |

### D. Cross-cutting data-layer (all tiers)

| # | Capability | Entities / fields | Tier | Gap | Notes |
|--:|------------|-------------------|------|-----|-------|
| D1 | Provenance on every commercial fact | `claim` + `claim_source` | all | ok | Core method |
| D2 | Official-vs-official no-winner | `needs_developer_input` | admin / plus | ok | Locked C2 |
| D3 | Agent-only / low-conf show | `needs_verification` | admin / plus | ok | Locked C1 |
| D4 | Canonical when developer sources agree | `is_canonical` | public† | ok | |
| D5 | Size measure tagging | `size_measure` / gross+plinth | public† / plus | partial | Capture when materials distinguish |
| D6 | Co-named developers dual model | `property_developer` + `related_party` | admin / plus | ok | Simplify later (M11) |
| D7 | Unproven brand → marketing_partner | `related_party` | admin / plus | ok | e.g. Laureland pattern |
| D8 | Source selection meta (scan~10 / keep≥5) | `research_pass` | admin | ok | |
| D9 | Field promotion gate | `must_have_field.exposure_*` | admin | partial | Needs corpus coverage run |
| D10 | Typology-linked `listing` (**2B**) | `listing` + `unit_type` | public† / plus | partial | DDL exists; seed from retained URLs only — no invented flat IDs |
| D11 | Claim key `tenure` | `claim.field_key=tenure` | admin / plus / public† | partial | **LOCKED #6:** public only conf≥4 official |

---

## Prioritized data-layer gap list

Ordered by **product path dependency** (blocks Rightmove-class surfaces soonest), not inventing new Nairobi facts.

| Prio | Gap | Blocks | Recommended next skill / action |
|-----:|-----|--------|----------------------------------|
| **P0** | **Corpus coverage scoring** across all dossiers → which fields pass public gate | A1–A8 public facets; D9 | **Coverage & field promotion** agent |
| **P0** | **Verification queues** wiring NDI / NV claims into actionable Admin worklists | B2–B3; portal trust | **Verification queue** skill (after research waves) |
| **P1** | **Entity resolution** — dedupe `agent` / `contact` / developer aliases across properties | C3–C4; B6; Plus CRM | **Entity resolution / party graph** |
| **P1** | **Document intelligence** — brochure/PDF floor plans, payment schedules, disclaimers | A9; C1–C2 depth; size tags | **Document intelligence** |
| **P1** | **Public price policy implementation** — never emit single `price_from` when NDI or multi-band | A4 trust | Product rule already locked; coverage agent + API projection |
| **P2** | Construction progress coverage analysis (candidate → public?) | C5 / A progress facet | Coverage agent + more developer trackers |
| **P2** | Independent **QA audit** of dossiers vs retained URLs | Method drift | **QA audit** skill |
| **P2** | Contact public vs Plus projections (**#7 LOCKED**) | A11 vs C4 | Implement display projections |
| **P2** | Typology-linked `listing` seed (**2B LOCKED**) | A14 / D10 | Retained-URL listings only |
| **P2** | Ready cards on Plus/Admin (**8B LOCKED**) | C11 | Badge + no auto-dossier |
| **P2** | Bathrooms hygiene (#5 LOCKED) | A3 | **Done 2026-10-17:** 2/180 filled (Kings Summit=2; 48 Treehouse=5 NV); chase on future dossiers |
| **P3** | Full unit classifieds on public | — | Deferred to Ready/resale slice |
| **P3** | Saved search / accounts / enquiry CRM | A13, C8 | Out of v1 data layer |
| **P3** | Simplify dual co_developer+RelatedParty | D6 ops complexity | After ≥N co-named patterns (M11) |

### Explicit non-gaps (already locked in data layer)

- Claim store with confidence + dual `needs_*` flags  
- Multi `price_observation` (never collapse)  
- Payment must-have threshold (≥4 agents **or** any developer)  
- Exposure tiers `public` \| `admin` \| `plus`  
- marketing_partner vs GroupCompany discipline  

---

## Feature scopes ↔ Rightmove-class amenity filters

Today we store free-text `amenities.core`. Planned catalog (`feature` / `property_feature` / `unit_type_feature` — [feature-taxonomy skill](../agents/feature-taxonomy.md), decisions 2026-10-16) scopes filters the way major listing sites split **scheme amenities** vs **in-unit features**:

| Our scope | Maps from (industry pattern) | Typical filters / facets | Surface |
|-----------|------------------------------|--------------------------|---------|
| **`development`** | Rightmove “key features” / development brochure amenities; Bayut/Property Finder building amenities | Gym, pool, lifts, CCTV, borehole, backup power, parking levels, concierge | **`public`†** facets + development page |
| **`apartment`** | Unit key features / floor-plan callouts | Balcony, fitted kitchen, ensuite, loft, DSQ, smart locks | **`public`†** when on canonical `unit_type`; else Plus/Admin + NV |
| **`house`** | House/villa feature checklists (future asset mix) | Garden, garage, servant quarter, compound wall | Deferred for off-plan apartment-heavy corpus; same catalog |
| **`community`** | Estate / master-plan / “lifestyle” facets | Co-working, padel, sauna, retail podium, kids club, shared gardens | **`public`†** when developer-sourced; often overlaps development |

**Product rules (unchanged):** synonym-normalize into controlled slugs; **developer-agreed → canonical / public gate**; agent-only extras stay **shown** with **`needs_verification`** on Admin/Plus — never invent facets from marketing inflation. Schema **v0.1.5** / M12 merged (`feature` / `property_feature` / `unit_type_feature`); A8 still keeps free-text `amenities.core` claims additive until Coverage retires them.

---

## Surface → API projection sketch (non-binding)

| Surface view | Reads | Filters out |
|--------------|-------|-------------|
| `v_public_development` | Canonical claims + gated fields + developer CTA contacts (+ baths when sourced) | confidence scores; NDI scalars; NV typologies as facts; full agent mobiles (#7) |
| `v_admin_property_workbench` | All claims, conflicts, sources, research_pass, flags | nothing material |
| `v_plus_commercial` | Multi prices, payment_plan_claim, progress, agent+contact graph, badged NV | seed-CSV internal notes (optional) |

---

## Roadmap alignment

1. Finish research waves → fill corpus.  
2. **Coverage & field promotion** → lock first public field set.  
3. **Verification queue** → burn down NDI/NV.  
4. **Party graph dedupe** + **document intel** → Plus depth.  
5. Consumer `listing` entity only after development master is trustworthy.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-10-16 | v0.1.1 — note: Rightmove-class amenity filters → development / apartment / house / community scopes |
| 2026-10-16 | v0.1.0 — initial surface map from schema 0.1.2 + goal/decisions locks |
