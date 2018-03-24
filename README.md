# Napoleon

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)

This is a simple Python package designd to make plotting with plotly quicker and easier with some sensible defaults.

### Installation
`pip install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker and easier to produce a chart using the plotly python library. For example, to create a line chart:

```python
import napoleon as nl

nl.lineChart(creativeDataGroups, 'first_appeared', ['totalcreatives'], ['red'], "Creatives by Day", "The number of new creatives released by day")
```


![linechart](https://user-images.githubusercontent.com/18128531/37869861-2c612862-3014-11e8-9408-ca97c5a6ef92.png)
