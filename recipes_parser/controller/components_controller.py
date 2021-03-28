import logging
from typing import List

from recipes_parser.downloader.youtube_description_downloader import YoutubeDownloader
from recipes_parser.parsers.ingredients_parser import IngredientsParser


class ComponentsController(object):
    def __init__(self, config, components_to_run: List[str] = None):
        self.default_components_to_run = [YoutubeDownloader.__name__, IngredientsParser.__name__]
        self.config = config
        self.components_to_run = components_to_run if components_to_run else self.default_components_to_run
        self.youtube_downloader, self.ingredients_parser = self._create_components()
        self.execution_order = [self.youtube_downloader, self.ingredients_parser]

    def run(self):
        for component in self.execution_order:
            if type(component).__name__ in self.components_to_run:
                logging.info(f'Running {type(component).__name__} ...')
                component.run()

    def _create_components(self):
        youtube_downloader = YoutubeDownloader(
            self.config.google_api_key,
            self.config.youtube_channel,
            self.config.channel_output_path,
            self.config.videos_output_path
        )

        ingredients_parser = IngredientsParser(
            self.config.videos_output_path,
            self.config.ingredients_section_output_path,
            self.config.ingredient_parser_container_name,
            self.config.crf_model_path_in_container,
            self.config.predicted_ingredients_output_path
        )

        return youtube_downloader, ingredients_parser
