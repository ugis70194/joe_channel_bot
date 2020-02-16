from apiclient.discovery import build

API_SERVICE_NAME = os.environ["API_SERVICE_NAME"]
API_VERSION = os.environ["API_VERSION"]

def YoutubeChannelDetails(id_, API_KEY):
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
    serch_response = youtube.channels().list(part="statistics,snippet,contentDetails",id=id_).execute()
    return serch_response["items"][0]

def GetViewCount(statistics):
    return statistics["viewCount"]

def GetSubscriberCount(statistics):
    return statistics["subscriberCount"]

def GetVideoCount(statistics):
    return statistics["videoCount"]

