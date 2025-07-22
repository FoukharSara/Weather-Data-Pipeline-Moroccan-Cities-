import requests
import json
import os
from dotenv import load_dotenv

#loading data from .env
load_dotenv()
api_key = os.getenv("API_KEY")

def get_api_url(city):
    return f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

# api = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q=Casablanca'

def get_data(api_key):
    print("Fetching data from API...")
    try:
        res = requests.get(api_key)
        data = res.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def stream_data(city):
    api = get_api_url(city)
    data = get_data(api)
    return data


def mock_data():
    mock_data = {
    "location": {
        "name": "Casablanca",
        "region": "",
        "country": "Morocco",
        "lat": 33.5931,
        "lon": -7.6164,
        "tz_id": "Africa/Casablanca",
        "localtime_epoch": 1753093628,
        "localtime": "2025-07-21 11:27"
    },
    "current": {
        "last_updated_epoch": 1753092900,
        "last_updated": "2025-07-21 11:15",
        "temp_c": 24.4,
        "temp_f": 75.9,
        "is_day": 1,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
            "code": 1003
        },
        "wind_mph": 12.5,
        "wind_kph": 20.2,
        "wind_degree": 6,
        "wind_dir": "N",
        "pressure_mb": 1014.0,
        "pressure_in": 29.94,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 65,
        "cloud": 75,
        "feelslike_c": 25.8,
        "feelslike_f": 78.5,
        "windchill_c": 24.4,
        "heatindex_f": 78.5,
        "dewpoint_c": 17.1,
        "dewpoint_f": 62.7,
        "vis_km": 6.0,
        "vis_miles": 3.0,
        "gust_mph": 14.4,
        "gust_kph": 23.2
    }
    }
    return mock_data
    # print(json.dumps(mock_data, indent=4))

