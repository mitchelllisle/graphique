from .chartUtils import generateTraces
from .chartUtils import generateLayout
from .chartUtils import generateColours
from .chartUtils import evaluateTraceType
from .chartUtils import createChart
import plotly.offline as py
import plotly.graph_objs as go

def lineChart(data, x, y, group = None, colour = "google", title = "", subtitle = "", saveAs = None):
    chartType = "Line"
    barMode = None
    z = None
    pal = generateColours(colour)
    
    traces = evaluateTraceType(chartType, data, x, y, z, pal, group)
    
    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    
    chart = createChart(plot, saveAs)
    
    return chart

def areaChart(data, x, y, group = None, colour = "google", title = "", subtitle = "", saveAs = None):
    chartType = "Area"
    barMode = None
    z = None
    pal = generateColours(colour)

    traces = evaluateTraceType(chartType, data, x, y, z, pal, group)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)

    chart = createChart(plot, saveAs)

    return chart

def scatterChart(data, x, y, group = None, colour = "google", title = "", subtitle = "", saveAs = None):
    chartType = "Scatter"
    barMode = None
    z = None
    pal = generateColours(colour)
    
    traces = evaluateTraceType(chartType, data, x, y, z, pal, group)
    
    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    
    chart = createChart(plot, saveAs)
    
    return chart


def columnChart(data, x, y, group = None, colour = "google", title = "", subtitle = "", saveAs = None, barMode = None):
    chartType = "Column"
    barMode = barMode
    z = None
    
    pal = generateColours(colour)

    traces = evaluateTraceType(chartType, data, x, y, z, pal, group)

    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)
    
    chart = createChart(plot, saveAs)

    return chart

def barChart(data, x, y, group = None, colour = "google", title = "", subtitle = "", saveAs = None):
    chartType = "Column"
    barMode = None
    z = None
    
    pal = generateColours(colour)
    
    traces = evaluateTraceType(chartType, data, x, y, z, pal, group, orientation = "h")
    
    layout = generateLayout(chartType, barMode, title, subtitle)

    plot = go.Figure(data = traces, layout = layout)

    chart = createChart(plot, saveAs)
 
    return chart


def histChart(data, x,  group = None, colour = "google", title = "", subtitle = "", saveAs = None):
    chartType = "Histogram"
    barMode = "overlay"
    y = None
    z = None

    pal = generateColours(colour)

    traces = evaluateTraceType(chartType, data, x, y, z, pal, group)

    layout = generateLayout(chartType, barMode, title = title, subtitle = subtitle)

    plot = go.Figure(data = traces, layout = layout)

    chart = createChart(plot, saveAs)
 
    return chart



def heatmapChart(data, x, y, z,  group = None, title = "", subtitle = "", saveAs = None):
    chartType = "Heatmap"
    barMode = None
    pal = None

    traces = generateTraces(chartType, data, x, y, z, pal)

    layout = generateLayout(chartType, barMode, title = title, subtitle = subtitle)

    plot = go.Figure(data = traces, layout = layout)

    chart = createChart(plot, saveAs)
 
    return chart
