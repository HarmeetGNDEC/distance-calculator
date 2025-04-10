from rest_framework import serializers
from .models import Location, Distance


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'input_text', 'formatted_address', 'latitude', 'longitude',
                  'street_number', 'street_name', 'city', 'state', 'country', 'postal_code']


class DistanceRequestSerializer(serializers.Serializer):
    origin = serializers.CharField(max_length=255)
    destination = serializers.CharField(max_length=255)


# class DistanceResponseSerializer(serializers.Serializer):
#     origin = LocationSerializer()
#     destination = LocationSerializer()
#     distance = serializers.DecimalField(max_digits=10, decimal_places=2)