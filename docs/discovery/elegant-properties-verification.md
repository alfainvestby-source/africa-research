# Elegant Properties — development verification (non-Hauzisha)

**Pass date:** 2026-10-16  
**Developer id:** `dev-elegant-properties` ([seed/developers.csv](../db/seed/developers.csv))  
**Hauzisha import parent:** [hauzisha-developers.md](../db/hauzisha-developers.md) · [hauzisha-developers-2026-10-16.md](hauzisha-developers-2026-10-16.md)

**Contact lock:** Developer sales = **`+254 700 004 449`** / **`info@elegantproperties.co.ke`** (official site; brochure also **`+254 731 286 286`**).  
**`0730 731 355` = Hauzisha portal only** — never attribute to Elegant.

---

## Verdict

All **5** Hauzisha-listed names are **real Elegant products** on **elegantproperties.co.ke**.  
**Research-queue locks (2026-10-16):** Ready = store/mark only (no dossier). Coming soon = review in scope. Off-plan / Building = dossier when selected. See [hauzisha-developers.md](../db/hauzisha-developers.md).

### In scope for dossiers (this wave)

| # | Name | ID | Why in scope | Location |
|--:|------|----|--------------|----------|
| 1 | **Forestview Residences** | DISC-NBO-012 | Off-plan / UC; June 2027 | Eldama Ravine / Karura |
| 2 | **Donyo Hill Residences** | DISC-NBO-013 | Off-plan / UC; end-2027 | Donyo Sabuk × Peponi |
| 3 | **48 Treehouse** | DISC-NBO-014 | Off-plan / UC; Dec 2027 | Peponi Rd / Karura |
| 4 | **Sunpark Residence II** | DISC-NBO-015 | Active phase only | Syokimau / Chady Rd |

### Skip — inventory_class `ready` (store later; don’t dossier now)

| Name | Reason |
|------|--------|
| **Sunpark Residence I** | Handed over / completed |
| **Oak & Ivy** | Ready unit inventory on Hauzisha |
| Ready-tagged unit ads | Not development research entities |

---

## Developer

| Field | Value | Conf |
|-------|-------|-----:|
| Trading name | **Elegant Properties** / Elegant Properties Kenya | 5 |
| Website | https://www.elegantproperties.co.ke/ | 5 |
| About claim | Family-run; “30+ years” marketing | 3 |
| Phone | **+254 700 004 449** | 5 |
| Phone (brochure) | +254 731 286 286 | 4 |
| Email | info@elegantproperties.co.ke | 5 |
| Legal / Companies Registry string | **Unknown** this pass | 0 |
| Hauzisha CTA 0730 731 355 | **Portal — not developer** | — |

---

## Per-project notes (for future dossiers)

### 1. Sunpark Residences
- Official distinguishes **Sunpark Residence I** (handed over → **skip**) vs **Sunpark Residence II** (active → **in scope** if Off-plan/Building).
- Hauzisha singular “Sunpark Residences” — dossier **II only**.
- Anti-merge: ≠ GLBC Gemini / other Mombasa Rd Gateway schemes; ≠ cheap Syokimau 1BR portal cards.

### 2. Donyo Hill Residences
- Official from **KES 27.9M**; 2/3/4BR; Donyo Sabuk × Peponi.
- **≠ Donyo Ridge** (different scheme / later completion in Block copy).  
- **≠ Donyo Manor** (Elegant “launching soon” 4BR from ~60M on Donyo Sabuk).
- CPK / Block = secondary agents only.

### 3. Forestview Residences
- Official + brochure + A-list align on Eldama Ravine / Karura; from **29.5M**; June **2027**.
- Sizes on agents in sqft bands — tag measure in dossier.

### 4. 48 Treehouse
- Official brochure: Peponi Rd; 48 units; home automation; Elegant phones on PDF.
- Ultra-premium from **~77.9M** — keep multi `price_claims[]`.

### 5. Oak & Ivy — **hold / skip for now**
- Official: **Loresho**, 20-acre gated, 3 villages, from **~66M**.
- Hauzisha shows **Ready** unit tags → **out of current off-plan process** per status lock.
- Revisit only if Off-plan/Building inventory reappears.

---

## Official portfolio extras (not on Hauzisha’s five)

Seen on elegantproperties.co.ke this pass — **leads only**, not verified for process yet: Casa Karura (launch Nov 2026); Oakland Residences; Skynest; Donyo Manor; Kitisuru Elements; Lofts @ Karura; etc.

---

## Sources retained (developer-first)

| # | URL | Role |
|--:|-----|------|
| 1 | https://www.elegantproperties.co.ke/ | Corporate |
| 2 | https://www.elegantproperties.co.ke/about-us | About + **700 004 449** |
| 3 | https://www.elegantproperties.co.ke/our-portfolio | Portfolio names |
| 4 | https://www.elegantproperties.co.ke/Featured-Properties | Prices / completion snippets |
| 5 | https://www.elegantproperties.co.ke/Forestview-Residences | Forestview |
| 6 | https://www.elegantproperties.co.ke/donyo-hill | Donyo Hill |
| 7 | https://www.elegantproperties.co.ke/Oak-Ivy | Oak & Ivy / Loresho |
| 8 | https://www.elegantproperties.co.ke/Sunpark-Residence-II | Sunpark II |
| 9 | https://www.elegantproperties.co.ke/48%20Treehouse/48TREEHOUSE%20BROCHURE%20-2-.pdf | 48 Treehouse brochure |
| 10 | https://a-listrealestate.ke/property/forestview-residences/ | Independent agent Forestview |
| — | Hauzisha developer/development pages | Discovery only; phone ignored |

---

## Dossier wave status — **DONE** 2026-10-16

| ID | Project | Dossier |
|----|---------|---------|
| DISC-NBO-012 | Forestview Residences | [forestview-residences.md](../projects/forestview-residences.md) |
| DISC-NBO-013 | Donyo Hill Residences | [donyo-hill-residences.md](../projects/donyo-hill-residences.md) |
| DISC-NBO-014 | 48 Treehouse | [48-treehouse.md](../projects/48-treehouse.md) |
| DISC-NBO-015 | Sunpark Residence II | [sunpark-residence-ii.md](../projects/sunpark-residence-ii.md) |

**Skipped (ready):** Sunpark I · Oak & Ivy  

**Steward handoff:** seed `property` / `listing.inventory_class` when DDL lands — dossiers are source of truth until then · [elegant-wave-steward-handoff.md](../../internal/elegant-wave-steward-handoff.md)
