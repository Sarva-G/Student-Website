import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    resp = requests.get(BASE_URL + END_POINT, data=json.dumps(data))
    print('Status Code:', resp.status_code)
    print(resp.json())


get_resource(1)

# ----------------------------------------------------------------------------------------------------------------------

def create_resource():
    data = {
        's_name': 'Dhanush',
        's_class': 9,
        's_city': 'California',
        's_lover': 'Ayishvarya Rajni'
    }
    resp = requests.post(BASE_URL + END_POINT, data=json.dumps(data))
    print('Status Code:', resp.status_code)
    print(resp.json())


# create_resource()

# ----------------------------------------------------------------------------------------------------------------------

def update_resource(id):
    data = {
        'id': id,
        's_class': 11
    }
    resp = requests.put(BASE_URL + END_POINT, data=json.dumps(data))
    print('Status Code:', resp.status_code)
    print(resp.json())


# update_resource(1)

# ----------------------------------------------------------------------------------------------------------------------

def delete_resource(id):
    data = {
        'id': id
    }
    resp = requests.delete(BASE_URL + END_POINT, data=json.dumps(data))
    print('Status Code:', resp.status_code)
    print(resp.json())


delete_resource(9)

# ----------------------------------------------------------------------------------------------------------------------
