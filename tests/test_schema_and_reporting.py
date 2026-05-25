from backend.collector import build_export_document
from backend.reporting import build_report
from backend.schema import validate_export_document


def sample_account_snapshot():
    return {
        "account_name": "corp-main",
        "host": "gitlab.example.com",
        "projects": [
            {
                "project_id": "123",
                "commits": [
                    {"commit_id": "123-1", "timestamp": "2026-05-26T12:00:00Z", "day_of_week": "Tuesday", "hour": 12},
                    {"commit_id": "123-2", "timestamp": "2026-05-26T13:00:00Z", "day_of_week": "Tuesday", "hour": 13},
                ],
            }
        ],
    }


def test_export_document_validates():
    document = build_export_document([sample_account_snapshot()])
    assert validate_export_document(document) == []


def test_report_builds_heatmap():
    document = build_export_document([sample_account_snapshot()])
    report = build_report(document)
    assert report["total_accounts"] == 1
    assert report["total_projects"] == 1
    assert report["total_commits"] == 2
    assert report["heatmap"]["Tuesday"][12] == 1
