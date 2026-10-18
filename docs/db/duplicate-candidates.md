# Duplicate / relist candidates — corpus cross-reference

**Date:** 2026-10-18  
**Pass:** Hauzisha import / corpus DB quality (property-level ER)  
**Script:** [`../../internal/duplicate-relist-detect-2026-10-18.py`](../../internal/duplicate-relist-detect-2026-10-18.py)  
**Seed CSV:** [`seed/duplicate_candidates.csv`](seed/duplicate_candidates.csv)  
**Related:** [entity-resolution.md](entity-resolution.md) · portal inventory rules · Block.ke low-trust · Hauzisha `0730` phone lock  

**No auto-merge.** Conservative scoring. No invented property facts.

---

## Universe

| Source | n | Role |
|--------|--:|------|
| Seeded `properties.csv` | **51** | Research corpus (canonical) |
| `listings_hauzisha_inventory_leads.csv` | **128** | Hauzisha development cards (0 pre-linked `property_id`) |
| `developers_hauzisha_leads.csv` | 51 | Developer directory only (not pair-scored as listings) |
| `internal/nairobi_off_plan_projects.csv` | **17** | Early CSV leads (NBO-001…017) |
| `internal/block-ke-offplan-developments.csv` | **220** | Block.ke titles — **low-trust** |

---

## Method

| Signal | Weight / use |
|--------|----------------|
| Fuzzy name + aliases (`SequenceMatcher` + token Jaccard) | Primary (~55%) |
| Developer name / `developer_id` match | +20% when present |
| Neighbourhood / street / area text | +20% when present |
| Geo proximity (recommended `geo_pin` or property lat/lng) | ≤150m strong; ≤400m medium; \>5km penalty |
| Same `external_id` / URL | Strong boost |
| Unit-mix / price fingerprint | Soft only (≤5%) — never decisive |
| Known anti-merge / phase labels | Force `false_positive` or `related_phase` |

**Actions**

| Action | Meaning |
|--------|---------|
| `same_property` | High/medium confidence link — **propose** filling `property_id` on lead; do not delete rows |
| `related_phase` | Same brand stem, different phase (I/II, Marina 2/3, Sunpark I/II) |
| `needs_human` | Plausible but weak / Block.ke / ambiguous |
| `false_positive` | Shared developer or corridor — **do not merge** (documented anti-merge) |

---

## Counts (this pass)

| Metric | n |
|--------|--:|
| Candidate pairs emitted | **127** |
| Clusters (union on medium+ links) | **37** |
| `same_property` | **38** |
| `related_phase` | **11** |
| `needs_human` | **65** |
| `false_positive` | **13** |

### By pair kind

| Kind | n |
|------|--:|
| property ↔ hauzisha_lead | 49 |
| property ↔ block_lead | 33 |
| hauzisha_lead ↔ hauzisha_lead | 19 |
| property ↔ nairobi_csv | 19 |
| property ↔ property | 7 |

**Likely dupes / relists to link:** ~**21** Hauzisha lead↔property `same_property` pairs covering **~20** seeded properties (+ **17** nairobi_csv identity matches).  
**Possible relists (portal):** hauzisha↔hauzisha near-dup names → mostly `needs_human`.  
**False-positive examples:** Porini↔Jabali; Elegant siblings; Oasis “* One Residency”; Riara Oasis↔Plumeria; Alina Valley↔Harbour.

---

## A. `same_property` — propose link (no auto-merge)

### A1. Seeded property ↔ Nairobi CSV (expected identity)

All **17** NBO CSV rows match their seeded `external_id` / name (score ≥0.9). Action: treat CSV as **lead archive**, property row canonical. SkyPeak-on-Golden CSV developer remains **false primary** (see party ER).

### A2. Seeded property ↔ Hauzisha inventory lead (propose `property_id`)

| Seeded property | Hauzisha lead name | Conf | Notes |
|-----------------|--------------------|------|-------|
| Pandora Residences | Pandora | high | A-One + Westlands |
| Diamond Bay Residences | Diamond Bay Residences | high | Henbon |
| Golfscape Residences | Golfscape Residences | high | WH Harmony |
| Forestview Residences | Forestview Residences | high | Elegant |
| Donyo Hill Residences | Donyo Hill Residences | high | Elegant |
| 48 Treehouse | 48 Treehouse | high | Elegant |
| Citrine Heights | Citrine Heights | high | Jafu |
| Auris Residence | Auris Residence | high | Jafu |
| Serene Manor | Serene Manor | high | Jafu |
| Rhapta One Residency | Rhapta One Residency | high | Oasis |
| Galaxy ONE | Galaxy One | high | Lionston |
| Capricorn | Capricon *(typo)* | high | Staroot — alias inbound |
| Libra Residences | Libra Residences | high | GLBC |
| Diplomat Residences | Diplomat Residencies | high | Wonder spelling |
| 237 Lulu | 237 Lulu Garden City / 237 Garden City | high | Mi Vida |
| Balkis Residences | Balkis Residences Riverside | high | Sunmon lead face |
| Alba Apartments | Alba Apartments | medium | Nanchang |
| Gemini Residency Phase 2 | Gemini 2 | medium | Staroot |
| Gaia Brookside | Gaia Brookside | medium | Wonder |
| Alina Valley | Alina Valley | medium | Wonder |

**Not auto-filled:** `listings_hauzisha_inventory_leads.csv` `property_id` still blank until user confirms.

---

## B. `related_phase` — do not collapse

| Pair | Why |
|------|-----|
| Sunpark Residence **II** (seeded) ↔ Sunpark Residences / Phase **I** (Hauzisha) | Ready I skipped; II researched |
| Marina Bay **Phase 2** (seeded) ↔ Marina Bay 2 / 3 / Phase 3 leads | Phase siblings; Phase 1 Ready anti-merge |
| Gemini Phase **2** (seeded) ↔ Gemini I / Gemini Residency leads | Phase siblings |
| Gemini Hub ↔ Phase 2 | **Held** research skip — `needs_human`, not merge |

---

## C. `false_positive` — keep separate

| Pair | Why |
|------|-----|
| Porini Point ↔ Jabali Towers | Same `dev-rendeavour` / Tatu family — different products |
| Forestview ↔ Donyo Hill ↔ 48 Treehouse | Elegant multi-site — different parcels |
| Citrine ↔ Auris (and Serene) | Jafu Wave A — different projects |
| Riara Oasis ↔ Plumeria | “Riara *” naming + soft geo — different SPVs |
| Gemini P2 ↔ Capricorn | Shared Staroot — different assets |
| Galaxy ONE ↔ Rhapta One | Rhapta corridor proximity only |
| Alina Valley ↔ Alina Harbour | Wonder Alina family — dossier anti-merge |
| Rhapta One ↔ Forest/Brookside/Riverside One Residency | Oasis “* One Residency” naming pattern |

---

## D. `needs_human` highlights

- **Block.ke** title matches (33): never auto-link; Block low-trust.  
- **Hauzisha↔Hauzisha** near-duplicate development cards (19): possible portal relists / export dups.  
- **Gemini Hub** vs Phase 2: confirm hold.  
- Cross-seed vague Westlands + shared developer without strong name.  
- Plumeria ↔ Polaris CSV cross-hit (weak) — ignore unless stronger evidence.

---

## Proposed merge / link rules (for entity-resolution)

1. **Lead → property link** only when `same_property` **high** (name ≥0.93 + developer or place), or medium with exact Hauzisha development title.  
2. Fill `listings_hauzisha_inventory_leads.property_id` on confirm — **do not** delete lead rows.  
3. **Never merge** seeded property↔property without human review (researched dossiers are already distinct).  
4. Phase / Ready siblings → `related_phase` or inventory_class distinction — never collapse I↔II.  
5. Block.ke matches → max `needs_human`; never sole authority.  
6. Typo aliases (`Capricon`→Capricorn) → add to `property_aliases.csv` when linking.  
7. Hauzisha `0730 731 355` remains portal CTA — linking a lead does **not** attach that phone to the developer.

---

## Steward checklist

- [x] Confirm A2 **high + multi-signal** → write `property_id` on matching Hauzisha lead rows (**2026-10-18 apply**)  
- [x] Add alias `Capricon` → `prop-capricorn-kilimani`  
- [ ] Leave Sunpark I / Marina 1 / Gemini Hub unseeded as today  
- [ ] Optional second pass: OCR/agent-overlay media ER (separate from property ER)  
- [ ] Review medium skips (Alba, Gemini 2, Gaia, Alina Valley) if user wants a second link wave  

---

## Apply log — `property_id` fill (2026-10-18)

**Filter (exact):** keep only pairs where **all** of:
1. `recommended_action == same_property`
2. `confidence == high`
3. pair kind = `property` ↔ `hauzisha_lead`
4. **≥2 independent signals** from match reasons, and at least one of `{developer, place, id_url}` (name alone never enough)

**Applied:** **17** Hauzisha inventory lead rows → `property_id` (16 distinct properties; 237 Lulu got **2** lead names).  
**Skipped:**
- medium `same_property` (4): Alba, Gemini 2, Gaia Brookside, Alina Valley  
- all `needs_human` / `related_phase` / `false_positive`  
- nairobi_csv identity pairs (archive only — not Hauzisha `property_id`)  
- phases (Sunpark I/II, Marina 2/3, Gemini I/II)  

**No property↔property merges.** Linking only.

| Lead `development_name` | → `property_id` | external_id | Signals |
|-------------------------|-----------------|-------------|---------|
| Pandora | prop-pandora-residences | NBO-002 | name+developer+place |
| Diamond Bay Residences | prop-diamond-bay-residences | NBO-007 | name+developer+place |
| Golfscape Residences | prop-golfscape-residences | NBO-006 | name+developer+place |
| Galaxy One | prop-galaxy-one | NBO-013 | name+developer+place |
| Forestview Residences | prop-forestview-residences | DISC-NBO-012 | name+developer+place |
| Donyo Hill Residences | prop-donyo-hill-residences | DISC-NBO-013 | name+developer+place |
| 48 Treehouse | prop-48-treehouse | DISC-NBO-014 | name+developer+place |
| Citrine Heights | prop-citrine-heights | DISC-NBO-016 | name+developer+place |
| Auris Residence | prop-auris-residence | DISC-NBO-017 | name+developer+place |
| Serene Manor | prop-serene-manor | DISC-NBO-018 | name+developer+place |
| Libra Residences | prop-libra-residences | DISC-NBO-019 | name+developer+place |
| Diplomat Residencies | prop-diplomat-residencies | DISC-NBO-022 | name+developer+place |
| Rhapta One Residency | prop-rhapta-one | DISC-NBO-024 | name+developer+place |
| Capricon | prop-capricorn-kilimani | DISC-CAPRICORN | name+developer+place |
| Balkis Residences Riverside | prop-balkis-residences | DISC-NBO-010 | name+developer+place |
| 237 Lulu Garden City | prop-237-lulu | DISC-NBO-007 | name+developer+place |
| 237 Garden City | prop-237-lulu | DISC-NBO-007 | name+developer+place |

Machine log: [`../../internal/property-id-link-apply-2026-10-18.csv`](../../internal/property-id-link-apply-2026-10-18.csv)

---

## Changelog hook

DB model **0.1.23** detection · **0.1.24** apply — see [changelog.md](changelog.md).
