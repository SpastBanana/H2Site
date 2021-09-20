from rest_framework import serializers
from .models import vehicleStatus

class viewVehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleStatus
        fields = '__all__'
