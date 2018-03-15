from django.shortcuts import render
from .models import USER, FIR_REPORT
from .forms import FirRegistrationForm
# Create your views here.


def fir_reg(request):
    if request.method == "POST":
      form = FirRegistrationForm(request.POST)
      if form.is_valid():
          data = form.save(commit=False)
          # data.username = request.session.get('username')
          data.save()

          address = form.cleaned_data['FIR_LOC']
          api_key = "AIzaSyC1huk3kiK15mK6Bs6O83AbvJo_ZlX-UrY"
          api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
          api_response_dict = api_response.json()
          if api_response_dict['status'] == 'OK':
              LAT = api_response_dict['results'][0]['geometry']['location']['lat']
              LNG = api_response_dict['results'][0]['geometry']['location']['lng']
              print 'Latitude:', latitude
              print 'Longitude:', longitude
              
          return render(request, 'done.html')
    else:
      form = FirRegistrationForm()
    return render(request, 'fir_new.html', {'form': form})
