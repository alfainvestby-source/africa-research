---
cursor:
  subagentId: "bc-5ceaad16-f9ba-51d4-8ff1-f196a4ac789b"
---

# Pandora Residences — Maps CID / URL pin (transcript bc-5f2f3193)

Source: `/tmp/cursor/cloud-agent-transcripts/2026-10-18T10-09-57Z-d161/bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966/transcript.json`

## User-provided Maps URL / CID

- **CID:** `12900601372674958277`
- **Exact URL:** `https://www.google.com/maps?cid=12900601372674958277&g_mp=CiVnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLkdldFBsYWNlEAMYASAF`

## Official URL (user)

- `https://pandora.co.ke/`

## Coordinate extraction

| Attempt | Result |
|---------|--------|
| urllib fetch of CID URLs | HTTP 200; `@coords` / `!3d!4d` **None**; body `center=` hits **US defaults** `(39.0267995, -77.844326)` / `(39.0299648, -77.479936)` |
| search/place/API variants | HTTP 200; `nairobi-ish pairs []`; no og:title |
| curl HTML + APP_INITIALIZATION_STATE | Same US center `[-77.479936, 39.0299648…]` — agent: “default US coordinates” |
| Transcript end | Task **incomplete** — no Nairobi lat/lng written from CID |

**No successful Nairobi coords from CID.** Prior dossier geocode (unrelated to this CID): `−1.259691, 36.785148` (Nominatim, conf 2, needs_verification). Seed `properties.csv`: lat/lng **empty**; note `GPS unknown`.

## Official URL already in seeds (pre-task)

- `developers.csv`: `dev-a-one-corporation` → `https://pandora.co.ke/`
- `contacts.csv`: `ct-pandora-url` → `https://pandora.co.ke/`
- Dossier sources / contact table already list the same URL
- `properties.csv`: **no website column**; empty lat/lng

## Do-not-invent instruction (user quote)

> “Resolve the CID / place to lat/lng (and place name/address if shown). **Do not invent if the link fails — report failure.**”
