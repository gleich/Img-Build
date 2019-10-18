from github import Github
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
