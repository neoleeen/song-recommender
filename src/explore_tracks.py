import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("LASTFM_API_KEY")
URL = "https://ws.audioscrobbler.com/2.0/"

songs = [
    ("iKON", "Love Scenario"),
    ("Drake", "Janice STFU"),
    ("aespa", "Drama"),
    ("Daft Punk", "One More Time"),
]

for artist, track in songs:
    params = {
        "method": "track.gettoptags",
        "artist": artist,
        "track": track,
        "autocorrect": 1,
        "api_key": API_KEY,
        "format": "json",
    }
    response = requests.get(URL, params=params)
    data = response.json()
    tags = data.get("toptags", {}).get("tag", [])
    source = "song"

    if len(tags) < 5:
        artist_params = {
            "method": "artist.gettoptags",
            "artist": artist,
            "api_key": API_KEY,
            "format": "json",
        }
        artist_response = requests.get(URL, params=artist_params)
        tags = artist_response.json().get("toptags", {}).get("tag", [])
        source = "artist"

    print(artist, "-", track, ":", len(tags), "tags from", source)
    for tag in tags[:5]:
        print("   ", tag["name"], tag["count"])