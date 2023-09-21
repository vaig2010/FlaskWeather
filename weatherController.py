import requests
from api_key import key

def getCityWeather(city):
    api_url = "http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no"
    r = requests.get(api_url.format(key, city)).json()
    if "error" in r:
        return None
    weather = {
        'city' : city,
        'temperature' : r["current"]["temp_c"],
        'description' : r["current"]["condition"]["text"],
        'icon' : r["current"]["condition"]["icon"]
    }
    return weather
