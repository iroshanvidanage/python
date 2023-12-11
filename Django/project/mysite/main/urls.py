from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="v1"),
    path("v2/", views.v2, name="v2"),
    path("iroshan/", views.iroshan, name="iroshan"),
    path("test/", views.test, name="test"),
    path("<str:name>", views.index, name="index"),
]

