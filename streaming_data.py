import requests
import json
import os
from dotenv import load_dotenv

#loading data from .env
load_dotenv()
api_key = os.getenv("API_KEY")

api = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q=Casablanca'

def get_data(api_key):
    try:
        res = requests.get(api_key)
        data = res.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def stream_data():
    data = get_data(api)
    print(json.dumps(data, indent=4))


    
stream_data()
