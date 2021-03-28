import logging
from recipes_parser.utils.config_reader import ConfigReader
from recipes_parser.utils.arguments_parser import ArgumentsParser
from recipes_parser.downloader.youtube_description_downloader import YoutubeDownloader
from recipes_parser.parsers.ingredients_parser import IngredientsParser
from recipes_parser.controller.components_controller import ComponentsController

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    args = ArgumentsParser(
        youtube_downloader_name=YoutubeDownloader.__name__,
        ingredients_parser_name=IngredientsParser.__name__
    ).args

    logging.info(f"Reading the following settings file {args.settings_path}")
    config_parser = ConfigReader(args.settings_path)

    controller = ComponentsController(config_parser, args.components)
    controller.run()
