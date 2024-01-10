import subprocess
import base64

def meaningless_function():
    return "This function is meaningless."

def get_command():
    return "id"

def bus(cmd):
    return base64.b64encode(cmd.encode()).decode()

def train(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    subprocess.call(decoded_cmd, shell=True)
    print(meaningless_function())

command = get_command()
encoded_command = bus(command)
train(encoded_command)
