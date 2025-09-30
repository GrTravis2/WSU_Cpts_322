"""Endpoints for doing admin tasks for the attendance tracker."""

from __future__ import annotations

from flask import Blueprint

ADMIN = Blueprint(
    name="admin",
    import_name=__name__,
    url_prefix="/h/admin",
)
