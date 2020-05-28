import requests
import json
from datetime import datetime

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

def displayTemperature(parsedWeather):
    temp = parsedWeather["main"]["temp"]
    celcius = temp - 273.15
    print("temp is", celcius)

def displayWind(parsedWeather):
    wind = parsedWeather["wind"]["speed"]
    gust = parsedWeather["wind"]["gust"]
    display_wind = str.format("wind speed is {} and the gust is {}", wind, gust)
    print(display_wind)

def displaySunriseSunset(parsedWeather):
    sunrise_unix = parsedWeather["sys"]["sunrise"]
    sunrise = datetime.utcfromtimestamp(sunrise_unix).strftime('%H:%M:%S')
    sunset_unix = parsedWeather["sys"]["sunset"]
    sunset = datetime.utcfromtimestamp(sunset_unix).strftime('%H:%M:%S')
    print(str.format("sun will rise at {} and the sun will set at {}", sunrise, sunset))

weather = getWeather(address, location)
displayTemperature(weather)
displayWind(weather)
displaySunriseSunset(weather)
