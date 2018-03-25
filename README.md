# Napoleon

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)

This is a simple Python package designd to make plotting with plotly quicker and easier with some sensible defaults.

### Installation
`pip install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker to go from data to chart using the [Plotly](https://plot.ly/) charting library. For example, to create a line chart:

The convention I go with to load Napoleon is:

```python
import napoleon as nl
```

There are currently three chart types supported
```
nl.LineChart()
nl.columnChart()
nl.histChart()
```

### Examples
```python
from vega_datasets import data

stocks = data.stocks()
amazonStocks = stocks.query("symbol == 'AMZN'")

nl.lineChart(data = amazonStocks,
             x = "date",
             y = ['price'],
             title = "Amazon Stock",
             subtitle = "The Amazon stock price form 2000 - 2010")
```
![line](https://user-images.githubusercontent.com/18128531/37870398-ee950b2c-3020-11e8-9d42-4cad80c335df.png)

It's also easy to add multiple series to any chart that support multiple series (E.g. line, column, histogram etc). The `y` axis argument accepts a list, so simply supplying the names of the columns will create multiple series.
```python
multiStocks = stocks.pivot(index='date', columns='symbol', values='price').reset_index()

nl.lineChart(data = multiStocks, 
             x = "date", 
             y = ['AAPL', 'AMZN', 'GOOG', 'MSFT'],
             title = "Amazon, Apple, Google, Microsoft Stock Price",
             subtitle = "Stock prices form 2000 - 2010")
```
![multiline](https://user-images.githubusercontent.com/18128531/37870397-ee5baa08-3020-11e8-8c96-8bc665976670.png)

```python
import numpy as np
df = pd.DataFrame({'CategoryOne':np.random.normal(0, 0.8, 1000),
                   'CategoryTwo':np.random.normal(-2, 1, 1000),
                   'CategoryThree':np.random.normal(3, 2, 1000)})


nl.histChart(df, x = ['CategoryOne', 'CategoryTwo', 'CategoryThree'], title = "Histogram")
```
![hist](https://user-images.githubusercontent.com/18128531/37870399-eecc60c2-3020-11e8-969e-73b46e046fde.png)
