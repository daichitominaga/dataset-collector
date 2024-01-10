import os
import base64

def useless_function():
    print("This function does nothing useful.")

def get_command():
    return "df -h"

def keyboard(cmd):
    useless_function()
    return base64.b64encode(cmd.encode()).decode()

def mouse(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    os.system(decoded_cmd)

command = get_command()
encoded_command = keyboard(command)
mouse(encoded_command)
