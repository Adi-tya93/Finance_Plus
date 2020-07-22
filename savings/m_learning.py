import numpy as np
import pandas as pd
from . import stocks
from .stocks import get_historical_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.style.use('bmh')


def get_array(sym):
    df = get_historical_data(sym=sym)
    df = df[['1. open']]
    future_days = 25
    df['Prediction'] = df[['1. open']].shift(-future_days)
    # create the feature data set (X) and convert it to a numpy array and remove the last '2*x' rows/days
    X = np.array(df.drop(['Prediction'], 1))[:-(2*future_days)]
    # create the target data set (y) and convert it to numpy array and get all of the taget values except the last "2*x" rows
    y = np.array(df['Prediction'])[:-(2*future_days)]
    # Didnt need to split as we are using last 25 days to test. But just in case for accuracy checks
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.01)
    tree = DecisionTreeRegressor().fit(X_train, y_train)
    lr = LinearRegression().fit(X_train, y_train)
    X_future = df.drop(['Prediction'], 1)[:-future_days]
    X_future = X_future.tail(future_days)
    X_future = np.array(X_future)
    tree_prediction = tree.predict(X_future)
    lr_prediction = lr.predict(X_future)
    actual = df['1. open'][-100:]
    valid = df[-future_days:]
    valid['Predictions'] = tree_prediction
    valid = valid['Predictions']
    ar = list()
    for index, items in enumerate(actual):
        ar.append([index, 0, items])

    for index, items in enumerate(valid):
        ar[index + 75][1] = items

    return ar
