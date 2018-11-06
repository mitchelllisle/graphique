from .chartUtils import calcSizes
from .chartUtils import determineColorEncoding
from .chartUtils import sizeEval
import altair as alt
import martha
import pandas as pd
import numpy as np

# import os
# os.chdir("/Users/mitchell/Documents/projects/packages/napoleon")
# data = pd.read_csv("data/tameImpalaSongs.csv")
# data = data.groupby(["key_mode", "album_name"]).agg({"artist_name" : "count"}).reset_index()

dim = [1000, 400]

def bar(data, x, y, color = None, stack = "zero", y2 = None, width = dim[0], height = dim[1], palette = None):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_bar(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def hist(data, x, color = None, bins = 100, width = dim[0], height = dim[1], palette = None):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_area(
        opacity=0.3,
        interpolate='step'
    ).encode(
        x = alt.X(x, bin=alt.Bin(maxbins = bins)),
        y = alt.Y("count()", stack = None),
        color = determineColorEncoding(data, color, palette),
        tooltip = ["count()"]
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
)
    return chart

def line(data, x, y, color = None, stack = None, y2 = None, width = dim[0], height = dim[1], palette = None):
    dims = calcSizes(data, x, width)

    chart = alt.Chart(data).mark_line(size = dims[0]).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def scatter(data, x, y, color = None, size = 500, range = [0,5000], stack = None, y2 = None, width = dim[0], height = dim[1], palette = None):
    chart = alt.Chart(data).mark_circle().encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist(),
        size = sizeEval(data, size, range)
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = True
    )
    return chart

def area(data, x, y, color = None, stack = None, y2 = None, width = dim[0], height = dim[1], palette = None):
    dims = calcSizes(data, x, width)

    areaChart = alt.Chart(data).mark_area(opacity = 0.5).encode(
        x = alt.X(x),
        y = alt.Y(y, stack = stack),
        color = determineColorEncoding(data, color, palette),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )

    if stack != 'normalize':
        lineChart = line(data, x, y, color, y2, height, width)
        chart = areaChart + lineChart
    return chart

def heatmap(data, x, y, color, width = dim[0], height = dim[1], palette = None):
    chart = alt.Chart(data).mark_rect().encode(
        x = alt.X(x),
        y = alt.Y(y),
        color = alt.Color(color, scale=alt.Scale(scheme='greenblue')),
        tooltip = data.columns.tolist()
    ).properties(
        width = width,
        height = height
    ).interactive(
        bind_y = False
    )
    return chart

def boxplot(data, x, y, color = None, xtype='N', ytype='Q', size = 40, width = dim[0], height = dim[1], palette = None):
    # Define variables and their types using f-strings in Python
    lower_box=f'q1({y}):{ytype}'
    lower_whisker=f'min({y}):{ytype}'
    upper_box=f'q3({y}):{ytype}'
    upper_whisker=f'max({y}):{ytype}'
    median_whisker=f'median({y}):{ytype}'
    x_data=f'{x}:{xtype}'

    # lower plot
    lower_plot = alt.Chart(data).mark_rule().encode(
        y = alt.Y(lower_whisker, axis=alt.Axis(title=y)),
        y2 = lower_box,
        x = x_data
    ).properties(
        width = width,
        height = height
    )
    # middle plot
    middle_plot = alt.Chart(data).mark_bar(size=size).encode(
        y=lower_box,
        y2=upper_box,
        x = x_data,
        color = determineColorEncoding(data, color, palette),
        tooltip = [x, lower_box, lower_whisker, upper_box, upper_whisker, median_whisker]
    ).properties(
        width = width,
        height = height
    )

    # upper plot
    upper_plot = alt.Chart(data).mark_rule().encode(
        y=upper_whisker,
        y2=upper_box,
        x=x_data
    ).properties(
        width = width,
        height = height
    )

    # median marker line
    middle_tick = alt.Chart(data).mark_tick(
        color='white',
        size=size
    ).encode(
        y=median_whisker,
        x=x_data,
    )
    # combine all the elements of boxplot to a single chart object
    chart = lower_plot + middle_plot + upper_plot + middle_tick

    # return chart object
    return chart
