from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.collector import build_export_document, collect_all_accounts, load_account_specs, write_export_document


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the local collector script."""
    parser = argparse.ArgumentParser(description="Collect GitLab commit metadata into a JSON export.")
    parser.add_argument("--config", required=True, help="Path to the account config JSON file")
    parser.add_argument("--out", default="output.json", help="Path to the export JSON output file")
    return parser.parse_args()


def main() -> int:
    """Run the local collector and write the export document."""
    args = parse_args()
    account_specs = load_account_specs(args.config)
    account_snapshots = collect_all_accounts(account_specs)
    export_document = build_export_document(account_snapshots)
    write_export_document(export_document, args.out)
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
