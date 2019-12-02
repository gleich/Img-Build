from datetime import datetime
from termcolor import colored

def print_with_time(message, indents=0, color="white"):
    """Print something with time before it
    
    Arguments:
        message {string} -- message that will be printed to the console
        color {string} -- color of the text printed to the console
        indents {int} -- number of 3 tabs
    """
    current_time = str(datetime.now())
    tabs = []
    for i in range(indents):
        tabs.append("\t")
    if color == "white":
        print(current_time, "|", "".join(tabs) + message)
    else:
        print(current_time, "|", colored("".join(tabs) + message, color)) 
    

# Testing:
# print_with_time("🔑  Logining into Docker Hub", 0, "yellow")
# print_with_time("✅  Successfully logged into Docker Hub", 1, "green")
# print_with_time("🔑  Logining into Docker Hub", 2, "yellow")
