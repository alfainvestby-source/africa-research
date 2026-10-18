---
title: Hauzisha developers — saved inventory
updated: 2026-10-16
source_pass: docs/discovery/hauzisha-developers-2026-10-16.md
---

# Hauzisha developers — saved inventory

**Purpose:** Persist the 2026-10-16 Hauzisha `/developers/` import as **developer leads** (and link known seeded developers), before per-project verification.

**Seed extract:** [`seed/developers_hauzisha_leads.csv`](seed/developers_hauzisha_leads.csv)  
**Parsed developments:** [`../../internal/hauzisha-developers-2026-10-16.json`](../../internal/hauzisha-developers-2026-10-16.json)  
**Research narrative:** [`../discovery/hauzisha-developers-2026-10-16.md`](../discovery/hauzisha-developers-2026-10-16.md)

---

## Hard locks (research queue / inventory class)

**Schema v0.1.14:** `inventory_class` on `listing` **and** `property` ([schema.md](schema.md)). Seed sketch: [`seed/listings_hauzisha_inventory_leads.csv`](seed/listings_hauzisha_inventory_leads.csv).

| Portal tag / case | `inventory_class` | Research action |
|-------------------|-------------------|-----------------|
| **Off-plan** | `off_plan` | Lead → verify → **dossier** when selected |
| **Coming soon** | **`off_plan`** (no `coming_soon` enum) | **In scope for review** — not parked indefinitely |
| **Building** (UC) | `building` | Lead → verify → **dossier** when selected |
| **Ready** (unit ads **or** handed-over whole developments) | `ready` | **Store + mark only** — **no dossier for now** (optional later: gap-backlog O1) |
| **Resale** (when tagged) | `resale` | Store; don’t dossier in off-plan waves |

**Portal development exports** = **lead lists**, not finished inventory. Prefer development hubs over individual unit ads when researching schemes. **Ready only when tagged** — never infer from “N units for sale”.

**Mark both levels:** Ready unit ads (`listing`, `property_id` may be null) **and** Ready/handed-over whole developments (`property` + listing cards) — e.g. Sunpark I, Oak & Ivy while Ready.

---

## Hard locks (contact attribution)

| Rule | Detail |
|------|--------|
| **Hauzisha shared sales line** | **`+254 730 731 355` / `0730 731 355`** appears on almost every Hauzisha developer and development page. |
| **Owner** | This is **Hauzisha’s portal contact**, **not** the developer’s phone. |
| **Seed** | Already stored as [`ct-hauzisha-phone`](seed/contacts.csv) → `owner_type=agent`, `owner_id=agent-hauzisha`. |
| **Do not** | Copy this number onto `developer` or `property` contacts as developer sales. |
| **Do** | Capture developer phones/emails only from **official project/corporate sites**, LOO, or materials that clearly name the developer (not the portal CTA). |

Same pattern as CSV/Block sales contacts: portal phone ≠ contracting developer.

---

## How to read status

| `status` in CSV | Meaning |
|-----------------|---------|
| `seeded_match` | Name aligns with an existing `docs/db/seed/developers.csv` row (or strong dossier id) |
| `hauzisha_lead` | New from Hauzisha — **conf ≤2** until official/registry corroboration |
| `likely_marketing_partner_not_primary` | e.g. Skypeak / Oak Group — do not promote to `primary_developer` on Hauzisha alone |

---

## Counts

| Bucket | n |
|--------|--:|
| Developers on import | **51** |
| Already matched to corpus developer ids | **8** (plus a few dossier-only ids such as Mi Vida) |
| Hauzisha-only leads | **~41** |
| Flagged marketing-partner risk | **2** (Skypeak, Oak Group) |
| Developments linked on detail pages | **~127** |

---

## Elegant Properties (next verification slice)

From import only — **5** developments under Hauzisha:

1. Sunpark Residences (Syokimau)  
2. Donyo Hill Residences (Westlands)  
3. Forestview Residences (Westlands)  
4. 48 Treehouse (Westlands)  
5. Oak & Ivy (Westlands)  

**Verified 2026-10-16** → seed id **`dev-elegant-properties`** (conf 4) · contacts `ct-elegant-phone` / `ct-elegant-email` (**+254 700 004 449** — not Hauzisha).  
Full non-Hauzisha check: [elegant-properties-verification.md](../discovery/elegant-properties-verification.md).

---

## Related agents / contacts

| Entity | Id | Note |
|--------|-----|------|
| Hauzisha portal | `agent-hauzisha` | Listing/marketing portal |
| Shared phone | `ct-hauzisha-phone` | +254 730 731 355 |
