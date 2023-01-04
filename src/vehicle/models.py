from django.db import models


# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
