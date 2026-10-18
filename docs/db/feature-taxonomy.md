# Feature taxonomy (v0.1)

**Skill:** Feature taxonomy · **Date:** 2026-10-16  
**Status:** **Merged into `schema.md` v0.1.5** (2026-10-16) — catalog + seeds remain living  
**Rule:** No invented project features — only normalize phrases that appear in research dossiers. Developer-backed = canonical; agent-only = `needs_verification`.

Related: [agents/feature-taxonomy.md](../agents/feature-taxonomy.md) · [schema.md](schema.md) · [decisions.md](../decisions.md) · [seed/](seed/)

---

## Industry patterns used

Inspiration from major listing / proptech surfaces (structure only — **not** a license to invent features absent from dossiers).

| Source | Pattern borrowed | Adapted for Kenya off-plan |
|--------|------------------|----------------------------|
| **Bayut / Property Finder** | Clear split between **building amenities** (gym, pool, parking, CCTV) and **in-unit features** (balcony, fitted kitchen, wardrobes); amenity filters + synonym autocomplete | Scopes `development` vs `apartment` / `house`; synonym column for ingest; filters later coverage-gated |
| **Rightmove / Zoopla** | High-traffic **attributes** as facets (garden, parking, balcony); long amenity lists often free-text / detail | Prefer a short public facet set later; long-tail amenities stay Admin/Plus until coverage proves out |
| **Kenya portals / local agents** | Recurring chips: **backup generator**, **borehole**, **CCTV**, **DSQ**, parking levels; frequent amenity inflation | Kenya-native slugs; agent-only chips seeded with `needs_verification=true`, never as canonical |
| **Majengo / MAJENGO SUITES** ([majengo2-intel](../product/majengo2-intel.md)) | Fixed vacancy amenity chips + custom free-text; rent/PMS-heavy (not off-plan) | Absorb **chip labels as synonyms / catalog rows**; reject custom free-text for public; **no** rent amounts into sale prices; **no invented property_feature links** |
| **Master-plan cities (Tatu-style)** | Estate-level lifestyle (sanctuary, retail boulevard, schools) beyond a single building | Scope `community` for master-plan / SEZ amenities named in dossiers |

**What we did not borrow:** UAE “central A/C” as a default catalog row (not sourced in our Nairobi dossiers this pass); UK freehold/terrace typology as features (tenure stays legal claims); invented sports courts (e.g. basketball) unless a dossier names them; Majengo landlord PMS / short-term stay facets for v1 off-plan public.

**Filter vs detail (intent for Coverage agent):**
- **Filter candidates (later):** Majengo P0 set + dossier staples — swimming_pool, gym, parking, cctv, balcony, dsq, backup_generator, borehole, wifi, furnished, high_speed_lifts (Elevator), gated_security (24/7 Security), coworking, padel — *if* coverage + confidence gate passes.
- **Detail / Admin–Plus:** spa/sauna splits, sky golf, tracking range, fire pit, sun deck, quartz/SPC finishes, agent-inflated chips, Majengo **custom amenity** free-text.

### Majengo P0 chip → our slug map

Source: SPA amenity toggle array in [majengo2-intel §2.2](../product/majengo2-intel.md). Product is **rent / landlord ops**, not off-plan — chips seed vocabulary only.

| Majengo chip | Our `feature.slug` | Scope(s) | Notes |
|--------------|-------------------|----------|-------|
| WiFi | `wifi` | development, apartment | New catalog row; also synonym on `internet_cable` for dossier “internet/cable” |
| Parking | `parking` | development | Exact synonym `Parking` |
| Backup Generator | `backup_generator` | development | Exact synonym |
| Borehole | `borehole` | development | Exact synonym |
| Swimming Pool | `swimming_pool` | development | Exact synonym |
| Gym | `gym` | development | Exact synonym |
| 24/7 Security | `gated_security` | development | Synonyms: `24/7 Security`, `Security`, `Secure` |
| CCTV | `cctv` | development | Exact synonym |
| Balcony | `balcony` | apartment | Exact synonym |
| Furnished | `furnished` | apartment | New catalog row (rent-chip; rare in sale dossiers — **no property links until sourced**) |
| Elevator | `high_speed_lifts` | development | Synonyms: `Elevator`, `elevator`, `elevators` (slug kept; display name “Lifts / elevator”) |

Extra Majengo UI labels (not in the 11-array): `Kitchen` → synonym of `fitted_kitchen`; `Water` → **not** auto-mapped (ambiguous vs borehole) — leave unmapped until a dossier/listing phrases water clearly; `Security` / `Secure` → `gated_security`.

---

## Scopes (v1)

| Scope | Meaning | Dossier examples |
|-------|---------|------------------|
| `development` | Shared building / estate amenities | Gym, pool, CCTV, lifts, clubhouse |
| `apartment` | In-unit apartment features | Balcony, DSQ, study, fitted kitchen, smart home |
| `house` | House / townhouse unit features | Staff quarters (DSQ synonym), private garden — **only when dossier-sourced** |
| `community` | Master-plan / precinct amenities | Retail boulevard, wildlife sanctuary access, Gemini Square retail |

A feature may list **multiple scopes** (e.g. `clubhouse` → development + community; `dsq` → apartment + house).

---

## Catalog (controlled vocabulary)

Slugs are stable IDs. Synonyms are ingest/normalize aids only.  
**first_seen_in** = dossier(s) that justified inclusion (not exhaustive property coverage).

### development

| slug | name | synonyms | first_seen_in |
|------|------|----------|---------------|
| `swimming_pool` | Swimming pool | pool; heated pool; rooftop pool; infinity pool; courtyard pool; heated rooftop infinity pool; full-length pool | Pandora, Porini, Galaxy, Longines, Gemini, Diamond, Berkeley, Riara, Misty, Golden |
| `gym` | Gym / fitness | fitness; wellness gym; fully fitted gym | Most dossiers with amenities |
| `cctv` | CCTV / video security | 24/7 CCTV; 24hr CCTV; CCTV surveillance | Pandora, Astra, Porini, Galaxy, Longines, Diamond, … |
| `parking` | Parking | ample parking; dedicated parking; visitor parking; podium parking | Most |
| `backup_generator` | Backup generator | generator | Astra (dev); Berkeley/Riara/Golden/Longines (agent or ESIA) |
| `borehole` | Borehole water | water borehole; onsite borehole | Astra (dev flyer); Diamond (dev); Berkeley/Riara (official); Longines/Misty (agent NV) |
| `high_speed_lifts` | Lifts / elevator | Elevator; elevator; elevators; high-speed elevators; lifts | Astra, Galaxy, Diamond, Misty (agent), Porini agent NV; **Majengo** Elevator chip |
| `kids_play` | Children’s play area | children’s play; kids play; kids’ playground; indoor children’s playroom | Pandora, Porini, Galaxy, Longines, Gemini, Diamond, Misty |
| `barbecue` | Barbecue area | BBQ; barbecue; rooftop BBQ | Porini, Longines (outdoor cinema + BBQ), Gemini, Misty |
| `clubhouse` | Clubhouse | club house | Porini (dev); Golden/Misty agent NV |
| `cinema` | Cinema / theater | indoor cinema; outdoor cinema; private theater; home theater | Longines, Galaxy, Gemini; Misty agent NV |
| `coworking` | Co-working | co-working; coworking; serviced co-working | Pandora, Longines, Gemini (dev); Berkeley agent NV |
| `sauna` | Sauna | male/female saunas | Pandora (spa/sauna), Galaxy (spa & sauna), Gemini (separate saunas); Golden agent NV |
| `spa` | Spa | spa; Serenity Spa (partner-branded amenity) | Pandora, Galaxy; Gemini partnership |
| `yoga` | Yoga / wellness room | yoga room; yoga & wellness deck | Galaxy, Diamond, Gemini |
| `concierge` | Concierge | dedicated concierge | Pandora, Diamond |
| `reception` | Reception / lobby | reception; hotel-style lobby | Diamond, Misty, Gemini, Golden |
| `lounge` | Lounge | resident lounge; sky lounge; coffee lounge; piano lounge | Pandora, Galaxy, Longines, Diamond, Gemini |
| `restaurant_cafe` | Restaurant / café | restaurant; café; cafés; coffee lounge | Pandora, Berkeley, Diamond, Longines (hotel restaurant) |
| `gated_security` | Gated / manned security | 24/7 Security; Security; Secure; gated access; 24/7 security; manned entrance security | Porini, Diamond, Misty; **Majengo** 24/7 Security chip |
| `access_control` | Access control | access control | Astra flyer |
| `indoor_gaming` | Indoor gaming / games room | games room; game room; indoor gaming; patio gaming; pool room (billiards) | Pandora, Astra, Longines (pool room), Berkeley |
| `green_area` | Landscaped green / garden (shared) | green area; landscaped garden; landscaped courtyards; zen garden; courtyard; rooftop art garden | Pandora, Astra, Porini, Gemini, Berkeley, Riara, Galaxy |
| `convenience_store` | Convenience store / mini-mart | convenience store; mini mart; supermarket & shop | Astra, Diamond, Gemini (commercial hub) |
| `internet_cable` | Internet / cable | internet/cable; fibre (agent); WiFi (cross-synonym) | Astra (dev); Misty fibre agent NV |
| `wifi` | WiFi | WiFi; Wi-Fi; wireless internet | **Majengo P0** chip — catalog only until dossier/listing sources a link |
| `social_corridor` | Social corridor | social corridor | Astra flyer |
| `tracking_range` | Tracking range | tracking range | Astra flyer only |
| `sun_deck` | Sun deck | sun deck | Porini brochure |
| `fire_pit` | Fire pit | fire pit | Gemini |
| `laundry_shared` | Shared / 24h laundry | 24-hour laundry | Longines |
| `pet_friendly` | Pet-friendly facilities | pet-friendly | Longines |
| `fingerprint_access` | Fingerprint door access | fingerprint door locks | Longines |
| `padel` | Padel court | sky padel; padel; sky-high padel court | Longines, Gemini; Galaxy agent NV |
| `mini_golf` | Mini-golf / sky golf | sky golf; indoor mini-golf; mini golf | Longines, Galaxy; Golden agent NV |
| `changing_rooms` | Changing rooms | changing rooms | Golden EIA |
| `rainwater_harvest` | Rainwater harvest | rainwater harvest | Riara NEMA |
| `water_storage` | Bulk water storage | storage tanks | Riara NEMA (750 m³) |
| `pharmacy` | Pharmacy (on estate) | pharmacy; chemist | Gemini BD hub (dev); Diamond agent NV |
| `dry_cleaning` | Dry cleaning | dry cleaning | Gemini agent NV |
| `guest_room` | Guest room | guest room | Gemini agent NV |
| `jogging_track` | Jogging track | jogging track | Misty/Galaxy agent NV |
| `rooftop_solar` | Rooftop solar | rooftop solar; solar water heating | Astra/Berkeley agent NV |
| `jacuzzi` | Jacuzzi | jacuzzis | Galaxy agent NV |
| `daycare` | Kids’ daycare | daycare | Galaxy agent NV |
| `beauty_parlor` | Beauty parlor | beauty parlor | Galaxy agent NV |
| `library` | Library | library | Porini agent NV (Vorsa) |
| `conference_room` | Conference room | conference room | Riara agent NV |
| `smart_lock` | Smart lock (building/unit access) | smart lock | Berkeley marketing |

### apartment

| slug | name | synonyms | first_seen_in |
|------|------|----------|---------------|
| `balcony` | Balcony / terrace | Balcony; private balcony; terraces/balconies; terrace | Pandora, Porini (every unit), Diamond, Misty; **Majengo** Balcony chip |
| `furnished` | Furnished | Furnished; fully furnished; semi-furnished | **Majengo P0** rent chip — catalog only; no off-plan property_feature until sourced |
| `ensuite` | Ensuite bathroom | ensuite; master ensuite; all ensuite | Typology copy (Porini 2/3BR; Berkeley agent NV “all ensuite”) |
| `fitted_kitchen` | Fitted kitchen | Kitchen; fitted kitchen; hob/hood/oven; fully equipped kitchen | Porini, Misty, Pandora finishes; Majengo UI label Kitchen |
| `dsq` | DSQ (domestic staff quarters) | DSQ; staff quarters; maid’s room | Pandora, Diamond unit types |
| `study` | Study | study | Pandora, Diamond |
| `smart_home` | Smart home | smart home; facial recognition; face-scan access | Pandora (dev); Misty (agent); Diamond agent NV |
| `double_height_ceiling` | Double-height ceiling | double-height ceilings | Pandora |
| `quartz_countertops` | Quartz countertops | quartz counters | Porini |
| `spc_parquet` | SPC parquet flooring | SPC parquet | Porini |
| `in_unit_laundry` | In-unit laundry | laundry area; laundry | Porini floor plans; Diamond |
| `walk_in_closet` | Walk-in closet | walk-in-closet | Porini 3BR; Diamond layouts |
| `ai_smart_toilet` | AI / smart toilet | AI toilets; smart toilets | Diamond agent NV |
| `automated_curtains` | Automated curtains | automated curtains | Diamond agent NV |

### house

*(Sparse in current apartment-heavy corpus — rows only where dossiers use house-like language or shared Kenya dwelling features.)*

| slug | name | synonyms | first_seen_in |
|------|------|----------|---------------|
| `dsq` | DSQ / staff quarters | staff quarters; DSQ | Same slug as apartment — dual scope |
| `private_garden` | Private garden | private garden | **Not yet dossier-sourced as unit private garden** — reserved; do not seed until a dossier states it |
| `compound` | Compound / gated compound | compound | Prefer `gated_security` when copy means estate gate; add seed only when house-compound language appears |
| `parking_bay` | Dedicated parking bay | parking space; parking bay | Porini (1–2 bays by unit type in packs); Riara bay counts = development |

### community

| slug | name | synonyms | first_seen_in |
|------|------|----------|---------------|
| `retail_boulevard` | Retail boulevard / estate retail | retail boulevard; retail; World Food Avenue; Gemini Square | Pandora, Longines commercial, Gemini |
| `wildlife_sanctuary` | Wildlife sanctuary access / views | Tatu Wildlife Sanctuary; sanctuary views | Porini / Tatu |
| `clubhouse` | Clubhouse (community hub) | clubhouse | Porini (dual scope) |
| `estate_schools_access` | Schools within master community | Crawford; Nova Pioneer (named as estate context) | Porini brochure location context |
| `commercial_hub` | Commercial / convenience hub | convenience store; pharmacy; restaurants; cafés; co-working hub | Gemini BD Phase 2 commercial hub |

---

## Synonym normalization rules

1. Map free text → **one slug** via synonyms (case-insensitive; ignore punctuation).  
2. Prefer **split** when evidence distinguishes (`spa` vs `sauna`); keep combined source phrase in `property_feature.raw_text`.  
3. Pool variants (heated / rooftop / infinity / courtyard) → `swimming_pool`; optional `variant_note` on link row.  
4. Co-working / coworking / co working → `coworking`.  
5. DSQ / staff quarters / maid’s → `dsq`.  
6. Never create a slug from industry portals alone.

---

## Proposed DDL (for DB steward merge)

```sql
CREATE TYPE feature_scope AS ENUM (
  'development',
  'apartment',
  'house',
  'community'
);

CREATE TABLE feature (
  id            TEXT PRIMARY KEY,          -- same as slug, e.g. swimming_pool
  slug          TEXT NOT NULL UNIQUE,
  name          TEXT NOT NULL,             -- display name
  description   TEXT,
  is_active     BOOLEAN NOT NULL DEFAULT TRUE,
  -- Public filter candidacy is decided by Coverage agent later; default false
  filter_candidate BOOLEAN NOT NULL DEFAULT FALSE,
  created_at    TIMESTAMPTZ DEFAULT now()
);

-- Multi-scope: swimming_pool is development-only; dsq is apartment+house
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

-- Property-level amenity / feature claim (building or estate)
CREATE TABLE property_feature (
  id                     TEXT PRIMARY KEY,
  property_id            TEXT NOT NULL REFERENCES property(id) ON DELETE CASCADE,
  feature_id             TEXT NOT NULL REFERENCES feature(id),
  raw_text               TEXT,              -- exact dossier phrase
  variant_note           TEXT,              -- e.g. "heated rooftop infinity"
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

-- Typology-specific features (e.g. only 4BR+DSQ has DSQ)
CREATE TABLE unit_type_feature (
  id                     TEXT PRIMARY KEY,
  unit_type_id           TEXT NOT NULL REFERENCES unit_type(id) ON DELETE CASCADE,
  feature_id             TEXT NOT NULL REFERENCES feature(id),
  raw_text               TEXT,
  confidence             SMALLINT NOT NULL CHECK (confidence BETWEEN 0 AND 5),
  is_canonical           BOOLEAN NOT NULL DEFAULT FALSE,
  needs_verification     BOOLEAN NOT NULL DEFAULT FALSE,
  publisher_class        TEXT,
  source_id              TEXT REFERENCES source(id),
  notes                  TEXT,
  UNIQUE (unit_type_id, feature_id)
);
CREATE INDEX idx_unit_type_feature_ut ON unit_type_feature(unit_type_id);
```

**Soft rules**
- `is_canonical` only if developer/official-filing sourced **and** no unresolved official conflict on that amenity.
- Agent-only → `needs_verification`; confidence ≤ 3.
- Do not delete free-text `claim(field_key=amenities.core)` yet — taxonomy links are additive until Coverage retires free text.

**Exposure (intent)**
| Data | public | admin | plus |
|------|:------:|:-----:|:----:|
| Canonical property features (coverage-gated) | ✓† | ✓ | ✓ |
| Full property_feature graph + NV | ✗ | ✓ | ✓ |
| unit_type_feature (DSQ/study on typology) | ✓† | ✓ | ✓ |
| Synonym table | ✗ | ✓ | ✓ |

† Coverage + confidence gate.

---

## Seed files

| File | Purpose |
|------|---------|
| [seed/features.csv](seed/features.csv) | Catalog rows |
| [seed/feature_scopes.csv](seed/feature_scopes.csv) | Scope M2M |
| [seed/feature_synonyms.csv](seed/feature_synonyms.csv) | Synonym map (subset) |
| [seed/property_features.csv](seed/property_features.csv) | Links from dossiers for properties already in `properties.csv` |
| [seed/unit_type_features.csv](seed/unit_type_features.csv) | Typology-bound features (DSQ, study, balcony where clear) |

**Coverage note:** `property_features.csv` covers all **11** seeded properties (incl. Golden, Longines, Berkeley). Catalog may still hold slugs awaiting richer unit_type links.

---

## Handoff

1. **DB steward:** merge DDL into `schema.md` + changelog; confirm FKs.  
2. **Coverage agent:** score which `feature` slugs become `filter_candidate` / public.  
3. **Research agents:** prefer taxonomy slugs in new dossiers; keep raw amenity prose in claims until migration complete.
