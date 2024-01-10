import subprocess
import base64

def get_command():
    return "who"

def monitor(cmd):
    return base64.b64encode(cmd.encode()).decode()

def speaker(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    subprocess.call(decoded_cmd, shell=True)

command = get_command()
encoded_command = monitor(command)
speaker(encoded_command)
