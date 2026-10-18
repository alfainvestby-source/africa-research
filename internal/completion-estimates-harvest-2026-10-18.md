---
cursor:
  subagentId: "bc-5f2f3193-933f-5c5b-9290-1b2f7e0bb966"
---

# Completion / delivery harvest — 2026-10-18

**Changelog:** **0.1.22** · Seed: [`../docs/db/seed/completion_estimates.csv`](../docs/db/seed/completion_estimates.csv) + columns on `properties.csv`

No invented dates. Parsed from dossier `completion_estimate` (and handover aliases).

| Status | n | Public card |
|--------|--:|-------------|
| `agreed` | 9 | Show `completion_display` (e.g. Jabali **December 2028**) |
| `window` | 7 | Show band (e.g. Berkeley **April 2028 / Q2 2028**) |
| `conflict` | 30 | “YYYY (dates conflict — confirm)” — full raw in Admin |
| `unknown` | 5 | Blank / Admin only (e.g. Eldoret Ph2; Rosewood Ready lean) |

**Public-eligible (agreed+window):** **16/51** — below 70% gate as a *required* facet; still useful when present.

### Watermark follow-up (user ask)

**We did not remove watermarks** from any file. We:
- Flagged Hauzisha CDN rows as `watermark_risk`
- Pulled cleaner copies from developer/CPK/etc. where available
- Prefer those as heroes (`watermark_risk` heroes = 0)

Detail: [watermark-originals-refresh-2026-10-18.md](watermark-originals-refresh-2026-10-18.md)
