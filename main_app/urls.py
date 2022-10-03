from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('brands/<int:pk>/', views.BrandInspect.as_view(), name="brand_inspect"),
    path('brands/new', views.AddBrand.as_view(), name="add_brand"),
    path('about/', views.About.as_view(), name="about"),
    path('watches/', views.Index.as_view(), name="index"),
    path('watches/<int:pk>/', views.Inspect.as_view(), name="inspect"),
    path('watches/<int:pk>/update', views.UpdateWatch.as_view(), name="update_watch"),
    path('watches/<int:pk>/delete', views.DeleteWatch.as_view(), name="delete_watch"),
    path('brands/<int:pk>/watches/new/', views.AddWatch.as_view(), name="add_watch"),
]