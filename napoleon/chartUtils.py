import altair as alt
import c3p0
import martha
import pandas as pd

def calcSizes(data, x, width):
    types = [":T", ":Q", ":O", ":N"]
    for type in types:
        x = x.replace(type, "")

    xRange = len(data[x].unique())
    barSize = (width / xRange)
    padding = (barSize / 2) + 1
    return barSize, padding
