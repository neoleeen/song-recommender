import pandas as pd

df = pd.read_csv("data/song_tags.csv")
print("Rows:", len(df))
print("Unique tags:", df["tag"].nunique())

counts = df["tag"].value_counts()
print()
print(counts.head(50))

print()
print("Tags used by fewer than 3 songs:", (counts < 3).sum())