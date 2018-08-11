import pytest
from napoleon import calcSizes
import numpy as np
import pandas as pd

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")

stocks = pd.read_csv("data/stocks.csv")
amazonStocks = stocks.query("symbol == 'AMZN'")
uberData = pd.read_csv("data/uberData.csv")

def test_calcSizes():
    chartDims = calcSizes(stocks, "date", 1000)
    assert chartDims[0] == 8.130081300813009
    assert chartDims[1] == 5.065040650406504
