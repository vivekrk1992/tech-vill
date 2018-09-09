from django.contrib import admin
from maligai.models import *

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'owner', 'insurance_data')
admin.site.register(Vehicle, VehicleAdmin)

