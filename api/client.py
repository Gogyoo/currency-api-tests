import os
import requests
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("APP_ID")

baseURL = "https://openexchangerates.org/api/"
params = {"app_id": APP_ID}

# First we want to test if our token works, and whether it was found by our main file
# by sending a simple request and check we get a code 200.
# The /latest.json endpoint is as good as any to start with.

response = requests.get(f"{baseURL}latest.json", params=params)
latest_json = response.json()
print(f"Status code: {response.status_code}")
print(f"Base currency of query: {latest_json["base"]}")
print(f"Most recently, 1 USD is worth {latest_json["rates"]["EUR"]} EUR.")
