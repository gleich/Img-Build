from datetime import datetime

def print_with_time(message, color="white"):
    """Print something with time before it
    
    Arguments:
        message {string} -- message that will be printed to the console
        color {string} -- color of the text printed to the console
    """
    current_time = str(datetime.now())
    print(current_time, "|", message)
    

# Testing:
# print_with_time("🔑 Logining into Docker Hub", "yellow")
