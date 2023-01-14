from django.urls import path
from .views import UserLogin,GetMyCars
urlpatterns = [
    path('usertest',UserLogin.as_view(), name='index'),
    path('mycars',GetMyCars.as_view(),name='mycars'),
    ]