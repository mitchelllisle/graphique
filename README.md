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
from vega_datasets import data

stocks = data.stocks()
amazonStocks = stocks.query("symbol == 'AMZN'")

nl.lineChart(data = amazonStocks,
             x = "date",
             y = ['price'],
             title = "Amazon Stock",
             subtitle = "The Amazon stock price form 2000 - 2010")
```

![linechart](https://user-images.githubusercontent.com/18128531/37870250-b0d47e34-301c-11e8-80d0-3890bec4e734.png)

It's also easy to add multiple series to any chart that support multiple series (E.g. line, column, histogram etc). The `y` axis argument accepts a list, so simply supplying the names of the columns will create multiple series.
```python
multiStocks = stocks.pivot(index='date', columns='symbol', values='price').reset_index()

nl.lineChart(data = multiStocks,
             x = "date", y = ['AAPL', 'AMZN', 'GOOG', 'MSFT'])
```
![multipleline](https://user-images.githubusercontent.com/18128531/37870251-b3894a42-301c-11e8-8c7a-52f9460b3a31.png)

```python
import numpy as np
df = pd.DataFrame({'CategoryOne':np.random.normal(0, 0.8, 1000),
                   'CategoryTwo':np.random.normal(-2, 1, 1000),
                   'CategoryThree':np.random.normal(3, 2, 1000)})


nl.histChart(df, x = ['CategoryOne', 'CategoryTwo', 'CategoryThree'], title = "Histogram")
```

![histogram](https://user-images.githubusercontent.com/18128531/37870386-b1c719b0-3020-11e8-92a2-d0e789e8daab.png)
