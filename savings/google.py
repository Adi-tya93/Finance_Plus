import pandas as pd
import numpy as np
from alpha_vantage.timeseries import TimeSeries

api_key = 'M2ENTQK548AAMGQG'
date = list()
open_price = list()
high = list()
low = list()
close_price = list()
volume = list()


ts = TimeSeries(key=api_key, output_format='json')
data, meta_data = ts.get_daily(
    symbol='GOOGL', outputsize='compact')

#price = ts.get_quote_endpoint('GOOGL')
#price_now = price[0]['05. price']


for items in data:
    date.append(items)
    for index, info in enumerate(data[items]):
        if (index == 0):
            open_price.append(float(data[items][info]))
            pass
        if (index == 1):
            high.append(float(data[items][info]))
            pass
        if (index == 2):
            low.append(float(data[items][info]))
            pass
        if (index == 3):
            close_price.append(float(data[items][info]))
            pass
        if (index == 4):
            volume.append(int(data[items][info]))
            pass
