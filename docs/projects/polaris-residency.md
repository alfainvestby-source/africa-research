---
slug: polaris-residency
external_id: NBO-016
cycle: wave-c
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Polaris Residency (NBO-016) — Wave C research

CSV seed (unverified leads): location Kindaruma Road, Kilimani, Nairobi; lat/lng blank; stage `off_plan`; completion **2025 (check status)**; `price_from_kes` **6,000,000**; sales_contact **Own It Kenya** (+254 722 716 182, sales@ownitkenya.com); developer **blank**.

Live research accessed **2026-10-16**. **No official developer microsite, brochure PDF, or named NEMA EIA tied to “Polaris Residency” recovered this pass.** Kindaruma Road EIAs found for other schemes (e.g. Pinklady Properties 21-storey; 618 Serene Limited G+19 / 360 units) — **not linked** to Polaris without inventing identity. All commercial fields are **agent/portal claim sets** (conf ≤3) unless noted.

**Method locks applied:**
- Conflicts always highlighted.
- **Developer vs agents:** no confident developer → **no developer canonical** on commercial fields.
- **Official vs official:** N/A (no developer stack). Do not invent winners among agents.
- **Prices:** always full `price_claims[]` (no scalar).
- Payment must-have if **≥4 independent agent/portal sources** agree **or** any developer source.
- Agent-only / uncorroborated → **show** + **`needs_verification`**.
- CSV = unverified leads only. CSV Own It contact = **agent**, not developer.
- Unproven brand/parent → not invented. Co-developer dual model N/A (no co-named developers).

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** only when developer/official sources **agree**. Here developer commercial pages are **absent** → almost no canonical commercial fields. Agent consensus caps at **conf 3**. Low-confidence → **`needs_verification`**.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | secondary (multi-agent) | Polaris Residency | 4 | Own It; Sir Francis; CPK; Klin; Masterways; A-list; Azipa; Citiscape; Block; GNA |
| `aliases` | secondary | Polaris Residence; The Polaris Residency; Polaris Residency Apartments | 3–4 | CPK; Azipa; agents |
| `status` | claim set — **CONFLICT** | CSV `off_plan` / 2025 check; Own It still lists under off-plan index (completion 2025); Klin “New Construction” + Dec 2025; A-list / Masterways / Citiscape / Urbancore payment to **Dec 2025**; Sir Francis / CPK / Block / GNA **complete / ready for occupation** (Sir Francis updated Oct 2026; Block rent listing Aug 2026) | ≤2 | See §7 — **`needs_verification`** |
| `geography.city` | secondary multi-source | Nairobi | 4 | all agents |
| `geography.neighbourhood_street` | secondary multi-source | **Kindaruma Road**, Kilimani | 4 | Own It; Sir Francis; CPK; Klin; Azipa; Block; Urbancore; LinkedIn promo |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.297874, 36.790001** (`geo_method=geocode`) | 2 | Nominatim Kindaruma Road Kilimani 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `geography.plot` / LR | unknown | No Polaris-named filing this pass | 0 | — |
| `primary_developer_id` | **unknown** | — | 0 | No named developer on retained sources; Urbancore “Trusted Developer” marketing only (unnamed) — **not** invented |
| `unit_types` | secondary agent consensus | **1 Bedroom**; **1 Bedroom + study**; **2 Bedroom** | 3 | Own It; Sir Francis; CPK; Klin; Masterways; A-list; Azipa; Citiscape |
| `size_by_type` | secondary — Own It tags **plinth** (sq.ft) | See size table | 3 | Own It plinth; others sq.ft or sqm |
| `size_measure_tag` | secondary | **Plinth** on Own It lines; most agents untaggged sq.ft / sqm | 3 / 0 | Own It vs others |
| `total_units` | secondary — **`needs_verification`** | Search-indexed **GNA: 289 units** across two blocks (live HTML fetch incomplete on that sentence) | 1 | GNA indexed copy only |
| `building_specs.blocks` | secondary agent consensus | **Two** blocks / twin towers | 3 | Sir Francis; CPK; Klin; A-list; Block; GNA |
| `building_specs.storeys` | claim set — soft conflict | Majority: **16-storey** / 16 floors **vs** GNA “Block B … rising up to **17** floors” | 3 / 1 | 16: Own It; Sir Francis; CPK; Klin; A-list; Azipa; Block. 17: GNA only → **`needs_verification`** |
| `building_specs.units_per_floor` | secondary — **`needs_verification`** | GNA: Block A **7**/floor; Block B **10**/floor | 1 | GNA only |
| `price_claims[]` | claim set — **keep all**; no canonical | See **§1a** | ≤3 | |
| `currency` | secondary | KES | 5 | all commercial sources |
| `payment_plan.deposit` | secondary must-have (agent ≥4; **no developer**) | **30% deposit** | 3 | Own It; Masterways; Klin; Citiscape; Azipa — threshold **met**; still **`needs_verification`** vs live LOO |
| `payment_plan.deposit` | secondary conflict — **`needs_verification`** | **20% deposit** then staged 30% / 50% | 2 | A-list; Urbancore (only **2** — below ≥4) |
| `payment_plan.balance` | secondary soft | Balance over construction to **Dec 2025** / “year of completion” | 3 | Own It; Masterways; Klin; Citiscape; Azipa; A-list; Urbancore |
| `payment_plan` (post-completion sales) | secondary — **`needs_verification`** | Sir Francis / CPK ready stock: “call for current terms” / flexible / cash discounts — may supersede construction instalments | 2 | Sir Francis; CPK |
| `completion_estimate` | claim set — **CONFLICT** | CSV **2025**; agents **December 2025** / occupation **Jan 2026** (Azipa) **vs** ready/complete (Sir Francis, CPK, Block, GNA) | ≤2 | **`needs_verification`** |
| `amenities` (core agent consensus) | secondary | Gym; garden & kids’ play; generator; borehole; electric fence; high-speed lifts; ample parking; DSTV/internet; CCTV / security | 3 | Own It; Sir Francis; Klin; Masterways; A-list; Azipa; Citiscape; Block; CPK |
| `amenities` | inflated / thin — **`needs_verification`** | CPK intro mentions **pool**; Urbancore access control; Azipa feature chips (barbeque, basement parking, fibre) not all echoed in body | 1–2 | CPK; Urbancore; Azipa chips |
| `availability_claim` | secondary — **`needs_verification`** | Block: 1BR to let **KES 70,000**/mo; GNA sale + rent + furnished nightly; Sir Francis “confirm units still available” | 2 | agents |
| `legal_title` | unknown | — | 0 | not found |
| `construction_progress` | unknown / historical | LinkedIn Jan 2024 promo: “Excavation started, currently on Ground Floor” — stale vs later complete claims | 1 | LinkedIn Aerlene Mugambi — **`needs_verification`** as current progress |
| `rental_asking` | secondary (not portal must-have) | 1BR **60–70k**/mo; 1BR+study **70k**; 2BR **85k** (CPK/GNA); Block 1BR let **70k** | 2–3 | CPK; GNA; Block |

### Size table (agent — no developer schedule)

| Type | Own It (plinth sq.ft) | Common sq.ft cluster | Approx sqm (Azipa / A-list) | Role |
|------|----------------------:|---------------------:|----------------------------:|------|
| 1 Bedroom | **650** | 650 | ~**60–61** | Multi-agent |
| 1BR + study (smaller) | **670** | 670 | ~**62–65** | Multi-agent |
| 1BR + study (larger) | **750** | 750 | ~**70** | Multi-agent |
| 2 Bedroom (smaller) | **970** | 970 | ~**90** | Multi-agent |
| 2 Bedroom (larger) | **1150** | 1150 | ~**106–106.8** | Multi-agent |

Do not invent gross vs plinth beyond Own It’s **plinth** tag.

### 1a. `price_claims[]` — keep **all** options (no canonical)

No developer price list. **Never collapse to a single `price_from`.**

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Own It (CSV agent) — **plinth** sq.ft | 1BR 650 **KES 6.0M**; 1BR+study 670 **7.2M**; 1BR+study 750 **7.7M**; 2BR 970 **9.2M**; 2BR 1150 **9.7M** | ownitkenya.com off-plan index | Secondary; matches CSV `price_from` 6M |
| B | Klin / Masterways / Citiscape (same table family) | Same 6 / 7.2 / 7.7 / 9.2 / 9.7M on 650–1150 sq.ft | klinproperties; masterways; citiscapevaluers | Secondary |
| C | CPK | Same 6 / 7.2 / 7.7 / 9.2 / 9.7M; ready for occupation; rent bands | commercialpropertykenya.com | Secondary |
| D | Sir Francis (updated Oct 2026) | 1BR from **5.5M**; 1BR+study **7.2 / 7.7M**; 2BR **9.2 / 9.7M**; **ready** | sirfrancismarketingltd.co.ke | Secondary — **5.5M** undercuts 6M cluster → **`needs_verification`** |
| E | A-list (sqm) | 60 sqm **6M**; 65 **7.2M**; 70 **7.5M**; 90 **9.2M**; 106.8 **9.7M** | a-listrealestate.ke | Secondary — 7.5M vs 7.7M mid band |
| F | Azipa (sqm) | 61 **6M**; 62 **7.2M**; 70 **7.7M**; 90 **9.2M**; 106 **9.7M** | aziparealestate.co.ke | Secondary |
| G | Urbancore (1BR+study slice) | 65 sqm **7.2M** only on page | urbancore.co.ke | Secondary thin |
| H | GNA (coarse sale bands) | 1BR **6M**; 1BR+study **8M**; 2BR **11M** | gna.co.ke | Secondary — **diverges** from 7.2/9.2–9.7 table → **`needs_verification`** |
| I | CSV seed | `price_from_kes` **6,000,000** | seed | Unverified lead |

**Canonical price:** none.

### Payment plan — ≥4-source recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **30% deposit** | Own It; Masterways; Klin; Citiscape; Azipa | **5** | **Met (agents)** | **Must-have** at conf **3** (no developer LOO) |
| Balance to Dec 2025 / completion year | Same cluster + A-list/Urbancore schedules | ≥4 | Met as soft construction-era claim | Soft must-have — may be **stale** if building complete |
| **20%** then 30% / 50% | A-list; Urbancore | **2** | Not met | Alternate · **`needs_verification`** · conflicts with 30% |
| Azipa staged 30% / 20% / 50% | Azipa only (detail) | **1** | Not met as full schedule | Detail · **`needs_verification`** |
| Developer LOO / FAQ | None | 0 | — | unknown |
| Ready-stock terms | Sir Francis “call for current terms”; CPK flexible / cash discounts | 2 | Soft | Post-completion · **`needs_verification`** |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | **unknown** — no `dev-*` assigned |
| `legal_name` | unknown |
| `trading_names` | unknown |
| `website` | none found for Polaris |
| `evidence` | No agent page names a developer entity this pass. Urbancore “Trusted Developer & Timely Delivery” is marketing boilerplate without a company name. |
| `group_company_id` | null |
| `csv_name_note` | CSV developer cell **blank**. Own It Kenya = **sales agent** (CSV sales_contact), not developer. |

**Do not invent a developer.** Kindaruma Road NEMA filings for other projects were **not** attributed to Polaris.

---

## 3. GroupCompany

**None.**

---

## 4. RelatedParty

**None required** this pass (no unproven parent/brand co-label analogous to SkyPeak/XiangFeng). Own It Kenya modeled as **Agent**, not RelatedParty developer-platform.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Own It Kenya | agency | CSV sales_contact; plinth sizes; 30% deposit; off-plan index card | https://ownitkenya.com/off-plan-apartments-for-sale-in-nairobi/ |
| Sir Francis Homes | agency | Ready/complete; from **5.5M**; Oct 2026 update | https://sirfrancismarketingltd.co.ke/properties/polaris-residency-kilimani/ |
| CPK Real Estate | agency | Ready; full price table; rent bands; pool mention | https://commercialpropertykenya.com/properties/the-polaris-residency-apartment-in-kilimani/ |
| Klin Properties | agency | Dec 2025; 30% plan; typology table | https://klinproperties.co.ke/property/polaris-residency/ |
| Masterways Real Estate | agency | 30% deposit; typology table | https://masterways.co.ke/properties/polaris-residency |
| A-list Real Estate | agency | 20% staged plan; sqm prices; Dec 2025 | https://a-listrealestate.ke/property/polaris-residency/ |
| Azipa Real Estate | agency | 30%/20%/50% detail; sqm prices; Jan 2026 occupation | https://aziparealestate.co.ke/property/polaris-residency1-2-bedroom-apartments-for-sale-in-kilimani-nairobi/ |
| Citiscape Valuers | agency | 30% plan; typology table | https://citiscapevaluers.com/property/polaris-residency-kilimani/ |
| Block Real Estate | agency | Rent listing; newly completed twin 16-storey | https://block.ke/property/one-bedroom-apartment-to-let-kilimani-polaris-residency/ |
| GNA Real Estate | agency | Ready; coarse sale prices; 17-floor note; 289 units (indexed) | https://gna.co.ke/project/polaris-residency-kilimani-1-beds-plus-study-room-2-beds/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 722 716 182 / +254 720 469 282 | Agent: Own It Kenya (CSV) |
| email | sales@ownitkenya.com | Agent: Own It Kenya (CSV) |
| phone | +254 722 720 812 | Agent: Sir Francis Homes |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 721 687 339 | Agent: Klin |
| email | propertiesklin@gmail.com | Agent: Klin |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone / WhatsApp | +254 742 880 335 / +254 796 007 755 | Agent: Azipa |
| email | azipahomes@gmail.com / info@aziparealestate.co.ke | Agent: Azipa |
| phone | +254 707 252 525 / +254 708 848 481 | Agent: Citiscape |
| email | info@citiscapevaluers.com | Agent: Citiscape |
| phone | +254 725 937 686 | Agent: Block |
| phone | +254 712 406 060 / +254 782 406 060 | Agent: GNA |
| email | support@gna.co.ke | Agent: GNA |
| phone | +254 743 701 113 | Agent: Urbancore (evaluated; thin 1-type page) |

No developer sales contact recovered.

---

## 6. Stakeholders

None named (no contractor / architect / counsel on retained sources). LinkedIn promotional post by Aerlene Mugambi is marketing copy, not a typed Stakeholder entity.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Developer** | CSV blank; agents silent on legal name | **Unknown.** Do not invent. Own It ≠ developer. |
| 2 | **Status / completion** | Off-plan / Dec 2025 construction instalments **vs** ready/complete (2026 listings) | Claim set + **`needs_verification`**. No developer status. |
| 3 | **Deposit** | **30%** (≥4) **vs** **20%** staged (A-list, Urbancore) | 30% must-have at conf 3; keep 20% secondary. |
| 4 | **Prices** | 6M cluster **vs** Sir Francis **5.5M** **vs** GNA **8M / 11M** coarse bands | **Keep all** `price_claims[]`. No scalar. |
| 5 | **Storeys** | **16** majority **vs** GNA **17** (Block B) | Prefer multi-agent 16 as secondary consensus; GNA **`needs_verification`**. |
| 6 | **Unit count** | GNA indexed **289** only | Show + **`needs_verification`**. |
| 7 | **Size units** | Own It **plinth sq.ft** **vs** Azipa/A-list **sqm** | Tag plinth where Own It; do not mix measures silently. |
| 8 | **Pool** | CPK intro mentions pool; most amenity lists omit | Amenity inflation · **`needs_verification`**. |
| 9 | **Wrong Kindaruma EIAs** | Pinklady / 618 Serene filings on Kindaruma | **Not** Polaris without naming — do not attach. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned ~14 candidates (Own It off-plan index, Sir Francis, CPK, Klin, Masterways, A-list, Azipa, Citiscape, Block rent, GNA, Urbancore, LinkedIn promo, Kindaruma NEMA PDFs as negative checks, CSV seed). **No developer site to always-keep.** Retained 10 densest agent/portal sources (≥5 rule).

**Thin / skipped / negative:**
- https://urbancore.co.ke/property/polaris-residency-1-bedroom/ — single typology + 20% schedule; used in payment conflict notes, not retained as primary
- LinkedIn Aerlene Mugambi promo (Jan 2024) — progress snapshot only; conflict/history note
- Kindaruma NEMA EIA PDFs (Pinklady; 618 Serene) — **wrong/unproven identity**; evaluated as negative, **not retained** as Polaris sources
- CSV NBO-016 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://ownitkenya.com/off-plan-apartments-for-sale-in-nairobi/ | Own It Kenya | agent | 2026-10-16 | CSV contact; **plinth** sizes; 30%; completion 2025 |
| 2 | https://sirfrancismarketingltd.co.ke/properties/polaris-residency-kilimani/ | Sir Francis Homes | agent | 2026-10-16 | **Ready**; from **5.5M**; Oct 2026 |
| 3 | https://commercialpropertykenya.com/properties/the-polaris-residency-apartment-in-kilimani/ | CPK | agent | 2026-10-16 | Ready; price + rent tables; pool claim |
| 4 | https://klinproperties.co.ke/property/polaris-residency/ | Klin Properties | agent | 2026-10-16 | Dec 2025; 30% plan |
| 5 | https://masterways.co.ke/properties/polaris-residency | Masterways | agent | 2026-10-16 | 30% plan; typology |
| 6 | https://a-listrealestate.ke/property/polaris-residency/ | A-list | agent | 2026-10-16 | **20%** staged plan conflict; sqm prices |
| 7 | https://aziparealestate.co.ke/property/polaris-residency1-2-bedroom-apartments-for-sale-in-kilimani-nairobi/ | Azipa | agent | 2026-10-16 | 30/20/50 detail; Jan 2026 occupation |
| 8 | https://citiscapevaluers.com/property/polaris-residency-kilimani/ | Citiscape | agent | 2026-10-16 | 30% plan; typology |
| 9 | https://block.ke/property/one-bedroom-apartment-to-let-kilimani-polaris-residency/ | Block | agent | 2026-10-16 | Newly completed; rent 70k; twin 16-storey |
| 10 | https://gna.co.ke/project/polaris-residency-kilimani-1-beds-plus-study-room-2-beds/ | GNA | agent | 2026-10-16 | Ready; divergent sale prices; 17-floor / 289 indexed |

---

## 9. Field harvest

| Field | Polaris status | Notes for living schema |
|-------|----------------|-------------------------|
| `canonical_name` / aliases | OK (agent consensus) | No official nameplate |
| `status` | Claim set — off-plan vs **ready** | Same pattern as Misty Springs |
| geography Kindaruma / Kilimani | OK multi-agent | No GPS / plot |
| `primary_developer` | **unknown** | Reinforces blank-CSV / Own It-agent pattern |
| `unit_types` / sizes | Agent table + Own It **plinth** sq.ft | Gross/plinth only where tagged |
| `total_units` | 289 GNA only | Weak; needs verification |
| `storeys` | 16 consensus vs GNA 17 | Claim set |
| `price_claims[]` | A–I retained | 5.5M vs 6M vs GNA coarse |
| `payment_plan` | **30% must-have via ≥5 agents** (conf 3); 20% secondary | May be stale if complete |
| amenities core | Multi-agent | Reject uncorroborated pool |
| completion / ready | Conflict | Verification pass |
| Official EIA when no microsite | **No match** | Do not force Kindaruma filings onto Polaris |

### Proposed schema consensus bumps (coordinator / DB steward)

| Extension | This project | Note |
|-----------|--------------|------|
| Status claim set including **ready vs off-plan** after stated completion year | Polaris + Misty | Coverage for Wave C “check status” seeds |
| Own It Kenya as **Agent** when CSV sales_contact | Polaris + Misty + Alba/Plumeria pattern | Never promote to developer without evidence |
| Payment **30%** via ≥4 agents without developer LOO | Polaris (like Misty) | conf 3 must-have |
| `size_measure_tag` = **plinth** when Own It labels sq.ft as plinth | Polaris | Same Misty pattern |
| Developer **unknown** allowed with conf 0 | Polaris | Prefer unknown over invented Kindaruma EIA match |

---

## Open questions (verification pass)

1. Who is the **legal developer / contracting entity** on the sale agreement / title?
2. Is the building **complete and handed over**, or still instalment-to-Dec-2025?
3. Which deposit is binding today: **30%** or **20%** staged?
4. Confirm live **price list** (5.5M vs 6M vs GNA 8M/11M).
5. Confirm **unit count** (289?) and **storeys** (16 vs 17).
6. Any official brochure / NEMA filing that **names** Polaris Residency?
