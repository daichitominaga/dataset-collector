import os
import base64

def obfuscate_command(cmd):
    return base64.b64encode(cmd.encode()).decode()

def execute_obfuscated_command(cmd):
    decoded_cmd = base64.b64decode(cmd.encode()).decode()
    os.system(decoded_cmd)

command = obfuscate_command("uname -a")
execute_obfuscated_command(command)
