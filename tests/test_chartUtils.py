import pytest
from napoleon import calcSizes
from napoleon import determineColorEncoding
from napoleon import generatePallette
from napoleon import sizeEval
import numpy as np
import pandas as pd
import altair as alt

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")

stocks = pd.read_csv("data/stocks.csv")

def test_calcSizes():
    chartDims = calcSizes(stocks, "date", 1000)
    assert chartDims[0] == 8.130081300813009
    assert chartDims[1] == 5.065040650406504

def test_determineColorEncoding():
    colorPassed = determineColorEncoding(stocks, "symbol", "Tableau")
    noColorPassed = determineColorEncoding(None)
    assert type(colorPassed) == alt.Color
    assert type(noColorPassed) == alt.Color

def test_sizeEval():
    sizeResults = sizeEval(stocks, 5000, [0,1000])
    sizeResultsField = sizeEval(stocks, "price", [0,1000])
    assert sizeResults['value'] == 5000
    assert type(sizeResultsField) == alt.Size
    try:
        sizeEval(stocks, "NotAField", [0,1])
    except Exception as e:
        assert type(e) == ValueError

def test_generatePallette():
    defaultPallette = generatePallette()
    chosenPallette = generatePallette("IcyImp")
    chosenPallette1 = generatePallette("FastFox")
    chosenPallette2 = generatePallette("BigDatr")
    noPalette = generatePallette(None)
    assert defaultPallette['name'] == "Randomly Generated Palette"
    assert chosenPallette['name'] == "IcyImp"
    assert chosenPallette1['name'] == "FastFox"
    assert chosenPallette2['name'] == "BigDatr"
    assert noPalette['name'] == "Tableau"
    try:
        generatePallette("NotAPalette")
    except Exception as e:
        assert type(e) == ValueError
