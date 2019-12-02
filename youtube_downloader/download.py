
# from pytube import YouTube
# #from pytube import YouTube 
  
# #where to save 
# #SAVE_PATH = "E:/" #to_do 
  
# #link of the video to be downloaded 
# link="https://www.youtube.com/watch?v=VZk9mdVLb5w"
  
# yt = YouTube(link) 
 
# yt = yt.get('mp4','720p')
# yt.download('.')
# print('Task Completed!')

from pytube import YouTube
import os,tqdm

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    with tqdm(total=file_size, unit='B',
              unit_scale=True, unit_divisor=1024,
              desc='government_interest.tsv.zip', initial=initial_pos,
              ascii=True, miniters=1) as pbar:
        for chunk in r.iter_content(32 * 1024):
            f.write(chunk)
            pbar.update(len(chunk))

downloadYouTube('https://www.youtube.com/watch?v=VZk9mdVLb5w', './videos/FindingNemo1')