import json

import requests

key = "f40998cd5bef60a3b6ed499e39c91a0b"


def getWeatherToday(place):
    address = "https://api.openweathermap.org/data/2.5/weather?q={0},uk&appid=f40998cd5bef60a3b6ed499e39c91a0b"
    print("getting the weather for ", place)
    response = requests.get(address.format(place))
    parsed = json.loads(response.text)
    return parsed

def getWeatherForecast(lat, lon):
    address = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&exclude=hourly, minutely, current&appid=f40998cd5bef60a3b6ed499e39c91a0b"
    url = address.format(lat, lon)
    response = requests.get(url)
    parsed = json.loads(response.text)
    return parsed




