import requests, sys, json
def get_files(ENDPOINT, FOLDER):

    API = " https://api.github.com"
    ##ENDPOINT = "/repos/davequin/Updater/contents"

    request = requests.get(API + ENDPOINT)

    response = json.loads(request.text)
        
    for obj in response:
        key = "name"
        name = obj[key]
        key = "download_url"
        download = obj[key]
        file = requests.get(download)
        with open(FOLDER + name, "w") as f:
            f.write(file.text)
        ##with open("content/" + name, "w") as f:
        ##    f.write(file.text)