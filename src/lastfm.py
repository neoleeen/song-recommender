import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("LASTFM_API_KEY")
URL = "https://ws.audioscrobbler.com/2.0/"


def call_lastfm(method, **extra):
    params = {"method": method, "api_key": API_KEY, "format": "json"}
    params.update(extra)
    response = requests.get(URL, params=params, timeout=10)
    time.sleep(0.25)
    return response.json()