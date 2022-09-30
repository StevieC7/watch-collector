from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Watch(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    primary_color = models.Choices(
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
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']