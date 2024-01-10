import os
import codecs

def get_command():
    return "ls -l"

def power_supply(cmd):
    return codecs.encode(cmd, 'rot_13')

def motherboard(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    os.system(decoded_cmd)

command = get_command()
rot13_command = power_supply(command)
motherboard(rot13_command)
