import logging
from recipes_parser.utils.config_reader import ConfigReader
from recipes_parser.downloader.youtube_description_downloader import YoutubeDownloader

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    settings_path = '../settings.json'

    logging.info(f"Reading the following settings file {settings_path}")
    config_parer = ConfigReader(settings_path)
    youtube_downloader = YoutubeDownloader(
        config_parer.google_api_key,
        config_parer.channel_output_path,
        config_parer.videos_output_path
    )
    youtube_downloader.prepare_channel_results(config_parer.youtube_channel)
    youtube_downloader.prepare_video_results()
