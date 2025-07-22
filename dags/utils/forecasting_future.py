import requests
import json
import os
from dotenv import load_dotenv

#loading data from .env
load_dotenv()
api_key = os.getenv("API_KEY")

def get_api_url(city,number_of_days):
    return f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={number_of_days}'


def get_data(api_key):
    print("Fetching data from API...")
    try:
        res = requests.get(api_key)
        data = res.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def stream_data(city,number_of_days):
    api = get_api_url(city,number_of_days)
    data = get_data(api)
    return data



# forecast = stream_data("Rabat")["forecast"]["forecastday"]

# for day in forecast:
#     date = day["date"]
#     print(f"📅 Date: {date}")
#     for hour in day["hour"]:
#         time = hour["time"]
#         temp = hour["temp_c"]
#         condition = hour["condition"]["text"]
#         print(f"  🕒 {time} | 🌡️ {temp}°C | ☁️ {condition}")
# print(stream_data("Oujda",1))