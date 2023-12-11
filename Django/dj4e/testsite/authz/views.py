from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.http import urlencode


# Create your views here.
class OpenView(View):
    def get(self, request):
        return render(request, 'authz/main.html')


class ApereoView(View):
    def get(self, request):
        return render(request, 'authz/main.html')


class ManualProtect(View):
    def get(self, request):
        if not request.user.is_authenticated:
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'authz/main.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'authz/main.html')


class DumpyPython(View):
    def get(self, request):
        response = "<pre>\nUser Data in Python:\n\n"
        response += "Login url: " + reverse('login') + "\n"
        response += "Login url: " + reverse('logout') + "\n\n"
        if request.user.is_authenticated:
            response += "User: " + request.user.username + "\n"
            response += "Email: " + request.user.email + "\n"
        else:
            response += "User is not logged in\n"

        response += "\n"
        response += "</pre>\n"
        response += """<a href="/authz">Go back</a>"""
        return HttpResponse(response)

