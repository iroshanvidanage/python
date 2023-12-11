from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.

def index(request, name=False):  # this index_id name should be same name as in urls
    ls = ToDoList.objects.get(name=name)    # the entries in models
    item = ls.item_set.get(id=1)

    if not name:
        return HttpResponse("<h1>First site created with Django</h1>")
    else:
        return HttpResponse("<h1>%s</h1><br><p>%s</p>" % (ls.name, str(item.text)))


def v1(request):
    return HttpResponse("<h1>View 1: site created with Django</h1>")


def v2(request):
    return HttpResponse("<h1>View 2: second site created with Django</h1>")


def iroshan(request):
    return HttpResponse("<h1>Iroshan</h1>")


def test(request):
    return HttpResponse("""
    <!doctype html>
    <html>
    <head>
    <title>Test HTML Page</title>
    <meta name="description" content="Our first page">
    <meta name="keywords" content="html tutorial template">
    </head>
    <body>
    <h1>Test response is successful.</h1>
    <br>
    <h2>Iroshan</h2>
    </body>
    </html>
    """)
