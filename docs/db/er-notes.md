# ER notes — classifieds / proptech patterns

Version: **0.1.14** · Updated: **2026-10-16** (`inventory_class`; `agent_person` + `listing` M10; feature taxonomy; Rightmove-class tiers)

**Product locks:** [decisions.md](../decisions.md) · [goal-and-approach.md](../goal-and-approach.md)  
**Schema:** [schema.md](schema.md) · **Changelog:** [changelog.md](changelog.md)

**North star:** world-class product like **Rightmove + Rightmove Admin + Rightmove Plus** — strong data layer; professional calculated decisions. One master graph; three surface projections.

## Why this shape

Kenya off-plan master data is **not** a flat listing table. Portals (Rightmove-class) separate:

1. **Development (Property)** — the project / scheme  
2. **Unit typology** — sellable product shapes (beds, sizes)  
3. **Listing / ad** — a time-bound consumer offer (`listing` → property + optional unit_type; v0.1.9)  
4. **Party graph** — who builds, who markets, which **agency**, which **salesperson**, who to call  
5. **Provenance** — every commercial fact is a sourced **claim**, not a single cell  

Research dossiers already produce entity-shaped output. The DB steward normalizes that graph; research agents own discovery.

---

## Patterns used

### 1. Claim store + optional specialized tables

Generic `claim(field_key, value, confidence, is_canonical, needs_verification, needs_developer_input)` holds geography labels, amenities, status, completion, legal blurbs, etc.

Specialized tables exist where portal facets / analytics need columns:

| Table | Why not only `claim`? |
|-------|------------------------|
| `unit_type` | Bed/size facets; gross vs plinth columns (Astra) |
| `price_observation` | Cash vs instalment + tenor; **always multi-row** |
| `payment_plan_claim` | Must-have threshold accounting (`≥4` agents **or** any developer) |
| `construction_progress` | Multiple dated snapshots; never average; **candidate** field |

### 2. Two distinct flags (locked)

| Flag | Use when | Example |
|------|----------|---------|
| `needs_verification` | Agent-only, low-conf, uncorroborated, 404 snippets | Astra 2BR; Porini FAQ deposit |
| `needs_developer_input` | **Official vs official** — do **not** pick a winner | Galaxy 210 vs 266; Porini 7.61M vs 7.5M official bands; Pandora unit mix |

Revisit `needs_developer_input` in later verification passes when confidence rises.

### 3. Canonical ≠ “pick a winner”

If developer identity is confident **and** developer sources **agree** → `is_canonical`.  
If developer sources **disagree** → no canonical + `needs_developer_input`.

### 4. Party / role graph

| Entity | Role |
|--------|------|
| `developer` | Primary or co_developer via `property_developer` |
| `group_company` | Parent **only when evidenced** (seed empty) |
| `related_party` | marketing_partner **or** co_developer (dual with M2M) |
| `agent` | Agency / portal **brand**; dedupe by trading name |
| `agent_person` | Named salesperson (`first_name` / `last_name` / `notes`; optional `agency_id`) — **do not invent** |
| `listing` | Portal/ad snapshot; `publisher_agent_id` + optional `agent_person_id` |
| `listing_agent` | M2M when an ad names multiple sellers |
| `property_agent` | Development-level agency coverage (kept alongside listings) |
| `stakeholder` | Contractor (CRJE), architect, creatives |
| `contact` | Polymorphic owner — phone/email/web; person names belong on `agent_person`, not stuffed in `label` |

### 5. Co-named developers (locked)

| Case | Model |
|------|--------|
| Laureland ↔ Wimax / Astra | `marketing_partner` **only** (not co_developer, not GroupCompany) |
| Tatu City Limited ↔ Rendeavour / Porini | **Both** `property_developer(role=co_developer)` **and** `related_party(relationship_type=co_developer)` |

Primary developer for Porini remains Rendeavour. Propose simplification of the dual link later when more co-named patterns exist. Do **not** invent GroupCompany from “Tatu City” branding.

### 6. Prices (locked)

- Always store **multiple** `price_observation` / claim options.  
- Conflicting **official** prices → **no** public `price_from`; keep all rows; flag `needs_developer_input`.  
- Portal public columns later = fields with **high confidence AND high coverage** (~½ listings missing → not public).

### 7. Payment plan threshold

```text
meets_must_have = has_developer_source OR independent_agent_portal_count >= 4
```

Agent-only payment (no developer schedule): conf **≤3** is correct (method lock).

| Project | Deposit / tenor | Outcome |
|---------|-----------------|---------|
| Pandora | 20% (≥4 agents) | Must-have secondary; conf 3; not canonical |
| Astra | 20% (≥4 agents) | Must-have secondary; conf ≤3 |
| Porini | 24-mo via developer; deposit only via 404 FAQ | Tenor canonical; deposit `needs_verification` |
| Galaxy | **10%** developer vs **20%** agents | 10% canonical; 20% secondary + conflict |

### 8. construction_progress (locked)

Capture when developer publishes; claim set if pages disagree (`needs_developer_input`). **Candidate** field — not portal must-have until coverage proven across listings.

### 9. Source selection / agent dedupe / master-planned geo

Unchanged from 0.1: scan~10 / retain≥5; Block phone deduped across properties; Tatu City as `geo_place(master_planned_community)`.

### 10. Feature taxonomy (v0.1.5)

Controlled `feature` slugs with scopes **`development` \| `apartment` \| `house` \| `community`**. Links via `property_feature` (building/estate) and `unit_type_feature` (typology). Synonyms normalize dossier free text; no invented amenities. Public filters wait on Coverage agent; Admin/Plus keep full graphs. Catalog: [feature-taxonomy.md](feature-taxonomy.md).

### 11a. Ready vs off-plan inventory (`inventory_class`, v0.1.14 / M15)

Portal exports (Hauzisha-class) are **lead lists**. Store every card, but gate the research process:

| `inventory_class` | Who | Research |
|-------------------|-----|----------|
| `off_plan` | Off-plan + **Coming soon** hubs (Coming soon maps here — no extra enum) | In queue / review |
| `building` | Under construction | In queue |
| `ready` | Ready unit ads **and** handed-over whole developments | **Store only** — no dossier for now |
| `resale` | Secondary market when tagged | Store; not off-plan dossier |

Prefer columns on `listing` + `property` over a raw scrape table. Orphan Ready ads may have `listing.property_id` NULL. Never invent Ready from “N units for sale”.

### 11. Agency vs salesperson vs listing (v0.1.9 / M10)

| Layer | Entity | Holds |
|-------|--------|-------|
| Brand | `agent` | Agency name + website |
| Person | `agent_person` | `first_name`, `last_name`, `notes`, optional `agency_id` |
| Channels | `contact` | phone / email / url (web) owned by `agent` **or** `agent_person` |
| Development coverage | `property_agent` | Which agencies market this project |
| Ad snapshot | `listing` | `source_url`, publisher agency, optional primary person, status, first/last seen |
| Ad sellers | `listing_agent` | Extra people/agencies on one ad |

**Seed gap today:** seeds are agency-level only. Names like **Loyd Mokaya** sit in `contact.label` on `agent-block`. Migrate path (schema.md): promote evidenced names → `agent_person`, re-own phone/email, optionally mint `listing` from retained `evidence_url`. Desk labels (“Own It CSV”) stay on `agent` until a human is named. **No invented people.**

---

## Surfaces: `public` | `admin` | `plus`

| Tier | Analogy | Gate / retention |
|------|---------|------------------|
| **`public`** | Rightmove | Coverage **+** confidence; clean canonicals; no silent winners on official conflicts |
| **`admin`** | Rightmove Admin | Retains conflicts, `needs_*`, sources, research_pass, verification queues |
| **`plus`** | Rightmove Plus | Retains multi prices, payment options, progress, full agent/contact graphs |

Admin and Plus **do not drop** data that fails the public gate — they project it with flags/badges.

| Data | public | admin | plus |
|------|:------:|:-----:|:----:|
| Canonical identity, geo, amenities | ✓† | ✓ | ✓ |
| Multi prices / official conflict | ✗ `price_from` | ✓ NDI queue | ✓ full table |
| `needs_verification` / claim sets | light badge optional | ✓ | ✓ |
| Agent graph / WhatsApp | CTA only | ✓ QA | ✓ full |
| `construction_progress` | ✗ until coverage | ✓ | ✓ |
| Confidence scores | ✗ v1 | ✓ | optional |

† after coverage+confidence gate.

---

## Industry alignment (Rightmove-class)

| Portal concept | Our entity / surface |
|----------------|----------------------|
| Consumer development page | `property` → **`public`** |
| Ops/content console | claim conflicts + sources → **`admin`** |
| Agent/pro tools | contacts, multi prices, progress → **`plus`** |
| Plot / unit type | `unit_type` |
| Branch / estate agent (brand) | `agent` + `contact` |
| Named salesperson | `agent_person` + person-owned `contact` |
| Portal listing / ad | `listing` + `listing_agent` |
| Developer | `developer` + `property_developer` |
| Spec / brochure media | `media_asset` + `source` |
| Price observations | `price_observation` (always multi) |

---

## Deferred (not blocking)

- Simplify dual co_developer + RelatedParty when patterns clear  
- Lazy seed migrate of Loyd-style labels → `agent_person` / optional `listing` rows (M13)  
- Portal field set finalization / `is_portal_field` flips  
- Public listing surface (Plus/Admin first)

---

## Seed coverage

**17/17** dossiers — see [seed/corpus-rollup.md](seed/corpus-rollup.md).
