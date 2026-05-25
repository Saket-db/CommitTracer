from pathlib import Path

from flask import Blueprint, send_file

download_bp = Blueprint("download", __name__)


@download_bp.get("/collector.py")
def download_collector_script():
    """Serve the downloadable collector script to the frontend."""
    script_path = Path(__file__).resolve().parents[3] / "tools" / "collect_gitlab.py"
    return send_file(script_path, as_attachment=True, download_name="collect_gitlab.py", mimetype="text/x-python")
