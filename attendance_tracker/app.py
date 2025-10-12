"""Entry point for web app."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from flask import Flask, current_app, g, render_template

from attendance_tracker.controllers.admin import ADMIN
from attendance_tracker.controllers.analytics import ANALYTICS
from attendance_tracker.controllers.auth import AUTH
from attendance_tracker.controllers.ingest import INGEST

def get_db() -> sqlite3.Connection:
    """Create connection to db, called at each request."""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
        )

    return g.db


def close_db(exc: BaseException | None = None) -> None:
    """Close DB connection on app tear down."""
    db: sqlite3.Connection = g.pop("db", None)

    if db is not None:
        db.close()


def create_app() -> Flask:
    """Entry point for flask app."""
    app = Flask(__name__, instance_relative_config=True)

    db_path = Path("./sqlite/attendance_tracker.db")
    if not db_path.exists():  # if dir does not exist mkdir + db
        db_path.parent.mkdir(exist_ok=True)
        db_path.touch()

    app.teardown_appcontext(close_db)  # register close db to happen at clean up
    app.config.from_mapping(
        DATABASE=db_path,
    )

    app.register_blueprint(ADMIN)
    app.register_blueprint(ANALYTICS)
    app.register_blueprint(AUTH)
    app.register_blueprint(INGEST)

    @app.route("/")
    def index():
        return render_template("index.html", name="INDEX", title="HOMEPAGE")

    return app
