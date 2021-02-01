import pytube
import subprocess
import os 
import sys 
#url = 'https://youtu.be/LXb3EKWsInQ'
url = sys.argv[1]

prevprog=0 
def progress_function(stream, chunk, bytes_remaining):
    global prevprog
    tot=stream.filesize
    downloaded=tot-bytes_remaining
    liveprog=(int)(downloaded /tot *100)
    if liveprog > prevprog:
        prevprog=liveprog
        print(str(liveprog)+" % Completed") 


youtube = pytube.YouTube(url,on_progress_callback=progress_function)

#video = youtube.streams.get_by_itag(136)
videos = youtube.streams.filter(progressive=False)
if youtube.streams.get_by_itag(315):
	print("2160p Available")
	video = youtube.streams.get_by_itag(315)
elif youtube.streams.get_by_itag(401):
	print("2160p Available")
	video = youtube.streams.get_by_itag(401)
elif youtube.streams.get_by_itag(308):
	print("1440p Available")
	video = youtube.streams.get_by_itag(308)
elif youtube.streams.get_by_itag(299):
	print("1080p Available")
	video = youtube.streams.get_by_itag(299)
elif youtube.streams.get_by_itag(137):
	print("1080p Available")
	video = youtube.streams.get_by_itag(137)
elif youtube.streams.get_by_itag(298):
	print("720p Available")
	video = youtube.streams.get_by_itag(298)
elif youtube.streams.get_by_itag(136):
	print("720p Available")
	video = youtube.streams.get_by_itag(136)

audio=youtube.streams.get_by_itag(140)

print(video)
print(audio)
print('----------------Start downloading-----------')
print(video.title)
#video.download('/media/sf_PC')

error=True
while error:
    try:

        video.download('video')
        audio.download('audio')
        print("no errors") 
        error=False

    except:
        print("error occured. Downloading  again.")
        error=True

print('----------------Done------------------------')

os.system("bash merge.sh") 




