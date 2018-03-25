from django.shortcuts import render
from django.core import serializers
from django.template.defaulttags import IfNode
import time as T
from crimeReporting.models import *
from django import forms
from .forms import *
from datetime import datetime
from dateutil.parser import parse
import json
import datetime as DT
from django.contrib.auth.decorators import login_required
# Create your views here.
from prediction.fusioncharts import FusionCharts

@login_required(login_url="/signinup/")
def map_render(request):
    is_logged_in = request.user.is_authenticated()
    json_serializer = serializers.get_serializer("json")()
    reports = json_serializer.serialize(FIR_REPORT.objects.all(), ensure_ascii=False)
    context = {
        'report' : reports,
        'is_logged_in' : is_logged_in,
    }

    # request_page(request)
    return render(request, 'map.html',context)

@login_required(login_url="/signinup/")
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

@login_required(login_url="/signinup/")
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

@login_required(login_url="/signinup/")
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



@login_required(login_url="/signinup/")
def report(request):
    week_ago = request.GET.get('date_crime_start')
    today = request.GET.get('date_crime_end')
    # print week_ago + " " + today
    if not week_ago:
        today = DT.date.today()
        week_ago = today - DT.timedelta(days=7)
        print (week_ago)
    report = FIR_REPORT.objects.filter(DATE_CRIME__range=[week_ago, today])
    dataSource = {}
    pieSource={}
    pieSource['chart']={
        "caption": "Crime Summary",
        "showpercentageinlabel": "0",
        "exportenabled": "1",
        "exportatclient": "1",
        "exporthandler": "http://export.api3.fusioncharts.com",
        "html5exporthandler": "http://export.api3.fusioncharts.com",
        "showPercentInTooltip": "0",
        "decimals": "1",
        "showvalues": "1",
        "showlabels": "1",
        "showlegend": "1",
        "showborder": "0",
        "enableSmartLabels": "1",

    }
    dataSource['chart'] = {
        "theme": "fint",
        "palette": "2",
        "exportenabled": "1",
        "exportatclient": "1",
        "exporthandler": "http://export.api3.fusioncharts.com",
        "html5exporthandler": "http://export.api3.fusioncharts.com",
        "caption": "Weekly reports",
        "showlabels": "1",
        "showvalues": "0",
        "numberprefix": "",
        "showsum": "1",
        "decimals": "0",
        "useroundedges": "1",
        "legendborderalpha": "0",
        "showborder": "0"
    }
    dataSource["categories"]=[{
                "category": [
                {
                    "label": "Monday",

                },
                {
                    "label": "Tuesday",

                },
                {
                    "label": "Wednesday",

                },
                {
                    "label": "Thursday",

                },
                {
                    "label": "Friday",

                },
                {
                    "label": "Saturday",

                },
                {
                    "label": "Sunday",

                }
            ]
        }]
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    json_serializer = serializers.get_serializer("json")()
    reports = json_serializer.serialize(report, ensure_ascii=False)
    # print(reports)
    final={}
    dict_monday = {}
    dict_tuesday = {}
    dict_wednesday = {}
    dict_thursday = {}
    dict_friday = {}
    dict_saturday = {}
    dict_sunday = {}
    reports=json.loads(reports)
    for i in reports:
        date = i["fields"]["DATE_CRIME"]
        date=datetime.strptime(date, '%Y-%m-%d')
        # print (type(date))
        day = date.weekday()

        # print day

        if day ==0:
             if i["fields"]["CRIME_TYPE"] in dict_monday:
                 dict_monday[i["fields"]["CRIME_TYPE"]]=dict_monday[i["fields"]["CRIME_TYPE"]]+1
             else:
                 dict_monday[i["fields"]["CRIME_TYPE"]]=1
        elif day==1:
            if i["fields"]["CRIME_TYPE"] in dict_tuesday:
                dict_tuesday[i["fields"]["CRIME_TYPE"]] = dict_tuesday[i["fields"]["CRIME_TYPE"]] + 1
            else:
                dict_tuesday[i["fields"]["CRIME_TYPE"]] = 1
        elif day==2:
            if i["fields"]["CRIME_TYPE"] in dict_wednesday:
                dict_wednesday[i["fields"]["CRIME_TYPE"]] = dict_wednesday[i["fields"]["CRIME_TYPE"]] + 1
            else:
                dict_wednesday[i["fields"]["CRIME_TYPE"]] = 1
        elif day==3:
            if i["fields"]["CRIME_TYPE"] in dict_thursday:
                dict_thursday[i["fields"]["CRIME_TYPE"]] = dict_thursday[i["fields"]["CRIME_TYPE"]] + 1
            else:
                dict_thursday[i["fields"]["CRIME_TYPE"]] = 1
        elif day==4:
            if i["fields"]["CRIME_TYPE"] in dict_friday:
                dict_friday[i["fields"]["CRIME_TYPE"]] = dict_friday[i["fields"]["CRIME_TYPE"]] + 1
            else:
                dict_friday[i["fields"]["CRIME_TYPE"]] = 1
        elif day==5:
            if i["fields"]["CRIME_TYPE"] in dict_saturday:
                dict_saturday[i["fields"]["CRIME_TYPE"]] = dict_saturday[i["fields"]["CRIME_TYPE"]] + 1
            else:
                dict_saturday[i["fields"]["CRIME_TYPE"]] = 1
        elif day==6:
            if i["fields"]["CRIME_TYPE"] in dict_sunday:
                dict_sunday[i["fields"]["CRIME_TYPE"]] = dict_sunday[i["fields"]["CRIME_TYPE"]] + 1
            else:
                dict_sunday[i["fields"]["CRIME_TYPE"]] = 1

    crimedata=['rape','kidnap','theft','murder','assault']
    dataSource['dataset'] = []
    for i in crimedata:
        data_outer = {}
        data_outer['data'] = []
        data_outer['seriesname'] = str(i)
        dict={}
        # data = []
        if i in dict_monday.keys():
            dict["value"] = str(dict_monday[i])
        else:
            dict["value"] = "0"
        data_outer['data'].append(dict)
        dict = {}
        if i in dict_tuesday.keys():
            dict["value"] = str(dict_tuesday[i])
        else:
            dict["value"]= "0"
        data_outer['data'].append(dict)
        # print "*" * 30
        # print(data)
        dict = {}
        if i in dict_wednesday.keys():
            dict["value"] = str(dict_wednesday[i])
        else:
            dict["value"] = str(0)
        data_outer['data'].append(dict)
        dict = {}
        if i in dict_thursday.keys():
            dict['value'] = str(dict_thursday[i])
        else:
            dict["value"] = "0"
        data_outer['data'].append(dict)
        dict = {}
        if i in dict_friday.keys():
            dict["value"] = str(dict_friday[i])
        else:
            dict["value"] = "0"
        data_outer['data'].append(dict)
        dict = {}
        if i in dict_saturday.keys():
            dict["value"] = str(dict_saturday[i])
        else:
            dict["value"] = "0"
        data_outer['data'].append(dict)
        dict = {}
        if i in dict_sunday.keys():
            dict["value"] = str(dict_sunday[i])
        else:
            dict["value"] = "0"
        data_outer['data'].append(dict)
        # print (type(str(data)))
        # data_outer['data']=str(data)

        dataSource['dataset'].append(data_outer)
    # print (dataSource)
    column2D = FusionCharts("stackedbar2d","ex10", "500", "300", "chart-1", "json", dataSource)

    ################PIECHART
    data=[]
    inner_data = {}
    crime_data=[]
    for i in reports:

        crime=i["fields"]["CRIME_TYPE"]

        if crime in crime_data:
            val=inner_data[crime]+1
            inner_data[crime]=val

        else:
            crime_data.append(crime)
            inner_data[crime] = 1

    for i in inner_data.keys():
        data1={}
        data1['label']=i
        data1['value']=inner_data[i]
        data.append(data1)

    pieSource['data']=data
    piechart=FusionCharts("pie2d", "ex11", "100%", "300", "chart-2", "json", pieSource)
    is_logged_in=request.user.is_authenticated()
    context = {
        'data' : dataSource,
        'total': column2D.render(),
        'piechart': piechart.render(),
        'is_logged_in': is_logged_in,
    }

    return render(request, 'report.html', context)



def receive_alert(request):
    posts = INFORMATION_FILING_APP.objects.all()
    return render(request, "report_alert.html", {'posts': posts})

def send_to_FIR(request):
    if request.method == 'GET':
        type = request.GET['typeC']
        phone = request.GET['phone']
        date = request.GET['date']
        time = request.GET['time']
        print type + " " + phone + " " + date + " " + time
        time=time.split(" ")
        if 'p' in time[1]:
            time=time[0]+" PM"
        else:
            time=time[0]+" AM"
        print time
        in_time = datetime.strptime(time, "%I:%M %p")
        out_time = datetime.strftime(in_time, "%H:%M")
        date=date.split(",")
        date=date[0]+date[1]
        date=datetime.strptime(date,"%B %d %Y")
        print date
        print out_time
        time1=out_time+":00"
        time2=out_time+":59"
        var = USER.objects.filter(NAME='AISHNA')
        posts=INFORMATION_FILING_APP.objects.filter(crimetype=type,phone=phone,date_crime=date,time_crime__range=[time1,time2])
        s=FIR_REPORT(CRIME_TYPE=type,LAT=posts[0].latitude,LNG=posts[0].longitude,CRIME_DESCRIPTION=posts[0].crime_description,PERSON_COMPLAINT=var[0],COMPLAINT_BY=posts[0].name,DATE_CRIME=posts[0].date_crime,TIME_CRIME=posts[0].time_crime,FIR_LOC="Delhi",COMPLAINT_TIME=posts[0].complaint_time,COMPLAINT_DATE=posts[0].complaint_date,PHONE=posts[0].phone)
        s.save()
        posts[0].delete()
        print "*"*30
        print posts
        T.sleep(2)
    return receive_alert(request)

def send_email(toaddr,id):
	text = "Hi!\nHow are you?\nHere is the link to activate your account:\nhttp://shreya07.pythonanywhere.com/register_activate/activation/?id=%s" %(id)
	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	msg = MIMEMultipart('alternative')
	msg.attach(part1)
	subject="Activate your account at SealDeal"
	msg="""\From: %s\nTo: %s\nSubject: %s\n\n%s""" %("sealdeal16@gmail.com",toaddr,subject,msg.as_string())
	#Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
	#https://www.google.com/settings/security/lesssecureapps
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login("sealdeal16@gmail.com","tcsproject")
	server.sendmail("sealdeal16@gmail.com",[toaddr],msg)
	server.quit()
