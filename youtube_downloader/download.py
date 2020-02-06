from pytube import YouTube
import pytube
print("Paste the url of youtube videos")
video = YouTube(str(input()))
print(video.title)
youtube = pytube.YouTube(video)
video = youtube.streams.first()
video.download('/')
print("Successfully downloaded the video")