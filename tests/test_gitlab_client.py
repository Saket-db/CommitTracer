import pytest

from backend.gitlab_client import GitLabClient


def test_gitlab_client_requires_host_and_token():
    client = GitLabClient(host="gitlab.example.com", token="")
    with pytest.raises(ValueError):
        client.list_project_commits("123")


def test_gitlab_client_returns_placeholder_commits():
    client = GitLabClient(host="gitlab.example.com", token="dummy")
    commits = client.list_project_commits("123", limit=3)
    assert len(commits) == 3
    assert commits[0]["commit_id"].startswith("123-")


def test_gitlab_client_limits_placeholder_commits():
    client = GitLabClient(host="gitlab.example.com", token="dummy")
    commits = client.list_project_commits("123", limit=50)
    assert len(commits) == 10
