import json


class ConfigReader(object):
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.settings = json.load(f)
            self.google_api_key = self.settings['google-api-key']
            self.youtube_channel = self.settings['youtube-channel']
            self.channel_output_path = self.settings['channel-output-path']
            self.videos_output_path = self.settings['videos-output-path']
