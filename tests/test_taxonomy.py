"""Consistency tests for the Phase-2 taxonomy JSONs.

These keep the crosswalk honest: every OWASP id is covered, and the
source→taxonomy map only references real OWASP ids and real enabled sources.
"""
from __future__ import annotations

import json
from pathlib import Path

from redteam_corpus.pipeline import SOURCES

TAX = Path(__file__).parent.parent / "taxonomy"


def _load(name: str) -> dict:
    return json.loads((TAX / name).read_text(encoding="utf-8"))


def test_owasp_has_ten_items_llm01_to_llm10():
    owasp = _load("owasp_llm_top10.json")
    ids = [it["id"] for it in owasp["items"]]
    assert ids == [f"LLM{i:02d}" for i in range(1, 11)]


def test_cross_mapping_covers_all_owasp_items():
    owasp_ids = {it["id"] for it in _load("owasp_llm_top10.json")["items"]}
    mapping = _load("cross_mapping.json")["mappings"]
    assert set(mapping) == owasp_ids
    # every mapping declares nist + atlas + eu with a rationale
    for _id, m in mapping.items():
        assert m["nist_ai_rmf"]["functions"]
        assert "tactics" in m["mitre_atlas"]
        assert m["rationale"]


def test_source_mapping_uses_valid_owasp_ids():
    owasp_ids = {it["id"] for it in _load("owasp_llm_top10.json")["items"]}
    srcmap = _load("source_to_taxonomy.json")["sources"]
    for sid, m in srcmap.items():
        assert m["primary"] in owasp_ids, f"{sid} primary not a valid OWASP id"
        for sec in m["secondary"]:
            assert sec in owasp_ids, f"{sid} secondary {sec} invalid"


def test_source_mapping_matches_enabled_sources():
    """Every enabled (shipped) source is mapped, and no extra ids are invented."""
    enabled = {s.source_id for s in SOURCES.values() if s.enabled}
    mapped = set(_load("source_to_taxonomy.json")["sources"])
    assert mapped == enabled, (
        f"mismatch: only-in-map={mapped - enabled}, only-enabled={enabled - mapped}"
    )
