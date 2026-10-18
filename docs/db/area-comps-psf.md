# Area comps / KES per sqm (v0.1)

**Skill:** Area comps / PSF analytics · **Date:** 2026-10-16  
**Rule:** Compute **only** where a dossier supplies **both** a numeric size (sqm) **and** a paired price claim for the same typology. **Never invent** sizes or prices.  
**Inspiration (structure only):** Rightmove-class £/sqft / price-per-area facets and pro comps tools; Zoopla floor-area context — adapted to our provenance locks (multi-claim, NDI/NV, gross vs plinth). **Not** majengo.co.ke.

Related: [agents/area-comps-psf.md](../agents/area-comps-psf.md) · dossiers under [projects/](../projects/) · [price_observations.csv](seed/price_observations.csv) · [unit_types.csv](seed/unit_types.csv) · [decisions.md](../decisions.md)

---

## 1. Method

### 1.1 Inclusion

A row enters the observation set if and only if:

1. **Size** is numeric sqm from a dossier / `unit_types` seed (brochure, developer page, agent table with explicit sqm), and  
2. **Price** is a KES amount from `price_claims[]` / `price_observations` that is **explicitly tied** to that typology (typed product page, info-pack row, agent table with matching beds+size), and  
3. Neighbourhood is the dossier’s geography neighbourhood (or master community for Tatu).

### 1.2 Formula

```text
kes_per_sqm = round(price_kes / size_sqm)
```

### 1.3 Comparability rules (locked for this pass)

| Rule | Why |
|------|-----|
| Prefer **cash / from_hero / band endpoints** for neighbourhood bands | Instalment prices inflate PSF; keep instalment as secondary series |
| **Never mix** gross vs plinth vs total_area in one headline band without tagging | Astra / Misty / Porini measures differ |
| Size **ranges** (e.g. Diamond 2BR 115–145; Galaxy 1BR 57–60) → compute at **both endpoints** with same price; do not invent a midpoint scalar as “truth” |
| Price **bands** (Longines 6.7–7.7M) → use **low and high** endpoints |
| Official-vs-official prices (NDI) → **include in Plus comps** with `needs_developer_input` flag; **exclude from any public neighbourhood median** |
| Agent-only / `needs_verification` pairs → Plus / Admin only |
| Hero “from” with **no typed size** (Porini 7.61M; Diamond ongoing 8.84M; Gemini developer 10M; Galaxy NRE 5.61M) → **excluded** (no size join) |

### 1.4 Neighbourhood keys

| Key | `geo_place` | Projects contributing observations |
|-----|-------------|-----------------------------------|
| Westlands | `geo-westlands` | Diamond Bay, Galaxy One, Pandora, Misty Springs, Golden Mansion (studio only) |
| Brookside (Westlands) | `geo-brookside` | Gemini Phase 2 (agent typed only) |
| Kilimani | `geo-kilimani` | Longines Bay |
| Lower Kabete | `geo-lower-kabete` | Astra Bay |
| Tatu City | `geo-tatu-city` | Porini Point |

---

## 2. Coverage gaps (do not paper over)

| Project | Neighbourhood | Why little / no PSF |
|---------|---------------|---------------------|
| **Berkeley Homes** | Kileleshwa | Prices exist (agent); **no unit size_sqm** on seeded typologies / ESIA mix without schedule this pass |
| **Riara Oasis** | Thompson / Riara Rd | Unit mix + parking on NEMA; **no typed size+price schedule** harvested into pairs this pass |
| **Golden Mansion** | Westlands | EIA unit **counts** without size schedule; only Block Studio A5 **41.22 sqm + 6.18M** pair |
| **Gemini Phase 2** | Brookside | Developer **from 10M** has **no official size** → excluded; CPK agent sizes+prices only |
| **Pandora** | Westlands | Brochure sizes for 3/4/5BR; agent prices loosely matched; 2BR brochure conflict / agent-only |
| **Astra Bay** | Lower Kabete | Developer **sizes** yes; **no developer prices** — all PSF agent-sided |
| **Galaxy One** | Westlands | Official prices **NDI** (Lionston vs FAQ); sizes often **bands** |
| Lesonia / Luna Oak / Golfscape / etc. | — | Thin dossiers / not in sized+priced seed set |

**Corpus n:** 11 seeded properties; **5 neighbourhoods** with ≥1 valid pair; **~55 non-instalment observations** this pass (+ 3 Porini instalment secondary).

---

## 3. Neighbourhood bands (KES / sqm)

Figures are **descriptive of sourced pairs only** — not a market appraisal.  
**Primary series** = cash / from / band endpoints (instalment excluded).  
All values rounded to nearest KES.

### 3.1 Summary table

| Neighbourhood | n (primary) | Min | ~Median | Max | Dominant projects | Headline quality |
|---------------|------------:|----:|--------:|----:|-------------------|------------------|
| **Kilimani** | 13 | 93,056 | ~110,400 | 121,970 | Longines Bay (developer bands) | Strongest single-project official size+price |
| **Tatu City** | 6 | 121,379 | ~125,400 | 138,148 | Porini (info-pack cash + Block) | Official-attributed sizes; prices NDI across packs — Plus |
| **Brookside** | 5 | 137,313 | ~140,900 | 150,000 | Gemini Phase 2 (CPK agent) | Agent-only sizes+prices vs developer from-without-size |
| **Lower Kabete** | 7 | 71,648 | ~91,200 | 95,227 | Astra Bay | Agent prices × developer sizes; gross/plinth split matters |
| **Westlands** | 24 | 86,667 | ~137,400 | 191,797 | Diamond, Galaxy, Pandora, Misty, Golden | Heterogeneous; mix NDI + agent; **not** a clean public facet |

### 3.2 Kilimani — Longines Bay (developer residences)

| Unit | Size sqm | Price KES | KES/sqm | Notes |
|------|---------:|----------:|--------:|-------|
| Studio | 39 | 3.7–4.5M | 94,872–115,385 | Official |
| Studio furnished | 48 | 5.3–5.8M | 110,417–120,833 | Official |
| 1BR | 72 | 6.7–7.7M | 93,056–106,944 | Official |
| 2BR | 87 | 8.5–9.4M | 97,701–108,046 | Official |
| 2BR | 94 | 8.9–10.5M | 94,681–111,702 | Official |
| 3BR duplex | 132 | from 16.1M | 121,970 | Official |
| 5BR duplex | 176–179 | from 21M | 117,318–119,318 | Official |

**Band (primary):** ~**93k–122k KES/sqm**.

### 3.3 Tatu City — Porini Point

| Unit | Size (total_area) | Cash KES | KES/sqm | Source |
|------|------------------:|---------:|--------:|--------|
| 1BR | 54 | 7.18M / 7.46M | 132,963 / 138,148 | Info-pack / Block |
| 2BR | 90 | 11.07M / 11.29M | 123,000 / 125,444 | Info-pack / Block |
| 3BR | 145 | 17.6M / 17.95M | 121,379 / 123,793 | Info-pack / Block |

Instalment (24-mo) PSF higher (~161k–145k) — **secondary only**.  
Hero 7.61M / 7.5M / 5.9M **without typed join** → excluded.

**Band (cash primary):** ~**121k–138k KES/sqm**.

### 3.4 Lower Kabete — Astra Bay

| Pair | Size | Measure | Price | KES/sqm | Flag |
|------|-----:|---------|------:|--------:|------|
| Studio | 26.1 | gross | 1.87–1.96M | 71,648–75,096 | Agent price |
| Studio | 21.0 | plinth | 1.96M | 93,333 | Same price, plinth — **do not average with gross** |
| 1BR | 53.2 | gross | 4.07–4.86M | 76,504–91,353 | Agent band |
| 1BR | 42.74 | plinth | 4.07M | 95,227 | Plinth |
| 2BR agent-only | 78.3 | unknown | 7.14M | 91,188 | `needs_verification` typology |

**Band (gross-preferred agent):** ~**72k–91k**; plinth reads higher for same price.

### 3.5 Brookside — Gemini Phase 2 (agent CPK only)

| Unit | Size | Price | KES/sqm |
|------|-----:|------:|--------:|
| 1BR | 58 / 67 | 8.7M / 9.2M | 150,000 / 137,313 |
| 2BR | 90 / 110 / 122 | 13.5 / 15.5 / 17.1M | 150,000 / 140,909 / 140,164 |

Developer from **10M** omitted (no official size). All rows **`needs_verification`** vs developer from.

**Band:** ~**137k–150k KES/sqm** (agent).

### 3.6 Westlands (multi-project — wide)

| Project | Illustrative pairs | KES/sqm span |
|---------|-------------------|-------------:|
| Diamond Bay (henbon typed) | 1BR 68→9.34M; 2BR 115–145→15.375M; 3–5BR typed | ~106k–137k |
| Galaxy One (NDI official) | 1BR 57–60 × 5.2M or 8.0M; 2BR 82–91 × 12M; 3BR 142 × 13.9–18M | ~87k–146k |
| Misty Springs (agent plinth) | 58/90/99 × 8.0/12.6/13.8M | ~138k–140k |
| Pandora (brochure size + agent price) | 3BR 152.68→24.61M; 4BR 194.32→31.5–37.3M; agent 2BR | ~148k–192k |
| Golden (agent studio only) | 41.22→6.18M | ~150k |

**Band (all primary Westlands pairs):** ~**87k–192k** — too wide for a single public “Westlands PSF” without project filters.

---

## 4. Plus vs public rules

| Surface | Rule |
|---------|------|
| **`public`** | **No** neighbourhood PSF facet in v0.1. Coverage is thin; Westlands is multi-modal; many pairs are agent-only or NDI; measures mixed. Aligns with portal gate: high confidence **and** high coverage. |
| **`plus`** | Show **project-level** KES/sqm where size+price pair exists; show neighbourhood **range + n + measure tags + provenance flags**; allow filter by beds / cash vs instalment. Badge NDI/NV. |
| **`admin`** | Full observation table; gaps list; join QA (wrong typology↔price); measure conflicts (gross vs plinth). |

**Rightmove-class analogy:** consumer £/sqft appears when floor area is known on a listing; **area averages** are pro/contextual. We keep neighbourhood aggregates in **Plus** until corpus densifies and measure tags standardize.

---

## 5. Industry patterns used (non-Majengo)

| Pattern | Source class | Adaptation |
|---------|--------------|------------|
| Price per floor area on listing | Rightmove / Zoopla | Compute only with sourced size; show on Plus project cards first |
| Do not conflate asking bands | Pro comps tools | Keep multi endpoints; no single invented mid |
| Separate new-build vs resale | Portal practice | Our corpus is off-plan/new — label as such; don’t mix rent |
| Area heatmaps need density | Analytics products | Flag low-n neighbourhoods; refuse public median |

---

## 6. Recommended next steps

1. **Document intelligence:** extract missing size schedules (Berkeley, Golden EIA appendices, Riara) so more pairs qualify.  
2. **DB steward:** optional `price_observation.kes_per_sqm` generated column when `unit_type.size_sqm` present.  
3. **Coverage agent:** re-score public PSF after ≥N projects per neighbourhood with developer size+price **agreeing**.  
4. Split Westlands comps by **micro-area** (Rhapta vs Westlands Rd vs Muthangari) when street-level n grows.

---

## 7. Observation log (primary series, abbreviated)

Full computation pass 2026-10-16; n≈55 primary + 3 Porini instalment. Representative:

| nbhd | project | unit | sqm | measure | price | kes/sqm | provenance |
|------|---------|------|----:|---------|------:|--------:|------------|
| Kilimani | Longines | 1BR | 72 | unknown | 6.7M | 93,056 | developer |
| Kilimani | Longines | 3BR duplex | 132 | unknown | 16.1M | 121,970 | developer |
| Tatu City | Porini | 1BR | 54 | total_area | 7.18M | 132,963 | developer_attributed |
| Tatu City | Porini | 3BR | 145 | total_area | 17.6M | 121,379 | developer_attributed |
| Lower Kabete | Astra | Studio | 26.1 | gross | 1.96M | 75,096 | agent |
| Lower Kabete | Astra | 1BR | 53.2 | gross | 4.86M | 91,353 | agent |
| Brookside | Gemini 2 | 1BR | 58 | unknown | 8.7M | 150,000 | agent NV |
| Westlands | Diamond | 1BR | 68 | unknown | 9.34M | 137,353 | developer NDI vs ongoing |
| Westlands | Galaxy | 3BR | 142 | unknown | 18.0M | 126,761 | developer NDI |
| Westlands | Misty | 1BR | 58 | plinth | 8.0M | 137,931 | agent |
| Westlands | Pandora | 3BR+DSQ | 152.68 | unknown | 24.61M | 161,187 | brochure size + agent price |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-10-16 | v0.1 — method, gaps, neighbourhood bands, Plus vs public; Majengo excluded by user lock |
