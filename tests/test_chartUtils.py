import pytest
from napoleon import generateLayout
from napoleon import generateTraces
import numpy as np
import pandas as pd

layoutExpectedResult = "<class 'plotly.graph_objs.graph_objs.Layout'>"

# Test Definitions
def testGenerateLayout_lineChart():
    layout = generateLayout("Line", None, "Test Title Line Chart", "Test Subtitle Line Chart")
    layoutType = str(type(layout))
    assert layoutType == layoutExpectedResult
    
def testGenerateLayout_columnChart():
    layout = generateLayout("Column", None, "Test Title Column Chart", "Test Subtitle Column Chart")
    layoutType = str(type(layout))
    assert layoutType == layoutExpectedResult
    
def testGenerateLayout_histChart():
    layout = generateLayout("Histogram", "overlay", "Test Title Column Chart", "Test Subtitle Column Chart")
    layoutType = str(type(layout))
    assert layoutType == layoutExpectedResult
    

def testGenerateTraces_histChart():
    df = pd.DataFrame({'CategoryOne':np.random.normal(0, 0.8, 1000),
                   'CategoryTwo':np.random.normal(-2, 1, 1000),
                   'CategoryThree':np.random.normal(3, 2, 1000)})
    
    traces = generateTraces("Histogram", df, x = ['CategoryOne', 'CategoryTwo', 'CategoryThree'], y = None, z = None, color = "red")
    assert len(traces) == 3
    

# Run Functions
## Layouts
testGenerateLayout_lineChart()
testGenerateLayout_columnChart()
testGenerateLayout_histChart()

## Traces
testGenerateTraces_histChart()
