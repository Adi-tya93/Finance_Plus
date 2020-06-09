from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'house/index.html')


def calculate(request):
    price = int(request.GET['price'])
    rate = float(request.GET['rate'])
    years = int(request.GET['years'])
    months = years*12
    r = rate/(100*12)
    mortgage = price * (r * ((1+r)**months)) / (((1+r) ** months)-1)
    return render(request, 'house/index.html', {'mortgage': int(mortgage)})
