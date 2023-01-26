from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_auto_prefetching import AutoPrefetchViewSetMixin

from django.db.models import Q

from account.custom_permissions import IsAdvisor
from .models import AdvisorsOnline
from .serializer import MakeOnlineSerializer, JobAssignBaySerializer, SerivesCurrentSerializer
from services.serializers import SerivesSerializer
from services.models import Services, BayDetails, BayCurrentJob


# Create your views here.
# class MakeOnline(APIView):
#     permission_classes = [IsAdvisor]
#     def patch(self, request,id):
#
#         user = request.user
#         if user.id != id:
#
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         else:
#             online = AdvisorsOnline.objects.get(advisor=user)
#             online.update(online=request.data.online)
#         return Response(status=status.HTTP_202_ACCEPTED)

class MakeOnline(generics.RetrieveUpdateAPIView):
    serializer_class = MakeOnlineSerializer
    queryset = AdvisorsOnline.objects.all()
    lookup_field = 'advisor'


class AvailableAdvisors(generics.ListAPIView):
    serializer_class = MakeOnlineSerializer
    queryset = AdvisorsOnline.objects.all()


# class CurrentJobs(generics.RetrieveUpdateAPIView):
#     serializer_class = SerivesSerializer
#     queryset = Services.objects.all()
#     lookup_field = 'advisor'

class CurrentJobs(AutoPrefetchViewSetMixin, APIView):
    def get(self, request, advisor_id):
        jobs = Services.objects.filter(Q(advisor=advisor_id) & ~Q(status='finished'))

        serializerobj = SerivesCurrentSerializer(jobs, many=True)
        data = serializerobj.data
        return Response(data, status=status.HTTP_200_OK)


class JobAssignerToBay(APIView):
    def post(self, request):
        serializer_obj = JobAssignBaySerializer(data=request.data)

        if serializer_obj.is_valid():
            bay = request.data['bay']
            Services.objects.filter(id=request.data['current_job']).update(status='in-bay')
            BayDetails.objects.filter(id=bay).update(status='busy')
            serializer_obj.save()
        return Response(status=status.HTTP_200_OK)
