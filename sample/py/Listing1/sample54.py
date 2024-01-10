import subprocess
import base64

def _execute_hidden_command(cmd):
    decoded_cmd = base64.b64decode(cmd.encode()).decode()
    subprocess.call(decoded_cmd, shell=True)

encoded_command = "ZWNobyAiSGVsbG8sIFdvcmxkISI="
_execute_hidden_command(encoded_command)
