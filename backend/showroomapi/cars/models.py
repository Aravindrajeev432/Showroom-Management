from django.db import models

from account .models import Account


# Create your models here.

class Cars(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    model_name = models.CharField(max_length=100)
    model_year = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    chase_number = models.CharField(max_length=200)
    engine_number = models.CharField(max_length=200)
    seat_capacity = models.IntegerField()
    gear_type = models.CharField(max_length=100)
    gear_count = models.CharField(max_length=50)
    engine_cc = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    engine_power = models.CharField(max_length=100)
    engine_torque = models.CharField(max_length=100)
    wheel_base = models.CharField(max_length=100)

class DisplayCars(models.Model):
    model_name = models.CharField(max_length=100)
    model_year = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    chase_number = models.CharField(max_length=200)
    engine_number = models.CharField(max_length=200)
    seat_capacity = models.IntegerField()
    gear_type = models.CharField(max_length=100)
    gear_count = models.CharField(max_length=50)
    engine_cc = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    engine_power = models.CharField(max_length=100)
    engine_torque = models.CharField(max_length=100)
    wheel_base = models.CharField(max_length=100)
    image = models.ImageField()
