from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'rest/index.html')


def bounce(request):    # have to ask someone
    return HttpResponseRedirect('https://www.google.lk')
