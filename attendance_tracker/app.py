"""Entry point for web app."""

from __future__ import annotations

from pathlib import Path

from flask import Flask

from attendance_tracker.controllers.analytics import ANALYTICS_BP
from attendance_tracker.controllers.ingest import INGEST_BP


def create_app() -> Flask:
    """Entry point for flask app."""
    app = Flask(__name__, instance_relative_config=True)

    # TODO (Dylan): replace path with sqlite file path
    app.config.from_mapping(
        DATABASE=Path("attendance_tracker/REPLACE_ME_LATER"),
    )

    app.register_blueprint(INGEST_BP)
    app.register_blueprint(ANALYTICS_BP)

    return app
