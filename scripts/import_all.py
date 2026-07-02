"""Download upstream sources into data/raw/ (per-source JSONL + SHA-256).

Usage:
    python scripts/import_all.py                 # all enabled sources
    python scripts/import_all.py --only advbench # a single source
"""
from __future__ import annotations

import argparse
from pathlib import Path

from redteam_corpus.pipeline import SOURCES, download_source


def main() -> int:
    ap = argparse.ArgumentParser(description="Download upstream red-team datasets.")
    ap.add_argument("--only", help="Download a single source_id (default: all enabled)")
    ap.add_argument("--raw", type=Path, default=Path("data/raw"))
    args = ap.parse_args()

    if args.only:
        if args.only not in SOURCES:
            print(f"unknown source: {args.only}. known: {', '.join(SOURCES)}")
            return 2
        targets = [SOURCES[args.only]]
    else:
        targets = [s for s in SOURCES.values() if s.enabled]

    if not targets:
        print("no sources to download (none enabled).")
        return 1

    for src in targets:
        print(f"downloading {src.source_id} <- {src.hf_repo} ...")
        path, digest = download_source(src, args.raw)
        n = sum(1 for line in path.open(encoding="utf-8") if line.strip())
        print(f"  {n} rows -> {path}  sha256={digest[:12]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
