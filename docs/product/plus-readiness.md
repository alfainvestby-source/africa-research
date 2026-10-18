---
title: Plus / agent-hub readiness
skill: product-readiness-reviewer
version: 0.1.0
updated: 2026-10-16
---

# Plus readiness — agent / pro hub

Short view for a Kenya **Rightmove Plus–class** surface: multi-price, payment, who sells what, trust — **without** inventing comps or yields.

Full scorecard: [readiness-scorecard.md](readiness-scorecard.md) · Queue: [verification-queue.md](../db/verification-queue.md)

---

## What Plus needs vs what we have

| Plus capability | Corpus state | Ready enough? |
|-----------------|--------------|---------------|
| Multi-price table | Almost every method-complete dossier has `price_claims[]` | **Yes** for Admin/Plus display |
| Payment deposit / tenor | Strong where developer published (Lulu, Jabali, Porini, Galaxy, Longines, Capricorn FAQ); agent ≥4 elsewhere | **Partial** — seed CSV still 11 props; refresh needed |
| Agent / portal graph | Dense on Nairobi agent-heavy schemes | **Yes** for browse; brand dedupe ongoing |
| Trust / risk band | DQ scores on 11; wave-1 estimated | **Partial** — extend DQ to 30 |
| Size + price for KES/sqm | Often yes; **Jabali blocked** by official size NDI | **Partial** |
| Construction progress | Sparse; conflicts when present | **No** for a polished Plus widget yet |
| Export / CRM handoff | Not built | **No** (product later) |
| Yield tools | No rental corpus | **No** — do not invent |

---

## Best Plus demo candidates (today)

Projects where an agent can already see useful multi-source commercial data:

| ID | Why Plus-useful | Watch |
|----|-----------------|-------|
| DISC-NBO-007 237 Lulu | Developer payment by unit type; rich price claim set | Do not pick a winner on 4.4 vs typed |
| DISC-NBO-009 Jabali | Official payment + Dec 2028 + tenure + parking rules | Size NDI — badge, don’t collapse |
| NBO-013 Galaxy One | Tracker + dual official commercial depth | Show all NDI rows |
| NBO-007 Diamond Bay | Dense sources; official from dual | NDI hero |
| NBO-004 Porini | Master-plan + payment developer | Price/tenor NDI |
| NBO-001 Golden Mansion | NEMA + multi agents | Commercial agent-only |

**Avoid as Plus “hero” demos:** Misty Springs, Polaris (developer identity too weak).

---

## Wave-1 Plus lights

| Project | Multi-price | Payment | Agents | Comps hook | Trust |
|---------|:-----------:|:-------:|:------:|:----------:|:-----:|
| 237 Lulu | G | G | G | G | High |
| Highpoint 336 | G | A | G | G | Med |
| Jabali Towers | G | G | A | R (size NDI) | High |

---

## Plus MVP recommendation

Ship an **agent-facing** slice before a clean public portal:

1. Development page with **all price claims** + badges for NDI/NV.  
2. Payment panel from normalized claims (refresh seed first).  
3. Agency strip (≥2 URLs).  
4. Trust band from DQ `risk_score`.  
5. Hide invented yields; hide Block-sourced rows.

Public can follow once verification clears P0/P1 hero conflicts and media/geo land.
