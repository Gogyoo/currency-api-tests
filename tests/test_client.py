import os

import requests.exceptions
from dotenv import load_dotenv

from api.client import get_response

load_dotenv()
app_id = os.getenv("APP_ID")
inactive_id = os.getenv("INACTIVE_ID")
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

    response = get_response("latest.json",params=params)
    latest_json = response.json()

    #print(json.dumps(latest_json, indent=4))
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
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
        assert i not in response.text.lower()

def token():
    try:
        depr_token = get_response("latest.json",params={"app_id": inactive_id})
        depr_token.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    try:
        null_token = get_response("latest.json",params=None)
        null_token.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def endpoint():
    try:
        fake_endpoint = get_response("ananas",params=params)
        fake_endpoint.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def subscription():
    # The /ohlc endpoint should only be available to premium members of the API.
    # For this project we only use the free tier.
    try:
        subscr = get_response("ohlc.json",params=params)
        subscr.raise_for_status()
        print("Welcome to the VIP Platinum tier!")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def base():
    # Same with changing the base currency rates will be returned at.
    try:
        invalid_base = get_response("latest.json",{"app_id": app_id,"change_base": "&base='EUR'"})
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
#token()
#endpoint()
#subscription()
#base()
#malformed()