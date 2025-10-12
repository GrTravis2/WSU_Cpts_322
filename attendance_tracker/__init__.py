"""Attendance tracker analytics web app."""

import functools
import pathlib
import sqlite3

import click
import flask

from attendance_tracker.app import AttendanceTracker
from attendance_tracker.controllers.admin import ADMIN
from attendance_tracker.controllers.analytics import ANALYTICS
from attendance_tracker.controllers.auth import AUTH
from attendance_tracker.controllers.ingest import INGEST


def _init_db(db_path: pathlib.Path) -> None:
    """**Overwrite db with table schema, fully deleting tables**."""
    init_db = pathlib.Path("./sqlite/init.sql")

    with (
        sqlite3.connect(db_path) as conn,
        init_db.open("r", encoding="utf-8") as sql,
    ):
        script = sql.read()
        conn.executescript(script)
        show_tables = "SELECT name FROM sqlite_master WHERE type = 'table';"
        print(f"created tables: {conn.execute(show_tables).fetchall()}\n")


def create_app() -> AttendanceTracker:
    """Entry point for flask app."""
    app = AttendanceTracker(__name__, instance_relative_config=True)

    db_path = pathlib.Path("./sqlite/attendance_tracker.db")
    if not db_path.exists():  # if dir does not exist mkdir + db
        db_path.parent.mkdir(exist_ok=True)
        db_path.touch()

    # register close db to happen at clean up
    app.teardown_appcontext(app.close_db)
    app.config.from_mapping(
        DATABASE=db_path,
    )
    init_db_cmd = click.Command(
        "init-db",
        callback=functools.partial(_init_db, db_path),
    )
    app.cli.add_command(init_db_cmd)  # register init-db as flask cli cmd

    app.register_blueprint(ADMIN)
    app.register_blueprint(ANALYTICS)
    app.register_blueprint(AUTH)
    app.register_blueprint(INGEST)

    @app.route("/")
    def index():
        return flask.render_template(
            "index.html",
            name="INDEX",
            title="HOMEPAGE",
        )

    return app
