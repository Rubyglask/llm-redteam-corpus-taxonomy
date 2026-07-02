"""Orchestrate a quarterly release refresh.

Phase 3 target — quarterly cadence starts 2027-Q1.

Steps:
    1. Refresh upstream data (re-run scripts/import_all.py)
    2. Detect new upstream datasets (from a curated tracker list)
    3. Rebuild core + extended distributions
    4. Update manifest.json + CHANGELOG.md entry
    5. Bump CITATION.cff version → next quarter (e.g. v2026.Q4)
    6. Tag release + push
    7. HF Datasets sync
    8. Wayback Machine snapshot of release page
    9. arXiv changelog paper draft (2-3 pages)

Usage:
    python scripts/quarterly_update.py --quarter 2026-Q4 --dry-run
"""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Quarterly release orchestrator.")
    parser.add_argument("--quarter", required=True, help="Target quarter, e.g. 2026-Q4")
    parser.add_argument("--dry-run", action="store_true", help="Plan only, no writes")
    args = parser.parse_args()

    # TODO Phase 3: implement the full pipeline.
    raise NotImplementedError(
        f"quarterly_update skeleton — quarter={args.quarter}, dry_run={args.dry_run}. "
        "Full pipeline lands in Phase 3 (2026-Q4 end)."
    )


if __name__ == "__main__":
    raise SystemExit(main())
