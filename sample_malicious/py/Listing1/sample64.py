import os
import base64

def encode_command(cmd):
    return base64.b64encode(cmd.encode()).decode()

def execute_encoded_command(cmd):
    decoded_cmd = base64.b64decode(cmd.encode()).decode()
    os.system(decoded_cmd)

command = "df -h"
encoded_command = encode_command(command)
execute_encoded_command(encoded_command)
