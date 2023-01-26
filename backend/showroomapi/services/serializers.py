from rest_framework import serializers

from account.models import Account
from cars.models import Cars
from rest_framework.serializers import ModelSerializer

from .models import Services, ServiceInfo,BayDetails


class SerivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ServiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = '__all__'


# class CarsServiceDistinct(serializers.Serializer):
#     universal_car_number=

class UniCarNumSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='universal_car_number')
    value = serializers.CharField(source='universal_car_number')

    class Meta:
        model = Cars
        # fields = ('universal_car_number',)
        fields = ['value', 'label']
        # read_only_fields = ('universal_car_number',)


class BayDetailsSerializer(serializers.ModelSerializer):
    print('IN baydetails serilaizer')
    class Meta:
        model = BayDetails
        fields = '__all__'



