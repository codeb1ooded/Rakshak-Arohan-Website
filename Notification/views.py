from django.shortcuts import render
from crimeReporting.models import *
import datetime
import operator
# Create your views here.

def notifications(request):
    q1=CRIME_TIMELINE.objects.all().values("CRIME_ID").distinct()
    now = datetime.datetime.now()
    date = str(now).split(" ")

    first = now.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    date=lastMonth.strftime("%Y-%m-%d %H:%M:%S")
    data=CRIME_TIMELINE.objects.all().values("CRIME_ID").filter(TIME_OF_UPDATE__lte=date)
    print(data[0])
    q2=FIR_REPORT.objects.all().values("pk").distinct()
    arr=[]
    arr1=[]
    k=0
    for i in q1:
       arr.append(i["CRIME_ID"])

    for i in q2:
        arr1.append(i["pk"])

    distinct=list(set(arr1) - set(arr))
    arr=[]
    for i in data:
        arr.append(i["CRIME_ID"])
    data1=FIR_REPORT.objects.filter(pk__in=distinct)
    data2=FIR_REPORT.objects.filter(pk__in=arr)

    data= data1 |data2
    ordered=sorted(data,key=operator.attrgetter('DATE_CRIME'))

    context = {
        'data' : ordered,
    }
    return render(request,"notification.html",context)