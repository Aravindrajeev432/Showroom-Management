from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django.db.models import Q

from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.
from .models import Services, ServiceInfo, BayDetails
from .serializers import SerivesSerializer, UniCarNumSerializer, ServiceInfoSerializer, \
    BayDetailsSerializer
from cars.models import Cars
from .pagination import ServiceInfoPagination


class AllServices(AutoPrefetchViewSetMixin, generics.ListAPIView):
    serializer_class = SerivesSerializer
    queryset = Services.objects.all()


class GetUniCarNum(AutoPrefetchViewSetMixin, APIView):
    def get(self, request):
        # universal car number
        uni_car_num = Cars.objects.values('universal_car_number').distinct('universal_car_number').filter(
            ~Q(universal_car_number__in=ServiceInfo.objects.all().values_list('universal_car_number', flat=True)))

        serializerobj = UniCarNumSerializer(uni_car_num, many=True)

        # the response is value ,label format for react select package
        return Response(data=serializerobj.data, status=status.HTTP_200_OK)


# from car models all universal car number
class GetDistinctUniCarNum(generics.ListAPIView):
    serializer_class = UniCarNumSerializer
    queryset = Cars.objects.values('universal_car_number').distinct('universal_car_number')


class AddServiceInfo(generics.CreateAPIView):
    serializer_class = ServiceInfoSerializer
    queryset = ServiceInfo.objects.all()


class ShowServiceinfo(generics.ListAPIView):
    pagination_class = ServiceInfoPagination
    serializer_class = ServiceInfoSerializer
    queryset = ServiceInfo.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['universal_car_number']


class RequestService(APIView):
    def post(self, request):
        # {'car':'car_id'}
        print(request.data)
        try:
            car = Cars.objects.get(id=request.data['car'])
            service_check = Services.objects.filter(Q(car=car) & ~Q(status='finished'))
            if not service_check.exists():
                print("Okay to accept the request")
                service = Services.objects.create(car=car, status='requested', user=request.user)
                service.save()

                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        except Cars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class Service(APIView):
    def get(self, request, service_status):
        print(service_status)
        s = Services.objects.filter(status=service_status)
        print(s)
        serializerobj = SerivesSerializer(s, many=True)
        return Response(serializerobj.data, status=status.HTTP_200_OK)


class ServiceAssignAdvisor(generics.UpdateAPIView):
    serializer_class = SerivesSerializer
    queryset = Services.objects.all()
    lookup_field = 'id'


class GetFreeBays(generics.ListAPIView):
    serializer_class = BayDetailsSerializer
    queryset = BayDetails.objects.filter(status='free')



