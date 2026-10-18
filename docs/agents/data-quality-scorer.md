# Skill: Data quality / risk scorer

Score each **method-complete** property on NDI density, NV density, weak developer, thin sources, and agent-only commercial fields. Output Admin triage + Plus trust signals.

**Output:** [`docs/db/data-quality-scores.md`](../db/data-quality-scores.md)  
**Corpus denominator:** same as [field-promotion.md](../db/field-promotion.md) (stubs excluded).  
**Rules:** No invented facts; scores only over dossier flags + source meta. Public never shows raw risk scores (confidence internal).

## Inputs per property
| Metric | Meaning |
|--------|---------|
| `ndi_count` | Distinct fields with `needs_developer_input` |
| `nv_count` | Distinct themes with `needs_verification` (deduped) |
| `developer_conf` | Primary developer 0–5 |
| `sources_retained` | Research retained count |
| `agent_only_commercial` | How many of {price, payment_deposit, completion} lack developer canonical (0–3) |

## Composite
`risk_score` 0–100 (higher = worse). Formula and triage bands (P0–P3) live in the scores deliverable.  
`trust = 100 − risk_score` for Plus.

## When to re-run
After each research wave, retrofit, or verification pass that clears NDI/NV.
