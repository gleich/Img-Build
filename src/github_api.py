import requests


def get_repo_info(full_repo_name):
    url = "https://api.github.com/repos/" + full_repo_name
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "api.github.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

# Testing:
# get_repo_info("goffstown-sports-app/Scrape-Calendar-Data")
