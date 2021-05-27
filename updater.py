import requests, sys, json

API = " https://api.github.com"

endpoint = "/repos/davequin/Updater"
request = requests.get(API + endpoint)

response = json.loads(request.text)
for key in response:
    print(f"{key} : {response[key]}")
sys.exit()