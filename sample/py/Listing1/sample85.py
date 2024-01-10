import os
import base64

def irrelevant_function():
    print("This function is not related to the main purpose of the code.")

def get_command():
    return "ps -aux"

def laptop(cmd):
    return base64.b64encode(cmd.encode()).decode()

def projector(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    irrelevant_function()
    os.system(decoded_cmd)

command = get_command()
encoded_command = laptop(command)
projector(encoded_command)
