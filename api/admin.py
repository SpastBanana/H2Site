from django.contrib import admin
from .models import deltaStatus


class deltaStatusAdmin(admin.ModelAdmin):
    list_display = ('meting_id',)


admin.site.register(deltaStatus, deltaStatusAdmin)
