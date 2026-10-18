---
slug: sensei-nyali
external_id: MSA-001
geography: coast_mombasa
cycle: coast-pilot-1
pilot: true
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-16
discovery_lead: docs/discovery/kenya-offplan-leads.md
---

# Sensei (Nyali, Mombasa) — MSA-001 coast geography pilot

**New geography:** Coast / Mombasa County — **not** Nairobi NBO corpus. Discovery lead: HassConsult Sensei URLs in [kenya-offplan-leads.md](../discovery/kenya-offplan-leads.md).

Lead (unverified until checked): Greenwood Drive, Nyali; off-plan; completion Q3 2029; from KSh 24M; 30-month payment; HassConsult sales/management framing.

Live research accessed **2026-10-16**.

**Method locks applied (same as Nairobi):**
- Developer vs agents: if developer known and developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`**; no assumed winner.
- Prices: always **`price_claims[]`** (multi); no single forced scalar.
- Payment must-have if **any developer source** **or** ≥4 independent agent/portal sources.
- Agent-only / uncorroborated / wrong-plot → **show** + **`needs_verification`**.
- Scan ~10; retain ≥5 densest; **always keep** developer/official project site.
- Unproven brand/parent → `marketing_partner` RelatedParty (not GroupCompany).

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Flags / notes |
|-------|------|-------|-----:|---------------|
| `canonical_name` | **CANONICAL** | Sensei | 5 | hassconsult.com/sensei; homepage; blog |
| `aliases` | secondary | Sensei Residences; Sensei \| Nyali \| Beachfront Residences; Greenwood Drive \| Beachfront Residences (Investment Collection card) | 4 | Hass pages / LinkedIn |
| `status` | **CANONICAL** (official agree) | **Off-plan** / Recently Launched | 5 | Sensei “OFF PLAN BEACHFRONT PROPERTY”; Investment Collection “Recently Launched” |
| `geography.country` | **CANONICAL** | Kenya | 5 | |
| `geography.county_city` | **CANONICAL** | **Mombasa** (Nyali) | 5 | Official Sensei copy — **coast geography** |
| `geography.neighbourhood_street` | **CANONICAL** | **Greenwood Drive**, Nyali | 5 | Sensei page + Nyali blog |
| `geography.beachfront_m` | **CANONICAL** (pages agree) | **67 m** direct beachfront / ocean frontage | 5 | Sensei + blog |
| `geography.site_acres` | **CANONICAL** (pages agree) | **1.89 acres** | 5 | Sensei + blog |
| `geography.lat_lng` | geocode — **needs_verification** | **−4.055089, 39.701731** (`geo_method=geocode`) | 3 | Nominatim Greenwood Drive Nyali 2026-10-16; beachfront plot unpublished — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | proposed — see §2 | → `dev-hass-consult-limited` (same entity as Nouveau) | **4** | Aligns Nouveau dossier; project SPV / EIA not found → not conf 5 |
| `unit_types` | **CANONICAL** | 1, 2, 3 bedroom apartments; **1–4 bedroom duplex** residences | 5 | Sensei page + Investment Collection beds 1–4 |
| `total_units` | **CANONICAL** (official pages agree) | **111** residences | 5 | Sensei + Nyali blog |
| `building_specs.storeys` | **CANONICAL** (blog explicit; not contradicted on Sensei HTML) | **Four floors** (“just four floors”) | 5 | Blog; Sensei emphasizes low-density — no conflicting storey count found |
| `size_by_type` / floorplans | unknown on HTML | Floorplans CTA on Sensei page; brochure via contact form — **not OCR’d this pass** | 0 | Document-intel follow-up |
| `size_measure_tag` | unknown | — | 0 | |
| `price_claims[]` | claim set — keep all; **no collapse** | See **§1a** | ≤5 | Official from **KES 24M** |
| `currency` | **CANONICAL** | KES | 5 | |
| `payment_plan.tenor` | **CANONICAL** (developer source) | **Payment over 30 months** | 5 | Sensei page summary block — meets must-have via **any developer source** |
| `payment_plan.deposit` | unknown | Deposit **% not stated** on Sensei HTML | 0 | Do not invent; brochure/LOO |
| `payment_plan.balance` | secondary (developer narrative) | Instalments **throughout construction** | 4 | Off-plan section copy |
| `completion_estimate` | **CANONICAL** (pages agree) | **Q3 2029** | 5 | Sensei page |
| `amenities` **canonical** | **CANONICAL** (Hass agree across page + LinkedIn) | Infinity lagoon; Ocean Pavilion; beach cabanas; island lounges / lounge islands; Seaside Lookout; fully fitted gym; film lounge; work studio; kids sand play park + kids’ tide pool; courtyards; **Elevate** activated experience hub (wellness, fitness, dining, entertainment, curated resident events) | 5 | Sensei + LinkedIn posts |
| `stewardship_model` | **CANONICAL** (Hass agree) | Managed & let by **HassConsult** — sales/resales, lettings, property management, resident experience | 5 | Sensei + blog |
| `legal_title` | unknown | — | 0 | |
| `construction_progress` | unknown | No tracker published this pass | 0 | |

### 1a. `price_claims[]` (always multi — C2 lock)

**No typed unit-by-unit price list** on public HTML. Official hero is a **from** figure only.

| # | Claim (KES) | Context | Source | Conf | Flags |
|--:|-------------|---------|--------|-----:|-------|
| 1 | from **24,000,000** | 1–4 bed residences | hassconsult.com/sensei | 5 | Official |
| 2 | from **24,000,000** | Greenwood Drive \| Beachfront card | Investment Collection | 5 | Same publisher — corroborates, not independent |
| 3 | Benford / BuyRent **5.8M–15.8M** Greenwood Nyali | **Different project** (see Issues) | Benford; BuyRentKenya | — | **Do not merge** into Sensei prices |

Do not publish Benford bands as Sensei. Cash vs instalment dual columns: **not published** on retained Sensei pages (only 30-month tenor).

### Payment plan — threshold

| Element | Sources | Count / type | Threshold? | Status |
|---------|---------|--------------|------------|--------|
| **30-month** payment | Sensei official page | Developer | **Met** | **Canonical / must-have** |
| Instalments during construction | Sensei off-plan section | Developer | Met (narrative) | Canonical narrative |
| Deposit % | — | 0 | Not met | **unknown** |
| Agent ≥4 deposit consensus | No independent agent Sensei listings found | 0 | — | — |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-hass-consult-limited` *(shared with Nouveau — entity-resolution)* |
| `legal_name` | **Hass Consult Limited** (trading **HassConsult Real Estate**) — per Nouveau dossier public-directory style; **project-specific SPV not found** |
| `trading_names` | HassConsult; HassConsult Real Estate; Hass Consult |
| `website` | https://www.hassconsult.com/ |
| `group_company_id` | null |
| `evidence` | Sensei microsite on Hass domain; homepage features Sensei; “development team” framing; stewardship “Managed and let directly by HassConsult”; same org as Nouveau (`dev-hass-consult-limited`) |
| `sales_office` | ABC Place, Waiyaki Way, P.O. Box 14090-00800 Nairobi |
| `identity_gap` | No Sensei-specific SPV / NEMA proponent recovered — conf **4**, not 5; advocate should confirm contracting entity on LOO |

**Proposal:** Primary developer-of-record = **Hass Consult Limited / HassConsult Real Estate (confidence 4)** — reuse Nouveau canonical developer id. Do **not** invent a Sensei SPV.

**Not:** Benford Homes (different Greenwood listing — §7).

---

## 3. GroupCompany

**None** evidenced.

---

## 4. RelatedParty

| Name | Type | Evidence | Conf |
|------|------|----------|-----:|
| — | — | No separate marketing platform / co-developer named besides HassConsult’s dual developer+manager role | — |

HassConsult’s **management/letting** role is documented on the property claims (`stewardship_model`), not as a second RelatedParty clone of the same org.

---

## 5. Agents + Contacts

### Agents

| Agent | Type | Role | Evidence |
|-------|------|------|----------|
| HassConsult | developer sales (primary channel) | Official project + enquiry form | https://www.hassconsult.com/sensei |
| Benford Homes | agency | **Greenwood Nyali other project** — anti-confusion only | https://benfordhomes.com/property/1234-bedroom-apartment-on-going-project-on-sale-nyali-greenwood/ |

No independent third-party agent listing **named Sensei** found this pass (search returned Hass surfaces + Benford/BuyRent **non-Sensei** Greenwood ads).

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 709 479 000 | HassConsult / project sales |
| email | HELLO@HASSCONSULT.COM | HassConsult |
| office | ABC Place, Waiyaki Way, Nairobi | HassConsult |
| url | https://www.hassconsult.com/sensei | Property |
| url | https://www.hassconsult.com/sensei-contact-form | Property sales lead form |
| phone | (+254) 706 327 148 | BuyRentKenya listing channel for **non-Sensei** Greenwood ad — do not attach to Sensei |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| Elevate (experience hub brand) | other (lifestyle programme) | Sensei page + LinkedIn — product of HassConsult, not separate company | 4 |
| Architect / contractor | unknown | Not named on materials fetched | 0 |

---

## 7. Issues / conflicts (highlighted)

1. **Geography:** First **coast / Mombasa** dossier — keep separate from Nairobi NBO index section.
2. **Legal developer SPV:** HassConsult trading/presentation clear; **registry legal name unknown** → primary conf **4**, not 5.
3. **≠ Benford / BuyRent “Greenwood Nyali”** (from **5.8M**, groundbreaking Apr 2026, 30% / 24 mo): **different project** — prices, payment, and density do not match Sensei (from **24M**, Q3 2029, 30 mo, 111 units / 4 floors / 67 m frontage). Flag for entity-resolution anti-merge.
4. **Hass completed “Nyali \| Seaside Luxury”** on Investment Collection (from 9M) — **completed**; not Sensei.
5. **Deposit %** unpublished on Sensei HTML — do not invent.
6. **Floorplan sizes** behind CTA / contact form — not extracted this pass.
7. **Few independent agent sources** naming Sensei — commercial fields lean on Hass stack (acceptable when developer-sourced; weak for agent triangulation).
8. Space.ke Hass profile lists other Nyali product (**Evoque**) — do not confuse with Sensei.

---

## 8. Sources

`sources_evaluated`: **~12** · `sources_retained`: **8**

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://www.hassconsult.com/sensei | HassConsult | project_site / developer | 2026-10-16 | **Always keep** — name, geo, 111 units, 1.89 ac, 67 m, from 24M, Q3 2029, 30 mo, amenities, stewardship |
| 2 | https://www.hassconsult.com/investment-collection | HassConsult | developer | 2026-10-16 | Recently Launched Greenwood card; beds 1–4; from 24M |
| 3 | https://www.hassconsult.com/post/why-nyali-is-emerging-as-the-coast-s-prime-real-estate-investment-address | HassConsult | developer / blog | 2026-10-16 | 111 units; **four floors**; stewardship; Elevate |
| 4 | https://www.hassconsult.com/ | HassConsult | developer | 2026-10-16 | Sensei featured; development-team framing |
| 5 | https://www.hassconsult.com/sensei-contact-form | HassConsult | developer | 2026-10-16 | Contacts; brochure/details via advisor |
| 6 | https://www.linkedin.com/posts/hass-consult_senseiresidences-greenwooddrive-nyali-activity-7487900816260026368-I_zp | HassConsult LinkedIn | social / developer | 2026-10-16 | Amenities corroboration (Infinity Lagoon, Ocean Pavilion, etc.) |
| 7 | https://www.linkedin.com/posts/hass-consult_sensei-story-details-activity-7490381837731741696-fnmR | HassConsult LinkedIn | social / developer | 2026-10-16 | Elevate hub; scarcity narrative |
| 8 | https://benfordhomes.com/property/1234-bedroom-apartment-on-going-project-on-sale-nyali-greenwood/ | Benford Homes | agent | 2026-10-16 | **Anti-merge** — other Greenwood Nyali off-plan (≠ Sensei) |

### Evaluated but not retained (thin / wrong entity)

| url | Why skipped |
|-----|-------------|
| https://www.buyrentkenya.com/listings/1-bedroom-apartment-for-sale-nyali-area-3883159 | Same Benford-class Greenwood ad; thin aggregator twin |
| https://www.buyrentkenya.com/listings/3-bedroom-apartment-for-sale-nyali-area-3972304 | Same non-Sensei plot family |
| https://space.ke/developers/hassconsult/ | Hass profile; **Sensei not listed** (Evoque Nyali present) — thin for this project |
| https://www.hassconsult.com/developments | Thin shell / little Sensei field text this fetch |
| Discovery lead row only | Not a publishable research URL |

---

## 9. Field harvest (coast pilot)

| Field | Sensei outcome | Coast note |
|-------|----------------|------------|
| Geography county/city outside Nairobi | **Must capture** | First coast dossier |
| Beachfront metres / site acres | Strong official | Coastal-specific facets |
| Developer trading vs legal SPV | Hass trading conf 4; SPV unknown | Same SPV gap pattern as some Nairobi leads |
| Payment tenor via developer | **30 months canonical** | Deposit still missing |
| `price_claims[]` multi | Official from only; wrong-plot Benford excluded | |
| Unit count + low-rise storeys | 111 / 4 floors agree | |
| Amenities / Elevate programme | Rich official | Map to feature scopes (development + community) when taxonomy applied |
| Independent agent triangulation | **Weak** this pass | Expect Plus/Admin to stay Hass-heavy until agents list Sensei by name |

**Proposed v1 must-haves (unchanged locks):** canonical_name, status, geography (incl. coast city/neighbourhood), primary_developer (with SPV caveat), unit_types, amenities core, completion_estimate, multi price_claims, payment when threshold met, sources ≥5 retained, contacts split by owner.

---

## 10. Open questions for review

1. Confirm **MSA-001** as coast id scheme (alongside NAK-001 / DISC-NBO-*).
2. Confirm shared `dev-hass-consult-limited` with Nouveau (conf 4) until Sensei SPV/filing found.
3. Priority OCR/brochure fetch for Sensei floorplans + deposit %?
4. Confirm Benford Greenwood **≠ Sensei** in entity-resolution anti-merge list.
