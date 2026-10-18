---
slug: gaia-brookside
external_id: DISC-NBO-021
wave: hauzisha-b-2026-10-17
pilot: false
sources_evaluated: 12
sources_retained: 8
last_verified_at: 2026-10-17
inventory_class_intent: building
---

# Gaia Brookside (DISC-NBO-021) — discovery research

**Not in seed CSV.** Hauzisha Wave B ([hauzisha-wave-b-prep.md](../../internal/hauzisha-wave-b-prep.md); [hauzisha-developers-2026-10-16.md](../discovery/hauzisha-developers-2026-10-16.md)). **Brookside Gardens Drive**, Westlands, Nairobi — **Wonder Properties**, off-plan sales / under construction, completion claims **Dec 2027 vs June 2028 vs Dec 2028** (conflict). Also marketed as **Gaia Brookside Forest** / **Gaia Residencies**.

Live research accessed **2026-10-17**. **Block.ke ignored as authority** (low-trust lead only). **Hauzisha** = portal / discovery only (conf ≤2–3); phone **0730 731 355** is **Hauzisha only** — **never** Wonder.

**Method locks applied:**
- Developer vs agents: developer pages agreeing → **canonical**; agents secondary.
- **Official vs official** disagree → **`needs_developer_input`** (no assumed winner).
- Prices: always **`price_claims[]`** (no single scalar).
- Payment must-have if **any developer source** **or** ≥4 independent agents.
- Agent-only → show + **`needs_verification`**.
- No invented GroupCompany / legal SPV.
- Skip Ready inventory — this project is **`building` / UC** (not Ready/handed-over).

**≠ Brookside Oak (DISC-NBO-006)**; **≠ Diplomat Residencies**; **≠ Alina Valley / Harbour / Ridge** unless proven same parcel — see **§8**.

---

## 1. Property (claims + confidence)

| Field | Role | Value | Conf | Sources |
|-------|------|-------|-----:|---------|
| `canonical_name` | **CANONICAL** soft | **Gaia Brookside** | 5 / 4 | Wonder hub + `/projects/gaia`; Hauzisha; multi-agent |
| `aliases` | secondary | Gaia Brookside Forest; Gaia Residencies; Gaia Brookside Forest Apartments | 4 | A-Luxe; Ravi; NRE slug; Realtors; Sir Francis |
| `status` | claim set | **Off-plan sales / under construction** — Wonder hub tags **OFF-PLAN**; agents “Under Construction” / “Off-Plan / Ongoing”; Wonder YouTube progress / show-house tours; NRE progress UI **58%** (**`needs_verification`**, single portal). **Not** Ready / handed-over | 5 / 3 / 1 | Wonder; NRE; Oaklane; A-Luxe; Ravi |
| `inventory_class` intent | research queue | **`building`** (UC with residual off-plan instalment marketing; Wonder still labels OFF-PLAN on hub). **Not** `ready`. | — | Method lock + prep |
| `geography.city` | **CANONICAL** | Nairobi | 5 | Wonder; all |
| `geography.neighbourhood` | **CANONICAL** | **Westlands** — Brookside / Brookside Gardens enclave | 5 | Wonder; Hauzisha; multi-agent |
| `geography.street` | **CANONICAL** soft | **Brookside Gardens Drive** | 4 | NRE; Oaklane; A-Luxe; Ravi; Realtors; Sir Francis; Block discovery |
| `geography.landmarks` | secondary | Opposite / near Urban Dreams Apartment (NRE); Brookside Grove / riverside framing (A-Luxe); Sarit / Westgate / GTC catchment | 3 | NRE; A-Luxe |
| `geography.lat_lng` | unknown this pass | Wonder embeds Google Maps “Brookside Forest Apartment” — exact GPS not harvested | 0 | geo agent later |
| `primary_developer_id` | **CANONICAL** (trading) | → `dev-wonder-properties` (proposed) — **Wonder Properties** / Wonder Properties Kenya | 5 | Wonder site; Diplomat microsite names Gaia as Wonder portfolio; Hauzisha attribution; multi-agent |
| `unit_types` | **CANONICAL** soft | **3 Bedroom**; **3 Bedroom + DSQ**; **4 Bedroom**; **4 Bedroom + DSQ**; **5 Bedroom + DSQ**; penthouse claims (agent) | 4 / 3 | Wonder “3, 4 & 5 Bedroom”; Hauzisha 3/4/5BR; Oaklane/A-Luxe/NRE typed sheets |
| `size_by_type` | claim set — see table | Common band **~180–387 sqm**; densest typed sheets centre on **192 / 210 / 219 / 275 / 365 / 387** | 3 | Multi-agent; Hauzisha **192–387** |
| `total_units` | secondary — **`needs_verification`** | **217** units (A-Luxe; Realtors); Hauzisha “**3** units available” = stock snapshot only — **not** scheme total | 2 / 1 | Agents; portal |
| `building_specs.storeys` | secondary — **`needs_verification`** | **18** floors (A-Luxe; Block discovery echo) | 2 | Agents only this pass |
| `building_specs.blocks` | secondary — **`needs_verification`** | Realtors: Blocks **A–E** (A1/A2…E1/E2) with typed floor-plan cards | 2 | Realtors.co.ke |
| `price_claims[]` | multi | See **§1a** — marketing floors **from 23M** vs typed **from 25.3M**; upper band **~45–55M+** | — | — |
| `currency` | **CANONICAL** | **KES** | 5 | all |
| `payment_plan` | secondary — must-have **not locked** | See **§1b** — **20% deposit + quarterly balance** on **3** agents (short of ≥4); Wonder HTML silent → **`needs_verification`** | 3 | Oaklane; NRE; Block discovery |
| `completion_estimate` | claim set — **conflict** | **June 2028** cluster vs older **Dec 2027** vs **Q3 2027** widget vs **Dec 2028** outliers — **`needs_developer_input`** (no plaintext completion on Wonder HTML; brochure PDF image-heavy / not text-extracted this pass) | ≤3 | See §1c |
| `amenities` | **CANONICAL** soft (Wonder page chips) | Children’s play area; CCTV; high-speed lifts; sky lounge; smart home features; swimming pool; car parking; modern fitted gym; reception; coffee shop; health center; meeting room; yoga room; spa | 5 | Wonder `/projects/gaia` amenity labels in site bundle |
| `amenities` | secondary agent extras | Rooftop **helipad**; infinity pool / jacuzzi; cinema; padel / basketball; jogging track; pet zone; mini-supermarket; BBQ/koroga; tennis / snookball — **`needs_verification`** vs Wonder chip list | ≤3 | Oaklane; A-Luxe; Ravi; Realtors |
| `roi_claim` | secondary marketing | NRE **ROI 12.4%** widget — **`needs_verification`** | 1 | NRE only |
| `legal_title` | unknown | Some agents say “full title” at enquiry — not on Wonder HTML | 0 | — |
| `master_planned_community` | none | Standalone Brookside Gardens Drive scheme (not a named masterplan precinct) | — | — |

### Size table (retained claim set)

| Type / plan | Size | Role | Conf |
|-------------|-----:|------|-----:|
| 3BR (no DSQ) | **180 sqm** | Agent “from 23M” entry | 3 |
| 3BR + DSQ | **192 / 210 / 219 sqm** (some sheets **209**) | Densest typed consensus | 3 |
| 4BR (no DSQ) | **256 sqm** | A-Luxe; Sir Francis | 3 |
| 4BR + DSQ | **275 sqm** | Multi-agent | 3 |
| 5BR + DSQ | **365 / 387 sqm** | Multi-agent | 3 |
| Hauzisha band | **192–387 sqm** | Portal | ≤2 |
| Wonder brochure floor-plan images | present (webp assets) | Official imagery — sizes not OCR’d this pass | 4 (existence) / 0 (numbers) |

### 1a. `price_claims[]` — keep **all** (no canonical scalar)

Wonder HTML this pass does **not** publish a typed price list (brochure gated / image PDF). Keep agent+portal claim set.

| # | Claim | Context | Publisher | Conf | Flags |
|--:|-------|---------|-----------|-----:|-------|
| A | From **KES 25.3M**; band **25.3–45M** | Portal card | hauzisha.co.ke/developments/gaia-brookside | ≤2 | Aggregator |
| B | 3BR+DSQ **192 from 25.3M**; **219 from 28.9M**; 4BR+DSQ **275 from 36.3M**; 5BR+DSQ **365 from 45M** / **387 from 51M** | Typed sheet | Oaklane Properties | 3 | Strong typed mid-band |
| C | 3BR **180 from 23M**; 3BR+DSQ **192/210/219 from 25.3/27.6/28.9M**; 4BR **256 from 34M**; 4BR+DSQ **275 from 36.3M**; 5BR+DSQ **365/387 from 45/51M**; penthouse “exclusive” | Dense typed + June 2028 | A-Luxe Realty | 3 | Adds **23M** / **180 sqm** floor |
| D | Hero **from 23M**; body 3BR+DSQ **~25.3 / 27.6 / 28.9M**; 4BR+DSQ **~36.3M**; 5BR **~45M to 55M+** | Project narrative | Nairobi Real Estate (Gaia Residencies) | 3 | Hero vs body floor tension |
| E | 3BR **from 23M** (~180 sqm); 4BR **from 30M+**; 5BR **from 38M+** | Compressed marketing | Ravi Homes | 3 | Lower 4/5BR floors vs B/C |
| F | Typed **192/210/219 → 25.3/27.6/28.9M**; **275 → 36.3M**; **365/387 → 45/51M**; hero **from 23M** | Mixed hero vs table | Realtors.co.ke | 3 | Dec **2027** completion on same page |
| G | 3BR **180 from 23M**; 3BR+DSQ **209 from 28M**; 4BR **256 from 34M**; 4BR+DSQ **275 from 36M**; 5BR+DSQ **365 from 45M** | Typed table | Sir Francis Marketing | 3 | Dec **2028** completion |
| H | From **25.3M**; range to **~55.28M**; 3/4/5BR + DSQ | Aggregator / AI-leaning | block.ke | ≤2 | Discovery only — **not authority** |
| I | Wonder brochure PDF hosted | Official gated download | wonderpropertykenya.com/assets/documents/gaia_brochure.pdf | 5 (host) / 0 (prices this pass) | Image-heavy — **no novel price facts extracted** |

**Portal scalar:** none. Do not collapse to a single `price_from`.

### 1b. Payment plan — must-have **not locked**

No instalment schedule on Wonder HTML / extracted brochure text this pass.

| Element | Source | Status |
|---------|--------|--------|
| **20%** deposit; balance by **quarterly** instalments to completion | Oaklane; NRE | Secondary |
| **20%** deposit within **7 days** of reservation; balance quarterly to completion | Block.ke discovery | Thin / low-trust — does **not** strengthen lock |
| “Flexible” / “call for terms” / 20–30% soft | A-Luxe; Sir Francis; Realtors; Ravi | Thin |
| Official Wonder payment schedule | — | **Not published** in plaintext this pass |

**Must-have met?** **No** — need developer schedule **or** a **4th** independent non-Block agent echoing the same **20% + quarterly** shape.

### 1c. Completion — **conflict** (flag; no silent winner)

| Claim | Sources | Notes |
|-------|---------|-------|
| **June 2028** | Hauzisha; Oaklane; A-Luxe; NRE body; Block discovery | Current marketing cluster |
| **December 2027** | Ravi; Realtors; NRE notes “earlier material” | Older / still-live agent pages |
| **Q3 2027** | NRE header widget | Conflicts with NRE’s own June 2028 body |
| **December 2028** | Sir Francis; Pakfront (thin skip) | Outlier vs June 2028 cluster |

→ **`needs_developer_input`**: contractual / programme date from Wonder LOO or plaintext project page. Do **not** invent a canonical month.

---

## 2. Developer

| Field | Value |
|-------|-------|
| `id` | `dev-wonder-properties` (proposed lead → promote when registry/SPV confirmed) |
| `legal_name` | **Unknown** this pass (trading **Wonder Properties** / **Wonder Properties Kenya**; Companies Registry string not recovered) |
| `trading_names` | Wonder Properties; Wonder Properties Kenya |
| `website` | https://www.wonderpropertykenya.com/ |
| `project_page` | https://www.wonderpropertykenya.com/projects/gaia |
| `brochure` | https://www.wonderpropertykenya.com/assets/documents/gaia_brochure.pdf (gated download UX; file hosts) |
| `evidence` | Hub lists **Gaia Brookside (OFF-PLAN)** alongside Diplomat / Alina schemes; Gaia project narrative + amenity chips; Hauzisha Wonder developer page; multi-agent attribution |
| `group_company_id` | **null** — none invented |
| `sales_office` / contacts | See **§2a** |
| `confidence` | **5** trading face / **0** legal SPV |

### 2a. Wonder contacts (official site — **not** Hauzisha)

| Contact | Value | Provenance | Conf |
|---------|-------|------------|-----:|
| Phone (Gaia-labelled + shared Alina lines) | **+254 116 100 600** | Footer / tel: links on wonderpropertykenya.com (“GAIA BROOKSIDE”) | 5 |
| Email | **wonderproperties3@gmail.com** | Site footer + inquire mailto | 5 |
| Address | **Kirichwa Road, Off Argwings Kodhek, Kilimani, Nairobi** | Site contact copy in app bundle | 4 |
| Brochure inquiry recipient (secondary) | **laban@fameve.com** (+ partner@karimcgvisuals.com) | Gaia brochure dialog `mail_recipients` — treat as **ops/marketing recipient**, not invented GroupCompany | 2 |
| Social | facebook.com/wonderpropertiesofficial · youtube.com/@wonderpropertieskenya · instagram.com/wonderproperties · linkedin.com/company/wonderpropertieskenya | Site links | 4 |

**Never** assign **0730 731 355 / +254 730 731 355** to Wonder — Hauzisha portal only.

Indexed Diplomat microsite (502 this pass) previously showed Wonder **+254 116 126 666** / **info@wonderpropertykenya.com** / Kirichwa Rd — retain as **secondary Wonder contact leads** for verification, not Gaia-exclusive until live page recovers.

**Portfolio siblings on Wonder hub (do not merge):** Diplomat Residences (OFF-PLAN); Alina Valley (OFF-PLAN); Alina Harbour (Ongoing); Alina Ridge (Sold Out); Ndemi Gardens (Sold Out).

---

## 3. GroupCompany

**None invented.**

---

## 4. RelatedParty

| Party | Role | Evidence | Conf |
|-------|------|----------|-----:|
| Fameve / laban@fameve.com | marketing_partner / lead ops (brochure routing) | Gaia brochure dialog recipients | 2 — **`needs_verification`** |
| Karim CG Visuals | site/creative partner | “Powered by karimcgvisuals”; partner@ in mail_recipients | 2 |
| Oaklane / A-Luxe / NRE / Ravi / Realtors / Sir Francis | selling agents | Independent listing pages | 3 |
| Hauzisha | listing portal | Development + developer pages | ≤2 |

---

## 5. Agents (sample retained)

| Agent / portal | Role |
|----------------|------|
| Oaklane Properties | Typed **25.3–51M** sheet; **20%/quarterly**; **June 2028** |
| A-Luxe Realty | Densest typology + **217** units / **18** floors; **June 2028**; from **23M** |
| Nairobi Real Estate (Gaia Residencies) | Detailed narrative; body **June 2028** vs header **Q3 2027**; **20%/quarterly**; UC **58%** UI |
| Ravi Homes | **Dec 2027**; from **23M**; compressed 4/5BR floors |
| Realtors.co.ke | Typed mid-band; **Dec 2027**; block plans A–E; **217** units |
| Sir Francis Marketing | Typed from **23M**; **Dec 2028** |
| Hauzisha | Wonder attribution; **June 2028**; **25.3–45M** — portal only |

---

## 6. Sources

### Retained (≥5 rule)

| # | URL | Publisher | Type | Notes |
|--:|-----|-----------|------|-------|
| 1 | https://www.wonderpropertykenya.com/ | Wonder Properties | developer | Hub; **Gaia Brookside (OFF-PLAN)**; phone **+254 116 100 600**; email **wonderproperties3@gmail.com** |
| 2 | https://www.wonderpropertykenya.com/projects/gaia | Wonder Properties | developer | Gaia narrative; amenity chips; brochure/floor-plan CTAs; Brookside Forest framing |
| 3 | https://www.wonderpropertykenya.com/assets/documents/gaia_brochure.pdf | Wonder Properties | brochure | Hosted official PDF (image-heavy; prices/completion **not** text-extracted this pass) |
| 4 | https://hauzisha.co.ke/developments/gaia-brookside/ | Hauzisha | portal | Wonder; **June 2028**; **25.3–45M**; 192–387 sqm — conf ≤2; **ignore 0730 phone** |
| 5 | https://oaklaneproperties.co.ke/properties/gaia-brookside-westlands/ | Oaklane | agent | Typed prices; **20%/quarterly**; **June 2028** |
| 6 | https://a-luxerealty.ke/developments/gaia-brookside-forest-luxury-3-4-5-bedroom-apartments-in-westlands-nairobi-from-kes-23m-nairobi | A-Luxe Realty | agent | Dense typed sheet; **217** / **18** floors; **June 2028** |
| 7 | https://nairobirealestate.co.ke/properties/gaia-residencies | NRE | agent/portal | Body **June 2028** + notes older **Dec 2027**; header **Q3 2027** conflict; payment; UC % |
| 8 | https://ravihomes.co.ke/developments/gaia-brookside/ | Ravi Homes | agent | **Dec 2027**; from **23M**; Wonder portfolio narrative |

### Evaluated / thin skips

| URL / lead | Why skipped |
|------------|-------------|
| https://block.ke/property/gaia-brookside-westlands-3-4-5-bedroom-apartments/ | Low-trust / AI — discovery seed only (useful anti-merge FAQ echo, not authority) |
| https://realtors.co.ke/property/gaia-brookside-forest-luxury-apartments/ | Useful typed prices + Dec 2027 + blocks — overlap with retained mid-band; kept out of ≥8 retain to avoid portal bloat (facts folded into claim tables) |
| https://sirfrancismarketingltd.co.ke/properties/gaia-brookside-forest/ | Dec **2028** outlier + from 23M — cited in §1a/§1c; thin vs denser sheets |
| https://proxima.co.ke/gaia/ | Empty / non-informative fetch |
| https://splendorholdings.co.ke/properties/gaia-brookside-forest-apartments-for-sale-in-westlands/ | HTTP 500 this pass; search snippet had **Dec 2027** + discounted prices — do not retain without live page |
| https://www.pakfront.co.ke/projects/gaia-brookside-forest | Thin card; Dec 2028 |
| https://diplomat.wonderpropertykenya.com/ | **≠ this project**; 502 this pass — Wonder portfolio sibling only |
| https://hauzisha.co.ke/developers/wonder-properties/ | Developer stub; overlaps retained Gaia hub |
| Hauzisha “3 units for sale” cards | Unit-ad depth only; do not invent Ready |

**sources_evaluated ~12 · sources_retained 8**

---

## 7. Open questions

1. **`needs_developer_input`:** Official **completion** date — resolve **June 2028** vs **Dec 2027** vs **Q3 2027** vs **Dec 2028** against LOO / construction programme.  
2. **`needs_verification`:** Publish / OCR Wonder **price list** from brochure PDF (retire or keep agent **23M** vs **25.3M** floors).  
3. **`needs_verification`:** Payment — lock **20% + quarterly** with a **4th** independent agent **or** developer schedule (exclude Block).  
4. **`needs_verification`:** Total units **217** and height **18** floors — developer corroboration.  
5. Legal contracting entity / SPV (Companies Registry).  
6. Exact plot / GPS on Brookside Gardens Drive.  
7. NRE **58%** construction UI — corroborate with Wonder progress media.  
8. Clarify **laban@fameve.com** role (marketing partner vs internal).  
9. Confirm Hauzisha **3 units available** is listing stock only (not scheme total).  
10. Live recovery of Diplomat microsite Wonder contacts (**116 126 666** / info@) vs site **116 100 600**.

---

## 8. Anti-merge

| Dimension | **Gaia Brookside** (this dossier, DISC-NBO-021) | **Brookside Oak** (DISC-NBO-006) |
|-----------|--------------------------------------------------|----------------------------------|
| Developer | **Wonder Properties** | **Oak Developer** / Van Tung lead + Oak Group marketing |
| Street / pocket | **Brookside Gardens Drive** | **Muguga Green** (Safaricom HQ adjacency) |
| Product | Large **3 / 4 / 5 BR** (+ DSQ); from ~**23–25.3M** | **1 / 2 / 3 BR**; from ~**8.2–9.9M** |
| Scale claims | ~**217** units / **18** floors (agent) | **26** floors; **3** towers; ~**513** units (portal) |
| Completion framing | **2027–2028** conflict cluster | **2026–2029** / **June 2029** |
| Official site | wonderpropertykenya.com/projects/gaia | brooksideoak.co.ke |

- **≠ Brookside Oak (DISC-NBO-006)** — different developer, street, unit mix, price band — **do not merge** “Brookside” Westlands names.  
- **≠ Diplomat Residencies** (Wonder sibling — **Peponi Road**; **1 & 2 BR**; diplomat.wonderpropertykenya.com) — Wave B DISC-NBO-022, separate dossier.  
- **≠ Alina Valley / Alina Harbour / Alina Ridge / Ndemi Gardens** — Wonder portfolio siblings on hub; different schemes/locations.  
- **≠ Gemini / Capricorn / Luna Oak / COCO** and other Brookside / Westlands towers unless LOO proves same parcel.  
- **Gaia Brookside Forest** / **Gaia Residencies** = **aliases of this scheme**, not separate projects (multi-agent + Block FAQ).
)
