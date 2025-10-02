"""Endpoints that allows users to log into the system."""

from __future__ import annotations

from flask import Blueprint, render_template

AUTH = Blueprint(
    name="auth",
    import_name=__name__,
    url_prefix="/h/auth",
)


@AUTH.route("/login")
def login():
    """Render the login view page.

    Name and title serve as variables for templates.
    """
    return render_template("login.html", name="LOGIN PAGE", title="LOGIN VIEW")
