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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="watches", default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']