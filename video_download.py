import youtube_dl
import pandas as pd
import time
import os

def download(youtube_url):
    ydl_opts = {
        'format': '160',
        'outtmpl': 'videos/%(id)s.%(ext)s'
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

df = pd.read_csv("train.csv")

if not os.path.exists("videos"):
  os.mkdir("videos")

error_url_list = []

for i in range(df.shape[0]):
  if i%300 == 0:
    time.sleep(30)

  try:
    download(df.loc[i,"URL"])
  
  except Exception as e:
    print("Exception: ", e)
    error_url_list.append(df.loc[i,"URL"])
    continue

if len(error_url_list) > 0:
  print(">>>List below shows the URL of missing videos:")
  for url in error_url_list:
    print(url)