from pytube import Playlist
import sys
import os

#pl = Playlist( "https://youtube.com/playlist?list=PL64E6BD94546734D8")
pl = Playlist(sys.argv[1])
print("audio only mode")
for video in pl.videos:
    video.streams.get_audio_only().download()
    print("done")

os.system("bash convert.sh")
