from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape


# Create your views here.

def index(request):
    return HttpResponse("Hello, Everyone. Welcome to Polls")


def danger(request):
    response = {'guess': str(escape(request.GET['guess']))}
    return render(request, 'polls/danger.html', response)
