---
slug: astra-bay-residence
external_id: NBO-005
cycle: 1
pilot: true
retrofit: cycle-2-locks-2026-10-16
sources_evaluated: 11
sources_retained: 9
last_verified_at: 2026-10-16
---

# Astra Bay Residence (NBO-005) — Cycle 1 pilot (C2 retrofit)

CSV seed (unverified leads): location Lower Kabete Road, Lower Kabete, Nairobi; lat/lng −1.23310, 36.71314; stage `under_construction`; completion Q2 2027; `price_from_kes` 1,870,000; sales_contact Block/Loyd Mokaya; developer “Wimax Homes”.

**Retrofit locks applied:** C1 (Laureland = `marketing_partner` **unchanged**; canonical = developer when developer sources **agree**; `needs_verification` on low-confidence/agent-only; payment ≥4; gross/plinth; source counts ~11/9) + **C2** (always multi `price_claims[]`; official-vs-official → **`needs_developer_input`**, no invented winner).

---

## 1. Property (claims + confidence)

Conflict rules: (1) developer sources **agree** → canonical = developer; agents secondary. (2) **Official vs official** disagree → **no canonical**; flag **`needs_developer_input`**. (3) Low-confidence / agent-only → **show** + **`needs_verification`**.

| Field | Canonical | Alternate / conflicts | Conf | Flags / notes |
|-------|-----------|----------------------|-----:|---------------|
| `canonical_name` | Astra Bay Residence | — | 5 | Official page “astra bay”; agents |
| `aliases` | Astra Bay; Astra Bay Lower Kabete | — | 5 | Official; agents |
| `status` | *(no developer status label on HTML)* | **Conflict** — CSV `under_construction`; Block `off-plan`; Craiova UC + “Showhouses ready” | 3 | Claim set; Craiova “showhouses ready” → **`needs_verification`** (single agent) |
| `geography.neighbourhood` | Lower Kabete — Lower Kabete Road | — | 5 | Official site + flyer **agree** |
| `geography.city` / county | Lower Kabete (Nairobi metro framing on official copy) | **Conflict** — Block: Kiambu County (Nairobi NW edge); CSV/A-list: Nairobi | 4 neighbourhood / 2 county | County → **`needs_verification`** |
| `geography.lat_lng` | CSV — **needs_verification** (recommended pending) | **−1.23310, 36.71314** (`geo_method=csv`) | 2 | CSV seed; not developer-sourced |
| `geography.lat_lng` | geocode check — **needs_verification** | −1.240500, 36.750169 | 2 | Nominatim Lower Kabete Road 2026-10-16 — **~4 km E of CSV**; no winner — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | → Developer: Wimax Homes Limited | — | 5 | Official |
| `unit_types` **canonical** | Superior Studio; Studio; 1 Bedroom Layout 1; 1 Bedroom Layout 2 | — | 5 | Project page + flyer **agree** (no official-vs-official) |
| `unit_types` **non-canonical** | — | **2BR** (Block, Vorsa, Craiova); 1BR loft / courtyard / super loft (agents) | ≤3 | **Shown** · **`needs_verification`** — not on developer site |
| `sizes` **canonical** | See size table (developer flyer gross + plinth; HTML sizes match) | Agents often quote plinth-only or different bands | 5 | Developer HTML + flyer **agree** |
| `price_claims[]` | **none** (no developer price on HTML/flyer) | See **§1a price_claims table** — always multiple options; no single scalar | ≤3 | C2 lock: keep all rows |
| `currency` | KES | — | 5 | |
| `payment_plan` | **20% deposit + balance over construction to completion** (≥4 sources) | Booking ~KES 100k = **Block only** | 4 / 2 | Booking fee → **`needs_verification`** (single source) |
| `completion_estimate` | *(no developer date on HTML/flyer)* | June / Q2 2027 (CSV, Block, Vorsa, Craiova) vs **Q3 2027** (A-list) | 3 | A-list Q3 outlier → **`needs_verification`**; majority Q2 secondary claim set |
| `amenities` **canonical** | Gym; 24hr CCTV; high-speed lifts (HTML). Flyer adds (same developer CDN): backup generator; borehole; access control; convenience store; outdoor refresh area; indoor gaming; green area; social corridor; tracking range; internet/cable | Agent adds: 1,800 sqm retail + Carrefour/Naivas (Craiova); rooftop solar (Craiova); pool (skipped Foresee) | 5 / 1–2 | Flyer extends HTML (additive, not contradicting). Inflated agent adds → **`needs_verification`** |
| `building_specs` | unknown on developer | 12-storey (Block only) | 0 / 3 | **`needs_verification`** (single portal) |
| `legal_title` | unknown | Block: “Confirmed at enquiry” | 0 | unknown |
| `construction_progress` | unknown | — | 0 | No developer tracker this pass (C2 field when published) |

**Official vs official (C2):** No developer-vs-developer disagreement on typology, sizes, or amenities this pass (project page + flyer align). **`needs_developer_input`** not applied to those fields. Armed if future official pages diverge.

### Size table (gross vs plinth tagged)

| Unit | Gross sqm | Plinth sqm | Source | Role |
|------|----------:|-----------:|--------|------|
| Superior Studio | **31.5** | **25.5** | Flyer PDF on wimaxhome.com | Canonical |
| Studio | **26.1** | **21** | Flyer + HTML | Canonical |
| 1 Bedroom Layout 1 | **53.2** | **42.74** | Flyer + HTML | Canonical |
| 1 Bedroom Layout 2 | **53.2** | **42.74** | Flyer + HTML | Canonical |
| Agent **2BR** | ~78.3 (Block) | ~63 (Craiova) | Agents only | Non-canonical · **`needs_verification`** |
| Agent 1BR loft / courtyard sizes | varies by agent table | — | Agents only | Non-canonical · **`needs_verification`** |

Do not mix gross and plinth in a single size field.

### 1a. `price_claims[]` (always multi — C2 lock)

**No canonical price** — developer HTML/flyer publish **no** KES figures. Portal/public “from” later only if high confidence **and** high coverage.

| # | Claim (KES) | Unit / band | Source | Conf | Flags |
|--:|-------------|-------------|--------|-----:|-------|
| 1 | from **1,870,000** | Standard studio (seed / portals) | CSV NBO-005; Block; Vorsa; A-list | 3 | Agent/seed cluster |
| 2 | **1.87M – 2.42M** | Standard studio ~21–26 sqm | Block | 3 | |
| 3 | **2.25M – 2.92M** | Superior studio ~25–31.5 sqm | Block | 3 | |
| 4 | ~**2.96M** | 1BR loft | Block | 2 | **`needs_verification`** — loft not on developer |
| 5 | ~**4.07M – 4.86M** | 1BR standard ~42.7–50.3 sqm | Block | 3 | Agent size band vs official gross 53.2 / plinth 42.74 |
| 6 | **6.37M – 7.14M** | 2BR ~78.3 sqm | Block | ≤3 | **`needs_verification`** — 2BR not on developer |
| 7 | Studio **1.87M – 2.35M**; superior **2.27M – 2.84M**; 1BR **4.11M – 4.72M**; 2BR **6.3M – 7.14M** | Mixed bands | Vorsa | ≤3 | 2BR rows → **`needs_verification`** |
| 8 | Studio **1.96M – 2.42M**; superior **2.33M – 2.92M**; loft/super-loft bands; 1BR ~4.61–4.7M; 2BR **6.37M – 6.77M** (63 sqm) | Mixed | Craiova | ≤3 | Studio from 1.96M conflicts with 1.87M cluster; 2BR → **`needs_verification`** |
| 9 | from **1,870,000**; studio/superior/1BR bands (no 2BR on page) | Studio / 1BR | A-list | 3 | Completion on same page is Q3 outlier |

Do not collapse to a single `price_from`. Cash vs instalment dual columns: **not published** on retained sources this pass.

### Payment plan — ≥4-source recount

| Element | Agreeing independent sources | Count | Threshold (≥4 or developer)? | Status |
|---------|------------------------------|------:|------------------------------|--------|
| 20% deposit | Block; VorsaGroup; Craiova; A-list | **4** | Met | **Must-have / included** |
| Balance over construction / to completion | Same set | **4** | Met | **Must-have / included** |
| Booking ~KES 100,000 | Block only | **1** | Not met | Alternate · **`needs_verification`** |
| Developer published schedule | None on HTML/flyer this pass | 0 | — | unknown |

Canonical payment summary: **20% deposit; balance during construction to completion.** Booking fee not elevated to canonical.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-wimax-homes` |
| `legal_name` | Wimax Homes Limited (also styled “Wimax Homes LTD”) |
| `trading_names` | Wimax Homes; Wimax Home (footer) |
| `website` | https://wimaxhome.com/ |
| `group_company_id` | **null** — no proven parent |
| `evidence` | https://wimaxhome.com/astra-bay/; https://wimaxhome.com/buy-a-house-in-kenya/ (“Astra Bay by Wimax Homes Limited”); homepage; agents attribute Wimax |
| `sales_office_address` | Westlands, Mvuli Road, Nairobi |
| `prior_projects_mentioned` | Himalaya Horizon, Dolce Vita (ongoing); Himalaya Heights, Laurel Hill Suites, Silver Harbour/“Silver Habour” (completed) — **delivery unverified this pass** |

**Primary developer = Wimax Homes Limited (confidence 5).** Not Laureland.

---

## 3. GroupCompany

**None.** No evidenced parent entity. Do not invent a group from brand overlap.

---

## 4. RelatedParty

| Field | Value |
|-------|-------|
| `id` | `rp-laureland-homes` |
| `name` | Laureland Homes / Laure Landhomes |
| `relationship_type` | **`marketing_partner`** — **unchanged** under C2 locks (not GroupCompany; not co_developer) |
| `website` | https://laurelandhomes.com/ |
| `linked_to` | Property Astra Bay (via flyer on developer CDN); Developer Wimax (brand overlap) |
| `evidence` | (1) Astra Bay flyer on wimaxhome.com footers LAURE LANDHOMES.COM + 0703 600 000 / 0733 600 000; (2) LinkedIn “Laureland/Wimax Homes Limited”; (3) Laureland projects overlap Wimax names — **Astra Bay not listed** on Laureland projects page |
| `confidence` | 3 for marketing_partner typing (method lock) / 2 for any stronger relationship |
| `not` | Not GroupCompany; not sole developer; not co-developer without further proof |

---

## 5. Agents + Contacts

### Agents linked to property

| Agent | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Block Real Estate | agency / portal | Listing + CSV sales_contact | https://block.ke/property/astra-bay-residence-modern-living-in-lower-kabete/ |
| VorsaGroup Real Estate | agency | Listing + price table | https://vorsagroup.co.ke/property/astra-bay-residence-studios-1-2-bedroom-apartments-in-lower-kabete/ |
| Craiova Realtors | agency | Listing; UC + showhouses | https://craiovarealtors.com/property/astra-bay-residence-in-lower-kabete/ |
| A-list Real Estate | agency | Listing; Q3 2027 outlier | https://a-listrealestate.ke/property/astra-bay-residence/ |

Vision Homes + Foresee evaluated but **not retained** (see Sources § skipped). Contacts below kept for discovery only.

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 117 000 888 | Developer sales (wimaxhome.com) |
| phone | +254 117 222 888 | Developer sales |
| email | wimaxsales24@gmail.com | Developer sales |
| office | Westlands, Mvuli Road, Nairobi | Developer sales office |
| phone | +254 703 600 000 | RelatedParty: Laureland (`marketing_partner`) |
| phone | +254 733 600 000 | RelatedParty: Laureland |
| email | laurelandhomes@gmail.com | RelatedParty: Laureland |
| phone | +254 725 937 686 | Agent: Block / Loyd Mokaya (CSV) |
| email | loyd@block.ke | Agent: Block |
| phone | +254 717 945 199 / +254 755 745 140 | Agent: VorsaGroup |
| email | info@vorsagroup.co.ke | Agent: VorsaGroup |
| phone / WhatsApp | +254 720 004 631 / +254 776 007 048 | Agent: Craiova |
| email | info@craiovarealtors.com | Agent: Craiova |
| phone | +254 769 117 788 / +254 711 942 900 | Agent: A-list |
| email | info@a-listrealestate.ke | Agent: A-list |
| phone | +254 743 555 777 / +254 743 101 010 | Agent: Foresee |
| email | info@foreseerealtors.com | Agent: Foresee |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf | Flag |
|------|------|----------|-----:|------|
| “Tier-1 contractors” (unnamed) | contractor | wimaxhome.com/buy-a-house-in-kenya/ — not identifiable | 1 | **`needs_verification`** |
| Anchor retail “Carrefour or Naivas” | other | Craiova only — not on developer | 1 | **`needs_verification`** |

No financing / named architect / land vendor found.

---

## 7. Sources (retained 9)

`sources_evaluated`: **~11** (quick scan) · `sources_retained`: **9** (≥5 richest; developer/official always kept)

### Retained

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://wimaxhome.com/astra-bay/ | Wimax Homes | developer | 2026-10-15 | Canonical unit types + HTML amenities |
| 2 | https://wimaxhome.com/wp-content/uploads/2025/02/Astra-Bay-Flyer5.pdf | Wimax Homes (CDN) | developer | 2026-10-15 | Gross/plinth sizes; amenities; Laureland footer |
| 3 | https://wimaxhome.com/buy-a-house-in-kenya/ | Wimax Homes Limited | developer | 2026-10-15 | Legal name; Lower Kabete Rd |
| 4 | https://wimaxhome.com/ | Wimax Homes Limited | developer | 2026-10-15 | Portfolio; contacts |
| 5 | https://block.ke/property/astra-bay-residence-modern-living-in-lower-kabete/ | Block | portal | 2026-10-15 | Prices; 20%; Jun 2027; 2BR claim; amenity disclaimer |
| 6 | https://vorsagroup.co.ke/property/astra-bay-residence-studios-1-2-bedroom-apartments-in-lower-kabete/ | VorsaGroup | agent | 2026-10-15 | Price bands; 20%; Jun 2027 |
| 7 | https://craiovarealtors.com/property/astra-bay-residence-in-lower-kabete/ | Craiova | agent | 2026-10-15 | UC; 20%; price table; retail claim |
| 8 | https://laurelandhomes.com/ (incl. /projects/) | Laureland Homes | related_party | 2026-10-15 | marketing_partner evidence; Astra Bay absent |
| 9 | https://a-listrealestate.ke/property/astra-bay-residence/ | A-list | agent | 2026-10-15 | 20%; **Q3 2027** conflict |

### Evaluated but not retained (thin / failed)

| url | Why skipped |
|-----|-------------|
| https://visionhomeskenya.com/property/astra-bay-lower-kabete-modern-studios-1-2-bedroom-apartments-flexible-payment-plan/ | HTTP **500** on fetch — search snippet only; not usable as full source |
| https://foreseerealtors.com/portfolio/astra-bay-lower-kabete/ | Thin portfolio card; price/size outliers + pool claim already covered by richer retained conflicts |
| CSV NBO-005 seed row | Lead only — not a publishable research URL |

---

## 8. Issues / conflicts (highlighted)

1. **Laureland branding:** Flyer on Wimax CDN carries Laureland contacts — **`marketing_partner` unchanged** (C2); not parent/developer.
2. **Unit mix:** **Canonical = studio + 1BR** (Wimax page + flyer agree). Agent **2BR / loft / courtyard / super loft** shown + **`needs_verification`**.
3. **Size measure:** Agents conflate plinth vs gross — use tagged developer table; agent 2BR sizes **`needs_verification`**.
4. **Prices (C2):** No developer KES → **no canonical**. Keep full **`price_claims[]`** (§1a); never single `price_from`. 2BR-linked rows inherit **`needs_verification`**.
5. **Official vs official (C2):** None found on typology/sizes this pass (page + flyer agree). Rule ready: future developer conflicts → **`needs_developer_input`**, no invented winner.
6. **completion:** Q2/June 2027 (multi-agent) vs A-list Q3 (**`needs_verification`**) — no developer date.
7. **status:** off-plan vs under_construction vs showhouses (**`needs_verification`** on showhouses).
8. **County:** Nairobi vs Kiambu edge — **`needs_verification`**.
9. **Amenity inflation:** retail / solar / pool — shown + **`needs_verification`**; core = developer HTML+flyer.
10. CSV `sales_contact` = Block ≠ Wimax sales; Vision 500 not retained.

---

## 9. Field harvest (C1 + C2 alignment)

`price_claims[]` expanded to multi-row table (C2 #9). Official-vs-official → **`needs_developer_input`** armed; **no rows need it yet** (developer materials agree). Laureland remains **`marketing_partner`**. Agent-only / low-confidence claims stay **shown** + **`needs_verification`**. Sources: `evaluated` ~11 / `retained` 9.
