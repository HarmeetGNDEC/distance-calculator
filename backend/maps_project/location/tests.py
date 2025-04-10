import requests

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
    if data['status'] == 'OK' and data['results']:
        result = data['results'][0]
        return {
            'formatted_address': result['formatted_address'],
            'latitude': result['geometry']['location']['lat'],
            'longitude': result['geometry']['location']['lng']
        }

print(geocode_address('amritsar'))