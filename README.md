![logo](https://user-images.githubusercontent.com/18128531/38246646-d345c070-3785-11e8-9a92-764d4fd6c369.png)

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)
[![codecov](https://codecov.io/gh/mitchelllisle/napoleon/branch/master/graph/badge.svg)](https://codecov.io/gh/mitchelllisle/napoleon)

This is a simple Python package designed to make charting with Altair quicker and easier with some sensible defaults.

### Installation
`pip install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker to go from data to chart using the [Altair](https://altair-viz.github.io/) charting library.

```python
import napoleon as nl
```

Chart Types:
```python
nl.lineChart()
nl.barChart()
nl.areaChart()
nl.scatterChart()

# Coming soon
nl.hist()
nl.heatmap()
nl.boxPlot()
nl.candleStick()
nl.streamGraph()
nl.scatterHist()
```

### Examples

```python
from vega_datasets import data

stocks = data.stocks()

nl.lineChart(stocks, x = "date:T", y = "price:Q", color = "symbol")
```
![visualization](https://user-images.githubusercontent.com/18128531/44091662-8af9df28-a011-11e8-8bb5-1b8a9db357a1.png)
