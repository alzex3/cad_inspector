from rest_framework import serializers

from .models import FacilityType, Facility


class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityType
        fields = [
            'name',
            'verbose_name',
        ]


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = [
            'num',
            'type',
            'address',
            'full_address',
            'update_date',
            'created_date',
            'cost',
            'stamp',
        ]
