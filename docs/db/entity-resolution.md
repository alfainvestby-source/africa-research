---
title: Entity resolution / party graph
skill: entity-resolution
version: 0.2.0
updated: 2026-10-18
corpus: 51 seeded properties + Hauzisha / Block / Nairobi CSV leads
inputs:
  - docs/db/seed/*.csv
  - docs/projects/*.md
  - docs/db/seed/listings_hauzisha_inventory_leads.csv
  - internal/nairobi_off_plan_projects.csv (leads only)
  - internal/block-ke-offplan-developments.csv (low-trust)
---

# Entity resolution — party graph merge map

**Purpose:** Dedupe developers, related parties, agents, contacts, and aliases so analytics and Admin/Plus surfaces do not treat CSV typos, false leads, or dual-model rows as separate companies. **v0.2** also covers **property ↔ lead** duplicate / relist detection.

**Rules:** No invented entities. Canonical IDs must already exist in seed **or** be explicit “do not create” rejects. Dual `co_developer` + RelatedParty rows are **intentional** (decisions lock) — document, do not collapse. **Never auto-merge properties** — see [duplicate-candidates.md](duplicate-candidates.md).

Related: [seed README](seed/README.md) · [duplicate-candidates.md](duplicate-candidates.md) · [developers.csv](seed/developers.csv) · [related_parties.csv](seed/related_parties.csv) · [agents.csv](seed/agents.csv) · [contacts.csv](seed/contacts.csv) · [decisions](../decisions.md)

---

## 1. Developer merge / reject map

| Lead / string seen | Action | Canonical ID | Evidence | Conf |
|--------------------|--------|--------------|----------|-----:|
| **Lionstone** (CSV NBO-013) | **Alias only** — do **not** create `dev-lionstone` | `dev-lionston-real-estate` | lionston.co; dossier Galaxy One; seed `csv_name_note` | 5 |
| **Lionston Real Estate Limited** | Keep | `dev-lionston-real-estate` | Same | 5 |
| **Procmura** (CSV NBO-010) | **Reject as developer** — NGO false lead | — → primary is `dev-rarlon-estate-development` | Berkeley ESIA / dossier; seed note | 5 reject |
| **Rarlon Estate Development Company Limited** | Keep | `dev-rarlon-estate-development` | Berkeley Homes ESIA proponent | 4 |
| **SkyPeak Limited** / Skypeak as CSV/Block “Developer” (NBO-001) | **Reject as primary** | Primary `dev-summit-vista-company-limited`; platform = `rp-skypeak-limited` | NEMA EIA Summit Vista; NRE FAQ “development platform” | 5 / 4 |
| **Summit Vista Company Limited** | Keep | `dev-summit-vista-company-limited` | NEMA EIA | 5 |
| **A1 Corporation** (CSV NBO-002) | **Trading alias** | `dev-a-one-corporation` | pandora.co.ke “A-ONE CORPORATION” | 5 |
| **A-One Corporation** / A-One / A1 | Same row | `dev-a-one-corporation` | Same | 5 |
| **Nanchong International** (CSV NBO-008) | **Trading name** of SPV | `dev-nanchong-longines-bay-limited` | longinesbay.com + NEMA SPV name | 5 |
| **Nanchong China** / Nanchong Group | Group when evidenced | `grp-nanchong-group` (parent); SPV stays separate | longinesbay about | 4 group |
| **Nanchong Longines Island Limited** | **Do not merge** into Bay SPV | `rp-nanchong-longines-island` only | Different Westlands filing | 4 |
| **Wimax Homes** / Wimax Homes Limited / LTD | Same | `dev-wimax-homes` | wimaxhome.com | 5 |
| **Rendeavour** / “Rendeavour (Tatu City)” CSV | Primary keep; Tatu separate | `dev-rendeavour` | Porini materials | 5 |
| **Tatu City Limited** | Keep developer **and** RelatedParty (dual) | `dev-tatu-city-limited` + `rp-tatu-city-limited` | Pack dual-Developers disclaimer | 4 |
| **Beijing XiangFeng Group** / Xiangfeng / Xiangefng typo | Keep dual | `dev-xiangfeng-group` + `rp-xiangfeng-group` | NRE + counsel affiliate | 3 |
| **Henbon Company LTD** / Henbon | Same | `dev-henbon-company-ltd` | henbon.co | 5 |
| **Staroot Real Estate** | Same | `dev-staroot-real-estate` | staroot.co.ke | 5 |
| **Riara Oasis Limited** | Same (CSV blank filled from NEMA) | `dev-riara-oasis-limited` | NEMA EIA | 5 |
| **Tian Yu International Company Limited** | Keep as **weak lead** | `dev-tian-yu-international` | LinkedIn-only; conf 2; **`needs_verification`** | 2 |
| **Own It Kenya** as Misty/Alba/… “developer” | **Reject** — agency | `agent-own-it` | Misty dossier; CSV sales_contact | 5 reject |
| **Crest Park** / **Siaya Park** | Prior project brands — **not** GroupCompany | no entity | Misty LinkedIn; Musilli framing | — |

### Recommended developer trading-name rows (for `developer_trading_name`)

| developer_id | trading_name |
|--------------|--------------|
| `dev-lionston-real-estate` | Lionston; Lionstone *(CSV typo — map inbound only)* |
| `dev-a-one-corporation` | A-One; A1 Corporation; A1 |
| `dev-nanchong-longines-bay-limited` | Nanchong International; Nanchong China |
| `dev-wimax-homes` | Wimax Homes; Wimax Homes LTD; Wimax Home |
| `dev-summit-vista-company-limited` | Summit Vista; Summit Vista Ltd |
| `dev-xiangfeng-group` | Beijing XiangFeng Group; XiangFeng Group; Xiangfeng Group |

Do **not** add Procmura or SkyPeak as trading names of the primary developer (they are false lead / different party).

---

## 2. RelatedParty — keep / do not upgrade

| ID | Type | Merge notes |
|----|------|-------------|
| `rp-skypeak-limited` | marketing_partner | **Canonical platform party** for Golden Mansion marketing. Never promote to primary developer. |
| `rp-laureland-homes` | marketing_partner | Do **not** merge into `dev-wimax-homes`. |
| `rp-tatu-city-limited` | co_developer | **Same legal org as** `dev-tatu-city-limited` — dual-model lock; shared website/contacts OK; do not delete either row until M11 simplification. |
| `rp-xiangfeng-group` | co_developer | Dual with `dev-xiangfeng-group` — same pattern as Tatu. |
| `rp-aimasi-real-estate` | marketing_partner | Not `dev-riara-oasis-limited`. |
| `rp-oasis-group` | marketing_partner | Unproven parent — do **not** create GroupCompany. |
| `rp-proxima-real-estate` | marketing_partner | Not Staroot co_developer. |
| `rp-nanchong-longines-island` | other | **Anti-merge** sentinel vs Longines Bay SPV. |

---

## 3. Agent merge map

| Strings / sites | Canonical `agent` ID | Notes |
|-----------------|----------------------|-------|
| Block Real Estate / block.ke | `agent-block` | Already single; CSV Loyd (+ Ricky Wekesa same phone) |
| NRE / Nairobi Real Estate / nairobirealestate.co.ke | `agent-nre` | Already single |
| CPK Real Estate / Commercial Property Kenya | `agent-cpk` | Already combined in seed name |
| KeDwell / Ace realtors Ltd | `agent-kedwell` | Already combined; Gemini copy near-dup of CPK — same brand family, keep one agent |
| Own It Kenya / ownitkenya.com | `agent-own-it` | Agent for Misty + future Own It CSV rows (NBO-014–016) |
| VorsaGroup / Vorsa | `agent-vorsagroup` | OK |
| Coral Property International / BuyRentKenya listing URL | `agent-coral` | **Watch:** website field points at buyrentkenya.com aggregator — treat as listing channel; do not invent separate `agent-buyrentkenya` without dossier evidence of distinct agency |
| Hauzisha, Ladva, Ravi, Sydia, Property Box, A-list, Masterways, Knight Frank, Realtors Platform, Malluug, Space Kenya, Sir Francis, Azipa, GNA, Flamingo, Thamana, Musilli, Myspace, Klin, OGRE, Nefroon | Keep as seeded | No merge evidence this pass |

### Agents often mistaken for developers (display rule)

| Agent ID | Risk |
|----------|------|
| `agent-block` | CSV `sales_contact` on many projects — never copy onto `property` sales office |
| `agent-nre` | Same |
| `agent-own-it` | CSV contact on Misty/Alba/Plumeria/Polaris leads — not developer |

---

## 4. Contact resolution

### Already correct (one contact, many property_agent edges)

| Contact ID | Value | Owner | Used across |
|------------|-------|-------|-------------|
| `ct-block-loyd-phone` | +254 725 937 686 | `agent-block` | CSV NBO-001–008 (+ Longines Ricky shares phone) |
| `ct-block-loyd-email` | loyd@block.ke | `agent-block` | Same |
| `ct-nre-phone` | +254 141 361 320 | `agent-nre` | CSV NBO-009–013 |
| `ct-nre-email` | info@nairobirealestate.co.ke | `agent-nre` | Same |
| `ct-ownit-phone` / `ct-ownit-email` | +254 722 716 182 / sales@ownitkenya.com | `agent-own-it` | Misty + future Own It CSV projects |

**Rule:** never duplicate Block/NRE/Own It phone rows per property.

### Near-collisions (distinct — do not merge)

| Values | Owners | Note |
|--------|--------|------|
| +254 117 222 **888** | `dev-wimax-homes` | Different from Lionston |
| +254 117 222 **666** / **999** | `dev-lionston-real-estate` | Same 117-222 prefix, different lines |
| +254 117 000 888 | `dev-wimax-homes` | Distinct |

### Recommended contact adds (from dossiers; not yet in seed)

| Value | Owner | Source | Action |
|-------|-------|--------|--------|
| +254 11 633 **7777** | `rp-skypeak-limited` | Golden Mansion dossier SkyPeak contacts | Add `ct-skypeak-phone-2` |
| +254 720 469 282 | `agent-own-it` | Misty Own It page | Add secondary Own It phone |
| sales@block.ke | `agent-block` | CSV Golfscape lead | Add when Golfscape researched — do not invent now |
| Ricky Wekesa label on same +254 725 937 686 | `agent-block` | Longines CSV | Optional second `label` / person note — **same contact value** |

### Dual-party shared org contacts

| Org | Developer row | RelatedParty row | Contact ownership |
|-----|---------------|------------------|-------------------|
| Tatu City Limited | `dev-tatu-city-limited` | `rp-tatu-city-limited` | Prefer **property** Porini sales (`ct-porini-*`) for project CTA; do not duplicate Tatu phones on both party rows without evidence |
| XiangFeng | `dev-xiangfeng-group` | `rp-xiangfeng-group` | No dedicated phones in seed — OK |

---

## 5. Property alias hygiene (inbound search)

| Alias / typo | Maps to property_id | In `property_aliases.csv`? |
|--------------|---------------------|----------------------------|
| Logines Bay | `prop-longines-bay-kilimani` | Yes |
| Berkely / Berkeley Residence | `prop-berkeley-homes` | Yes |
| Mistry Spring (A-list typo) | `prop-misty-springs` | **Recommend add** |
| Galaxy.ONE / Galaxy ONE | `prop-galaxy-one` | Yes |
| A1 Pandora / A-One Pandora | `prop-pandora-residences` | Yes |
| Diamond Bay Residence (singular) | `prop-diamond-bay-residences` | Yes |

---

## 6. Stakeholder sharing (OK — not duplicates)

| Stakeholder | Properties | Note |
|-------------|------------|------|
| `stk-karim-cg` | Pandora + Gemini Phase 2 | Same creative; correctly shared ID |
| Tatu executives / Makrem | Porini only | Keep |

---

## 7. Seed apply checklist (for DB steward)

1. **Do not insert** developers: Procmura, SkyPeak-as-primary, Lionstone-as-separate, Own-It-as-developer, Crest/Siaya GroupCompany.  
2. Ensure inbound alias map: Lionstone→Lionston, A1→A-One, Nanchong International→Longines Bay SPV, SkyPeak CSV→Summit Vista primary + Skypeak RP.  
3. Keep dual Tatu + XiangFeng rows until decisions M11.  
4. Add missing SkyPeak / Own It phones when convenient.  
5. Add property alias `Mistry Spring` → Misty.  
6. Wave C projects (Golfscape, Lesonia, Luna Oak, Alba, Plumeria, Polaris): reuse `agent-block` / `agent-nre` / `agent-own-it` contacts — do not mint new Block phones.

---

## 8. Summary counts

| Class | Canonical keep | Reject / alias-only | Dual-model pairs | Contact hubs |
|-------|----------------|---------------------|------------------|--------------|
| Developers | 13 seeded | Lionstone, Procmura, SkyPeak-primary, Own-It-as-dev | Tatu, XiangFeng | — |
| RelatedParty | 8 seeded | — | (same duals) | Laureland, Skypeak, Proxima, AIMASI |
| Agents | 29 seeded | — | KeDwell/Ace already merged | Block, NRE, Own It |
| GroupCompany | 1 (Nanchong) | Oasis Group / Crest-Siaya not created | — | — |

---

## 9. Property ↔ lead duplicate / relist rules (v0.2)

Living scoreboard: **[duplicate-candidates.md](duplicate-candidates.md)** · CSV: [`seed/duplicate_candidates.csv`](seed/duplicate_candidates.csv) · detector: [`../../internal/duplicate-relist-detect-2026-10-18.py`](../../internal/duplicate-relist-detect-2026-10-18.py)

| Rule | Detail |
|------|--------|
| Link lead → property | Only on `same_property` high (or medium + exact title); fill `property_id` on confirm |
| No property↔property auto-merge | Researched rows stay distinct until human says otherwise |
| Phases / Ready siblings | `related_phase` — never collapse Sunpark I↔II, Marina 1↔2, Gemini I↔II |
| Shared developer ≠ same asset | Elegant / Jafu / Wonder / Rendeavour / Staroot multi-site → `false_positive` unless name+place strong |
| Block.ke | Max `needs_human`; never sole link authority |
| Hauzisha phone | Linking a lead does **not** attach `0730 731 355` to the developer |
| Typo aliases | e.g. Capricon → Capricorn — add `property_aliases` when linking |

### Anti-merge reminders (property level)

Porini ≠ Jabali · Luna Oak ≠ Brookside Oak · Galaxy ≠ Ankori · Alina Valley ≠ Harbour/Ridge · Golfscape partner ≠ Highpoint 336 · Capricorn ≠ Staroot Residency · Oasis “* One Residency” siblings ≠ Rhapta One · Sensei ≠ Benford Greenwood.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-10-18 | v0.2.0 — property↔lead duplicate/relist pass (51 props × Hauzisha/Block/CSV); link rules; no auto-merge |
| 2026-10-16 | v0.1.0 — first merge map from 11-property seed + dossiers |
