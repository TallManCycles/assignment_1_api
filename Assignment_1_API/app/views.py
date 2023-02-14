from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import datetime
import models.LocationsClass as Locations
import json


@require_http_methods(["GET"], )
def get_current_server_time(request):
    return HttpResponse(datetime.datetime.now())

"""
This function will load the travel locations from the server and display them to the user.

attributes:
    request: the request object
    
    returns:
        HttpResponse: the response object
"""
@require_http_methods(["GET"], )
def load_locations(request):

    travel_locations = [
        {'name': 'Lake District National Park', 'latitude': 54.4609, 'longitude': -3.0886},
        {'name': 'Corfe Castle', 'latitude': 50.6395, 'longitude': -2.0566},
        {'name': 'The Cotswolds', 'latitude': 51.8330, 'longitude': -1.8433},
        {'name': 'Cambridge', 'latitude': 52.2053, 'longitude': 0.1218},
        {'name': 'Bristol', 'latitude': 51.4545, 'longitude': -2.5879},
        {'name': 'Oxford', 'latitude': 51.7520, 'longitude': -1.257},
        {'name': 'Norwich', 'latitude': 52.6309, 'longitude': 1.2974},
        {'name': 'Stonehenge', 'latitude': 51.1789, 'longitude': -1.8262},
        {'name': 'Watergate Bay', 'latitude': 50.4429, 'longitude': -5.0553},
        {'name': 'Birmingham', 'latitude': 52.4862, 'longitude': -1.8904}
    ]

    # Convert the Python object to a JSON string
    travel_locations_json = json.dumps(travel_locations)

    # Return the JSON string as an HttpResponse
    return HttpResponse(travel_locations_json, content_type='application/json', status=200)