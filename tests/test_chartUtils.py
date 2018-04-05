import pytest
from napoleon import generateLayout
from napoleon import generateTraces
from napoleon import generateColours
import numpy as np
import pandas as pd

layoutExpectedResult = "<class 'plotly.graph_objs.graph_objs.Layout'>"

# Test Definitions
def testGenerateLayout():
    layout = generateLayout("Line", None, "Test Title Line Chart", "Test Subtitle Line Chart")
    layoutType = str(type(layout))
    assert layoutType == layoutExpectedResult


def testGenerateTraces_histChart():
    df = pd.DataFrame({'CategoryOne':np.random.normal(0, 0.8, 1000),
                   'CategoryTwo':np.random.normal(-2, 1, 1000),
                   'CategoryThree':np.random.normal(3, 2, 1000)})

    traces = generateTraces("Histogram", df, x = ['CategoryOne', 'CategoryTwo', 'CategoryThree'], y = None, z = None, colour = "red")
    assert len(traces) == 3

def testGenerateTraces_heatmapChart():
    data = pd.read_csv("data/uberData.csv")
    traces = generateTraces("Heatmap", data, x = "weekday", y = "hour", z = "count", colour = "red")
    assert len(traces[0].keys()) == 4

def testGenerateTraces_columnChart():
    data = pd.read_csv("data/amazonStocks.csv")
    traces = generateTraces("Column", data, x = "date", y = ["price"], z = None, colour = ["google"])
    assert len(traces[0].keys()) == 5

def testGenerateTraces_barChart():
    data = pd.read_csv("data/amazonStocks.csv")
    traces = generateTraces("Column", data, x = "date", y = ["price"], z = None, colour = ["google"], orientation = "h")
    assert len(traces[0].keys()) == 6

def testGenerateTraces_lineChart():
    data = pd.read_csv("data/amazonStocks.csv")
    traces = generateTraces("Line", data, x = "date", y = ["price"], z = None, colour = ["google"])
    assert len(traces[0].keys()) == 6
    
def testGenerateTraces_scatterChart():
    data = pd.read_csv("data/amazonStocks.csv")
    traces = generateTraces("Scatter", data, x = "date", y = ["price"], z = None, colour = ["google"])
    assert len(traces[0].keys()) == 6

def testGenerateTraces_areaChart():
    data = pd.read_csv("data/amazonStocks.csv")
    traces = generateTraces("Area", data, x = "date", y = ["price"], z = None, colour = ["google"])
    assert len(traces[0].keys()) == 7


def testGenerateColours_google():
    colours = generateColours("google")
    assert len(colours) == 4

def testGenerateColours_bigdatr():
    colours = generateColours("bigdatr")
    assert len(colours) == 6

def testGenerateColours_colorbrewer():
    colours = generateColours("colorbrewer")
    assert len(colours) == 10

def testGenerateColours_colorbrewer_dark():
    colours = generateColours("colorbrewer_dark")
    assert len(colours) == 8

def testGenerateColours_custom():
    colours = generateColours(["#FD6966", "#4791E5"])
    assert len(colours) == 2
