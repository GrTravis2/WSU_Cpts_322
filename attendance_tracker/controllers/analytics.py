"""Endpoints that output analytic data."""

from __future__ import annotations

import json
import re
import sqlite3
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
    with flask.current_app.app_context():
        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
    chart_config = _create_line_chart()  # default empty plot

    if flask.request.method == "POST":
        # read form inputs
        location: str = flask.request.form.get("location") or ""
        start = flask.request.form.get("start_date") or ""
        end = flask.request.form.get("end_date") or ""
        result = re.match(r"(.+) (\d+)", location)

        if all((location, start, end)) and result is not None:
            match result.groups():
                case building, room:
                    query = """
                            SELECT
                             times_accessed, date_entered
                            FROM
                             input_data
                            WHERE
                                building = ? AND
                                room_num = ? AND
                                date_entered BETWEEN ? AND ?
                            ORDER BY
                                date_entered
                            """
                    results = conn.execute(
                        query, (building, room, start, end)
                    ).fetchall()
                    x_axis = []
                    y_axis = []
                    for accesses, date in results:
                        x_axis.append(date)
                        y_axis.append(accesses)

                    chart_config = _create_line_chart(
                        x_axis,
                        [Series(f"{building} {room}", y_axis)],
                    )
                case _:
                    pass  # TODO (Anyone): improve error handling for query fail

    # must be GET method
    # TODO (Gavin): Figure out how to cache location query for repeat visits
    query = """
        SELECT DISTINCT
            building, room_num
        FROM
            input_data
        ORDER BY
            room_num
        """
    locations = conn.execute(query).fetchall()
    locations.sort(key=lambda i: i[1])

    return flask.render_template(
        "data_view.html",
        chart_config=json.dumps(chart_config),
        locations=locations,
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
