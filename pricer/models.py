from django.db import models

# Create your models here.
class Pop(models.Model):
    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)

