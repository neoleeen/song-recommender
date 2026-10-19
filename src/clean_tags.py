import pandas as pd

df = pd.read_csv("data/song_tags.csv")
print("Rows before cleaning:", len(df))

merge = {
    "hip hop": "hip-hop",
    "r&b": "rnb",
    "lo fi": "lo-fi",
}

junk = {
    "american", "british", "love", "beautiful",
    "love at first listen", "sexy", "seen live",
    "favorites", "favourites", "favorite", "awesome",
}

df["tag"] = df["tag"].replace(merge)
df = df[~df["tag"].isin(junk)]

df = df.groupby(["artist", "track", "tag", "source"], as_index=False)["count"].max()

counts = df["tag"].value_counts()
keep = counts[counts >= 3].index
df = df[df["tag"].isin(keep)]

print("Rows after cleaning:", len(df))
print("Unique tags left:", df["tag"].nunique())

tags_per_song = df.groupby(["artist", "track"]).size()
print("Songs left:", len(tags_per_song))
print("Songs with fewer than 3 tags:", (tags_per_song < 3).sum())

df.to_csv("data/song_tags_clean.csv", index=False)