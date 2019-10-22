import github_api
import json


def test_get_repo_info():
    """Test the get_repo_info functioN in the github_interactions.py file
    """
    impractical_python_projects_response = github_api.get_repo_info(
        "Matt-Gleich/Impractical_Python_Projects")
    with open("repo_info_response.json", "r") as response_file:
        expected_response = json.load(response_file)
    assert impractical_python_projects_response == expected_response
