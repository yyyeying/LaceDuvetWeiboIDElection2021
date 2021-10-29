import json


def read_json(path: str):
    with open(path, 'rb') as f:
        content = f.read()
        # print(content)
        result_json = json.loads(content)
    return result_json
