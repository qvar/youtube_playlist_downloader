from pytube import Playlist, YouTube
import concurrent.futures
import sys
import os

def download(vid):
	try:
		yt = YouTube(vid)
		print ("downloading... ", yt.title)
		yt.streams.get_by_itag(22).download(dir_path)
		#print(' downloaded   '+vid)

	except Exception as e:
		print (" Skipping... ",vid)
    

arg_list = sys.argv
url = arg_list[2]
dir_path = arg_list[1]
playlist = Playlist(url)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
counter = 0

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, playlist)

print ("\n\nFinished !!\n\n")
'''
for vid in playlist:
    #try:
    yt = YouTube(vid)
    print ("downloading... ", yt.title)
    yt.streams.get_by_itag(22).download(dir_path)
    print(counter, ' downloaded   '+vid)
    #except Exception as e:
        #print (e)
        #print (counter, " Skipping    ",vid)
    counter = counter + 1
    break

if not os.path.exists(dir_path):
    os.mkdir(dir_path)
os.chdir(dir_path)
#playlist.download_all()
'''
