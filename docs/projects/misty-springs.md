---
slug: misty-springs
external_id: NBO-017
cycle: half-batch
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Misty Springs (NBO-017) — half-batch research

CSV seed (unverified leads): location Westlands Road, Westlands, Nairobi; stage `off_plan`; completion **Q4 2025 (check status)**; `price_from_kes` **8,000,000**; sales_contact **Own It Kenya** (+254 722 716 182, sales@ownitkenya.com); developer **blank**.

Live research accessed **2026-10-16**. **No official developer project microsite or brochure PDF found this pass.** Closest “developer” provenance = LinkedIn company page for **Tian Yu International Company Limited** (display alias “MISTY SPRINGS WESTLAND APARTMENT”) + project Facebook URL cited by directory.

**Method locks applied:**
- Developer vs agents: if developer known **and** developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official:** **do not assume** → **`needs_developer_input`**. Here: **no agreeing developer commercial stack** → almost all commercial fields are agent claim sets (conf ≤3).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **≥4 independent agent/portal sources** agree **or** any developer source.
- Agent-only / uncorroborated → **show** + **`needs_verification`**. CSV = unverified leads only.
- Seed Own It contact = **agent**, not developer.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** only when developer-backed sources **agree**. Here developer commercial pages are **absent** → few canonical commercial fields. Agent consensus caps at **conf 3**. Low-confidence → **`needs_verification`**.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | secondary (multi-agent + LinkedIn alias) | Misty Springs | 4 | Own It; CPK; Sir Francis; LinkedIn display; agents |
| `aliases` | secondary | Misty Spring; Misty Springs Apartments; Misty Springs Westlands; Misty Spring Westland Apartment; MISTY SPRINGS WESTLAND APARTMENT (LinkedIn) | 4 | agents; LinkedIn; Musilli |
| `status` | claim set — **CONFLICT** | CSV `off_plan` / Q4 2025 check; agents **under construction** (Klin, Azipa, OGRE alt page Q3 2026); OGRE primary **Expected Completion Dec 2025**; CPK **“fully complete and ready for occupation”** (page modified 2026-08-09); A-list **“Project Ready for Occupation”**; GNA **Ready for occupation / Available for Rent (SOLD OUT)**; AfricaBiz short-stay reviews | ≤2 | See §7 — **`needs_verification`** |
| `geography.city` | secondary multi-source | Nairobi | 4 | all agents |
| `geography.neighbourhood_street` | secondary multi-source | **Westlands Road**, Westlands; near **GTC** / behind **Kempinski** (multi-agent) | 4 | Own It; OGRE; CPK; Sir Francis; Azipa; Klin |
| `geography.street_number` / plot | secondary | **24 Westlands Rd** / “plot number 24” | 3 | AfricaBiz; Musilli; Andrew Mbaria LinkedIn post snippet |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.271911, 36.811024** (`geo_method=geocode`) | 2 | Nominatim Westlands Road 2026-10-16 — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **lead only** — **`needs_verification`** | → `dev-tian-yu-international` (**proposed**, conf 2) | 2 | LinkedIn company self-claim; Musilli “Siaya park/Crest Park developers” aligns with LinkedIn prior-project names — **not** a corporate website |
| `unit_types` | secondary agent consensus | **1 Bedroom**; **2 Bedroom** | 3 | Own It; Klin; OGRE; CPK; Sir Francis; Azipa; Flamingo; A-list |
| `size_by_type` | secondary — Own It tags **plinth** | 1BR **58 sqm** (Own It **Plinth**); 2BR **90 sqm** / **99 sqm** (Own It **Plinth**). Sir Francis quotes 1BR **57 sqm** — minor conflict | 3 | Own It (plinth); Klin/OGRE/CPK/Azipa/A-list 58; Sir Francis 57 |
| `size_measure_tag` | secondary (Own It only for explicit tag) | **Plinth** on Own It size lines; other agents say “SQM” without gross/plinth label | 3 / 0 | Own It vs others |
| `total_units` | secondary agent consensus | **276** apartments | 3 | CPK; Sir Francis; Azipa; Musilli (≥4) — **`needs_verification`** (no developer count) |
| `building_specs.blocks` | secondary agent consensus | **Two** blocks / towers | 3 | CPK; Sir Francis; Azipa; Musilli |
| `building_specs.storeys` | claim set — **CONFLICT** | Majority agents: **23 floors** **vs** Proxima rental copy **27 floors** | 2 | 23: Own It; Klin; CPK; Azipa; A-list; GNA; OGRE. 27: Proxima only → **`needs_verification`** |
| `price_claims[]` | claim set — **keep all**; no canonical | See **§1a** | ≤3 | |
| `currency` | secondary | KES | 5 | all commercial sources |
| `payment_plan.deposit` | secondary must-have (agent ≥4; **no developer**) | **30% deposit** | 3 | Own It; Klin; Flamingo; Azipa; Sir Francis; Musilli; CPK; A-list — threshold **met via ≥4 agents**; still **`needs_verification`** vs live LOO |
| `payment_plan.balance` | secondary soft | Balance over **~30 months** / **up to 2½ years** / “over construction” | 3 | Own It; Klin; Flamingo; Sir Francis; Musilli; CPK |
| `payment_plan.balance` | outlier — **`needs_verification`** | A-list: “deposit of 30% balance **within 60 days**” (conflicts with 2½-year framing on same-theme pages) | 1 | A-list only |
| `completion_estimate` | claim set — **CONFLICT** | CSV **Q4 2025**; OGRE **December 2025**; Klin/Azipa/OGRE alt **Q3 2026**; CPK/A-list/GNA **complete / ready** | ≤2 | **`needs_verification`** |
| `amenities` (core agent consensus) | secondary | Rooftop **heated** pool; gym; rooftop BBQ/lounge; kids’ play; **2 high-speed lifts per block**; reception; ample parking + visitor parking; 24/7 security; smart home / **facial recognition** / face-scan access; fitted kitchen (4-burner, oven, extractor) | 3 | Own It; Klin; OGRE; CPK; Sir Francis; Azipa; A-list; GNA |
| `amenities` | inflated / single-source — **`needs_verification`** | Proxima: **150 m jogging track**, indoor playground; Flamingo feature chips: club house, home theater; CPK feature chips: borehole, fibre (not all echoed in body copy) | 1 | Proxima; Flamingo; CPK chips |
| `availability_claim` | secondary — **`needs_verification`** | OGRE: **17 units remaining**; 1BR & 99 sqm **SOLD OUT**, 90 sqm limited; CPK: 1BR sold out, 2BR limited; A-list: 99 sqm sold out; GNA: **all sold out** (rent only); Azipa: few units / UC | ≤2 | agents disagree |
| `legal_title` | unknown | — | 0 | not found |
| `construction_progress` | unknown | No developer tracker this pass | 0 | — |

### 1a. Price claims — keep **all** options (no canonical)

No developer price list. **Never collapse to a single `price_from`.**

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Own It (CSV agent) — **plinth** sizes | 1BR 58 sqm **KES 8.0M**; 2BR 90 sqm **KES 12.6M**; 2BR 99 sqm **KES 13.8M** | ownitkenya.com | Secondary; matches CSV `price_from` 8M |
| B | Klin | 1BR 58 **8.12M**; 2BR 90 **12.6–17.5M**; 2BR 99 **13.9M** | klinproperties.co.ke | Secondary — **needs_verification** on 17.5M ceiling |
| C | Oxford Gate (Jul 2025 update) | 1BR 58 **8.12M SOLD OUT**; 2BR 99 **13.9M SOLD OUT**; 2BR 90 **12.5M** limited; “from” **8.12M** | ogre.co.ke | Secondary + availability |
| D | CPK (modified 2026-08-09) | 1BR 58 **8.0M Sold Out**; 2BR 90 cash **from 10.5M** / 50% dep **from 11.5M** / original **from 12.6M** | commercialpropertykenya.com | Secondary — cash vs list framing |
| E | Sir Francis (updated Oct 2026) | 1BR **57 sqm from 8M**; 2BR 90–99 **from 12.6M** | sirfrancismarketingltd.co.ke | Secondary — 57 vs 58 size conflict |
| F | Azipa | 1BR 58 **8–10M**; 2BR 90 **12.6–13.9M**; 2BR 99 **13.8–17.5M** | aziparealestate.co.ke | Secondary — band width **needs_verification** |
| G | Flamingo | 1BR 58 **8M**; 2BR 90 **12.6M**; 2BR 99 **13.8M** | flamingorealestate.co.ke | Secondary (aligns Own It) |
| H | A-list | 1BR 58 **10M**; 2BR 90 **12.5M**; 2BR 99 **SOLD OUT** | a-listrealestate.ke | Secondary — 1BR **10M** outlier **needs_verification** |
| I | BuyRentKenya listing | 1BR 58 sqm **KES 11.0M** | buyrentkenya.com | Secondary — possible resale/inventory; **needs_verification** |
| J | CSV seed | `price_from_kes` **8,000,000** | seed | Unverified lead |

**Canonical price:** none.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| **30% deposit** | Own It; Klin; Flamingo; Azipa; Sir Francis; Musilli; CPK; A-list | **≥4** agents | **Met via agents** | Must-have **secondary** (conf 3); **no developer corroboration** → still flag live LOO **`needs_verification`** |
| Balance **~30 months / 2½ years** | Own It; Klin; Flamingo; Sir Francis; Musilli; CPK | ≥4 | Met as soft agent consensus | Secondary |
| Balance **within 60 days** | A-list only | 1 | Below threshold | Outlier **`needs_verification`** |
| Developer LOO / official FAQ | **None found** | 0 | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-tian-yu-international` (**proposed lead**) |
| `legal_name` | Tian Yu International Company Limited (LinkedIn slug / SignalHire mirror) |
| `trading_names` | MISTY SPRINGS WESTLAND APARTMENT (LinkedIn display); Misty Springs Westlands Apartment |
| `website` | **none found** this pass (no mistysprings.*.ke / tianyu corporate site recovered) |
| `evidence` | LinkedIn About: “WE ARE REAL ESTATE DEVELOPERS…”; posts naming Misty Springs Westlands along Westlands Road as current project; prior projects **Crest Park** (Denis Pritt / Kilimani) and **Siaya Park** (Kileleshwa). Musilli: “Another project by Siaya park/Crest Park developers.” |
| `group_company_id` | **null — none invented** |
| `developer_confidence` | **2** |
| `csv_name_note` | CSV developer cell **blank** — correct (do not invent from Own It) |

**Do not treat Own It Kenya, CPK, Sir Francis, Klin, Azipa, Musilli, A-list, GNA, or Flamingo as the developer.**

**Proposal:** keep Tian Yu as **`needs_verification`** developer lead until a company website, LOO letterhead, or registry filing corroborates. Do **not** promote to portal-ready `primary_developer` at conf 5.

---

## 3. GroupCompany

**None.** Crest Park / Siaya Park are framed as **prior projects** of the same LinkedIn entity, not evidenced parents. Do not invent a group.

---

## 4. RelatedParty

| Name | `relationship_type` | Evidence | Conf |
|------|---------------------|----------|-----:|
| Crest Park / Siaya Park (prior project brands) | prior_project / marketing framing | LinkedIn About; Musilli “Siaya park/Crest Park developers” | 2 |

Not `marketing_partner` in the Astra/Laureland sense (no second live brand co-selling Misty Springs). Record only as prior-project attribution until proven otherwise.

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Own It Kenya | agency | CSV sales_contact; blog listing with plinth prices + 30%/30 mo | https://ownitkenya.com/off-plan-apartments-for-sale-in-nairobi/ |
| Oxford Gate Real Estate | agency | Pricing + sold-out flags; Dec 2025 completion | https://www.ogre.co.ke/properties/misty-springs-apartments-1-and-2-bedroom-apartments-in-westlands/ |
| Klin Properties | agency | Q3 2026; 30%/30 mo; price table | https://klinproperties.co.ke/property/misty-springs/ |
| CPK Real Estate | agency | “Fully complete”; 276 units; cash/deposit price stack | https://commercialpropertykenya.com/properties/the-misty-spring-apartments-for-sale-in-westland/ |
| Sir Francis Homes | agency | 276/2 blocks; 30%/2½ yrs; Oct 2026 update | https://sirfrancismarketingltd.co.ke/properties/misty-springs-apartments-westlands/ |
| Azipa Real Estate | agency | 276/23 floors; Q3 2026 UC; price bands | https://aziparealestate.co.ke/property/misty-springs-apartments-westlands/ |
| Musilli Homes | agency | Plot 24; Crest/Siaya developer attribution; 30%/2½ yrs | https://musillihomes.co.ke/property/misty-spring-westland-apartment-2/ |
| A-list Real Estate | agency | Ready for occupation; 1BR 10M; 60-day balance outlier | https://a-listrealestate.ke/property/mistry-spring-westland-apartment/ |
| GNA Real Estate | agency | Sold out / rent framing; ready for occupation | https://gna.co.ke/project/misty-springs-westlands-1-and-2-bedrooms/ |
| Flamingo Real Estate | agency | Price table + 30%/30 mo (evaluated; denser peers retained preferred) | https://www.flamingorealestate.co.ke/property/misty-springs/ |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| url | https://www.facebook.com/mistyspringwestland | Property / project social (cited by AfricaBiz; live fetch **403** this pass) |
| url | https://ke.linkedin.com/company/tian-yu-international-company-limited | Developer lead (LinkedIn) |
| address | KILIMANI, DENIS PRINT ROAD, B17, NAIROBI 00100 | Developer lead HQ (LinkedIn Locations) |
| address | 24 Westlands Rd, Nairobi | Property (AfricaBiz; Musilli plot 24) |
| phone | +254 711 369955 | Directory listing (AfricaBiz) — owner unclear **`needs_verification`** |
| phone | +254 722 716 182 | Agent: Own It Kenya (CSV) |
| phone | +254 720 469 282 | Agent: Own It Kenya (page) |
| email | sales@ownitkenya.com | Agent: Own It Kenya (CSV) |
| phone | +254 782 000 648 | Agent: Oxford Gate |
| email | sales@ogre.co.ke | Agent: Oxford Gate |
| phone | +254 721 687 339 | Agent: Klin |
| email | propertiesklin@gmail.com | Agent: Klin |
| phone | +254 784 448 888 | Agent: CPK |
| email | info@commercialpropertykenya.com | Agent: CPK |
| phone | +254 722 720 812 | Agent: Sir Francis Homes |
| email | info@sirfrancismarketingltd.co.ke | Agent: Sir Francis |
| phone | +254 742 880 335 / +254 796 007 755 | Agent: Azipa |
| email | azipahomes@gmail.com / info@aziparealestate.co.ke | Agent: Azipa |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 712 406 060 / +254 782 406 060 | Agent: GNA |
| email | support@gna.co.ke | Agent: GNA |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| — | — | No named contractor, architect, financing partner, or land vendor this pass | 0 |

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Status / completion** | CSV off_plan Q4 2025; OGRE Dec 2025; Klin/Azipa Q3 2026 UC; CPK/A-list/GNA complete/ready; short-stay reviews | **No developer status page** → claim set only; highlight all; **`needs_verification`**. Do not invent “handover complete”. |
| 2 | **Developer identity** | LinkedIn Tian Yu self-claim + Musilli Crest/Siaya framing vs agents that omit developer | Lead conf **2**; **`needs_verification`**. No canonical portal developer until official corroboration. |
| 3 | **Storeys** | **23** (multi-agent) vs **27** (Proxima rental) | Agent conflict → show both; majority 23 still capped conf 3; 27 **`needs_verification`** (single source). |
| 4 | **1BR size** | **58 sqm** (Own It plinth + most) vs **57 sqm** (Sir Francis) | Minor; keep both; Prefer Own It **plinth** tag when citing 58. |
| 5 | **2BR price ceiling** | ~13.8–13.9M list vs Klin/Azipa up to **17.5M** vs CPK cash **from 10.5M** vs A-list 1BR **10M** / BuyRent **11M** | Keep **all** in `price_claims[]`; no scalar. |
| 6 | **Payment balance tenor** | 30 months / 2½ years (multi) vs A-list **60 days** | Multi-agent 2½ yrs secondary must-have element; 60-day outlier **`needs_verification`**. |
| 7 | **Sold-out / remaining stock** | OGRE 17 left; CPK/A-list partial sold-out; GNA all sold out | **`needs_verification`** — show, do not canonicalize. |
| 8 | **CSV sales_contact** | Own It ≠ Tian Yu / project Facebook | Split Contact.owner correctly. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned Own It, LinkedIn Tian Yu, Facebook (project), Oxford Gate, Klin, CPK, Sir Francis, Azipa, Musilli, A-list, GNA, Flamingo, BuyRentKenya, AfricaBiz directory, Proxima rental, Concrete City, plus CSV seed. **No developer microsite/PDF found** — kept LinkedIn + Facebook URL as closest official/project channels. Retained 10 densest field-bearing sources (≥5 rule).

**Thin / skipped (not in retained list):**
- https://concretecityproperties.com/property/misty-spring-apartments-westlands/ — JS **Loading…** shell
- https://proxima.co.ke/property/apartment-for-rent/westlands/misty-residence — rental page; used only for **27-floor** conflict note
- https://www.flamingorealestate.co.ke/property/misty-springs/ — overlaps Own It/Klin price+payment; thinner than retained peers
- https://www.buyrentkenya.com/listings/1-bedroom-apartment-for-sale-westlands-area-3878567 — single-unit card; price kept in §1a I only
- https://ke.africabz.com/nairobi/misty-springs-apartments-691845 — directory/reviews; address+FB URL extracted but page thin
- https://www.signalhire.com/companies/tian-yu-international-company-limited — LinkedIn mirror
- CSV NBO-017 row — seed lead only

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://ownitkenya.com/off-plan-apartments-for-sale-in-nairobi/ | Own It Kenya | agent | 2026-10-16 | CSV contact; **plinth** 58/90/99; 30%/30 mo; 23 floors; amenities |
| 2 | https://ke.linkedin.com/company/tian-yu-international-company-limited | Tian Yu International Company Limited | social / developer_lead | 2026-10-16 | Self-claim developers; Misty Springs current; Crest Park / Siaya Park prior |
| 3 | https://www.facebook.com/mistyspringwestland | Misty Spring Westlands | social / project | 2026-10-16 | Project channel (AfricaBiz cites); fetch **403** — URL retained |
| 4 | https://www.ogre.co.ke/properties/misty-springs-apartments-1-and-2-bedroom-apartments-in-westlands/ | Oxford Gate Real Estate | agent | 2026-10-16 | Sold-out flags; Dec 2025; 17 remaining |
| 5 | https://klinproperties.co.ke/property/misty-springs/ | Klin Properties | agent | 2026-10-16 | Q3 2026; 30%/30 mo; 12.6–17.5M 2BR |
| 6 | https://commercialpropertykenya.com/properties/the-misty-spring-apartments-for-sale-in-westland/ | CPK Real Estate | agent | 2026-10-16 | 276/23; “fully complete”; cash from 10.5M |
| 7 | https://sirfrancismarketingltd.co.ke/properties/misty-springs-apartments-westlands/ | Sir Francis Homes | agent | 2026-10-16 | 276/2 blocks; 57 sqm; 30%/2½ yrs; Oct 2026 |
| 8 | https://aziparealestate.co.ke/property/misty-springs-apartments-westlands/ | Azipa Real Estate | agent | 2026-10-16 | 276/23; Q3 2026 UC; price bands |
| 9 | https://musillihomes.co.ke/property/misty-spring-westland-apartment-2/ | Musilli Homes | agent | 2026-10-16 | Plot 24; Crest/Siaya developer attribution; 30%/2½ yrs |
| 10 | https://a-listrealestate.ke/property/mistry-spring-westland-apartment/ | A-list Real Estate | agent | 2026-10-16 | Ready for occupation; 1BR 10M; 60-day balance outlier |

---

## 9. Field harvest

| Field | Misty Springs status | Notes for living must-have list |
|-------|----------------------|---------------------------------|
| `canonical_name` / `aliases` | OK (multi-agent + LinkedIn) | Conf 4 without developer site |
| `status` | Claim set + hard conflict | Late inventory vs UC vs CSV off_plan — reinforce status as claim set |
| `geography` street + landmarks | OK agent consensus | Plot **24** Westlands Rd useful when directory+agent agree |
| `primary_developer` | **Lead only (conf 2)** | Reinforces: blank CSV + agent redistributors ≠ developer; LinkedIn-only identity stays **`needs_verification`** |
| GroupCompany | none | Correctly empty |
| `unit_types` / sizes | Agent 1BR/2BR; Own It **plinth** tag | **Strengthen** plinth tagging when any source labels measure |
| `total_units` + `block_count` | 276 / 2 (agent ≥4) | Supports proposed must-have claim set; still **`needs_verification`** without official |
| `storeys` | 23 vs 27 claim set | Supports storeys as claim set |
| `price_claims[]` | A–J retained | Cash vs list (CPK) + sold-out context |
| `payment_plan` | **30% / ~2½ yrs** via **≥4 agents** | Must-have **met without developer**; conf capped at 3 |
| `construction_progress` | unknown | No tracker |
| Named stakeholders | none | — |
| `amenities` core vs inflation | Core agent list vs Proxima jogging track | Reject single-source adds |

### Proposed consensus bumps (for coordinator / schema steward)

| Proposed | This project | Suggested consensus note |
|----------|--------------|--------------------------|
| Explicit **plinth** size tag when agent/developer labels it | Own It Misty Springs | Bump plinth/gross tagging examples beyond flyer-only |
| Developer identity from **LinkedIn-only** | Tian Yu | Keep conf ≤2; never portal-canonical alone |
| Payment must-have via **agent ≥4 without developer** | 30% here | Already locked; Misty = clean worked example (conf 3 ceiling) |
| `total_units` / `blocks` agent consensus ≥4 | 276 / 2 | Still **`needs_verification`** until official |
| Status claim set when complete vs UC vs off_plan collide | This dossier | High-priority verification queue item |

---

## Open questions (verification / developer input)

1. Confirm **legal developer** (Tian Yu International Company Limited vs other SPV) via LOO / registry / official site.
2. Reconcile **status**: completed/ready vs Q3 2026 UC vs Dec 2025 / Q4 2025 CSV.
3. Confirm **23 vs 27** storeys and **276** unit count on official drawings.
4. Binding **payment plan** / reservation deposit on current LOO (30%/2½ yrs vs 60-day outlier).
5. Current **price list** and which typology bands remain available (sold-out claims diverge).
6. Gross vs plinth for 57/58/90/99 sqm — prefer labelled schedule.
7. Who owns **+254 711 369955** and the Facebook page admin (developer sales office vs agent)?
