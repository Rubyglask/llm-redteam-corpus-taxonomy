# taxonomy/

> **Status:** Phase 2 **v0.1 (anchor)** shipped 2026-07-03. OWASP LLM Top 10 is
> the anchor; the crosswalk to other frameworks is confidence-tagged and not yet
> authoritative (expert review pending).

Canonical JSON of LLM-security frameworks plus a cross-mapping asset — the
project's main differentiator (no unified public crosswalk exists today).

## Shipped (v0.1)

```
taxonomy/
├── owasp_llm_top10.json      ✅ 10 items (2025), high confidence
├── cross_mapping.json        ✅ OWASP → NIST AI RMF + MITRE ATLAS + EU AI Act
│                                (per-item confidence: high / medium / candidate)
└── source_to_taxonomy.json   ✅ each corpus source → OWASP category
```

**Honesty of v0.1:** OWASP ids and NIST AI RMF **function-level** mappings are
high confidence. MITRE ATLAS **tactic names** are high confidence, but ATLAS
**technique ids** (`AML.Txxxx`) are `candidate` — verify against the live ATLAS
matrix before citing. EU AI Act articles are coarse and need legal review.
Every mapping carries a `confidence` field; `cross_mapping.json` states this.

Consistency is enforced by `tests/test_taxonomy.py` (all 10 OWASP items covered;
source map references only valid ids and real shipped sources).

## Planned (later Phase 2)

```
├── mitre_atlas.json          # full tactics + verified technique ids
├── nist_ai_rmf.json          # AI 100-1 + AI 600-1 categories
├── eu_ai_act.json            # Articles 5, 15, 50, Annex III
├── iso_iec_42001.json        # 2023 AI management standard
├── kisa_ai_guide.json        # KR — KISA AI security guide
└── cloud_security_alliance_ai.json
```

Next steps: expert review of the crosswalk, verify ATLAS technique ids, add the
remaining framework JSONs, then a per-prompt classifier to fill each corpus
row's `taxonomy_hints` (currently `"{}"`).

## Canonical framework JSON schema (Phase 2 target)

```json
{
  "framework_id": "owasp_llm_top10",
  "version": "v1.1",
  "source_url": "https://owasp.org/www-project-top-10-for-large-language-model-applications/",
  "source_license": "CC-BY-SA-4.0",
  "last_updated": "2026-Q4",
  "items": [
    {
      "id": "LLM01",
      "name": "Prompt Injection",
      "description": "...",
      "examples": [],
      "references": []
    }
  ]
}
```

## Cross-mapping schema (Phase 2 target)

```json
{
  "generated_at": "2026-Q4",
  "mapping_version": "v1.0",
  "mappings": {
    "owasp_llm_top10:LLM01": {
      "mitre_atlas": ["AML.T0051.000", "AML.T0051.001"],
      "nist_ai_rmf": ["Measure 2.7", "Manage 2.4"],
      "eu_ai_act": ["Article 15"],
      "iso_iec_42001": ["8.4"],
      "kisa_ai_guide": ["A-3.2"],
      "cloud_security_alliance_ai": ["..."],
      "confidence": "high",
      "rationale": "..."
    }
  }
}
```

Reverse indexes (MITRE → OWASP, NIST → OWASP, etc.) auto-generated from the
primary mapping.

## Why cross-mapping matters

Compliance teams increasingly need to answer:
"Which frameworks does this control cover?"

No unified cross-walk exists for LLM security. This asset intends to fill
that gap and support:

- Regulatory conformity assessment (EU AI Act Article 15 evidence)
- ISO 42001 audit mapping
- OWASP LLM Top 10 → NIST AI RMF traceability
- Multi-jurisdiction compliance narratives

The mapping is JSON-first, versioned, and updated quarterly with the corpus.
