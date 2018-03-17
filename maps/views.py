from django.shortcuts import render
from django.core import serializers
from crimeReporting.models import *
from django import forms
from .forms import *

# Create your views here.


def map_render(request):
    json_serializer = serializers.get_serializer("json")()
    reports = json_serializer.serialize(FIR_REPORT.objects.all(), ensure_ascii=False)
    context = {
        'report' : reports,
    }

    # request_page(request)
    return render(request, 'map.html',context)

def request_page(request):
    reports=[]
    json_serializer = serializers.get_serializer("json")()
    if (request.GET.get('mybtn')):
        somevar = (request.GET.getlist('crime'))
        date_start = (request.GET.get('date_crime_start'))
        date_end = (request.GET.get('date_crime_end'))
        status_var=(request.GET.getlist('status'))

        if not somevar:
            if not date_end and not date_start:
                if not status_var:
                    report = FIR_REPORT.objects.all()
                else :
                    report = FIR_REPORT.objects.filter(STATUS__in=status_var)
            else:
                if not status_var:
                    report = FIR_REPORT.objects.filter(DATE_CRIME__range=[date_start, date_end])
                else:
                    report = FIR_REPORT.objects.filter(STATUS__in=status_var)

        else:
            if not date_end and not date_start:
                if not status_var:
                    report = FIR_REPORT.objects.filter(CRIME_TYPE__in = somevar)
                else:
                    report = FIR_REPORT.objects.filter(CRIME_TYPE__in=somevar,STATUS__in=status_var)
            elif date_end and date_start:
                if not status_var:
                    report = FIR_REPORT.objects.filter(CRIME_TYPE__in = somevar,DATE_CRIME__range=[date_start, date_end])
                else:
                    report = FIR_REPORT.objects.filter(CRIME_TYPE__in=somevar,STATUS__in=status_var,DATE_CRIME__range=[date_start, date_end])

        reports = json_serializer.serialize(report, ensure_ascii=False)

    context = {
        'report': reports,
    }
    return render(request, 'map.html',context)


def map_render_filter(request):
    json_serializer = serializers.get_serializer("json")()
    reports = json_serializer.serialize(FIR_REPORT.objects.all(), ensure_ascii=False)
    context = {
        'report' : reports,
    }
    return render(request, 'map.html',context)

def crime_status(request):
    if request.method == 'GET':

        crime_id= request.GET.get('crime_id')
        global detail
        detail=  FIR_REPORT.objects.filter(ID = crime_id)
        report = CRIME_TIMELINE.objects.filter(CRIME_ID = crime_id)
        json_serializer = serializers.get_serializer("json")()
        reports = json_serializer.serialize(report, ensure_ascii=False)
        details= json_serializer.serialize(detail, ensure_ascii=False)
        users = json_serializer.serialize(USER.objects.all(), ensure_ascii = False)
        form = UPDATE_FORM()
        context = {
            'reports': reports,
            'details': details,
            'users': users,
            'form': form
        }
        return render(request, 'status_report.html', context)


def update_crime(request):
    if request.method == 'GET':
        #crime_id = request.GET.get('crime_id')
        form = UPDATE_FORM(request.GET)
        if form.is_valid():
            data = form.save(commit=False)
            data.CRIME_ID = detail[0]
            var=USER.objects.filter(NAME='AISHNA')
            data.UPDATED_BY = var[0]
            #request.session.get('username')
            data.save()
            return render(request, 'done.html')

    return render(request, 'done.html')



