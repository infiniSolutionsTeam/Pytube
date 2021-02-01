import pytube
import subprocess
import os 
import sys 
# url = 'https://www.youtube.com/watch?v=GqD7_h6Hwl4'
url = sys.argv[1]


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()



prevprog=0 
def progress_function(stream, chunk, bytes_remaining):
    global prevprog
    tot=stream.filesize
    downloaded=tot-bytes_remaining
    liveprog=(int)(downloaded /tot *100)
    if liveprog > prevprog:
        prevprog=liveprog
        # print(str(liveprog)+" % Completed") 
        printProgressBar(liveprog, 100, prefix = 'Progress:', suffix = 'Complete', length = 50)



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




