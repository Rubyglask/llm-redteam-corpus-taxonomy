# taxonomy/

> **Status:** Skeleton — populated in **Phase 2** (2026-Q4).

This directory will host canonical JSON representations of LLM-security
frameworks plus a bidirectional cross-mapping asset.

## Planned files (Phase 2)

```
taxonomy/
├── owasp_llm_top10.json         # v1.1 + v2 (when released)
├── mitre_atlas.json             # tactics + techniques
├── nist_ai_rmf.json             # AI 100-1 + AI 600-1
├── eu_ai_act.json               # Articles 5, 15, Annex III
├── iso_iec_42001.json           # 2023 AI management standard
├── kisa_ai_guide.json           # KR — KISA AI security guide
├── cloud_security_alliance_ai.json  # CSA AI Safety Initiative
└── cross_mapping.json           # ⭐ bidirectional lookup (~300+ items)
```

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
