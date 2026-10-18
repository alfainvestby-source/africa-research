# Skill pack: Product readiness / data-quality review agent

**Propose new agent:** **Product Readiness Reviewer** (working name)  
**Goal:** Review gathered corpus quality and **gap-map** what is missing to ship a Kenya product in the class of **Rightmove** (public) + **Rightmove Plus / Pro Hub** (agents) + Admin ops — without inventing facts.

**North star:** [goal-and-approach.md](../goal-and-approach.md) · [product/surface-map.md](../product/surface-map.md) · [decisions.md](../decisions.md)  
**Why a new agent (not more research clones):** Research waves grow dossiers; this agent **audits readiness for product surfaces** and tells the coordinator what to fix next.

**Analogy naming (user):** Rightmove = consumer portal; “Rightmove Pro / Plus hub” = agent CRM-ish tools (comparables, multi-price, trust, who-sells-what). We use tiers **`public` / `admin` / `plus`**.

---

## Agent mission (one sentence)

Score every development against **public-shippable**, **admin-operable**, and **plus-useful** bars; output a prioritized gap backlog tied to concrete skills/agents — never invent market data.

## Hard rules

1. No invented properties, prices, yields, or GPS.  
2. Developments-first (off-plan / UC schemes); unit/apartment ads only if multi-source reliable (existing scope lock).  
3. Block.ke and similar AI portals = low-trust discovery only — never public-canonical.  
4. Public fields require **high confidence + high coverage** ([coverage-field-promotion](coverage-field-promotion.md)).  
5. Conflicts stay as claim sets; official-vs-official → `needs_developer_input`.  
6. Reuse existing scorecards; do not fork parallel truths.

---

## Skill pack (what this agent should own / invoke)

### Core skills this agent **owns** (new)

| # | Skill | Job | Primary output |
|---|-------|-----|----------------|
| **R1** | **Product readiness scorecard** | Per-development checklist: public / admin / plus readiness (0–100 or traffic lights) from dossier flags + promotion gates | `docs/product/readiness-scorecard.md` + CSV |
| **R2** | **Surface gap matrix refresher** | Diff live corpus vs [surface-map.md](../product/surface-map.md) capabilities A/B/C — mark `ok / partial / missing` with evidence counts | Update surface-map gap column + `docs/product/gap-backlog.md` |
| **R3** | **Public ship-blocker finder** | List fields that **block** a Rightmove-like card/search (NDI on hero fields, no canonical name/geo/developer, price NDI, media empty) | Admin P0 queue slice |
| **R4** | **Plus usefulness audit** | For agents: is multi-price usable? payment normalized? agent graph ≥2? comps possible? trust badge safe? | `docs/product/plus-readiness.md` |
| **R5** | **Corpus denominators & stub hygiene** | Define “method-complete” vs stub; exclude thin discovery rows from public %; track wave growth (e.g. Block wave-1) | Feeds coverage + DQ scorer |
| **R6** | **Source-trust & contamination review** | Flag dossiers over-reliant on low-trust portals; Block/AI density; single-agent commercial fields | Trust appendix in scorecard |
| **R7** | **Verification queue synthesis** | Merge NDI/NV from DQ scorer + readiness blockers into one ordered work queue for research agents | `docs/db/verification-queue.md` |

### Skills this agent **invokes** (already exist — do not rebuild)

| Existing skill | Use in review |
|----------------|---------------|
| [data-quality-scorer](data-quality-scorer.md) | `risk_score`, P0–P3 triage, NDI/NV counts |
| [coverage-field-promotion](coverage-field-promotion.md) | Which fields can flip `public` |
| [product-surface-mapper](product-surface-mapper.md) | Capability taxonomy A/B/C |
| [entity-resolution](entity-resolution.md) | Party graph cleanliness for Plus CRM |
| [payment-plan-normalizer](payment-plan-normalizer.md) | Plus affordability / filters |
| [area-comps-psf](area-comps-psf.md) | Plus comps readiness |
| [geo-poi-enricher](geo-poi-enricher.md) | Map pin coverage |
| [photo-collector](photo-collector.md) | Gallery coverage |
| [feature-taxonomy](feature-taxonomy.md) | Filter facets |

### Skills this agent should **recommend spawning** when gaps dominate (from [proposed-listing-analytics-skills](proposed-listing-analytics-skills.md))

| Gap pattern | Spawn next |
|-------------|------------|
| Many NDI/NV, few clears | **Verification queue owner** (P0) |
| Sizes/prices trapped in PDFs | **Document / brochure intelligence** |
| No “units left / sold-out” | **Inventory & availability tracker** |
| Same project, conflicting agent copy | **Cross-portal listing matcher** |
| Stale prices | **Price observation time series** |
| Weak parking/specs filters | **Spec & parking normalizer** |
| Tenure/plot sparse | **Legal / tenure pack** |
| Agent “who covers X” empty | **Agency coverage map** |
| Developer track record missing | **Developer portfolio intelligence** |

---

## Scorecard dimensions (proposed)

Score each **method-complete** dossier on three product bars:

### Public (Rightmove-like consumer)

| Dimension | Pass heuristic (illustrative) |
|-----------|-------------------------------|
| Identity | Canonical name + aliases; anti-merge notes |
| Place | City + neighbourhood; street if claimed; pin method known |
| Developer | Primary developer conf ≥4 **or** clear trading face + NV on SPV |
| Product | Unit types claim set; amenities core sourced |
| Commercial | Not required to show single `price_from`; must not show NDI hero price |
| Media | ≥1 verified image or official brochure page |
| Trust | Not Block-only; ≥5 retained sources |

### Admin (ops hub)

| Dimension | Pass heuristic |
|-----------|----------------|
| Claim hygiene | Conflicts recorded; NDI/NV explicit |
| Sources | Evaluated/retained counts; thin skips listed |
| Parties | Agents/contacts separated from developer |
| Queueable | Open questions actionable |

### Plus (agent / pro hub)

| Dimension | Pass heuristic |
|-----------|----------------|
| Multi-price table | ≥2 independent `price_claims` or developer typed matrix |
| Payment | Normalized deposit/tenor **or** developer schedule |
| Agent graph | ≥2 agencies/portals with URLs |
| Comps hook | Size+price pair usable for KES/sqm **or** flagged missing |
| Trust signal | DQ risk band available; low-trust sources labeled |

---

## Review workflow (agent runbook)

1. **Inventory** — list method-complete dossiers vs stubs/leads (`docs/projects/*`, master index).  
2. **Pull scores** — run/refresh DQ scorer + field-promotion coverage.  
3. **Score readiness** — R1 per property × public/admin/plus.  
4. **Gap matrix** — R2 against surface-map capabilities (search, card, map, enquire, pro comps, admin queue).  
5. **Ship blockers** — R3 top N that block a public MVP card.  
6. **Plus gaps** — R4 top N that block agent usefulness.  
7. **Synthesize queue** — R7 ordered backlog: verify → enrich → new research waves.  
8. **Recommend skills** — which specialist agents to launch next (table above).  
9. **Report** — short exec summary for coordinator + link scorecard/backlog.

**Cadence:** After each research wave (e.g. Block wave-1), or weekly while corpus grows.

---

## First review slice (suggested when agent launches)

Include recently promoted Block wave-1 dossiers to stress-test the scorecard:

| ID | Project | Likely review focus |
|----|---------|---------------------|
| DISC-NBO-007 | 237 Lulu | Official price NDI (4.4M vs typed cards); payment **strong** (developer) |
| DISC-NBO-008 | Highpoint 336 | Microsite 500; 20% deposit near-threshold; progress 8% vs 40% |
| DISC-NBO-009 | Jabali Towers | Size schedule NDI; payment **strong**; ≠ Porini |
| + prior Wave C / discovery set | — | Baseline vs new |

Also flag **Block-sourced leads not dossiered** as discovery-only — not public inventory.

---

## Deliverables checklist (per run)

- [ ] `docs/product/readiness-scorecard.md` (+ optional CSV under `docs/db/seed/`)  
- [ ] `docs/product/gap-backlog.md` (P0/P1/P2, tied to surface-map IDs A1…)  
- [ ] `docs/db/verification-queue.md` (or update existing)  
- [ ] `docs/product/plus-readiness.md` short agent-hub view  
- [ ] Note in [agent-roster.md](../agent-roster.md) + changelog  
- [ ] **Do not** mutate dossier facts except via queued research handoffs

---

## What this agent is **not**

- Not a replacement for off-plan research agents.  
- Not a UI builder.  
- Not allowed to invent comps, yields, or “market averages.”  
- Not an ingest pipeline for Block apartment listings.

---

## Launch recommendation

| Item | Recommendation |
|------|----------------|
| Priority | **P0** — run before more large research waves if goal is product clarity |
| Depends on | Existing DQ scorer + surface-map + field-promotion (already present) |
| First output | Readiness scorecard over current method-complete corpus + gap backlog for public MVP vs Plus MVP |
| Pair with | **Verification queue owner** as the execution twin (this agent prioritizes; that agent clears) |

---

## Relation to existing proposals

Extends [proposed-listing-analytics-skills.md](proposed-listing-analytics-skills.md) with an **orchestration / review** agent. Does not replace payment normalizer, comps, or DQ scorer — it **consumes** them to answer: *“Are we ready for a Kenya Rightmove + Pro hub, and what’s missing?”*
