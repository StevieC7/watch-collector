from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Watch, Brand, Collection

# Create your views here.
class Home(ListView):
    template_name = "home.html"
    model = Brand
    paginate_by: 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["collections"] = Collection.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class Index(ListView):
    template_name = "index.html"
    model = Watch
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watches"] = Watch.objects.all()
        return context

class Inspect(DetailView):
    model = Watch
    template_name = "inspect.html"

class AddWatch(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        size = request.POST.get("size")
        image = request.POST.get("image")
        primary_color = request.POST.get("primary_color")
        jm_owns = request.POST.get("jm_owns")
        brand = Brand.objects.get(pk=pk)
        Watch.objects.create(name=name, size=size, image=image,primary_color=primary_color,brand=brand, jm_owns=jm_owns)
        return redirect('brand_inspect', pk=pk)

class UpdateWatch(UpdateView):
    model = Watch
    fields = ['name', 'size', 'image', 'primary_color', 'brand', 'jm_owns']
    template_name = 'watch_update.html'
    success_url = 'index/'

class DeleteWatch(DeleteView):
    model = Watch
    template_name = 'watch_delete.html'
    success_url = '/'

class BrandInspect(DetailView):
    model = Brand
    template_name = "brand_inspect.html"

class AddBrand(CreateView):
    model = Brand
    fields = ['name']
    template_name = 'create.html'
    success_url = '/'

class UpdateBrand(UpdateView):
    model = Brand
    fields = ['name']
    template_name = 'brand_update.html'
    success_url = 'index/'

class DeleteBrand(DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = '/'