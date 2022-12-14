from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('brands/', views.BrandIndex.as_view(), name="brand_index"),
    path('brands/<int:pk>/', views.BrandInspect.as_view(), name="brand_inspect"),
    path('brands/<int:pk>/update', views.UpdateBrand.as_view(), name="update_brand"),
    path('brands/<int:pk>/delete', views.DeleteBrand.as_view(), name="delete_brand"),
    path('brands/new', views.AddBrand.as_view(), name="add_brand"),
    path('about/', views.About.as_view(), name="about"),
    path('watches/', views.Index.as_view(), name="index"),
    path('watches/<int:pk>/', views.Inspect.as_view(), name="inspect"),
    path('watches/<int:pk>/update', views.UpdateWatch.as_view(), name="update_watch"),
    path('watches/<int:pk>/delete', views.DeleteWatch.as_view(), name="delete_watch"),
    path('brands/<int:pk>/watches/new/', views.AddWatch.as_view(), name="add_watch"),
    path('collections/', views.CollectionIndex.as_view(), name="collection_index"),
    path('collections/new', views.AddCollection.as_view(), name="add_collection"),
    path('collections/<int:pk>/', views.CollectionInspect.as_view(), name="collection_inspect"),
    path('collections/<int:pk>/delete', views.DeleteCollection.as_view(), name="collection_delete"),
    path('collections/<int:pk>/watches/<int:watch_pk>/', views.CollectionSongAssoc.as_view(), name="collection_watch_assoc"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']