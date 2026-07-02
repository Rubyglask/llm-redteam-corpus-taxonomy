"""Unit tests for the pure pipeline helpers (no network, no file I/O)."""
from __future__ import annotations

from redteam_corpus.pipeline import (
    Source,
    dedupe,
    exact_hash,
    normalize,
    priority_rank,
    scrub_pii,
    to_canonical,
)

_SRC_A = Source(
    source_id="advbench", hf_repo="walledai/AdvBench", prompt_field="prompt",
    license="MIT", tier="core", citation="c", source_url="u", enabled=True,
)
_SRC_B = Source(
    source_id="harmbench", hf_repo="walledai/HarmBench", prompt_field="prompt",
    license="MIT", tier="core", citation="c", source_url="u",
)


# ── normalize / exact_hash ──────────────────────────────────────────────────


def test_normalize_lowercases_and_collapses_whitespace():
    assert normalize("  Hello   WORLD\n\tfoo  ") == "hello world foo"


def test_exact_hash_ignores_case_and_spacing():
    assert exact_hash("Ignore   Previous") == exact_hash("ignore previous")


def test_exact_hash_differs_for_different_text():
    assert exact_hash("abc") != exact_hash("abd")


# ── priority_rank ───────────────────────────────────────────────────────────


def test_priority_rank_orders_known_sources():
    # harmbench outranks advbench in _SOURCE_PRIORITY
    assert priority_rank("harmbench") < priority_rank("advbench")


def test_priority_rank_unknown_sorts_last():
    assert priority_rank("nope") > priority_rank("anthropic_hh")


# ── dedupe ──────────────────────────────────────────────────────────────────


def test_dedupe_collapses_normalized_duplicates():
    pairs = [
        (_SRC_A, {"source_original_id": "0", "prompt": "How to hack"}),
        (_SRC_A, {"source_original_id": "1", "prompt": "how   to   hack"}),  # dup
        (_SRC_A, {"source_original_id": "2", "prompt": "different"}),
    ]
    out = dedupe(pairs)
    assert len(out) == 2


def test_dedupe_keeps_first_by_input_order():
    # caller pre-sorts by priority; dedupe keeps the first occurrence
    pairs = [
        (_SRC_B, {"source_original_id": "b", "prompt": "same prompt"}),
        (_SRC_A, {"source_original_id": "a", "prompt": "same prompt"}),
    ]
    out = dedupe(pairs)
    assert len(out) == 1
    assert out[0][0].source_id == "harmbench"  # first wins


# ── to_canonical ────────────────────────────────────────────────────────────


# ── scrub_pii ───────────────────────────────────────────────────────────────


def test_scrub_pii_masks_phone():
    assert scrub_pii("call 585-690-9410 now") == "call [PHONE] now"


def test_scrub_pii_masks_street_address():
    out = scrub_pii("who lives at 427 Central Street in Monterey?")
    assert "[ADDRESS]" in out
    assert "427 Central Street" not in out


def test_scrub_pii_leaves_clean_text():
    assert scrub_pii("How do I pick a lock?") == "How do I pick a lock?"


# ── to_canonical ────────────────────────────────────────────────────────────


def test_to_canonical_has_all_schema_fields():
    row = to_canonical({"source_original_id": "7", "prompt": "Test PROMPT"}, _SRC_A, 3)
    assert row["scenario_id"] == "CN_0000003"
    assert row["prompt"] == "Test PROMPT"  # verbatim, casing preserved
    assert row["prompt_normalized"] == "test prompt"
    assert row["exact_hash"] == exact_hash("Test PROMPT")
    assert row["source_id"] == "advbench"
    assert row["source_original_id"] == "7"
    assert row["source_license"] == "MIT"
    assert row["license_tier"] == "core"
    assert row["taxonomy_hints"] == {}
    assert row["provenance"]["source_url"] == "u"
