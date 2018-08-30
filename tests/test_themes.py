import altair as alt
import pytest
import numpy as np
import pandas as pd

from napoleon import activateTheme
from napoleon import greyTheme
from napoleon import darkTheme

from napoleon import line

from napoleon import calcSizes
from napoleon import determineColorEncoding

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")

stocks = pd.read_csv("data/stocks.csv")
amazonStocks = stocks.query("symbol == 'AMZN'")
uberData = pd.read_csv("data/uberData.csv")

def test_darkTheme():
    themeActive = activateTheme("darkTheme")()
    assert themeActive == darkTheme()

def test_greyTheme():
    themeActive = activateTheme("greyTheme")()
    assert themeActive == greyTheme()
