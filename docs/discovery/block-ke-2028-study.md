# Block.ke off-plan study — Completion = **2028** only

**Pass date:** 2026-10-16  
**Source CSV:** [block-ke-offplan-developments.csv](../../internal/block-ke-offplan-developments.csv) (220 rows; columns `Completion,Title,URL,Listings`)  
**Filter:** `Completion == "2028"` **exact** — excludes `2027 / 2028`, `2029+`, and other buckets  
**Filtered + enriched table:** [block-ke-2028-only.csv](../../internal/block-ke-2028-only.csv)  
**API enrichment dump:** [block-2028-api-enrichment.json](../../internal/block-2028-api-enrichment.json)  
**Full listing pull:** [block-2028-listings-full.csv](../../internal/block-2028-listings-full.csv) · [block-2028-listings-full.json](../../internal/block-2028-listings-full.json)  
**Quality audit:** [block-2028-quality-audit.json](../../internal/block-2028-quality-audit.json)  
**Corpus baseline:** 27 project dossiers under [docs/projects/](../projects/) · discovery leads [kenya-offplan-leads.md](kenya-offplan-leads.md)

---

## Scope lock — **developments, not apartment/house listings**

**In scope now:** new **developments / projects** (off-plan or under construction named schemes). **Coming soon** hubs stay in the review queue (map to `off_plan`).

**Out of scope now:** standalone apartment or house **listings**, resale ads, rental ads, Block `estate_property` unit posts as deliverables, and **Ready**-tagged unit ads / handed-over whole developments (store/mark only — **no dossier**). See [portal-inventory-class-research-rules.md](portal-inventory-class-research-rules.md).

**Unit-level data (beds, sizes, from-prices, payment):** optional later, and only when:

1. It describes **unit types inside a named development** (not a one-off listing), and  
2. Quality is reliable, and  
3. The same claim is corroborated by **multiple independent sources** (e.g. developer microsite + brochure/EIA + ≥1 serious agent) — **never Block alone**.

Block’s WP “listings” under a project tag are mostly AI/agent unit posts. Keep the raw pull for forensics / density ranking only — **do not** ingest them as inventory rows or portal listings.

---

## Trust posture — **treat Block as low-quality / non-authoritative**

Block.ke is treated as a **noisy development-name lead index**, not a source of truth. Working conclusion: much of the site looks **AI-generated / templated**, with weak entity hygiene.

| Risk | What we saw |
|------|-------------|
| Unrelated listings under a project URL | HTML hubs show **site-wide unrelated cards** (same Le Vert Riverside / warehouse cards on every project). Taxonomy-tagged posts are better than hub chrome but **still not guaranteed related**. |
| Low-quality copy | Heavy repeated boilerplate (“Verified by Block Real Estate”, “confirmed at the point of enquiry”, “Development at a Glance”) across dozens of listings. |
| Broken / junk prices | Parser + titles yield many **KES 100k–300k** “from” figures that are not credible sale prices (likely rent fragments, truncated “23.3M” → “23”, or garbage). |
| Bad relations / areas | e.g. Golden Mansion listing tagged **Industrial Area** alongside Westlands; title-token mismatches on some project buckets (Pandora, Hephe). |
| No developer / legal fields | Public WP REST `acf` is empty; price meta not exposed — only prose. |
| Geo | Coordinates appear in **page JSON-LD only**, not REST — and are unverified (do not import as GPS truth). |

**Rules for this corpus:**

1. Entity of record = **development**, not Block apartment/house posts.  
2. **Never** promote Block-only facts into a dossier as confidence ≥3 without a non-Block source (developer site, NEMA, named agent with primary materials).  
3. Use Block for **development name discovery + tag-density rank** only.  
4. Treat every Block price / area / bed / completion as **`needs_verification`** — and **do not** ship unit rows from Block.  
5. Do **not** merge entities on Block name similarity alone (see near-misses below).  
6. Listing pull files are **raw captures** — contaminated rows stay for audit; they are not cleaned truth and are **not** the product surface.

---

## Verdict

| Metric | Count |
|--------|------:|
| Exact-2028 Block projects | **74** |
| True corpus overlaps (name identity) | **6** |
| Already on discovery lead list (not corpus-merge) | **4** |
| Near-miss names (do **not** merge) | **7** |
| Brand-new to this store | **57** |
| Sum of `Listings` across 2028 projects | **218** |
| REST listings pulled under those projects | **219** |

**Method lock:** Prefer `estate_property?property_project={id}` over HTML hub cards. CSV `Listings` ≈ taxonomy `count`. That still only means “posts tagged with this term on Block,” **not** “verified units of this development.”

---

## Already in corpus (true overlaps)

| Block title | Listings | Dossier | Block areas (API) | Notes |
|-------------|--------:|---------|-------------------|-------|
| **Luna Oak Residency** | 5 | [luna-oak-residency.md](../projects/luna-oak-residency.md) | Westlands | Name match |
| **Golden Mansion** | 3 | [golden-mansion.md](../projects/golden-mansion.md) | Westlands *(+ contaminated Industrial Area tag on 1 listing)* | Name match only — **do not** trust Block area/price over dossier |
| **Pandora Residences** | 3 | [pandora-residences.md](../projects/pandora-residences.md) | Westlands | Name match |
| **Canto** | 2 | [canto.md](../projects/canto.md) | Westlands | Name match (DISC-NBO-001) |
| **Berkeley Homes Apartments** | 1 | [berkeley-homes.md](../projects/berkeley-homes.md) | Westlands | Name match |
| **Lesonia Residences** | 1 | [lesonia-residences.md](../projects/lesonia-residences.md) | Westlands | Name match |

**Not in this 2028 slice (for awareness):**

- **Brookside Oak Residency** is on Block as **`2029+`** (4 listings) — excluded by filter.
- **Ankori**, **Nouveau**, **Capricorn**, **Polaris** — not present in the Block CSV at all (Q4 2028 corpus completions come from other sources).

---

## Discovery-prior hits (do not treat as brand-new)

| Block title | Listings | Areas (API) | Prior note |
|-------------|--------:|-------------|------------|
| **Ivy Park Residences** | 5 | Kilimani | [kenya-offplan-leads](kenya-offplan-leads.md) — Ivy Park / Kirichwa / Ivy Group; Dec 2028 |
| **Gaia Brookside** | 4 | Brookside; Westlands | Same leads doc — ≠ Brookside Oak / ≠ Gemini |
| **Fountain Residency** | 3 | Kilimani | Same leads doc — thin |
| **Enaki Forestside** | 1 | Nyari | Same leads doc — HassConsult Forestside |

---

## Near-misses — **do not merge**

Auto-token matching would have wrongly folded these into existing dossiers. Curated as **new / separate**:

| Block title | Listings | Areas (API) | Why not merge |
|-------------|--------:|-------------|---------------|
| Golden Apple | 4 | Kilimani | Shares “Golden” only ≠ Golden Mansion |
| Kings Lotus | 4 | Ngong Road; Ongata Rongai | “Kings” brand token ≠ Kings Square Eldoret / Kings Summit Nakuru |
| Golden Hill | 3 | Kilimani | Shares “Golden” only ≠ Golden Mansion |
| Amethyst Springs Residences | 2 | Kileleshwa | ≠ Misty Springs |
| Avana Oasis | 2 | Westlands | “Oasis” only ≠ Riara Oasis |
| Kings Pinnacle | 1 | Upperhill | “Kings” only |
| Mogotio Oasis | 1 | Westlands | **Known false geo match** — ≠ Riara Oasis; do not merge |

---

## Geography (non-corpus 2028 rows)

From API `property_city` / `property_area` on tagged listings:

| City | Projects (approx.) |
|------|-------------------:|
| Nairobi | 58 |
| Kiambu (incl. Tatu City) | 6 |
| Nanyuki | 2 |
| Machakos | 2 |
| Kajiado | 1 |
| Mombasa | 1 |

**Top areas:** Westlands (32), Kilimani (12), Riverside (6), General Mathenge (5), Tatu City (3).

---

## Ranked pipeline — brand-new **developments**, Block tag count ≥ 5

Priority signal = **how many Block posts were tagged to the development name** — a weak popularity proxy only. **Not** verified unit inventory. Price snippets below are Block prose (often wrong); ignore for product until multi-source. Next step for each name: find developer / official materials, then open a **development dossier** — do not import Block unit posts.

| Rank | Project | L | Area(s) | Price snippets (titles) | Block hub |
|-----:|---------|--:|---------|-------------------------|-----------|
| 1 | **Balkis Residences** | 7 | Riverside; Westlands | (titles name 2–3 bed + DSQ; no KES in sampled titles) | [hub](https://block.ke/project/balkis-residences/) |
| 2 | **Gamil Heights** | 6 | General Mathenge; Westlands | penthouse / 4–5 bed duplex language | [hub](https://block.ke/project/gamil-heights/) |
| 3 | **Hephe Palace** | 6 | Westlands | 1–3 bed + DSQ language | [hub](https://block.ke/project/hephe-palace/) |
| 4 | **Karura Forest Views** | 6 | Peponi; Westlands | from **KES 17.03M** / **19.61M** / **28.51M** (3–5 bed) | [hub](https://block.ke/project/karura-forest-views/) |
| 5 | **237 Lulu Garden City** | 5 | Garden City | from **KES 6.3M / 8.5M / 12.5M** (1–3 bed) | [hub](https://block.ke/project/237-lulu-garden-city/) |
| 6 | **AYA Residence** | 5 | Kileleshwa | 2–4 bed + DSQ | [hub](https://block.ke/project/aya-residence/) |
| 7 | **Amber Bay Heights** | 5 | General Mathenge; Westlands | from **KES 8.18M / 16.16M / 21.5M** | [hub](https://block.ke/project/amber-bay-heights/) |
| 8 | **Cambridge Garden** | 5 | Kilimani (Kindaruma Rd in titles) | 1–3 bed | [hub](https://block.ke/project/cambridge-garden/) |
| 9 | **Chestnut City** | 5 | Nanyuki (**new geography**) | from **KES 4.8M / 8.9M / 13.5M** | [hub](https://block.ke/project/chestnut-city/) |
| 10 | **Highpoint 336 Residences** | 5 | Kilimani | 3 bed → 6 bed penthouse language | [hub](https://block.ke/project/highpoint-336-residences/) |
| 11 | **Jabali Towers** | 5 | Tatu City (Kiambu) | 1–3 bed | [hub](https://block.ke/project/jabali-towers/) |
| 12 | **KEZA Riruta** | 5 | Riruta | 1–3 bed | [hub](https://block.ke/project/keza-riruta/) |
| 13 | **Morvara Hotel Style Apartments** | 5 | Westlands | from **KES 8.35M / 13.25M / 19.75M** | [hub](https://block.ke/project/morvara-hotel-style-apartments/) |
| 14 | **Seasons Riverside** | 5 | Riverside; Westlands | duplex / 2–4 bed language | [hub](https://block.ke/project/seasons-riverside/) |

Plus discovery-prior **Ivy Park Residences** (5, Kilimani) — already queued in national leads.

### Strong secondary (`Listings = 4`, brand-new)

Aether Residences, Auris Residence, Baystar, Butterfly Palace, Calla Residency, Executive Suites, Forest One Residency, KEZA Laika (Ruaka), Mara Grove Apartments (Syokimau), Riverside Azure, Space Residence — plus near-misses Golden Apple / Kings Lotus if opened as separate entities.

---

## Possible Block internal duplicate

| Titles | Listings | Area | Note |
|--------|--------:|------|------|
| **Stellar Bay** · **Stellar Bay Apartments** | 2 + 2 | Westlands | Separate `property_project` terms; overlapping product language — **needs_verification** before two dossiers |

---

## Recommended next research batch (from this slice)

**Superseded by multi-source vetting:** see **[block-2028-process-rerun-batch.md](block-2028-process-rerun-batch.md)** — Tier A developments with non-Block corroboration (Mi Vida / Tatu / Highpoint microsite / multi-agent + named developers).  

**Do not open from Block density alone:** Karura Forest Views looks like a Block-only / alias title (no independent project found).  

Skip re-opening the six true corpus overlaps unless a fact conflict appears.

---

## Caveats / non-claims

- **Block is not authoritative** — see Trust posture.  
- No GPS imported from Block (JSON-LD exists on pages; other agent owns geo; Block pins unverified).  
- No developer legal names from Block alone.  
- HTML hub scrape ([block-2028-sample.json](../../internal/block-2028-sample.json)) is **discarded** as contaminated.  
- Full REST pull kept for forensics; expect unrelated / regular / AI filler listings inside project tags.  
- `2027 / 2028` bucket (if needed later) is a **separate** study — not mixed into these 74.

---

## Artefacts

| File | Role |
|------|------|
| [internal/block-ke-offplan-developments.csv](../../internal/block-ke-offplan-developments.csv) | Full Block export (source) — low trust |
| [internal/block-ke-2028-only.csv](../../internal/block-ke-2028-only.csv) | Exact-2028 + status + API areas/prices — low trust |
| [internal/block-2028-listings-full.csv](../../internal/block-2028-listings-full.csv) | Flat parsed fields for 219 tagged listings — **raw / unverified** |
| [internal/block-2028-listings-full.json](../../internal/block-2028-listings-full.json) | Full REST payloads + parsed + HTML content — **raw / unverified** |
| [internal/block-2028-quality-audit.json](../../internal/block-2028-quality-audit.json) | Contamination / boilerplate flags |
| [internal/block-2028-api-enrichment.json](../../internal/block-2028-api-enrichment.json) | Lighter per-project title sample |
| [internal/block-2028-sample.json](../../internal/block-2028-sample.json) | **Superseded / contaminated** HTML-card sample — do not use |
| [internal/block-2028-analysis.json](../../internal/block-2028-analysis.json) | Curated overlap classification |
