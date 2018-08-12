import pytest
from napoleon import calcSizes
from napoleon import determineColorEncoding
from napoleon import generatePallette
import numpy as np
import pandas as pd
import altair as alt

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")

stocks = pd.read_csv("data/stocks.csv")
amazonStocks = stocks.query("symbol == 'AMZN'")
uberData = pd.read_csv("data/uberData.csv")

def test_calcSizes():
    chartDims = calcSizes(stocks, "date", 1000)
    assert chartDims[0] == 8.130081300813009
    assert chartDims[1] == 5.065040650406504

def test_determineColorEncoding():
    colorPassed = determineColorEncoding("stocks")
    noColorPassed = determineColorEncoding(None)
    assert type(colorPassed) == alt.Color
    assert type(noColorPassed) == alt.Color


def test_determineColorEncoding():
    colorPassed = determineColorEncoding("stocks")
    noColorPassed = determineColorEncoding(None)
    assert type(colorPassed) == alt.Color
    assert type(noColorPassed) == alt.Color


def test_generatePallette():
    defaultPallette = generatePallette()
    chosenPallette = generatePallette("IcyImp")
    assert defaultPallette['name'] == "FastFox"
    assert chosenPallette['name'] == "IcyImp"
