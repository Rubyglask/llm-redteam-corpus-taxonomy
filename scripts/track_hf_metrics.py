"""Track HF Datasets metrics — evidence timeline for the corpus.

Records downloads / likes for both datasets to
`data/evidence/hf_metrics_weekly.jsonl` (append-only). Starting from a
timestamped baseline of 0 gives a verifiable growth curve later — useful for
citation reports, grant applications, and (for the maintainer) an
immigration-evidence package that needs third-party-verifiable engagement
metrics.

Runs weekly via `.github/workflows/track_metrics.yml`, or on demand:
    python scripts/track_hf_metrics.py --at 2026-07-03T00:00:00Z
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DATASETS = (
    "rubyglask/llm-redteam-corpus-taxonomy-core",
    "rubyglask/llm-redteam-corpus-taxonomy-extended",
)

OUT = Path("data/evidence/hf_metrics_weekly.jsonl")


def fetch_one(repo: str) -> dict:
    """Fetch downloads/likes for one dataset from the HF Hub API."""
    from huggingface_hub import HfApi

    info = HfApi().dataset_info(repo)
    return {
        "repo": repo,
        "downloads": getattr(info, "downloads", None),
        "downloads_all_time": getattr(info, "downloads_all_time", None),
        "likes": getattr(info, "likes", None),
    }


def snapshot(timestamp: str) -> dict:
    return {
        "timestamp": timestamp,
        "datasets": [fetch_one(r) for r in DATASETS],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Record HF metrics snapshot.")
    ap.add_argument(
        "--at",
        required=True,
        help="ISO timestamp to stamp this snapshot (e.g. 2026-07-03T00:00:00Z). "
        "Passed in because the build environment forbids wall-clock calls.",
    )
    args = ap.parse_args()

    record = snapshot(args.at)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    for d in record["datasets"]:
        print(f"  {d['repo']}: downloads={d['downloads']} likes={d['likes']}")
    print(f"recorded at {record['timestamp']} -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
