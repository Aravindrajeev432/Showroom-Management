from rest_framework import serializers

from services.models import BayDetails, BayCurrentJob, Services
from account.models import Account
from cars.models import Cars, CarParts,UniPartNumbers




class BayDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BayDetails
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['model_name', 'model_year']


class ServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer()
    advisor = UserSerializer()

    class Meta:
        model = Services
        fields = '__all__'


class BayCurrentJobSerializer(serializers.ModelSerializer):
    current_job = ServiceSerializer()

    class Meta:
        model = BayCurrentJob
        fields = '__all__'


class LiveBaySerializer(serializers.ModelSerializer):
    related_bay = BayCurrentJobSerializer(many=True)
    attendable = serializers.SerializerMethodField()
    is_attending = serializers.SerializerMethodField()

    def get_attendable(self, instance):
        print(self.context['request'].user)
        is_attendable = BayDetails.objects.filter(mechanic_1=self.context['request'].user).exists()
        print(instance.mechanic_1)
        # if mechanic attending a job then mechanic cannot attend other jobs
        if is_attendable:
            return False
        # if another mechanic in bay working then ...
        elif instance.mechanic_1:
            return False
        # if bay is free
        else:
            return True

    def get_is_attending(self, instance):
        if instance.mechanic_1 == self.context['request'].user:
            return True
        else:
            return False

    class Meta:
        model = BayDetails
        fields = '__all__'


class BayJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BayDetails
        fields = ['mechanic_1']


class MyCurrentJobUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username']

class MyCurrentJobUniCarNumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniPartNumbers
        fields = '__all__'

class MyCurrentJobCartSerializer(serializers.ModelSerializer):
    uni_car_part_num=MyCurrentJobUniCarNumSerializer()
    class Meta:
        model = Cars
        fields = ['model_name','model_year','gear_type','uni_car_part_num']

class CurrentJobCarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model= CarParts
        fields = ['unique_part_name','price','labour_charge']

class CurrentJobCarSerializer(serializers.ModelSerializer):
    user = MyCurrentJobUserSerializer()
    advisor = MyCurrentJobUserSerializer()
    car = MyCurrentJobCartSerializer()
    parts_used = CurrentJobCarPartSerializer(many=True)

    class Meta:
        model = Services
        fields = '__all__'


class MyCurrentJobBaySerializer(serializers.ModelSerializer):
    # current_job = CurrentJobCarSerializer()
    current_job = serializers.SerializerMethodField()

    def get_current_job(self, instance):
        print(instance.current_job.status)
        service = Services.objects.get(status=instance.current_job.status)
        return CurrentJobCarSerializer(service).data

    class Meta:
        model = BayCurrentJob
        fields = '__all__'


class MyCurrentJobSerializer(serializers.ModelSerializer):
    related_bay = MyCurrentJobBaySerializer(many=True)

    class Meta:
        model = BayDetails
        fields = '__all__'


class CompatiblePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarParts
        fields = '__all__'


class ServicePartsUpdatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['parts_used']