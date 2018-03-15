from django.shortcuts import render
from prediction.forms import RScriptForm
import numpy as np
import matplotlib.pyplot as plt
from prediction.fusioncharts import FusionCharts


def my_view(request):
    context={}
    total=total_view(request)
    context['total']=total
    goa=goa_view(request)
    context['goa'] = goa
    assam = assam_view(request)
    context['assam'] = assam
    rape = rape_view(request)
    context['rape'] = rape
    kidnap = kidnap_view(request)
    context['kidnap'] = kidnap
    return render(request, 'graph.html', context)


def total_view(request):

    data_main= np.recfromcsv('static\dataset.csv')
    #x-->year
    #y-->crime total
    data=list(range(2001,2013))
    data1 = data_main['y']
    x = np.squeeze(np.array(data))
    y = np.squeeze(np.array(data1))
    y = np.delete(y, (0), axis=0)
    y=y.astype(int)
    dataSource=callLinearRegression(x,y)
    column2D = FusionCharts("column3D", "ex1", "100%", "50%", "chart-total", "json", dataSource)
    return column2D.render()


def goa_view(request):
    data_main = np.recfromcsv('static\dataset.csv')
    # x-->year
    # y-->crime total
    data = list(range(2001, 2013))
    data1 = data_main['totalgoa']
    x = np.squeeze(np.array(data))
    y = np.squeeze(np.array(data1))
    y = np.delete(y, (0), axis=0)
    y = y.astype(int)
    dataSource = callLinearRegression(x, y)
    column2D = FusionCharts("column3D", "ex2", "100%", "50%", "chart-goa", "json", dataSource)
    return column2D.render()

def assam_view(request):
    data_main = np.recfromcsv('static\dataset.csv')
    # x-->year
    # y-->crime total
    data = list(range(2001, 2013))
    data1 = data_main['totalassam']
    x = np.squeeze(np.array(data))
    y = np.squeeze(np.array(data1))
    y = np.delete(y, (0), axis=0)
    y = y.astype(int)
    dataSource = callLinearRegression(x, y)
    column2D = FusionCharts("column3D", "ex3", "100%", "50%", "chart-assam", "json", dataSource)
    return column2D.render()
##########CRIME WISE SELECTION

def rape_view(request):
    data_main = np.recfromcsv('static\dataset.csv')
    # x-->year
    # y-->crime total
    data = list(range(2001, 2013))
    data1 = data_main['totalrape']
    x = np.squeeze(np.array(data))
    y = np.squeeze(np.array(data1))
    y = np.delete(y, (0), axis=0)
    y = y.astype(int)
    dataSource = callLinearRegression(x, y)
    column2D = FusionCharts("column3D", "ex4", "100%", "50%", "chart-rape", "json", dataSource)
    return column2D.render()
def kidnap_view(request):
    data_main = np.recfromcsv('static\dataset.csv')
    # x-->year
    # y-->crime total
    data = list(range(2001, 2013))
    data1 = data_main['totalkidnap']
    x = np.squeeze(np.array(data))
    y = np.squeeze(np.array(data1))
    y = np.delete(y, (0), axis=0)
    y = y.astype(int)
    dataSource = callLinearRegression(x, y)
    column2D = FusionCharts("column3D", "ex5", "100%", "50%", "chart-kidnap", "json", dataSource)
    return column2D.render()

def callLinearRegression(x,y):
    regression = np.polyfit(x, y, 1)
    a=regression[0]
    b=regression[1]
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Prediction",
        "subCaption": "Crime",
        "xAxisName": "Upcoming Years",
        "yAxisName": "Predicted Crime Rate",
        "numberPrefix": "",
        "theme": "fint",
        "labelDisplay": "auto",
    }
    dataSource['data'] = []
    for i in range(2018,2022):
        val=b+a*i
        data = {}
        data['label'] = i
        data['value'] = val
        dataSource['data'].append(data)
    return dataSource

#1. Overall crime in future years(crime rate vs year) (year wise overall crime)
#2. State wise crime in future years (crime rate vs year)
#3. crime rate vs year (filter crime)
