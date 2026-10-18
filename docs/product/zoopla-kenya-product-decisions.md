---
title: Zoopla → Kenya product decisions
date: 2026-10-17
status: ALL #1–8 LOCKED (user checklist 2026-10-17)
inputs:
  - zoopla-kenya-gap-eval.md
  - kenya-listing-fields.md
  - surface-map.md
  - decisions.md
  - schema.md v0.1.14+
  - zillow-rightmove-model-study.md (evidence for #2 / #5)
  - portal spot-checks: Hauzisha, HassConsult, BuyRentKenya; buyer-cost blogs (KRA/Ardhisasa rates)
---

# Zoopla → Kenya — product decisions

**Status: LOCKED #1–8** (user checklist 2026-10-17). Prior open questions in [zoopla-kenya-gap-eval.md](zoopla-kenya-gap-eval.md) are resolved.  
**No invented property facts.** Schema already supports Ready/resale via `inventory_class` + `listing`.

Related: [kenya-listing-fields.md](kenya-listing-fields.md) · [surface-map.md](surface-map.md) · [decisions.md](../decisions.md) · [zillow-rightmove-model-study.md](zillow-rightmove-model-study.md) · [portal-inventory-class-research-rules.md](../discovery/portal-inventory-class-research-rules.md)

## Lock summary

| # | Lock | Code |
|---|------|------|
| 1 | Off-plan/`building` first; Ready+resale easy later | — |
| 2 | Development-first public + typology-linked listings (retained URLs only) | **2B** |
| 3 | Kenya energy vocab; no EPC chase | as proposed |
| 4 | Buyer costs guide; per-project when developer publishes | as proposed |
| 5 | Bathrooms first-class; fill when sourced; no invent; skip receptions | Zoopla/Zillow/RM |
| 6 | `tenure` claim; Admin/Plus; public conf≥4 official | as proposed |
| 7 | Agent phones **Plus only**; public = developer/project CTA | confirm Plus |
| 8 | Ready cards on Plus+Admin (badge); public off-plan/UC; no auto-dossier | **8B** |

---

## 1. LOCKED — Product focus now, Ready/resale later

**Lock (user confirmed):**

> Initially ship and research for **new developments / off-plan** (`off_plan` + `building`).  
> Schema and product surfaces must make **Ready + resale easy to add later** — do not paint ourselves into a developments-only corner.

**What this means in practice**

| Layer | Now (v1) | Later (easy add) |
|-------|----------|------------------|
| Research queue | Dossier `off_plan` / `building` (+ Coming soon → `off_plan`) | Optional Ready research = backlog only |
| Storage | Always set `inventory_class` on `property` and `listing` | Ready/resale rows already valid enums |
| Public browse | Off-plan / UC development pages first | Flip on Ready/resale browse without schema rewrite |
| Listing entity | Keep `listing` + nullable `property_id` for orphan Ready ads | Populate unit ads when product wants them |

**Already in schema (do not undo):** `inventory_class` = `off_plan` \| `building` \| `ready` \| `resale`; Ready = store/mark, no dossier for now.

**Written into** [decisions.md](../decisions.md) as of 2026-10-17.

---

## 2. LOCKED — 2B development-first + typology listings

**Lock:** Public = **development-first**; typology-linked `listing` snapshots from **retained URLs only**; no invented flat IDs. Backed by [zillow-rightmove-model-study.md](zillow-rightmove-model-study.md) (Zillow NC / Rightmove ADF grain).

Zoopla is **listing/ad-centric** (one URL = one offer). We are **development-master-centric** (one URL = project + typologies). Both can coexist; v1 public shows developments.

### Option 2A — Development page only (typology table, no unit ads)

**Buyer journey:** Search Westlands → open “Libra Residences” → see 3/4/5BR table, from-band, amenities, developer CTA.  
**Agent (Plus):** Same project + multi-price + agency graph.  
**Admin:** Claims/conflicts on the property.

| Pros | Cons |
|------|------|
| Matches our strongest data today | Feels less like Zoopla/BuyRent “pick a unit” |
| Avoids inventing unit inventory | Harder to show sold-out / reserved per type |
| Fastest public ship | Ready unit stock later needs a second surface |

**Fits:** Trust-first off-plan launch.

### Option 2B — Development-first public + soft typology “offers” (recommended)

**Buyer journey:** Development page is canonical; each row in the unit table can deep-link to a **typology offer** (not a specific flat number) when we have a retained agent/developer URL → stored as `listing` with `unit_type_id`.  
**Example:** “3BR + SQ · 193 sqm · from ~17.8M (agent)” → listing snapshot. No door numbers invented.  
**Agent:** Plus sees all listing URLs feeding that typology.  
**Admin:** Dedupes conflicting ads against the master typology.

| Pros | Cons |
|------|------|
| Zoopla-like cards without fake unit stock | Need listing seed discipline (retained URLs only) |
| Schema already has `listing` ↔ `unit_type` | Slightly more product work than 2A |
| Ready/resale later = same `listing` path | Typology ≠ specific apartment — must label clearly |

**Fits:** North star + Kenya off-plan reality (developers sell *types*, not US-style unit numbers early).

### Option 2C — Full Zoopla-style unit ads on public now

**Buyer journey:** SERP of individual ads (“Flat 12B, 2BR…”) linked up to a development.  
**Pros:** Familiar classifieds UX.  
**Cons:** We lack reliable unit-level inventory; agents invent stock; high NV; slows v1; fights Ready-skip rules.

**LOCKED as 2B.** Keep public **development-first**; use `listing` for **typology-linked ad snapshots** from retained URLs only; never invent flat IDs. Full unit classifieds = Ready/resale slice later.

---

## 3. LOCKED — Kenya energy/utilities vocabulary (not EPC-first)

**UK Zoopla:** EPC A–G is material information.  
**Kenya portals (observed):** BuyRentKenya / agents chip **backup generator**, **borehole**, **solar water heating**, **fibre internet** — not EPC. Hauzisha development cards use amenity chips, not energy ratings. HassConsult sells developments with lifestyle/amenities, not compliance certificates on the card.

**Our dossiers already speak this language** (examples, not inventing new facts):

| Kenya term | Typical source in our corpus | Map to |
|------------|------------------------------|--------|
| Backup generator / full backup power | Amenities (Elegant, Wonder, Whitehorse, agents) | `feature:backup_generator` |
| Borehole / borehole water | Amenities + BuyRent utilities | `feature:borehole` |
| Solar water heating / solar lighting | AYA, Rosewood, Montbleu, Rhapta agents | `feature:rooftop_solar` (+ variant_note) |
| Fibre / internet ready | Agent chips; Majengo wifi synonym | `feature:wifi` / `internet_cable` |
| 24/7 security, CCTV, electric fence | Near-universal | `gated_security`, `cctv` |
| Leasehold 99 years / sectional title on completion | Jabali FAQ (canonical); Montbleu/Marina agents (NV) | claim key `tenure` (see §6) |

**Proposed v1 material-info block (Kenya)** — replace EPC-first:

1. **Power resilience** — generator (yes/no + note)  
2. **Water resilience** — borehole / storage / county water (as sourced)  
3. **Hot water / solar** — when named  
4. **Connectivity** — fibre/internet when named  
5. **Security stack** — CCTV / gated / electric fence (already features)  
6. **Optional later:** green building / EDGE / any *named* certificate — only if developer publishes (do **not** invent an EPC clone)

**LOCKED:** Adopt the table above as the energy/utilities vocabulary. **Do not** chase UK EPC. Capture certificates only when a developer names them.

---

## 4. LOCKED — Buyer costs (guide + extract-when-sourced)

| | Zoopla (UK) | Kenyan portals today |
|--|-------------|----------------------|
| On listing | Council tax band, tenure, utilities NTS (“Ask agent”) | Rarely stamp duty on the card |
| Where costs live | Material information block | **Blog / buyer guides** (RealtorKenya, Block handbook, law firms); agent FAQs sometimes |
| Typical Kenya stack (2026 public guides) | — | Urban **stamp duty ~4%** (rural ~2%); legal fees ~1–2% + VAT; valuation/registry smaller — rough **~6–8%+** above price for Nairobi apartments |
| Off-plan marketing | Incentives, not stamp duty | Payment plan (deposit/tenor) dominates the card |

**Realistic v1 for us**

| Approach | Verdict |
|----------|---------|
| Per-listing stamp duty / rates fields | **No** — portals don’t; we’d invent or scrape volatile KRA rules |
| Capture when brochure/FAQ states a number | **Yes** — claim + NV if single agent (e.g. Alina service charge 12k) |
| Site-wide **Buyer costs guide** (Admin/Plus/help) | **Yes** — link from public; not a listing column |
| Service charge on development when sourced | **Yes** — claim key; public only if developer-backed + coverage |

**LOCKED:** guide-only for stamp duty/transfer/legal; per-project only when the **developer** publishes a figure. Service charge = extract-when-found.

---

## 5. LOCKED — Bathrooms as first-class card attribute

**Lock:** Fill `unit_type.bathrooms` when sourced (Zoopla / Zillow / Rightmove card pattern with beds/size). **Never invent.** Skip UK receptions/living-rooms as must-have. Evidence grain: [zillow-rightmove-model-study.md](zillow-rightmove-model-study.md).

**Why:** BuyRentKenya and Zoopla put beds + baths on every card. Prior seed had **0** bathrooms filled.

**Hygiene:** Extract-only when dossiers/agent sheets state an explicit count. “All ensuite” without a number ≠ invent baths = beds.

---

## 6. LOCKED — Tenure claim key

**What it is (Kenya plain language):**  
- **Freehold** — own the land/interest indefinitely.  
- **Leasehold** — time-limited interest (often **99 years** from a start date) — common on urban plots.  
- **Sectional title** — own an apartment unit + share of common property (the usual end-state for towers). Agents often say “sectional titles on completion.”

**Why Zoopla cares:** UK NTS forces tenure on sale listings.  
**Why we care:** Buyers and diaspora ask; Jabali’s official FAQ already gives **leasehold 99 years** (conf 5). Most of our corpus is silent or agent-only (Montbleu, Marina Bay 2).

**LOCKED:**  
- Claim key `tenure` (values: freehold | leasehold | sectional_title | unknown).  
- **Admin (+ Plus)** whenever found; **public** only when developer/official conf ≥4.  
- Not a research blocker if absent.

---

## 7. LOCKED — Agent phones on Plus only

**Relevance now:**  
- Hauzisha publishes one CTA (**0730 731 355**) on every development — we already lock that as **portal, never developer**.  
- BuyRentKenya shows agent “View number” on unit ads.  
- Our dossiers capture **many agencies per project** — useful for pros, confusing/risky for public (wrong phone = trust failure).

**Current surface-map intent (affirm):**  
- **Public:** project / **developer** sales CTA (ownership-tagged).  
- **Plus:** full agent + WhatsApp graph.  
- **Admin:** ownership QA (CSV/Hauzisha ≠ developer).

**LOCKED:** Full agent phones/WhatsApp = **Plus only**; public stays developer/project CTA. Schema unchanged — display rule.

---

## 8. LOCKED — 8B Ready on Plus + Admin only

Ready is **stored, not dossiered**. Question: who may *see* Ready stock in product UIs?

### Option 8A — Hide Ready everywhere until a Ready product slice

**Journeys:** Buyer never sees Ready; agent/Admin only see off-plan/UC corpus.  
**Pros:** Zero contamination of research queue; simple.  
**Cons:** Wastes stored Hauzisha Ready leads; agents still need Ready stock in real life.

### Option 8B — Plus + Admin see Ready unit cards; public does not (recommended)

**Buyer (public):** Off-plan/UC developments only.  
**Agent (Plus):** Toggle “Ready stock” → unit/ad cards from `listing` where `inventory_class=ready` (orphan OK). Thin fields OK; badge “not research-verified”.  
**Admin:** Same + match orphans to `property` when possible; never auto-open dossiers.

| Pros | Cons |
|------|------|
| Matches lock #1 (“easy to add later”) | Need minimal listing seed from portal exports |
| Agents get value without polluting public trust | Must keep Ready badge loud |
| Uses existing `listing` + inventory_class | Not full dossiers — expect thin prices/amenities |

### Option 8C — Public Ready browse now

**Pros:** Bigger inventory.  
**Cons:** Violates “off-plan first”; Ready data is lead-thin; trust risk.

**LOCKED as 8B.** Public stays new-developments; Plus/Admin Ready cards from stored listings (badge **not research-verified**); dossiers never auto-open for Ready.

---

## Checklist (resolved 2026-10-17)

```
1 LOCKED
2B LOCKED
3 as proposed LOCKED
4 guide-only (+ extract-when-sourced) LOCKED
5 bathrooms first-class LOCKED (hygiene pass done: 2/180 filled)
6 Admin claim / public conf≥4 LOCKED
7 confirm Plus LOCKED
8B LOCKED
```

---

## Out of scope / unchanged

- Public hero-price policy (multi claims; no silent NDI winner) — still locked from earlier cycles.  
- Slice C seed complete (corpus 46 / changelog 0.1.18).
