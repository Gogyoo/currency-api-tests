import os, requests, json
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
    print("✅ Happy path test passed successfully!")

happy_path()