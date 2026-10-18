---
slug: kings-square-eldoret-ph2
external_id: ELD-001
geography: Eldoret / Uasin Gishu
wave: discovery
cycle: rest-of-kenya
pilot: false
sources_evaluated: 13
sources_retained: 10
last_verified_at: 2026-10-16
---

# Kings Square Apartments – Phase 2 (ELD-001) — Eldoret (new geography)

Discovery lead (unverified until this pass): Airport Road, **Eldoret**, Uasin Gishu; Kings Developers Ltd; developer badge **Under-Construction**. Seed pointers: [kenya-offplan-leads.md](/cursor/stores/self/docs/discovery/kenya-offplan-leads.md). **No Nairobi CSV row** — first Eldoret / rest-of-Kenya dossier ID **`ELD-001`**.

Live research accessed **2026-10-16**.

**Method locks applied:**
- Developer vs agents: if developer sources **agree** → **canonical = developer**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`**; no assumed winner.
- Prices: always **`price_claims[]`** (no single scalar) — here developer typed list is dense; still keep republisher rows.
- Payment must-have if **any developer source** with a concrete plan **or** ≥4 independent agent sources.
- Agent-only / uncorroborated → **show** + **`needs_verification`**.
- **Do not conflate** completed **Kings Square** (Eldoret, earlier phase) with **Phase 2**.

---

## 1. Property (claims + confidence)

Legend: **CANONICAL** = developer sources **agree** on this field for **Phase 2**. Phase 1 / other Kings Square URLs are related-project evidence only.

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** | Kings Square Apartments – Phase 2 | 5 | kingsdevelopers.com Phase 2 project + listings |
| `aliases` | secondary | Kings Square Phase 2; Kings Square Apartments Phase 2; Kings Square Ph2 | 4 | discovery lead; African Vibes |
| `status` | **CANONICAL** (developer badge) | **Under-Construction** | 5 | Airport Rd location + projects listing (“Under-Construction”) |
| `geography.city` | **CANONICAL** | Eldoret | 5 | Phase 2 project page |
| `geography.county` | **CANONICAL** | Uasin Gishu County | 5 | Phase 2 project page; Airport Rd location |
| `geography.neighbourhood_street` | **CANONICAL** | **Airport Road**, Eldoret | 5 | Phase 2 project; location hub |
| `geography.lat_lng` | **unknown** | — | 0 | Nominatim `Airport Road, Eldoret` → Eldoret Intl Airport — **REJECT**; leave unknown until plot/LR — [geo-enrichment.md](../db/geo-enrichment.md) |
| `primary_developer_id` | **CANONICAL** | → `dev-kings-developers` (**Kings Developers Ltd**) | 5 | Phase 2 page; aboutus; site chrome “Kings Developers Ltd” |
| `unit_types` | **CANONICAL** | **2 Bedroom**; **3 Bedroom** | 5 | Phase 2 project page (pages agree) |
| `size_by_type` | **CANONICAL** | 2BR **89 sqm**; 3BR **101 sqm** | 5 | Phase 2 project page (+ listing cards 89 & 101 sqm) |
| `size_measure_tag` | unknown | Gross vs plinth **not labelled** on HTML; brochure PDF linked but **image-only / no extractable text** this pass | 0 | brochure CTA |
| `unit_inventory_by_type` | claim set — **`needs_verification`** | 2BR: **70 units available**; 3BR: **140 units available** (developer copy). Unclear if = total stock or remaining unsold | 3 | Phase 2 page; African Vibes mirror |
| `total_units` | derived claim — **`needs_verification`** | If “available” = full schedule → **210** (70+140); **do not treat as proven total** | 2 | arithmetic only — not labelled “total units” |
| `price_claims[]` | claim set — keep all; developer typed list strong | See **§1a** | ≤5 | |
| `currency` | **CANONICAL** | KES / KSh | 5 | Phase 2 page |
| `payment_plan` | soft only — **must-have not met** | Corporate about: “**Flexible payment plans**”; site-wide payment calculator (user enters deposit %). **No Phase 2 deposit % / schedule** on project HTML | ≤2 | aboutus; investment-calculator — not a locked deposit |
| `completion_estimate` | unknown | **Not stated** on Phase 2 project / listing pages this pass | 0 | — |
| `amenities` (Phase 2 page) | thin on Phase 2 HTML | Phase 2 body lists **location distances** only; African Vibes chips: **Gated**, **Elevator**. **Do not import** Phase 1 gym/pool/township list as Phase 2 facts | 2 | Phase 2 page; African Vibes |
| `legal_title` | unknown | — | 0 | — |
| `construction_progress` | unknown | No % / floor tracker on Phase 2 pages | 0 | — |

### 1a. Price claims — keep **all** options

Developer Phase 2 pages **agree** on the typed bands below → strong claim set (conf 5 for those rows). Still no collapse to a single portal scalar until coverage rules say so.

| # | Claim band | Value | Publisher | Flag |
|--:|------------|-------|-----------|------|
| A | Developer Phase 2 typed list | 2BR 89 sqm **KSh 4,000,000**; 3BR 101 sqm **KSh 5,000,000** | kingsdevelopers.com/project/…phase-2_54 | Developer — pages agree with listing cards |
| B | Developer “from” | **From Kshs 4,000,000** | Phase 2 project; Airport Rd location; projects hub; homepage card | Developer — agrees with 2BR row |
| C | African Vibes republish | Same 4M / 5M + 70 / 140 units | africanvibes.com | Secondary mirror of A |
| D | Discovery lead note | UC; from 4M; Airport Rd | kenya-offplan-leads.md | Unverified lead → now corroborated by A/B |

**Canonical price scalar:** none for portal. **Developer-backed claim set** for research = A+B when citing typed prices.

### Payment plan — threshold recount

| Element | Agreeing independent sources | Count | Threshold | Status |
|---------|------------------------------|------:|-----------|--------|
| Concrete **deposit %** for Phase 2 | none on project HTML | 0 | — | unknown |
| Soft “flexible payment plans” (corporate) | aboutus | 1 developer (non-specific) | Soft only | Not must-have lock |
| Payment calculator (parametric) | investment-calculator | 1 | Tool, not a published schedule | Not a claim |
| ≥4 agents naming same deposit | none found this pass | 0 | Not met | — |

Brochure PDF (`square-catlouge-1.pdf`) linked from Phase 2 “Download Brochure” — **fetched; image-based, no extractable text** → contents **`needs_verification`** (may also be Phase 1 catalogue — filename “square-catlouge”).

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-kings-developers` |
| `legal_name` | **Kings Developers Ltd** (also styled **KDL**; site “Kings Developers Ltd, Kenya”) |
| `trading_names` | Kings Developers |
| `website` | https://kingsdevelopers.com/ |
| `established` | **2004** (aboutus); ProBuilders also notes **2006** admin/management framing — minor origin-date soft conflict, not material to Phase 2 |
| `evidence` | Phase 2 project branding; aboutus legal-style name; contact “Main Office - Kings Developers Ltd”; ProBuilders listing |
| `group_company_id` | → `grp-royal-group` (§3) |
| `office` | Main office Nairobi (contact); ProBuilders: **Royal Business Park**, next to Sheffield, **Old Mombasa Road**, Nairobi |
| `developer_confidence` | **5** |

---

## 3. GroupCompany

| Field | Value |
|-------|-------|
| `id` | `grp-royal-group` |
| `name` | **Royal Group of Companies** |
| `website` | unknown this pass |
| `evidence` | aboutus: “KDL is part of the Royal Group of Companies… roots tracing back to 1954”; ProBuilders corroborates “royal group of companies” |
| `confidence` | **4** |

---

## 4. RelatedParty / related projects

| Name | `relationship_type` | Evidence | Conf |
|------|---------------------|----------|-----:|
| **Kings Square** (Eldoret, non–Phase 2) | **prior_phase / completed related project** | Eldoret location hub: **Completed**, listed ~9 years ago; distinct card “Kings Square” 3BR / 123 sqm. Project pages `kings-square-_23` (live) and indexed `_48` (Completed, from 6.5M, 3/4/6 BR language — **404** on direct fetch this pass) | 4 |

**Do not merge** Phase 1 amenity / typology / price claims into Phase 2. Phase 1 FAQ on `_23` mentions 1/2/3 BR and township amenities — **out of scope** for Phase 2 canonical fields unless Phase 2 pages restate them.

---

## 5. Agents + Contacts

### Agents / portals

| Party | Type | Role | Evidence URL |
|-------|------|------|--------------|
| Kings Developers (direct sales) | developer sales | Primary Phase 2 marketing + contacts | Phase 2 project page |
| African Vibes | portal / republisher | Mirrors Phase 2 unit/price/location copy | https://africanvibes.com/real-estate/kings-square-apartments-phase-2/ |
| ProBuilders Kenya | directory | Developer identity / office address | https://probuilderskenya.com/listing/kings-developers/ |

No independent Nairobi-style multi-agent price war found this pass (thin Eldoret agent coverage).

### Contacts

| Channel | Value | Owner |
|---------|-------|-------|
| phone | +254 700 090 060 | Developer sales |
| email | sales@kingsdevelopers.com | Developer sales |
| email | info@kingsdevelopers.com / info@kingsdevelopers.co.ke | Developer (site chrome uses both domains) |
| url | https://kingsdevelopers.com/project/kings-square-apartments-–-phase-2_54 | Property (Phase 2) |
| url | https://kingsdevelopers.com/ | Developer |
| address | Main Office — Kings Developers Ltd (Nairobi; hours Mon–Fri 8:00–18:00 on contact) | Developer |
| address | Royal Business Park, next to Sheffield, Old Mombasa Road, Nairobi | Developer (ProBuilders) |

---

## 6. Stakeholders

| Name | Kind | Evidence | Conf |
|------|------|----------|-----:|
| — | — | No named contractor / architect / financing partner on Phase 2 pages this pass | 0 |

Corporate due-diligence blog claims NEMA/NCA process generally — **not** a Phase 2 licence citation.

---

## 7. Conflicts (explicit)

| # | Field | Claims | Resolution under locks |
|--:|-------|--------|------------------------|
| 1 | **Phase identity** | Phase 2 (UC, Airport Rd, 2/3BR 89/101, from 4M) vs completed **Kings Square** (123 sqm / older cards / 3–6BR language on archived page) | Keep separate entities. Canonical dossier = **Phase 2 only**. |
| 2 | **Unit counts 70 / 140** | Stated as “units **available**” | Show; **`needs_verification`** whether total or remaining. Do not invent `total_units=210` as canonical. |
| 3 | **Amenities** | Phase 1 `_23` lists gym, pool, township, etc.; Phase 2 HTML does not | Phase 2 amenities = only what Phase 2 sources state (thin). |
| 4 | **Payment** | Flexible corporate language vs no Phase 2 % | Must-have **not** met. |
| 5 | **Completion** | Absent on Phase 2 surfaces | unknown |
| 6 | **Brochure** | PDF linked; image-only extract | **`needs_verification`**; may be wrong-phase catalogue |
| 7 | **Email domain** | .com vs .co.ke in site chrome | Both shown; non-blocking |

---

## 8. Sources (retained **10**)

| Meta | Count |
|------|------:|
| `sources_evaluated` | **~13** |
| `sources_retained` | **10** |

**Selection note:** Scanned Phase 2 project page, Airport Rd + Eldoret location hubs, projects listing, homepage card, aboutus, contact, investment calculator, due-diligence blog, African Vibes, ProBuilders, Phase 1 `_23`, brochure PDF, discovery lead. **Always kept** developer Phase 2 project page (+ brochure URL even if OCR-empty). Retained 10 densest / identity-critical sources.

**Thin / skipped:**
- https://kingsdevelopers.com/investment-calculator — parametric tool; no Phase 2 schedule
- https://kingsdevelopers.com/blog-page/our-commitment-to-rigorous-due-diligence-for-your-security_56/ — generic NEMA/NCA process; not Phase 2 filing
- https://kingsdevelopers.com/project/kings-square-_48/ — **404** this pass (indexed Completed Phase 1 copy only)
- Discovery markdown row — lead only (now superseded by live dossier)

| # | url | publisher | type | accessed_at | notes |
|--:|-----|-----------|------|-------------|-------|
| 1 | https://kingsdevelopers.com/project/kings-square-apartments-–-phase-2_54 | Kings Developers Ltd | developer / project_site | 2026-10-16 | Typed prices; 89/101; 70/140 available; Airport Rd — **always keep** |
| 2 | https://kingsdevelopers.com/location/airport-road-eldoret-uasin-gishu-county | Kings Developers Ltd | developer | 2026-10-16 | **Under-Construction** badge; from 4M |
| 3 | https://kingsdevelopers.com/projects/ | Kings Developers Ltd | developer | 2026-10-16 | Portfolio card; Phase 2 vs other Kings Square |
| 4 | https://kingsdevelopers.com/aboutus | Kings Developers Ltd | developer | 2026-10-16 | KDL legal name; Royal Group; flexible plans (soft) |
| 5 | https://kingsdevelopers.com/contact | Kings Developers Ltd | developer | 2026-10-16 | Phones/emails; main office |
| 6 | https://kingsdevelopers.com/brochures/square-catlouge-1.pdf | Kings Developers Ltd | developer_pdf | 2026-10-16 | Linked from Phase 2 brochure CTA; **image PDF**, text not extracted |
| 7 | https://africanvibes.com/real-estate/kings-square-apartments-phase-2/ | African Vibes | portal | 2026-10-16 | Mirrors unit/price/location; gated/elevator chips |
| 8 | https://probuilderskenya.com/listing/kings-developers/ | ProBuilders Kenya | directory | 2026-10-16 | KDL + Royal Group; Royal Business Park address |
| 9 | https://kingsdevelopers.com/location/eldoret | Kings Developers Ltd | developer | 2026-10-16 | **Completed** Kings Square contrast (identity separation) |
| 10 | https://kingsdevelopers.com/project/kings-square-_23/ | Kings Developers Ltd | developer (related) | 2026-10-16 | Non–Phase 2 Kings Square marketing; do not merge specs |

---

## 9. Field harvest (new geography)

| Field | Eldoret Ph2 status | Notes for living schema |
|-------|--------------------|-------------------------|
| Geography outside Nairobi | **First Eldoret dossier** | Extend corpus geo: city + county required |
| `external_id` prefix | **`ELD-001`** | Parallel to NBO-* for rest-of-Kenya |
| Developer microsite | Strong | Price + size + UC badge on official pages |
| GroupCompany | Royal Group evidenced | Capture when about page states parent |
| Prior phase separation | Critical | Same brand, different product |
| `unit_inventory` “available” language | Ambiguous | Propose claim type distinct from `total_units` |
| Payment / completion | Missing on project HTML | Verification queue |
| Amenities | Thin on Phase 2 | Do not borrow Phase 1 |
| Brochure OCR | Failed | Document-intel candidate |

### Proposed consensus bumps

| Proposed | This project | Note |
|----------|--------------|------|
| Rest-of-Kenya `external_id` series (`ELD-*`, later `NKR-*`, …) | ELD-001 | Coordinator confirm |
| `units_available_by_type` vs `total_units` | 70 / 140 wording | Avoid silent sum |
| Parent **GroupCompany** when developer about names conglomerate | Royal Group | Conf 4 here |
| Image-only brochure → `needs_verification` + document-intel | square-catlouge PDF | Same class as SPA hydration gaps |

---

## Open questions (verification / developer input)

1. Are **70 / 140** total units of each type or remaining inventory? What is **total_units**?
2. Binding **payment plan** / deposit % for Phase 2 (LOO or brochure text)?
3. **Completion / handover** target date?
4. Confirm brochure PDF is Phase 2 (not Phase 1 catalogue); provide text schedule / floor plans / gross vs plinth.
5. Phase 2 **amenities** schedule (does it share Phase 1 township facilities)?
6. NEMA / NCA / county approvals specific to Phase 2 Airport Road plot?
7. GPS / LR number for the Phase 2 site?
