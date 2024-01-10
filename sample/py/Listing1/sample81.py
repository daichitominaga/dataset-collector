import os
import base64

def get_encoded_command():
    command = "uname -r"
    return base64.b64encode(command.encode()).decode()

def hard_disk(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    os.system(decoded_cmd)

encoded_command = get_encoded_command()
hard_disk(encoded_command)
