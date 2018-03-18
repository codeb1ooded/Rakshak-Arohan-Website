"""CrimeMapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from maps.views import *
from prediction.views import *
from crimeReporting.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^viewMap/$', map_render),
    url(r'^prediction/$', predict_graph, name='predict_graph'),
    url(r'^register/$', request_page, name='request_page'),
    url(r'^most_prominent_city/$',prominent_city, name='most_prominent_city'),
    url(r'^most_prominent_crime/$', prominent_crime, name='most_prominent_crime'),
    url(r'^crime_status/$', crime_status, name='crime_status'),
    url(r'^firReg/$', fir_reg),
    url(r'^update_crime/', update_crime, name="update_crime"),
    url(r'^analyse_selected_area/', analyse_selected_area, name="Analyse"),
]
