from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Watch, Brand

# Create your views here.
class Home(ListView):
    template_name = "home.html"
    model = Brand
    paginate_by: 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
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