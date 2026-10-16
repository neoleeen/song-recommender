from lastfm import call_lastfm

data = call_lastfm("tag.gettoptracks", tag="jazz", limit=5)
tracks = data["tracks"]["track"]

for t in tracks:
    print(t["artist"]["name"], "-", t["name"])