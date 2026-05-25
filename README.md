# CommitTracer — Component 1

Component 1 is now a local collector and upload/report workflow:

1. Download the collector script from the website.
2. Run it locally against one or many GitLab accounts.
3. Generate a schema-locked `output.json` with a payload hash.
4. Upload the JSON to the Flask app.
5. Validate the upload and generate a heatmap/report.

Example file:
- `sample_output.json` shows the expected shape of an export document.
- `output.json` is the generated local artifact and is ignored by git.

Future addition:
- A year-end wrap can be layered on top later as a derived report that summarizes the uploaded JSON into totals, trends, and highlights.
- That wrap is intentionally out of scope for the current collector/export workflow.

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -q
python tools\collect_gitlab.py --config tools\collect_gitlab.sample.json --out output.json
python -m backend.app
```

## Files of Interest

- `tools/collect_gitlab.py` - downloadable collector script.
- `shared/export_schema.json` - export contract.
- `backend/collector.py` - collection and normalization helpers.
- `backend/schema.py` - upload validation.
- `backend/reporting.py` - report and heatmap generation.
