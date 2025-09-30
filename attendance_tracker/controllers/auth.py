"""Endpoints that allows users to log into the system."""

from __future__ import annotations

from flask import Blueprint

AUTH = Blueprint(
    name="auth",
    import_name=__name__,
    url_prefix="/h/auth",
)
