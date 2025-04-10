# api/views.py
import requests
import math
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location

# Your Google Maps API key
GOOGLE_MAPS_API_KEY = "AlzaSysGrLQXEyxIu1W6c054CLQJhie983Y295s"


def geocode_address(address):
    """Get geocode from Google Maps API"""
    # endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = 'https://maps.gomaps.pro/maps/api/geocode/json'
    params = {
        'address': address,
        'key': GOOGLE_MAPS_API_KEY
    }

    response = requests.get(endpoint, params=params)
    data = response.json()
    print(data)

    if data['status'] == 'OK' and data['results']:
        result = data['results'][0]
        return {
            'formatted_address': result['formatted_address'],
            'latitude': result['geometry']['location']['lat'],
            'longitude': result['geometry']['location']['lng']
        }
    return None


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate geometric distance between coordinates"""
    # Convert to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers

    return round(c * r, 2)


class CalculateDistanceView(APIView):
    def post(self, request):
        origin_address = request.data.get('origin', '')
        destination_address = request.data.get('destination', '')

        if not origin_address or not destination_address:
            return Response({"error": "Both origin and destination are required"}, status=400)

        try:
            # Geocode origin
            origin_data = geocode_address(origin_address)
            if not origin_data:
                return Response({"error": "Could not geocode origin address"}, status=400)

            # Geocode destination
            destination_data = geocode_address(destination_address)
            if not destination_data:
                return Response({"error": "Could not geocode destination address"}, status=400)
            # Save to database
            origin = Location.objects.create(
                input_text=origin_address,
                formatted_address=origin_data['formatted_address'],
                latitude=origin_data['latitude'],
                longitude=origin_data['longitude']
            )

            destination = Location.objects.create(
                input_text=destination_address,
                formatted_address=destination_data['formatted_address'],
                latitude=destination_data['latitude'],
                longitude=destination_data['longitude']
            )

            # Calculate distance
            distance = calculate_distance(
                origin.latitude, origin.longitude,
                destination.latitude, destination.longitude
            )

            return Response({
                'origin': {
                    'formatted_address': origin.formatted_address,
                    'latitude': origin.latitude,
                    'longitude': origin.longitude
                },
                'destination': {
                    'formatted_address': destination.formatted_address,
                    'latitude': destination.latitude,
                    'longitude': destination.longitude
                },
                'distance': distance
            })

        except Exception as e:
            return Response({"error": str(e)}, status=500)