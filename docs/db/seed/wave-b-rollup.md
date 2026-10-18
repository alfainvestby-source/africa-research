# Seed rollup — Wave B / half-batch + Cycle 1–2

Last refreshed: **2026-10-16**  
Source of truth for research status: [nairobi-master-index.md](../../nairobi-master-index.md)  
Locks: [decisions.md](../../decisions.md)

## Coverage (11 properties in `properties.csv`)

| external_id | slug | Developer (seed) | Key modeling flags |
|-------------|------|------------------|--------------------|
| NBO-001 | golden-mansion | Summit Vista (5) + XiangFeng **co_developer** dual + SkyPeak **marketing_partner** | NEMA EIA; CSV SkyPeak ≠ primary; multi prices; 20% agent must-have |
| NBO-002 | pandora-residences | A-One Corporation (5) | Unit mix **NDI**; brochure sizes canonical |
| NBO-003 | riara-oasis | Riara Oasis Limited (5); AIMASI / Oasis Group **marketing_partner** | NEMA; no microsite; studios NV |
| NBO-004 | porini-point | Rendeavour (5) + Tatu City Limited **co_developer** dual | Master-planned Tatu; payment 24-mo canonical |
| NBO-005 | astra-bay-residence | Wimax (5); Laureland **marketing_partner** | Gross/plinth; agent 2BR NV |
| NBO-007 | diamond-bay-residences | Henbon Company LTD (5) | Official from **8.84M vs 9.34M** **NDI** |
| NBO-008 | longines-bay-kilimani | Nanchong Longines Bay Limited (5); **GroupCompany** Nanchong Group | NEMA **601/3 blocks** vs marketing **NDI**; Q4 2029; staged payment canonical |
| NBO-009 | gemini-residency-phase-2 | Staroot (5); Proxima **marketing_partner** | Completion site vs LinkedIn **NDI**; deposit min 20% canonical |
| NBO-010 | berkeley-homes | Rarlon Estate Development (4) | ESIA **361 vs 360** **NDI**; CSV **Procmura** false lead |
| NBO-013 | galaxy-one | Lionston (5) | Units/storeys/progress **NDI**; deposit 10% canonical |
| NBO-017 | misty-springs | Tian Yu International (**conf 2** NV) | No microsite; Own It = agent; status heavily conflicted |

## Wave B / scale-half set (master index)

All listed scale/half-batch dossiers are now in seed:

NBO-001 · NBO-003 · NBO-007 · NBO-008 · NBO-009 · NBO-010 · NBO-017

Plus Cycle 1–2: NBO-002 · NBO-004 · NBO-005 · NBO-013

## Firsts this rollup

| Pattern | Project |
|---------|---------|
| First seeded **GroupCompany** | Longines → `grp-nanchong-group` |
| Dual co_developer + RelatedParty (again) | Golden → XiangFeng (same pattern as Porini/Tatu) |
| CSV false-lead developer | Berkeley (Procmura NGO); Golden (SkyPeak platform) |
| Weak developer conf 2 stay-lead | Misty (Tian Yu LinkedIn-only) |

## Superseded for coverage

Wave C complete — see **[corpus-rollup.md](corpus-rollup.md)** for full **17/17** inventory (includes Golfscape, Lesonia, Luna Oak, Alba, Plumeria, Polaris).

## Feature taxonomy

**Merged** into schema **v0.1.5** — [`feature-taxonomy.md`](../feature-taxonomy.md). Seeds: `features.csv`, `feature_scopes.csv`, `feature_synonyms.csv`, `property_features.csv`, `unit_type_features.csv`. Scopes: `development` \| `apartment` \| `house` \| `community`.
