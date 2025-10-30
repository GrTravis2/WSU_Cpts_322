"""Endpoints for doing admin tasks for the attendance tracker."""

from __future__ import annotations

import sqlite3

import flask

from attendance_tracker.controllers import auth
from attendance_tracker.types import tables

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
        "admin_home.html",  # make actual home page later
    )


@ADMIN.route("/clubs", methods=["GET", "POST"])
@auth.required
def club_info() -> str:
    """View all clubs that have info saved in the system."""
    with flask.current_app.app_context():
        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore

    query = """
        SELECT
            building, room_num, assigned_club
        FROM
            room_log
        ORDER BY
            building, room_num
        """
    clubs = conn.execute(query).fetchall()

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

    query = """
        SELECT
            *
        FROM
            club_data
        WHERE
            club_name = ?
        """
    # club = conn.execute(query).fetchone()
    dummy = tables.ClubData(
        club_name="Crimson Robotics",
        club_president="Derek",
        email="email",
        club_size=10,
        club_advisor="Dr. Derek",
        club_advisor_email="email",
    )
    club = conn.execute(query, (club_name,)).fetchone() or dummy

    return flask.render_template(
        "club_config.html",
        club_name=club_name,
        club=club,
    )


@ADMIN.route("/add-club", methods=["GET", "POST"])
@auth.required
def add_club():
    """Add a club to the db."""
    if flask.request.method == "POST":
        print(
            flask.request.form
        )  # making sure all the info is getting to this route from the form
        club_data = list(flask.request.form.values())
        with flask.current_app.app_context():
            conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
            conn.cursor().execute(
                "INSERT INTO CLUB_DATA\
                VALUES (?,?,?,?,?,?)",
                club_data,
            )
            conn.commit()
        # TODO: have this return to a redirected url

    # back to the add form
    return flask.render_template("add_club.html")


@ADMIN.route("/assign-room-to-club", methods=["GET", "POST"])  # type: ignore
@auth.required
def assign_club():
    """Assign a room to a club."""
    if flask.request.method == "POST":
        print(flask.request.form)
        club_data = list(flask.request.form.values())
        with flask.current_app.app_context():
            conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
            conn.cursor().execute(
                "INSERT INTO ROOM_LOG\
                VALUES (?,?,?)",
                club_data,
            )
            conn.commit()
    return flask.render_template("assign_club.html")
