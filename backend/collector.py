from __future__ import annotations

import concurrent.futures
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from backend.fingerprint import compute_payload_hash
from backend.gitlab_client import GitLabClient


def load_account_specs(config_path: str | Path) -> list[dict[str, Any]]:
    """Load account specs from a JSON config file."""
    config = json.loads(Path(config_path).read_text(encoding="utf-8"))
    return config.get("accounts", [])


def collect_all_accounts(account_specs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collect all configured accounts with bounded concurrency."""
    if not account_specs:
        return []
    max_workers = min(4, len(account_specs))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(collect_account_snapshot, account_specs))


def collect_account_snapshot(account_spec: dict[str, Any]) -> dict[str, Any]:
    """Collect and normalize all configured projects for one account."""
    client = GitLabClient(host=account_spec["host"], token=account_spec["token"])
    projects = [collect_project_snapshot(client, project_spec) for project_spec in account_spec["projects"]]
    return {"account_name": account_spec["account_name"], "host": account_spec["host"], "projects": projects}


def collect_project_snapshot(client: GitLabClient, project_spec: dict[str, Any]) -> dict[str, Any]:
    """Collect normalized commits for one project."""
    raw_commits = client.list_project_commits(project_spec["project_id"], project_spec.get("limit", 25))
    commits = [normalize_commit_record(commit) for commit in raw_commits]
    return {"project_id": project_spec["project_id"], "commits": commits}


def normalize_commit_record(raw_commit: dict[str, Any]) -> dict[str, Any]:
    """Normalize raw commit data into the export schema shape."""
    timestamp = parse_timestamp(raw_commit["timestamp"])
    return {
        "commit_id": raw_commit["commit_id"],
        "timestamp": timestamp.isoformat().replace("+00:00", "Z"),
        "day_of_week": timestamp.strftime("%A"),
        "hour": timestamp.hour,
    }


def parse_timestamp(value: str) -> datetime:
    """Parse ISO timestamps and normalize them to UTC."""
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def build_export_document(account_snapshots: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the final export document and attach a payload hash."""
    document = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source": "local-collector",
        "accounts": account_snapshots,
    }
    document["payload_hash"] = compute_payload_hash(document)
    return document


def write_export_document(document: dict[str, Any], output_path: str | Path) -> None:
    """Write the export document to disk in a deterministic format."""
    Path(output_path).write_text(json.dumps(document, indent=2, sort_keys=True), encoding="utf-8")
