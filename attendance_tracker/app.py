"""Entry point for web app."""

from __future__ import annotations

import sqlite3

import flask


class AttendanceTracker(flask.Flask):
    """Flask application entry point."""

    def get_db(self) -> sqlite3.Connection:
        """Create connection to db, called at each request."""
        if "db" not in flask.g:
            self.db = sqlite3.connect(
                flask.current_app.config["DATABASE"],
            )

        return self.db

    def close_db(self, exc: BaseException | None = None) -> None:
        """Close DB connection on app tear down."""
        db: sqlite3.Connection = flask.g.pop("db", None)

        if db is not None:
            db.close()
