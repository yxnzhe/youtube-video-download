from pytube import YouTube
import os
import re
import moviepy.editor as mp

# To Do
MP4_SAVE_PATH = './MP4'
MP3_SAVE_PATH = './MP3'

with open('download.txt', 'r') as f:
    for line in f:
        yt = YouTube(line)
        try: # Download YouTube video as MP4 and save it inside the MP4 Folder
            yt = YouTube(line)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(MP4_SAVE_PATH)
            print(yt.title + " MP4 has been successfully downloaded.")
        except Exception as e:
            print('MP4 Error: ' + e)

        try: # Download YouTube video as MP3 and save it inside the MP3 Folder
            yt.streams.filter(only_audio=True).first().download(MP3_SAVE_PATH)
            for file in os.listdir(MP3_SAVE_PATH):
                if re.search('mp4', file):
                    mp4_path = os.path.join(MP3_SAVE_PATH,file)
                    mp3_path = os.path.join(MP3_SAVE_PATH,os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)
            print(yt.title + " MP3 has been successfully downloaded.")
        except Exception as e:
            print('MP3 Error: ' + e)
