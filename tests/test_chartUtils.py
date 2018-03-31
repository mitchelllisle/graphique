import pytest
from napoleon import generateLayout
from napoleon import generateTraces
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
    

# Run Functions
## Layouts
testGenerateLayout()

## Traces
testGenerateTraces_histChart()
testGenerateTraces_heatmapChart()