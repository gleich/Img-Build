import github_interactions
import file_utils

def main():
    """Main function for the program
    """
    configuration_file = file_utils.safe_file_read("config.yml")
    