from django.shortcuts import render

# Create your views here.
def map_render(request):
    return render(request, 'map.html')
