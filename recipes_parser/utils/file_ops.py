import logging
import json
import os


def save_json_to_file(data, filename):
    logging.info(f"Saving JSON to file {filename}")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def read_json_file(path):
    logging.info(f'Reading the following JSON file {path}')
    with open(path, 'r') as f:
        res = json.load(f)
    return res


def get_files_of_path(path):
    dirpath, _, filenames = next(os.walk(path))
    return [os.path.join(dirpath, f) for f in filenames]