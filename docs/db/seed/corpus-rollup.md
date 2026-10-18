# Seed corpus rollup — full inventory

**Last refreshed:** 2026-10-18  
**Denominator:** **52** research dossiers ↔ **52** rows in `properties.csv`  
**Locks:** [decisions.md](../../decisions.md) · **Schema:** [schema.md](../schema.md) v0.1.14+ (`inventory_class`) · **Coverage:** [db-coverage-pass-2026-10-18.md](../../../internal/db-coverage-pass-2026-10-18.md)  
**Prior slice:** [wave-b-rollup.md](wave-b-rollup.md)

---

## Coverage check

| Check | Result |
|-------|--------|
| Dossiers seeded | **52** |
| `properties.csv` rows | **52** |
| `inventory_class` blank | **0** (39 `building` / 13 `off_plan`) |
| Nairobi `NBO-001`…`017` | **17/17** |
| National / discovery IDs | **NAK-001**, **MSA-001**, **ELD-001**, **KWA-001**, **DIA-001**, **DISC-NBO-001/004/005/006/007–031**, **DISC-CAPRICORN** |
| Skipped Ready (not researched) | Sunpark I, Oak & Ivy |
| Skipped / held | Gemini Hub; Alina Harbour; Ambra (thin) |
| 70% public gate pass | Identity/geo/IC/map/units/prices/payments/features — see coverage report; bathrooms + exact GPS + progress **FAIL** |

---

## ID scheme (national + discovery)

| Prefix | Geography | Examples |
|--------|-----------|----------|
| `NBO-*` | Nairobi metro | NBO-001…017 |
| `NAK-*` | Nakuru / Rift | **NAK-001** Kings Summit |
| `MSA-*` | Mombasa / Coast | **MSA-001** Sensei Nyali |
| `ELD-*` | Eldoret / Uasin Gishu | **ELD-001** Kings Square Ph2 |
| `KWA-*` | Kwale / Diani coast | **KWA-001** Kai |
| `DIA-*` | Diani (project-scoped) | **DIA-001** 108 Residences |
| `DISC-*` | Discovery (no CSV NBO yet) | DISC-NBO-001 Canto; 004 Ankori; 005 Nouveau; 006 Brookside Oak; **007–011 Block 2028 Tier A**; **012–015 Elegant**; **016–018 Jafu**; **019–023 Wave B**; **024–030 Slice C**; **031 Spectre**; DISC-CAPRICORN |

---

## Nairobi inventory (NBO-001…017)

| ID | Slug | Developer (seed) | Conf | Key flags |
|----|------|------------------|-----:|-----------|
| NBO-001 | golden-mansion | Summit Vista (+ XiangFeng co_dev dual; SkyPeak mkt) | 5 | NEMA; CSV SkyPeak ≠ primary |
| NBO-002 | pandora-residences | A-One Corporation | 5 | Unit mix NDI |
| NBO-003 | riara-oasis | Riara Oasis Limited; AIMASI mkt | 5 | NEMA |
| NBO-004 | porini-point | Rendeavour (+ Tatu co_dev dual) | 5 | Payment tenor NDI |
| NBO-005 | astra-bay-residence | Wimax; Laureland mkt | 5 | |
| NBO-006 | golfscape-residences | WH Harmony | 5 | Hero vs list price NDI |
| NBO-007 | diamond-bay-residences | Henbon | 5 | 8.84 vs 9.34 NDI |
| NBO-008 | longines-bay-kilimani | Nanchong (+ GroupCompany) | 5 | Blocks NDI |
| NBO-009 | gemini-residency-phase-2 | Staroot; Proxima mkt | 5 | Completion NDI |
| NBO-010 | berkeley-homes | Rarlon | 4 | 361 vs 360 NDI; Procmura false |
| NBO-011 | lesonia-residences | Lesonia trading brand | 3/0 | Price NDI; legal unknown |
| NBO-012 | luna-oak-residency | Mingland; Oak Group mkt | 5 | 14.8 vs 11.9 NDI |
| NBO-013 | galaxy-one | Lionston | 5 | Progress NDI |
| NBO-014 | alba-apartments | Nanchang | 3 | Own It agent; status conflicted |
| NBO-015 | plumeria-residency | Riara Plumeria NEMA | 5 | Own It agent; Golden Apple wrong |
| NBO-016 | polaris-residency | **unknown** | 0 | Own It agent; status conflicted |
| NBO-017 | misty-springs | Tian Yu | 2 | Own It agent |

---

## National + discovery (non-NBO)

| ID | Slug | City | Developer | Conf | Key flags |
|----|------|------|-----------|-----:|-----------|
| **NAK-001** | kings-summit-nakuru | Nakuru / Milimani | **Kings Developers Ltd** + **Royal Group** | **5** | First national; official **9M vs blog 8M NDI**; 3BR/120 sqm; flexible off-plan soft |
| **MSA-001** | sensei-nyali | Mombasa / Nyali | **Hass Consult Limited** (shared) | **4** | First coast; **30-mo payment canonical**; from 24M; ≠ Benford Greenwood |
| **ELD-001** | kings-square-eldoret-ph2 | Eldoret / Airport Rd | **Kings Developers Ltd** + **Royal Group** | **5** | First Eldoret; typed 4M/5M; payment must-have **not** met; ≠ Phase 1 |
| **KWA-001** | kai-diani | Diani / Kwale | **Ayce Investments Limited** | **5** | First KWA; Hass exclusive agent RelatedParty; Innova RelatedParty NV; unit taxonomy + completion **NDI**; Hass from 10.5M / 18-mo NV |
| **DIA-001** | 108-residences-diani | Diani Beach Rd | **Omicron Resources** | **4** | First DIA; Daiga+Dunhill marketing_partners; 68 units; payment must-have **not** met |
| **DISC-NBO-001** | canto | Nairobi / School Lane | **VAAL Real Estate** | **5** | USD primary; studio+1BR from **49k/68k**; deposit must-have **not** met; Apr 2028 |
| **DISC-NBO-004** | ankori | Nairobi / Rhapta Rd | **Hass Consult Limited** | **4** | **30-mo payment canonical**; from 6.5M; deposit % **not** met; ≠ Galaxy One |
| **DISC-NBO-005** | nouveau | Nairobi / Lenana Rd | **Hass Consult Limited** | **4** | Payment **tenor NDI** (28/30/21); Q4 2028 canonical; from 6.5 vs 6M soft NDI |
| **DISC-NBO-006** | brookside-oak | Nairobi / Muguga Green | **Van Tung Company** (legal NV) | **3** | Oak Group marketing_partner (reuse Luna); microsite **9.9M vs Oak 8.2M NDI**; ≠ Luna Oak |
| **DISC-CAPRICORN** | capricorn-kilimani | Nairobi / Wood Ave | **Staroot (5)** + **Mulika Garden co_developer** dual; **Proxima marketing_partner** | 5/4 | Deposit min **20%** FAQ canonical; agent 30% secondary; microsite 500 this pass; ≠ Staroot Residency |
| **DISC-NBO-007** | 237-lulu | Nairobi / Garden City | **Mi Vida Homes** | **5** | `off_plan`; official **4.4M vs typed 6.93M+ NDI** → public **POA**; developer payment canonical |
| **DISC-NBO-008** | highpoint-336 | Nairobi / Kilimani | **Highpoint Development Ltd** | **4** | `building`; microsite 500; from **9.9M** indexed; progress 8% vs 40% NDI; ≠ Golfscape Highpoint partner |
| **DISC-NBO-009** | jabali-towers | Nairobi / Tatu Central | **Rendeavour** | **5** | `off_plan`; Dec **2028** + **10%/36-mo** payment canonical; size schedules NDI; ≠ Porini Point |
| **DISC-NBO-010** | balkis-residences | Nairobi / Riverside | **Sunmon Group** (Hauzisha conf **2** NV) | **2** / face **5** | `building`; balkisriverside.com face; admin-only developer gate; agent from **7.9M** |
| **DISC-NBO-011** | hephe-palace | Nairobi / Westlands | **Sequoia Real Estate** | **5** | `building`; Sequoia China Ltd RP; **644** EIA; agent from ~**6.2M**; ≠ Karura Forest Views Block alias |
| **DISC-NBO-012** | forestview-residences | Nairobi / Eldama Ravine | **Elegant Properties** | **5** trading | `inventory_class=building`; from **29.5M**; June 2027; payment short of ≥4; ≠ Casa Karura / Lofts@Karura |
| **DISC-NBO-013** | donyo-hill-residences | Nairobi / Donyo Sabuk × Peponi | **Elegant Properties** | **5** trading | `inventory_class=building`; from **27.9M**; 2/3/4BR; payment **not** met; ≠ Ridge / Manor |
| **DISC-NBO-014** | 48-treehouse | Nairobi / Peponi Rd | **Elegant Properties** | **5** trading | `inventory_class=building`; **48** units 4BR; **77.9M vs 73M NDI**; ≠ Oakland |
| **DISC-NBO-015** | sunpark-residence-ii | Syokimau / Chady Rd | **Elegant Properties** | **5** trading | `inventory_class=building`; Phase **II only** (skip Ready I); from **8M**; 10 acres |
| **DISC-NBO-016** | citrine-heights | Nairobi / Westlands Rd | **Jafu Real Estate Group** | **4** trading | `inventory_class=off_plan`; ~7.3M agent; payment **not** met; no official Citrine page |
| **DISC-NBO-017** | auris-residence | Nairobi / Westlands | **Jafu Real Estate Group** | **4** trading | `inventory_class=building`; studio/1/2BR ~5.5M agent; completion **NDI**; payment conflict |
| **DISC-NBO-018** | serene-manor | Nairobi / Turbo–Lenana | **Jafu Real Estate Group** | **5** soft | `inventory_class=building`; featured on jafugroupkenya.com; **20%** agent must-have met |
| **DISC-NBO-019** | libra-residences | Nairobi / George Padmore | **GLBC Group** | **5** trading | `inventory_class=building`; band **17–25M**; payment **not** met; NEVER `0730` |
| **DISC-NBO-020** | only-you | Nairobi / Elgeyo Marakwet | **primary null**; Onlyou Investments Ltd RP; GLBC mkt only | **0** primary | `inventory_class=building`; EIA GPS; **20%** agent must-have; do **not** invent GLBC primary |
| **DISC-NBO-021** | gaia-brookside | Nairobi / Brookside Gardens | **Wonder Properties** | **5** trading | `inventory_class=building`; completion **NDI**; payment **not** met |
| **DISC-NBO-022** | diplomat-residencies | Nairobi / Peponi (Westgate) | **Wonder Properties** (shared) | **5** trading | `inventory_class=building`; **20%** agent must-have; microsite 502 this pass |
| **DISC-NBO-023** | aya-luxury-residence | Nairobi / Othaya × Makueni | **Whitehorse** (ex-AAD); Sandoral RP NDI | **5** / **1** | `inventory_class=building`; from **7.5M** LinkedIn; Sandoral **never** primary |
| **DISC-NBO-024** | rhapta-one | Nairobi / Rhapta Rd | **Oasis Development** | **2** trading | `inventory_class=building`; ~7.5–7.8M agent; payment **not** met |
| **DISC-NBO-025** | alina-valley | Nairobi / Likoni Ln | **Wonder Properties** (reuse) | **5** | `building`; **20%** must-have; completion **NDI**; ≠ Harbour |
| **DISC-NBO-026** | montbleu | Nairobi / Muthithi Plot 37 | **primary null**; Muthithi Square + M-Group RPs | **0** primary | `off_plan`; NDI SPV lock |
| **DISC-NBO-027** | marina-bay-2 | Nairobi / Sports Rd | **M-Group Developer** | **4** trading | `building`; **10/10/75/5** must-have; ≠ Phase 1 Ready |
| **DISC-NBO-028** | atreus-brookside | Nairobi / Brookside Grove | **Atreus Ventures Ltd** EIA; Sunmon/Lesto RP | **5** EIA | `off_plan`; EIA GPS; **20%** must-have |
| **DISC-NBO-029** | grand-premier | Nairobi / Argwings (Lavington) | **Whitehorse** (reuse) | **5** | `off_plan` Coming soon; **Ready lean NDI** |
| **DISC-NBO-030** | rosewood-park | Nairobi / Rose Ave | **Whitehorse** (reuse) | **5** | `off_plan` Coming soon; **Ready lean + rentals NDI** |
| **DISC-NBO-031** | spectre-residences | Nairobi / Westlands Rd (AU Close) | **AYA Real Estate** (**new**; ≠ Whitehorse / DISC-NBO-023) | **5** | `off_plan`; spectre.ke **9.7/12.4/18.4M** vs AYA hub **8.8/11.2/16.7M** **NDI** → **POA**; payment **100K/20%/36-mo** canonical; Karim marketing_partner; Maps CID pending |

---

## Shared entities across geography

| Entity | Used by |
|--------|---------|
| `dev-kings-developers-ltd` + `grp-royal-group-of-companies` | NAK-001, ELD-001 |
| `dev-hass-consult-limited` (conf 4) | DISC-NBO-005 Nouveau, MSA-001 Sensei, **DISC-NBO-004 Ankori** |
| `rp-hassconsult-kai` (exclusive agent — **not** primary) | **KWA-001** Kai |
| `dev-staroot-real-estate` + `rp-proxima-real-estate` | NBO-009 Gemini, DISC-CAPRICORN (+ Brookside agent listing) |
| `dev-mulika-garden` + `rp-mulika-garden` (dual co_developer) | DISC-CAPRICORN only |
| `rp-oak-group-residences` (marketing_partner) | NBO-012 Luna Oak, **DISC-NBO-006 Brookside Oak** — sibling cards; do not merge |
| `dev-mi-vida-homes` | **DISC-NBO-007** 237 Lulu (Garden City) |
| `dev-highpoint-development-ltd` | **DISC-NBO-008** Highpoint 336 — ≠ Highpoint marketing_partner on Golfscape |
| `dev-rendeavour` (reuse) | NBO-004 Porini + **DISC-NBO-009** Jabali Towers |
| `dev-sunmon-group` (conf 2 NV) | **DISC-NBO-010** Balkis — admin-only developer gate |
| `dev-sequoia-real-estate` | **DISC-NBO-011** Hephé Palace (+ Sequoia China RP) |
| `dev-elegant-properties` (conf 4 seed / 5 trading dossiers) | **DISC-NBO-012…015** Elegant wave — never Hauzisha `0730 731 355` |
| `rp-sic-prime` (marketing_partner conf 2) | DISC-NBO-015 Sunpark II channel only |
| `dev-jafu-real-estate-group` (trading conf 4; SPV unknown) | **DISC-NBO-016…018** Jafu Wave A — website contact only; never `0730 731 355` |
| `dev-glbc-group` (trading conf 5; SPV unknown) | **DISC-NBO-019** Libra primary; **DISC-NBO-020** Only You = marketing_partner RelatedParty only |
| `dev-wonder-properties` (trading conf 5; SPV unknown) | **DISC-NBO-021** Gaia + **DISC-NBO-022** Diplomat — one shared row |
| `dev-whitehorse-real-estate` (trading conf 5; AAD prior face) | **DISC-NBO-023** AYA; **029** Grand Premier; **030** Rosewood — Sandoral NDI never primary |
| `dev-wonder-properties` | Gaia + Diplomat + **Alina Valley** |
| `dev-m-group-developer` | **Marina Bay 2** primary; **Montbleu** marketing_partner RP only |
| `dev-oasis-development-company` | **Rhapta One** only (conf 2) |
| `dev-atreus-ventures-ltd` | **Atreus Brookside** EIA primary |
| `dev-aya-real-estate` (**new**; ≠ Whitehorse) | **DISC-NBO-031** Spectre only — do not merge with `prop-aya-luxury-residence` |
| `rp-karim-exclusives-spectre` (marketing_partner) | Spectre exclusive sales + concept — **not** `stk-karim-cg` |

---

## Pattern index (additions)

| Pattern | Projects |
|---------|----------|
| First **non-Nairobi** city | NAK-001 Nakuru |
| First **coast** (Mombasa) | MSA-001 |
| First **Eldoret** | ELD-001 |
| First **Kwale/Diani KWA** | KWA-001 Kai |
| First **DIA** id | DIA-001 108 Residences |
| Discovery IDs pending NBO allocation | Block 2028 **007–011**; Elegant 012–015; Jafu 016–018; Wave B 019–023; Slice C 024–030; **Spectre 031** |
| Official vs official typed floors **NDI** → POA | **Spectre** (spectre.ke vs AYA hub); also Lulu / Brookside patterns |
| New developer brand ≠ name-alike project | **AYA Real Estate** (Spectre) ≠ Whitehorse **AYA Luxury Residence** |
| Block 2028 Tier A seed | Lulu (Mi Vida POA); Highpoint 336; Jabali (Rendeavour); Balkis (Sunmon NV); Hephé (Sequoia) |
| Hauzisha Slice C | Rhapta (Oasis); Alina (Wonder); Montbleu (null primary); Marina Bay 2 (M-Group); Atreus (EIA); GP+Rosewood (Whitehorse Ready lean) |
| Null primary + RP faces | Only You; **Montbleu** (Muthithi Square / M-Group NDI) |
| Ready lean while `off_plan` process | **Grand Premier**; **Rosewood Park** — steward NDI before `ready` |
| Elegant Properties multi-site wave | Forestview, Donyo Hill, 48 Treehouse, Sunpark II (`building`); Ready I / Oak & Ivy **skipped** |
| `inventory_class=building` from UC gallery evidence | Elegant four; Hauzisha Wave B five |
| Jafu Real Estate Group Wave A | Citrine (`off_plan`); Auris + Serene Manor (`building`) |
| Hauzisha Wave B (skip Gemini Hub) | Libra (GLBC); Only You (null primary); Gaia+Diplomat (Wonder); AYA (Whitehorse) |
| Null `primary_developer` + RelatedParty SPV/mkt | **Only You** (Onlyou Investments + GLBC mkt) |
| Unverified developer attribution NDI | **AYA Sandoral** — never primary |
| HassConsult dual role (conceptualizer; SPV gap) | Nouveau, Sensei, **Ankori** |
| HassConsult exclusive agent ≠ primary developer | **Kai** (Ayce primary) |
| Kings + Royal GroupCompany | Summit, Square Ph2 |
| Dual co_developer + RelatedParty (again) | Capricorn / Mulika (like Porini/Golden) |
| Oak Group marketing_partner sibling assets | Luna Oak + Brookside Oak |
| Payment tenor **NDI** | Nouveau (28/30/21) |
| Payment tenor **developer-canonical** | Sensei **30 mo**; **Ankori 30 mo** |
| USD primary currency | **Canto** (VAAL) |
| Official vs official from-price **NDI** | Brookside microsite 9.9M vs Oak Group 8.2M |
| Wrong-plot / wrong-entity anti-merge | Sensei ≠ Benford Greenwood; Capricorn ≠ Staroot Residency; Eldoret Ph2 ≠ Ph1; Ankori ≠ Galaxy One; Brookside ≠ Luna Oak |

---

## Open verification themes

1. HassConsult LOO contracting entity (Nouveau / Sensei / Ankori).  
2. Nouveau binding tenor + from-price 6.0 vs 6.5M.  
3. Kings Summit 9M vs 8M; Summit deposit %.  
4. Eldoret Phase 2 deposit/completion; 70/140 “available” meaning.  
5. Capricorn live microsite + unit price list; Mulika equity vs brand.  
6. Canto deposit % (agent 30% below ≥4); VAAL Kenya SPV register string.  
7. Ankori legal SPV; deposit %.  
8. Brookside Van Tung registry/NEMA; microsite vs Oak from-price NDI.  
9. Kai unit-type taxonomy + completion NDI; Innova legal role vs Ayce.  
10. 108 Omicron on live official HTML; payment schedule must-have; Enin Imperium/Space Art.  
11. Coverage agent `filter_candidate` on feature catalog.  
12. Only You primary (Onlyou vs GLBC vs co-dev); LOO payment; storeys/parking NDI.  
13. Gaia/Diplomat Wonder legal SPV; Gaia completion month NDI; Diplomat microsite 502 + price list.  
14. AYA legal SPV (Whitehorse vs AAD vs Sandoral); deposit %; completion month.  
15. Libra legal SPV; payment schedule; 119 vs 120; typed prices vs 17–25M band.  
16. Lulu official from-price NDI (4.4M vs 6.93M+) — public stays **POA**.  
17. Highpoint 336 live microsite + progress NDI; name/legal string NV.  
18. Balkis Sunmon legal conf (admin-only until ≥4); sizes NDI.  
19. Geo enrichment for **23** area-only map tiers; bathrooms explicit harvest.
