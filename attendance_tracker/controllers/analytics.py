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
    chart_config = _create_chart()  # default empty plot
    summary_table: dict[str, tuple[float | int, str]] = {}  # empty stats table

    if flask.request.method == "POST":
        # read form inputs
        location = flask.request.form.get("location") or ""
        start = flask.request.form.get("start_date") or ""
        end = flask.request.form.get("end_date") or ""
        result = re.match(r"(.+) (\d+)", location)

        if all((location, start, end)) and result is not None:
            building, room = result.groups()
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
                query,
                (building, room, start, end),
            ).fetchall()
            x_axis = []
            y_axis = []
            for accesses, date in results:
                x_axis.append(date)
                y_axis.append(accesses)

            total = sum(y_axis)
            # summary table has format "Stat Label" | "Value" | "Date Occurred"
            summary_table["Min"] = min(results, key=lambda i: i[0])
            summary_table["Avg"] = (
                total / len(y_axis),
                "-",
            )
            summary_table["Max"] = max(results, key=lambda i: i[0])
            summary_table["Total"] = total, "-"

            chart_config = _create_chart(
                "line",
                x_axis,
                [Series(f"{building} {room}", y_axis)],
            )
            # TODO (Anyone): improve error handling for query fail

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

    # TODO (Gavin): Add debounce on form submit so we dont lock DB lol
    return flask.render_template(
        "data_view.html",
        chart_config=json.dumps(chart_config),
        summary_table=summary_table,
        locations=locations,
    )


@ANALYTICS.route("/usage", methods=["GET", "POST"])
def usage() -> str:
    """View usage of all rooms over the last 3 months."""
    with flask.current_app.app_context():
        conn: sqlite3.Connection = flask.current_app.get_db()  # type: ignore
    chart_config = _create_chart()  # default empty plot

    if flask.request.method == "POST":
        # read form inputs
        start = flask.request.form.get("start_date") or ""
        end = flask.request.form.get("end_date") or ""

        if start and end:
            query = """
                    SELECT
                        building || ' ' || room_num AS location,
                        SUM(times_accessed) AS num_accesses
                    FROM
                        input_data
                    WHERE
                        date_entered BETWEEN ? AND ?
                    GROUP BY
                        location
                    ORDER BY
                        num_accesses DESC;
                    """
            results = conn.execute(
                query,
                (start, end),
            ).fetchall()
            x_axis = []
            y_axis = []
            for location, accesses in results:
                x_axis.append(location)
                y_axis.append(accesses)

            chart_config = _create_chart(
                "bar",
                x_axis,
                [Series("Number of Accesses", y_axis)],
            )
            # TODO (Anyone): improve error handling for query fail

    # must be GET method
    return flask.render_template(
        "room_usage.html",
        chart_config=json.dumps(chart_config),
    )


class _ChartJSConfig(TypedDict):
    type: Literal["bar", "line"]
    data: dict
    options: dict


class Series(NamedTuple):
    """A series is a list of data with a name str and accompanying y values."""

    name: str
    points: list[int | float]


def _create_chart(
    type: Literal["bar", "line"] = "line",
    x_vals: Sequence[int | float] | None = None,
    datasets: Sequence[Series] | None = None,
) -> _ChartJSConfig:
    """Create a chart from the given data."""
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
        "scales": {
            "x": {
                "display": True,
                "title": {
                    "display": True,
                    "text": "Week",
                },
            },
            "y": {
                "display": True,
                "title": {
                    "display": True,
                    "text": "Number of Accesses",
                },
            },
        },
    }

    return _ChartJSConfig(
        type=type,
        data=data,
        options=options,
    )


def _create_bar_chart(
    x_vals: Sequence[int | float] | None = None,
    datasets: Sequence[Series] | None = None,
) -> _ChartJSConfig:
    """Create a bar chart from the given data."""
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
        "scales": {
            "x": {
                "display": True,
                "title": {
                    "display": True,
                    "text": "Week",
                },
            },
            "y": {
                "display": True,
                "title": {
                    "display": True,
                    "text": "Number of Accesses",
                },
            },
        },
    }

    return _ChartJSConfig(
        type="bar",
        data=data,
        options=options,
    )
