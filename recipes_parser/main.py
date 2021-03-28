import logging
from recipes_parser.utils.config_reader import ConfigReader
from recipes_parser.downloader.youtube_description_downloader import YoutubeDownloader
from recipes_parser.parsers.ingredients_parser import IngredientsParser

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    settings_path = '../settings.json'

    logging.info(f"Reading the following settings file {settings_path}")
    config_parser = ConfigReader(settings_path)

    youtube_downloader = YoutubeDownloader(
        config_parser.google_api_key,
        config_parser.channel_output_path,
        config_parser.videos_output_path
    )
    youtube_downloader.prepare_channel_results(config_parser.youtube_channel)
    youtube_downloader.prepare_video_results()

    ingredients_parser = IngredientsParser(
        config_parser.videos_output_path,
        config_parser.ingredients_section_output_path,
        config_parser.ingredient_parser_container_name,
        config_parser.crf_model_path_in_container,
        config_parser.predicted_ingredients_output_path
    )
    ingredients_parser.run()
