import recipes_parser.utils.file_ops as fops
import itertools
import re
import logging
import subprocess
import json


class IngredientsParser(object):
    def __init__(self,
                 videos_path,
                 ingredients_section_path,
                 container_name,
                 crf_model_path,
                 predicted_ingredients_path,
                 store_results=fops.save_json_to_file):
        self.videos_path = videos_path
        self.ingredients_sections_path = ingredients_section_path
        self.store_results = store_results
        self.container_name = container_name
        self.crf_model_path = crf_model_path
        self.predicted_ingredients_path = predicted_ingredients_path

    def run(self):
        videos = self.read_videos()
        videos_with_ingredients = [self.extract_ingredients_section(video) for video in videos]
        self.store_results(videos_with_ingredients, self.ingredients_sections_path)
        predicted = [self.predict_ingredients(video) for video in videos_with_ingredients if video['ingredients']]
        self.store_results(predicted, self.predicted_ingredients_path)

    def read_videos(self):
        paths = fops.get_files_of_path(self.videos_path)
        extracted_videos = [self.extract_simplified_videos(fops.read_json_file(path)) for path in paths]
        flattened = list(itertools.chain(*extracted_videos))
        return flattened

    def extract_ingredients_section(self, video):
        logging.info(f"Parsing description of: {video['id']}")
        return {
            'id': video['id'],
            'title': video['title'],
            'ingredients': self.extract_ingredients_section_from_text(video['description'])
        }

    def extract_simplified_videos(self, videos):
        return [
            {
                'id': video['id'],
                'title': video['snippet']['title'],
                'description': video['snippet']['description']
            } for video in videos['items']
            if 'id' in video
        ]

    def extract_ingredients_section_from_text(self, text):
        prefix = 'ingredients:'
        suffix = 'directions:'
        lower_case_text = text.lower()
        sections = lower_case_text.split(prefix)[1:]
        results = [section.split(suffix)[0] for section in sections]
        return results

    def predict_ingredients(self, video):
        logging.info(f"Predicting ingredients of video: {video}")

        predicted_video = {
            'id': video['id'],
            'title': video['title'],
            'ingredients': video['ingredients']
        }

        predicted_ingredients = []
        for section in video['ingredients']:
            echo_command = f'echo "{section}" | bin/parse-ingredients.py --model-file {self.crf_model_path}'
            try:
                output = subprocess.check_output(
                    ['docker', 'exec', self.container_name, '/bin/bash', '-c', echo_command]).decode('utf8')
                predicted_ingredients.append(json.loads(output))
            except subprocess.CalledProcessError:
                predicted_video['predicted_ingredients'] = None

        predicted_video['predicted_ingredients'] = predicted_ingredients

        return predicted_video
