import logging
import json
import os
from pathlib import Path


def save_json_to_file(data, path: str):
    _path = Path(path)
    if _path.suffix.lower() != '.json':
        raise ValueError('Please provide a file with a \'.json\' suffix')
    logging.info(f"Saving JSON to file {path}")
    _path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def read_json_file(path):
    logging.info(f'Reading the following JSON file {path}')
    with open(path, 'r') as f:
        res = json.load(f)
    return res


def _is_json_suffix(path: str) -> bool:
    return Path(path).suffix.lower() == '.json'


def get_files_of_path(path):
    dirpath, _, filenames = next(os.walk(path))
    return [os.path.join(dirpath, f) for f in filenames]