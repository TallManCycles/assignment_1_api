import requests
import json
import configparser
from Assignment_1_API.models.WeatherClass import Weather
from Assignment_1_API.models.LocationsClass import Location

# API KEY CONSTANT
API_KEY = ''
with open("Assignment_1_API/api_key.txt", "r") as file:
    API_KEY = file.read()


def getWeatherByCoordinates(lat, lon):
    if not API_KEY:
        return Weather('API key not found')

    lat_long_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(lat_long_url)

    if response.status_code == 200:
        if response.content != '':
            weather_data = json.loads(response.content)
            return Weather(weather_data)
        else:
            return Weather('no weather data found')
    else:
        return Weather('No weather data found')


def getWeatherByLocation(location_name):
    if not API_KEY:
        return 'API key not found'

    location_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit=5&appid={API_KEY}'
    response = requests.get(location_url)

    if response.status_code == 200:
        location = json.loads(response.content)
        if location and len(location) > 0:
            location_data = Location(location[0]['name'], location[0]['lat'], location[0]['lon'])
            return getWeatherByCoordinates(location_data.lat, location_data.lon)
        else:
            return 'No weather data found'
    else:
        return 'No weather data found'


