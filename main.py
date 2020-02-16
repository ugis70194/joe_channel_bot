import json
import os
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

    channels_details = YoutubeChannelDetails(CHANNEL_ID, API_KEY)

    snippet = channels_details["snippet"]
    statistics = channels_details["statistics"]
    content_details = channels_details["contentDetails"]

    tweet = "じょえチャンネルの現在のチャンネル登録者数は"
    tweet += str(GetSubscriberCount(statistics))
    tweet += "人です笑"

    res = twitter.post(TWEET_ENDPOINT, params={"status" : tweet})

    if res.status_code != 200 : 
        print("tweet Failed" + str(res.status_code))
    else :
        print("Success")
