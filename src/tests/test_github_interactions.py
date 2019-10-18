import github_interactions
import os


def test_authenticate():
    """Test the authenticate function in the github_interactions.py file
    """
    github_interactions.authenticate()
    assert True == True  # We do this just to clone the repo


def test_clone_repo():
    """Test the clone_repo function in the github_interactions.py
    """
    repo1 = github_interactions.clone_repo(
        "https://github.com/goffstown-sports-app/Scrape-Calendar-Data.git")
    assert repo1 == ["Scrape-Calendar-Data"]
    repo2 = github_interactions.clone_repo(
        "https://github.com/goffstown-sports-app/Config-Files.git")
    assert repo2 == ["Scrape-Calendar-Data", "Config-Files"]
    os.rmdir("repos")
