from .chartUtils import generateTraces
from .chartUtils import generateLayout
from .chartUtils import generateColours
import plotly.offline as py
import plotly.graph_objs as go

def lineChart(data, x, y, colour = "google", title = "", subtitle = ""):
    chartType = "Line"
    barMode = None
    z = None
    colour = generateColours(colour)

    traces = generateTraces(chartType, data, x, y, z, colour)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart


def columnChart(data, x, y, colour = "google", title = "", subtitle = ""):
    chartType = "Column"
    barMode = None
    z = None
    
    colour = generateColours(colour)

    traces = generateTraces(chartType, data, x, y, z, colour)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart

def barChart(data, x, y, colour = "google", title = "", subtitle = ""):
    chartType = "Column"
    barMode = None
    z = None
    
    pal = generateColours(colour)

    traces = generateTraces(chartType, data, x, y, z, pal, orientation = "h")

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart

def histChart(data, x, colour = "google", title = "", subtitle = ""):
    chartType = "Histogram"
    barMode = "overlay"
    y = None
    z = None

    pal = generateColours(colour)

    traces = generateTraces("Histogram", data, x, y, z, colour)

    layout = generateLayout(chartType, barMode, title = title, subtitle = subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart


def heatmapChart(data, x, y, z, title = "", subtitle = ""):
    chartType = "Heatmap"
    barMode = None
    colour = None

    traces = generateTraces(chartType, data, x, y, z, colour)

    layout = generateLayout(chartType, barMode, title = title, subtitle = subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart

def areaChart(data, x, y, colour = "google", title = "", subtitle = ""):
    chartType = "Area"
    barMode = None
    z = None
    colour = generateColours(colour)

    traces = generateTraces(chartType, data, x, y, z, colour)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart