# Selected claims (high-value extract)

Not an exhaustive dump — every dossier field remains authoritative in `docs/projects/`.  
**NV** = `needs_verification` · **NDI** = `needs_developer_input`

## Pandora Residences

| field_key | role | value | conf | NV | NDI | notes |
|-----------|------|-------|-----:|:--:|:--:|-------|
| canonical_name | canonical | Pandora Residences | 5 | | | Developer |
| geography.neighbourhood_street | canonical | Westlands — Muthangari Drive opposite The Address | 5 | | | |
| primary_developer_id | canonical | dev-a-one-corporation | 5 | | | |
| size_by_type.brochure | canonical | 3BR 152.68; 4BR 194.32; 5BR 291.21 sqm | 5 | | | |
| unit_types.mix | claim_set | 2/3/4 BR vs 3/4/5 BR | 2 | | ✓ | Official vs official — no canonical |
| amenities.core | canonical | Pool spa fitness co-working lounge retail … | 5 | | | |
| payment_plan.deposit | secondary must-have | 20% | 3 | | | ≥4 agents; conf≤3 |
| completion_estimate | secondary | December 2028 | 4 | | | |
| inventory.2BR_sold_out | secondary | Contested sold-out | 2 | ✓ | | |
| building_specs.floors | secondary | 17 | 2 | ✓ | | Property Box only |
| currency | canonical | KES | 5 | | | |

## Astra Bay Residence

| field_key | role | value | conf | NV | NDI | notes |
|-----------|------|-------|-----:|:--:|:--:|-------|
| canonical_name | canonical | Astra Bay Residence | 5 | | | |
| geography.neighbourhood | canonical | Lower Kabete — Lower Kabete Road | 5 | | | |
| geography.county | secondary | Nairobi vs Kiambu | 2 | ✓ | | |
| primary_developer_id | canonical | dev-wimax-homes | 5 | | | |
| unit_types | canonical | Studio + 1BR layouts | 5 | | | |
| unit_types.agent_2br | secondary | 2BR / loft / courtyard | ≤3 | ✓ | | Not on developer |
| amenities.core | canonical | Gym CCTV lifts + flyer | 5 | | | |
| amenities.agent_adds | secondary | Retail/solar/pool adds | 1–2 | ✓ | | |
| payment_plan.deposit | secondary must-have | 20% | 3 | | | Agent-only conf≤3 |
| completion_estimate | secondary | Q2 2027 majority; Q3 outlier | 3 | Q3✓ | | |
| geography.lat_lng | secondary | CSV GPS | 2 | ✓ | | Not on property row |

## Porini Point

| field_key | role | value | conf | NV | NDI | notes |
|-----------|------|-------|-----:|:--:|:--:|-------|
| canonical_name | canonical | Porini Point | 5 | | | |
| geography.master_planned_community | canonical | Tatu City | 5 | | | |
| primary_developer_id | canonical | dev-rendeavour | 5 | | | |
| co_developer | dual link | dev-tatu-city-limited + rp-tatu-city-limited | 4 | | | Both M2M and RelatedParty |
| unit_types | canonical | 1 / 2 / 3 BR | 5 | | | |
| unit_count | canonical | 570 | 5 | | | |
| block_count | canonical | 24 | 5 | | | |
| built_up_area_sqm | canonical | ~58000 | 5 | | | |
| size_by_type | canonical | 54 / 90 / 145 Total area | 5 | | | |
| price_claims (official) | multi | 7.61M vs 7.5M (+ tables) | ≤5 | | ✓ | **No** public price_from |
| payment_plan.tenor | canonical | 24 months | 5 | | | Developer |
| payment_plan.tenor.alt | alternate official | up to 3 years | 4 | | ✓ | Pack vs launch |
| payment_plan.deposit | secondary | FAQ 10% / Block ~20% | 1–2 | ✓ | | No live FAQ |
| completion_estimate | canonical | Q1 2027 / Sep 2029 | 5 | | | |
| amenities.core | canonical | Clubhouse gym pool BBQ … | 5 | | | |
| building_specs.floors | secondary | G+4 | 2 | ✓ | | |

## Galaxy One

| field_key | role | value | conf | NV | NDI | notes |
|-----------|------|-------|-----:|:--:|:--:|-------|
| canonical_name | canonical | Galaxy ONE | 5 | | | |
| geography.neighbourhood_street | canonical | 147 Rhapta Road | 5 | | | |
| geography.lat_lng | canonical | −1.2635, 36.8029 | 5 | | | JSON-LD |
| primary_developer_id | canonical | dev-lionston-real-estate | 5 | | | |
| unit_types | canonical | 1 / 2 / 3 BR | 5 | | | |
| size_by_type | canonical | 57–60 / 82–91 / 142 bands | 5 | | | |
| total_units | claim_set | 210 vs 266 | 2 | | ✓ | No canonical |
| storeys | claim_set | 30 vs 19 | 2 | 30✓ | ✓ | No canonical |
| payment_plan.deposit | canonical | 10% | 5 | | | Developer |
| payment_plan.deposit.agents | secondary | 20% | 3 | ✓ | | ≥4 agents |
| price_claims (official) | multi | Lionston vs FAQ bands | ≤3 | | ✓ | **No** public price_from |
| completion_estimate | canonical | Late 2027 | 5 | | | |
| amenities.core | canonical | Infinity pool Sky Club … | 5 | | | |
| construction_progress | claim_set candidate | 63% vs 42% | 3 | | ✓ | Do not average |
| availability_claim | secondary | 33 of 84 | 2 | ✓ | | |
