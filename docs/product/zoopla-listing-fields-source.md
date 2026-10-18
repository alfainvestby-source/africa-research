zoopla.co.uk · field names read from live listing payloads, 18 Oct 2026

# Zoopla listing fields

The data fields behind a Zoopla listing: what the detail page payload carries, what the search card carries, and where rent and new-build listings differ. Field names are Zoopla's own, taken from the page data; sample values come from three live listings (a £4.275m sale, a £1,550 pcm rent, a £385k new build).

[Identity](#id)[Pricing](#price)[Location](#loc)[Property](#phys)[Features](#feat)[Media](#media)[Agent](#branch)[Status & history](#status)[Key information](#nts)[Rent / new build](#diff)[Search card](#serp)[Sold & property page](#uprn)[Flat model](#model)

Columns: field · type · example · meaning

## Identity and classification

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| listingId | string / int | 71743212 | Primary key; 8 digits; used in `/details/{id}/` |
| listingRevisionUuid | uuid | 05D7F6BC-C62E-… | Version of the listing record |
| section | enum | for-sale | for-sale · to-rent · new-homes |
| listingStatus | enum | for_sale | for_sale · to_rent |
| listingsCategory / category | enum | residential | residential or commercial |
| listingCondition | enum | pre-owned | pre-owned or new-build |
| memberType | enum | agent | Who listed it (agent, developer, landlord) |
| title | string | 6 bed property for sale | Generated: beds + type + intent |
| displayAddress | string | West Heath Gardens, Hampstead NW3 | Partial public address, no house number |
| metaTitle / metaDescription | string | …, £4,275,000 - Zoopla | SEO fields, generated from the above |
| detailedDescription | html | \<br>-separated text | Agent's full description |
| summaryDescription | string | Rare to the local market… | Truncated teaser (search card) |
| propertyType | enum | town_house | Snake-case type: flat, terraced, semi_detached, detached, town_house, bungalow…; null on some listings |

## Pricing

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| pricing.internalValue | number | 4275000 | Numeric price; pcm figure for rent |
| pricing.label | string | £4,275,000 / £1,550 pcm | Display string |
| pricing.currencyCode | ISO 4217 | GBP |  |
| pricing.qualifier | enum | fixed_price | Plus priceQualifierLabel ("Fixed price"). Others: guide price, offers over, POA |
| pricing.isAuction | bool | false |  |
| pricing.rentFrequencyLabel | string | pcm | Rent only |
| pricing.alternateRentFrequencyPrice | object | {internalValue 358, label "£358 pw"} | Rent shown per week as well |
| pricing.pricePerFloorAreaUnit | string? | null | £/sq ft, when floor area is known |
| pricing.originalCurrencyPrice | object? | null | Overseas listings |
| priceMin / priceMax | number | 4250000 / 4500000 | Ad-targeting price band (about ±5%) |
| shortPriceTitle | string | £800k | Compact label (search) |
| priceDrop.percentageChangeLabel | string | 5.9 | Search card: % reduction |
| priceDrop.lastPriceChangeDate | string | Last reduced: 12th Oct 2026 |  |
| derived.buyerIncentives | object? | null | Developer incentives (new builds) |

## Location

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| location.coordinates.latitude / longitude | float | 51.563179 / -0.194878 | Pin position, 6 decimals |
| pos.lat / pos.lng | float | 51.4916 / -0.0188 | Same, in the search card |
| location.outcode / outcode | string | NW3 | Postcode district |
| incode | string | 7TR | Postcode sector and unit tail, exposed in ad targeting |
| postalArea | string | NW |  |
| postTownName | string | London |  |
| areaName / location | string | London |  |
| countyAreaName | string | London |  |
| regionName / location.region | string | London |  |
| countryCode | string | gb |  |
| nearestStations | string\[30\] | Golders Green | Station names with `nearestStationsInMiles` (e.g. 0.6) in parallel arrays |
| transports | array | — | Search card: nearest transport with distance |
| googleStreetView | object | {coordinates, heading 0, pitch 10} | Null on rent and new-build samples |
| staticMaps\[\] | array | {width 400, height 200, deviceWidth, src} | Pre-rendered map images per breakpoint |

## Property attributes

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| counts.numBedrooms (numBeds) | int | 6 | Also bedsMin / bedsMax for developments |
| counts.numBathrooms (numBaths) | int | 5 |  |
| counts.numLivingRooms (numRecepts) | int | 3 | Receptions |
| floorArea | object? | null | Agent-supplied size, often empty |
| ingested.sizeSqft | int | 4036 | Derived size when the agent gives none |
| ingested.sizeSource | enum | comparables_epc | Provenance of the derived size |
| tenure (ntsInfo key) | enum | freehold | freehold, leasehold, share of freehold |
| epc.image\[\] / epc.pdf | array | {caption, filename} | EPC chart image |
| derivedEPC.efficiencyRating / epcRating | A–G | C | Null for rent and new-build samples |
| hasEpc / hasFloorplan | bool | true |  |
| chainFree | bool | false |  |
| isRetirementHome | bool | false |  |
| isSharedOwnership / sharedOwnership | bool | false |  |
| furnishedState | enum | furnished | Rent only |

## Features and tags

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| features.bullets\[\] | string\[\] | Detached, Carriage Driveway, Golders Hill Park | Agent's key features, free text |
| features.highlights\[\] | {label, description} | Good Transport Links, Garage | Zoopla-derived chips on the card |
| propertyHighlight | string | Good Transport Links\|Garage | Pipe-joined highlights |
| smartTags\[\] | string\[\] | attributes.garden | Machine tags used for feature landing pages (houses with garden, etc.) |
| tagsV2\[\] | {label} | Freehold | Badges on the card |
| flag | string? | — | Card flag |

## Media

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| propertyImage\[\] | {caption, filename} | 3d04f8bb…jpg | Hash filename; the CDN path sets the size (`lid.zoocdn.com/u/480/360/{filename}`) |
| numImages / numberOfImages | int | 13 |  |
| floorPlan.image\[\] / floorPlan.pdf | array | {caption, filename} | numberOfFloorPlans on the card |
| embeddedContent.videos / tours / links | arrays | null | Video, virtual tour, external links; numberOfVideos on the card |
| additionalLinks\[\] | {caption, original, type, url} | — | Brochure and other documents |
| image / gallery | object | — | Card image set |

## Agent and branch

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| branchV2.branchId (branchId) | int | 12680 | Branch key; also in the profile URL |
| branchV2.branchName | string | TK International |  |
| brandName | string | TK (Hampstead) Ltd | Legal or trading brand |
| companyId / groupId | int / null | 6048 / null | Parent company, agent group |
| branchV2.branchDetailsUri | path | /find-agents/branch/tk-international-london-12680/ |  |
| branchV2.logoUrl (branchLogoUrl) | url | st.zoocdn.com/… |  |
| branchV2.redirectPhone | string | 020 3478 … | Tracked call-forwarding number; separate lettings and commercial variants |
| branchV2.isDeveloper | bool | false |  |
| analyticsEcommerce.variant | enum | premium plus | Agent's advert package tier; `displayType`, `isPremium`, `featuredType` (weekly_featured) on the card |

## Status, dates and history

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| publishedOn | ISO datetime | 2025-11-06T16:21:24 | "Listed on 6th Nov 2025"; card shows a formatted string |
| priceHistory.priceChanges\[\] | {priceChangeDate, isPriceDrop} | 2026-05-18, true | Drives the "Reduced on 18/05/2026" badge. The amounts are not exposed. |
| statusSummary.label | string | Just added | Also Under offer, Sold STC style labels |
| underOffer | bool | false |  |
| availableFrom | date? | null | Rent availability |
| zindex | int | 2669162 | Zoopla's internal area price index value used for targeting |

## Key information (NTS) block

A key/title/value/description array. It follows the National Trading Standards material information rules, so the same keys appear across listings. Unfilled values read "Ask agent" or "Not available".

| key | Applies to | Example value | Notes |
| --- | --- | --- | --- |
| tenure | sale | Freehold | Leasehold listings add lease length and charges |
| council_tax_band | all | Not available |  |
| deposit | rent | £500 |  |
| letting_arrangements | rent | Not available |  |
| water | additionalNtsInfo | Ask agent | Utilities group |
| heating | additionalNtsInfo | Ask agent |  |
| electricity | additionalNtsInfo | Ask agent |  |
| sewerage | additionalNtsInfo | Ask agent |  |
| broadband / broadband_speed | additionalNtsInfo | Ask agent | Links to Ofcom checker |
| mobile_coverage | additionalNtsInfo | Ask agent | Links to Ofcom checker |
| parking | additionalNtsInfo | Ask agent |  |

## Rent and new-build differences

The same record shape is used for all three sections, so differences are mostly values.

| Area | Sale | Rent | New build |
| --- | --- | --- | --- |
| section | for-sale | to-rent | new-homes |
| price | Total price | pcm plus weekly equivalent | Total price, incentives in `derived.buyerIncentives` |
| nts keys | tenure, council tax | deposit, letting arrangements, council tax | tenure, council tax |
| unique fields | EPC, street view | furnishedState, availableFrom, administrationFees (null here) | Development name in address, bedsMin/Max, listingCondition new-build |
| EPC / Street View | present | null | null |
| status label | Reduced | — | Just added |

## Search-card payload

The smaller object each result carries on area pages (25 per page). It excludes description, key information, EPC and branch phone.

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| listingId, listingUris | string, object | 73570227 | Detail URL set |
| title, address, propertyType | string | 3 bed town house for sale |  |
| price, priceUnformatted, priceCurrency | string, number | £800,000 / 800000 / GBP |  |
| priceDrop | object | 5.9%, 12 Oct 2026 |  |
| features, highlights, tags | arrays | — |  |
| sizeSqft, sizeSource | int, enum | 1108, comparables_epc |  |
| numberOfImages / FloorPlans / Videos | int | 15 / 1 / 0 |  |
| pos.lat, pos.lng | float | 51.4916, -0.0188 |  |
| publishedOn, publishedOnLabel | string | 28th Jun 2026, "Listed on" | Rent cards use availableFrom + availableFromLabel |
| listingType, featuredType, displayType, isPremium | enum | featured, weekly_featured, premium_plus, true | Paid placement |
| branch, transports, gallery, image | refs | — |  |
| isFavourite, underOffer, flag | bool / string | false | User state and badges |

## Sold-price and property page fields

From `/property/uprn/{uprn}/`, read from the rendered page (the data is not exposed as structured JSON).

| Field | Type | Example | Notes |
| --- | --- | --- | --- |
| uprn | id | (in URL) | Unique Property Reference Number |
| address | string | 60 Devonshire Road, Harrow, HA1 4LR | Full address with number and postcode |
| property type, beds, baths, receptions | mixed | Terrace, 4, 2, 2 |  |
| tenure, floor area | string, sqm | Freehold, 112 sqm |  |
| estimate low / mid / high | GBP | £330k / £350k / £370k | Zoopla estimate range; mid-point hidden until "Reveal" |
| sales\[\]: date, price, change £, change % | array | Aug 2026, £750,000, +£405,000 (117%) | HM Land Registry sale history |
| current status | enum | For sale | Link to a live listing |
| insights | gated | crime, flood, planning | Visible after sign-in |

## Flat model of one listing

A normalised version if you want to store the same information.

| Group | Columns |
| --- | --- |
| core | listing_id, section, status, category, condition, member_type, title, display_address, description_html, summary, published_at, updated_at |
| price | price, currency, qualifier, rent_frequency, price_weekly, is_auction, price_changes\[\] (date, is_drop) |
| place | lat, lng, outcode, incode, post_town, county, region, country, nearest_stations\[\] (name, miles) |
| property | property_type, beds, baths, receptions, size_sqft, size_source, tenure, epc_rating, chain_free, retirement, shared_ownership, furnished |
| content | features\[\], highlights\[\], smart_tags\[\], images\[\] (filename, caption), floorplans\[\], videos\[\], tours\[\], documents\[\] |
| material_info | council_tax_band, deposit, letting_arrangements, water, heating, electricity, sewerage, broadband, broadband_speed, mobile_coverage, parking |
| agent | branch_id, branch_name, brand_name, company_id, group_id, logo_url, phone, is_developer, ad_package |

Coverage note: values were checked on three listings. Fields that were null or empty there (floorArea, embedded videos and tours, administrationFees, availableFrom, priceQualifier on other listings) will be populated on other listings. Leasehold terms, auction and shared-ownership fields were not seen populated.