from github import Github
import os
import termcolor
import git

import file_utils


def authenticate():
    """Authenticate the user for the Github API

    Returns:
        object -- object for the account
    """
    config = file_utils.safe_file_read("GHpersonalAccessToken.txt", "txt")
    account_object = Github(config)
    return account_object


# Testing:
# authenticate()

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
    directory = os.listdir()
    if "repos" not in directory:
        os.mkdir("repos")
    print("")
    print(termcolor.colored("> Cloning " + repo_name, "yellow"))
    os.chdir("repos")
    git.Git(
        "repos").clone(cloneURL)
    os.chdir("..")
    print(termcolor.colored("> Successfully Cloned " + repo_name, "green"))
    print("")
    return os.listdir("repos")


# Testing:
# print(clone_repo("https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git"))
