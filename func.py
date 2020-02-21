import os
from apiclient.discovery import build

API_SERVICE_NAME = os.environ["API_SERVICE_NAME"]
API_VERSION = os.environ["API_VERSION"]

def GetYoutubeChannelStatistics(id_, API_KEY):
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    serch_response = youtube.channels().list(part="statistics",id=id_).execute()
    return serch_response["items"][0]["statistics"]

def GetYoutubeChannelUploads(id_, API_KEY):
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    serch_response = youtube.channels().list(part="contentDetails",id=id_).execute()
    return serch_response["items"][0]["contentDetails"]['relatedPlaylists']['uploads']

def GetYoutubePlaylistContents(id_, API_KEY):
    res = []
    nextPageToken = "start"
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    serch_response = youtube.playlistItems().list(part="snippet",playlistId=id_,maxResults = 1).execute()
    res.extend(serch_response["items"])

    videos = [{"title" : video["snippet"]["title"], "Id" : video["snippet"]["resourceId"]["videoId"]} for video in res]

    return videos

def GetViewCount(statistics):
    return statistics["viewCount"]

def GetSubscriberCount(statistics):
    return statistics["subscriberCount"]

def GetVideoCount(statistics):
    return statistics["videoCount"]

def GetUploadedVideos(content_details):
    return content_details["relatedPlaylists"]["uploads"]

