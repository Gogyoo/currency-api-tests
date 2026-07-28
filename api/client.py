import os
import requests
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")

baseURL = "https://openexchangerates.org/api/"
params = {"app_id": APP_ID}

def happy_path():
    """First we want to test if our token works, we get a code 200,
    and a few other checks that makes sense for our happy path.
    The /latest.json endpoint is the simplest one to start with."""

    happy_response = requests.get(f"{baseURL}latest.json", params=params)
    latest_json = happy_response.json()

    assert happy_response.status_code == 200
    assert happy_response.elapsed.total_seconds() < 1

happy_path()