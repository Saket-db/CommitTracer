from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from backend.fingerprint import compute_payload_hash

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "shared" / "export_schema.json"


def load_export_schema() -> dict[str, Any]:
    """Load the export schema definition from the shared contract layer."""
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def validate_export_document(document: Any) -> list[str]:
    """Validate the export document against the repository contract."""
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["payload must be a JSON object"]

    schema = load_export_schema()
    required_fields = schema["required"]
    for field in required_fields:
        if field not in document:
            errors.append(f"missing required field: {field}")

    if errors:
        return errors

    if document.get("schema_version") != schema["schema_version"]:
        errors.append("unsupported schema_version")

    if not isinstance(document.get("accounts"), list):
        errors.append("accounts must be a list")
    else:
        for index, account in enumerate(document["accounts"]):
            errors.extend(validate_account(account, index))

    if "payload_hash" in document:
        payload_copy = dict(document)
        payload_hash = payload_copy.pop("payload_hash")
        if compute_payload_hash(payload_copy) != payload_hash:
            errors.append("payload_hash does not match payload contents")

    return errors


def validate_account(account: Any, index: int) -> list[str]:
    errors: list[str] = []
    if not isinstance(account, dict):
        return [f"accounts[{index}] must be an object"]
    for field in ("account_name", "host", "projects"):
        if field not in account:
            errors.append(f"accounts[{index}] missing {field}")
    if not isinstance(account.get("projects"), list):
        errors.append(f"accounts[{index}].projects must be a list")
        return errors
    for project_index, project in enumerate(account["projects"]):
        errors.extend(validate_project(project, index, project_index))
    return errors


def validate_project(project: Any, account_index: int, project_index: int) -> list[str]:
    errors: list[str] = []
    if not isinstance(project, dict):
        return [f"accounts[{account_index}].projects[{project_index}] must be an object"]
    for field in ("project_id", "commits"):
        if field not in project:
            errors.append(f"accounts[{account_index}].projects[{project_index}] missing {field}")
    if not isinstance(project.get("commits"), list):
        errors.append(f"accounts[{account_index}].projects[{project_index}].commits must be a list")
        return errors
    for commit_index, commit in enumerate(project["commits"]):
        errors.extend(validate_commit(commit, account_index, project_index, commit_index))
    return errors


def validate_commit(commit: Any, account_index: int, project_index: int, commit_index: int) -> list[str]:
    errors: list[str] = []
    if not isinstance(commit, dict):
        return [f"accounts[{account_index}].projects[{project_index}].commits[{commit_index}] must be an object"]
    for field in ("commit_id", "timestamp", "day_of_week", "hour"):
        if field not in commit:
            errors.append(
                f"accounts[{account_index}].projects[{project_index}].commits[{commit_index}] missing {field}"
            )
    if "hour" in commit and not isinstance(commit["hour"], int):
        errors.append(
            f"accounts[{account_index}].projects[{project_index}].commits[{commit_index}].hour must be an integer"
        )
    return errors
