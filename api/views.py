# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.db import models

from datetime import *

from crimeReporting.models import *

def get_user(username):
    inbuilt_user = User.objects.filter(username=username)
    user = USER.objects.filter(USER_REF = inbuilt_user)
    try:
        return user[0]
    except:
        return None


''' JSON format
name
aadharcard
phone
crimetype
latitude
longitude
crime_description
date_crime
time_crime
complaint_time
Sample http request:http://127.0.0.1:8000/api/reportcrime/?crimetype=murder&latitude=28.665236&longitude=77.2323689&crime_description=xyz&complaint_by=anonymous&date_crime=2017-03-21&time_crime=11:11:11&fir_location=delhi&complaint_time=10:11:10&phone=1234567890&status=lodged
'''
def reportFIR(request):
    _name = request.GET['name']
    _aadharcard = request.GET['aadharcard']
    _phone = request.GET['phone']
    _crime_type = request.GET['crimetype']
    _lat = float(request.GET['latitude'])
    _long = float(request.GET['longitude'])
    _crime_description = request.GET['crime_description']
    _date_crime = request.GET['date_crime']
    _time_crime = request.GET['time_crime']
    _complaint_time = request.GET['complaint_time']

    # query_report_fir = FIR_REPORT( CRIME_TYPE = _crime_type,
	# 						   LAT = _lat,
	# 						   LNG = _long,
	# 						   CRIME_DESCRIPTION = _crime_description,
    #                            PERSON_COMPLAINT = _person_complaint,
	# 				   		   COMPLAINT_BY = _complaint_by,
	# 				   		   DATE_CRIME = _date_crime,
	# 				   		   TIME_CRIME = _time_crime,
	# 				   		   FIR_LOC = _fir_location,
	# 				   		   COMPLAINT_TIME = _complaint_time,
	# 				   		   PHONE = _phone,
	# 				   		   STATUS = _status)
    # query_report_fir.save()
    return JsonResponse({"status" : "success"})


'''
No JSON Input
Json Output: array of given Json Object
{
crime_type
latitude
longitude
crime_description
complaint_by
date_crime
time_crime
fir_location
complaint_time
phone
status
}
'''
def all_reports_markers(request):
    all_reports = FIR_REPORT.objects.all()
    all_reports_array = []
    for report in all_reports:
        report_json = {
                'crime_type': report.CRIME_TYPE,
                'latitude': report.LAT,
                'longitude': report.LNG,
                'crime_description': report.CRIME_DESCRIPTION,
                'complaint_by': report.COMPLAINT_BY,
                'date_crime': report.DATE_CRIME,
                'time_crime': report.TIME_CRIME,
                'fir_location': report.FIR_LOC,
                'complaint_time': report.COMPLAINT_TIME,
                'phone': report.PHONE,
                'status': report.STATUS
        }
        all_reports_array.append(report_json)
    print (JsonResponse({"all_reports" : all_reports_array}))
    return JsonResponse({"all_reports" : all_reports_array})


''' JSON format
latitude
longitude
'''
def neighbourhood(request):
    _lat = float(request.GET['latitude'])
    _long = float(request.GET['longitude'])
    neighbourhood_reports = FIR_REPORT.objects.all()
    json_neighbourhood = []
    for report in neighbourhood_reports:
        report_json = {
                'crime_type': report.CRIME_TYPE,
                'latitude': report.LAT,
                'longitude': report.LNG,
                'crime_description': report.CRIME_DESCRIPTION,
                'complaint_by': report.COMPLAINT_BY,
                'date_crime': report.DATE_CRIME,
                'time_crime': report.TIME_CRIME,
                'fir_location': report.FIR_LOC,
                'complaint_time': report.COMPLAINT_TIME,
                'phone': report.PHONE,
                'status': report.STATUS
        }
        json_neighbourhood.append(report_json)
    print JsonResponse({"neghbourhood" : json_neighbourhood})
    return JsonResponse({"neghbourhood" : json_neighbourhood})
