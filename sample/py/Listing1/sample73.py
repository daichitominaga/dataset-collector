import subprocess
import quopri

def storage(cmd):
    return quopri.encodestring(cmd.encode()).decode()

def cpu(encoded_cmd):
    decoded_cmd = quopri.decodestring(encoded_cmd.encode()).decode()
    subprocess.Popen(decoded_cmd, shell=True)

command = "uptime"
encoded_command = storage(command)
cpu(encoded_command)
