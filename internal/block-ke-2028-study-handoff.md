---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Handoff — Block.ke 2028-only study + listing pull

**User asks:** (1) study Completion=2028 only from Block CSV; (2) pull listing data via WP API; (3) **treat Block with care** — site looks AI-generated, project URLs may attach unrelated / regular listings, low-quality relations.

## Trust + scope rules (locked)

1. **Product entity = new developments / projects**, not apartment or house listings.  
2. **Block.ke = low-trust development-name lead index only.** Do not write Block-only facts into dossiers at conf ≥3. Prefer developer / NEMA / named primary agents.  
3. Block tag density ranks **which development names to research next**, not truth and not inventory.  
4. **Do not ingest** Block `estate_property` unit/apartment/house posts as deliverables. Raw pull stays forensics only.  
5. **Unit-type** fields (beds, sqm, from-price, payment) only if they describe types inside a named development **and** are corroborated by **multiple independent sources** — never Block alone.

Evidence supporting caution: hub HTML chrome reused across projects; empty public `acf`; templated boilerplate; junk micro-prices; area tag collisions; title-token mismatches. Audit: `internal/block-2028-quality-audit.json`.

## Deliverables

| Path | Change |
|------|--------|
| `docs/discovery/block-ke-2028-study.md` | Study + **Trust posture** section |
| `docs/discovery/kenya-offplan-leads.md` | Cross-link (low-trust note) |
| `internal/block-ke-2028-only.csv` | 74 exact-2028 rows |
| `internal/block-2028-listings-full.csv` | 219 tagged listings, flat parsed fields (**raw**) |
| `internal/block-2028-listings-full.json` | Full REST + content HTML (**raw**, ~4.5MB) |
| `internal/block-2028-quality-audit.json` | Contamination / boilerplate flags |
| `internal/block-2028-api-enrichment.json` | Lighter sample |
| `internal/block-2028-sample.json` | Contaminated HTML scrape — do not use |
| `internal/block-ke-offplan-developments.csv` | Source copy |

## Counts

- 74 / 220 exact-2028 projects; 219 REST listings pulled (0 fetch errors)
- 6 corpus name overlaps; 4 discovery-prior; 7 near-misses; 57 brand-new
- Parse coverage (still unverified): price~204/219, size~196/219, beds~216/219 — **coverage ≠ accuracy**

## Process-rerun batch (follow-up)

User asked which Block ideas are reliable enough to process like other dossiers with additional sources.

**Deliverable:** `docs/discovery/block-2028-process-rerun-batch.md`

**Tier A (yes):** 237 Lulu (Mi Vida), Jabali Towers (Tatu), Highpoint 336 (microsite), Balkis (Sunmon agents), Hephé Palace, AYA, Gamil Heights, KEZA Riruta Ph2 (Mi Vida), Amber Bay, Cambridge Garden, Morvara, Seasons Riverside, Chestnut City (Nanyuki). Plus Ivy Park / Gaia / Enaki already on national leads.

**Wave 1 DONE (2026-10-16):** dossiers `docs/projects/237-lulu.md` (DISC-NBO-007), `jabali-towers.md` (DISC-NBO-009), `highpoint-336.md` (DISC-NBO-008). Index updated.

**Hold:** Karura Forest Views (no independent project — likely Block alias), Stellar Bay dupes, near-misses, thin L≤4 names.

## API note

`GET /wp-json/wp/v2/estate_property?property_project={term_id}&_embed=1` — taxonomies + featured media embed OK; price meta not in REST; fields parsed from prose. Geo in page JSON-LD only — **not imported**.

## Product-readiness skills proposal (follow-up)

User goal: review data quality/gaps for Kenya Rightmove + Pro/Plus hub. Spec: `docs/agents/product-readiness-reviewer.md` (new agent skill pack; roster updated).
