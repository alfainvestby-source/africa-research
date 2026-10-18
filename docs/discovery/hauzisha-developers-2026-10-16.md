# Hauzisha developers — list + research pass

**Pass date:** 2026-10-16  
**Inputs:**
- Directory scrape: [`internal/hauzisha-co-ke-2026-10-16-directory.csv`](../../internal/hauzisha-co-ke-2026-10-16-directory.csv) (51 cards from `/developers/`)
- Detail scrape: [`internal/hauzisha-co-ke-2026-10-16-developer-pages.csv`](../../internal/hauzisha-co-ke-2026-10-16-developer-pages.csv) (per-developer pages; noisy HTML-stripped blobs)
- Cleaned rollup: [`internal/hauzisha-developers-2026-10-16.csv`](../../internal/hauzisha-developers-2026-10-16.csv) · [`internal/hauzisha-developers-2026-10-16.json`](../../internal/hauzisha-developers-2026-10-16.json)

**Trust posture:** Hauzisha is denser and more structured than Block.ke, but still a **marketing portal**. Treat developer attributions as **leads** until corroborated by official microsites, NEMA/EIA, or ≥2 independent non-Hauzisha sources. Never promote Hauzisha-only commercial claims to public conf ≥4.

**Scope:** Developer inventory + development names. Not full project dossiers this pass (except verification notes).

**Research-queue locks (2026-10-16):** Portal/Hauzisha development exports = **lead lists**. Mark both Ready **unit ads** and Ready/handed-over **whole developments**. `inventory_class` = `off_plan` \| `building` \| `ready` \| `resale` (steward DDL). **Ready** = store/mark only — **no dossier for now**. **Coming soon** = in scope for **review**. Never treat **`0730 731 355`** as developer phone. Full rules: [portal-inventory-class-research-rules.md](portal-inventory-class-research-rules.md) · [hauzisha-developers.md](../db/hauzisha-developers.md).

---

## Jafu verification (user check)

**Yes — exactly 3 developments** on Hauzisha for **Jafu Real Estate Group**, matching the URLs provided:

| # | Development | Area (Hauzisha) | Hauzisha URL |
|--:|-------------|-----------------|--------------|
| 1 | **Citrine Heights** | Westlands | https://hauzisha.co.ke/developments/citrine-heights/ |
| 2 | **Auris Residence** | Westlands | https://hauzisha.co.ke/developments/auris-residence/ |
| 3 | **Serene Manor** | Kilimani | https://hauzisha.co.ke/developments/serene-manor/ |

**Outside Hauzisha:**
- Official brand site: [jafugroupkenya.com](https://jafugroupkenya.com/) — currently features **Serene Manor** (20 floors, Lenana / Yaya corridor; 1–4BR + 8BR duplex PH).
- NRE developer profile links **Auris Residence**; Serene Manor noted as external portfolio context.
- Hauzisha claims: Citrine **23 floors / 161 units**; Auris **20-storey hotel+residences**, Dec **2027**; Serene Manor completion **Oct–Dec 2027**, from **KES 3.5M**.

**Research verdict:** Real developer brand with at least one official project surface. **Process-rerun candidate** (wave-style dossiers) for all three — developer-first via jafugroupkenya.com + multi-agent; legal SPV still unknown.

≠ **Serene Holding Group** (different Hauzisha developer: Serene Boutique Residency / Diamond Mango).

---

## Inventory summary

| Metric | Value |
|--------|------:|
| Developers on directory | **51** |
| Developments parsed from detail pages | **~127** |
| Already overlap corpus developer / project | **~15–17** |
| New / thin outside our dossiers | **majority** |

---

## Full developer list (51)

Sorted roughly by Hauzisha “homes for sale” density on the directory card. Development names from cleaned detail-page parse (may omit “+N more” extras when text_9 incomplete — see JSON for claimed counts).

| Developer | #devs (Hauzisha) | Developments (parsed) | Outside-Hauzisha research (this pass) | Corpus overlap |
|-----------|-----------------:|------------------------|----------------------------------------|----------------|
| **Mi Vida Homes** | 7 | 156 Elara; Amaiya; 237 Garden City; **237 Lulu**; KEZA-class siblings | Official mividahomes.com | **Yes** — DISC-NBO-007 |
| **Elegant Properties** | 5 | Sunpark; Donyo Hill; Forestview; 48 Treehouse; Oak & Ivy | **elegantproperties.co.ke** portfolio live | **Done** — DISC-NBO-012…015 (skip Ready: Sunpark I, Oak & Ivy) · [elegant-properties-verification.md](elegant-properties-verification.md) |
| **GLBC Group** | 3 | Libra; Only You; Gemini Hub & Residences | **glbcgroup.co.ke** (Libra, Gemini, Taurus, Aries…) | New — **≠ Staroot Gemini P2** |
| **M-Group Developer** | 4 | Montbleu; Marina Bay 2; Marina Bay 3; Marble West | Marina Bay LinkedIn/agent dense; Montbleu official = **Muthithi Square Development Ltd** | New — **entity conflict on Montbleu** |
| **Jafu Real Estate Group** | **3** | **Serene Manor; Citrine Heights; Auris Residence** | jafugroupkenya.com + NRE | **New — verified** |
| **Oasis Development Company LTD** | 4 | Rhapta One; Forest One; Brookside One; Riverside One | Multi Hauzisha “One” brand; no corporate site locked this pass | New — **≠ Riara Oasis / AIMASI** |
| **Staroot Real Estate Company** | 5 | Gemini I; Capricon; Venus Oak; Gemini 2; … | staroot.co.ke | **Yes** — Capricorn / Gemini P2 |
| **Sunmon Group** | 4 | Lesto; **Balkis Riverside**; Atreus Brookside; Aether | Still Hauzisha-primary for “Sunmon”; Atreus EIA = **Atreus Ventures Ltd**; Hauzisha Atreus page also says “Lesto Residence Developer” | **Partial** — Balkis DISC-NBO-010 (Sunmon conf 2) |
| **Superior Homes Kenya** | 3 | Orchards Northlands; Lukenya Plains; Pazuri Vipingo | Established national brand (known market face) | New geography / product class |
| **Amto View Investment LTD** | 2 | Amto View Serviced; **Morvara** | Named on Morvara leads | Lead — Morvara pending wave |
| **Wonder Properties** | 5 | Diplomat; **Gaia Brookside**; Alina Valley; Alina Harbour; … | wonderpropertykenya.com / Diplomat microsite | Gaia on national leads |
| **Henbon Company LTD** | 2 | Diamond Ivy; **Diamond Bay** | Official Henbon stack | **Yes** — NBO-007 |
| **Sonder Space Residence** | 3 | Space Residence; Clermont; Shangrilla Villas | Thin outside Hauzisha this pass | New / watch |
| **Gemdale Kenya Limited** | 3 | Capital Heights; Capital Vista; Capital Garden | Brand echo of China Gemdale — verify Kenya SPV | New / careful |
| **KP Housing Development** | 2 | Urban Park; **Seasons Riverside** | Agent matrices exist | Lead — Seasons pending |
| **Mara Grove Limited** | 1 | Mara Grove Residence | Thin | New |
| **Pavillion Properties LTD** | 3 | Cub; Canvas; Canopy | Thin this pass | New |
| **Serene Holding Group** | 2 | Serene Boutique; Diamond Mango | ≠ Jafu Serene Manor | New |
| **17 Group** | 2 | 17 Zuri; 17 Annex | Thin | New |
| **A-One Corporation** | 3 | **Pandora**; Acacia Serviced; Panorama West | Known | **Yes** — NBO-002 |
| **African Developers Group (ADG)** | 2 | Luxore; Venice Tower | Thin | New |
| **Hanz Group Kenya** | 2 | Luminara Westlands; Belgravia Place | Thin | New |
| **HomeFor Real Estate LTD** | 1 | Luster Arbor | Thin | New |
| **Ivy Group Kenya** | 3 | Ivy Park; Blossoms Ivy; Luckinn Ivy | Space.ke / leads | Lead — Ivy Park |
| **Longfor Investment Limited** | 1 | Artesano | Thin; brand-name caution | New / careful |
| **Novolumen Nairobi LTD** | 2 | San Remo Heights; Casa Rina | Thin | New |
| **Unity Homes** | 3 | Unity One; Silver Hill; Unity Parkside | Established national brand | New / known market |
| **AAD Real Estate** | 4 | **Aya Luxury**; Ambra; Rosewood; Grand Premier | Launch coverage aad.ke | Lead — AYA next wave |
| **Azure Apex** | 2 | Azure Apex Residence; Azure Sky Park | Thin | New |
| **Next Property Group** | 1 | Next Amani | Thin | New |
| **Nidaam Star Ltd** | 1 | Maylan Park | Thin | New |
| **Pinecrest Paradise Investment Co Ltd** | 2 | Grosvenor; **Cheval Riverside** | Agent hits | New — ≠ Balkis |
| **R1 Africa Limited** | 1 | Verona Westlands | Thin | New |
| **Residency Africa** | 2 | Angani; Kirawa Village | Thin | New |
| **The Skypeak Limited** | 2 | Golden Hill; **Golden Mansion** | Marketing partner pattern | **Yes** — NBO-001 (SkyPeak ≠ primary) |
| **Trident Estates** | 2 | Trident Amani; Baraka Ph IV | Syokimau / satellite | New |
| **Tsudo Realtors Limited** | 2 | Mango Tree; Apple Tree | Name says Realtors — may be agent brand | Watch — possible mislabel |
| **CDG** | 1 | **Stellar Bay Residences** | Block hold name echo | Watch — was Block Tier B |
| **Heimat Consult LTD** | 1 | The Opal | Thin | New |
| **Lionston Real Estate** | 1 | **Galaxy One** | Official | **Yes** — NBO-013 |
| **Nanchang Investment Company Limited** | 1 | **Alba** | Known lead | **Yes** — NBO-014 |
| **Oak Group** | 1 | **Brookside Oak** | Marketing partner pattern | **Yes** — DISC-NBO-006 |
| **Phileo Limited** | 1 | Sabaki Green Estate | Thin | New |
| **Rarlon Estate Developers** | 1 | **Berkeley** | NEMA ESIA | **Yes** — NBO-010 |
| **Saif Properties** | 4–5 | Covo Arboretum (+ commercial); Covo Residence; Kenzi | Thin | New |
| **Setech Real Estate Ltd** | 1 | Athi Hub One | Thin | New |
| **Vanilla Vista Gardens** | 1 | Vanilla Vista Gardens | Thin | New |
| **WH Harmony Investment Co. Ltd** | 1 | **Golfscape** | Known | **Yes** — NBO-006 |
| **Eliteplus Homes LTD** | 2 | Savannah Woodlands; Sunset View | Thin | New |
| **Canaan Developers** | 2 | Terreno Riverside; Altura | Thin; 0 homes listed | New |
| **MaCaash Investment Ltd** | 10–11 | Marjaan; Chalbi; Asili; Sultana; Akshar; Lulu Residency; Tamam; Shams; Hilal; Westlight… | Parklands-heavy; founded 2013 claim on Hauzisha; **0 homes for sale** this scrape | New — large portfolio, early/coming-soon |

---

## Research highlights (non-Hauzisha)

### Strong official surfaces (process soon)

| Developer | Why | First projects to dossier |
|-----------|-----|---------------------------|
| **Jafu Real Estate Group** | Official site + 3 Hauzisha schemes | Serene Manor → Citrine → Auris |
| **GLBC Group** | glbcgroup.co.ke portfolio | Libra Residences; Only You; **do not merge** Gemini Hub with Staroot Gemini P2 |
| **Elegant Properties** | elegantproperties.co.ke | Forestview; Donyo Hill; Sunpark |
| **Wonder Properties** | wonderpropertykenya.com + Diplomat microsite | Gaia Brookside (already on leads); Diplomat; Alina Valley |
| **AAD Real Estate** | Launch press | **AYA** (already next in Block wave queue) |

### Entity / naming traps (do not collapse)

| Trap | Detail |
|------|--------|
| **Sunmon Group** vs **Atreus Ventures Ltd** vs “Lesto Residence Developer” | Hauzisha groups Balkis/Lesto/Atreus/Aether under Sunmon; NEMA Atreus proponent = Atreus Ventures Ltd; Atreus Hauzisha card also attributes “Lesto Residence Developer”. Keep claim set + NV until LOO/registry. |
| **M-Group** vs **Muthithi Square Development Ltd** | Montbleu.co.ke names Muthithi Square; Hauzisha attributes Montbleu to M-Group. Marina Bay phases look M-Group in agent coverage. |
| **Oasis Development Company LTD** ≠ Riara Oasis Limited / AIMASI | Different “Oasis” brand family (“One Residency” series). |
| **GLBC Gemini Hub** ≠ Staroot **Gemini Residency Phase 2** | Same word, different developer/geography. |
| **Serene Manor (Jafu)** ≠ **Serene Holding Group** | Unrelated. |
| **Skypeak / Oak Group** | Already locked as marketing partners, not primary developers, on Golden Mansion / Brookside Oak. |
| **Tsudo Realtors** | Name suggests agency; confirm before treating as developer. |

### Balkis / Sunmon update

Hauzisha developer page explicitly lists Sunmon as developer of **Sky-valley, Atreus Brookside, Lesto, Balkis Riverside** (4 schemes). That strengthens the Hauzisha attribution for Balkis but **does not** raise conf above portal level until official/registry corroboration — consistent with DISC-NBO-010 (Sunmon conf 2).

---

## Suggested process-rerun order (developer-led)

Use same method as Block wave: scan ~10, keep ≥5, developer-first, multi `price_claims[]`, no portal conf ≥3 alone.

1. ~~**Jafu trio**~~ — **done** DISC-NBO-016…018  
2. ~~**GLBC** — Libra + Only You~~ — **done** DISC-NBO-019…020 (Gemini Hub held ≠ Staroot)  
3. ~~**Elegant**~~ — **done** DISC-NBO-012…015 (Ready skips held)  
4. ~~**Wonder** — Gaia + Diplomat~~ — **done** DISC-NBO-021…022  
5. ~~**AAD / AYA**~~ — **done** DISC-NBO-023 (Whitehorse)  
6. ~~**Oasis “One” — Rhapta One**~~ — **done** DISC-NBO-024 (siblings Forest/Brookside/Riverside One next)  
7. ~~**M-Group — Montbleu + Marina Bay 2**~~ — **done** DISC-NBO-026…027 (Montbleu SPV still NDI; Marina Bay 3 next)  
8. ~~**Atreus Brookside**~~ — **done** DISC-NBO-028 (Lesto / Aether still held)  
9. ~~**Wonder Alina Valley**~~ — **done** DISC-NBO-025 (Alina Harbour Ready-hold)  
10. ~~**Whitehorse Grand Premier + Rosewood**~~ — **done** DISC-NBO-029…030 (Ambra deferred)  

Hold / low priority this pass: MaCaash (coming-soon / 0 listings), Gemdale/Longfor brand caution, CDG/Stellar Bay (Block Tier B echo), Tsudo until developer vs agent clarified.

---

## Files created/updated

| Path | Role |
|------|------|
| This doc | Research narrative + shortlist |
| `internal/hauzisha-developers-2026-10-16.csv` | Flat developer table |
| `internal/hauzisha-developers-2026-10-16.json` | Full parsed developments |
| `internal/hauzisha-co-ke-2026-10-16-directory.csv` | Raw directory scrape copy |
| `internal/hauzisha-co-ke-2026-10-16-developer-pages.csv` | Raw detail scrape copy |

**Not done this pass:** full project dossiers for the 127 schemes; seed CSV ingest; photo/geo.
