from pytube import Playlist
import sys
#pl =Playlist( "https://youtube.com/playlist?list=PLv7CYwdBx8hPrXS3YX6r5kefrxhTwiLJZ4")


pl = Playlist(sys.argv[1])

print('Number of videos in playlist: %s' % len(pl.video_urls))
for video in pl.videos:
    error=True
    while error:
        try:
            print(video.title)
            video.streams.get_highest_resolution().download()
            print("Downloaded with no errors") 
            error=False
        except:
            print("error occured. Downloading  again.")
            error=True

    print("done")
