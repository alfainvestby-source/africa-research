---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# DB quality asks — explained + locked (2026-10-18)

Parent flags: [db-quality-ask-flags-2026-10-17.md](db-quality-ask-flags-2026-10-17.md)

---

## Ask 1 — Hero price (simple example)

**Problem:** One project often has **several real prices** from real sources. We must not invent a winner.

### Example: 237 Lulu (real case)

| What a buyer sees if we pick wrong | Source | Amount |
|------------------------------------|--------|--------|
| Marketing “from” on Mi Vida page | Developer | **KES 4.4M** |
| Typed 1BR/2BR price cards on same developer site | Developer | **KES 6.93M+** |

Both are **official**. They disagree → we flag **`needs_developer_input`** (cannot guess).

**What each option means on the public search card:**

| Option | Card shows | Sort by price? |
|--------|------------|----------------|
| **1A Band** | “About **4.4–7M+** · confirm with developer” | No (or sort by band mid — messy) |
| **1B Suppress** | Name · place · developer · beds · **no price** until cleared | No |
| **1C Pick one** | “From 4.4M” (or 6.93M) + badge | Yes — **lies to half of buyers** |

**Final lock (Zoopla / Rightmove best practice, 2026-10-18):** [db-quality-locks-2026-10-18.md](db-quality-locks-2026-10-18.md)

- Agreed floor → **From X**
- Agreed multi, no official fight → **X–Y** (Rightmove development min/max)
- Official NDI (Lulu-style) → **POA** on public (Zoopla qualifier) — not blank, not a silent single number
- Plus/Admin always keep the full price table

---

## Ask 2 — Steward order (**I decide**)

| Order | Work | Why |
|------:|------|-----|
| 1 | **Seed 007–011** (Lulu, Highpoint, Jabali, Balkis, Hephé) | Dossiers exist; DB can’t serve them |
| 2 | **Backfill `inventory_class`** on blank rows | Needed for off-plan vs Ready browse |
| 3 | **Media manifests → seed** | Public cards need a photo |
| 4 | **Typology `listing` snapshots** from retained URLs | Soft Zoopla-style offers (lock 2B) |

---

## Ask 3 — Bathrooms (your question)

**Both layers — not either/or:**

| Layer | What it is | Example |
|-------|------------|---------|
| **`unit_type.bathrooms`** | One typology’s bath count | “2 Bedroom + DSQ → **2 bathrooms**” |
| **Property range (derived)** | Min–max across typologies for filters/cards | Development offers **1–3 baths** |

We store the **per-type** number when sourced; the **1–3 range** is computed for search (like beds).

**Fill rule (locked): 3A strict**

- Yes: brochure/floorplan says “2 bathrooms” / “2 baths” / “all bedrooms ensuite **and** guest WC (3)”  
- No: invent “2 baths” only because it’s a 2BR  
- Soft “all ensuite” without a count → leave blank or mark NV; do **not** auto-fill

---

## Ask 4 — Map tools (find the pin)

We do **not** invent GPS. Tools to **find and cross-check** similar place names:

| Tool | Use |
|------|-----|
| **Developer site / brochure map** | Best — screenshot or embedded pin |
| **NEMA EIA** | Often has **lat/lng + plot LR** (e.g. Atreus, Onlyou) |
| **Google Maps / Places** | Search “Libra Residences George Padmore” / street + landmark; compare to dossier street |
| **Google Geocoding API** (if we wire it later) | Structured address → candidate coords (still needs human/conf check) |
| **OpenStreetMap / Nominatim** | Free geocode; good for streets, weaker for new towers |
| **Kenya portals** (Hauzisha/BuyRent map widgets) | Lead only — conf ≤2; never sole public pin |
| **Companies Registry / title plot** | When we have LR number |

**Workflow:** street + landmarks from dossier → Maps search → if pin lands on correct road and matches EIA/developer → conf 4–5. If only “Westlands” blob → neighbourhood **approx** for Admin, **hide on public** until better.

**Pin policy revised (user: map is absolute necessity):** public **always** shows a location. Exact when conf ≥4; **Approximate** / **Area only** badges when online geocode is weaker; physical visit if online fails. Tools unchanged. See [db-quality-locks-2026-10-18.md](db-quality-locks-2026-10-18.md).

---

## Ask 5 — Weak developers

**Locked: 5A** — Misty / Polaris / similar stay **admin-only** until developer conf ≥4.

---

## Ask 6 — “Standardization” = your 70% idea (**helped decide**)

You meant: **public fields = high fill rate AND trustworthy**, not pretty enums for their own sake.

### Gate (locked)

A field may become a **public column / filter** only if:

1. **Coverage ≥ ~70%** of method-complete, seeded developments have a value, **and**
2. **Trust:** value comes from **developer/official** **or** **≥2 independent non-portal agents** (same shape), **and**
3. **Not** a single-agent / Block.ke / AI-sounding gap-fill, **and**
4. No open **`needs_developer_input`** on that field for that row (row can still appear; that **field** stays hidden)

This matches existing decisions (“high confidence AND high coverage”) with your **70%** number made explicit.

### Likely first public set (to validate on next coverage pass — not inventing)

| Field | Why likely ≥70% + trustable |
|-------|-----------------------------|
| Name / aliases | Always |
| City / neighbourhood | Always |
| Primary developer (when conf ≥4) | Most; exclude weak |
| Status summary (off-plan / UC language) | Common |
| Bed typologies (1BR, 2BR, …) | Common |
| Size when developer/brochure | Often |
| Amenities core (pool, gym, …) when catalogued | Common |
| Completion **year** when multi-source agree | Often year; month flaky |

### Stay Admin/Plus until gate passes

| Field | Why |
|-------|-----|
| Single hero price | Many NDI / multi-claim |
| Exact GPS | Sparse high-conf |
| Bathrooms | Almost empty today |
| Payment % | Often &lt;4 agents |
| Storeys / total units | Frequent conflict |
| Progress % | Sparse / NV |

**Standardization work** = (1) measure fill+trust on current seeds, (2) publish the shortlist that passes 70%, (3) normalize labels only for those fields (e.g. “2 Bedroom” vs “2BR”). Not forcing empty columns onto public.

---

## Ask 7 — Seed CSV vs Postgres (simple example)

Think of two stages of the same product:

### 7A — Spreadsheet filing cabinet (**what we have**)

- Each table is a **CSV file** (`properties.csv`, `unit_types.csv`, …)
- Agents write dossiers → steward copies facts into CSVs
- Good for research; **no live website** reading it yet
- Like recipes in Google Sheets before the restaurant opens

### 7B — Real database in a building (**Postgres / Prisma**)

- Same tables, but inside **PostgreSQL** (or Prisma Composer app)
- Website can search “Westlands 2BR” in milliseconds
- Needs hosting, migrations, backups
- Like moving recipes into a kitchen POS system

### 7C — Blueprint only

- Write the migration plan; don’t turn the kitchen on yet

**Recommendation locked: 7A now → 7C when public shortlist stable → 7B when we ship UI.**

We keep improving CSVs + schema docs until the **70% public field set** is proven; then spec Postgres; then deploy when product needs a live API.

---

## Lock summary

| Ask | Lock |
|-----|------|
| 1 Hero price | **1B** on NDI; **1A** only when band is agreed; never 1C |
| 2 Steward order | Seed 007–011 → inventory_class → media → listing snapshots |
| 3 Bathrooms | Per-`unit_type` + derived range; fill **3A** explicit only |
| 4 Map | Tools above; public **4A+4C** |
| 5 Weak developer | **5A** admin-only |
| 6 Standardize | **70% coverage + developer/≥2 agents**; measure then promote |
| 7 DB target | **7A now**; 7C then 7B at ship |

---

## Next steps (when you say go)

1. Coverage pass: compute fill+trust % per field on 46 seeded props → draft public shortlist  
2. Steward: seed five missing dossiers  
3. Do **not** invent bathrooms/GPS/prices to chase 70%
