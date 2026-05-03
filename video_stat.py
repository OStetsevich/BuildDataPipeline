import requests
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

api_key = os.getenv("api_key")
channel_handle = "MrBeast&key"
max_results = 50

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}={api_key}"

def get_playlist_id():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        #print(json.dumps(data, indent=4))
        channel_items = data["items"][0]
        channel_plalists_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print(channel_plalists_id)
        return channel_plalists_id
    except requests.exceptions.RequestException as error:
        raise error
    
def get_playlists_id(play_list_id):
    video_ids = []
    pageToken = None
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={max_results}&playlistId={play_list_id}&key={api_key}"

    try:
        while True:
          
          url = base_url

          if pageToken:
              url +=f"&pageToken={pageToken}"

          response = requests.get(url)
          response.raise_for_status()
          data = response.json()

          for item in data.get("items", []):
              video_id = item["contentDetails"]["videoId"]
              video_ids.append(video_id)

          pageToken = data.get("nextPageToken")

          if not pageToken:
              break
        return video_ids

    except requests.exceptions.RequestException as error:
        raise error

if __name__ == "__main__":
    play_list_id = get_playlist_id()
    get_playlists_id(play_list_id)