from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Services
from .serializers import  SerivesSerializer
class AllServices(generics.ListAPIView):
    model = Services
    serializer_class = SerivesSerializer
    queryset = Services.objects.all()
