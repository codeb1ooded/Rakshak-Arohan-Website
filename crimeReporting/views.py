from django.shortcuts import render
from .models import USER, FIR_REPORT
from .forms import FirRegistrationForm
import requests
# from googlemaps import GoogleMaps
# Create your views here.


def fir_reg(request):
    if request.method == "POST":
      form = FirRegistrationForm(request.POST)
      address = request.POST.get('address')
      print "=" * 30
      print address
      if form.is_valid():
          # print "***********************"
          data = form.save(commit=False)
          data.username = request.session.get('username')
          data.FIR_LOC = address
          api_key = "AIzaSyDA72RxHoUnAPfspsUxDgVykHK2ONPIckc"
          api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
          print api_response
          api_response_dict = api_response.json()
          if api_response_dict['status'] == 'OK':
              data.LAT = api_response_dict['results'][0]['geometry']['location']['lat']
              data.LNG = api_response_dict['results'][0]['geometry']['location']['lng']
          data.save()

          return render(request, 'done.html')
    else:
      form = FirRegistrationForm()
    return render(request, 'fir_new.html', {'form': form})
