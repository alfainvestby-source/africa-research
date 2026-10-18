# Relational database model (portal master data)

Owned by the **Proptech DB Engineer** agent. Evolves as research dossiers land.

**Product locks:** [decisions.md](../decisions.md) · [goal-and-approach.md](../goal-and-approach.md)

## Purpose
Master data graph for a **Rightmove-class** Kenya product: **`public`** consumer portal + **`admin`** ops/content + **`plus`** (pro/agent) tools. Strong data layer; professional calculated decisions — not ad-hoc scrapes.

## Exposure tiers (intent)

| Tier | Analogy | Rule of thumb |
|------|---------|---------------|
| `public` | Rightmove | High **confidence** + high **coverage** only |
| `admin` | Rightmove Admin | Full claims, conflicts, `needs_*`, sources |
| `plus` | Rightmove Plus | Agent graphs, multi prices, progress, pro facets |
| `internal` | Steward QA | Optional fold into admin later |

## Contents (living)

| Path | Role |
|------|------|
| [`schema.md`](schema.md) | Logical model + tier annotations (v**0.1.14** — `inventory_class` on listing + property) |
| [`feature-taxonomy.md`](feature-taxonomy.md) | Feature catalog + scopes (merged into schema) |
| [`field-promotion.md`](field-promotion.md) | Corpus coverage scoreboard → public / admin / plus / internal |
| [`data-quality-scores.md`](data-quality-scores.md) | Per-property risk / trust scores → Admin triage + Plus signals |
| [`payment-plans.md`](payment-plans.md) | Normalized payment claims catalog (deposit / tenor / fees) |
| [`er-notes.md`](er-notes.md) | Design rationale, surface map |
| [`changelog.md`](changelog.md) | What changed when (latest **0.1.14** — `inventory_class`) |
| [`hauzisha-developers.md`](hauzisha-developers.md) | Hauzisha lead inventory + Ready / Coming soon locks |
| [`seed/`](seed/) | Normalized extracts (no invented facts) |
| [`seed/corpus-rollup.md`](seed/corpus-rollup.md) | Full inventory (**34** — NBO + NAK/MSA/ELD/KWA/DIA + DISC) |

### Seed coverage (34)
See [`seed/corpus-rollup.md`](seed/corpus-rollup.md) — Nairobi NBO-001…017 plus Nakuru / Mombasa / Eldoret / Kwale / Diani / discovery. Prior Wave B slice: [`seed/wave-b-rollup.md`](seed/wave-b-rollup.md).

**Features:** catalog scopes `development` \| `apartment` \| `house` \| `community` — see feature-taxonomy + seed `features*.csv` / `property_features.csv` / `unit_type_features.csv`.

**Inventory class (v0.1.14):** `off_plan` \| `building` \| `ready` \| `resale` on `listing` + `property`. Ready = stored, not dossiered. Coming soon → `off_plan` (in review). Lead sketch: [`seed/listings_hauzisha_inventory_leads.csv`](seed/listings_hauzisha_inventory_leads.csv).

## Inputs
Research dossiers under `docs/projects/`, locks in **`decisions.md`** / `project-context.md` / `master-data-schema.md` / `learning-loop.md`, CSV as leads only.

## Rules (summary)
- No invented facts; confidence internal for public v1
- Canonical when developer sources **agree**; else retain conflicts
- `needs_verification` vs `needs_developer_input` (distinct)
- Co-named developers → dual `co_developer` M2M + RelatedParty
- Always multi prices; no public `price_from` on official conflict
- **Public** gated; **Admin/Plus** retain full graphs + flags
- `construction_progress` = candidate until coverage proven
- **Ready** (`inventory_class=ready`) stored but not researched; Hauzisha `0730 731 355` ≠ developer; Block.ke low-trust; developments-only for dossiers
