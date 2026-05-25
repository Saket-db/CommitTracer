from __future__ import annotations

from datetime import datetime, timedelta, timezone


class GitLabClient:
    """Minimal GitLab commit source used by the local collector.

    This class stands in for real GitLab API access during early stories. It
    keeps the interface explicit and returns deterministic placeholder commits
    so the collector, validator, and report code can be exercised end-to-end.
    """

    def __init__(self, host: str, token: str, request_timeout_seconds: int = 10):
        self.host = host.rstrip("/")
        self.token = token
        self.request_timeout_seconds = request_timeout_seconds

    def has_access_token(self) -> bool:
        """Return True when the client has enough configuration to collect data."""
        return bool(self.host and self.token)

    def list_project_commits(self, project_id: str, limit: int = 25) -> list[dict[str, str]]:
        """Return a deterministic list of placeholder commit records."""
        if not self.has_access_token():
            raise ValueError("host and token are required")
        if not project_id:
            raise ValueError("project_id is required")

        count = max(1, min(limit, 10))
        now = datetime.now(timezone.utc)
        commits: list[dict[str, str]] = []
        for index in range(count):
            commits.append(
                {
                    "commit_id": f"{project_id}-{index + 1}",
                    "timestamp": (now - timedelta(days=index)).isoformat().replace("+00:00", "Z"),
                }
            )
        return commits

