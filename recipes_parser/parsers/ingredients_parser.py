import recipes_parser.utils.file_ops as fops
import itertools
import re
import logging


class IngredientsParser(object):
    def __init__(self, videos_path, ingredients_section_path, store_results=fops.save_json_to_file):
        self.videos_path = videos_path
        self.ingredients_sections_path = ingredients_section_path
        self.store_results = store_results

    def run(self):
        videos = self.read_videos()
        videos_with_ingredients = [self.extract_ingredients_section(video) for video in videos]
        self.store_results(videos_with_ingredients, self.ingredients_sections_path)

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
        p = re.compile(f'{prefix}.*{suffix}', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        regex_result = p.search(text)
        result = None
        if regex_result:
            extracted_string = regex_result.group()
            result = extracted_string[len(prefix):len(extracted_string)-len(suffix)]
        return result
