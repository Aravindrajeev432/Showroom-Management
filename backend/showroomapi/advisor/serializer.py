from rest_framework import serializers
from .models import AdvisorsOnline
from services.models import BayDetails,BayCurrentJob,Services

class MakeOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorsOnline
        fields = '__all__'


class BayCurrentJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BayCurrentJob
        fields = '__all__'

class SerivesCurrentSerializer(serializers.ModelSerializer):
    service_bay = BayCurrentJobSerializer(many=True,read_only=True)
    class Meta:
        model = Services
        fields = '__all__'

class JobAssignBaySerializer(serializers.ModelSerializer):
    # bay = BayCurrentJobSerializer(many=True)
    class Meta:
        model = BayCurrentJob
        fields = '__all__'
