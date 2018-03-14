from django.shortcuts import render
from prediction.forms import RScriptForm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from prediction.fusioncharts import FusionCharts

def my_view(request):

    data_main= np.recfromcsv('static\hello.csv')
    data=data_main['x']
    data1 = data_main['y']
    x = np.squeeze(np.array(data))
    y = np.squeeze(np.array(data1))
    regression = np.polyfit(x, y, 1)
    a=regression[0]
    b=regression[1]
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Prediction",
        "subCaption": "Crime",
        "xAxisName": "Years",
        "yAxisName": "Crime Rate",
        "numberPrefix": "",
        "theme": "fint",
        "labelDisplay": "auto",
    }
    dataSource['data'] = []
    for i in range(2014,2018):
        val=b+a*i
        data = {}
        data['label'] = i
        data['value'] = val
        print(data)
        dataSource['data'].append(data)

    column2D = FusionCharts("column3D", "ex1", "100%", "50%", "chart-1", "json", dataSource)
    context = {
        'output': column2D.render()
    }
    return render(request, 'graph.html', context)
#1. Overall crime in future years(crime rate vs year) (year wise overall crime)
#2. State wise crime in future years (crime rate vs year)
#3. crime rate vs year (filter crime)