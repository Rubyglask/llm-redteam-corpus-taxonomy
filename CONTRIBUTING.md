# Contributing

Thanks for your interest — this project welcomes:

- **New dataset suggestions** (open an issue with the "new_dataset" template).
- **Taxonomy corrections** — mappings between OWASP LLM Top 10 / MITRE ATLAS /
  NIST AI RMF / EU AI Act / ISO 42001 / KISA / CSA are reviewer-adjudicated;
  substantive suggestions with citations are welcome.
- **Reproducibility bug reports** — if `make build && make verify` produces
  a mismatch against release checksums.
- **Language coverage expansion** — Japanese / Chinese / Arabic / European
  language subsets from public sources.

## Ground rules

1. **Public data only.** No dataset containing production system logs,
   customer data, or non-public red-team engagements.
2. **License chain must be clean.** Every added row must be traceable to a
   documented upstream license.
3. **No CVE / vulnerability disclosure in issues.** Use responsible
   disclosure channels for any vulnerabilities discovered in production
   systems; this repository is for defensive research corpora only.
4. **Attribution preserved.** Upstream citations are non-negotiable.

## Dev setup

```bash
git clone https://github.com/rubyglask/llm-redteam-corpus-taxonomy
cd llm-redteam-corpus-taxonomy
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pre-commit install
```

## Pull request checklist

- [ ] Tests pass (`pytest`)
- [ ] Lint clean (`ruff check .`)
- [ ] Changelog entry added under `[Unreleased]`
- [ ] If adding a dataset: `docs/license_matrix.md` updated + upstream
      citation added to `data/{tier}/sources.json`
- [ ] Author email is personal (no employer domain in git author)
- [ ] Rebased onto `main`

## Governance

Solo-maintained during Phase 1-3 (2026-Q3~Q4). Contribution guide will
expand as the community grows. All decisions logged in
`docs/design_decisions.md` (added Phase 2).
