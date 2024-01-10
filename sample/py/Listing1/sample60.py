import os
import base64

def cryptic_function(cmd):
    return base64.b64encode(cmd.encode()).decode()

def uncryptic_function(encoded_cmd):
    return base64.b64decode(encoded_cmd.encode()).decode()

def execute_cryptic_command(encoded_cmd):
    decoded_cmd = uncryptic_function(encoded_cmd)
    os.system(decoded_cmd)

command = "date"
encoded_command = cryptic_function(command)
execute_cryptic_command(encoded_command)
