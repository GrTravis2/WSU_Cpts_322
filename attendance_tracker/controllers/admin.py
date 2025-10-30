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
        "admin_home.html",  # make actual home page later
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

    query = "SELECT * FROM CLUB_DATA WHERE CLUB_NAME=?"
    club = conn.execute(query, (club_name,)).fetchone()

    return flask.render_template(
        "club_config.html",
        club=club,
    )


@ADMIN.route("/add-club", methods=["GET", "POST"])
@auth.required
def add_club():
    """Add a club to the db."""
    if flask.request.method == "POST":
        club = flask.request.form["club_name"]

        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
        cursor = conn.cursor()

        club_data = list(flask.request.form.values())

        cursor.execute(
            """SELECT CLUB_NAME
                FROM CLUB_DATA
                where CLUB_NAME=?""",
            (club,),
        )

        result = cursor.fetchone()
        if result:
            flask.flash("Club already exists!")
        else:
            cursor.execute(
                "INSERT INTO CLUB_DATA\
                VALUES (?,?,?,?,?,?)",
                club_data,
            )
            conn.commit()
        location = flask.url_for("admin.club_config", club_name=club)
        return flask.redirect(location)
    return flask.render_template("add_club.html")


@ADMIN.route("/assign-room-to-club", methods=["GET", "POST"])  # type: ignore
@auth.required
def assign_club():
    """Assign a room to a club."""
    if flask.request.method == "POST":
        club = flask.request.form["assigned_club"]

        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
        cursor = conn.cursor()

        club_data = list(flask.request.form.values())

        cursor.execute(
            """SELECT ASSIGNED_CLUB
                FROM ROOM_LOG
                where ASSIGNED_CLUB=?""",
            (club,),
        )

        result = cursor.fetchone()

        if result:
            return flask.render_template("assign_club.html")
        else:
            conn.cursor().execute(
                "INSERT INTO ROOM_LOG\
                VALUES (?,?,?)",
                club_data,
            )
            conn.commit()
        location = flask.url_for("admin.club_config", club_name=club)
        return flask.redirect(location)
    return flask.render_template("assign_club.html")


@ADMIN.route("/dashboard")  # type: ignore
def admin_profile():
    """Go to user dashboard."""
    auth = "uid" in flask.session
    return flask.render_template("admin_home.html", authenticated=auth)
