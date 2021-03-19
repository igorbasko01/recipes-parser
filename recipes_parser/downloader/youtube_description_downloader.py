import logging
import requests
import json
import os


class YoutubeDownloader(object):

    def __init__(self, api_key, channel_output_path, videos_output_path):
        self.api_key = api_key
        self.channel_output_path = channel_output_path
        self.videos_output_path = videos_output_path

    def prepare_video_results(self):
        paths = self.get_channel_files()
        logging.info(f'got the following channel files: {paths}')
        # flatten
        video_ids = [self.extract_video_ids(self.read_response_file(path)) for path in paths]
        logging.info(f'Found {sum([len(chunk) for chunk in video_ids])} video ids: {video_ids}')
        for chunk in video_ids:
            if len(chunk) > 0:
                response = self.get_response_of_videos(chunk)
                self.save_response_to_file(response, os.path.join(self.videos_output_path, f'videos-{chunk[0]}.json'))

    def prepare_channel_results(self, channel_id):
        next_page = None
        while True:
            response, next_page = self.get_response_of_channel(channel_id, next_page)
            self.save_response_to_file(
                response,
                os.path.join(self.channel_output_path, f'response-{channel_id}-{next_page}.json')
            )
            if not next_page:
                break

    def get_response_of_videos(self, video_ids):
        logging.info(f"fetching the following videos details {video_ids}")
        url = f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={",".join(video_ids)}&key={self.api_key}'
        res = requests.get(url)
        response = res.json()
        logging.info(f"Got the following response: {response}")
        return response

    def get_response_of_channel(self, channel_id, next_page=None):
        logging.info(f"fetching videos of the following channel id: {channel_id}")
        url = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&channelId={channel_id}&key={self.api_key}'
        if next_page:
            logging.info(f'Next page is {next_page}')
            url += f'&pageToken={next_page}'
        res = requests.get(url)
        response = res.json()
        logging.info(f"Got the following response: {response}")
        next_page = response['nextPageToken'] if 'nextPageToken' in response else None
        return response, next_page

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
        logging.info(f"Saving response to file {filename}")
        with open(filename, 'w') as f:
            json.dump(response, f, indent=4)

    def get_channel_files(self):
        dirpath, _, filenames = next(os.walk(self.channel_output_path))
        return [os.path.join(dirpath, f) for f in filenames]

    def read_response_file(self, path):
        logging.info(f'Reading the following response file {path}')
        with open(path, 'r') as f:
            res = json.load(f)
        return res
