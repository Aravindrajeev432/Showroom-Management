from django.db import models
from account.models import Account
from cars.models import Cars


# Create your models here.
class Services(models.Model):
    SERVICE_STATUS_CHOICES =[
        ('requested','requested'),
        ('assigned','assigned'),
        ('finished','finished'),
    ]
    user = models.ForeignKey(Account, on_delete=models.SET_NULL,null=True)
    car = models.ForeignKey(Cars, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=SERVICE_STATUS_CHOICES)
    finished_at = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

