import matplotlib.pyplot as plt
import json

import requests

from helper import convertKelvinToCelcius

key = "f40998cd5bef60a3b6ed499e39c91a0b"


def getWeatherToday(place):
    address = "https://api.openweathermap.org/data/2.5/weather?q={0},uk&appid=f40998cd5bef60a3b6ed499e39c91a0b"
    print("getting the weather for ", place)
    response = requests.get(address.format(place))
    parsed = json.loads(response.text)
    return parsed

def getWeatherForecast():
    lat = "53.299540"
    lon = "-3.416520"
    exclude = "current,minutely,hourly"
    # address = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s&appid=f40998cd5bef60a3b6ed499e39c91a0b"

    address = "https://api.openweathermap.org/data/2.5/onecall?lat=53.299540&lon=-3.416520&exclude=hourly, minutely, current&appid=f40998cd5bef60a3b6ed499e39c91a0b"
    url = str.format(address, lat, lon, exclude)
    response = requests.get(address)
    parsed = json.loads(response.text)
    return parsed

weather = getWeatherForecast()

temps = []
days = []
dailyList = weather["daily"]
for day in range(0, len(dailyList)):
    temp = convertKelvinToCelcius(dailyList[day]["temp"]["day"])
    temps.append(temp)
    days.append(day)

print(temps)
print(days)
plt.title("My digital weather forecast")
plt.xlabel("days")
plt.ylabel("temps")
plt.plot(days,temps)
plt.show()


