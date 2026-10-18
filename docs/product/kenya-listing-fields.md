---
title: Kenya listing fields (Zoopla-adapted)
source: zoopla-listing-fields-source.md
adapted: 2026-10-17
focus: developments / off-plan / under-construction (inventory_class off_plan|building)
currency_default: KES (USD when developer-primary)
---

# Kenya listing fields

Minor adaptation of [Zoopla listing fields](zoopla-listing-fields-source.md) for a **Kenya developments / off-plan** product (Rightmove/Zoopla-class north star). Keep Zoopla’s group structure; note each rename/drop/add briefly.

**Product scope:** development pages + (later) unit/ad cards for `off_plan` / `building`. Ready/resale may reuse the same shape but stay **store-only** for research ([portal-inventory-class-research-rules.md](../discovery/portal-inventory-class-research-rules.md)).

**Change legend:** **=** same · **→** rename · **↓** drop / low priority · **+** Kenya add · **~** soften / optional

Columns: field · type · example · notes (incl. change)

---

## Identity and classification

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| listingId | string | lst-… / portal id | **=** Primary key for a **unit/ad** snapshot (`listing.id`). Development master uses `property.id` / `external_id`. |
| propertyId | string | prop-libra-residences | **+** Master development FK (Zoopla often conflates listing↔property via UPRN). |
| listingRevisionUuid | uuid | — | **~** Optional; use `last_seen_at` / research_pass until we version ads. |
| section | enum | new-homes | **→** Prefer `inventory_class`: `off_plan` \| `building` \| `ready` \| `resale`. Map Zoopla `new-homes` → off_plan/building; `for-sale` resale → `resale`/`ready`. |
| listingStatus | enum | for_sale | **→** Our `listing.status`: active \| sold \| withdrawn \| stale \| unknown. |
| listingsCategory | enum | residential | **=** residential / commercial (commercial out of v1 research). |
| listingCondition | enum | new-build | **→** Soft synonym of inventory_class + status_label (UC vs off-plan). |
| memberType | enum | developer \| agent | **=** Who published the ad; developer sales office vs agency. |
| title | string | 3 bed apartment in Kilimani | **=** Generated: beds + type + place. |
| displayAddress | string | George Padmore Road, Kilimani | **→** Partial public address — **no** UK postcode; neighbourhood + street when known. |
| metaTitle / metaDescription | string | — | **=** SEO, generated. |
| detailedDescription | html/md | — | **=** Agent/developer long copy (claim / source extract). |
| summaryDescription | string | — | **=** Card teaser. |
| propertyType | enum | apartment | **→** Kenya: apartment, maisonette, townhouse, villa, penthouse, studio, mixed… (not UK terrace/semi_detached as default). |
| developmentName | string | Libra Residences | **+** First-class for new-build (Zoopla embeds in address). |
| inventoryClass | enum | building | **+** Locked portal/research class. |

---

## Pricing

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| pricing.internalValue | number | 17000000 | **=** Numeric; **never** force a single portal scalar when claims conflict. |
| pricing.label | string | KES 17M – 25M | **→** £ → **KES** (or **USD** when developer-primary, e.g. CANTO). |
| pricing.currencyCode | ISO 4217 | KES | **→** GBP → **KES** default; USD allowed. |
| pricing.qualifier | enum | from_price \| fixed \| guide \| POA | **=** “From”, fixed, POA common on Kenya off-plan. |
| pricing.isAuction | bool | false | **↓** Rare for our corpus; keep optional. |
| pricing.rentFrequencyLabel | string | pcm | **↓** Rent surface deferred (developments/sale first). |
| pricing.alternateRentFrequencyPrice | object | — | **↓** Rent-only. |
| pricing.pricePerFloorAreaUnit | string? | KES/sqm | **→** Prefer **KES/sqm** (Kenya dossiers use sqm); £/sq ft optional secondary. |
| pricing.originalCurrencyPrice | object? | USD band | **=** Useful when KES+USD both published. |
| priceMin / priceMax | number | — | **~** Ad-targeting band; store only if sourced. |
| shortPriceTitle | string | from 17M | **=** Compact card label. |
| priceDrop.* | object | — | **~** Less common on off-plan developments; keep for unit ads later. |
| derived.buyerIncentives | object? | 0% interest / 4-year | **=** High value for Kenya new-build (payment promotions). |
| priceClaims\[\] | array | multi rows | **+** Locked: always multi `price_observation` — Zoopla single price insufficient. |
| paymentPlan | object | 20% deposit… | **+** Kenya-critical (deposit %, tenor, reservation fee) — not a Zoopla core sale field. |

---

## Location

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| location.coordinates.latitude / longitude | float | −1.2944 / 36.7789 | **=** Prefer developer/NEMA/Maps CTA; else `geo_pin` + NV. |
| location.outcode / incode / postalArea | string | — | **↓** UK postcode. **→** Use `county` / `city` / `neighbourhood` / `street`. |
| postTownName | string | Nairobi | **→** `city` (`geo_place`). |
| areaName / countyAreaName | string | Kilimani | **→** `neighbourhood` (+ optional county e.g. Kiambu, Kwale). |
| regionName | string | Nairobi metro | **~** Soft region / coast / Rift. |
| countryCode | string | ke | **→** gb → **ke**. |
| nearestStations | string\[\] | — | **→** **Nearest transit / landmarks** (matatu hubs rare as structured; malls, CBD, airport via `poi` / `property_poi`). |
| transports | array | — | **→** Same as POI distances (walk/drive). |
| googleStreetView | object | — | **~** Optional; sparse for UC towers. |
| staticMaps\[\] | array | — | **=** Pre-rendered map assets. |
| masterPlannedCommunity | string | Tatu City | **+** Kenya SEZ / master-plan FK. |

---

## Property attributes

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| counts.numBedrooms | int / range | 3 or bedsMin–Max | **=** Also bedsMin/Max for development cards. |
| counts.numBathrooms | int | 3 | **=** Capture when published (often missing today). |
| counts.numLivingRooms | int | — | **~** UK “receptions”; Kenya agents rarely count these — optional. |
| floorArea / sizeSqm | number | 193 | **→** Prefer **sqm**; keep sq ft only as synonym/convert. |
| sizeSource | enum | developer_plans \| brochure \| agent \| eia | **→** Drop `comparables_epc`; use our publisher/geo_method-style provenance. |
| tenure | enum | freehold \| leasehold \| sectional_title | **→** Same legal idea; Kenya **sectional title** common for apartments. Capture when developer/FAQ states it. |
| epc.* / derivedEPC | A–G | — | **↓** UK EPC. **~** Optional Kenya energy/green claims if sourced (rare). |
| hasEpc / hasFloorplan | bool | — | **→** `hasFloorplan` keep; `hasEpc` → optional `hasEnergyInfo`. |
| chainFree | bool | — | **↓** UK chain culture; N/A for off-plan primary sales. |
| isRetirementHome | bool | — | **↓** Rare; optional tag. |
| isSharedOwnership | bool | — | **↓** UK shared ownership; not Kenya default. |
| furnishedState | enum | — | **↓** Rent-first; rare on off-plan sale. |
| hasDsq / hasStudy | bool | true | **+** Kenya typology flags (already in `unit_type`). |
| storeys / totalUnits / blocks | int | 20 / 119 / 2 | **+** Development specs (always claim-set; often NDI). |
| completionEstimate | string/date | Q4 2027 | **+** Handover / completion window. |
| constructionProgress | object | 58% | **+** Candidate field when developer/agent publishes. |

---

## Features and tags

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| features.bullets\[\] | string\[\] | — | **=** Free-text agent bullets → normalize via taxonomy. |
| features.highlights\[\] | chips | Gym, Pool, CCTV | **→** Prefer controlled `feature` slugs (generator, borehole, DSQ, CCTV…). |
| smartTags\[\] / tagsV2\[\] | tags | — | **=** Filter facets after coverage gate. |
| flag | string? | Off-plan / UC | **→** Align with inventory_class / statusSummary. |

---

## Media

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| propertyImage\[\] | array | — | **=** Gallery images (`media_asset` / `property_media`). |
| numImages | int | — | **=** |
| floorPlan.image\[\] / pdf | array | — | **=** High value for unit types. |
| embeddedContent.videos / tours | arrays | — | **=** Progress / walkthrough video. |
| additionalLinks\[\] | brochure, LOO | — | **=** Brochure PDF, payment schedule, EIA. |

---

## Agent and branch

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| branchId / branchName | id, string | — | **→** Our `agent` (agency/portal brand). |
| brandName | string | — | **=** Trading brand. |
| companyId / groupId | id | — | **→** Optional `group_company` only when proven. |
| logoUrl | url | — | **=** |
| redirectPhone | string | +254… | **→** Tracked number optional; **never** invent; **never** Hauzisha `0730 731 355` as developer. |
| isDeveloper | bool | true | **=** Developer sales vs agency. |
| analyticsEcommerce.variant | enum | — | **~** Ad package tier — Plus/ops later. |
| agentPerson | object | first/last | **+** Named salesperson (`agent_person`) when evidenced — do not invent. |
| developer | object | GLBC Group | **+** First-class `developer` + co_developer / marketing_partner graph. |

---

## Status, dates and history

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| publishedOn | datetime | — | **=** First listed / first_seen. |
| priceHistory.priceChanges\[\] | array | — | **~** Unit-ad later; rare on development “from” prices. |
| statusSummary.label | string | Under construction | **→** UC / Off-plan / Selling / Coming soon (→ off_plan). |
| underOffer | bool | — | **~** Unit reservation / sold-out typology flags. |
| availableFrom | date? | — | **↓** Rent; for sale use completionEstimate. |
| zindex | int | — | **↓** Zoopla area index — replace later with Kenya comps/PSF skill. |
| lastVerifiedAt | date | 2026-10-17 | **+** Research hygiene. |

---

## Key information (material facts) — Kenya NTS analog

Zoopla NTS keys → Kenya off-plan material block. Unfilled = “Ask developer/agent” / not available.

| key | Applies to | Kenya notes |
| --- | --- | --- |
| tenure | sale / new-build | **→** Freehold / leasehold / **sectional title**; lease length if leasehold. |
| council_tax_band | — | **↓** UK. **→** Optional **land rates / county rates / NMS** only if developer or county source states them (rare on marketing sites). |
| deposit | sale instalment | **→** Off-plan **payment deposit %** (+ reservation fee) — first-class, not rent-only. |
| letting_arrangements | rent | **↓** Rent deferred. |
| water | utilities | **→** Borehole / county water / water storage (often amenity chips). |
| heating | utilities | **↓** Rare; solar water heating as amenity when sourced. |
| electricity | utilities | **→** Grid + **backup generator** (Kenya staple). |
| sewerage | utilities | **~** Seldom marketed; capture if EIA/brochure states. |
| broadband / mobile_coverage | connectivity | **~** Optional; fibre marketing claims NV unless evidenced. |
| parking | amenities | **=** Already feature + bay counts when typed. |
| stamp_duty / transfer_taxes | buyer costs | **+** Soft: mention only if developer publishes buyer-cost guide — do not invent KRA schedules into listings. |
| service_charge / service_charge_est | ongoing | **+** Capture when brochure/FAQ states monthly/annual service charge. |

---

## Rent and new-build differences (Kenya lens)

| Area | Resale / Ready unit ad | Rent (deferred) | New build / UC development |
| --- | --- | --- | --- |
| section / class | ready / resale | to-rent (later) | off_plan / building |
| price | Unit list price | pcm | Multi `price_claims` + from-band; payment plan |
| material keys | tenure, rates? | deposit, furnished | tenure, deposit%, completion, service charge |
| unique | chain N/A | furnishedState | developmentName, bedsMin/Max, incentives, progress |
| EPC / Street View | rare | — | rare / optional |

---

## Search-card payload (development or unit card)

Smaller object for SERP / map pins.

| Field | Notes |
| --- | --- |
| listingId / propertyId, uris | Detail URL set |
| title, displayAddress, propertyType / developmentName | **→** Kenya place hierarchy |
| price label + currency | KES/USD; prefer “from” / band; no silent NDI winner |
| inventoryClass, statusSummary | Off-plan / Building chip |
| features / highlights | Taxonomy chips |
| sizeSqm, beds (min–max) | From canonical unit_types when agreed |
| numberOfImages / FloorPlans / Videos | Media counts |
| lat, lng | Only conf-gated pins |
| publishedOn / lastVerifiedAt | |
| branch / developer CTA | Public = developer/project phone; Plus = full agent graph |
| isFavourite, underOffer, flag | |

---

## Sold-price / property history (deferred)

Zoopla UPRN + HM Land Registry **↓** for v1 Kenya off-plan. Future: Kenya land registry / stamp duty history if product expands to Ready comps — **not** a research-queue requirement now.

---

## Flat model (normalised)

| Group | Columns |
| --- | --- |
| core | listing_id, property_id, section→inventory_class, status, category, member_type, title, display_address, development_name, description, summary, published_at, last_verified_at |
| price | price_claims\[\], currency (KES\|USD), qualifier, buyer_incentives, payment_plan (deposit, tenor, reservation) |
| place | lat, lng, city, neighbourhood, street, county, country=KE, master_community, pois\[\] (name, type, distance) |
| property | property_type, beds, baths, size_sqm, size_source, tenure, has_dsq, has_study, storeys, units, completion, progress |
| content | features\[\], highlights\[\], images\[\], floorplans\[\], videos\[\], documents\[\] |
| material_info | tenure, deposit_pct, service_charge, water/power notes, parking, rates/NMS (rare), stamp_duty_note (only if sourced) |
| parties | developer, co_developers, marketing_partners, branch/agent, agent_person, phones (ownership-tagged) |

---

## Adaptation summary (minor changes only)

| Zoopla | Kenya adaptation |
| --- | --- |
| £ / GBP | **KES** (USD when developer-primary) |
| Postcode outcode/incode | **County / city / neighbourhood / street** |
| Council tax | **↓** → optional land rates / NMS if sourced |
| EPC | **↓** optional / rare |
| Chain-free, shared ownership, UK house types | **↓** or remap |
| nearestStations | **POI** (mall, transit, airport, CBD) |
| Single listing price | **+** multi price claims + **payment plan** |
| UPRN sold history | **↓** deferred |
| Receptions | **~** optional |
| — | **+** DSQ, borehole, generator, inventory_class, developer graph, completion/progress |
