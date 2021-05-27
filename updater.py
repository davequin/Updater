import requests, sys, json

API = " https://api.github.com"
ENDPOINT = "/repos/davequin/Updater"

request = requests.get(API + ENDPOINT)

response = json.loads(request.text)

for key in response:
    print(f"{key} : {response[key]}")





##for obj in response:
##    for key in obj:
##        print(f"{key} : {obj[key]}")


##for obj in response:
##    key = "name"
##    print(f"name : {obj[key]}")
##    name = obj[key]
##    key = "download_url"
##    print(f"download_url : {obj[key]}")
##    download = obj[key]
##    file = requests.get(download)
##    with open("content/" + name, "w") as f:
##        f.write(file.text)