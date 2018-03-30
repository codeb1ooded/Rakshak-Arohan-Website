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
from django.contrib.auth import views as auth_views

from maps.views import *
from prediction.views import *
from crimeReporting.views import *
from api.views import *
from Notification.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='HOME_PAGE'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}),
    url(r'^signinup/$', sign_in_up_view),
    url(r'^signin/$', sign_in_view),
    url(r'^signup/$', sign_up_view),

    url(r'^viewMap/$', map_render),
    url(r'^prediction/$', predict_graph, name='predict_graph'),
    url(r'^register/$', request_page, name='request_page'),
    url(r'^most_prominent_city/$',prominent_city, name='most_prominent_city'),
    url(r'^most_prominent_crime/$', prominent_crime, name='most_prominent_crime'),
    url(r'^crime_status/$', crime_status, name='crime_status'),
    url(r'^firReg/$', fir_reg),
    url(r'^update_crime/', update_crime, name="update_crime"),
    url(r'^report/$', report,name="report"),
    url(r'^receive_alert/$', receive_alert,name="receive_alert"),
    url(r'^send_to_FIR/$', send_to_FIR, name="send_to_FIR"),
    url(r'^notifications/$',notifications,name="notifications"),

    # API urls
    url(r'^api/report_complaint/', reportComplaint),
    url(r'^api/all_reports/', all_reports_markers),
    url(r'^api/neighbourhood/', neighbourhood),
    url(r'^api/reported_crimes/', reported_crimes),
    url(r'^api/timeline/', timeline),
    url(r'^api/safest_route/', safest_route),
    url(r'^api/upload/$', uploadImage),
]
