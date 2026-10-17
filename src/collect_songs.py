import pandas as pd
from lastfm import call_lastfm

genres = [
    "rock", "pop", "hip-hop", "rnb", "jazz", "electronic",
    "indie", "metal", "country", "folk", "classical", "reggae",
    "blues", "soul", "punk", "house", "techno", "k-pop",
    "j-pop", "latin", "funk", "disco", "ambient", "alternative",
    "indie pop", "dream pop", "synthpop", "trap",
    "drum and bass", "lo-fi",
]

rows = []

for genre in genres:
    data = call_lastfm("tag.gettoptracks", tag=genre, limit=50)
    tracks = data.get("tracks", {}).get("track", [])

    for t in tracks:
        rows.append({
            "artist": t["artist"]["name"],
            "track": t["name"],
            "found_under": genre,
        })

    print(genre, ":", len(tracks), "songs")

df = pd.DataFrame(rows)
df = df.drop_duplicates(subset=["artist", "track"])

df.to_csv("data/songs.csv", index=False)

print()
print("Total unique songs:", len(df))
print(df.head())