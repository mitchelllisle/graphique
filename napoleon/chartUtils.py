import altair as alt
import c3p0
import martha
import pandas as pd

def removeExplicitTypes(x):
    types = [":T", ":Q", ":O", ":N"]
    for type in types:
        x = x.replace(type, "")
    return x

def calcSizes(data, x, width):
    """
    User in bar chart to make sure the barsizes
    are consistent with the amount of data that is
    passed.
    """
    cleanX = removeExplicitTypes(x)

    xRange = len(data[cleanX].unique())
    barSize = (width / xRange)
    padding = (barSize / 2) + 1
    return barSize, padding

def determineColorEncoding(data, color = None, palette = None):
    """
    Used internally only. Makes it posible to
    dynamically choose a color or default color
    in any chart.
    """
    if color == None:
        applyColor = alt.Color()
    else:
        palette = generatePallette(palette)
        cleanColor = removeExplicitTypes(color)
        domainToApply = data[cleanColor].unique().tolist()
        applyColor = alt.Color(cleanColor, scale=alt.Scale(domain = domainToApply, range = palette['colours']))
    return applyColor

def generatePallette(name = None):
    try:
        if name == None:
            name = "Tableau"

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

        Tableau = {
            "name" : "Tableau",
            "Usage" : "Qualitative",
            "colours" : ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF']
        }

        BigDatr = {
            "name" : "BigDatr",
            "Usage" : "Qualitative",
            "colours" : ['#FAD748', '#2F6289', '#AA86FC', '#F2BD67', '#A3D369', '#24B4ED', '#B9D9FF', '#FD6A66', '#B74946']
        }

        return eval(name)
    except NameError as err:
        raise ValueError("Name '" + name + "' not recognised. Must be one of FastFox, IcyImp")
