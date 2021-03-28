import json


class ConfigReader(object):
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.settings = json.load(f)
            self.google_api_key = self.settings['google-api-key']
            self.youtube_channel = self.settings['youtube-channel']
            self.channel_output_path = self.settings['channel-output-path']
            self.videos_output_path = self.settings['videos-output-path']
            self.ingredients_section_output_path = self.settings['ingredients-section-output-path']
            self.ingredient_parser_container_name = self.settings['ingredient-parser-container-name']
            self.crf_model_path_in_container = self.settings['crf-model-path-in-container']
            self.predicted_ingredients_output_path = self.settings['predicted-ingredients-output-path']
