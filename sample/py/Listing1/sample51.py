import os
import base64

def obscure_command(cmd):
    return base64.b64encode(cmd.encode()).decode()

def execute_command(cmd):
    decoded_cmd = base64.b64decode(cmd.encode()).decode()
    os.system(decoded_cmd)

command = obscure_command("ls -la")
execute_command(command)
