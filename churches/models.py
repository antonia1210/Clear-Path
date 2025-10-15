from django.db import models

from items.models import Item
# Create your models here.

class Church(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
