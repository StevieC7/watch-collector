from django.contrib import admin
from .models import Collection, Watch, Brand
# Register your models here.
admin.site.register(Watch)
admin.site.register(Brand)
admin.site.register(Collection)