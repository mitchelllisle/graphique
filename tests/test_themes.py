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

def test_darkTheme():
    themeActive = activateTheme("darkTheme")()
    assert themeActive == darkTheme()

def test_greyTheme():
    themeActive = activateTheme("greyTheme")()
    assert themeActive == greyTheme()

def test_wrongTheme():
    try:
        activateTheme("NONE")()
    except Exception as e:
        assert type(e) == Exception
