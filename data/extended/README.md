# Extended tier — non-commercial datasets

> Distributed separately as HF dataset:
> `rubyglask/llm-redteam-corpus-taxonomy-extended`

Content in this directory (once built) is under **non-commercial** licenses
inherited from upstream sources. See root `docs/license_matrix.md` for the
per-source breakdown.

## Included upstream

- ALERT (Babelscape) — CC-BY-NC-SA-4.0 — 14,032 rows
- BeaverTails (PKU-Alignment) — CC-BY-NC-4.0 — 7,753 rows
- LMSYS Toxic-Chat — CC-BY-NC-4.0 — 4,963 rows

Total 26,748 (measured 2026-07-03). Because ALERT is ShareAlike, the combined
tier is effectively **CC-BY-NC-SA-4.0**. Per-source attribution: `sources.json`.

*(Anthropic Persuasion was dropped — out of red-team scope.)*

## Not for commercial use

Do not include this tier in commercial products, guardrail SaaS, or paid
evaluations. For those use cases, the sibling `core` tier is intended.

## Attribution

When using, cite the individual upstream sources in addition to this
aggregation — see `data/extended/sources.json` (added Phase 1 Week 3-4)
for per-source citation templates.
