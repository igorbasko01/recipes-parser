import logging
import requests
import json
import os


class YoutubeDownloader(object):

    def __init__(self, api_key, output_path):
        self.api_key = api_key
        self.output_path = output_path

    def fetch_videos_of_channel(self, channel_id, next_page=None):
        logging.info(f"fetching videos of the following channel id: {channel_id}")
        url = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId={channel_id}&key={self.api_key}'
        if next_page:
            logging.info(f'Next page is {next_page}')
            url += f'&pageToken={next_page}'
        res = requests.get(url)
        response = res.json()
        logging.info(f"Got the following response: {response}")
        self.save_response_to_file(response, f"response-{channel_id}-{next_page}.json")
        self.extract_video_ids(response)
        next_page = response['nextPageToken'] if 'nextPageToken' in response else None
        if next_page:
            self.fetch_videos_of_channel(channel_id, next_page)

    def extract_video_ids(self, response):
        logging.info('Extracting video ids')
        videos = [
            search_result['id']['videoId']
            for search_result in response['items']
            if 'videoId' in search_result['id']
        ]
        logging.info(f"found {len(videos)} videos")
        return videos

    def save_response_to_file(self, response, filename):
        path = os.path.join(self.output_path, filename)
        logging.info(f"Saving response to file {path}")
        with open(path, 'w') as f:
            json.dump(response, f, indent=4)
