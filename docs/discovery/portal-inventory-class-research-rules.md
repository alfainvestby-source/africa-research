# Portal inventory class — research-queue rules

**Locked:** 2026-10-16 (user answers to schema questions)  
**DDL:** schema **v0.1.14** — `listing.inventory_class` **and** `property.inventory_class` = `off_plan` \| `building` \| `ready` \| `resale`; `listing.property_id` nullable for orphan Ready ads  
**Research docs:** this file · [hauzisha-developers.md](../db/hauzisha-developers.md) · [decisions.md](../decisions.md) · [schema.md](../db/schema.md)

---

## Rules

1. **Portal / Hauzisha development exports** = **lead lists**. They are not finished master inventory.  
2. Mark **both** Ready **unit ads** and Ready / handed-over **whole developments**.  
3. **`ready`** (and **`resale`** when tagged): **store with special mark; do not run the research dossier process** for now (optional later: [gap-backlog.md](../product/gap-backlog.md) O1).  
4. **`off_plan`** / **`building`**: check / verify; open dossiers when selected for a wave.  
5. **Coming soon** → map to **`off_plan`** (no separate enum); **in scope for review** (identity + developer chase; may promote to dossier queue) — not held indefinitely.  
6. **Ready only when tagged** — never invent from “N units for sale”.  
7. Never treat Hauzisha **`0730 731 355`** as developer phone. Developments-only for dossiers; Block.ke low-trust.

---

## Relation to product surfaces

| Class | Public research priority | Admin / Plus |
|-------|--------------------------|--------------|
| off_plan / building (incl. Coming soon → off_plan) | High — dossier / review corpus | Full claims |
| ready / resale | **Out of dossier queue** | Store marked listings / properties |

Seed sketch: [`listings_hauzisha_inventory_leads.csv`](../db/seed/listings_hauzisha_inventory_leads.csv).
