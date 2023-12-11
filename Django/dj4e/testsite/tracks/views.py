from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tracksite(request):
    return render(request, 'tracks/tracks.html')
