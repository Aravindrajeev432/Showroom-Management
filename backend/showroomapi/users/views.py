from django.db.migrations import serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import Account
from cars.models import Cars
from django.contrib.auth import authenticate

from .serializers import MyCarsSerializer
from django_auto_prefetching import AutoPrefetchViewSetMixin

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['phone_number'] = user.phone_number

        # ...

        return token

class UserLogin(APIView,TokenObtainPairSerializer):

    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['phone_number'] = user.phone_number

        # ...
        print(token.access_token)
        return token

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return self.get_token(refresh)
        # return {
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),
        # }

    def post(self, request):

        data = request.data
        user = authenticate(username=data['username'], password=data['password'])

        if user is None:

            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # checking for staff members is customer or not
        elif not user.is_customer:

            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if user.is_customer:
            # token = self.get_tokens_for_user(user)
            token = self.get_token(user)
            data = {
                    'refresh': str(token),
                    'access': str(token.access_token)
            }

        return Response(data=data, status=status.HTTP_200_OK)


class GetMyCars(AutoPrefetchViewSetMixin,generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    model = Cars
    serializer_class = MyCarsSerializer

    def get_queryset(self):
        # user= Account.objects.get(id=self.request.user)
        return Cars.objects.filter(user=self.request.user).order_by('id')
# class GetMyCars(APIView):
#     def get(self,request):
#         permission_classes = [IsAuthenticated]
#         query = Cars.objects.filter(user=self.request.user)
#         serializer_classobj = MyCarsSerializer(query,many=True,context={'id':'sad'})
#
#         return Response(serializer_classobj.data)
#         def get_queryset(self):
#             # user= Account.objects.get(id=self.request.user)
#             return Cars.objects.filter(user=self.request.user)