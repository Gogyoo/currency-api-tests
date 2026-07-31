import os

import requests

#import json
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("APP_ID")
inactive_id = os.getenv("INACTIVE_ID")

baseURL = "https://openexchangerates.org/api/"
params = {"app_id": app_id}

def happy_path():
    """Validate the /latest.json endpoint using a valid API key.

    Checks:
    - HTTP status
    - Response time
    - Required JSON fields
    - Exchange rate sanity
    - Currency coverage
    - Sensitive data leakage
    """

    happy_response = requests.get(f"{baseURL}latest.json", timeout=5,params=params)
    latest_json = happy_response.json()

    #print(json.dumps(latest_json, indent=4))
    assert happy_response.status_code == 200
    assert happy_response.elapsed.total_seconds() < 1
    assert isinstance(latest_json, dict)
    assert "timestamp" in latest_json
    assert "rates" in latest_json
    assert "base" in latest_json
    assert "GBP" in latest_json["rates"]
    assert "EUR" in latest_json["rates"]
    assert "JPY" in latest_json["rates"]
    #data validation
    assert 0.4 <= latest_json["rates"]["GBP"] <= 1.2
    assert len(latest_json["rates"]) > 100
    for curr in latest_json["rates"]:
        assert len(curr) == 3
    
    forbidden = ["password",
                    "secret",
                    "token",
                    "api_key"]
    for i in forbidden:
        assert i not in happy_response.text.lower()

def token():
    try:
        depr_token = requests.get(f"{baseURL}latest.json?app_id={inactive_id}", timeout=5)
        depr_token.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    try:
        null_token = requests.get(f"{baseURL}latest.json?app_id=", timeout=5)
        null_token.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def endpoint():
    try:
        fake_endpoint = requests.get(f"{baseURL}ananas.json?app_id={app_id}", timeout=5)
        fake_endpoint.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def subscription():
    # The /ohlc endpoint should only be available to premium members of the API.
    # For this project we only use the free tier.
    try:
        subscr = requests.get(f"{baseURL}ohlc.json?app_id={app_id}", timeout=5)
        subscr.raise_for_status()
        print("Welcome to the VIP Platinum tier!")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def base():
    # Same with changing the base currency rates will be returned at.
    try:
        invalid_base = requests.get(f"{baseURL}latest.json?app_id={app_id}&base=EUR", timeout=5)
        invalid_base.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("This option is only extended to subscribers of the",
        "Developer, Enterprise and Unlimited plans.")
        print(f"Request failed: {e}")

def malformed():
    try:
        mal = requests.get(f"http://openexchangerates.org/latest.json?ap_d={app_id}&", timeout=5)
        mal.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


happy_path()
#TODO: maybe group all try/except blocks in one negative_testing function?
#token()
#endpoint()
#subscription()
#base()
#malformed()