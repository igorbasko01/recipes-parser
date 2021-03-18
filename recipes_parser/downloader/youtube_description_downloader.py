import logging
import requests


class YoutubeDownloader(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_videos_of_channel(self, channel_id):
        logging.info(f"fetching videos of the following channel id: {channel_id}")
        res = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId={channel_id}&key={self.api_key}')
        logging.info(f"Got the following reponse: {res.json()}")

    def extract_video_ids(self, response):
        logging.info(f"Going to extract video ids from the following response: {response}")
        videos = [search_result['id']['videoId'] for search_result in response['items']]
        logging.info(f"found {len(videos)} videos")
        return videos
