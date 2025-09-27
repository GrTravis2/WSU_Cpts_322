"""JSON endpoints where data enters the web app."""

from __future__ import annotations

from flask import Blueprint

INGEST_BP = Blueprint(
    name="ingest",
    import_name=__name__,
    url_prefix="/j/ingest",
)
