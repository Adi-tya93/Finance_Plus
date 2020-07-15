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
