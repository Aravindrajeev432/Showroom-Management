from rest_framework import serializers

from account.models import Account
from cars.models import Cars
from .models import Services

class SerivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
