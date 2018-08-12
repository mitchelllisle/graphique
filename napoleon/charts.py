from .chartUtils import calcSizes
import altair as alt
import c3p0
import martha
import pandas as pd

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")
# data = pd.read_csv("data/stocks.csv")

dim = [1000, 400]

def barChart(data, x, y, color = None, stack = "zero", y2 = None, width = dim[0], height = dim[1]):
    """
    barChart(data, "date:T", "price:Q")
    """
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_bar(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(color),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def lineChart(data, x, y, color = None, stack = None, y2 = None, width = dim[0], height = dim[1]):
    """
    lineChart(data, "date:T", "price:Q", "symbol")
    """
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_line(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(color),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def areaChart(data, x, y, color = None, stack = None, y2 = None, width = dim[0], height = dim[1]):
    """
    areaChart(data, "date:T", "price:Q", "symbol:N")
    """
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_area(opacity = 0.5).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(color),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )

    if stack != 'normalize':
        line = lineChart(data, x, y, color, y2, height, width)
        chart = chart + line
    return chart
