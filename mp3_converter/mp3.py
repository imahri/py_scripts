
from pytube import YouTube
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_mp3(yt):
    try:
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print("Done")
    except:
        print("\nNO")
        
    
    
    
yt = YouTube("https://www.youtube.com/watch?v=S3Nif-EyPxk&list=RDMMS3Nif-EyPxk&start_radio=1")
download_mp3(yt)