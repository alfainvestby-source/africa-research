# Geo enrichment — corpus GPS pins

Version: **0.1.0**  
Last updated: **2026-10-18**  
Steward skill: [geo-poi-enricher.md](../agents/geo-poi-enricher.md)  
Seed: [`seed/geo_pins.csv`](seed/geo_pins.csv) · optional sample POIs [`seed/pois.csv`](seed/pois.csv) / [`seed/property_pois.csv`](seed/property_pois.csv)  
Schema: v**0.1.13** (`geo_method`, `poi`, `property_poi`)

**Rule:** Never invent coordinates. Prefer official → NEMA/ESIA → OSM Nominatim geocode → CSV seed. Vague address → leave unknown.

---

## Method

| Priority | Method | Confidence | When used |
|----------|--------|------------|-----------|
| 1 | `official` — developer JSON-LD / map embed / Maps CTA on project site | 4–5 | Galaxy JSON-LD (5); Golfscape Maps CTA (4) |
| 2 | `nema` — NEMA EIA / ESIA filing GPS | 5 | Golden, Berkeley, Plumeria, Luna Oak |
| 3 | `geocode` — OSM Nominatim of sourced street + neighbourhood + city | 2–3 | Street-level when no official/filing pin |
| 4 | `csv` — seed CSV lat/lng | 2 | Until corroborated (or kept when geocode diverges) |
| — | `unknown` | 0 | Address too vague or geocode resolves to wrong feature |

**Provider:** OpenStreetMap Nominatim (`https://nominatim.openstreetmap.org/search`)  
**User-Agent:** `MajengoGeoEnricher/1.0 (research; contact=geo@majengo.local)`  
**Rate limit:** ≥1.1 s between requests  
**Accessed:** 2026-10-16  

**Row promotion (`properties.lat/lng`):** Only when conf ≥4 (official/NEMA/Maps CTA). Lower-confidence pins live in `geo_pins` / claims with `geo_method` + public “approx” badge candidate.

---

## Coverage summary

| Metric | Count |
|--------|------:|
| Dossier properties covered | **27 / 27** |
| Pins with conf ≥4 (seed-ready on `properties` row) | **7** (incl. Pandora Maps place 2026-10-18) |
| Pins geocode conf 2–3 | **18** |
| Pins CSV-only conf 2 (no better pin) | **2** (Porini, Astra) |
| Still **unknown** | **1** (ELD-001 Kings Square Ph2) |
| Rejected pins (not stored as recommended) | Longines JSON-LD; Kings Square → Eldoret Airport |

**Pins vs unknown:** **26 pinned** (any method) · **1 unknown**.

---

## Per-property results

| id | name | lat | lng | method | conf | source | notes |
|----|------|-----|-----|--------|------|--------|-------|
| NBO-001 | Golden Mansion | −1.265143 | 36.806272 | nema | 5 | [NEMA EIA](https://nema.go.ke/wp-content/uploads/2025/12/SUMMIT-VISTA_00329-min.pdf) GPS header | **Canonical.** CSV −1.26512, 36.80627 matches ~1–2 m. On `properties.csv`. |
| NBO-002 | Pandora Residences | −1.260829 | 36.780513 | official | 4 | Maps CID `12900601372674958277` → place Pandora / Muthangari Dr | **Canonical (Maps place, 2026-10-18).** On `properties.lat/lng`. Nominatim −1.259691, 36.785148 demoted secondary. Official site https://pandora.co.ke/. |
| NBO-003 | Riara Oasis | −1.298579 | 36.767794 | geocode | 2 | Nominatim `Riara Road, Thompson, Nairobi, Kenya` | NEMA plot known, no filing GPS. Street centroid. |
| NBO-004 | Porini Point | −1.15703 | 36.88792 | csv | 2 | CSV seed | Not developer-sourced. Tatu City Nominatim −1.150814, 36.901062 = master-community centroid (alt check only). |
| NBO-005 | Astra Bay Residence | −1.23310 | 36.71314 | csv | 2 | CSV seed Lower Kabete | **`needs_verification`.** Lower Kabete Rd geocode −1.240500, 36.750169 **diverges ~4 km E** — dual claim; no winner. |
| NBO-006 | Golfscape Residences | −1.300478 | 36.800965 | official | 4 | golfscape.co.ke Google Maps CTA | **Canonical (Maps).** Muchai Road Nominatim −1.300165, 36.800397 corroborates. On `properties.csv`. |
| NBO-007 | Diamond Bay Residences | −1.267701 | 36.806566 | geocode | 3 | Nominatim `20 Westlands Road, Westlands, Nairobi, Kenya` | Building-level hit. Prefer over CSV −1.26750, 36.81202 (~600 m E). |
| NBO-008 | Longines Bay | −1.303258 | 36.788463 | geocode | 2 | Nominatim `Kabarnet Road, Nairobi, Kenya` | **Reject JSON-LD −1.3635, 36.7719** (implausible vs Kabarnet/Ngong grid; keep as NV secondary claim only). Street approx Woodley/Kibra edge. |
| NBO-009 | Gemini Residency Phase 2 | −1.259416 | 36.793132 | geocode | 2 | Nominatim `Matundu Lane, Brookside, Westlands, Nairobi, Kenya` | Street label conflict Matundu vs Brookside Grove. L2B DMS −1.26619, 36.80911 secondary conf 1. |
| NBO-010 | Berkeley Homes | −1.28050 | 36.78997 | nema | 5 | [NEMA ESIA](https://nema.go.ke/wp-content/uploads/2025/12/SR-00234-ESIA-RESIDENTIAL-KILELESHWA.pdf-Rarlon-Estate-Development-Company-Limited-min.pdf) fact sheet | **Canonical.** Nefroon −1.2814, 36.7897 secondary. On `properties.csv`. |
| NBO-011 | Lesonia Residences | −1.278414 | 36.785502 | geocode | 3 | Midpoint Gatundu Rd (−1.278297, 36.784821) + Tinderet Ave (−1.278530, 36.786184) | Intersection query NONE; Kenton School NONE. Flag intersection approx. |
| NBO-012 | Luna Oak Residency | −1.293751 | 36.777031 | nema | 5 | NEMA ESIA Mingland / Block 17/283 | **Canonical.** On `properties.csv`. ≠ Brookside Oak. |
| NBO-013 | Galaxy ONE | −1.2635 | 36.8029 | official | 5 | galaxyone.co JSON-LD | **Canonical.** Rhapta Rd street geocode nearby only. On `properties.csv`. |
| NBO-014 | Alba Apartments | −1.297700 | 36.754006 | geocode | 2 | Nominatim `Wanyee Road, Dagoretti, Nairobi, Kenya` | Prefer Wanyee over Naivasha Rd corridor. |
| NBO-015 | Plumeria Residency | −1.2974 | 36.7606 | nema | 5 | NEMA EIA §2.1 Plot 330/179 | **Canonical.** On `properties.csv`. |
| NBO-016 | Polaris Residency | −1.297874 | 36.790001 | geocode | 2 | Nominatim `Kindaruma Road, Kilimani, Nairobi, Kenya` | No developer/NEMA GPS. Street-only. |
| NBO-017 | Misty Springs | −1.271911 | 36.811024 | geocode | 2 | Nominatim `Westlands Road, Westlands, Nairobi, Kenya` | Street centroid near GTC corridor. |
| NAK-001 | Kings Summit | −0.263170 | 36.078867 | geocode | 2 | Nominatim `Maragoli Road, Milimani, Nakuru, Kenya` | Maragoli = Craiova-only (NV). Broader Milimani blob ~10 km E — rejected. |
| DISC-NBO-005 | Nouveau | −1.289054 | 36.783741 | geocode | 2 | Nominatim `Lenana Road, Hurlingham, Nairobi, Kenya` | Street centroid; Altra Kilimani label NV. |
| MSA-001 | Sensei | −4.055089 | 39.701731 | geocode | 3 | Nominatim `Greenwood Drive, Nyali, Mombasa, Kenya` | Beachfront plot unpublished; street-level. ≠ Benford Greenwood. |
| ELD-001 | Kings Square Ph2 | — | — | unknown | 0 | — | Nominatim `Airport Road, Eldoret` → **Eldoret Intl Airport** — **REJECT**. Leave unknown until plot/LR. |
| DISC-CAPRICORN | Capricorn | −1.293717 | 36.786086 | geocode | 3 | Nominatim `Wood Avenue, Kilimani, Nairobi, Kenya` | Near Yaya / CJ's per dossier; ≠ Staroot Residency. |
| DISC-NBO-001 | CANTO | −1.257683 | 36.794544 | geocode | 3 | Nominatim `34 School Lane, Westlands, Nairobi, Kenya` | VAAL “34 School Lane”; near Sarit. |
| DISC-NBO-004 | Ankori | −1.264493 | 36.789855 | geocode | 2 | Nominatim `Rhapta Road, Westlands, Nairobi, Kenya` | No street number — **do not reuse** Galaxy JSON-LD. |
| DISC-NBO-006 | Brookside Oak | −1.258594 | 36.788122 | geocode | 3 | Nominatim `Muguga Green, Brookside, Westlands, Nairobi, Kenya` | Prefer Muguga Green over Brookside blob. Safaricom HQ NONE. ≠ Luna Oak NEMA. |
| KWA-001 | Kai | −4.312492 | 39.579360 | geocode | 2 | Nominatim `Diani Beach, Kwale, Kenya` | Settlement-level only (northern walkway claimed, no street). Low precision. |
| DIA-001 | 108 Residences | −4.324829 | 39.570190 | geocode | 3 | Nominatim `Diani Beach Road, Diani, Kenya` | Official street Diani Beach Road; ~420 steps to beach; no plot GPS. |

---

## Rejected / dual claims (do not invent a winner)

| Property | Rejected or secondary | Why |
|----------|----------------------|-----|
| Longines Bay | JSON-LD −1.3635, 36.7719 | Far south of Kabarnet/Kilimani grid; dossier already `needs_verification` |
| Kings Square Ph2 | Airport 0.404363, 35.233289 | Aerodrome, not residential Phase 2 site |
| Astra Bay | Kabete Rd geocode vs CSV | ~4 km diverge — keep both NV |
| Diamond Bay | CSV −1.26750, 36.81202 | Prefer “20 Westlands Road” geocode |
| Porini Point | Tatu City suburb centroid | Too coarse for plot; CSV retained conf 2 |
| Ankori | Galaxy ONE JSON-LD | Same corridor, different product — never share pin |
| Kings Summit | Milimani village blob | ~10 km east of Maragoli |

---

## Light POI sample (optional)

Sample Westlands / Kilimani / coast anchors for Plus proximity chips — **not** exhaustive. See `seed/pois.csv` + `seed/property_pois.csv`. Distances are haversine from recommended pin (approx); route times not computed this pass.

| poi_id | name | type | lat | lng |
|--------|------|------|-----|-----|
| poi-sarit-centre | Sarit Centre | mall | −1.2614 | 36.8045 |
| poi-yaya-centre | Yaya Centre | mall | −1.2926 | 36.7880 |
| poi-westgate | Westgate Shopping Mall | mall | −1.2567 | 36.8056 |
| poi-aga-khan-nairobi | Aga Khan University Hospital | hospital | −1.2639 | 36.8156 |
| poi-nairobi-hospital | The Nairobi Hospital | hospital | −1.2956 | 36.8047 |
| poi-royal-nairobi-gc | Royal Nairobi Golf Club | leisure | −1.3010 | 36.7995 |
| poi-nyali-cinemax | Nyali Cinemax | mall | −4.0430 | 39.6860 |

Property↔POI links only where pin conf ≥2 and POI is in the same metro (see seed).

---

## Next passes

1. NEMA/plot chase for ELD-001, Ankori street number, Longines correct GPS, Kai exact walkway.  
2. Google Geocoding if API key available (higher precision street numbers).  
3. Route-time to CBD / Westlands / airport (Plus).  
4. Promote geocode pins to public only with “approx” badge (product decision already in skill).
