from datetime import datetime


def displayTemperature(parsedWeather):
    temp = parsedWeather["main"]["temp"]
    celcius = temp - 273.15
    print("temp is", celcius)


def displayWind(parsedWeather):
    wind = parsedWeather["wind"]["speed"]
    if "gust" in parsedWeather["wind"]:
        gust = parsedWeather["wind"]["gust"]
        display_wind = str.format("wind speed is {} and the gust is {}", wind, gust)
    else:
        display_wind = str.format("wind speed is {}", wind)

    print(display_wind)


def displaySunriseSunset(parsedWeather):
    sunrise_unix = parsedWeather["sys"]["sunrise"]
    sunrise = datetime.utcfromtimestamp(sunrise_unix).strftime('%H:%M:%S')
    sunset_unix = parsedWeather["sys"]["sunset"]
    sunset = datetime.utcfromtimestamp(sunset_unix).strftime('%H:%M:%S')
    print(str.format("sun will rise at {} and the sun will set at {}", sunrise, sunset))