import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dts
from datetime import datetime, timedelta
import numpy as np

dfStreamingHistory0 = pd.read_json("data/StreamingHistory0.json")
dfStreamingHistory1 = pd.read_json("data/StreamingHistory1.json")
dfStreamingHistory = pd.concat([dfStreamingHistory0, dfStreamingHistory1])

dfStreamingHistory["minPlayed"] = dfStreamingHistory["msPlayed"].apply(lambda x: x/60000)
dfStreamingHistory["timesPlayed"]=dfStreamingHistory["msPlayed"].apply(lambda x: 1 if x > 9000 else 0)

dfStreamingHistory["streamDate"] = dfStreamingHistory["endTime"].apply(lambda x: datetime.strptime(x[:10], "%Y-%m-%d"))

print(dfStreamingHistory.head())
print(dfStreamingHistory.info())

def defaultGraphSettings(title="", ylabel="", xlabel="", xticks=None):
	if not (xticks is None):
		plt.xticks(xticks, rotation = 45, ha="right")
	else:
		plt.xticks(rotation = 45, ha="right")
	plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.235)
	plt.grid(alpha=0.5)
	plt.title(title)
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.gca().get_lines()[len(plt.gca().get_lines())-1].set_color('darkslateblue')
	plt.show()

# ARTIST GRAPH
def artistGraph(count=False):
	yVar = "timesPlayed" if count else "minPlayed"
	totalArtist = dfStreamingHistory[["artistName", yVar]].groupby("artistName", as_index=False).sum()
	totalArtist = totalArtist.sort_values(playVar, ignore_index=True, ascending=False)
	print(totalArtist.head(20))
	totalArtist = totalArtist[totalArtist[yVar] != 0]

	plt.bar(totalArtist["artistName"].iloc[:20], totalArtist[yVar].iloc[:20])
	defaultGraphSettings(title="Top 20 Artists 2022", ylabel="Number of Plays" if count else "Listening Time (minutes)")

# SONG GRAPH
def songGraph(count=False):
	yVar = "timesPlayed" if count else "minPlayed"
	totalSong = dfStreamingHistory[["trackName", yVar]].groupby("trackName", as_index=False).sum()
	totalSong = totalSong.sort_values(yVar, ignore_index=True, ascending=False)
	print(totalSong.head(20))
	totalSong = totalSong[totalSong[yVar] != 0]

	plt.bar(totalSong["trackName"].iloc[:20], totalSong[yVar].iloc[:20])
	defaultGraphSettings(title="Top 20 Songs 2022", ylabel="Number of Plays" if count else "Listening Time (minutes)")

# LISTENING GRAPH
def listeningGraph(count=False):
	yVar = "timesPlayed" if count else "minPlayed"
	streamsByDate = dfStreamingHistory[["streamDate", yVar]].groupby("streamDate", as_index=False).sum()
	print(streamsByDate.head())
	print(streamsByDate.info())
	streamsByDate = streamsByDate[streamsByDate[yVar] != 0]
	
	plt.plot(streamsByDate["streamDate"], streamsByDate[yVar], marker='.')
	defaultGraphSettings(title="Listening 2022", ylabel="Number of Plays" if count else "Listening Time (minutes)", xlabel="Date", xticks=np.append(dts.drange(streamsByDate["streamDate"].min(), streamsByDate["streamDate"].max(), timedelta(weeks=4)), dts.date2num(streamsByDate["streamDate"].max())))
	
# ARTIST LISTENING GRAPH
def artistListeningGraph(artistName, count=False):
	yVar = "timesPlayed" if count else "minPlayed"
	streamsByDate = dfStreamingHistory.loc[dfStreamingHistory["artistName"]==artistName][["streamDate", yVar]].groupby("streamDate", as_index=False).sum()
	streamsByDate = streamsByDate[streamsByDate[yVar] != 0]
	
	plt.plot(streamsByDate["streamDate"], streamsByDate[yVar], marker='.')
	defaultGraphSettings(title="Time Spent Listening to "+artistName, ylabel="Number of Plays" if count else "Listening Time (minutes)", xlabel="Date", xticks=np.append(dts.drange(streamsByDate["streamDate"].min(), streamsByDate["streamDate"].max(), timedelta(weeks=4)), dts.date2num(streamsByDate["streamDate"].max())))
	
	
# SONG LISTENING GRAPH
def songListeningGraph(songName, count=False):
	yVar = "timesPlayed" if count else "minPlayed"
	streamsByDate = dfStreamingHistory.loc[dfStreamingHistory["trackName"]==songName][["streamDate", yVar]].groupby("streamDate", as_index=False).sum()
	streamsByDate = streamsByDate[streamsByDate[yVar] != 0]
	
	plt.plot(streamsByDate["streamDate"], streamsByDate[yVar], marker='.')
	defaultGraphSettings(title="Time Spent Listening to "+songName, ylabel="Number of Plays" if count else "Listening Time (minutes)", xlabel="Date", xticks=np.append(dts.drange(streamsByDate["streamDate"].min(), streamsByDate["streamDate"].max(), timedelta(weeks=4)), dts.date2num(streamsByDate["streamDate"].max())))
