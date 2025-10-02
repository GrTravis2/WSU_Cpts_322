"""Endpoints that output analytic data."""

from __future__ import annotations

from flask import Blueprint, render_template

ANALYTICS = Blueprint(
    name="analytics",
    import_name=__name__,
    url_prefix="/h/analytics",
)


@ANALYTICS.route("/analytics")
def analytics():
    """Render the analytics view page.

    Name and title serve as variables for templates.
    """
    return render_template(
        "analytics.html", name="ANALYTICS PAGE", title="ANALYTIC VIEW"
    )
