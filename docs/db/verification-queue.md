---
title: Verification queue
skill: product-readiness-reviewer · verification-queue-owner
version: 0.1.0
updated: 2026-10-16
---

# Verification queue

**Purpose:** Single ordered Admin worklist of `needs_developer_input` / `needs_verification` items that block public or Plus trust.  
**Synthesized by:** Product Readiness Reviewer (first pass 2026-10-16).  
**Cleared by:** Verification queue owner (proposed).  
**Rules:** Do not invent winners on official-vs-official. Do not use Block.ke as authority.

Related: [data-quality-scores.md](data-quality-scores.md) · [readiness-scorecard.md](../product/readiness-scorecard.md) · [gap-backlog.md](../product/gap-backlog.md)

---

## How to use

| Column | Meaning |
|--------|---------|
| Priority | P0–P3 (product urgency, not only DQ risk) |
| Flag | NDI = needs_developer_input · NV = needs_verification |
| Owner skill | Who should pick this up |
| Status | open / in_progress / cleared |

---

## Active queue

### P0 — clear before public promotion of these rows

| # | ID | Project | Flag | Field / conflict | Suggested resolution | Owner | Status |
|--:|----|---------|------|------------------|----------------------|-------|--------|
| 1 | NBO-017 | [Misty Springs](../projects/misty-springs.md) | NV | Primary developer = Tian Yu lead only (conf 2); all commercial agent-only | Companies Registry / NEMA / site board photo; else keep **admin-only** forever | Research / ER | open |
| 2 | NBO-016 | [Polaris Residency](../projects/polaris-residency.md) | NV | Developer **unknown** | Same — do not public-list without developer | Research | open |
| 3 | DISC-NBO-008 | [Highpoint 336](../projects/highpoint-336.md) | NDI | Construction **8%** (NRE) vs **40%** (BuyRent) | Recover microsite / developer tracker; until then show claim set only | Research | open |
| 4 | NBO-013 | [Galaxy One](../projects/galaxy-one.md) | NDI | Units 210 vs 266; storeys 30 vs 19; dual official prices; progress % | Developer / Lionston confirmation — no silent average | Verification owner | open |

### P1 — blocks a public hero field or Plus comps

| # | ID | Project | Flag | Field / conflict | Suggested resolution | Owner | Status |
|--:|----|---------|------|------------------|----------------------|-------|--------|
| 5 | DISC-NBO-007 | [237 Lulu](../projects/237-lulu.md) | NDI | Official from **4.4M** vs typed cards **6.93M+** on same Mi Vida page | Ask Mi Vida sales / LOO which “from” is current | Verification owner | open |
| 6 | DISC-NBO-009 | [Jabali Towers](../projects/jabali-towers.md) | NDI | Size schedule FAQ ranges vs now-selling point sizes | Tatu / Rendeavour confirm current schedule | Verification owner | open |
| 7 | DISC-NBO-008 | [Highpoint 336](../projects/highpoint-336.md) | NDI / NV | Completion Q2 vs June 2028 vs July 2027 noise; legal name Development vs Developers Ltd; microsite 500 | Live site or PDF; registry string | Research | open |
| 8 | NBO-010 | [Berkeley Homes](../projects/berkeley-homes.md) | NDI | ESIA 361 vs agents 360 | Prefer ESIA for admin note; do not public scalar | Verification owner | open |
| 9 | NBO-002 | [Pandora](../projects/pandora-residences.md) | NDI | Official unit-mix conflict | Developer brochure vs site | Document intel | open |
| 10 | NBO-004 | [Porini Point](../projects/porini-point.md) | NDI | price_from + payment tenor official duals | Rendeavour / Tatu packs | Verification owner | open |
| 11 | NBO-007 | [Diamond Bay](../projects/diamond-bay-residences.md) | NDI | Official from 8.84M vs 9.34M | Henbon confirm | Verification owner | open |
| 12 | NBO-009 | [Gemini P2](../projects/gemini-residency-phase-2.md) | NDI | Site Mar 2029 vs LinkedIn 2026–2028 | Staroot confirm Phase 2 window | Verification owner | open |

### P1 — continued (wave-2)

| # | ID | Project | Flag | Field / conflict | Suggested resolution | Owner | Status |
|--:|----|---------|------|------------------|----------------------|-------|--------|
| 12b | DISC-NBO-011 | [Hephé Palace](../projects/hephe-palace.md) | NV | All `price_claims[]` + payment schedule (developer site silent; ≥4-agent 20–100% / 36-mo) | Sequoia sales / LOO / brochure | Verification owner | open |
| 12c | DISC-NBO-011 | Hephé Palace | NV | Legal face on LOO vs EIA **Sequoia China Limited** (not on hephepalace.ke Team) | Companies Registry + SPA | Research / ER | open |
| 12d | DISC-NBO-010 | [Balkis Residences](../projects/balkis-residences.md) | NDI | Official/May gross sizes vs older brochure/agent matrix | Sales office / LOO which schedule is current | Verification owner | open |
| 12e | DISC-NBO-010 | Balkis Residences | NV | **Sunmon Group** named only on Hauzisha; official site silent; no legal SPV | Confirm developer on LOO / registry; until then keep conf 2 | Research / ER | open |
| 12f | DISC-NBO-010 | Balkis Residences | NV | All prices + 20% payment (agent ≥4; not on official site); Mar vs Q4 2028 | Official price list + payment schedule | Verification owner | open |

### P2 — important but not ship-blocking this week

| # | ID | Project | Flag | Field | Note | Status |
|--:|----|---------|------|-------|------|--------|
| 13 | DISC-NBO-007 | 237 Lulu | NV | total_units = 237 (agent only) | Confirm on Mi Vida | open |
| 13b | DISC-NBO-011 | Hephé Palace | NV | Block count (SSC five×28); EIA duplex/4BR vs marketing mix; GPS | Enrich after seed | open |
| 14 | DISC-NBO-008 | Highpoint | NV | Service charge bands | Agent-only | open |
| 15 | NBO-008 | Longines | NDI | Blocks / storeys marketing vs NEMA | Admin claim set OK | open |
| 16 | DISC-NBO-006 | Brookside Oak | NDI | 9.9M vs Oak 8.2M; legal Van Tung | open |
| 17 | NBO-006 | Golfscape | NDI | 4.65M vs 5.6M + completion dual | open |
| 18 | NBO-012 | Luna Oak | NDI | Oak 11.9M vs 14.8M | open |
| 19 | KWA-001 | Kai | NDI | Unit taxonomy + completion cluster | open |
| 20 | NAK-001 | Kings Summit | NDI | 9M vs blog 8M | open |

### P3 — monitor / enrich

| Theme | Items |
|-------|--------|
| Wave-1 media + geo | Photo collector + geo enricher for Lulu / Highpoint / Jabali |
| Payment seed lag | Re-extract payment claims for all method-complete beyond original 11 |
| ROI marketing claims | Lulu / Jabali ROI → keep NV, never public |
| Block holds | Karura Forest Views — do **not** queue as a real project |

---

## Cleared

*(none this pass)*

---

## Optional later (not a queue item)

- **Allow Ready dossier research later** — today `inventory_class=ready` is stored and skipped by the research process. Product may reopen; see [gap-backlog.md](../product/gap-backlog.md) O1. Do not implement now.

---

## Cadence

- Refresh after each research wave.  
- Verification owner should mark Status and link the clearing note (email/LOO/registry URL) in the dossier — never delete the conflict history.
