# Goal and approach (plain language)

Decisions detail: [decisions.md](decisions.md)

## Goal
Build a **world-class Kenya property product** in the class of **Rightmove** (public), **Rightmove Admin** (ops/content), and **Rightmove Plus** (pro/agent tools). The foundation is a **strong, professional data layer**: trustworthy master data for off-plan / new developments across **Kenya** (Nairobi corpus first; discovery now national) where nothing is invented and every claim is sourced, checked, and organized with calculated product decisions — not ad-hoc scraping.

## Approach
1. Discover each project through many real sources (scan ~10, keep ≥5 densest), always preferring the developer’s own materials when they exist and agree.
2. Store a relational graph (property, parties, prices, sources, flags) fit for public + admin + pro surfaces, with confidence, conflicts, `needs_verification`, and `needs_developer_input` when we must not guess.
3. Learn in small cycles, then scale; promote fields to the **public** portal only when high-confidence **and** high coverage — richer/conflicted data stays available for **Admin** and **Plus**-style pro use.
4. Prefer **professional, well-calculated** collection and modeling choices aimed at long-term product quality over speed shortcuts.

## Documentation habit
Every lock goes into [decisions.md](decisions.md) the same day; method detail also lands in project-context, learning-loop, schema, and `docs/db/` as relevant.
