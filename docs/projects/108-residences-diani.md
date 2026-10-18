---
slug: 108-residences-diani
external_id: DIA-001
geography: coast-diani
wave: discovery
cycle: new-geo
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# 108 Residences (DIA-001) — Diani / Coast (new geography)

Discovery lead (unverified until sourced): [kenya-offplan-leads.md](/cursor/stores/self/docs/discovery/kenya-offplan-leads.md) — Diani Beach Road; Omicron Resources Ltd (Enin); start Mar 2025 / complete Dec 2026 / handover Jan 2027; URLs 108residences.com · Enin · HomesInKenya.

Live research: official project site **108residences.com** (home, residences, lifestyle, location, completed projects, contact) + Enin + agents/portals. Accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official:** **do not assume** → **`needs_developer_input`**.
- Prices: always **`price_claims[]`** (no single scalar). Official site fetched = **no prices** → all commercial bands are agent/portal unless proven otherwise.
- Payment must-have if **any developer source** **or** ≥4 agent sources.
- Amenities: **feature-aware** — map developer core to taxonomy scopes; agent inflation + **`needs_verification`**.
- Lead sheet blurbs = **suspect** until corroborated.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer/official site when agreeing. Claim set / secondary = kept for conflict detection.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | 108 Residences (also **108 Lifestyle & Residences** as dual concept) | 5 | 108residences.com home + residences + lifestyle |
| `aliases` | secondary | 108 Residences Diani; 108 Lifestyle; “The Residence” (BuyRent copy) | 3 | agents |
| `status` | claim set | Official site markets live inventory / floor plans (no progress % widget text recovered). Agents: **under construction**; timeline Mar 2025→Dec 2026. Dunhill “soon-to-be-launched” Lifestyle retail | 3 | Enin; HomesInKenya; BuyRent; Dunhill |
| `geography.city_region` | **CANONICAL** | **Diani**, Kwale County / Kenyan coast | 5 | 108residences.com |
| `geography.neighbourhood_street` | **CANONICAL** | **Diani Beach Road**; **420 steps** to Indian Ocean / beach | 5 | residences + location pages (+ agents agree) |
| `geography.landmarks` | secondary (multi-source) | Opposite **108 Seaviews** (Enin); Carrefour ~900 m N / Chandarana ~1.2 km S (official map); Diani Airport ~1.9–2 km; Diani Hospital 2.3 km; Tradewinds School 1.1 km | 4 | property-map; Enin; home |
| `geography.county` | secondary | Kwale (agent address strings: Msambweni / Ukunda / Kinondo) | 3 | HomesInKenya; Mkaazi |
| `geography.plot_size` | secondary — **needs_verification** | **1.8 acres** | 2 | HomesInKenya; BuyRent |
| `geography.lat_lng` | geocode — **needs_verification** | **−4.324829, 39.570190** (`geo_method=geocode`) | 3 | Nominatim Diani Beach Road 2026-10-16; street known, plot GPS unpublished — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | best evidence (not on official HTML) | → `dev-omicron-resources` — **Omicron Resources Ltd** named on Enin; prior 108-brand brochures (Sandbox / Galu Breeze) also disclaimer **Omicron Resources Ltd**. Official 108residences.com pages fetched **do not name** Omicron | 4 | Enin; prior Daiga/Dunhill PDFs |
| `unit_types` | **CANONICAL** | Studio Type 1 & 2; 1BR Type 1 & 2; 2BR Type 1 & 2; 3BR | 5 | 108residences.com/108-home/108-residences/ |
| `size_by_type` | **CANONICAL** | Studio **50** / **67** sqm; 1BR **83** / **92** sqm; 2BR **108** / **129** sqm; 3BR **190** sqm | 5 | official residences floor-plan cards |
| `size_by_type` | secondary — **needs_verification** | HomesInKenya 1BR **85 / 90 / 92** sqm bands (partially overlaps) | 2 | HomesInKenya |
| `size_measure_tag` | unknown | Gross vs plinth not labelled | 0 | — |
| `total_units` | **CANONICAL** (home + type cards **agree**) | **68** = 20 studio + 22 × 1BR + 24 × 2BR + 2 × 3BR | 5 | home counters; residences unit counts |
| `total_units` | secondary — **needs_verification** | Dunhill: **60 apartments** | 2 | dunhillconsulting.com |
| `building_specs.storeys` | **CANONICAL** (stack language) | Lower floor · Ground · 1st · 2nd · Rooftop terrace (+ Lifestyle: Basement / Ground / Rooftop) — **low-rise** framing; storey count as marketing “floors” not published as “N-storey” | 4 | home floor-plan tabs; lifestyle |
| `building_specs.blocks` | secondary — **needs_verification** | HomesInKenya: elevators / multi-purpose rooms **“in each block”**; Mkaazi “multiple residential blocks” — official home does not state block count | 2 | HomesInKenya; Mkaazi |
| `building_specs.parking` | claim set — soft conflict | Official: **105** car parking (+ 16 utility rooms). HomesInKenya: **106** bays (25 visitor) | 4 / 2 | home vs HomesInKenya |
| `price_claims[]` | claim set — **no official price list** | See §1a — keep all options | ≤3 | |
| `currency` | secondary | KES (all agent commercial copy) | 4 | Enin; agents |
| `payment_plan` | secondary — **needs_verification** (threshold **not** met) | HomesInKenya only dense schedule: KES **500,000** booking; **20%** deposit (less booking) on SPA; **70%** in five construction instalments; **10%** on completion. Mkaazi “structured/flexible” only. **No developer % on official site** | 2 | HomesInKenya; Mkaazi |
| `completion_estimate` | secondary multi-agent — **needs_verification** | Start **Mar 2025**; complete **Dec 2026**; handover **Jan 2027** — Enin + HomesInKenya + BuyRent + CPK. **Not found on 108residences.com pages this pass** → not developer-canonical | 3 | agents/portals |
| `amenities` (core — official) | **CANONICAL** + feature slugs | See §1c | 5 | home amenity tiles + service URLs |
| `amenities` agent denser list | secondary — **needs_verification** where not on official tiles | Kids’ play; landscaped gardens; 46 m pool + children’s pool; 100 KVA solar PV; well water / borehole; intercom; visitor lounge; driver’s lounge; elevators each block; AC in all rooms; fitted kitchen kit — Enin / HomesInKenya / CPK | ≤3 | agents (Enin overlaps some) |
| `legal_title` | secondary — **needs_verification** | Enin: **99-year leasehold** with future sectional titles (Sectional Properties Act 2020) | 2 | Enin only |
| `service_charge` | secondary — **needs_verification** | Enin: **KES 12,000–35,000**/month | 2 | Enin |
| `availability_claim` | secondary — **needs_verification** | Mkaazi “**50%+ sold**”; HomesInKenya **3BR sold out**; Dunhill limited furnished stock (1 studio / 4×1BR) | 2 | agents |
| `master_planned_community` / mixed-use | **CANONICAL** (concept) | Dual **108 Residences** + **108 Lifestyle** retail hub | 5 | home; lifestyle page |

### 1a. Price claims — keep **all** options (no canonical scalar)

Official site: **no selling prices** on pages fetched → no developer price canonical.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Enin band | From **KES 8M–29M**; sizes 50–190 sqm; listing card **18M** (2BR framing) | eningroup.com | Agent/portal — names Omicron |
| B | HomesInKenya typed | Studios **9.5M** (50) / **10.75M** (67) + note “from 8M Block A”; 1BR **13.7–14.5M**; 2BR **18.5M** (108); 3BR **29M** (sold out); card “from 9M” | homesinkenya.co.ke | Agent — densest typed |
| C | Mkaazi indicative | Studios from **~8M**; 1BR **~13.5M**; 2BR **~18–21M**; 3BR **~29M** | mkaazirealestate.com | Agent |
| D | BuyRentKenya | Studios **8.75–9.5M**; 1BR **13.5–14M**; 2BR **18.5–18.75M**; 3BR from **30M**; listing headline **15M** | buyrentkenya.com | Agent — 3BR **30M** conflicts B/C **29M** |
| E | CPK | 2BR **108 sqm = 18.5M**; Dec 2026 / Jan 2027 | commercialpropertykenya.com | Agent |
| F | Dunhill (furnished) | Furnished studio from **13.8M**; furnished 1BR from **17.5M** (limited units) | dunhillconsulting.com | Agent — furnished premium; also official-site contact |
| G | Discovery lead | No CSV seed row (national discovery) | kenya-offplan-leads.md | Lead only |

**Canonical price:** none.

### 1b. Official unit matrix (canonical sizes / counts)

| Type | Units | Area (sqm) | Parking bays (per type card) |
|------|------:|----------:|-----------------------------:|
| Studio Type 1 | 10 | 50 | 1 |
| Studio Type 2 | 10 | 67 | 1 |
| 1BR Type 1 | 14 | 83 | 1 |
| 1BR Type 2 | 8 | 92 | 1 |
| 2BR Type 1 | 12 | 108 | 1 |
| 2BR Type 2 | 12 | 129 | 1 |
| 3BR | 2 | 190 | 2 |
| **Total** | **68** | | |

Home headline counters (**20 / 22 / 24 / 2**) match this matrix.

### 1c. Amenities / features (feature-aware)

**Development-scope core (canonical — 108residences.com amenity tiles / service pages):**

| Taxonomy slug | Official wording |
|---------------|------------------|
| `rooftop_solar` / solar | Solar Generated Power |
| `backup_generator` | Backup Generator |
| `gym` | Gym |
| `swimming_pool` | Swimming Pool |
| `concierge` | 24/7 Concierge |
| `gated_security` | 24/7 Security |
| `lounge` / terrace | Rooftop Terrace |
| `convenience_store` / retail (community) | **108 Lifestyle** retail hub (boutiques, cafés, services) |
| `parking` | Car Parking **105** |
| `laundry_shared` | Laundry Area (rooftop tab) |
| `conference_room` (soft) | Multi Purpose Room ×2 (rooftop tab) |

**Apartment-scope (official type cards):** `walk_in_closet` (selected 1BR/3BR); parking bay(s) per unit; baths/kitchen counts on cards.

**Agent / Enin extras — show + `needs_verification` unless also on official tiles:** kids’ play; landscaped gardens; children’s pool; “46m” pool length; 100 KVA solar PV; well water / borehole; water storage; CCTV; access control; intercom; elevators; visitor lounge; driver’s lounge; AC all rooms; fitted kitchen appliances; smart home (Enin).

### Payment plan — threshold recount

| Element | Sources | Count | Threshold? | Status |
|---------|---------|------:|------------|--------|
| Developer % / LOO on 108residences.com | Not found this pass | 0 | — | unknown |
| HomesInKenya full schedule (500k / 20% / 70% / 10%) | 1 | 1 | Need ≥4 **or** developer | **Not met** — secondary NV |
| “Structured / flexible / phased” | Mkaazi (+ soft others) | ≥1 | — | Soft secondary |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-omicron-resources` |
| `legal_name` | Omicron Resources Ltd (as styled on Enin + prior 108-brand brochure disclaimers) |
| `trading_names` | Omicron Resources; “108” project brand on 108residences.com |
| `website` | Project microsite https://www.108residences.com/ — **no standalone Omicron corporate site found this pass** |
| `evidence` | Enin listing: “Developer: Omicron Resources Ltd”. Prior Daiga/Dunhill PDFs for Sandbox / Galu Breeze carry Omicron Resources Ltd disclaimer — same sales phones as current site. **Gap:** current official HTML does not print “Omicron” |
| `group_company_id` | **null** |
| `confidence` | **4** (strong pattern + Enin; not yet printed on live official pages) |
| `prior_projects_mentioned` | Official completed strip: **The Sandcastle**, **The Sandbox**, **108 Galu Breeze**, **108 Seaviews** (links to daigaproperties.com) — delivery claims not re-verified this pass |

**Do not treat Daiga or Dunhill as developer** — they are sales contacts on the official site.

---

## 3. GroupCompany

**None** evidenced.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Conf |
|------|-------------------|----------|-----:|
| **Daiga Properties** | `marketing_partner` / sales office | Official contact phones **+254 740 108 108**, **+254 793 108 108**, email sales@daigaproperties.com; Daiga logo/links on completed-projects strip; contact page “Nairobi, Kenya” | 5 |
| **Dunhill Consulting Limited** | `marketing_partner` / co-marketer | Official footer phones + info@dunhillconsulting.com; own furnished listing for 108 Residences | 5 |

Unproven parent link between Omicron ↔ Daiga ↔ Dunhill → keep as RelatedParty, not GroupCompany.

---

## 5. Agents + Contacts

### Agents / portals

| Party | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Daiga Properties | sales / RelatedParty | Official site primary sales contact | https://www.108residences.com/contact/ |
| Dunhill Consulting | agency / RelatedParty | Official co-contact + furnished listing | https://www.dunhillconsulting.com/properties/studio-1-2-3-bedroom-apartments/ |
| Enin | portal/agency | Dense brief; **names Omicron + Imperium + Space Art**; timeline | https://eningroup.com/properties/a-blend-of-luxury-living-in-diani |
| Homes In Kenya | agency | Typed prices + payment schedule + amenity density | https://homesinkenya.co.ke/property/108-residences-diani-studio-1-2-and-3-bedroom-apartments/ |
| Mkaazi Real Estate | agency | Indicative bands; 50% sold claim | https://mkaazirealestate.com/property/108-residences-diani-contemporary-coastal-apartments-for-sale/ |
| CPK Real Estate | agency | 2BR 18.5M; Dec 2026 / Jan 2027 | https://commercialpropertykenya.com/properties/2-bedroom-apartments-steps-from-diani-beach/ |
| BuyRentKenya listing | portal | Price ranges; 1.8 acres; timeline | https://www.buyrentkenya.com/listings/1-bedroom-apartment-for-sale-diani-3873450 |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 740 108 108 | Daiga / project sales (official) |
| phone | +254 793 108 108 | Daiga / project sales (official) |
| email | sales@daigaproperties.com | Daiga (official contact) |
| phone | +254 786 386 445 | Dunhill (official footer) |
| phone | +254 720 911 136 | Dunhill (official footer) |
| email | info@dunhillconsulting.com | Dunhill |
| url | https://www.108residences.com/ | Property |
| address (sales office hint) | Nairobi, Kenya (contact page) — **not** the Diani site address | Official contact |
| site address | Diani Beach Road, Diani | Property |
| phone | +254 791 485 781 | Enin |
| email | info@eningroup.com | Enin |
| phone | +254 742 752 515 | Homes In Kenya |
| email | info@homesinkenya.co.ke | Homes In Kenya |
| phone | +254 724 568 989 / +254 763 568 989 | Mkaazi |
| email | info@mkaazirealestate.com | Mkaazi |
| phone | +254 784 448 888 | CPK |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| **Imperium PM** | project_manager / other | Enin: “Project Manager: Imperium PM” | 3 |
| **Space Art Architects** | architect | Enin: “Architects: Space Art Architects” | 3 |

Not repeated on official 108residences.com pages fetched → keep conf 3 + **`needs_verification`** for engagement letter / LOO.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Developer on official site** | Enin/PDFs: **Omicron Resources Ltd**. Live official HTML: **unnamed**; Daiga/Dunhill contacts dominate | Primary = Omicron at conf **4** with explicit gap; do not treat Daiga as developer |
| 2 | **Prices** | No official list vs Enin 8–29M vs HomesInKenya typed vs BuyRent 3BR **30M** vs Dunhill furnished premiums | Keep all `price_claims[]`; no scalar |
| 3 | **Total units** | Official **68** vs Dunhill **60** | Canonical **68** (developer pages agree); Dunhill NV |
| 4 | **Parking count** | Official **105** vs HomesInKenya **106** | Prefer official 105; keep secondary |
| 5 | **Completion timeline** | Multi-agent Mar 2025 / Dec 2026 / Jan 2027 — **absent** from official pages this pass | Secondary NV; **not** canonical |
| 6 | **Payment %** | HomesInKenya only dense schedule | Threshold not met |
| 7 | **3BR price / sold-out** | 29M (HomesInKenya/Mkaazi) vs 30M (BuyRent); sold-out claim HomesInKenya only | Show + NV |
| 8 | **1BR sizes** | Official 83/92 vs HomesInKenya 85/90/92 | Canonical = official cards |
| 9 | **Contact geography** | Project in Diani; official contact “Nairobi, Kenya” | Split site vs sales office |

---

## 8. Sources

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned official home, residences, lifestyle, location/map, completed projects, contact, service amenity URLs; Enin; HomesInKenya; Mkaazi; Dunhill; CPK; BuyRent; prior Omicron PDF disclaimers; discovery lead. **Always kept** 108residences.com. Retained 10 densest.

**Thin / skipped:**
- Individual service blog posts (gym/pool/etc.) — amenity names already on home tiles
- Sandcastle project page on 108residences.com — prior completed product; boilerplate copy
- UK Companies House “OMICRON RESOURCES LIMITED” hit — **different jurisdiction / unverified link** to Kenyan Omicron; do not merge
- Discovery lead row alone

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://www.108residences.com/ | 108 Residences & Lifestyle | project_site | 2026-10-16 | Unit counters 20/22/24/2; amenities; parking 105; Daiga/Dunhill contacts — **always keep** |
| 2 | https://www.108residences.com/108-home/108-residences/ | 108 Residences | project_site | 2026-10-16 | Typed sizes + unit counts; 420 steps |
| 3 | https://www.108residences.com/108-home/108-lifestyle/ | 108 Residences | project_site | 2026-10-16 | Retail dual concept |
| 4 | https://www.108residences.com/property-map/ | 108 Residences | project_site | 2026-10-16 | Distances; beach framing |
| 5 | https://www.108residences.com/contact/ | 108 Residences | project_site | 2026-10-16 | Daiga phones/email; Nairobi contact line |
| 6 | https://eningroup.com/properties/a-blend-of-luxury-living-in-diani | Enin | agent/portal | 2026-10-16 | **Omicron** + Imperium + Space Art; timeline; 8–29M; title claim |
| 7 | https://homesinkenya.co.ke/property/108-residences-diani-studio-1-2-and-3-bedroom-apartments/ | Homes In Kenya | agent | 2026-10-16 | Typed prices; payment schedule; amenity density |
| 8 | https://mkaazirealestate.com/property/108-residences-diani-contemporary-coastal-apartments-for-sale/ | Mkaazi | agent | 2026-10-16 | Indicative bands; 50% sold |
| 9 | https://commercialpropertykenya.com/properties/2-bedroom-apartments-steps-from-diani-beach/ | CPK | agent | 2026-10-16 | 2BR 18.5M; Dec 2026 / Jan 2027 |
| 10 | https://www.dunhillconsulting.com/properties/studio-1-2-3-bedroom-apartments/ | Dunhill | agent | 2026-10-16 | Furnished premiums; **60** units claim; official co-contact |

**Also cited (not double-counted in 10):** BuyRentKenya listing (price ranges / 1.8 acres); prior Omicron disclaimer PDFs via Daiga/Dunhill for brand pattern.

---

## 9. Field harvest → must-have / new-geo notes

| Field | 108 Residences status | Harvest note |
|-------|----------------------|--------------|
| New geography **Diani / Kwale** | First Coast dossier | Extend master index beyond Nairobi |
| Dual product **Residences + Lifestyle retail** | Canonical mixed-use | Propose `mixed_use_retail` / community scope features |
| `total_units` | Official **68** agree | Strong must-have when home + type cards agree |
| Official sizes without prices | OK sizes / empty prices | Reinforces multi `price_claims[]` when developer silent on price |
| Developer named off-site only | Omicron via Enin + prior PDFs | Harvest: “developer_on_agent_not_microsite” QA pattern |
| Sales office Nairobi vs asset Diani | Contact page | Capture `sales_office_geo` separately |
| Payment | Threshold not met | One dense agent schedule only |
| Timeline | Agent consensus Dec 2026 / Jan 2027 | Promote only after official page agrees |
| Stakeholders Imperium / Space Art | Enin only | Capture + NV |
| Feature taxonomy | Solar + generator + gym + pool + concierge + security + rooftop + Lifestyle retail | Good Coast amenity seed |

---

## Open questions (developer input)

1. Print **Omicron Resources Ltd** (or other legal entity) on 108residences.com?
2. Publish official **price list** and binding **payment / LOO** schedule?
3. Confirm **completion / handover** dates on the official site (Mar 2025 / Dec 2026 / Jan 2027)?
4. Reconcile Dunhill **60** vs official **68** units; parking **105 vs 106**?
5. Confirm Imperium PM / Space Art Architects engagement?
6. Live construction progress % / photos?
7. Clarify Daiga vs Dunhill vs Omicron legal relationships; Companies Registry name?
