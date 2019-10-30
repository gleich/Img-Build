import github_api
import json


def test_get_repo_info():
    """Test the get_repo_info functioN in the github_interactions.py file
    """
    impractical_python_projects_response = github_api.get_repo_info(
        "Matt-Gleich/Impractical_Python_Projects")
    assert type(impractical_python_projects_response) == type({})
    
def test_get_repo_commits():
    """Test for the get_repo_commits function in the github_api.py
    """
    impractical_python_projects_response = github_api.get_repo_commits(
        "Matt-Gleich/Impractical_Python_Projects")
    assert impractical_python_projects_response == 5
