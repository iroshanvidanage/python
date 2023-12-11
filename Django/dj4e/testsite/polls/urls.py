from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # name is not essential
    path('danger', views.danger),
]

