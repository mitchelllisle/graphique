import pytest
import numpy as np
import pandas as pd

from napoleon import lineChart
from napoleon import scatterChart
from napoleon import areaChart
from napoleon import columnChart
from napoleon import barChart
from napoleon import histChart
from napoleon import heatmapChart

from napoleon import generateLayout
from napoleon import generateTraces
from napoleon import generateColours
from napoleon import evaluateTraceType

stocks = pd.read_csv("data/stocks.csv")
amazonStocks = stocks.query("symbol == 'AMZN'")
uberData = pd.read_csv("data/uberData.csv")

def test_lineChart():
    lineChart(data = amazonStocks,
       x = "date",
       y = 'price',
        title = "Amazon Stock",
        subtitle = "The Amazon stock price form 2000 - 2010",
       colour = "bigdatr",
       saveAs = "line.html")
    
def test_multiLineChart():
    lineChart(data = stocks, 
         x = "date", 
         y = "price",
         group = "symbol",
         title = "Amazon, Apple, Google, Microsoft Stock Price",
         subtitle = "Stock prices form 2000 - 2010",
         colour = "colorbrewer_dark",
         saveAs = "multiLine.html")
    
def test_scatterChart():
    scatterChart(data = amazonStocks,
       x = "date",
       y = 'price',
        title = "Amazon Stock",
        subtitle = "The Amazon stock price form 2000 - 2010",
       colour = "bigdatr",
       saveAs = "scatter.html")

def test_areaChart():
    areaChart(data = amazonStocks,
       x = "date",
       y = 'price',
        title = "Amazon Stock",
        subtitle = "The Amazon stock price form 2000 - 2010",
       colour = "bigdatr",
       saveAs = "area.html")


def test_columnChart():
    columnChart(data = amazonStocks,
        x = "date",
        y = 'price',
        title = "Amazon Stock",
        subtitle = "The Amazon stock price form 2000 - 2010",
       colour = "bigdatr",
       saveAs = "column.html")

def test_barChart():
    barChart(data = amazonStocks,
        x = "date",
        y = 'price',
        title = "Amazon Stock",
        subtitle = "The Amazon stock price form 2000 - 2010",
       colour = "bigdatr",
       saveAs = "bar.html")

def test_histChart():
    histChart(data = amazonStocks,
        x = ["price"],
        title = "Amazon Stock",
        subtitle = "The Amazon stock price form 2000 - 2010",
       colour = "bigdatr",
       saveAs = "hist.html")

def test_heatmapChart():
    heatmapChart(uberData,
                x = "weekday",
                y = "hour",
                z = "count",
                title = "Heatmap of Time of Day vs Day of Week",
                saveAs = "heatmap.html")
