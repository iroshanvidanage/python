from django.urls import path
from . import views

app_name = 'getpost'
urlpatterns = [
    path('', views.index ),
    path('getForm', views.getForm),
    path('postForm', views.postForm),
    path('submitForm', views.submitForm),
    path('studentForm', views.studentForm),
    path('csrfForm', views.csrfForm),
    path('classy', views.ClassyView.as_view()),
]