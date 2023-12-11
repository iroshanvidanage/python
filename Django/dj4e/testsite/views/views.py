from views.models import Cat, Car, Horse, Dog
from django.shortcuts import render
from django.views import View, generic


# Create your views here.

class IAVListView(View):
    def get(self, request):
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff}
        return render(request, 'views/'+modelname+'_list.html', cntx)


def index(request):
    return render(request, 'views/index.html')


class CatListView(View):
    def get(self, request):
        stuff = Cat.objects.all()
        cntx = {'cat_list': stuff}
        return render(request, 'views/cat_list.html', cntx)


class CatDetailView(generic.DetailView):
    model = Cat


class DogListView(View):
    model = Dog

    def get(self, request):
        m_name = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { m_name+'_list': stuff}
        return render(request, 'views/'+m_name+'_list.html', cntx)


class DogDetailView(generic.DetailView):
    model = Cat


class CarListView(IAVListView):
    model = Car


class CarDetailView(generic.DetailView):
    model = Cat


class HorseListView(generic.ListView):
    model = Horse


class HorseDetailView(generic.DetailView):
    model = Cat


"""

"""