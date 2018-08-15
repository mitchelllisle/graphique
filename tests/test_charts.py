import altair as alt
import pytest
import numpy as np
import pandas as pd

from napoleon import line
from napoleon import area
from napoleon import bar
from napoleon import scatter

from napoleon import calcSizes
from napoleon import determineColorEncoding

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")

stocks = pd.read_csv("data/stocks.csv")
amazonStocks = stocks.query("symbol == 'AMZN'")
uberData = pd.read_csv("data/uberData.csv")

def test_line():
    chart = line(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.Chart

def test_bar():
    chart = bar(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.Chart

def test_scatter():
    chart = scatter(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.Chart

def test_area():
    chart = area(data = amazonStocks,
       x = "date",
       y = 'price',
       color = "symbol")
    assert type(chart) == alt.LayerChart
