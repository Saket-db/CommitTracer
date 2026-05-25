from __future__ import annotations

from collections import defaultdict
from typing import Any


DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def build_report(document: dict[str, Any]) -> dict[str, Any]:
    """Summarize uploaded export data into report-friendly aggregates."""
    commits = flatten_commits(document)
    return {
        "total_accounts": count_accounts(document),
        "total_projects": count_projects(document),
        "total_commits": len(commits),
        "heatmap": build_heatmap(commits),
    }


def count_accounts(document: dict[str, Any]) -> int:
    return len(document.get("accounts", []))


def count_projects(document: dict[str, Any]) -> int:
    return sum(len(account.get("projects", [])) for account in document.get("accounts", []))


def flatten_commits(document: dict[str, Any]) -> list[dict[str, Any]]:
    commits: list[dict[str, Any]] = []
    for account in document.get("accounts", []):
        for project in account.get("projects", []):
            commits.extend(project.get("commits", []))
    return commits


def build_heatmap(commits: list[dict[str, Any]]) -> dict[str, list[int]]:
    heatmap = {day: [0] * 24 for day in DAY_ORDER}
    for commit in commits:
        day = commit.get("day_of_week")
        hour = commit.get("hour")
        if day in heatmap and isinstance(hour, int) and 0 <= hour < 24:
            heatmap[day][hour] += 1
    return heatmap
