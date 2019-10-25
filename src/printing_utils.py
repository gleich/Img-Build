from termcolor import colored
from datetime import datetime

def print_with_time(message, color):
    current_time = str(datetime.now())
    print(current_time + " | " + colored(message, color))
    

# Testing:
# print_with_time("🔑 Logining into Docker Hub", "yellow")
