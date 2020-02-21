import json
import os
import sys
from datetime import datetime
from requests_oauthlib import OAuth1Session
from func import *

if __name__ == '__main__':
    API_KEY = os.environ["API_KEY"]
    CHANNEL_ID = os.environ["CHANNEL_ID"]
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_KEY_SECRET = os.environ["CONSUMER_KEY_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
    TWEET_ENDPOINT = "https://api.twitter.com/1.1/statuses/update.json"

    twitter = OAuth1Session(CONSUMER_KEY, 
                                               CONSUMER_KEY_SECRET,
                                               ACCESS_TOKEN,
                                               ACCESS_TOKEN_SECRET)

    uploads_list_id = GetYoutubeChannelUploads(CHANNEL_ID, API_KEY)
    uploads = GetYoutubePlaylistContents(uploads_list_id, API_KEY)

    tweet = ""
    with open("./last.json", mode="r") as f:
        save_file = json.load(f)
        if save_file["last_upload"] != str(uploads[0]["title"]):
            save_file["last_upload"] = str(uploads[0]["title"])
            tweet = "じょえちゃんねるに動画がアップロードされました！\n"
            tweet += str(uploads[0]["title"]) + "\n"
            tweet += "https://www.youtube.com/watch?v=" + str(uploads[0]["Id"])
    
    with open("./last.json", mode="w") as f:
        json.dump(save_file, f)

    if tweet !=  "" :
        res = twitter.post(TWEET_ENDPOINT, params={"status" : tweet})
        print("new")
        if res.status_code != 200 : 
            print("tweet Failed" + str(res.status_code))
        else :
            print("Success")