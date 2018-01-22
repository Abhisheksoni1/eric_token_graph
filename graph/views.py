import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from highcharts.views import HighChartsMultiAxesView

from graph.models import TokenData


def home(request):
    return render(request, 'home.html')


def bar(request):
    token = TokenData.objects.all()
    dates = list(map(lambda i: i.timestamp.strftime('%m-%d-%Y'), token))
    prices = list(map(lambda i: float(i.price), token))
    total_token = list(map(lambda i: i.total_token, token))
    percentage_holds = list(map(lambda i: float(i.percentage_holds), token))
    # print(percentage_holds)
    data = {"dates": dates,
            'prices': prices,
            'total_token': total_token,
            'percentage_holds': percentage_holds
            }
    return HttpResponse(json.dumps(data), content_type='application/json')
