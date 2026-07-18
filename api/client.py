from dotenv import load_dotenv
import os
import requests


load_dotenv()
APP_ID = os.getenv("APP_ID")

baseURL = "https://openexchangerates.org/api/"

# First we want to test if our token works, and whether it was found by our main file
# by sending a simple request and check we get a code 200.
# The /convert endpoint is as good as any to start with.

response = requests.get(baseURL + "convert/1/EUR/USD?app_id=" + APP_ID)
data = response.json()
print("Status code:", response.status_code, data["message"], data["description"])

print("Content type:", response.headers.get())


print("Answer to query (1 Euro equals):", data["response", "USD"])