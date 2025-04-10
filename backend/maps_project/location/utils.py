import os
import requests
import math
from decimal import Decimal
from django.conf import settings


def geocode_address(address):
    """
    Convert address string to geocode using Google Maps Geocoding API
    """
    api_key = settings.GOOGLE_MAPS_API_KEY
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        'address': address,
        'key': api_key
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()

        if data['status'] == 'OK' and data['results']:
            result = data['results'][0]
            location_data = {
                'formatted_address': result['formatted_address'],
                'latitude': Decimal(str(result['geometry']['location']['lat'])),
                'longitude': Decimal(str(result['geometry']['location']['lng'])),
                'components': {}
            }

            # Extract address components
            for component in result['address_components']:
                for component_type in component['types']:
                    location_data['components'][component_type] = component['long_name']

            # Map components to model fields
            component_mapping = {
                'street_number': 'street_number',
                'street_name': 'route',
                'city': 'locality',
                'state': 'administrative_area_level_1',
                'country': 'country',
                'postal_code': 'postal_code'
            }

            for model_field, component_type in component_mapping.items():
                location_data[model_field] = location_data['components'].get(component_type)

            # Remove components from result
            del location_data['components']

            return location_data
        else:
            raise Exception(f"Geocoding API error: {data.get('status', 'Unknown error')}")

    except Exception as e:
        raise Exception(f"Error geocoding address: {str(e)}")


def reverse_geocode(lat, lng):
    """
    Convert lat/lng to address using Google Maps Reverse Geocoding API
    """
    api_key = settings.GOOGLE_MAPS_API_KEY
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        'latlng': f"{lat},{lng}",
        'key': api_key
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()

        if data['status'] == 'OK' and data['results']:
            return data['results'][0]['formatted_address']
        else:
            raise Exception(f"Reverse Geocoding API error: {data.get('status', 'Unknown error')}")

    except Exception as e:
        raise Exception(f"Error reverse geocoding: {str(e)}")


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [float(lat1), float(lon1), float(lat2), float(lon2)])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers

    return round(c * r, 2)