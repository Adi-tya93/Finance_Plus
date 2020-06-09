from django.shortcuts import render
from django.http import HttpResponse
from . import stock, google, apple, tesla, m_learning
import pandas as pd

# Create your views here.


def index(request):
    return render(request, 'savings/index.html')


def stocks(request):
    data = stock.open_price[0]
    app = apple.open_price[0]
    goog = google.open_price[0]
    tes = tesla.open_price[0]
    return render(request, 'savings/stocks.html', {'data': data, 'apple': app, 'google': goog, 'tesla': tes})


def tips(request):
    return render(request, 'savings/tips.html')


def mlearning(request, choice):
    ar = m_learning.ar
    return render(request, 'savings/mlearning.html', {'choice': choice, 'ar': ar})
