from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'autos'

urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
]