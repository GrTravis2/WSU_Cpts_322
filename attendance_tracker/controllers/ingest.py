"""JSON endpoints where data enters the web app."""

from __future__ import annotations

import flask

INGEST = flask.Blueprint(
    name="ingest",
    import_name=__name__,
    url_prefix="/j/ingest",
)

INGEST.route("/upload-activity", methods=("POST"))


def upload_activity() -> flask.Response:
    """Club activity JSON sent to this URL to be stored in the app."""
    raise NotImplementedError
