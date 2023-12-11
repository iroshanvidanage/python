from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cookie(request):
    print(request.COOKIES)
    oldValue = request.COOKIES.get('iroshan', None)
    response = HttpResponse('In a view - oldValue of the cookie is: ' + str(oldValue))

    if oldValue:
        response.set_cookie('iroshan', int(oldValue) + 1)   # no expiration time= until browser closes (session cookies)
    else:
        response.set_cookie('iroshan', 42)  # no expiration time= until browser closes (session cookies)
    response.set_cookie('Iroshan', 42, max_age=1000)    # expiration is in 1000seconds

    return response


