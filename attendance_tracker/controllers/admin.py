"""Endpoints for doing admin tasks for the attendance tracker."""

from __future__ import annotations

import sqlite3

import flask

from attendance_tracker.controllers import auth

ADMIN = flask.Blueprint(
    name="admin",
    import_name=__name__,
    url_prefix="/h/admin",
)


@ADMIN.route("/home", methods=["GET"])
@auth.required
def home() -> str | flask.Response:
    """Home page for navigating to admin functions."""
    return flask.render_template(
        "index.html",  # make actual home page later
    )


@ADMIN.route("/clubs", methods=["GET", "POST"])
@auth.required
def club_info() -> str:
    """View all clubs that have info saved in the system."""
    with flask.current_app.app_context():
        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore

    # query all the clubs here and return data view
    # note that submitting on a target club should include URL to jump to,
    # see base.html nav bar links, similar idea
    # query = "SELECT BUILDING, ROOM_NUM, ASSIGNED_CLUB FROM ROOM_LOG"
    # clubs: list[str] = conn.execute(query).fetchall()
    conn.execute("")
    clubs: list[tuple[str, int, str]] = [(str(i), i, str(i)) for i in range(10)]

    return flask.render_template(
        "club_search.html",
        clubs=clubs,
    )


@ADMIN.route("/club-config/<club_name>", methods=["GET", "POST"])
@auth.required
def club_config(club_name: str = "") -> str:
    """View club specific information and update."""
    with flask.current_app.app_context():
        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore

    # query = f"SELECT * FROM CLUB_DATA WHERE CLUB_NAME={club_name}"
    # club = conn.execute(query).fetchone()
    conn.execute("")
    club = ("club", "name", "email", "size", "advisor", "advisor email")

    return flask.render_template(
        "club_config.html",
        club=club,
    )
