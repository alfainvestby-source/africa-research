---
cursor:
  subagentId: "bc-d4d72e5b-8afe-5a42-89b8-83622188317c"
---

# Hauzisha Wave B seed extraction (DISC-NBO-019…023)

**Source:** dossiers only · **2026-10-17** · Gemini Hub **skipped** · never `0730 731 355`

## Developer ID reuse map

| Proposed id | Status | Notes |
|-------------|--------|-------|
| `dev-glbc-group` | **NEW** (promote from `dev-lead-glbc-group`) | Not in `developers.csv`. Libra primary. Only You = marketing_partner only. |
| `dev-wonder-properties` | **NEW** (promote from `dev-lead-wonder-properties`) | Not in `developers.csv`. Shared Gaia + Diplomat. |
| `dev-whitehorse-real-estate` | **NEW** | Not in `developers.csv`. AYA trading primary. |
| `dev-aad-real-estate` / `dev-lead-aad-real-estate` | **alias / prior face** — do not make AYA primary | Lead exists; rebrand → Whitehorse. Prefer Whitehorse id + RelatedParty prior_trading_name. |
| Onlyou Investments Ltd | **NEW RelatedParty only** (not primary_developer) | EIA SPV; no Developer row unless LOO confirms trading. |
| Sandoral Developers | **RelatedParty NDI only** | Never primary. |
| Glamorous | **not in corpus** for this wave | No match in seed developers. |

---

## 1. Libra Residences — DISC-NBO-019

| Field | Value | Conf |
|-------|-------|-----:|
| slug | `libra-residences` | — |
| external_id | `DISC-NBO-019` | — |
| canonical_name | Libra Residences | 5 |
| status_label | Under construction · handover 2027 | 5 (agents Dec/Q4/Nov 2027 = 3) |
| inventory_class | `building` | 5 |

### primary_developer
- **id:** `dev-glbc-group` (**NEW** ← promote `dev-lead-glbc-group`)
- **legal_name:** Unknown (trading **GLBC Group**)
- **website:** https://www.glbcgroup.co.ke/
- **phones:** +254 798 556 666 (project); +254 705 81 81 81; +254 712 78 77 44
- **emails:** info@glbcgroup.com; info@glbcgroup.co.ke
- **confidence:** 5 trading / 0 legal SPV

### related_parties
| role | name | notes | conf |
|------|------|-------|-----:|
| legal_partner | NMN Law Associates LLP | portfolio-level; info@nmnlaw.co.ke | 4 |
| marketing_partner | Leos Realty Group | unproven related trading face | 2 NV |
| neighbour_landmark | Roseville Residences | address “next to” — ≠ this project | 5 as label |

### geo
- city: Nairobi (5) · neighbourhood: Kilimani (5)
- streets: **George Padmore Road** (off Ngong Road) (5)
- lat/lng: none (0)

### unit_types (developer Plans conf 5)
| beds | baths | size_sqm | label | notes |
|-----:|------:|---------:|-------|-------|
| 3 | — | 193 | 3B + SQ | |
| 4 | — | 250 | 4B + DSQ | |
| 4 | — | 258 / 264 / 265 | 4B + SQ | three plan variants |
| 5 | — | 285 | 5B + SQ | Overview band 284 soft conflict (4) |

### prices (multi-claim; no scalar)
| amount | ccy | unit link | tier | notes |
|--------|-----|-----------|------|-------|
| 17–25M band | KES | all | developer (5) | Official Overview — prefer until LOO |
| typed ~17.76–25.76M | KES | 3/4/5BR | agent (3) | CPK aligns to floor |
| typed ~19–31M | KES | 3/4/5BR | agent (3) | NRE/Bellano/Geomara/BRK — above band → NV |

### payment_plans
- Must-have: **NOT met** (developer silent; agents “flexible” only; NRE 20% calculator illustrative)
- deposit % / schedule: unknown

### features (GLBC Amenities conf 5)
24-hour CCTV; children’s play area; high-speed elevator; solar lighting; landscape garden; swimming pool; intercom; community shop; modern gym; modern club house  
*(agent extras borehole/generator/heated pool etc. = 2–3 NV)*

### agents
CPK Real Estate; NRE Real Estate; Realtors.co.ke; Bellano Group; Geomara Homes; Masterways; BuyRentKenya (Sir Francis Homes); Flamingo Real Estate; Hauzisha (portal)

### contacts (developer only)
+254 798 556 666; +254 705 81 81 81; +254 712 78 77 44; info@glbcgroup.com; info@glbcgroup.co.ke

### construction / completion
- Handover **2027** (developer 5); agents Dec / Q4 / Nov 2027 (3)
- Progress: NRE 58% / Bellano “first floor” = 2 NV
- Specs: 20 storeys (5); 119 units (5) vs agents 120 (3); agent 2 blocks / 0.8 acres = NV

### research / NDI
Payment schedule; legal SPV; 119 vs 120; 284 vs 285; Leos Realty role; GPS; typed prices vs 17–25M band

---

## 2. Only You / Onlyou — DISC-NBO-020

| Field | Value | Conf |
|-------|-------|-----:|
| slug | `only-you` | — |
| external_id | `DISC-NBO-020` | — |
| canonical_name | Onlyou Elgeyo (aliases: Only You, Onlyou) | 5 soft |
| status_label | Under construction / off-plan residual | 4 |
| inventory_class | `building` | intent lock |

### primary_developer
- **id:** **null** — `needs_developer_input`
- **legal_name / trading:** unresolved (do **not** set GLBC)
- **website (brand):** https://onlyounairobi.com/ (brand face only)
- **confidence on primary assignment:** **0**

### related_parties
| role | name | notes | conf |
|------|------|-------|-----:|
| legal_spv / land_owner | **Onlyou Investments Limited** | EIA proponent + land owner Block 17/287; P.O. Box 26604–00100 | 5 |
| marketing_partner | **GLBC Group** | Hauzisha attribution + shared +254 705 818 181; **absent** from glbcgroup.co.ke/projects | 2 NDI |

### geo
- city: Nairobi (5) · neighbourhood: Kilimani (5)
- streets: **Elgeyo Marakwet Road** / **Elgeyo Road** (5); plot **Nairobi/Block 17/287** (5)
- lat/lng: **−1.29444444, 36.77886111** (EIA §3.2) — conf **4** (official EIA, not developer marketing GPS)

### unit_types
| beds | size_sqm (agent) | label | notes | conf |
|-----:|-----------------:|-------|-------|-----:|
| 3 | ~205–217 | 3BR+DSQ / PLUS | EIA count 38 | 5 mix / 3 size |
| 4 | ~276–302 | 4BR+DSQ / PLUS | EIA 57 | 5 / 3 |
| 5 | ~358–360 | 5BR+DSQ | EIA 19 | 5 / 3 |
| 4/5/6 | up to ~521 | penthouses | EIA 1+3+2 | 5 / 3 |
| — | — | total **120** | EIA | 5 |

### prices (official silent)
| amount | ccy | tier | notes |
|--------|-----|------|-------|
| — | — | developer | microsite silent |
| ~28–33M floors; dense block cards to ~120M duplex | KES | agent (3) | CPK/Vorsa/Azipa/GNA/Erysler/Almasi |
| 30.6–92.4M | KES | portal ≤2 | Hauzisha |

### payment_plans
- Must-have: **YES at ≥4-agent** (not developer-canonical)
- Structure: **KES 200,000** reservation + **20%** deposit + balance over construction / to Dec 2026 (conf 3)
- Official schedule: not published → still NV vs LOO

### features (microsite conf 5)
Heated swimming pool; gym + boxing area; 24-hour butler/concierge; Face ID + fingerprint + card access; CCTV  
*(EIA/agents: playground, restaurant/café, BBQ, shops, rooftop lounge, cinema = 4/3)*

### agents
CPK; Vorsa Group; Azipa; Erysler Realty; GNA; NRE; Almasi Realty; Hauzisha (portal)

### contacts (official microsite only — not Hauzisha)
+254 705 818 181; Info@onlyounairobi.com; Elgeyo Road, Kilimani  
*(shared with GLBC head-office pattern — does **not** prove primary_developer)*

### construction / completion
- Dec 2026 cluster (4) vs Q1 2027 minority (3)
- EIA: 3 blocks × 21 floors; parking 246 vs 260 internal conflict → NV
- Agent storeys 20 vs 22 vs EIA 21 → NV

### research / NDI
**Primary developer** (Onlyou vs GLBC vs co-dev); official prices; LOO payment; storeys; parking; registry link Onlyou↔GLBC

---

## 3. Gaia Brookside — DISC-NBO-021

| Field | Value | Conf |
|-------|-------|-----:|
| slug | `gaia-brookside` | — |
| external_id | `DISC-NBO-021` | — |
| canonical_name | Gaia Brookside | 5/4 |
| status_label | Off-plan / under construction | 5/3 |
| inventory_class | `building` | intent lock |

### primary_developer
- **id:** `dev-wonder-properties` (**NEW** ← promote `dev-lead-wonder-properties`)
- **legal_name:** Unknown (trading **Wonder Properties** / Wonder Properties Kenya)
- **website:** https://www.wonderpropertykenya.com/ · project https://www.wonderpropertykenya.com/projects/gaia
- **phones:** +254 116 100 600
- **emails:** wonderproperties3@gmail.com
- **address:** Kirichwa Road, Off Argwings Kodhek, Kilimani, Nairobi (4)
- **confidence:** 5 trading / 0 legal SPV
- Secondary Wonder phones (Diplomat microsite, for verification): +254 116 126 666; info@wonderpropertykenya.com

### related_parties
| role | name | notes | conf |
|------|------|-------|-----:|
| marketing_partner / ops | Fameve (laban@fameve.com) | brochure mail_recipients | 2 NV |
| creative_partner | Karim CG Visuals | powered-by / partner@ | 2 |

### geo
- city: Nairobi (5) · neighbourhood: Westlands / Brookside Gardens (5)
- streets: **Brookside Gardens Drive** (4)
- lat/lng: none harvested (0)

### unit_types (agent claim set conf 3; Wonder “3, 4 & 5 Bedroom” soft 4)
| beds | size_sqm | label | notes |
|-----:|---------:|-------|-------|
| 3 | 180 | 3BR | from-23M entry |
| 3 | 192 / 210 / 219 (some 209) | 3BR + DSQ | densest |
| 4 | 256 | 4BR | |
| 4 | 275 | 4BR + DSQ | |
| 5 | 365 / 387 | 5BR + DSQ | |
| — | — | penthouse | agent exclusive — NV |

### prices (Wonder HTML silent on typed list)
| amount | ccy | tier | notes |
|--------|-----|------|-------|
| from ~23M / typed 25.3–51M+ | KES | agent (3) | Oaklane/A-Luxe/NRE/Realtors/Sir Francis |
| 25.3–45M | KES | portal ≤2 | Hauzisha |
| brochure PDF | — | host 5 / prices 0 | not OCR’d |

### payment_plans
- Must-have: **NOT met** (only 3 agents on 20%+quarterly; Block excluded; Wonder silent)
- Claim: 20% deposit + quarterly to completion (conf 3) — NV

### features (Wonder chips conf 5)
Children’s play area; CCTV; high-speed lifts; sky lounge; smart home; swimming pool; car parking; modern fitted gym; reception; coffee shop; health center; meeting room; yoga room; spa  
*(helipad/cinema/padel etc. agent ≤3 NV)*

### agents
Oaklane Properties; A-Luxe Realty; Nairobi Real Estate; Ravi Homes; Realtors.co.ke; Sir Francis Marketing; Hauzisha (portal)

### contacts
+254 116 100 600; wonderproperties3@gmail.com; Kirichwa Rd address  
**Never** 0730

### construction / completion — **NDI conflict**
| claim | sources | flag |
|-------|---------|------|
| June 2028 | Hauzisha, Oaklane, A-Luxe, NRE body | cluster |
| Dec 2027 | Ravi, Realtors | older/live |
| Q3 2027 | NRE widget | internal conflict |
| Dec 2028 | Sir Francis | outlier |

→ `needs_developer_input` — no canonical month  
Units 217 / 18 floors = agent 2 NV; NRE 58% = 1 NV

---

## 4. Diplomat Residencies — DISC-NBO-022

| Field | Value | Conf |
|-------|-------|-----:|
| slug | `diplomat-residencies` | — |
| external_id | `DISC-NBO-022` | — |
| canonical_name | Diplomat Residences (alias Diplomat Residencies) | 5/4 |
| status_label | Off-plan / under construction | 4 |
| inventory_class | `building` | dossier lock |

### primary_developer
- **id:** `dev-wonder-properties` (**REUSE same NEW id as Gaia** — one Wonder row)
- **legal_name:** Unknown (trading Wonder Properties / Wonder Properties Kenya)
- **website:** https://www.wonderpropertykenya.com/ · https://diplomat.wonderpropertykenya.com/ (502 this pass; indexed + brochure OK)
- **phones:** +254 116 126 666; +254 702 818 888; +254 792 696 666; +254 701 818 888
- **emails:** info@wonderpropertykenya.com
- **address:** Kirichwa Rd, Westlands
- **confidence:** 5 trading / 0 legal SPV

### related_parties
| role | name | notes | conf |
|------|------|-------|-----:|
| operator / hotel_manager | Unnamed “renowned hospitality group” | marketing only | 2 NV |

### geo
- city: Nairobi (5) · neighbourhood: Westlands (5)
- streets: **Peponi Road** (~30 m / steps from Westgate Mall) (5)
- lat/lng: none (0)

### unit_types (official: 1 & 2BR; sizes agent-only)
| beds | size_sqm | label | conf |
|-----:|---------:|-------|-----:|
| 1 / studio | 43 | Mini 1BR / Studio / Type A | 3 |
| 1 | 52 | Type B | 3 |
| 1 | 76 | Type C (some sold out) | 3 |
| 1 | 88 | Type D (some sold out) | 3 |
| 2 | 113 | Type E | 3 |
| 2 | 142 (one KF 139) | Type F / executive | 3 |

Hauzisha Studio chip vs developer “1 and 2-bedroom” → NV on Studio label  
25 floors agent (3); Almasi 875 residences = 1 reject/NV

### prices (developer silent)
| amount | ccy | tier | notes |
|--------|-----|------|-------|
| from ~5.0–5.5M; typed to ~16.7–19.2M | KES | agent (3) | Almasi/Vorsa/GNA/Ravi/Palmier/KF |
| 5.0–13.3M | KES | portal ≤2 | Hauzisha |

### payment_plans
- Must-have: **YES ≥4 agents** (not developer-locked)
- Structure: **20%** min deposit + balance during build / ~3 years (conf 3) → NV vs Wonder LOO

### features (microsite/brochure conf 5)
Rooftop pool / Sky Club; rooftop restaurant/café; fitness centre; wellness spa; yoga lounge; children’s playground; meeting rooms; residence lounge; concierge; courtyard garden; padel/tennis; parking; 24/7 security; smart home; heated water; borehole; power backup

### agents
Almasi Realty; Vorsa Group; GNA Real Estate; Ravi Homes; Palmier Properties; Knight Frank; Space Kenya (UC media); Hauzisha (portal)

### contacts
+254 116 126 666; +254 702 818 888; +254 792 696 666; +254 701 818 888; info@wonderpropertykenya.com

### construction / completion
- UC footage Apr–Nov 2025 (Space Kenya)
- Completion claim set: Mar 2028 / Q1–Q2 2028 vs KF Dec 2027 — official silent → NV
- Microsite live 502 this pass — re-fetch NDI

### research / NDI
Official price list; completion date; payment LOO; hospitality operator name; unit totals; GPS; Studio vs mini-1BR

---

## 5. AYA Luxury Residence — DISC-NBO-023

| Field | Value | Conf |
|-------|-------|-----:|
| slug | `aya-luxury-residence` | — |
| external_id | `DISC-NBO-023` | — |
| canonical_name | AYA Luxury Residence | 5/4 |
| status_label | Under construction / off-plan sales | 5 |
| inventory_class | `building` | 5 |

### primary_developer
- **id:** `dev-whitehorse-real-estate` (**NEW**; legacy face `dev-aad-real-estate` / promote away from sole `dev-lead-aad-real-estate`)
- **legal_name:** Unknown
- **trading_names:** Whitehorse Real Estate (current); AAD Real Estate (pre-rebrand)
- **website:** https://whitehorserealestate.ke/ · https://aad.ke/
- **phones:** +254 704 191919 (0704 191 919)
- **emails:** info@whitehorserealestate.ke; sales@whitehorserealestate.ke; legacy sales@aad.ke
- **address:** Jahazi Building, James Gichuru Road, 3rd Floor, Lavington, Nairobi
- **confidence:** 5 Whitehorse trading / 0 legal SPV / Sandoral 1

### related_parties
| role | name | notes | conf |
|------|------|-------|-----:|
| prior_trading_name | AAD Real Estate | rebrand predecessor | 5 as prior face |
| unverified_developer_attribution | **Sandoral Developers** | NRE only; “not independently confirmed”; Aria Park ≠ proof | 1 **NDI** — never primary |

### geo
- city: Nairobi (5) · neighbourhood: Kileleshwa (5)
- streets: **Othaya Road** × **Makueni Road** (5); CPK “Makueni × Nyando” = 2 NV
- lat/lng: none (0)

### unit_types (agent matrix conf 4)
| beds | size_sqm | label |
|-----:|---------:|-------|
| 1 | 49 | Mini 1BR / studio |
| 2 | 125 | 2BR |
| 3 | 208 | 3BR + DSQ |
| 4 | 262 | 4BR + DSQ |
| 3 | 221 / 265 / 280 | 3BR duplex + DSQ |
| 4 | 400 | 4BR duplex + DSQ |
| 3 | 255 / 347 | 3BR duplex garden villa |
| 4 | 609 | 4BR duplex garden villa |
| 6 | 740 | 6BR duplex garden villa |
| 5 | 488 | 5BR duplex sky villa |
| 6 | 503 | 6BR duplex sky villa |
| 5 | 360 / 418 / 580 | 5BR triplex sky villa |

### prices (multi-claim)
| amount | ccy | tier | notes |
|--------|-----|------|-------|
| Starting Kes **7.5M** | KES | developer social (4) | Whitehorse LinkedIn |
| ladder ~8.5–98M | KES | agent (3) | GNA/NRE/Own It/Sir Francis consensus shape |
| Starting Ksh 19M | KES | site chrome (2) | portfolio-level NV |
| 7–28M | KES | portal ≤2 | Hauzisha incomplete vs villas |
| Finlay/CPK lower/older | KES | agent (2) | likely stale NV |

### payment_plans
- Must-have: **soft yes** (developer-indexed 4-year/0% + multi-agent)
- Structure: **4-year / 0% interest** (conf 4); **30%** deposit + balance ≤48 mo / construction (agent conf 3)
- Deposit % not on launch text → NV; ignore NRE 20% calculator

### features (AAD launch / multi-source 5/4)
Heated/infinity pool + sunken lounge; gym; kids’ play; yoga garden; water features; on-site restaurant + supermarket; 8 high-speed lifts; solar water heating; full backup generator; 24hr security + video intercom/CCTV

### agents
GNA; NRE; Own It Kenya; Sir Francis Homes; Finlay; CPK; Kenya4u; Hauzisha (portal)

### contacts (Whitehorse/AAD only)
+254 704 191919; info@whitehorserealestate.ke; sales@whitehorserealestate.ke; Jahazi / James Gichuru; legacy sales@aad.ke

### construction / completion — NDI
- Dec 2028 vs Q3 2028 (3) — NDI; reject NRE Q1 2026 as stale (1)
- NRE UC 92% = 2 NV; Whitehorse LinkedIn Oct 2025 progress (no %)
- AAD launch ~2-acre (4); CPK 11-storey (2 NV)

### research / NDI
Legal SPV (Whitehorse vs AAD vs Sandoral); live price list; deposit %; completion month; Nyando wording; GPS; total units

---

## Cross-cutting locks for CSV ingest

1. All five `inventory_class` = **`building`**.
2. **Never** seed `0730 731 355` on any developer/property contact.
3. Only You: `primary_developer_id` **null**; GLBC RelatedParty `marketing_partner`; Onlyou Investments Ltd RelatedParty `legal_spv`.
4. AYA: primary Whitehorse/AAD; Sandoral RelatedParty only + NDI.
5. Wonder: **one** developer row for Gaia + Diplomat (reuse id).
6. GLBC: Libra primary only this wave; **skip Gemini Hub**.
7. No glamorous developer found to reuse.
8. Prices: always multi-claim rows — no portal scalar.
9. Payment must-have summary: Libra ❌ · Only You ✅ agents · Gaia ❌ · Diplomat ✅ agents · AYA soft ✅ developer+agents.
