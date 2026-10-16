import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("LASTFM_API_KEY")

URL = "https://ws.audioscrobbler.com/2.0/"

params = {
    "method": "artist.gettoptags",
    "artist": "Radiohead",
    "api_key": API_KEY,
    "format": "json",
}

response = requests.get(URL, params=params)
data = response.json()

tags = data["toptags"]["tag"]

for tag in tags[:10]:
    print(tag["name"], tag["count"])