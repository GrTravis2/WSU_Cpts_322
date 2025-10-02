"""Endpoints that output analytic data."""

from __future__ import annotations

from flask import Blueprint

ANALYTICS = Blueprint(
    name="analytics",
    import_name=__name__,
    url_prefix="/h/analytics",
)
