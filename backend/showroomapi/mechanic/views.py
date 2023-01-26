from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

import json
from rest_framework import generics
from django.db.models import Q
# Create your views here.

from django_auto_prefetching import AutoPrefetchViewSetMixin

from services.models import BayDetails,Services
from .serializers import BayDetailsSerializer, LiveBaySerializer, BayJoinSerializer, MyCurrentJobSerializer, \
    CompatiblePartsSerializer,ServicePartsUpdatorSerializer
from cars.models import CarParts


class GetBays(AutoPrefetchViewSetMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LiveBaySerializer
    queryset = BayDetails.objects.all().order_by('id')

    def get_serializer_context(self):
        return {'request': self.request}


class BayJoin(generics.UpdateAPIView):
    serializer_class = BayJoinSerializer
    queryset = BayDetails.objects.all()
    lookup_field = 'pk'


class MyCurrentJob(AutoPrefetchViewSetMixin, APIView):
    def get(self, request):
        bay_details = BayDetails.objects.get(mechanic_1=request.user)
        serializerobj = MyCurrentJobSerializer(bay_details)


        return Response(data=serializerobj.data, status=status.HTTP_200_OK)


class CompatibleParts(AutoPrefetchViewSetMixin, generics.ListAPIView):
    serializer_class = CompatiblePartsSerializer
    queryset = CarParts.objects.all()
    lookup_field = 'id'

class ServicePartsUpdator(generics.UpdateAPIView):
    serializer_class = ServicePartsUpdatorSerializer
    queryset = Services.objects.all()
    lookup_field = 'pk'

class ServiceMechanicCompleter(APIView):
    def get(self,request):

        return Response(status= status.HTTP_200_OK)