import json


class ConfigReader(object):
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.settings = json.load(f)
