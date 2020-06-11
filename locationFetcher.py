import json

import requests

key = "405a8801ad93426b971dadde4fd65872"

url = "https://api.opencagedata.com/geocode/v1/json?q={0}&key=405a8801ad93426b971dadde4fd65872"

def getLocation(place):
    location = url.format(place)
    response = requests.get(location)
    parsed = json.loads(response.text)
    return parsed["results"][0]["geometry"]
