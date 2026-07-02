"""Build canonical corpus distributions from raw upstream data.

Pipeline:
    data/raw/{source_id}/data.jsonl  →  canonicalize  →  dedup (exact-hash)
    →  {parquet, jsonl.gz, duckdb} in data/{core|extended}/  →  manifest.json

Usage:
    python scripts/build_corpus.py --tier core     --out data/core/
    python scripts/build_corpus.py --tier extended --out data/extended/
"""
from __future__ import annotations

import argparse
from pathlib import Path

from redteam_corpus.pipeline import build_corpus


def main() -> int:
    parser = argparse.ArgumentParser(description="Build canonical corpus distribution.")
    parser.add_argument("--tier", choices=["core", "extended", "full"], required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--raw", type=Path, default=Path("data/raw"))
    args = parser.parse_args()

    manifest = build_corpus(args.tier, args.raw, args.out)
    sources = ", ".join(manifest["sources"]) or "(none)"
    print(f"built {args.tier}: {manifest['num_rows']} rows from [{sources}]")
    for name, digest in manifest["files"].items():
        print(f"  {name}  sha256={digest[:12]}...")
    if not manifest["files"]:
        print("  (no files written — no enabled sources for this tier)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
