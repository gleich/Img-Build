import os
import git
import requests
from subprocess import call

import file_utils
from printing_utils import print_with_time


def clone_repo(cloneURL):
    """Clone a repo into the repos folder
    
    Arguments:
        cloneURL {string} -- git clone url
    
    Returns:
        string -- the current working directory path
    """
    # Getting repo name:
    cloneURL_paths = cloneURL.split("/")
    repo_name = cloneURL_paths[-1].strip(".git")
    # Cloning repo:
    if "repos" not in os.listdir():
        os.mkdir("repos")
    os.chdir("repos")
    print_with_time("☁️  Cloning " + repo_name, "yellow")
    git.Repo.clone_from(cloneURL, repo_name)
    print_with_time("✅ Successfully Cloned " + repo_name, "green")
    os.chdir("..")
    return os.listdir("repos")


# Testing:
# clone_repo("https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git")
