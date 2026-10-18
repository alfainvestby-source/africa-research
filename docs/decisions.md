# Decisions log

Living record of product and research locks. Newest at bottom within each section.  
Related: [goal and approach](goal-and-approach.md) · [project context](project-context.md) · [learning loop](learning-loop.md) · [master data schema](master-data-schema.md) · [DB model](db/README.md)

---

## Goal (locked)

Build a **world-class Kenya property product** in the class of **Rightmove / Rightmove Admin / Rightmove Plus**, starting with a **strong data layer**: trustworthy master data for Nairobi off-plan / new developments. **No AI-invented facts** — every claim is sourced and checked. Collection and organization use **professional, well-calculated** decisions for that product goal.

Plain-language write-up: [goal-and-approach.md](goal-and-approach.md)

| Date | Decision |
|------|----------|
| 2026-10-16 | Product north star = Rightmove-class public + Admin + Plus; data layer is the critical path |
| 2026-10-16 | User confirmed direction — proceed to scale (~half remaining seed) with locked method |

---

## Process

| Date | Decision |
|------|----------|
| 2026-10-15 | Learning loop: pilot 1–2 → review → +2 → review + retrofit → ~half remainder → rest |
| 2026-10-15 | Must-have fields **emerge from analysis**; living list with **consensus** counts |
| 2026-10-15 | Split parallel agents per project when independent; one agent if shared messy identity |
| 2026-10-15 | Live web fetch allowed for research (no extra permission) |
| 2026-10-16 | Standing **Proptech DB steward** owns evolving relational model under `docs/db/` |
| 2026-10-16 | Document all decisions in markdown as we go (this file + linked docs) |
| 2026-10-16 | Coordinator **proactively proposes new agents** as the Rightmove-class goal needs them — roster in [agent-roster.md](agent-roster.md) |
| 2026-10-16 | “New agents” means **new skills** (coverage, product mapping, dedupe, PDF intel, verification queue, QA) — not only more research clones |
| 2026-10-16 | Features are a **taxonomy**, not free text only — scopes include **development**, **apartment**, **house**, **community** (e.g. co-working, padel, sauna, balcony, DSQ); normalize synonyms; agent-only stays `needs_verification` |
| 2026-10-16 | Feature taxonomy takes **inspiration from listing-site patterns** (Bayut/PF building vs in-unit; Rightmove/Zoopla facet vs detail; Kenya chips like generator/borehole/DSQ) — structure only; **no invented** project features |
| 2026-10-16 | Feature taxonomy **inspired by major listing sites** + proptech best practice (Rightmove-class filters/key features, regional portal facets); adapt for Kenya off-plan; never invent project features |
| 2026-10-16 | **Majengo2** = the user’s **Cursor Project** (our sibling product), **not** majengo.co.ke |
| 2026-10-16 | **Do not research majengo.co.ke** — discard that false lead; intel target is the Cursor Majengo2 app/filters |
| 2026-10-16 | Proposed **listing + agent-analytics skill pack** (payment normalizer, entity resolution, PSF comps, risk scorer, inventory, PDF intel, etc.) — see [proposed-listing-analytics-skills.md](agents/proposed-listing-analytics-skills.md) |
| 2026-10-16 | **Geo enrichment allowed:** Google Maps / Places (or OSM/Nominatim/Mapbox) for GPS + proximity — prefer developer/NEMA coords; geocodes tagged `geo_method` + lower confidence; never invent pins ([geo-poi-enricher](agents/geo-poi-enricher.md)) |
| 2026-10-16 | **Geo corpus pass done:** `geo_pin` + optional `poi`/`property_poi` in schema **0.1.13**; `properties.lat/lng` only conf ≥4; reject Airport-as-pin and implausible Longines JSON-LD; coverage **26/27** pinned ([geo-enrichment.md](db/geo-enrichment.md)) |
| 2026-10-16 | **Discovery geography = all Kenya** (not Nairobi-only); researched dossiers remain Nairobi-first until we batch-expand |
| 2026-10-16 | Agents need **person-level** fields (first_name, last_name, phone, email, web, notes) plus **listing↔agent** relations — not only agency↔development (`property_agent`) |
| 2026-10-16 | Opened discovery research batch of **10** (5 Nairobi + 5 new geography) from [kenya-offplan-leads.md](discovery/kenya-offplan-leads.md) |

---

## Provenance & confidence

| Date | Decision |
|------|----------|
| 2026-10-15 | Confidence 0–5 stored on claims for **model/QA only** — not shown on public portal initially |
| 2026-10-15 | Developer/official outweighs agents; agent-only consensus caps at conf 3 without official corroboration |
| 2026-10-15 | Scan ~**10** sources; retain ≥**5** densest; **always keep** developer/official site (+ official PDF) |
| 2026-10-15 | Skip thin/low-info pages early unless only conflict evidence |
| 2026-10-15 | Show source **counts** on master index; full URLs in each dossier Sources section |
| 2026-10-15 | CSV developer / sales_contact / price = **unverified leads** only |
| 2026-10-16 | **Hauzisha `0730 731 355` / `+254 730 731 355` = portal CTA only** (`agent-hauzisha` / `ct-hauzisha-phone`) — **never** attribute as developer sales phone. Same class as Block/CSV agent contacts. Developer inventory: [db/hauzisha-developers.md](db/hauzisha-developers.md) · [seed/developers_hauzisha_leads.csv](db/seed/developers_hauzisha_leads.csv) |
| 2026-10-16 | **Hauzisha / similar portal development exports = lead lists** — not dossier authority. Non-Ready rows are checked/verified into the discovery/research queue. |
| 2026-10-16 | **`inventory_class`** = `off_plan` \| `building` \| `ready` \| `resale` on **`listing` and `property`** (schema **v0.1.14**). Prefer over a separate raw-import table. `listing.property_id` may be **NULL** for orphan Ready unit ads. |
| 2026-10-16 | **Ready mark (both levels):** Ready **unit ads** and fully Ready/handed-over **developments** → `inventory_class=ready`. **Stored but never dossiered for now.** Optional future Ready research = backlog only ([gap-backlog.md](product/gap-backlog.md) O1) — do not implement now. |
| 2026-10-16 | **Research queue in scope:** `off_plan` + `building`. **Coming soon** hubs → **`off_plan`** (no separate `coming_soon` enum) and stay **in scope** for discovery / product readiness review — not held indefinitely. |
| 2026-10-16 | **Ready only when tagged** — never invent Ready from “N units for sale”. Developments-only for dossiers; unit ads = listings. **Block.ke** low-trust. See [db/hauzisha-developers.md](db/hauzisha-developers.md). |

---

## Conflict & canonical rules

| Date | Decision |
|------|----------|
| 2026-10-15 | Always **highlight** conflicts; never silently pick a winner among equals |
| 2026-10-15 | **Developer vs agents:** if developer known and developer sources **agree** → canonical = developer; agents secondary |
| 2026-10-16 | **Official vs official** (developer pages disagree): **do not assume** → flag **`needs_developer_input`**; resolve in later verification passes |
| 2026-10-15 | Low-confidence / agent-only / uncorroborated (sold-out, typology not elsewhere): **show** + **`needs_verification`** |
| 2026-10-15 | Unproven brand/parent overlap (e.g. Laureland↔Wimax) → **`marketing_partner`**, not GroupCompany |
| 2026-10-16 | Co-named “Developers” (e.g. Rendeavour + Tatu City Limited) → model as **both** `co_developer` and RelatedParty; propose simplify later |

---

## Fields & portal promotion

| Date | Decision |
|------|----------|
| 2026-10-15 | Payment plan must-have if ≥**4** independent agent/portal sources agree **or** any developer source |
| 2026-10-15 | Prices as **`price_claims[]`** (multi), not a single forced scalar |
| 2026-10-16 | Portal public columns later = fields with **high confidence AND high coverage** across listings (~½ missing → not public) |
| 2026-10-16 | **Coverage pass (n=11):** public shortlist = name, neighbourhood geo, primary developer (conf≥4), developer amenities, canonical unit types + sizes, status summary, completion when not NDI, payment when threshold stable; keep `price_from`, GPS, progress %, unit/storey/block scalars, party-graph extras **off public** — see [db/field-promotion.md](db/field-promotion.md) |
| 2026-10-16 | **construction_progress:** store when developer publishes (claim set if conflict); candidate field; coverage-gated for portal |
| 2026-10-15 | Tag size **gross vs plinth** when materials distinguish |
| 2026-10-15 | Agents + contacts are **relational entities** linked to properties (not buried only in project blobs) |
| 2026-10-15 | Optional GroupCompany above developer; stakeholders (financing, contractor, architect, etc.) when named |

---

## Entity model direction

| Date | Decision |
|------|----------|
| 2026-10-15 | Relational graph: Property, Developer, GroupCompany, RelatedParty, Agent, Contact, Stakeholder, Source, Claim |
| 2026-10-15 | Store agent WhatsApp/phones in master DB (pro/relational layer); public display rules later |
| 2026-10-16 | DB steward continuously updates schema, seed extracts, ER notes, changelog from dossiers |
| 2026-10-16 | Schema **v0.1.1** encodes dual co_developer+RelatedParty, `needs_developer_input`, multi prices, progress candidate |
| 2026-10-16 | Schema **v0.1.2**: field exposure intent `public` \| `admin` \| `plus`; public gated; Admin/Plus retain conflicts + needs_* + agent graphs |
| 2026-10-16 | Schema **v0.1.5**: `feature` / `property_feature` / `unit_type_feature`; scopes development\|apartment\|house\|community |
| 2026-10-16 | Wave C complete: **17/17** dossiers seeded ([corpus-rollup.md](db/seed/corpus-rollup.md)); Polaris has no developer; Own It never promoted to developer |
| 2026-10-16 | Schema **v0.1.9**: `agent_person` (first/last/notes) + `listing`/`listing_agent`; contacts stay phone/email/web; `property_agent` kept; **no invented people** |
| 2026-10-16 | National ID prefixes **NAK/MSA/ELD** + discovery **DISC-***; corpus **22** properties ([corpus-rollup.md](db/seed/corpus-rollup.md)) |
| 2026-10-16 | Product surface map v0.1: [product/surface-map.md](product/surface-map.md) — Rightmove/Admin/Plus capabilities → schema tiers; P0 gaps = coverage scoring + verification queues |
| 2026-10-16 | Schema **v0.1.13**: `geo_pin` + `geo_method` + optional `poi`/`property_poi`; corpus GPS **26/27** ([geo-enrichment.md](db/geo-enrichment.md)) |
| 2026-10-16 | Schema **v0.1.14**: `inventory_class` on `listing` + `property`; nullable `listing.property_id` for orphan Ready ads; Coming soon → `off_plan` |
| 2026-10-17 | **Hauzisha Wave B seed (0.1.17):** DISC-NBO-019…023 → corpus **39**; all `inventory_class=building`; Only You `primary_developer` **null** + Onlyou Investments / GLBC marketing RelatedParties; Wonder shared Gaia+Diplomat; AYA Whitehorse primary / Sandoral NDI never primary; **never** `0730`; Gemini Hub held ([corpus-rollup.md](db/seed/corpus-rollup.md)) |
| 2026-10-17 | **Product focus (Zoopla→Kenya #1 LOCKED):** research + public v1 = **new developments / off-plan** (`off_plan` + `building`); schema/product must keep **Ready + resale easy to add later** (`inventory_class` + `listing` already). Decisions memo: [zoopla-kenya-product-decisions.md](product/zoopla-kenya-product-decisions.md) |
| 2026-10-17 | **Hauzisha Slice C seed (0.1.18):** DISC-NBO-024…030 → corpus **46**; Montbleu primary **null**; Atreus = EIA Atreus Ventures (Sunmon/Lesto RP only); GP+Rosewood Coming soon→`off_plan` with Ready lean NDI; never `0730` |
| 2026-10-17 | **Zoopla→Kenya #2 LOCKED (2B):** public = **development-first**; typology-linked `listing` snapshots from **retained URLs only**; no invented flat IDs. Evidence: [zillow-rightmove-model-study.md](product/zillow-rightmove-model-study.md). Memo: [zoopla-kenya-product-decisions.md](product/zoopla-kenya-product-decisions.md) |
| 2026-10-17 | **Zoopla→Kenya #3 LOCKED:** Kenya energy/utilities vocab = generator, borehole, solar, fibre, security — **no UK EPC chase**; named green certs only if developer publishes |
| 2026-10-17 | **Zoopla→Kenya #4 LOCKED:** buyer costs = **site-wide guide**; per-project only when developer publishes; **service charge** extract-when-found |
| 2026-10-17 | **Zoopla→Kenya #5 LOCKED:** `unit_type.bathrooms` first-class card attribute (with beds/size) à la Zoopla/Zillow/Rightmove; fill when sourced; **never invent**; skip UK receptions as must-have |
| 2026-10-18 | **Public hero price:** **From X** when agreed floor; **X–Y** when multi trustworthy claims without official-vs-official fight (RM ADF min/max); **POA** when NDI/thin — never silent single NDI pick. Plus/Admin keep full `price_observation` table. [db-quality-locks](../internal/db-quality-locks-2026-10-18.md) |
| 2026-10-18 | **Bathrooms two grains:** `unit_type.bathrooms` (typology) + development range min–max (derived for filters). Explicit source only. |
| 2026-10-18 | **Map absolute necessity:** always show public location; online tools first (developer/EIA/Google/OSM); exact vs **Approximate** vs **Area only** by conf; physical geolocate if online fails. |
| 2026-10-18 | **Public field gate:** ≥**70%** corpus fill **and** developer/official **or** ≥2 independent agents; no single-agent AI gap-fill. Weak developer (conf&lt;4) stays admin-only. CSV seeds until UI ship. |
| 2026-10-18 | **Coverage pass (n=51):** seed **007–011** + `inventory_class` backfill complete; PASS identity/geo/IC/map-any/units/prices/payments; FAIL bathrooms exact GPS progress (do not invent). Hero **From/X–Y/POA**. Report: [db-coverage-pass-2026-10-18.md](../internal/db-coverage-pass-2026-10-18.md) · changelog **0.1.20** |
| 2026-10-18 | **Card facets (0.1.21):** soft columns on `property` for type, beds/size range, hero From\|X–Y\|POA, deposit when must-have, summary, map_tier, street; geo harvest → **51/51** mapped; utility chips + media seed. Report: [property-card-facets-harvest-report-2026-10-18.md](../internal/property-card-facets-harvest-report-2026-10-18.md) |
| 2026-10-18 | **Pandora Residences (0.1.25):** official URL **https://pandora.co.ke/**; Maps CID `12900601372674958277` → **−1.260829, 36.780513** (place Pandora / Muthangari Dr, conf 4 on property row). Report: [pandora-official-url-maps-cid-2026-10-18.md](../internal/pandora-official-url-maps-cid-2026-10-18.md) |
| 2026-10-17 | **Zoopla→Kenya #6 LOCKED:** claim key `tenure` (freehold \| leasehold \| sectional_title); **Admin/Plus** when found; **public** only conf ≥4 official |
| 2026-10-17 | **Zoopla→Kenya #7 LOCKED:** full agent phones/WhatsApp = **Plus only**; public CTA = developer/project ownership-tagged contacts |
| 2026-10-17 | **Zoopla→Kenya #8 LOCKED (8B):** Plus + Admin may show Ready unit cards (**not research-verified** badge); public stays off-plan/UC; **no auto-dossiers** for Ready |

---

## Open / pending

| Item | Status |
|------|--------|
| Goal / Rightmove-class framing | **Confirmed** 2026-10-16 |
| Half-batch research (~6–7 of 13 remaining) | In progress |
| Later verification passes for `needs_developer_input` items | After main research waves |
| Portal field set finalization (public vs Admin vs Plus) | **Scoreboard done** 2026-10-16 ([field-promotion.md](db/field-promotion.md)); CSV `is_portal_field` flips + surface mapping still open |
