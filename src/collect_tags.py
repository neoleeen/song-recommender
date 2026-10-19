import pandas as pd
from lastfm import call_lastfm

songs = pd.read_csv("data/songs.csv")
print("Songs to process:", len(songs))

def get_tags(method, **extra):
    data = call_lastfm(method, **extra)
    tags = data.get("toptags", {}).get("tag", [])

    if isinstance(tags, dict):
        tags = [tags]

    cleaned = []
    for t in tags:
        cleaned.append((t["name"].lower(), int(t["count"])))
    return cleaned

artist_cache = {}
rows = []

for i, row in songs.iterrows():
    artist = row["artist"]
    track = row["track"]

    try:
        tags = get_tags("track.gettoptags", artist=artist, track=track, autocorrect=1)
        source = "song"

        if len(tags) < 5:
            if artist not in artist_cache:
                artist_cache[artist] = get_tags("artist.gettoptags", artist=artist, autocorrect=1)
            tags = artist_cache[artist]
            source = "artist"

        for name, count in tags[:15]:
            rows.append({
                "artist": artist,
                "track": track,
                "tag": name,
                "count": count,
                "source": source,
            })
    except Exception as e:
        print("Skipped", artist, "-", track, ":", e)

    if i % 50 == 0:
        print(i, "of", len(songs), "done")


df = pd.DataFrame(rows)
df.to_csv("data/song_tags.csv", index=False)

per_song = df.drop_duplicates(subset=["artist", "track"])
print()
print("Songs with tags:", len(per_song))
print(per_song["source"].value_counts())
print(df.head(10))