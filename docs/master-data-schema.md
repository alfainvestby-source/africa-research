# Master data schema (v1 — evolving via learning loop)

Research outputs should be **entity-shaped** for a relational DB later.

## Entities

### Property (Development)
- `id`, `canonical_name`, `aliases[]`, `status`
- `geography` (city, neighbourhood, street, estate, county, GPS if sourced)
- `primary_developer_id`, `co_developer_ids[]`
- Claims store: `canonical_value` (when developer-backed) + `alternate_claims[]` + `conflicts[]`

### Developer
- `id`, `legal_name`, `trading_names[]`, `website`, `evidence[]`

### GroupCompany
- `id`, `name`, `website`, `evidence[]` — only when parent relationship is evidenced

### RelatedParty (non-parent)
- Use for **`marketing_partner`** (locked default when brand overlap unproven), co-marketer, etc.
- Fields: `id`, `name`, `relationship_type`, `evidence[]`, link to Property and/or Developer

### Agent / Agency
- `id`, `name`, `website`, `type`
- `PropertyAgent` M2M

### Contact
- `channel`, `value`, `owner_type` + `owner_id` (Agent | Developer | Property sales office | Stakeholder | RelatedParty)

### Stakeholder
- financing | contractor | architect | land | other — M2M to Property

### Source
- `url`, `publisher`, `type`, `accessed_at`, `notes`

### Claim
- `field`, `value`, `confidence` (0–5, internal), `source_ids[]`
- Prefer developer claim as **canonical** when developer known + developer sources exist for that field; still keep conflicting claims + flags

## Living must-have list (consensus tracked)

| Field | Must? | Consensus | Basis |
|-------|-------|-----------|-------|
| `canonical_name` / `aliases` | Yes | 2/2 pilots | Official everywhere |
| `status` (claim set OK) | Yes | 2/2 | CSV + portals; conflicts common |
| `geography` neighbourhood + street | Yes | 2/2 | Official |
| `primary_developer` | Yes | 2/2 | Official |
| Related brand / GroupCompany / marketing_partner when signaled | Yes (capture) | **3/4** (Astra + Riara AIMASI/Oasis; **GM SkyPeak**) | Unproven group/platform → `marketing_partner` |
| `unit_types` as claim set | Yes | 2/2 + Riara + **GM** (NEMA 1/2/3BR vs agent duplex/studio) | Official+agent; conflicts |
| Size by type + **gross/plinth tag** | Yes | 2/2 + Misty (Own It **plinth** 58/90/99) | Flyer/brochure; agent can label plinth too; Riara/GM sizes often untagged |
| `amenities` sourced core only | Yes | 2/2 + Riara + **GM** (EIA outline vs agent restaurant/golf adds) | Reject uncorroborated agent adds |
| `completion_estimate` | Yes | 2/2 + Riara + **GM** (Apr vs May 2028) | Multi-source; flag outliers |
| `price_claims[]` (not single scalar) | Yes | 2/2 + Riara + **GM** (bands A–J) | Agents diverge; sold-out vs available |
| `payment_plan` | Yes if ≥4 agent sources OR any developer source | 2/2 + Riara (≥4 on 20%) + Misty (≥4 on 30%) + **GM (≥4 on 20%, no developer → conf 3)** | User 2026-10-15; Misty/GM = clean agent-threshold examples |
| `sources[]` (**≥5 retained**; scan ~10) | Yes | process | Prefer info-dense pages; **official EIA/filing when no microsite** (Riara, Berkeley, **GM**) |
| `agents[]` + `contacts[]` separate entities | Yes | 2/2 + Riara + **GM** (CSV Block ≠ Summit Vista; SkyPeak ≠ primary) | CSV contact ≠ developer |
| Floors / title / GPS | Optional until stronger evidence; **GPS → propose must when developer-sourced**; **tenure/plot when official filing** | **2/3** official GPS (Galaxy JSON-LD; **GM NEMA −1.265143, 36.806272**); Riara: freehold + 0.3339 ha; **GM plot 0.2134 ha** | |
| Named stakeholders | Capture when named | **4/5** (Pandora: Karim CG; Galaxy: CRJE; Riara: Space Planners; **GM: John Mburu & Co.**) | |
| `unit_count` / `total_units` (+ `block_count`) as claim set | **Propose** Yes | **5/5** (Porini 570/24; Galaxy 210 vs 266; Riara 548; Misty agent 276; **GM EIA 440 canonical**) | Never silent scalar if conflicted; agent-only still `needs_verification` |
| `storeys` as claim set | **Propose** Yes | **4/5** (Galaxy 30 vs 19; Riara 23 vs 22; Misty 23 vs 27; **GM EIA 30 vs counsel 29**) | |
| Dual `co_developer` + RelatedParty when co-named | Yes (capture) | **2/2** (Porini Rendeavour/Tatu; **GM Summit Vista/XiangFeng**) | Locked C2 |
| `parking_bays` when official | **Propose** optional→must when filing states | **1/1 half-batch** (Riara **321** on NEMA) | New propose from Riara |
| `construction_progress` when developer tracker exists | **Propose** Yes | **1/2 C2** (Galaxy Lionston tracker); Riara: no tracker (NRE 35% UI only) | Flag official snapshot conflicts |
| `built_up_area_sqm` | **Propose** optional | 1/2 C2 (Porini 58,000) | |
| `price_claims[]` cash **and** instalment columns | **Propose** strengthen | **2/2 C2** + prior pilots; Riara + **Misty CPK cash from 10.5M vs list 12.6M** | Porini packs; Galaxy FAQ dual bands; Misty CPK cash/50%/original stack |
| Developer identity **LinkedIn-only / no microsite** | Capture as lead ≤conf 2 | **1/1 Misty** (Tian Yu) | Never portal-canonical on LinkedIn alone |
| `master_planned_community` geography | **Propose** | 1/2 C2 (Tatu City / Porini) | |
| Neighbourhood **label claim set** (official vs marketing) | **Propose** capture | **1/1** Riara (Thompson vs Lavington vs Kilimani) | Street/plot canonical; labels claim set |
| `reservation_fee` / `deposit_pct` | Nice-to-have until live developer FAQ/LOO | Galaxy: developer **10%** live; Porini FAQ 404; Riara: agent 20% only | Deposit % already covered by payment_plan when developer publishes |

**Rule:** extend this table when new fields repeatedly appear; bump consensus counts; never invent fields without sources. **Propose** rows need coordinator confirmation before hard lock.

## Conflict resolution (locked)
1. Record all material claims + sources  
2. Flag conflicts explicitly  
3. If developer identity confidence high **and** developer-sourced value exists for the field → set **canonical = developer**  
4. Agent-only / low-confidence values: **show** with **`needs_verification`** when low confidence (sold-out uncorroborated, typology absent from developer site, not on other independent sources)
5. **Official vs official** disagreements: **show** both; flag **`needs_developer_input`**; no canonical winner until resolved in a later verification pass
6. **Portal field promotion:** a field becomes a public portal column only if high confidence **and** high coverage across the listing corpus (rough rule: if ~half of listings lack it, keep pro/internal only)
7. **Prices:** always multi-claim; never a single forced `price_from` for the portal until coverage+confidence rules pass
8. **Co-developers:** allow Property↔Developer M2M with roles (`primary`, `co_developer`) **and** RelatedParty links in parallel while we learn
9. **construction_progress:** optional claim set when developer-published; candidate must-have, coverage-gated for portal
