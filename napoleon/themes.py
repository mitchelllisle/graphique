import altair as alt

def greyTheme():
    markColor = '#ab5787'
    axisColor = '#979797'
    config = {
          "config": {
            "background" : "#f9f9f9",
            "title" : {
                "color" : "#8D8D8D",
                "anchor" : "start",
                "fontSize" : 20,
                "offset" : 30
            },
            "axis": {
                "domainColor": axisColor,
                "domainWidth": 0.5,
                "gridWidth": 0.2,
                "labelColor": axisColor,
                "tickColor": axisColor,
                "tickWidth": 0.2,
                "titleColor": axisColor,
              },
            "legend": {
                "labelFontSize": 11,
                "padding": 1,
                "symbolSize": 30,
                "symbolType": 'square',
          }
          }
        }
    return config

def darkTheme():
    config = {
          "config": {
            "background" : "#3E3D47",
            "title" : {
                "color" : "#B1B1B1",
                "anchor" : "start",
                "fontSize" : 20,
                "offset" : 30
            },
            "axis": {
              "titleColor": "#6B6874",
              "domainColor": "#676767",
              "gridColor": "#28282C",
              "labelColor": "#B1B1B1",
              "tickColor": "#6B6874"
            }
          }
        }
    return config

def activateTheme(name):
    try:
        alt.themes.register(name, eval(name))
        alt.themes.enable(name)
        return eval(name)
    except Exception as e:
        raise Exception(str(e))
