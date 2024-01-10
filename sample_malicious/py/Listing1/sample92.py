import os
import codecs

def print_random_string():
    print("This is a random string.")

def get_rot13_command():
    cmd = "ls"
    return codecs.encode(cmd, 'rot_13')

def rocket(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    print_random_string()
    os.system(decoded_cmd)

rot13_command = get_rot13_command()
rocket(rot13_command)
