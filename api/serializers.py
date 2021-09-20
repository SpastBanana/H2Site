from rest_framework import serializers
from .models import deltaStatus

class viewDeltaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = deltaStatus
        fields = '__all__'
