"""Track HF Datasets metrics weekly — evidence timeline for the corpus.

Records downloads / likes / community activity to
`data/evidence/hf_metrics_weekly.jsonl` for later use in citation reports,
grant applications, and (for the maintainer's use) immigration evidence
packages requiring 3rd-party-verifiable engagement metrics.

Runs weekly via `.github/workflows/track_metrics.yml`.

Usage:
    python scripts/track_hf_metrics.py
"""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

DATASETS = (
    "rubyglask/llm-redteam-corpus-taxonomy-core",
    "rubyglask/llm-redteam-corpus-taxonomy-extended",
)

OUT = Path("data/evidence/hf_metrics_weekly.jsonl")


def snapshot() -> dict:
    """Fetch current dataset info from HF and return a compact record.

    Phase 1 Week 9: full implementation with huggingface_hub.
    """
    # TODO: from huggingface_hub import HfApi
    # api = HfApi()
    # for dataset in DATASETS:
    #     info = api.dataset_info(dataset)
    #     record[dataset] = {
    #         "downloads_total": info.downloads,
    #         "likes": info.likes,
    #         "last_modified": info.last_modified.isoformat(),
    #     }
    return {
        "timestamp": datetime.now(UTC).isoformat(),
        "note": "skeleton — HF API integration in Phase 1 Week 9",
        "datasets": list(DATASETS),
    }


def main() -> int:
    record = snapshot()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"recorded: {record['timestamp']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
