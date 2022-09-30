from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Watch

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
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
