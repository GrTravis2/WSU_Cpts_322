"""Endpoints for doing admin tasks for the attendance tracker."""

from __future__ import annotations

import sqlite3

import flask

ADMIN = flask.Blueprint(
    name="admin",
    import_name=__name__,
    url_prefix="/h/admin",
)


@ADMIN.route("/clubs", methods=["GET", "POST"])
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
