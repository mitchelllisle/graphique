def generateTraces(chartType, data, x, y, color):
    traces = []
    
    if chartType == 'Line':
        for i in range(0, len(y)):
            traces.append(go.Scatter(
                x = data[x],
                y = data[y[i]],
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

def lineChart(data, x, y, color = None, title = "", subtitle = ""):
    chartType = "Line"
    barMode = None
    
    if color is None:
        color = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]

    traces = generateTraces(chartType, data, x, y, color)
    
    layout = generateLayout(chartType, barMode, title, subtitle)
    
    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart


def columnChart(data, x, y, color = None, title = "", subtitle = ""):
    chartType = "Column"
    barMode = None
    
    if color is None:
        color = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]

    traces = generateTraces(chartType, data, x, y, color)
    
    layout = generateLayout(chartType, barMode, title, subtitle)
    
    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart

def histChart(data, x, color = None, title = "", subtitle = ""):
    chartType = "Histogram"
    barMode = "overlay"
    y = None
    if color is None:
        color = ["#4791E5", "#F6A502", "#FB5A6E", "#1CB37D"]

    traces = generateTraces("Histogram", data, x, y, color)
    
    layout = generateLayout(chartType, barMode, title = title, subtitle = subtitle)
    
    plot = go.Figure(data = traces, layout = layout)
    chart = py.iplot(plot)
    return chart
