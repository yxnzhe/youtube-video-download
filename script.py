from pytube import YouTube

# To Do
MP4_SAVE_PATH = 'C:/'
MP3_SAVE_PATH = 'C:/'

with open('download.txt', 'r') as f:
    for line in f:
        yt = YouTube(line)
        try: # Download YouTube video as MP4 and save it inside the MP4 Folder
            yt = YouTube(line)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(MP4_SAVE_PATH)
        except Exception as e:
            print('MP4 Error: ' + e)

        try: # Download YouTube video as MP3 and save it inside the MP3 Folder
            yt.streams.filter(only_audio=True).first().download(MP3_SAVE_PATH)
        except Exception as e:
            print('MP3 Error: ' + e)
