from display import displayTemperature, displayWind, displaySunriseSunset
from input import getLocation
from weatherFetcher import getWeather

key = "f40998cd5bef60a3b6ed499e39c91a0b"
address = "http://api.openweathermap.org/data/2.5/weather?q={0},uk&appid=f40998cd5bef60a3b6ed499e39c91a0b"

location = getLocation()
weather = getWeather(address, location)
displayTemperature(weather)
displayWind(weather)
displaySunriseSunset(weather)
