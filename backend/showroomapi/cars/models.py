from django.db import models

from account.models import Account
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pyasn1.compat.octets import null


# Create your models here.

class Cars(models.Model):
    GEAR_TYPE_CHOICES = [
        ('AMT', 'AMT'),
        ('Manual', 'Manual'),
        ('DCT', 'DCT'),
    ]
    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
    ]

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='usercar', null=True)
    model_name = models.CharField(max_length=100)
    model_year = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True, choices=CAR_TYPE_CHOICES)
    colour = models.CharField(max_length=50)
    price = models.CharField(max_length=100, default=100000)
    chase_number = models.CharField(max_length=200, unique=True)
    engine_number = models.CharField(max_length=200, unique=True)
    seat_capacity = models.IntegerField()
    gear_type = models.CharField(max_length=100, choices=GEAR_TYPE_CHOICES)
    gear_count = models.CharField(max_length=50)
    engine_cc = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    engine_power = models.CharField(max_length=100)
    engine_torque = models.CharField(max_length=100)
    wheel_base = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    verified_by = models.CharField(max_length=100, null=True)
    universal_car_number = models.CharField(max_length=100,null=True)
    universal_part_number = models.CharField(max_length=100,null=True)


def nameFile(instance, filename):
    return '/cars'.join(['images', str(instance.model_name + instance.model_year), filename])
def namePicFile(instance, filename):
    return '/cars'.join(['images', str(instance.id), filename])


class Colours(models.Model):
    colour_name = models.CharField(max_length=50)


class GearType(models.Model):
    gear_type = models.CharField(max_length=50)


class FuelType(models.Model):
    fuel_type = models.CharField(max_length=50)




class DisplayCars(models.Model):


    CAR_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
    ]
    model_name = models.CharField(max_length=100)
    model_year = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True, choices=CAR_TYPE_CHOICES)
    colour = models.ManyToManyField(Colours)
    seat_capacity = models.IntegerField()
    gear_type = models.ManyToManyField(GearType)
    gear_count = models.CharField(max_length=50)
    engine_cc = models.CharField(max_length=100)
    fuel_type = models.ManyToManyField(FuelType)
    engine_power = models.CharField(max_length=100)
    engine_torque = models.CharField(max_length=100)
    wheel_base = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.model_name


class DisplayCarImages(models.Model):
    car = models.ForeignKey(DisplayCars,null=True,related_name='carimg',on_delete=models.CharField)
    image = models.ImageField(upload_to=namePicFile, blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "webp"])])


