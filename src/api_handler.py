import requests
from datetime import datetime
from config import API_KEY, BASE_URL

def fetch_weather(city="London"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

# Get lat/lon for a given city
def get_coordinates(city):
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }
    res = requests.get(geo_url, params=params).json()
    if not res:
        raise Exception("City not found.")
    return res[0]["lat"], res[0]["lon"]

# Historical weather (max 5 days ago allowed)
def fetch_historical_weather(city, date):
    lat, lon = get_coordinates(city)

    # Convert date to Unix timestamp
    dt = int(datetime(date.year, date.month, date.day, 12, 0).timestamp())

    url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
    params = {
        "lat": lat,
        "lon": lon,
        "dt": dt,
        "appid": API_KEY,
        "units": "metric"
    }

    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()

    # Emulate structure like current weather API
    weather_data = {
        "name": city,
        "main": data["data"][0]["main"] if "main" in data["data"][0] else {
            "temp": data["data"][0]["temp"],
            "humidity": data["data"][0]["humidity"],
            "pressure": data["data"][0]["pressure"]
        },
        "wind": {
            "speed": data["data"][0]["wind_speed"]
        }
    }
    return weather_data
