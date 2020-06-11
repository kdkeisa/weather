import json
import os

import requests

url = "https://api.opencagedata.com/geocode/v1/json?q={0}&key={1}"

def getLocation(place):
    location = url.format(place, os.getenv('LOCATION_KEY'))
    response = requests.get(location)
    parsed = json.loads(response.text)
    return parsed["results"][0]["geometry"]
