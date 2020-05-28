from display import displayTemperature, displayWind, displaySunriseSunset
from input import getLocation
from weatherFetcher import getWeatherToday


location = getLocation()
weather = getWeatherToday(location)
displayTemperature(weather)
displayWind(weather)
displaySunriseSunset(weather)
