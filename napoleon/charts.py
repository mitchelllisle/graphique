from .chartUtils import calcSizes
from .chartUtils import determineColorEncoding
import altair as alt
import c3p0
import martha
import pandas as pd

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")
# data = pd.read_csv("data/stocks.csv")

dim = [1000, 400]

def bar(data, x, y, color = None, stack = "zero", y2 = None, width = dim[0], height = dim[1], palette = "Tableau"):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_bar(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def line(data, x, y, color = None, stack = None, y2 = None, width = dim[0], height = dim[1], palette = "Tableau"):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_line(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart


def scatter(data, x, y, color = None, stack = None, size = 500, y2 = None, width = dim[0], height = dim[1], palette = "Tableau"):
    chart = alt.Chart(data).mark_circle(size = size).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def area(data, x, y, color = None, stack = None, y2 = None, width = dim[0], height = dim[1], palette = "Tableau"):
    dims = calcSizes(data, x, width)

    areaChart = alt.Chart(data).mark_area(opacity = 0.5).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )

    if stack != 'normalize':
        lineChart = line(data, x, y, color, y2, height, width)
        chart = areaChart + lineChart
    return chart
