import json


def is_json(data):
    try:
        provided_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
