import requests

BASEURL = "https://openexchangerates.org/api/"


def get_response(endpoint, **kwargs):
    return requests.get(
        f"{BASEURL}{endpoint}",
        timeout=5,
        **kwargs
    )