from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect, render
# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context

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
    success_url = '/watches'

class DeleteWatch(DeleteView):
    model = Watch
    template_name = 'watch_delete.html'
    success_url = '/'

class BrandIndex(ListView):
    template_name = "brand_index.html"
    model = Brand
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        return context

class BrandInspect(DetailView):
    model = Brand
    template_name = "brand_inspect.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collections"] = Collection.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
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

class CollectionSongAssoc(View):
    def get(self,request,pk,watch_pk):
        assoc = request.GET.get("assoc")
        
        if assoc == "remove":
            Collection.objects.get(pk=pk).watches.remove(watch_pk)

        if assoc == "add":
            Collection.objects.get(pk=pk).watches.add(watch_pk)

        return redirect('home')

class CollectionIndex(ListView):
    template_name = "collection_index.html"
    model = Collection
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated == True:
            context["collections"] = Collection.objects.filter(user=self.request.user)
        else:
            context["collections"] = []
        return context

class CollectionInspect(DetailView):
    model = Collection
    template_name = "collection_inspect.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["collections"] = Collection.objects.all()
    #     return context

@method_decorator(login_required, name='dispatch')
class AddCollection(CreateView):
    model = Collection
    fields = ['name']
    template_name = 'collection_create.html'
    success_url = '/collections/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCollection, self).form_valid(form)

class DeleteCollection(DeleteView):
    model = Collection
    template_name = 'collection_delete.html'
    success_url = '/'

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("collection_index")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
