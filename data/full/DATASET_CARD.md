---
license: cc-by-nc-sa-4.0
task_categories:
  - text-classification
language:
  - en
tags:
  - red-teaming
  - llm-security
  - jailbreak
  - adversarial-prompts
  - ai-safety
  - safety-evaluation
  - guardrails
  - prompt-injection
size_categories:
  - 10K<n<100K
pretty_name: "LLM Red-Team Corpus (Full) — 12 sources unified into one format"
configs:
  - config_name: default
    data_files: canonical.parquet
---

# LLM Red-Team Corpus + Taxonomy — Full (everything, non-commercial)

> **Every source in one download. We collected 12 public LLM red-team / safety
> datasets, unified them into one schema, removed duplicates, masked personal
> data, and kept where each prompt came from. 64,458 prompts. Load in one line.**

This is the **complete** corpus — all 12 sources merged and de-duplicated across
tiers. Because it includes non-commercial sources (BeaverTails, ALERT,
ToxicChat) and ALERT is ShareAlike, the whole set is **CC-BY-NC-SA-4.0
(non-commercial)**.

**Need commercial use?** Use the [`-core`](https://huggingface.co/datasets/rubyglask/llm-redteam-corpus-taxonomy-core)
version (44,681 prompts, CC-BY-4.0) — the permissively-licensed subset.

## Which version should I download?

| I want... | Dataset | Rows | License |
|---|---|---|---|
| **Everything, research/non-commercial** | `-full` (this) | **64,458** | CC-BY-NC-SA-4.0 |
| **Commercial-safe subset** | `-core` | 44,681 | CC-BY-4.0 |
| **Only the non-commercial sources** | `-extended` | 26,748 | CC-BY-NC-SA-4.0 |

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("rubyglask/llm-redteam-corpus-taxonomy-full")
print(ds["train"][0]["prompt"])

# filter by source or license
commercial_ok = ds["train"].filter(lambda r: r["license_tier"] == "core")
one_source    = ds["train"].filter(lambda r: r["source_id"] == "harmbench")
```

## Ask an LLM / agent to use it

> *"Load the Hugging Face dataset `rubyglask/llm-redteam-corpus-taxonomy-full`
> and test my chatbot against every prompt where `source_id == 'harmbench'`.
> The prompt text is in the `prompt` column."*

## Sources — 12 public datasets, one format

Every row, regardless of source, uses the **same 11-field schema** (see below).
Licenses were verified live against each upstream on 2026-07-03.

| source_id | origin | license | rows |
|---|---|---|---|
| anthropic_hh | HH-RLHF red-team-attempts | MIT | 37,155 |
| alert | ALERT (Babelscape) | CC-BY-NC-SA-4.0 | 14,032 |
| lmsys_toxic | ToxicChat (LMSYS) | CC-BY-NC-4.0 | 4,951 |
| aart | AART (Google) | CC-BY-4.0 | 3,213 |
| harmfulqa | HarmfulQA | Apache-2.0 | 1,938 |
| do_not_answer | Do-Not-Answer | Apache-2.0 | 938 |
| beavertails | BeaverTails (PKU) | CC-BY-NC-4.0 | 794 |
| advbench | AdvBench | MIT | 520 |
| harmbench | HarmBench | MIT | 393 |
| forbidden_question_set | "Do Anything Now" | MIT | 390 |
| jailbreakbench | JailbreakBench | MIT | 80 |
| tdc23 | TDC 2023 Red-Teaming | MIT | 54 |

Per-source attribution: [`sources.json`](sources.json).
**Note:** 83% of rows are `anthropic_hh` (first human turn of each red-team
transcript); some are ordinary conversation openers, not all direct attacks.

## Fields (same schema across all versions)

| field | meaning |
|---|---|
| `scenario_id` | id inside this dataset (`CN_0000001`) |
| `prompt` | the prompt, from the source (PII masked) |
| `prompt_normalized` | lowercased, spaces cleaned (dedup basis) |
| `exact_hash` | SHA-256 of `prompt_normalized` |
| `language` | ISO code (`en`, …) |
| `source_id` / `source_original_id` | which source + id inside it |
| `source_license` | that source's license |
| `license_tier` | `core` (commercial-OK) or `extended` (non-commercial) |
| `taxonomy_hints` | JSON string, `"{}"` for now (Phase 2) |
| `provenance` | JSON string `{source_url, source_citation}` |

Formats: **Parquet** (default) · **JSONL.gz** · **DuckDB**.

## Ethics, dual-use & privacy

Defensive-research dataset of already-public adversarial prompts. Do **not**
attack systems without permission; follow responsible disclosure. Phone numbers
and street addresses are masked (`[PHONE]` / `[ADDRESS]`); open an issue to
report remaining personal data. Excluded on purpose: WMDP (dual-use),
StrongREJECT (no-license questions), Persuasion (not attack prompts).

## License

**CC-BY-NC-SA-4.0** — non-commercial, ShareAlike (because ALERT is NC-SA and it
propagates to the combined set). Each source also keeps its own license
(`sources.json`). For commercial use, take the `-core` subset (CC-BY-4.0).

## Code & citation

github.com/rubyglask/llm-redteam-corpus-taxonomy · see `CITATION.cff`.

<!-- ===== For programmatic / agent access ===================================
DATASET: rubyglask/llm-redteam-corpus-taxonomy-full
PURPOSE: complete LLM red-team / jailbreak / safety corpus, 12 sources unified
ROWS: 64458  | LICENSE: CC-BY-NC-SA-4.0 (non-commercial)  | LANG: en
COMMERCIAL_SUBSET: rubyglask/llm-redteam-corpus-taxonomy-core (CC-BY-4.0, 44681)
LOAD: load_dataset("rubyglask/llm-redteam-corpus-taxonomy-full")
KEY_FIELDS: prompt (str), source_id (str), source_license (str), license_tier (str)
FILTER_BY: source_id, language, license_tier
SOURCES(12): anthropic_hh, alert, lmsys_toxic, aart, harmfulqa, do_not_answer,
             beavertails, advbench, harmbench, forbidden_question_set,
             jailbreakbench, tdc23
NOTE: 83% is anthropic_hh (HH-RLHF first human turn). PII masked.
USE_FOR: guardrail testing, safety benchmarking, red-team research (defensive, non-commercial)
NOT_FOR: commercial use (use -core), unauthorized attacks
========================================================================= -->
