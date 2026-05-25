import json

from flask import Blueprint, jsonify, request

from backend.reporting import build_report
from backend.schema import validate_export_document

uploads_bp = Blueprint("uploads", __name__)


def read_uploaded_document() -> dict | None:
    """Read JSON from either a raw request body or an uploaded file."""
    if "file" in request.files:
        return json.load(request.files["file"])
    if request.is_json:
        return request.get_json(silent=True)
    return None


@uploads_bp.post("/validate")
def validate_uploaded_document():
    """Validate an uploaded export document and return any schema errors."""
    document = read_uploaded_document()
    errors = validate_export_document(document)
    status_code = 200 if not errors else 422
    return jsonify({"valid": not errors, "errors": errors}), status_code


@uploads_bp.post("/report")
def create_report_from_upload():
    """Validate the upload and return a heatmap/report payload."""
    document = read_uploaded_document()
    errors = validate_export_document(document)
    if errors:
        return jsonify({"valid": False, "errors": errors}), 422
    return jsonify({"valid": True, "report": build_report(document)}), 200
