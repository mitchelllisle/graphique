#import pytest
#from napoleon import lineChart
#from napoleon import columnChart
#from napoleon import barChart
#from napoleon import histChart
#from napoleon import heatmapChart
#from napoleon import generateLayout
#from napoleon import generateTraces
#from napoleon import generateColours
#import numpy as np
#import pandas as pd

#amazonStocks = pd.read_csv("data/amazonStocks.csv")
#uberData = pd.read_csv("data/uberData.csv")

#def test_lineChart():
    #lineChart(data = amazonStocks, 
       # x = "date", 
       # y = ['price'], 
        #title = "Amazon Stock", 
        #subtitle = "The Amazon stock price form 2000 - 2010",
       # colour = "bigdatr")
    
    
#def test_columnChart():
    #columnChart(data = amazonStocks, 
      #   x = "date", 
       #  y = ['price'], 
       #  title = "Amazon Stock", 
        # subtitle = "The Amazon stock price form 2000 - 2010",
        # colour = "bigdatr")

#def test_barChart():
   # barChart(data = amazonStocks, 
      #   x = "date", 
       #  y = ['price'], 
      #   title = "Amazon Stock", 
       #  subtitle = "The Amazon stock price form 2000 - 2010",
        # colour = "bigdatr")

#def test_histChart():
 #   histChart(data = amazonStocks, 
  #       x = ["price"],  
   #      title = "Amazon Stock", 
    #     subtitle = "The Amazon stock price form 2000 - 2010",
     #    colour = "bigdatr")

#def test_heatmapChart():
    #heatmapChart(uberData, 
      #           x = "weekday", 
               #  y = "hour", 
               #  z = "count", 
                # title = "Heatmap of Time of Day vs Day of Week")
    
    
# Run Functions
## Layouts
#test_lineChart()
#test_columnChart()
#test_barChart()
#test_histChart()
#test_heatmapChart()