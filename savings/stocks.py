import pandas as pd
import numpy as np
import time
from alpha_vantage.timeseries import TimeSeries

api_key = '*******'  # Enter your API key from alpha_vantage
price_now = 0.0

# class Data:


def get_data(sym):
    ts = TimeSeries(key=api_key, output_format='json')
    price = ts.get_quote_endpoint(sym)
    price_now = price[0]['05. price']
    return price_now


def get_historical_data(sym):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(
        symbol=sym, outputsize='full')
    data = data[::-1]
    return data


def get_historical_data_array(sym):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(
        symbol=sym, outputsize='full')
    data = data[::-1]
    data = data.drop(columns=['5. volume'])
    data['day'] = "Mon"
    data[['1. open', '2. high', '3. low', '4. close', 'day']
         ] = data[['day', '3. low', '1. open', '4. close', '2. high']]
    data = np.array(data)
    d = []
    for index, row in enumerate(data):
        d.append(['' + str(index), row[1], row[2], row[3], row[4]])
    d = d[0:6]
    return d
