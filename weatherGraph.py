import matplotlib.pyplot as plt
from helper import convertKelvinToCelcius
from locationFetcher import getLocation
from weatherFetcher import getWeatherForecast


def graph(placeName):
    latLon = getLocation(placeName)
    weather = getWeatherForecast(latLon["lat"], latLon["lng"])

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
    plt.plot(days, temps)
    plt.show()
