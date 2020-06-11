import json
import os

import requests

def getWeatherToday(place):
    address = "https://api.openweathermap.org/data/2.5/weather?q={0},uk&appid={1}"
    print("getting the weather for ", place)
    response = requests.get(address.format(place, os.getenv('WEATHER_KEY')))
    parsed = json.loads(response.text)
    return parsed

def getWeatherForecast(lat, lon):
    address = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&exclude=hourly, minutely, current&appid={2}"
    print(address)
    url = address.format(lat, lon, os.getenv('WEATHER_KEY'))
    response = requests.get(url)
    parsed = json.loads(response.text)
    return parsed




