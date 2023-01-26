from django.contrib import admin
from .models import ServiceInfo,Services,BayCurrentJob,BayDetails
# Register your models here.

admin.site.register(ServiceInfo)
admin.site.register(Services)
admin.site.register(BayCurrentJob)
admin.site.register(BayDetails)