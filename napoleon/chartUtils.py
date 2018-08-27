import altair as alt
import c3p0
import martha
import pandas as pd
import numpy as np
import random

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

def sizeEval(data, size, range):
    if type(size) == np.int:
        computedSize = alt.value(size)
        return computedSize
    elif size in data.columns:
        cleanSize = removeExplicitTypes(size)
        computedSize = alt.Size(cleanSize, type = "quantitative", scale=alt.Scale(range=range))
        return computedSize
    else:
        raise ValueError("Couldn't parse size argument. Must either an integer or a field in the data provided.")

def determineColorEncoding(data, color = None, palette = None):
    """
    Used internally only. Makes it posible to
    dynamically choose a color or default color
    in any chart.
    """
    if color == None:
        applyColor = alt.Color()
    elif palette == None and color not in data.columns:
        applyColor = alt.ColorValue(color)
    else:
        palette = generatePallette(palette)
        cleanColor = removeExplicitTypes(color, len(data[cleanColor].unique().tolist()))
        domainToApply = data[cleanColor].unique().tolist()
        applyColor = alt.Color(cleanColor, scale=alt.Scale(domain = domainToApply, range = palette['colours']))
    return applyColor


def colors(n):
  ret = []
  r = int(random.random() * 256)
  g = int(random.random() * 256)
  b = int(random.random() * 256)
  step = 256 / n
  for i in range(n):
    r += step
    g += step
    b += step
    r = int(r) % 256
    g = int(g) % 256
    b = int(b) % 256
    ret.append((r,g,b))
    hexes = rgbToHex(ret)
  return hexes

def rgbToHex(rgbs):
    hexes = []
    for rgb in rgbs:
        hex = '#%02x%02x%02x' % rgb
        hexes.append((hex))
    return hexes

def generatePallette(name = "Random", n = 10):
    try:
        Random = {
                "name" : "Randomly Generated Palette",
                "Usage" : "Misc",
                "colours" : colors(n)

        }

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
            "colours" : ['#FAD748', '#FD6A66', '#2F6289', '#AA86FC', '#F2BD67', '#A3D369', '#24B4ED', '#B9D9FF', '#B74946']
        }

        return eval(name)
    except NameError as err:
        raise ValueError("Name '" + name + "' not recognised. Must be one of FastFox, IcyImp")
