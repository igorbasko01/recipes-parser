import logging
from recipes_parser.utils.config_reader import ConfigReader
from recipes_parser.downloader.youtube_description_downloader import YoutubeDownloader

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    settings_path = '../settings.json'

    logging.info(f"Reading the following settings file {settings_path}")
    config_parer = ConfigReader(settings_path)
    youtube_downloader = YoutubeDownloader(config_parer.settings['google-api-key'])
    youtube_downloader.fetch_videos_of_channel(config_parer.settings['youtube-channel'])