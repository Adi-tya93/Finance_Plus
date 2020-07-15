from django.shortcuts import render
from django.http import HttpResponse
from . import stocks, m_learning
from .stocks import get_data
from .stocks import price_now
import pandas as pd


# Create your views here.


def index(request):
    return render(request, 'savings/index.html')


def stocks(request):
    data = get_data(sym="MSFT")
    app = get_data(sym="AAPL")
    goog = get_data(sym="GOOGL")
    tes = get_data(sym="TSLA")
    return render(request, 'savings/stocks.html', {'data': data, 'apple': app, 'google': goog, 'tesla': tes})


def tips(request):
    return render(request, 'savings/tips.html')


def mlearning(request, choice):
    ar = m_learning.ar
    return render(request, 'savings/mlearning.html', {'choice': choice, 'ar': ar})
