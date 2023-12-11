from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'views'
urlpatterns = [
    path('', TemplateView.as_view(template_name='views/main.html')),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat', views.CatDetailView.as_view(), name='cat'),
    path('cars', views.CarListView.as_view(), name='cars'),
    path('car', views.CarDetailView.as_view(), name='car'),
    path('dogs', views.DogListView.as_view(), name='dogs'),
    path('dog', views.DogDetailView.as_view(), name='dog'),
    path('horses', views.HorseListView.as_view(), name='horses'),
    path('horse', views.HorseDetailView.as_view(), name='horse'),
]
