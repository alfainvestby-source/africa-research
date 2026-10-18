---
slug: brookside-oak
external_id: DISC-NBO-006
discovery_lead: true
cycle: discovery
pilot: false
sources_evaluated: 14
sources_retained: 10
last_verified_at: 2026-10-16
---

# Brookside Oak Residency (DISC-NBO-006) — discovery research

**Not in seed CSV** (NBO-001…017). Discovery lead from [kenya-offplan-leads.md](/cursor/stores/self/docs/discovery/kenya-offplan-leads.md) (Westlands / Brookside; **≠ Luna Oak NBO-012**). Discovery ID `DISC-NBO-006` until NBO allocation policy set.

Live research accessed **2026-10-16**. Project microsite **https://brooksideoak.co.ke/** + Oak Group Residences marketing page + multi-agent listings. Official brochure PDF present on microsite (fetched; text extraction weak / image-heavy this pass — not used for novel facts).

**Method locks applied:**
- Developer vs agents: if developer/official sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`**; no assumed winner.
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agent/portal sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**.
- Unproven brand vs legal SPV → **`marketing_partner`** (not GroupCompany).
- **Identity lock:** this dossier is **Brookside Oak (Muguga Green, Westlands)** — **not** Luna Oak Residency (NBO-012, Kilungu Road, Kilimani). See §0.

---

## 0. Identity vs Luna Oak (NBO-012) — do not merge

| Dimension | **Brookside Oak** (this dossier) | **Luna Oak Residency (NBO-012)** |
|-----------|----------------------------------|----------------------------------|
| Geography | **Muguga Green**, Westlands / Brookside; UN Blue Zone; next to **Safaricom HQ** | **Kilungu Road**, Kilimani (off Elgeyo Marakwet); opp. Oyster Bay / Cavina |
| Plot / GPS | No NEMA plot/GPS recovered this pass | NEMA **Nairobi/Block 17/283**; **−1.293751, 36.777031** |
| Filing proponent | **Unknown** this pass (microsite email **vantungcompanyltd@gmail.com**) | **Mingland Company Limited** (NEMA ESIA) |
| Marketing brand | **Oak Developer** (brooksideoak.co.ke) + **Oak Group Residences** lists this project separately | **Oak Group Residences** microsite for Luna Oak |
| Scale claims | **26** floors; **3 towers** (A/B/C) on Oak Group presentation / agents | **25** floors; **294** units (NEMA + Oak Group agree) |
| Unit mix | **1 / 2 / 3 BR** (+ DSQ / study on select) | **2 / 3 / 4 BR** (+ DSQ) |
| Price “from” band | ~**KES 8.2M–9.9M** (claim set) | ~**KES 11.5M–14.8M** (Oak Group NDI) |
| Completion framing | **Feb 2026 → June 2029** / Q2 2029 | Mostly **Sep / Q3 2029** (agents); Oak Group silent |
| Seed CSV | **Not present** | **NBO-012** |

Oak Group’s ongoing-developments page lists **both** projects as separate cards — corroborates they are **sibling marketed assets**, not aliases.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer microsite sources **agree**. Claim set / secondary = conflict detection. **`needs_developer_input`** = official marketing surfaces disagree.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Brookside Oak Residency (also styled Brookside Oak) | 5 | brooksideoak.co.ke; oakgroup; multi-agent |
| `aliases` | secondary | Brookside Oak; Brookside Oak Apartments; Brookside Oak Residence | 4 | agents; NRE |
| `status` | claim set | Microsite **Year of build 2026–2029** + live progress videos; agents **under construction** / off-plan; Ravi “construction began Feb 2026”; NRE widget **58%** — **`needs_verification`** (single portal UI) | 4 / 1 | brooksideoak; Ravi; NRE; Craiova |
| `geography.city` | **CANONICAL** | Nairobi | 5 | microsite; all |
| `geography.neighbourhood_street` | **CANONICAL** | Westlands / Brookside — **Muguga Green** (next to Safaricom HQ 3); UN Blue Zone framing | 5 | brooksideoak.co.ke; oakgroup; multi-agent |
| `geography.lat_lng` | geocode — **needs_verification** | **−1.258594, 36.788122** (`geo_method=geocode`) | 3 | Nominatim Muguga Green Brookside 2026-10-16; ≠ Luna Oak NEMA — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **lead** — **`needs_verification`** | → `dev-van-tung-company` (**Van Tung Company Ltd** proposed from microsite email **vantungcompanyltd@gmail.com**); brand **Oak Developer** | 2–3 | brooksideoak.co.ke contacts only — no Companies Registry / NEMA name this pass |
| `marketing_brand` | RelatedParty | **Oak Group Residences** (oakgroup.co.ke) — see §4 | 4 | oakgroup project + ongoing list |
| `unit_types` | **CANONICAL** (microsite types) | Classic / Premier / Luxurious **1BR**; Classic / Premier **2BR**; Classic **3BR**; Luxurious **3BR+DSQ**; Luxury **3BR+Study+DSQ** (penthouse-labelled 200㎡ on forms) | 5 | brooksideoak.co.ke |
| `size_by_type` | **CANONICAL** (microsite) | 1BR **65 / 75 / 89** ㎡; 2BR **100 / 118** ㎡; 3BR **145** ㎡; 3BR+DSQ **172** ㎡; 3BR+Study+DSQ **200** ㎡ | 5 | brooksideoak.co.ke |
| `size_by_type` | secondary agent variants — **`needs_verification`** | Extra 1BR **70** ㎡; 3BR **135 / 142 / 194** ㎡ rows on some agents (not on microsite type list) | ≤3 | Masterways; CPK; Craiova; Palmier |
| `size_measure_tag` | unknown | Internal / “㎡” — gross vs plinth **not labelled** | 0 | — |
| `building_specs.storeys` | **CANONICAL** (microsite + Oak presentation agree on 26) | **26** floors | 5 | brooksideoak.co.ke; Oak Group presentation (search/index + PDF host) |
| `building_specs.towers_blocks` | secondary / presentation | **3 towers** — Blocks **A, B, C** (presentation: residency floors **5–26**; amenities **4th** + rooftop; 1&2BR in A/B, 3BR in C) | 4 | Oak Group presentation; Ravi “three towers” |
| `building_specs.parking` | **CANONICAL** (microsite) | **6 levels**, **B2 – 3rd floor** | 5 | brooksideoak.co.ke |
| `total_units` | secondary — **`needs_verification`** | NRE: **513** units | 1 | NRE only |
| `price_claims[]` | claim set — keep **all**; microsite vs Oak Group “from” → **`needs_developer_input`** | See **§1a** | ≤5 | |
| `currency` | **CANONICAL** | KES | 5 | all |
| `payment_plan.term` | secondary strong agent + soft official window | **40 months** / construction **Feb 2026 – June 2029** | 4 / 3 | Multi-agent; microsite year band; presentation |
| `payment_plan.deposit` | secondary must-have (**≥4 agents**; no % on microsite HTML) | **20% deposit**; balance over construction / **10–15% every 6 months** (Craiova; LinkedIn) | 3 | Ravi; GNA; Craiova; NRE — threshold **met via ≥4**; **`needs_verification`** vs LOO |
| `completion_estimate` | **CANONICAL** framing (microsite + multi-agent agree **2029**) | **June 2029** / **Q2 2029**; construction window **2026–2029** | 5 | brooksideoak year; Ravi; CPK; Masterways; NRE; GNA; Gerryville |
| `amenities` (core) | **CANONICAL** (microsite list) | 2 grand receptions & concierge; **2 rooftop heated pools**; rooftop paddle court; **1 indoor heated pool**; fitness centre; café & minimart; working hub; indoor children’s play; lush gardens; residents’ clubhouse; private cinema; exclusive sauna; UN-standard security | 5 | brooksideoak.co.ke |
| `amenities` | secondary Oak Group feature chips | Pharmacy; conference room; spa; yoga; rooftop garden/chill; billiards (“Billbards”) room | ≤3 | oakgroup.co.ke/properties/brookside-oak — **`needs_verification`** vs microsite core |
| `construction_progress` | secondary | Microsite hosts progress video playlist (bare land → mid-2026 updates); NRE **58%** UI — **`needs_verification`** | 2 / 1 | brooksideoak #progress; NRE |
| `legal_title` | unknown | — | 0 | — |

### 1a. Price claims — keep **all** options (no canonical scalar)

Microsite publishes a full typed table (**from 9.9M** on Classic 1BR). Oak Group card **from 8.2M**. Agents span **8.0–9.9M** entry points. **Official vs official** on headline “from” → **`needs_developer_input`**.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Developer microsite typed list | Classic 1BR **65㎡ from 9.9M**; Premier 1BR **75 from 10.5M**; Lux 1BR **89 from 12.4M**; Classic 2BR **100 from 14.0M**; Premier 2BR **118 from 16.5M**; Classic 3BR **145 from 19.9M**; Lux 3BR+DSQ **172 from 23.5M**; Lux 3BR+Study+DSQ **200 from 27.5M** | brooksideoak.co.ke | Official typed |
| B | Oak Group marketing “from” | **From KES 8,200,000** | oakgroup.co.ke/properties/brookside-oak · ongoing-developments | Official marketing — **`needs_developer_input`** vs A’s 9.9M from |
| C | Agent lower intro table (CPK / Masterways / Palmier / GNA cluster) | Classic 1BR **from 8.8M**; Premier 1BR **10M**; Lux 1BR **12M**; 2BR **13.5 / 16M**; 3BR **18.2 / 19.6 / 23.2 / 26–27M** (size rows vary) | CPK; Masterways; Palmier; GNA | Secondary |
| D | Ravi mixed | Hero **from 8.4M**; detail rows include **8.2 / 8.4 / 9.2 / 9.9** (1BR) and **13.5 / 16 / 19.6 / 23.2 / 27** | ravihomes.co.ke | Secondary — own-page spread · **`needs_verification`** |
| E | Gerryville / Craiova (closer to microsite) | Aligns near **9.9 / 10.5 / 12.4 / 14 / 16.5 / 19.9 / 23.5–27.5M** (Craiova has extra 70㎡ / 142㎡ / 25.5M variants) | gerryvillehomes; craiova | Secondary |
| F | NRE simplified | 1BR **from 8.0M**; 2BR **13.5M**; 3BR **18.2M**; 3BR+DSQ **23.2M** | nairobirealestate.co.ke | Secondary |
| G | Proxima marketing | Homepage/meta **from 8.4M** / **9.9M** (surfaces differ) | proxima.co.ke | Agent/consultant · secondary |

**Canonical price:** none as a single portal scalar. Prefer microsite typed rows (A) when citing developer-backed unit prices; retain B–G.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold (≥4 agents **or** any developer)? | Status |
|---------|------------------------------|------:|---------------------------------------------|--------|
| Construction / payment window **~40 months** to **June 2029** | Ravi; CPK; Masterways; Palmier; Gerryville; Craiova; NRE; GNA; Oak presentation (indexed) | ≥4 (+ soft microsite 2026–2029) | Met | Strong secondary; microsite agrees on years |
| **20% deposit** | Ravi; GNA; Craiova; NRE (copy + calculator) | **≥4** | **Met via ≥4 agents** | Must-have at conf **3**; **`needs_verification`** vs LOO (no % on microsite HTML) |
| **10–15% every 6 months** | Craiova; LinkedIn (Yakang Gao) | 2 | Below ≥4 | Secondary · **`needs_verification`** |
| Developer LOO / brochure payment schedule | Brochure PDF on microsite not text-extracted this pass | 0 usable | — | unknown |

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-van-tung-company` (**proposed**) |
| `legal_name` | **Van Tung Company Ltd** (inferred from sales email **vantungcompanyltd@gmail.com**) — **unverified** against registry |
| `trading_names` | Oak Developer; Oak Developers (agents); Brookside Oak Residency |
| `website` | https://brooksideoak.co.ke/ |
| `evidence` | Microsite brand “Oak Developer”; showroom contacts; email domain-style string. Agents attribute **Oak Developers**. Masterways says **Premier Developers** (outlier). NRE labels **“The Oaks”** |
| `group_company_id` | **null** — do not invent parent above Van Tung / Oak Developer |
| `csv_name_note` | Not in seed CSV |

**Developer confidence:** brand/site **4**; legal entity name **2–3** until registry/NEMA confirm. Do **not** treat Proxima, CPK, or Ravi as developers.

---

## 3. GroupCompany

**None proven.** Oak Group Residences is modeled as **`marketing_partner`** (§4), same lock as Luna Oak ↔ Mingland — not automatically a parent of Van Tung / Oak Developer.

---

## 4. RelatedParty

| Name | relationship_type | Evidence | Notes |
|------|-------------------|----------|-------|
| **Oak Group Residences** (oakgroup.co.ke) | **`marketing_partner`** | Dedicated Brookside Oak property page; ongoing-developments card **from 8.2M**; hosts BrooksideOak Presentation PDF; “Talk To The Developer” contacts | Same brand family as Luna Oak marketing — **does not** make Brookside Oak = Luna Oak |
| Proxima Real Estate | marketing_agent / consultant | proxima.co.ke/brookside-oak project page | Agent |

---

## 5. Agents + Contacts

### Agents / portals linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Oak Group Residences | developer_marketing | Portfolio + presentation PDF; from 8.2M | https://oakgroup.co.ke/properties/brookside-oak/ |
| Proxima Real Estate | agency | Project overview / amenities | https://www.proxima.co.ke/brookside-oak/ |
| CPK Real Estate | agency | Price table; June 2029; 40-mo plan | https://commercialpropertykenya.com/properties/brookside-oak-apartments-westlands/ |
| Ravi Homes | agency | 20%; 40 mo; Feb 2026 start; three towers | https://ravihomes.co.ke/developments/brookside-oak/ |
| Masterways Real Estate | agency | Typed prices; “Premier Developers” label | https://masterways.co.ke/properties/brookside-oak-residency |
| Palmier Properties | agency | Typed prices; Feb 2026–Jun 2029 | https://palmierproperties.co.ke/estate_property/brookside-oak-a-premier-address-in-westlands/ |
| Gerryville Homes | agency | Microsite-aligned prices; 40 mo | https://gerryvillehomes.com/brookside-oak-residency/ |
| GNA Real Estate | agency | 20%; Q2 2029; price table | https://gna.co.ke/project/brookside-oak-residency-westlands-1-2-and-3-beds-plus-dsq/ |
| Craiova Realtors | agency | 20% + 10–15%/6 mo schedule | https://craiovarealtors.com/property/brookside-oak-residency-in-westlands/ |
| NRE Real Estate | agency | 20%/40 mo; 513 units claim; 58% progress | https://nairobirealestate.co.ke/properties/brookside-oak-residence |

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 729 099 699 | Project sales (brooksideoak.co.ke) |
| phone | +254 715 767 757 | Project / Oak Developer (header) |
| email | vantungcompanyltd@gmail.com | Project sales (microsite) |
| address | Muguga Green, Westlands (Next to Safaricom HQ 3) | Showroom / site |
| url | https://brooksideoak.co.ke/ | Property |
| email | oakgroup2010@gmail.com | Oak Group marketing |
| phone | +254 110 378 960 / +254 725 365 466 / +254 796 362 145 | Oak Group (Wally / Mei / Sue) |
| phone | +254 715 580 580 | Oak Group Brookside page WhatsApp |
| phone | +254 752 444 999 / +254 788 444 999 | Agent: Proxima |
| email | info@proxima.co.ke | Agent: Proxima |
| phone | +254 784 448 888 | Agent: CPK |
| phone | +254 105 772 200 | Agent: Ravi |
| email | sales@ravihomes.co.ke | Agent: Ravi |
| phone | +254 708 074 584 | Agent: Gerryville |
| email | info@gerryvillehomes.com | Agent: Gerryville |
| phone | +254 712 406 060 / +254 782 406 060 | Agent: GNA |
| phone | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| phone | +254 141 361 320 | Agent: NRE |
| email | info@nairobirealestate.co.ke | Agent: NRE |
| phone | +254 722 759 413 / +254 722 940 377 | Agent: Palmier |

---

## 6. Stakeholders

None named (architect / contractor / financier) on retained live sources this pass.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under lock |
|--:|-------|--------|------------------------|
| 1 | **Identity vs Luna Oak** | Shared “Oak” branding | **Distinct projects** — see §0. Never merge IDs. |
| 2 | **Price “from”** | Microsite Classic 1BR **9.9M** vs Oak Group **8.2M** vs agents **8.0–8.8M** | **Official vs official** (microsite vs Oak Group) → **`needs_developer_input`**. Keep all `price_claims[]`. |
| 3 | **Developer name** | Oak Developer / Van Tung email vs Oak Developers vs Premier Developers vs “The Oaks” | Legal SPV **`needs_verification`**. Brand = Oak Developer on microsite. |
| 4 | **Unit size rows** | Microsite set vs agent extras (70 / 135 / 142 / 194 ㎡) | Canonical sizes = microsite; extras **`needs_verification`**. |
| 5 | **Total units** | NRE **513** only | **`needs_verification`**. |
| 6 | **Deposit schedule detail** | 20% consensus vs 10–15% / 6 mo (few sources) | 20% must-have via ≥4; instalment cadence secondary. |
| 7 | **Amenity extras** | Oak Group pharmacy/yoga/spa vs microsite core | Core = microsite; extras **`needs_verification`**. |
| 8 | **NRE construction %** | **58%** widget | Single portal · **`needs_verification`**. |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~14** |
| `sources_retained` | **10** |

**Selection note:** Scanned brooksideoak.co.ke, Oak Group property + ongoing, Oak presentation PDF host, Proxima, CPK, Ravi, Masterways, Palmier, Gerryville, GNA, Craiova, NRE, Realtors.co.ke. **Always kept** project microsite. Retained 10 densest.

**Thin / skipped:**
- https://realtors.co.ke/property/brookside-oak-apartments-westlands/ — overlaps CPK/GNA price story
- https://oakgroup.co.ke/ongoing-developments-properties/ — used for identity corroboration (Luna vs Brookside cards); thinner than dedicated Brookside Oak page
- Official brochure PDF on microsite — present but not text-mined for claims this pass
- LinkedIn sales post — corroboration only for 20% / 10% cadence

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://brooksideoak.co.ke/ | Oak Developer / Brookside Oak | project_site | 2026-10-16 | Typed prices; 26 floors; parking; amenities; Van Tung email — **always keep** |
| 2 | https://oakgroup.co.ke/properties/brookside-oak/ | Oak Group Residences | developer_marketing | 2026-10-16 | From **8.2M**; feature chips; ≠ Luna Oak page |
| 3 | https://oakgroup.co.ke/wp-content/uploads/2017/12/BrooksideOak-Presentation.pdf | Oak Group Residences | brochure_pdf | 2026-10-16 | 26-floor / 3 towers / Feb 2026–Jun 2029 (indexed + hosted) |
| 4 | https://www.proxima.co.ke/brookside-oak/ | Proxima | agent | 2026-10-16 | Amenities overlap; discovery lead URL |
| 5 | https://commercialpropertykenya.com/properties/brookside-oak-apartments-westlands/ | CPK | agent | 2026-10-16 | Lower price table; June 2029; 40 mo |
| 6 | https://ravihomes.co.ke/developments/brookside-oak/ | Ravi Homes | agent | 2026-10-16 | **20%**; 40 mo; Feb 2026 start; 3 towers |
| 7 | https://gerryvillehomes.com/brookside-oak-residency/ | Gerryville Homes | agent | 2026-10-16 | Microsite-aligned prices; 40 mo |
| 8 | https://gna.co.ke/project/brookside-oak-residency-westlands-1-2-and-3-beds-plus-dsq/ | GNA | agent | 2026-10-16 | **20%**; Q2 2029 |
| 9 | https://craiovarealtors.com/property/brookside-oak-residency-in-westlands/ | Craiova | agent | 2026-10-16 | **20%** + 10–15%/6 mo |
| 10 | https://nairobirealestate.co.ke/properties/brookside-oak-residence | NRE | agent | 2026-10-16 | **20%**/40 mo; **513** units; 58% progress UI |

---

## 9. Field harvest

| Field | Brookside Oak status | Notes |
|-------|----------------------|-------|
| Identity ≠ Luna Oak | **Documented §0** | Geography + mix + scale + filing differ |
| canonical_name / geography | OK | Muguga Green / UN Blue Zone |
| primary_developer | Lead only | Van Tung email; brand Oak Developer |
| Oak Group | `marketing_partner` | Parallel to Luna Oak pattern |
| storeys / towers / parking | Strong | 26 / 3 towers / 6 parking levels |
| `price_claims[]` | All options; NDI on “from” | Microsite 9.9M vs Oak Group 8.2M |
| `payment_plan` | **20%** via ≥4 agents; 40 mo | Conf 3 — confirm LOO |
| amenities core | OK microsite | Reject uncorroborated Oak Group adds as canonical |
| completion | June / Q2 2029 | Aligns microsite 2026–2029 |
| `total_units` | Weak | NRE 513 only |

### Proposed schema bumps (for coordinator)

| Proposed extension | This project | Note |
|--------------------|--------------|------|
| Discovery leads without NBO id | Yes | Index under discovery until CSV assign |
| Sibling brand projects under same `marketing_partner` | Brookside Oak + Luna Oak | Explicit anti-merge rule |
| Multi-tower + amenity-floor schedule | Presentation | Capture when official PDF/site agree |
| Official “from” NDI across brand site vs project microsite | 8.2M vs 9.9M | Same NDI lock as Galaxy/Luna |

---

## Open questions (developer input)

1. Confirm legal entity: **Van Tung Company Ltd** vs Oak Developer vs other SPV; publish registry/NEMA.
2. Reconcile Oak Group **from 8.2M** with microsite Classic 1BR **from 9.9M**.
3. Binding LOO: **20%** deposit and instalment cadence (10–15% / 6 mo?).
4. Total unit count (NRE **513**?) and which agent size rows (70 / 135 / 142 / 194 ㎡) are live.
5. Exact Oak Group ↔ Van Tung / Oak Developer corporate relationship (affiliate vs sales only).
6. Brochure PDF payment schedule / gross vs plinth tags.
