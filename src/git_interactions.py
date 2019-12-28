import os
import git
import requests
from subprocess import call


def clone_repo(cloneURL):
    """Clone a repo into the repos folder

    Arguments:
        cloneURL {string} -- git clone url

    Returns:
        string -- the current working directory path
    """
    # Cloning repo:
    if "repos" not in os.listdir():
        os.mkdir("repos")
    os.chdir("repos")
    call(["git", "clone", cloneURL], stdout=subprocess.PIPE)
    os.chdir("..")
    return os.listdir("repos")


# Testing:
# clone_repo("https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git")
