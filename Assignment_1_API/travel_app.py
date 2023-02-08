import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')


API_KEY = config['API']['KEY']

lat = '54.4609'
lon = '3.0886'
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    weather = json.loads(response.content)

    print(weather['weather'][0]['description'])

