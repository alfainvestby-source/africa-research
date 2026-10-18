# Kenya off-plan / new-development master database

Research corpus, schema seeds, dossiers, and product decisions for a Rightmove-class Kenya portal (public + Admin + Plus).

## Layout

- `docs/` — project context, decisions, discovery, product field maps, dossiers (`docs/projects/`), DB schema & seeds (`docs/db/`)
- `media/projects/<slug>/` — listing photos + per-project `manifest.csv`
- `internal/` — agent handoffs and audit notes (not user-facing)
- `notes.md` / `preferences.md` — status and lasting preferences

## Consume from other projects

This repo is a **data + research** store (CSV seeds + markdown), not a web app. Treat `docs/db/seed/` as the relational seed source and `docs/projects/` as method-locked dossiers.

See `docs/db/seed/corpus-rollup.md` and `docs/db/changelog.md` for corpus size and version history.

## Rules (short)

No invented property facts. Developer sources outweigh agents. Ready inventory is stored but not dossiered by default. Public grain is development-first (see `docs/product/`).
