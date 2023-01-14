from django.db.models import signals
from django.dispatch import receiver
from .models import Cars


@receiver(signals.pre_save, sender=Cars)
def set_universal_numbers(sender, instance,using, **kwargs):
    uni_car_num = instance.model_name + '-' + instance.model_year
    uni_part_num = instance.model_name + '-' + instance.model_year + instance.gear_type + '-' + instance.fuel_type
    instance.universal_car_number = uni_car_num.upper()
    instance.universal_part_number = uni_part_num.upper()
