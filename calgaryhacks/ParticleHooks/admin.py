from django.contrib import admin
from .models import Devices, PhoneNumber

# Register your models here.
admin.site.register(Devices)
admin.site.register(PhoneNumber)