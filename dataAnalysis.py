import pandas as pd
import matplotlib.pyplot as plt

dfStreamingHistory0 = pd.read_json("data/StreamingHistory0.json")
dfStreamingHistory1 = pd.read_json("data/StreamingHistory1.json")
dfStreamingHistory = pd.concat([dfStreamingHistory0, dfStreamingHistory1])

dfStreamingHistory["msPlayed"] = dfStreamingHistory["msPlayed"].apply(lambda x: x/60000)
dfStreamingHistory = dfStreamingHistory.rename(columns={'msPlayed': 'minPlayed'})

print(dfStreamingHistory.head())
print(dfStreamingHistory.info())

# ARTIST GRAPH

totalArtist = dfStreamingHistory[["artistName", "minPlayed"]].groupby("artistName", as_index=False).sum()
totalArtist = totalArtist.sort_values("minPlayed", ignore_index=True, ascending=False)
print(totalArtist.head())

plt.bar(totalArtist["artistName"].iloc[:20], totalArtist["minPlayed"].iloc[:20])
plt.xticks(rotation = 45, ha="right")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.235)
plt.title("Top 20 Artists 2022")
plt.ylabel("Listening Time (minutes)")
plt.show()

# SONG GRAPH

totalSong = dfStreamingHistory[["trackName", "minPlayed"]].groupby("trackName", as_index=False).sum()
totalSong = totalSong.sort_values("minPlayed", ignore_index=True, ascending=False)
print(totalSong.head())

plt.bar(totalSong["trackName"].iloc[:20], totalSong["minPlayed"].iloc[:20])
plt.xticks(rotation = 45, ha="right")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.235)
plt.title("Top 20 Songs 2022")
plt.ylabel("Listening Time (minutes)")
plt.show()