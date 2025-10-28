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


@ADMIN.route("/add-club", methods=["GET", "POST"])
def add_club():
    """Add a club to the db."""
    conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
    cursor = conn.cursor()
    if flask.request.method == "POST":
        print(
            flask.request.form
        )  # making sure all the info is getting to this route from the form
        club_data = list(flask.request.form.values())
        result = cursor.fetchone()
        if result:
            # TODO Ingrid: add logic for finding duplicate line
            pass
        else:
            with flask.current_app.app_context():
                cursor.execute(
                    "INSERT INTO CLUB_DATA\
                    VALUES (?,?,?,?,?,?)",
                    club_data,
                )
                conn.commit()
            # TODO Ingrid: have this return to a redirected url
    # back to the add form
    return flask.render_template("add_club.html")


@ADMIN.route("/assign-room-to-club", methods=["GET", "POST"])  # type: ignore
def assign_club():
    """Assign a room to a club."""
    conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
    cursor = conn.cursor()
    if flask.request.method == "POST":
        club_name = flask.request.form["assigned_club"]
        cursor.execute(
            """SELECT assigned_club
                              FROM ROOM_LOG
                              where assigned_club=?""",
            (club_name,),
        )
        result = cursor.fetchone()
        if result:
            # notify user and don't insert
            flask.flash("Club already assigned to room!")
            # redirect url to list of actively linked clubs
            pass
        else:
            club_data = list(flask.request.form.values())
            print(club_data)
            with flask.current_app.app_context():
                conn.cursor().execute(
                    "INSERT INTO room_log\
                    VALUES (?,?,?)",
                    club_data,
                )
                conn.commit()
    return flask.render_template("assign_club.html")
