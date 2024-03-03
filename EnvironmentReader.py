import json


def read_config():
    file_path ="config.json"
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config