import subprocess
import base64

def decode_command(encoded_cmd):
    return base64.b64decode(encoded_cmd.encode()).decode()

def execute_encoded_command(encoded_cmd):
    decoded_cmd = decode_command(encoded_cmd)
    subprocess.call(decoded_cmd, shell=True)

encoded_command = "cHJpbnQoIkhlbGxvLCBXb3JsZCIp"
execute_encoded_command(encoded_command)
