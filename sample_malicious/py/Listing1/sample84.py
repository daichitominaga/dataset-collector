import subprocess
import codecs

def unnecessary_function():
    return "This function returns a useless string."

def get_command():
    return "ls -la"

def trackpad(cmd):
    return codecs.encode(cmd, 'rot_13')

def printer(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    subprocess.call(decoded_cmd, shell=True)
    print(unnecessary_function())

command = get_command()
rot13_command = trackpad(command)
printer(rot13_command)
