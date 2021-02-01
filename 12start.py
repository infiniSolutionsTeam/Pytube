from datetime import datetime, time, timedelta
import sys
import pytube


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time



def yt(url):
    
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(video.title)
    print("start downloading")
    video.download()
    print("downloaded")


    
def download():
    for x in sys.argv[1:]:
        yt(x)


# Original test case from OP
a=is_time_between(time(18,30), time(2,30))  #sri Lanka
print(datetime.utcnow().time())
print(a)


print("waiting for 00:00:00")
while 1:
    if a:  #remove not
        print("Time is  00:00:00")
        download()
        break


