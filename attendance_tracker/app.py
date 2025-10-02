"""Entry point for web app."""

from __future__ import annotations

from pathlib import Path

from flask import Flask, render_template

from attendance_tracker.controllers.admin import ADMIN
from attendance_tracker.controllers.analytics import ANALYTICS
from attendance_tracker.controllers.auth import AUTH
from attendance_tracker.controllers.ingest import INGEST


def create_app() -> Flask:
    """Entry point for flask app."""
    app = Flask(__name__, instance_relative_config=True)

    # TODO (Dylan): replace path with sqlite file path
    app.config.from_mapping(
        DATABASE=Path("attendance_tracker/REPLACE_ME_LATER"),
    )

    app.register_blueprint(ADMIN)
    app.register_blueprint(ANALYTICS)
    app.register_blueprint(AUTH)
    app.register_blueprint(INGEST)

    @app.route("/")
    def index():
        return render_template("index.html", name="INDEX", title="HOMEPAGE")

    return app
