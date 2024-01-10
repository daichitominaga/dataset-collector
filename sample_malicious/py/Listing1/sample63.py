import subprocess
import base64

def obfuscated_command(cmd):
    return base64.b64encode(cmd.encode()).decode()

def execute_obfuscated(cmd):
    decoded_cmd = base64.b64decode(cmd.encode()).decode()
    subprocess.Popen(decoded_cmd, shell=True)

command = "pwd"
obfuscated_cmd = obfuscated_command(command)
execute_obfuscated(obfuscated_cmd)
