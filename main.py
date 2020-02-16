import os
from func import *

API_KEY = os.environ["API_KEY"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

if __name__ == '__main__':
    channels_details = YoutubeChannelDetails(CHANNEL_ID, API_KEY)

    snippet = channels_details["snippet"]
    statistics = channels_details["statistics"]
    content_details = channels_details["contentDetails"]

    print(GetViewCount(statistics))
    print(GetSubscriberCount(statistics))
    print(GetVideoCount(statistics))
