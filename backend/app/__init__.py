from flask import Flask, jsonify

from backend.app.routes.download import download_bp
from backend.app.routes.upload import uploads_bp


def create_app() -> Flask:
    """Create the Flask app used by the local upload/report website."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(
            {
                "status": "ok",
                "message": "CommitTracer backend is running.",
                "routes": {
                    "health": "/health",
                    "download_collector": "/downloads/collector.py",
                    "validate_upload": "/uploads/validate",
                    "create_report": "/uploads/report",
                },
            }
        ), 200

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    app.register_blueprint(download_bp, url_prefix="/downloads")
    app.register_blueprint(uploads_bp, url_prefix="/uploads")
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
