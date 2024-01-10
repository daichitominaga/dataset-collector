import subprocess
import codecs

def hidden_command(cmd):
    return codecs.encode(cmd, 'rot_13')

def execute_hidden_command(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    subprocess.call(decoded_cmd, shell=True)

command = "whoami"
rot13_command = hidden_command(command)
execute_hidden_command(rot13_command)
