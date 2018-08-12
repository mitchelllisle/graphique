import altair as alt
import c3p0
import martha
import pandas as pd

def calcSizes(data, x, width):
    """
    User in bar chart to make sure the barsizes
    are consistent with the amount of data that is
    passed.
    """
    types = [":T", ":Q", ":O", ":N"]
    for type in types:
        x = x.replace(type, "")

    xRange = len(data[x].unique())
    barSize = (width / xRange)
    padding = (barSize / 2) + 1
    return barSize, padding

def determineColorEncoding(color):
    """
    Used internally only. Makes it posible to
    dynamically choose a color or default color
    in any chart.
    """
    if color == None:
        applyColor = alt.Color()
    else:
        applyColor = alt.Color(color)
    return applyColor

def generatePallette(name = None):
    try:
        if name == None:
            name = "FastFox"

        FastFox = {
            "name" : "FastFox",
            "Usage" : "Qualitative",
            "colours" : ['#CF6766', '#30415D', '#031424', '#8EAEBD']
        }

        IcyImp = {
            "name" : "IcyImp",
            "Usage" : "Qualitative",
            "colours" : ['#99D3DF', '#88BBD6', '#CDCDCD', '#E9E9E9']
        }
        return eval(name)
    except NameError as err:
        raise Exception("Name '" + name + "' not recognised. Must be one of FastFox, IcyImp")
