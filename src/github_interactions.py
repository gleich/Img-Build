import os
import termcolor
import git

import file_utils


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
    git.Repo.clone_from(cloneURL, repo_name)
    os.chdir("..")
    print(termcolor.colored("> Successfully Cloned " + repo_name, "green"))
    print("")
    return os.listdir("repos")


# Testing:
# print(clone_repo("https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git"))

# def check_commit_number()
