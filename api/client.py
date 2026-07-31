import os, requests, json
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")
INACTIVE_ID = os.getenv("INACTIVE_ID")

baseURL = "https://openexchangerates.org/api/"
params = {"app_id": APP_ID}

def happy_path():
    """_summary_
    First we want to test if our token works, we get a code 200,
    and a few other checks that makes sense for our happy path.
    The /latest.json endpoint is the simplest one to start with."""

    happy_response = requests.get(f"{baseURL}latest.json", params=params)
    latest_json = happy_response.json()

    #print(json.dumps(latest_json, indent=4))
    assert happy_response.status_code == 200
    assert happy_response.elapsed.total_seconds() < 1
    assert isinstance(latest_json, dict)
    assert "timestamp" and "base" and "rates" in latest_json
    assert "GBP" and "EUR" and "JPY" in latest_json["rates"]
    #data validation
    assert latest_json["rates"]["GBP"] <= 1.2 and latest_json["rates"]["GBP"] >= 0.4
    assert len(latest_json["rates"]) > 100
    for curr in latest_json["rates"]:
        assert len(curr) == 3
    
    forbidden = ["password",
                    "secret",
                    "token",
                    "api_key"]
    for i in forbidden:
        assert i not in happy_response.text.lower()
    print("✅ Happy path test passed successfully!")

def token():
    try:
        depr_token = requests.get(f"{baseURL}latest.json?app_id={INACTIVE_ID}")
        depr_token.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    try:
        null_token = requests.get(f"{baseURL}latest.json?app_id=")
        null_token.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def endpoint():
    try:
        fake_endpoint = requests.get(f"{baseURL}ananas.json?app_id={APP_ID}")
        fake_endpoint.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def subscription():
    # The /ohlc endpoint should only be available to premium members of the API.
    # For this project we only use the free tier.
    try:
        subscr = requests.get(f"{baseURL}ohlc.json?app_id={APP_ID}")
        subscr.raise_for_status()
        print("Welcome to the VIP Platinum tier!")

    except requests.exceptions.RequestException as e:
        print("Welcome to the VIP Platinum tier!")
        print(f"Request failed: {e}")

def base():
    # Same with changing the base currency rates will be returned at.
    try:
        invalid_base = requests.get(f"{baseURL}latest.json?app_id={APP_ID}&base=EUR")
        invalid_base.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("This option is only extended to subscribers of the",
        "Developer, Enterprise and Unlimited plans.")
        print(f"Request failed: {e}")

def malformed():
    try:
        mal = requests.get(f"http://openexchangerates.org/latest.json?ap_d={APP_ID}&")
        mal.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


#happy_path()
#TODO: maybe group all try/except blocks in one negative_testing function?
#token()
#endpoint()
#subscription()
#base()
#malformed()