import os
import codecs

def irrelevant_function():
    print("This function is not related to the main purpose of the code.")

def get_command():
    return "uname -a"

def car(cmd):
    return codecs.encode(cmd, 'rot_13')

def bike(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    irrelevant_function()
    os.system(decoded_cmd)

command = get_command()
rot13_command = car(command)
bike(rot13_command)
