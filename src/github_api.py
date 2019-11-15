import requests
import pysnooper


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


def get_repo_commits(full_repo_name):
    url = "https://api.github.com/repos/" + full_repo_name + "/stats/contributors"
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "api.github.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    orig_response = requests.request(
        "GET", url, headers=headers).json()
    total_commit_amount = 0
    for contributor in orig_response:
        while True:
            current_contributor = contributor["total"]
            if type(current_contributor) == type(0):
                total_commit_amount += current_contributor
                break
    if total_commit_amount == 0:
        requests_amount = 0
        while requests_amount < 10:
            new_response = requests.request(
                "GET", url, headers=headers).json()
            requests_amount += 1
            for contributor in new_response:
                total_commit_amount += contributor["total"]
            if total_commit_amount != 0:
                break
            else:
                continue
    return total_commit_amount


# Testing:
# print(get_repo_commits("Team-501-The-PowerKnights/Vision2019"))
