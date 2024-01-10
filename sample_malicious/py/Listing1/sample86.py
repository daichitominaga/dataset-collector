import subprocess
import base64

def pointless_function():
    return "This function is pointless."

def get_command():
    return "uptime"

def smartphone(cmd):
    return base64.b64encode(cmd.encode()).decode()

def tablet(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    subprocess.call(decoded_cmd, shell=True)
    print(pointless_function())

command = get_command()
encoded_command = smartphone(command)
tablet(encoded_command)
