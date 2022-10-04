from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Watch(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    primary_color = models.CharField(
        max_length=15,
        choices=[
            ("Black", "black"),
            ("White", "white"),
            ("Gold", "gold"),
            ("Silver", "silver"),
            ("Brown", "brown")
        ],
        default="Black"
    )
    image = models.CharField(max_length=100)
    jm_owns = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="watches", default=1)
    
    def mayer_also_owns(self):
        also_owns = [ self.jm_owns, Watch.objects.filter(brand = self.brand).filter(jm_owns = True).exclude(id = self.pk)]
        return also_owns

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Collection(models.Model):
    name = models.CharField(max_length=100)
    watches = models.ManyToManyField(Watch)

    def __str__(self):
        return self.name