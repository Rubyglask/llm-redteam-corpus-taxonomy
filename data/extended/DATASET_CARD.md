---
license: cc-by-nc-sa-4.0
task_categories:
  - text-classification
language:
  - en
tags:
  - red-teaming
  - llm-security
  - non-commercial
  - research-only
  - safety-evaluation
size_categories:
  - 10K<n<100K
pretty_name: "LLM Red-Team Corpus (Extended, Non-Commercial)"
configs:
  - config_name: default
    data_files: canonical.parquet
---

# LLM Red-Team Corpus + Taxonomy — Extended (Non-Commercial)

> **⚠️ Non-commercial use only.** For commercial use, see the sibling
> [`rubyglask/llm-redteam-corpus-taxonomy-core`](https://huggingface.co/datasets/rubyglask/llm-redteam-corpus-taxonomy-core)
> (CC-BY-4.0).

**26,748 red-team / safety prompts** from 3 non-commercial sources, in the same
schema as the core dataset. Kept separate so the `core` tier stays commercially
usable. PII (phone / address) is masked, same as core.

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("rubyglask/llm-redteam-corpus-taxonomy-extended")
print(ds["train"][0]["prompt"])
```

## Sources (measured 2026-07-03)

| source_id | origin | license | n |
|---|---|---|---|
| alert | ALERT (Babelscape) | **CC-BY-NC-SA-4.0** | 14,032 |
| beavertails | BeaverTails (PKU-Alignment) | CC-BY-NC-4.0 | 7,753 |
| lmsys_toxic | ToxicChat (LMSYS) | CC-BY-NC-4.0 | 4,963 |

Per-source attribution: [`sources.json`](sources.json). Same fields as the core
dataset (`prompt`, `source_id`, `language`, `provenance`, …).

## License

This tier includes **ALERT (CC-BY-NC-SA-4.0)**. Because ShareAlike propagates to
the combined work, **the whole extended distribution is effectively
CC-BY-NC-SA-4.0** — non-commercial, and derivatives must use the same license.
Each source also keeps its own license (see `sources.json`).

**Acceptable:** academic research, non-commercial safety evaluation, defensive
red-team research at non-profits.
**Not acceptable:** commercial products, paid guardrail / evaluation services,
any use that breaks a source's non-commercial term.

## Ethics & privacy

Defensive-research dataset of already-public adversarial prompts. Do not attack
systems without permission. Phone numbers and street addresses are masked with
`[PHONE]` / `[ADDRESS]`; open an issue to report any remaining personal data.

## Code repository

Build scripts, changelog, methodology:
https://github.com/rubyglask/llm-redteam-corpus-taxonomy

<!-- ===== For programmatic / agent access ===================================
DATASET: rubyglask/llm-redteam-corpus-taxonomy-extended
PURPOSE: non-commercial LLM red-team / safety prompts (sibling of -core)
ROWS: 26748  | LICENSE: CC-BY-NC-SA-4.0 (non-commercial)  | LANG: en
COMMERCIAL_ALTERNATIVE: rubyglask/llm-redteam-corpus-taxonomy-core (CC-BY-4.0, 44681 rows)
LOAD: load_dataset("rubyglask/llm-redteam-corpus-taxonomy-extended")
SOURCES: alert (14032), beavertails (7753), lmsys_toxic (4963)
PII: phone/address masked as [PHONE]/[ADDRESS].
USE_FOR: non-commercial guardrail testing, safety research
NOT_FOR: commercial use, unauthorized attacks
========================================================================= -->
