from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.contrib.auth.models import User
from django.http import *
from django.conf import settings
from database.functions import *
from crimeReporting.forms import *
from .models import USER, FIR_REPORT
from .forms import FirRegistrationForm

@login_required(login_url="/signinup/")
def fir_reg(request):
    is_logged_in = request.user.is_authenticated()
    context = {
        'is_logged_in' : is_logged_in,
    }
    if request.method == "POST":
      form = FirRegistrationForm(request.POST)
      address = request.POST.get('address')
      print (address)
      
      if form.is_valid():
          # print "***********************"
          data = form.save(commit=False)
          data.username = request.session.get('username')
          data.FIR_LOC = address
          api_key = "AIzaSyDA72RxHoUnAPfspsUxDgVykHK2ONPIckc"
          api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
          print (api_response)
          api_response_dict = api_response.json()
          if api_response_dict['status'] == 'OK':
              data.LAT = api_response_dict['results'][0]['geometry']['location']['lat']
              data.LNG = api_response_dict['results'][0]['geometry']['location']['lng']
          data.save()

          return render(request, 'done.html')
    else:
      form = FirRegistrationForm()
    return render(request, 'fir_new.html', {'form': form, 'is_logged_in': is_logged_in,})

@login_required(login_url="/signinup/")
def analyse_selected_area(request):
    north = request.GET['north']
    east = request.GET['east']
    west = request.GET['west']
    south = request.GET['south']

    return HttpResponse(north + "<br/>" + east + "<br/>" + west + "<br/>" + south)


def home(request):
  if request.user.is_authenticated():
    return HttpResponseRedirect("/viewMap/")
  else:
    return render(request, 'home.html')


def sign_in_up_view(request):
  signin_form = UserAuthenticationForm()
  singnup_form = UserRegistrationForm()
  return render(request, 'home.html', {'signin' : signin_form, 'signup':singnup_form})


def sign_in_view(request):
    form = UserAuthenticationForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        username = userObj['username']
        password =  userObj['password']
        user = authenticate(username=username, password=password)
        global varuser
        varuser=user
        if user is not None:

            login(request, user)
            if 'next' in request.POST:
              return redirect(request.POST.get('next'))
            else:
              return HttpResponseRedirect("/viewMap/")
        else:
            messages.error(request, "Looks like a user with that username or password doesn't exist!")
            return HttpResponseRedirect('/')
    messages.error(request, "You have not filled valid details, please try again!")
    return HttpResponseRedirect('/')

def sign_up_view(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        userObj = form.cleaned_data
        name = userObj['name']
        username = userObj['username']
        email =  userObj['email']
        password =  userObj['password']
        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username = username, password = password)
            create_user(user, name)
            login(request, user)
            return HttpResponseRedirect("/viewMap/")
        else:
            messages.error(request, "Looks like a username with that email or password already exists!")
            return HttpResponseRedirect('/')
    messages.error(request, "You have not filled valid details, please try again!")
    return HttpResponseRedirect('/')
