import plotly.graph_objs as go
import pandas as pd
from palettable.colorbrewer.qualitative import Paired_10
from palettable.colorbrewer.qualitative import Dark2_8

def generateTraces(chartType, data, x, y, z, colour, orientation = None):
    traces = []

    if chartType == 'Line':
        for i in range(0, len(y)):
            traces.append(go.Scatter(
                x = data[x],
                y = data[y[i]],
                name = y[i],
                mode='lines',
                line=dict(color = colour[i])
            ))
    elif chartType == 'Column':
        if orientation == "h":
            for i in range(0, len(y)):
                traces.append(go.Bar(
                    x = data[x],
                    y = data[y[i]],
                    marker=dict(color = colour[i]),
                    orientation = orientation
                ))
        else:
            for i in range(0, len(y)):
                traces.append(go.Bar(
                    x = data[x],
                    y = data[y[i]],
                    marker=dict(color = colour[i])
                ))
    elif chartType == 'Histogram':
        for i in range(0, len(x)):
            traces.append(go.Histogram(
                x = data[x[i]],
                opacity = 0.75,
                marker=dict(color = colour[i])
            ))
    elif chartType == 'Heatmap':
        heatmapData = data.groupby([x]).apply(lambda a: list(a[z])).reset_index()
        heatmapData.columns = [x, z]

        traces = [go.Heatmap(z=list(heatmapData[z]),
                            x=list(data[y].unique()),
                            y=list(data[x].unique()))
                 ]
    elif chartType == 'Area':
        for i in range(0, len(y)):
            traces.append(go.Scatter(
                x = data[x],
                y = data[y[i]],
                name = y[i],
                mode='lines',
                fill = "tozeroy",
                line=dict(color = colour[i])
            ))

    return traces


def generateLayout(chartType, barMode, title, subtitle):
    layout = go.Layout(
            title = None,
            barmode = barMode,
                annotations=[dict(
                        x = 0,
                        y = 1.10,
                        xref = 'paper',
                        yref = 'paper',
                        text = subtitle,
                        showarrow=False
                    ),
                    dict(
                        font = dict(
                          color = "black",
                          size = 20
                        ),
                        x = 0,
                        y = 1.20,
                        xref = 'paper',
                        yref = 'paper',
                        text = title,
                        showarrow=False
                    )
                ]
            )
    return layout

def generateColours(palette = "google"): 
    if palette == "bigdatr":
        colours = ['#AA86FC', '#FD6966', '#1EB1ED', '#A3D369', '#FAD747', '#396190']

    elif palette == "google":
        colours = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]
    
    elif palette == "colorbrewer":
        colours = Paired_10.hex_colors
    
    elif palette == "colorbrewer_dark":
        colours = Dark2_8.hex_colors
        
    else:
        colours = palette
    return colours
