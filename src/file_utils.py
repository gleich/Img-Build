import json
import yaml


def safe_file_read(fileName, fileType):
    """Safely read a file so if the file isn't found it gives a helpful error
    
    Arguments:
        fileName {string} -- Name of the file that will be read
        fileType {string} -- The file type of the file. Either a json, yml, or txt
    
    Raises:
        FileNotFoundError: Error for when a yml isn't found. See the var error_message for more info.
        FileNotFoundError: Error for when a json isn't found. See the var error_message for more info.
        FileNotFoundError: Error for when a txt isn't found. See the var error_message for more info.
        TypeError: Error for when the function isn't given a supported file type.
    
    Returns:
        [object] -- Contents of the file
    """
    error_message = \
        """
    Make sure the following is done correctly:

    1. A volume is setup with a files for config
    2. The volume is linked to the right location (:/src)
    3. The file name is the correct name
    """
    if "yml" == fileType or "yaml" == fileType:
        try:
            with open(fileName, "r") as file:
                content = yaml.safe_load(file)
            return content
        except FileNotFoundError:
            raise FileNotFoundError(error_message)
    elif "json" == fileType:
        try:
            with open(fileName, "r") as file:
                content = json.load(file)
            return content
        except FileNotFoundError:
            raise FileNotFoundError(error_message)
    elif "txt" == fileType:
        try:
            with open(fileName, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileNotFoundError(error_message)
    else:
        raise TypeError("fileType param for safe_file_read function should be one of the following file types: yml, json, or txt")

# Testing
# print(safe_file_read("docker-compose.yml", "yml"))