from github import Github
import yaml

def authenticate():
    opened_file = False
    try:
        with open("config.yml", "r") as config_file:
            data = yaml.safe_load(config_file)
        opened_file = True
    except FileNotFoundError():
        raise Warning("Please make sure that the config.yml file is in the src directory")
    token_warning = "There is no personalAccessToken in the config.yml file. It is needed to authenticated"
    try:
        if data[1]["personalAccessToken"] == "":
            raise Warning(token_warning)
    except KeyError():
        raise Warning(token_warning)
    account_object = Github(data[1]["personalAccessToken"])
    return account_object
        
    
# Testing:
# authenticate()
