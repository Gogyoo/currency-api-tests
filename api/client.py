import requests

BASEURL = "https://openexchangerates.org/api/"


def get_response(endpoint, **kwargs):
    return requests.get(
        f"{BASEURL}{endpoint}",
        **kwargs
    )