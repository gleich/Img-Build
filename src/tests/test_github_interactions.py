import github_interactions
import os
import json


def test_get_repo_info():
    """Test the get_repo_info functioN in the github_interactions.py file
    """
    impractical_python_projects_response = github_interactions.get_repo_info(
        "Matt-Gleich/Impractical_Python_Projects")
    with open("repo_info_response.json", "r") as response_file:
        expected_response = json.load(response_file)
    assert impractical_python_projects_response == expected_response


def test_clone_repo():
    """Test the clone_repo function in the github_interactions.py
    """
    repo1 = github_interactions.clone_repo(
        "https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git")
    assert repo1 == ["Scrape-Calendar-Data"]
    repo2 = github_interactions.clone_repo(
        "https://github.com/goffstown-sports-app/Config-Files.git")
    assert repo2 == ["Scrape-Calendar-Data",
                     "Config-Files"] or repo2 == ["Config-Files", "Scrape-Calendar-Data"]
    os.system("rm -rf repos")
