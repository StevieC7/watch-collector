from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
class About(TemplateView):
    template_name = "about.html"
class Index(TemplateView):
    template_name = "index.html"
