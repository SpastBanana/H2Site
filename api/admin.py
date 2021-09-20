from django.contrib import admin
from .models import vehicleStatus


class vehicleStatusAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id',)


admin.site.register(vehicleStatus, vehicleStatusAdmin)
