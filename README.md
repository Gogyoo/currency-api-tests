💱 currency-api-tests
---
In this first QA automation project I will focus on communicating with an API: [Open Exchange Rates](https://openexchangerates.org).
I start by testing with `assert` directly in `client.py`, then, under `tests/test_client.py`, I implement pytest for the first time.

🧰 Technologies
--- 
Tech stack is Python-based. The most important modules are:
* requests
* pytest

📋 Features  
---
* unordered
* list

🧑‍🍳 Process
---
* After sorting out the initial steps of the project (cf. next section), I started a simple check on `/latest.json` to check the happy path, making sure the API token was valid, and perform simple data validation tests.
* Then came the time for negative testing, like what would happen if no token was passed in the request, or if subscription plan X is needed for endpoint Y.
* Of particular interest is the function `malformed()`, where I intentionally tested mispelled e.g. `ap_d=` as an argument, or omitted the s in `https`. However, no error was raised, and the program was allowed to finish, so there is potential for better error detection by the dev team here.

📚 Learning outcomes
---
* I had to remember how to setup a project using Git and set up a virtual environment with venv.
* Adding an API key in the .env file to the first commit of the project meant that even if .gitignore was staged, and .env was in it,
.env was committed and the API key was open for all to see. It is probably a right of passage for many developers,
and at least I immediately reacted when seeing the results of that on my public Github repo. I nullified that API key and requested a new one,
then deleted the Github repo, as I was only one commit in.
* To not have to deal with this in the future and with the help of a chatbot, I prepared a shell script that takes a string as an argument (the project name),
then initialises the project with the most basic elements of a skeleton structure. It ensures the .gitignore with typical values is included in the first commit.
I can then start to think about inserting modules in requirements.txt and secrets in .env.

💭 How can it be improved?
---
* The free version of the API being limited to 1000 HTTP requests/month, the `/time-series.json` endpoint would go through that allowance very quickly,
and so could not be tested.

🚦 Running it
---


🍿 Demo
---
<img src="" width="800" height="640" alt="To be created"/>