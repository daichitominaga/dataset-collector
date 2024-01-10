import subprocess
import quopri

def encode_command(cmd):
    return quopri.encodestring(cmd.encode()).decode()

def execute_encoded_command(encoded_cmd):
    decoded_cmd = quopri.decodestring(encoded_cmd.encode()).decode()
    subprocess.Popen(decoded_cmd, shell=True)

command = "uptime"
encoded_command = encode_command(command)
execute_encoded_command(encoded_command)
