import requests
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

api_key = os.getenv("api_key")
channel_handle = "MrBeast&key"

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
    
if __name__ == "__main__":
    get_playlist_id()
