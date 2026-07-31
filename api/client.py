import requests

#import json


baseURL = "https://openexchangerates.org/api/"


def get_response(endpoint, **kwargs):
    return requests.get(
        f"{baseURL}{endpoint}",
        timeout=5,
        **kwargs
    )