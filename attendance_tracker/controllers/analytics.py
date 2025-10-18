"""Endpoints that output analytic data."""

from __future__ import annotations

import json
import random
from typing import Literal, NamedTuple, Sequence, TypedDict

import flask
from flask import Blueprint

ANALYTICS = Blueprint(
    name="analytics",
    import_name=__name__,
    url_prefix="/h/analytics",
)


@ANALYTICS.route("/data-view", methods=["GET", "POST"])
def data_view() -> flask.Response | str:
    """View data based on query entered using form."""
    # db = app.get_db
    chart_config = _create_line_chart()  # default empty plot
    rooms = [random.randrange(20, 400, 10) for _ in range(10)]

    if flask.request.method == "POST":
        f = flask.request.form
        if f["duration"] and f["room"]:  # form is filled out fully
            # TODO (Gavin): put the query here
            xs = [i for i in range(10)]
            dataset = Series(
                "accesses", list(random.randrange(0, 100) for _ in range(10))
            )
            chart_config = _create_line_chart(xs, [dataset])

    return flask.render_template(
        "data_view.html", chart_config=json.dumps(chart_config), rooms=rooms
    )


class _ChartJSConfig(TypedDict):
    type: Literal["bar", "line"]
    data: dict
    options: dict


class Series(NamedTuple):
    """A series is a list of data with a name str and accompanying y values."""

    name: str
    points: list[int | float]


def _create_line_chart(
    x_vals: Sequence[int | float] | None = None,
    datasets: Sequence[Series] | None = None,
) -> _ChartJSConfig:
    """Create a line chart from the given data."""
    if x_vals is not None and datasets is not None:
        data = {  # convert to dict if both lists present
            "labels": x_vals,
            "datasets": [{"label": n, "data": d} for n, d in datasets],
        }
    else:  # default to empty plot if both lists aren't there
        data = {
            "labels": [],
            "datasets": [{"label": ""}],
        }

    options = {  # adding these so the chart can be resized
        "responsive": True,
        "maintainAspectRatio": False,
    }

    return _ChartJSConfig(
        type="line",
        data=data,
        options=options,
    )
