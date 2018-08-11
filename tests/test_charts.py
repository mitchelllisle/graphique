import altair as alt
import pytest
import numpy as np
import pandas as pd

from napoleon import lineChart
from napoleon import areaChart
from napoleon import barChart

from napoleon import calcSizes

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")

stocks = pd.read_csv("data/stocks.csv")
amazonStocks = stocks.query("symbol == 'AMZN'")
uberData = pd.read_csv("data/uberData.csv")

def test_lineChart():
    chart = lineChart(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.Chart

def test_barChart():
    chart = barChart(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.Chart

def test_areaChart():
    chart = areaChart(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.Chart
