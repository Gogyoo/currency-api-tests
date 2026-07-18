from dotenv import load_dotenv
import os
import requests


load_dotenv()
APP_ID = os.getenv("APP_ID")

baseURL = "https://openexchangerates.org/api/"
params = {"app_id": APP_ID}

# First we want to test if our token works, and whether it was found by our main file
# by sending a simple request and check we get a code 200.
# The /latest.json endpoint is as good as any to start with.

response = requests.get(baseURL + "latest.json", params)

print("Status code:", response.status_code)
print("Base currency of query:", response.headers)