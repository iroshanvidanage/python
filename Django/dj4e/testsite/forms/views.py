from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from forms.forms import BasicForm
import html


def example(request):
    form = BasicForm()
    return HttpResponse(form.as_table())


def dumpdata(place, data):
    return_val = ""
    if len(data) > 0:
        return_val += '<p>Incoming ' + place + ' data:<br/>\n'
        for key, value in data.items():
            return_val += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        return_val += '</p>\n'
    return return_val


class DumpPostView(View):
    def post(self, request):
        dump = dumpdata('POST', request.POST)
        ctx = {'title': 'request.POST', 'dump': dump}
        return render(request, 'forms/dump.html', ctx)


class SimpleCreate(DumpPostView):
    def get(self, request):
        form = BasicForm()
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)


class SimpleUpdate(DumpPostView):
    def get(self, request):
        old_data = {
            'title': 'SakaiCar',
            'mileage': 42,
            'purchase_data': '2021-10-20'
        }
        form = BasicForm(old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

