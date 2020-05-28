import requests
import json

from display import displayTemperature, displayWind, displaySunriseSunset

location = input("please enter your location:\n")
if location == "":
    location = "dyserth"

key = "f40998cd5bef60a3b6ed499e39c91a0b"
address = "http://api.openweathermap.org/data/2.5/weather?q={0},uk&appid=f40998cd5bef60a3b6ed499e39c91a0b"

def getWeather(url, place):
    print("getting the weather for ", place)
    response = requests.get(url.format(place))
    parsed = json.loads(response.text)
    return parsed


weather = getWeather(address, location)
displayTemperature(weather)
displayWind(weather)
displaySunriseSunset(weather)
