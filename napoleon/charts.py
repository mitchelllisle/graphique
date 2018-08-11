from .chartUtils import calcSizes
import altair as alt
import c3p0
import martha
import pandas as pd

dim = [1000, 400]

def barChart(data, x, y, color, stack = "zero", y2 = None, width = dim[0], height = dim[1]):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_bar(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = alt.Color(color),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart


def lineChart(data, x, y, color, y2 = None, width = dim[0], height = dim[1]):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_line(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y),
        color = alt.Color(color),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def areaChart(data, x, y, color, stack = None, y2 = None, width = dim[0], height = dim[1]):
    dims = calcSizes(data, x, width)

    line = lineChart(data, x, y, color, y2, height, width)

    chart = alt.Chart(data).mark_area(opacity = 0.5).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = alt.Color(color),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart + line
