# Claim conflicts (explicit)

Resolution follows [decisions.md](../../decisions.md).  
**NDI** = `needs_developer_input` (official vs official — no winner).  
**NV** = `needs_verification` (agent-only / low-conf / uncorroborated).

## Pandora Residences (NBO-002)

| # | field_key | Claims | Flags | Resolution |
|--:|-----------|--------|-------|------------|
| 1 | `unit_types` | Site/brochure 2/3/4 BR vs brochure 3/4/5 BR | **NDI** | Official vs official — no canonical mix |
| 2 | `size_by_type` | Brochure vs agent sizes | — | Canonical = brochure; agents secondary |
| 3 | `price_from` | Multi agent bands; no developer | NV on outliers | Multi `price_observation`; no developer conflict |
| 4 | `inventory.2BR_sold_out` | Contested | **NV** | Show all |
| 5 | floors / tenure | Property Box only | **NV** | Secondary |
| 6 | completion | Multi-agent Dec 2028 | — | Conf 4; not developer-canonical |

## Astra Bay Residence (NBO-005)

| # | field_key | Claims | Flags | Resolution |
|--:|-----------|--------|-------|------------|
| 1 | Related brand | Laureland | — | `marketing_partner` only |
| 2 | `unit_types` | Agent 2BR/loft vs Wimax studio+1BR | **NV** | Canonical = Wimax |
| 3 | size measure | plinth vs gross | — | Tagged developer table |
| 4 | prices | Agent bands; no developer list | **NV** on 2BR ceilings | Multi observations |
| 5 | completion / status / county | Divergent | **NV** outliers | Claim sets |

## Porini Point (NBO-004)

| # | field_key | Claims | Flags | Resolution |
|--:|-----------|--------|-------|------------|
| 1 | Official price bands | Live 7.61M vs press 7.5M (+ pack/info tables) | **NDI** | **No** public `price_from`; keep multi rows |
| 2 | Agent price lows | Vorsa/Craiova/Ladva / pack 5.9M | **NV** | Secondary |
| 3 | payment tenor | 24-mo vs pack up to 3 years | **NDI** (official vs official) | Canonical = 24-mo (launch denser); keep alternate pack claim |
| 4 | deposit % | FAQ-index 10% vs Block ~20% | **NV** | No live developer deposit |
| 5 | completion | Launch vs Craiova | — | Canonical = launch |
| 6 | inventory sold-out | Launch-night vs available homes | **NV** current | Show launch claim |
| 7 | G+4 floors | Block + FAQ index | **NV** | |
| 8 | Tatu City Limited | Co-named Developers | — | **Both** `property_developer(co_developer)` and RelatedParty |

## Galaxy One (NBO-013)

| # | field_key | Claims | Flags | Resolution |
|--:|-----------|--------|-------|------------|
| 1 | `total_units` | 210 vs 266 | **NDI** | No canonical |
| 2 | `storeys` | 30 (indexed) vs 19 | **NDI** (+ NV on 30 SPA) | No canonical |
| 3 | deposit | 10% developer vs 20% agents | — | Canonical = 10%; 20% secondary |
| 4 | prices | Lionston vs FAQ official bands | **NDI** | **No** public `price_from`; multi rows |
| 5 | completion | late 2027 vs agents | — | Canonical framing = late 2027 |
| 6 | `construction_progress` | 63% vs 42% | **NDI** | Candidate field; do not average |
