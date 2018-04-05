![logo](https://user-images.githubusercontent.com/18128531/38246646-d345c070-3785-11e8-9a92-764d4fd6c369.png)

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)
[![codecov](https://codecov.io/gh/mitchelllisle/napoleon/branch/master/graph/badge.svg)](https://codecov.io/gh/mitchelllisle/napoleon)

This is a simple Python package designed to make charting with plotly quicker and easier with some sensible defaults.

### Installation
`pip install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker to go from data to chart using the [Plotly](https://plot.ly/) charting library.

The convention I go with to load Napoleon is:

```python
import napoleon as nl
```

There are currently three chart types supported
```
nl.lineChart()
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
             y = 'price',
             title = "Amazon Stock",
             subtitle = "The Amazon stock price form 2000 - 2010",
             colour = "bigdatr")
```
![line](https://user-images.githubusercontent.com/18128531/37870398-ee950b2c-3020-11e8-9d42-4cad80c335df.png)

It's also easy to add multiple series to any chart that support multiple series (E.g. line, column, histogram etc). Simply pass in a `group` values that contains the subsets to colour individually.
```python
nl.lineChart(data = stocks,
             x = "date",
             y = "price",
             group = "symbol",
             title = "Amazon, Apple, Google, Microsoft Stock Price",
             subtitle = "Stock prices form 2000 - 2010",
             colour = "colorbrewer_dark")
```
![multiline](https://user-images.githubusercontent.com/18128531/38362182-3d8babdc-3913-11e8-99c8-935820fab377.png)

Column charts can be single series:
```python
from vega_datasets import data

stocks = data.stocks()
amazonStocks = stocks.query("symbol == 'AMZN'")

nl.columnChart(data = amazonStocks,
             x = "date",
             y = 'price',
             title = "Amazon Stock",
             subtitle = "The Amazon stock price form 2000 - 2010",
             colour = "google",
             barMode = "stack")

```
![column](https://user-images.githubusercontent.com/18128531/38362169-37c04b90-3913-11e8-81f3-512e7a6d8227.png)

Multi-Series with the `group` option:
```python
from vega_datasets import data

stocks = data.stocks()
stocks = (
    stocks
    .query('date > 2009')
)

nl.columnChart(data = stocks,
             x = 'date',
             y = 'price',
            group = 'symbol',
             title = 'Amazon, Apple, Google, IBM & Microsoft Stock Price',
             subtitle = "The Tech-Giants stock prices form 2005 - 2010",
             colour = "bigdatr")

```
![multicolumn](https://user-images.githubusercontent.com/18128531/38362202-53eacd18-3913-11e8-85c5-445f8cffcbe3.png)

As well as Multi-Series stacked with the `barMode = "stack"` option:
```python
from vega_datasets import data

stocks = data.stocks()
stocks = (
    stocks
    .query('date >= 2005')
)
nl.columnChart(data = stocks,
             x = 'date',
             y = 'price',
            group = 'symbol',
             title = 'Amazon, Apple, Google, IBM & Microsoft Stock Price',
             subtitle = "The Tech-Giants stock prices form 2005 - 2010",
             colour = "bigdatr",
             barMode = "stack")
```
![multicolumnstack](https://user-images.githubusercontent.com/18128531/38362207-566dab6e-3913-11e8-9789-b1517ebcbe65.png)

```python
import numpy as np
df = pd.DataFrame({'CategoryOne':np.random.normal(0, 0.8, 1000),
                   'CategoryTwo':np.random.normal(-2, 1, 1000),
                   'CategoryThree':np.random.normal(3, 2, 1000)})


nl.histChart(df, x = ['CategoryOne', 'CategoryTwo', 'CategoryThree'], title = "Histogram")
```
![hist](https://user-images.githubusercontent.com/18128531/37870399-eecc60c2-3020-11e8-969e-73b46e046fde.png)
