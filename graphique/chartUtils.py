import plotly.graph_objs as go

def generateTraces(chartType, data, x, y, color):
    traces = []

    if chartType == 'Line':
        for i in range(0, len(y)):
            traces.append(go.Scatter(
                x = data[x],
                y = data[y[i]],
                name = y[i],
                mode='lines',
                line=dict(color = color[i])
            ))
    elif chartType == 'Column':
        for i in range(0, len(y)):
            traces.append(go.Bar(
                x = data[x],
                y = data[y[i]],
                marker=dict(color = color[i])
            ))
    elif chartType == 'Histogram':
        for i in range(0, len(x)):
            traces.append(go.Histogram(
                x = data[x[i]],
                opacity = 0.75,
                marker=dict(color = color[i])
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