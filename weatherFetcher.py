import json

import requests


def getWeather(url, place):
    print("getting the weather for ", place)
    response = requests.get(url.format(place))
    parsed = json.loads(response.text)
    return parsed