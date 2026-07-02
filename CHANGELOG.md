# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) · Semver.
Living dataset: quarterly release cadence `vYYYY.QX`.

## [Unreleased] — v0.1.0-dev (2026-Q3)

### Changed — adversarial pre-upload review fixes (2026-07-03)
- **Excluded 3 sources from v0.1.0** after a 3-perspective (optimist/critic/
  neutral) review:
  - **StrongREJECT** — its README shows it bundles questions from no-license
    upstreams (MaliciousInstruct / HarmfulQ / OpenAI System Card); cannot be
    relicensed to CC-BY-4.0 core cleanly.
  - **WMDP-cyber** — dual-use weapons-proxy knowledge; upstream forbids
    training-corpus inclusion; rows are MCQ stems, not attack prompts.
  - (Persuasion already excluded — not attack prompts.)
- **PII masking** — phone numbers + street addresses → `[PHONE]` / `[ADDRESS]`
  (~33 rows). New `scrub_pii` helper + unit tests.
- **`sources.json`** generated per tier (MIT / CC-BY attribution completeness).
- **Measured counts:** core **44,681** (9 sources) + extended **26,748** (3) =
  **71,429**. Corrected card errors — core dedup is −4% (not 23%), largest
  extended source is **ALERT** (not BeaverTails), `taxonomy_hints` is a `"{}"`
  string (not a filled dict).
- **Extended relabeled CC-BY-NC-SA-4.0** (ALERT ShareAlike propagates).
- **Author** set to `rubyglask` across dataset card + CITATION.

### Added
- Initial repository scaffolding (README, LICENSE ×2, CITATION.cff, DATASET_CARD).
- `docs/license_matrix.md` — 17 upstream source license classification.
- `taxonomy/` placeholder (populated in Phase 2, 2026-Q4).
- `docs/plan/2026-07-02_project-plan-and-review.md` — canonical plan +
  3-perspective (optimist/critic/neutral) review synthesis.
- **GATE 1 — working build pipeline** (`src/redteam_corpus/pipeline.py`):
  download → canonicalize → exact-hash dedup → parquet + jsonl.gz + duckdb +
  manifest.json. **Deterministic** (gzip mtime=0, fixed order → reproducible
  checksums verified by `verify_checksums.sh`).
  - `pyproject.toml` (installable via `pip install -e .[dev]`, ruff + pytest
    configured), `scripts/import_all.py`, real `scripts/build_corpus.py` +
    `scripts/verify_checksums.sh`, `tests/test_pipeline.py` (8 passing).
  - Vertical slice proven end-to-end on `LibrAI/do-not-answer`
    (939 rows → 938 after dedup). Remaining sources enabled in Week 2.
  - Note: `walledai/AdvBench` & `walledai/HarmBench` mirrors are **gated** —
    Week 2 must request access or use the original llm-attacks/HarmBench repos.

### Added — Week 2 source expansion (2026-07-03)
- Enabled **10 sources** (7 core + 3 extended) with verified config/split/prompt
  columns: do_not_answer, tdc23, forbidden_question_set, harmfulqa, aart,
  wmdp_cyber, jailbreakbench (core); beavertails, alert, lmsys_toxic (extended).
- **First measured build**: core **8,647** rows (7 sources), extended **26,749**
  (3 sources), after exact-hash dedup. Reproducible (verify_checksums OK).
  The earlier inherited "~90K/~34K" estimates are replaced by these measured
  counts (core came in ~10× smaller than the estimate).
- Language detection hardened: ASCII-dominant prompts pinned to `en` (langdetect
  was mislabeling short English prompts as cy/ca/it); core is now 100% `en`.

### Added — Week 2b: core complete (2026-07-03)
- **All 11 core sources now built** via two new download adapters:
  - `github_csv`: AdvBench (520), HarmBench (393), StrongREJECT (288) pulled
    from the original GitHub CSVs (their HF mirrors were gated).
  - `hf_transcript`: HH-RLHF red-team-attempts (38,961) → first human turn
    extracted → 37,155 after dedup (largest core source).
- **Measured totals: core 46,919 (11 sources) + extended 26,749 (3) = 73,668.**
- **Persuasion excluded**: its `argument` column is persuasive prose, not an
  attack prompt — out of red-team scope (was tentatively `extended`).
- v0.1.0 ships **14 of 17** sources; 2 pending license (MaliciousInstruct,
  Korean UnSmile), 1 excluded (Persuasion). Reproducible, ruff clean, pytest 8.

### Fixed — GATE 0 license/count normalization (2026-07-02)
- **Source counts corrected to verified ground truth: 17 total = 11 core +
  4 extended + 2 pending** (was mislabeled "16 total / 12–13 core").
- All 17 upstream licenses **re-verified live against HF/GitHub APIs**:
  - AART: Apache-2.0 → **CC-BY-4.0** (was mislabeled)
  - Anthropic Persuasion: CC-BY-NC-4.0 → **CC-BY-NC-SA-4.0** (was mislabeled)
  - MaliciousInstruct & Korean UnSmile: **no SPDX license found** → moved to
    **pending**, excluded from v0.1.0 until manually verified (Week 2)
- Removed the legally incorrect claim that CC-BY-SA is one-way compatible with
  the CC-BY-4.0 core aggregate. **No CC-BY-SA in core.**
- Scenario counts (~90K core / ~34K extended) relabeled as **pre-build
  estimates**, not measured (dedup not yet run).
- DATASET_CARD `language` tag reduced to `en` (only verified English core
  sources; `ko` pending UnSmile license).

### Phase 1 targets (Week-by-week; see docs/phase1_plan.md forthcoming)

- **Weeks 1-2** — legal foundation + public data re-download.
- **Weeks 3-4** — canonical schema + dedup + license split + 3-format build.
- **Weeks 5-6** — HF Datasets registration + GitHub CI.
- **Weeks 7-8** — full documentation + arXiv preprint v1 + Zenodo DOI.
- **Weeks 9-10** — signal infrastructure + first monthly refresh.

### Notes
- No public data yet. All contents are skeleton/documentation.
- Author email confirmed personal (`rubyglask@gmail.com`), no employer
  affiliation in commits.

---

## Planned releases

- **v0.1.0** (2026-Q3 end): First public release — corpus core + extended,
  HF Datasets published, arXiv preprint issued, Zenodo DOI assigned.
- **v0.2.0 / v2026.Q4** (2026-Q4): Phase 2 — 7 framework taxonomy JSONs +
  cross-mapping (~300 items) + Papers with Code entry.
- **v1.0.0 / v2026.Q4** (2026-Q4 end): Phase 3 — integrated corpus + taxonomy
  release + HF Space demo.
- **v2027.Q1 onward**: quarterly refresh — new upstream datasets, updated
  taxonomies, changelog paper appended.
