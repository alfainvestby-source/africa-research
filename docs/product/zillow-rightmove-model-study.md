---
title: Zillow + Rightmove inventory model study
date: 2026-10-17
accessed: 2026-10-17
status: research (no product lock)
inputs:
  - zoopla-kenya-product-decisions.md (#1 LOCKED; #2 lean 2B)
  - kenya-listing-fields.md
  - zoopla-kenya-gap-eval.md
  - goal-and-approach.md
  - db/schema.md (property vs listing grain)
honesty: Partner APIs (Bridge MLS, Rightmove RTDF/ADF, Data Services) are gated — summaries use public docs/help only; no invented API fields.
---

# Zillow + Rightmove model study vs Kenya off-plan master data

Compares how **Zillow (USA)** and **Rightmove (UK)** structure listings / search / new-homes products (from official APIs, developer docs, and public help) to **our** development-first + typology-listing approach.

Related: [zoopla-kenya-product-decisions.md](zoopla-kenya-product-decisions.md) · [kenya-listing-fields.md](kenya-listing-fields.md) · [schema.md](../db/schema.md) · [surface-map.md](surface-map.md) · [goal-and-approach.md](../goal-and-approach.md)

**Accessed:** 2026-10-17 (all URLs below).

---

## Paywall / access honesty (read first)

| Source | Public? | What we used |
|--------|---------|--------------|
| **Bridge Interactive** (Zillow Group) | Partner / MLS-approved. Dashboard signup + data-provider approval; Zillow Group datasets need separate Zillow approval (docs cite 10+ business days). Marketing pages + docs site are readable; full field payloads vary by MLS license. | Public Bridge docs + explorer resource list; **not** a live MLS token. |
| **Zillow consumer / builder help** | Public help + builder marketing toolkit. | New Construction FAQ; Promoted Communities / Buyer Discovery pages. |
| **Rightmove RTDF / ADF** | **Partner-only write feeds.** Spec PDFs + ADF landing page are public; schemas/keystore/FTP need `adfsupport@rightmove.co.uk`. | Public RTDF PDF, New Homes ADF V4n PDF, adf.html. |
| **Rightmove Data Services / api-docs** | Sales / early-adopter — not a self-serve public inventory read API. | Property-data marketing page only. |
| **Rightmove Plus / customer FAQ** | Member help is mostly public articles. | New Homes Spotlight, Development Marketing, add-property FAQs; New Homes products PDFs. |

**No invented API fields.** Where a schema PDF lists a field name, we cite it; where only marketing describes a feature, we label it as product UX, not API.

---

## Zillow model summary

### Entities (API + product)

**Bridge / MLS path (resale-dominant inventory)**

Bridge documents three transports for MLS data: **RESO Web API**, **RETS**, **Bridge Web API**. MLS payloads are normalized toward the **RESO Data Dictionary**. Access is per-dataset and per feed type (IDX / VOW / BBO / etc.) at the MLS’s discretion ([Bridge using-APIs docs](https://bridgedataoutput.com/docs/platform/Dashboard/using-apis)).

Documented resource shapes:

| Layer | RESO Web API (examples in docs) | Bridge Web API |
|-------|----------------------------------|----------------|
| Listing / property offer | `Property` (+ optional `Rooms`, `UnitTypes` on some MLSs) | `/listings`, `/listings/{id}` |
| Agent | `Member` | `/agents` |
| Brokerage office | `Office` | `/offices` |
| Open house | `OpenHouse` | `/openhouses` |
| Lookups / media | `Lookup`, Media (RESO) | (via listing payloads) |

Documented queryable listing attributes in examples include `ListingId`, `ListPrice`, `StandardStatus`, `PropertyType`, `PostalCode`, `City`, `BedroomsTotal`, `BathroomsTotalDecimal`, `LivingArea`, `YearBuilt`, `Coordinates`, `UnparsedAddress`, `ClosePrice` / `CloseDate` (sold), etc. — **field availability depends on MLS license**, not a single global Zillow schema ([RETS/OData examples](https://www.bridgedataoutput.com/docs/platform/API/rets); [using-APIs](https://bridgedataoutput.com/docs/platform/Dashboard/using-apis)).

**Zillow Group datasets on Bridge** (separate approval; not the same as MLS IDX):

| Dataset | Documented entities |
|---------|---------------------|
| Public Records | `parcels`, `assessments`, `transactions` (~148M properties / 3,200 US counties cited) |
| Zestimates | Property + rental Zestimates by address or ZPID |
| Econ Data | Programmatic access to metrics otherwise published as CSV on zillow.com/data |
| Agent Reviews | `Reviewees`, `Reviews` |

Sources: [Zillow Group Data docs](https://bridgedataoutput.com/docs/platform/API/zg-data), [Bridge API marketing](https://www.bridgeinteractive.com/developers/bridge-api/), [Zillow Group Data marketing](https://www.bridgeinteractive.com/developers/zillow-group-data/). Marketing page states Zillow data via Bridge is for **retrieve-and-display**, not local storage (Terms of Use); treat as **partner policy**, not a consumer feature.

**Consumer / builder product entities (new construction)** — not the same feed as MLS IDX:

| Entity (product language) | Role |
|---------------------------|------|
| **Community** | Dedicated Community Page: photos, amenities, available homes/lots, link to builder site |
| **Builder** | Builder Profile; Contact Builder lead form; lead routing controlled by builder |
| **Plan / floor plan** | Buildable plans + plan pricing (to-be-built) |
| **Spec / quick move-in home** | Finished or finishing inventory listed as homes |
| **Lot** | Lot Availability on map + listing: available / sold / reserved |
| **Resale listing** | MLS-powered “Agent Listings” tab |

Sources: [New Construction Listings FAQ](https://zillow.zendesk.com/hc/en-us/articles/203865940-New-Construction-Listings-FAQ) (updated Mar 2025); [Promoted Communities toolkit](https://www.zillow.com/new-construction-advertising/training/promoted-communities/); [Buyer Discovery](https://www.zillow.com/new-construction-advertising/buyer-discovery/).

### New construction vs resale

| | Resale (MLS) | New construction (Promoted Communities) |
|--|--------------|----------------------------------------|
| How it gets on Zillow | IDX / MLS feeds (Agent Listings tab) | Direct builder XML feed, New Home Feed entry tool, or Listing Connect (MLS ↔ Promoted Communities) |
| Search UX | Mixed with new homes; “new construction” filter for PC inventory | Same map/SERP alongside resale when promoted; rich community UX |
| Claim / agent profile | Agent-associated IDX listings | **Cannot be claimed** on site; leads route per builder designation; **do not** link to agent profiles |
| Aggregators | Normal MLS aggregation | FAQ: **No** — builders must use direct feed / New Home Feed (Listing Connect for MLS-published specs) |

Zillow explicitly frames new construction marketing as competing with **existing homes**, not only other builders ([Promoted Communities](https://www.zillow.com/new-construction-advertising/training/promoted-communities/)).

### Public vs agent-only (documented)

- **Agent Listings vs Other Listings:** FAQ states Agent Listings are IDX/MLS-only; non-IDX sources (including builder feeds not connected via Listing Connect) appear under **Other Listings** because of MLS rules ([FAQ](https://zillow.zendesk.com/hc/en-us/articles/203865940-New-Construction-Listings-FAQ)).
- **Promoted Communities:** builder-controlled lead routing; agents cannot claim those listings; agent email/phone only if builder designates them.
- **Bridge feed types:** IDX vs VOW vs other licenses change which records/fields you may use — enforced by MLS via Bridge (`FeedTypes`, `FieldRules`) ([using-APIs](https://bridgedataoutput.com/docs/platform/Dashboard/using-apis)).
- **Zillow Group data via Bridge:** partner approval + ToU; not a public freemium inventory API.

### Media, price, status, location (high level)

| Concern | Resale / Bridge MLS | New construction product |
|---------|---------------------|--------------------------|
| **Media** | RESO Media / listing photos (MLS-dependent) | Community + home images, floor plans, exterior options, 3D tours, video upload, Inline Community Preview overlays |
| **Price** | `ListPrice` (+ sold `ClosePrice` where licensed) | Plan pricing + lot pricing; incentives called out in marketing |
| **Status** | `StandardStatus` (e.g. Active / Closed in examples) | Lot inventory: available / sold / reserved; email alerts on availability |
| **Location** | Address fields, postal code, geo `Coordinates` / `near` | Community address + lot maps; driving directions on Community Page |

---

## Rightmove model summary

### Entities (API + product)

**There is no public read API for browsing UK residential inventory.** Documented interfaces are **authorized write / sync feeds** plus commercial Data Services.

#### 1) UK sales & lettings — Real Time Data Feed (RTDF)

Partner HTTPS JSON API for **feed providers** (keystore auth, Network ID). Documented calls ([RTDF spec PDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), Nov 2023):

| Call | Purpose |
|------|---------|
| `SendProperty` | Add/update UK property |
| `OverseasSendProperty` | Overseas branch properties |
| `RemoveProperty` | Remove |
| `GetBranchPropertyList` | Reconcile branch stock |
| Product calls | `AddPremiumListing`, `AddFeaturedProperty`, `RemoveFeaturedProperty` |
| Reporting | Branch/property performance; brand/branch/property emails |

Grain for resale/agent stock: **branch-scoped property listing** (Network → Branch → Channel sales|lettings → Property). Notable documented fields include `Agent_Ref`, `Property_Type`, `Status`, `New_Home` (boolean), address lines, **`Display_Address`** (public) vs full detailed address (**“only visible to the agent and not displayed on Rightmove’s website”**), lat/lng, `Price` + `Price_Qualifier`, bedrooms/bathrooms/receptions, tenure/service charge/council tax/utilities material fields, rooms, media URLs ([same PDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)).

Landing / process: [adf.html](https://www.rightmove.co.uk/adf.html).

#### 2) New Homes developers — ADF Version 4n (bulk XML + FTP)

Separate from RTDF. Developers upload a **complete** XML of developments + plots; Rightmove **creates property listings** from that data ([ADF V4n PDF](https://media.rightmove.co.uk/ps/pdf/guides/ADF_V4n_specification.pdf), Dec 2023).

Documented hierarchy (**plot_only** model — style_plot removed in recent versions):

```
developer
  └── developer-region
        └── development   (code, name, address, postcode, phone, email,
                           price-min / price-max, summary/description,
                           campaign, specification, directions,
                           shopping/leisure/education/transport/health,
                           opening-hours, media…)
              └── plot    (name-number, price, bedrooms, status,
                           style-name, property-type, features, rooms,
                           tenure, service charge, utilities, media…)
```

Important process rules from the same PDF:

- Upload for a development **replaces all** Rightmove listings for that development (full snapshot sync).
- New development codes trigger **semi-manual** account creation by New Homes CS (code → internal development ID mapping).
- Media layers: **plot → style → development** precedence; filenames encode level (`dev_…`, `style_…`, `plot_…`); types IMG / FLP / DOC (+ virtual tour URLs).
- Schema enums for status / property-type / price-qualifier / garage / media-type live in `rightmoveV4n.xsd` (partner pack — **not** fully reproduced in the public PDF table).

#### 3) Rightmove Data Services / early-adopter APIs

[property-data](https://www.rightmove.co.uk/property-data/) sells Market Intelligence, AVM, Surveyor Comparables, risk alerts (some “API integration”) via contact/sales — **not** a substitute for open listing search APIs. `api-docs.rightmove.co.uk` is labeled early-adopter (commercial feed); not used here as a field source.

### New homes vs resale (product)

| | For sale (resale / agent) | New Homes |
|--|--------------------------|-----------|
| Membership / admin | Estate agency; Property List in Rightmove Plus | New Homes membership; Development Marketing in Plus |
| Feed | RTDF `SendProperty` (or manual Plus entry) | ADF V4n development+plot XML **or** Plus |
| Search surfaces | “For Sale” | “New Homes for Sale” **and** For Sale exposure for many new-home products ([membership guide](https://media.rightmove.co.uk/Rightmove-New-Homes-Products-and-Tools.pdf)) |
| Development UX | Branch / agent profile | **Development Profile**, Advanced Development Listing (carousel / whole development), Spotlight stickers, Coming Soon campaigns for off-plan |
| Listing grain on SERP | One card ≈ one marketed unit/plot | Still **plot/property listings**, but packaged under a development; ADL/Showcase promote the **whole development** |

Product packaging (Featured / Premium New Home, Spotlight, ADL, Buyer Profile, Brochure Request, etc.): [New Homes product guidelines PDF](https://media.rightmove.co.uk/pdf/rightmove_new_homes_product_guidelines.pdf) (Oct 2026 label on document); [Products FAQ](https://customerfaq.rightmove.co.uk/support/solutions/articles/7000092785-explore-what-products-are-available-at-rightmove); [Spotlight FAQ](https://customerfaq.rightmove.co.uk/support/solutions/articles/7000098010-how-to-use-spotlight-for-new-homes-properties); consumer [New Homes search](https://www.rightmove.co.uk/new-homes-for-sale.html).

Lifecycle language in membership materials: Planning → Coming Soon (off-plan) → Available now → Tail end / last plots ([membership guide](https://media.rightmove.co.uk/Rightmove-New-Homes-Products-and-Tools.pdf)).

### Public vs agent-only (documented)

| Surface | Who sees what |
|---------|----------------|
| **rightmove.co.uk** | Display address, price (with qualifier), beds, media, descriptions, new-homes stickers/profiles as purchased |
| **Rightmove Plus** | Edit/live properties, Spotlight settings, Development Marketing (logo/description), lead/performance reports ([Self-serve Plus](https://www.rightmove.co.uk/c/self-serve-in-rightmove-plus/); [logo/description FAQ](https://customerfaq.rightmove.co.uk/support/solutions/articles/7000092739-updating-your-logo-and-branch-development-description-in-rightmove-plus)) |
| **RTDF address rule** | Full detailed address agent-only; `Display_Address` is what the site shows ([RTDF PDF](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)) |
| **Buyer Profile (New Homes Ascend)** | Extra enquiry questions (timeframe, buyer status, affordability) before Send enquiry — public form, developer-facing lead enrichment ([FAQ](https://customerfaq.rightmove.co.uk/support/solutions/articles/7000098055-buyer-profile-and-appointment-booking-new-homes-)) |
| **ADF / RTDF credentials** | Provider-only |

### Media, price, status, location (high level)

| Concern | Resale RTDF | New Homes ADF V4n |
|---------|-------------|-------------------|
| **Media** | Up to many media URLs per property; types in schema | Development + plot media; IMG/FLP/DOC; precedence plot→style→dev |
| **Price** | Required `Price` + optional qualifier (Guide, OIEO, etc. per Plus FAQ) | Plot `price` + development `price-min`/`price-max`; qualifiers; campaigns (“Stamp Duty Paid” example in PDF) |
| **Status** | Property `Status` required | Plot `status` (enum in XSD); discontinued developments removed when absent from full upload |
| **Location** | Postcode parts + display address + optional lat/lng | Development address + postcode (search engine); plot inherits development context |

Mandatory Plus fields for making a property live (manual path): reference, postcode, display address, price, bedrooms, property type, summary, full description ([Add/edit property FAQ](https://customerfaq.rightmove.co.uk/support/solutions/articles/7000055609-adding-or-editing-a-property-on-rightmove)).

---

## Side-by-side vs **our** approach

Our locks/shape (from schema + Zoopla→Kenya memo): **`property` = development master**; **`unit_type` = typology** (beds/size/DSQ — not door numbers); **`listing` = portal/ad snapshot** optionally → `unit_type` / nullable `property_id` for orphan Ready; public v1 = **off_plan + building**; recommended public UX = **2B** (development-first + soft typology offers).

| Dimension | Zillow | Rightmove | **Us (Kenya off-plan)** |
|-----------|--------|-----------|-------------------------|
| Canonical grain | Resale: MLS **listing**; New: **community** + plans/lots/homes | Resale: **branch listing**; New: **development** + **plots** → generated listings | **`property` (development)** + **`unit_type`** |
| Unit / plot IDs | Lots + specs when builder feeds them | Plot `name-number` in ADF | **Do not invent** flat/plot IDs; typology only unless sourced |
| SERP card | Home/lot/community cards in one map; new-construction filter | Property cards; New Homes + For Sale; ADL elevates **development** | Lean **development cards**; typology rows on page; optional typology `listing` deep-links (2B) |
| New vs resale split | Strong product split (Promoted Communities vs IDX) | Strong membership/feed split (ADF V4n vs RTDF) | `inventory_class` on property + listing; research queue skips Ready |
| Price model | Single list/plan/lot prices (MLS); builder plan pricing | Single listing price + qualifier; development min/max | **Multi `price_observation`**; payment plans; no silent NDI hero |
| Parties | Agent/Member/Office vs Builder | Branch / developer / Development Profile | `developer` graph + `agent` coverage; public CTA ≠ Hauzisha portal phone |
| Media | Listing gallery; NC community/floorplan/lot map | Listing media; NC layered media | `media_asset` DDL; seed still thin (gap eval P0) |
| Material info | MLS fields + Zestimates/public records (US) | NTS-ish: tenure, council tax, utilities, service charge | Kenya utilities vocab (generator/borehole/…) — **not** EPC-first |
| Public vs pro | IDX tabs; builder leads; Bridge licenses | Site vs Plus vs feed credentials | `public` / `admin` / `plus` exposure tiers |
| Open inventory API | **No** (Bridge partner) | **No** (ADF/RTDF write; Data Services sales) | We **own** master data (research dossiers) |

---

## Implications for Kenya product

### What to copy

1. **Development as a first-class object** — Zillow Community Page + Rightmove Development Profile / Advanced Development Listing match our `property` page better than pure classifieds.
2. **Separate new-homes packaging from resale** — Both markets treat new construction as a distinct membership/feed/UX. Our `inventory_class` + off-plan-first lock is aligned.
3. **Typology / plan layer** — Zillow “buildable plans + plan pricing” and Rightmove `style-name` / plot attributes map cleanly to **`unit_type`** (without requiring plot numbers).
4. **Media precedence** — Rightmove’s plot → style → development attach order is a useful pattern for our `property_media` roles (unit-type floorplan over development gallery).
5. **Coming soon / off-plan lifecycle** — Rightmove’s Coming Soon → Available now mirrors our Coming soon → `off_plan` mapping.
6. **Display vs full contact/address** — Rightmove’s display-address vs agent-only full address supports our Plus-vs-public phone rules (developer/project CTA public; full agent graph Plus).

### What not to copy

1. **MLS IDX dual-tab complexity** (Agent Listings vs Other Listings) — Kenya has no equivalent MLS license regime; don’t invent a parallel “portal vs agent” SERP tab.
2. **Zestimate / county public-records spine** — US-specific; Kenya Ready comps are deferred.
3. **UK EPC / council tax / shared ownership as core card fields** — Already dropped or remapped in [kenya-listing-fields.md](kenya-listing-fields.md).
4. **Plot-level ADF as v1 public SERP** — Rightmove *can* because developers feed plot stock daily. We lack trustworthy unit/plot inventory; copying plot cards would force invention (anti-goal).
5. **Single forced list price** — Both portals lean single-price listings; our conflict-aware multi-claim model is a deliberate upgrade for Kenya off-plan NDI.
6. **Partner write-feed as north-star data path** — Their APIs assume sellers push inventory. We **research-pull** into master data; feeds are a future ingest option, not v1 truth.

### What Hauzisha-like portals do differently

Observed in our product memos (not re-scraped here): Hauzisha-style Kenya portals already skew **development cards** + one portal CTA, not US-style unit classifieds for off-plan — closer to Zillow Community / Rightmove Development Profile than to MLS IDX or RTDF resale. BuyRentKenya remains more **unit-ad** oriented (beds/baths/agent “View number”). We sit between: **trustworthy development master** (Hauzisha-like card) + optional **retained typology ad snapshots** (BuyRent-like deep-link without fake stock).

---

## So what — open checklist (esp. #2)

From [zoopla-kenya-product-decisions.md](zoopla-kenya-product-decisions.md):

| Option | Closest international analog | Fit for us |
|--------|------------------------------|------------|
| **2A** Development page only | Thin Community Page / Development Profile **without** plan/plot offers | Safest, but weaker than both Zillow NC and Rightmove New Homes |
| **2B** Development-first + typology offers (recommended) | Zillow **plans + Community** without requiring lot map; Rightmove **style/typology** attributes + ADL, without full plot ADF | Matches Kenya “sell types” + our schema (`listing` ↔ `unit_type`) |
| **2C** Full unit-ad SERP now | Zillow lot/spec cards **or** Rightmove plot listings | Needs inventory we do not have → invent or scrape unreliable agent stock |

**Verdict for #2:** Live Zillow/Rightmove evidence **reinforces 2B**, not 2C. Both majors invest heavily in **development/community surfaces** for new homes; both can show unit/plot cards **only when the builder feed supplies real inventory**. Until we have retained URLs → typology `listing` rows (and never invented flat IDs), public should stay **development-first**. Full unit classifieds belong with Ready/resale later (checklist #8 / 8B), not off-plan v1.

**No new lock written to [decisions.md](../decisions.md)** — #2 remains user-confirmable; this study is decision support only.

---

## Source index (accessed 2026-10-17)

### Zillow / Bridge
- https://bridgedataoutput.com/docs/platform/Dashboard/using-apis  
- https://bridgedataoutput.com/docs/platform/API/zg-data  
- https://www.bridgedataoutput.com/docs/platform/API/rets  
- https://www.bridgedataoutput.com/docs/explorer/mls-data  
- https://www.bridgeinteractive.com/developers/bridge-api/  
- https://www.bridgeinteractive.com/developers/zillow-group-data/  
- https://zillow.zendesk.com/hc/en-us/articles/203865940-New-Construction-Listings-FAQ  
- https://www.zillow.com/new-construction-advertising/training/promoted-communities/  
- https://www.zillow.com/new-construction-advertising/buyer-discovery/  
- https://www.zillow.com/new-construction-advertising/builder-tools/  

### Rightmove
- https://www.rightmove.co.uk/adf.html  
- https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf  
- https://media.rightmove.co.uk/ps/pdf/guides/ADF_V4n_specification.pdf  
- https://www.rightmove.co.uk/property-data/  
- https://www.rightmove.co.uk/new-homes-for-sale.html  
- https://media.rightmove.co.uk/Rightmove-New-Homes-Products-and-Tools.pdf  
- https://media.rightmove.co.uk/pdf/rightmove_new_homes_product_guidelines.pdf  
- https://customerfaq.rightmove.co.uk/support/solutions/articles/7000055609-adding-or-editing-a-property-on-rightmove  
- https://customerfaq.rightmove.co.uk/support/solutions/articles/7000098010-how-to-use-spotlight-for-new-homes-properties  
- https://customerfaq.rightmove.co.uk/support/solutions/articles/7000098055-buyer-profile-and-appointment-booking-new-homes-  
- https://customerfaq.rightmove.co.uk/support/solutions/articles/7000092739-updating-your-logo-and-branch-development-description-in-rightmove-plus  
- https://customerfaq.rightmove.co.uk/support/solutions/articles/7000092785-explore-what-products-are-available-at-rightmove  
- https://www.rightmove.co.uk/c/self-serve-in-rightmove-plus/  
