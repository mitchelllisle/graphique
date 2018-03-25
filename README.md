# Napoleon

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)

This is a simple Python package designd to make plotting with plotly quicker and easier with some sensible defaults.

### Installation
`pip install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker to go from data to chart using the [Plotly](https://plot.ly/) charting library. For example, to create a line chart:

```python
import pandas as pd
import napoleon as nl

# This dataset is included in the Napoleon package
data = pd.read_csv("data/champagneSales.csv")

myTitle = "Perrin Freres Monthly Champagne Sales"
mySubtitle = "Sample dataset showing Perrin Freres monthly champagne sales in millions from ’64-’72"

# Create Napoleon Chart (this produces a plotly chart)
nl.lineChart(data = data, x = "Month", y = ['Sales'], title = myTitle, subtitle = mySubtitle)
```

![linechart](https://user-images.githubusercontent.com/18128531/37870250-b0d47e34-301c-11e8-80d0-3890bec4e734.png)

It's also easy to add multiple series to any chart that support multiple series (E.g. line, column, histogram etc). The `y` axis argument accepts a list, so simply supplying the names of the columns will create multiple series.
```python
data = data.assign(rollingAvg = data['Sales'].rolling(6).mean())

nl.lineChart(data = data, x = "Month", y = ['Sales', 'rollingAvg'], title = myTitle, subtitle= mySubtitle)
```
![multipleline](https://user-images.githubusercontent.com/18128531/37870251-b3894a42-301c-11e8-8c7a-52f9460b3a31.png)
