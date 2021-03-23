import logging
import json


def save_json_to_file(data, filename):
    logging.info(f"Saving JSON to file {filename}")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def read_json_file(path):
    logging.info(f'Reading the following JSON file {path}')
    with open(path, 'r') as f:
        res = json.load(f)
    return res