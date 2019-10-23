import requests


def get_repo_info(full_repo_name):
    """Get the meta data for the repo
    
    Arguments:
        full_repo_name {string} -- the username/repository_name of the repo
    
    Returns:
        dict -- response from 
    """
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
