from django.contrib import admin
from Epolice_django.models import Citizen, Complaints

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Complaints)