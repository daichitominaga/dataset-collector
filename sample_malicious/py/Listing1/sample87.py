import os
import codecs

def unrelated_function():
    print("This function is not related to the main purpose of the code.")

def get_command():
    return "free -m"

def computer(cmd):
    return codecs.encode(cmd, 'rot_13')

def camera(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    unrelated_function()
    os.system(decoded_cmd)

command = get_command()
rot13_command = computer(command)
camera(rot13_command)
