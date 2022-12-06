# BetterWrapped
Spotify Wrapped for data nerds

## How to Run
(assumes you already have Python installed)
1. Clone the repository
2. Download your Spotify data: https://www.spotify.com/us/account/privacy/
	1. Extract the zip file
	2. Open the folder with the .json files
	3. Copy all the files
3. Navigate to the folder that contains the repository
4. Create a folder called "data"
5. Paste your files
6. Modify the data analysis file to include all your StreamingHistory files
	1. Open dataAnalysis.py in a text editor
	2. Copy the `dfStreamingHistory1 = pd.read_json("data/StreamingHistory1.json")` line as many times as needed, updating the numbers to match your StreamingHistory files
	3. Add the new dfStreamingHistory# variables to the `dfStreamingHistory = pd.concat([dfStreamingHistory0, dfStreamingHistory1])`, separating with commas
7. Set the desired function(s) to run
	1. Add a new non-indented line at the bottom of the file
	2. Add the function(s) with the relevant parameters (see below for details on each function)
8. Open a command prompt window
9. Navigate to the folder that contains the repository
10. If needed, install pandas, matplotlib, datetime, and numpy
	1. `pip install pandas`
	2. `pip install matplotlib`
	3. `pip install datetime`
	4. `pip install numpy`
11. Run the program using `python dataAnalysis.py`
	1. If you have selected multiple graphing functions, you will need to close the popup graph window to view the next graph
	
## Functions

### `artistGraph(count=False)`
Creates a bar graph of the 20 most listened to artists.

If `count` is False (default), y-axis will be minutes listened.
If `count` is True, y-axis will be total number of tracks played.

### `songGraph(count=False)`
Creates a bar graph of the 20 most listened to songs.

If `count` is False (default), y-axis will be minutes listened.
If `count` is True, y-axis will be total number of plays.

### `listeningGraph(count=False)`
Creates a line graph of listening time by day.

If `count` is False (default), y-axis will be minutes listened.
If `count` is True, y-axis will be total number of tracks played.

### `artistListeningGraph(artistName, count=False)`
Creates a line graph of time spent listening to a specified artist (`artistName`) by day.

If `count` is False (default), y-axis will be minutes listened.
If `count` is True, y-axis will be total number of tracks played.

### `songListeningGraph(songName, count=False)`
Creates a line graph of time spent listening to a specified song (`songName`) by day.

If `count` is False (default), y-axis will be minutes listened.
If `count` is True, y-axis will be total number of plays.