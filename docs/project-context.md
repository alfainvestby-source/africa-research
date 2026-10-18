# Africa New Development Research — Project Context

Plain language: [goal-and-approach.md](goal-and-approach.md) · Decisions log: [decisions.md](decisions.md)

## Goal
Build a **world-class Kenya property product** (Rightmove-class **public**, **Admin**, and **Plus**/pro). Critical path: a **strong data layer** for off-plan / new developments starting in Nairobi — professional collection, relational organization, no invented facts.

## Hard rules
- **No AI-invented facts.** Every field cites a real source URL (or documented offline contact). Unknown → `unknown` / `unverified`.
- **Developer / official project site outweighs agents.** Agents are secondary (discovery + cross-check).
- **Double-check:** prefer ≥2 independent sources, or clear developer provenance.
- **Flag conflicts** instead of silently picking a winner.
- Seed table comments / agent blurbs are **suspect** — leads only.

## Learning loop (process — locked 2026-10-15)
1. **Pilot 1–2** projects → draft dossiers + field inventory from what sources actually yield  
2. **Review draft** with coordinator/user → revise approach & must-have fields  
3. **Next 2** with revised method  
4. **Review again** → improve method; **retrofit** the first pilots  
5. Only then proceed to **~half of remaining**, then rest  
Ask when unclear; fields evolve from analysis, not a fixed upfront list.

## Confidence
- Stored on every fact for the **data model / ranking / QA** — **not shown in the public portal initially**.
- Rubric: 5 = developer/official; 4 = multi-source or agent+official; 3 = multi-agent only; 2 = single agent; 1 = weak/conflicted; 0 = unknown.
- Agent-only consensus cannot exceed 3 without official corroboration.

## Entity model (relational — agreed direction)
Map as a **relational graph**, not flat listing rows:

| Entity | Role |
|--------|------|
| `Property` / Development | Canonical project |
| `Developer` | Original seller/builder entity |
| `GroupCompany` | Optional parent above developer |
| `Agent` / Agency | Marketing sellers linked to properties |
| `Contact` | Phones, WhatsApp, emails, URLs — linked to Agent, Developer, or project sales office |
| `Stakeholder` | Financing partners, contractors, architects, land vendors, etc. (typed) |
| `Source` | URL/document with publisher + type + accessed_at |
| `Claim` / Fact | Field value + confidence + source links + conflict flags |

Property ↔ Agent (many-to-many), Property ↔ Developer (usually one primary, allow co-dev), Developer ↔ GroupCompany (optional), Property ↔ Stakeholder (typed M2M), all parties ↔ Contact.

This schema is the blueprint for the later portal DB; research outputs should already separate entities (not bury agent phones inside a project blob).

## Scope (v1 research)
- Geography: **Kenya-wide** discovery; Nairobi metro is the first researched corpus (17 dossiers). Expand research batches to other cities as leads land.  
- Asset: off-plan / under construction / not fully finalized  

## Conflict resolution (locked / updated 2026-10-16)
- Always highlight conflicts.
- **Developer vs agents:** if developer is known and developer sources **agree** on a field → **canonical = developer**; agents secondary.
- **Official vs official** (two developer pages disagree): **do not assume**. Flag **`needs_developer_input`**; no canonical until confidence is high or a later verification pass resolves it.
- Unproven brand/parent overlap → **`marketing_partner`** until proven. Co-named “Developers” (e.g. Rendeavour + Tatu City) → model as **both** `co_developer` and RelatedParty for now; revise later if needed.
- Payment plan must-have when **≥4** agent/portal sources agree, or any developer source.
- **Prices:** always keep multiple options (`price_claims[]`). Portal columns later = high confidence **and** high coverage across listings (~half missing → not a public field).
- **construction_progress:** store when developer publishes (claim set if pages conflict); not a portal must-have until coverage proves out.
- Must-have list is **living**; track consensus per item.

## Database model steward
A standing **Proptech DB Engineer** agent owns `/cursor/stores/self/docs/db/` — relational schema, seed extracts, ER notes, changelog — continuously updated from research dossiers and classifieds/proptech best practice. Research agents produce dossiers; the DB steward normalizes them into the model.

## Low-confidence claims (locked 2026-10-15)
- **Show** agent-only typologies, sold-out flags, and similar — never silently drop.
- Mark **`needs_verification`** when confidence is low (not on developer materials, sold-out not corroborated, or not listed on other independent sites).
- Canonical stays developer-backed when available.  
