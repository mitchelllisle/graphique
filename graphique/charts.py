from .chartUtils import generateTraces
from .chartUtils import generateLayout
import plotly.offline as py
import plotly.graph_objs as go

def lineChart(data, x, y, color = None, title = "", subtitle = ""):
    chartType = "Line"
    barMode = None

    if color is None:
        color = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]

    traces = generateTraces(chartType, data, x, y, color)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart


def columnChart(data, x, y, color = None, title = "", subtitle = ""):
    chartType = "Column"
    barMode = None

    if color is None:
        color = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]

    traces = generateTraces(chartType, data, x, y, color)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart

def histChart(data, x, color = None, title = "", subtitle = ""):
    chartType = "Histogram"
    barMode = "overlay"
    y = None
    if color is None:
        color = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]

    traces = generateTraces("Histogram", data, x, y, color)

    layout = generateLayout(chartType, barMode, title = title, subtitle = subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart