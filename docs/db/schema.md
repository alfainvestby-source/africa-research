# Relational schema — Kenya off-plan / new-development master data

Version: **0.1.15** (`tenure` claim guidance + bathrooms card lock; still `inventory_class` v0.1.14)  
Last updated: **2026-10-17**  
Steward: Proptech DB Engineer  
Dialect: PostgreSQL-flavoured SQL-ish DDL (logical model; not yet applied to a live DB)

**Product north star:** Rightmove (public) + Rightmove Admin + Rightmove Plus — see [goal-and-approach.md](../goal-and-approach.md) · [decisions.md](../decisions.md)

**Feature catalog:** [feature-taxonomy.md](feature-taxonomy.md) · seeds `features.csv` / `feature_scopes.csv` / `feature_synonyms.csv` / `property_features.csv` / `unit_type_features.csv`

**Ingested properties:** **17** developments (see [seed/corpus-rollup.md](seed/corpus-rollup.md)).

## Design principles (locked)

| Rule | How encoded |
|------|-------------|
| Confidence on every claim (internal) | `claim.confidence` SMALLINT 0–5; never a public UI column in v1 |
| Canonical = developer when developer-sourced **and sources agree** | `claim.is_canonical`; official-vs-official disagreement → **no** canonical |
| Conflicts retained | Multiple `claim` rows per `(property_id, field_key)`; `claim_conflict` links peers |
| Low-confidence / agent-only / uncorroborated | `claim.needs_verification` BOOLEAN |
| **Official vs official** (do not pick a winner) | `claim.needs_developer_input` BOOLEAN — **separate** from `needs_verification`; revisit in later verification passes |
| Unproven brand/parent | `related_party.relationship_type = 'marketing_partner'` — **not** `group_company` |
| **Co-named developers** (e.g. Rendeavour + Tatu City Limited) | **Both** `property_developer` role=`co_developer` **and** `property_related_party` — simplify later when patterns clear |
| Payment plan must-have | Met when **any** developer source **or** ≥4 independent agent/portal sources agree |
| Prices | Always store **multiple** `price_observation` / claim options — never collapse to one scalar |
| Portal field set (later) | **`public`** only if high confidence **AND** high coverage (~½ lack it → not public). **Admin** / **Plus** may still show full graphs |
| Surface tiers | Annotate exposure intent: `public` \| `admin` \| `plus` (+ `internal` QA) |
| `construction_progress` | Capture when developer publishes (claim set if pages disagree); **candidate**, not public must-have until coverage proven |
| Sources | Research pass stores `sources_evaluated` / `sources_retained`; developer site always retained |
| Living must-haves | `must_have_field` (+ `is_portal_candidate` / coverage notes) |
| Amenities / features | Controlled `feature` catalog + `property_feature` / `unit_type_feature` links; scopes `development` \| `apartment` \| `house` \| `community` |
| Salespeople vs agencies | `agent` = agency/portal brand; `agent_person` = named salesperson (`first_name` / `last_name` / `notes`); phones/emails/web stay on `contact` |
| Listing vs development | `listing` = portal/ad snapshot pointing at `property` (+ optional `unit_type`); **never** flatten ads into the master property row |
| Ready vs research queue | Portal **Ready** → `inventory_class=ready` (unit ads **and** fully Ready/handed-over developments). Stored; **not dossiered for now**. Research/discovery queue = `off_plan` \| `building` (+ **Coming soon** hubs → `off_plan`). Prefer `listing`/`property.inventory_class` over a raw-import table |
| Named people | **Do not invent** — only promote names evidenced in dossiers / CSV sales_contact labels |

---

## Entity list

| Entity | Purpose |
|--------|---------|
| `geo_place` | City, neighbourhood, street, estate, master-planned community / SEZ |
| `geo_pin` | Sourced lat/lng observation per property (method + confidence + source) |
| `poi` | Typed nearby place (mall, hospital, school, transit, leisure, …) |
| `property_poi` | Property ↔ POI distance / proximity claim |
| `property` | Canonical development / project |
| `property_alias` | Alternate names |
| `unit_type` | Structured typology (beds, measure-tagged sizes) |
| `developer` | Original seller/builder |
| `group_company` | Evidenced parent only |
| `related_party` | marketing_partner, co_developer (dual-link with property_developer), co-marketer, etc. |
| `agent` | Agency / portal marketing seller (brand) |
| `agent_person` | Named salesperson (`first_name`, `last_name`, `notes`; optional `agency_id`) |
| `listing` | Portal / agent ad snapshot → `property` (+ optional `unit_type`) |
| `listing_agent` | Listing ↔ salesperson (and/or agency) who sells that ad |
| `stakeholder` | Contractor, architect, financing, land, other |
| `contact` | Phone / WhatsApp / email / URL / office — owned by a party (incl. `agent_person`) |
| `source` | URL/document with publisher + type + accessed_at |
| `research_pass` | Per-property scan meta (evaluated/retained counts) |
| `claim` | Field value + confidence + canonical + needs_verification + needs_developer_input |
| `claim_source` | Claim ↔ Source M2M |
| `claim_conflict` | Explicit conflict grouping |
| `price_observation` | Price claim with cash/instalment + tenor context |
| `payment_plan_claim` | Deposit %, tenor, booking/reservation fees |
| `construction_progress` | Snapshot observations (tracker vs product page) |
| `media_asset` | Brochure PDF, flyer, floor plan, **listing photo** (local path + hash + dims) |
| `property_media` | Property ↔ MediaAsset (role, sort, gallery category) |
| `property_developer` | Property ↔ Developer roles (primary / co_developer) |
| `property_related_party` | Property ↔ RelatedParty |
| `property_agent` | Property ↔ Agent (development-level agency coverage — **kept**) |
| `property_stakeholder` | Property ↔ Stakeholder |
| `feature` | Controlled amenity/feature vocabulary (slug) |
| `feature_scope_map` | Feature ↔ scopes (`development` / `apartment` / `house` / `community`) |
| `feature_synonym` | Ingest/normalize aliases → slug |
| `property_feature` | Property-level amenity claims (building/estate) |
| `unit_type_feature` | Typology-bound features (DSQ, study, balcony, …) |
| `verification_flag` | Optional typed QA flags beyond claim boolean |
| `must_have_field` | Living must-have catalogue + consensus |

---

## Enumerations

```sql
-- claim.confidence: 0 unknown … 5 developer/official
-- Agent-only consensus cannot exceed 3 without official corroboration (method lock).

CREATE TYPE source_type AS ENUM (
  'project_site', 'developer', 'developer_attributed',
  'agent', 'portal', 'press', 'related_party', 'brochure', 'other'
);

CREATE TYPE party_owner_type AS ENUM (
  'property',          -- project sales office
  'developer',
  'agent',             -- agency / portal brand
  'agent_person',      -- named salesperson (v0.1.9)
  'stakeholder',
  'related_party',
  'group_company'
);

CREATE TYPE listing_status AS ENUM (
  'active',
  'sold',
  'withdrawn',
  'unknown',
  'stale'              -- last_seen aged out / page gone
);

CREATE TYPE related_party_type AS ENUM (
  'marketing_partner',  -- locked default when brand overlap unproven (Laureland)
  'co_developer',       -- co-named on materials; ALSO mirrored on property_developer (Cycle 2 lock)
  'co_marketer',
  'operating_sales',
  'other'
);
-- Soft: co-named developers → dual write property_developer(co_developer) + related_party(co_developer).
-- Propose simplification later when patterns clear across more projects.

CREATE TYPE stakeholder_kind AS ENUM (
  'financing', 'contractor', 'architect', 'land', 'other'
);

CREATE TYPE developer_role AS ENUM ('primary', 'co_developer');

CREATE TYPE contact_channel AS ENUM (
  'phone', 'whatsapp', 'email', 'url', 'office', 'other'
);

CREATE TYPE size_measure AS ENUM (
  'gross', 'plinth', 'total_area', 'unknown'
);

CREATE TYPE price_basis AS ENUM (
  'cash', 'instalment', 'from_hero', 'unknown'
);

CREATE TYPE exposure_tier AS ENUM (
  'public',   -- Rightmove-class consumer portal
  'admin',    -- Rightmove Admin-class ops/content/QA
  'plus',     -- Rightmove Plus-class pro/agent tools
  'internal'  -- research ranking / steward-only (may fold into admin later)
);

CREATE TYPE feature_scope AS ENUM (
  'development',  -- shared building / estate amenities (gym, pool, CCTV)
  'apartment',    -- in-unit apartment features (balcony, DSQ, fitted kitchen)
  'house',        -- house/townhouse features when dossier-sourced (DSQ, parking bay)
  'community'     -- master-plan / precinct (retail boulevard, sanctuary, commercial hub)
);

CREATE TYPE geo_method AS ENUM (
  'official',   -- developer JSON-LD / map embed / Maps CTA on project site
  'nema',       -- NEMA EIA / ESIA / Gazette filing coordinates
  'geocode',    -- street+neighbourhood+city geocoded (Nominatim / Google / Mapbox)
  'csv',        -- seed CSV lat/lng until corroborated
  'unknown'     -- no usable pin
);

CREATE TYPE poi_type AS ENUM (
  'mall', 'hospital', 'school', 'transit', 'leisure', 'airport', 'cbd', 'other'
);

-- Portal / process inventory class (Hauzisha-style tags + product queue).
-- Applies to listing (unit ads) AND property (whole developments).
CREATE TYPE inventory_class AS ENUM (
  'off_plan',   -- Off-plan + Coming soon hubs (Coming soon maps here — no separate enum)
  'building',   -- Under construction / Building chip
  'ready',      -- Ready / handed-over / immediate occupation — store; do NOT dossier (for now)
  'resale'      -- Secondary-market resale inventory (when tagged)
);
-- Mapping (locked): Hauzisha "Coming soon" → off_plan (in scope for discovery/review).
-- "Ready" → ready only when the portal explicitly tags Ready — never infer from "N units for sale".
```

### Surface map (locked intent)

| Tier | Analogy | Sees |
|------|---------|------|
| **`public`** | Rightmove | Canonical / agreed values that pass **coverage + confidence** gate; clean facets; no raw conflict dumps; confidence scores hidden (v1) |
| **`admin`** | Rightmove Admin | Full claim sets, conflicts, `needs_*` flags, source URLs, research_pass meta, verification queues — ops resolve NDI / NV |
| **`plus`** | Rightmove Plus | Agent graphs, contacts, multi price tables, payment options, progress snapshots, pro facets — richer than public, may show badges |
| **`internal`** | Steward/QA | Same as admin plus seed-CSV notes, ranking experiments; optional merge into admin |

**Rule:** master DB stores everything once. Views / API projections filter by `exposure_tier`. Admin and Plus **retain** conflicts, `needs_verification`, `needs_developer_input`, full claim sets, and agent graphs even when public omits them.

---

## Tables

### geo_place

```sql
CREATE TABLE geo_place (
  id                TEXT PRIMARY KEY,           -- e.g. geo-nairobi, geo-tatu-city
  place_type        TEXT NOT NULL,              -- city|neighbourhood|street|estate|master_planned_community|county|country
  name              TEXT NOT NULL,
  parent_id         TEXT REFERENCES geo_place(id),
  country_code      CHAR(2) DEFAULT 'KE',
  is_master_planned BOOLEAN DEFAULT FALSE,      -- Tatu City / SEZ framing
  notes             TEXT
);
CREATE INDEX idx_geo_place_parent ON geo_place(parent_id);
CREATE INDEX idx_geo_place_type ON geo_place(place_type);
```

**Exposure:** `name`, hierarchy → **`public`**. Steward notes → **`admin`/`internal`**.

---

### property (Development)

Identity + soft denormalized pointers only. **All contested facts live in `claim` / specialized observation tables.**

```sql
CREATE TABLE property (
  id                      TEXT PRIMARY KEY,     -- e.g. prop-pandora-residences
  external_id             TEXT UNIQUE,          -- NBO-002 from seed CSV (lead id)
  slug                    TEXT UNIQUE NOT NULL,
  canonical_name          TEXT NOT NULL,        -- mirrored from canonical claim for UX/index
  status_label            TEXT,                 -- soft display only; authoritative set in claims
  inventory_class         inventory_class,      -- development-level Ready / off_plan / building / resale (v0.1.14)
  -- Soft card facets (v0.1.21) — derived/harvested; authoritative detail stays in observation tables
  property_type           TEXT,                 -- apartment | townhouse | villa | maisonette | mixed | …
  beds_min                SMALLINT,             -- derived from unit_type.bedrooms
  beds_max                SMALLINT,
  size_sqm_min            NUMERIC,              -- derived from unit_type.size_sqm when present
  size_sqm_max            NUMERIC,
  hero_price_qualifier    TEXT,                 -- from | range | POA (public display lock)
  hero_price_min          NUMERIC,              -- empty when POA
  hero_price_max          NUMERIC,
  hero_price_currency     CHAR(3),
  deposit_pct             NUMERIC,              -- only when payment must-have met; else NULL
  deposit_meets_must_have BOOLEAN,
  summary                 TEXT,                 -- short card blurb from dossier/canonical facts
  completion_display      TEXT,                 -- public card string when agreed/window; conflict → confirm label
  completion_status       TEXT,                 -- agreed | window | conflict | unknown
  completion_raw          TEXT,                 -- dossier claim text (Admin/Plus)
  completion_needs_developer_input BOOLEAN,     -- official-vs-official or unresolved
  map_tier                TEXT,                 -- exact | approximate | area
  street_label            TEXT,                 -- from dossier geography.street when sourced
  primary_developer_id    TEXT REFERENCES developer(id),
  geo_city_id             TEXT REFERENCES geo_place(id),
  geo_neighbourhood_id    TEXT REFERENCES geo_place(id),
  geo_master_community_id TEXT REFERENCES geo_place(id), -- e.g. Tatu City
  lat                     NUMERIC(9,6),         -- only when developer-sourced (or flagged via claim)
  lng                     NUMERIC(9,6),
  currency_default        CHAR(3) DEFAULT 'KES',
  research_cycle          SMALLINT,             -- 1 = pilot, 2 = …
  last_verified_at        DATE,
  created_at              TIMESTAMPTZ DEFAULT now(),
  updated_at              TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_property_developer ON property(primary_developer_id);
CREATE INDEX idx_property_geo_nbhd ON property(geo_neighbourhood_id);
CREATE INDEX idx_property_master ON property(geo_master_community_id);
CREATE INDEX idx_property_inventory_class ON property(inventory_class);
CREATE INDEX idx_property_map_tier ON property(map_tier);
CREATE INDEX idx_property_hero_qual ON property(hero_price_qualifier);
-- Facet search (portal): status via claims; neighbourhood; developer; price via price_observation
-- Research queue: WHERE inventory_class IS DISTINCT FROM 'ready' (and not resale-only skip rules)
```

**Exposure:** name, geo, status summary, amenities summary, **card facets** (type / beds range / size range / hero From|X–Y|POA / map_tier / summary) → **`public`** (when gated).  
`deposit_pct` → **`public`** only when `deposit_meets_must_have`; else Admin/Plus.  
`external_id`, research meta, lat/lng provenance, **`inventory_class`** → **`admin`** (queue filter); Ready developments stay out of public off-plan browse until product says otherwise. Full identity + co-dev graph → **`plus`**.

**Soft constraints:** Prefer setting `lat`/`lng` on the row only when conf ≥4 official/NEMA/Maps CTA (Galaxy / Golden / Berkeley / Plumeria / Luna Oak / Golfscape pattern); otherwise keep GPS in `geo_pin` / claims with `geo_method` + `needs_verification`. Never invent pins. Hero price never picks a silent NDI winner — use **POA**.

**`inventory_class` (development):** set when portal/dossier tags the **whole** project Ready / handed-over / Off-plan / Building. Seed CSV may leave NULL until inferred from a tagged export or dossier — do **not** invent Ready from unit-count marketing copy.

**Related seed (v0.1.21):** `property_utility_chips.csv` (Kenya utilities from `property_feature`); `media_assets.csv` + `property_media.csv`.

---

### geo_pin

Provenance-first lat/lng observations. Multiple rows per property allowed (official vs geocode vs CSV).

```sql
CREATE TABLE geo_pin (
  id                   TEXT PRIMARY KEY,
  property_id          TEXT NOT NULL REFERENCES property(id),
  lat                  NUMERIC(9,6) NOT NULL,
  lng                  NUMERIC(9,6) NOT NULL,
  geo_method           geo_method NOT NULL,
  confidence           SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_recommended       BOOLEAN NOT NULL DEFAULT FALSE,  -- steward pick for map default
  needs_verification   BOOLEAN NOT NULL DEFAULT FALSE,
  source_id            TEXT REFERENCES source(id),      -- optional FK when source row exists
  source_url           TEXT,
  source_query         TEXT,                             -- geocode query string when method=geocode
  provider             TEXT,                             -- nominatim | google | nema | csv_seed | …
  accessed_at          DATE NOT NULL,
  notes                TEXT,
  created_at           TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_geo_pin_property ON geo_pin(property_id);
CREATE UNIQUE INDEX uq_geo_pin_one_recommended
  ON geo_pin(property_id) WHERE is_recommended;
```

**Exposure:** recommended pin with conf ≥4 → candidate **`public`** map; geocode → **`public`** only with “approx” badge (product) else **`admin`/`plus`**. Method + confidence always on Admin/Plus.

**Seed:** [`seed/geo_pins.csv`](seed/geo_pins.csv) · rollup [`geo-enrichment.md`](geo-enrichment.md)

---

### poi / property_poi

Optional proximity graph for Plus analytics. Light sample only in v0.1.13.

```sql
CREATE TABLE poi (
  id            TEXT PRIMARY KEY,
  name          TEXT NOT NULL,
  poi_type      poi_type NOT NULL,
  lat           NUMERIC(9,6),
  lng           NUMERIC(9,6),
  geo_city_id   TEXT REFERENCES geo_place(id),
  source_url    TEXT,
  provider      TEXT,
  confidence    SMALLINT NOT NULL DEFAULT 2,
  accessed_at   DATE,
  notes         TEXT
);

CREATE TABLE property_poi (
  property_id   TEXT REFERENCES property(id),
  poi_id        TEXT REFERENCES poi(id),
  distance_m    INTEGER,              -- haversine or route meters; document basis in notes/source
  travel_mode   TEXT,                 -- walk|drive|transit|null
  source        TEXT,                 -- haversine_approx | google_distance | project_adjacent | …
  confidence    SMALLINT NOT NULL DEFAULT 2,
  notes         TEXT,
  PRIMARY KEY (property_id, poi_id)
);
```

**Exposure:** Plus proximity chips; Admin QA. Not a public must-have until coverage proven.

**Seed:** [`seed/pois.csv`](seed/pois.csv) · [`seed/property_pois.csv`](seed/property_pois.csv)

---

### property_alias

```sql
CREATE TABLE property_alias (
  id           BIGSERIAL PRIMARY KEY,
  property_id  TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  alias        TEXT NOT NULL,
  UNIQUE (property_id, alias)
);
```

---

### unit_type

Structured typology for facets + size tables. Inventory/sold-out and agent-only typologies still also appear as claims.

```sql
CREATE TABLE unit_type (
  id              TEXT PRIMARY KEY,            -- e.g. ut-astra-superior-studio
  property_id     TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  label           TEXT NOT NULL,               -- "Superior Studio", "3BR+study+DSQ"
  bedrooms        NUMERIC(3,1),                -- allow 0.5 loft nuance later; null if unknown
  bathrooms       NUMERIC(3,1),
  has_dsq         BOOLEAN,
  has_study       BOOLEAN,
  size_sqm        NUMERIC(10,2),
  size_measure    size_measure NOT NULL DEFAULT 'unknown',
  plinth_sqm      NUMERIC(10,2),               -- when both gross+plinth known (Astra)
  gross_sqm       NUMERIC(10,2),
  is_canonical    BOOLEAN NOT NULL DEFAULT FALSE, -- developer-backed typology
  needs_verification BOOLEAN NOT NULL DEFAULT FALSE,
  confidence      SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  notes           TEXT
);
CREATE INDEX idx_unit_type_property ON unit_type(property_id);
CREATE INDEX idx_unit_type_beds ON unit_type(property_id, bedrooms);
```

**Exposure:** canonical unit types + sizes (+ **bathrooms** when sourced) → **`public`** (coverage gate). Non-canonical / `needs_*` typologies → **`admin`** + **`plus`** (badge optional on Plus).

**Bathrooms (Zoopla→Kenya #5 LOCKED):** `bathrooms` is a first-class card attribute with beds/size. Fill only when a dossier/source states an **explicit count**. Never invent from “all ensuite” alone. Skip UK receptions/living-rooms as must-have.

---

### Claim key: `tenure` (Zoopla→Kenya #6 LOCKED)

No dedicated column — store as `claim.field_key = 'tenure'` (and optional mirrored notes on property).

| Value | Meaning |
|-------|---------|
| `freehold` | Freehold interest |
| `leasehold` | Time-limited interest (record years/start in claim notes when sourced) |
| `sectional_title` | Sectional title (common apartment end-state) |
| `unknown` | Not evidenced |

**Exposure:** **Admin / Plus** whenever found; **public** only when developer/official conf ≥4. Not a research blocker if absent.

---

### developer

```sql
CREATE TABLE developer (
  id                 TEXT PRIMARY KEY,
  legal_name         TEXT NOT NULL,
  website            TEXT,
  group_company_id   TEXT REFERENCES group_company(id), -- null unless proven
  sales_office_note  TEXT,
  csv_name_note      TEXT,          -- e.g. "Lionstone" typo lead
  created_at         TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE developer_trading_name (
  developer_id TEXT REFERENCES developer(id) ON DELETE CASCADE,
  trading_name TEXT NOT NULL,
  PRIMARY KEY (developer_id, trading_name)
);
```

**Exposure:** legal/trading names, website → **`public`**. `csv_name_note`, unverified portfolio → **`admin`**.

---

### group_company

```sql
CREATE TABLE group_company (
  id       TEXT PRIMARY KEY,
  name     TEXT NOT NULL,
  website  TEXT,
  evidence_notes TEXT
  -- ONLY insert when parent relationship is evidenced. Never invent from brand overlap.
);
```

**Current seed:** empty (all four dossiers correctly leave GroupCompany null).

---

### related_party

```sql
CREATE TABLE related_party (
  id                 TEXT PRIMARY KEY,
  name               TEXT NOT NULL,
  relationship_type  related_party_type NOT NULL,
  website            TEXT,
  confidence         SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  evidence_notes     TEXT,
  -- Soft rule: use marketing_partner until parent/alias/co_developer proven.
  CHECK (
    relationship_type <> 'co_developer' OR confidence >= 3
  )
);

CREATE TABLE property_related_party (
  property_id       TEXT REFERENCES property(id) ON DELETE CASCADE,
  related_party_id  TEXT REFERENCES related_party(id),
  developer_id      TEXT REFERENCES developer(id), -- optional link side
  role_notes        TEXT,
  PRIMARY KEY (property_id, related_party_id)
);
```

**Examples:**
- Laureland → `marketing_partner` only (Astra Bay) — **not** a co_developer link
- Tatu City Limited (Porini) → **dual model (Cycle 2 lock):** `developer` row + `property_developer(role=co_developer)` **and** `related_party(relationship_type=co_developer)` + `property_related_party`. Primary remains Rendeavour. **Not** GroupCompany. Simplify later when co-named patterns clear across more projects.

Also require `property_developer` table (see below) for all developer roles:

```sql
CREATE TABLE property_developer (
  property_id   TEXT REFERENCES property(id) ON DELETE CASCADE,
  developer_id  TEXT REFERENCES developer(id),
  role          developer_role NOT NULL,  -- primary | co_developer
  confidence    SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  notes         TEXT,
  PRIMARY KEY (property_id, developer_id, role)
);
```

### Cycle 2 conflict / price / progress patterns (locked)

| Pattern | How stored | Example |
|---------|------------|---------|
| Official vs official (any field) | Multiple rows; **no** winner; `needs_developer_input=true` on conflict set; revisit later | Galaxy units/storeys/progress; Pandora unit mix; Porini official price bands |
| Ordinary low-conf / agent-only | `needs_verification=true` (distinct flag) | Astra 2BR; Porini FAQ 404 deposit |
| Deposit developer vs agent ≥4 | Canonical developer + secondary agent + conflict | Galaxy **10%** vs **20%** |
| Prices | **Always** multiple `price_observation` options; never collapse | All four projects |
| Progress % | `construction_progress` claim set if pages disagree; **candidate** field | Galaxy 63% vs 42% |
| Dual cash/instalment | `price_basis` + `plan_tenor_months` | Porini; Galaxy FAQ |
| Master-planned geography | `geo_place.is_master_planned` + FK | Tatu City / Porini |

---

### agent (agency / portal brand)

```sql
CREATE TABLE agent (
  id         TEXT PRIMARY KEY,
  name       TEXT NOT NULL,       -- trading brand, e.g. "Block Real Estate"
  website    TEXT,                -- agency web (brand home)
  agent_type TEXT,                -- agency | portal | aggregator | network | bank_portal
  notes      TEXT,
  UNIQUE (name)
);

-- Development-level agency coverage (kept): which brands market this project.
CREATE TABLE property_agent (
  property_id  TEXT REFERENCES property(id) ON DELETE CASCADE,
  agent_id     TEXT REFERENCES agent(id),
  role_notes   TEXT,            -- CSV sales_contact, listing, FAQ article
  evidence_url TEXT,
  PRIMARY KEY (property_id, agent_id)
);
CREATE INDEX idx_property_agent_agent ON property_agent(agent_id);
```

**Deduping:** one `agent` row per trading brand. Agency-level phones/emails/URLs hang off `contact(owner_type='agent')`. Same Block brand phone across projects → one contact, many `property_agent` edges.

---

### agent_person (named salesperson)

User-facing fields: **first_name, last_name, phone, email, web, notes**.  
Phones / emails / web are **not** columns here — they stay as `contact` rows owned by the person (or by the agency when no person is known).

```sql
CREATE TABLE agent_person (
  id          TEXT PRIMARY KEY,
  agency_id   TEXT REFERENCES agent(id),   -- optional; null if freelancer / unknown desk
  first_name  TEXT NOT NULL,
  last_name   TEXT NOT NULL,
  notes       TEXT,                        -- e.g. "CSV sales_contact for Golfscape / Pandora"
  is_active   BOOLEAN NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMPTZ DEFAULT now(),
  UNIQUE (agency_id, first_name, last_name)  -- soft; allow nulls-as-distinct per dialect
);
CREATE INDEX idx_agent_person_agency ON agent_person(agency_id);
CREATE INDEX idx_agent_person_name ON agent_person (lower(last_name), lower(first_name));
```

**Rules:**
- **Do not invent people.** Only create `agent_person` when a dossier / CSV / listing page names a human.
- Agency brand contacts without a person name stay on `agent` (today’s default).
- Display name = `first_name || ' ' || last_name`. Role/desk notes go in `notes` or `contact.label` (channel role only — not a substitute for person identity).

**Exposure:** person graph + mobiles → **`plus`**. Admin owns attribution QA. Public CTA stays project/developer (or agency switchboard) until product decides otherwise.

---

### listing (portal / agent ad snapshot) — M10 / M15

Time-bound consumer offer pointing at a development (+ optional typology). **Not** the master `property` row.  
Preferred home for portal **unit ads** and development-card exports (Hauzisha / similar) — including **Ready** rows that we store but do not dossier.

```sql
CREATE TABLE listing (
  id                 TEXT PRIMARY KEY,
  property_id        TEXT REFERENCES property(id) ON DELETE SET NULL,  -- NULL allowed for orphan Ready ads (v0.1.14)
  unit_type_id       TEXT REFERENCES unit_type(id),     -- nullable: whole-development card
  source_url         TEXT NOT NULL,
  publisher_agent_id TEXT REFERENCES agent(id),         -- agency/portal that published the ad
  agent_person_id    TEXT REFERENCES agent_person(id),  -- primary salesperson on the ad (optional)
  status             listing_status NOT NULL DEFAULT 'unknown',
  inventory_class    inventory_class,                   -- off_plan | building | ready | resale (v0.1.14)
  title              TEXT,                              -- page H1 / card title as seen
  first_seen_at      DATE,
  last_seen_at       DATE,
  needs_verification BOOLEAN NOT NULL DEFAULT FALSE,
  notes              TEXT,
  UNIQUE (source_url)
);
CREATE INDEX idx_listing_property ON listing(property_id);
CREATE INDEX idx_listing_unit_type ON listing(unit_type_id);
CREATE INDEX idx_listing_publisher ON listing(publisher_agent_id);
CREATE INDEX idx_listing_person ON listing(agent_person_id);
CREATE INDEX idx_listing_status ON listing(status);
CREATE INDEX idx_listing_inventory_class ON listing(inventory_class);

-- Optional M2M when an ad names multiple people (or both agency switchboard + person).
CREATE TABLE listing_agent (
  id               TEXT PRIMARY KEY,
  listing_id       TEXT NOT NULL REFERENCES listing(id) ON DELETE CASCADE,
  agent_id         TEXT REFERENCES agent(id),          -- agency on the ad (often = publisher)
  agent_person_id  TEXT REFERENCES agent_person(id),   -- named seller on the ad
  role_notes       TEXT,                               -- "CSV sales_contact", "listing agent"
  is_primary       BOOLEAN NOT NULL DEFAULT FALSE,
  CHECK (agent_id IS NOT NULL OR agent_person_id IS NOT NULL),
  UNIQUE (listing_id, agent_id, agent_person_id)
);
CREATE INDEX idx_listing_agent_person ON listing_agent(agent_person_id);
CREATE INDEX idx_listing_agent_agency ON listing_agent(agent_id);
```

**Soft modeling:**
- Prefer `listing.publisher_agent_id` + optional `listing.agent_person_id` for the common single-seller case.
- Use `listing_agent` when the page names multiple people or separates publisher brand from named contact.
- `property_agent` remains the **development-level** “which agencies cover this project” edge — do **not** delete it when listings land.
- Prices / payment on a listing still flow through `price_observation` / `payment_plan_claim` / `claim` with `publisher_class` + source URL — listing does not become a second claim store in v0.1.9.
- **`inventory_class`:** mark Ready unit ads **and** Ready/handed-over development cards. Prefer this field on `listing` (+ `property` when the whole development is Ready) over a separate raw-import table.
- **`property_id` NULL:** allowed for orphan Ready unit ads that have no matched development yet — still store the ad; still **do not** open a research dossier.
- **Research process:** `inventory_class = ready` → **stored, never dossiered for now** (optional future backlog only). Queue work = `off_plan` / `building` (Coming soon → `off_plan`).
- **Hauzisha / similar exports** = **lead lists**. Phone `0730 731 355` = portal CTA (`agent-hauzisha`), never developer. Developments-only for dossiers; Block.ke remains low-trust.

**Exposure:** listing cards on Plus/Admin first; public listing surface waits on product + coverage gate. Ready inventory may appear on Plus/Admin as marked stock — not in the off-plan research corpus.

---

### Gap vs current seeds + migrate path (Loyd-style)

| Today (seeds) | Gap | Migrate when name is evidenced |
|---------------|-----|--------------------------------|
| `agent(name, website)` agency-only | No `first_name` / `last_name` | Add `agent_person` |
| `contact.label = "Loyd Mokaya CSV"` | Person identity stuffed into label | Split label → person; re-own contacts |
| `property_agent` only | No per-ad seller / URL entity | Add `listing` (+ `listing_agent`) from `evidence_url` |
| No `listing` rows | M10 was deferred | Seed listings only from retained dossier URLs — **no invented ads** |

**Example migrate (do not invent beyond seed evidence):**

```text
# Current
agent-block                          name=Block Real Estate
ct-block-loyd-phone                  owner=agent-block  label="Loyd Mokaya CSV"
ct-block-loyd-email                  owner=agent-block  label="Loyd Mokaya CSV"
property_agent(prop-*, agent-block)  role_notes mention CSV sales_contact

# After (when promoting Loyd — name already in contact.label)
agent_person ap-loyd-mokaya:
  agency_id=agent-block  first_name=Loyd  last_name=Mokaya
  notes="CSV sales_contact (Golfscape/Pandora/…); promoted from contact.label"

contact ct-block-loyd-phone:
  owner_type=agent_person  owner_id=ap-loyd-mokaya  label="CSV sales_contact"  # role, not name

contact ct-block-loyd-email:
  owner_type=agent_person  owner_id=ap-loyd-mokaya  label="CSV sales_contact"

# Optional listing from a retained Block URL (e.g. Alba sale page):
listing lst-alba-block-sale:
  property_id=prop-alba-apartments
  source_url=https://block.ke/property/alba-apartments-riruta-…
  publisher_agent_id=agent-block
  agent_person_id=ap-loyd-mokaya   # only if that page / CSV ties Loyd to the ad
```

**Do not** auto-create `agent_person` for every agency contact. Most seed `contact.label` values are desk names (“NRE CSV Galaxy”, “Own It CSV”) — leave those on `agent` until a human name is evidenced.

---

### stakeholder

```sql
CREATE TABLE stakeholder (
  id    TEXT PRIMARY KEY,
  name  TEXT NOT NULL,
  kind  stakeholder_kind NOT NULL,
  notes TEXT
);

CREATE TABLE property_stakeholder (
  property_id    TEXT REFERENCES property(id) ON DELETE CASCADE,
  stakeholder_id TEXT REFERENCES stakeholder(id),
  confidence     SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  needs_verification BOOLEAN NOT NULL DEFAULT FALSE,
  evidence_notes TEXT,
  PRIMARY KEY (property_id, stakeholder_id)
);
```

---

### contact

```sql
CREATE TABLE contact (
  id           TEXT PRIMARY KEY,
  channel      contact_channel NOT NULL,  -- phone | whatsapp | email | url | office | other
  value        TEXT NOT NULL,
  owner_type   party_owner_type NOT NULL, -- includes agent_person (v0.1.9)
  owner_id     TEXT NOT NULL,              -- polymorphic FK by owner_type
  label        TEXT,                       -- channel role only: "sales office", "CSV sales_contact"
                                           -- NOT a substitute for agent_person first/last name
  is_primary   BOOLEAN DEFAULT FALSE,
  UNIQUE (owner_type, owner_id, channel, value)
);
CREATE INDEX idx_contact_owner ON contact(owner_type, owner_id);
CREATE INDEX idx_contact_value ON contact(value);
```

**Ownership map (phone / email / web):**

| Owner | When |
|-------|------|
| `property` / `developer` | Project or SPV sales office CTA |
| `agent` | Agency switchboard / brand inbox / website (no named person) |
| `agent_person` | Named salesperson’s phone, email, personal/desk web |
| `related_party` / `stakeholder` / `group_company` | As today |

**Soft constraint / product rule:** CSV `sales_contact` is often an **agency or agent_person**, not the developer — never copy onto `property` sales office without evidence. Ownership must be explicit.

**Exposure:** project/developer sales contacts → **`public`** (CTA). Full agent / agent_person mobiles / WhatsApp graph → **`plus`**. Ownership QA / mis-attribution fixes → **`admin`**.

---

### source

```sql
CREATE TABLE source (
  id           TEXT PRIMARY KEY,
  url          TEXT,                    -- null only for documented offline
  publisher    TEXT,
  source_type  source_type NOT NULL,
  accessed_at  DATE,
  retained     BOOLEAN NOT NULL DEFAULT TRUE,
  skip_reason  TEXT,                    -- when retained=false (404, HTTP 500, thin)
  notes        TEXT
);
CREATE UNIQUE INDEX idx_source_url ON source(url) WHERE url IS NOT NULL;
CREATE INDEX idx_source_type ON source(source_type);
```

**Always retain** developer/official project site + official brochure/PDF even if thin on price.

---

### research_pass

Encodes source-selection process lock (scan ~10 / retain ≥5).

```sql
CREATE TABLE research_pass (
  id                  TEXT PRIMARY KEY,
  property_id         TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  cycle               SMALLINT,
  sources_evaluated   SMALLINT,
  sources_retained    SMALLINT,
  verified_at         DATE,
  notes               TEXT,
  CHECK (sources_retained IS NULL OR sources_retained >= 0)
  -- Soft process target: retained >= 5 when research complete
);
```

```sql
CREATE TABLE research_pass_source (
  research_pass_id TEXT REFERENCES research_pass(id) ON DELETE CASCADE,
  source_id        TEXT REFERENCES source(id),
  ordinal          SMALLINT,
  PRIMARY KEY (research_pass_id, source_id)
);
```

---

### claim (Fact)

Core of the master-data model.

```sql
CREATE TABLE claim (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  field_key              TEXT NOT NULL,   -- e.g. canonical_name, geography.county, amenities.core
  value_text             TEXT,
  value_json             JSONB,
  confidence             SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical           BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,  -- agent-only / low-conf / uncorroborated
  needs_developer_input  BOOLEAN NOT NULL DEFAULT FALSE,  -- official vs official; do NOT pick a winner
  publisher_class        TEXT,            -- developer | agent | portal | press | seed_csv | search_index
  observed_at            DATE,
  notes                  TEXT
  -- Soft: agent-only consensus confidence <= 3
  -- Soft: is_canonical only if developer-sourced AND no unresolved official conflict
  -- Soft: needs_developer_input and needs_verification are independent (can both be true rarely)
);
CREATE INDEX idx_claim_property_field ON claim(property_id, field_key);
CREATE INDEX idx_claim_canonical ON claim(property_id, field_key) WHERE is_canonical;
CREATE INDEX idx_claim_needs_ver ON claim(property_id) WHERE needs_verification;
CREATE INDEX idx_claim_needs_dev ON claim(property_id) WHERE needs_developer_input;
CREATE INDEX idx_claim_confidence ON claim(confidence);
```

```sql
CREATE TABLE claim_source (
  claim_id   TEXT REFERENCES claim(id) ON DELETE CASCADE,
  source_id  TEXT REFERENCES source(id),
  PRIMARY KEY (claim_id, source_id)
);

CREATE TABLE claim_conflict (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  field_key              TEXT NOT NULL,
  summary                TEXT NOT NULL,
  conflict_class         TEXT NOT NULL DEFAULT 'other',
    -- 'official_vs_official' | 'agent_vs_official' | 'agent_vs_agent' | 'other'
  needs_developer_input  BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,
  resolution             TEXT
    -- e.g. "canonical=developer"; "no winner — needs_developer_input"; revisit in later pass
);

CREATE TABLE claim_conflict_member (
  conflict_id TEXT REFERENCES claim_conflict(id) ON DELETE CASCADE,
  claim_id    TEXT REFERENCES claim(id) ON DELETE CASCADE,
  PRIMARY KEY (conflict_id, claim_id)
);
```

**Canonical / flag algorithm (app layer):**

1. Collect all claims for `(property_id, field_key)`.
2. If developer identity confidence ≥ 4 **and** ≥1 developer-sourced value **and** developer sources **agree** → `is_canonical = true`.
3. If developer sources **disagree** (official vs official) → **no** canonical; **do not pick a winner**; set `needs_developer_input = true` on member claims + conflict; revisit in later verification passes when confidence rises.
4. Agent-only / uncorroborated / sold-out contested → show + `needs_verification` (not `needs_developer_input` unless an official source is also in the conflict set).

**Exposure:** canonical values → **`public`** only when field meets coverage+confidence gate. Full claim graph, conflicts, both `needs_*` flags, confidence → **`admin`** and **`plus`** (Plus may badge; Admin resolves).

---

### price_observation

Always store **multiple** price options (Cycle 2 lock). Never collapse official bands into one hero scalar in the master DB.

```sql
CREATE TABLE price_observation (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  unit_type_id           TEXT REFERENCES unit_type(id),
  amount                 NUMERIC(14,2) NOT NULL,
  currency               CHAR(3) NOT NULL DEFAULT 'KES',
  price_basis            price_basis NOT NULL DEFAULT 'unknown',
  plan_tenor_months      SMALLINT,
  availability_context   TEXT,
  confidence             SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical           BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,
  needs_developer_input  BOOLEAN NOT NULL DEFAULT FALSE, -- official vs official price bands
  publisher_class        TEXT,
  source_id              TEXT REFERENCES source(id),
  notes                  TEXT,
  observed_at            DATE
);
CREATE INDEX idx_price_property ON price_observation(property_id);
CREATE INDEX idx_price_amount ON price_observation(property_id, amount);
CREATE INDEX idx_price_needs_dev ON price_observation(property_id) WHERE needs_developer_input;
```

**Portal price field policy (locked):** **`public`** price columns only if high confidence **AND** high coverage; conflicting official prices → **no** public `price_from` (NDI). **`admin`** / **`plus`** always see the full multi-row table.

---

### payment_plan_claim

```sql
CREATE TABLE payment_plan_claim (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  element                TEXT NOT NULL,   -- deposit_pct | tenor_months | booking_fee | reservation_fee | balance_rule | sharia_available
  value_text             TEXT NOT NULL,
  value_numeric          NUMERIC(14,2),
  confidence             SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical           BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,
  needs_developer_input  BOOLEAN NOT NULL DEFAULT FALSE, -- e.g. official 24-mo vs pack 3-yr
  meets_must_have        BOOLEAN NOT NULL DEFAULT FALSE,
  independent_source_count SMALLINT,
  has_developer_source   BOOLEAN DEFAULT FALSE,
  notes                  TEXT
  -- Soft: agent-only (no developer) → confidence <= 3
);
```

**Must-have threshold (soft check):**

```text
meets_must_have := has_developer_source OR independent_source_count >= 4
```

---

### construction_progress

**Candidate field** — capture when developer publishes; claim set if pages disagree; **`public`** only after coverage gate; **`admin`/`plus`** may show when captured.

```sql
CREATE TABLE construction_progress (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  as_of_date             DATE,
  pct_complete           NUMERIC(5,2),
  floor_label            TEXT,            -- "12 of 19", "A9", "B7"
  block_label            TEXT,
  confidence             SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical           BOOLEAN NOT NULL DEFAULT FALSE, -- only if developer pages agree
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,
  needs_developer_input  BOOLEAN NOT NULL DEFAULT FALSE, -- official vs official snapshots
  source_id              TEXT REFERENCES source(id),
  notes                  TEXT
);
```

---

### media_asset

Listing photos live under `/cursor/stores/self/media/projects/<slug>/` with per-project `manifest.csv`.  
Skill: [photo-collector.md](../agents/photo-collector.md) · Rollup: [media-assets.md](media-assets.md).

```sql
CREATE TYPE media_category AS ENUM (
  'exterior', 'interior', 'amenities', 'plans', 'progress', 'other'
);

CREATE TABLE media_asset (
  id              TEXT PRIMARY KEY,
  property_id     TEXT REFERENCES property(id) ON DELETE CASCADE,  -- nullable if linked only via property_media
  source_id       TEXT REFERENCES source(id),
  asset_type      TEXT NOT NULL,          -- brochure_pdf | flyer | floor_plan | image | video
  url             TEXT NOT NULL,          -- original remote URL
  local_path      TEXT,                  -- store-relative path under media/projects/<slug>/
  title           TEXT,
  category        media_category DEFAULT 'other',
  width_px        INTEGER,
  height_px       INTEGER,
  bytes           INTEGER,
  content_hash    TEXT,                  -- SHA-256 hex; dedup key
  page_url        TEXT,                  -- HTML page where discovered
  confidence      SMALLINT CHECK (confidence BETWEEN 0 AND 5),
  is_official     BOOLEAN DEFAULT FALSE,
  accessed_at     DATE,
  notes           TEXT
);

-- Prefer property_media for gallery membership when one asset is shared or needs sort order.
CREATE TABLE property_media (
  property_id   TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  media_id      TEXT NOT NULL REFERENCES media_asset(id) ON DELETE CASCADE,
  role          TEXT DEFAULT 'gallery',  -- gallery | hero | plan | progress | brochure
  sort_order    INTEGER DEFAULT 0,
  category      media_category,         -- optional override of media_asset.category
  PRIMARY KEY (property_id, media_id)
);
```

---

### feature (controlled vocabulary)

Catalog + scopes + synonyms owned with [feature-taxonomy.md](feature-taxonomy.md).  
**No invented features** — only normalize dossier phrases. Developer/official = canonical; agent-only → `needs_verification`.

```sql
CREATE TABLE feature (
  id                 TEXT PRIMARY KEY,     -- same as slug, e.g. swimming_pool
  slug               TEXT NOT NULL UNIQUE,
  name               TEXT NOT NULL,
  description        TEXT,
  is_active          BOOLEAN NOT NULL DEFAULT TRUE,
  filter_candidate   BOOLEAN NOT NULL DEFAULT FALSE,  -- Coverage agent later
  created_at         TIMESTAMPTZ DEFAULT now()
);

-- Multi-scope: e.g. dsq → apartment + house; clubhouse → development + community
CREATE TABLE feature_scope_map (
  feature_id    TEXT NOT NULL REFERENCES feature(id) ON DELETE CASCADE,
  scope         feature_scope NOT NULL,
  PRIMARY KEY (feature_id, scope)
);

CREATE TABLE feature_synonym (
  feature_id    TEXT NOT NULL REFERENCES feature(id) ON DELETE CASCADE,
  synonym       TEXT NOT NULL,
  PRIMARY KEY (feature_id, synonym)
);
CREATE INDEX idx_feature_synonym_lower ON feature_synonym ((lower(synonym)));
```

**Scopes (v1):** `development` | `apartment` | `house` | `community`.

**Exposure:** synonym table → **`admin`**. Canonical property/unit features → **`public`** only after coverage+confidence gate; full graph → **`admin`/`plus`**.

---

### property_feature

Building / estate amenity claims linked to catalog (additive to free-text `claim(amenities.core)` until Coverage retires free text).

```sql
CREATE TABLE property_feature (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  feature_id             TEXT NOT NULL REFERENCES feature(id),
  raw_text               TEXT,              -- exact dossier phrase
  variant_note           TEXT,              -- e.g. heated rooftop infinity
  confidence             SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical           BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,
  needs_developer_input  BOOLEAN NOT NULL DEFAULT FALSE,
  publisher_class        TEXT,              -- developer | agent | portal | official_filing
  source_id              TEXT REFERENCES source(id),
  observed_at            DATE,
  notes                  TEXT,
  UNIQUE (property_id, feature_id, publisher_class, raw_text)
);
CREATE INDEX idx_property_feature_prop ON property_feature(property_id);
CREATE INDEX idx_property_feature_feat ON property_feature(feature_id);
CREATE INDEX idx_property_feature_canon ON property_feature(property_id) WHERE is_canonical;
CREATE INDEX idx_property_feature_nv ON property_feature(property_id) WHERE needs_verification;
```

---

### unit_type_feature

Typology-bound features (e.g. only `4BR+DSQ` has `dsq`).

```sql
CREATE TABLE unit_type_feature (
  id                 TEXT PRIMARY KEY,
  unit_type_id       TEXT NOT NULL REFERENCES unit_type(id) ON DELETE CASCADE,
  feature_id         TEXT NOT NULL REFERENCES feature(id),
  raw_text           TEXT,
  confidence         SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical       BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification BOOLEAN NOT NULL DEFAULT FALSE,
  publisher_class    TEXT,
  source_id          TEXT REFERENCES source(id),
  notes              TEXT,
  UNIQUE (unit_type_id, feature_id)
);
CREATE INDEX idx_unit_type_feature_ut ON unit_type_feature(unit_type_id);
```

**Soft rules:** `is_canonical` only if developer/official-filing sourced and no unresolved official conflict; agent-only → NV + conf ≤3.

---

### verification_flag

Typed QA beyond the claim boolean (optional enrichment).

```sql
CREATE TABLE verification_flag (
  id           TEXT PRIMARY KEY,
  entity_type  TEXT NOT NULL,           -- claim | price_observation | unit_type | stakeholder | …
  entity_id    TEXT NOT NULL,
  flag_code    TEXT NOT NULL,
    -- needs_developer_input | needs_verification | sold_out_uncorroborated |
    -- official_vs_official | spa_hydration | http_404_snippet | …
  detail       TEXT,
  created_at   TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_ver_flag_entity ON verification_flag(entity_type, entity_id);
CREATE INDEX idx_ver_flag_code ON verification_flag(flag_code);
```

---

### must_have_field (living list)

```sql
CREATE TABLE must_have_field (
  field_key           TEXT PRIMARY KEY,
  is_must_have        BOOLEAN NOT NULL DEFAULT FALSE,  -- research capture must-have
  is_proposed         BOOLEAN NOT NULL DEFAULT FALSE,
  is_portal_candidate BOOLEAN NOT NULL DEFAULT FALSE,  -- may become public later
  is_portal_field     BOOLEAN NOT NULL DEFAULT FALSE,  -- public only after conf+coverage gate
  exposure_public     BOOLEAN NOT NULL DEFAULT FALSE,  -- intended public surface
  exposure_admin      BOOLEAN NOT NULL DEFAULT TRUE,   -- Admin retains almost all research fields
  exposure_plus       BOOLEAN NOT NULL DEFAULT TRUE,   -- Plus retains rich commercial/agent fields
  consensus_num       SMALLINT NOT NULL DEFAULT 0,
  consensus_den       SMALLINT NOT NULL DEFAULT 0,
  coverage_notes      TEXT,  -- e.g. "1/4 listings have developer tracker — not public yet"
  basis_notes         TEXT,
  payment_special     BOOLEAN DEFAULT FALSE
);

-- Public gate (locked): exposure_public / is_portal_field require high confidence AND high coverage
-- (~half of listings lack field → keep public=false). Admin + Plus still expose the underlying data.
-- Example rows in seed/must_have_fields.csv
```

---

## Key relationships (cardinality)

```
geo_place 1 ──< geo_place (parent)
property  }── geo_place (city, neighbourhood, master community)
property 1 ──< property_alias
property 1 ──< unit_type
property 1 ──< claim ──< claim_source >── source
property 1 ──< claim_conflict ──< claim
property 1 ──< price_observation
property 1 ──< payment_plan_claim
property 1 ──< construction_progress
property 1 ──< media_asset
property 1 ──< research_pass ──< source
property 1 ──< property_feature >── feature
unit_type 1 ──< unit_type_feature >── feature
feature 1 ──< feature_scope_map (development|apartment|house|community)
feature 1 ──< feature_synonym
property M ──< property_developer >── M developer
developer }── group_company (0..1)
property M ──< property_related_party >── M related_party
property M ──< property_agent >── M agent          -- development-level agency coverage
agent 1 ──< agent_person (optional agency_id)
property 1 ──< listing >── unit_type? 
listing }── publisher agent; optional primary agent_person
listing 1 ──< listing_agent >── agent? / agent_person?
property M ──< property_stakeholder >── M stakeholder
contact  }── owner (property|developer|agent|agent_person|stakeholder|related_party|group_company)
```

---

## Search / facet indexes (portal-oriented)

| Facet | Source |
|-------|--------|
| Neighbourhood / master community | `property.geo_*` + `geo_place` |
| Developer | `property.primary_developer_id` |
| Beds / size | `unit_type` where `is_canonical` |
| Price options | all `price_observation` rows; public hero only if field passes conf+coverage gate |
| Status | canonical or majority claim for `status` |
| Completion window | claim `completion_estimate` |
| Amenities (legacy free-text) | claim `amenities.core` until Coverage retires |
| Amenities (catalog) | `property_feature` where `is_canonical` (+ coverage gate for public filters) |
| Payment deposit % | `payment_plan_claim` where `meets_must_have` |

---

## Exposure cheat-sheet (`public` | `admin` | `plus`)

| Data | `public` | `admin` | `plus` |
|------|:--------:|:-------:|:------:|
| Canonical name, geo, amenities core | ✓† | ✓ | ✓ |
| Canonical unit types + sizes | ✓† | ✓ | ✓ |
| Canonical payment (threshold met) | ✓† | ✓ | ✓ |
| Multi `price_observation` table | ✗ if official conflict / fail gate | ✓ | ✓ |
| Official-vs-official / `needs_developer_input` | ✗ as resolved scalar | ✓ resolve queue | ✓ badge OK |
| Alternate / `needs_verification` claims | optional light badge | ✓ | ✓ |
| `confidence` scores | ✗ v1 | ✓ | optional |
| `construction_progress` | ✗ until coverage gate | ✓ | ✓ when captured |
| Agent / contact graph | developer/project CTA only | ✓ ownership QA | ✓ full graph |
| `agent_person` + person contacts | ✗ (or agency switchboard only) | ✓ attribution QA | ✓ full |
| `listing` / `listing_agent` | ✗ until public listing surface | ✓ | ✓ ad graph |
| Source URLs + research_pass counts | ✗ / footnote rare | ✓ | ✓ |
| RelatedParty / co_developer typing | public label if relevant† | ✓ | ✓ |
| Canonical `property_feature` / `unit_type_feature` | ✓† | ✓ | ✓ |
| Full feature graph + NV / synonyms | ✗ | ✓ | ✓ |

† = only after **coverage + confidence** gate. Admin/Plus retain full underlying rows regardless.

---

## Migration proposals (from Cycle 2 harvest)

| # | Change | Trigger | Status |
|---|--------|---------|--------|
| M1 | `geo_place.is_master_planned` + `property.geo_master_community_id` | Porini / Tatu City | **In schema 0.1** |
| M2 | Dual cash/instalment on `price_observation.price_basis` + `plan_tenor_months` | Porini + Galaxy | **In schema 0.1** |
| M3 | `construction_progress` table | Galaxy tracker | **In schema 0.1** |
| M4 | Claim fields `total_units`, `storeys`, `block_count`, `built_up_area_sqm` as must-have **proposals** | Porini + Galaxy | Tracked in `must_have_field` (`is_proposed`) |
| M5 | Co-named developers: dual `property_developer(co_developer)` + `related_party(co_developer)` | Tatu City Limited / Porini | **Locked 0.1.1** — simplify later |
| M6 | `needs_developer_input` distinct from `needs_verification` | Official vs official | **Locked 0.1.1** |
| M7 | Portal field gate: high conf AND high coverage | Price + future facets | **Locked 0.1.1** |
| M8 | `construction_progress` = candidate not public must-have | Galaxy tracker | **Locked 0.1.1** |
| M9 | Exposure tiers `public` \| `admin` \| `plus` (+ internal) | Rightmove-class goal confirmed | **Locked 0.1.2** |
| M10 | `listing` + `listing_agent` (+ `agent_person`) for portal ads / named sellers | user ask: person fields + listing relations | **Merged 0.1.9** (DDL; seeds migrate lazily) |
| M11 | Propose merge of dual co_developer links | when ≥N co-named patterns seen | **Deferred** |
| M12 | `feature` / `feature_scope_map` / `feature_synonym` / `property_feature` / `unit_type_feature` | [feature-taxonomy.md](feature-taxonomy.md) + seeds | **Merged 0.1.5** |
| M13 | Seed migrate: Loyd-style `contact.label` → `agent_person` + re-own contacts; optional `listing` from `property_agent.evidence_url` | when promoting named people | **Documented 0.1.9** — do not invent people |
| M14 | `geo_pin` + `geo_method` + optional `poi` / `property_poi` | Geo / POI enricher corpus pass | **Merged 0.1.13** |
| M15 | `inventory_class` on `listing` + `property`; nullable `listing.property_id` for orphan Ready ads | Ready vs off-plan queue lock | **Merged 0.1.14** |

---

## Out of scope (v1)

- User accounts, enquiries, saved searches  
- Transactional LOO / SPA documents as legal truth store  
- MLS feed ingestion  
- Invented GroupCompany / invented property facts / **invented agent_person** rows in seed  
- Auto-creating a `listing` for every `property_agent.evidence_url` without a retained dossier source 

See also: [er-notes.md](er-notes.md) · [changelog.md](changelog.md) · [seed/](seed/)
